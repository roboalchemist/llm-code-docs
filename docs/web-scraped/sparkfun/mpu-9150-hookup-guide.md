# Source: https://learn.sparkfun.com/tutorials/mpu-9150-hookup-guide

## Introduction

The [MPU-9150](https://www.sparkfun.com/products/11486) is a nine **d**egrees **o**f **f**reedom (9DOF) **i**nertial **m**easurement **u**nit (IMU) in a sigle package. It houses a 3-axis [accelerometer](/tutorials/63), 3-axis [gyroscope](/tutorials/24), 3-axis [magnetometer](https://www.google.com/search?q=magnetometer&ie=utf-8&oe=utf-8) and a Digital Motion Processor™ (DMP™) hardware accelerator engine. The range of each sensor is configurable: the accelerometer\'s scale can be set to ±2g, ±4g, ±6g, ±8g, or ±16g, the gyroscope supports ±250, ±500, and ±2000 °/s, and the magnetometer has full-scale range of ±1200µT (±12 gauss).

[![MPU-9150](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/MPU-9150_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/MPU-9150_2.jpg)

The MPU-9150 supports [I^2^C](/tutorials/82). There is a single reference to in the datasheet for [SPI](/tutorials/16), but all other evidence points to the contrary. We have only testing using I^2^C, and, for the purposes of this tutorial, we will only be covering how to use this device in I^2^C mode.

### Covered In This Tutorial

This tutorial is devoted to all things MPU-9150. First we\'ll introduce you to the breakout board. Then we\'ll switch over to example code and show you how to interface with the board using an Arduino and our \[SFE_MPU-9150 Arduino library\](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/MPU-9150_libraries.zip).

The tutorial is split into the following sections:

- [Breakout Board Overview](#hardware-overview) \-- This page examines the MPU-9150 Breakout Board \-- topics like the pinout, jumpers, and schematic are covered.
- [Hardware Assembly](#hardware-assembly) \-- How to assemble the hardware to run some example code.
- [Installing the Arduino Library](#installing-the-arduino-library) \-- How to install the **Arduino library**, and use a simple example sketch to verify that your hookup works.
- [Resources & Going Further](#resources--going-further) \-- Resources for learning and doing more with the MPU-9150.

### Required Materials

This tutorial explains how to use the MPU-9150 Breakout Board with an Arduino. To follow along, you\'ll need the following materials:

**The MPU-9150 is a 3.3V device!** Supplying voltages greater than 6V can permanently damage the IC. InvenSense recommends running from **2.375V to 3.465V**. As long as your Arduino has a 3.3V supply output, and you\'re OK with using I^2^C, you shouldn\'t need any extra level shifting.

### Suggested Reading

If you\'re not familiar with some of the concepts below, we recommend checking out that tutorial before continuing on.

- [Pull-up Resistors](https://learn.sparkfun.com/tutorials/pull-up-resistors)
- [Accelerometer Basics](https://learn.sparkfun.com/tutorials/accelerometer-basics)
- [Gyroscopes](https://learn.sparkfun.com/tutorials/gyroscope)
- [Inter-IC Communication (I^2^C)](https://learn.sparkfun.com/tutorials/i2c)

## Hardware Overview

### The Pinout

In total, the MPU-9150 Breakout breaks out 11 pins.

[![MPU-9150 product photo](https://cdn.sparkfun.com//assets/parts/7/3/7/6/11486-04.jpg "The SparkFun MPU-9150 Breakout")](https://cdn.sparkfun.com//assets/parts/7/3/7/6/11486-04.jpg)

The bare-minimum connections required are broken out on the left side of the board. These are the power and I^2^C pins (the communication interface the board defaults to):

Pin Label

Pin Function

Notes

GND

Ground

0V voltage supply

VCC

Power Supply

Supply voltage to the chip. Should be regulated between **2.375V and 3.465V**.

SDA

I^2^C: Serial Data

I^2^C: Serial data (bi-directional)

SCL

Serial Clock

I^2^C serial clock (up to 400kHz)

The remaining pins break out additional functionality and interrupt outputs:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Pin Label               Pin Function                          Notes
  ----------------------- ------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  ESD                     Auxiliary I^2^C master serial data    9150 can act as a master or pass-through to additional I^2^C devices.

  ESC                     Auxiliary I^2^C master serial clock   9150 can act as a master or pass-through to additional I^2^C devices.

  COUT                    Clock output                          Outputs a 50% duty cycle square wave (see [register map](https://cdn.sparkfun.com/datasheets/Sensors/IMU/MPU-9150-Register-Map.pdf)).

  CIN                     Clock input                           Optional external reference clock input, grounded through jumper.\
                                                                I using an external clock source, cut \'CLK\' jumper.

  AD0                     I^2^C Slave Address LSB               If low I^2^C address is 0x68, else 0x69. Connected to jumper. (0x68 default)

  FSYNC                   Frame synchronization                 External frame sync input that latches to capture external bus interrupts\
                                                                If using this pin cut \'SYNC\' jumper.

  INT                     Interrupt pin                         Configurable digital output to signal the host processor of an event.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Power Supply

The VCC and GND pins are where you\'ll supply a voltage and 0V reference to the IC. The breakout board does not regulate this voltage, so make sure it falls within the allowed supply voltage range of the MPU-9150: **2.375V to 3.465V**. Logic voltage levels can be as low as 1.8V ±5% up to VCC.

The communication pins are not 5V tolerant, so they\'ll need to be regulated to within a few mV of VDD.

### Communication

SDA, SCL, ESD, and ESC are used for the I^2^C interfaces. The auxiliary clock and data pins will require external pull-up resistors. These ave to be tuned on a case-by-case basis depending on bus capacitance to get proper rise times.

SDA and SCL have integrated 10KΩ pull-ups. If you plan on using more than one I^2^C device on the bus, you might want to remove these pull-ups. If the I^2^C lines are pulled-up too strongly by multiple sets of pull-ups, the bus will likely be out of spec and not function correctly.

The following image shows a stock PCBA on the left, and one with the pull-up resistors removed on the right. To remove these, I recommend reflowing a fair amount of solder onto the resistors. It doens\'t take very long to fully cover all 4 joints with molten solder and the two part will slide right off. So easily in my case that I wasn\'t able to capture a picture of the excess solder before the parts had come off. Wick off the excess solder, wipe clean with some DI water, and you are done.

[![pull-ups removed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/7/removed_resistors.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/removed_resistors.JPG)

### Interrupts

There are a variety of interrupts on the MPU-9150. While connecting up to these is not as critical as the communication or power supply pins, using them will help you get the most out of the chip. The INT pin is a digital output to the host controller. The FSYNC pin can be configured as an interrupt input to optionally be passed through out the INT pin.

These can be programmed to interrupt as either active-high or active-low. More details on these configurations can be found in the product [register map](https://cdn.sparkfun.com/datasheets/Sensors/IMU/MPU-9150-Register-Map.pdf).

### The Jumpers

The most commonly used jumper will be to the address pin (AD0). It defaults to being pulled to ground selecting address 0x68, but with a soldering iron can be changed to be pulled up, switching the I^2^C address to 0x69.

The AD0 pin broken out is connected directly to ground by default. Alternatively it\'s connected straight to VCC. Make sure to remove the solder from both sides of the 3-way jumper before connecting it externally.

[![Address jumper](https://cdn.sparkfun.com//assets/parts/7/3/7/6/11486-04.jpg "The SparkFun MPU-9150 Breakout")](https://cdn.sparkfun.com//assets/parts/7/3/7/6/11486-04.jpg)

*The address selection jumper on the front of the board. Allows you to select the LSB of the I^2^C address*

The intention of these jumpers is to make it as easy-as-possible to use the board; using as few wires as possible. The CLK jumper is used to ground the external clock input as the datasheet recommends when not using an external clock. Make sure to cut this jumper if you attach an external clock to the CIN connection. The SYNC jumper ties FSYNC to ground as the manufacturer instructs one to do when not using it. Make sure to cut this jumper if use the FSYNC through hole connection.

[![Back of MPU-9150 Breakout](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/mpu9150_back.jpg "Back of MPU-9150 Breakout")](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/mpu9150_back.jpgg)

To disable any of these jumpers, whip out your [handy hobby knife](https://www.sparkfun.com/products/9200), and carefully cut the small traces between middle pad and edge pads.

### Funny Business

Be very careful trusting the datasheet. It\'s full of inconsistencies or lacking clarification. For example pin 22. There is a single reference to it functioning as a clock output (next image). There are several places stating that it\'s not to be used, such as the table shown two images below.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/22isClockOut.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/22isClockOut.png)

*Only reference to CLKOUT in datasheet*

\

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/22isntClockOut.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/22isntClockOut.png)

*One of several examples of pin 22 being recommended to not be connected or a clock*

The register map reads \"This bit also enables the clock output.\", but that\'s the only reference. It\'s not even specified clearly to which bit they are referring. We were able to test this, and sure enough it outputs a clock. Maybe this clock is is okay to use. Maybe it was designed for factory testing only.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/clockSignal_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/clockSignal_1.png)

Enabling this clock output was persistent even after a power cycle. Be careful when changing under documented bits in the registers!

SPI is another example of being poorly documented. The following image implies that the address selection line is also SDO. The digital IO power supply pin is also the chip select line. Most serial peripherals we are familiar with don\'t source power out their chip select pins.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/7/SPI.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/SPI.png)

*Only reference to SPI in the datasheet or the register map*

Finally one last quote to show how amazing the datasheet is: \"The internal registers and memory of the MPU-9150 can be accessed using **either** I^2^C at 400 kHz.\" Either fast mode I^2^C, or what? As often as we tell you to RTFM, sometimes the manual can be misleading.

## Hardware Assembly

The basic use case for the MPU-9150 requires four connections to the µController or µProcessor; power, ground, I^2^C clock and data. The following images shows how we used a [SparkFun FTDI Basic Breakout](https://www.sparkfun.com/products/9873), and an [3.3V Arduino Pro Mini](https://www.sparkfun.com/products/11114) to power and interface to an [MPU-9150](https://www.sparkfun.com/products/11486). The demo required the use of an interrupt (right-most yellow jumper) connected to D2 (INT0).

[![hooked-up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/7/HookedUp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/HookedUp.jpg)

*An MPU-9150 wired up to and Arduino Pro Mini for the MPU6050_DMP6 demo*

Make connections to the breakout anyway that makes you happy. The board in the above photo has a right angle header soldered to it. We could have used a straight header, or wire, etc. *Please note that different mounting orientations will alter the orientation of the axes.* Make sure your code matches the physical orientation for your projects.

For this demo, we made the following connections:

  Arduino Pro Mini   MPU‑9150 Breakout   Notes
  ------------------ ------------------- ------------------------------------------------------------------------------
  VCC                VCC                 +3.3V
  GND                GND                 +0V
  SDA                SDA                 Serial data @ +3.3V CMOS logic
  SCL                SCL                 Serial clock @ +3.3V CMOS logic
  D2                 INT                 INT0 on Arduino \| Interrupt output \"totem pole or open-drain\" on MPU-9150

The whole system in our testing was powered via USB through the FTDI basic.

[![USB to FTDI to Pro Mini to MPU-9150 Breakout Fritzing diagram](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/mpu9150_1_1.svg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/7/mpu9150_1_1.svg)

*Electrical connections for demo*

## Installing the Arduino Library

### Download and Install the Library

Visit the [GitHub repository](https://github.com/sparkfun/MPU-9150_Breakout/tree/master/firmware) to download the most recent version of the libraries, or click the link below:

[Download the MPU-9150 Arduino Libraries](https://github.com/sparkfun/MPU-9150_Breakout/archive/master.zip)

For help installing the library, check out our [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) tutorial. You\'ll need to move/copy the both the *I2Cdev* and *MPU6050* directories inside the firmware directory into the *libraries* directory within your Arduino sketchbook. If you don\'t have a directory called *libraries*, create one and drop both directories in there.

The example Arduino code allows you to do things like print raw accelerometer, gyro, and magnetometer data. The original library came from [i2cdevlib.com](http://www.i2cdevlib.com/) and was based on the very similar MPU-6050, which only used an accelerometer and gyro. The MPU-6050 device library was modified to include raw magnetometer data for the MPU-9150.

### Running the MPU6050_DMP6 Example

Now, you can now run the example sketches. Open File ⇒ Examples ⇒ MPU6050 ⇒ Examples ⇒ MPU6050_DMP6. By default, this sketch is configured to do a fun teapot demo that uses processing. That\'s a little more involved than the scope of this hookup guide. We will output the acceleration components with gravity removed.

Uncomment line 102 `//#define OUTPUT_READABLE_REALACCEL`. Comment out line 112 `#define OUTPUT_TEAPOT`. Compile and upload the sketch. When it finishes uploading, open the [serial monitor](/tutorials/112), and set the baud rate to 115200 baud. You should see this:

    Initializing I2C devices...
    Testing device connections...
    MPU6050 connection successful

    Send any character to begin DMP programming and demo:

At the top of the serial monitor type any \'normal\' character (such as alphanumeric) and press Send. Your system should respond with:

    Initializing DMP...
    Enabling DMP...
    Enabling interrupt detection (Arduino external interrupt 0)...
    DMP ready! Waiting for first interrupt...

If you have the interrupt line connected properly, you should see lines similar to this:

    areal   -8680   1460    -1448
    areal   -9721   1460    -1463
    ...