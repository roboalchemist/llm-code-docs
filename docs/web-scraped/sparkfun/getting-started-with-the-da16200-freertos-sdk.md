# Source: https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Getting Started with the DA16200 FreeRTOS SDK

# Getting Started with the DA16200 FreeRTOS SDK

[≡ Pages](#)

Contributors: [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2418&name=Getting+Started+with+the+DA16200+FreeRTOS+SDK "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2418 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+the+DA16200+FreeRTOS+SDK&url=http%3A%2F%2Fsfe.io%2Ft2418&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2418&t=Getting+Started+with+the+DA16200+FreeRTOS+SDK "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2418&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F4%2F1%2F8%2Fthumbnail.jpg&description=Getting+Started+with+the+DA16200+FreeRTOS+SDK "Pin It")

## Introduction

**Note:** Before getting started with this tutorial, users should familiarize themselves with the [**DA16200 FreeRTOS Getting Started Guide**](https://www.renesas.com/us/en/document/qsg/um-wi-056-da16200-da16600-freertos-getting-started-guide?language=en&r=1599971) for the DA16200MOD.

This tutorial is meant to supplement the [**DA16200 FreeRTOS Getting Started Guide**](https://www.renesas.com/us/en/document/qsg/um-wi-056-da16200-da16600-freertos-getting-started-guide?language=en&r=1599971) and adapt the information specifically, to our DA16200 boards. The majority of the material in this tutorial, including the installation and examples, are derived from that manual.

Additionally, users should note that the information in this tutorial may become depricated and hyperlinks may break as Dialog/Renesas provides new software releases. Please, refer to the [DA16200 product page](https://www.renesas.com/us/en/products/interface-connectivity/wireless-communications/wi-fi/low-power-wi-fi/da16200mod-ultra-low-power-wi-fi-modules-battery-powered-iot-devices#document) for the latest updates and resources.

**Advanced Software:** Novice users, may find the amount information contained in this tutorial somewhat daunting. The SDK and IDE are relatively complex.

- For beginners, who have never programmed; we highly recommend that these users begin with a simpler microcontroller learning kit; such as the [SparkFun Inventor\'s Kit (SIK)](https://www.sparkfun.com/products/15631). The kit utilizes a simpler development and programming platform called the [Arduino IDE](https://www.arduino.cc/en/Guide/Environment).

**System Requirements:** The minimum system requirements for the DA16200 FreeRTOS SDK are:

[**Windows 10**] and [**Ubuntu 20.04.1 LTS**]

- *Users may need administrative privileges to install some of the following software.*

[xPack Project Manager:](https://xpack.github.io/install/)

- GNU Arm GCC 10.2.1
- Windows: Windows Build Tools

[Eclipse 2020-09](https://www.eclipse.org/downloads/packages/installer)

[DA16200 FreeRTOS SDK](https://www.renesas.com/us/en/products/interface-connectivity/wireless-communications/wi-fi/low-power-wi-fi/da16200-ultra-low-power-wi-fi-soc-battery-powered-iot-devices#tab-software-and-tools)

Serial Terminal with Y-Modem support

- Windows: [Tera Term](http://www.teraterm.org/) *(Recommended)*
- Linux: minicom *(Recommended)*

*\*For more information on the required software, please refer to the [DA16200 FreeRTOS Getting Started Guide](https://www.renesas.com/us/en/document/qsg/um-wi-056-da16200-da16600-freertos-getting-started-guide?language=en&r=1599971).*

Manufactured by [Dialog (a subsidiary of Renesas)](https://www.dialog-semiconductor.com/), the DA16200MOD is a highly integrated ultra-low power Wi-Fi system on chip (SoC). The DA16200 contains a 802.11b/g/n radio (PHY), a baseband processor, a media access controller (MAC), on-chip memory, and a host networking application processor, all on a single silicon die. With multiple sleep modes (down to 0.2 - 3.5 µA), the DA16200MOD perfect for your next IoT project. Additionally, the SoC has full offload capabilities to run the entire networking OS and TCP/IP stack on chip; therefore, an external network processor, CPU, or microcontroller are not required.

\
*Arm Smart Home with SparkFun and Renesas DA16200 (Source: [Arm](https://www.arm.com/))*

Users can utilize the DA16200 FreeRTOS SDK and the Eclipse IDE on either a Windows 10 or Linux computer, to develop their Wi-Fi solutions. This guide will walk users through the download and installation process to get started with the DA16200 FreeRTOS SDK. Then, users will be shown the basic examples for the peripheral pin functions.

[![SparkFun Qwiic WiFi Shield - DA16200](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/0/2/6/18567-SparkFun_Qwiic_WiFi_Shield_-_DA16200-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-wifi-shield-da16200.html)

### [SparkFun Qwiic WiFi Shield - DA16200](https://www.sparkfun.com/sparkfun-qwiic-wifi-shield-da16200.html) 

[ WRL-18567 ]

SparkFun has teamed up with ARM and Dialog to provide you with this WiFi Shield based around the DA16200 module.

[ [\$19.95] ]

[![SparkFun MicroMod WiFi Function Board - DA16200](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/0/8/5/18594-MicroMod_DA16200_Function_Board-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-wifi-function-board-da16200.html)

### [SparkFun MicroMod WiFi Function Board - DA16200](https://www.sparkfun.com/sparkfun-micromod-wifi-function-board-da16200.html) 

[ WRL-18594 ]

The SparkFun MicroMod DA16200 Function Board adds a fully integrated WiFi module to any MicroMod project.

[\$29.95] [ [\$14.98] ]

[![SparkFun Thing Plus - DA16200](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/3/9/3/DA16200-_01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-da16200.html)

### [SparkFun Thing Plus - DA16200](https://www.sparkfun.com/sparkfun-thing-plus-da16200.html) 

[ WRL-19696 ]

The SparkFun DA16200 Thing Plus utilizes a highly integrated ultra-low power WiFi system on chip that allows users to develop...

[\$34.95] [ [\$14.95] ]

### Required Materials

To follow along with this guide, we recommend the hardware below. Users will need a DA16200 module and a way to connect it to their computer.

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![SparkFun Thing Plus - DA16200](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/3/9/3/DA16200-_01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-da16200.html)

### [SparkFun Thing Plus - DA16200](https://www.sparkfun.com/sparkfun-thing-plus-da16200.html) 

[ WRL-19696 ]

The SparkFun DA16200 Thing Plus utilizes a highly integrated ultra-low power WiFi system on chip that allows users to develop...

[\$34.95] [ [\$14.95] ]

### Suggested Reading

If you\'re unfamiliar with serial terminals, jumper pads, or I^2^C be sure to checkout some of these foundational tutorials.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide)

### Dialog ULP WiFi DA16200 R3 Shield Hookup Guide 

Add WiFi to your project with this hookup guide for our Dialog\'s Ultra Low Power DA16200 R3 shield!

[](https://learn.sparkfun.com/tutorials/micromod-wifi-function-board---da16200-hookup-guide)

### MicroMod WiFi Function Board - DA16200 Hookup Guide 

Add IoT functionality to any MicroMod project with the MicroMod WiFi function Board - DA16200!

[](https://learn.sparkfun.com/tutorials/da16200-thing-plus-hookup-guide)

### DA16200 Thing Plus Hookup Guide 

A guide to get started with the DA16200 Thing Plus.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/connectivity-of-the-internet-of-things)

### Connectivity of the Internet of Things 

An overview of the different protocols that can be used for the development of Internet of Things (IoT)-based projects.

[](https://learn.sparkfun.com/tutorials/arm-programming)

### ARM Programming 

How to program SAMD21 or SAMD51 boards (or other ARM processors).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2418&name=Getting+Started+with+the+DA16200+FreeRTOS+SDK "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2418 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+the+DA16200+FreeRTOS+SDK&url=http%3A%2F%2Fsfe.io%2Ft2418&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2418&t=Getting+Started+with+the+DA16200+FreeRTOS+SDK "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2418&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F4%2F1%2F8%2Fthumbnail.jpg&description=Getting+Started+with+the+DA16200+FreeRTOS+SDK "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/all) [Next Page →\
[FreeRTOS and SDK]](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/freertos-and-sdk)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/introduction) [FreeRTOS and SDK](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/freertos-and-sdk) [Software Setup](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/software-setup) [Serial Debug Interface](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/serial-debug-interface) [Build an Example Project](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/build-an-example-project) [Programming and Debugging](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/programming-and-debugging) [Example: GPIO Control](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/example-gpio-control) [Example: I2C](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/example-i2c) [Example: WiFi](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/example-wifi) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/discuss) [Single Page](https://learn.sparkfun.com/tutorials/getting-started-with-the-da16200-freertos-sdk/all) [Print]

- **Tags**
- - [Development](https://learn.sparkfun.com/tutorials/tags/development)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Skill](https://learn.sparkfun.com/tutorials/tags/skill)
  - [Start a Project](https://learn.sparkfun.com/tutorials/tags/start-a-project)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]