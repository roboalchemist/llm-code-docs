# Source: https://learn.sparkfun.com/tutorials/sparkfun-temperature-sensor---stts22h-qwiic-hookup-guide

## Introduction

The [SparkFun Temperature Sensor - STTS22H (Qwiic)](https://www.sparkfun.com/products/21262) and the [SparkFun Micro Temperature Sensor - STTS22H (Qwiic)](https://www.sparkfun.com/products/21273) are Qwiic enabled breakout boards based on the ultralow-power, high-accuracy, digital temperature sensor STTS22H from ST Microelectronics. Thanks to its factory calibration the STTS22H offers high-end accuracy performance over the entire operating temperature range, reaching as low as ±0.5 °C without requiring any further calibration at the application level.

[![SparkFun Temperature Sensor - STTS22H (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/0/3/8/STTS22-_01.jpg)](https://www.sparkfun.com/sparkfun-temperature-sensor-stts22h-qwiic.html)

### [SparkFun Temperature Sensor - STTS22H (Qwiic)](https://www.sparkfun.com/sparkfun-temperature-sensor-stts22h-qwiic.html) 

[ SEN-21262 ]

Thanks to its factory calibration the STTS22H offers high-end accuracy performance over the entire operating temperature rang...

[ [\$6.95] ]

[![SparkFun Micro Temperature Sensor - STTS22H (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/0/5/1/STTS22Micro-_01.jpg)](https://www.sparkfun.com/sparkfun-micro-temperature-sensor-stts22h-qwiic.html)

### [SparkFun Micro Temperature Sensor - STTS22H (Qwiic)](https://www.sparkfun.com/sparkfun-micro-temperature-sensor-stts22h-qwiic.html) 

[ SEN-21273 ]

Thanks to its factory calibration the STTS22H offers high-end accuracy performance over the entire operating temperature rang...

[ [\$8.53] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v)

### Using the Arduino Pro Mini 3.3V 

This tutorial is your guide to all things Arduino Pro Mini. It explains what it is, what it\'s not, and how to get started using it.

## Hardware Overview

### STTS22

The STTS22H is an ultralow-power, high-accuracy, digital temperature sensor offering high performance over the entire operating temperature range. Thanks to its factory calibration the STTS22H offers high-end accuracy performance over the entire operating temperature range, reaching as low as ±0.5 °C without requiring any further calibration at the application level. The sensor operating mode is user-configurable and allows selecting between different ODRs (down to 1 Hz) or the one-shot mode for battery saving. In one-shot mode, the sensor current consumption falls to 1.75 µA. For more information, refer to the [datasheet](https://cdn.sparkfun.com/assets/3/0/b/7/6/STTS22h-Datasheet.pdf).

  [![STTS22 Highlight](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_Sensor.jpg)   [![STTS22 Highlight on Micro](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-Sensor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-Sensor.png)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *STTS22*                                                                                                                                                                                                                          *STTS22 on Micro*

### Qwiic Connectors

There are two Qwiic connectors on either side of the SparkFun Temperature Sensor - STTS22H to provide power and I^2^C connectivity simultaneously. The Micro version has a single Qwiic connector that again provides power and I^2^C connectivity. The I^2^C address of both boards is **0x3C** by default, but the 1x1 board has 3 other addresses the board can be configured to use, while the Micro has 1 other address available.

  [![Qwiic Connectors](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_QwiicConnectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_QwiicConnectors.jpg)   [![Qwiic Connector on Micro](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-QwiicConnector.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-QwiicConnector.png)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *Qwiic Connectors*                                                                                                                                                                                                                                  *Qwiic Connector on Micro*

### Power

Ideally, power will be supplied via the Qwiic connector(s). Alternatively, power can be supplied through the header along the bottom side of the board labeled `3V3` and `GND`. The input voltage range should be between **1.5**-**3.6V**. The Micro version has a single Ground Pin available.

  [![3.3V & GND Pins](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_PowerPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_PowerPins.jpg)   [![GND Pins on Micro](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-GroundPin.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-GroundPin.png)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *3.3V & GND Pins*                                                                                                                                                                                                                      *GND Pin on Micro*

⚡ **Note:** There is no onboard voltage regulation on either of these boards. If you choose to provide power via the plated through holes, ensure that your voltage does not exceed **5.5V**.

### Interrupt Pin

An interrupt pin is available to signal the application whenever the selectable high or low threshold has been exceeded.

  [![Interrupt Pin](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_InterruptPin.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_InterruptPin.jpg)   [![Interrupt Pin on Micro](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-InterruptPin.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-InterruptPin.png)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *Interrupt Pin*                                                                                                                                                                                                                            *Interrupt Pin on Micro*

### Power LED

Hopefully this is self-explanatory, but this LED lights up when power is supplied to the board.

  [![Power LED](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_PWRLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_PWRLED.jpg)   [![Power LED on Micro](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-PowerLED.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-PowerLED.png)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *Power LED*                                                                                                                                                                                                                *Power LED on Micro*

### Exposed Pad

There\'s an extra pad on the bottom side of each board that allows for the most accurate possible readings.

  [![Exposed Pad](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_BareCopperSensorPad.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_BareCopperSensorPad.jpg)   [![Exposed Pad on Micro](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-BareCopperSensorPad.png)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-BareCopperSensorPad.png)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *Exposed Pad*                                                                                                                                                                                                                                                    *Exposed Pad on Micro*

### Jumpers

#### LED Jumper

If power consumption is an issue, cut this jumper to disable the LED on the front of the board.

  [![Power LED Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_LED-Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_LED-Jumper.jpg)   [![Power LED Jumperon Micro](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-LED-Jumper.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-LED-Jumper.png)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *Power LED Jumper*                                                                                                                                                                                                                        *Power LED Jumper on Micro*

#### Address Jumpers

The 1x1 board has two address jumpers available. The default I^2^C address is **0x3C**. By cutting various trace combinations, there are three other I^2^C addresses available.

+--------------------------+
| **ADDR**                 |
+=========+================+
| R8(15K) | 0x3C (Default) |
+---------+----------------+
| R7(56K) | 0x3E           |
+---------+----------------+
| VDD     | 0x38           |
+---------+----------------+
| GND     | 0x3F           |
+---------+----------------+
| OPEN    | Undefined      |
+---------+----------------+

  [![Address Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_ADDR-Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_ADDR-Jumper.jpg)   [![Address Jumper 1](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_ADDR1-Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_ADDR1-Jumper.jpg)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *Address Jumper*                                                                                                                                                                                                                          *Address Jumper 1*

The Micro version of this board has a single address jumper that affords the ability to change the I^2^C address from **0x3C (Default)** to 0x38.

[![Address jumper is highlighted on the back of the Micro Board](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-Address-Jumper.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-Address-Jumper.png)

#### I^2^C Jumper

These boards are both equipped with pull-up resistors. If you are daisy-chaining multiple Qwiic devices, you will want to cut this jumper; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. To disable the pull up resistors, use an X-acto knife to cut the joint between the two jumper pads highlighted below.

  [![I\<sup\>2\</sup\>C Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_I2C-Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_I2C-Jumper.jpg)   [![I\<sup\>2\</sup\>C Jumper on Micro](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-I2C-Jumper.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-I2C-Jumper.png)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *I^2^C Jumper*                                                                                                                                                                                                                                     *I^2^C Jumper on Micro*

### Board Outline

The standard Temperature Sensor STTS22H Breakout measures 1\" x 1\".

[![Standard Board measures 1 inch by 1 inch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/21262-SparkFun_Temperature_Sensor-STTS22H-BoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-SparkFun_Temperature_Sensor-STTS22H-BoardOutline.png)

The Micro Temperature Sensor STTS22H Breakout measures 0.75\" x 0.3\".

[![Micro Board measures 0.75 inches by 0.3 inches](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/21273-SparkFun_Micro_Temperature_Sensor-STTS22H-BoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-SparkFun_Micro_Temperature_Sensor-STTS22H-BoardOutline.png)

## Hardware Hookup

The delightful thing about our [Qwiic System](https://www.sparkfun.com/qwiic) is that it makes hooking up your project as easy as plug and play. Pop one end of your Qwiic connector into the controlling board and plug the other end of your Qwiic connector into your Temperature Sensor board! Voila!

[![Qwiic cable connects RedBoard to the 1x1 board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H-BasicHookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H-BasicHookup.jpg)

[![Qwiic cable connects RedBoard to the Micro board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-BasicHookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21273-Micro_Temperature_Sensor-STTS22H-BasicHookup.jpg)

## Software Setup

**Note:** Make sure you are using the latest stable version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

SparkFun has written a library to work with the SparkFun Temperature Sensor - STTS22H (Qwiic). You can obtain this library through the Arduino Library Manager by searching for \"STTS22H\". Find the one written by SparkFun Electronics and install the latest version. If you prefer downloading libraries manually, you can grab them from the GitHub Repository.

[SparkFun STTS22H Arduino Library GitHub](https://github.com/sparkfun/SparkFun_STTS22H_Arduino_Library/archive/refs/heads/main.zip)

## Examples

### Example 1: Basic

Now that we\'ve got our library installed and our hardware all hooked up, let\'s look at some examples.

This first example just does some basic measurements. To find Example 1, go to **File** \> **Examples** \> **SparkFun Temperature Sensor - STTS22H** \> **example1-basic**:

[![Image shows menu pulldown as described above](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/Example1_Menu.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/Example1_Menu.jpg)

*Having a hard time seeing details? Click the image for a closer look.*

Or alternatively you can copy and paste the code below into a nice shiny new Arduino window:

    language:c
    /*
    example1-basic.ino

    This example shows basic data retrieval from the SparkFun Temperature Sensor - STTS22H.

    Output Data Rates: 

    STTS22H_POWER_DOWN
    STTS22H_ONE_SHOT  
    STTS22H_1Hz       
    STTS22H_25Hz      
    STTS22H_50Hz      
    STTS22H_100Hz     
    STTS22H_200Hz     

    Written by: 
    Elias Santistevan @ SparkFun Electronics December, 2022

    Products: 
       SparkFun Temperature Sensor - STTS2H              https://www.sparkfun.com/products/21262
       SparkFun Micro Temperature Sensor - STTS2H        https://www.sparkfun.com/products/21051

    Repository:
         https://github.com/sparkfun/SparkFun_STTS22H_Arduino_Library

    SparkFun code, firmware, and software is released under the MIT
    License(http://opensource.org/licenses/MIT).

    */

    #include <Wire.h>
    #include "SparkFun_STTS22H.h"

    SparkFun_STTS22H mySTTS; 

    float temp; 

    void setup()
    

        Serial.println("Ready");

        // Other output data rates can be found in the description
        // above. To change the ODR or mode, the device must first be
        // powered down.
        mySTTS.setDataRate(STTS22H_POWER_DOWN);
        delay(10);
        mySTTS.setDataRate(STTS22H_1Hz);

        // Enables incrementing register behavior for the IC.
        // It is not enabled by default as the datsheet states and
        // is vital for reading the two temperature registers.
        mySTTS.enableAutoIncrement();

        delay(100);
    }

    void loop()
     

        // delay = 1/ODR 
        delay(1000);

    }

Once you\'re ready to go, go ahead and hit the upload button (the right facing arrow button under the \"Edit\" menu item). Once your code is uploaded, open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and you\'ll see information start printing out.

[![example1 Output shows temperature readings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/example1_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/example1_Output.jpg)

### Example 2: Interrupt

Example 2 can be found under **File** \> **Examples** \> **SparkFun Temperature Sensor - STTS22H** \> **example2-interrupt**:

[![Image shows menu pulldown as described above](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/Example2_Menu.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/Example2_Menu.jpg)

You can also copy the code below into a new Arduino file:

    language:c
    /*
    example2_basic.ino

    This example desmonstrates how to set temperature thresholds to trigger an interrupt. 

    Output Data Rates: 

    STTS22H_POWER_DOWN
    STTS22H_ONE_SHOT  
    STTS22H_1Hz       
    STTS22H_25Hz      
    STTS22H_50Hz      
    STTS22H_100Hz     
    STTS22H_200Hz     

    Written by: 
    Elias Santistevan @ SparkFun Electronics December, 2022

    Products: 
       SparkFun Temperature Sensor - STTS2H              https://www.sparkfun.com/products/21262
       SparkFun Micro Temperature Sensor - STTS2H        https://www.sparkfun.com/products/21051

    Repository:
         https://github.com/sparkfun/SparkFun_STTS22H_Arduino_Library

    SparkFun code, firmware, and software is released under the MIT
    License(http://opensource.org/licenses/MIT).

    */

    #include <Wire.h>
    #include "SparkFun_STTS22H.h"

    SparkFun_STTS22H mySTTS; 

    float temp; 

    // These values are in Farenheit
    float interruptHighValue = 90.5;
    float interruptLowValue = 42.0;

    int tempInterrupt = 2; 

    void setup()
    

        Serial.println("Ready");

        // Other output data rates can be found in the description
        // above. To change the ODR or mode, the device must first be
        // powered down.
        mySTTS.setDataRate(STTS22H_POWER_DOWN);
        delay(10);
        mySTTS.setDataRate(STTS22H_25Hz);

        // Enables incrementing register behavior for the IC.
        // It is not enabled by default as the datsheet states and
        // is vital for reading the two temperature registers.
        mySTTS.enableAutoIncrement();

        // Set interrupts for both lower and higher thresholds.
        // Note: These functions accept Farenheit as their arguments.
        // Other functions for different units just below. 
        mySTTS.setInterruptLowF(interruptLowValue);
        mySTTS.setInterruptHighF(interruptHighValue);

        //mySTTS.setInterruptLowC(interruptLowValue);
        //mySTTS.setInterruptHighC(interruptHighValue);

        //mySTTS.setInterruptLowK(interruptLowValue);
        //mySTTS.setInterruptHighK(interruptHighValue);

        delay(100);
    }

    void loop()
    

        // delay = 1/ODR 
        delay(1000);

    }

Note that depending on which processor board you are using, you may need to alter the Interrupt Pin. Since we\'re using a RedBoard here, our Interrupt Pin is 2 (`int tempInterrupt = 2;`). Also, in this example, we\'ve used an [IC hook with a pigtail](https://www.sparkfun.com/products/9741) to connect the Interrupt Pin to the RedBoard pin 2, but you can also [solder headers](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) to the STTS22H Temperature Sensor so you can use the interrupt pin. Your hardware hookup should look something like the following:

[![Hardware Hookup of example 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_InterruptExample.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/21262-Temperature_Sensor-STTS22H_InterruptExample.jpg)

*Having a hard time seeing details? Click the image for a closer look.*

Once you\'re ready to go, go ahead and hit the upload button (the right facing arrow button under the \"Edit\" menu item). Once your code is uploaded, open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and you\'ll see information start printing out.

If you have a look at the code, you\'ll notice that we\'ve set our upper threshhold to 90.5 degrees F, and our lower threshhold to 42 degrees F. I held the sensor in front of a heater to hit the upper threshhold:

[![Example 2 output shows upper threshhold being hit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/example2_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/example2_Output.jpg)

The lower threshhold was reached by sticking the sensor in a plastic bag and then putting that plastic bag into ice water:

[![Example 2 output shows lower threshhold being hit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/example2_Output_LowerThresh.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/example2_Output_LowerThresh.jpg)

### Example 3: One Shot

In Example 3, we\'re going to have a look at the One Shot functionality. To find Example 3, go to **File** \> **Examples** \> **SparkFun Temperature Sensor - STTS22H** \> **example3-one_shot**:

[![Image shows menu pulldown as described above](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/7/Example3_Menu.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/Example3_Menu.jpg)

Or you can copy and paste the code below into a clean Arduino sketch:

    language:c
    /*
    example3-one_shot.ino

    This example shows basic data retrieval using the "one-shot" feature i.e. - get the temp
    now feature. 

    Output Data Rates: 

    STTS22H_POWER_DOWN
    STTS22H_ONE_SHOT   < -------- This one. 
    STTS22H_1Hz       
    STTS22H_25Hz      
    STTS22H_50Hz      
    STTS22H_100Hz     
    STTS22H_200Hz     

    Written by: 
    Elias Santistevan @ SparkFun Electronics December, 2022

    Products: 
       SparkFun Temperature Sensor - STTS2H              https://www.sparkfun.com/products/21262
       SparkFun Micro Temperature Sensor - STTS2H        https://www.sparkfun.com/products/21051

    Repository:
         https://github.com/sparkfun/SparkFun_STTS22H_Arduino_Library

    SparkFun code, firmware, and software is released under the MIT
    License(http://opensource.org/licenses/MIT).

    */

    #include <Wire.h>
    #include "SparkFun_STTS22H.h"

    SparkFun_STTS22H mySTTS; 

    float temp; 

    void setup()
    

        Serial.println("Ready");

        // Other output data rates can be found in the description
        // above. To change the ODR or mode, the device must first be
        // powered down.
        mySTTS.setDataRate(STTS22H_POWER_DOWN);
        delay(10);
        // Force new reading, temp sensor will power down after conversion. 
        mySTTS.setDataRate(STTS22H_ONE_SHOT); 

        // Enables incrementing register behavior for the IC.
        // It is not enabled by default as the datsheet states and
        // is vital for reading the two temperature registers.
        mySTTS.enableAutoIncrement();

        delay(100);
    }

    void loop()
     

        // Demonstrative delay. 
        delay(100);

    }

Once you\'re ready to go, go ahead and hit the upload button (the right facing arrow button under the \"Edit\" menu item). Once your code is uploaded, open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and you\'ll see information start printing out.

[![Example 3 output](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/Example3_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/7/Example3_Output.jpg)

This really isn\'t all that exciting until you measure the current consumption!

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)