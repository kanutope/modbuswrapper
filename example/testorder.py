from getopt import gnu_getopt
from logging import DEBUG, ERROR, INFO, basicConfig
from sys import argv

from modbus.configuration import NODES
from modbuswrapper.alfen_functions import FUNCTIONS as FNC_alfen
from modbuswrapper.thermia_functions import FUNCTIONS as FNC_thermia
from modbuswrapper.ubbink_functions import FUNCTIONS as FNC_ubbink
from modbuswrapper.wrapper import modbus_client, modbus_interface


def init_clients():
    clnts = {}
    for name, node in NODES.items():
        DEV = node['serial'] if 'serial' in node else node['tcp'] if 'tcp' in node else None
        clnts[name] = modbus_client(DEV)

    return clnts


def init_interfaces(clnts, bytorder, wordorder):
    interfaces = {}
    for name, node in NODES.items():
        if name == 'vigor':
            fnc = FNC_ubbink
        elif name == 'thermia':
            fnc = FNC_thermia
        elif name == 'alfen':
            fnc = FNC_alfen
        else:
            raise UserWarning(f"%%% Unsupported device type '{name}' in configuration file")

        interfaces[name] = modbus_interface(clnts[name], node['slave'], functions=fnc,
                                           delay=node.get('delay', 0),
                                           byteorder=bytorder,
                                           wordorder=wordorder)
    return interfaces


functions = {
    'alfen': {
        'conf-modbus-maxcurrent': {},
        'conf-charge-using-1-or-3-phases': {},
        'conf-modbus-max-current-valid-time': {},
    },
    'thermia': {
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
    optList, args = gnu_getopt(argv, '1234w:', ['order1', 'order2', 'order3', 'order4', 'write='])
    clients = init_clients()

    i = 0
    par = 0
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
            par = int(arg)

    if i == 0:
        raise UserWarning(f"%%% Unsupported configuration {i}")

    ifaces = init_interfaces(clients, order[i]['byteorder'], order[i]['wordorder'])
    print(order[i])

    if wr:
        # 'conf-modbus-maxcurrent': {}, maxcurr = 13.0
        v = 13 - par*0.25
        device = 'alfen'
        func = 'conf-modbus-maxcurrent'
        ret = ifaces[device].write_parameter(func, f"{v}")
        print(f"{func}({v}) -> {ret}")
        ifaces[device].read_parameter(func)

        # 'conf-charge-using-1-or-3-phases': {}, phases = 1
        v = 1 + (par % 2)*2
        device = 'alfen'
        func = 'conf-charge-using-1-or-3-phases'
        ret = ifaces[device].write_parameter(func, f"{v}")
        print(f"{func}({v}) -> {ret}")
        ifaces[device].read_parameter(func)

        # 'maximum-allowed-gear-in-heating': {}, maxgear = 9
        v = 9 - par
        device = 'thermia'
        func = 'maximum-allowed-gear-in-heating'
        ret = ifaces[device].write_parameter(func, f"{v}")
        print(f"{func}({v}) -> {ret}")
        ifaces[device].read_parameter(func)
    else:
        for name, fies in functions.items():
            for func in fies:
                print(f"appliance [{name}] -> function [{func}]")
                ifaces[name].read_parameter(func)
