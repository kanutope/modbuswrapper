from modbuswrapper.ubbink_functions import FUNCTIONS as FNC_ubbink
from modbuswrapper.thermia_functions import FUNCTIONS as FNC_thermia
from modbuswrapper.alfen_functions import FUNCTIONS as FNC_alfen
from modbuswrapper.wrapper import modbus_client, modbus_interface
from modbuswrapper.configuration import NODES
import modbuswrapper.example.implement as implement

from time import sleep
from sys import argv
from getopt import gnu_getopt
from logging import basicConfig, DEBUG, INFO, ERROR


def init_clients():
    clnts = {}
    for el in NODES:
        DEV = NODES[el]['serial'] if 'serial' in NODES[el] else NODES[el]['tcp'] if 'tcp' in NODES[el] else None
        clnts[el] = modbus_client(DEV)

    return clnts


def init_interfaces(clnts, bytorder, wordorder):
    interfaces = {}
    for dev in NODES:
        if dev == 'vigor':
            fnc = FNC_ubbink
        elif dev == 'calibra':
            fnc = FNC_thermia
        elif dev == 'alfen':
            fnc = FNC_alfen
        else:
            raise UserWarning(f"%%% Unsupported device type '{dev}' in configuration file")

        interfaces[dev] = modbus_interface(clnts[dev], NODES[dev]['slave'], functions=fnc,
                                           delay=NODES[dev]['delay'] if 'delay' in NODES[dev] else 0,
                                           byteorder=bytorder,
                                           wordorder=wordorder)
    return interfaces


"""
modbuswrapper/alfen_functions.py:    'conf-modbus-maxcurrent': {
modbuswrapper/alfen_functions.py:        'len': 2, 'rd': 3, 'wr': 16, 'scale': 1,
modbuswrapper/alfen_functions.py:        'validate': 'between(5, 13)', 'datatype': 'flt32', 'unit': 'A'},
modbuswrapper/alfen_functions.py:    'conf-charge-using-1-or-3-phases': {
modbuswrapper/alfen_functions.py:        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
modbuswrapper/alfen_functions.py:        'validate': 'in_list(1, 3)', 'datatype': 'uint16', 'unit': 'phases'},
modbuswrapper/alfen_functions.py:    'conf-modbus-max-current-valid-time': {
modbuswrapper/alfen_functions.py:        'validate': '', 'datatype': 'uint32', 'unit': 's'},
modbuswrapper/thermia_functions.py:    'compressor-operating-hours': {
modbuswrapper/thermia_functions.py:        'validate': '', 'datatype': 'int32', 'unit': 'hrs'},
modbuswrapper/thermia_functions.py:    'tap-water-operating-hours': {
modbuswrapper/thermia_functions.py:        'validate': '', 'datatype': 'int32', 'unit': 'hrs'},
modbuswrapper/thermia_functions.py:    'maximum-allowed-gear-in-heating': {
modbuswrapper/thermia_functions.py:        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
modbuswrapper/thermia_functions.py:        'validate': '', 'datatype': 'int16', 'unit': ''},
modbuswrapper/ubbink_functions.py:    'total-flow-in-m3/h': {
modbuswrapper/ubbink_functions.py:        'validate': '', 'datatype': 'uint32', 'unit': 'm3/h'},
modbuswrapper/ubbink_functions.py:    'operating-time': {
modbuswrapper/ubbink_functions.py:        'validate': '', 'datatype': 'uint32', 'unit': 'hrs'},
"""

functions = {
    'alfen': {
        'conf-modbus-maxcurrent': {},
        'conf-charge-using-1-or-3-phases': {},
        'conf-modbus-max-current-valid-time': {},
    },
    'calibra': {
        'compressor-operating-hours': {},
        'tap-water-operating-hours': {},
        'maximum-allowed-gear-in-heating': {},
    },
    'vigor': {
        'total-flow-in-m3/h': {},
        'operating-time': {},
    }
}


basicConfig(level=INFO)

order = {
    1: {'byteorder': '>', 'wordorder': '>'},
    2: {'byteorder': '<', 'wordorder': '>'},
    3: {'byteorder': '>', 'wordorder': '<'},
    4: {'byteorder': '<', 'wordorder': '<'},
}

if __name__ == '__main__':
    optList, args = gnu_getopt(argv, '1234w', ['order1', 'order2', 'order3', 'order4', 'write'])
    clients = init_clients()

    i = 0
    wr = False
    ifaces = None
    for opt, arg in optList:
        print(f"opt: {opt}")

        if opt in ('-1', '-order1'):
            i = 1
        elif opt in ('-2', '-order2'):
            i = 2
        elif opt in ('-3', '-order3'):
            i = 3
        elif opt in ('-4', '-order4'):
            i = 4
        elif opt in ('-w', '-write'):
            wr = True

    if i == 0:
        raise UserWarning(f"%%% Unsupported configuration {i}")

    ifaces = init_interfaces(clients, order[i]['byteorder'], order[i]['wordorder'])
    print(order[i])

    for appl in functions:
        for func in functions[appl]:
            print(f"appliance [{appl}] -> function [{func}]")
            implement.read_parameter(ifaces[appl], func)
