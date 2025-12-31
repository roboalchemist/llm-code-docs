# Source: https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroMod GNSS Function Board - ZED-F9P Hookup Guide

# MicroMod GNSS Function Board - ZED-F9P Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2419&name=MicroMod+GNSS+Function+Board+-+ZED-F9P+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2419 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+GNSS+Function+Board+-+ZED-F9P+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2419&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2419&t=MicroMod+GNSS+Function+Board+-+ZED-F9P+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2419&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F4%2F1%2F9%2FMM_ZED-F9P_FB-Thumb.jpg&description=MicroMod+GNSS+Function+Board+-+ZED-F9P+Hookup+Guide "Pin It")

## Introduction

As some readers may guess by the assortment of SparkFun products featuring it, we love the ZED-F9P GNSS module from u-blox. The [SparkFun MicroMod GNSS Function Board - ZED-F9P](https://www.sparkfun.com/products/19663) provides high precision GNSS capabilities for MicroMod projects using Main Board/Function Board assemblies. The ZED-F9P module from u-blox is capable of up to 10mm 3-dimensional accuracy though the module requires a clear view of the sky as well as correction data from an RTCM source to achieve this accuracy. The ZED-F9P can act as a base station as well so you can use it with a second Function Board (or another SparkFun ZED-F9P product) together to achieve millimeter positional accuracy.

[![SparkFun MicroMod GNSS Function Board - ZED-F9P](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/3/3/9/ZEDF9P_01.jpg)](https://www.sparkfun.com/sparkfun-micromod-gnss-function-board-zed-f9p.html)

### [SparkFun MicroMod GNSS Function Board - ZED-F9P](https://www.sparkfun.com/sparkfun-micromod-gnss-function-board-zed-f9p.html) 

[ GPS-19663 ]

The SparkFun MicroMod GNSS Function Board takes everything we love about the ZED-F9P module from u-blox and combines it with ...

[\$274.95] [ [\$184.22] ]

Having the ZED-F9P on a MicroMod Function board allows for even more versatility with projects using the ZED-F9P allowing users to mix and match not only their preferred Processor but also to pair it with another Function Board to add even more versatility to a GNSS project.

This guide will go over the hardware present on this Function Board, how to assemble it into a MicroMod circuit as well as an Arduino example to start getting location data from the ZED-F9P.

### Required Materials

You\'ll need the following materials along with the MicroMod GNSS Function Board - ZED-F9P to complete this tutorial and use the Function Board.

#### Main Board

All Function Boards require a Main Board and Processor to connect to each other. Depending on your application, you may need either a Single or Dual Main Board:

[![SparkFun MicroMod Main Board - Single](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/0/4/2/18575-SparkFun_MicroMod_Main_Board_-_Single-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-single-dev-18575.html)

### [SparkFun MicroMod Main Board - Single](https://www.sparkfun.com/sparkfun-micromod-main-board-single-dev-18575.html) 

[ DEV-18575 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with a single ...

**Retired**

[![SparkFun MicroMod Main Board - Double](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/0/4/3/18576-SparkFun_MicroMod_Main_Board_-_Double-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-double-dev-18576.html)

### [SparkFun MicroMod Main Board - Double](https://www.sparkfun.com/sparkfun-micromod-main-board-double-dev-18576.html) 

[ DEV-18576 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with up to two...

**Retired**

#### Processor Board

You\'ll need a Processor Board to act as a host controller for the Function Board:

[![SparkFun MicroMod Teensy Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/2/16402-SparkFun_MicroMod_Teensy_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html)

### [SparkFun MicroMod Teensy Processor](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html) 

[ DEV-16402 ]

This board leverages the awesome computing power of the NXP iMXRT1062 chip (ARM Cortex-M7) and pairs it with the M.2 MicroMod...

[ [\$24.95] ]

[![SparkFun MicroMod ESP32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/8/0/16781-SparkFun_MicroMod_ESP32_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html)

### [SparkFun MicroMod ESP32 Processor](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html) 

[ WRL-16781 ]

This board combines Espressif\'s ESP32 with our M.2 connector interface to bring a power-packed processor board into our Micro...

[ [\$19.95] ]

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

#### Antenna

The GNSS Function Board also requires an antenna. We recommend using a GNSS multi-band antenna compatible with both L1 and L2 bands for full reception like the ones below:

[![GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/1/15192-GNSS_Multi-band_Magnetic_Mount_Antenna_SMA_-_5m-01.jpg)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html)

### [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html) 

[ GPS-15192 ]

The ANN-MB-00 GNSS multi-band antenna is extremely unique from other GNSS/GPS antennas in that it is designed to receive both...

[ [\$109.95] ]

[![GNSS Multi-Band L1/L2 Helical Antenna (SMA) BT-560](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/4/1/9/17383-GNSS_Multi-Band_L1_L2_Helical_Antenna__SMA__BT-560-01a.jpg)](https://www.sparkfun.com/gnss-multi-band-l1-l2-helical-antenna-sma-bt-560.html)

### [GNSS Multi-Band L1/L2 Helical Antenna (SMA) BT-560](https://www.sparkfun.com/gnss-multi-band-l1-l2-helical-antenna-sma-bt-560.html) 

[ GPS-17383 ]

The BT-560 antenna is a small, very light weight GNSS/GPS L1/L2 multiband antenna for GPS, GLONASS, Galileo, and BeiDou const...

**Retired**

**Note:** If you want to try different GNSS antennas, the following antennas will work but are limited to L1 frequencies so they will not enable the full L1/L2 capabilities of the ZED-F9P.\
\

[![GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/0/14986-GPS_GNSS_Magnetic_Mount_Antenna_SMA_-_3m-01.jpg)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html)

### [GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html) 

[ GPS-14986 ]

This exceptional GPS/GNSS antenna is designed for both GPS and GLONASS reception.

[ [\$16.50] ]

[![GPS/GNSS Embedded Antenna - 1m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/1/14987-GPS_GNSS_Embedded_Antenna_SMA_-_1m-01a.jpg)](https://www.sparkfun.com/gps-gnss-embedded-antenna-1m-sma.html)

### [GPS/GNSS Embedded Antenna - 1m (SMA)](https://www.sparkfun.com/gps-gnss-embedded-antenna-1m-sma.html) 

[ GPS-14987 ]

This tri-band GNSS antenna is ideal for GPS L1, GLONASS L1, and Beidou B2 reception.

[ [\$95.95] ]

#### Antenna Accessories

The GNNS Function Board uses a u.Fl connector for the antenna connection so in order to use the antennas listed above, you will need an adapter cable like the ones below. You may also want a grounding plate to maximize your antenna\'s reception:

[![RP-SMA to U.FL Cable - 150mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/0/3/0/18569-RP-SMA_to_U.FL_Cable_-_150mm-01.jpg)](https://www.sparkfun.com/rp-sma-to-u-fl-cable-150mm.html)

### [RP-SMA to U.FL Cable - 150mm](https://www.sparkfun.com/rp-sma-to-u-fl-cable-150mm.html) 

[ WRL-18569 ]

This RP-SMA to U.FL Cable is commonly used to connect boards with the compact U.FL connector to an enclosure wall. This allow...

[ [\$2.75] ]

[![GPS Antenna Ground Plate](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/5/9/3/17519-GPS_Antenna_Ground_Plate-01.jpg)](https://www.sparkfun.com/gps-antenna-ground-plate.html)

### [GPS Antenna Ground Plate](https://www.sparkfun.com/gps-antenna-ground-plate.html) 

[ GPS-17519 ]

Using this simple steel plate effectively improves simple patch antenna performance to near professional level antenna setups...

[ [\$7.25] ]

[![Interface Cable SMA to U.FL - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/2/09145-01b.jpg)](https://www.sparkfun.com/interface-cable-sma-to-u-fl.html)

### [Interface Cable SMA to U.FL - 100mm](https://www.sparkfun.com/interface-cable-sma-to-u-fl.html) 

[ WRL-09145 ]

This is a 4\" connector cable that interfaces U.FL RF connectors to regular SMA connectors. This cable is commonly used to con...

[ [\$5.75] ]

[![Interface Cable U.FL to SMA - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/7/9/18154-Interface_Cable_U.FL_to_SMA-03.jpg)](https://www.sparkfun.com/interface-cable-u-fl-to-sma-100mm.html)

### [Interface Cable U.FL to SMA - 100mm](https://www.sparkfun.com/interface-cable-u-fl-to-sma-100mm.html) 

[ WRL-18154 ]

A U.FL to SMA (jack) bulkhead straight connector with a 1.32 mm diameter cable.

**Retired**

### Suggested Reading

The [MicroMod ecosystem](https://www.sparkfun.com/micromod) is a unique way to allow users to customize their project to their needs. If you aren\'t familiar with the MicroMod system, click on the banner below for more information.

[![MicroMod Logo](https://cdn.sparkfun.com/r/500-70/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)

\

Before getting started, be sure to check out our [What is GPS RTK?](https://learn.sparkfun.com/tutorials/what-is-gps-rtk) tutorial and if you\'re not familiary with u-center, have a look at our [Getting Started with U-Center](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox) as well as these related tutorials:

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/serial-basic-hookup-guide)

### Serial Basic Hookup Guide 

Get connected quickly with this Serial to USB adapter.

[](https://learn.sparkfun.com/tutorials/what-is-gps-rtk)

### What is GPS RTK? 

Learn about the latest generation of GPS and GNSS receivers to get 14mm positional accuracy!

[](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox)

### Getting Started with U-Center for u-blox 

Learn the tips and tricks to use the u-blox software tool to configure your GPS receiver.

This tutorial is based around the guide for the SparkFun GPS-RTK2 Board - ZED-F9P so you may want to check out these tutorials for more information on GPS-RTK:

[](https://learn.sparkfun.com/tutorials/gps-rtk-hookup-guide)

### GPS-RTK Hookup Guide 

September 13, 2018

Find out where you are! Use this easy hook-up guide to get up and running with the SparkFun high precision GPS-RTK NEO-M8P-2 breakout board.

[](https://learn.sparkfun.com/tutorials/gps-rtk2-hookup-guide)

### GPS-RTK2 Hookup Guide 

January 14, 2019

Get precision down to the diameter of a dime with the new ZED-F9P from u-blox.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2419&name=MicroMod+GNSS+Function+Board+-+ZED-F9P+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2419 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+GNSS+Function+Board+-+ZED-F9P+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2419&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2419&t=MicroMod+GNSS+Function+Board+-+ZED-F9P+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2419&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F4%2F1%2F9%2FMM_ZED-F9P_FB-Thumb.jpg&description=MicroMod+GNSS+Function+Board+-+ZED-F9P+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/hardware-assembly) [Software Installation](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/software-installation) [Arduino Example](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/arduino-example) [Troubleshooting](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [ESP32](https://learn.sparkfun.com/tutorials/tags/esp32)
  - [GNSS](https://learn.sparkfun.com/tutorials/tags/gnss)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [MicroMod](https://learn.sparkfun.com/tutorials/tags/micromod)
  - [Navigation](https://learn.sparkfun.com/tutorials/tags/navigation)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]