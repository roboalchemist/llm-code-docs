# Source: https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SAMD21 Mini/Dev Breakout Hookup Guide

# SAMD21 Mini/Dev Breakout Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft454&name=SAMD21+Mini%2FDev+Breakout+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft454 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SAMD21+Mini%2FDev+Breakout+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft454&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft454&t=SAMD21+Mini%2FDev+Breakout+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft454&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F5%2F4%2Fphoto-hardware-plugin.jpg&description=SAMD21+Mini%2FDev+Breakout+Hookup+Guide "Pin It")

## Introduction

If you\'re ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the ATSAMD21 is an awesome alternative. The ATSAMD21G18 is an ARM Cortex M0+, 32-bit microcontroller that can run at up to 48MHz, and it comes complete with 256KB of flash memory and 32KB of SRAM. Plus, best of all, it\'s **fully supported in the Arduino IDE**!

SparkFun has come up with two new breakout boards for the ATSAMD21G18, both coming in familiar shapes. There\'s the full-size, Arduino-shaped [SAMD21 Dev Breakout](https://www.sparkfun.com/products/13672). And the minuscule, [Pro Mini](https://www.sparkfun.com/products/11114)-shaped [SAMD21 Mini Breakout](https://www.sparkfun.com/products/13664).

[![SparkFun SAMD21 Dev Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/1/1/5/13672-01.jpg)](https://www.sparkfun.com/sparkfun-samd21-dev-breakout.html)

### [SparkFun SAMD21 Dev Breakout](https://www.sparkfun.com/sparkfun-samd21-dev-breakout.html) 

[ DEV-13672 ]

If you're ready to step your Arduino game up from older 8-bit/16MHz microcontrollers, the SparkFun SAMD21 Dev Breakout is a...

[ [\$29.95] ]

[![SparkFun SAMD21 Mini Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/0/9/2/13664-01.jpg)](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html)

### [SparkFun SAMD21 Mini Breakout](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html) 

[ DEV-13664 ]

If you're ready to step your Arduino game up from older 8-bit/16MHz microcontrollers, the SparkFun SAMD21 Mini Breakout is ...

[ [\$24.95] ]

Both boards have similar feature sets \-- they equip the ATSAMD21G18 with a USB interface for programming and power, then surround it with an RTC crystal, 600mA 3.3V regulator, and a variety of other components. The Dev Breakout\'s extra PCB real-estate leaves room for extra GPIO and an integrated LiPo charger.

### Tutorial Scope

This tutorial covers, from the ground up, all things ATSAMD21 and the SparkFun Mini and Dev Breakout boards. It\'s split into a number of pages, including:

- **[SAMD21 Overview](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/samd21-overview)** \-- An introduction to the SAMD21 microprocessor. Highlights of some of the µC\'s most unique features.
- **Board Overviews** \-- An overview of the hardware features of each breakout board:
  - **[SAMD21 Dev Breakout Overview](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/samd21-dev-breakout-overview)**
  - **[SAMD21 Mini Breakout Overview](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/samd21-mini-breakout-overview)**
- **[Hardware Setup](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/hardware-setup)** \-- How to power, assemble the SAMD21 boards. Plus **driver installation** for Windows users!
- **[Setting Up Arduino](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/setting-up-arduino)** \-- How to set up support for the SparkFun SAMD21 boards in the Arduino IDE.
- **Example Sketches** \-- Simple Arduino sketches to help demonstrate some of the unique features of the SAMD21.
  - **[Blink](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/example-blink)** \-- Blinking an LED is the classic starting point for learning how to program embedded electronics. It's the "Hello, World!" of microcontrollers.
  - **[Serial Ports](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/example-serial-ports)** \-- Learn the difference between `Serial`, `Serial1`, and `SerialUSB`.
  - **[Analog Input and Output](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/example-analog-input-and-output)** \-- Plotting the DAC output with an ADC input.
  - **[Real-Time Clock (RTC)](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/example-real-time-clock)** \-- Using the RTC to create a serial-controlled alarm clock.
- **[Troubleshooting](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/troubleshooting)** \-- Tips for working around some of the SAMD21\'s quirks.

### Materials

In addition to either of the SAMD21 Breakout Boards, you\'ll also need a [Micro-B Cable](https://www.sparkfun.com/products/10215) (as if you don\'t already have dozens in your USB cable drawer!). That\'s all you\'ll need to get started. But\...

Eventually you\'ll want to solder something to the board. If you don\'t already have soldering tools, a [soldering iron](https://www.sparkfun.com/products/9507) and some [solder](https://www.sparkfun.com/products/9325) may also come in handy. You can choose your own adventure when it comes to soldering connectors into the boards. Any of these headers (or wire) may come in handy:

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

[![Stackable Header - Female (PTH, 0.1in., 6-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/8/1/09280-1.jpg)](https://www.sparkfun.com/arduino-stackable-header-6-pin.html)

### [Stackable Header - Female (PTH, 0.1in., 6-Pin)](https://www.sparkfun.com/arduino-stackable-header-6-pin.html) 

[ PRT-09280 ]

This is a 6-pin female header, with extra long legs \-- great for stacking Arduino shields. Pins are spaced by 0.1\".

[ [\$0.80] ]

If you have a SAMD21 Dev Board, you can take advantage of its LiPo charger with a [single-cell Lithium Polymer battery](https://www.sparkfun.com/search/results?term=lithium%20polymer), and/or solder a [PTH Barrel Jack](https://www.sparkfun.com/products/119) in to power it with a [5V Wall Adapter](https://www.sparkfun.com/products/12889).

### Suggested Reading

Before continuing on with this tutorial, you may want to familiarize yourself with some of these topics if they're unfamiliar to you:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft454&name=SAMD21+Mini%2FDev+Breakout+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft454 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SAMD21+Mini%2FDev+Breakout+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft454&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft454&t=SAMD21+Mini%2FDev+Breakout+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft454&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F5%2F4%2Fphoto-hardware-plugin.jpg&description=SAMD21+Mini%2FDev+Breakout+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/all) [Next Page →\
[SAMD21 Overview]](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/samd21-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/introduction) [SAMD21 Overview](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/samd21-overview) [SAMD21 Dev Breakout Overview](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/samd21-dev-breakout-overview) [SAMD21 Mini Breakout Overview](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/samd21-mini-breakout-overview) [Hardware Setup](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/hardware-setup) [Drivers (If You Need Them)](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/drivers-if-you-need-them) [Setting Up Arduino](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/setting-up-arduino) [Example: Blink](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/example-blink) [Example: Serial Ports](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/example-serial-ports) [Example: Analog Input and Output](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/example-analog-input-and-output) [Example: Real-Time Clock](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/example-real-time-clock) [Troubleshooting](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/resources--going-further)

[Comments [19]](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Time](https://learn.sparkfun.com/tutorials/tags/time)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]