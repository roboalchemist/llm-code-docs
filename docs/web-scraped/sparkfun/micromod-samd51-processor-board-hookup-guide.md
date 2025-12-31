# Source: https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroMod SAMD51 Processor Board Hookup Guide

# MicroMod SAMD51 Processor Board Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/814545d7cad2a95dda668529c61c99d0?d=retro&s=20&r=pg) bboyho], [![](https://cdn.sparkfun.com/avatar/5c320824995fcd6990beaf7a3d3f6037?d=retro&s=20&r=pg) Elias The Sparkiest]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1207&name=MicroMod+SAMD51+Processor+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1207 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+SAMD51+Processor+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1207&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1207&t=MicroMod+SAMD51+Processor+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1207&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F0%2F7%2F16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg&description=MicroMod+SAMD51+Processor+Board+Hookup+Guide "Pin It")

## Introduction

With the MicroMod specification, we shrunk down the PCB size for the SAMD51 32-bit ARM Cortex-M4F MCU! This tutorial covers the basic functionality of the [MicroMod SAMD51](https://www.sparkfun.com/products/16791) and highlights its features.

[![SparkFun MicroMod SAMD51 Processor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/6/9/8/16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html)

### [SparkFun MicroMod SAMD51 Processor](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html) 

[ DEV-16791 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun MicroMod SAMD51 Processor Board is one powerful microcontroller packaged on a ...

[ [\$18.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![SparkFun MicroMod ATP Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/1/2/16885-SparkFun_MicroMod_ATP_Carrier_Board-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html)

### [SparkFun MicroMod ATP Carrier Board](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html) 

[ DEV-16885 ]

If you need a \"lot\" of GPIO with a simple to program, ready to go to market module, the ATP is the fix you need.

[ [\$20.50] ]

[![SparkFun MicroMod SAMD51 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/8/16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html)

### [SparkFun MicroMod SAMD51 Processor](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html) 

[ DEV-16791 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun MicroMod SAMD51 Processor Board is one powerful microcontroller packaged on a ...

[ [\$18.95] ]

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

### Suggested Reading

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/micromod).

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you aren't familiar with the following concepts, we also recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1207&name=MicroMod+SAMD51+Processor+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1207 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+SAMD51+Processor+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1207&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1207&t=MicroMod+SAMD51+Processor+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1207&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F0%2F7%2F16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg&description=MicroMod+SAMD51+Processor+Board+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/hardware-assembly) [UF2 Bootloader & Drivers](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/uf2-bootloader--drivers) [Setting Up the Arduino IDE](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/setting-up-the-arduino-ide) [Arduino Examples](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/arduino-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/resources-and-going-further)

[Comments [4]](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]