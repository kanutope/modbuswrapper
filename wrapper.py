""" modbuswrapper

    having one main components:
    - class `ModbusWrapper`, providing the 'brokering' features for the program accessing modbus connected appliances
    - class `ModbusInterface` which incorporates the previously created ModbusXXXClient.
      The actual modbus read or write calls are made through its member method 'ModbusInterface.call'
    - function `modbus_client(node)` which returns either a `ModbusSerialClient` or `ModbusTCPClient` object.
"""
import ast
import os
import stat
from collections.abc import Callable
from logging import getLogger
from socket import AF_INET, SOCK_STREAM, socket
from time import sleep
from typing import Any

from pymodbus.client import ModbusSerialClient, ModbusTcpClient
from pymodbus.client.base import ModbusBaseClient
from pymodbus.exceptions import ModbusException
from pymodbus.framer.rtu_framer import ModbusRtuFramer
from pymodbus.framer.socket_framer import ModbusSocketFramer
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.pdu import ExceptionResponse

from modbuswrapper.alfen_functions import FUNCTIONS as FNC_alfen
from modbuswrapper.thermia_functions import FUNCTIONS as FNC_thermia
from modbuswrapper.ubbink_functions import FUNCTIONS as FNC_ubbink

_logger = getLogger(__name__)


# pymodbus defaults overwrite
# Defaults.Retries = 10
# Defaults.Timeout = 10
# Defaults.Reconnects = 10
# ReconnectDelay = 500


class ConstraintFactory:
    """provides ConstraintFactory which allows to implement custom built validation checks on given constraints.
    Parses constraint strings once and compiles them into executable lambda functions.
    (built by Gemini (Google AI)"""

    def __init__(self) -> None:
        # Map constraint names to factory functions returning a lambda
        # PEP 585: Using built-in dict instead of typing.Dict
        # PEP 585: Using collections.abc.Callable instead of typing.Callable
        self._factories: dict[str, Callable[..., Callable[[Any], bool]]] = {
            "between": self._make_between,
            "in_list": self._make_in_list,
        }

    @staticmethod
    def _make_between(min_val: float, max_val: float) -> Callable[[Any], bool]:
        """Returns a lambda that evaluates min_val <= val <= max_val"""
        return lambda val: min_val <= val <= max_val

    @staticmethod
    def _make_in_list(*allowed_values: Any) -> Callable[[Any], bool]:
        """Returns a lambda that evaluates val in allowed_values"""
        # Converting allowed_values to a set gives O(1) lookup speed
        allowed_set = set(allowed_values)
        return lambda val: val in allowed_set

    def _parse_string(self, constraint_str: str) -> tuple[str, list[Any]]:
        """Safely extracts the function name and argument literals using AST."""
        try:
            tree = ast.parse(constraint_str, mode="eval")
            call_node = tree.body

            if not isinstance(call_node, ast.Call) or not isinstance(
                call_node.func, ast.Name
            ):
                raise TypeError(
                    "Expected a single function call e.g. 'between(a, b)'"
                )

            func_name = call_node.func.id
            args = [ast.literal_eval(arg) for arg in call_node.args]
            return func_name, args

        except Exception as err:
            raise ValueError(
                f"Malformed constraint string '{constraint_str}': {err}"
            ) from err

    def compile(self, constraint_str: str) -> Callable[[Any], bool]:
        """Compiles a constraint string into an executable lambda validator."""
        if not constraint_str or not constraint_str.strip():
            return lambda val: True  # No constraint -> always valid

        func_name, args = self._parse_string(constraint_str)

        if func_name not in self._factories:
            raise ValueError(f"Unsupported constraint rule: '{func_name}'")

        factory = self._factories[func_name]
        try:
            return factory(*args)
        except TypeError as err:
            raise ValueError(
                f"Argument count mismatch in constraint '{constraint_str}'"
            ) from err


class payloadBuilder(BinaryPayloadBuilder):
    """ extends the BinaryPayloadBuilder class with a dictionary allowing to call the various add_xxx methods by 'label'
    """
    def __init__(self, byteorder='>', wordorder='>'):
        """ creates the 'add' dictionary which renders the various add_methods callable by 'label'
            parameters:
                byteorder - string -  default  '>' (big endian)
                wordorder - string - default  '>' (big endian)
        """
        super().__init__(byteorder=byteorder, wordorder=wordorder)
        self.add = {
            'bits': super().add_bits,
            'flt16': super().add_16bit_float,
            'flt32': super().add_32bit_float,
            'flt64': super().add_64bit_float,
            'int16': super().add_16bit_int,
            'int32': super().add_32bit_int,
            'int64': super().add_64bit_int,
            'int8': super().add_8bit_int,
            'str': super().add_string,
            'uint16': super().add_16bit_uint,
            'uint32': super().add_32bit_uint,
            'uint64': super().add_64bit_uint,
            'uint8': super().add_8bit_uint,
        }


