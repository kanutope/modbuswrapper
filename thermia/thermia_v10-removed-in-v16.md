# modbus registers (calls) removed from diplomat

The following registers (calls/functions) were in later versions removed from the genesis protocol definition between v10.

| ref | class | diplomat inverter | address | de facto address | descr | rd | wr | aka |
|:---:|-------|:-----------------:|--------:|-----------------:|-------|:--:|:--:|-----|
| 4.1 | Heat pump unit | X | 4 | 5 | Enable internal additional heater | 1 | 5 | enable-internal-additional-heater |
| 4.1 | Heat pump unit | X | 53 | 10054 | Internal additional heater alarm | 2 | 0 | internal-additional-heater-alarm |
| 4.1 | Heat pump unit | X | 81 | 10082 | Tap water end tank sensor alarm | 2 | 0 | tap-water-end-tank-sensor-alarm |
| 4.1 | Heat pump unit | X | 82 | 10083 | Maximum time for anti-legionella exceeded alarm | 2 | 0 | maximum-time-for-anti-legionella-exceeded-alarm |
| 4.1 | Heat pump unit | X | 222 | 10223 | Internal additional heater active | 2 | 0 | internal-additional-heater-active |
| 4.1 | Heat pump unit | X | 57 | 30058 | Software version: Major | 4 | 0 | software-version:-major |
| 4.1 | Heat pump unit | X | 58 | 30059 | Software version: Minor | 4 | 0 | software-version:-minor |
| 4.1 | Heat pump unit | X | 59 | 30060 | Software version: Micro | 4 | 0 | software-version:-micro |
| 4.1 | Heat pump unit | X | 132 | 30133 | P - value for gear shifting and demand calculation | 4 | 0 | p-value-gear-shifting-and-demand-calc |
| 4.1 | Heat pump unit | X | 133 | 30134 | I - value for gear shifting and demand calculation | 4 | 0 | i-value-gear-shifting-and-demand-calc |
| 4.1 | Heat pump unit | X | 134 | 30135 | D - value for gear shifting and demand calculation | 4 | 0 | d-value-gear-shifting-and-demand-calc |
| 4.1 | Heat pump unit | X | 135 | 30136 | I - value for compressor ON/OFF (Buffer tank) | 4 | 0 | i-value-for-compressor-on_off |
| 4.1 | Heat pump unit | X | 136 | 30137 | P - value for compressor ON/OFF (Buffer tank) | 4 | 0 | p-value-for-compressor-on_off |
| 6.1 | Tap water | X | 24 | 25 | Enable anti legionella | 1 | 5 | enable-anti-legionella |
| 8.1 | Pool | X | 32 | 33 | Enable internal additional heater for pool (EM) | 1 | 5 | enable-internal-additional-heater-pool |
| 8.1 | Pool | X | 237 | 10238 | Pool circulation pump control signal (EM) | 2 | 0 | pool-circulation-pump-control-signal |
| 8.1 | Pool | X | 244 | 10245 | Pool regulation control signal (EM) | 2 | 0 | pool-regulation-control-signal |
| 8.1 | Pool | X | 94 | 30095 | Pool supply line mix valve position (EM) | 4 | 0 | pool-supply-line-mix-valve-position |
| 5.2 | Mix valve 1 | X | 36 | 37 | Enable cooling mode for mixing valve 1 | 1 | 5 | enable-cooling-mode-for-mix-valve-1 |
| 6.2 | TWC | X | 12 | 13 | Enable TWC | 1 | 5 | enable-twc |
| 6.2 | TWC | X | 45 | 10046 | TWC supply line sensor alarm (EM) | 2 | 0 | twc-supply-line-sensor-alarm |
| 6.2 | TWC | X | 51 | 10052 | TWC circulation return sensor alarm (EM) | 2 | 0 | twc-circulation-return-sensor-alarm |
| 6.2 | TWC | X | 58 | 10059 | TWC circulation return low temperature alarm (EM) | 2 | 0 | twc-circulation-return-low-temp-alarm |
| 6.2 | TWC | X | 59 | 10060 | TWC supply low temperature alarm (EM) | 2 | 0 | twc-supply-low-temp-alarm |
| 6.2 | TWC | X | 230 | 10231 | TWC supply line circulation pump control signal (EM) | 2 | 0 | twc-supply-line-circulation-pump-control-signal |
| 6.2 | TWC | X | 234 | 10235 | TWC end tank heater control signal (EM) | 2 | 0 | twc-end-tank-heater-control-signal |
| 6.2 | TWC | X | 86 | 30087 | TWC valve position (EM) | 4 | 0 | twc-valve-position |
| 6.2 | TWC | X | 95 | 30096 | TWC supply line temperature (EM) | 4 | 0 | twc-supply-line-temp |
| 6.2 | TWC | X | 96 | 30097 | TWC return temperature (EM) | 4 | 0 | twc-return-temp |
| 6.2 | TWC | X | 98 | 30099 | TWC end tank temperature (EM) | 4 | 0 | twc-end-tank-temp |
| 6.2 | TWC | X | 31 | 40032 | TWC mix valve set point (EM) | 3 | 6 | twc-mix-valve-set-point |
| 6.2 | TWC | X | 33 | 40034 | TWC mix valve lowest allowed opening degree (EM) | 3 | 6 | twc-mix-valve-lowest-allowed-opening-degree |
| 6.2 | TWC | X | 34 | 40035 | TWC mix valve highest allowed opening degree (EM) | 3 | 6 | twc-mix-valve-highest-allowed-opening-degree |
| 6.2 | TWC | X | 35 | 40036 | TWC start temperature immersion heater (EM) | 3 | 6 | twc-start-temp-immersion-heater |
| 6.2 | TWC | X | 36 | 40037 | TWC start delay immersion heater, seconds (EM) | 3 | 6 | twc-start-delay-immersion-heater |
| 6.2 | TWC | X | 37 | 40038 | TWC stop temperature immersion heater (EM) | 3 | 6 | twc-stop-temp-immersion-heater |
| 5.3 | Mix valve 2 | X | 16 | 17 | Enable mix valve 2 (EM) | 1 | 5 | enable-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 37 | 10038 | Mix valve 2 supply line sensor alarm (EM) | 2 | 0 | mix-valve-2-supply-line-sensor-alarm |
| 5.3 | Mix valve 2 | X | 61 | 10062 | Mix valve 2 supply temperature deviation alarm (EM) | 2 | 0 | mix-valve-2-supply-temp-deviation-alarm |
| 5.3 | Mix valve 2 | X | 87 | 30088 | Mix valve 2 position (EM) | 4 | 0 | mix-valve-2-position |
| 5.3 | Mix valve 2 | X | 99 | 30100 | Mix valve 2 supply line temperature (EM) | 4 | 0 | mix-valve-2-supply-line-temp |
| 5.3 | Mix valve 2 | X | 109 | 30110 | Mix valve 2 return line temperature (EM) | 4 | 0 | mix-valve-2-return-line-temp |
| 5.3 | Mix valve 2 | X | 148 | 30149 | Desired temperature distribution circuit Mix valve 2 | 4 | 0 | desired-temp-distribution-circuit-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 40 | 40041 | Mix valve 2 lowest allowed opening degree (EM) | 3 | 6 | mix-valve-2-lowest-allowed-opening-degree |
| 5.3 | Mix valve 2 | X | 41 | 40042 | Mix valve 2 highest allowed opening degree (EM) | 3 | 6 | mix-valve-2-highest-allowed-opening-degree |
| 5.3 | Mix valve 2 | X | 199 | 40200 | min. limitation Set point curve radiator Mix valve 2 | 3 | 6 | min-limit-set-point-curve-radiator-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 200 | 40201 | Max limitation Set point curve radiator Mix valve 2 | 3 | 6 | max-limit-set-point-curve-radiator-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 201 | 40202 | Set point curve, Y-coordinate 1 Mix valve 2 (highest outdoor temperature) | 3 | 6 | set-point-curve-y-coordinate-1-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 202 | 40203 | Set point curve, Y-coordinate 2 Mix valve 2 | 3 | 6 | set-point-curve-y-coordinate-2-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 203 | 40204 | Set point curve, Y-coordinate 3 Mix valve 2 | 3 | 6 | set-point-curve-y-coordinate-3-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 204 | 40205 | Set point curve, Y-coordinate 4 Mix valve 2 | 3 | 6 | set-point-curve-y-coordinate-4-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 205 | 40206 | Set point curve, Y-coordinate 5 Mix valve 2 | 3 | 6 | set-point-curve-y-coordinate-5-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 206 | 40207 | Set point curve, Y-coordinate 6 Mix valve 2 | 3 | 6 | set-point-curve-y-coordinate-6-mix-valve-2 |
| 5.3 | Mix valve 2 | X | 207 | 40208 | Set point curve, Y-coordinate 7 Mix valve 2 (lowest outdoor temperature) | 3 | 6 | set-point-curve-y-coordinate-7-mix-valve-2 |
| 5.4 | Mix valve 3 | X | 17 | 18 | Enable mix valve 3 (EM) | 1 | 5 | enable-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 38 | 10039 | Mix valve 3 supply line sensor alarm (EM) | 2 | 0 | mix-valve-3-supply-line-sensor-alarm |
| 5.4 | Mix valve 3 | X | 62 | 10063 | Mix valve 3 supply temperature deviation alarm (EM) | 2 | 0 | mix-valve-3-supply-temp-deviation-alarm |
| 5.4 | Mix valve 3 | X | 88 | 30089 | Mix valve 3 position (EM) | 4 | 0 | mix-valve-3-position |
| 5.4 | Mix valve 3 | X | 100 | 30101 | Mix valve 3 supply line temperature (EM) | 4 | 0 | mix-valve-3-supply-line-temp |
| 5.4 | Mix valve 3 | X | 111 | 30112 | Mix valve 3 return line temperature (EM) | 4 | 0 | mix-valve-3-return-line-temp |
| 5.4 | Mix valve 3 | X | 149 | 30150 | Desired temperature distribution circuit Mix valve 3 | 4 | 0 | desired-temp-distribution-circuit-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 42 | 40043 | Mix valve 3 lowest allowed opening degree (EM) | 3 | 6 | mix-valve-3-lowest-allowed-opening-degree |
| 5.4 | Mix valve 3 | X | 43 | 40044 | Mix valve 3 highest allowed opening degree (EM) | 3 | 6 | mix-valve-3-highest-allowed-opening-degree |
| 5.4 | Mix valve 3 | X | 208 | 40209 | min. limitation Set point curve radiator Mix valve 3 | 3 | 6 | min-limit-set-point-curve-radiator-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 209 | 40210 | Max limitation Set point curve radiator Mix valve 3 | 3 | 6 | max-limit-set-point-curve-radiator-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 210 | 40211 | Set point curve, Y-coordinate 1 Mix valve 3 (highest outdoor temperature) | 3 | 6 | set-point-curve-y-coordinate-1-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 211 | 40212 | Set point curve, Y-coordinate 2 Mix valve 3 | 3 | 6 | set-point-curve-y-coordinate-2-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 212 | 40213 | Set point curve, Y-coordinate 3 Mix valve 3 | 3 | 6 | set-point-curve-y-coordinate-3-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 213 | 40214 | Set point curve, Y-coordinate 4 Mix valve 3 | 3 | 6 | set-point-curve-y-coordinate-4-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 214 | 40215 | Set point curve, Y-coordinate 5 Mix valve 3 | 3 | 6 | set-point-curve-y-coordinate-5-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 215 | 40216 | Set point curve, Y-coordinate 6 Mix valve 3 | 3 | 6 | set-point-curve-y-coordinate-6-mix-valve-3 |
| 5.4 | Mix valve 3 | X | 216 | 40217 | Set point curve, Y-coordinate 7 Mix valve 3 (lowest outdoor temperature) | 3 | 6 | set-point-curve-y-coordinate-7-mix-valve-3 |
| 5.5 | Mix valve 4 | X | 18 | 19 | Enable mix valve 4 (EM) | 1 | 5 | enable-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 39 | 10040 | Mix valve 4 supply line sensor alarm (EM) | 2 | 0 | mix-valve-4-supply-line-sensor-alarm |
| 5.5 | Mix valve 4 | X | 63 | 10064 | Mix valve 4 supply temperature deviation alarm (EM) | 2 | 0 | mix-valve-4-supply-temp-deviation-alarm |
| 5.5 | Mix valve 4 | X | 89 | 30090 | Mix valve 4 position (EM) | 4 | 0 | mix-valve-4-position |
| 5.5 | Mix valve 4 | X | 101 | 30102 | Mix valve 4 supply line temperature (EM) | 4 | 0 | mix-valve-4-supply-line-temp |
| 5.5 | Mix valve 4 | X | 113 | 30114 | Mix valve 4 return line temperature (EM) | 4 | 0 | mix-valve-4-return-line-temp |
| 5.5 | Mix valve 4 | X | 150 | 30151 | Desired temperature distribution circuit Mix valve 4 | 4 | 0 | desired-temp-distribution-circuit-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 44 | 40045 | Mix valve 4 lowest allowed opening degree (EM) | 3 | 6 | mix-valve-4-lowest-allowed-opening-degree |
| 5.5 | Mix valve 4 | X | 45 | 40046 | Mix valve 4 highest allowed opening degree (EM) | 3 | 6 | mix-valve-4-highest-allowed-opening-degree |
| 5.5 | Mix valve 4 | X | 239 | 40240 | min. limitation Set point curve radiator Mix valve 4 | 3 | 6 | min-limit-set-point-curve-radiator-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 240 | 40241 | Max limitation Set point curve radiator Mix valve 4 | 3 | 6 | max-limit-set-point-curve-radiator-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 241 | 40242 | Set point curve, Y-coordinate 1 Mix valve 4 (highest outdoor temperature) | 3 | 6 | set-point-curve-y-coordinate-1-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 242 | 40243 | Set point curve, Y-coordinate 2 Mix valve 4 | 3 | 6 | set-point-curve-y-coordinate-2-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 243 | 40244 | Set point curve, Y-coordinate 3 Mix valve 4 | 3 | 6 | set-point-curve-y-coordinate-3-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 244 | 40245 | Set point curve, Y-coordinate 4 Mix valve 4 | 3 | 6 | set-point-curve-y-coordinate-4-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 245 | 40246 | Set point curve, Y-coordinate 5 Mix valve 4 | 3 | 6 | set-point-curve-y-coordinate-5-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 246 | 40247 | Set point curve, Y-coordinate 6 Mix valve 4 | 3 | 6 | set-point-curve-y-coordinate-6-mix-valve-4 |
| 5.5 | Mix valve 4 | X | 247 | 40248 | Set point curve, Y-coordinate 7 Mix valve 4 (lowest outdoor temperature) | 3 | 6 | set-point-curve-y-coordinate-7-mix-valve-4 |
| 5.6 | Mix valve 5 | X | 19 | 20 | Enable mix valve 5 (EM) | 1 | 5 | enable-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 40 | 10041 | Mix valve 5 supply line sensor alarm (EM) | 2 | 0 | mix-valve-5-supply-line-sensor-alarm |
| 5.6 | Mix valve 5 | X | 64 | 10065 | Mix valve 5 supply temperature deviation alarm (EM) | 2 | 0 | mix-valve-5-supply-temp-deviation-alarm |
| 5.6 | Mix valve 5 | X | 90 | 30091 | Mix valve 5 position (EM) | 4 | 0 | mix-valve-5-position |
| 5.6 | Mix valve 5 | X | 107 | 30108 | Mix valve 5 supply line temperature (EM) | 4 | 0 | mix-valve-5-supply-line-temp |
| 5.6 | Mix valve 5 | X | 115 | 30116 | Mix valve 5 return line temperature (EM) | 4 | 0 | mix-valve-5-return-line-temp |
| 5.6 | Mix valve 5 | X | 151 | 30152 | Desired temperature distribution circuit Mix valve 5 | 4 | 0 | desired-temp-distribution-circuit-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 46 | 40047 | Mix valve 5 lowest allowed opening degree (EM) | 3 | 6 | mix-valve-5-lowest-allowed-opening-degree |
| 5.6 | Mix valve 5 | X | 47 | 40048 | Mix valve 5 highest allowed opening degree (EM) | 3 | 6 | mix-valve-5-highest-allowed-opening-degree |
| 5.6 | Mix valve 5 | X | 248 | 40249 | min. limitation Set point curve radiator Mix valve 5 | 3 | 6 | min-limit-set-point-curve-radiator-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 249 | 40250 | Max limitation Set point curve radiator Mix valve 5 | 3 | 6 | max-limit-set-point-curve-radiator-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 250 | 40251 | Set point curve, Y-coordinate 1 Mix valve 5 (highest outdoor temperature) | 3 | 6 | set-point-curve-y-coordinate-1-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 251 | 40252 | Set point curve, Y-coordinate 2 Mix valve 5 | 3 | 6 | set-point-curve-y-coordinate-2-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 252 | 40253 | Set point curve, Y-coordinate 3 Mix valve 5 | 3 | 6 | set-point-curve-y-coordinate-3-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 253 | 40254 | Set point curve, Y-coordinate 4 Mix valve 5 | 3 | 6 | set-point-curve-y-coordinate-4-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 254 | 40255 | Set point curve, Y-coordinate 5 Mix valve 5 | 3 | 6 | set-point-curve-y-coordinate-5-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 255 | 40256 | Set point curve, Y-coordinate 6 Mix valve 5 | 3 | 6 | set-point-curve-y-coordinate-6-mix-valve-5 |
| 5.6 | Mix valve 5 | X | 256 | 40257 | Set point curve, Y-coordinate 7 Mix valve 5 (lowest outdoor temperature) | 3 | 6 | set-point-curve-y-coordinate-7-mix-valve-5 |
