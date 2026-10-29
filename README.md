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
way, equals highly configurable.

## pymodbus

I started with  `pymodbus` package version 'v3.6' and kept it running for a long time on a
**Raspberry Pi Zero 2 W**. Just recently I worked through upgrading it, up to the current
version '**v3.16.1**'.

It took me a few tweaks to get/keep it running, as I did want to keep it backwards compatibility
(as a sort of personal challenge). It broke twice, once at v3.7 and at v3.10. As I was running
largely behind, I could have fixed and aligned my code with the latest version and leave it like that.

Nevertheless, I did want to find a solution to support two incompatible versions, and that's how I came
to `pkg_proxy.py`. The solution being quite simple, it works: the same code can run with `pymodbus-3.6.9`
up to `pymodbus-3.16.1` without modification.

## modbuswrapper v2.0 refactoring

I have refactored the wrapper to encapsulate more into the core class.

The version 1.x required the user (program) to first create the *ModbusXXXClient* (devices or sockets to
*communicate* with the appliances) and then to create the appropriate interfaces (functions applicable to
the appliance). All that has now been integrated in one wrapper class ***ModbusWrapper***.

Additionally, after an AI quality check, I replaced the *dynamic* code I wrote for validation (based on `eval()`)
with a safer implementation. As proposed by Gemini AI, this resulted in the ***ConstraintFactory*** class.

## version history

- v2.1            SMA solar inverter modbus control added
- v2.0            modbus wrapper refactored with better encapsulation
- v1.1            genesis 16 protocal added
- v1.0            configuration.py moved away to application
- v0.1            Standalone (submoduled) repo

## devices (appliances) implemented

The following modbus capable appliance are implemented

- Alfen Eve Single S-Line (Alfen NG9xx platform v2.3 2020-10-30)
- Ubiflux Vigor Wxxx (Modbus UWA2-B/UWA2-E)
- Thermia Calibra (Modbus Genesis v10/v16/v17)
    - copy the applicable version to `therma_functions.py` (the actual file being used).
- SMA Solar Inverter (MODBUS-HTML_SBxx-1AV-41-GG10-V13)


## solution

The solution I finally built is contained in the core module ***wrapper.py***.


It provides the main component (class) `ModbusWrapper`, providing the 'brokering' features for the program accessing
modbus connected appliances. The user program initializes the whole by creating the wrapper with its known device
configuration:

```python
    # Initialize physical devices
    mdbwrapper = ModbusWrapper(NODES)
```

So, the user program has only to define the *dict* `NODES`, defining the connection with
the appliance either as a serial device (*ModbusSerialClient*) or a networked device (*ModbusTcpClient*):

```python
NODES = {
    'vigor': {
        'serial': {
            'device': '/dev/ttyAMA0',
            'baudrate': 19200,
        },
        'byteorder': '>', 'wordorder': '>',
        'slave': 20,
    },
    'thermia': {
        'tcp': {
            'host': '172.16.1.14',
            'port': 502,
        },
        'byteorder': '>', 'wordorder': '>',
        'slave': 1,
    },
```

The actual modbus read or write calls are then further managed through the interfaces attached
to each device. Sample code can be found in `example/main.py` which relies on `example/implement.py`.


## modbus function configuration

On a per appliance (type) basis, I have created configurations files, describing
the various modbus functions supported by that device. The data got extracted from
documentation provided by the supplier. Each function got a user defined name (without spaces
for convenient usage in REST calls). E.g.:

```python
    'info-firmware-version': {
        'address': 123,
        'slave': 200,
        'descr': 'Firmware version',
        'len': 17, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'str', 'unit': ''},

    'msmt-current-N': {
        'address': 318,
        'slave': 1,
        'descr': 'Current N',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
```

Observe in the example above that a different slave address can be specified per function
(register) call.

The `ModbusWrapper` class only supports validation rules that are defined by the `ConstraintFactory` class.
Currently only two validation function are defined:

    - in_list(0, 1, 2)
    - between(0, 1000)

This can easily be extended by adding more static member functions `_make_XXX` to the `ConstraintFactory` class

```python
    @staticmethod
    def _make_my_own_validation(params) -> Callable[[Any], bool]:
```


## license

[GNU lesser GPL](LICENSE)

## author

Paul B - aka Kanutope

All feedback more than welcome. Hope it helps :-).
