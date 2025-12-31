# Source: https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- RP2040 Thing Plus Hookup Guide

# RP2040 Thing Plus Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3f2ffc88a128ff5f69a13c855d407dab?d=retro&s=20&r=pg) Nick Poole], [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1527&name=RP2040+Thing+Plus+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1527 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=RP2040+Thing+Plus+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1527&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1527&t=RP2040+Thing+Plus+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1527&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F5%2F2%2F7%2Fdemo_double_oled_small.jpg&description=RP2040+Thing+Plus+Hookup+Guide "Pin It")

## Introduction

Introducing the [SparkFun Thing Plus - RP2040](https://www.sparkfun.com/products/17745), featuring the RP2040 microcontroller (MCU) on a Feather (Thing Plus) form-factor. Additionally, this development platform also provides an SD card slot, 16MB (128Mbit) flash memory, a JST single cell battery connector (with a charging circuit and attached fuel gauge sensor), a WS2812 RGB LED, JTAG (PTH) pins, and our signature Qwiic connector.

[![SparkFun Thing Plus - RP2040](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/8/7/0/17745-SparkFun_Thing_Plus_-_RP2040-01a.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-rp2040.html)

### [SparkFun Thing Plus - RP2040](https://www.sparkfun.com/sparkfun-thing-plus-rp2040.html) 

[ DEV-17745 ]

The SparkFun Thing Plus - RP2040 is a low-cost, high performance board with flexible digital interfaces featuring the Raspber...

[ [\$19.95] ]

The [Raspberry Pi RP2040](https://datasheets.raspberrypi.org/rp2040/rp2040_datasheet.pdf) *(the first MCU from the [Raspberry Pi Foundation](https://www.raspberrypi.org/))* is a low cost, dual-core Arm^®^ Cortex^®^ M0+ microcontroller with 264kB of SRAM, running at 133MHz. It includes USB host functionality, a timer with 4 alarms, a real time counter (RTC), six dedicated IO pins for Quad-SPI flash (supporting execute in place), and thirty multifunction GPIO (*\*18 of which are broken out on the board*), with the following capabilities:

- Four 12-bit Analogue to Digital Converter (ADC) channels
- Two UART buses
- Two I^2^C buses
- Two SPI buses
- Up to 16 PWM channels
- Can emulate interfaces such as SD Card and VGA

### Required Materials

To get started, users will need a few items. Now some users may have a few of these items, feel free to modify your cart accordingly.

- [SparkFun Thing Plus - RP2040](https://www.sparkfun.com/products/17745)
- [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/products/14743) - The USB interface serves two purposes: it powers the board and allows you to upload programs to it. (*\*If your computer doesn\'t provide a USB-A slot, then you will need to choose an appropriate cable or purchase an adapter as well.*)
- Computer with an operating system (OS) that is compatible with all the software installation requirements:
  - Windows 10
  - Mac OSX
  - Raspberry Pi OS

[![SparkFun Thing Plus - RP2040](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/7/0/17745-SparkFun_Thing_Plus_-_RP2040-01a.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-rp2040.html)

### [SparkFun Thing Plus - RP2040](https://www.sparkfun.com/sparkfun-thing-plus-rp2040.html) 

[ DEV-17745 ]

The SparkFun Thing Plus - RP2040 is a low-cost, high performance board with flexible digital interfaces featuring the Raspber...

[ [\$19.95] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[**Batteries**](#LiPo) [**Jumper Modification**](#Jumper_Materials) [**Headers & Accessories**](#Headers)

***Click the buttons** above to toggle the **additional materials** based on the tasks you\
wish to perform. Feel free to modify the items in your cart to fit your needs.*

\

#### Li-Po Battery

For mobile applications, users will want to pick up a [single-cell LiPo battery](https://www.sparkfun.com/categories/54) from our catalog. Below, are a few available options:

[![Lithium Ion Battery - 110mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/0/13853-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-110mah.html)

### [Lithium Ion Battery - 110mAh](https://www.sparkfun.com/lithium-ion-battery-110mah.html) 

[ PRT-13853 ]

This is a very small, extremely light weight battery based on Lithium Ion chemistry. This is the highest energy density curre...

[ [\$7.53] ]

[![Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/8/13857-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-400mah.html)

### [Lithium Ion Battery - 400mAh](https://www.sparkfun.com/lithium-ion-battery-400mah.html) 

[ PRT-13851 ]

This is a very small, extremely lightweight battery based on Lithium Ion chemistry, with the highest energy density currently...

[ [\$7.98] ]

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

\

#### Jumper Modification

To modify the jumpers, users will need [soldering equipment](https://www.sparkfun.com/categories/49) and/or a [knife](https://www.sparkfun.com/categories/379).

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

[Headers](https://www.sparkfun.com/categories/381) are great for development purposes, letting users swap parts with just a set of jumper wires. If you would like to add headers to your board, check out some of the options for the Thing Plus or Feather form factor boards:

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

[![Straight Header - Female (PTH, 0.1in., 8-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/9/8/11895-01.jpg)](https://www.sparkfun.com/header-8-pin-female-pth-0-1.html)

### [Straight Header - Female (PTH, 0.1in., 8-Pin)](https://www.sparkfun.com/header-8-pin-female-pth-0-1.html) 

[ PRT-11895 ]

These are standard 0.1\" spaced header pins that can be through-hole mounted. This header connects perfectly with most 8-pin m...

[ [\$0.80] ]

[![Straight Header - Female (PTH, 0.1in., 12-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/0/3/14321-02.jpg)](https://www.sparkfun.com/photon-header-12-pin-female.html)

### [Straight Header - Female (PTH, 0.1in., 12-Pin)](https://www.sparkfun.com/photon-header-12-pin-female.html) 

[ PRT-14321 ]

These standard female headers add a great deal of connectivity to your next project where you need 12-pins in a line. Each or...

[ [\$0.80] ]

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

#### JTAG Functionality

Users interested in JTAG applications *(i.e. programming and debugging the RP2040)* will need an [Arm^®^ Programmer](https://www.sparkfun.com/categories/26) and need to solder on a [JTAG header](https://www.sparkfun.com/products/15362). We recommend these programmers from our catalog:

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

Here are a few tutorials that may help users familiarize themselves with various aspects of the board.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

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

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

One of the new, convenient features of the board is that it takes advantage of the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials. Click on the banner above to learn more about [Qwiic products](https://www.sparkfun.com/qwiic).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1527&name=RP2040+Thing+Plus+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1527 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=RP2040+Thing+Plus+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1527&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1527&t=RP2040+Thing+Plus+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1527&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F5%2F2%2F7%2Fdemo_double_oled_small.jpg&description=RP2040+Thing+Plus+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/all) [Next Page →\
[UF2 Bootloader]](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/uf2-bootloader)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/introduction) [UF2 Bootloader](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/uf2-bootloader) [Hardware Overview](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/hardware-overview) [Software Overview](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/software-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/hardware-assembly) [MicroPython Examples](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/micropython-examples) [Resources and Going Further](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/resources-and-going-further)

[Comments [10]](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/rp2040-thing-plus-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Computer Engineering](https://learn.sparkfun.com/tutorials/tags/computer-engineering-)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [LEDs](https://learn.sparkfun.com/tutorials/tags/leds)
  - [micropython](https://learn.sparkfun.com/tutorials/tags/micropython)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Thing Plus](https://learn.sparkfun.com/tutorials/tags/thing-plus)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]