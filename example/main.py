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


basicConfig(level=INFO)

selector = {
    'calibra': {
        1: ['enable-brine-out-monitoring',
            'enable-brine-pump-continuous-operation',
            'enable-variable-speed-mode-for-brine-pump',
            'enable-brine-in-monitoring',
            'brine-temp-out-of-range-alarm',
            'brine-in-sensor-alarm',
            'brine-out-sensor-alarm',
            'brine-delta-out-of-range-alarm',
            'brine-in-high-temp-alarm',
            'brine-in-low-temp-alarm',
            'brine-out-low-temp-alarm',
            'external-start-brine-pump',
            'brine-pump-on/off-control',
            'brine-in-temp',
            'brine-out-temp',
            'brine-circulation-pump-speed',
            'brine-in-high-alarm-limit',
            'brine-in-low-alarm-limit',
            'brine-out-low-alarm-limit',
            'brine-max-delta-limit',
            'brine-pump-lowest-allowed-speed',
            'brine-pump-highest-allowed-speed',
            'brine-pump-standby-speed',
            ],
        2: ['enable-tap-water',
            'start-temp-tap-water',
            'stop-temp-tap-water',
            ],
        3: ['enable-passive-cooling',
            'mix-valve-1-producing-passive-cooling',
            'set-point-supply-line-temp-cooling-mix-valve-1',
            ],
    },
    'vigor': {
        1: ['pwm-supply-preset-0',
            'pwm-supply-preset-1',
            'pwm-supply-preset-2',
            'pwm-supply-preset-3',
            'pwm-exhaust-preset-0',
            'pwm-exhaust-preset-1',
            'pwm-exhaust-preset-2',
            'pwm-exhaust-preset-3',
            ],
        2: ['modbus-control',
            'switch-position',
            'flow-rate-setting',
            'standby-mode',
            'filter-warning',
            'appliance-reset',
            ],
        3: ['flow-preset-0',
            'flow-preset-1',
            'flow-preset-2',
            'flow-preset-3',
            ]
    },
    'alfen': {
        1: ['info-name',
            'info-manufacturer',
            'info-firmware-version',
            'info-platform-type',
            'info-station-serial-number',
            ],
        2: ['msmt-voltage-phase-v(L1-N)',
            'msmt-voltage-phase-v(L2-N)',
            'msmt-voltage-phase-v(L3-N)',
            ],
        3: [
            'conf-availability',
            'conf-mode-3-state',
            'conf-actual-applied-max-current',
            'conf-modbus-max-current-valid-time',
            'conf-modbus-maxcurrent',
            'conf-active-load-balancing-safe-current',
            'conf-modbus-setpoint-accounted-for',
            'conf-charge-using-1-or-3-phases',
        ]
    },
}

clients = {}
for el in NODES:
    DEV = NODES[el]['serial'] if 'serial' in NODES[el] else NODES[el]['tcp'] if 'tcp' in NODES[el] else None
    clients[el] = modbus_client(DEV)

ifaces = {}
for dev in NODES:
    if dev == 'vigor':
        fnc = FNC_ubbink
    elif dev == 'calibra':
        fnc = FNC_thermia
    elif dev == 'alfen':
        fnc = FNC_alfen
    else:
        raise UserWarning(f"%%% Unsupported device type '{dev}' in configuration file")

    ifaces[dev] = modbus_interface(clients[dev], NODES[dev]['slave'], functions=fnc,
                                   delay=NODES[dev]['delay'] if 'delay' in NODES[dev] else 0,
                                   byteorder=NODES[dev]['byteorder'] if 'byteorder' in NODES[dev] else '>',
                                   wordorder=NODES[dev]['wordorder'] if 'wordorder' in NODES[dev] else '>')


def read_all(xfc=None, cnt=10):
    if xfc is None:
        for fName in ifaces:
            print("*******")
            print(f"{fName}")
            print("*******")
            implement.read_all(ifaces[fName], cnt)
    else:
        print("*******")
        implement.read_all(xfc, cnt)


def set_mode(iface, mode):
    mc = 1
    implement.modbus_control(iface, mc)
    while implement.modbus_control(iface) != mc:
        print(f"... waiting for modbus_control to become {mc}")
        sleep(1)

    implement.switch_position(iface, mode)
    while implement.switch_position(iface) != mode:
        print(f"... waiting for  switch_position to become {mode}")
        sleep(1)

    print("Done")


