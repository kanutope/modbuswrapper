
from modbuswrapper.wrapper import ModbusInterface


def heat_curve(iface: ModbusInterface):
    for i in range(7):
        fName = f"set-point-heat-currve-y-coordinate-{i+1}"
        print(f"heat_curve - {fName}: {iface.read_parameter(fName)}")


def comfort_wheel(iface: ModbusInterface, val=None):
    fName = 'comfort-wheel-setting'
    curr = iface.read_parameter(fName)
    print(f"{fName} current: {curr}")

    if val is not None:
        rr = iface.write_parameter(fName, val)
        print(f"{fName} - writing val {val} returns {rr}")
        par1 = iface.read_parameter(fName)
        print(f"{fName} reads: {par1}")


def toggle_tap_water(iface: ModbusInterface, flag=None):
    fName = 'enable-tap-water'
    curr = iface.read_parameter(fName)
    new = not curr

    if flag is not None:
        rr = iface.write_parameter(fName, new)
        print(f"{fName} writing returns {rr}")
    
    par = iface.read_parameter(fName)
    print(f"{fName} curr: {curr} new: {new} reads => {par}")


def test_interface(iface: ModbusInterface, lst):
    for fName in lst:
        curr = iface.read_parameter(fName)
        print(f"{fName} current: {curr}")


def read_all(iface: ModbusInterface, cnt):
    for fName, params in iface.functions().items():
        if cnt > 0:
            ret = iface.read_parameter(fName)
            print(f"{params['address']}\t{fName}\t{ret}\t{params['unit']}\t{params['datatype']}")
        cnt = cnt - 1


def modbus_control(iface: ModbusInterface, mode=None):
    fName = 'modbus-control'
    if mode is None:
        return iface.read_parameter(fName)
    else:
        return iface.write_parameter(fName, mode)


def flow_rate_setting(iface: ModbusInterface, spd=None):
    fName = 'flow-rate-setting'
    if spd is None:
        return iface.read_parameter(fName)
    else:
        return iface.write_parameter(fName, spd)


def switch_position(iface: ModbusInterface, swtch=None):
    fName = 'switch-position'
    if swtch is None:
        return iface.read_parameter(fName)
    else:
        return iface.write_parameter(fName, swtch)


def flow_preset(iface: ModbusInterface, spds=None):
    ret = []
    for i in range(4):
        fName = f"flow-preset-{i}"

        if spds is None:
            ret.append(iface.read_parameter(fName))
        else:
            ret.append(iface.write_parameter(fName, spds[i]))

    return ret


def set_max_current(iface: ModbusInterface, curr=None):
    fName = 'conf-modbus-maxcurrent'

    if curr == 0:
        return iface.read_parameter(fName)
    else:
        return iface.write_parameter(fName, curr)
