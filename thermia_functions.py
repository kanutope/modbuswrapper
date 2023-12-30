FUNCTIONS = {
    'reset-all-alarms': {
        'address': 3,
        'descr': 'Reset all alarms',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-internal-additional-heater': {
        'address': 4,
        'descr': 'Enable internal additional heater',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-external-additional-heater': {
        'address': 5,
        'descr': 'Enable external additional heater',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-hgw': {
        'address': 6,
        'descr': 'Enable HGW',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-flow-switch/pressure-switch': {
        'address': 7,
        'descr': 'Enable flow switch/pressure switch',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-tap-water': {
        'address': 8,
        'descr': 'Enable tap water',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-heat': {
        'address': 9,
        'descr': 'Enable heat',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-active-cooling': {
        'address': 10,
        'descr': 'Enable active cooling',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-mix-valve-1': {
        'address': 11,
        'descr': 'Enable mix valve 1',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-twc': {
        'address': 12,
        'descr': 'Enable TWC',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-wcs': {
        'address': 13,
        'descr': 'Enable WCS',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-hot-gas-pump': {
        'address': 14,
        'descr': 'Enable hot gas pump',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-mix-valve-2': {
        'address': 16,
        'descr': 'Enable mix valve 2 (EM)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-mix-valve-3': {
        'address': 17,
        'descr': 'Enable mix valve 3 (EM)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-mix-valve-4': {
        'address': 18,
        'descr': 'Enable mix valve 4 (EM)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-mix-valve-5': {
        'address': 19,
        'descr': 'Enable mix valve 5 (EM)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-brine-out-monitoring': {
        'address': 20,
        'descr': 'Enable brine out monitoring',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-brine-pump-continuous-operation': {
        'address': 21,
        'descr': 'Enable brine pump continuous operation',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-system-circulation-pump': {
        'address': 22,
        'descr': 'Enable system circulation pump',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-dew-point-calculation': {
        'address': 23,
        'descr': 'Enable dew point calculation',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-anti-legionella': {
        'address': 24,
        'descr': 'Enable anti legionella',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-additional-heater-only': {
        'address': 25,
        'descr': 'Enable additional heater only (No compressor). Requires Operation mode: Standby',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-current-limitation': {
        'address': 26,
        'descr': 'Enable current limitation',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-pool': {
        'address': 28,
        'descr': 'Enable pool (EM)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-surplus-heat-chiller': {
        'address': 29,
        'descr': 'Enable surplus heat, chiller (no borehole)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-surplus-heat-borehole': {
        'address': 30,
        'descr': 'Enable surplus heat, borehole (no chiller)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-external-additional-heater-pool': {
        'address': 31,
        'descr': 'Enable external additional heater for pool (EM)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-internal-additional-heater-pool': {
        'address': 32,
        'descr': 'Enable internal additional heater for pool (EM)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-passive-cooling': {
        'address': 33,
        'descr': 'Enable passive cooling (EM)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-var-speed-mode-condenser-pump': {
        'address': 34,
        'descr': 'Enable variable speed mode for condenser pump',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-variable-speed-mode-for-brine-pump': {
        'address': 35,
        'descr': 'Enable variable speed mode for brine pump',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-cooling-mode-for-mix-valve-1': {
        'address': 36,
        'descr': 'Enable cooling mode for mixing valve 1',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-cooling-mix-valve-1': {
        'address': 37,
        'descr': 'Enable outdoor temp dependent for cooling with mixing valve 1',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-internal-brine-pump-cooling-mix-valve-1': {
        'address': 38,
        'descr': 'Enable internal brine pump to start when cooling is active for mixing valve 1',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-external-heater': {
        'address': 39,
        'descr': 'Enable outdoor temp dependent for external heater',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-brine-in-monitoring': {
        'address': 40,
        'descr': 'Enable brine in monitoring',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-fixed-system-supply-set-point': {
        'address': 41,
        'descr': 'Enable fixed system supply set point, allows defacto address 40117',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-evaporator-freeze-protection': {
        'address': 42,
        'descr': 'Enable evaporator freeze protection',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-cooling-mix-valve-2': {
        'address': 43,
        'descr': 'Enable outdoor temp dependent for cooling with mixing valve 2 (EM3 only)*5',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-dew-point-calculation-on-mix-valve-2': {
        'address': 44,
        'descr': 'Enable dew point calculation on mixing valve 2, requires room sensor for mixing valve 2 (EM3 only)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-heating-mix-valve-2': {
        'address': 45,
        'descr': 'Enable outdoor temp dependent for heating with mixing valve 2 (EM3 only)*5',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-cooling-mix-valve-3': {
        'address': 46,
        'descr': 'Enable outdoor temp dependent for cooling with mixing valve 3 (EM3 only)*5',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-dew-point-calculation-on-mix-valve-3': {
        'address': 47,
        'descr': 'Enable dew point calculation on mixing valve 3, requires room sensor for mixing valve 3 (EM3 only)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-heating-mix-valve-3': {
        'address': 48,
        'descr': 'Enable outdoor temp dependent for heating with mixing valve 3 (EM3 only)*5',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-cooling-mix-valve-4': {
        'address': 49,
        'descr': 'Enable outdoor temp dependent for cooling with mixing valve 4 (EM3 only)*5',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-dew-point-calculation-on-mix-valve-4': {
        'address': 50,
        'descr': 'Enable dew point calculation on mixing valve 4, requires room sensor for mixing valve 4 (EM3 only)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-heating-mix-valve-4': {
        'address': 51,
        'descr': 'Enable outdoor temp dependent for heating with mixing valve 4 (EM3 only)*5',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-cooling-mix-valve-5': {
        'address': 52,
        'descr': 'Enable outdoor temp dependent for cooling with mixing valve 5 (EM3 only)*5',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-dew-point-calculation-on-mix-valve-5': {
        'address': 53,
        'descr': 'Enable dew point calculation on mixing valve 5, requires room sensor for mixing valve 5 (EM3 only)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-outdoor-temp-heating-mix-valve-5': {
        'address': 54,
        'descr': 'Enable outdoor temp dependent for heating with mixing valve 5 (EM3 only)*5',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-internal-brine-pump-cooling-mix-valve-2': {
        'address': 55,
        'descr': 'Enable internal brine pump to start when cooling is active for mixing valve 2 (EM3 only)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-internal-brine-pump-cooling-mix-valve-3': {
        'address': 56,
        'descr': 'Enable internal brine pump to start when cooling is active for mixing valve 3 (EM3 only)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-internal-brine-pump-cooling-mix-valve-4': {
        'address': 57,
        'descr': 'Enable internal brine pump to start when cooling is active for mixing valve 4 (EM3 only)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'enable-internal-brine-pump-cooling-mix-valve-5': {
        'address': 58,
        'descr': 'Enable internal brine pump to start when cooling is active for mixing valve 5 (EM3 only)',
        'len': 1, 'rd': 1, 'wr': 5, 'scale': 1,
        'validate': 'in_list(0, 1)', 'datatype': 'bits', 'unit': ''},
    'alarm-active-classA': {
        'address': 0,
        'descr': 'Alarm active, Class: A',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'alarm-active-classB': {
        'address': 1,
        'descr': 'Alarm active, Class: B',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'alarm-active-classC': {
        'address': 2,
        'descr': 'Alarm active, Class: C',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'alarm-active-classD': {
        'address': 3,
        'descr': 'Alarm active, Class: D - Genesis secondary',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'alarm-active-classE': {
        'address': 4,
        'descr': 'Alarm active, Class: E - Legacy secondary',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'high-pressure-switch-alarm': {
        'address': 9,
        'descr': 'High pressure switch alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'low-pressure-level-alarm': {
        'address': 10,
        'descr': 'Low pressure level alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'high-discharge-pipe-temp-alarm': {
        'address': 11,
        'descr': 'High discharge pipe temperature alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'operating-pressure-limit-indication': {
        'address': 12,
        'descr': 'Operating pressure limit indication',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'discharge-pipe-sensor-alarm': {
        'address': 13,
        'descr': 'Discharge pipe sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'liquid-line-sensor-alarm': {
        'address': 14,
        'descr': 'Liquid line sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'suction-gas-sensor-alarm': {
        'address': 15,
        'descr': 'Suction gas sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'flow/pressure-switch-alarm': {
        'address': 16,
        'descr': 'Flow/pressure switch alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'power-input-phase-detection-alarm': {
        'address': 22,
        'descr': 'Power input phase detection alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'inverter-slice-alarm': {
        'address': 23,
        'descr': 'Inverter slice alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'system-supply-low-temp-alarm': {
        'address': 24,
        'descr': 'System supply low temperature alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'compressor-low-speed-alarm': {
        'address': 25,
        'descr': 'Compressor low speed alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'low-super-heat-alarm': {
        'address': 26,
        'descr': 'Low super heat alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'pressure-ratio-out-of-range-alarm': {
        'address': 27,
        'descr': 'Pressure ratio out of range alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'compressor-pressure-outside-envelope-alarm': {
        'address': 28,
        'descr': 'Compressor pressure outside envelope alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'brine-temp-out-of-range-alarm': {
        'address': 29,
        'descr': 'Brine temperature out of range alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'brine-in-sensor-alarm': {
        'address': 30,
        'descr': 'Brine in sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'brine-out-sensor-alarm': {
        'address': 31,
        'descr': 'Brine out sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'condenser-in-sensor-alarm': {
        'address': 32,
        'descr': 'Condenser in sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'condenser-out-sensor-alarm': {
        'address': 33,
        'descr': 'Condenser out sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'outdoor-sensor-alarm': {
        'address': 34,
        'descr': 'Outdoor sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'system-supply-line-sensor-alarm': {
        'address': 35,
        'descr': 'System supply line sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-1-supply-line-sensor-alarm': {
        'address': 36,
        'descr': 'Mix valve 1 supply line sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-2-supply-line-sensor-alarm': {
        'address': 37,
        'descr': 'Mix valve 2 supply line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-3-supply-line-sensor-alarm': {
        'address': 38,
        'descr': 'Mix valve 3 supply line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-4-supply-line-sensor-alarm': {
        'address': 39,
        'descr': 'Mix valve 4 supply line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-5-supply-line-sensor-alarm': {
        'address': 40,
        'descr': 'Mix valve 5 supply line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'wcs-return-line-sensor-alarm': {
        'address': 44,
        'descr': 'WCS return line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'twc-supply-line-sensor-alarm': {
        'address': 45,
        'descr': 'TWC supply line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'cooling-tank-sensor-alarm': {
        'address': 46,
        'descr': 'Cooling tank sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'cooling-supply-line-sensor-alarm': {
        'address': 47,
        'descr': 'Cooling supply line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'cooling-circuit-return-line-sensor-alarm': {
        'address': 48,
        'descr': 'Cooling circuit return line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'brine-delta-out-of-range-alarm': {
        'address': 49,
        'descr': 'Brine delta out of range alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'tap-water-mid-sensor-alarm': {
        'address': 50,
        'descr': 'Tap water mid sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'twc-circulation-return-sensor-alarm': {
        'address': 51,
        'descr': 'TWC circulation return sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'hgw-sensor-alarm': {
        'address': 52,
        'descr': 'HGW sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'internal-additional-heater-alarm': {
        'address': 53,
        'descr': 'Internal additional heater alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'brine-in-high-temp-alarm': {
        'address': 55,
        'descr': 'Brine in high temperature alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'brine-in-low-temp-alarm': {
        'address': 56,
        'descr': 'Brine in low temperature alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'brine-out-low-temp-alarm': {
        'address': 57,
        'descr': 'Brine out low temperature alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'twc-circulation-return-low-temp-alarm': {
        'address': 58,
        'descr': 'TWC circulation return low temperature alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'twc-supply-low-temp-alarm': {
        'address': 59,
        'descr': 'TWC supply low temperature alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-1-supply-temp-deviation-alarm': {
        'address': 60,
        'descr': 'Mix valve 1 supply temperature deviation alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-2-supply-temp-deviation-alarm': {
        'address': 61,
        'descr': 'Mix valve 2 supply temperature deviation alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-3-supply-temp-deviation-alarm': {
        'address': 62,
        'descr': 'Mix valve 3 supply temperature deviation alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-4-supply-temp-deviation-alarm': {
        'address': 63,
        'descr': 'Mix valve 4 supply temperature deviation alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-5-supply-temp-deviation-alarm': {
        'address': 64,
        'descr': 'Mix valve 5 supply temperature deviation alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'wcs-return-line-temp-deviation-alarm': {
        'address': 65,
        'descr': 'WCS return line temperature deviation alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'sum-alarm': {
        'address': 66,
        'descr': 'Sum alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'cooling-circuit-supply-line-temp-deviation-alarm': {
        'address': 67,
        'descr': 'Cooling circuit supply line temperature deviation alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'cooling-tank-temp-deviation-alarm': {
        'address': 68,
        'descr': 'Cooling tank temperature deviation alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'surplus-heat-temp-deviation-alarm': {
        'address': 69,
        'descr': 'Surplus heat temperature deviation alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'humidity-room-sensor-alarm': {
        'address': 70,
        'descr': 'Humidity room sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'surplus-heat-supply-line-sensor-alarm': {
        'address': 71,
        'descr': 'Surplus heat supply line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'surplus-heat-return-line-sensor-alarm': {
        'address': 72,
        'descr': 'Surplus heat return line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'cooling-tank-return-line-sensor-alarm': {
        'address': 73,
        'descr': 'Cooling tank return line sensor alarm (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'temp-room-sensor-alarm': {
        'address': 74,
        'descr': 'Temperature room sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'inverter-slice-communication-alarm': {
        'address': 75,
        'descr': 'Inverter slice communication alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'pool-return-line-sensor-alarm': {
        'address': 76,
        'descr': 'Pool return line sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'external-stop-pool': {
        'address': 77,
        'descr': 'External stop for pool, read only',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'external-start-brine-pump': {
        'address': 78,
        'descr': 'External start brine pump, read only',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'external-relay-for-brine-or-ground-water-pump.': {
        'address': 79,
        'descr': 'External relay for brine/ground water pump.',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'tap-water-end-tank-sensor-alarm': {
        'address': 81,
        'descr': 'Tap water end tank sensor alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'maximum-time-for-anti-legionella-exceeded-alarm': {
        'address': 82,
        'descr': 'Maximum time for anti-legionella exceeded alarm',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'genesis-secondary-slice-alarm': {
        'address': 83,
        'descr': 'Genesis secondary slice alarm - this specific secondary slice cannot communicate with its primary.',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'primary-alarm-network-mask-conflict': {
        'address': 84,
        'descr': 'Primary slice alarm - other primary slices detected with a conflict network mask.',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'primary-alarm-secondary-slices-missing': {
        'address': 85,
        'descr': 'Primary slice alarm - the primary has not detected all secondary slices.',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'oil-boost-in-progress': {
        'address': 86,
        'descr': 'Oil boost in progress',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'compressor-control-signal': {
        'address': 199,
        'descr': 'Compressor control signal',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'smart-grid-1': {
        'address': 201,
        'descr': 'Smart Grid 1, EVU input',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'external-alarm-input': {
        'address': 202,
        'descr': 'External alarm input',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'smart-grid-2': {
        'address': 204,
        'descr': 'Smart Grid 2',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'external-additional-heater-control-signal': {
        'address': 206,
        'descr': 'External additional heater control signal',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-1-circulation-pump-control-signal': {
        'address': 209,
        'descr': 'Mix valve 1 circulation pump control signal',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'condenser-pump-on/off-control': {
        'address': 210,
        'descr': 'Condenser pump On/off control',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'system-circulation-pump-control-signal': {
        'address': 211,
        'descr': 'System circulation pump control signal',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'hot-gas-circulation-pump-control-signal': {
        'address': 213,
        'descr': 'Hot gas circulation pump control signal',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'brine-pump-on/off-control': {
        'address': 218,
        'descr': 'Brine pump On/off control',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'external-heater-circulation-pump-control-signal': {
        'address': 219,
        'descr': 'External heater circulation pump control signal',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'heating-season-active': {
        'address': 220,
        'descr': 'Heating season (winter) active',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'external-additional-heater-active': {
        'address': 221,
        'descr': 'External additional heater active',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'internal-additional-heater-active': {
        'address': 222,
        'descr': 'Internal additional heater active',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'hgw-regulation-control-signal': {
        'address': 223,
        'descr': 'HGW regulation control signal',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'heat-pump-stopping': {
        'address': 224,
        'descr': 'Heat pump stopping',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'heat-pump-ok-to-start': {
        'address': 225,
        'descr': 'Heat pump OK to start',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'twc-supply-line-circulation-pump-control-signal': {
        'address': 230,
        'descr': 'TWC supply line circulation pump control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'wcs-regulation-control-signal': {
        'address': 232,
        'descr': 'WCS regulation control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'wcs-circulation-pump-control-signal': {
        'address': 233,
        'descr': 'WCS circulation pump control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'twc-end-tank-heater-control-signal': {
        'address': 234,
        'descr': 'TWC end tank heater control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'pool-directional-valve-position': {
        'address': 235,
        'descr': 'Pool directional valve position (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'cooling-circuit-circulation-pump-control-signal': {
        'address': 236,
        'descr': 'Cooling circuit circulation pump control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'pool-circulation-pump-control-signal': {
        'address': 237,
        'descr': 'Pool circulation pump control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'surplus-heat-directional-valve-position': {
        'address': 238,
        'descr': 'Surplus heat directional valve position (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'surplus-heat-circulation-pump-control-signal': {
        'address': 239,
        'descr': 'Surplus heat circulation pump control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'cooling-circuit-regulation-control-signal': {
        'address': 240,
        'descr': 'Cooling circuit regulation control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'surplus-heat-regulation-control-signal': {
        'address': 241,
        'descr': 'Surplus heat regulation control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'active-cooling-directional-valve-position': {
        'address': 242,
        'descr': 'Active cooling directional valve position (Borehole disconnecte',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'cooling-directional-valve-position': {
        'address': 243,
        'descr': 'Passive/Active cooling directional valve position (Cooling tank (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'pool-regulation-control-signal': {
        'address': 244,
        'descr': 'Pool regulation control signal (EM)',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'mix-valve-1-producing-passive-cooling': {
        'address': 245,
        'descr': 'Indication when mixing valve 1 is producing passive cooling',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'compressor-is-unable-to-speed-up': {
        'address': 246,
        'descr': 'Compressor is unable to speed up',
        'len': 1, 'rd': 2, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'bits', 'unit': ''},
    'currently-first-prioritised-demand': {
        'address': 1,
        'descr': 'Currently running: First prioritised demand *1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'compressor-available-gears': {
        'address': 4,
        'descr': 'Compressor available gears *3',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'compressor-speed-rpm': {
        'address': 5,
        'descr': 'Compressor speed RPM',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'rpm'},
    'external-additional-heater:-current-demand': {
        'address': 6,
        'descr': 'External additional heater: Current demand (%)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'discharge-pipe-temp': {
        'address': 7,
        'descr': 'Discharge pipe temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'condenser-in-temp': {
        'address': 8,
        'descr': 'Condenser in temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'condenser-out-temp': {
        'address': 9,
        'descr': 'Condenser out temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'brine-in-temp': {
        'address': 10,
        'descr': 'Brine in temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'brine-out-temp': {
        'address': 11,
        'descr': 'Brine out temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'system-supply-line-temp': {
        'address': 12,
        'descr': 'System supply line temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'outdoor-temp': {
        'address': 13,
        'descr': 'Outdoor temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'tap-water-top-temp': {
        'address': 15,
        'descr': 'Tap water top temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'tap-water-lower-temp': {
        'address': 16,
        'descr': 'Tap water lower temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'tap-water-weighted-temp': {
        'address': 17,
        'descr': 'Tap water weighted temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'system-supply-line-calculated-set-point': {
        'address': 18,
        'descr': 'System supply line calculated set point',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'selected-heat-curve': {
        'address': 19,
        'descr': 'Selected heat curve, (system) supply line',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'heat-curve-x-coordinate-1': {
        'address': 20,
        'descr': 'Heat curve, X-coordinate 1 (highest outdoor temperature)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'heat-curve-x-coordinate-2': {
        'address': 21,
        'descr': 'Heat curve, X-coordinate 2',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'heat-curve-x-coordinate-3': {
        'address': 22,
        'descr': 'Heat curve, X-coordinate 3',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'heat-curve-x-coordinate-4': {
        'address': 23,
        'descr': 'Heat curve, X-coordinate 4',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'heat-curve-x-coordinate-5': {
        'address': 24,
        'descr': 'Heat curve, X-coordinate 5',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'heat-curve-x-coordinate-6': {
        'address': 25,
        'descr': 'Heat curve, X-coordinate 6',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'heat-curve-x-coordinate-7': {
        'address': 26,
        'descr': 'Heat curve, X-coordinate 7 (lowest outdoor temperature)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'cooling-season-integral-value': {
        'address': 36,
        'descr': 'Cooling season integral value',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'condenser-circulation-pump-speed': {
        'address': 39,
        'descr': 'Condenser circulation pump speed (%)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'mix-valve-1-supply-line-temp': {
        'address': 40,
        'descr': 'Mix valve 1 supply line temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'buffer-tank-temp': {
        'address': 41,
        'descr': 'Buffer tank temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'mix-valve-1-position': {
        'address': 43,
        'descr': 'Mix valve 1 position',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'brine-circulation-pump-speed': {
        'address': 44,
        'descr': 'Brine circulation pump speed (%)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'hgw-supply-line-temp': {
        'address': 45,
        'descr': 'HGW supply line temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'hot-water-directional-valve-position': {
        'address': 47,
        'descr': 'Hot water directional valve position (%)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'compressor-operating-hours': {
        'address': 48,
        'descr': 'Compressor operating hours (MSB)',
        'len': 2, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int32', 'unit': 'hrs'},

    'tap-water-operating-hours': {
        'address': 50,
        'descr': 'Tap water operating hours (MSB)',
        'len': 2, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int32', 'unit': 'hrs'},

    'external-additional-heater-operating-hours': {
        'address': 52,
        'descr': 'External additional heater operating hours (MSB)',
        'len': 2, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int32', 'unit': 'hrs'},

    'compressor-speed-percent': {
        'address': 54,
        'descr': 'Compressor speed percent',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'currently-second-prioritised-demand': {
        'address': 55,
        'descr': 'Currently running: Second prioritised demand *1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'currently-third-prioritised-demand': {
        'address': 56,
        'descr': 'Currently running: Third prioritised demand *1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'software-version:-major': {
        'address': 57,
        'descr': 'Software version: Major',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'software-version:-minor': {
        'address': 58,
        'descr': 'Software version: Minor',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'software-version:-micro': {
        'address': 59,
        'descr': 'Software version: Micro',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'compressor-temporarily-blocked': {
        'address': 60,
        'descr': 'Compressor temporarily blocked, (start restriction timer)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'sec'},
    'compressor-current-gear': {
        'address': 61,
        'descr': 'Compressor current gear',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'queued-demand-first-priority': {
        'address': 62,
        'descr': 'Queued demand, first priority *1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'queued-demand-second-priority': {
        'address': 63,
        'descr': 'Queued demand, second priority *1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'queued-demand-third-priority': {
        'address': 64,
        'descr': 'Queued demand, third priority *1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'queued-demand-fourth-priority': {
        'address': 65,
        'descr': 'Queued demand, fourth priority *1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'queued-demand-fifth-priority': {
        'address': 66,
        'descr': 'Queued demand, fifth priority *1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'internal-additional-heater-current-step': {
        'address': 67,
        'descr': 'Internal additional heater current step',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'buffer-tank-charge-set-point': {
        'address': 68,
        'descr': 'Buffer tank charge set point',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'electric-meter-l1-current': {
        'address': 69,
        'descr': 'Electric meter L1 current (A)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'A'},
    'electric-meter-l2-current': {
        'address': 70,
        'descr': 'Electric meter L2 current (A)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'A'},
    'electric-meter-l3-current': {
        'address': 71,
        'descr': 'Electric meter L3 current (A)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'A'},
    'electric-meter-l1-0-voltage': {
        'address': 72,
        'descr': 'Electric meter L1-0 voltage (V)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'V'},
    'electric-meter-l2-0-voltage': {
        'address': 73,
        'descr': 'Electric meter L2-0 voltage (V)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'V'},
    'electric-meter-l3-0-voltage': {
        'address': 74,
        'descr': 'Electric meter L3-0 voltage (V)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'V'},
    'electric-meter-l1-l2-voltage': {
        'address': 75,
        'descr': 'Electric meter L1-L2 voltage (V)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': 'V'},
    'electric-meter-l2-l3-voltage': {
        'address': 76,
        'descr': 'Electric meter L2-L3 voltage (V)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': 'V'},
    'electric-meter-l3-l1-voltage': {
        'address': 77,
        'descr': 'Electric meter L3-L1 voltage (V)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': 'V'},
    'electric-meter-l1-power': {
        'address': 78,
        'descr': 'Electric meter L1 power (W)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'W'},
    'electric-meter-l2-power': {
        'address': 79,
        'descr': 'Electric meter L2 power (W)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'W'},
    'electric-meter-l3-power': {
        'address': 80,
        'descr': 'Electric meter L3 power (W)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'W'},
    'electric-meter-meter-value': {
        'address': 81,
        'descr': 'Electric meter - meter value (kWh)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': 'kWh'},
    'comfort-mode': {
        'address': 82,
        'descr': 'Comfort mode *4',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'electric-meter-kwh-total-(lsb)': {
        'address': 83,
        'descr': 'Electric meter kWh total (LSB)',
        'len': 2, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int32', 'unit': 'kWh'},

    'wcs-valve-position': {
        'address': 85,
        'descr': 'WCS valve position (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'twc-valve-position': {
        'address': 86,
        'descr': 'TWC valve position (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-2-position': {
        'address': 87,
        'descr': 'Mix valve 2 position (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-3-position': {
        'address': 88,
        'descr': 'Mix valve 3 position (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-4-position': {
        'address': 89,
        'descr': 'Mix valve 4 position (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-5-position': {
        'address': 90,
        'descr': 'Mix valve 5 position (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'dew-point-room': {
        'address': 91,
        'descr': 'Dew point room (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'cooling-supply-line-mix-valve-position': {
        'address': 92,
        'descr': 'Cooling supply line mix valve position (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'surplus-heat-fan-speed': {
        'address': 93,
        'descr': 'Surplus heat fan speed (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'rpm'},
    'pool-supply-line-mix-valve-position': {
        'address': 94,
        'descr': 'Pool supply line mix valve position (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'twc-supply-line-temp': {
        'address': 95,
        'descr': 'TWC supply line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'twc-return-temp': {
        'address': 96,
        'descr': 'TWC return temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'wcs-return-line-temp': {
        'address': 97,
        'descr': 'WCS return line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'twc-end-tank-temp': {
        'address': 98,
        'descr': 'TWC end tank temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'mix-valve-2-supply-line-temp': {
        'address': 99,
        'descr': 'Mix valve 2 supply line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'mix-valve-3-supply-line-temp': {
        'address': 100,
        'descr': 'Mix valve 3 supply line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'mix-valve-4-supply-line-temp': {
        'address': 101,
        'descr': 'Mix valve 4 supply line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'cooling-circuit-return-line-temp': {
        'address': 103,
        'descr': 'Cooling circuit return line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'cooling-tank-temp': {
        'address': 104,
        'descr': 'Cooling tank temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'cooling-tank-return-line-temp': {
        'address': 105,
        'descr': 'Cooling tank return line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'cooling-circuit-supply-line-temp': {
        'address': 106,
        'descr': 'Cooling circuit supply line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'mix-valve-5-supply-line-temp': {
        'address': 107,
        'descr': 'Mix valve 5 supply line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'mix-valve-2-return-line-temp': {
        'address': 109,
        'descr': 'Mix valve 2 return line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'mix-valve-3-return-line-temp': {
        'address': 111,
        'descr': 'Mix valve 3 return line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'mix-valve-4-return-line-temp': {
        'address': 113,
        'descr': 'Mix valve 4 return line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'mix-valve-5-return-line-temp': {
        'address': 115,
        'descr': 'Mix valve 5 return line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'surplus-heat-return-line-temp': {
        'address': 117,
        'descr': 'Surplus heat return line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'surplus-heat-supply-line-temp': {
        'address': 118,
        'descr': 'Surplus heat supply line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'pool-supply-line-temp': {
        'address': 119,
        'descr': 'Pool supply line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'pool-return-line-temp': {
        'address': 120,
        'descr': 'Pool return line temperature (EM)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'room-temp-sensor': {
        'address': 121,
        'descr': 'Room temperature sensor',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'bubble-point-high-pressure-temp': {
        'address': 122,
        'descr': 'Bubble point, high pressure temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'dew-point-high-pressure-temp': {
        'address': 123,
        'descr': 'Dew point, high pressure temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'dew-point-low-pressure-temp': {
        'address': 124,
        'descr': 'Dew point, low pressure temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'superheat-temp': {
        'address': 125,
        'descr': 'Superheat temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'sub-cooling-temp': {
        'address': 126,
        'descr': 'Sub cooling temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'low-pressure-side': {
        'address': 127,
        'descr': 'Low pressure side, pressure (bar(g))',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'bar'},
    'high-pressure-side': {
        'address': 128,
        'descr': 'High pressure side, pressure (bar(g))',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'bar'},
    'liquid-line-temp': {
        'address': 129,
        'descr': 'Liquid line temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'suction-gas-temp': {
        'address': 130,
        'descr': 'Suction gas temperature',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'heating-season-integral-value': {
        'address': 131,
        'descr': 'Heating season integral value',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'p-value-gear-shifting-and-demand-calc': {
        'address': 132,
        'descr': 'P - value for gear shifting and demand calculation',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'i-value-gear-shifting-and-demand-calc': {
        'address': 133,
        'descr': 'I - value for gear shifting and demand calculation',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'd-value-gear-shifting-and-demand-calc': {
        'address': 134,
        'descr': 'D - value for gear shifting and demand calculation',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'i-value-for-compressor-on/off': {
        'address': 135,
        'descr': 'I - value for compressor ON/OFF (Buffer tank)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'p-value-for-compressor-on/off': {
        'address': 136,
        'descr': 'P - value for compressor ON/OFF (Buffer tank)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'mix-valve-cooling-opening-degree': {
        'address': 137,
        'descr': 'Mix valve cooling opening degree (EM2/3)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'desired-gear-for-tap-water': {
        'address': 139,
        'descr': 'Desired gear for tap water',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'desired-gear-for-heating': {
        'address': 140,
        'descr': 'Desired gear for heating',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'desired-gear-for-cooling': {
        'address': 141,
        'descr': 'Desired gear for cooling',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'desired-gear-pool': {
        'address': 142,
        'descr': 'Desired gear for pool',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'number-of-available-secondaries-genesis': {
        'address': 143,
        'descr': 'Number of available secondaries Genesis',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'number-of-available-secondaries-legacy': {
        'address': 144,
        'descr': 'Number of available secondaries Legacy',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'total-distributed-gears-to-all-slices': {
        'address': 145,
        'descr': 'Total distributed gears to all slices',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'maximum-gear': {
        'address': 146,
        'descr': 'Maximum gear out of all the currently requested gears',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'desired-temp-distribution-circuit-mix-valve-1': {
        'address': 147,
        'descr': 'Desired temperature distribution circuit Mix valve 1',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'desired-temp-distribution-circuit-mix-valve-2': {
        'address': 148,
        'descr': 'Desired temperature distribution circuit Mix valve 2',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'desired-temp-distribution-circuit-mix-valve-3': {
        'address': 149,
        'descr': 'Desired temperature distribution circuit Mix valve 3',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'desired-temp-distribution-circuit-mix-valve-4': {
        'address': 150,
        'descr': 'Desired temperature distribution circuit Mix valve 4',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'desired-temp-distribution-circuit-mix-valve-5': {
        'address': 151,
        'descr': 'Desired temperature distribution circuit Mix valve 5',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'disconnect-hot-gas-end-tank': {
        'address': 152,
        'descr': 'Disconnect hot gas end tank, 0 = connected, 1 = disconnected',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'legacy-heat-pump-compressor-running': {
        'address': 153,
        'descr': 'Legacy heat pump compressor running (bit field)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'legacy-heat-pump-reporting-alarm': {
        'address': 154,
        'descr': 'Legacy heat pump reporting alarm (bit field)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'legacy-heat-pump-start-signal': {
        'address': 155,
        'descr': 'Legacy heat pump start signal (bit field)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'legacy-heat-pump-tap-water-signal': {
        'address': 156,
        'descr': 'Legacy heat pump tap water signal (bit field)',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'primary-alarm-combined-classD-alarms': {
        'address': 160,
        'descr': 'Primary slice alarm - the combined output of all Class D alarms.',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'primary-alarm-secondaries-comm-lost': {
        'address': 161,
        'descr': 'Primary slice alarm - the primary slice has lost communication with one or more secondaries.',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'primary-alarm-classA-secondary-heat-pomp': {
        'address': 162,
        'descr': 'Primary slice alarm - Class A alarm detected on the Genesis secondary heat pump slice.',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'primary-alarm-classB-secondary-heat-pomp': {
        'address': 163,
        'descr': 'Primary slice alarm - Class B alarm detected on the Genesis secondary heat pump slice.',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'primary-alarm-combined-classE-alarms': {
        'address': 170,
        'descr': 'Primary slice alarm - the combined output of all Class E alarms.',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'primary-alarm-legacy-heat-pump': {
        'address': 171,
        'descr': 'Primary slice alarm - general legacy heat pump alarm.',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'primary-alarm-expansion-card-comm': {
        'address': 173,
        'descr': 'Primary slice alarm - the primary slice cannot communicate with the legacy heat pump expansion card.',
        'len': 1, 'rd': 4, 'wr': 0, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'operational-mode': {
        'address': 0,
        'descr': 'Operational mode *2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'max-limitation-set-point-curve-radiator': {
        'address': 3,
        'descr': 'Max limitation, set point curve radiator',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'min-limitation-set-point-curve-radiator': {
        'address': 4,
        'descr': 'min. limitation, set point curve radiator',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'comfort-wheel-setting': {
        'address': 5,
        'descr': 'Comfort wheel setting',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-heat-curve-y-coordinate-1': {
        'address': 6,
        'descr': 'Set point heat curve, Y-coordinate 1 (highest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-heat-curve-y-coordinate-2': {
        'address': 7,
        'descr': 'Set point heat curve, Y-coordinate 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-heat-curve-y-coordinate-3': {
        'address': 8,
        'descr': 'Set point heat curve, Y-coordinate 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-heat-curve-y-coordinate-4': {
        'address': 9,
        'descr': 'Set point heat curve, Y-coordinate 4',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-heat-curve-y-coordinate-5': {
        'address': 10,
        'descr': 'Set point heat curve, Y-coordinate 5',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-heat-curve-y-coordinate-6': {
        'address': 11,
        'descr': 'Set point heat curve, Y-coordinate 6',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-heat-curve-y-coordinate-7': {
        'address': 12,
        'descr': 'Set point heat curve, Y-coordinate 7 (lowest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'heating-season-stop-temp': {
        'address': 16,
        'descr': 'Heating season stop temperature',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'start-temp-tap-water': {
        'address': 22,
        'descr': 'Start temperature tap water',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'stop-temp-tap-water': {
        'address': 23,
        'descr': 'Stop temperature tap water',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'min-allowed-gear-in-heating': {
        'address': 26,
        'descr': 'min. allowed gear in heating *3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'maximum-allowed-gear-in-heating': {
        'address': 27,
        'descr': 'Maximum allowed gear in heating *3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'maximum-allowed-gear-in-tap-water': {
        'address': 28,
        'descr': 'Maximum allowed gear in tap water *3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'min-allowed-gear-in-tap-water': {
        'address': 29,
        'descr': 'min. allowed gear in tap water *3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'cooling-mix-valve-set-point': {
        'address': 30,
        'descr': 'Cooling mix valve set point (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'twc-mix-valve-set-point': {
        'address': 31,
        'descr': 'TWC mix valve set point (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'wcs-return-line-set-point': {
        'address': 32,
        'descr': 'WCS return line set point (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'twc-mix-valve-lowest-allowed-opening-degree': {
        'address': 33,
        'descr': 'TWC mix valve lowest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'twc-mix-valve-highest-allowed-opening-degree': {
        'address': 34,
        'descr': 'TWC mix valve highest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'twc-start-temp-immersion-heater': {
        'address': 35,
        'descr': 'TWC start temperature immersion heater (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'twc-start-delay-immersion-heater': {
        'address': 36,
        'descr': 'TWC start delay immersion heater, seconds (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': 'sec'},
    'twc-stop-temp-immersion-heater': {
        'address': 37,
        'descr': 'TWC stop temperature immersion heater (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'wcs-mix-valve-lowest-allowed-opening-degree': {
        'address': 38,
        'descr': 'WCS mix valve lowest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'wcs-mix-valve-highest-allowed-opening-degree': {
        'address': 39,
        'descr': 'WCS mix valve highest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-2-lowest-allowed-opening-degree': {
        'address': 40,
        'descr': 'Mix valve 2 lowest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-2-highest-allowed-opening-degree': {
        'address': 41,
        'descr': 'Mix valve 2 highest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-3-lowest-allowed-opening-degree': {
        'address': 42,
        'descr': 'Mix valve 3 lowest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-3-highest-allowed-opening-degree': {
        'address': 43,
        'descr': 'Mix valve 3 highest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-4-lowest-allowed-opening-degree': {
        'address': 44,
        'descr': 'Mix valve 4 lowest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-4-highest-allowed-opening-degree': {
        'address': 45,
        'descr': 'Mix valve 4 highest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-5-lowest-allowed-opening-degree': {
        'address': 46,
        'descr': 'Mix valve 5 lowest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'mix-valve-5-highest-allowed-opening-degree': {
        'address': 47,
        'descr': 'Mix valve 5 highest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'surplus-heat-chiller-set-point': {
        'address': 48,
        'descr': 'Surplus heat chiller set point (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'cooling-supply-line-mix-valve-lowest-allowed': {
        'address': 49,
        'descr': 'Cooling supply line mix valve: Lowest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'cooling-supply-line-mix-valve-highest-allowed': {
        'address': 50,
        'descr': 'Cooling supply line mix valve: Highest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'surplus-heat-opening-degree-for-starting-fan-1': {
        'address': 51,
        'descr': 'Surplus heat opening degree for starting fan 1 (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'surplus-heat-opening-degree-for-starting-fan-2': {
        'address': 52,
        'descr': 'Surplus heat opening degree for starting fan 2 (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'surplus-heat-opening-degree-for-stopping-fan-1': {
        'address': 53,
        'descr': 'Surplus heat opening degree for stopping fan 1 (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'surplus-heat-opening-degree-for-stopping-fan-2': {
        'address': 54,
        'descr': 'Surplus heat opening degree for stopping fan 2 (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'surplus-heat-lowest-allowed-opening-degree': {
        'address': 55,
        'descr': 'Surplus heat lowest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'surplus-heat-highest-allowed-opening-degree': {
        'address': 56,
        'descr': 'Surplus heat highest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'pool-charge-set-point': {
        'address': 58,
        'descr': 'Pool charge set point (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'pool-mix-valve-lowest-allowed-opening-degree': {
        'address': 59,
        'descr': 'Pool mix valve lowest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'pool-mix-valve-highest-allowed-opening-degree': {
        'address': 60,
        'descr': 'Pool mix valve highest allowed opening degree (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°'},
    'gear-shift-delay-heating': {
        'address': 61,
        'descr': 'Gear shift delay heating',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'gear-shift-delay-pool': {
        'address': 62,
        'descr': 'Gear shift delay pool',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'gear-shift-delay-cooling': {
        'address': 63,
        'descr': 'Gear shift delay cooling',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'brine-in-high-alarm-limit': {
        'address': 67,
        'descr': 'Brine in high alarm limit',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'brine-in-low-alarm-limit': {
        'address': 68,
        'descr': 'Brine in low alarm limit',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'brine-out-low-alarm-limit': {
        'address': 69,
        'descr': 'Brine out low alarm limit',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'brine-max-delta-limit': {
        'address': 70,
        'descr': 'Brine max delta limit',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'hot-gas-pump-start-temp-discharge-pipe': {
        'address': 71,
        'descr': 'Hot gas pump start temperature discharge pipe',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'hot-gas-pump-lower-stop-limit-temp-discharge-pipe': {
        'address': 72,
        'descr': 'Hot gas pump lower stop limit temperature discharge pipe',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'hot-gas-pump-upper-stop-limit-temp-discharge-pipe': {
        'address': 73,
        'descr': 'Hot gas pump upper stop limit temperature discharge pipe',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'external-additional-heater-start-(pid-sum)': {
        'address': 75,
        'descr': 'External additional heater start (PID sum)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'condenser-pump-lowest-allowed-speed': {
        'address': 76,
        'descr': 'Condenser pump lowest allowed speed (%)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'brine-pump-lowest-allowed-speed': {
        'address': 77,
        'descr': 'Brine pump lowest allowed speed (%)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'external-additional-heater-stop-(pid-sum)': {
        'address': 78,
        'descr': 'External additional heater stop (PID sum)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'condenser-pump-highest-allowed-speed': {
        'address': 79,
        'descr': 'Condenser pump highest allowed speed (%)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'brine-pump-highest-allowed-speed': {
        'address': 80,
        'descr': 'Brine pump highest allowed speed (%)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'condenser-pump-standby-speed': {
        'address': 81,
        'descr': 'Condenser pump standby speed (%)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'brine-pump-standby-speed': {
        'address': 82,
        'descr': 'Brine pump standby speed (%)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '%'},
    'min-allowed-gear-in-pool': {
        'address': 85,
        'descr': 'min. allowed gear in pool *3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'maximum-allowed-gear-in-pool': {
        'address': 86,
        'descr': 'Maximum allowed gear in pool *3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'min-allowed-gear-in-cooling': {
        'address': 87,
        'descr': 'min. allowed gear in cooling *3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'maximum-allowed-gear-in-cooling': {
        'address': 88,
        'descr': 'Maximum allowed gear in cooling *3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': '', 'datatype': 'int16', 'unit': ''},
    'start-temp-for-cooling': {
        'address': 105,
        'descr': 'Start temp for cooling (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'stop-temp-for-cooling': {
        'address': 106,
        'descr': 'Stop temp for cooling (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'min-limit-set-point-curve-radiator-mix-valve-1': {
        'address': 107,
        'descr': 'min. limitation Set point curve radiator Mix valve 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'max-limit-set-point-curve-radiator-mix-valve-1': {
        'address': 108,
        'descr': 'Max limitation Set point curve radiator Mix valve 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-1-mix-valve-1': {
        'address': 109,
        'descr': 'Set point curve, Y-coordinate 1 Mix valve 1 (highest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-2-mix-valve-1': {
        'address': 110,
        'descr': 'Set point curve, Y-coordinate 2 Mix valve 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-3-mix-valve-1': {
        'address': 111,
        'descr': 'Set point curve, Y-coordinate 3 Mix valve 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-4-mix-valve-1': {
        'address': 112,
        'descr': 'Set point curve, Y-coordinate 4 Mix valve 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-5-mix-valve-1': {
        'address': 113,
        'descr': 'Set point curve, Y-coordinate 5 Mix valve 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-6-mix-valve-1': {
        'address': 114,
        'descr': 'Set point curve, Y-coordinate 6 Mix valve 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-7-mix-valve-1': {
        'address': 115,
        'descr': 'Set point curve, Y-coordinate 7 Mix valve 1 (lowest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'fixed-system-supply-set-point': {
        'address': 116,
        'descr': 'Fixed system supply set point, requires defacto address 42 to be enabled',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'min-limit-set-point-curve-radiator-mix-valve-2': {
        'address': 199,
        'descr': 'min. limitation Set point curve radiator Mix valve 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'max-limit-set-point-curve-radiator-mix-valve-2': {
        'address': 200,
        'descr': 'Max limitation Set point curve radiator Mix valve 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-1-mix-valve-2': {
        'address': 201,
        'descr': 'Set point curve, Y-coordinate 1 Mix valve 2 (highest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-2-mix-valve-2': {
        'address': 202,
        'descr': 'Set point curve, Y-coordinate 2 Mix valve 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-3-mix-valve-2': {
        'address': 203,
        'descr': 'Set point curve, Y-coordinate 3 Mix valve 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-4-mix-valve-2': {
        'address': 204,
        'descr': 'Set point curve, Y-coordinate 4 Mix valve 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-5-mix-valve-2': {
        'address': 205,
        'descr': 'Set point curve, Y-coordinate 5 Mix valve 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-6-mix-valve-2': {
        'address': 206,
        'descr': 'Set point curve, Y-coordinate 6 Mix valve 2',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-7-mix-valve-2': {
        'address': 207,
        'descr': 'Set point curve, Y-coordinate 7 Mix valve 2 (lowest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'min-limit-set-point-curve-radiator-mix-valve-3': {
        'address': 208,
        'descr': 'min. limitation Set point curve radiator Mix valve 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'max-limit-set-point-curve-radiator-mix-valve-3': {
        'address': 209,
        'descr': 'Max limitation Set point curve radiator Mix valve 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-1-mix-valve-3': {
        'address': 210,
        'descr': 'Set point curve, Y-coordinate 1 Mix valve 3 (highest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-2-mix-valve-3': {
        'address': 211,
        'descr': 'Set point curve, Y-coordinate 2 Mix valve 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-3-mix-valve-3': {
        'address': 212,
        'descr': 'Set point curve, Y-coordinate 3 Mix valve 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-4-mix-valve-3': {
        'address': 213,
        'descr': 'Set point curve, Y-coordinate 4 Mix valve 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-5-mix-valve-3': {
        'address': 214,
        'descr': 'Set point curve, Y-coordinate 5 Mix valve 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-6-mix-valve-3': {
        'address': 215,
        'descr': 'Set point curve, Y-coordinate 6 Mix valve 3',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-7-mix-valve-3': {
        'address': 216,
        'descr': 'Set point curve, Y-coordinate 7 Mix valve 3 (lowest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'min-limit-set-point-curve-radiator-mix-valve-4': {
        'address': 239,
        'descr': 'min. limitation Set point curve radiator Mix valve 4',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'max-limit-set-point-curve-radiator-mix-valve-4': {
        'address': 240,
        'descr': 'Max limitation Set point curve radiator Mix valve 4',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-1-mix-valve-4': {
        'address': 241,
        'descr': 'Set point curve, Y-coordinate 1 Mix valve 4 (highest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-2-mix-valve-4': {
        'address': 242,
        'descr': 'Set point curve, Y-coordinate 2 Mix valve 4',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-3-mix-valve-4': {
        'address': 243,
        'descr': 'Set point curve, Y-coordinate 3 Mix valve 4',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-4-mix-valve-4': {
        'address': 244,
        'descr': 'Set point curve, Y-coordinate 4 Mix valve 4',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-5-mix-valve-4': {
        'address': 245,
        'descr': 'Set point curve, Y-coordinate 5 Mix valve 4',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-6-mix-valve-4': {
        'address': 246,
        'descr': 'Set point curve, Y-coordinate 6 Mix valve 4',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-7-mix-valve-4': {
        'address': 247,
        'descr': 'Set point curve, Y-coordinate 7 Mix valve 4 (lowest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'min-limit-set-point-curve-radiator-mix-valve-5': {
        'address': 248,
        'descr': 'min. limitation Set point curve radiator Mix valve 5',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'max-limit-set-point-curve-radiator-mix-valve-5': {
        'address': 249,
        'descr': 'Max limitation Set point curve radiator Mix valve 5',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-1-mix-valve-5': {
        'address': 250,
        'descr': 'Set point curve, Y-coordinate 1 Mix valve 5 (highest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-2-mix-valve-5': {
        'address': 251,
        'descr': 'Set point curve, Y-coordinate 2 Mix valve 5',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-3-mix-valve-5': {
        'address': 252,
        'descr': 'Set point curve, Y-coordinate 3 Mix valve 5',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-4-mix-valve-5': {
        'address': 253,
        'descr': 'Set point curve, Y-coordinate 4 Mix valve 5',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-5-mix-valve-5': {
        'address': 254,
        'descr': 'Set point curve, Y-coordinate 5 Mix valve 5',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-6-mix-valve-5': {
        'address': 255,
        'descr': 'Set point curve, Y-coordinate 6 Mix valve 5',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-curve-y-coordinate-7-mix-valve-5': {
        'address': 256,
        'descr': 'Set point curve, Y-coordinate 7 Mix valve 5 (lowest outdoor temperature)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-return-temp-from-pool-to-heat-exchanger': {
        'address': 299,
        'descr': 'Set point return temp from pool to heat exchanger (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-pool-hysteresis': {
        'address': 300,
        'descr': 'Set point pool hysteresis (EM)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 10,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-supply-line-temp-cooling-mix-valve-1': {
        'address': 302,
        'descr': 'Set point for supply line temp passive cooling with mixing valve 1',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'set-point-min-outdoor-temp-when-cooling': {
        'address': 303,
        'descr': 'Set point min. outdoor temp when cooling is permitted',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'external-heater-outdoor-temp-limit': {
        'address': 304,
        'descr': 'External heater outdoor temp limit',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'selected-mode-for-mix-valve-2': {
        'address': 305,
        'descr': 'Selected mode for mixing valve 2, 0:Heat, 1:Cool, 2:Auto (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'in_list(0, 1, 2)', 'datatype': 'int16', 'unit': ''},
    'desired-cooling-temp-setpoint-mix-valve-2': {
        'address': 306,
        'descr': 'Desired cooling temperature setpoint mixing valve 2 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'seasonal-cooling-temp-mix-valve-2': {
        'address': 307,
        'descr': 'Seasonal cooling temperature (outdoor temp.), mixing valve 2 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'seasonal-heating-temp-mix-valve-2': {
        'address': 308,
        'descr': 'Seasonal heating temperature (outdoor temp.), mixing valve 2 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'selected-mode-for-mix-valve-3': {
        'address': 309,
        'descr': 'Selected mode for mixing valve 3, 0:Heat, 1:Cool, 2:Auto (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'in_list(0, 1, 2)', 'datatype': 'int16', 'unit': ''},
    'desired-cooling-temp-setpoint-mix-valve-3': {
        'address': 310,
        'descr': 'Desired cooling temperature setpoint mixing valve 3 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'seasonal-cooling-temp-mix-valve-3': {
        'address': 311,
        'descr': 'Seasonal cooling temperature (outdoor temp.), mixing valve 3 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'seasonal-heating-temp-mix-valve-3': {
        'address': 312,
        'descr': 'Seasonal heating temperature (outdoor temp.), mixing valve 3 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'selected-mode-for-mix-valve-4': {
        'address': 313,
        'descr': 'Selected mode for mixing valve 4, 0:Heat, 1:Cool, 2:Auto (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'in_list(0, 1, 2)', 'datatype': 'int16', 'unit': ''},
    'desired-cooling-temp-setpoint-mix-valve-4': {
        'address': 314,
        'descr': 'Desired cooling temperature setpoint mixing valve 4 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'seasonal-cooling-temp-mix-valve-4': {
        'address': 315,
        'descr': 'Seasonal cooling temperature (outdoor temp.), mixing valve 4 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'seasonal-heating-temp-mix-valve-4': {
        'address': 316,
        'descr': 'Seasonal heating temperature (outdoor temp.), mixing valve 4 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'selected-mode-for-mix-valve-5': {
        'address': 317,
        'descr': 'Selected mode for mixing valve 5, 0:Heat, 1:Cool, 2:Auto (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 1,
        'validate': 'in_list(0, 1, 2)', 'datatype': 'int16', 'unit': ''},
    'desired-cooling-temp-setpoint-mix-valve-5': {
        'address': 318,
        'descr': 'Desired cooling temperature setpoint mixing valve 5 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'seasonal-cooling-temp-mix-valve-5': {
        'address': 319,
        'descr': 'Seasonal cooling temperature (outdoor temp.), mixing valve 5 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
    'seasonal-heating-temp-mix-valve-5': {
        'address': 320,
        'descr': 'Seasonal heating temperature (outdoor temp.), mixing valve 5 (EM3 only)',
        'len': 1, 'rd': 3, 'wr': 6, 'scale': 100,
        'validate': '', 'datatype': 'int16', 'unit': '°C'},
}
