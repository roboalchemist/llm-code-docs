# Source: https://learn.sparkfun.com/tutorials/si7021-humidity-and-temperature-sensor-hookup-guide

## Introduction

The [Si7021](https://www.sparkfun.com/products/13763) is a low-cost, easy to use, highly accurate, digital temperature and humidity sensor. All you need is two lines for I^2^C communication, and you'll have relative humidity readings and accurate temperature readings as well! This sensor is ideal for environmental sensing and data logging, perfect for a weather station or humidor control system.

[![SparkFun Humidity and Temperature Sensor Breakout - Si7021](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/3/0/8/13763-01a.jpg)](https://www.sparkfun.com/sparkfun-humidity-and-temperature-sensor-breakout-si7021.html)

### [SparkFun Humidity and Temperature Sensor Breakout - Si7021](https://www.sparkfun.com/sparkfun-humidity-and-temperature-sensor-breakout-si7021.html) 

[ SEN-13763 ]

The Si7021 is a low-cost, easy-to-use, highly accurate, digital humidity and temperature sensor. This sensor is ideal for env...

**Retired**

The Si7021 also comes equipped with a hydrophobic PTFE filter covering the inlet on the sensor. This filter blocks contaminants but allows water vapor to pass through, keeping your sensor safe from water damage while still proving accurate sensor readings.

### Required Materials

To follow along with this hookup guide, you will need the following:

### Suggested Reading

Before embarking upon this tutorial, you may find the following links useful:

[](https://learn.sparkfun.com/tutorials/pull-up-resistors)

### Pull-up Resistors 

A quick introduction to pull-up resistors - whey they\'re important, and how/when to use them.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Board Overview 

Let\'s go over the Si7021 Breakout in detail.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/13763-02a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/13763-02a.jpg)

#### Si7021 Details:

- Uses the I^2^C interface
- Typical humidity accuracy of ±2%
- Typical temperature accuracy of ±0.3C
- Operates from 0 to 100% humidity but this sensor isn't recommended for harsh environments where it could come in contact with water (such as rain)
- 3.3V sensor - use inline [logic level converters](https://www.sparkfun.com/products/12009) or 10kΩ resistors to limit 5V signals
- Only one Si7021 sensor can reside on the I^2^C bus at a time

### Pull-up Resistors

This breakout board has built-in 4.7KΩ pull up resistors for I^2^C communications. If you\'re hooking up multiple I^2^C devices on the same bus, you may want to disable/enable the pull-up resistors for one or more boards. On the Si7021, the pull-ups are enabled by default. To disable them, simply use some [solder wick](https://www.sparkfun.com/products/8775) to remove the solder on the jumper labeled **PU**. This will disconnect the resistors from VCC and from the I2C bus.

### PTFE Filter

The tiny white cover on the IC is known as a Polytetrafluorethylene (PTFE) Membrane Filter. It keeps moisture out but allows humidity in. This filter is very low-profile, hydrophobic and oleophobic, and excludes particulates down to 0.35 microns in size.

**Heads up!** Do not remove this white filter, mistaking it for some IC tape that was left on by mistake. Removing the filter may result in a shortened life span of the device or failure in highly humid areas.

From the Si7021 [datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/Si7021Datasheet.pdf):

\"Because the sensor operates on the principal of measuring a change in capacitance, any changes to the dielectric constant of the polymer film will be detected as a change in relative humidity. Therefore, it is important to minimize the probability of contaminants coming into contact with the sensor. Dust and other particles as well as liquids can affect the RH reading.\"

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/filter.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/filter.png)

*Image courtesy of Silicon Labs [datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/Si7021Datasheet.pdf)*

## Hooking It Up

Wiring up the Si7021 is very easy! We recommend [soldering](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) four [male headers](https://www.sparkfun.com/products/116) to the breakout board. You can also solder [wires](https://www.sparkfun.com/products/11375) if your application needs.

### Power

This board runs at **3.3V**. Be sure to power the board from the 3.3V pin! Because I^2^C is an open drain signal, there\'s no need to worry about level shifting the signal; the 3.3V signal will be adequate to communicate with the Arduino and the signal will never reach a dangerous level for the pins on the Si7021.

### Connections: Breakout to Arduino

#### Method 1

There are two ways to connect an Si7021 to an Arduino. The first is using pins A4 and A5 on classic Arduino boards. This breakout was designed using our standard I^2^C pinout, allowing the sensor to be connected directly to an Arduino without using a breadboard or wires.

- GND → A2
- VCC → A3
- SDA → A4
- SCL → A5

This would look like the following:

[![Fritzing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/7/13763-updatedfritzing.jpeg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/13763-updatedfritzing.jpeg)

**Heads up!** This method will only work with Arduino boards that run at **3.3V** such as the [3.3V Arduino Pro](https://www.sparkfun.com/products/10914), the [3.3V Arduino Pro Mini](https://www.sparkfun.com/products/11114), the [SparkFun SAMD21 Mini Breakout](https://www.sparkfun.com/products/13664) and the [SparkFun SAMD21 Dev Breakout](https://www.sparkfun.com/products/13672).\
\
Also, if using this wiring scheme, be sure to **assign pins A2 and A3 as GND and VCC**, respectively, in your code.\
\
If you need to use this device with a 5V microcontoller, you will need to use a [Logic Level Converter](https://www.sparkfun.com/products/12009).

#### Method 2

This method is for those with newer model Arduino boards that have the SDA and SCL lines broken out. We\'ll be hooking up VCC and GND to the normal power pins and two data lines for I^2^C communication. Connect the SDA and SCL lines directly to the SDA and SCL lines broken out on the Arduino headers.

- VCC → 3.3V
- GND → GND
- SDA → SDA
- SCL → SCL

This would look something like the following:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/7/Si7021Fritzing2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/Si7021Fritzing2.png)

## Si7021 Library and Example Code 

To get started, use the example code and library files below.

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

You can download the library from the link below. Check out our [Installing an Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) for more help.

[Si7021 Arduino Library](https://github.com/sparkfun/SparkFun_Si7021_Arduino_Library)

Once the library is installed, open Arduino, and expand the examples menu. You should see the Si7021 example.

[![menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/7/Si7021Menu.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/Si7021Menu.png)

*The examples menu expanded to show Si7021 example*

    language:c
    /******************************************************************************
      SparkFun Si7021 Breakout Example
      Joel Bartlett @ SparkFun Electronics
      Original Creation Date: May 18, 2015
      Updated May 4, 2016
      This sketch prints the temperature and humidity the Serial port.

      The library used in this example can be found here:
      https://github.com/sparkfun/Si7021_Breakout/tree/master/Libraries

      Hardware Connections:
          HTU21D ------------- Photon
          (-) ------------------- GND
          (+) ------------------- 3.3V (VCC)
           CL ------------------- D1/SCL
           DA ------------------- D0/SDA

      Development environment specifics:
        IDE: Particle Dev
        Hardware Platform: SparkFun RedBoard
                           Arduino IDE 1.6.5

      This code is beerware; if you see me (or any other SparkFun
      employee) at the local, and you've found our code helpful,
      please buy us a round!
      Distributed as-is; no warranty is given.
    *******************************************************************************/
    #include "SparkFun_Si7021_Breakout_Library.h"
    #include <Wire.h>

    float humidity = 0;
    float tempf = 0;

    int power = A3;
    int GND = A2;

    //Create Instance of HTU21D or SI7021 temp and humidity sensor and MPL3115A2 barrometric sensor
    Weather sensor;

    //---------------------------------------------------------------
    void setup()
    
    //---------------------------------------------------------------
    void loop()
    
    //---------------------------------------------------------------
    void getWeather()
    
    //---------------------------------------------------------------
    void printInfo()
    

Once you\'ve uploaded the code, connect using this [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics) to see the output.

### Si7021 Functions:

`Weather::getRH()` - Returns current Relative Humidity measurement.

`Weather::readTemp()` - Returns temperature in Celsius from previous RH measurement.

`Weather::getTemp()` - Returns current temp in Celsius.

`Weather::readTempF()` - Returns temperature in Fahrenheit from previous RH measurement.

`Weather::getTempF()` - Returns current temp in Fahrenheit.

`Weather::changeResolution()` - Allows the user to change the humidity and temperature resolution. The vast majority of users do not need to change the resolution. By default the sensor will be in its highest resolution settings. This function is useful if you need to decrease the amount of time between readings or to save power. See the [datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/Si7021Datasheet.pdf) for more information. As an example, to change the resolution to 11 bit RH and 11 bit temperature, you would call myHumidity.SetResolution(0b10000001); to set bit 7 and bit 0.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/7/resolution.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/7/resolution.png)

*Resolution table can be found on page 25 of the datasheet.*