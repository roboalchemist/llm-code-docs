# Source: https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide

## Introduction

The [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) is the newest edition of the Arduino-compatible development platforms in the SparkFun catalog. This updated version of the *classic* [SparkFun RedBoard](https://www.sparkfun.com/products/13975) incorporates a few key improvements over its predecessor (see [Hardware Overview](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide#hardware-overview)). However, like the *original* SparkFun RedBoard, it is designed to be an easy-to-use learning platform for coding, physical computing, and project prototyping. These skills are becoming increasingly significant in today\'s education and the technological community.

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

This tutorial aims to familiarize you with the new SparkFun RedBoard Qwiic and help you get started using it. To begin, we\'ll guide you through the installation of the [Arduino IDE (Integrated Development Environment) software](https://www.arduino.cc/en/Guide/HomePage), the main user interface for programming the board. Next, we will go over the hardware and features of the board. Finally, we will walk you through a few examples using the Arduino IDE.

The SparkFun RedBoard Qwiic can interact with real-world sensors, control motors, display information, and perform near-instantaneous calculations. It enables *anyone* to create unique, nifty projects from something as simple as [displaying characters on an LCD display](https://learn.sparkfun.com/tutorials/pic-based-serial-enabled-character-lcd-hookup-guide) or [detecting changes in light](https://learn.sparkfun.com/tutorials/photocell-hookup-guide) to vastly more complicated projects like an [IoT cellular device](https://learn.sparkfun.com/tutorials/lte-cat-m1nb-iot-shield-hookup-guide) (**Not** recommend for beginners\... start with something simpler and work your way up.). If you\'re familiar with how the *original* SparkFun RedBoard worked, you may want to skim over parts of this tutorial.

### Required Materials/Tools

To get started, all you need is a few things:

- [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) - You\'ll definitely need this; otherwise, you might be on the wrong tutorial (*wink-wink*).
- [USB micro-B Cable - 6 Foot](https://www.sparkfun.com/products/10215) - The USB interface serves two purposes: it powers the board and allows you to upload programs to it.
- Computer with the **Arduino IDE** installed on it - That is how we will program the board and interface with it.

<!-- -->

- ::: 
  **Troubleshooting Tip:** If you are not a technical or computer savy individual and you have your choice of computers, a [**Windows 7 or 10**] computer is highly recommended. You will usually run into the the least issues, if any, with these operating systems.
  :::

That is ALL\... pretty simple right? Now you won\'t be able to do much since there are no additional sensors to interact with the physical world. However, you can at least blink an LED and do some math calculations.

[**Jumper Modification**](#Jumper_Materials) [**Qwiic Example**](#Example_Materials)

***Click the buttons** above to toggle the **additional materials** based on the tasks you\
wish to perform. Feel free to modify the items in your cart to fit your needs.*

\

#### Jumper Modification

If you would like to modify the 3.3V/5V I/O jumper or A4/A5 Qwiic connector jumpers, you will need [soldering equipment](https://www.sparkfun.com/categories/49) and/or a [knife](https://www.sparkfun.com/categories/379).\
\

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Chip Quik No-Clean Flux Pen - 10mL](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/5/14579-Chip_Quik_No-Clean_Flux_Pen_-_10mL-01.jpg)](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html)

### [Chip Quik No-Clean Flux Pen - 10mL](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html) 

[ TOL-14579 ]

This 10mL no-clean flux pen from Chip Quik is great for all of your solder, de-solder, rework, and reflow purposes!

[ [\$8.50] ]

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

\

#### Qwiic Example

If you would like to follow along with the examples below to interact with the physical world, you will also need the following items:\
\

[![SparkFun Distance Sensor Breakout - 4 Meter, VL53L1X (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/4/8/14722-SparkFun_Distance_Sensor_Breakout-_4_Meter__VL53L1X__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-distance-sensor-breakout-4-meter-vl53l1x-qwiic.html)

### [SparkFun Distance Sensor Breakout - 4 Meter, VL53L1X (Qwiic)](https://www.sparkfun.com/sparkfun-distance-sensor-breakout-4-meter-vl53l1x-qwiic.html) 

[ SEN-14722 ]

This SparkFun Distance Sensor Breakout utilizes the VL53L1X next generation ToF sensor module to give you the highly accurate...

[ [\$29.95] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Suggested Reading

The **SparkFun RedBoard Qwiic** aims to be a beginner-friendly microcontroller platform. You can get started without an innate knowledge of [Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) or [How Electricity Works](https://learn.sparkfun.com/tutorials/what-is-electricity) (but a little understanding wouldn\'t hurt!). The following are some subjects you should be familiar with; however, to use the more advanced features of the board, it is recommended that you read up on the **Logic Levels** and **I^2^C** tutorials.

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

One of the new, advanced features of the board is that it takes advantage of the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials (above) before using it, as all **Qwiic** sensors utilize an **I^2^C** communication protocol. Click on the banner above to learn more about [Qwiic products](https://www.sparkfun.com/qwiic).

**Fun Fact:** Qwiic is a play on words between \"quick\" and I^2^C or \"iic\".

------------------------------------------------------------------------

## Installing Drivers

**Note:** The USB-to-Serial adapter IC, used on the RedBoard Qwiic, is different from what was used on the original RedBoard. **The new CH340C chip will require a different driver than the FTDI chip used on the original [RedBoard](https://www.sparkfun.com/products/13975)** because they are different chips made by separate manufacturers. **[Please make sure to follow the [driver installation guide](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) before plugging this new board into your computer].**

The SparkFun RedBoard Qwiic uses a CH340C USB-to-Serial adapter made by [WCH](http://www.wch.cn/). The driver for the CH340C chip will need to be installed on your computer. We have tested and confirmed that the driver works on Windows 7, Windows 10, Mac OSX High Sierra, and Raspbian Stretch (11-13-2018 release) for the Raspberry Pi. On all operating systems, if you have previously installed the CH340G drivers, you will need to uninstall those drivers first before updating to the new CH340C driver. For more information, check out our [How to Install CH340 Drivers Tutorial](https://www.sparkfun.com/ch340).

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

Installing the CH340C driver allows your computer to recognize the SparkFun RedBoard Qwiic as a device and lets it communicate with the board over the USB connection. You can also find the [latest version of the CH340 drivers from WCH here](http://www.wch.cn/products/CH340.html). (*Most of their pages are in Mandarin, but if you use a Chrome web browser, you should have the option to have the web page translated.*)

## Installing the Arduino IDE

### Download/Install Arduino

You can [download the Arduino IDE](http://arduino.cc/en/Main/Software) from their website. They have [installation instructions](https://www.arduino.cc/en/Guide/HomePage), but we will also go over the installation process as well. Make sure you download the version that matches your operating system.

[Click for Arduino IDE Download Page](http://arduino.cc/en/Main/Software)

The installation procedure is fairly straightforward, but it does vary by OS. Here are some tips to help you along. We\'ve also written a separate [Installing Arduino tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide) in case you get stuck.

**Troubleshooting Tips:**\

- We recommend using a computer with a full desktop operating system like Windows 7/10 ([**avoid**] Windows 8 if you can), Mac OSX, and certain flavors Linux (check the [Arduino FAQ page for compatibility](https://www.arduino.cc/en/Main/FAQ#toc12)).
  \
  - If you are not a technical or computer savy individual and you have your choice of computers, I highly recommend using a [**Windows 7 or 10**] computer. You will usually run into the the least issues, if any, with these operating systems.

  \
- We do [**[NOT]**] recommend using a Chromebook, Netbook, tablet, phone, or the Arduino Web IDE in general. You will be responsible for troubleshooting any driver or Arduino Web IDE issues.
  \
- As of writing this tutorial (12-14-2018), the most recent and stable release of the Arduino IDE is version 1.8.5. We recommend using that version of the Arduino IDE; you can download the [previous releases here](https://www.arduino.cc/en/Main/OldSoftwareReleases#previous).
  \
- On Windows 10, we do [**[NOT]**] recommend installing the Arduino IDE from the app store. You may run into issues because the OS will automatically update to the most recent release of the Arduino IDE, which may have unknown bugs (like the compiler errors in versions 1.8.6 and 1.8.7).
  \
- Raspberry Pi users with Raspbian installed should use the **Linux ARM** download. We do not recommend using the command line installation. It will install the oldest release of Arduino, which is useless when it comes to installing new boards definitions or libraries.
  \
- For additional troubleshooting tips, here is a [troubleshooting guide from Arduino](https://www.arduino.cc/en/Guide/Troubleshooting).

[**Windows 7/10**](#Windows) [**Mac OSX**](#Mac_OSX) [**Linux**](#Linux)

***Click the buttons above** for OS specific instructions.*

### Windows Install Tips

The Windows version of Arduino is offered in two options: an installer or a zip file. The **installer** is the easier of the two options, just download that, and run the executable file to begin the installation.\
\

[![Windows 10- Arduino Installation Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Win_10-_Installation_Diagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Win_10-_Installation_Diagram.png)\
*Windows install steps. Click the image to get a bigger view.*

\
When you\'re prompted to install a driver during installation, select \"Install\". This will install drivers for Arduino specific boards (like the Uno, Nano, etc.) that you may use in the future.\
\

- If you choose to download the **zip file** version of Arduino, you\'ll need to extract the files yourself. Don\'t forget which folder you extract the files into! You will need to run the executable Arduino file in the folder to start the Arduino IDE.
  \
- On Windows 10, there is an option to install Arduino through their app store. we do not recommend installing the Arduino IDE from the app store. You may run into issues because the OS will automatically update to the most recent release of the Arduino IDE, which may have unknown bugs.

### Mac Install Tips

The Mac download of Arduino is only offered in a zip file version. After the download is finished, simply **double-click the .zip file** to unzip it.\
\

[![Mac Install Screenshot](https://cdn.sparkfun.com/assets/3/4/1/7/b/52cc895fce395fe16e8b456a.jpg)](https://cdn.sparkfun.com/assets/3/4/1/7/b/52cc895fce395fe16e8b456a.jpg)\
*Mac OSX Arduino.app*

\
Following that, you\'ll need to **copy the Arduino application into your applications folder** to complete the installation.

### Linux Install Tips

As Linux users are no doubt aware, there are many flavors of Linux out there, each with unique installation routines. Check out the [FAQ section](https://www.arduino.cc/en/Main/FAQ#toc11) of the Arduino webpage for more details. Otherwise, you can also use the [Linux section of our Installing Arduino tutorial](https://learn.sparkfun.com/tutorials/installing-arduino/linux) for some helpful links for an assortment of Linux distributions.

##### Raspbian Stretch

Raspberry Pi users with Raspbian installed should use the **Linux ARM** download. Do not use the command line installation process. For more information, please refer to this [blog post from Arduino](https://playground.arduino.cc/Linux/Raspbian).

##### Ubuntu and Debian

For Ubuntu and Debian users, installing Arduino should only need a simple \"**apt-get**\" command like:\
\

    sudo apt-get update && sudo apt-get install arduino arduino-core

##### Other Distributions

Other Linux distros aren\'t too dissimilar from the Ubuntu and Debian instructions.

\
With Arduino downloaded and installed, the next step is to plug the board in and test it out! Pretty soon you\'ll be blinking LEDs, reading buttons, and doing some physical computing!

------------------------------------------------------------------------

## Hardware Overview

Below is an annotated image, and an overview of all of the important features for the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123):

[![Annotated image of RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Hardware_Overview.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Hardware_Overview.png)

***Click the buttons** below for more details.*

\

[**New Features**](#New_Features) [**Dimensions**](#Size) [**Microcontroller**](#ATmega) [**Power/Reset**](#Power) [**Status LEDs**](#LEDs) [**Programming**](#Programming) [**Pin Functions**](#Pin) [**Pin Connections**](#Wiring) [**Qwiic Connection**](#Qwiic) [**Jumpers**](#Jumpers)

### New Features

The new features of the SparkFun RedBoard Qwiic include:

- An updated Serial-USB Converter Chip
- An improved AP2112 Voltage Regulator
- A [Qwiic Connector](https://www.sparkfun.com/products/14417)
- Available A4/A5 Jumpers
- Available Voltage Level Jumpers
- An improved Reset Button
- RX/TX LED color change

[![Annotated image of new features](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_New_Features-1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_New_Features-1.png)\
*New features of RedBoard Qwiic.*

#### Serial-USB Converter Chip

The new CH340C IC allows the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) to utilize the USB micro-B connection and should reduce the need for users to manually install drivers. Newer operating systems should automatically recognize and install the drivers for the board.

#### AP2112 Voltage Regulator

The AP2112 is a more robust **3.3V** regulator to provide more power to daisy chain multiple Qwiic devices. Unlike the MIC5205, which could only source about 150mA of current; the AP2112 can source up to **600mA** of current and should be able to handle most of your [Qwiic device](https://www.sparkfun.com/qwiic) needs.

#### Qwiic Connector

This connector allows the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) to seamlessly interface with [SparkFun\'s Qwiic Ecosystem](https://www.sparkfun.com/qwiic).

#### A4/A5 Jumpers

Pins **A4** and **A5** are tied directly to the I^2^C bus. These jumpers can be used to disconnect the logic level converters from pins **A4** and **A5** so that they might be used independently from the [Qwiic system](https://www.sparkfun.com/qwiic) for analog readings.

#### Voltage Level Jumpers

These jumpers allow users to easily switch from a **3.3V** to **5V** board. This allows the user to convert the board (and I/O pins) to either **3.3V** or **5V** based on their needs. Unlike the the *original* [SparkFun RedBoard](https://www.sparkfun.com/products/13975), you no longer need a logic level converter to interface directly to a **3.3V** device or sensor.

#### Reset Button

The board also includes a new, more pronounced reset button that is easier to push. Anyone with \"*fat fingers*\" can relate to this struggle.

[![Reset Button Comparison](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Reset_Button_Comparison-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Reset_Button_Comparison-1.jpg)\
*The more ergonomic reset button that is easier to press.*

#### RX/TX LEDs

The TX LED is now green, instead of yellow and the RX LED is now yellow, instead of red.

### Dimensions

The dimensions for the board are approximately 2.7\" x 2.1\". The board uses female headers laid out in a standard configuration for Arduino shields. The barrel jack for power uses a standard 5.5mm outer diameter and 2.1mm inner diameter mating connection. The Qwiic connector uses a [4-pin JST SH type](https://www.sparkfun.com/products/14417) connector. There are also 4 mounting points on the board.\
\

[![RedBoard Qwiic Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/RedBoard_Qwiic_Dimensions.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/RedBoard_Qwiic_Dimensions.PNG)\
*Screen shot of RedBoard Qwiic board layout in Eagle. (**Click image** to enlarge.)*

\
For the more details on the board sizing and component placement please refer to the Eagle files provided.\
\

[Download Eagle Files (ZIP)](https://cdn.sparkfun.com/assets/e/a/2/1/6/RedBoard-Qwiic.zip)

\
[Eagle](https://www.autodesk.com/products/eagle/free-download) is a free for educators, makers, and hobbyists (i.e. basically, anything not for commercial purposes). All measurements are accurate, excluding any manufacturing tolerances. (Unfortunately, we do not have any tolerance information available; you may need to just measure the board you purchase.)

### Microcontroller

The microcontroller (ATmega328 IC) is the work horse of the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123). The ATmega328 is an 8-bit AVR microcontroller manufactured by Atmel, now Microchip. Once an Arduino sketch is uploaded to the board, the program is stored in the memory of the ATmega328. The microcontroller will then run/execute the program while the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) is powered.\
\

[![ATmega328](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_ATmega328-2.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_ATmega328-2.JPG)\
*Image of the ATmega328 IC.*

#### Clock

An external 16 MHz crystal is used as the clock for the ATmega328.

#### Memory

The ATmega328 has **Flash**, **SRAM** (Static Random Access Memory), and **EEPROM** (Electrically Erasable Programmable Read-Only Memory) memory.\
\

- 32KB Flash Memory - where the Arduino sketch/program is stored (including the 512 byte Optiboot bootloader).
- 2KB SRAM - where the sketch/program creates and manipulates variables when it runs.
- 1KB EEPROM - is available for stable long-term storage (read/written with the [EEPROM library](https://www.arduino.cc/en/Reference/EEPROM)).

The Flash and EEPROM memory are non-volatile; the data is still stored even when the board is no longer powered. The SRAM, on the other hand, is volatile and the data is only available while the board is powered.\
\

**Troubleshooting Tips:**\

- The EEPROM can be corrupted with low power/brown out issues.
- When you run out of SRAM, the sketch may fail or act strangely after it is uploaded. If you suspect this is the issue, try to comment out any long strings or large data structures. If the sketch starts to run normally, then you may need to modify your data requirements.

#### Bootloader

The Optiboot bootloader is a unique piece of firmware (512 bytes) at the end of the address space of the flash memory. The Optiboot bootloader is specifically configured for the ATmega328 to interface with the Arduino IDE, through a serial interface, to upload code. Without a bootloader, you would need to external programmer and program the microcontroller through the SPI interface (specifically, the ISP/ICSP headers).\
\
For more details on the ATmega328, memory, and the bootloader check out these tutorials:

- [Arduino Memory Tutorial](https://www.arduino.cc/en/Tutorial/Memory)
- [SparkFun EEPROM Tutorial](https://learn.sparkfun.com/tutorials/reading-and-writing-serial-eeproms)
- [Arduino Bootloader Page](https://www.arduino.cc/en/Hacking/Bootloader?from=Tutorial.Bootloader)
- [Arduino as ISP and Arduino Bootloaders](https://www.arduino.cc/en/Tutorial/ArduinoISP)
- [StackExchange Forum Post on Bootloaders](https://electronics.stackexchange.com/questions/27486/what-is-a-boot-loader-and-how-would-i-develop-one)

You can also find the datasheet for the ATmega328 from the [Microchip product page](https://www.microchip.com/wwwproducts/en/ATmega328).

### Power/Reset

The [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) can be powered via the USB and/or barrel jack connectors. If you choose to power it via USB, the other end of the USB cable can be connected to either a **computer or a 5V (regulated)** [USB wall charger](https://www.sparkfun.com/products/11456). Otherwise, should you choose to use the barrel jack, any wall adapter connected to this jack should supply a **DC voltage between 7 and 15V**.\
\

[![Annotated image of power features](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Power_Reset.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Power_Reset.png)\
*Annotated image of RedBoard Qwiic with power and reset features highlighted.*

#### Power LED Indicator

Just to the right of the word *RedBoard* on your circuit board, there's a tiny LED next to the word **ON**. This green LED should light up whenever you plug your Arduino into a power source. If this light doesn't turn on, there's a good chance something is wrong.

#### Reset Button

Just like the original Nintendo, the Arduino has a reset button. Pushing it will temporarily connect the reset pin to ground and restart any code that is loaded on the Arduino. This can be very useful if your code doesn't repeat, but you want to test it multiple times. Unlike the original Nintendo however, blowing on the Arduino doesn't usually fix any problems.

[![Reset Button Comparison](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Reset_Button_Comparison-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Reset_Button_Comparison-1.jpg)\
*This updated version of the RedBoard has a more ergonomic reset button that is easier to press.*

#### Barrel Jack for VIN

The barrel jack accepts a male, center-positive connector with a 5.5mm outer diameter and 2.1mm inner diameter. Check out this [tutorial](https://learn.sparkfun.com/tutorials/connector-basics#power-connectors) for more information on power connectors.\
\
Our [9V](https://www.sparkfun.com/products/298) and [12V](https://www.sparkfun.com/products/9442) power adapters are good choices if you\'re looking to power the board through the barrel jack. Any wall adapter connected to this jack should supply a **DC voltage between 7 and 15V** as specified by the electrical characteristics of the LM1117 voltage regulator used on the board. The input voltage pin [VIN] on the power headers is directly connected to the input voltage of the barrel jack.\
\

**Troubleshooting Tips:**\
The board could operate on an external supply of [**6 to 20 volts**], but the recommended range is [**7 to 12 volts**]. (*\*If supplied with less than 7V, the 5V pin may supply less than five volts and the board may be unstable. Using more than 12V, the voltage regulator may overheat and damage itself and/or the board.*)\
\
*For more technical details about voltage regulators and thermal dissipation, I suggest taking a look at these blog posts and tutorial:*

- [According to Pete - Voltage Regulators](https://www.sparkfun.com/news/1067)
- [Enginursday: Linear Regulator Thermal Tests](https://www.sparkfun.com/news/2173)
- [Power and Thermal Dissipation](https://www.sparkfun.com/tutorials/217)
- [Enginursday: Voltage Regulator Temperature Mobile App](https://www.sparkfun.com/news/2258)

#### USB

A [USB micro-B cable](https://www.sparkfun.com/products/10215) is usually the easiest way to power the board, especially when you\'re programming it because the USB interface is required for uploading code too. A traditional USB port supplies a regulated **5V**, but is limited to about **500mA** (USB 2.0). Additionally, there is a fuse that protects your computer from shorts and overcurrent. If more than \~750mA is drawn through the USB port, it automatically throttles the current draw or disconnects power until the short/overload is removed. If you need more than that a barrel jack wall adapter is the best choice.

[![USB connection example](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_USB_Connector__No_Prying_.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_USB_Connector__No_Prying_.gif)\
*An example of how to pull USB cable straight out.*

**Troubleshooting Tip:**\
Users should take care [**NOT**] to pry or leverage on the connector when inserting/removing the USB cable. Doing so, [**WILL**] damage the board and cause the pads and/or traces to tear off as well. The cable should be removed by pulling straight outwards from the board.\
\
The fuse can also be tripped with a high current draw and high ambient temperatures.

#### AP2112 Voltage Regulator

The AP2112 is a more robust **3.3V** regulator to provide more power to daisy chain multiple Qwiic (I^2^C) devices. Unlike the MIC5205, which could only source about 150mA of current; the AP2112 can source up to **600mA** of current and should be able to handle the needs of your Qwiic devices.\
\

**Troubleshooting Tip:**\
If you need more power for your Qwiic devices, you can attach a separate power supply. However, it is recommended that you cut the 3.3V line of the Qwiic cable to the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123). Leave the GND line alone, as that ground loops your system, providing a consistent reference voltage for your I^2^C signals. By cutting the 3.3V line, this allows you to power all your devices without straining the 3.3V regulator. For more details on voltage regulators, check out this [According to Pete](https://www.sparkfun.com/news/1067) blog post.

#### The Power Header

The power headers provides all your reference, input, and output, voltages.\
\

[![Annotated image of power header](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Power_Header-1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Power_Header-1.png)\
*RedBoard Qwiic Power Header*

\

- **VIN**- The input voltage to the Arduino board when it\'s using an external power source. You can provide an external supply voltage through this pin or access the external supply voltage from the power jack through this pin. If only powered through a USB connection, voltage will be around 5V.
- **5V**- This pin outputs a regulated 5V from the regulator on the board. The board can be supplied with power either from the DC power jack (7 - 12V), the USB connector (5V), or the VIN pin of the board (7-12V). Supplying voltage via the 5V or 3.3V pins bypasses the regulator, and can damage your board. We don\'t advise it.
- **3V3**- A 3.3 volt supply generated by the on-board regulator. Maximum current draw is 600 mA.
- **GND**- Ground pins.
- **RESET**- This pin is tied to the Reset pin of the microcontroller and Reset Button. If this pin is toggled low or shorted to the GND pin, it will trigger a reset of the microcontroller.

#### Dual Power

It is fine to connect both a barrel jack and a USB connector at the same time. The [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) has power-control circuitry to automatically select the best power source.\
\

[![USB and barrel jack wires connected](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Dual_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Dual_Power.jpg)\
\
*USB and barrel jack wires connected.*

### Status Indicator LEDs

There are 4 status LEDs on the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) that indicate power, serial communication, and a test/status LED.\
\

[![Annotated image of status LEDs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Status_LEDs.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Status_LEDs.png)\
*Status LEDs on the RedBoard Qwiic.*

**Note:**\
There is a small change to the color of ther status LEDs from the *original* [RedBoard](https://www.sparkfun.com/products/13975). The power LED is green, the LED for Pin 13 is blue, the RX LED is yellow, and the TX LED is green. However, the color of the LED\'s don\'t really matter, the indication is based on whether the LED is on/off. The color differences only help to indicate which LED is on when the LED is blinks quickly or from a quick glance.

#### Power

The first LED is the **power** LED. This LED indicates that there is a potential between the VCC and GND pins. A good secondary test for this status indicator is to use a multimeter to test the VIN, 5V, and 3.3V pins against the GND pin.

#### RX/TX

The next two status LEDs are the serial communication LEDs. These LEDs indicate that there is data moving between the serial UART **RX/TX** pins and the **USB-to-Serial Converter**. A good secondary test for this status indicator is to make sure that these LEDs are flashing during upload or any other [serial communication](https://learn.sparkfun.com/tutorials/serial-communication).

#### Pin 13

The last indicator is the **Pin 13** LED. This is typically only used as a test LED to make sure that a board is working or for basic debugging. However, for the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123), this LED also indicates if the presence of the bootloader. If the board was properly flashed, the LED should flash a few times on power up.

**Troubleshooting Tips:**

- New boards will come programmed with a test sketch that cycles between the RX and TX LEDs.

- Pin 13 is difficult to use as a digital input because of the voltage drop from status LED and resistor soldered in series to it. If the pin is enabled as an input with the internal 20k pullup resistor, it will always read a LOW state; an expected 5V (HIGH) signal will instead read around 1.7V (LOW).\
  \
  If you must use pin 13 as a digital input, it is recommended that you set the **pinMode()** as an **INPUT**\
  \

      pinMode(13, INPUT);

  and use an external pulldown resistor.

### Programming

There are two ways to program the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123). The most common way for users is through the USB connection. The other slightly less common method is through the ISP headers or pins.\
\

[![Annotated image of programming connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Programming.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Programming.png)\
*RedBoard Qwiic programming connections.*

#### USB Connection

The USB micro-B connector is the most convenient way to power and program the board. To program the board through the USB connection, you will need a [USB micro-B cable](https://www.sparkfun.com/products/10215) and there must be a bootloader flashed to the microcontroller (factory \"*installed*\"). For the SparkFun [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123), this is the same Optiboot bootloader from the Arduino UNO. For most users, the board will be programmed through a USB connection using the Arduino IDE.\
\

[![USB connection example](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_USB_Connector__No_Prying_.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_USB_Connector__No_Prying_.gif)\
*An example of how to pull USB cable straight out.*

**Troubleshooting Tip:**\
Users should take care [**NOT**] to pry or leverage on the connector when inserting/removing the USB cable. Doing so, [**WILL**] damage the board and cause the pads and/or traces to tear off as well. The cable should be removed by pulling straight outwards from the board.

##### CH340C USB-to-Serial Converter

Unlike the *classic* [SparkFun RedBoard](https://www.sparkfun.com/products/13975), that uses an FTDI IC; this board uses the CH340C IC for USB-to-serial conversion. One advantage is that it does not need a driver since most operating systems will have the drivers already installed. The chip is used to convert USB data coming to and from your computer into a serial protocol for the microcontroller.\
\

**Troubleshooting Tip:**

- Whenever you upload to your board or send serial data, you should seen the RX and/or TX LEDs flashing. The best way to test the functionality of this part is to send serial data between your computer and the board.
- For more details on what happens in the Arduino IDE when code is uploaded through the bootloader, check out this great [forum post](https://arduino.stackexchange.com/questions/15936/what-happens-when-code-is-uploaded-using-the-bootloader).

\
*For more tips and details on serial communication, read our [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication#common-pitfalls) and [Terminal Basics](https://learn.sparkfun.com/tutorials/terminal-basics/all#tips-and-tricks) tutorials.*

#### ISP or ICSP Connector

A less common way for most users to program the microcontroller on their board, is to use the ISP header. This method programs a microcontroller directly through the **SPI pins**. A more experienced user, with a firm grasp on digital electronics and the microcontroller (datasheet), will probably use a software package like Atmel studio, which is easier to debug. The most common reasons for programming an AVR via an in-system programmer (ISP) are:

- ISP is faster and more reliable- We use this method in our QC process for most boards.
- There is no bootloader on the microcontroller or your board wasn\'t flashed properly:
  - This is probably the only way to program the microcontroller without a bootloader.
- You want to use your own, custom bootloader.
- Configure fuse bits for various settings.
- Program without bootloader, when you need just a little bit more space for your program to load.

Most AVRs are programmed through a **[Serial Peripheral Interface](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) (SPI)**. There are six unique signals required for communication between ISP and AVR.\
\

[![top avr isp pinouts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/4/isp-pinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/isp-pinout.png)

*AVR ISP Pinouts -- Top View.*

On the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) the MOSI and D11 pins, MISO and D12 pins, and SCK and D13 pins are tied together. To program the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) through the ISP pins, you will want to **set the I/O jumper to 5V**. This will tie the **V~CC~** of the microcontroller to the **5V rail//pin** of the ISP header. Otherwise, you will probably run into issues and likely damage the I/O pins and/or the microcontoller chipset.\
\

**Troubleshooting Tip:** [Re-flashing the Bootloader]\
Often, this method is used as a last ditch effort, when after all else has failed to revive a board (do not attempt, unless you know what you are doing). Most likely your board isn't bricked unless you have done something drastic like modified the fuses. In which case, reflashing the board probably won't help you. However, if you have no options left and want to try to reflash the bootloader with an Uno or RedBoard. Here are links to some tutorials to get you started:\

- [SparkFun\'s Installing an Arduino Bootloader Tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-bootloader)
- [Arduino as ISP and Arduino Bootloaders](https://www.arduino.cc/en/Tutorial/ArduinoISP)
- [Arduino Programming a Microcontroller Tutorial](https://www.arduino.cc/en/Tutorial/ArduinoToBreadboard)
- [Pi AVR Programmer Hookup Guide](https://learn.sparkfun.com/tutorials/pi-avr-programmer-hat-hookup-guide)

\

**Time Capsule:** If you would like to take a look back, here is a tutorial from back in **June 2008** on [How to Get Code Onto a Microcontroller](https://www.sparkfun.com/tutorials/93). We have come so far since then!\
\
Back then, it wasn\'t as easy to get into programming or processing. Without a USB-to Serial Converter or Bootloader, you needed an external ISP programmer to flash a microcontroller. You needed to use a lower level language and complex development platform to create and compile code for your microcontroller. Before flash memory, you could only program chips once.

(*\*Make sure to upload the ISP sketch to the programming board. Lastly, be sure to double check the board options you are selecting so that the Arduino IDE uses the correct bootloader hex file.*)

### Pin Functions

All of the [SparkFun RedBoard Qwiic\'s](https://www.sparkfun.com/products/15123) pins are broken out to 0.1\" spaced female headers (i.e. connectors) on the outer edges of the board. The pins are arranged into logical collections; there are headers dedicated to power inputs/outputs, analog inputs, and digital inputs.\
\

[![Annotated image of pin functionality](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Pin_Functions.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Pin_Functions.JPG)\
*RedBoard Qwiic pin functionality.*

\

**Note:** To learn more about analog vs. digital signals, check out this great [tutorial](https://learn.sparkfun.com/tutorials/analog-vs-digital).

------------------------------------------------------------------------

#### Power Pins

The power pins aren\'t really **I/O** (Input/Output) pins for the microcontroller; however, they are pertinent to the board. For more details on these pins, see the [**Power/Reset** section](#Power).\
\

[![Annotated image of power header](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Power_Header-1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Power_Header-1.png)\
*RedBoard Qwiic Power Header*

\
The **power header** is mostly full of voltage supply pins. These pins are traditionally **used as power sources** for other pieces of hardware (like LEDs, potentiometers, and other circuits).

- **3.3V**- A regulated 3.3V voltage source.
- **5V**- A regulated 5V voltage source.
- **GND**- The common ground or the 0V reference for the voltage supplies.
- **VIN**- The input voltage, it\'ll be equal to the voltage of your input supply if you have a wall adapter connected. If nothing is connected to the barrel jack, and you\'re powering the board via USB, **VIN** should be around 5V.
- **RESET**- The RESET pin can be shorted to the GND pin to reset the microcontroller, similar to using the reset button.

------------------------------------------------------------------------

#### Microcontroller I/O Pins

All of the **I/O** pins on this board are **digital** **inputs** or **outputs** for the microcontroller (ATmega328). There are select pins, like the **Analog pins**, which have additional capabilities.

#### Digital I/O

There are 20 **I/O** pins on this board that can be used as **digital** **inputs** or **outputs** for the microcontroller (ATmega328). This includes the pins labeled as **Analog**, which may be configured and used in the same manner as the **Digital pins**. These are what you connect to buttons, LEDs, sensors, etc. to interface the Arduino with other pieces of hardware.

- ##### Input

  By default, all digital I/O pins are configured as inputs. It is best practice to define the [**pinMode()**](https://www.arduino.cc/reference/en/language/functions/digital-io/pinmode/) in the setup of each **sketch** (programs written in the Arduino IDE) for the pins used. When configured properly, an **input** pin will be looking for a **HIGH** or **LOW** state. **Input** pins are **High Impedance** and takes very little current to move the input pin from one state to another.\
  \

  ::: 
  **Troubleshooting Tips:**
  - If an input pin is read and that is **floating** (with nothing connected to it), you will see random data/states. In practice, it may be useful to tie an input pin to a known state with a **pullup resistor** (to VCC), or a **pulldown resistor** (to GND).
  - There are 20K pullup resistors built into the ATmega328 chip that can be configured by setting the pinMode() as INPUT_PULLUP.
  - Pin 13 is difficult to use as a digital input because of the voltage drop from status LED and resistor soldered in series to it. If the pin is enabled as an input with the internal 20k pullup resistor, it will always read a LOW state; an expected 5V (HIGH) signal will instead read around 1.7V (LOW). If you must use pin 13 as a digital input, it is recommended that you set the **pinMode()** as an **INPUT** and use an external pulldown resistor.
  :::

  ##### Output

  When configured as an **output** the pin will be at a **HIGH** or **LOW** voltage. **Output** pins are **Low Impedance**: This means that they can provide a substantial amount of current to other circuits.\
  \

  ::: 
  **Troubleshooting Tip:**\
  The maximum current an I/O pin can source (provide positive current) or sink (provide negative current) is 40 mA (milliamps). For more details, you can refer to the [ATmega328 datasheet](https://www.microchip.com/wwwproducts/en/ATmega328) or this [reference page](https://playground.arduino.cc/Main/ArduinoPinCurrentLimitations). Attempting to run high current devices may damage the output the pin or entire ATmega328 chip.
  :::

**Note:** For more details about **digital** pins, check out this [reference page](https://www.arduino.cc/en/Tutorial/DigitalPins).

#### Additional Functions

There are several pins that have special functionality in addition to general **digital I/O**. These pins and their additional functions are listed in the tabs below. For more technical specifications on the **I/O** pins, you can refer to the [ATmega328 datasheet](https://www.microchip.com/wwwproducts/en/ATmega328).\
\

- [Analog Input](#Analog-Input-tab)
- [PWM Output](#PWM-Output-tab)
- [Serial Comm.](#Serial-tab)
- [SPI](#SPI-tab)
- [I^2^C](#I2C-tab)
- [Interrupt](#Interrupt-tab)

##### Analog Input Pins

There are 6 **analog inputs** on the analog header. These pins all have 10-bit (10-bit = 1024 different values) [analog to digital converter](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) (ADC), which can be used to read in an analog voltage between 0 and VCC. These are useful if you need to read the output of a potentiometer or other analog sensors.\
\

**Troubleshooting Tip:**\
To take analog readings on pins A4/A5, the jumpers for the Qwiic connector need to be cut. Otherwise, the pullup resistors for the logic level converters will act as voltage dividers and the pins will read improper values at lower voltages.

[![Annotated image of analog inputs](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Analog_Inputs.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Analog_Inputs.JPG)\
*RedBoard Qwiic analog input pins.*

\

**Note:**\
The **AREF** pin provides a reference voltage for the analog inputs. This pin can be used to get a higher resolution at lower voltage levels. Be sure to read the [**Notes and Warnings**] on the [**analogReference()**](https://www.arduino.cc/reference/en/language/functions/analog-io/analogreference/) page.\
\
Analog pins 4 and 5 also support I^2^C (TWI) communication using the Wire library.

For more details on the analog inputs, check out these tutorials:

- [SparkFun Analog Pin Tutorial](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)
- [Arduino Analog Pin Tutorial](https://www.arduino.cc/en/Tutorial/AnalogInputPins)

##### Pulse Width Modulation (PWM) Output Pins

Digital pins (3, 5, 6, 9, 10, and 11) marked with a tilde (\~) are 8-bit [PWM capable outputs](https://learn.sparkfun.com/tutorials/pulse-width-modulation), which you can use to dim LEDs or run servo motors.

[![Annotated image of PWM pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_PWM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_PWM.png)\
*RedBoard Qwiic PWM pins.*

\

**Troubleshooting Tip:**\
Novice users often mistake PWM pins as an analog output. Although, it can somewhat mimic that functionality, it is not a true analog output.

For more details on pulse width modulation, check out these tutorials:

- [SparkFun PWM Tutorial](https://learn.sparkfun.com/tutorials/pulse-width-modulation)
- [Arduino PWM Tutorial](https://www.arduino.cc/en/Tutorial/PWM)
- [Arduino: Secrets of Arduino PWM](https://www.arduino.cc/en/Tutorial/SecretsOfArduinoPWM)

##### Serial Communication Pins

Digital pins 0 (RX) and 1 (TX) are also dedicated serial communication pins ties to the USB-to-serial converter (CH340C). These pins are used to receive (RX) and transmit (TX) TTL serial data as well as program the microcontroller. Other digital pins can be use to emulate serial communication with [**SoftwareSerial()**](https://www.arduino.cc/en/Reference/softwareSerial).

[![Annotated image of serial communication pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Serial.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Serial.JPG)\
*RedBoard Qwiic dedicated serial communication pins.*

\

**Troubleshooting Tip:**\
If a device is communicating to the microcontroller over digital pins 0 and 1, while you are trying to upload code, you will run into an upload error. Disconnect the device before uploading code again. It may be easier to emulate serial communication with another set of pins to make debugging easier.

For more details on serial communication, check out these tutorials:

- [SparkFun Serial Communication Tutorial](https://learn.sparkfun.com/tutorials/serial-communication)
- [Arduino Serial Reference Page](https://www.arduino.cc/reference/en/language/functions/communication/serial/)
- [Arduino SoftwareSerial Reference Page](https://www.arduino.cc/en/Reference/SoftwareSerial)
- [Arduino SoftwareSerial Tutorial](https://www.arduino.cc/en/Tutorial/SoftwareSerialExample)

##### SPI Communication Pins

Digital pins 10 (SS), 11 (MOSI), 12 (MISO), and 13 (SCK) support Serial Peripheral Interface (SPI) communication.

[![Annotated image of SPI pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_SPI.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_SPI.JPG)\
*RedBoard Qwiic SPI pins.*

\

**Note:**\
Using the Serial Peripheral Interface, configures the SCK and MOSI pins to be directly managed by the SPI hardware. Therefore, while in use, pins 11 and 13 can\'t be used (i.e. the LED on pin 13 can no longer be used as a debug/status indicator.) Executing \"SPI.end();\" allows those pins 11 and 13 to be used as general I/O again.

For more details on the serial peripheral interface, check out these tutorials:

- [SparkFun SPI Tutorial](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)
- [Arduino SPI Tutorial](https://www.arduino.cc/en/Tutorial/SPIIntro)
- [Arduino SPI Reference Page](https://www.arduino.cc/en/Reference/SPI)
- [Arduino SPI Settings Reference Page](https://www.arduino.cc/en/Reference/SPISettings)

##### I^2^C Communication Pins

Analog pins 4 (SDA) and 5 (SCL) support I^2^C (TWI) communication.

[![Annotated image of I2C pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_I2C.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_I2C.JPG)\
*RedBoard Qwiic I^2^C pins.*

##### Qwiic System

The Qwiic system is intended to be a quick, hassle-free cabling/connector system for I^2^C devices. The Qwiic connector is tied to the I^2^C pins via the A4 /A5 jumpers. Also, there are a set of logic level converters for the Qwiic system, which uses a 3.3V logic level.

**Troubleshooting Tip:**\
Be sure to double check that you are not trying to use and I^2^C device while you are trying use analog pin 4 or 5 to read analog data, you will run into issues. You can only do one or the other.

For more details on the serial peripheral interface, check out these tutorials:

- [SparkFun I^2^C Tutorial](https://learn.sparkfun.com/tutorials/i2c)
- [Arduino I^2^C Reference Page](https://www.arduino.cc/en/Reference/Wire)

##### Interrupt Pins

Interrupts allow you to *interrupt* the code running in your main loop and execute another set of instructions (also known as interrupt handler or interrupt service routine) before returning back to the main loop. Digital pins 2 and 3 can be configured to trigger an interrupt on a low value, a rising or falling edge, or a change in value.

[![Annotated image of interrupt pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Interrupt.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Interrupt.JPG)\
*RedBoard Qwiic interrupt pins.*

\
For more details on the interrupts, check out these tutorials:

- [SparkFun Interrupt Tutorial](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino)
- [Arduino Interrupt Tutorial](http://playground.arduino.cc/code/interrupts)
- [Arduino attachinterrupt() Reference Page](https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt)

### Connecting to the Board

#### Jumper Wire

All of the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123)\'s pins are broken out to 0.1\"-spaced female headers (i.e. connectors) on the outer edges of the board. There are a variety of wires, connectors, and other items that can be inserted into these headers to interface with the Arduino. [Jumper wires](https://www.sparkfun.com/products/11026) are a good option if you want to connect the RedBoard up to other pieces of circuitry that may live on a breadboard.

[![RedBoard connected to breadboard via jumper wires](https://cdn.sparkfun.com/r/600-600/assets/0/9/9/4/e/5230c645757b7fa32c8b4568.png)](https://cdn.sparkfun.com/assets/0/9/9/4/e/5230c645757b7fa32c8b4568.png)\
*A tangled assortment of [jumper wires](https://www.sparkfun.com/products/8431) run between the RedBoard headers and components on a [breadboard](https://www.sparkfun.com/products/11317). An [Arduino baseplate](https://www.sparkfun.com/products/11235) holds them all in one place.*

\
When connecting to the headers, be sure you are aware of the functionality of the pins you are using.

**Troubleshooting tip:**\
If you don\'t have jumper wires, you can [strip and cut](https://learn.sparkfun.com/tutorials/working-with-wire/how-to-strip-a-wire) some [solid core wire](https://www.sparkfun.com/products/11367) (20-24 AWG wire works best).

#### Arduino Shields

Shields are another popular way to interface with the headers. These Arduino-shaped boards are stackable and connect to all four headers of the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) at once. Shields exist in hundreds of forms, they can add GPS, WiFi, MP3 decoding, and all sorts of other functionality to your Arduino. For more details on Arduino shields and shield assembly, please refer to this [Arduino Shields](https://learn.sparkfun.com/tutorials/arduino-shields) tutorial.\
\

[![Ethernet Shield on RedBoard](https://cdn.sparkfun.com/r/600-600/assets/f/9/8/b/b/5230c645757b7fb32d8b4568.png)](https://cdn.sparkfun.com/assets/f/9/8/b/b/5230c645757b7fb32d8b4568.png)\
*An [Ethernet Shield](https://www.sparkfun.com/products/10864) stacks onto a RedBoard to help get it connected to the Internet.*

\

**Troubleshooting tip:**\
Most shields are expecting a 5V board. Double check the documentation or datasheet for the shield you are using to verify what voltage it is expecting. You will need to adjust the I/O jumper accordingly.

### Qwiic Connector

The most convenient feature of the board is the Qwiic connector that allows the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) to seamlessly interface with [SparkFun\'s Qwiic Ecosystem](https://www.sparkfun.com/qwiic).

### What is Qwiic?

The Qwiic system is intended a quick, hassle-free cabling/connector system for I^2^C devices. Qwiic is actually a play on words between \"quick\" and I^2^C or \"iic\".\
\

#### Features of the Qwiic System

- [No Soldering](#Soldering-tab)
- [Polarized Connector](#Connector-tab)
- [Daisy Chain](#Daisy-tab)

## Keep your soldering iron at bay. 

Cables plug easily between boards making quick work of setting up a new prototype. We currently offer three different lengths of Qwiic cables as well as a breadboard friendly cable to connect any Qwiic enabled board to anything else. Initially you may need to solder headers onto the shield to connect your platform to the Qwiic system but once that's done it's plug and go!

![Qwiic Cable and Board](https://cdn.sparkfun.com/assets/8/d/9/2/a/jst-board.jpg)

Qwiic cables connected to [Spectral Sensor Breakout](https://www.sparkfun.com/products/14414)

## Minimize your mistakes. 

How many times have you swapped the SDA and SCL wires on your breadboard hoping the sensor will start working? The Qwiic connector is polarized so you know you'll have it wired correctly, every time, from the start.

The PCB connector is part number SM04B-SRSS ([Datasheet](https://cdn.sparkfun.com/assets/parts/1/2/2/8/9/Qwiic_Connector_Datasheet.pdf)) or equivalent. The mating connector used on cables is part number SHR04V-S-B or equivalent. This is a common and low cost connector.

![JST Connector](https://cdn.sparkfun.com/assets/d/a/2/e/6/jst-connector_1.jpg)

1mm pitch, 4-pin JST connector

## Expand with ease. 

It's time to leverage the power of the I^2^C bus! Most Qwiic boards will have two or more connectors on them allowing multiple devices to be connected.

![Daisy Chain](https://cdn.sparkfun.com/assets/b/d/0/1/0/daisy-chain_2.png)

Shown above: [Qwiic Shield for Arduino](https://www.sparkfun.com/products/14352) on [RedBoard](https://www.sparkfun.com/products/13975), [Spectral Sensor Breakout - NIR](https://www.sparkfun.com/products/14351), [Spectral Sensor Breakout - Visible](https://www.sparkfun.com/products/14347) and [SparkFun GPS Breakout](https://www.sparkfun.com/products/14414)

#### Logic Level Conversion

There are logic level converters used on the Qwiic connector to maintain a 3.3V logic level on the I^2^C bus. They are tied directly to the VCC of the microcontroller and the 3.3V rail. Therefore, the board automatically does the logic level conversion for the I/O voltage selected.\
\

[![Qwiic Logic Level Voltage](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/Qwiic_IO.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_IO.PNG)\
*RedBoard (Qwiic) schematic of voltage for logic level converters (click image for closer view).*

#### A4/A5 Jumpers

These jumpers directly disconnect the logic level converters and the Qwiic connector from the A4/SDA and A5/SCL pins.\
\

[![Qwiic jumper](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Qwiic_Jumpers.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Qwiic_Jumpers.JPG)\
*A4/A5 or Qwiic jumpers.*

\

**Troubleshooting Tip:**\
To take analog readings on pins A4/A5, the jumpers for the Qwiic connector need to be cut. Otherwise, the pullup resistors for the logic level converters will act as voltage dividers and the pins will read improper values at lower voltages.

##### How to Modify the A4/A5 Jumper

You will need a [knife](https://www.sparkfun.com/categories/379) to modify the A4/A5 jumpers. To modify the jumper, located on the back of the board next to the Qwiic connector, you need to [cut the trace](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all#cutting-a-trace-between-jumper-pads) between the two pads. Once you have cut the trace, the Qwiic connector and logic level conveters will be disconnected. To repair the connection, you just need to solder a jumper between the pads of both jumpers. Be sure to test the jumper with a multimeter to make sure you have a good soldered connection.

#### Adding External Power

If you need more power for your Qwiic devices, you can attach a separate power supply. However, it is recommended that you cut the 3.3V line of the Qwiic cable to the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123). Leave the GND line alone, as that ground loops your system, providing a consistent reference voltage for your I^2^C signals.\
\

[![cutting the 3.3V line](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Qwiic_Extra_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Qwiic_Extra_Power.jpg)\
*Cutting the 3.3V line of the Qwiic cable to the Qwiic connector.*

\
By cutting the 3.3V line, this allows you to power all your devices without straining the 3.3V regulator on the board. Since, all voltage regulators are slightly different and don\'t maintain a perfect 3.3 voltage, the 3.3V AP2112 regulator would be constantly battling the voltage regulator of your separate power supply to regulate *its* version of 3.3V. For more details on voltage regulators, check out this [According to Pete](https://www.sparkfun.com/news/1067) blog post.

### Jumpers

There are 3 jumpers on the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123). The two jumpers on the back of the board can be used to disconnect the Qwiic connector from the A4/SDA and A5/SCL pins. The last jumper, on the top of the board, allows users to change the voltage level of the microcontroller.

#### Using the I/O jumper

One of the great features of the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) is this **I/O jumper** that allows users to easily switch from a **3.3V** to **5V** board.\
\

[![I/O jumper](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_IO_Jumper.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_IO_Jumper.JPG)\
*I/O jumper.*

##### Why is this an important feature and what does it even do?

This jumper allows users to easily convert the **I/O** pins to either **3.3V** or **5V logic levels** based on their needs. With the *original* [SparkFun RedBoard](https://www.sparkfun.com/products/13975), a 5V board, you would need logic level converter to interface directly to a 3.3V device or sensor.

##### What are Logic Levels?

The logic levels are a specific range of voltages, in which a device can recognize as HIGH or LOW signals.\
\

[![ATmega328 Logic Levels](https://cdn.sparkfun.com/r/270-270/assets/7/9/3/a/c/5V-logic-levels_fixed.png)](https://cdn.sparkfun.com/assets/7/9/3/a/c/5V-logic-levels_fixed.png)\
\
*ATmega328 Logic Levels*

\
In most electrical devices, the logic level used is the same as the **V~CC~** (**Voltage Common Collector**). For example, in the *original* [SparkFun RedBoard](https://www.sparkfun.com/products/13975), the **V~CC~** of the microcontroller is set by the LM117 **5V** linear voltage regulator. Therefore, the *original* [SparkFun RedBoard](https://www.sparkfun.com/products/13975) was a **5V board** that used **5V logic levels**.\
\

[![RedBoard schematic with 5V regulator highlighted](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/RedBoard_ATmega328-5V.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/RedBoard_ATmega328-5V.PNG)\
*RedBoard schematic with 5V regulator highlighted (click image for closer view).*

\
However, the *updated* [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) has an IO voltage jumper that lets you connect the **V~CC~** of the microcontroller to the LM117 **5V** or AP2112 **3.3V** linear voltage regulator. Therefore, the logic level of the ATmega328 can be set to **3.3V** or **5V**. For more details see our [Logic Level](https://learn.sparkfun.com/tutorials/logic-levels) tutorial.\
\

[![RedBoard (Qwiic) schematic with IO jumper highlighted](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/RedBoard_ATmega328-IO.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/RedBoard_ATmega328-IO.PNG)\
*RedBoard (Qwiic) schematic with IO jumper highlighted (click image for closer view).*

##### How to Modify the I/O

If you would like to modify the 3.3V/5V I/O jumper, you will need [soldering equipment](https://www.sparkfun.com/categories/49) and a [knife](https://www.sparkfun.com/categories/379). To modify the jumper, located next to the \"I/O\" silkscreen (pictured), you need to [cut the trace](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all#cutting-a-trace-between-jumper-pads) between the center and the 5V pads. Once you have cut the trace, to select a specific I/O voltage, you just need to solder a jumper between the center pad and the correlating voltage pad of your choice. Be sure to test the jumper with a multimeter to make sure you have a good jumper soldered.\
\

**Troubleshooting Tips:**

- When cutting the jumper, cut downwards (away from the \"I/O\" silk screened on the board), it will give you a little more wiggle room in case your knife slips while cutting the jumper, the trace for the 5V line is a little further away from the jumper than the I/O trace.
- To test if you have fully cut the jumper, you can plug your board back in. If the jumper has been completely severed, the VCC line will not be powered and none of the status LEDs will turn on.

**Programming via ISP:**\
If you choose to program the [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) through the ISP pins, you will want to **set the I/O jumper to 5V**. This will tie the **V~CC~** of the microcontroller to the **5V rail//pin** of the ISP header. Otherwise, you will probably run into issues and likely damage the I/O pins and/or the microcontoller chipset.

#### A4/A5 jumpers

Since the [SparkFun\'s Qwiic System](https://www.sparkfun.com/qwiic), utilizes the I^2^C bus of the SparkFun RedBoard Qwiic, these jumpers are used to separate the board from the Qwiic connector are provided. These jumpers directly disconnect the logic level converters and the Qwiic connector from the A4/SDA and A5/SCL pins.\
\

[![Qwiic jumper](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Qwiic_Jumpers.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_Redboard_-_Qwiic_Jumpers.JPG)\
*A4/A5 or Qwiic jumpers.*

\

**Note:** There are logic level converters used on the Qwiic connector to maintain a 3.3V logic level on the I^2^C bus. They are tied directly to the VCC of the microcontroller and the 3.3V rail. Therefore, the board automatically does the logic level conversion for the I/O voltage selected.

##### How to Modify the I/O

You will need a [knife](https://www.sparkfun.com/categories/379) to modify the A4/A5 jumpers. To modify the jumper, located on the back of the board next to the Qwiic connector, you need to [cut the trace](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all#cutting-a-trace-between-jumper-pads) between the two pads. Once you have cut the trace, the Qwiic connector and logic level converters will be disconnected. To repair the connection, you just need to solder a jumper between the pads of both jumpers. Be sure to test the jumper with a multimeter to make sure you have a good soldered connection.

------------------------------------------------------------------------

## Arduino Examples

### Example 1: Uploading Blink

In this example we will go over the basics of the Arduino IDE and upload a sample code. This is a great way to test the basic functionality of any board to make sure it is working.

#### The Arduino IDE

Now it\'s finally time to **open up the Arduino software**. You\'ll be presented with a window that looks a little something like this:\
\

[![Arduino IDE annotated](https://cdn.sparkfun.com/assets/8/4/5/b/d/52309c7e757b7f522d8b4567.png)](https://cdn.sparkfun.com/assets/8/4/5/b/d/52309c7e757b7f522d8b4567.png)\
*Layout of the Arduino IDE.*

\
Before we can send the code over to the RedBoard, there are a couple of adjustments we need to make.

#### Select a Board

This step is required to tell the Arduino IDE *which* of the [available Arduino boards](https://learn.sparkfun.com/tutorials/choosing-an-arduino-for-your-project), we are using. Go up to the **Tools** menu. Then hover over **Board** and make sure **Arduino/Genuino Uno** is selected.\

[![Board Selection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Board_Selection.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Board_Selection.PNG)\
*Screen shot of **Board** selection.*

#### Select a Serial Port

Next up we need to tell the Arduino IDE which of our computer\'s serial ports the RedBoard is connected to. For this, again go up to **Tools**, then hover over **Serial Port** and select your RedBoard\'s COM port.\

[![Port Selection](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/Serial_Port_Selection.PNG)](ttps://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Serial_Port_Selection.PNG)\
*Screen shot of **COM Port** selection.*

\
If you\'ve got more than one port, and you\'re not sure which of the serial ports is your RedBoard, unplug it for a moment and check the menu to see which one disappears.

#### Blink Sketch

Code written for the Arduino IDE are referred to as sketches. All code in Arduino is C based. Let us upload a **Blink sketch** to make sure our new RedBoard setup is totally functional. Go up to the **File** menu in Arduino, then go to **Examples \> 01.Basics \> Blink** to open it up.\

[![Board Selection](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/Selecting_Sketch.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Selecting_Sketch.PNG)\
*Screen shot of **Blink sketch** selection.*

#### Upload!

With all of those settings adjusted, you\'re finally ready to upload some code! Click the **Upload** button (the right-pointing arrow) and allow the IDE some time to compile and upload your code. It should take around 10-20 seconds for the process to complete. When the code has uploaded, you should see something like this in your console window:\

[![Done uploading](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/Uploaded_Code.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Uploaded_Code.PNG)\
*Screen shot of upload complete.*

\
And if you look over to the RedBoard, you should see the blue LED turn on for a second, off for a second, on for a second, off for a second\...ad infinitum (at least until it loses power).

[![Blink Example](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Blink_Example.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_Blink_Example.gif)\
*Expected response from board*

\
If you want to adjust the blink speed, try messing with the \"1000\" value in the `delay(1000);` lines. You\'re well on your way to becoming an Arduino programmer!

#### Something Wrong?

Uh oh! If you didn\'t get a \"Done Uploading\" message, and instead got an error, there are a few things we can double-check.

If you got an `avrdude: stk500_getsync(): not in sync: resp=0x00` error in your console window.\

[![Upload error](https://cdn.sparkfun.com/assets/9/a/6/f/b/5230a5fa757b7fcf2d8b4567.png)](https://cdn.sparkfun.com/assets/9/a/6/f/b/5230a5fa757b7fcf2d8b4567.png)\
*Screen shot of **Error Message** in the **Console**.*

\
Either your serial port or board may be incorrectly set. Again, make sure **Arduino/Genuino Uno** is the board selection (under the \"**Tools** \> **Board**\" menu). The serial port is usually the more common culprit here. Is the Serial Port correctly set (under the \"**Tools** \> **Serial Port**\" menu)? Did the drivers successfully install? To double check your RedBoard\'s serial port, look at the menu when the board is plugged in, then unplug it and look for the missing port. If none of the ports are missing, you may need to go back to [driver installation](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide#installing-drivers).

### Example 2: Qwiic Connector

One of the great features of the RedBoard (Qwiic) is its ability to interface with I^2^C devices using our [Qwiic system](https://www.sparkfun.com/qwiic). The Qwiic system is a solderless connection system that allows users to seamlessly daisy chain multiple I^2^C devices with ease.

#### The Qwiic Distance Sensor

For this example, we will be running a basic sketch using the [SparkFun 4m Distance Sensor (VL53L1X)](https://www.sparkfun.com/products/14722). For more examples with this sensor, please refer to the [complete hookup guide](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-hookup-guide).

#### Hardware Assembly

The wiring for this is simple. Use the Qwiic cable and connect the distance sensor to the board. That is it! The connections are polarized, so you don\'t have to worry about which side or connector you are using.

[![Hardware assembly for VL53L1X example](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_VL53L1X_Example.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Qwiic_RedBoard_-_VL53L1X_Example.jpg)

*Hardware assembly for [VL53L1X distance sensor](https://www.sparkfun.com/products/14722) example.*

Let\'s run an example for our distance sensor to see how it behaves.

#### Install the Arduino Library

**Note:** If you have not previously installed an Arduino library, please check out our [Arduino library installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

First, you\'ll need the **Sparkfun VL53L1X** Arduino library. You can obtain these libraries through the Arduino Library Manager. Search for **Sparkfun VL53L1X Arduino Library** to install the latest version. If you prefer downloading the libraries from the [GitHub repository](https://github.com/sparkfun/SparkFun_VL53L1X_Arduino_Library/) and manually installing it, you can grab them here:

[DOWNLOAD THE SPARKFUN VL53L1X ARDUINO LIBRARY (ZIP)](https://github.com/sparkfun/SparkFun_VL53L1X_Arduino_Library/archive/master.zip)

#### Example 1 - Read Distance

To get started with this example, open up **File** \> **Examples** \> **SparkFun VL53L1x 4M Laser Distance Sensor** \> **Example1_ReadDistance**. In this example, we begin by creating a **`SFEVL53L1X`** object called `distanceSensor` with our wire port, `Wire`, and then our shutdown and interrupt pins. Then we initialize our sensor object in the `setup()` loop. The code to do this is shown below.

    language:c
    #include <Wire.h>
    #include "SparkFun_VL53L1X.h"

    //Optional interrupt and shutdown pins.
    #define SHUTDOWN_PIN 2
    #define INTERRUPT_PIN 3

    SFEVL53L1X distanceSensor(Wire, SHUTDOWN_PIN, INTERRUPT_PIN);

    void setup(void)
    

Once we\'ve initialized our sensor, we can start grabbing measurements from it. To do this, we send some configuration bytes to our sensor using `distanceSensor.startRanging()` to initiate the measurement. We then wait for data to become available and when it does, we read it in, convert it from millimeters to feet, and print it out over serial. The `void loop()` function that does this is shown below.

    language:c
    void loop(void)
    

Opening your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) to a baud rate of **9600** should show the distance between the sensor and the object it\'s pointed at in both millimeters and feet. The output should look something like the below image.

[![Read Distance](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/4/EX1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/4/EX1.PNG)\
*Distance readings in mm and ft*

## Troubleshooting

Below, we have also included some additional troubleshooting tips for issues that you may come across with the new RedBoard (Qwiic).

1.  One of our employees compiled a great [list of troubleshooting tips](https://learn.sparkfun.com/tutorials/sparkfun-troubleshooting-tips) based on the most common customer issues. This is the perfect place to start.
2.  For any Arduino IDE specific issues, I recommend starting with their [troubleshooting guide](https://www.arduino.cc/en/Guide/Troubleshooting).

If neither of the troubleshooting guides above were able to help, here are some tips you might have missed. (Most of this material is summarized from the tutorial.):

### Are You Using a Recommended Computer OS?

This board is not tested using the Arduino Web IDE. We do [**NOT**] recommend using a Chromebook, Netbook, tablet, phone, or the Arduino Web IDE in general. If you are here, try a [**RECOMMENDED**] operating system (see [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide#installing-the-arduino-ide)).

### My Board Isn\'t Working:

Every board that **we** manufacture gets tested. If you didn\'t buy the board from us or one of our authorized distributors, it could be a knock-off. That being said, let\'s try a basic test to see if just the board is working. Disconnect everything that you have attached to the board; we just want to test the board.

1.  **Inspect the board:**\
    Check the board to make sure everything looks about right. Use the pictures on the [product page](https://www.sparkfun.com/products/15123) to verify component placement or alignment, and bad solder joints, or damage.
2.  **Power and check the status LEDs:**\
    Using a known good [USB micro-B cable](https://www.sparkfun.com/products/10215), plug your board in to the computer. Do any of the status LEDs turn on (see [Hardware Overview](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide#hardware-overview))?
    - New boards will come programmed with a test sketch that cycles between the RX and TX LEDs.
3.  **Upload the *Blink* sketch:**\
    Try to upload a blink sketch. Why blink? It is simple, known to work (from the example files), and you have an indicator LED.
    - Double check that you have the proper **Board** and **Serial Port** selected.
    - For boards that are already running the blink example, I recommend changing the timing parameters to check for a change in the board\'s response.

    Verify that you see the status LED blinking properly and that the Arduino IDE shows a status of \"**Done uploading.**\"

### I Don\'t See My Board on a Serial/COM Port:

If you don\'t see your board as an available COM port on the Arduino IDE:

- Try to re-open the Arduino IDE.
- Check the **Device Manager** to verify that your computer recognizes the board. Click the **Driver Verification** button in the [Installing Drivers](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide#installing-drivers) section of the tutorial.
- If you have previously installed the **older CH340G drivers**, you may need to update your drivers. Particularly on Macs, you will need to delete the previous drivers and install the updated drivers.
- If that is not the case, you issue might be related to your USB cable. Check that you are using a USB cable capable of data transfers. **Some cables only have the power pins connected for charging**. A good way to test this is to plug in a device to your USB cable (like a phone). If it doesn\'t show up as a device or drive, then try a new [USB micro-B cable](https://www.sparkfun.com/products/10215).
- This rarely happens, but it is easy to check. If you are using a USB 3.0 port (you will see a blue \"*tongue*\" in the USB jack or bad USB port, try a different USB port. You can also try to test the board on a different computer to double check for a hardware incompatibility (usually with expansion boards).

### Errors Uploading to the Board:

There are two types of issues that you will usually see in the console of the Arduino IDE, compile errors or upload errors. The easiest way to see where to start is by clicking the **Verify** button (check mark); the Arduino IDE will try to compile your code. A failure here is a compile error.

It takes a some experience, but if you enable the verbose output from the Arduino IDE **preferences**, it may give you more clues to where the issue is.

[![Screen shots of enabling verbose output](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/Enable_Verbose_Output.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Enable_Verbose_Output.png)

*Screen shots of how to enable verbose output. **Click** to enlarge.*

- **Compile Errors:**\
  With compile errors, there are several things that could be causing issues. However, 99% of the time, it is user error. Usually something wrong with your code or the library you are using. Once in a while you will have a file structure issue if you manually added a file/folder in any of the Arduino folders (still user error).
- **Upload Errors:**\
  Upload errors get a little more tricky. You will usually just see the Arduino IDE trying to upload to the board multiple times. There are usually several different causes for this, often without specific errors in the console. Here are a few common examples:
  - Wrong Board Selection:\
    Double check you board selection options. If you uploaded with the wrong board selection, there is a small chance that you may have overwritten the bootloader on the board or damaged the microcontroller.
  - Missing Bootloader:\
    If your board has the bootloader flashed, pin 13 will flash several times on power up.
  - Serial Port Interference:\
    If a device is communicating to the microcontroller over digital pins 0 and 1, while you are trying to upload code.
  - Bad USB cable or port (see Serial Port section above).

### Additional Tips:

- If an input pin is read and that is floating (with nothing connected to it), you will see random data/states. In practice, it may be useful to tie an input pin to a known state with a pullup resistor (to VCC), or a pulldown resistor (to GND).

- Pin 13 is difficult to use as a digital input because of the voltage drop from status LED and resistor soldered in series to it. If you must use pin 13 as a digital input, it is recommended that you set the pinMode() as an INPUT and use an external pulldown resistor.

- The maximum current an I/O pin can source (provide positive current) or sink (provide negative current) is 40 mA (milliamps). You can power small sections of LED strips or small motors, but will run into issue with high power devices.

- Be sure to double check that you are not trying to use an I^2^C device while you are trying use analog pins A4 or A5 to read analog data. You will run into issues where the analog read will appear to be at a constant value. As a result, the analog readings will not reflect the changes seen from the sensor output. You can only do one or the other.

- Using the Serial Peripheral Interface, configures the SCK and MOSI pins to be directly managed by the SPI hardware. Therefore, while in use, pins 11 and 13 can\'t be used (i.e. the LED on pin 13 can no longer be used as a debug/status indicator.) Executing \"SPI.end();\" allows those pins 11 and 13 to be used as general I/O again.

- This issue doesn\'t happen too often, but it can be *arbitrarily, common*: If your mouse pointer begins to move erratically, your mouse becomes unresponsive to your inputs, and your board is sending a lot of serial data, there is a chance that your computer thinks your board as a serial mouse. The fix is to unplug your board and the plug it back in while holding the reset button down, giving your computer a chance enumerate the COM port.