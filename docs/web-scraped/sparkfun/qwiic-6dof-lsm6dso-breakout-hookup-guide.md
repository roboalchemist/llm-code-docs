# Source: https://learn.sparkfun.com/tutorials/qwiic-6dof-lsm6dso-breakout-hookup-guide

## Introduction

**Note:** This tutorial is for the LSM6DSO. It is important to note that last designation for the IC is the letter `O` as opposed to the number `0`. There is also the LSM6DS0 that was released by STMicroelectronics but it is EOL.

The [LSM6DSO](https://www.sparkfun.com/products/18020) is an accelerometer and gyroscope sensor with a giant 9 kbyte buffer and embedded processing interrupt functions, specifically targeted at the cellphone market. The sensor is super-flexible and can be configured specifically for an application. We\'ve put together a driver and slew of examples to help you explore the possibilities.

[![SparkFun 6 Degrees of Freedom Breakout - LSM6DSO (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/2/4/2/18020-SparkFun_6_Degrees_of_Freedom_Breakout_-_LSM6DSO__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-6-degrees-of-freedom-breakout-lsm6dso-qwiic.html)

### [SparkFun 6 Degrees of Freedom Breakout - LSM6DSO (Qwiic)](https://www.sparkfun.com/sparkfun-6-degrees-of-freedom-breakout-lsm6dso-qwiic.html) 

[ SEN-18020 ]

The LSM6DSO 6DoF Breakout is an accelerometer and gyroscope sensor with a giant 9kB FIFO buffer and embedded processing inter...

[ [\$16.95] ]

Some of the things the LSM6DSO can do:

- Read accelerometer data up to 6.66 kilosamples per second, for super accurate movement sensing
- Read gyroscope data up to 6.66 kilosamples per second
- Operates at 0.55mA for up to 6.66 ksps modes
- Read temperature
- Buffer up to 9 kbytes of data between reads (built-in FIFO)
- Count steps (Pedometer)
- Detect shocks, tilt, motion, taps, double-taps
- Host other sensors into its FIFO
- Drive interrupt pins by embedded functions or by FIFO low-capacity/overflow warning.

### Covered In This Tutorial

This tutorial gives you all you need to get going with the LSM6DSO. We\'ll introduce you to the chip itself, then the breakout board. Then we\'ll switch over to example code and show you how to interface with the board using an Arduino and our [SparkFun LSM6DSO Arduino library](https://github.com/sparkfun/SparkFun_Qwiic_6DoF_LSM6DSO_Arduino_Library).

The tutorial is split into the following pages:

- **Introduction** - Basic information
- **Hardware Overview** - Hardware connections
- **Hardware Assembly** - Connect to the LSM6DSO by I2C or SPI
- **Installing the Arduino Library** - Includes overview of the examples
- **Using the Arduino Library** - Explains the user API
- **Resources and Going Further** - Links to the datasheet and application notes, plus inspirational projects

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun 6 Degrees of Freedom Breakout - LSM6DSO (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/2/4/2/18020-SparkFun_6_Degrees_of_Freedom_Breakout_-_LSM6DSO__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-6-degrees-of-freedom-breakout-lsm6dso-qwiic.html)

### [SparkFun 6 Degrees of Freedom Breakout - LSM6DSO (Qwiic)](https://www.sparkfun.com/sparkfun-6-degrees-of-freedom-breakout-lsm6dso-qwiic.html) 

[ SEN-18020 ]

The LSM6DSO 6DoF Breakout is an accelerometer and gyroscope sensor with a giant 9kB FIFO buffer and embedded processing inter...

[ [\$16.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Reversible USB A to Reversible Micro-B Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/7/15428-Reversible_USB_A_to_Reversible_Micro-B_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-0-8m.html)

### [Reversible USB A to Reversible Micro-B Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-0-8m.html) 

[ CAB-15428 ]

These 0.8m cables have minor, yet genius modifications that allow both ends to be plugged into their ports regardless of thei...

[ [\$5.50] ]

**[] Warning!** The LSM6DSO is a 3.3V device! Supplying voltages greater than \~3.6V can permanently damage the IC. As long as your Arduino has a 3.3V supply output, and you\'re ok with using I^2^C, you shouldn\'t need any extra level shifting. If you want to use SPI, you may need a [level shifter](https://www.sparkfun.com/products/12009).\
\

[![SparkFun Logic Level Converter - Bi-Directional](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/2/2/12009-06.jpg)](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html)

### [SparkFun Logic Level Converter - Bi-Directional](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html) 

[ BOB-12009 ]

The SparkFun bi-directional logic level converter is a small device that safely steps down 5V signals to 3.3V AND steps up 3....

[ [\$3.95] ]

[![SparkFun Level Translator Breakout - PCA9306](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/0/15439-SparkFun_Level_Translator_Breakout_-_PCA9306-01a.jpg)](https://www.sparkfun.com/sparkfun-level-translator-breakout-pca9306.html)

### [SparkFun Level Translator Breakout - PCA9306](https://www.sparkfun.com/sparkfun-level-translator-breakout-pca9306.html) 

[ BOB-15439 ]

Different parts sometimes use different voltage levels to communicate. This PCA9306 Level Translator can be the key to making...

[ [\$5.25] ]

A logic level shifter is required for any 5V-operating Arduino (Uno, RedBoard, Leonardo, etc). If you use a 3.3V-based \'duino \-- like the [Arduino Pro 3.3V](https://www.sparkfun.com/products/10914) or [3.3V Pro Mini](https://www.sparkfun.com/products/11114) \-- there is no need for level shifting.\
\
The RedBoard Qwiic has two level shifters on the I^2^C lines so you do not need to worry about the logic levels when using the board in I^2^C mode. You could also adjust the system voltage by [cutting the jumper and adding solder](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) to the 3.3V side when using the board in SPI.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/1/Adjust_RedBoard_Logic_Levels_3V3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/Adjust_RedBoard_Logic_Levels_3V3.jpg)

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic) .

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you aren't familiar with the following concepts, we also recommend checking out a few of these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/gyroscope)

### Gyroscope 

Gyroscopes measure the speed of rotation around an axis and are an essential part in determines ones orientation in space.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

In this section, we\'ll highlight the features of the board. We recommend looking at the datasheet and application notes linked in the Resources and Going Further for more information on the LSM6DSO. Open them in a non-browser viewer that can display the index/table of contents in a pane. There is so much information, paned viewing is a must!

### Power and Logic Levels

We recommend powering the board through the Qwiic connector when quickly prototyping. For a more secure connection, you can always [solder to the PTH](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) labeled **3V3** and **GND**. The recommended input voltage when using the board with a microcontroller is **3.3V** if you are using the Qwiic connector. However, you can use a regulated supply voltage between 1.71V and 3.6V to power the sensor. The logic levels will match the input voltage (e.g. if the sensor is powered at 3.3V, the logic level will be 3.3V as well).

[![Power Net](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Power.jpg)

### I^2^C

The main method of reading the LSM6DSO is through the I^2^C bus. The board includes two Qwiic connectors for fast prototyping and removes the need for soldering. All you need to do is plug a Qwiic cable into the Qwiic connector and voila! You can also [solder to the PTHs](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) labeled as **SDA** and **SCL** as an alternative. The default address for the IC is **0x6B**. However, you can adjust the jumper on the back of the board to change the address to **0x6A**.

[![I2C Pins and Qwiic Connectors](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_I2C.jpg)

### SPI

If you decide to use a [SPI bus](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all), you will need to [solder header pins or wires](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) to the board.

- **SDA/SDI** - Device data in. Note that the SDA pin used for I^2^C is also the SDI pin used for SPI. Flipping the board to the bottom side will show the label for the SPI pin.
- **SCL** - Serial clock for either I^2^C or SPI.
- **SDO** - Device data out. By default, the SDO pin is connected to power to set the I^2^C address. Make sure to cut the trace as explained below if you decide to use this sensor in SPI mode.
- CS
  \- Chip select.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top of Board for SPI](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Top_SPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Top_SPI.jpg)   [![Bottom of Board for SPI](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Back_SPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Back_SPI.jpg)
  *Top of Board for SPI*                                                                                                                                                                                                                                                    *Bottom of Board for SPI*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using the board in SPI mode, you will need to cut the I^2^C jumper for the default address (e.g. 0x6B) on the back and leave the jumper pads unconnected when using SPI.

[![Cut Jumper for SPI Mode](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Cut_Jumper_for_SPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Cut_Jumper_for_SPI.jpg)

### Interrupt Pins

INT1 and INT2 are programmable interrupts for the accelerometer and gyroscope. They can be set to alert on over/under thresholds, data ready, or FIFO overruns. Make sure these are connected to an INPUT pin to prevent driving 5v back into the LSM6DSO.

[![Interrupt Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Interrupts.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Interrupts.jpg)

There are a variety of interrupts on the LSM6DSO. While connecting these is not as critical as the communication or power supply pins, using them will help you get the most out of the chip.

The interrupt pins are **INT1** and **INT2**. One or both pins can be software configured and mapped to the following conditions:

- Step detected
- Step detected after delta time
- Step counter overflowed
- Significant motion (shock, drop)
- FIFO full
- FIFO overrun
- FIFO threshold reached (Datasheet calls this the \"watermark\")
- Boot status
- Gyroscope data ready
- Accelerometer data ready
- Inactivity
- Single tap
- Wake-up
- Free-fall
- Double tap
- 6D (orientation)
- Tilt
- Timer
- Ironing interrupt

Only a few interrupt examples are provided. See the datasheet and application guide for using the advanced interrupt features.

### Auxiliary Pins

The auxiliary serial data output pins are used to attach slave I^2^C and auxiliary SPI 3/4-wire devices for FIFO data collection. This function is not covered in this tutorial.

- OCS - aux chip select
- SCX - aux serial clock
- SDIX - aux serial data input
- SDOX - aux serial data output

[![Auxiliary Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Auxiliary.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Auxiliary.jpg)

### Reference Axis

For easy reference, we\'ve documented the 6DoF\'s vectors with 3D Cartesian coordinate axes on the top and bottom side of the board. Make sure to orient and mount the board correctly for your application. Remember, it\'s all relative.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![6DoF Reference (Top)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Top_6DoF_Reference.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Top_6DoF_Reference.jpg)   [![6DoF Reference (Bottom)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Bottom_6DoF_Reference.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Bottom_6DoF_Reference.jpg)
  *6DoF Reference (Top)*                                                                                                                                                                                                                                                                          *6DoF Reference (Bottom)*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### LED

The board includes an LED indicator that lights up when there is power available.

[![LED](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_LED.jpg)

### Jumper Pins

There are five jumpers on the back of the board. For more information, check out our [tutorial on working with jumper pads and PCB traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all) should you decide to cut the traces with a hobby knife.

- **LED** - This is connected to the PWR LED on the top of the board. Cutting this disables the LED.
- **I2C** - The I2C jumper is connected to the 4.7kΩ pull-up resistors for the I^2^C bus. Most of the time you can leave these alone unless your project requires you to [disconnect the pull-up resistors](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level). SPI works with these connected but really should be cut apart for better signal shape at high speeds and to lower power consumption.
- **0x6B/0x6A** - These jumpers are used to select the address 0x6B (default) or 0x6A for I^2^C communication. This jumper must be **opened for SPI mode** or the SDO line will not supply data.
- **SCX** - By default, this pin is connected to GND since ST recommends pulling the unused SCX to power or ground when not in use. For most users, you can leave this jumper alone. If your project requires connecting slave devices to the auxiliary pin, cut this trace.
- **SDIX** - By default, this pin is connected to GND since ST recommends pulling the unused SDIX to power or ground when not in use. For most users, you can leave this jumper alone. If your project requires connecting slave devices to the auxiliary pin, cut this trace.

[![Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/18020-SparkFun_Qwiic_6_Degrees_of_Freedom_LSM6DSO_Jumpers.jpg)

### Board Dimensions

The board uses the standard Qwiic size 1.0\"x1.0\" with four mounting holes by each corner.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/9/9/6/f/a/SparkFun_Qwiic_6DoF_LSMDSO_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/9/9/6/f/a/SparkFun_Qwiic_6DoF_LSMDSO_Board_Dimensions.png)

## Hardware Assembly

### I^2^C Mode

For this example, we\'ll use a RedBoard Qwiic and associated USB cable. With that and a Qwiic cable, the assembly is very simple. Plug a Qwiic cable between the RedBoard Qwiic and the Qwiic 6DoF LSM6DSO. If you\'re going to be [soldering to the through hole pins](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering), then just attach lines to power, ground, and the I^2^C data lines to the microcontroller of your choice. Just make sure to match to use a logic level converter to match the 3.3V logic on the Qwiic 6DoF.

[![Qwiic Cable Connecting Arduino and LSM6DSO](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/6/4/Qwiic_6_Degrees_of_Freedom_LSM6DSO_Arduino_Connected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/Qwiic_6_Degrees_of_Freedom_LSM6DSO_Arduino_Connected.jpg)

### SPI Mode

Here\'s how to connect the SPI lines to a 5V system like the RedBoard Qwiic using a [SparkFun Logic Level Converter](https://www.sparkfun.com/products/12009). Be sure to orient the converter\'s low side to the LSM6DSO. If using a Teensy or other 3.3V microcontroller, the SPI lines can be connected directly!

[![Fritzing Diagram of LSM6DSO in SPI Mode with an Arduino and Logic Level Converter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/6/4/SparkFun_Qwiic_6DoF_LSM6DSO_SPI_Mode_Arduino_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/4/SparkFun_Qwiic_6DoF_LSM6DSO_SPI_Mode_Arduino_bb.jpg)

**Note:** When using the LSM6DSO, make sure to firmly attach the thing that is being measured to filter movement noise. To secure the board using its mounting holes, you will need screws and standoffs.

## Installing the Arduino Library

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We\'ve written an Arduino library to help make interfacing with the LSM6DSO\'s gyro, accelerometer, and temperature sensor as easy-as-possible. Download using the Arduino library manager by searching for \'**SparkFun Qwiic 6DoF LSM6DSO Arduino Library**\' or you can manually install the library by downloading the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_6DoF_LSM6DSO_Arduino_Library):

[Download the SparkFun Qwiic 6DoF LSM6DSO Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_6DoF_LSM6DSO_Arduino_Library/archive/refs/heads/main.zip)

**Note:** The LSM6DSO library is based on the LSM6DS3\'s Arduino Library. While the libraries are similar, the LSM6DS3\'s library will not work with the LSM6DSO. Make sure to download the correct library for your IC!

## Examples

### Basic Readings

There are a few examples in the library but we recommend using the Basic Readings in I^2^C mode to get started.

Hook up the LSM6DSO to the I^2^C bus, and click \"**File** \> **Examples** \> **SparkFun Qwiic 6 DoF - LSM6DSO** \> **Basic_Readings**\". This example demonstrates the highest level of usage. Besides setting up the Wire library and bus, you will you have to do is create a variable of the type \"`LSM6DSO`\", set it to `.begin();`, and initialize the `BASIC_SETTINGS`. To read the accelerometer, gyro, or temperature sensor using the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux).

We\'ll assume that you have selected the board (in this case the **Arduino Uno**), COM port at this point. If you have the code open, hit the upload button. Otherwise, copy and paste the following into the Arduino IDE.

    language:c
    /******************************************************************************
    Basic_Readings.ino

    https://github.com/sparkfun/SparkFun_Qwiic_6DoF_LSM6DSO
    https://github.com/sparkfun/SparkFun_Qwiic_6DoF_LSM6DSO_Arduino_Library

    Description:
    Most basic example of use.

    Example using the LSM6DSO with basic settings.  This sketch collects Gyro and
    Accelerometer data every second, then presents it on the serial monitor.

    Development environment tested:
    Arduino IDE 1.8.2

    This code is released under the [MIT License](http://opensource.org/licenses/MIT).
    Please review the LICENSE.md file included with this example. If you have any questions 
    or concerns with licensing, please contact techsupport@sparkfun.com.
    Distributed as-is; no warranty is given.
    ******************************************************************************/

    #include "SparkFunLSM6DSO.h"
    #include "Wire.h"
    //#include "SPI.h"

    LSM6DSO myIMU; //Default constructor is I2C, addr 0x6B

    void setup() 

      if( myIMU.initialize(BASIC_SETTINGS) )
        Serial.println("Loaded Settings.");

    }

    void loop()
    

After uploading, open the Serial Monitor and set it at **115200**.