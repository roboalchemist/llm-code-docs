# Source: https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroMod Asset Tracker Carrier Board Hookup Guide

# MicroMod Asset Tracker Carrier Board Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino], [![](https://cdn.sparkfun.com/avatar/ea6398c8ad1d378f523ba26e9c5169ac?d=retro&s=20&r=pg) PaulZC]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1663&name=MicroMod+Asset+Tracker+Carrier+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1663 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+Asset+Tracker+Carrier+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1663&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1663&t=MicroMod+Asset+Tracker+Carrier+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1663&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F6%2F6%2F3%2FMicroMod_Asset_Tracker-Thumbnail.jpg&description=MicroMod+Asset+Tracker+Carrier+Board+Hookup+Guide "Pin It")

## Introduction

The [MicroMod Asset Tracker Carrier Board](https://www.sparkfun.com/products/17272) provides you with a toolkit to monitor and track the location of your assets. Do you want to know where your assets are at all times? Or maybe you just want an update if an asset is moved? If so, this is the product for you!

[![SparkFun MicroMod Asset Tracker Carrier Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/2/7/9/17272-SparkFun_MicroMod_Asset_Tracker_Carrier_Board-06a.jpg)](https://www.sparkfun.com/sparkfun-micromod-asset-tracker-carrier-board.html)

### [SparkFun MicroMod Asset Tracker Carrier Board](https://www.sparkfun.com/sparkfun-micromod-asset-tracker-carrier-board.html) 

[ DEV-17272 ]

The MicroMod Asset Tracker Carrier Board provides you with a toolkit to monitor and track the location of your assets

[ [\$154.50] ]

Built around the u-blox SARA-R510M8S module, the MicroMod Asset Tracker Carrier Board offers Secure Cloud LTE-M data communication for multi-regional use and has an integrated u-blox M8 GNSS receiver for accurate positioning information.

Want to be able to communicate directly with the SARA-R5 over USB-C, without needing a Processor Board? Or, want to upgrade the SARA firmware? The included [Asset Tracker Update Tool](https://www.sparkfun.com/products/17725) lets you do just that. The Asset Tracker requires a Nano SIM for LTE-M connectivity. You can use the included [Hologram eUICC SIM card](https://www.sparkfun.com/products/17117) or choose one from your preferred service provider if you prefer.

The Asset Tracker will work with any of our MicroMod Processor Boards, but because the asset tracker offers so many features and can be configured in different ways, some processor boards may be a better choice for your application than others. Please see "Choosing a Processor Board" below for more details.

The SARA-R5 supports many different forms of data communication from full TCP/IP sockets and packet switched data, through HTTP Get/Put/Post, FTP (the SARA has a built-in file system), Ping, to good old SMS text messaging!

The Asset Tracker has an integrated ICM-20948 Inertial Measurement Unit for 9-Degree Of Freedom orientation and movement detection. Want to send a message if your asset is moved? The asset tracker can do that! It also has a built-in digital microphone and so can send an alert as soon as a noise is detected too. Want to add a light sensor? The Qwiic connector will let you do that.

Want to use the Asset Tracker to log data during a journey or shipping? It has a built-in micro-SD card socket for data logging. Power options include both USB-C and LiPo battery (with built-in charging and battery fuel gauge), but you can provide power via a breakout pin too.

We've provided a full [set of examples](https://github.com/sparkfun/MicroMod_Asset_Tracker/tree/main/Examples) to get you up and running quickly and our [SARA-R5 Arduino Library](https://github.com/sparkfun/SparkFun_u-blox_SARA-R5_Arduino_Library) does all of the heavy lifting for you.

### Required Materials

In addition to the MicroMod Asset Tracker Carrier Board, you'll need a processor board to get started. Depending on which features of the SARA-R5 you want to use, some of our processor boards may be a better choice for your application. Please see "Choosing a Processor Board" below for more details.

[![SparkFun MicroMod ESP32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/8/0/16781-SparkFun_MicroMod_ESP32_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html)

### [SparkFun MicroMod ESP32 Processor](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html) 

[ WRL-16781 ]

This board combines Espressif\'s ESP32 with our M.2 connector interface to bring a power-packed processor board into our Micro...

[ [\$19.95] ]

[![SparkFun MicroMod nRF52840 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/9/2/1/16984-SparkFun_MicroMod_nRF52840_Processor-04.jpg)](https://www.sparkfun.com/sparkfun-micromod-nrf52840-processor.html)

### [SparkFun MicroMod nRF52840 Processor](https://www.sparkfun.com/sparkfun-micromod-nrf52840-processor.html) 

[ WRL-16984 ]

The SparkFun MicroMod nRF52840 Processor offers a powerful combination of ARM Cortex-M4 CPU and 2.4 GHz Bluetooth transceiver...

[ [\$29.50] ]

[![SparkFun MicroMod SAMD51 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/8/16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html)

### [SparkFun MicroMod SAMD51 Processor](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html) 

[ DEV-16791 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun MicroMod SAMD51 Processor Board is one powerful microcontroller packaged on a ...

[ [\$18.95] ]

[![SparkFun MicroMod Artemis Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/0/16401-SparkFun_MicroMod_Artemis_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html)

### [SparkFun MicroMod Artemis Processor](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html) 

[ DEV-16401 ]

Featuring the Artemis Module, this processor is capable of machine learning, Bluetooth, I2C, GPIO, PWM, SPI & packaged to fit...

[ [\$17.50] ]

You\'ll also need a USB-C cable to connect the Carrier to your computer and if you want to add some Qwiic breakouts to your MicroMod project you\'ll want at least one Qwiic cable to connect it all together. Below are some options for both of those cables:

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Flexible Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/6/17259-Flexible_Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-100mm.html)

### [Flexible Qwiic Cable - 100mm](https://www.sparkfun.com/flexible-qwiic-cable-100mm.html) 

[ PRT-17259 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

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

You can power the Asset Tracker via USB-C but for portable applications you\'ll need a single-cell LiPo battery too. Here are some examples:

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

You\'ll also need LTE and GNSS antennas. There are many to choose from, but here are some recommendations:

[![GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/1/15192-GNSS_Multi-band_Magnetic_Mount_Antenna_SMA_-_5m-01.jpg)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html)

### [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html) 

[ GPS-15192 ]

The ANN-MB-00 GNSS multi-band antenna is extremely unique from other GNSS/GPS antennas in that it is designed to receive both...

[ [\$109.95] ]

[![GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/0/14986-GPS_GNSS_Magnetic_Mount_Antenna_SMA_-_3m-01.jpg)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html)

### [GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html) 

[ GPS-14986 ]

This exceptional GPS/GNSS antenna is designed for both GPS and GLONASS reception.

[ [\$16.50] ]

[![LTE Hinged External Antenna - 698MHz-2.7GHz, SMA Male](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/8/7/16432-698MHz-2.7GHz_LTE_Hinged_External_Antenna__with_SMA_Male_Connector-01.jpg)](https://www.sparkfun.com/lte-hinged-external-antenna-698mhz-2-7ghz-sma-male.html)

### [LTE Hinged External Antenna - 698MHz-2.7GHz, SMA Male](https://www.sparkfun.com/lte-hinged-external-antenna-698mhz-2-7ghz-sma-male.html) 

[ CEL-16432 ]

Molex LTE/5G Cellular External Antennas are designed for 2G/3G/4G/5G modules and devices.

[ [\$12.95] ]

**Note:** The SMA connections are standard polarity: the connector on the Asset Tracker is female, the antenna connection needs to be standard male. Antennas with reverse-polarity connectors are not suitable for the Asset Tracker.

### Recommended Tools

You will need a screw driver to tighten the screw between the processor board and carrier board.

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

### Suggested Reading

If you are not familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/micromod). We recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)   [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*                                                                                                                                        *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Finally, if you aren\'t familiar with the following concepts you may want to check out a few of these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1663&name=MicroMod+Asset+Tracker+Carrier+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1663 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+Asset+Tracker+Carrier+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1663&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1663&t=MicroMod+Asset+Tracker+Carrier+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1663&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F6%2F6%2F3%2FMicroMod_Asset_Tracker-Thumbnail.jpg&description=MicroMod+Asset+Tracker+Carrier+Board+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/hardware-overview) [Choosing a Processor Board](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/choosing-a-processor-board) [Hardware Assembly](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/hardware-assembly) [Software Setup](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/software-setup) [Arduino Examples](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/arduino-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/resources-and-going-further)

[Comments [1]](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Cellular](https://learn.sparkfun.com/tutorials/tags/cellular)
  - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [MicroMod](https://learn.sparkfun.com/tutorials/tags/micromod)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]