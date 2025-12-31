# Source: https://learn.sparkfun.com/tutorials/arduino-weather-shield-hookup-guide-v12

## Introduction

**Heads up!** This is for the Arduino Weather Shield v12 \[DEV-13956\] that uses the Si7021. If you are looking at the older version of the weather shield, you should check out the [older tutorial for DEV-12081](https://learn.sparkfun.com/tutorials/weather-shield-hookup-guide) that uses the HTU21D.

**Updated Content:** This guide was updated on 7/5/23.

- The *Weather Station* and *Weather Station with GPS* firmware were modified to utilize our new **SparkFun Weather Meter Kit** Arduino library
- A few of the parts and instructions, were also updated to account for any retired components, outdated information, etc.
- Please note, this shield is currently [**not**] compatible with the new **Arduino Uno (R4)**. There is an issue with the values returned from the Arduino libraries for the I^2^C sensors *(temperature, humidity, and pressure)*.

**Library Versions:**

While this tutorial and its example code were recently updated, this was before the [lastest release of the SparkFun Si7021 Arduino library](https://github.com/sparkfun/SparkFun_Si7021_Arduino_Library/releases/tag/v2.0.0). The latest release is not backwards compatible and will [create compilation issues](https://github.com/sparkfun/Weather_Shield/issues/36) with the existing example code for this hookup guide. Therefore, we recommend users only utilize these specific version of these libraries, until we have a more permanent fix:

- SparkFun Si7021 Arduino Library **v1.0.5**
- SparkFun External MPL3115A2 Arduino Library **v1.2.4**

The [Arduino Weather Shield](https://www.sparkfun.com/products/13956) from SparkFun is an easy-to-use Arduino shield that grants you access to barometric pressure, relative humidity, luminosity, and temperature. There are also connections to optional sensors such as wind speed/direction, rain gauge, and GPS for location and super accurate timing.

[![SparkFun Weather Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/6/6/5/13956-01.jpg)](https://www.sparkfun.com/sparkfun-weather-shield.html)

### [SparkFun Weather Shield](https://www.sparkfun.com/sparkfun-weather-shield.html) 

[ DEV-13956 ]

The SparkFun Weather Shield is an easy-to-use Arduino shield that grants you access to barometric pressure, relative humidity...

[ [\$42.95] ]

Things you should know about this shield:

- Uses the [Si7021](https://www.sparkfun.com/products/12064) sensor, [MPL3115A2 barometric pressure sensor](https://www.sparkfun.com/products/11084), and [ALS-PT19 light sensor](https://www.sparkfun.com/products/12566).
- Has a 6-pin JST connector for the [GP-735 compact GPS module](https://www.sparkfun.com/products/13670)
  - The Weather shield is not compatible with the [EM-506](https://www.sparkfun.com/products/12751) or [EM-506N5](https://www.sparkfun.com/products/19629) GPS receivers. The shield does not provide enough power for those GPS modules.
- Has optional [RJ11 connector](https://www.sparkfun.com/products/132) footprints to connect the [SparkFun weather meter kit](https://www.sparkfun.com/products/8942)
- Weather shield can operate from **3V to 10V** and has built in voltage regulators and signal translators
  - When utilized with the [Weather Meter Kit](https://www.sparkfun.com/products/8942), the shield must be used with a 5V board (i.e. RedBoard, Arduino Uno (R3), etc.) for compatibility with the wind vane data.
  - The new Arduino Uno **(R4)** is not compatible with the Arduino libraries of the I^2^C sensors and is not recommended to use with the shield.
- Typical humidity accuracy of ±2%
- Typical pressure accuracy of ±50Pa
- Typical temperature accuracy of ±0.3C

### Required Materials

**Compatibility Issue:** The Arduino libraries of the I^2^C sensors on this shield are [**NOT**] compatible with the [**Arduino Uno (R4)**]. Please, use the Arduino Uno (R3) or the Redboard as suggested below.

To get up and running with the Weather Shield you\'ll need the following parts:

- [Arduino Uno (R3)](https://www.sparkfun.com/products/11021), [RedBoard](https://www.sparkfun.com/products/18158), or other compatible board
  - Compatible USB cable
- [Arduino Stackable Headers](https://www.sparkfun.com/products/11417)
- [Soldering Tools](https://www.sparkfun.com/categories/49)

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![Arduino Stackable Header Kit - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/7/2/1/6/11417-01a.jpg)](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html)

### [Arduino Stackable Header Kit - R3](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html) 

[ PRT-11417 ]

These headers are made to work with the Arduino Uno R3, Leonardo and new Arduino boards going forward. They are the perfect h...

[ [\$2.75] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![USB Cable A to B - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/7/00512-USB_Cable_A_to_B_-_6_Foot-01.jpg)](https://www.sparkfun.com/usb-cable-a-to-b-6-foot.html)

### [USB Cable A to B - 6 Foot](https://www.sparkfun.com/usb-cable-a-to-b-6-foot.html) 

[ CAB-00512 ]

This is a standard issue USB 2.0 cable. This is the most common A to B Male/Male type peripheral cable, the kind that\'s usual...

[ [\$5.50] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Chip Quik No-Clean Flux Pen - 10mL](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/5/14579-Chip_Quik_No-Clean_Flux_Pen_-_10mL-01.jpg)](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html)

### [Chip Quik No-Clean Flux Pen - 10mL](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html) 

[ TOL-14579 ]

This 10mL no-clean flux pen from Chip Quik is great for all of your solder, de-solder, rework, and reflow purposes!

[ [\$8.50] ]

#### Related Accessories

- [GP-735 GPS Module](https://www.sparkfun.com/products/13670) and ~~[1.75\" mating cable](https://www.sparkfun.com/products/574)~~
  - The shorter 1.75\" JST cable has been retired; however, our [1ft. 6-pin JST cable](https://www.sparkfun.com/products/9123) is still available
- Two [RJ11 6-pin Connectors](https://www.sparkfun.com/products/132)
- [Weather Meter Kit](https://www.sparkfun.com/products/8942)

[![Weather Meter Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/5/3/9/15901-Weather_Meter-02.jpg)](https://www.sparkfun.com/weather-meter-kit.html)

### [Weather Meter Kit](https://www.sparkfun.com/weather-meter-kit.html) 

[ SEN-15901 ]

Whether you are measuring wind speed, direction or rain, this is the Weather Meter for you.

[ [\$79.95] ]

[![GPS Receiver - GP-735 (56 Channel)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/1/3/13670-01a.jpg)](https://www.sparkfun.com/gps-receiver-gp-735-56-channel.html)

### [GPS Receiver - GP-735 (56 Channel)](https://www.sparkfun.com/gps-receiver-gp-735-56-channel.html) 

[ GPS-13670 ]

The GP-735 is a slim, ultra-high performance, easy to use GPS smart antenna receiver. With -162dBm tracking sensitivity and o...

[ [\$50.95] ]

[![RJ11 6-Pin Connector](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/00132-01.jpg)](https://www.sparkfun.com/rj11-6-pin-connector.html)

### [RJ11 6-Pin Connector](https://www.sparkfun.com/rj11-6-pin-connector.html) 

[ PRT-00132 ]

Through-hole RJ11 socket with PCB mounting posts. 6-pin connection - housing accepts common telephone connectors/wiring. I...

[ [\$1.75] ]

[![JST SH Jumper 6 Wire - 1 Foot (EM-401 and EM-406)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/3/7/09123-03-L.jpg)](https://www.sparkfun.com/jst-sh-jumper-6-wire-1-foot-em-401-and-em-406.html)

### [JST SH Jumper 6 Wire - 1 Foot (EM-401 and EM-406)](https://www.sparkfun.com/jst-sh-jumper-6-wire-1-foot-em-401-and-em-406.html) 

[ GPS-09123 ]

This is a 1 foot long JST SH communication cable which can be cut and hacked to your needs. Ideal if you have a UAV project w...

[\$3.95] [ [\$1.48] ]

### Suggested Reading

If you are unfamiliar with any of the concepts below, we suggest checking out these tutorials.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/arduino-shields-v2)

### Arduino Shields v2 

An update to our classic Arduino Shields Tutorial! All things Arduino shields. What they are and how to assemble them.

Check out our hookup guides for more information about the temperature/humidity and pressure sensors on the shield. If you intend to collect wind and rain data, assembly instructions for the [Weather Meter Kit](https://www.sparkfun.com/products/8942) can be found in our Weather Meter Assembly Guide.

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/mpl3115a2-pressure-sensor-hookup-guide)

### MPL3115A2 Pressure Sensor Hookup Guide 

Getting started with the MPL3115A2 Pressure Sensor.

[](https://learn.sparkfun.com/tutorials/si7021-humidity-and-temperature-sensor-hookup-guide)

### Si7021 Humidity and Temperature Sensor Hookup Guide 

The Si7021 humidity and temperature sensor is an easy to use, digital, low-cost sensor to aid you in all your environment sensing needs.

[](https://learn.sparkfun.com/tutorials/weather-meter-hookup-guide)

### Weather Meter Hookup Guide 

How to assemble your very own weather meter!

To understand how the libraries of the associated sensors work, we recommend the following tutorials.

[](https://learn.sparkfun.com/tutorials/pull-up-resistors)

### Pull-up Resistors 

A quick introduction to pull-up resistors - whey they\'re important, and how/when to use them.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino)

### Processor Interrupts with Arduino 

What is an interrupt? In a nutshell, there is a method by which a processor can execute its normal program while continuously monitoring for some kind of event, or interrupt. There are two types of interrupts: hardware and software interrupts. For the purposes of this tutorial, we will focus on hardware interrupts.

## Hardware Assembly

**Note:** Users who are unfamiliar with Arduino shields or soldering, should review the following tutorials:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/arduino-shields-v2)

### Arduino Shields v2 

An update to our classic Arduino Shields Tutorial! All things Arduino shields. What they are and how to assemble them.

[Solder the stackable headers](https://learn.sparkfun.com/tutorials/arduino-shields-v2/installing-headers-assembly) onto the shield, and insert the shield into your Arduino. You are welcome to solder in the RJ11 connectors to the top of the board as well. If you have the [GP-735 GPS module](https://www.sparkfun.com/products/13670), don\'t worry about attaching it at this time, we\'ll get to GPS later.

[![Weather shield with wind and rain meter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/6/Arduino_Weather_Shield3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/Arduino_Weather_Shield3.jpg)

*Shield on a [RedBoard](https://www.sparkfun.com/products/11575) with optional weather meter (\'W\'ind and \'R\'ain cables) and GPS attached*

## Software Overview

**Note:** This tutorial assumes you are using the latest version of the Arduino IDE on your desktop and that you have installed the necessary board files and drivers for your development board. If this is your first time using Arduino, please review the following tutorials.\
\

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

### Firmware for Examples

All the example code for this tutorial, can be downloaded the [GitHub Repository](https://github.com/sparkfun/Weather_Shield) of the Weather shield:

[Weather Shield Firmware](https://github.com/sparkfun/Weather_Shield/tree/master/Firmware)

### Arduino Libraries

To utilize the example firmware, users will need to install and configure the Arduino libraries for the following components.

#### On Board Sensors

The firmware examples below rely on the SparkFun [Si7021](https://github.com/sparkfun/SparkFun_Si7021_Arduino_Library) and [MPL3115A2](https://github.com/sparkfun/SparkFun_MPL3115A2_Breakout_Arduino_Library) Arduino libraries. These libraries can be installed through the Arduino Library Manager. Search for **SparkFun MPL3115** and **SparkFun Si7021** to install the latest version. The libraries can also be manually downloaded from their GitHub repository:

- [SparkFun Si7021 Arduino Library](https://github.com/sparkfun/SparkFun_Si7021_Arduino_Library)
- [SparkFun External MPL3115A2 Arduino Library](https://github.com/sparkfun/SparkFun_MPL3115A2_Breakout_Arduino_Library)

or utilize the buttons below:

[Download the Si7021 Arduino Library](https://github.com/sparkfun/SparkFun_Si7021_Arduino_Library/archive/refs/heads/master.zip) [Download the MPL3115A2 Arduino Library](https://github.com/sparkfun/SparkFun_MPL3115A2_Breakout_Arduino_Library/archive/refs/heads/master.zip)

**Library Versions:** This tutorial and its example code were recently updated; however, this was before the [lastest release of the SparkFun Si7021 Arduino library](https://github.com/sparkfun/SparkFun_Si7021_Arduino_Library/releases/tag/v2.0.0). This latest release is not backwards compatible and will [create compilation issues](https://github.com/sparkfun/Weather_Shield/issues/36) with the existing example code for this hookup guide. Therefore, we recommend users only utilize these specific version of these libraries, until we have a more permanent fix:

- SparkFun Si7021 Arduino Library **v1.0.5**
- SparkFun External MPL3115A2 Arduino Library **v1.2.4**

For more details on these sensors and their Arduino libraries, please refer to the hookup guides of their breakout boards:

[](https://learn.sparkfun.com/tutorials/mpl3115a2-pressure-sensor-hookup-guide)

### MPL3115A2 Pressure Sensor Hookup Guide 

Getting started with the MPL3115A2 Pressure Sensor.

[](https://learn.sparkfun.com/tutorials/si7021-humidity-and-temperature-sensor-hookup-guide)

### Si7021 Humidity and Temperature Sensor Hookup Guide 

The Si7021 humidity and temperature sensor is an easy to use, digital, low-cost sensor to aid you in all your environment sensing needs.

#### Weather Meter Kit

We\'ve written an Arduino library for users to easily setup and read data from the [SparkFun Weather Meter Kit](https://www.sparkfun.com/products/15901). The library can be installed through the Arduino Library Manager; search for **SparkFun Weather Meter Kit** to install the latest version. Users can also manually download the library from the [GitHub repository](https://github.com/sparkfun/SparkFun_Weather_Meter_Kit_Arduino_Library) or by clicking the button below:

[Download the SparkFun Weather Meter Kit Arduino Library](https://github.com/sparkfun/SparkFun_Weather_Meter_Kit_Arduino_Library/archive/refs/heads/main.zip)

**[Configuration]**

The SparkFun Weather Meter Kit Arduino library was originally written to be used with the [ESP32 MicroMod Processor](https://www.sparkfun.com/products/16781) and [MicroMod Weather Carrier board](https://www.sparkfun.com/products/16794). Therefore, it assumes certain electrical and microcontroller constraints when reading the wind vane direction. To utilize this library with this tutorial, users will need to make the following modifications:

- In the [`SparkFun_Weather_Meter_Kit_Arduino_Library.cpp`](https://github.com/sparkfun/SparkFun_Weather_Meter_Kit_Arduino_Library/blob/main/src/SparkFun_Weather_Meter_Kit_Arduino_Library.cpp) file of the library (located in the `src` folder), users will need to modify the file by commenting out [lines 26-41](https://github.com/sparkfun/SparkFun_Weather_Meter_Kit_Arduino_Library/blob/main/src/SparkFun_Weather_Meter_Kit_Arduino_Library.cpp#L26-L41) and enabling [lines 45-60](https://github.com/sparkfun/SparkFun_Weather_Meter_Kit_Arduino_Library/blob/main/src/SparkFun_Weather_Meter_Kit_Arduino_Library.cpp#L45-L60). This modifies the expected ADC values for the wind vane direction.

- The library assumes that a 12-bit ADC is connected to the weather vane. This can be modified through the library for boards like the Arduino Uno or RedBoard, which have a 10-bit ADC.

  - In the `setup()` loop, specify the ADC resolution; where `<ADC resolution>` should be an integer value of the microcontroller\'s ADC resolution in bits:

        setADCResolutionBits(<ADC resolution>);

- Users will also need to declare the electrical connections from the Weather shield to the sensors of Weather Meter Kit

      const byte WSPEED = 3;
      const byte RAIN = 2;
      const byte WDIR = A0;

#### GPS Module

In order to interpret the NMEA sentences from the GPS module, the firmware below relies on the [TinyGPSPlus](https://github.com/mikalhart/TinyGPSPlus) Arduino library, written by [Mikal Hart](https://github.com/mikalhart). The library can be installed through the Arduino Library Manager; search for **TinyGPSPlus** to install the latest version. Users can also manually download the library from the [GitHub repository](https://github.com/mikalhart/TinyGPSPlus) or by clicking the button below:

[Download the TinyGPSPlus Arduino Library](https://github.com/mikalhart/TinyGPSPlus/archive/refs/heads/master.zip)

For more details about the TinyGPSPlus Arduino library, please refer this blog post on [Arduiniana](http://arduiniana.org/libraries/tinygpsplus/).

**[Configuration]**

When the switch on the Weather shield toggled to [SW-UART], the **TinyGPSPlus** Arduino library will need to utilize the **SoftwareSerial** Arduino library. In order to parse the data, users will need to declare the electrical connections from the Weather shield to the GPS module.

- When the switch is toggled to [SW-UART], the RX and TX pins of the GP-735 GPS module are:

      language:c
      static const int RXPin = 5, TXPin = 4;

  ::: 
  **Note:** When the switch is toggled to [HW-UART], the RX and TX pins of the GP-735 GPS module are:

  ``` 
  Copy Codestatic const int RXPin = 0, TXPin = 1;
  ```
  :::

Users will also need to declare the baud rate of the GP-735 GPS module.

    language:c
    static const uint32_t GPSBaud = 9600;

In the firmware, users will need to include and create an instance for the the **SoftwareSerial** Arduino library. Then, the baud rate will need be configured in the `setup()` loop for the GPS module:

- language:c
      #include <SoftwareSerial.h>       //Needed for GPS
      SoftwareSerial ss(RXPin, TXPin);

- language:c
      ss.begin(GPSBaud);

## Example Firmware - Basic

Before uploading code to your Arduino with the Weather Shield attached, make sure the GPS UART switch is in the [SW-UART] position. Having the switch in the opposite position connects the GPS lines to the USB lines and may cause errors while uploading.

[![switch](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/gpsSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/gpsSwitch.jpg)

Open the `Weather_Shield_Basic_V12.ino` sketch from the `Firmware` folder or copy and paste the code below into the Arduino IDE:

    language:c
    /*
     Weather Shield Example
     By: Nathan Seidle
     SparkFun Electronics
     Date: June 10th, 2016
     License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

     This example prints the current humidity, air pressure, temperature and light levels.

     The weather shield is capable of a lot. Be sure to checkout the other more advanced examples for creating
     your own weather station.

     Updated by Joel Bartlett
     03/02/2017
     Removed HTU21D code and replaced with Si7021
     */

    #include <Wire.h> //I2C needed for sensors
    #include "SparkFunMPL3115A2.h" //Pressure sensor - Search "SparkFun MPL3115" and install from Library Manager
    #include "SparkFun_Si7021_Breakout_Library.h" //Humidity sensor - Search "SparkFun Si7021" and install from Library Manager

    MPL3115A2 myPressure; //Create an instance of the pressure sensor
    Weather myHumidity;//Create an instance of the humidity sensor

    //Hardware pin definitions
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    const byte STAT_BLUE = 7;
    const byte STAT_GREEN = 8;

    const byte REFERENCE_3V3 = A3;
    const byte LIGHT = A1;
    const byte BATT = A2;

    //Global Variables
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    long lastSecond; //The millis counter to see when a second rolls by

    void setup()
    

    void loop()
    
        else
        

        digitalWrite(STAT_BLUE, LOW); //Turn off stat LED
      }

      delay(100);
    }

    //Returns the voltage of the light sensor based on the 3.3V rail
    //This allows us to ignore what VCC might be (an Arduino plugged into USB has VCC of 4.5 to 5.2V)
    float get_light_level()
    

    //Returns the voltage of the raw pin based on the 3.3V rail
    //This allows us to ignore what VCC might be (an Arduino plugged into USB has VCC of 4.5 to 5.2V)
    //Battery level is connected to the RAW pin on Arduino and is fed through two 5% resistors:
    //3.9K on the high side (R1), and 1K on the low side (R2)
    float get_battery_level()
    

Open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics). You should see the following output:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/terminal.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/terminal.png)

Put your hand over the small clear device labeled \'Light\', and watch the light level change to 0. Blow lightly on the humidity sensor, and watch the humidity change.

## Example Firmware - Weather Station

For the more adventurous, check out the `Weather_Shield_Weather_Station_V12.ino` sketch. This code demonstrates shield\'s capabilities to collect weather data, when a [weather meter kit](https://www.sparkfun.com/products/8942) is connected:

    language:c
    /*
      Weather Shield Example
      By: Nathan Seidle
      SparkFun Electronics
      Date: November 16th, 2013
      License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

      Much of this is based on Mike Grusin's USB Weather Board code: https://www.sparkfun.com/products/10586

      This is a more advanced example of how to utilize every aspect of the weather shield. See the basic
      example if you're just getting started.

      This code reads all the various sensors (wind speed, direction, rain gauge, humidity, pressure, light, batt_lvl)
      and reports it over the serial comm port. This can be easily routed to a datalogger (such as OpenLog) or
      a wireless transmitter (such as Electric Imp).

      Measurements are reported once a second but windspeed and rain gauge are tied to interrupts that are
      calculated at each report.

      This example code assumes the GPS module is not used.

      Updated by Joel Bartlett
      03/02/2017
      Removed HTU21D code and replaced with Si7021

      Updated be Wes Furuya
      06/19/2023
      Implemented "Weather Meter" Arduino library
    */

    #include <Wire.h>                                        //I2C needed for sensors
    #include "SparkFunMPL3115A2.h"                           //Pressure sensor - Search "SparkFun MPL3115" and install from Library Manager
    #include "SparkFun_Si7021_Breakout_Library.h"            //Humidity sensor - Search "SparkFun Si7021" and install from Library Manager
    #include "SparkFun_Weather_Meter_Kit_Arduino_Library.h"  //Weather meter kit - Search "SparkFun Weather Meter" and install from Library Manager

    //Hardware pin definitions
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    // digital I/O pins
    const byte WSPEED = 3;
    const byte RAIN = 2;
    const byte STAT1 = 7;
    const byte STAT2 = 8;

    // analog I/O pins
    const byte REFERENCE_3V3 = A3;
    const byte LIGHT = A1;
    const byte BATT = A2;
    const byte WDIR = A0;
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    //Global Variables
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    long lastSecond;  //The millis counter to see when a second rolls by

    float humidity = 0;  // [%]
    float tempf = 0;     // [temperature F]
    //float baromin = 30.03;// [barom in] - It's hard to calculate baromin locally, do this in the agent
    float pressure = 0;

    float wind_dir = 0;    // [degrees (Cardinal)]
    float wind_speed = 0;  // [kph]
    float rain = 0;        // [mm]

    float batt_lvl = 11.8;  //[analog value from 0 to 1023]
    float light_lvl = 455;  //[analog value from 0 to 1023]
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    MPL3115A2 myPressure;                                      //Create an instance of the pressure sensor
    Weather myHumidity;                                        //Create an instance of the humidity sensor
    SFEWeatherMeterKit myweatherMeterKit(WDIR, WSPEED, RAIN);  // Create an instance of the weather meter kit

    void setup() 

    void loop() 

      digitalWrite(STAT1, LOW);  //Turn off stat LED

      delay(100);
    }

    //Calculates each of the variables that wunderground is expecting
    void calcWeather() 

    //Returns the voltage of the light sensor based on the 3.3V rail
    //This allows us to ignore what VCC might be (an Arduino plugged into USB has VCC of 4.5 to 5.2V)
    float get_light_level() 

    //Returns the voltage of the raw pin based on the 3.3V rail
    //This allows us to ignore what VCC might be (an Arduino plugged into USB has VCC of 4.5 to 5.2V)
    //Battery level is connected to the RAW pin on Arduino and is fed through two 5% resistors:
    //3.9K on the high side (R1), and 1K on the low side (R2)
    float get_battery_level() 

    //Prints the various variables directly to the port
    //I don't like the way this function is written but Arduino doesn't support floats under sprintf
    void printWeather() 

Upload the sketch onto your board and open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) at **115200 bps**. You should see output similar to the following:

[![Weather Station Example Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/6/weather_station-updated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/weather_station-updated.png)

*Click the image for a closer look.*

## Example Firmware - Weather Station with GPS

[![Weather Shield with GPS](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/6/Arduino_Weather_Shield_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/Arduino_Weather_Shield_2.jpg)

*Shield on a [RedBoard](https://www.sparkfun.com/products/11575) with optional weather meter connectors and GPS attached*

Attach the [GP-735 GPS module](https://www.sparkfun.com/products/13670) using a JST cable. To secure the module, there is space on the shield to attach the module using double-stick tape.

[![Picture of serial switch](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/gpsSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/gpsSwitch.jpg)

*Serial pins are connected to digital pins 4 and 5 when Serial is set to soft and are attached to the internal [UART](https://learn.sparkfun.com/tutorials/serial-communication/uarts) when set to hard.*

There is a switch labeled **Serial** on the shield. This is to select which pins on the Arduino to connect the GPS to. In almost all cases the switch should be set to \'Soft\'. This will attach the GPS serial pins to digital pins 5 (TX from the GPS) and 4 (RX into the GPS).

Grab the GPS example sketch from the GitHub repo that demonstrates using the GP-735 with all the other sensors. Load it onto your Arduino, and open the serial monitor at **115200 bps**.

You can also copy the code below:

    language:c
    /*
      Weather Shield Example
      By: Nathan Seidle
      SparkFun Electronics
      Date: November 16th, 2013
      License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

      Much of this is based on Mike Grusin's USB Weather Board code: https://www.sparkfun.com/products/10586

      This code reads all the various sensors (wind speed, direction, rain gauge, humidity, pressure, light, batt_lvl, GPS data)
      and reports it over the serial comm port. This can be easily routed to a datalogger (such as OpenLog) or
      a wireless transmitter (such as Electric Imp).

      Measurements are reported once a second. The windspeed and rain gauge are tied to interrupts and are
      calculated at the instance of each report.

      This example code assumes the GP-735 GPS module is attached.

      Updated by Joel Bartlett
      03/02/2017
      Removed HTU21D code and replaced with Si7021

      Updated be Wes Furuya
      06/19/2023
      Implemented "Weather Meter" Arduino library
      Updated to TinyGPSPlus Arduino library
    */

    #include <Wire.h>                                        //I2C needed for sensors
    #include "SparkFunMPL3115A2.h"                           //Pressure sensor - Search "SparkFun MPL3115" and install from Library Manager
    #include "SparkFun_Si7021_Breakout_Library.h"            //Humidity sensor - Search "SparkFun Si7021" and install from Library Manager
    #include "SparkFun_Weather_Meter_Kit_Arduino_Library.h"  //Weather meter kit - Search "SparkFun Weather Meter" and install from Library Manager
    #include <SoftwareSerial.h>                              //Needed for GPS
    #include <TinyGPSPlus.h>                                 //Parsing GPS data - Available through the Library Manager.

    //Hardware pin definitions
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    // digital I/O pins
    const byte WSPEED = 3;
    const byte RAIN = 2;
    const byte STAT1 = 7;
    const byte STAT2 = 8;
    // const byte GPS_PWRCTL = 6;              //Pulling this pin low puts GPS to sleep but maintains RTC and RAM
    static const int RXPin = 5, TXPin = 4;  //GPS is attached to pin 4(TX from GPS) and pin 5(RX into GPS)
    static const uint32_t GPSBaud = 9600;   // Default baud rate of the GP-735 GPS module

    // analog I/O pins
    const byte REFERENCE_3V3 = A3;
    const byte LIGHT = A1;
    const byte BATT = A2;
    const byte WDIR = A0;
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    //Global Variables
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    long lastSecond;     //The millis counter to see when a second rolls by
    long lastChars = 0;  //Character counter for GPS parsing

    float humidity = 0;  // [%]
    float tempf = 0;     // [temperature F]
    //float baromin = 30.03;// [barom in] - It's hard to calculate barom in locally, do this in the agent
    float pressure = 0;

    float wind_dir = 0;    // [degrees (Cardinal)]
    float wind_speed = 0;  // [kph]
    float rain = 0;        // [mm]

    float batt_lvl = 11.8;  //[analog value from 0 to 1023]
    float light_lvl = 455;  //[analog value from 0 to 1023]
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    MPL3115A2 myPressure;                                      //Create an instance of the pressure sensor
    Weather myHumidity;                                        //Create an instance of the humidity sensor
    SFEWeatherMeterKit myweatherMeterKit(WDIR, WSPEED, RAIN);  // Create an instance of the weather meter kit

    TinyGPSPlus gps;
    SoftwareSerial ss(RXPin, TXPin);

    void setup() 

    void loop() 

    }

    void printGPS() 

            break;
          }

          else 
        }
      }

      //Prints error message if not data has been receiver from the GPS module
      if (gps.charsProcessed() - lastChars < 10) 

      parseGPS();
    }

    void parseGPS()  else 

      Serial.print(", date=");
      if (gps.date.isValid())  else 

      Serial.print(", time=");
      if (gps.time.isValid())  else 
    }

    //Calculates each of the weather variables
    void calcWeather() 

    //Returns the voltage of the light sensor based on the 3.3V rail
    //This allows us to ignore what VCC might be (an Arduino plugged into USB has VCC of 4.5 to 5.2V)
    float get_light_level() 

    //Returns the voltage of the raw pin based on the 3.3V rail
    //This allows us to ignore what VCC might be (an Arduino plugged into USB has VCC of 4.5 to 5.2V)
    //Battery level is connected to the RAW pin on Arduino and is fed through two 5% resistors:
    //3.9K on the high side (R1), and 1K on the low side (R2)
    float get_battery_level() 

    //Prints the weather variables directly to the port
    //I don't like the way this function is written but Arduino doesn't support floats under sprintf
    void printWeather() 

You should see output similar to the following:

[![Weather Shield with GPS Example Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/6/weather_station_gps-updated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/6/weather_station_gps-updated.png)

*Click the image for a closer look.*

**Note:** The `batt_lvl` is indicating 4.08V. This is correct and is the actual voltage read from the Arduino powered over USB. The GPS module will add 50-80mA to the overall power consumption. If you are using a long or thin USB cable you may see significant voltage drop similar to this example. There is absolutely no harm in this! The Weather Shield runs at 3.3V and the Arduino will continue to run just fine down to about 3V. The reading is very helpful for monitoring your power source (USB, battery, solar, etc).

This example demonstrates how you can get location, altitude, and time from the GPS module. This would be helpful with weather stations that are moving such as balloon satellites, [AVL](http://en.wikipedia.org/wiki/Automatic_vehicle_location), package tracking, and even static stations where you need to know precise altitude or timestamps.

## Troubleshooting

[] **Not working as expected and need help?**

If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\

If you don\'t find what you need there, our [SparkFun Forums](https://forum.sparkfun.com/viewforum.php?f=143) are a great place to find and ask for help.

[SparkFun Forums](https://forum.sparkfun.com/)

### I^2^C Error

If there is an error you will see:

    I2C communication to sensors is not working. Check solder connections.

This message appears when the board is unable to get a response from the I2C sensors. This could be because of a faulty solder connection, or if there are other devices on the A5/A4 lines (which are also called SDA/SCL).

### Barometeric Reading

The Weather Shield example firmware outputs regular barometric pressure. This is very different from the pressure that weather stations report. For more information, see the definition of \"[altimeter setting pressure](http://www.crh.noaa.gov/bou/awebphp/definitions_pressure.php)\". For an example of how to calculate altimeter setting type barometric pressure see the [MPL3115A2 hook-up guide](https://learn.sparkfun.com/tutorials/mpl3115a2-pressure-sensor-hookup-guide/pressure-vs-altimeter-setting). Also check out the [MPL3115A2 library](https://github.com/sparkfun/MPL3115A2_Breakout), specifically the `BarometricHgInch` example.

### No GPS Data

Even if the GPS module doesn\'t have a fix, it should still transmit blank NMEA sentences. However, if there is no serial data being transmitted from the GPS module, the following error will be displayed before the GPS data.

    No GPS data: check wiring/switch.

If the GPS module is connected properly, double check the switch position on the board and that the **RX/TX** pin connections are defined properly in the sketch.

### Status LEDs

1.  In the example firmware, the blue LED should blink when the data from the weather sensors are being transmitted.
2.  In the example firmware, the green LED will only turn on when the GPS data has been updated. The LED may blink, as blank or incomplete NMEA sentences get parsed from the GPS module.
    - There is a commented out block of code, if users wish to reconfigure the logic for the LED to check for new GPS data that is also valid.