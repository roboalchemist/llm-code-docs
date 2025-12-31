# Source: https://learn.sparkfun.com/tutorials/micromod-qwiic-pro-kit-project-guide

## Introduction

**Note:** If you are looking for the previous version of this tutorial, head over to the [Qwiic Pro Kit Project Guide](https://learn.sparkfun.com/tutorials/qwiic-pro-kit-project-guide).

The [MicroMod Qwiic Pro Kit](https://www.sparkfun.com/products/20407) was designed to allow users to get started with Arduino without the need for soldering or a breadboard. We\'ve included three inputs (a joystick, accelerometer, and proximity sensor) and one display that can be daisy chained to your Arduino. Hooking up a handful of inputs and outputs to an Arduino has never been so easy with the MicroMod and Qwiic ecosystems!

[![SparkFun MicroMod Qwiic Pro Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/2/2/3/MicroMod_Qwiic_Pro_Kit_01.jpg)](https://www.sparkfun.com/sparkfun-micromod-qwiic-pro-kit.html)

### [SparkFun MicroMod Qwiic Pro Kit](https://www.sparkfun.com/sparkfun-micromod-qwiic-pro-kit.html) 

[ KIT-20407 ]

This kit provides you with a MicroMod Base, two sensors, a joystick, and an OLED screen as well as all the cables you need to...

**Retired**

### Suggested Reading

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/micromod). We recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)   [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*                                                                                                                                        *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials to set up the RedBoard Turbo and get a feel for each Qwiic component.

[](https://learn.sparkfun.com/tutorials/qwiic-carrier-board-hookup-guide)

### Qwiic Carrier Board Hookup Guide 

March 18, 2021

The Qwiic carrier board is the latest way to rapid prototype with the included M.2 socket to swap processor boards and Qwiic connectors to easily connect I2C devices.

[](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide)

### MicroMod SAMD51 Processor Board Hookup Guide 

October 21, 2020

This tutorial covers the basic functionality of the MicroMod SAMD51 and highlights the features of the ARM Cortex-M4F development board.

[](https://learn.sparkfun.com/tutorials/qwiic-micro-oled-hookup-guide)

### Qwiic Micro OLED Hookup Guide 

Get started displaying things with the Qwiic Micro OLED.

[](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide)

### Qwiic Joystick Hookup Guide 

Looking for an easy way to implement a joystick to your next Arduino or Raspberry Pi project? This hookup guide will walk you through using the Qwiic Joystick with the Arduino IDE on a RedBoard Qwiic and in Python on a Raspberry Pi.

[](https://learn.sparkfun.com/tutorials/qwiic-proximity-sensor-vcnl4040-hookup-guide)

### Qwiic Proximity Sensor (VCNL4040) Hookup Guide 

The SparkFun Qwiic Proximity Sensor is a great, qualitative proximity (up to 20 cm) and light sensor. This hookup guide covers a few examples to retrieve basic sensor readings.

[](https://learn.sparkfun.com/tutorials/qwiic-9dof---ism330dhcx-mmc5983ma-hookup-guide)

### Qwiic 9DoF - ISM330DHCX, MMC5983MA Hookup Guide 

Find all your degrees of freedom with this little Qwiic breakout board combining the ISM330DHCX 6Dof and the MMC5983MA Magnetometer!

## Kit Contents

You will find the following parts in the kit.

[![Qwiic Pro Kit Contents](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/2/MicroMod_Qwiic_Pro_Kit_01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/2/MicroMod_Qwiic_Pro_Kit_01.jpg)

- 1x [MicroMod Qwiic Carrier Board - Single](https://www.sparkfun.com/products/17723)
- 1x [MicroMod SAMD51 Processor](https://www.sparkfun.com/products/16791)
- 1x [Reversible USB A to USB C Cable - 0.8 Meter](https://www.sparkfun.com/products/15425)
- 1x [MicroMod Screwdriver](https://www.sparkfun.com/products/19012)
- Inputs
  - 1x [Qwiic Joystick](https://www.sparkfun.com/products/15168)
  - 1x [Qwiic 9DoF IMU Sensor](https://www.sparkfun.com/products/19895)
  - 1x [Qwiic Proximity Sensor (VCNL4040)](https://www.sparkfun.com/products/15177)
- Outputs
  - 1x [Qwiic Micro OLED Display](https://www.sparkfun.com/products/14532)
- Qwiic Cables
  - 2x [50mm](https://www.sparkfun.com/products/17260)
  - 2x [100mm](https://www.sparkfun.com/products/17259)
  - 1x [200mm](https://www.sparkfun.com/products/14428)
  - 1x [500mm](https://www.sparkfun.com/products/14429)
  - 1x [SparkFun Mini Screwdriver](https://www.sparkfun.com/products/9146)

**Note:** Prior to MicroMod Qwiic Pro Kit was the Qwiic Pro Kit. Instead of the RedBoard Turbo with SAMD21 and USB micro-b cable , the MicroMod Qwiic Pro Kit includes the MicroMod SAMD51 Processor Board, Qwiic Carrier Board - Single, USB C Cable, and a MicroMod screwdriver. The Qwiic Triple Axis Accelerometer Breakout - MMA8452Q is also replaced by the 9DoF IMU Breakout - ISM330DHCX, MMC5983MA (Qwiic).

## Hardware Hookup

If you have not already, make sure to check out the [Getting Started with MicroMod: Hardware Hookup](https://learn.sparkfun.com/tutorials/getting-started-with-micromod#hardware-hookup) for information on inserting your Processor Board to your Carrier Board. The [MicroMod Qwiic Carrier Board Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-carrier-board-hookup-guide#hardware-assembly) also goes over how to connect the boards together as well!

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

October 21, 2020

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

Remove the screw across from the MicroMod Qwiic Carrier Board - Single. Then insert the MicroMod SAMD51 Processor Board into the M.2 socket. The Processor Board will stick up at an angle (at around 25°), as seen here.

[![MicroMod SAMD51 Processor Board Inserted M.2 Socket](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/2/Insert_SAMD51_PB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/2/Insert_SAMD51_PB.jpg)

Hold the board down and tighten the screw with a Philip\'s head.

[![Tighten Screw](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/2/Tighten_Screw_SAMD51_PB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/2/Tighten_Screw_SAMD51_PB.jpg)

Once connected, your board should be secured to the MicroMod Qwiic Carrier Board - Single like the image shown below.

[![SAMD51 Secure in MicroMod Qwiic Carrier Board\'s M.2 Socket](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/2/SAMD51_PB_Secure_Qwiic_Carrier_Board.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/2/SAMD51_PB_Secure_Qwiic_Carrier_Board.jpg)

Insert the Qwiic cable of your choice between each to each of the boards. You can daisy chain the boards any way you like. However, we found it easier to control the 9DoF\'s accelerometer by having it at the end and connecting a longer Qwiic cable. Depending on the player, you will need to orient the 9DoF\'s accelerometer with respect to the paddle. The vertical and horizontal Qwiic connectors also connect to the same port so you can connect to either one. We also found it easier to connect the Qwiic Distance Sensor with VCNL4040 to the other end as well. Then connect the USB cable between your computer and MicroMod Qwiic Carrier Board - Single.

[![MicroMod Qwiic Pro Kit Connected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/2/MicroMod_Qwiic_Pro_Kit_MicroOLED_Proximity_Joystick_ISM330DHCX_Accelerometer.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/2/MicroMod_Qwiic_Pro_Kit_MicroOLED_Proximity_Joystick_ISM330DHCX_Accelerometer.jpg)

**Warning!** You will need to connect all of the boards together when using the demo code in this tutorial. Otherwise, you will need to comment out lines of code for the Qwiic board that is not connected to the daisy chain.

### Mounting Qwiic Boards to the Standoffs

You can also mount the Qwiic Micro OLED breakout to the end of the two standoffs as shown below. Remove the yellow tape that is covering the mounting holes. Align the mounting hole with the standoffs. Insert a 4-40 screw between the Qwiic Micro OLED\'s mounting hole and tighten. You\'ll need to use some elbow grease to drive each 4-40 screw into the standoffs since they are slightly offset. Make sure to be careful with the Qwiic connector that is closest to the mounting holes. The height of the standoffs and the position of the connector can make the connector push against the end of the Qwiic Carrier Board - Single. However, it was enough to hold the display down.

[![MicroMod Qwiic Pro Kit Connected with Micro OLED Breakout Mounted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/2/MicroMod_Qwiic_Pro_Kit_MicroOLED-Mounted__Proximity_Joystick_ISM330DHCX_Accelerometer.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/2/MicroMod_Qwiic_Pro_Kit_MicroOLED-Mounted__Proximity_Joystick_ISM330DHCX_Accelerometer.jpg)

We recommend not mounting the Qwiic Distance Sensor, Qwiic Joystick, and Qwiic 9DoF so that users that are sitting across from each other are able to control their paddle on their side without getting in the way of the display.

[**Note:**](#redboard-qwiic) The code used in this tutorial is also compatible with Atmega328P-based Arduinos like the RedBoard Qwiic! If you purchased the components separately or Qwiic Ideation Kit, the setup is the same. Instead of the MicroMod SAMD51 Processor Board, you would be using the RedBoard Qwiic. Check the [note below for more information](https://learn.sparkfun.com/tutorials/qwiic-pro-kit-project-guide#atmega328p) when compiling for the Atmega328P-based microcontrollers! You can also swap out different MicroMod Processor Boards with Arduino Cores as well!\
\

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun MicroMod Artemis Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/0/16401-SparkFun_MicroMod_Artemis_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html)

### [SparkFun MicroMod Artemis Processor](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html) 

[ DEV-16401 ]

Featuring the Artemis Module, this processor is capable of machine learning, Bluetooth, I2C, GPIO, PWM, SPI & packaged to fit...

[ [\$17.50] ]

## Installing the Board Add-Ons and Drivers

**Note:** This code/library has been written and tested on Arduino IDE version v1.8.12. Otherwise, make sure you are using the latest stable version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

There are a few board add-ons to install before you are able to upload code to your MicroMod SAMD51 Processor Board. If you have not already, make sure to check out the MicroMod SAMD51 Processor Board hookup guide to install the SAMD51 and SparkFun board add-ons.

[Installing the SAMD and SparkFun Board Add-Ons](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/setting-up-the-arduino-ide)

### Drivers

**Heads up!** Please be aware that the MicroMod SAMD51 Processor Board is **NOT currently supported on Windows 8** due to a lack of support drivers for those specific OS\'s.

The MicroMod SAMD51 Processor Board is now easier than ever to program, thanks the [UF2 bootloader](https://learn.sparkfun.com/tutorials/redboard-turbo-hookup-guide#uf2-bootloader). With this bootloader, the MicroMod SAMD51 Processor Board shows up on your computer as a USB storage device **without having to install drivers** for Windows 10, Mac, and Linux!

## Installing the Libraries

**Note:** If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

SparkFun has written a library for the Qwiic enabled joystick, 9DoF IMU (ISM330DHCX, MMC5983MA), proximity sensor (VCNL4040), and 64x48 micro OLED. You can obtain these libraries through the Arduino Library Manager. Search for the following terms to automatically install the latest versions of each library. If you have issues compiling, you may need to download the respective library versions listed below.

- [SparkFun Joystick](https://github.com/sparkfun/SparkFun_Qwiic_Joystick_Arduino_Library) (v1.0.4)
- [SparkFun 6DoF ISM330DHCX - Accelerometer and Gyro](https://github.com/sparkfun/SparkFun_6DoF_ISM330DHCX_Arduino_Library) (v1.0.0)
- [SparkFun MMC5983MA - Magnetometer](https://github.com/sparkfun/SparkFun_MMC5983MA_Magnetometer_Arduino_Library) (v1.0.0)
- [SparkFun VCNL4040](https://github.com/sparkfun/SparkFun_VCNL4040_Arduino_Library) (v1.0.2)
- [SparkFun micro OLED](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library) (v1.2.5)

If you prefer downloading the libraries manually, you can grab them from each of the respective GitHub repositories.

[SparkFun Qwiic Joystick Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_Joystick_Arduino_Library/archive/master.zip)

[SparkFun 6DoF ISM330DHCX - Accelerometer and Gyro Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_6DoF_ISM330DHCX_Arduino_Library/archive/refs/heads/main.zip)

[SparkFun MMC5983MA - Magnetometer Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_MMC5983MA_Magnetometer_Arduino_Library/archive/refs/heads/main.zip)

[SparkFun VCNL4040 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_VCNL4040_Arduino_Library/archive/master.zip)

[SparkFun Micro OLED Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library/archive/master.zip)

**Note:** The demo code currently just uses the accelerometer to control the paddle. We have linked the library in this section in case you use the magnetometer in case you decide to use it as well!

## Example Code

We recommend grabbing the code from its the [GitHub repository](https://github.com/sparkfun/Qwiic-Pro-Kit-Code). Otherwise, you can download the zipped file from the link below.

[Download the MicroMod Qwiic Pro Kit Code (ZIP)](https://github.com/sparkfun/Qwiic-Pro-Kit-Code/archive/master.zip)

After downloading, unzip the files and open the *MicroModQwiicStarterExample.ino* sketch. It should be located in the downloads folder similar to this path: **\.../Firmware/Arduino/MicroModQwiicStarterExample/MicroModQwiicStarterExample.ino**. Open the code up in the Arduino IDE, select the board (i.e. the **SparkFun SAMD51 MicroMod**), and the COM port that the board enumerated on. Then hit the upload button.

With a friend, try rocking the 9DoF back and forth along the x-axis or moving your hand above the proximity sensor to control each paddle. You can also take a PCB or flat object as shown in the GIF below to make it easier to control. Remember, you will need to orient the 9DoF\'s accelerometer with respect to the paddle (if you notice in the GIF, player 1 had the board oriented in a way that had the paddle controls were reversed). You will need to orient the micro OLED so that the paddle is on the side of the player\'s Qwiic board. The game will continue as long as the ball hits the paddle and bounces to the other side. A player will win a round as soon as the other player fails to bounce the ball back to the other side. The current score will be briefly displayed before the next game. Try to rack up more points than your opponent!

[![MicroPong Demo with MicroMod Qwiic Pro Kit](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/2/MicroMod_Qwiic_Pro_Kit_MicroOLED-Mounted__Proximity_Joystick_ISM330DHCX_Accelerometer_Demo_MicroPong.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/2/MicroMod_Qwiic_Pro_Kit_MicroOLED-Mounted__Proximity_Joystick_ISM330DHCX_Accelerometer_Demo_MicroPong.gif)

**Heads up!** As with any distance sensor, there is a minimum distance at which the sensor can detect an object accurately. If your hand or finger is too close to the sensor, the readings for the distance can jump to a higher value causing the paddle to move off the screen. Make sure to be within the range to successfully hit the ball or try adjusting the code to include a minimum and maximum range for the paddle.

The default code uses the 9DoF\'s accelerometer as player 1 and the proximity sensor as player 2. Try adjusting the code to use the joystick for one of the players by [adding and removing the single line comments](https://www.arduino.cc/reference/en/language/structure/further-syntax/singlelinecomment/). The joystick will control the paddle along the \"vertical\" y-axis. Each board can only have one player assigned. See if you can try to remove the unused Qwiic board from the daisy chain and commenting out each instance of the related board. Or try adjusting the code to control the paddle with the magnetometer and a magnet!

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)