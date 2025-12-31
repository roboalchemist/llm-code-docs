# Source: https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SAMD51 Thing Plus Hookup Guide

# SAMD51 Thing Plus Hookup Guide

[≡ Pages](#)

Contributors: [ santaimpersonator], [![](https://cdn.sparkfun.com/avatar/fde91fc929973498fdcfcfc9ccb086ab?d=retro&s=20&r=pg) Englandsaurus]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft888&name=SAMD51+Thing+Plus+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft888 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SAMD51+Thing+Plus+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft888&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft888&t=SAMD51+Thing+Plus+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft888&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F8%2F8%2FHeaders_Stackable.JPG&description=SAMD51+Thing+Plus+Hookup+Guide "Pin It")

## Introduction

SparkFun is proud to welcome the [SAMD51 Thing Plus](https://www.sparkfun.com/products/14713) to our microcontroller lineup! With a 32-bit ARM Cortex-M4F MCU, it is one of our most powerful microcontroller boards yet.

[![SparkFun Thing Plus - SAMD51](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/9/2/7/14713-SparkFun_Thing_Plus_-_SAMD51-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html)

### [SparkFun Thing Plus - SAMD51](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html) 

[ DEV-14713 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun SAMD51 Thing Plus is one of our most powerful microcontroller boards yet!

[ [\$25.50] ]

The ATSAMD51J20 microcontroller boasts a maximum CPU speed of 120MHz, 1MB of flash memory, 256KB of SRAM, up to 6 SERCOM interfaces, amongst other features (*see [datasheet](https://cdn.sparkfun.com/assets/0/0/5/9/2/60001507C.pdf)*). The [SAMD51 Thing Plus](https://www.sparkfun.com/products/14713) provides a USB interface for programming and power, a Qwiic connector, 600mA 3.3V regulator, and LiPo charger all in a feather pin layout. For a full list of details, check out the [**Hardware Overview**](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/hardware-overview) section below. In addition, this board comes flashed with the same convenient, UF2 bootloader as the [RedBoard Turbo](https://www.sparkfun.com/products/14812).

This tutorial aims to familiarize you with the new SAMD51 Thing Plus and help you get started using it. If you are new to the world of Arduino or microcontrollers, please check out our [RedBoard Qwiic](https://www.sparkfun.com/products/15123) and [RedBoard Qwiic Hookup Guide](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide).

### Required Materials

To get started, all you need is a few things:

- [SAMD51 Thing Plus](https://www.sparkfun.com/products/14713) - You\'ll definitely need this; otherwise, you are probably on the wrong tutorial page (*wink*).
- [USB micro-B Cable - 6 Foot](https://www.sparkfun.com/products/10215) - The USB interface serves two purposes: it powers the board and allows you to upload programs to it. (*You might even have a few of these in you drawer!*)
- Computer with the **Arduino IDE** installed on it - That is how we will program the board and interface with it.

<!-- -->

- ::: 
  **Troubleshooting Tip:** If you are not a technical or computer savy individual and you have your choice of computers, a [**Windows 10**] computer is highly recommended. You will usually run into the least issues, if any, with this operating systems.
  :::

That is ALL\... pretty simple right? Now you won\'t be able to do much since there are no additional sensors to interact with the physical world. However, you can at least blink an LED and do some math calculations.

[**Jumper Modification**](#Jumper_Materials) [**Headers & Accessories**](#Headers) [**ARM Programmers**](#Programmers)

***Click the buttons** above to toggle the **additional materials** based on the tasks you\
wish to perform. Feel free to modify the items in your cart to fit your needs.*

\

#### Jumper Modification

If you would like to modify the 3.3V/5V I/O jumper or A4/A5 Qwiic connector jumpers, you will need [soldering equipment](https://www.sparkfun.com/categories/49) and/or a [knife](https://www.sparkfun.com/categories/379).

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

#### ARM Programmers

If you would like to debug or flash your ARM processor on your own, here are some of our [ARM Programmers](https://www.sparkfun.com/categories/26):

[![Segger J-Link EDU Mini](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/4/0/2/24078-J-Link-Mini-Feature.jpg)](https://www.sparkfun.com/segger-j-link-edu-mini.html)

### [Segger J-Link EDU Mini](https://www.sparkfun.com/segger-j-link-edu-mini.html) 

[ PGM-24078 ]

The J-Link EDU Mini is a stripped-down, budget-friendly model of the J-Link debug probe created for educational use.

[ [\$60.00] ]

### Suggested Reading

Before continuing on with this tutorial, you may want to familiarize yourself with some of these topics if they're unfamiliar to you:

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/adding-more-sercom-ports-for-samd-boards)

### Adding More SERCOM Ports for SAMD Boards 

How to setup extra SPI, UART, and I2C serial ports on a SAMD-based boards.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/arm-programming)

### ARM Programming 

How to program SAMD21 or SAMD51 boards (or other ARM processors).

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

One of the new, advanced features of the board is that it takes advantage of the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials (above) before using it, as all **Qwiic** sensors utilize an **I^2^C** communication protocol. Click on the banner above to learn more about [Qwiic products](https://www.sparkfun.com/categories/399).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft888&name=SAMD51+Thing+Plus+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft888 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SAMD51+Thing+Plus+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft888&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft888&t=SAMD51+Thing+Plus+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft888&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F8%2F8%2FHeaders_Stackable.JPG&description=SAMD51+Thing+Plus+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/all) [Next Page →\
[UF2 Bootloader & Drivers]](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/uf2-bootloader--drivers)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/introduction-) [UF2 Bootloader & Drivers](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/uf2-bootloader--drivers) [Setting Up the Arduino IDE](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/setting-up-the-arduino-ide) [Hardware Overview](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/hardware-assembly) [Arduino Examples](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/arduino-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/resources-and-going-further)

[Comments [5]](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/samd51-thing-plus-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Prototyping](https://learn.sparkfun.com/tutorials/tags/prototyping)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Thing Plus](https://learn.sparkfun.com/tutorials/tags/thing-plus)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]