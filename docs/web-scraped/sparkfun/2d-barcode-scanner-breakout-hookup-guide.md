# Source: https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- 2D Barcode Scanner Breakout Hookup Guide

# 2D Barcode Scanner Breakout Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino], [ MAKIN-STUFF]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1599&name=2D+Barcode+Scanner+Breakout+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1599 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=2D+Barcode+Scanner+Breakout+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1599&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1599&t=2D+Barcode+Scanner+Breakout+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1599&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F5%2F9%2F9%2F2D_Barcode_Scanner_Breakout-Thumb.jpg&description=2D+Barcode+Scanner+Breakout+Hookup+Guide "Pin It")

## Introduction

The [SparkFun 2D Barcode Scanner Breakout](https://www.sparkfun.com/products/18088) is a nifty little breakout board featuring the DE2120 barcode scanner module from DYScan. The DE2120 reads 20 different barcode symbologies (both 1D and 2D) using a camera coupled with on-board image processing to identify and decode everything from UPC codes to QR codes. The module also features two LEDs: one for illumination and one to project the red line for \"aiming\" that you\'re used to seeing from laser-based scanners.

[![SparkFun 2D Barcode Scanner Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/4/0/7/18088-SparkFun_2D_Barcode_Scanner-06.jpg)](https://www.sparkfun.com/sparkfun-2d-barcode-scanner-breakout.html)

### [SparkFun 2D Barcode Scanner Breakout](https://www.sparkfun.com/sparkfun-2d-barcode-scanner-breakout.html) 

[ SEN-18088 ]

This tiny \"scan engine\" will read 20 different barcode symbologies --- both 1D and 2D!

[ [\$66.95] ]

The breakout makes it easy to use the scanner module by connecting the scanner\'s USB serial output to a USB-C connector. The breakout also includes a standard 0.1\"-spaced PTH header for the power, serial UART, trigger and status output connections. On top of that, we\'ve added a trigger button, buzzer and status LED connected to the appropriate drive circuits to easily initialize scans and receive feedback from scanning barcodes.

### Required Materials

You\'ll need a few things along with the 2D Barcode Scanner Breakout to follow this tutorial. You may not need everything though depending on what you have already so add anything you need from the items below to your cart.

The 2D Barcode Scanner Breakout can work as a USB device connected to a computer (PC or Single-Board like the Pi) with a USB Type-C cable.

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

If you want to use the 2D Barcode Scanner Breakout with a Pi, the options below can get you started:

[![Raspberry Pi 4 Model B (8 GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/2/5/16811-Raspberry_Pi_4_Model_B__8_GB_-01.jpg)](https://www.sparkfun.com/raspberry-pi-4-model-b-8-gb.html)

### [Raspberry Pi 4 Model B (8 GB)](https://www.sparkfun.com/raspberry-pi-4-model-b-8-gb.html) 

[ DEV-16811 ]

The 8GB Raspberry Pi 4 features the ability to run two 4k resolution monitors, to run true Gigabit Ethernet operations, all a...

[ [\$119.95] ]

[![Raspberry Pi 4 Model B (2 GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/2/1/15446-Raspberry_Pi_4_Model_B__2_GB_-01.jpg)](https://www.sparkfun.com/raspberry-pi-4-model-b-2-gb.html)

### [Raspberry Pi 4 Model B (2 GB)](https://www.sparkfun.com/raspberry-pi-4-model-b-2-gb.html) 

[ DEV-15446 ]

The 2 GB Raspberry Pi 4 features the ability to run two 4k resolution monitors, to run true Gigabit Ethernet operations, all ...

[ [\$69.75] ]

[![SparkFun Raspberry Pi 4 Basic Kit - 8GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/1/5/0/17980-SparkFun_Raspberry_Pi_4_Basic_Kit_-_8GB-01.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-basic-kit-8gb.html)

### [SparkFun Raspberry Pi 4 Basic Kit - 8GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-basic-kit-8gb.html) 

[ KIT-17980 ]

The Raspberry Pi 4 Basic Kit includes everything you\'ll need to get up and running with the new Raspberry Pi 4 8GB.

[ [\$123.50] ]

[![Raspberry Pi 3 B+](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/2/8/14643-Raspberry_Pi_3_B_-02.jpg)](https://www.sparkfun.com/raspberry-pi-3-b.html)

### [Raspberry Pi 3 B+](https://www.sparkfun.com/raspberry-pi-3-b.html) 

[ DEV-14643 ]

The Raspberry Pi 3 B+ is here to provide you with the same Pi as before, but now with gigabit and PoE capable Ethernet!

[ [\$43.50] ]

The breakout can also communicate with a microcontroller like an Arduino through the serial UART pins and other dedicated pins on the breakout\'s PTH header.

[![SparkFun Qwiic Pro Micro - USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/0/4/15795-Pro_Micro_C-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html)

### [SparkFun Qwiic Pro Micro - USB-C](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html) 

[ DEV-15795 ]

The SparkFun Qwiic Pro Micro adds a reset button, Qwiic connector, USB-C, and castellated pads to the miniaturized Arduino bo...

[ [\$23.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

Using the breakout\'s PTH header requires some assembly and soldering. You may already have a few of these items but if not, the tools and hardware below will help with that assembly:

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

### Recommended Reading

We would also recommend taking a look at the following tutorials if you aren\'t familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1599&name=2D+Barcode+Scanner+Breakout+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1599 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=2D+Barcode+Scanner+Breakout+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1599&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1599&t=2D+Barcode+Scanner+Breakout+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1599&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F5%2F9%2F9%2F2D_Barcode_Scanner_Breakout-Thumb.jpg&description=2D+Barcode+Scanner+Breakout+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/hardware-assembly) [DE2120 Arduino Library](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/de2120-arduino-library) [Arduino Examples](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/arduino-examples) [DE2120 Python Package](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/de2120-python-package) [Python Examples](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/python-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/tr) [Resources and Going Further](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/resources--going-further)

[Comments [3]](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/2d-barcode-scanner-breakout-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Communication](https://learn.sparkfun.com/tutorials/tags/communication)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]