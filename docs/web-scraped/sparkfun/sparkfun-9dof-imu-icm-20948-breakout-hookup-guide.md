# Source: https://learn.sparkfun.com/tutorials/sparkfun-9dof-imu-icm-20948-breakout-hookup-guide

## Introduction

The [SparkFun 9DoF IMU Breakout](https://www.sparkfun.com/products/15335) incorporates all the amazing features of Invensense\'s ICM-20948 into a Qwiic-enabled breakout board replete with logic shifting and broken out GPIO pins for all your motion sensing needs. The ICM-20948 itself is an extremely low powered, I^2^C and SPI enabled 9-axis motion tracking device that is ideally suited for smartphones, tablets, wearable sensors, and IoT applications. Featuring a 3-Axis Gyroscope with four selectable ranges, a 3-Axis Accelerometer, again with four selectable ranges, a 3-axis compass with a wide range to ±4900 µT, and an on-board Digital Motion Processor, this little breakout can even detect the motion of invisibility cloaks. Not really. Just checking to see if you were still with me. But it *is* pretty amazing. Check it out:

[![SparkFun 9DoF IMU Breakout - ICM-20948 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/8/6/0/15335-SparkFun_9DoF_IMU_Breakout_-_ICM-20948__Qwiic_-01b.jpg)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-icm-20948-qwiic.html)

### [SparkFun 9DoF IMU Breakout - ICM-20948 (Qwiic)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-icm-20948-qwiic.html) 

[ SEN-15335 ]

The SparkFun 9DoF IMU Breakout incorporates all the amazing features of the ICM-20948 into a Qwiic-enabled breakout board.

[ [\$21.95] ]

In this hookup guide, we\'ll connect our sensor up to our [Esp32 Thing Plus](https://www.sparkfun.com/products/14689) microcontroller and run a of quick (Qwiic) example to get you up and running with this fantastic board!

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

If you choose to utilize the broken out GPIO, you will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: text-center                                                                                                                                     |
| [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic) |
| :::                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

## Hardware Overview

We\'ve put a lot of effort into making this the most useful and versatile breakout for the ICM 20948. Let\'s take a closer look at all the special parts.

### Sensor

At the heart of the board (metaphorically and geometrically) is the ICM 20948 from Invensense. This puppy packs the ability to measure up to 10 unique values (3 axes of acceleration, rotational rate, and magnetic strength data as well as an on-board temperature sensor). The sensor is placed dead-center between the four 4-40 stand-off mounting holes to drastically simplify computation in dynamics.

[![ICM 20948 Sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/3/15335-Sensor.jpg)

*ICM 20948 Sensor*

### Level Shifters

The ICM is a fickle fellow - optionally allowing a **3.3V** supply voltage but requiring I/O to work at 1.8V. This is just the price we pay for amazing technolojay (hey that rhymes). Since there aren\'t many popular development boards that run at the [voltage of the future](https://en.wikipedia.org/wiki/LVCMOS) we\'ve added high speed level shifting to each and every IO pin. These cool MOSFETS allow for bi-directional voltage translation up to the maximum SPI speed of the ICM - 7MHz - which will allow you to make inertial measurements with fantastic temporal resolution. Feel free to use the ICM IO anywhere from 1.8V to 5.5V!

[![Mosfets](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-Mosfets.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/3/15335-Mosfets.jpg)

*TXS0108 Modules*

### Power

Input power on this board should be between **1.8-5.5V**. The ICM is riding the wave of 1.8V level devices so we\'ve included a built-in regulator to make it easy to interface with 3.3V or 5V microcontrollers. There is an LED on the front of the board that will light up when the board is powered correctly. You can disable the LED functionality by cutting the LED jumper on the back of the board. This is described in the ***Jumpers*** section below.

[![power LED on the front of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-PowerLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/3/15335-PowerLED.jpg)

*Power LED*

### Qwiic Connectors

There are two Qwiic connectors on the board such that you can daisy-chain the boards should you choose to do so. If you\'re unfamiliar with our Qwiic system, head on over to our [Qwiic page](https://www.sparkfun.com/qwiic) to see the advantages! Of course, if you don\'t want to use Qwiic we\'ve still broken out every pin on 0.1\" spaced plated through-hole headers. You can find more information about these connections in the ***Headers*** section.

[![Qwiic Connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-QwiicConnex.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/3/15335-QwiicConnex.jpg)

*Qwiic Connectors*

### GPIO

For flexibility, we\'ve broken out functional pins for both I^2^C and SPI. There are no modifications required to switch between I^2^C mode and SPI out of the box, but if the \'ADR\' jumper on the back is closed SPI will be unavailable.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-GPIO_I2C.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-GPIO_I2C.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-GPIO_SPI.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-GPIO_SPI.jpg)
  *I^2^C Pin Labels*                                                                                                                                                              *SPI Pin Labels*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Jumpers

Look at all those jumpers on the back of the board! Here\'s what they do:

#### Pullup Jumpers

- **I^2^C Pullup** - Does nothing, the pullups are not populated on the board because the TXS0108 has them built-in
- **Aux Pullup** - Cut these jumpers to disconnect the pullup resistors from the auxiliary I^2^C bus

#### LED Jumper

- Cutting this jumper allows you to disable the LED functionality on the front of the board.

#### Address Jumper

- When open (default) the address of the ICM is 0x69 and it is possible to use SPI communication. When soldered closed the address changes to 0x68. Closing the jumper prevents you from using SPI.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-PullupJumpers.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-PullupJumpers.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-LEDJumper.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-LEDJumper.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-AddrJumper.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-AddrJumper.jpg)
  *Pullup Jumpers*                                                                                                                                                                          *LED Jumper*                                                                                                                                                                      *I^2^C Address Jumper*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Hardware Hookup

One of the many advantages of the Qwiic system is that hooking up your hardware is extremely simple. Simply grab a Qwiic cable and plug your 9DoF in!

[![Hooking up microcontroller to breakout via qwiic cable](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/3/15335_qwiic_9Dof_hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/3/15335_qwiic_9Dof_hookup.jpg)

*Easy peasy lemon squeezy*

**⚡WARNING!**\
If you are using the ESP32 Thing Plus, make sure your power supply is **5V**, NOT 5.1V. We have noticed a power spike in our [5.1V power supplies](https://www.sparkfun.com/products/13831), that can damage the IC on the ESP32 Thing Plus. Long cables can also generate a large enough voltage spike to damage the IC. We recommend keeping power supply cables shorter than 6 feet to minimize potential damage.

If you\'d like to use the broken out GPIO pins, things get a bit more complicated. That said, to make life a little easier we\'ve organized them by function, and provided lots of labels. You\'ll first notice that one side has the text \'I^2^C\' and the other side says \'SPI.\' The labels on either side are those that apply to that kind of communication.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-GPIO_I2C.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-GPIO_I2C.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-GPIO_SPI.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/15335-GPIO_SPI.jpg)
  *I^2^C Pin Labels*                                                                                                                                                              *SPI Pin Labels*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, you\'ll see that on the left side are the main connections to the host microcontroller. When connecting I^2^C you\'ll have a \'No Connect\' pin that serves as the chip select when using SPI. As noted before, there are no modifications required to switch between I^2^C mode and SPI out of the box. However if the \'ADR\' jumper is closed SPI will be unavailable.

On the right side are connections to external sensors that can be controlled by the ICM, as well as the \'INT\' and \'FSYNC\' interrupt pins. The auxiliary I^2^C bus pins are level shifted to/from the \'VIN\' level that you supply.

+-----------------------------------------------------------------------------------------+
| Breakout Board Pin Functions (SPI)                                                      |
+==============+=============+==================+=========================================+
| Breakout Pin | Arduino Uno | Esp32 Thing Plus | Microcontroller Pin Requirements        |
+--------------+-------------+------------------+-----------------------------------------+
| MOSI         | 11          | 18               | Data output of chosen SPI port          |
+--------------+-------------+------------------+-----------------------------------------+
| SCLK         | 13          | 5                | Clock output of chosen SPI port         |
+--------------+-------------+------------------+-----------------------------------------+
| MISO         | 12          | 19               | Data input of chosen SPI port           |
+--------------+-------------+------------------+-----------------------------------------+
| CS           | 2           | 2                | An output pin to select the ICM for SPI |
+--------------+-------------+------------------+-----------------------------------------+

+-------------------------------------------------------------------------------------------------------+
| Breakout Board Pin Functions (I^2^C)                                                                  |
+==============+=============+==================+=======================================================+
| Breakout Pin | Arduino Uno | Esp32 Thing Plus | Microcontroller Pin Requirements                      |
+--------------+-------------+------------------+-------------------------------------------------------+
| DA           | SDA         | 23               | Data line of chosen I^2^C port                        |
+--------------+-------------+------------------+-------------------------------------------------------+
| CL           | SCL         | 22               | Clock line of chosen I^2^C port                       |
+--------------+-------------+------------------+-------------------------------------------------------+
| AD0          | \-          | \-               | Optional - use to control I^2^C address from software |
+--------------+-------------+------------------+-------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------+
| Breakout Board Pin Functions (Auxiliary I^2^C and Interrupts)                                                                           |
+==================+==================+==================+================================================================================+
| Breakout Pin     | Arduino Uno      | Esp32 Thing Plus | Microcontroller Pin Requirements                                               |
+------------------+------------------+------------------+--------------------------------------------------------------------------------+
| ADA              | \-               | \-               | Data line of auxiliary I^2^C bus                                               |
+------------------+------------------+------------------+--------------------------------------------------------------------------------+
| ACL              | \-               | \-               | Clock line of auxiliary I^2^C bus                                              |
+------------------+------------------+------------------+--------------------------------------------------------------------------------+
| FSYNC            | \-               | \-               | Optional - synchronize measurements with a signal out from the microcontroller |
+------------------+------------------+------------------+--------------------------------------------------------------------------------+
| INT              | \-               | \-               | Optional - respond to configurable interrupts in from the ICM                  |
+------------------+------------------+------------------+--------------------------------------------------------------------------------+

## Software Setup and Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

In this example, we are using the [SparkFun Esp32 Thing WROOM Plus](https://www.sparkfun.com/products/14689). If you have not used this board before, head on over to the [ESP32 Thing Plus Hookup Guide](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide) for a general overview, as well as information on getting set up with board definitions.

[](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide)

### ESP32 Thing Plus Hookup Guide 

March 7, 2019

Hookup guide for the ESP32 Thing Plus (Micro-B) using the ESP32 WROOM\'s WiFi/Bluetooth system-on-chip in Arduino.

In order to use the ICM-20948 breakout, you\'ll need to install the [SparkFun ICM-20948 Arduino Library](https://github.com/sparkfun/SparkFun_ICM-20948_ArduinoLibrary). We recommend you install the library via the Arduino IDE by using the library manager and search for **Sparkfun 9DoF IMU Breakout**. Or you can download and manually install a zip of the library by clicking on the link below. For those who want to view the code, check out the [GitHub repo](https://github.com/sparkfun/SparkFun_ICM-20948_ArduinoLibrary).

[SparkFun 9DoF IMU Breakout Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_ICM-20948_ArduinoLibrary/archive/main.zip)

### Example 1

In this example, we\'ve hookup up our ICM-20948 to an [ESP32 Thing Plus](https://www.sparkfun.com/products/14689) using a short [Qwiic cable](https://www.sparkfun.com/products/14427).

Once you\'ve installed the ICM-20948 library, load the first example sketch from **File**-\>**Examples**-\>**SparkFun 9DoF IMU Breakout - ICM 20948 - Arduino Library**-\>**Arduino**-\>**Example1_Basics**.

[![Where to find Example 1 in the Arduino IDE](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/Example1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/3/Example1.jpg)

*Having a hard time seeing? Click the image for a closer look.*

The very first thing you\'ll see in the code is the `#include` statement for the library. Alongside that is a convenient link that will help you get the library through the Arduino library manager. Next is a commented out `#define` statement called \'USE_SPI\'. If instead you have chosen to connect your ICM with the SPI pins all you need to do is uncomment that line.

    language:c
    #include "ICM_20948.h"  // Click here to get the library: http://librarymanager/All#SparkFun_ICM_20948_IMU

    //#define USE_SPI       // Uncomment this to use SPI

Up next is a short section where you can configure your particular setup. First of all if you need to change your serial port, e.g. if you\'re using a SAMD21 board, you can change the \'SERIAL_PORT\' define (\'SerialUSB\' for SAMD21). You can do the same to change your I2C port or SPI port, depending on which you\'re using. When using I2C you have the ability to change the I2C address of the sensor with the Address 0 bit. By default it is \'1\' but you could change it to 0 if you\'ve closed the \'ADR\' jumper. When using SPI you need to specify a chip select pin - in the example we default to pin 2.

    language:c
    #define SERIAL_PORT Serial

    #define SPI_PORT SPI    // Your desired SPI port.       Used only when "USE_SPI" is defined
    #define CS_PIN 2        // Which pin you connect CS to. Used only when "USE_SPI" is defined

    #define WIRE_PORT Wire  // Your desired Wire port.      Used when "USE_SPI" is not defined
    #define AD0_VAL   1     // The value of the last bit of the I2C address. 
                            // On the SparkFun 9DoF IMU breakout the default is 1, and when 
                            // the ADR jumper is closed the value becomes 0

That\'s it for stuff you (might) need to do to set up the example! Now we\'ll just all hop in the bus, take a tour, and I\'ll point out items on your right and left.

The next little block creates either a `ICM_20948_I2C` or `ICM_20948_SPI` object called \'myICM\'. Since they have the same name, and they both inherit from the grandaddy `ICM_20948` class, we\'ll be able to use them interchangeably later on in the example.

    language:c
    #ifdef USE_SPI
      ICM_20948_SPI myICM;  // If using SPI create an ICM_20948_SPI object
    #else
      ICM_20948_I2C myICM;  // Otherwise create an ICM_20948_I2C object
    #endif

In the `setup()` function we have your standard Arduino initialization of your serial port, and then we have the last interface-dependent section. There you\'ll see the \'myICM\' object being started up with the appropriate arguments for the chosen interface. This example shows all arguments being explicitly stated, but it is also possible to call the `.begin()` function with default arguments. The initialization will repeat with a delay until the device is successfully found. If it is not connecting try checking your wiring.

    language:c
    #ifdef USE_SPI
        SPI_PORT.begin();
        myICM.begin( CS_PIN, SPI_PORT ); 
    #else
        WIRE_PORT.begin();
        WIRE_PORT.setClock(400000);
        myICM.begin( WIRE_PORT, AD0_VAL );
    #endif

Here\'s a little trick for debugging the ICM - nearly all operations will update the internal \'myICM.status\' value. You can check it directly (0 means all good, anything else is an error) or you can use the `statusString()` method to get the latest status in human-readable form.

    language:c
        SERIAL_PORT.print( F("Initialization of the sensor returned: ") );
        SERIAL_PORT.println( myICM.statusString() );
        if( myICM.status != ICM_20948_Stat_Ok )else

The last part of the sketch is the `loop()` where the sensor gets polled for new data, and that data gets pushed over the serial port. All the data is contained in the \'AGMT\' structure, which stands for Accelerometer, Gyroscope, Magnetometer, and Temperature sensors. For convenience this sketch also includes functions (that are not part of the library) to print the results in a pretty format.

    language:c
    void loop() else

    }

When you open up your [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics), you should see something like the following:

[![Serial Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/3/SerialOutput.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/3/SerialOutput.png)

*Having a hard time seeing? Click the image for a closer look.*

There ya have it! Now go ahead and hack it up.