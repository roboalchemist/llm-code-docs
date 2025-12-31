# Source: https://learn.sparkfun.com/tutorials/qwiic-pro-kit-project-guide

## Introduction

**Note:** Unfortunately, the accelerometer (MMA8452Q) included in this kit went EOL. If you are looking for the latest version of this kit and tutorial, head over to the [MicroMod Qwiic Pro Kit Project Guide](https://learn.sparkfun.com/tutorials/micromod-qwiic-pro-kit-project-guide)!

The [Qwiic Pro Kit](https://www.sparkfun.com/products/15349) was designed to allow users to get started with Arduino without the need for soldering or a breadboard. We\'ve included three inputs (a joystick, accelerometer, and proximity sensor) and one display that can be daisy chained to your Arduino. Hooking up a handful of inputs and outputs to an Arduino has never been so easy with the Qwiic system!

[![SparkFun Qwiic Pro Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/8/7/6/15349-Qwiic_Starter_Kit-01.jpg)](https://www.sparkfun.com/products/15349)

### [SparkFun Qwiic Pro Kit](https://www.sparkfun.com/products/15349) 

[ KIT-15349 ]

This kit provides you with a RedBoard Turbo, two sensors, a joystick, and an OLED screen as well as all the cables you need t...

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials to set up the RedBoard Turbo and get a feel for each Qwiic component.

[](https://learn.sparkfun.com/tutorials/redboard-turbo-hookup-guide)

### RedBoard Turbo Hookup Guide 

January 24, 2019

An introduction to the RedBoard Turbo. Level up your Arduino-skills with the powerful SAMD21 ARM Cortex M0+ processor!

[](https://learn.sparkfun.com/tutorials/qwiic-micro-oled-hookup-guide)

### Qwiic Micro OLED Hookup Guide 

Get started displaying things with the Qwiic Micro OLED.

[](https://learn.sparkfun.com/tutorials/qwiic-accelerometer-mma8452q-hookup-guide)

### Qwiic Accelerometer (MMA8452Q) Hookup Guide 

Freescale's MMA8452Q is a smart, low-power, three-axis, capacitive micro-machined accelerometer with 12-bits of resolution. It's perfect for any project that needs to sense orientation or motion. We've taken that accelerometer and stuck it on a Qwiic-Enabled breakout board to make interfacing with the tiny, QFN package a bit easier.

[](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide)

### Qwiic Joystick Hookup Guide 

Looking for an easy way to implement a joystick to your next Arduino or Raspberry Pi project? This hookup guide will walk you through using the Qwiic Joystick with the Arduino IDE on a RedBoard Qwiic and in Python on a Raspberry Pi.

[](https://learn.sparkfun.com/tutorials/qwiic-proximity-sensor-vcnl4040-hookup-guide)

### Qwiic Proximity Sensor (VCNL4040) Hookup Guide 

The SparkFun Qwiic Proximity Sensor is a great, qualitative proximity (up to 20 cm) and light sensor. This hookup guide covers a few examples to retrieve basic sensor readings.

## Kit Contents

You will find the following parts in the kit.

[![Qwiic Pro Kit Contents](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/3/15349-Qwiic_Starter_Kit_Parts_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/3/15349-Qwiic_Starter_Kit_Parts_Arduino.jpg)

- 1x [RedBoard Turbo (SAMD21) Development Board](https://www.sparkfun.com/products/14812)
- 1x [Reversible USB A to Reversible Micro-B Cable - 0.8m](https://www.sparkfun.com/products/15428)
- Inputs
  - 1x [Qwiic Joystick](https://www.sparkfun.com/products/15168)
  - 1x [Qwiic Triple Axis Accelerometer (MMA8452Q)](https://www.sparkfun.com/products/14587)
  - 1x [Qwiic Proximity Sensor (VCNL4040)](https://www.sparkfun.com/products/15177)
- Outputs
  - 1x [Qwiic Micro OLED Display](https://www.sparkfun.com/products/14532)
- Qwiic Cables
  - 2x [50mm](https://www.sparkfun.com/products/14426)
  - 2x [100mm](https://www.sparkfun.com/products/14427)
  - 1x [200mm](https://www.sparkfun.com/products/14428)
  - 1x [500mm](https://www.sparkfun.com/products/14429)

## Hardware Hookup

The Qwiic connection system makes it easy to connect the boards together. Simply grab a Qwiic cable of your choice to connect. If you are using the demo code from this tutorial to play micro pong, you will need to connect all the boards together. We recommend using longer cable lengths for users using the Qwiic boards to control each paddle and placing them on opposite sides of the micro OLED. We also found it easier to add the accelerometer at the end of the daisy chain since the board requires movement. Additionally, you will need to orient the micro OLED so that the paddle is on the side of the player\'s Qwiic board after uploading the example code.

[![Qwiic Boards Daisy Chained](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/3/Qwiic_Starter_Kit_Daisy_Chained_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/3/Qwiic_Starter_Kit_Daisy_Chained_I2C.jpg)

**Warning!** You will need to connect all of the boards together when using the demo code in this tutorial. Otherwise, you will need to comment out lines of code for the Qwiic board that is not connected to the daisy chain.

[**Note:**](#redboard-qwiic) The code used in this tutorial is also compatible with Atmega328P-based Arduinos like the RedBoard Qwiic! If you purchased the components separately or Qwiic Ideation Kit, the setup is the same. Instead of the RedBoard Turbo, you would be using the RedBoard Qwiic. Check the [note below for more information](https://learn.sparkfun.com/tutorials/qwiic-pro-kit-project-guide#atmega328p) when compiling for the Atmega328P-based microcontrollers!\
\

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun Qwiic Ideation Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/1/2/16262-SparkFun_Qwiic_Ideation_Kit-01b.jpg)](https://www.sparkfun.com/sparkfun-qwiic-ideation-kit.html)

### [SparkFun Qwiic Ideation Kit](https://www.sparkfun.com/sparkfun-qwiic-ideation-kit.html) 

[ KIT-16262 ]

The SparkFun Qwiic Ideation Kit is the smorgasbord of our best and most popular Qwiic boards that allows you to bring any pro...

**Retired**

## Installing the Board Add-Ons and Drivers

**Note:** This code/library has been written and tested on Arduino IDE version v1.8.8. Otherwise, make sure you are using the latest stable version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

There are a few board add-ons to install before you are able to upload code to your RedBoard Turbo. If you have not already, make sure to check out the RedBoard Turbo\'s hookup guide to install the SAMD21 and SparkFun board add-ons.

[Installing the SAMD and SparkFun Board Add-Ons](https://learn.sparkfun.com/tutorials/redboard-turbo-hookup-guide#setting-up-arduino)

### Drivers

**Heads up!** Please be aware that the RedBoard Turbo is **NOT currently supported on Windows 8** due to a lack of support drivers for those specific OS\'s.

The RedBoard Turbo is now easier than ever to program, thanks the [UF2 bootloader](https://learn.sparkfun.com/tutorials/redboard-turbo-hookup-guide#uf2-bootloader). With this bootloader, the RedBoard Turbo shows up on your computer as a USB storage device **without having to install drivers** for Windows 10, Mac, and Linux!

However, if you are using a Windows 7 OS, you will need to install SAMD drivers. Head to the RedBoard Turbo\'s hookup guide for more information about [installing drivers for Windows 7](https://learn.sparkfun.com/tutorials/redboard-turbo-hookup-guide#windows-7).

## Installing the Library

**Note:**If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

SparkFun has written a library for the Qwiic enabled joystick, triple axis accelerometer (MMA8452Q), proximity sensor (VCNL4040), and 64x48 micro OLED. You can obtain these libraries through the Arduino Library Manager. Search for the following terms to automatically install the latest versions of each library. If you have issues compiling, you may need to download the respective library versions listed below.

- [SparkFun Joystick](https://github.com/sparkfun/SparkFun_Qwiic_Joystick_Arduino_Library) (v1.0.4)
- [SparkFun MMA8452Q](https://github.com/sparkfun/SparkFun_MMA8452Q_Arduino_Library) (v1.4.0)
- [SparkFun VCNL4040](https://github.com/sparkfun/SparkFun_VCNL4040_Arduino_Library) (v1.0.2)
- [SparkFun micro OLED](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library) (v1.2.5)

If you prefer downloading the libraries manually, you can grab them from each of the respective GitHub repositories.

[SparkFun Qwiic Joystick Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_Joystick_Arduino_Library/archive/master.zip)

[SparkFun MMA8452Q Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_MMA8452Q_Arduino_Library/archive/master.zip)

[SparkFun VCNL4040 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_VCNL4040_Arduino_Library/archive/master.zip)

[SparkFun Micro OLED Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library/archive/master.zip)

## Example Code

We recommend grabbing the code from its the [GitHub repository](https://github.com/sparkfun/Qwiic-Pro-Kit-Code). Otherwise, you can download the zipped file from the link below.

[Download the Qwiic Pro Kit Code (ZIP)](https://github.com/sparkfun/Qwiic-Pro-Kit-Code/archive/master.zip)

After downloading, unzip the files and open the *QwiicStarterExample.ino* sketch. It should be located in the downloads folder similar to this path: **\.../Firmware/Arduino/QwiicStarterExample/QwiicStarterExample.ino**. Open the code up in the Arduino IDE, select the board (i.e. the **SparkFun RedBoard Turbo**), and the COM port that the board enumerated on. Then hit the upload button.

[**Note:**](https://learn.sparkfun.com/tutorials/qwiic-pro-kit-project-guide#atmega328p) To get the code working for an Atmega328P-based Arduino, simply comment out the line at the top by adding `//` in [front of the following line](https://github.com/sparkfun/Qwiic-Pro-Kit-Code/blob/master/Firmware/Arduino/QwiicStarterExample/QwiicStarterExample.ino#L37):\
\

``` cpp
#define Serial SerialUSB                            // Uncomment for RedBoard Turbo, this reroutes all Serial commands to SerialUSB
```

You\'ll also want to select the **Arduino/Genuino Uno** as the board before uploading and ensure that the [CH340 drivers are installed](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) for the RedBoard Qwiic.

With a friend, try rocking the accelerometer back and forth along the x-axis or moving your hand above the proximity sensor to control each paddle. You will need to orient the micro OLED so that the paddle is on the side of the player\'s Qwiic board. The game will continue as long as the ball hits the paddle and bounces to the other side. A player will win a round as soon as the other player fails to bounce the ball back to the other side. The current score will be briefly displayed before the next game. Try to rack up more points than your opponent!

[![Qwiic Pro Kit Demo](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/3/Qwiic_Accelerometer_Proximity_Sensor_Starter__Kit_Arduino_Demo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/3/Qwiic_Accelerometer_Proximity_Sensor_Starter__Kit_Arduino_Demo.gif)

**Heads up!** As with any distance sensor, there is a minimum distance at which the sensor can detect an object accurately. If your hand or finger is too close to the sensor, the readings for the distance can jump to a higher value causing the paddle to move off the screen. Make sure to be within the range to successfully hit the ball or try adjusting the code to include a minimum and maximum range for the paddle.

The default code uses the accelerometer as player 1 and the proximity sensor as player 2. Try adjusting the code to use the joystick for one of the players by [adding and removing the single line comments](https://www.arduino.cc/reference/en/language/structure/further-syntax/singlelinecomment/). The joystick will control the paddle along the \"vertical\" y-axis. Each board can only have one player assigned. See if you can try to remove the unused Qwiic board from the daisy chain and commenting out each instance of the related board.