# Source: https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroMod Update Tool Hookup Guide

# MicroMod Update Tool Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino], [![](https://cdn.sparkfun.com/avatar/ea6398c8ad1d378f523ba26e9c5169ac?d=retro&s=20&r=pg) PaulZC]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1662&name=MicroMod+Update+Tool+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1662 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+Update+Tool+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1662&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1662&t=MicroMod+Update+Tool+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1662&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F6%2F6%2F2%2FMicroMod_Update_Tool-Thumbnail.jpg&description=MicroMod+Update+Tool+Hookup+Guide "Pin It")

## Introduction

Introducing the [SparkFun MicroMod Update Tool](https://www.sparkfun.com/products/17725)! This simple little board allows you to interact directly with the SARA-R5 LTE-M / NB-IoT module on the [MicroMod Asset Tracker Carrier Board](https://www.sparkfun.com/products/17272) via the module\'s UART.

[![SparkFun MicroMod Update Tool](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/8/3/6/17725-SparkFun_MicroMod_Update_Tool-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-update-tool.html)

### [SparkFun MicroMod Update Tool](https://www.sparkfun.com/sparkfun-micromod-update-tool.html) 

[ DEV-17725 ]

The Update Tool also makes it simple to communicate directly with the SARA using u-blox's sophisticated m-center cellular e...

[ [\$5.95] ]

The MicroMod Asset Tracker Carrier Board provides you with a toolkit to monitor and track the location of your assets. Do you want to know where your assets are at all times? Or maybe you just want an update if an asset is moved? If so, this is the product for you!

Built around the u-blox SARA-R510M8S module, the asset tracker offers Secure Cloud LTE-M and NB-IoT data communication for multi-regional use and has an integrated u-blox M8 GNSS receiver for accurate positioning information. The SARA-R5 supports many different forms of data communication from full TCP/IP sockets and packet switched data, through HTTP Get/Put/Post, FTP (the SARA has a built-in file system), Ping, to good old SMS text messaging!

The Update Tool is not a full MicroMod Processor Board, it is much simpler than that. It has a CH340C USB-Serial converter on it which gives you full access to all eight pins of the SARA-R5\'s UART interface via the Asset Tracker's USB-C connector. Think of it as a bridge from USB to serial.

Why is this a good idea? Well, for a start - as the name suggests - it is an ideal way to upgrade the SARA-R5's firmware should you need to. The Update Tool also makes it simple to communicate directly with the SARA using u-blox's sophisticated m-center cellular evaluation software. If you're familiar with u-center, u-blox's GNSS evaluation software, you'll know how excellent their software is. m-center is every bit as good.

The Update Tool features eight pairs of Plated Through Hole connections for the UART signals. You can use these to connect directly to the SARA UART using **3.3V** signals if you want to. The split pads on the rear of the Tool can be opened to isolate the CH340C completely; the pins nearest the M.2 will link straight to the SARA UART.

### Required Materials

In order to follow along with this tutorial, you\'ll want to have the following items.

The Asset Tracker Firmware Update Tool, as the name suggests, is designed to work with the MicroMod Asset Tracker Carrier Board. The Update Tool along with a [Hologram eUICC SIM Card](https://www.sparkfun.com/products/17117) are included with the Asset Tracker:

[![SparkFun MicroMod Asset Tracker Carrier Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/2/7/9/17272-SparkFun_MicroMod_Asset_Tracker_Carrier_Board-06a.jpg)](https://www.sparkfun.com/sparkfun-micromod-asset-tracker-carrier-board.html)

### [SparkFun MicroMod Asset Tracker Carrier Board](https://www.sparkfun.com/sparkfun-micromod-asset-tracker-carrier-board.html) 

[ DEV-17272 ]

The MicroMod Asset Tracker Carrier Board provides you with a toolkit to monitor and track the location of your assets

[ [\$154.50] ]

You\'ll also need a USB-C cable to connect the Carrier to your computer. Below are some options for USB cables:

[![Reversible USB A to C Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/4/15425-Reversible_USB_A_to_C_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html)

### [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html) 

[ CAB-15425 ]

These 0.8m cables have minor modifications that allow them to be plugged into their ports regardless of orientation on the US...

[ [\$6.50] ]

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

### Optional Extras

If you want to manipulate the UART connections on the Update Tool we recommend soldering a set of headers to your board. Below are a few options:

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Straight Header - Male (PTH, 0.1in., 2x8-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/6/1/7/13156-01.jpg)](https://www.sparkfun.com/header-2x8-male-0-1.html)

### [Straight Header - Male (PTH, 0.1in., 2x8-Pin)](https://www.sparkfun.com/header-2x8-male-0-1.html) 

[ PRT-13156 ]

This is a simple 2x8 male PTH header. This header is that you will find commonly used to interface with a basic 8x2 character...

[\$0.95] [ [\$0.24] ]

If you wish to use the Update Tool to interact directly with the SARA-R5 module on your Asset Tracker and do not have these items already, you may also need LTE and GNSS antennas:

[![GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/1/15192-GNSS_Multi-band_Magnetic_Mount_Antenna_SMA_-_5m-01.jpg)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html)

### [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html) 

[ GPS-15192 ]

The ANN-MB-00 GNSS multi-band antenna is extremely unique from other GNSS/GPS antennas in that it is designed to receive both...

[ [\$109.95] ]

[![LTE Hinged External Antenna - 698MHz-2.7GHz, SMA Male](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/8/7/16432-698MHz-2.7GHz_LTE_Hinged_External_Antenna__with_SMA_Male_Connector-01.jpg)](https://www.sparkfun.com/lte-hinged-external-antenna-698mhz-2-7ghz-sma-male.html)

### [LTE Hinged External Antenna - 698MHz-2.7GHz, SMA Male](https://www.sparkfun.com/lte-hinged-external-antenna-698mhz-2-7ghz-sma-male.html) 

[ CEL-16432 ]

Molex LTE/5G Cellular External Antennas are designed for 2G/3G/4G/5G modules and devices.

[ [\$12.95] ]

### Suggested Reading

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading here for an overview:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend reading through the following tutorials if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1662&name=MicroMod+Update+Tool+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1662 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+Update+Tool+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1662&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1662&t=MicroMod+Update+Tool+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1662&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F6%2F6%2F2%2FMicroMod_Update_Tool-Thumbnail.jpg&description=MicroMod+Update+Tool+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/hardware-assembly) [Software Setup](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/software-setup) [Using the PTH Connections](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/using-the-pth-connections) [Troubleshooting](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/micromod-update-tool-hookup-guide/all) [Print]

- **Tags**
- - [Cellular](https://learn.sparkfun.com/tutorials/tags/cellular)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [MicroMod](https://learn.sparkfun.com/tutorials/tags/micromod)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]