# Source: https://learn.sparkfun.com/tutorials/red-v-thing-plus-hookup-guide

## Introduction

SparkFun is pleased to welcome its a whole new instruction set architecture (ISA) to its family, the RISC-V ISA (*pronounced "risk-five"*), and along with it, introduce the [RED-V Thing Plus](https://www.sparkfun.com/products/15594) (*pronounced "red-five"*). In this tutorial, we\'ll be focusing on the hardware.

[![SparkFun RED-V Thing Plus - SiFive RISC-V FE310 SoC](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/4/0/8/15799-SparkFun_RED-V_Thing_Plus_-_SiFive_RISC-V_FE310_SoC-01.jpg)](https://www.sparkfun.com/sparkfun-red-v-thing-plus-sifive-risc-v-fe310-soc.html)

### [SparkFun RED-V Thing Plus - SiFive RISC-V FE310 SoC](https://www.sparkfun.com/sparkfun-red-v-thing-plus-sifive-risc-v-fe310-soc.html) 

[ DEV-15799 ]

The RED-V Thing Plus from SparkFun is a low-cost, Arduino-compatible development board featuring the Freedom E310 which bring...

**Retired**

*\"The force is strong with this one.\" (Star Wars: A New Hope, 1977)*

What sets the [RISC-V](https://en.wikipedia.org/wiki/RISC-V) ISA from the rest is that it is completely open-source; including the [instruction set architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture) (ISA). That means anyone can make full use the microcontroller without requiring royalties, licenses, or non-disclosure agreements (NDAs). The RED-V comes in the familiar SparkFun Thing Plus form factor and includes the SiFive Freedom E310 core, 32MB of QSPI flash, an NXP K22 ARM Cortex-M4 for USB connectivity and operating as a JTAG interface, and a Qwiic connector.

### Required Materials

To follow along with this tutorial, you will need the following materials and software. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. Here is what you would need to get started:

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![SparkFun RED-V Thing Plus - SiFive RISC-V FE310 SoC](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/0/8/15799-SparkFun_RED-V_Thing_Plus_-_SiFive_RISC-V_FE310_SoC-01.jpg)](https://www.sparkfun.com/sparkfun-red-v-thing-plus-sifive-risc-v-fe310-soc.html)

### [SparkFun RED-V Thing Plus - SiFive RISC-V FE310 SoC](https://www.sparkfun.com/sparkfun-red-v-thing-plus-sifive-risc-v-fe310-soc.html) 

[ DEV-15799 ]

The RED-V Thing Plus from SparkFun is a low-cost, Arduino-compatible development board featuring the Freedom E310 which bring...

**Retired**

- [RED-V Thing Plus](https://www.sparkfun.com/products/15799) - You\'ll definitely need this; otherwise, you are probably on the wrong tutorial page (*wink*).
- [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/products/14743) - The USB interface serves two purposes: it powers the board and allows you to upload programs to it. (*You might even have a few of these in you drawer!*)

#### You Will Also Need

To utilize all the features of the development board, you may need the following tools and accessories.

[**Jumper Modification**](#Jumper_Materials) [**Headers & Accessories**](#Headers)

***Click the buttons** above to toggle the **additional materials** based on the tasks you\
wish to perform. Feel free to modify the items in your cart to fit your needs.*

\

#### Jumper Modification

If you would like to modify the jumpers on the board, you will need [soldering equipment](https://www.sparkfun.com/categories/49).

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

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

\

#### Qwiic Example

If you would like to follow along with the examples below to interact with the physical world, you will also need the following items:

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![SparkFun Qwiic 12 Bit ADC - 4 Channel (ADS1015)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/5/7/15334-SparkFun_Qwiic_12_Bit_ADC_-_4_Channel__ADS1015_-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-12-bit-adc-4-channel-ads1015.html)

### [SparkFun Qwiic 12 Bit ADC - 4 Channel (ADS1015)](https://www.sparkfun.com/sparkfun-qwiic-12-bit-adc-4-channel-ads1015.html) 

[ DEV-15334 ]

The SparkFun Qwiic 12 Bit ADC can provide four channels of I^2^C controlled ADC input to your Qwiic enabled project.

[ [\$9.95] ]

[![Magnetic Screwdriver Set (20 Piece)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/1/6/15003-Magnetic_Screwdriver_Set__24_Piece_-04.jpg)](https://www.sparkfun.com/products/15003)

### [Magnetic Screwdriver Set (20 Piece)](https://www.sparkfun.com/products/15003) 

[ TOL-15003 ]

This is a 20 piece screwdriver set that magnetically keeps each of the unused bits secured inside of a thin case that easily ...

**Retired**

\

#### Headers & Accessories

If you would like to add headers to your board, check out some of the following items:

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Feather Stackable Header Set](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/0/4/15187-Feather_Stackable_Header_Kit-01.jpg)](https://www.sparkfun.com/feather-stackable-header-kit.html)

### [Feather Stackable Header Set](https://www.sparkfun.com/feather-stackable-header-kit.html) 

[ PRT-15187 ]

These stackable headers are made to work with the \[SparkFun ESP32 Thing Plus\](https://www.sparkfun.com/products/14689) to con...

[ [\$2.25] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

Below is a sample selection of our other headers and soldering tools in our catalog. For a full selection of our available [**Headers**](https://www.sparkfun.com/categories/381) or [**Soldering Tools**](https://www.sparkfun.com/categories/49), click on the associated link.

[![Extended GPIO Header - Female (PTH, 0.1in., 2x20-Pin, 13.5mm/9.80mm)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/5/3/16764-2_X_20_Pin_Extended_GPIO_Header_-_Female_-_13.5mm_9.80mm-01.jpg)](https://www.sparkfun.com/extended-gpio-female-header-2x20-pin-13-5mm-9-80mm.html)

### [Extended GPIO Header - Female (PTH, 0.1in., 2x20-Pin, 13.5mm/9.80mm)](https://www.sparkfun.com/extended-gpio-female-header-2x20-pin-13-5mm-9-80mm.html) 

[ PRT-16764 ]

This 2x20 pin female header is meant to allow you to extend the reach of any board with the standard 2x20 GPIO pin footprint.

[ [\$3.25] ]

[![Socket, 24 pins, 0.1 inch (2.54 mm) Spacing](https://cdn.sparkfun.com/r/140-140/assets/parts/3/0/0/9/9/socket_24x1_28386.jpg)](https://www.sparkfun.com/socket-24-pins-0-1-inch-2-54-mm-spacing.html)

### [Socket, 24 pins, 0.1 inch (2.54 mm) Spacing](https://www.sparkfun.com/socket-24-pins-0-1-inch-2-54-mm-spacing.html) 

[ PRT-28386 ]

Single row of 24-holes, female header with standard 0.1\" (2.54mm) spacing.

[ [\$1.85] ]

[![Insulated GPIO Header - Female (PTH, 0.1in., 2x20-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/2/14017-07.jpg)](https://www.sparkfun.com/raspberry-pi-gpio-tall-header-2x20.html)

### [Insulated GPIO Header - Female (PTH, 0.1in., 2x20-Pin)](https://www.sparkfun.com/raspberry-pi-gpio-tall-header-2x20.html) 

[ PRT-14017 ]

This 2x20 \"tall\" header has the same number and spacing of pins as a Raspberry Pi and provides your board with the ability to...

[ [\$3.50] ]

[![GPIO Header - Male (PTH, 0.1in., 2x20-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/3/0/14275-01.jpg)](https://www.sparkfun.com/raspberry-pi-gpio-male-header-2x20.html)

### [GPIO Header - Male (PTH, 0.1in., 2x20-Pin)](https://www.sparkfun.com/raspberry-pi-gpio-male-header-2x20.html) 

[ PRT-14275 ]

This 2x20 male header has the same number and spacing of pins as a Raspberry Pi but is best served when used in conjunction w...

[ [\$1.10] ]

[![PINECIL - Smart Mini Portable Soldering Iron](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/2/7/0/23913-Pinecil-Smart-Mini-Portable-Soldering-Feature3.jpg)](https://www.sparkfun.com/pinecil-smart-mini-portable-soldering-iron.html)

### [PINECIL - Smart Mini Portable Soldering Iron](https://www.sparkfun.com/pinecil-smart-mini-portable-soldering-iron.html) 

[ TOL-23913 ]

The Pinecil is a smart mini portable soldering iron with a 32-bit RISC-V SoC.

[ [\$68.50] ]

[![PINECIL Soldering Iron Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/8/5/KIT-24063-PINECIL-Soldering-Iron-Kit-Feature.jpg)](https://www.sparkfun.com/pinecil-soldering-iron-kit.html)

### [PINECIL Soldering Iron Kit](https://www.sparkfun.com/pinecil-soldering-iron-kit.html) 

[ KIT-24063 ]

The PINECIL Soldering Iron Kit provides a compact powerhouse and everything you need to ignite your DIY dream.

[ [\$119.95] ]

[![Insulated Silicone Soldering Mat](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/7/0/14672-Insulated_Silicone_Soldering_Mat-01.jpg)](https://www.sparkfun.com/insulated-silicone-soldering-mat.html)

### [Insulated Silicone Soldering Mat](https://www.sparkfun.com/insulated-silicone-soldering-mat.html) 

[ TOL-14672 ]

With this Insulated Silicone Soldering Mat you will be provided with the means to protect your desktop, soldering station, or...

[ [\$15.95] ]

[![Soldering Stand with Brass Sponge](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/8/3/TOL-24061-Soldering-Stand-with-Brass-Sponge-Feature.jpg)](https://www.sparkfun.com/soldering-stand-with-brass-sponge.html)

### [Soldering Stand with Brass Sponge](https://www.sparkfun.com/soldering-stand-with-brass-sponge.html) 

[ TOL-24061 ]

A simple metal soldering iron stand with a brass tip cleaner.

[ [\$13.95] ]

\

#### Segger Programmers

If you would like to debug or flash your processor on your own, here are some of our [SEGGER Programmers](https://www.sparkfun.com/categories/tags/segger). Depending on the programmer that you use, you may need to use a combination of wire wrap and IC hooks to connect.

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

Before continuing on with this tutorial, you may want to familiarize yourself with some of these topics if they're unfamiliar to you.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

## Hardware Overview

### Power & Programming

There are a few different ways to power the SparkFun RED-V Thing Plus:

- USB-C
- JST connector (battery power)
- power pins broken out on the edge of the board

The easiest way (which will also allow you to program your board) is to simply plug it into your computer via USB-C. This will provide 5V to the board and will also allow you access to the super cool USB-to-JTAG interface for programming. Once you\'ve programmed your RED-V however, you may want to have it running off of a different power supply. If you use a wall wart on the USB-C connector, make sure it outputs a regulated **5V DC**. You can also use the black JST connector to provide battery power from a LiPo battery. There is an on-board LiPo charger with the **current rate set to 500mA**. Make sure to use LiPo batteries that have a capacity greater than 500mAh when charging. If you decide to power the board via the `VUSB` or `VBAT` pins, make sure to not exceed *6.5V* since this is the absolute maximum for the 3.3V voltage regulator. Or you can power the board through the breakout pins on the edge of the board. If you are using `3V3` and `GND`, make sure that your voltage is regulated when applying power to the pin.

[![USB, JST, and Power Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus_-_SiFive_RISC-V_FE310_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus_-_SiFive_RISC-V_FE310_Power.jpg)

#### Always-On Core

The FE310 contains an Always-On (AON) block that allows easy power control of the FE310. It includes its own real-time clock and is also attached to the [WAKE] button on the board. This allows you to put the FE310 to sleep and wake it up upon a time-generated or user-generated interrupt.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/FE310_IC__2_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/FE310_IC__2_.jpg)

### Buttons

The RED-V has two buttons: a `RESET` button and a `WAKE` button. The `RESET` button is pretty self explanatory and is used to reset the FE310. A single tap of the `RESET` button will run the code loaded onto the FE310\'s QSPI flash. A quick double tap will put the FE310 into safe bootloader mode, which will allow you to flash new code to the RED-V if you\'ve managed to really mess things up (i.e. Oops I put the core to sleep and forgot to add a way to wake it up). The pin is also broken out on the edge of the board. Adding a jumper wire from this pin to GND will reset the board as well.

[![Reset Button and Pin](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus_Reset.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus_Reset.jpg)

The RED-V is also equipped with an Always-On or AON core (mentioned above) which can be programmed to shut down the main core of the FE310 and wake it up upon a button-generated or user-generated interrupt. The `WAKE` button can be configured in software to wake the FE310 from deep sleep.

[![Wake Button](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus-Wake.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus-Wake.jpg)

### Jumpers

The FE310 has a few jumpers as well, all of which are open by default. The two jumpers located next to the `I2C` label is for the I^2^C pull-up resistors. These resistors are not attached by default as there are I^2^C pull-up resistors on all SparkFun Qwiic slaves. If you\'re using a 3^rd^ party board, you may need to [close these jumper by the Qwiic connector](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces#adding-a-solder-jumper) to attach the pull-ups to the I^2^C bus. The jumper by the USB-C connector (next to the Segger logo) is for bypassing the 0.5A PTC fuse. This is for special cases where you need a lot current. If you need to connect the NC pin to GND, you can also add a solder jumper on the pads as well. Most of the time, you can leave the bypass and NC jumpers open.

[![Pull-Up Resistors and By-Pass jumper](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus_SiFive_RISC-V_FE310_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus_SiFive_RISC-V_FE310_Jumpers.jpg)

### Dimensions

The RED-V Thing Plus measures at 2.3\"x0.90\".

[![Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/SparkFun_RED-V_Thing_Plus_Dimensions.png)

## Hardware Hookup

For the scope of the tutorial, you\'ll use a USB C cable to power, upload code, and send serial to the board. Simply connect the computer\'s USB port and the RED-V Thing Plus. The board uses standard Thing Plus footprint.

[![RED-V Thing Plus Connected to USB C Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/9/9/RED-V_Thing_Plus_Cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/9/9/RED-V_Thing_Plus_Cable.jpg)

**Note:** While the board uses the standard Thing Plus footprint, keep in mind the board uses [3.3V logic levels](https://learn.sparkfun.com/tutorials/logic-levels/all). Additionally, Thing Plus shields might have been only developed for a certain architecture and programming language. You may need to put in a little bit more effort to write a library in order to get it working depending on the FE310 and your preferred programming language.

The headers were left off the board to allow users the flexibility of connecting any type of 0.1\" header to the board. For temporary connections to the I/O pins, you could use IC hooks to test out the pins. However, you\'ll need to [solder headers or wires of your choice to the board](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) for a secure connection. Here are a few tutorials to connect to the PTH pads depending on your personal preference.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

February 8, 2013

How to strip, crimp, and work with wire.

## Software Development Guide

There are a few environments to get started with the RED-V. For information about programming the RED-V Thing Plus, check out the following tutorial.

[](https://learn.sparkfun.com/tutorials/red-v-development-guide)

### RED-V Development Guide 

November 27, 2019

This guide will help you get the RED-V RedBoard or Thing Plus up and running for the exhaust port. Depending on personal preference, there are a few environments to get started with the boards. All wings report in\... we\'re going in full-throttle.