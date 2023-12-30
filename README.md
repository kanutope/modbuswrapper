# modbus_wrapper

___

## context

Having refurbished our new home including a brand new technical installation, 
we've got a couple of (new) appliances that are modbus capable. So, I went 
looking for a python based solution in order to get grip on those devices.

I *stumbled* into [pyubbinkext](https://github.com/asillye/pyubbink) from
Adam Sillye, and succeeded to read from and even write to **Ubiflux Vigor W400**,
using a Raspberry Pi with an RS-485 hat. Though I had two more appliances to talk
with: the Thermia Calibra heat-pump and the Alfen Eve Single charging station.
The latter two accessible through [Modbus/TCP](https://modbus.org/toolkit.php).

So, I did want to be able to talk with three (and even more) different devices,
using both serial Modbus (RS485) and Modbus/TCP, in an as flexible as possible
way = in a highly configurable way.

## solution

So, the solution I finally built is contained in the core module ***wrapper.py***.
It has two main two components.

The first component is the function `modbus_client(node)` which returns either a `ModbusSerialClient`
or `ModbusTCPClient`. It takes a `dict` defining the device either as a serial or a networked (tcp) device:

        'serial': {
            'device': '/dev/ttyAMA0',
            'baudrate': 19200,
        },

        'tcp': {
            'host': '172.16.1.14',
            'port': 502,
        },

The second core component is the class `modbus_interface` which incorporates
the previously created ***ModbusXXXClient***. The actual Modbus read or write
calls are made through the member method

`modbus_interface.call(fName, action, value=None)` with

    fname: a textual, user defined name for the Modbus function 
            supported by the device, see 
    action: either 'rd' or 'wr'
    value:  only to be set when action == 'wr'

## modbus function configuration
On a per appliance (type) basis, I have created configurations files, describing
the various modbus functions supported by that device. The data got extracted from
documentation provided by the supplier. Each function got a user defined name (without spaces
for convenient usage in REST calls). E.g.:

    'comfort-wheel-setting': {
        'address': 5,
        'descr': 'Comfort wheel setting',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},

The `modbus_interface` class only supports validation rules that are definied as
member methods of the class - hence they can easily be extended - currently defined:
- in_list(0, 1, 2)
- between(0, 1000)

For the function details see:
- `alfen_functions.py` - [Alfen](https://alfen.com/file-download/download/public/1610)
- `ubbink_functions.py` - [Ubiflux (Brink)](https://www.brinkclimatesystems.nl/documenten/modbus-uwa2-b-uwa2-e-installation-regulations-gb-614882.pdf)
- `thermia_functions.py` - [Thermia](https://www.geotherma.be/wp-content/uploads/2021/10/Thermia-Modbus-protocol_compressed.pdf)

*hoping the links will continue to work for a while ;-)*

## license
[GNU lesser GPK](LICENSE)

## author
Paul B - aka Kanutope

All feedback more than welcome. Hope it helps :-).
