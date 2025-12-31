# Source: https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroMod STM32WB5MMG Hookup Guide

# MicroMod STM32WB5MMG Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft3144&name=MicroMod+STM32WB5MMG+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft3144 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+STM32WB5MMG+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft3144&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft3144&t=MicroMod+STM32WB5MMG+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft3144&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F1%2F4%2F4%2FMM_STM32WB-Thumbnail.jpg&description=MicroMod+STM32WB5MMG+Hookup+Guide "Pin It")

## Introduction

The MicroMod STM32WB5MMG Processor expands on SparkFun\'s MicroMod ST product line with a powerful combination of computing and wireless capabilities all on one Processor. The STM32WB5MMG from STMicroelectronics^™^ is an ultra-low power microcontroller that combines a pair of Arm^®^ Cortex^®^ processors; a Cortex-M4 processor for primary computing and a Cortex-M0 to run the 2.4 GHz radio. The radio is Bluetooth^®^ Low Energy 5.3, Zigbee^®^ 3.0, and OpenThread certified.

[![SparkFun MicroMod STM32WB5MMG Processor](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/2/6/8/21438-_DEV_MM_STM32WB-_01.jpg)](https://www.sparkfun.com/sparkfun-micromod-stm32wb5mmg-processor.html)

### [SparkFun MicroMod STM32WB5MMG Processor](https://www.sparkfun.com/sparkfun-micromod-stm32wb5mmg-processor.html) 

[ DEV-21438 ]

The MicroMod STM32WB5MMG Processor has a powerful combination of computing and wireless capabilities all on one Processor.

[ [\$19.95] ]

The STM32WB5MMG Processor boasts a host of interface and peripheral options including SPI, multiple UARTs, I^2^C buses, as well as I2S. This guide covers the hardware present on this MicroMod Processor, how to assemble it into a MicroMod circuit, and how to install and use the board in the Arduino IDE.

### Required Materials

You\'ll need a Carrier Board or Main Board to plug the Processor into. Below are a few options for both types of boards:

[![SparkFun MicroMod ATP Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/1/2/16885-SparkFun_MicroMod_ATP_Carrier_Board-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html)

### [SparkFun MicroMod ATP Carrier Board](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html) 

[ DEV-16885 ]

If you need a \"lot\" of GPIO with a simple to program, ready to go to market module, the ATP is the fix you need.

[ [\$20.50] ]

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

[![SparkFun MicroMod Qwiic Carrier Board - Single](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/3/4/17723-SparkFun_MicroMod_Qwiic_Carrier_Board_-_Single-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-qwiic-carrier-board-single.html)

### [SparkFun MicroMod Qwiic Carrier Board - Single](https://www.sparkfun.com/sparkfun-micromod-qwiic-carrier-board-single.html) 

[ DEV-17723 ]

The Single MicroMod Qwiic Carrier Board can be used to rapidly prototype with other Qwiic devices.

[ [\$11.50] ]

**Note:** Users who wish to take full advantage of all of the STM32WB5MMG\'s interfaces (I2S, QSPI, etc.) should use the ATP Carrier Board to access all the pins on this Processor though QSPI and I2S are *not* supported in the Arduino IDE. We recommend using the [STMCube IDE](https://www.st.com/en/development-tools/stm32cubeide.html) to use these interfaces.

You\'ll also need a USB-C cable to connect the Carrier Board to your computer and if you want to add some Qwiic breakouts to your MicroMod project you\'ll want at least one Qwiic cable to connect it all together. Below are some options for both of those cables:

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Flexible Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/6/17259-Flexible_Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-100mm.html)

### [Flexible Qwiic Cable - 100mm](https://www.sparkfun.com/flexible-qwiic-cable-100mm.html) 

[ PRT-17259 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

[![Reversible USB A to C Cable - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/3/15424-Reversible_USB_A_to_C_Cable_-_2m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html)

### [Reversible USB A to C Cable - 2m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html) 

[ CAB-15424 ]

These 2m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the U...

[ [\$10.50] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

### Suggested Reading

The SparkFun MicroMod ecosystem offers a unique way to allow users to customize their project to their needs. Do you want to send your weather data via a wireless signal (e.g. Bluetooth or WiFi)? There\'s a MicroMod Processor Board for that. Looking to instead maximize efficiency and processing power? You guessed it, there\'s a MicroMod Processor Board for that. If you are not familiar with the MicroMod ecosystem, take a look here:

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/micromod).

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend reading through the following tutorials if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/bluetooth-basics)

### Bluetooth Basics 

An overview of the Bluetooth wireless technology.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft3144&name=MicroMod+STM32WB5MMG+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft3144 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+STM32WB5MMG+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft3144&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft3144&t=MicroMod+STM32WB5MMG+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft3144&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F1%2F4%2F4%2FMM_STM32WB-Thumbnail.jpg&description=MicroMod+STM32WB5MMG+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/hardware-assembly) [Software Setup](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/software-setup) [Arduino Example - Blink](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/arduino-example---blink) [Resources and Going Further](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/resources-and-going-further)

[Comments [1]](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/micromod-stm32wb5mmg-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Bluetooth](https://learn.sparkfun.com/tutorials/tags/bluetooth)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [MicroMod](https://learn.sparkfun.com/tutorials/tags/micromod)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]