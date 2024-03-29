FUNCTIONS = {
    'info-name': {
        'address': 100,
        'slave': 200,
        'descr': 'Name',
        'len': 17, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'str', 'unit': ''},
    'info-manufacturer': {
        'address': 117,
        'slave': 200,
        'descr': 'Manufacturer',
        'len': 5, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'str', 'unit': ''},
    'info-modbus-table-version': {
        'address': 122,
        'slave': 200,
        'descr': 'Modbus table version',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'info-firmware-version': {
        'address': 123,
        'slave': 200,
        'descr': 'Firmware version',
        'len': 17, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'str', 'unit': ''},
    'info-platform-type': {
        'address': 140,
        'slave': 200,
        'descr': 'Platform type',
        'len': 17, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'str', 'unit': ''},
    'info-station-serial-number': {
        'address': 157,
        'slave': 200,
        'descr': 'Station serial number',
        'len': 11, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'str', 'unit': ''},
    'info-date-year': {
        'address': 168,
        'slave': 200,
        'descr': 'Date year',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'yr'},
    'info-date-month': {
        'address': 169,
        'slave': 200,
        'descr': 'Date month',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'mon'},
    'info-date-day': {
        'address': 170,
        'slave': 200,
        'descr': 'Date day',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'd'},
    'info-time-hour': {
        'address': 171,
        'slave': 200,
        'descr': 'Time hour',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'hr'},
    'info-time-minute': {
        'address': 172,
        'slave': 200,
        'descr': 'Time minute',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'min'},
    'info-time-second': {
        'address': 173,
        'slave': 200,
        'descr': 'Time second',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 's'},
    'info-uptime': {
        'address': 174,
        'slave': 200,
        'descr': 'Uptime',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint64', 'unit': 'ms'},
    'info-time-zone': {
        'address': 178,
        'slave': 200,
        'descr': 'Time zone',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'min'},
    'status-station-active-max': {
        'address': 1100,
        'slave': 200,
        'descr': 'Station Active Max',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'status-current-temperature': {
        'address': 1102,
        'slave': 200,
        'descr': 'Current Temperature',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': '°C'},
    'status-ocpp-state': {
        'address': 1104,
        'slave': 200,
        'descr': 'OCPP state',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'status-number-of-sockets': {
        'address': 1105,
        'slave': 200,
        'descr': 'Nr of sockets',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'SCN-name': {
        'address': 1400,
        'slave': 200,
        'descr': 'SCN name',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'str', 'unit': ''},
    'SCN-sockets': {
        'address': 1404,
        'slave': 200,
        'descr': 'SCN Sockets',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'A'},
    'SCN-total-consumption-L1': {
        'address': 1405,
        'slave': 200,
        'descr': 'SCN Total Consumption Phase L1',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-total-consumption-L2': {
        'address': 1407,
        'slave': 200,
        'descr': 'SCN Total Consumption Phase L2',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-total-consumption-L3': {
        'address': 1409,
        'slave': 200,
        'descr': 'SCN Total Consumption Phase L3',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-actual-max-current-L1': {
        'address': 1411,
        'slave': 200,
        'descr': 'SCN Actual Max Current Phase L1',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-actual-max-current-L2': {
        'address': 1413,
        'slave': 200,
        'descr': 'SCN Actual Max Current Phase L2',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-actual-max-current-L3': {
        'address': 1415,
        'slave': 200,
        'descr': 'SCN Actual Max Current Phase L3',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-max-current-per-L1': {
        'address': 1417,
        'slave': 200,
        'descr': 'SCN Max Current per Phase L1',
        'len': 2, 'rd': 3, 'wr': 16, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-max-current-per-L2': {
        'address': 1419,
        'slave': 200,
        'descr': 'SCN Max Current per Phase L2',
        'len': 2, 'rd': 3, 'wr': 16, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-max-current-per-L3': {
        'address': 1421,
        'slave': 200,
        'descr': 'SCN Max Current per Phase L3',
        'len': 2, 'rd': 3, 'wr': 16, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-rem-valid-time-max-current-L1': {
        'address': 1423,
        'slave': 200,
        'descr': 'Remaining valid time Max Current Phase L1',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint32', 'unit': 's'},
    'SCN-rem-valid-time-max-current-L2': {
        'address': 1425,
        'slave': 200,
        'descr': 'Remaining valid time Max Current Phase L2',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint32', 'unit': 's'},
    'SCN-rem-valid-time-max-current-L3': {
        'address': 1427,
        'slave': 200,
        'descr': 'Remaining valid time Max Current Phase L3',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint32', 'unit': 's'},
    'SCN-safe-current': {
        'address': 1429,
        'slave': 200,
        'descr': 'SCN Safe current',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'SCN-modbus-max-current-enable': {
        'address': 1431,
        'slave': 200,
        'descr': 'SCN Modbus Slave Max Current enable',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},

    'msmt-meter-state': {
        'address': 300,
        'slave': 1,
        'descr': 'Meter state',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'msmt-meter-last-value-timestamp': {
        'address': 301,
        'slave': 1,
        'descr': 'Meter last value timestamp',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint64', 'unit': 'ms'},
    'msmt-meter-type': {
        'address': 305,
        'slave': 1,
        'descr': 'Meter type',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 4)', 'datatype': 'uint16', 'unit': ''},
    'msmt-voltage-phase-v(L1-N)': {
        'address': 306,
        'slave': 1,
        'descr': 'Voltage Phase V(L1-N)',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'V'},
    'msmt-voltage-phase-v(L2-N)': {
        'address': 308,
        'slave': 1,
        'descr': 'Voltage Phase V(L2-N)',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'V'},
    'msmt-voltage-phase-v(L3-N)': {
        'address': 310,
        'slave': 1,
        'descr': 'Voltage Phase V(L3-N)',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'V'},
    'msmt-voltage-phase-v(L1-L2)': {
        'address': 312,
        'slave': 1,
        'descr': 'Voltage Phase V(L1-L2)',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'V'},
    'msmt-voltage-phase-v(L2-L3)': {
        'address': 314,
        'slave': 1,
        'descr': 'Voltage Phase V(L2-L3)',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'V'},
    'msmt-voltage-phase-v(L3-L1)': {
        'address': 316,
        'slave': 1,
        'descr': 'Voltage Phase V(L3-L1)',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'V'},
    'msmt-current-N': {
        'address': 318,
        'slave': 1,
        'descr': 'Current N',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'msmt-current-L1': {
        'address': 320,
        'slave': 1,
        'descr': 'Current Phase L1',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'msmt-current-L2': {
        'address': 322,
        'slave': 1,
        'descr': 'Current Phase L2',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'msmt-current-L3': {
        'address': 324,
        'slave': 1,
        'descr': 'Current Phase L3',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'msmt-current-sum': {
        'address': 326,
        'slave': 1,
        'descr': 'Current Sum',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'msmt-power-factor-L1': {
        'address': 328,
        'slave': 1,
        'descr': 'Power Factor Phase L1',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': ''},
    'msmt-power-factor-L2': {
        'address': 330,
        'slave': 1,
        'descr': 'Power Factor Phase L2',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': ''},
    'msmt-power-factor-L3': {
        'address': 332,
        'slave': 1,
        'descr': 'Power Factor Phase L3',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': ''},
    'msmt-power-factor-sum': {
        'address': 334,
        'slave': 1,
        'descr': 'Power Factor Sum',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': ''},
    'msmt-frequency': {
        'address': 336,
        'slave': 1,
        'descr': 'Frequency',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'Hz'},
    'msmt-real-power-L1': {
        'address': 338,
        'slave': 1,
        'descr': 'Real Power Phase L1',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'W'},
    'msmt-real-power-L2': {
        'address': 340,
        'slave': 1,
        'descr': 'Real Power Phase L2',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'W'},
    'msmt-real-power-L3': {
        'address': 342,
        'slave': 1,
        'descr': 'Real Power Phase L3',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'W'},
    'msmt-real-power-sum': {
        'address': 344,
        'slave': 1,
        'descr': 'Real Power Sum',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'W'},
    'msmt-apparent-power-L1': {
        'address': 346,
        'slave': 1,
        'descr': 'Apparent Power Phase L1',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'VA'},
    'msmt-apparent-power-L2': {
        'address': 348,
        'slave': 1,
        'descr': 'Apparent Power Phase L2',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'VA'},
    'msmt-apparent-power-L3': {
        'address': 350,
        'slave': 1,
        'descr': 'Apparent Power Phase L3',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'VA'},
    'msmt-apparent-power-sum': {
        'address': 352,
        'slave': 1,
        'descr': 'Apparent Power Sum',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'VA'},
    'msmt-reactive-power-L1': {
        'address': 354,
        'slave': 1,
        'descr': 'Reactive Power Phase L1',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'VAr'},
    'msmt-reactive-power-L2': {
        'address': 356,
        'slave': 1,
        'descr': 'Reactive Power Phase L2',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'VAr'},
    'msmt-reactive-power-L3': {
        'address': 358,
        'slave': 1,
        'descr': 'Reactive Power Phase L3',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'VAr'},
    'msmt-reactive-power-sum': {
        'address': 360,
        'slave': 1,
        'descr': 'Reactive Power Sum',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'VAr'},
    'msmt-real-energy-delivered-L1': {
        'address': 362,
        'slave': 1,
        'descr': 'Real Energy Delivered Phase L1',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'Wh'},
    'msmt-real-energy-delivered-L2': {
        'address': 366,
        'slave': 1,
        'descr': 'Real Energy Delivered Phase L2',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'Wh'},
    'msmt-real-energy-delivered-L3': {
        'address': 370,
        'slave': 1,
        'descr': 'Real Energy Delivered Phase L3',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'Wh'},
    'msmt-real-energy-delivered-sum': {
        'address': 374,
        'slave': 1,
        'descr': 'Real Energy Delivered Sum',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'Wh'},
    'msmt-real-energy-consumed-L1': {
        'address': 378,
        'slave': 1,
        'descr': 'Real Energy Consumed Phase L1',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'Wh'},
    'msmt-real-energy-consumed-L2': {
        'address': 382,
        'slave': 1,
        'descr': 'Real Energy Consumed Phase L2',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'Wh'},
    'msmt-real-energy-consumed-L3': {
        'address': 386,
        'slave': 1,
        'descr': 'Real Energy Consumed Phase L3',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'Wh'},
    'msmt-real-energy-consumed-sum': {
        'address': 390,
        'slave': 1,
        'descr': 'Real Energy Consumed Sum',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'Wh'},
    'msmt-apparent-energy-L1': {
        'address': 394,
        'slave': 1,
        'descr': 'Apparent Energy Phase L1',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'VAh'},
    'msmt-apparent-energy-L2': {
        'address': 398,
        'slave': 1,
        'descr': 'Apparent Energy Phase L2',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'VAh'},
    'msmt-apparent-energy-L3': {
        'address': 402,
        'slave': 1,
        'descr': 'Apparent Energy Phase L3',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'VAh'},
    'msmt-apparent-energy-sum': {
        'address': 406,
        'slave': 1,
        'descr': 'Apparent Energy Sum',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'VAh'},
    'msmt-reactive-energy-L1': {
        'address': 410,
        'slave': 1,
        'descr': 'Reactive Energy Phase L1',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'VArh'},
    'msmt-reactive-energy-L2': {
        'address': 414,
        'slave': 1,
        'descr': 'Reactive Energy Phase L2',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'VArh'},
    'msmt-reactive-energy-L3': {
        'address': 418,
        'slave': 1,
        'descr': 'Reactive Energy Phase L3',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'VArh'},
    'msmt-reactive-energy-sum': {
        'address': 422,
        'slave': 1,
        'descr': 'Reactive Energy Sum',
        'len': 4, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt64', 'unit': 'VArh'},

    'conf-availability': {
        'address': 1200,
        'slave': 1,
        'descr': 'Availability',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'conf-mode-3-state': {
        'address': 1201,
        'slave': 1,
        'descr': 'Mode 3 state',
        'len': 5, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'str', 'unit': ''},
    'conf-actual-applied-max-current': {
        'address': 1206,
        'slave': 1,
        'descr': 'Actual Applied Max Current',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'conf-modbus-max-current-valid-time': {
        'address': 1208,
        'slave': 1,
        'descr': 'Modbus Slave Max Current valid time',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint32', 'unit': 's'},
    'conf-modbus-maxcurrent': {
        'address': 1210,
        'slave': 1,
        'descr': 'Modbus Slave MaxCurrent',
        'len': 2, 'rd': 3, 'wr': 16, 'scale': 1,
        'validate': 'between(5, 13)', 'datatype': 'flt32', 'unit': 'A'},
    'conf-active-load-balancing-safe-current': {
        'address': 1212,
        'slave': 1,
        'descr': 'Active Load Balancing Safe Current',
        'len': 2, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'flt32', 'unit': 'A'},
    'conf-modbus-setpoint-accounted-for': {
        'address': 1214,
        'slave': 1,
        'descr': 'Modbus Slave received setpoint accounted for',
        'len': 1, 'rd': 3, 'wr': 0, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'conf-charge-using-1-or-3-phases': {
        'address': 1215,
        'slave': 1,
        'descr': 'Charge using 1 or 3 phases',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'in_list(1, 3)', 'datatype': 'uint16', 'unit': 'phases'},
}
