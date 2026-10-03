## new to v16

| ref | class | address | de facto | description | rd | wr | aka |
|----|----|----|----|----|----|----|----|
| 4.1 | Heat pump unit | 59  | 60  | Enable continuous operation mode for condenser pump. | 1  | 5  | enable-condensor-pump-continuous-operation |
| 4.1 | Heat pump unit | 60  | 61  | Allow current limiter to restrict external additional heater | 1  | 5  | allow-limiter-on-external-additional-heater |
| 4.1 | Heat pump unit | 61  | 62  | Allow current limiter to restrict secondary heat pump units | 1  | 5  | allow-limiter-on-secondary-heat-pumps |
| 4.1 | Heat pump unit | 87  | 10088  | Tap water top sensor alarm. | 2  | 0  | tap-water-top-sensor-alarm |
| 4.1 | Heat pump unit | 311  | 30312  | Control software version: Major | 4  | 0  | control-software-version_major |
| 4.1 | Heat pump unit | 312  | 30313  | Control software version: Minor | 4  | 0  | control-software-version_minor |
| 4.1 | Heat pump unit | 313  | 30314  | Control software version: Micro | 4  | 0  | control-software-version_micro |
| 4.1 | Heat pump unit | 315  | 30316  | Expansion valve opening degree | 4  | 0  | expansion-valve-opening |
| 4.1 | Heat pump unit | 319  | 30320  | Inverter temperature | 4  | 0  | inverter-temp |
| 4.1 | Heat pump unit | 117  | 40118  | Outdoor temperature source, is an enumeration where 0 = designated PT1000 sensor located on BM-card. 1 = BMS register 40119 (De Facto). When the source is BMS the outdoor temperature alarm is automatically removed when the sensor data is valid. If no valid sensor data is present the heat pump will use its designated PT1000 sensor and if that sensor is missing the heat pump will use 0 degrees C as a fallback value. | 3  | 6  | outdoor-temp-source |
| 4.1 | Heat pump unit | 118  | 40119  | Outdoor temperature sensor, this register will be the source of the outdoor temperature given that BMS-address 40118 is set to 1. The valid range of the temperature is between -50 to 200 degrees C. If this register is not updated with a new temperature within 12 hours or the value is outside the valid range, the fallback logic will be triggered stated in description of BMS register 40118. This signal is automatically filtered in the heat pump. | 3  | 6  | outdoor-temp-sensor |
| 4.1 | Heat pump unit | 119  | 40120  | Maximum phase current | 3  | 6  | max-phase-current |
| 4.1 | Heat pump unit | 120  | 40121  | Compressor current hysteresis | 3  | 6  | compressor-current-hysteresis |
| 4.1 | Heat pump unit | 321  | 40322  | Enabled immersion heater \*7 (0=Disable immersion heater, 2=Internal immersion heater enabled) | 3  | 6  | immersion-heater-enabled |
| 5.1 | Heating system | 2  | 30003  | Currently running: Bit registers that shows the all the current running demands according to \*6 (0: Manual operation Bit 1: Defrost, Bit 2: Hot water, Bit 3: Heat, Bit 4: Active Cooling, Bit 5: Pool, Bit 6: Anti legionella, Bit 7: Passive Cooling, Bit 8: Reserved, Bit 9: Standby, Bit 10: No demand, Bit 11: OFF) | 4  | 0  | currently-running-demands |
| 5.1 | Heating system | 27  | 30028  | System return line temperature. | 4  | 0  | system-return-line-temp |
| 5.1 | Heating system | 30  | 30031  | Calculated demand (heat) | 4  | 0  | calculated-demand |
| 5.2 | Mix valve 1 | 298  | 40299  | Selected mode for mixing valve 1 (0:Heat, 1:Cool, 2:Auto) | 3  | 6  | mix-valve-1-mode |
| 9.1 | Electric meter | 124  | 40125  | Desired Power Consumption Control, control mode. Controlled by BMS, may be overridden by the Digital input for Smart grid. In SG-Ready mode 0=Normal, 1=Load-Up, 2=EVU, 3=Boost. When in PL/LU mode 0=Normal, 1=Power Limit(defacto address 40126), 2=Load-Up, 3=Power Limit(defacto address 40126) | 3  | 6  | desired-power-consumption-control |
| 9.1 | Electric meter | 125  | 40126  | Input power limit during Power Limitation (defacto 40125), NOTE: If the power limitation is set too low, the compressor will be unable to run. | 3  | 6  | input-power-limit |
