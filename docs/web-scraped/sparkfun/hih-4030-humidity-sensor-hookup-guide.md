# Source: https://learn.sparkfun.com/tutorials/hih-4030-humidity-sensor-hookup-guide

## Introduction

The [SparkFun HIH-4030 Humidity Sensor Breakout](https://www.sparkfun.com/products/9569) measures **relative humidity (%RH)** from Honeywell\'s HIH-4030 humidity sensor. The breakout allows you to connect the analog output of the sensor directly to an ADC on a microcontroller.

[![SparkFun Humidity Sensor Breakout - HIH-4030](https://cdn.sparkfun.com/r/600-600/assets/parts/3/3/5/0/09569-02.jpg)](https://www.sparkfun.com/products/9569)

### [SparkFun Humidity Sensor Breakout - HIH-4030](https://www.sparkfun.com/products/9569) 

[ SEN-09569 ]

This is a breakout board for Honeywell\'s HIH-4030 humidity sensor. The HIH-4030 measures relative humidity (%RH) and delivers...

**Retired**

Voltage applied to the supply pins should be within 4-5.8 VDC, and optimally at 5V. The sensor will typically only consume about 200μA.

This tutorial serves as a introduction to the HIH-4030 and the SparkFun Humidity Sensor Breakout. It covers both the hardware and firmware requirements of the breakout to start receiving relative humidity (%RH) measurements as well as documenting example wiring, Arduino code and using the sensor in conjunction with a thermometer.

As we step through the Hookup Guide, you\'ll find it useful to have the HIH-4030 Datasheet on hand.

[HIH-4030 Datasheet](https://www.sparkfun.com/datasheets/Sensors/Weather/SEN-09569-HIH-4030-datasheet.pdf)

### Required Materials

To get the humidity sensor up and running, you\'ll need the following parts. Further in the tutorial, you\'ll learn how to incorporate a temperature sensor, specifically [SparkFun\'s Digital Temperature Sensor Breakout - TMP-102](https://www.sparkfun.com/products/11931), for properly determining relative humidity (%RH). Note that adding a temperature sensor is optional, but its use will be highlighted in this tutorial.

**Note:** As an alternative, you could also use the the Qwiic cables and the Qwiic TMP102 to easily connect without needing to solder or connect to the four pins.\
\

[![SparkFun Digital Temperature Sensor - TMP102 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/0/0/7/16304-SparkFun_Digital_Temperature_Sensor_-_TMP102__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-tmp102-qwiic.html)

### [SparkFun Digital Temperature Sensor - TMP102 (Qwiic)](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-tmp102-qwiic.html) 

[ SEN-16304 ]

The SparkFun TMP102 Qwiic is an easy-to-use digital temperature sensor equipped with a couple of Qwiic connectors for easy I2...

[ [\$8.23] ]

[![Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/1/14425-Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html)

### [Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-14425 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and a breadboard hookup...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Suggested Reading

Before getting started with the HIH-4030, you should ensure you are familiar with the following topics:

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

## Hardware Overview

The RH sensor uses a laser trimmed, thermoset polymer capacitive sensing element with on-chip integrated signal conditioning. The sensing element\'s multilayer construction provides excellent resistance to most application hazards such as condensation, dust, dirt, oils and common environmental chemicals.

### Protective Tape Removal

The HIH-4030 comes with a protective tape on the cover (sensing face). This tape is kept in place during our soldering process here at SparkFun. When you receive your HIH-4030 Breakout, you\'ll want to remove the protective tape.

[![HIH-4030 Tape Removal](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/HIH-4030_Humidity_Sensor-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/HIH-4030_Humidity_Sensor-03.jpg)

#### Protective Tape Removal

Reference: [Installation Instructions for the HIH-4030/4031 Humidity Sensors](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/HIH-4030_4031_Install_50022701-3-EN_Final_23Feb12.pdf)\
Useful tool to aid in this process: [ESD Safe Tweezers](https://www.sparkfun.com/products/10603)\
\

Use proper Electrostatic Discharge (ESD) protection

Use finger cots to ensure that no foreign debris falls into the filter, sensor cover or die

Remove protective tape according to the diagram below

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/Honeywell_HIH4030_TapeRemoval.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/Honeywell_HIH4030_TapeRemoval.png)

### Pinout

The three pin breakouts on the HIH-4030 Breakout board make it easy to measure relative humidity (%RH) as an analog voltage.

[![HIH-4030 Pinout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/HIH-4030_Humidity_Sensor-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/HIH-4030_Humidity_Sensor-04.jpg)

  Pin   Description
  ----- ---------------------
  GND   Ground
  OUT   Voltage Output
  5V    Supply Voltage (5V)

Voltage applied to the supply pins should be within 4-5.8VDC, optimally at 5V, making it perfect to power with your 5V / GND connections on your microcontroller shield like an Arduino or [SparkFun Redboard](https://www.sparkfun.com/products/12757). The data pin can be connected to an analog input of an Arduino, XBee, RaspberryPi, or any other IO device. The HIH-4030 has a low-power design. The sensor will typically only consume about 200μA.

#### Humidity Sensor Re-Conditioning

Humidity Sensors make use of a conductive polymer to measure relative humidity. If that polymer gets too dry (or over-saturated) the sensor won\'t function properly, but that can be reversed.

Any humidity sensors on our designs are put through a re-conditioning procedure to ensure that they keep their factory calibration. If you expose your sensor to a really dry environment for a prolonged period of time (or saturate it in a very humid environment) you may have to run it through the same process.

[Re-conditioning Humidity Sensors](https://www.sparkfun.com/news/1090)

[Build a Humidor Control Box](https://learn.sparkfun.com/tutorials/creating-a-humidor-control-box)

## Hardware Hookup

This product comes with the HIH-4030 soldered onto the breakout board. The pins of the 3-pin header are spaced by 0.1\".

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/HIH-4030_Humidity_Sensor-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/HIH-4030_Humidity_Sensor-02.jpg)

Before you can insert the HIH-4030 Breakout into a breadboard, you\'ll need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) either [wires](https://www.sparkfun.com/products/11375) or a 3-pin header to the GND, OUT, and 5V on-board connections. If you plan on breadboarding, we recommend [straight male headers](https://www.sparkfun.com/products/116). Here, [right angle headers](https://www.sparkfun.com/products/553) were used, which is another viable option.

[![HIH-4030 Breakout and Breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/HIH-4030_Humidity_Sensor-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/HIH-4030_Humidity_Sensor-05.jpg)

### Example Circuit with HIH-4030 Only

With the HIH-4030 Breakout, all you need is three wires between your microcontroller and the breakout board: **Power, Ground, and Analog Output**. This is a simplified circuit that should only be used to get your Humidity Sensor up and running. Here is an example hookup diagram demonstrating how to connect the board up to a SparkFun RedBoard:

[![Wiring Diagram HIH-4030](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/HIH4030_FritzingA.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/HIH4030_FritzingA.png)

### Example Circuit with TMP102 Temperature Sensor

Determining Relative Humidity (RH%) requires knowing an accurate temperature. The previous circuit example does not utilize this feature, therefore, it will be necessary to to use your HIH-4030 Breakout in conjunction with a Temperature Sensor. For this Hookup Guide, we have used the TMP102 Breakout.

[![SparkFun Digital Temperature Sensor Breakout - TMP102](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/9/3/13314-01a.jpg)](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-breakout-tmp102.html)

### [SparkFun Digital Temperature Sensor Breakout - TMP102](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-breakout-tmp102.html) 

[ SEN-13314 ]

The TMP102 is an easy-to-use digital temperature sensor from Texas Instruments. The TMP102 breakout allows you to easily inco...

[ [\$5.95] ]

The TMP102 is a digital sensor that communicates over I^2^C, has a resolution of 0.0625°C, and is accurate up to 0.5°C. There is no on-board voltage regulator, so supplied voltage should be between **1.4 to 3.6V**. **Do not hook up the TMP102 VCC to 5V.** You\'ll want to use 3.3V on your Arduino or SparkFun RedBoard for this connection. As an additional resource, refer to the [TMP102 datasheet](https://www.sparkfun.com/datasheets/Sensors/Temperature/tmp102.pdf).

You\'ll notice from the figure below, found on page three of the HIH-4030 sensor datasheet, the recommended operating temperature is between -40 and 85 °C (or -40 and 185 °F). If the operating zone lies outside either the recommended temperature or humidity extreme, the sensor is only specified to be accurate for 50 hours or less.

[![Operating Environment](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/HIH4030_OperatingEnvironment.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/HIH4030_OperatingEnvironment.png)

Since this is an I^2^C device, the connections you\'ll be most concerned with is the SDA (Data) and SCL (Clock) pins on either an Arduino or SparkFun RedBoard. Here is an example hookup diagram demonstrating how to connect the HIH-4030 Breakout with a TMP102 Digital Temperature Sensor board up to a SparkFun RedBoard:

[![Wiring Diagram HIH-4030 with TMP-102](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/HIH4030_FritzTemp.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/HIH4030_FritzTemp.png)

*Click the image for a closer look.*

## Using the SparkFun HIH-4030 Arduino Library

We\'ve written an Arduino library for the HIH-4030, which takes care of all your user specifications and calculating of formula found in the [datasheet](https://www.sparkfun.com/datasheets/Sensors/Weather/SEN-09569-HIH-4030-datasheet.pdf). Grab the most recent version of the library from our [SparkFun_HIH4030_Arduino_Library GitHub repository](https://github.com/sparkfun/SparkFun_HIH4030_Arduino_Library):

[Download the SparkFun HIH-4030 Arduino Library](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/SparkFun_HIH4030_Library.zip)

If you need any help with the installation process, check out the [How to Install an Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library). If you download the library\'s ZIP file, you can use Arduino\'s \"Add ZIP Library\...\" feature to install the source and example files.

[![Adding Library](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/IncludingLibrary.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/IncludingLibrary.png)

### Using the HIH4030_HumiditySensor_Example

Once you\'ve downloaded the library, open the `HIH4030_HumiditySensor_Example` by navigating to **File** \> **Examples** \> **SparkFun Humidity Sensor Breakout - HIH4030** \> **HIH4030_HumiditySensor_Example**:

[![Open Example Program](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/openExample.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/openExample.png)

You\'ll also want to make sure your board and port are correctly set in the Arduino IDE window before uploading the code:

[![Board, Port and Upload](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/BoardUploadSettings.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/BoardUploadSettings.gif)

Once the upload is complete, you can click over to the **Serial Monitor**. Make sure the baud rate is set to 9600 bps, and you should begin to see the Tempearture, Sensor Voltage, Relative Humidity and True Relative Humidity scroll across the screen:

[![Serial Monitor Output](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/SerialMonitor.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/SerialMonitor.gif)

### Customizing Settings in Code

#### Initialization

To begin, make sure you include the `SparkFun_HIH4030.h` library. If using a temperature sensor, you\'ll need to include `Wire.h` the Arduino I^2^C library:

    language:c
    #include <SparkFunDS1307RTC.h>
    #include <Wire.h>

Both the [SparkFun Digital Temperature Sensor Breakout - TMP102](https://www.sparkfun.com/products/11931) and the [SparkFun Infrared Temperature Breakout - TMP006](https://www.sparkfun.com/products/11859) would utilize the Wire.h library as they communicate via I^2^C.

#### Temperature Sensor Settings

The code by default is using a static value for the temperature reading.

    language:c
    // Are You Using a Temperature Sensor? 1 = YES / 0 = NO
    int tempSensor = 0;

You can change the `temp` variable from 25 degrees Celsius to any desired value to see how it affects the Relative Humidity (RH%).

[![Static Temperature Value](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/StaticTemp.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/StaticTemp.png)

It\'s important to remember that **True Relative Humidity (RH%) requires a known temperature for accurate measurement**. As an example, the previous section, *Hardware Hookup*, demonstrated how to wire both the [SparkFun Humidity Sensor Breakout - HIH-4030](https://www.sparkfun.com/products/9569) and [Digital Temperature Sensor Breakout - TMP102](https://www.sparkfun.com/products/11931). However, you can also use other Temperature Sensors available on the SparkFun storefront: [One-Wire Ambient Temperature Sensor - MAX31820](https://www.sparkfun.com/products/14049), [Temperature Sensor - TMP36](https://www.sparkfun.com/products/10988), [One Wire Digital Temperature Sensor - DS18B20](https://www.sparkfun.com/products/245), [SparkFun Infrared Temperature Breakout - TMP006](https://www.sparkfun.com/products/11859).

If you are utilizing a Temperature Sensor, you\'ll want to modify the following code from the default 0 to a 1:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/ChangeTempSensor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/ChangeTempSensor.png)

#### Humidity Sensor Settings

Two things that need to be defined for the `SparkFun_HIH4030 Library` is the Analog I/O Pin the HIH-4030 Sensor OUT is connected to and the voltage being supplied to the HIH-4030 Sensor. If your setup reflects the *Hardware Hookup* section, you can leave the values as is.

    language:c
    // Analog IO Pin Connected to OUT
    #define HIH4030_OUT A0

    // Supply Voltage - Typically 5 V
    #define HIH4030_SUPPLY 5

### Looking Inside the SparkFun_HIH4030 Library

#### vout( ) function

Since the output of the HIH-4030 Humidity Sensor is nearly linear, the `analogRead()` function is used and mapped to the correct range. This is where the value you defined for the Supply Voltage in your `HIH4030_HumiditySensor_Example` code comes into play.

    language:cpp
    // Read value from the sensor and convert to voltage value
    float HIH4030::vout() 

#### getSensorRH( ) function

From the [HIH-4030 Datasheet](https://www.sparkfun.com/datasheets/Sensors/Weather/SEN-09569-HIH-4030-datasheet.pdf), a Voltage output equation is given on page 2.

[![VOUT Equation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/Equation1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/Equation1.png)

With the previous `vout()` function and defined supply voltage, sensor RH can be calculated.

    language:cpp
    // Convert sensor reading into Relative Humidity (RH%) 
    //  using equation from Datasheet
    // VOUT = (VSUPPLY)(0.0062(SENSOR RH) + 0.16), 
    //  typical at 25 degrees Celsius

    float HIH4030::getSensorRH() 

#### getTrueRH( ) function

The True Relative Humidity euqation is also given on page 2 of the [HIH-4030 Datasheet](https://www.sparkfun.com/datasheets/Sensors/Weather/SEN-09569-HIH-4030-datasheet.pdf) which includes temperature compensation.

[![True RH Equation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/1/Equation2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/1/Equation2.png)

Aforementioned, True Relative Humidity required a known temperature for accurate measurement. The `getTrueRH(float temperature)` function will take the value of either your static temperature or sensor measurement, whichever is applicable, and calculate True RH.

    language:cpp
    // Get True Relative Humidity (RH%) compensated 
    //  with Static Temperature or Measured Temperature
    // TRUE RH = (SENSOR RH)/(1.0546 - 0.00216T), T in degrees Celsius

    float HIH4030::getTrueRH(float temperature)