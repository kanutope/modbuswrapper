from time import sleep

from modbuswrapper.wrapper import ModbusInterface


def read_parameter(iface: ModbusInterface, fName: str):
    rr = iface.call(fName, 'rd')
    cur = iface.decode_response(fName, rr)
    print(f"Parameter {fName}: {cur}")
    return cur


def heat_curve(iface: ModbusInterface):
    for i in range(7):
        fName = f"set-point-heat-curve-y-coordinate-{i+1}"
        read_parameter(iface, fName)


def comfort_wheel(iface: ModbusInterface, val=None):
    fName = 'comfort-wheel-setting'
    cur = read_parameter(iface, fName)

    if val is not None:
        print(f"{fName} current: {cur} => val: {val}")

        rr = iface.call(fName, 'wr', val)
        print(f"writing returns {rr}")
        read_parameter(iface, fName)


def toggle_tap_water(iface: ModbusInterface, flag=None):
    fName = 'enable-tap-water'
    cur = read_parameter(iface, fName)

    new = 1 - cur
    if flag is not None:
        rr = iface.call(fName, 'wr', new)
        print(f"writing returns {rr}")
        read_parameter(iface, fName)


def test_interface(iface: ModbusInterface, lst):
    for fName in lst:
        read_parameter(iface, fName)


def read_all(iface: ModbusInterface, cnt=999):
    for fName in iface.functions():
        if cnt > 0:
            read_parameter(iface, fName)
        cnt = cnt - 1


def modbus_control(iface: ModbusInterface, mode=None):
    fName = 'modbus-control'
    if mode is None:
        return read_parameter(iface, fName)
    else:
        return iface.call(fName, 'wr', mode)


def flow_rate_setting(iface: ModbusInterface, spd=None):
    fName = 'flow-rate-setting'
    if spd is None:
        return read_parameter(iface, fName)
    else:
        return iface.call(fName, 'wr', spd)


def switch_position(iface: ModbusInterface, swtch=None):
    fname = 'switch-position'
    if swtch is None:
        return read_parameter(iface, fname)
    else:
        return iface.call(fname, 'wr', swtch)


def flow_preset(iface: ModbusInterface, spds=None):
    ret = []
    for i in range(4):
        fName = f"flow-preset-{i}"

        if spds is None:
            ret.append(read_parameter(iface, fName))
        else:
            ret.append(iface.call(fName, 'wr', spds[i]))

    return ret


def set_max_current(iface: ModbusInterface, curr=None):
    fName = 'conf-modbus-maxcurrent'

    if curr == 0:
        return read_parameter(iface, fName)
    else:
        return iface.call(fName, 'wr', curr)
