# Source: https://learn.sparkfun.com/tutorials/red-v-redboard-hookup-guide

## Introduction

SparkFun is pleased to welcome a whole new instruction set architecture (ISA) to its family, the RISC-V ISA (*pronounced "risk-five"*), and along with it, introduce the [RED-V RedBoard](https://www.sparkfun.com/products/15594) (*pronounced "red-five"*). In this tutorial, we\'ll be focusing on the hardware.

[![SparkFun RED-V RedBoard - SiFive RISC-V FE310 SoC](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/2/0/0/15594-SparkFun_RED-V_RedBoard_-_SiFive_RISC-V_FE310_SoC-01.jpg)](https://www.sparkfun.com/sparkfun-red-v-redboard-sifive-risc-v-fe310-soc.html)

### [SparkFun RED-V RedBoard - SiFive RISC-V FE310 SoC](https://www.sparkfun.com/sparkfun-red-v-redboard-sifive-risc-v-fe310-soc.html) 

[ DEV-15594 ]

The RED-V RedBoard from SparkFun is a low-cost, Arduino-compatible development board featuring the Freedom E310 which brings ...

**Retired**

*\"The force is strong with this one.\" (Star Wars: A New Hope, 1977)*

What sets the [RISC-V](https://en.wikipedia.org/wiki/RISC-V) ISA from the rest is that it is completely open-source; including the [instruction set architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture) (ISA). That means anyone can make full use the microcontroller without requiring royalties, licenses, or non-disclosure agreements (NDAs). The RED-V comes in the familiar Arduino Uno form factor and includes the SiFive Freedom E310 core, 32MB of QSPI flash, an NXP K22 ARM Cortex-M4 for USB connectivity and operating as a JTAG interface, and a Qwiic connector.

### Required Materials

To follow along with this tutorial, you will need the following materials and software. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. Here is what you would need to get started:

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![SparkFun RED-V RedBoard - SiFive RISC-V FE310 SoC](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/0/0/15594-SparkFun_RED-V_RedBoard_-_SiFive_RISC-V_FE310_SoC-01.jpg)](https://www.sparkfun.com/sparkfun-red-v-redboard-sifive-risc-v-fe310-soc.html)

### [SparkFun RED-V RedBoard - SiFive RISC-V FE310 SoC](https://www.sparkfun.com/sparkfun-red-v-redboard-sifive-risc-v-fe310-soc.html) 

[ DEV-15594 ]

The RED-V RedBoard from SparkFun is a low-cost, Arduino-compatible development board featuring the Freedom E310 which brings ...

**Retired**

- [RED-V](https://www.sparkfun.com/products/15594) - You\'ll definitely need this; otherwise, you are probably on the wrong tutorial page (*wink*).
- [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/products/14743) - The USB interface serves two purposes: it powers the board and allows you to upload programs to it. (*You might even have a few of these in you drawer!*)

#### You Will Also Need

To utilize all the features of the development board, you may need the following tools and accessories. If you would like to modify the jumpers on the board, you will need [soldering equipment](https://www.sparkfun.com/categories/49).

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

#### Segger Programmers

If you would like to debug or flash your processor on your own, here are some of our [SEGGER Programmers](https://www.sparkfun.com/categories/tags/segger). We also recommend getting the 1.27mm header pins with some jumper wires to connect. Depending on the programmer that you use, you may need to use a combination of wire wrap and IC hooks to connect.

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

Before continuing on with this tutorial, you may want to familiarize yourself with some of these topics if they're unfamiliar to you.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

## Hardware Overview

### Power & Programming

There are a few different ways to power the SparkFun RED-V RedBoard:

- USB-C
- barrel jack connector
- power pins broken out on the edge of the board

The easiest way (which will also allow you to program your board) is to simply plug it into your computer via USB-C. This will provide 5V to the board and will also allow you access to the super cool USB-to-JTAG interface for programming. Once you\'ve programmed your RED-V however, you may want to have it running off of a different power supply. If you use a wall wart on the USB-C connector, make sure it outputs a regulated **5V DC**. You can also use the black barrel jack, in which case you\'ll need any wall adapter between **7 & 15 Volts DC**. Or you can also power the board through the header pins broken out on the edge of the board. If you are using `VIN` and `GND`, follow the same practice as using a wall adapter and stick to between 7 & 15 Volts. If you are using `5V` and `GND` or `3v3` and `GND`, make sure that your voltage is regulated when applying power to the 5V or 3.3V pins, respectively.

[![USB, Barrel Jack, and Power Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310_SoC_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310_SoC_Power.jpg)

#### Always-On Core

The FE310 contains an Always-On (AON) block that allows easy power control of the FE310. It includes its own real-time clock and is also attached to the [WAKE] button on the board. This allows you to put the FE310 to sleep and wake it up upon a time-generated or user-generated interrupt.

[![FE310 IC](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310.jpg)

### Buttons

The RED-V has two buttons: a `RESET` button and a `WAKE` button. The `RESET` button is pretty self explanatory and is used to reset the FE310. A single tap of the `RESET` button will run the code loaded onto the FE310\'s QSPI flash. A quick double tap will put the FE310 into safe bootloader mode, which will allow you to flash new code to the RED-V if you\'ve managed to really mess things up (i.e. Oops I put the core to sleep and forgot to add a way to wake it up). The pin is also broken out on the edge of the board. Adding a jumper wire from this pin to GND will reset the board as well.

[![Reset Button and Pin](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310_Reset.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310_Reset.jpg)

The RED-V is also equipped with an Always-On or AON core (mentioned above) which can be programmed to shut down the main core of the FE310 and wake it up upon a button-generated or user-generated interrupt. The `WAKE` button can be configured in software to wake the FE310 from deep sleep. This button is also broken out to the header pin nearest the barrel jack if you\'d like to use an external source to wake the FE310. Adding a jumper wire from this pin to GND will wake the board as well.

[![Wake Button and Pin](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310_Wake.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310_Wake.jpg)

### Jumpers

The FE310 has a few jumpers as well, all of which are open by default. The two jumpers located next to the `I2C` label is for the I^2^C pull-up resistors. These resistors are not attached by default as there are I^2^C pull-up resistors on all SparkFun Qwiic slaves. If you\'re using a 3^rd^ party board, you may need to [close these jumper by the Qwiic connector](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces#adding-a-solder-jumper) to attach the pull-ups to the I^2^C bus. The jumper by the USB-C connector is for bypassing the 0.5A PTC fuse. This is for special cases where you need a lot current. Most of the time, you can leave this jumper open.

[![Pull-Up Resistors and By-Pass jumper](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_SiFive_RISC-V_FE310_Jumpers.jpg)

### Dimensions

The RED-V RedBoard uses the Arduino Uno footprint. There are four mounting holes on the board.

[![Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/3/2/SparkFun_RED-V__RedBoard_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/SparkFun_RED-V__RedBoard_Dimensions.png)

## Hardware Hookup

For the scope of the tutorial, you\'ll use a USB C cable to power, upload code, and send serial to the board. Simply connect the computer\'s USB port and the RED-V. The board uses standard Arduino Uno R3 footprint with female headers to stack Arduino shields and easily connect prototyped circuits on breadboards with jumper wires.

[![USB Cable to RED-V](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/3/2/RED-V_RedBoard_cable.jpg)

**Note:** While the board uses the standard Arduino Uno R3 footprint, keep in mind the board uses [3.3V logic levels](https://learn.sparkfun.com/tutorials/logic-levels/all). Additionally, Arduino shields might have been only developed for an AVR architecture and the Arduino programming language. You may need to put in a little bit more effort to write a library in order to get it working depending on the FE310 and your preferred programming language.

## Software Development Guide

There are a few environments to get started with the RED-V. For information about programming the RED-V RedBoard, check out the following tutorial.

[](https://learn.sparkfun.com/tutorials/red-v-development-guide)

### RED-V Development Guide 

November 27, 2019

This guide will help you get the RED-V RedBoard or Thing Plus up and running for the exhaust port. Depending on personal preference, there are a few environments to get started with the boards. All wings report in\... we\'re going in full-throttle.