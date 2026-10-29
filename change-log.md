- removed the per call `close()` of the client connection
- `class payloadBuilder` and `class payloadDecoder` dropped because of incompatibility since 3.9.0 onwards
    - replaced by `self.client.convert_to_registers` and `self.client.convert_from_registers`
- `retry_on_empty=True` removed from `ModbusTcpClient` since 3.7.0 onwards
- `pkg_proxy.py` introduced in order to manage incompatibilities between `pymodbus` package
  versions
- `class ConstraintFactory` moved apart to `constraintfactory.py` for better manageabitlity

v2.1 (2026-10-23 16:59:05 +0200)

- adding SMA solar inverter appliance to 'main'

v2.0 (2026-10-21 05:39:40 +0200)

- modbus wrapper refactored with better encapsulation
    - consolidating modbuswrapper
    - freeing application (user program) from wrapper *internals*
    - `ruff` based cleanup
- making a few things more robust
    - replacing `eval()` based validation function by `class ConstraintFactory`
        (inspired by *Gemini*)
- mitigating issue with exclusive lock on ttyAMA0 (`exclusive=False`)
- thermia (calibra) genesis 17 protocal added
- documenting thermia genesis (thermia_genesis.md)

v1.1 (2025-08-15 11:53:45 +0200)

- thermia (calibra) genesis 16 protocal added

v1.0 (2025-03-07 12:08:53 +0100)

- configuration.py moved away to application (user program)
- validation inList has become in_list
- scaling added to ubbink functions
- slashes removed from function names
- extending testorder.py with writes

v0.1 (2023-12-30 17:56:30 +0100)

- First commit of independent package

20231222 - delay between multiple, consecutive calls is for certain devices a MUST, e.g. Alfen CS.

- It is set in configuration.py

20231223 - remove async entirely from project as it doesn't work (anymore) since ???

- implication: attribute 'synchro' is no longer used and removed from the configuration.