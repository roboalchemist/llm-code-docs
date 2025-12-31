# Source: https://learn.sparkfun.com/tutorials/qwiic-tof-imager---vl53l5cx-hookup-guide

## Introduction

The [Qwiic ToF Imager - VL53L5CX](https://www.sparkfun.com/products/18642) and the [Qwiic Mini ToF Imager - VL53L5CX](https://www.sparkfun.com/products/19013) are here! These little breakout boards are built around ST Electronics\' VL53L5CX; a state of the art, Time-of-Flight (ToF), multizone ranging sensor enhancing the ST FlightSense product family. This chip integrates a SPAD array, physical infrared filters, and diffractive optical elements (DOE) to achieve the best ranging performance in various ambient lighting conditions with a range of cover glass materials.

Multizone distance measurements are possible up to 8x8 zones with a wide 63° diagonal FoV which can be reduced by software. Thanks to ST Histogram patented algorithms, the VL53L5CX is able to detect different objects within the FoV. The Histogram also provides immunity to cover glass crosstalk beyond 60 cm.

Ideal for 3D room mapping, obstacle detection for robotics, gesture recognition, IoT, laser-assisted autofocus, and AR/VR enhancement, the Qwiic connector on this sensor makes integration easy.

[![SparkFun Qwiic ToF Imager - VL53L5CX](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/1/6/9/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-tof-imager-vl53l5cx.html)

### [SparkFun Qwiic ToF Imager - VL53L5CX](https://www.sparkfun.com/sparkfun-qwiic-tof-imager-vl53l5cx.html) 

[ SEN-18642 ]

The SparkFun Qwiic ToF Imager is built around VL53L5CX from ST Electronics; a state of the art, Time-of-Flight (ToF), multizo...

[ [\$32.50] ]

[![SparkFun Qwiic Mini ToF Imager - VL53L5CX](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/6/1/2/19013-SparkFun_Qwiic_Mini_ToF_Imager_-_VL53L5CX-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-mini-tof-imager-vl53l5cx.html)

### [SparkFun Qwiic Mini ToF Imager - VL53L5CX](https://www.sparkfun.com/sparkfun-qwiic-mini-tof-imager-vl53l5cx.html) 

[ SEN-19013 ]

The SparkFun Qwiic Mini ToF Imager is built around VL53L5CX from ST Electronics; a state of the art, Time-of-Flight (ToF), mu...

[ [\$25.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/hookup-guide-for-the-sparkfun-artemis-thing-plus)

### Hookup Guide for the SparkFun Artemis Thing Plus 

Get started with our SparkFun Artemis Thing Plus - our popular Thing Plus footprint with the powerful Artemis module for ultimate functionality.

## Hardware Overview

### VL53L5CX

The SparkFun Qwiic ToF Imager and Qwiic ToF Mini are state of the art, 64 pixel Time-of-Flight (ToF) 4 meter ranging sensors built around the VL53L5CX from ST. To see more details, refer to the [datasheet](https://cdn.sparkfun.com/assets/6/e/3/0/6/vl53l5cx-datasheet.pdf).

[] **Note:** Both of these boards ship with vacuum tape over the sensor. Please be sure to remove this tape before first use!

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![The sensor is smack in the middle of the front side of the board.](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-Sensor.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-Sensor.jpg)   [![The sensor is a little bit higher than the middle of the front side of the board.](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-Sensor1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-Sensor1.jpg)
  *Qwiic ToF Imager - VL53L5CX*                                                                                                                                                                                                                                                                                    *Qwiic Mini ToF Imager - VL53L5CX*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Qwiic Connectors

Our Qwiic Ecosystem makes sensors pretty much plug and play. There are two Qwiic connectors on either side of the Qwiic Air Velocity Sensor board to provide power and I^2^C connectivity simultaneously.

The 7-bit unshifted I^2^C address (most commonly used with Arduino) is **0x29**. The 8-bit I^2^C address of the board is **0x52** for writing and **0x53** for reading.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic connectors live on either side of the front side of the board (left and right).](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-Qwiic.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-Qwiic.jpg)   [![Qwiic connectors live on either side of the back side of the board (left and right).](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-Qwiic1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-Sensor1.jpg)
  *Qwiic ToF Imager - VL53L5CX*                                                                                                                                                                                                                                                                                                      *Qwiic Mini ToF Imager - VL53L5CX*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Power

Ideally power will be supplied by the Qwiic connector, but if you wish to supply your own power, pins have been broken out along the bottom side of the board labeled `3V3` and `GND`. The input voltage range should be between **2.7**-**3.3V**.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![First two pins from the left on the bottom of the front side of the board are Ground and 3V3](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-PwrPTH.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-PwrPTH.jpg)   [![First two pins from the right on the bottom of the front side of the board are Ground and 3V3.](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-PwrPTH1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-PwrPTH1.jpg)
  *Qwiic ToF Imager - VL53L5CX*                                                                                                                                                                                                                                                                                                               *Qwiic Mini ToF Imager - VL53L5CX*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### I^2^C

The I^2^C pins break out the functionality of the Qwiic connectors. Depending on your application, you can connect to these pins via the plated through holes for SDA and SCL.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![The two middle pins on the bottom edge of the front side of the board are SDA and SCL (in that order from left)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-SDASCL.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-SDASCL.jpg)   [![The two middle pins on the bottom edge of the front side of the board are SDA and SCL (in that order from left)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-SDASCL1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-SDASCL1.jpg)
  *Qwiic ToF Imager - VL53L5CX*                                                                                                                                                                                                                                                                                                                                  *Qwiic Mini ToF Imager - VL53L5CX*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### INT and RST

The interrupt pin is the interrupt output and defaults to an open-drain output. A 47 kΩ pull-up resistor to IOVDD is included.

The reset pin is the I^2^C interface reset pin and is active high. It is pulled to ground with a 47 kΩ resistor.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Interrupt and Reset are the two pins on the far right on the bottom side of the front of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-INTRST.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-INTRST.jpg)   [![Interrupt and Reset are the two pins on the far left on the bottom side of the front of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-INTRST1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-INTRST1.jpg)
  *Qwiic ToF Imager - VL53L5CX*                                                                                                                                                                                                                                                                                                                     *Qwiic Mini ToF Imager - VL53L5CX*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### LP, VDDIO, & VDDA

The pins in this section are specific to the 1\"x1\" board. LP is a *low power* enable pin. Drive this pin to logic 0 to disable the I^2^C comms to reduce power consumption. Drive this pin to logic 1 to enable I^2^C comms. This pin is typically only needed when you need to change the I2C address in multidevice systems. A 47 kΩ pull-up resistor to IOVDD is included so it can be left unconnected.

VDDIO/VDDA: These pins are used as an alternate power supply. By default, VDDIO and VDDA are tied together but by opening the PSU jumper they can be isolated. A user must then provide separate VDDIO and VDDA supplies. This is most applicable for users who want to use IO voltages (1.8, 2.8, or 3.3V) separate from AVDD voltages (2.8 or 3.3V) for maximum power reduction.

[![LP, VDDIO, and VDDA all live on the top side of the back of the board (in that order from left)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-GPIOBack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-GPIOBack.jpg)

### Jumpers

#### INT

Cut the **INT** jumper to remove the 47 kΩ pull-up resistor from the INT pin.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![INT is the top right jumper on the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-INTJumper.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-INTJumper.jpg)   [![The INT jumper is just to the right of middle on the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-INTJumper1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-INTJumper1.jpg)
  *Qwiic ToF Imager - VL53L5CX*                                                                                                                                                                                                                                                                             *Qwiic Mini ToF Imager - VL53L5CX*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### I^2^C

The SparkFun Qwiic ToF Imager Sensor has two 2.2 kΩ pull-up resistors attached to the I^2^C bus by default. If multiple sensors are connected to the bus with the pull-up resistors enabled the parallel equivalent resistance may create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull-up resistors they can be removed by cutting the traces on the corresponding jumper highlighted below.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![The I2C Jumper is at the top left of the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-I2CJumper.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-I2CJumper.jpg)   [![The I2C jumper is on the right side of the back of the board near the qwiic connector](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-I2CJumper1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-I2CJumper1.jpg)
  *Qwiic ToF Imager - VL53L5CX*                                                                                                                                                                                                                                                                                   *Qwiic Mini ToF Imager - VL53L5CX*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### PSU

This jumper is related to the pins specific to the 1\" x 1\" ToF board. By default, VDDIO and VDDA are tied together. Cutting the **PSU** jumper will isolate the power rails. A user must then provide separate VDDIO and VDDA supplies. This is most applicable for users who want to use IO voltages (1.8, 2.8, or 3.3V) separate from AVDD voltages (2.8 or 3.3V) for maximum power reduction.

[![The PSU is the left, bottom jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-PSUJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-PSUJumper.jpg)

#### LED

If minimal power consumption is a concern, or you just don\'t want that Power LED on the front of the board to light up, go ahead and cut this jumper.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![LED is the bottom right jumper](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-LEDJumper.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/18642-SparkFun_Qwiic_ToF_Imager_-_VL53L5CX-LEDJumper.jpg)   [![The LED jumper is on the back of the board to the left of the middle](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-LEDJumper1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/19013-Qwiic_ToF_Imager_Mini_VL53L5CX-LEDJumper1.jpg)
  *Qwiic ToF Imager - VL53L5CX*                                                                                                                                                                                                                                                       *Qwiic Mini ToF Imager - VL53L5CX*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Board Outline

#### Qwiic ToF Imager - VL53L5CX

This sensor measures 1\" x 1\".

[![Board measures 1\" x 1\"](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/BoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/BoardOutline.png)

*Click the image for a closer view*

#### Qwiic Mini ToF Imager - VL53L5CX

This sensor measures 0.5\" x 1\".

[![Board measures 0.5\" x 1\"](https://cdn.sparkfun.com/r/600-600/assets/1/1/8/5/1/19013-Qwiic-ToF-Imager_-VL53L5CX-Mini_BoardDimensions.png)](https://cdn.sparkfun.com/assets/1/1/8/5/1/19013-Qwiic-ToF-Imager_-VL53L5CX-Mini_BoardDimensions.png)

*Click the image for a closer view*

## Hardware Hookup

[] **A note on choosing a board:** The VL53L5CX is unique in that it requires its firmware to be loaded at power-on over the I2C bus. Because this firmware is \~90k bytes, we recommend a microcontroller with enough flash to store VL53L5CX\'s firmware as well as your program code. Sorry, Uno\'s are out. But didn\'t you want an excuse to try out something new? We recommend choosing either an [Artemis Thing Plus](https://www.sparkfun.com/products/15574) or an [ESP32 Thing Plus](https://www.sparkfun.com/products/15663) board as your development board.

Using the Qwiic system, assembling the hardware is simple. All you need to do is connect your VL53L5CX Imager Breakout to your chosen development board with a Qwiic cable or [adapter cable](https://www.sparkfun.com/products/14425). If Qwiic is not your thing, or if your dev board doesn\'t have one built in you can always solder directly to the I^2^C pins. If you are not using a Qwiic-enabled board, make sure your input voltage and logic are either running at **3.3V** or you are shifting the [logic level](https://learn.sparkfun.com/tutorials/logic-levels) from whatever logic your controller runs at to **3.3V**.

\

#### Qwiic ToF Imager - VL53L5CX

[![Artemis thing plus is connected to the ToF with a qwiic cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/SparkFun_Qwiic_ToF_Imager_-_VL53L5CX_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/SparkFun_Qwiic_ToF_Imager_-_VL53L5CX_Hookup_Guide-02.jpg)

*Click the image for a closer view*

\
\

#### Qwiic Mini ToF Imager - VL53L5CX

[![Artemis thing plus is connected to the ToF Mini with a qwiic cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/ToF-Hookup-Mini1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/ToF-Hookup-Min1i.jpg)

*Click the image for a closer view*

[] **Before Use:** Make sure to remove the vacuum tape from the VL53L5CX sensor before first use!

## Software Setup and Programming

**Note:** Make sure you are using the latest stable version of the Arduino IDE on your desktop. If this is your first time using Arduino IDE, library, or board add-on, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

We\'ve written a simple Arduino library to quickly get started reading data from the Qwiic ToF Imager. Install the library through the Arduino Library Manager tool by searching for **\"SparkFun VL53L5CX\"**. Users who prefer to manually install it can get the library from the [GitHub Repository](https://github.com/sparkfun/SparkFun_VL53L5CX_Arduino_Library) or download the ZIP by clicking the button below:

\

[SparkFun Qwiic Time-of-Flight Sensor VL53L5CX Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_VL53L5CX_Arduino_Library/archive/refs/heads/main.zip)

## Example1_DistanceArray 

Hook up your ToF imager to your Artemis Thing Plus via the Qwiic cables, and click \"**File** \> **Examples** \> **SparkFun VL53L5CX Arduino Library** \> **Example1_DistanceArray**\".

[![Where to find the Examples in the arduino menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/Examples.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/Examples.png)

We\'ll assume that you have selected the board (in this case the **SparkFun Artemis Thing Plus**) and the correct COM port at this point. If you have the code open, hit the upload button. Otherwise, copy and paste the following into the Arduino IDE, make sure to select the correct board and COM port, and then upload:

    language:c
    /*
      Read an 8x8 array of distances from the VL53L5CX
      By: Nathan Seidle
      SparkFun Electronics
      Date: October 26, 2021
      License: MIT. See license file for more information but you can
      basically do whatever you want with this code.

      This example shows how to read all 64 distance readings at once.

      Feel like supporting our work? Buy a board from SparkFun!
      https://www.sparkfun.com/products/18642

    */

    #include <Wire.h>

    #include <SparkFun_VL53L5CX_Library.h> //http://librarymanager/All#SparkFun_VL53L5CX

    SparkFun_VL53L5CX myImager;
    VL53L5CX_ResultsData measurementData; // Result data class structure, 1356 byes of RAM

    int imageResolution = 0; //Used to pretty print output
    int imageWidth = 0; //Used to pretty print output

    void setup()
    

      myImager.setResolution(8*8); //Enable all 64 pads

      imageResolution = myImager.getResolution(); //Query sensor for current resolution - either 4x4 or 8x8
      imageWidth = sqrt(imageResolution); //Calculate printing width

      myImager.startRanging();
    }

    void loop()
    
            Serial.println();
          }
          Serial.println();
        }
      }

      delay(5); //Small delay between polling
    }

\
Open up your [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics), make sure the baud rate is set appropriately, and you should see something like the following:

[![Serial Monitor output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/Example1_Output.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/Example1_Output.png)

*Click the image for a closer view*

## Example2_FastStartup 

Hook up your ToF imager to your Artemis Thing Plus via the Qwiic cables, and click \"**File** \> **Examples** \> **SparkFun VL53L5CX Arduino Library** \> **Example2_FastStartup**\".

[![Where to find the Examples in the arduino menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/Examples.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/Examples.png)

We\'ll assume that you have selected the board (in this case the **SparkFun Artemis Thing Plus**) and the correct COM port at this point. If you have the code open, hit the upload button. Otherwise, copy and paste the following into the Arduino IDE, make sure to select the correct board and COM port, and then upload:

    language:c
    /*
      Read an 8x8 array of distances from the VL53L5CX
      By: Nathan Seidle
      SparkFun Electronics
      Date: October 26, 2021
      License: MIT. See license file for more information but you can
      basically do whatever you want with this code.

      This example shows how to setup the I2C bus to minimize the amount
      of time taken to init the sensor.

      At each power on reset, a staggering 86,000 bytes of firmware have to be sent to the sensor.
      At 100kHz, this can take ~9.4s. By increasing the clock speed, we can cut this time down to ~1.4s.

      Two parameters can be tweaked: 

        Clock speed: The VL53L5CX has a max bus speed of 400kHz but we have had success up to 1MHz.

        Max transfer size: The majority of Arduino platforms default to 32 bytes. If you are using one 
        with a larger buffer (ESP32 is 128 bytes for example), this can help decrease transfer times a bit.

      Measurements:
        Default 100kHz clock and 32 byte transfer: 9.4s
        400kHz, 32 byte transfer: 2.8s
        400kHz, 128 byte transfer: 2.5s
        1MHz, 32 byte transfer: 1.65s
        1MHz, 128 byte transfer: 1.4s

      Feel like supporting our work? Buy a board from SparkFun!
      https://www.sparkfun.com/products/18642

    */

    #include <Wire.h>

    #include <SparkFun_VL53L5CX_Library.h> //http://librarymanager/All#SparkFun_VL53L5CX

    SparkFun_VL53L5CX myImager;
    VL53L5CX_ResultsData measurementData; // Result data class structure, 1356 byes of RAM

    int imageResolution = 0; //Used to pretty print output
    int imageWidth = 0; //Used to pretty print output

    void setup()
    

      Serial.print("Firmware transfer time: ");
      float timeTaken = (stopTime - startTime) / 1000.0;
      Serial.print(timeTaken, 3);
      Serial.println("s");

      myImager.setResolution(8*8); //Enable all 64 pads

      imageResolution = myImager.getResolution(); //Query sensor for current resolution - either 4x4 or 8x8
      imageWidth = sqrt(imageResolution); //Calculate printing width

      myImager.startRanging();
    }

    void loop()
    
            Serial.println();
          }
          Serial.println();
        }
      }

      delay(5); //Small delay between polling
    }

\
Open up your [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics), make sure the baud rate is set appropriately, and you should see something like the following:

[![Serial Monitor output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/Example2_SmallOutput.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/Example2_SmallOutput.png)

*Click the image for a closer view*

## Example3_SetFrequency 

Hook up your ToF imager to your Artemis Thing Plus via the Qwiic cables, and click \"**File** \> **Examples** \> **SparkFun VL53L5CX Arduino Library** \> **Example3_SetFrequency**\".

[![Where to find the Examples in the arduino menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/Examples.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/Examples.png)

We\'ll assume that you have selected the board (in this case the **SparkFun Artemis Thing Plus**) and the correct COM port at this point. If you have the code open, hit the upload button. Otherwise, copy and paste the following into the Arduino IDE, make sure to select the correct board and COM port, and then upload:

    language:c
    /*
      Read an 8x8 array of distances from the VL53L5CX
      By: Nathan Seidle
      SparkFun Electronics
      Date: October 26, 2021
      License: MIT. See license file for more information but you can
      basically do whatever you want with this code.

      This example shows how to increase output frequency.

      Default is 1Hz.
      Using 4x4, min frequency is 1Hz and max is 60Hz
      Using 8x8, min frequency is 1Hz and max is 15Hz

      Feel like supporting our work? Buy a board from SparkFun!
      https://www.sparkfun.com/products/18642

    */

    #include <Wire.h>

    #include <SparkFun_VL53L5CX_Library.h> //http://librarymanager/All#SparkFun_VL53L5CX

    SparkFun_VL53L5CX myImager;
    VL53L5CX_ResultsData measurementData; // Result data class structure, 1356 byes of RAM

    int imageResolution = 0; //Used to pretty print output
    int imageWidth = 0; //Used to pretty print output

    void setup()
    

      myImager.setResolution(8 * 8); //Enable all 64 pads

      imageResolution = myImager.getResolution(); //Query sensor for current resolution - either 4x4 or 8x8
      imageWidth = sqrt(imageResolution); //Calculate printing width

      //Using 4x4, min frequency is 1Hz and max is 60Hz
      //Using 8x8, min frequency is 1Hz and max is 15Hz
      bool response = myImager.setRangingFrequency(15);
      if (response == true)
      
        else
          Serial.println(F("Error recovering ranging frequency."));
      }
      else
      

      myImager.startRanging();
    }

    void loop()
    
            Serial.println();
          }
          Serial.println();
        }
      }

      delay(5); //Small delay between polling
    }

\
Open up your [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics), make sure the baud rate is set appropriately, and you should see something like the following:

[![Serial Monitor output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/Example3_Output.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/Example3_Output.png)

*Click the image for a closer view*

## Visualizing the Output

To 'see' the output, *Example4_MaxOutput* can be used with the [SparkFun Processing visualization app](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/SparkFun_VL53L5CX_3D_Depth_Map.zip).

Hook up your ToF imager to your Artemis Thing Plus via the Qwiic cables, and click \"**File** \> **Examples** \> **SparkFun VL53L5CX Arduino Library** \> **Example4_MaxOutput**\".

[![Where to find the Examples in the arduino menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/0/2/Examples.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/Examples.png)

Load this sketch onto your platform and open the serial monitor. You should see the distance array output in CSV format.

Next, download the Processing sketch [here](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/SparkFun_VL53L5CX_3D_Depth_Map.zip) and unzip it into a directory you can locate. If you don't have it installed, download and unzip [Processing](https://processing.org/) into a directory of your choice. Open the *SparkFun VL53L5CX 3D Depth Map* sketch and modify the following line to match your COM port:

[![Modify this line to connect Processing to the sensor](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/Processing_COM_Port_with_VL53L5CX.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/2/Processing_COM_Port_with_VL53L5CX.jpg)

*Modify this line to connect Processing to the sensor*

Once connected you should see output like this:

[![Visualizing the distances](https://cdn.sparkfun.com//assets/parts/1/8/1/6/9/VL53L5CX_Depth_Map_Example.gif)](https://cdn.sparkfun.com//assets/parts/1/8/1/6/9/VL53L5CX_Depth_Map_Example.gif)

*Visualizing the distances*

Our apologies if you suddenly realize an hour has gone by and you've done nothing but wave your hand in front of the sensor and looked at things like coffee cups from a meter away. It's really a lot of fun. Enjoy!

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.