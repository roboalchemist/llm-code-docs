# Source: https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- IOIO-OTG Hookup Guide

# IOIO-OTG Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1b00b259d107c598ffacb3664a190c26?d=retro&s=20&r=pg) Joel_E_B], [ Ytai]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft487&name=IOIO-OTG+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft487 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=IOIO-OTG+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft487&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft487&t=IOIO-OTG+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft487&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F8%2F7%2FIOIO_Hookup_Guide-03.jpg&description=IOIO-OTG+Hookup+Guide "Pin It")

## Introduction

The [IOIO-OTG](https://www.sparkfun.com/products/13613) (pronounced "yo-yo-O-T-G\"; the OTG stands for [On-The-Go](https://en.wikipedia.org/wiki/USB_On-The-Go)) is a development board specially designed to allow developers to add advanced hardware I/O capabilities to their Android or PC application. It features a PIC microcontroller, which acts like a bridge that connects an app on your PC or Android device to low-level peripherals like GPIO, PWM, ADC, I^2^C, SPI and UART. An app-level library helps you write control code for these low level peripherals in the same way you'd write any other Java app!

[![IOIO-OTG - v2.2](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/9/8/3/13613-01.jpg)](https://www.sparkfun.com/ioio-otg-v2-2.html)

### [IOIO-OTG - v2.2](https://www.sparkfun.com/ioio-otg-v2-2.html) 

[ DEV-13613 ]

The IOIO-OTG is a PIC development board specially designed to add advanced hardware I/O capabilities to your Android or PC ap...

[ [\$49.95] ]

What separates the IOIO-OTG from previous IOIO boards is its ability to leverage the USB On-The-Go specification to connect as a host *or* an accessory. There are several ways to connect the IOIO to your Java app. If the app is running on your Android device, the IOIO-OTG will act as a USB host and supply charging current to your device (meaning the IOIO-OTG will need its own power source). If your app is running on a Windows, Linux or OSX machine, the IOIO-OTG will assume device mode and present itself as a virtual serial port. When in device mode, the IOIO-OTG can be powered by the host. Connecting a USB Bluetooth^®^ dongle will cause the IOIO-OTG to show up as a Bluetooth serial connection, so you can go wireless!

### Required Materials

A [USB Female A to Micro A OTG Cable](https://www.sparkfun.com/products/11604) should have been included with the purchase of your IOIO-OTG.

In addition to the IOIO and this cable you will need these items to follow along with this tutorial.

### Suggested Reading

While not covered in this tutorial directly, the IOIO-OTG is capable of the functions mentioned below. Should you find any of them unfamiliar, take a detour over to that tutorial, then head on back here when finished.

The [IOIO Wiki](https://github.com/ytai/ioio/wiki) is full of great information that is helpful when read beforehand.

You should have a good understanding of using the [Command Line](http://cli.learncodethehardway.org/book/) before getting started with the IOIO-OTG.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft487&name=IOIO-OTG+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft487 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=IOIO-OTG+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft487&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft487&t=IOIO-OTG+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft487&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F8%2F7%2FIOIO_Hookup_Guide-03.jpg&description=IOIO-OTG+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/all) [Next Page →\
[IOIO Board Overview]](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/ioio-board-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/introduction-) [IOIO Board Overview](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/ioio-board-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/hardware-assembly) [Software Downloads and Installation](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/software-downloads-and-installation-) [Running Your First PC App](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/running-your-first-pc-app) [Building Your First PC App](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/building-your-first-pc-app) [Running Your First Android App](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/running-your-first-android-app) [Building Your First Android App](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/building-your-first-android-app) [IOIO Bridge for Development](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/ioio-bridge-for-development-) [Going Wireless with Bluetooth](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/going-wireless-with-bluetooth-) [Troubleshooting](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/res)

[Comments [2]](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/ioio-otg-hookup-guide/all) [Print]

- **Tags**
- - [Bluetooth](https://learn.sparkfun.com/tutorials/tags/bluetooth)
  - [Computer Engineering](https://learn.sparkfun.com/tutorials/tags/computer-engineering-)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]