class payloadDecoder:
    """ renders the various decode_xxx methods from a given BinaryPayloadDecoder object accessible by 'label'
    """
    def __init__(self, bpd: BinaryPayloadDecoder):
        """ creates the decoder dictionary which renders the various decoded_XXX methods callable by 'label'
            parameters:
                bpd - BinaryPayloadDecoder instance
        """
        self.decoder = {
            'bits': bpd.decode_bits,
            'flt16': bpd.decode_16bit_float,
            'flt32': bpd.decode_32bit_float,
            'flt64': bpd.decode_64bit_float,
            'int16': bpd.decode_16bit_int,
            'int32': bpd.decode_32bit_int,
            'int64': bpd.decode_64bit_int,
            'int8': bpd.decode_8bit_int,
            'str': bpd.decode_string,
            'uint16': bpd.decode_16bit_uint,
            'uint32': bpd.decode_32bit_uint,
            'uint64': bpd.decode_64bit_uint,
            'uint8': bpd.decode_8bit_uint,
        }


def device_exists(node):
    """ check whether a (serial) device file exists
        to be used the check accessibility of a serial device, to which a serial modbus appliance is connected
    """
    try:
        st = os.stat(node)

        # 1. Must be a character device
        if not stat.S_ISCHR(st.st_mode):
            txt = f"%%% {node} is not a character device"
            _logger.error(txt)
            return False

        # 2. Test if the CURRENT process effectively has R/W access
        if not os.access(node, os.R_OK | os.W_OK):
            txt = f"%%% Process lacks R/W permissions for {node}"
            _logger.error(txt)
            return False

        # 3. Explicit check: verify file group permissions match active process GIDs
        group_rw = bool(st.st_mode & stat.S_IRGRP) and bool(st.st_mode & stat.S_IWGRP)
        if group_rw:
            process_gids = set([os.getegid()] + os.getgroups())
            if st.st_gid not in process_gids and os.geteuid() != 0:
                txt = f"%%% Process GIDs {process_gids} do not include device group {st.st_gid}"
                _logger.error(txt)
                return False

        return True

    except OSError as ex:
        txt = f"%%% Device {node} unavailable -> {ex.strerror}"
        _logger.error(txt)
        return False


def socket_exists(host, port):
    """check whether an Modbus/TCP appliance is accessible
    to be used the check accessibility of a Modbus/TCP appliance
    """
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(3)

    try:
        s.connect((host, port))
        s.close()
        return True

    except TimeoutError as ex:
        txt = f"%%% Connecting {host}:{port} timed out -> {ex.strerror}"
        _logger.error(txt)
        return False
    except OSError as ex:
        # OSError: [Errno 113] No route to host
        # ConnectionRefusedError: [Errno 111] Connection refused
        txt = f"%%% Unable to connect {host}:{port} -> {ex.strerror}"
        _logger.error(txt)
        return False


def modbus_client(ctype, node) -> ModbusSerialClient | ModbusTcpClient | None:
    """function firstly called in order to create the ModbusClient object, for further use
        parameters:
            ctype - type of client, either 'serial' or 'tcp'
            node - dictionary describing the interfacing device, depending on ctype
                serial -> containing 'device', 'baudrate', 'bytesize', 'parity'
                tcp    -> containing 'host', 'port', 'timeout', 'retries'
    """

    def open_serial(dev, baudrate, bytesize, parity) -> ModbusSerialClient | None:
        """instantiates a ModbusSerialClient
        parameters:
            device - str # e.g. '/dev/ttyAMA0'
            baudrate - int
            bytesize - int
            parity - str # 'N', 'E', 'O'
        """
        if device_exists(dev):
            # issues encountered with exclusive lock on ttyAMA0, therefore exclusive=False
            return ModbusSerialClient(
                port=dev,
                framer=ModbusRtuFramer,
                baudrate=baudrate if baudrate is not None else 19200,
                bytesize=bytesize if bytesize is not None else 8,
                parity=parity if parity is not None else "E",
                exclusive=False,
            )
        else:
            return None

    def open_tcp(host, port, timeout, retries) -> ModbusTcpClient | None:
        """instantiates a ModbusTcpClient
        parameters:
            host - str # either IP address or host name
            port - int # port number
            timeout - int
            restries - int
        """
        if socket_exists(host=host, port=port):
            return ModbusTcpClient(
                host=host,
                port=port,
                framer=ModbusSocketFramer,
                timeout=timeout if timeout is not None else 100,
                retries=retries if retries is not None else 3,
                retry_on_empty=True,
            )
        else:
            return None

    # the dictionary node can describe both a serial or a networked device (tcp).
    # the differentiator is a value either for the keyword 'device' -> serial or 'host' -> tcp
    # depending on the device ctype, either a ModbusSerialClient or a ModbusTcpClient is returned.
    if ctype == 'serial':
        return open_serial(dev=node['device'],
                           baudrate=node.get('baudrate', None),
                           bytesize=node.get('bytesize', None),
                           parity=node.get('parity', None),
                           )
    elif ctype == 'tcp':
        return open_tcp(host=node['host'], port=node['port'],
                        timeout=node.get('timeout', None),
                        retries=node.get('retries', None),
                        )
    else:
        return None


