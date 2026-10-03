# Thermia Genesis

Since we only have a Calibra 7 heat pump with no other extension than an separate, external passive cooling heat exchanger, the whole Thermia approach is chiefly focused on the Calibra device - or better, I could only test things against our Calibra 7. In the course of developing this modbus wrapper, I have only worked on the Thermia Genesis modbus protocol v10, v16 and v17.

The Thermia modbus protocol documentation is always (until now) provided with the following structure.

Their are first four sections (3.1 to 3.4) that lists all available (accessible) registers, each grouped according to:

| ID  | call type                    | call function        | read | write | de facto offset   |
|-----+------------------------------+----------------------+------+-------+-------------------+
| 3.1 | Read/Write Digital Registers | COIL STATUS          |  1   |  5    | 00001             |
|     |                              |(multiple coils)      |      | 15    |                   |
| 3.2 | Read Digital Registers       | INPUT STATUS         |  2   | -     | 10001             |
| 3.3 | Read Analog Registers        | INPUT REGISTERS      |  4   | -     | 30001             |
| 3.4 | Read/Write Analog Registers  | HOLDING REGISTERS    |  3   |  6    | 40001             |
|     |                              | (multiple registers) |      | 16    |                   |
+-----+------------------------------+----------------------+------+-------+-------------------+

Next comes a number of sections that repeat exactly the same registers, though this time functionally grouped:

| ID  | class           |
+-----+-----------------+
| 4.1 | Heat pump unit  |
| 5.1 | Heating system  |
| 5.2 | Mix valve       |
| 6.1 | Tap water       |
| 6.2 | HGW             |
| 7.1 | Cooling         |
| 7.2 | Cooling circuit |
| 8.1 | Pool            |
| 9.1 | Electric meter  |
+-----+-----------------+

Strangely enough, in the various genesis modbus protocol versions that I have worked through, there are always
discrepancies between the two parts. Some registers are documented in one of the 3.x section while they are
not listed in any of the functional parts. Reversely, some registers alloted to one of the functional parts
is not listed in any of the 3.x sections. This discrepancy occurs in each of the 3 versions I have analyzed, though it differs across the various versions. In my approach, I have always 'maximized' the list of registers covered. And sometimes, I had to make an *informed guess*, as to the applicable *class*.

## version 10

Document reference: **VSJSD1002**

The documentation speaks about both *Mega* and *Diplomat* models, but *Diplomat* is said to be compatible with *Atlas* and *Calibra* - as is demonstrated by later versions of the protocol.

Some statistics:

- 440 different modbus registers listed, of which
    - 421   applicable to *Mega*
    - 331   applicable to *Diplomat* (and *Calibra*)
    - 28    solely applicable to *Diplomat*
    - 108   defined for *Diplomat* but are removed in the later version 16 (and 17)

## version 16

Document reference: ACMBDH01UG0202
Covering: Atlas, Calibra, Calibra Eco, Calibra Cool and Diplomat Inverter

Some statistics
- 264 different modbus registers listed, of which
    - 1     de-facto address occurs twice

| ref. | section   | de-facto | description |
|------|-----------|----------|-------------|
| 6.1  | Tap water | 30048    | Tap water valve position (%) |
| 6.2  |HGW        | 30048    | HGW mix valve position (%)   |


    - 20    not known/ defined in version 10
    - 195   got removed from version 10, of which
        - 87    were *mega-only*
        - 108   were assigned to *diplomat* (hence to *calibra*)  
            and they seem to be still accessible (only partly tested!)
    - 1     register (function) retained while it is assigned to *mega* in version 10

| ref. | section   | de-facto | description |
|------|-----------|----------|-------------|
| 7.4 | Surplus heat | 10239 | Surplus heat directional valve position (EM) |

## version 17.1

Document reference: ACMBDH01UG0402
Covering: Atlas, Calibra, Calibra E, Calibra Cool, Calibra RXT and Diplomat Inverter

Some statistics:
- 266 distinct modbus registers listed, of which
    - 2     not known/ defined in version 16
    - 1     register (function) retained while it is assigned to *mega* in version 10,
            the same as in version 16

| ref. | section   | de-facto | description |
|------|-----------|----------|-------------|
| 7.4 | Surplus heat | 10239 | Surplus heat directional valve position (EM) |
