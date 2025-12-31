# Source: https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Getting Started with the Artemis Development Kit

# Getting Started with the Artemis Development Kit

[≡ Pages](#)

Contributors: [ santaimpersonator], [![](https://cdn.sparkfun.com/avatar/92955b303c984cbfe9a72102a670afc7?d=retro&s=20&r=pg) Liquid Soulder], [ Member #1571936]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1198&name=Getting+Started+with+the+Artemis+Development+Kit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1198 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+the+Artemis+Development+Kit&url=http%3A%2F%2Fsfe.io%2Ft1198&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1198&t=Getting+Started+with+the+Artemis+Development+Kit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1198&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F1%2F9%2F8%2Fexample_blink.gif&description=Getting+Started+with+the+Artemis+Development+Kit "Pin It")

## Introduction

**OS Requirements:** The software utilized to program and use the Artemis Development Kit (ADK) may have limitations on various operating systems (OS):

- **Window 10** (or later) is required for almost all the additional software required for the ADK.
- Currently (7/7/20), there are no limitations for **Mac OS** due to their required OS updates.
- For **Linux** users, we have tested our instructions on Ubuntu 18.04.4 LTS desktop. Users may need to verify the software compatibility for their Linux distribution. In addition, users may need to adapt our instructions to their flavor of Linux.

**Mbed™ Release:** Pending the adoption of the Artemis module into Mbed™ OS, we have temporarily omitted parts of this tutorial. Users looking to get a jump start with Mbed™, can check out this [short tutorial on the *beta* version](https://learn.sparkfun.com/tutorials/artemis-development-on-arm-mbed-os-beta).

The [Artemis Development Kit](https://www.sparkfun.com/products/16828) and [Artemis Development Kit (with Camera)](https://www.sparkfun.com/products/17071) are the latest development kit from our [Artemis family of products](https://www.sparkfun.com/artemis). If you are looking to push the edge of your software development skills, the Artemis Development Kit is what you have been waiting for!

[![SparkFun Artemis Development Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/7/4/6/16828-SparkFun_Artemis_Development_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-artemis-development-kit.html)

### [SparkFun Artemis Development Kit](https://www.sparkfun.com/sparkfun-artemis-development-kit.html) 

[ DEV-16828 ]

The Artemis Development Kit based on the SparkFun Artemis Module and highlights software development features like Arm® Mbed...

**Retired**

[![SparkFun Artemis Development Kit with Camera](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/0/3/2/17071-SparkFun_Artemis_Development_Kit_with_Camera-01.jpg)](https://www.sparkfun.com/sparkfun-artemis-development-kit-with-camera.html)

### [SparkFun Artemis Development Kit with Camera](https://www.sparkfun.com/sparkfun-artemis-development-kit-with-camera.html) 

[ KIT-17071 ]

This Kit includes the SparkFun Artemis DK board as well as the accessories (Himax camera & USB-C cable) needed to get started...

**Retired**

This guide will cover the general design of the development board and the installation of the recommended software used to program the Artemis DK. The primary development programs are the AmbiqSDK, Mbed™ OS, and the Arduino IDE. In addition, we have provided basic examples to verify the operation of the board. For more advanced functionalities, we have software development guides for each of the recommended software platforms that users can reference.

*Product showcase video.*

*Livestream of the product demonstration with Mbed™.\
Users may need to watch the video on [YouTube](https://youtu.be/o3ffhf3z6so).*

**Note:** We do

[NOT] recommend novices begin with this board. There are a lot of details and fundamental knowledge involved with the use of this board. The content of this hardware guide alone can be daunting; not to mention, the three software development guides associated with this board, which can also be overwhelming for a first-time user.

Those who have become familiar with programming and electronic hardware will have an easier time developing with the Artemis DK as various components of this tutorial are geared towards the *professional* software developer.

### Required Materials

To get started, users will need a few items. Now some users may have a few of these items, feel free to modify your cart accordingly.

- [SparkFun Artemis Development Kit](https://www.sparkfun.com/products/16828) or [SparkFun Artemis Development Kit (with Camera)](https://www.sparkfun.com/products/17071)
- [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/products/14743) - The USB interface serves two purposes: it powers the board and allows you to upload programs to it. (*\*If your computer doesn\'t provide a USB-A slot, then you will need to choose an appropriate cable or purchase an adapter as well.*)
- [Himax CMOS Imaging Camera - HM01B0](https://www.sparkfun.com/products/15570) - The camera is optional, but is recommended for users interested in visual recognition applications. (*\* The camera is included in the [SparkFun Artemis Development Kit (with Camera)](https://www.sparkfun.com/products/17071).*)
- Computer with the an operating system (OS) that is compatible with all the software installation requirements.

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![SparkFun Artemis Development Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/4/6/16828-SparkFun_Artemis_Development_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-artemis-development-kit.html)

### [SparkFun Artemis Development Kit](https://www.sparkfun.com/sparkfun-artemis-development-kit.html) 

[ DEV-16828 ]

The Artemis Development Kit based on the SparkFun Artemis Module and highlights software development features like Arm® Mbed...

**Retired**

[![Himax CMOS Imaging Camera - HM01B0 (Monochrome)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/1/6/5/15570-Himax_Imaging_Camera-01.jpg)](https://www.sparkfun.com/himax-cmos-imaging-camera-hm01b0.html)

### [Himax CMOS Imaging Camera - HM01B0 (Monochrome)](https://www.sparkfun.com/himax-cmos-imaging-camera-hm01b0.html) 

[ SEN-15570 ]

An ultra low power CMOS Image Sensor that enables the integration of an "Always On" camera for computer vision applicatio...

[ [\$10.95] ]

[![SparkFun Artemis Development Kit with Camera](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/0/3/2/17071-SparkFun_Artemis_Development_Kit_with_Camera-01.jpg)](https://www.sparkfun.com/sparkfun-artemis-development-kit-with-camera.html)

### [SparkFun Artemis Development Kit with Camera](https://www.sparkfun.com/sparkfun-artemis-development-kit-with-camera.html) 

[ KIT-17071 ]

This Kit includes the SparkFun Artemis DK board as well as the accessories (Himax camera & USB-C cable) needed to get started...

**Retired**

#### Jumper Modification

If you would like to modify the jumpers, you will need [soldering equipment](https://www.sparkfun.com/categories/49) and/or a [hobby knife](https://www.sparkfun.com/categories/379).

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

#### Programming Firmware

Users interested in modifying or updating the firmware on the NXP chip will need an [Arm^®^ Programmer](https://www.sparkfun.com/categories/26) and need to solder on a [JTAG header](https://www.sparkfun.com/products/15362). The same programmer and an [**additional** header](https://www.sparkfun.com/products/15362) can also be used to program and debug the Atermis module. We recommend these programmers from our catalog:

[![Straight Header - Male (PTH, 0.05in., 2x5-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/0/0/15362-Male_2x5_1.27mm_headers-01.jpg)](https://www.sparkfun.com/header-2x5-pin-male-1-27mm.html)

### [Straight Header - Male (PTH, 0.05in., 2x5-Pin)](https://www.sparkfun.com/header-2x5-pin-male-1-27mm.html) 

[ PRT-15362 ]

This is a super small, 2x5 pin male PTH header. This header is in the common configuration for JTAG applications.

[ [\$1.95] ]

[![J-Link EDU Mini Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/2/15345-J-Link_EDU_Mini-01a.jpg)](https://www.sparkfun.com/products/15345)

### [J-Link EDU Mini Programmer](https://www.sparkfun.com/products/15345) 

[ PGM-15345 ]

Tiny J-Link programmer for programming any ARM microconroller. Comes with an educational/ non-commercial license.

**Retired**

[![J-Link EDU Base Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/3/15346-J-Link_EDU_Base-01.jpg)](https://www.sparkfun.com/products/15346)

### [J-Link EDU Base Programmer](https://www.sparkfun.com/products/15346) 

[ PGM-15346 ]

J-Link programmer for programming any ARM microconroller. Comes with an educational/ non-commercial license.

**Retired**

[![J-Link BASE Compact Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/4/15347-J-Link_Base_Compact-01.jpg)](https://www.sparkfun.com/products/15347)

### [J-Link BASE Compact Programmer](https://www.sparkfun.com/products/15347) 

[ PGM-15347 ]

Compact J-Link programmer for programming any ARM microconroller.

**Retired**

### Suggested Reading

As a more professionally oriented product, we will skip over the more fundamental tutorials (i.e. [**Ohm\'s Law**](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) and [**What is Electricity?**](https://learn.sparkfun.com/tutorials/what-is-electricity)). However, below are a few tutorials that may help users familiarize themselves with various aspects of the board.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/bluetooth-basics)

### Bluetooth Basics 

An overview of the Bluetooth wireless technology.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/arm-programming)

### ARM Programming 

How to program SAMD21 or SAMD51 boards (or other ARM processors).

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide)

### Artemis Development with the Arduino IDE 

This is an in-depth guide on developing in the Arduino IDE for the Artemis module and any Artemis microcontroller development board. Inside, users will find setup instructions and simple examples from blinking an LED and taking ADC measurements; to more complex features like BLE and I2C.

[](https://learn.sparkfun.com/tutorials/artemis-development-with-arduino)

### Artemis Development with Arduino 

Get our powerful Artemis based boards (Artemis Nano, BlackBoard Artemis, and BlackBoard Artemis ATP) blinking in less than 5 minutes using the SparkFun Artemis Arduino Core!

[](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk)

### Using SparkFun Edge Board with Ambiq Apollo3 SDK 

We will demonstrate how to get started with your SparkFun Edge Board by setting up the toolchain on your computer, examining an example program, and using the serial uploader tool to flash the chip.

[](https://learn.sparkfun.com/tutorials/designing-with-the-sparkfun-artemis)

### Designing with the SparkFun Artemis 

Let\'s chat about layout and design considerations when using the Artemis module.

[](https://learn.sparkfun.com/tutorials/programming-the-sparkfun-edge-with-arduino)

### Programming the SparkFun Edge with Arduino 

Running low-power machine learning examples on the SparkFun Edge can now be done using the familiar Arduino IDE. In this follow-up to the initial Edge tutorial, we\'ll look at how to get three examples up and running without the need to learn an entirely new SDK.

[](https://learn.sparkfun.com/tutorials/artemis-development-on-arm-mbed-os-beta)

### Artemis Development on Arm® Mbed™ OS (Beta) 

With the latest Artemis DK, board, we now offer full Bluetooth support within the Arduino IDE and development with Mbed™ OS. While we have worked tirelessly to get the Artemis module supported in the next Mbed™ OS release, the next release isn\'t slated until after the Artemis DK becomes available to the public. Therefore, this post will provide users with a jump start for developing with Mbed™ Studio, prior to the next release (in a beta of sorts), by utilizing our fork of Mbed™ OS.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit)

### Getting Started with the micro:bit 

The BBC micro:bit is a compact, powerful programming tool that requires no software installation. Read on to learn how to use it YOUR way!

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

One of the new, advanced features of the board is that it takes advantage of the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials. Click on the banner above to learn more about [Qwiic products](https://www.sparkfun.com/qwiic).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1198&name=Getting+Started+with+the+Artemis+Development+Kit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1198 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+the+Artemis+Development+Kit&url=http%3A%2F%2Fsfe.io%2Ft1198&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1198&t=Getting+Started+with+the+Artemis+Development+Kit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1198&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F1%2F9%2F8%2Fexample_blink.gif&description=Getting+Started+with+the+Artemis+Development+Kit "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/hardware-overview) [Software Overview](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/software-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/hardware-assembly) [Arduino Examples](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/arduino-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/discuss) [Single Page](https://learn.sparkfun.com/tutorials/getting-started-with-the-artemis-development-kit/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Artemis](https://learn.sparkfun.com/tutorials/tags/artemis)
  - [BLE](https://learn.sparkfun.com/tutorials/tags/ble)
  - [Bluetooth Low Energy](https://learn.sparkfun.com/tutorials/tags/bluetooth-low-energy)
  - [Computer Engineering](https://learn.sparkfun.com/tutorials/tags/computer-engineering-)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [mBed](https://learn.sparkfun.com/tutorials/tags/mbed)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Prototyping](https://learn.sparkfun.com/tutorials/tags/prototyping)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]