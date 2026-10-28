""" modbuswrapper

    having one main components:
    - class `ModbusWrapper`, providing the 'brokering' features for the program accessing modbus connected appliances
    - class `ModbusInterface` which incorporates the previously created ModbusXXXClient.
      The actual modbus read or write calls are made through its member method 'ModbusInterface.call'
    - function `modbus_client(node)` which returns either a `ModbusSerialClient` or `ModbusTCPClient` object.
"""
import os
import stat
from logging import getLogger
from socket import AF_INET, SOCK_STREAM, socket
from time import sleep

from pymodbus.client import ModbusSerialClient, ModbusTcpClient
from pymodbus.client.base import ModbusBaseClient
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse

from modbuswrapper.constraintfactory import ConstraintFactory
from modbuswrapper.functions_alfen import FUNCTIONS as FNC_alfen
from modbuswrapper.functions_sma import FUNCTIONS as FNC_sma
from modbuswrapper.functions_thermia import FUNCTIONS as FNC_thermia
from modbuswrapper.functions_ubbink import FUNCTIONS as FNC_ubbink
from modbuswrapper.payload_proxy import payloadBuilder, payloadDecoder
from modbuswrapper.pkg_proxy import RtuFramer, SocketFramer

_logger = getLogger(__name__)


# pymodbus defaults overwrite
# Defaults.Retries = 10
# Defaults.Timeout = 10
# Defaults.Reconnects = 10
# ReconnectDelay = 500

def device_exists(node) -> bool:
    """ check whether a (serial) device file exists
        to be used the check accessibility of a serial device, to which a serial modbus appliance is connected
    """
    try:
        st = os.stat(node)

        # 1. Must be a character device
        if not stat.S_ISCHR(st.st_mode):
            txt = f"%%% {node}: is not a character device"
            _logger.error(txt)
            return False

        # 2. Test if the CURRENT process effectively has R/W access
        if not os.access(node, os.R_OK | os.W_OK):
            txt = f"%%% {node}: Process lacks R/W permissions for"
            _logger.error(txt)
            return False

        # 3. Explicit check: verify file group permissions match active process GIDs
        group_rw = bool(st.st_mode & stat.S_IRGRP) and bool(st.st_mode & stat.S_IWGRP)
        if group_rw:
            process_gids = set([os.getegid()] + os.getgroups())
            if st.st_gid not in process_gids and os.geteuid() != 0:
                txt = f"%%% {node}: Process GIDs {process_gids} do not include device group {st.st_gid}"
                _logger.error(txt)
                return False

        return True

    except OSError as ex:
        txt = f"%%% Device {node} unavailable -> {ex.strerror}"
        _logger.error(txt)
        return False


def socket_exists(host, port) -> bool:
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
                tcp -> containing 'host', 'port', 'timeout', 'retries'
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
            # 20251121 - issues encountered with exclusive lock on ttyAMA0, therefore exclusive=False;
            # 20261025 - since pymodbus 3.7.0, tye parameter exclusive is no longer accepted,
            # hence removed. If the locking issue reoccurs, I'll (have to) mitigate.
            return ModbusSerialClient(
                port=dev,
                framer=RtuFramer,
                baudrate=baudrate if baudrate is not None else 19200,
                bytesize=bytesize if bytesize is not None else 8,
                parity=parity if parity is not None else "E",
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
        # 202610 - REMOVED `retry_on_empty=True` since incompatible with 3.7.0 onwards
        if socket_exists(host=host, port=port):
            return ModbusTcpClient(
                host=host,
                port=port,
                framer=SocketFramer,
                timeout=timeout if timeout is not None else 100,
                retries=retries if retries is not None else 3,
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


class ModbusInterface:
    """ core modbus interface class, handling the requests (calls) to the modbus client (slave)
    """
    def __init__(self, client: ModbusBaseClient, slave, functions, delay, byteorder, wordorder):
        """ Initializes the interface instance
            parameters:
                client - ModbusBaseClient
                slave - int  # Modbus slave ID for the device (slave)
                functions - dict # *all* available functions for the device
                delay - int (seconds) # some devices require a minimal delay between consecutive calls (e.g. Alfen)
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

    def print_order(self) -> str:
        """ print the byte- and wordorder configured for this interface
        """
        return f"byteorder: {self._byteorder} wordorder: {self._wordorder}"

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
                    self.value(int(float(value)))
                elif fnc['datatype'][0:3] == 'flt':
                    self.value(float(value))
                elif fnc['datatype'] == 'bits':
                    self.value(int(value))
                elif fnc['datatype'] == 'str':
                    self.value(bytes(value))
                else:
                    self.value(value)

                if fnc['_validator'] is not None and not fnc['_validator'](self.value()):
                    raise UserWarning(f"%%% Value [{self.value()}]({fnc['datatype']}) is out of range ({fnc['validate']})")

                # 2026-10-28 - so far, with the appliances and functions I could test, I only have to
                # use the (binary)payloadbuilder for the datatype 'flt**'
                if fnc['datatype'][0:3] == 'flt':
                    plb = payloadBuilder(byteorder=self._byteorder, wordorder=self._wordorder)
                    plb.add_payload(value=(self.value() * fnc['scale']), datatype=fnc['datatype'])
                    _par = plb.to_registers()
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
                decoder = payloadDecoder(rr.registers, byteorder=self._byteorder, wordorder=self._wordorder)
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

    def write_parameter(self, fName: str, val=None):
        if val is not None:
            return self.call(fName, 'wr', val)
        else:
            return False
            

    def read_parameter(self, fName: str):
        rr = self.call(fName, 'rd')
        return self.decode_response(fName, rr)

    def get_all_functions(self):
        """ returns the dictionary of 'functions' assigned to the ModbusInterface instance
        """
        return self._functions

    def get_function(self, fname):
        """ returns the dictionary object for a given (named) 'functions'
            parameters:
                fname - str # the name of the modbus request function to be retrieved
            returns None if the named 'function' is not defined
        """
        if fname in self._functions:
            return self._functions[fname]
        else:
            return None

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
                elif appl == "sma":
                    fncs = FNC_sma
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

    def get_interface(self, appl=None) -> ModbusInterface | None:
        """ return interface built for a given appliance
        """
        if appl not in self._ifaces:
            return None
        else:
            return self._ifaces[appl]

    def all_interfaces(self) -> dict[str, ModbusInterface, ]:
        """ return interfaces for all (defined) appliances
        """
        return self._ifaces
    