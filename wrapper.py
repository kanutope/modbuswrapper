"""modbuswrapper

    having two main components:
    - function `modbus_client(node)` which returns either a `ModbusSerialClient` or `ModbusTCPClient` object.
    - class `modbus_interface` which incorporates the previously created ModbusXXXClient.
      The actual modbus read or write calls are made through its member method 'modbus_interface.call'
"""
from pymodbus.client import ModbusSerialClient, ModbusTcpClient
from pymodbus.client.base import ModbusBaseClient
from pymodbus.framer.rtu_framer import ModbusRtuFramer
from pymodbus.framer.socket_framer import ModbusSocketFramer
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse

from io import open
from time import sleep
from logging import getLogger
from socket import socket, AF_INET, SOCK_STREAM


_logger = getLogger(__name__)


# pymodbus defaults overwrite
# Defaults.Retries = 10
# Defaults.Timeout = 10
# Defaults.Reconnects = 10
# ReconnectDelay = 500


class payloadBuilder(BinaryPayloadBuilder):
    """extends the BinaryPayloadBuilder class with a dictionary allowing to call the various add_xxx methods by 'label'
    """
    def __init__(self, byteorder='>', wordorder='>'):
        """creates the 'add' dictionary which renders the various add_methods callable by 'label'
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
    """renders the various decode_xxx methods from a given BinaryPayloadDecoder object accessible by 'label'
    """
    def __init__(self, bpd: BinaryPayloadDecoder):
        """creates the decoder dictionary which renders the various decoded_XXX methods callable by 'label'
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


def file_exists(node):
    try:
        with open(file=node, mode="rb") as file:
            file.close()
    except OSError as ex:
        raise OSError(f"%%% Unable to open device {node} -> {ex.strerror}")

    return True


def socket_exists(host, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(3)

    try:
        s.connect((host, port))
    except OSError as ex:
        # OSError: [Errno 113] No route to host
        # ConnectionRefusedError: [Errno 111] Connection refused
        raise OSError(f"%%% Unable to connect {host}:{port} -> {ex.strerror}")

    s.close()
    return True


def modbus_client(node) -> ModbusBaseClient:
    """function firstly called in order to create the ModbusClient object, for further use
        parameters:
            node - dictionary describing the interfacing device
                either serial -> containing 'dev', 'baudrate', 'bytesize', 'parity'
                or tcp -> containing 'host', 'port', 'timeout', 'retries' 
    """
    def open_serial(dev, baudrate, bytesize, parity):
        """instantiates a ModbusSerialClient
            parameters:
                device - str # e.g. '/dev/ttyAMA0'
                baudrate - int
                bytesize - int
                parity - str # 'N', 'E', 'O'
        """
        if file_exists(dev):
            return ModbusSerialClient(port=dev,
                                      framer=ModbusRtuFramer,
                                      baudrate=baudrate if baudrate is not None else 19200,
                                      bytesize=bytesize if bytesize is not None else 8,
                                      parity=parity if parity is not None else "E",
                                      )
        else:
            return None

    def open_tcp(host, port, timeout, retries):
        """instantiates a ModbusTcpClient
            parameters:
                host - str # either IP address or host name
                port - int # port number
                timeout - int
                restries - int
        """
        if socket_exists(host=host, port=port):
            return ModbusTcpClient(host=host,
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
    # depending on the device type, either a ModbusSerialClient or a ModbusTcpClient is returned.
    if 'device' in node:
        return open_serial(dev=node['device'],
                           baudrate=node['baudrate'] if 'baudrate' in node else None,
                           bytesize=node['bytesize'] if 'bytesize' in node else None,
                           parity=node['parity'] if 'parity' in node else None,
                           )
    elif 'host' in node:
        return open_tcp(host=node['host'], port=node['port'],
                        timeout=node['timeout'] if 'timeout' in node else None,
                        retries=node['retries'] if 'retries' in node else None,
                        )
    else:
        raise UserWarning(f"%%% Unsupported device {node}, hence quitting")


def sync_call(client, function, addr, param, slave):
    """executing the actual modbus calls
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
        _logger.error(f"*** pymodbus exception: {exc}")
        raise exc
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


class modbus_interface:
    """core modbus wrapper class, handling the requests (calls) to the modbus client (slave)
    """
    def __init__(self, client: ModbusBaseClient, slave, functions, delay, byteorder, wordorder):
        """Initializes the interface instance
            parameters:
                client - ModbusBaseClient
                slave - int # Modbus slave ID for the device (slave)
                functions - dict # *all* available functions for the device
                delay - int (seconds) # some devices require a minimal delay between consecutive calls (e.g. Alfen)
                byteorder - str # byte endianess, either '<' or '>'
                wordorder - str # word endianess, either '<' or '>'
        """
        if client is None:
            raise UserWarning("%%% modbus_interface requires a client been created.")
        if functions is None:
            raise UserWarning("%%% modbus_interface requires a set of functions attached.")

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
        return f"byteorder: {self._byteorder}  wordorder: {self._wordorder}"

    def value(self, val=None):
        """set or return the value, only used/applicable for 'write' calls
            parameters:
                val - optionale # when set, the value is stored in the attribute self._value
            returns:
                the value set
        """
        if val is not None:
            self._value = val
        return self._value

    def between(self, a0, a1):
        """validates whether a writeable value is between the two boundaries given
            parameters:
                a0 - number # lower boundary
                a1 - number # upper boundary
            returns:
                true when self._value is within range, otherwise false
        """
        return (a0 <= self._value) and (self._value <= a1)

    def in_list(self, *vals):
        """validates wheter a writeable value is member of a given range
            parameters:
                *vals - tuple # valid, acceptable values
            returns
                true when self._value is in the given tuple, otherwise false
        """
        return self._value in vals

    @staticmethod
    def okay():
        """optional validation method, which always return true = Okay
        """
        return True

    def validate(self, method):
        """dynamic validation of the writeable value - executes the validation method and returns the outcome
            parameters:
                method - str # made of method name - 'between' or 'in_list' - including arguments between parentheses.
                e.g. in_list(1, 2, 3) or between(1, 100)
        """
        if len(method) > 0:
            chk = 'self.' + method  # self.method - hence *not* a static method
            return eval(chk)
        else:
            return True

    @staticmethod
    def null(var):
        return var

    def call(self, fname, action, value=None):
        """core modbus wrapper method, used to execute the actual modbus read or write request
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
                elif fnc['datatype'][0:3] == 'flt':
                    cast = float
                else:
                    cast = self.null

                self.value(cast(value))

                if not self.validate(fnc['validate']):
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

            _logger.debug(f"Function={fname} action={action} fnc={fnc[action]} address={fnc['address']}")
            rr = sync_call(self.client, self._selector[fnc[action]], fnc['address'], _par, slave)

            if action == 'rd':
                _logger.debug(f"Function {fname} -> {self.decode_response(fname, rr)}")

            return rr
        else:
            raise UserWarning(f"%%% Unsupported function {fname}")

    def decode_response(self, fname, rr):
        """decodes the response for a (successful) read request
            parameters:
                fname - str # the label given to the modbus request
                rr # variable returned from read requeset
        """
        _logger.debug(f"--- decode_response type(rr)={type(rr)}")
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
        """returns the dictionary of 'functions' assigned to the modbus_interface instance
        """
        return self._functions

    def function(self, name):
        """returns the dictionary object for a given (named) 'functions'
            parameters:
                name - str # the name of the modbus request function to be retrieved
            returns None if the named 'function' is not defined
        """
        if name in self._functions:
            return self._functions[name]
        else:
            return None
