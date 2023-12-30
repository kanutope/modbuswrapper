from time import sleep

from modbuswrapper.wrapper import modbus_interface


def read_parameter(iface: modbus_interface, fName: str):
    rr = iface.call(fName, 'rd')
    cur = iface.decode_response(fName, rr)
    print(f"Parameter {fName}: {cur}")
    return cur


def heat_curve(iface: modbus_interface):
    for i in range(7):
        fName = f"set-point-heat-curve-y-coordinate-{i+1}"
        read_parameter(iface, fName)


def comfort_wheel(iface: modbus_interface, val=None):
    fName = 'comfort-wheel-setting'
    cur = read_parameter(iface, fName)

    if val is not None:
        print(f"{fName} current: {cur} => val: {val}")

        rr = iface.call(fName, 'wr', val)
        print(f"writing returns {rr}")
        read_parameter(iface, fName)


def toggle_tap_water(iface: modbus_interface, flag=None):
    fName = 'enable-tap-water'
    cur = read_parameter(iface, fName)

    new = 1 - cur
    if flag is not None:
        rr = iface.call(fName, 'wr', new)
        print(f"writing returns {rr}")
        read_parameter(iface, fName)


def test_interface(iface: modbus_interface, lst):
    for fName in lst:
        read_parameter(iface, fName)


def read_all(iface: modbus_interface, cnt=999):
    for fName in iface.functions():
        if cnt > 0:
            read_parameter(iface, fName)
        cnt = cnt - 1


def modbus_control(iface: modbus_interface, mode=None):
    fName = 'modbus-control'
    if mode is None:
        return read_parameter(iface, fName)
    else:
        return iface.call(fName, 'wr', mode)


def flow_rate_setting(iface: modbus_interface, spd=None):
    fName = 'flow-rate-setting'
    if spd is None:
        return read_parameter(iface, fName)
    else:
        return iface.call(fName, 'wr', spd)


def switch_position(iface: modbus_interface, swtch=None):
    fname = 'switch-position'
    if swtch is None:
        return read_parameter(iface, fname)
    else:
        return iface.call(fname, 'wr', swtch)


def flow_preset(iface: modbus_interface, spds=None):
    ret = []
    for i in range(4):
        fName = f"flow-preset-{i}"

        if spds is None:
            ret.append(read_parameter(iface, fName))
        else:
            ret.append(iface.call(fName, 'wr', spds[i]))

    return ret


def set_max_current(iface: modbus_interface, curr=None):
    fName = 'conf-modbus-maxcurrent'

    if curr == 0:
        return read_parameter(iface, fName)
    else:
        return iface.call(fName, 'wr', curr)
