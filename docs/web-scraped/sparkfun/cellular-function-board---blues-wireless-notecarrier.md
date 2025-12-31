# Source: https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Cellular Function Board - Blues Wireless Notecarrier

# Cellular Function Board - Blues Wireless Notecarrier

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2650&name=Cellular+Function+Board+-+Blues+Wireless+Notecarrier "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2650 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Cellular+Function+Board+-+Blues+Wireless+Notecarrier&url=http%3A%2F%2Fsfe.io%2Ft2650&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2650&t=Cellular+Function+Board+-+Blues+Wireless+Notecarrier "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2650&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F6%2F5%2F0%2FMM_Cellular_FB_-_Blues_Wireless_Single.jpg&description=Cellular+Function+Board+-+Blues+Wireless+Notecarrier "Pin It")

## Introduction

The [SparkFun Cellular Function Board - Blues Wireless Notecarrier](https://www.sparkfun.com/products/20409) features the Notecard from [Blues Wireless](https://blues.io/). The Notecard is unique among cellular modules as it has a built-in SIM card and includes a 10 year subscription and 500MB of data included in the price. The Notecard module also comes with integrated cellular, SIM, onboard GPS, 3-axis accelerometer with an on-chip temperature sensor. On top of that, the Notecard features outboard device firmware updates (DFU) meaning you can reprogram a connected Processor remotely through Blues\' Notehub service! There are some limitations to this process so make sure to read further in this guide for more information on how to properly perform Outboard device firmware updates.

[![SparkFun MicroMod Cellular Function Board - Blues Wireless Notecarrier](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/2/2/7/Function_Board-_05.jpg)](https://www.sparkfun.com/sparkfun-micromod-cellular-function-board-blues-wireless-notecarrier.html)

### [SparkFun MicroMod Cellular Function Board - Blues Wireless Notecarrier](https://www.sparkfun.com/sparkfun-micromod-cellular-function-board-blues-wireless-notecarrier.html) 

[ WRL-20409 ]

The SparkFun Notecarrier Cellular Function Board adds a cellular modem to the MicroMod ecosystem using the Notecard - NOTE-NB...

[\$119.95] [ [\$64.95] ]

The MicroMod Cellular Function Board includes everything you need : a carrier board (Blues calls them Notecarriers) and the globally enabled NB-IoT & LTE-M M.2 based module (Blues calls them Notecards).

### Required Materials

The following materials are necessary for following along with this guide *(check out our all inclusive, [starter kit](https://www.sparkfun.com/products/21702))*. All Function Boards require a Main Board and Processor to connect to each other. Depending on your application, you may need a Single or Dual Main Board:

[![SparkFun MicroMod Main Board - Double](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/4/2/5/20595-DEV_SparkFun_MicroMod_Main_Board_Double_v22-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-double.html)

### [SparkFun MicroMod Main Board - Double](https://www.sparkfun.com/sparkfun-micromod-main-board-double.html) 

[ DEV-20595 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with up to two...

[ [\$22.95] ]

[![SparkFun MicroMod Main Board - Single](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/7/7/20748-DEV_SparkFun_MicroMod_Main_Board_Single_v21-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html)

### [SparkFun MicroMod Main Board - Single](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html) 

[ DEV-20748 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with a single ...

[ [\$18.50] ]

[![SparkFun Blues Wireless MicroMod Starter Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/5/3/1/21702-_KIT-_01.jpg)](https://www.sparkfun.com/sparkfun-blues-wireless-micromod-starter-kit.html)

### [SparkFun Blues Wireless MicroMod Starter Kit](https://www.sparkfun.com/sparkfun-blues-wireless-micromod-starter-kit.html) 

[ KIT-21702 ]

The SparkFun Blues Wireless MicroMod Starter Kit provides every part needed to get you connected and start prototyping with t...

**Retired**

A Processor Board is needed to act as a host controller for the Function Board:

**Heads Up:** Outboard Device Firmware Updates only support the STM32 Processor v20 as of release. Other Processors may be supported in the future but are beyond the scope of this tutorial. We will update this guide if and when other Processors work with this feature.

[![SparkFun MicroMod STM32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/1/2/2/STM32F405-_01.jpg)](https://www.sparkfun.com/sparkfun-micromod-stm32-processor.html)

### [SparkFun MicroMod STM32 Processor](https://www.sparkfun.com/sparkfun-micromod-stm32-processor.html) 

[ DEV-21326 ]

The SparkFun MicroMod STM32 Processor Board is ready to rock your MicroMod world with its ARM® Cortex®-M4 32-bit RISC core!

[ [\$20.50] ]

[![SparkFun MicroMod Artemis Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/0/16401-SparkFun_MicroMod_Artemis_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html)

### [SparkFun MicroMod Artemis Processor](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html) 

[ DEV-16401 ]

Featuring the Artemis Module, this processor is capable of machine learning, Bluetooth, I2C, GPIO, PWM, SPI & packaged to fit...

[ [\$17.50] ]

You\'ll also need a cellular and GNSS antenna:

[![GPS Embedded Antenna SMA](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/7/00177-01.jpg)](https://www.sparkfun.com/gps-embedded-antenna-sma.html)

### [GPS Embedded Antenna SMA](https://www.sparkfun.com/gps-embedded-antenna-sma.html) 

[ GPS-00177 ]

Embedded antenna for small, mobile applications. Basic unpackaged antenna with LNA. 5inch cable terminated with standard male...

[ [\$18.50] ]

[![Molex Flexible GNSS Antenna - U.FL (Adhesive)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/7/1/1/15246-Molex_GPS_Antenna_-_U.FL__Adhesive_-01a.jpg)](https://www.sparkfun.com/molex-flexible-gnss-antenna-u-fl-adhesive.html)

### [Molex Flexible GNSS Antenna - U.FL (Adhesive)](https://www.sparkfun.com/molex-flexible-gnss-antenna-u-fl-adhesive.html) 

[ GPS-15246 ]

A flexible, paper-thin GNSS Antenna with a U.FL connector and an adhesive backing.

[ [\$6.50] ]

[![PCB Antenna - U.FL (2.4GHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/0/5/18086-2.4GHz_PCB_Antenna_-_U.FL-01.jpg)](https://www.sparkfun.com/pcb-antenna-u-fl-2-4ghz.html)

### [PCB Antenna - U.FL (2.4GHz)](https://www.sparkfun.com/pcb-antenna-u-fl-2-4ghz.html) 

[ WRL-18086 ]

This small form-factor antenna offers a 2.4GHz frequency range.

[ [\$1.95] ]

[![LTE Hinged External Antenna - 698MHz-2.7GHz, SMA Male](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/8/7/16432-698MHz-2.7GHz_LTE_Hinged_External_Antenna__with_SMA_Male_Connector-01.jpg)](https://www.sparkfun.com/lte-hinged-external-antenna-698mhz-2-7ghz-sma-male.html)

### [LTE Hinged External Antenna - 698MHz-2.7GHz, SMA Male](https://www.sparkfun.com/lte-hinged-external-antenna-698mhz-2-7ghz-sma-male.html) 

[ CEL-16432 ]

Molex LTE/5G Cellular External Antennas are designed for 2G/3G/4G/5G modules and devices.

[ [\$12.95] ]

The Notecard Module uses u.Fl connectors for both antenna connections so, depending on your choice of antennas, you may also need an adapter cable like these:

[![SMA to U.FL Cable - 150mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/0/2/9/18568-SMA_to_U.FL_Cable_-_150mm-01.jpg)](https://www.sparkfun.com/sma-to-u-fl-cable-150mm.html)

### [SMA to U.FL Cable - 150mm](https://www.sparkfun.com/sma-to-u-fl-cable-150mm.html) 

[ WRL-18568 ]

This SMA to U.FL Cable is commonly used to connect boards with the compact U.FL connector to an enclosure wall. This allows a...

[ [\$2.75] ]

[![Interface Cable SMA to U.FL - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/2/09145-01b.jpg)](https://www.sparkfun.com/interface-cable-sma-to-u-fl.html)

### [Interface Cable SMA to U.FL - 100mm](https://www.sparkfun.com/interface-cable-sma-to-u-fl.html) 

[ WRL-09145 ]

This is a 4\" connector cable that interfaces U.FL RF connectors to regular SMA connectors. This cable is commonly used to con...

[ [\$5.75] ]

[![Interface Cable U.FL to SMA - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/7/9/18154-Interface_Cable_U.FL_to_SMA-03.jpg)](https://www.sparkfun.com/interface-cable-u-fl-to-sma-100mm.html)

### [Interface Cable U.FL to SMA - 100mm](https://www.sparkfun.com/interface-cable-u-fl-to-sma-100mm.html) 

[ WRL-18154 ]

A U.FL to SMA (jack) bulkhead straight connector with a 1.32 mm diameter cable.

**Retired**

### Suggested Reading

The [MicroMod ecosystem](https://www.sparkfun.com/micromod) is a unique way to allow users to customize their project to their needs. If you aren\'t familiar with the MicroMod system, click on the banner below for more information.

[![MicroMod Logo](https://cdn.sparkfun.com/r/500-70/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)

\

You may also want to go through the tutorials below if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2650&name=Cellular+Function+Board+-+Blues+Wireless+Notecarrier "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2650 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Cellular+Function+Board+-+Blues+Wireless+Notecarrier&url=http%3A%2F%2Fsfe.io%2Ft2650&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2650&t=Cellular+Function+Board+-+Blues+Wireless+Notecarrier "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2650&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F6%2F5%2F0%2FMM_Cellular_FB_-_Blues_Wireless_Single.jpg&description=Cellular+Function+Board+-+Blues+Wireless+Notecarrier "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/hardware-assembly) [Software Setup](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/software-setup) [Arduino Example](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/arduino-example) [Outboard Device Firmware Update](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/outboard-device-firmware-update) [Troubleshooting](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/resources-and-going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/discuss) [Single Page](https://learn.sparkfun.com/tutorials/cellular-function-board---blues-wireless-notecarrier/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Cellular](https://learn.sparkfun.com/tutorials/tags/cellular)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [MicroMod](https://learn.sparkfun.com/tutorials/tags/micromod)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]