def set_flow_rate(iface, rate):
    mc = 2
    implement.modbus_control(iface, mc)
    while implement.modbus_control(iface) != mc:
        print(f"... waiting for modbus_control to become {mc}")
        sleep(1)

    print(f"... setting flowrate to {rate}")
    implement.flow_rate_setting(iface, rate)
    while implement.flow_rate_setting(iface) != rate:
        print(f"... waiting for flow_rate_setting to become {rate} ...")
        sleep(1)

    print("Done")


""" Vigor """
# iface = ifaces['vigor']
# implement.testUbbink()

# implement.test_interface(iface, selector['vigor'][idx])
# read_all(iface, 999)
# implement.flow_rate_setting(iface, 180)
# implement.flow_rate_setting(iface)


# set_mode(1)
# set_flow_rate(120)
"""
for i in range(4):
    mod = 3 - i
"""

# implement.switch_position(iface, 2)

""" Calibra """
# iface = ifaces['calibra']
# implement.toggle_tap_water(iface, 1)
# implement.comfort_wheel(iface, 21)
# implement.comfort_wheel(iface)
# implement.heat_curve(iface)
# read_all(iface, 999)

# implement.test_interface(iface, selector['calibra'][idx])

""" Alfen """

# implement.read_all(iface, 1)


def set_cooling(iface, temp):
    """
            'enable-passive-cooling',
            'mix-valve-1-producing-passive-cooling',
            'set-point-supply-line-temp-cooling-mix-valve-1',
    """
    fName = 'enable-passive-cooling'
    print(f"'{fName} -> {iface.call(fName, 'wr', 1)}")
    fName = 'set-point-supply-line-temp-cooling-mix-valve-1'
    print(f"'{fName} -> {iface.call(fName, 'wr', temp)}")


def unset_cooling(iface):
    """
            'enable-passive-cooling',
            'mix-valve-1-producing-passive-cooling',
            'set-point-supply-line-temp-cooling-mix-valve-1',
    """
    fName = 'enable-passive-cooling'
    print(f"'{fName} -> {iface.call(fName, 'wr', 0)}")
    fName = 'set-point-supply-line-temp-cooling-mix-valve-1'
    temp = 17
    print(f"'{fName} -> {iface.call(fName, 'wr', temp)}")


def exec_alfen(selection):
    dName = 'alfen'
    iface = ifaces[dName]
    for x in selection:
        print(f"{dName} selection: {x}")
        if x == '1' or x == '2' or x == '3':
            idx = int(x)
            for fName in selector[dName][idx]:
                implement.read_parameter(iface, fName)
        else:
            try:
                val = float(x)
                print(f"val={val}")

                implement.set_max_current(iface, val)
            except ValueError:
                raise UserWarning(f"%%% Cannot convert '{x}' into value")


def exec_calibra(selection):
    dName = 'calibra'
    iface = ifaces[dName]
    for x in selection:
        print(f"{dName} selection: {x} type is {type(x)}")
        if x == '1' or x == '2' or x == '3':
            idx = int(x)
            for fName in selector[dName][idx]:
                implement.read_parameter(iface, fName)
        elif x == 'a':
            read_all(iface, 999)
        elif x == 'c':
            set_cooling(iface, 23)
        elif x == 'u':
            unset_cooling(iface)
        else:
            print(f"{dName}: *not* covered selection {x}")


def exec_vigor(selection):
    dName = 'vigor'
    iface = ifaces[dName]
    for x in selection:
        print(f"{dName} selection: {x}")
        if x == '1' or x == '2' or x == '3':
            idx = int(x)
            for fName in selector[dName][idx]:
                implement.read_parameter(iface, fName)
        elif x == 'r':
            implement.flow_preset(iface)
        elif x == 'p':
            implement.flow_preset(iface, [140, 200, 260, 385])
        else:
            print(f"{dName}: *not* covered selection {x}")


optList, args = gnu_getopt(argv, 'a:c:v:', ['alfen=', 'calibra=', 'vigor='])

for a in args:
    print(f"args -> {a}")

for opt, arg in optList:
    sel = arg.split(',')
    if opt in ('-a', '--alfen'):
        exec_alfen(sel)
    elif opt in ('-c', '--calibra'):
        exec_calibra(sel)
    elif opt in ('-v', '--vigor'):
        exec_vigor(sel)
