# Source: https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- ESP32-S2 Thing Plus Hookup Guide

# ESP32-S2 Thing Plus Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete], [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1660&name=ESP32-S2+Thing+Plus+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1660 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=ESP32-S2+Thing+Plus+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1660&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1660&t=ESP32-S2+Thing+Plus+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1660&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F6%2F6%2F0%2Fthumbnail.jpg&description=ESP32-S2+Thing+Plus+Hookup+Guide "Pin It")

## Introduction

The [ESP32-S2 Thing Plus](https://www.sparkfun.com/products/17743) is a feather form-factor development board with the improved ESP32-S2 module, from [Espressif](https://www.espressif.com/). The new ESP32-S2 module addresses the [security flaws](https://www.espressif.com/en/news/ESP32_FIA_Analysis) in the original ESP32. While the ESP32-S2 does include improved security features, it lacks the Bluetooth capabilities of the original ESP32 module.

[![SparkFun Thing Plus - ESP32-S2 WROOM](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/8/6/2/17743-SparkFun_Thing_Plus_-_ESP32-S2_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html)

### [SparkFun Thing Plus - ESP32-S2 WROOM](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html) 

[ WRL-17743 ]

The SparkFun ESP32-S2 WROOM Thing Plus is a highly-integrated, Feather form-factor development board equipped with the 2.4 GH...

[ [\$24.50] ]

**Not Yet Implemented**: The Arduino core for the ESP32 microcontroller are still a work in progress. There are a handful of [peripherals and features](https://docs.espressif.com/projects/arduino-esp32/en/latest/libraries.html) that have yet to be implemented, including:

- ~~PWM/~~Analog Ouptut (`analogWrite([pin], [value])`)
  - Alternative: [LED Control API](https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/api/ledc.html)
- Pulse Counter
- SDIO
- ~~Timer/Real-Time Clock~~
  - Alternative: [Timer API](https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/api/timer.html)
  - Alternative: [ESP32Time Arduino library](https://github.com/fbiego/ESP32Time)
- TWAI

The peripherals are available (if, also, still in their infancy) in the [IoT Development Framework](https://github.com/espressif/esp-idf) for the ESP32. If your application requires any of the features above, consider giving the [ESP-IDF](https://github.com/espressif/esp-idf) a try! *(Updated: June 2022.)*

### Required Materials

To get started, users will need a few items. Now some users may have a few of these items, feel free to modify your cart accordingly.

- [ESP32-S2 Thing Plus](https://www.sparkfun.com/products/17743)
- [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/products/14743) - The USB interface serves two purposes: it powers the board and allows you to upload programs to it. (*\*If your computer doesn\'t provide a USB-A slot, then you will need to choose an appropriate cable or purchase an adapter as well.*)
- Computer with the an operating system (OS) that is compatible with all the software installation requirements.

[![SparkFun Thing Plus - ESP32-S2 WROOM](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/6/2/17743-SparkFun_Thing_Plus_-_ESP32-S2_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html)

### [SparkFun Thing Plus - ESP32-S2 WROOM](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html) 

[ WRL-17743 ]

The SparkFun ESP32-S2 WROOM Thing Plus is a highly-integrated, Feather form-factor development board equipped with the 2.4 GH...

[ [\$24.50] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[**Headers**](#Headers) [**Batteries**](#LiPo) [**Jumper Modification**](#Jumper_Materials) [**JTAG Functionality**](#JTAG)

***Click the buttons** above to toggle the **additional materials** based on the options you\
wish to use. Feel free to modify the items in your cart to fit your needs.*

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

#### Headers & Accessories

[Headers](https://www.sparkfun.com/categories/381) are great for development purposes, letting users swap parts with just a set of jumper wires. If you would like to add headers to your board, check out some of the options for the Thing Plus or Feather form factor boards below. For a full selection of our available [**Headers**](https://www.sparkfun.com/categories/381) or [**Soldering Tools**](https://www.sparkfun.com/categories/49), click on the associated links.

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

New to soldering? Check out our [Through-Hole Soldering Tutorial](https://learn.sparkfun.com/tutorials/5) for a quick introduction!

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

April 2, 2018

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

\

#### JTAG Functionality

Users interested in JTAG applications *(i.e. programming and debugging the ESP32)* will need an [JTAG Programmer](https://www.sparkfun.com/categories/26) and need to solder on a [JTAG header](https://www.sparkfun.com/products/15362). We recommend these programmers from our catalog:

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

[ ![JTAG 20 Pin 0.1 In. To 10 Pin 0.05 In. Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/8/3/5/18421-JTAG_20_Pin_0.1_In._To_10_Pin_0.05_In._Adapter.jpeg) ]

### JTAG 20 Pin 0.1 In. To 10 Pin 0.05 In. Adapter 

[ PGM-18421 ]

The adapter works fine with Segger\'s JLINK and other JTAG/SWD programmers/debuggers.

**Retired**

### Suggested Reading

As a more professionally oriented product, we will skip over the more fundamental tutorials (i.e. [**Ohm\'s Law**](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) and [**What is Electricity?**](https://learn.sparkfun.com/tutorials/what-is-electricity)). However, below are a few tutorials that may help users familiarize themselves with various aspects of the board.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

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

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide)

### ESP32 Thing Plus Hookup Guide 

Hookup guide for the ESP32 Thing Plus (Micro-B) using the ESP32 WROOM\'s WiFi/Bluetooth system-on-chip in Arduino.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

One of the new, advanced features of the board is that it takes advantage of the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials. Click on the banner above to learn more about [Qwiic products](https://www.sparkfun.com/qwiic).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1660&name=ESP32-S2+Thing+Plus+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1660 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=ESP32-S2+Thing+Plus+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1660&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1660&t=ESP32-S2+Thing+Plus+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1660&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F6%2F6%2F0%2Fthumbnail.jpg&description=ESP32-S2+Thing+Plus+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/hardware-overview) [Software Overview](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/software-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/hardware-assembly) [Arduino Examples](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/arduino-examples) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/resources-and-going-further)

[Comments [8]](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/esp32-s2-thing-plus-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [ESP32](https://learn.sparkfun.com/tutorials/tags/esp32)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Thing Plus](https://learn.sparkfun.com/tutorials/tags/thing-plus)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]