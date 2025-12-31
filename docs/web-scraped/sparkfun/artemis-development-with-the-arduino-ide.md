# Source: https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Artemis Development with the Arduino IDE

# Artemis Development with the Arduino IDE

[≡ Pages](#)

Contributors: [ santaimpersonator], [![](https://cdn.sparkfun.com/avatar/92955b303c984cbfe9a72102a670afc7?d=retro&s=20&r=pg) Liquid Soulder], [ Member #1571936]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1264&name=Artemis+Development+with+the+Arduino+IDE "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1264 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Artemis+Development+with+the+Arduino+IDE&url=http%3A%2F%2Fsfe.io%2Ft1264&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1264&t=Artemis+Development+with+the+Arduino+IDE "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1264&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F6%2F4%2Fcombo_logo.png&description=Artemis+Development+with+the+Arduino+IDE "Pin It")

## Introduction

The [SparkFun Artemis](https://www.sparkfun.com/products/15484) is an amazing module. So much functionality packed into a tiny 10x15mm footprint! But what really makes it powerful is the ability to quickly write sketches and build projects using only Arduino code. However, for more industry oriented programmer, it is also compatible with Arm® Mbed™ OS. Whether you are using one of our boards that has the Artemis module pre-integrated or have your own, this tutorial will get you started with the Arduino IDE and familiarize you with the various interfaces of the Artemis module.

[![SparkFun Artemis Module - Low Power Machine Learning BLE Cortex-M4F](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/7/4/15484-SparkFun_Artemis_Module_-_Low_Power_Machine_Learning_BLE_Cortex-M4F-01b.jpg)](https://www.sparkfun.com/sparkfun-artemis-module-low-power-machine-learning-ble-cortex-m4f.html)

### [SparkFun Artemis Module - Low Power Machine Learning BLE Cortex-M4F](https://www.sparkfun.com/sparkfun-artemis-module-low-power-machine-learning-ble-cortex-m4f.html) 

[ WRL-15484 ]

The Artemis Module from SparkFun is the first FCC certified, open-source, Cortex-M4F with BLE 5.0 running up to 96MHz and wit...

[ [\$9.95] ]

*Product showcase of the new Artemis module.*

### Required Materials

To follow along with this tutorial, you\'ll need development board with an Artemis module and a USB-C cable.

[![SparkFun RedBoard Artemis ATP](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/7/15442-SparkFun_RedBoard_Artemis_ATP-05.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis-atp.html)

### [SparkFun RedBoard Artemis ATP](https://www.sparkfun.com/sparkfun-redboard-artemis-atp.html) 

[ DEV-15442 ]

The RedBoard Artemis ATP has 48 GPIO and this board breaks out all of them in an Arduino Mega format.

[ [\$30.95] ]

[![SparkFun Artemis Module - Low Power Machine Learning BLE Cortex-M4F](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/7/4/15484-SparkFun_Artemis_Module_-_Low_Power_Machine_Learning_BLE_Cortex-M4F-01b.jpg)](https://www.sparkfun.com/sparkfun-artemis-module-low-power-machine-learning-ble-cortex-m4f.html)

### [SparkFun Artemis Module - Low Power Machine Learning BLE Cortex-M4F](https://www.sparkfun.com/sparkfun-artemis-module-low-power-machine-learning-ble-cortex-m4f.html) 

[ WRL-15484 ]

The Artemis Module from SparkFun is the first FCC certified, open-source, Cortex-M4F with BLE 5.0 running up to 96MHz and wit...

[ [\$9.95] ]

[![SparkFun Thing Plus - Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/1/7/0/15574-SparkFun_Thing_Plus_-_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html)

### [SparkFun Thing Plus - Artemis](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html) 

[ WRL-15574 ]

The SparkFun Artemis Thing Plus takes our popular Feather footprint and adds in the powerful Artemis module for ultimate func...

[ [\$25.95] ]

[![SparkFun OpenLog Data Collector with Machinechat - Base Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/0/8/KIT-20673_SparkFun___Machinechat_Qwiic_loT_Data_Mo-_01.jpg)](https://www.sparkfun.com/sparkfun-openlog-data-collector-with-machinechat-base-kit.html)

### [SparkFun OpenLog Data Collector with Machinechat - Base Kit](https://www.sparkfun.com/sparkfun-openlog-data-collector-with-machinechat-base-kit.html) 

[ KIT-20673 ]

The Base version of the SparkFun OpenLog Data Collector Kit with Machinechat is an easy way to organize and display your data...

[ [\$244.95] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![USB 2.0 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/5/0/15092-USB_2.0_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/products/15092)

### [USB 2.0 Cable A to C - 3 Foot](https://www.sparkfun.com/products/15092) 

[ CAB-15092 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

**Retired**

[![USB 2.0 C to C Cable - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/2/1/16395-USB_Type_C_to_Type_C_Cable_-_1_Meter__100W__USB_2.0-02.jpg)](https://www.sparkfun.com/usb-2-0-c-to-c-cable-1m.html)

### [USB 2.0 C to C Cable - 1m](https://www.sparkfun.com/usb-2-0-c-to-c-cable-1m.html) 

[ CAB-16395 ]

This is a 1m long USB 2.0 Type C to Type C cable with a 100W current rating.

**Retired**

#### Programming Firmware

Users interested in flashing their module will need an [ARM Programmer](https://www.sparkfun.com/categories/26) and need to solder on a [JTAG header](https://www.sparkfun.com/products/15362). We recommend these programmers from our catalog:

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

### Examples

Some of the Arduino examples in this tutorial will require additional hardware.

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Trimpot 10K Ohm with Knob](https://cdn.sparkfun.com/r/140-140/assets/parts/3/8/2/3/09806-01.jpg)](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html)

### [Trimpot 10K Ohm with Knob](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html) 

[ COM-09806 ]

This 10K trimmable potentiometer has a small knob built right in and it\'s breadboard friendly to boot!

[ [\$1.25] ]

[![SparkFun Environmental Sensor Breakout - BME680 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/3/2/9/16466-SparkFun_Environmental_Sensor_Breakout_-_BME680__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-environmental-sensor-breakout-bme680-qwiic.html)

### [SparkFun Environmental Sensor Breakout - BME680 (Qwiic)](https://www.sparkfun.com/sparkfun-environmental-sensor-breakout-bme680-qwiic.html) 

[ SEN-16466 ]

This SparkFun Environmental Sensor is a breakout for the 4-in-1 BME680 gas sensor from Bosch.

[ [\$22.95] ]

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![Jumper Wires Premium 6\" M/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/5/7/09140-02-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html)

### [Jumper Wires Premium 6\" M/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html) 

[ PRT-09140 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumper wires terminated as male to female. Use these to jumper fro...

[ [\$4.60] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

[![Zio Qwiic OLED Display (0.91 in, 128x32)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/6/9/16774-ZIO_OLED_Display__0.91_in__128x32__Qwiic_-01.jpg)](https://www.sparkfun.com/zio-qwiic-oled-display-0-91-in-128x32.html)

### [Zio Qwiic OLED Display (0.91 in, 128x32)](https://www.sparkfun.com/zio-qwiic-oled-display-0-91-in-128x32.html) 

[ LCD-16774 ]

This OLED Display from Zio can display up to 3 lines of text, is thinner & consumes less power than an LCD, & uses fast refre...

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/bluetooth-basics)

### Bluetooth Basics 

An overview of the Bluetooth wireless technology.

[](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino)

### Processor Interrupts with Arduino 

What is an interrupt? In a nutshell, there is a method by which a processor can execute its normal program while continuously monitoring for some kind of event, or interrupt. There are two types of interrupts: hardware and software interrupts. For the purposes of this tutorial, we will focus on hardware interrupts.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/designing-with-the-sparkfun-artemis)

### Designing with the SparkFun Artemis 

Let\'s chat about layout and design considerations when using the Artemis module.

[](https://learn.sparkfun.com/tutorials/artemis-development-with-arduino)

### Artemis Development with Arduino 

Get our powerful Artemis based boards (Artemis Nano, BlackBoard Artemis, and BlackBoard Artemis ATP) blinking in less than 5 minutes using the SparkFun Artemis Arduino Core!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1264&name=Artemis+Development+with+the+Arduino+IDE "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1264 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Artemis+Development+with+the+Arduino+IDE&url=http%3A%2F%2Fsfe.io%2Ft1264&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1264&t=Artemis+Development+with+the+Arduino+IDE "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1264&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F6%2F4%2Fcombo_logo.png&description=Artemis+Development+with+the+Arduino+IDE "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/all) [Next Page →\
[Do I Need Drivers?]](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/do-i-need-drivers)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/introduction) [Do I Need Drivers?](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/do-i-need-drivers) [Setting up the Arduino IDE](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/setting-up-the-arduino-ide) [Programming the Artemis Module](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/programming-the-artemis-module) [Status LED: Blink](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/status-led-blink) [Serial Port: Hello World and Enabling Peripherals](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/serial-port-hello-world-and-enabling-peripherals) [ADC: AnalogRead](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/adc-analogread) [PWM: AnalogWrite](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/pwm-analogwrite) [I2C: Qwiic OLED Display](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/i2c-qwiic-oled-display) [SPI: BME680 Environmental Sensor](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/spi-bme680-environmental-sensor) [Bluetooth: LED](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/bluetooth-led) [What About Interrupts?](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/what-about-interrupts) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/resources-and-going-further)

[Comments [1]](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Artemis](https://learn.sparkfun.com/tutorials/tags/artemis)
  - [BLE](https://learn.sparkfun.com/tutorials/tags/ble)
  - [Bluetooth Low Energy](https://learn.sparkfun.com/tutorials/tags/bluetooth-low-energy)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [SparkFun Edge](https://learn.sparkfun.com/tutorials/tags/sparkfun-edge)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]