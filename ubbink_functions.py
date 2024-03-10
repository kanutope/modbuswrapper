minFlow = 50
maxFlow = 385

FUNCTIONS = {
    'exhaust-air-current-flow': {
        'address': 4042,
        'descr': 'Current value flow exhaust air',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'm3/h'},
    'supply-air-current-flow': {
        'address': 4032,
        'descr': 'Current value of supply air',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'm3/h'},
    'exhaust-air-setpoint': {
        'address': 4041,
        'descr': 'Setpoint flow exhaust air',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'm3/h'},
    'supply-air-setpoint': {
        'address': 4031,
        'descr': 'Setpoint supply air',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'm3/h'},
    'exhaust-anemometer-speed': {
        'address': 4045,
        'descr': 'Speed exhaust anemometer',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'rpm'},
    'supply-anemometer-speed': {
        'address': 4035,
        'descr': 'Speed inlet anemometer',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'rpm'},
    'exhaust-fan-humidity': {
        'address': 4047,
        'descr': 'Fan exhaust sensor rel. humidity',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': 'between(0, 1000)', 'datatype': 'uint16', 'unit': '%'},
    'supply-fan-humidity': {
        'address': 4037,
        'descr': 'Fan inlet sensor rel. humidity',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': 'between(0, 1000)', 'datatype': 'uint16', 'unit': '%'},
    'exhaust-fan-speed': {
        'address': 4044,
        'descr': 'Speed exhaust fan',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'supply-fan-speed': {
        'address': 4034,
        'descr': 'Speed supply fan',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'rpm'},
    'exhaust-fan-status': {
        'address': 4040,
        'descr': 'Fan exhaust Status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(2, 6)', 'datatype': 'uint16', 'unit': ''},
    'supply-fan-status': {
        'address': 4030,
        'descr': 'Fan Inlet Status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(2, 6)', 'datatype': 'uint16', 'unit': ''},
    'exhaust-fan-temperature': {
        'address': 4046,
        'descr': 'Temperature sensor exhaust fan',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'supply-fan-temperature': {
        'address': 4036,
        'descr': 'Temperature sensor supply fan',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'exhaust-pressure-current': {
        'address': 4024,
        'descr': 'Current exhaust pressure',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 5000)', 'datatype': 'int16', 'unit': ''},
    'supply-pressure-current': {
        'address': 4023,
        'descr': 'Current supply pressure',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': 'dPa'},
    'analogue-input-1-mode': {
        'address': 6220,
        'descr': 'Analogue Input 1 Mode',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'analogue-input-1-vmax': {
        'address': 6222,
        'descr': 'Analogue input 1 Vmax',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': 'dV'},
    'analogue-input-1-vmin': {
        'address': 6221,
        'descr': 'Analogue input 1 Vmin',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': 'dV'},
    'analogue-input-2-mode': {
        'address': 6230,
        'descr': 'Analogue input 2 Mode',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'analogue-input-2-vmax': {
        'address': 6232,
        'descr': 'Analogue input 2 Vmax',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': 'dV'},
    'analogue-input-2-vmin': {
        'address': 6231,
        'descr': 'Analogue input 2 Vmin',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': 'dV'},
    'appliance-reset': {
        'address': 8011,
        'descr': 'Appliance reset',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'int16', 'unit': ''},
    'appliance-type-base-module': {
        'address': 4004,
        'descr': 'Appliance Type',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'bypass-boost': {
        'address': 6104,
        'descr': 'Bypass boost',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'bypass-boost-switch-position': {
        'address': 6105,
        'descr': 'Bypass boost switch position',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2, 3)', 'datatype': 'uint16', 'unit': ''},
    'bypass-mode': {
        'address': 6100,
        'descr': 'Bypass mode',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2)', 'datatype': 'uint16', 'unit': ''},
    'bypass-status': {
        'address': 4050,
        'descr': 'Bypass status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 4)', 'datatype': 'uint16', 'unit': ''},
    'bypass-step-position': {
        'address': 4051,
        'descr': 'Bypass Step Position',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'bypass-temp-from-dwelling': {
        'address': 6101,
        'descr': 'Bypass temperature from dwelling',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(15, 350)', 'datatype': 'int16', 'unit': '°C'},
    'bypass-temp-from-outside': {
        'address': 6102,
        'descr': 'Bypass temperature from outside',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(70, 150)', 'datatype': 'int16', 'unit': '°C'},
    'bypass-temp-hysteresis': {
        'address': 6103,
        'descr': 'Bypass temperature hysteresis',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(0, 50)', 'datatype': 'int16', 'unit': '°C'},
    'capacity-of-preheater': {
        'address': 4061,
        'descr': 'Capacity of preheater',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': '%'},
    'co2-sensor-1-high-level': {
        'address': 6152,
        'descr': 'CO2 sensor 1 high level',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(400, 2000)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-1-low-level': {
        'address': 6151,
        'descr': 'CO2 sensor 1 low level',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(400, 2000)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-1-status': {
        'address': 4200,
        'descr': 'CO2 sensor 1 status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 6)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-2-high-level': {
        'address': 6154,
        'descr': 'CO2 sensor 2 high level',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(400, 2000)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-2-low-level': {
        'address': 6153,
        'descr': 'CO2 sensor 2 low level',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(400, 2000)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-2-status': {
        'address': 4202,
        'descr': 'CO2 sensor 2 status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 6)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-3-high-level': {
        'address': 6156,
        'descr': 'CO2 sensor 3 high level',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(400, 2000)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-3-low-level': {
        'address': 6155,
        'descr': 'CO2 sensor 3 low level',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(400, 2000)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-3-status': {
        'address': 4204,
        'descr': 'CO2 sensor 3 status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 6)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-4-high-level': {
        'address': 6158,
        'descr': 'CO2 sensor 4 high level',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(400, 2000)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-4-low-level': {
        'address': 6157,
        'descr': 'CO2 sensor 4 low level',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(400, 2000)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-4-status': {
        'address': 4206,
        'descr': 'CO2 sensor 4 status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 6)', 'datatype': 'uint16', 'unit': ''},
    'co2-sensor-mode': {
        'address': 6150,
        'descr': 'CO2 sensor mode',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'current-date-days': {
        'address': 4111,
        'descr': 'Current date',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'current-date-years': {
        'address': 4112,
        'descr': 'Current date',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'current-time': {
        'address': 4110,
        'descr': 'Current time',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_time', 'unit': 'hrs'},
    'date-format': {
        'address': 6901,
        'descr': 'Date format',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'date-month-day': {
        'address': 6903,
        'descr': 'Date Month Day',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_month_day', 'unit': ''},
    'date-year': {
        'address': 6904,
        'descr': 'Date Year',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'datetime-rest': {
        'address': 6906,
        'descr': 'DateTime Rest',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_dt_rest', 'unit': ''},
    'days-before-filter-warning': {
        'address': 6120,
        'descr': 'Days before filter warning',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(1, 365)', 'datatype': 'uint16', 'unit': ''},
    'default-geo-heat-exchanger-valve-position': {
        'address': 6243,
        'descr': 'Default geo heat exchanger Valve Position',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'device-type-uif-module': {
        'address': 4404,
        'descr': 'Device Type',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'device-type-uwa2-e-module': {
        'address': 4504,
        'descr': 'Device Type',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'digital-input-1-exhaust-fan-function': {
        'address': 6203,
        'descr': 'Digital Input 1 exhaust fan function',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(0, 7)', 'datatype': 'uint16', 'unit': ''},
    'digital-input-1-supply-fan-function': {
        'address': 6202,
        'descr': 'Digital input 1 supply fan function',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(0, 7)', 'datatype': 'uint16', 'unit': ''},
    'digital-input-1-function': {
        'address': 6201,
        'descr': 'Digital Input 1 function',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(0, 4)', 'datatype': 'uint16', 'unit': ''},
    'digital-input-2-exhaust-fan-function': {
        'address': 6213,
        'descr': 'Digital input 2 exhaust fan function',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(0, 7)', 'datatype': 'uint16', 'unit': ''},
    'digital-input-2-supply-fan-function': {
        'address': 6212,
        'descr': 'Digital input 2 supply fan function',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(0, 7)', 'datatype': 'uint16', 'unit': ''},
    'digital-input-2-function': {
        'address': 6211,
        'descr': 'Digital input 2 function',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(0, 4)', 'datatype': 'uint16', 'unit': ''},
    'dipswitch-value-base-module': {
        'address': 4005,
        'descr': 'Dipswitch value',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 63)', 'datatype': 'uint16', 'unit': ''},
    'dipswitch-value-uif-module': {
        'address': 4405,
        'descr': 'Dipswitch value',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 999)', 'datatype': 'uint16', 'unit': ''},
    'dipswitch-value-uwa2-e-module': {
        'address': 4505,
        'descr': 'Dipswitch value',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 63)', 'datatype': 'uint16', 'unit': ''},
    'ebus-power-status': {
        'address': 4101,
        'descr': 'eBus power status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 5)', 'datatype': 'uint16', 'unit': ''},
    'extension-analogue-input-1': {
        'address': 4523,
        'descr': 'Extension Analogue Input 1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': ''},
    'extension-analogue-input-2': {
        'address': 4524,
        'descr': 'Extension Analogue Input 2',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': ''},
    'extension-analogue-output-1': {
        'address': 4543,
        'descr': 'Extension Analogue Output 1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': ''},
    'extension-analogue-output-2': {
        'address': 4544,
        'descr': 'Extension Analogue Output 2',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': ''},
    'extension-contact-1': {
        'address': 4521,
        'descr': 'Extension contact 1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'extension-contact-2': {
        'address': 4522,
        'descr': 'Extension contact 2',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'extension-relay-output-1': {
        'address': 4541,
        'descr': 'Extension Relay output 1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'extension-relay-output-2': {
        'address': 4542,
        'descr': 'Extension Relay output 2',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'external-heater-mode': {
        'address': 6130,
        'descr': 'External heater mode',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2)', 'datatype': 'uint16', 'unit': ''},
    'fan-control-type': {
        'address': 4021,
        'descr': 'Fan control type',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 6)', 'datatype': 'uint16', 'unit': ''},
    'fan-frost-reduction': {
        'address': 4072,
        'descr': 'Fan Frost Reduction',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': '%'},
    'filter-warning-reset': {
        'address': 8010,
        'descr': 'Reset filter warning',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 0xff)', 'datatype': 'int16', 'unit': ''},
    'filters-used-in-hours': {
        'address': 4115,
        'descr': 'Filters used in hours',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'hrs'},
    'filters-used-in-m3-per-hour': {
        'address': 4116,
        'descr': 'Filters used in m3/h',
        'len': 2, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint32', 'unit': 'm3/h'},
    'flow-preset-0': {
        'address': 6000,
        'descr': 'Flow preset 0',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'm3/h'},
    'flow-preset-1': {
        'address': 6001,
        'descr': 'Flow preset 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'm3/h'},
    'flow-preset-2': {
        'address': 6002,
        'descr': 'Flow preset 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'm3/h'},
    'flow-preset-3': {
        'address': 6003,
        'descr': 'Flow preset 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'm3/h'},
    'flow-rate-setting': {
        'address': 8002,
        'descr': 'Desired flow rate setting',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(minFlow, maxFlow)', 'datatype': 'int16', 'unit': 'm3/h'},
    'flow-switch-position': {
        'address': 4080,
        'descr': 'Flow switch position',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 3)', 'datatype': 'uint16', 'unit': ''},
    'flow-type': {
        'address': 6030,
        'descr': 'Flow type',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2)', 'datatype': 'uint16', 'unit': ''},
    'frost-control-min-supply-temperature': {
        'address': 6111,
        'descr': 'Frost control minimum inlet temperature',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(70, 220)', 'datatype': 'int16', 'unit': '°C'},
    'frost-control-temperature': {
        'address': 6110,
        'descr': 'Frost control temperature',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(0, 30)', 'datatype': 'int16', 'unit': '°C'},
    'frost-heaterpower': {
        'address': 4071,
        'descr': 'Frost heaterpower',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 100)', 'datatype': 'uint16', 'unit': '%'},
    'frost-status': {
        'address': 4070,
        'descr': 'Frost status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 16)', 'datatype': 'uint16', 'unit': ''},
    'geo-heat-exchanger': {
        'address': 6240,
        'descr': 'Geo-heat exchanger',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'geo-heat-exchanger-status': {
        'address': 4150,
        'descr': 'Geo heat exchanger status',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'inList(0, 1, 2)', 'datatype': 'uint16', 'unit': ''},
    'geo-heat-exchanger-valve-output': {
        'address': 6244,
        'descr': 'Geo heat exchanger valve output',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2, 3)', 'datatype': 'uint16', 'unit': ''},
    'heat-recovery-appliance': {
        'address': 6171,
        'descr': 'CV (Central Heating) - HRA (Heat Recovery Appliance)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'HRA-active-function': {
        'address': 4020,
        'descr': 'HRA Active Function',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 14)', 'datatype': 'uint16', 'unit': ''},
    'hw-version-base-module': {
        'address': 4003,
        'descr': 'HW Version Base',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_hw_version', 'unit': ''},
    'hw-version-uif-module': {
        'address': 4403,
        'descr': 'HW Version UIF Module',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_hw_version', 'unit': ''},
    'hw-version-uwa2-e-module': {
        'address': 4503,
        'descr': 'HW Version UWA2-E',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_hw_version', 'unit': ''},
    'imbalance-value': {
        'address': 6034,
        'descr': 'Imbalance value',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(0, 20)', 'datatype': 'uint16', 'unit': ''},
    'imbalans-allowed': {
        'address': 6033,
        'descr': 'Imbalans allowed',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'language': {
        'address': 6900,
        'descr': 'Language',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'language-data-version-uif': {
        'address': 4410,
        'descr': 'Language Data version UIF',
        'len': 3, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_sw_version', 'unit': ''},
    'local-button-value': {
        'address': 4421,
        'descr': 'Local Button value',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'local-uif-switch': {
        'address': 4420,
        'descr': 'Local UIF Switch',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'massflow-exhaust-actual': {
        'address': 4043,
        'descr': 'MassFlow exhaust, actual value',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'kg/h'},
    'massflow-supply-actual': {
        'address': 4033,
        'descr': 'MassFlow inlet, actual value',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': 'kg/h'},
    'max-temp-geo-heat-exchanger': {
        'address': 6242,
        'descr': 'Maximum temperature geo-heat exchanger',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(15, 400)', 'datatype': 'int16', 'unit': '°C'},
    'min-temp-geo-heat-exchanger': {
        'address': 6241,
        'descr': 'Minimum temperature geo-heat exchanger',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(0, 100)', 'datatype': 'int16', 'unit': '°C'},
    'modbus-control': {
        'address': 8000,
        'descr': 'Modbus control switched on',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2)', 'datatype': 'int16', 'unit': ''},
    'modbus-interface-type': {
        'address': 7990,
        'descr': 'Modbus interface type',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2)', 'datatype': 'uint16', 'unit': ''},
    'modbus-slave-address': {
        'address': 7991,
        'descr': 'Modbus slave address',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(1, 247)', 'datatype': 'uint16', 'unit': ''},
    'modbus-speed': {
        'address': 7992,
        'descr': 'Modbus speed',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(0, 7)', 'datatype': 'uint16', 'unit': ''},
    'ntc1-temperature': {
        'address': 4081,
        'descr': 'NTC1 temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'ntc2-temperature': {
        'address': 4082,
        'descr': 'NTC2 temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'offset-imbalance-exhaust': {
        'address': 6036,
        'descr': 'Offset imbalance exhaust',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(-15, 15)', 'datatype': 'int16', 'unit': ''},
    'offset-imbalance-supply': {
        'address': 6035,
        'descr': 'Offset imbalance supply',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(-15, 15)', 'datatype': 'int16', 'unit': ''},
    'operating-time': {
        'address': 4113,
        'descr': 'Operating time',
        'len': 2, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint32', 'unit': 'hrs'},
    'postheater-setpoint': {
        'address': 6131,
        'descr': 'Postheater setpoint',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': 'between(150, 300)', 'datatype': 'int16', 'unit': ''},
    'pwm-exhaust-preset-0': {
        'address': 6011,
        'descr': 'PWM exhaust preset 0',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(15, 100)', 'datatype': 'uint16', 'unit': '%'},
    'pwm-supply-preset-0': {
        'address': 6010,
        'descr': 'PWM inlet preset 0',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(15, 100)', 'datatype': 'uint16', 'unit': '%'},
    'pwm-exhaust-preset-1': {
        'address': 6013,
        'descr': 'PWM exhaust preset 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(15, 100)', 'datatype': 'uint16', 'unit': '%'},
    'pwm-supply-preset-1': {
        'address': 6012,
        'descr': 'PWM inlet preset 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(15, 100)', 'datatype': 'uint16', 'unit': '%'},
    'pwm-exhaust-preset-2': {
        'address': 6015,
        'descr': 'PWM exhaust preset 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(15, 100)', 'datatype': 'uint16', 'unit': '%'},
    'pwm-supply-preset-2': {
        'address': 6014,
        'descr': 'PWM inlet preset 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(15, 100)', 'datatype': 'uint16', 'unit': '%'},
    'pwm-exhaust-preset-3': {
        'address': 6017,
        'descr': 'PWM exhaust preset 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(15, 100)', 'datatype': 'uint16', 'unit': '%'},
    'pwm-supply-preset-3': {
        'address': 6016,
        'descr': 'PWM inlet preset 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(15, 100)', 'datatype': 'uint16', 'unit': '%'},
    'rel-humidity-sensor-mode': {
        'address': 6140,
        'descr': 'RHT (humidity) sensor mode',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'rel-humidity-sensor-sensitivity': {
        'address': 6141,
        'descr': 'RHT (humidity) sensor sensitivity',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'between(-2, 2)', 'datatype': 'int16', 'unit': ''},
    'rht-sensor-humidity': {
        'address': 4083,
        'descr': 'RHT Sensor Humidity',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': 'between(0, 1000)', 'datatype': 'uint16', 'unit': '%'},
    'serial-number-base-module': {
        'address': 4010,
        'descr': 'Serial number',
        'len': 3, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_serial_nr', 'unit': ''},
    'signal-output': {
        'address': 6170,
        'descr': 'Signal output',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2, 3)', 'datatype': 'uint16', 'unit': ''},
    'signal-output-level': {
        'address': 4090,
        'descr': 'Signal output',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'standby-mode': {
        'address': 8003,
        'descr': 'Request Standby',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2)', 'datatype': 'int16', 'unit': ''},
    'status-filter': {
        'address': 4100,
        'descr': 'Status filter',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'status-preheater': {
        'address': 4060,
        'descr': 'Status preheater',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'inList(0, 1, 2, 3)', 'datatype': 'uint16', 'unit': ''},
    'sw-version-uif-module-4400': {
        'address': 4400,
        'descr': 'SW Version UIF Module',
        'len': 3, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_sw_version', 'unit': ''},
    'sw-version-uif-module-4413': {
        'address': 4413,
        'descr': 'SW Version UIF Module',
        'len': 3, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_sw_version', 'unit': ''},
    'SW-version-UWA2-B': {
        'address': 4000,
        'descr': 'SW Version UWA2-B',
        'len': 3, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_sw_version', 'unit': ''},
    'sw-version-uwa2-e-module': {
        'address': 4500,
        'descr': 'SW Version UWA2-E',
        'len': 3, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_sw_version', 'unit': ''},
    'switch-default-position': {
        'address': 6031,
        'descr': 'Switch default position',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'switch-position': {
        'address': 8001,
        'descr': 'Request change in switch position',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1, 2, 3)', 'datatype': 'int16', 'unit': ''},
    'switch-type-input-1': {
        'address': 6200,
        'descr': 'Switch type Input 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'switch-type-input-2': {
        'address': 6210,
        'descr': 'Switch type Input 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'temperature-ntc-extension': {
        'address': 4520,
        'descr': 'Temperature NTC Extension',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'time': {
        'address': 6905,
        'descr': 'Time',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'ubbink_time', 'unit': ''},
    'time-notation': {
        'address': 6902,
        'descr': 'Time notation',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'total-flow-in-m3-per-hour': {
        'address': 4118,
        'descr': 'Total flow in m3/h',
        'len': 2, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint32', 'unit': 'm3/h'},
    'use-display-as-switch': {
        'address': 6032,
        'descr': 'Use display as switch',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'inList(0, 1)', 'datatype': 'uint16', 'unit': ''},
    'value-co2-sensor-1': {
        'address': 4201,
        'descr': 'Value CO2 sensor 1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'value-co2-sensor-2': {
        'address': 4203,
        'descr': 'Value CO2 sensor 2',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'value-co2-sensor-3': {
        'address': 4205,
        'descr': 'Value CO2 sensor 3',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'value-co2-sensor-4': {
        'address': 4207,
        'descr': 'Value CO2 sensor 4',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'uint16', 'unit': ''},
    'ventilation-mode': {
        'address': 4022,
        'descr': 'Ventilation mode',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': 'between(0, 4)', 'datatype': 'uint16', 'unit': ''},
}
