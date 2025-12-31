# Source: https://learn.sparkfun.com/tutorials/mpl3115a2-pressure-sensor-hookup-guide

## MPL3115A2 Overview

The [MPL3115A2](https://www.sparkfun.com/products/11084) is a low-cost, low power, highly accurate barometric pressure sensor. Use this sensor to detect changes in barometric pressure (weather changes) or for altitude (UAV controllers and the like). The sensor is *very* sensitive and capable of detecting a change of only 0.05kPa which equates to a 0.3m change in altitude.

[![SparkFun Altitude/Pressure Sensor Breakout - MPL3115A2](https://cdn.sparkfun.com/r/600-600/assets/parts/6/4/7/7/11084-01.jpg)](https://www.sparkfun.com/sparkfun-altitude-pressure-sensor-breakout-mpl3115a2.html)

### [SparkFun Altitude/Pressure Sensor Breakout - MPL3115A2](https://www.sparkfun.com/sparkfun-altitude-pressure-sensor-breakout-mpl3115a2.html) 

[ SEN-11084 ]

Life has its ups and downs, so why not measure them? The MPL3115A2 is a MEMS pressure sensor that provides Altitude data to w...

[ [\$16.75] ]

Things you should know about this sensor:

- Uses the I^2^C interface
- Only one sensor can reside on the I^2^C bus
- Uses the I^2^C repeated start condition. Arduino supports this, check if you\'re using a different microcontroller.
- Typical pressure accuracy of ±0.05kPa
- Typical altitude accuracy of ±0.3m
- Typical temperature accuracy of ±3C
- 3.3V sensor - use inline logic level converters or 330 ohm resistors to limit 5V signals
- Here's the [datasheet](http://cdn.sparkfun.com/datasheets/Sensors/Pressure/MPL3115A2.pdf)
- Here\'s the [schematic](http://cdn.sparkfun.com/datasheets/Sensors/Pressure/MPL3115A2_breakout.pdf) for the breakout board

This sensor is ideal for environmental sensing, a weather station, or datalogging. It is a worthy replacement for the [BMP085](https://www.sparkfun.com/products/retired/9694) and is more sensitive than the [MPL115A1](https://www.sparkfun.com/products/9721).

### Suggested Reading

- [Read about I^2^C!](https://learn.sparkfun.com/tutorials/i2c)
- [Using 3.3V sensors with 5V systems](https://learn.sparkfun.com/tutorials/logic-levels)
- [Installing an Arduino library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [What are pull-up resistors?](https://learn.sparkfun.com/tutorials/pull-up-resistors)
- [Local Pressure vs Weather Station Pressure](https://ambientweather.wikispaces.com/Barometric+pressure+does+not+match+the+official+weather+station)

## Hooking It Up

Wiring up the MPL3115A2 pressure sensor is very easy! After [soldering the headers of your choice](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) on the board, you\'ll need to convert the logic between the 5V and the sensor using a [logic level converter](https://www.sparkfun.com/products/12009).

[![Fritzing Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/Arduino-Fritzing-mpl3115a2-altitude-pressure-sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/Arduino-Fritzing-mpl3115a2-altitude-pressure-sensor.jpg)

You\'ll need 5v and 3.3V for VCC, one for GND, and two data lines for I^2^C communication from your Arduino. You may also use the A4 and A5 pins on older Arduino Boards that do not have SDA and SCL broken out.

**Note:** This breakout board has built-in 1kΩ pull up resistors for I^2^C communications. If you\'re hooking up multiple I^2^C devices on the same bus, you may need to disable the other resistors on the bus.

**Note:** If you have a RedBoard Qwiic, there is an alternative to use the built-in logic level converter using the qwiic adapter and cable or jumpers that can be used to adjust the voltage level to 3.3V.\
\

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Qwiic Cable - Grove Adapter (100mm)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/7/5/15109-Qwiic_Cable_-_Grove_Adapter__150mm_-01.jpg)](https://www.sparkfun.com/qwiic-cable-grove-adapter-100mm.html)

### [Qwiic Cable - Grove Adapter (100mm)](https://www.sparkfun.com/qwiic-cable-grove-adapter-100mm.html) 

[ PRT-15109 ]

The Qwiic to Grove Adapter Cable allows interoperability between the SparkFun Qwiic Connect System and the I2C based Grove bo...

[ [\$1.95] ]

[![SparkFun Qwiic Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/5/1/14495-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-adapter.html)

### [SparkFun Qwiic Adapter](https://www.sparkfun.com/sparkfun-qwiic-adapter.html) 

[ DEV-14495 ]

The SparkFun Qwiic Adapter provides the perfect means to make any old I^2^C board into a Qwiic enabled board.

[ [\$1.60] ]

### Hookup Table

With respect to the logic level converter, the pin connections starting from LV1 are listed in the table below.

  MPL3115A2   Logic Level Converter *(Low Side)*   Logic Level Converter *(High Side)*   5V Arduino w/ Atmega328P
  ----------- ------------------------------------ ------------------------------------- --------------------------
  SCL         LV1                                  HV1                                   SCL *(or A5)*
  SDA         LV2                                  HV2                                   SDA*(or A4)*
  VCC         LV                                                                         3.3V
                                                   HV                                    5V
  GND         GND                                  GND                                   GND

**Note:** Not all microcontrollers use the same pin for SDA and SCL. If you are using a [different architecture that is not the Atmega328P](https://www.arduino.cc/en/reference/wire), make sure to edit the code accordingly if you use those pins instead.

## Arduino Code

The following Arduino example will get your sensor up and running quickly, and will show you current pressure in Pascals.

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

[Download library here](https://github.com/sparkfun/SparkFun_MPL3115A2_Breakout_Arduino_Library/archive/master.zip)

[![Arduino Example Sub Menu](https://cdn.sparkfun.com/assets/b/a/8/a/b/5265b106757b7fc14c8b4568.jpg)](https://cdn.sparkfun.com/assets/b/a/8/a/b/5265b106757b7fc14c8b4568.jpg)

*Load the Pressure example*

Once the library is installed, open Arduino, and expand the examples menu. You should see the MPL3115A2_Pressure sub-menu. Load the \"Pressure\" example onto the Arduino. [Open the serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at 9600bps. You will see the current barometric pressure and temperature in the room!

[![Arduino terminal output](https://cdn.sparkfun.com/assets/f/b/c/7/8/5265cbb9757b7f704d8b4569.jpg)](https://cdn.sparkfun.com/assets/f/b/c/7/8/5265cbb9757b7f704d8b4569.jpg)

*Pressure readings!*

Load the `BarometricHgInch` example for an example that coverts pressure from Pascals to inches of mercury, altimeter setting adjusted. This type of pressure reading is used in the USA on Wunderground for home weather stations and aircraft.

Load the `Altimeter` example for an example that coverts pressure to current altitude in feet (or meters).

### Explanation of Functions

The library and example code demonstrate the most popular functions supported by the MPL3115A2. Here is an explanation of all the available functions in the library:

- **myPressure.begin()** gets sensor on the I^2^C bus.
- **myPressure.readAltitude()** returns a float with meters above sea level. Ex: 1638.94
- **myPressure.readAltitudeFt()** returns a float with feet above sea level. Ex: 5376.68
- **myPressure.readPressure()** returns a float with barometric pressure in Pa. Ex: 83351.25
- **myPressure.readTemp()** returns a float with current temperature in Celsius. Ex: 23.37
- **myPressure.readTempF()** returns a float with current temperature in Fahrenheit. Ex: 73.96
- **myPressure.setModeBarometer()** puts the sensor into Pascal measurement mode.
- **myPressure.setModeAltimeter()** puts the sensor into altimetry mode.
- **myPressure.setModeStandy()** puts the sensor into Standby mode. Required when changing CTRL1 register.
- **myPressure.setModeActive()** starts taking measurements!
- **myPressure.setOversampleRate(byte)** sets the \# of samples from 1 to 128. See note below \*
- **myPressure.enableEventFlags()** sets the fundamental event flags. Required during setup.

When you call the readAltitude, readAltitudeFt, readPressure, or readTemp you will get a float with the sensor reading or an error code:

- 1638.94 is an example of a valid reading.
- -999 indicates that I2C timed out (512ms max). Check your connections.

[![Oversample settings table](https://cdn.sparkfun.com/assets/8/0/2/2/e/5265a68a757b7f1a4c8b4569.jpg)](https://cdn.sparkfun.com/assets/8/0/2/2/e/5265a68a757b7f1a4c8b4569.jpg)

*Oversample settings*

- **setOversampleRate(byte)** receives a value from 0 to 7. Check table 59 above. Allows the user to change sample rate from 1 to 128. Increasing the sample rate significantly decreases the noise of each reading but increases the amount of time to capture each reading. A oversample of 128 will decrease noise to 1.5Pa RMS but requires 512ms per reading. The datasheet recommends oversample of 128 for basic applications.

The MPL3115A2 has a large number of features. Checkout the [datasheet](http://cdn.sparkfun.com/datasheets/Sensors/Pressure/MPL3115A2.pdf) for more info. This library covers the fundamentals. Help us out! Please add or suggesting more features on the [MPL3115A2 github repo](https://github.com/sparkfun/MPL3115A2_Breakout).

## Pressure vs Altimeter Setting

If you grabbed a few pressure readings and became confused when you checked your local weather conditions, you\'re not alone. The absolute pressure that the MPL3115A2 pressure sensor outputs is not the same as what weather stations refer to as pressure. Weather stations report pressure in lots of different units:

- millimeters Mercury (mmHg)
- inches Mercury (inHg)
- millibars or hectopascals (hPa)
- pounds per square inch
- atmospheres (Atm)
- kilogram per centimeter
- inches of water

In barometer mode, the MPL3115A2 outputs pressure readings in Pascals. This is most closely related to millibars or hectopascals. But, why does the sensor not agree with the station around the corner? This is because many stations report pressure in a few [different formats](http://www.crh.noaa.gov/bou/awebphp/definitions_pressure.php). Have a look at all these numbers for the [Boulder/Denver area](http://www.crh.noaa.gov/bou/include/webpres.php?product=webpres.txt). The key is that your local weather station is probably reporting the *Altimeter setting*.

Thank you National Oceanic and Atmospheric Administration ([NOAA](http://www.noaa.gov/))! Did you know they\'re headquartered here in Boulder, CO?

- **Station pressure** - This is the pressure that is observed at a specific elevation and is the true barometric pressure of a location.
- **Altimeter setting** - This is the pressure reading most commonly heard in radio and television broadcasts. It is not the true barometric pressure at a station. Instead it is the pressure \"reduced\" to mean sea level using the temperature profile of the \"standard\" atmosphere, which is representative of average conditions over the United States at 40 degrees north latitude.
- **Mean sea level pressure** - This is the pressure reading most commonly used by meteorologists to track weather systems at the surface. Like the altimeter setting, it is a \"reduced\" pressure, which uses observed conditions rather than \"standard\" conditions to remove the effects of elevation from pressure readings.

The calculation to get from Pascals to \'Altimeter setting\' is a bit gnarly:

[![Alimeter setting formula](https://cdn.sparkfun.com/r/600-600/assets/2/3/d/c/8/5265adca757b7fe14b8b4568.jpg)](https://cdn.sparkfun.com/assets/2/3/d/c/8/5265adca757b7fe14b8b4568.jpg)

*Formula to convert Pascal pressure to Altimeter setting*

Grab the [full formula here](https://www.weather.gov/media/epz/wxcalc/altimeterSetting.pdf) and give this great [Altimeter setting calculator](https://www.weather.gov/epz/wxcalc_altimetersetting) a try. This formula relies on two things: knowing the current pressure in milibars and knowing the height above sea level that the pressure was read. We recommend you capture altitude using a local survey point or a [GPS receiver](https://www.sparkfun.com/categories/4).

If you installed the [MPL3115A2 library](https://github.com/sparkfun/MPL3115A2_Breakout/blob/master/library/MPL3115A2_Pressure.zip), you should also have the *BarometricHgInch* example sketch under the Examples-\>MPL3115A2_Pressure menu under the Arduino IDE. We didn\'t build this calculation into the library because it could potentially chew up a lot of RAM and code space calculating all the floating point math. But, if you\'re doing home weather station calculations, this should get you started.