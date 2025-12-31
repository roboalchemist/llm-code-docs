# Source: https://learn.sparkfun.com/tutorials/microview-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroView Hookup Guide

# MicroView Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1b00b259d107c598ffacb3664a190c26?d=retro&s=20&r=pg) Joel_E_B], [ Marcus Schappi]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft477&name=MicroView+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft477 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroView+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft477&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft477&t=MicroView+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft477&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F7%2F7%2FMicroview_Actions.jpg&description=MicroView+Hookup+Guide "Pin It")

## Introduction

The [SparkFun MicroView](https://www.sparkfun.com/products/12923) is the first chip-size Arduino-compatible module that lets you see what your Arduino is thinking by using a built-in Organic Light-Emitting Diode (OLED) display. In the heart of MicroView, there is an ATMEL ATmega328P and a 64x48 pixel OLED display, together with other passive components that allow the MicroView to operate without any external components other than a power supply. It fits nicely into a breadboard to make prototyping easy. The MicroView also has a full-featured Arduino library to simplify programming the module.

[![SparkFun MicroView - OLED Arduino Module](https://cdn.sparkfun.com/r/600-600/assets/parts/9/8/4/5/12923-01.jpg)](https://www.sparkfun.com/sparkfun-microview-oled-arduino-module.html)

### [SparkFun MicroView - OLED Arduino Module](https://www.sparkfun.com/sparkfun-microview-oled-arduino-module.html) 

[ DEV-12923 ]

The MicroView is the first chip-sized Arduino compatible module that lets you see what your Arduino is thinking using a built...

[ [\$47.95] ]

This guide will cover everything you need to know about the MicroView, including hardware information, quick-start experiments, library installation and usage, and advanced information such as making your own MicroView font.

### Required Materials

The MicroView is a stand-alone system. However, you will need an external programmer to upload new code to the MicroView. The [MicroView USB programmer](https://www.sparkfun.com/products/12924) is sold separately, so you can purchase one programmer while purchasing as many MicroView modules as you need. If you do not have one already, you will need a MicroView USB programmer to follow along with this tutorial.

[![SparkFun MicroView - USB Programmer](https://cdn.sparkfun.com/r/600-600/assets/parts/9/8/4/6/12924-01.jpg)](https://www.sparkfun.com/sparkfun-microview-usb-programmer.html)

### [SparkFun MicroView - USB Programmer](https://www.sparkfun.com/sparkfun-microview-usb-programmer.html) 

[ DEV-12924 ]

The MicroView is the first chip-sized Arduino compatible module that lets you see what your Arduino is thinking using a built...

[ [\$19.50] ]

In addition to the MicroView and the USB programmer, you will need a few basic electronic components. Here is a complete list of the parts used in this tutorial.

Note that the USB extension cord is not necessary; the MicroView USB programmer can plug directly into a USB port. However, your USB port may be difficult to access, may be too tightly spaced for the programmer, or may result in the MicroView appearing upside down to you. In these instances, the USB extension cable comes in very handy. We carry both a [1.5-foot version](https://www.sparkfun.com/products/13309) and a [6-foot version](https://www.sparkfun.com/products/517).

### Suggested Reading

If you have never worked with the Arduino development environment before or need a refresher, you may find the following links useful.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft477&name=MicroView+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft477 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroView+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft477&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft477&t=MicroView+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft477&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F7%2F7%2FMicroview_Actions.jpg&description=MicroView+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/microview-hookup-guide/all) [Next Page →\
[MicroView Overview]](https://learn.sparkfun.com/tutorials/microview-hookup-guide/microview-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/microview-hookup-guide/introduction) [MicroView Overview](https://learn.sparkfun.com/tutorials/microview-hookup-guide/microview-overview) [Quick Start Tutorials](https://learn.sparkfun.com/tutorials/microview-hookup-guide/quick-start-tutorials) [MicroView Library Installation](https://learn.sparkfun.com/tutorials/microview-hookup-guide/microview-library-installation) [Example 1 - Hello, World!](https://learn.sparkfun.com/tutorials/microview-hookup-guide/example-1---hello-world-) [Example 2 - Basic Drawing](https://learn.sparkfun.com/tutorials/microview-hookup-guide/-example-2---basic-drawing-) [Example 3 - Widgets](https://learn.sparkfun.com/tutorials/microview-hookup-guide/example-3---widgets-) [Example 4 - Drawing Bitmaps](https://learn.sparkfun.com/tutorials/microview-hookup-guide/example-4---drawing-bitmaps) [OLED Memory Map](https://learn.sparkfun.com/tutorials/microview-hookup-guide/oled-memory-map) [Creating Fonts for MicroView](https://learn.sparkfun.com/tutorials/microview-hookup-guide/creating-fonts-for-microview) [MicroView Class Reference](https://learn.sparkfun.com/tutorials/microview-hookup-guide/microview-class-reference) [Resources and Going Further](https://learn.sparkfun.com/tutorials/microview-hookup-guide/res)

[Comments [10]](https://learn.sparkfun.com/tutorials/microview-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/microview-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Displays](https://learn.sparkfun.com/tutorials/tags/displays)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [MicroView](https://learn.sparkfun.com/tutorials/tags/microview)
  - [OLED](https://learn.sparkfun.com/tutorials/tags/oled)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]