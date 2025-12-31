# Source: https://learn.sparkfun.com/tutorials/artemis-development-with-arduino

## Introduction

**Updated Tutorial:** An [updated version of this tutorial for the Arduino IDE](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide) has been released. This tutorial will be retired once all the software tutorials (Arduino IDE, Mbed OS, and Ambiq SDK) for the Artemis module have been completed.

The [SparkFun Artemis](https://www.sparkfun.com/products/15484) is an amazing module. So much functionality packed into a tiny 10x15mm footprint! But what really makes it powerful is the ability to quickly write sketches and build projects using only Arduino code. Whether you are using one of our boards that has the Artemis module pre-integrated or have your own, this tutorial will show you how to install SparkFun\'s Apollo3 Arduino core and get you up and blinking in less than 5 minutes!

[![SparkFun Artemis Module - Low Power Machine Learning BLE Cortex-M4F](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/7/4/15484-SparkFun_Artemis_Module_-_Low_Power_Machine_Learning_BLE_Cortex-M4F-01b.jpg)](https://www.sparkfun.com/sparkfun-artemis-module-low-power-machine-learning-ble-cortex-m4f.html)

### [SparkFun Artemis Module - Low Power Machine Learning BLE Cortex-M4F](https://www.sparkfun.com/sparkfun-artemis-module-low-power-machine-learning-ble-cortex-m4f.html) 

[ WRL-15484 ]

The Artemis Module from SparkFun is the first FCC certified, open-source, Cortex-M4F with BLE 5.0 running up to 96MHz and wit...

[ [\$9.95] ]

### Required Materials

To follow along with this tutorial, you\'ll need one of the following Artemis carrier boards such as the [RedBoard](https://www.sparkfun.com/products/15444), [RedBoard Nano](https://www.sparkfun.com/products/15443), or [RedBoard ATP](https://www.sparkfun.com/products/15442) and a USB C cable.

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

[![SparkFun RedBoard Artemis Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/8/15443-SparkFun_RedBoard_Artemis_Nano-05.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis-nano.html)

### [SparkFun RedBoard Artemis Nano](https://www.sparkfun.com/sparkfun-redboard-artemis-nano.html) 

[ DEV-15443 ]

The RedBoard Artemis Nano is a miniature extremely versatile implementation of the Artemis module.

[ [\$19.95] ]

[![SparkFun RedBoard Artemis ATP](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/7/15442-SparkFun_RedBoard_Artemis_ATP-05.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis-atp.html)

### [SparkFun RedBoard Artemis ATP](https://www.sparkfun.com/sparkfun-redboard-artemis-atp.html) 

[ DEV-15442 ]

The RedBoard Artemis ATP has 48 GPIO and this board breaks out all of them in an Arduino Mega format.

[ [\$30.95] ]

[![USB 2.0 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/5/0/15092-USB_2.0_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/products/15092)

### [USB 2.0 Cable A to C - 3 Foot](https://www.sparkfun.com/products/15092) 

[ CAB-15092 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/designing-with-the-sparkfun-artemis)

### Designing with the SparkFun Artemis 

Let\'s chat about layout and design considerations when using the Artemis module.

## Arduino Installation

With the Arduino [Board Manager](https://www.arduino.cc/en/Guide/Cores), installing new board support within your Arduino IDE is a breeze!

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing the Arduino Core for Apollo3

We\'ve built the Arduino core for Apollo3 from scratch, making it as lightweight and easy to use as possible.

To install the SparkFun Apollo3 Arduino Core:

- Open the Arduino IDE (must be v1.6.12 or later)
- Navigate to **Preferences**

  ::: 
  [![Arduino Preferences, under File](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/1/Arduino-Preferences.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/Arduino-Preferences.png)
  :::

*Having a hard time seeing? Click the image for a closer look.*

- In the \"Additional Board Manager URL\" box, add

      language:c
      https://raw.githubusercontent.com/sparkfun/Arduino_Apollo3/main/package_sparkfun_apollo3_index.json

[![Additional Boards Manager URL location in the Preferences Dialog](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/1/Arduino-BoardMgrURLs_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/Arduino-BoardMgrURLs_2.png)

*Having a hard time seeing? Click the image for a closer look.*

- Go to **Tools** \> **Board** and select the **Boards Manager**

[![Arduino Boards Manager Dialog, under Tools](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/1/Arduino-BoardsManager.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/Arduino-BoardsManager.png)

*Having a hard time seeing? Click the image for a closer look.*

- Search for \"Apollo\", and you should find the **SparkFun Apollo3** board package.
- Make sure the latest version is selected and click **Install**

[![Board manager showing SparkFun Apollo3 Artemis install](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/1/SparkFun-Arduino-Apollo3-Boards-Install.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/SparkFun-Arduino-Apollo3-Boards-Install.jpg)

*Having a hard time seeing? Click the image for a closer look.*

Installation may take a few minutes \-- included in the install are all necessary source files for the Arduino core and Apollo3 libraries, plus all of the compiler and software-upload tools you\'ll need to use the Artemis with Arduino.

Once the board definitions have been installed, you should see a new set of Artemis boards under your Tools \> Board menu.

[![List of Artemis boards](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/SparkFun-Arduino-Apollo3-Boards-List.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/SparkFun-Arduino-Apollo3-Boards-List.jpg)

**Note:** The image here shows the SparkFun BlackBoard Artemis and is out of date. The [latest version of the SparkFun Apollo3 Arduino Core](https://github.com/sparkfun/Arduino_Apollo3) will have selections for the SparkFun RedBoard Artemis, Nano and ATP versions.

## Example: Blink It Up! 

The Blink example is about as basic as it gets. But it is also a good benchmark to make sure you\'ve got your core installed correctly and you can upload code to your module. To run this example, select your board from the Board Managers pulldown and choose the correct USB port. You can load the blink example by clicking on **File-\>Examples-\>01.Basics-\>Blink**.

[![The Blink Sketch is under file-\>examples-\>01.Basics-\>Blink](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/1/ArtemisBlinkItUp.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/ArtemisBlinkItUp.png)

Hit the upload button and enjoy the blinky goodness!

[![Pin13 is blinking away!](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/BlackBoard_Artemis.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/BlackBoard_Artemis.gif)

*Look at all the blinky!*

## Example: All the Features

We\'ve built the Arduino core for Artemis from the ground up. Be sure to checkout the large number of built-in examples. You\'ll find them under **File-\>Examples-\>\'Examples for Artemis\'**.

[![Arduino sub menu showing Artemis examples](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/Artemis-I2C-Examples-SmallMenu.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/Artemis-I2C-Examples-FullMenu.jpg)

*Click above image for full menu context*

We\'ve got examples for setting up multiple I2C ports (it\'s amazingly easy), writing to EEPROM, using SoftwareSerial (all 48 pins can be serial!), using the the onboard microphone, and using servos (up to 32!). We\'re adding more all the time so be sure to keep your core up to date.

## Bootloader Options

Each Artemis comes preloaded with two bootloaders. The SparkFun Variable Bootloader (SVL) will allow you reliably and conveniently load new code at data rates up to 921600bps. In addition to the SVL, we also enable the Ambiq factory bootloader for secure boot applications. Almost all users should use the SparkFun Variable Bootloader and forget about the [Ambiq](https://ambiq.com/) factory bootloader. For more information checkout the programming section of the [Designing with the Artemis Module](https://learn.sparkfun.com/tutorials/designing-with-the-sparkfun-artemis#programming) tutorial. Don\'t worry - you cannot damage or brick your Artemis using the incorrect bootloader.

[![The bootloader menu inside the SparkFun Apollo core](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/9/SparkFun_Artemis_Core-Bootloading_Type.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/9/SparkFun_Artemis_Core-Bootloading_Type.jpg)

*Don\'t select Ambiq Secure Bootloader unless you know what you\'re doing*

## Beyond Arduino

The SparkFun Apollo3 core supports all the [standard Arduino functions](https://www.arduino.cc/reference/en/). This means you can program `digitalWrite` I/O, `analogRead` ADC pins, `Serial` print to the Serial monitor, interact with hardware serial using `Serial1`, and even perform more complex I^2^C or SPI writes with the Wire and SPI libraries. The basics are there, so let\'s dive in to some more advanced capabilities of the Artemis!

[Ambiq](https://ambiq.com/) has created a software development kit to fully flex the Apollo3. The [Ambiq SDK](https://ambiqmicro.com/static/mcu/files/AmbiqSuite-Rel2.1.0.zip) contains a large number of examples and demonstrates all sorts of incredible aspects of the Apollo3. Each example uses various functions that look like this:

[![Various HAL functions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/1/Ambiq-SDK-HAL.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/Ambiq-SDK-HAL.jpg)

These long-named-functions are part of what\'s called a HAL or hardware abstraction layer. We aren\'t going to go into the specifics of setting up or using the SDK right now, but just know that the the SparkFun Arduino Apollo3 core is built upon this HAL which means you can call HAL functions directly inside the Arduino environment.

    language:c
    // Clear the RTC alarm interrupt.
    am_hal_rtc_int_clear(AM_HAL_RTC_INT_ALM);

[![Ambiq HAL inside the Arduino IDE](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/1/Ambiq_HAL_inside_Arduino_IDE.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/1/Ambiq_HAL_inside_Arduino_IDE.jpg)

This is a powerful tool for advanced users; you can use the built in Arduino functions such as Serial.begin(9600) and delay(100) while integrating more advanced HAL functions for controlling things like interrupts.

If you do decide to dig into the SDK, head on over to our [Using SparkFun Edge Board with Ambiq Apollo3 SDK](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/all) tutorial for more information!

[](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk)

### Using SparkFun Edge Board with Ambiq Apollo3 SDK 

March 28, 2019

We will demonstrate how to get started with your SparkFun Edge Board by setting up the toolchain on your computer, examining an example program, and using the serial uploader tool to flash the chip.

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\
[**SparkFun Artemis Forums**](https://forum.sparkfun.com/viewforum.php?f=163)