def sync_call(client, function, addr, param, slave):
    """ executing the actual modbus calls
        parameters:
            client - ModbusBaseClient # either a ModbusSerialClient or ModbusTcpClient instance
            function - ModbusBaseClient.function # the applicable member function of the ModbusBaseClient to call
            addr - int # start address to read from or write to, targeting the actual 'function' to request
            param # parameter (value) applicable for/when writing
            slave - int # Modbus slave ID
    """
    client.connect()
    assert client.connected

    try:
        rr = function(addr, param, slave)
    except ModbusException as exc:
        txt = f"*** pymodbus exception: {exc}"
        _logger.error(txt)
        raise ModbusException(txt)
    if rr.isError():
        txt = "*** pymodbus returned an error!"
        _logger.error(txt)
        raise ModbusException(txt)

    if isinstance(rr, ExceptionResponse):
        txt = f"*** exception from device {rr}!"
        _logger.error(txt)
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        raise ModbusException(txt)

    client.close()
    return rr


class ModbusWrapper:
    """ wrapper class, broker between the user program and the modbus interface
    """

    factory = ConstraintFactory()

    def __init__(self, nodes):
        """ initialise modbus wrapper with the given configuration

        Args:
            nodes (dict): configuration of the actual modbus (compatible) devices
        """
        # save configuration (nodes) for future use
        self._nodes = nodes

        # initialize client devices
        self._clients = {}
        for appl, node in self._nodes.items():
            if 'serial' in node:
                self._clients[appl] = modbus_client('serial', node['serial'])
            elif 'tcp' in node:
                self._clients[appl] = modbus_client('tcp', node['tcp'])
            else:
                txt = f"%%% Unsupported device {node} - revisit your configuration"
                _logger.warning(txt)
                self._clients[appl] = None

        # !!!
        ### as a result of the previous step,
        ### there is a possibility that a client is not successfully initialized
        ### a client can be misconfigured or it is invalid or not accessible
        ### in that case that client is set to None

        # initialize interfaces - in particular the functions that are available for each client (device)
        self._ifaces = {}
        for appl, client in self._clients.items():
            if client is None:
                self._ifaces[appl] = None
            else:
                if appl == "vigor":
                    fncs = FNC_ubbink
                elif appl == "thermia":
                    fncs = FNC_thermia
                elif appl == "alfen":
                    fncs = FNC_alfen
                else:
                    fncs = {}

                if fncs == {}:
                    txt = f"%%% Unsupported appliance type '{appl}' in configuration file"
                    _logger.warning(txt)
                else:
                    for fname, params in fncs.items():
                        if params.get('validate', False) and params['validate'] != '':
                            fncs[fname]['_validator'] = ModbusWrapper.factory.compile(params['validate'])
                        else:
                            fncs[fname]['_validator'] = None

                    self._ifaces[appl] = ModbusInterface(
                        client,
                        self._nodes[appl]["slave"],
                        functions=fncs,
                        delay=self._nodes[appl].get("delay", 0),
                        byteorder=self._nodes[appl].get("byteorder", ">"),
                        wordorder=self._nodes[appl].get("wordorder", ">"),
                    )

    def get_interface(self, appl=None):
        """ return interface built for a given appliance
        """
        if appl not in self._ifaces:
            return None
        else:
            return self._ifaces[appl]

    def all_interfaces(self):
        """ return interfaces for all (defined) appliances
        """
        return self._ifaces

