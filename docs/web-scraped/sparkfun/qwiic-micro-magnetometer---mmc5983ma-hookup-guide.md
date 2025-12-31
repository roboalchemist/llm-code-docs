# Source: https://learn.sparkfun.com/tutorials/qwiic-micro-magnetometer---mmc5983ma-hookup-guide

## Introduction

The [SparkFun Qwiic Micro MMC5983MA Magnetometer](https://www.sparkfun.com/products/19921) is a micro-sized, 0.75in. by 0.30in. sensor that utilizes the highly sensitive triple-axis magnetometer by MEMSIC. We\'ve attached the magnetometer IC onto an incredibly small Qwiic board form factor that we like to call Qwiic Micro! The MMC5983MA is capable of sensing down to 0.4mG, enabling a heading accuracy of ±0.5°. The Qwiic MMC5983MA IMU communicates over I^2^C by default utilizing our handy Qwiic Connect System, so no soldering is required to connect it to the rest of your boards.

Saturation is a problem for all mag sensors. The MMC5983MA has built-in degaussing circuitry to clear any residual magnetization. Output rates of 1000Hz, ±8G FSR, and 18-bit resolution make the MMC5983MA a phenomenal magnetic sensor for electronic compass applications.

[![SparkFun Micro Magnetometer - MMC5983MA (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/6/5/3/19921_03.jpg)](https://www.sparkfun.com/sparkfun-micro-magnetometer-mmc5983ma-qwiic.html)

### [SparkFun Micro Magnetometer - MMC5983MA (Qwiic)](https://www.sparkfun.com/sparkfun-micro-magnetometer-mmc5983ma-qwiic.html) 

[ SEN-19921 ]

The SparkFun Qwiic Micro MMC5983MA Magnetometer is a micro-sized 0.75in. by 0.30in. sensor that utilizes a highly sensitive t...

[ [\$18.50] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

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

The beautiful thing about this Qwiic board is that it is extremely simple. Let\'s dive in and have a look at its features!

### MMC5983MA

The MMC5983MA is an AEC-Q100 qualified, fully integrated 3-axis magnetic sensor with on-chip signal processing and integrated I^2^C/SPI bus. It has superior dynamic range and accuracy with ±8G FSR, 18bit operation, 0.4mG total RMS noise, and can enable heading accuracy of 0.5º. More information can be found in the [datasheet](https://cdn.sparkfun.com/assets/a/b/7/7/2/19921-09102019_MMC5983MA_Datasheet_Rev_A-1635338.pdf).

[![Magnetometer is located in the center of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_Magnetometer.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_Magnetometer.jpg)

### Qwiic Connector

Our Qwiic Ecosystem makes sensors pretty much plug and play. There\'s a Qwiic connector on the side of the Qwiic Micro Magnetometer to provide power and I^2^C connectivity simultaneously. The default I^2^C address is 0x30.

[![Qwiic connector is located at the bottom of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_QwiicConnector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_QwiicConnector.jpg)

### Pins

We\'ve broken out the interrupt and ground pins to PTH on either side of the board. The interrupt pin is active high - writing "1" will enable the interrupt for completed measurements. Once a measurement is finished, either magnetic field or temperature, an interrupt will be sent to the host.

[![INT and GND pins are on either side of the mounting hole at the top of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_GPIO.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_GPIO.jpg)

### Jumpers

#### I^2^C

Like our other Qwiic boards, the Qwiic Micro Magnetometer comes equipped with pull-up resistors on the clock and data pins. If you are daisy-chaining multiple Qwiic devices, you will want to cut this jumper; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. To disable the pull up resistors, use an X-acto knife to cut the joint between the two jumper pads highlighted here.

[![I2C Jumper is in the center bottom of the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_I2CJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_I2CJumper.jpg)

#### LED

If power consumption is an issue, cutting this jumper will disable the Power LED on the front of the board.

[![LED Jumper is in the left bottom of the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_LEDJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_MicroMagnetometer_LEDJumper.jpg)

### Board Outline

This ultra tiny Qwiic breakout board measures 0.75\" x 0.30\".

[![This ultra tiny Qwiic breakout board measures 0.75\" x 0.30\". ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/19921_QwiicMagnetometer-MMC5983MA-BoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/19921_QwiicMagnetometer-MMC5983MA-BoardOutline.png)

## Hardware Hookup

Grab your Qwiic cable and plug one end into the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) and the other end into the Qwiic Micro Magnetometer. Voila!

[![This image shows stuff plugged in](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/MicroMagnetometer_Action.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/MicroMagnetometer_Action.jpg)

## Software Setup and Programming

**Note:** Make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We\'ve written a simple Arduino library to quickly get started reading data from the Qwiic Micro Magnetometer. Install the library through the Arduino Library Manager tool by searching for **\"SparkFun MMC5983MA\"**. Users who prefer to manually install it can get the library from the [GitHub Repository](https://github.com/sparkfun/SparkFun_MMC5983MA_Magnetometer_Arduino_Library) or download the ZIP by clicking the button below:

\

[SparkFun Qwiic Micro Magnetometer - MMC5983MA Arduino Library](https://github.com/sparkfun/SparkFun_MMC5983MA_Magnetometer_Arduino_Library/archive/refs/heads/main.zip)

## Example 1: I2C Simple Measurement

Now that we\'ve got our library installed and our hardware all hooked up, let\'s look at some examples.

This first example just does some basic measurements. To find Example 1, go to **File** -\> **Examples** -\> **SparkFun MMC5983MA Magnetometer Arduino Library** -\> **Example1-I2C_Simple_measurement**.

[![Image shows menu pulldown as described above](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/Example1_Menu.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/Example1_Menu.png)

*Having a hard time seeing the image? Click the image for a closer look.*

Make sure you have the correct board and port selected. For this tutorial, your selections should look something like this:

[![Select the SparkFun RedBoard and the correct COM port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/Example1_BoardDefAndPort.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/Example1_BoardDefAndPort.png)

*Having a hard time seeing the image? Click the image for a closer look.*

Once you\'re ready to go, go ahead and hit the upload button (the right facing arrow button under the \"Edit\" menu item). Once your code is uploaded, open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and you\'ll see X, Y, and Z values start printing out.

[![Serial Monitor Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/Example1_SerialOutput.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/Example1_SerialOutput.png)

*Having a hard time seeing the image? Click the image for a closer look.*

## Example 2: I2C Digital Compass

Example 2 shows how to compute the heading based on the basic X/Y/Z readings from the sensor over Qwiic. To find this example, go to **File** -\> **Examples** -\> **SparkFun MMC5983MA Magnetometer Arduino Library** -\> **Example2-I2C_Digital_compass**.

[![Image shows menu pulldown as described above](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/Example2_Menu.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/Example2_Menu.png)

*Having a hard time seeing the image? Click the image for a closer look.*

Make sure you have the correct board and port selected. For this tutorial, your selections should look something like this:

[![Select the SparkFun RedBoard and the correct COM port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/Example1_BoardDefAndPort.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/Example1_BoardDefAndPort.png)

*Having a hard time seeing the image? Click the image for a closer look.*

Once you\'re ready to go, go ahead and hit the upload button (the right facing arrow button under the \"Edit\" menu item). Once your code is uploaded, open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and you\'ll see compass readings start printing out.

[![Serial Monitor Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/Example2_SerialOutput.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/Example2_SerialOutput.png)

*Having a hard time seeing the image? Click the image for a closer look.*

If you look at the above image, you\'ll see where I abruptly changed the direction the sensor was pointing.

## Example 3: I2C Continuous Measurement

Example 3 demonstrates how to use interrupts to quickly read the sensor instead of polling. To find this example, go to **File** -\> **Examples** -\> **SparkFun MMC5983MA Magnetometer Arduino Library** -\> **Example3-I2C_Continuous_measurement**.

[![Image shows menu pulldown as described above](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/Example3_Menu.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/Example3_Menu.png)

*Having a hard time seeing the image? Click the image for a closer look.*

Make sure you have the correct board and port selected. For this tutorial, your selections should look something like this:

[![Select the SparkFun RedBoard and the correct COM port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/Example1_BoardDefAndPort.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/Example1_BoardDefAndPort.png)

*Having a hard time seeing the image? Click the image for a closer look.*

Once you\'re ready to go, go ahead and hit the upload button (the right facing arrow button under the \"Edit\" menu item). Once your code is uploaded, open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and you\'ll see compass readings start printing out.

[![Serial Monitor Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/1/9/Example3_SerialOutput.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/1/9/Example3_SerialOutput.png)

*Having a hard time seeing the image? Click the image for a closer look.*

## Examples 4 and 5

**A Note on Examples 4 and 5:** This library is shared with the SparkX Breakout Board using the same MMC5983MA chip. However, due to the tiny size of this Micro Breakout Board, SPI functionality is not available for the Qwiic Micro Magnetometer. The two SPI examples included with the Arduino Library are for use with the SparkX board only.

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.