class ModbusInterface:
    """ core modbus interface class, handling the requests (calls) to the modbus client (slave)
    """
    def __init__(self, client: ModbusBaseClient, slave, functions, delay, byteorder, wordorder):
        """ Initializes the interface instance
            parameters:
                client    - ModbusBaseClient
                slave     - int  # Modbus slave ID for the device (slave)
                functions - dict # *all* available functions for the device
                delay     - int (seconds) # some devices require a minimal delay between consecutive calls (e.g. Alfen)
                byteorder - str  # byte endianess, either '<' or '>'
                wordorder - str  # word endianess, either '<' or '>'
        """
        if client is None:
            raise UserWarning("%%% ModbusInterface requires a client been created.")
        if functions is None:
            raise UserWarning("%%% ModbusInterface requires a set of functions attached.")

        self.client = client
        self.slave = slave

        self._delay = delay
        self._byteorder = byteorder
        self._wordorder = wordorder

        self._value = None
        self._functions = functions
        self._selector = {
            1: client.read_coils,
            2: client.read_discrete_inputs,
            3: client.read_holding_registers,
            4: client.read_input_registers,
            5: client.write_coil,
            6: client.write_register,
            7: client.read_exception_status,
            15: client.write_coils,
            16: client.write_registers,
        }
        self._builder = payloadBuilder(byteorder=self._byteorder, wordorder=self._wordorder)

    def print_order(self):
        """ print the byte- and wordorder configured for this interface
        """
        return f"byteorder: {self._byteorder}  wordorder: {self._wordorder}"

    def value(self, val=None):
        """ set or return the value, only used/applicable for 'write' calls
            parameters:
                val - optionale # when set, the value is stored in the attribute self._value
            returns:
                the value set
        """
        if val is not None:
            self._value = val
        return self._value

    @staticmethod
    def okay():
        """ optional validation method, which always return true = Okay
        """
        return True

    @staticmethod
    def null(var):
        """ dummy casting which returns the given variable unchanged
            parameters:
                any (kind of) variable
        """
        return var

    def call(self, fname, action, value=None):
        """ core modbus wrapper method, used to execute the actual modbus read or write request
            parameters:
                fname - str # the label given to the modbus request
                action - str # 'rd' or 'wr'
                value # set in case of a write request
        """
        if fname in self._functions:
            fnc = self._functions[fname]
            # Modbus slave ID may be overriden for a particular request
            if 'slave' in fnc:
                slave = fnc['slave']
            else:
                slave = self.slave

            if action == 'rd':
                _par = fnc['len']
            elif action == 'wr':
                if fnc['datatype'][0:3] == 'int' or fnc['datatype'][0:4] == 'uint':
                    cast = int
                    self.value(int(float(value)))
                elif fnc['datatype'][0:3] == 'flt':
                    cast = float
                    self.value(float(value))
                else:
                    cast = self.null

                if fnc['_validator'] is not None and not fnc['_validator'](self.value()):
                    raise UserWarning(f"%%% Value {self.value()} is out of range {fnc['validate']}")

                if cast == float:
                    # encode the value
                    self._builder.reset()
                    self._builder.add[fnc['datatype']](self.value() * fnc['scale'])
                    _par = self._builder.to_registers()
                else:
                    _par = self.value() * fnc['scale']
            else:
                raise UserWarning(f"%%% Unsupported action {action}")

            if self._delay is not None:
                sleep(self._delay)

            txt = f"Function={fname} action={action} fnc={fnc[action]} address={fnc['address']}"
            _logger.debug(txt)

            rr = sync_call(self.client, self._selector[fnc[action]], fnc['address'], _par, slave)

            if action == 'rd':
                txt = f"Function {fname} -> {self.decode_response(fname, rr)}"
                _logger.debug(txt)

            return rr
        else:
            raise UserWarning(f"%%% Unsupported function {fname}")

    def decode_response(self, fname, rr):
        """ decodes the response for a (successful) read request
            parameters:
                fname - str # the label given to the modbus request
                rr # variable returned from read requeset
        """
        txt = f"--- decode_response type(rr)={type(rr)}"
        _logger.debug(txt)

        if fname in self._functions:
            fnc = self._functions[fname]
            if fnc['datatype'] == 'bits':
                return rr.bits[0]
            else:
                decoder = payloadDecoder(BinaryPayloadDecoder.fromRegisters(registers=rr.registers,
                                                                            byteorder=self._byteorder,
                                                                            wordorder=self._wordorder))
                dtype = fnc['datatype']
                if dtype in decoder.decoder:
                    if dtype == 'str':
                        ret = decoder.decoder[dtype](fnc['len'])
                    else:
                        ret = decoder.decoder[dtype]()

                    return ret / fnc['scale'] if fnc['scale'] != 1 else ret
                else:
                    return rr.registers
        else:
            return None

    def functions(self):
        """ returns the dictionary of 'functions' assigned to the ModbusInterface instance
        """
        return self._functions

    def function(self, fname):
        """ returns the dictionary object for a given (named) 'functions'
            parameters:
                fname - str # the name of the modbus request function to be retrieved
            returns None if the named 'function' is not defined
        """
        if fname in self._functions:
            return self._functions[fname]
        else:
            return None
