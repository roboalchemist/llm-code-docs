# Source: https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- GNSS Timing Breakout - ZED-F9T (Qwiic) Hookup Guide

# GNSS Timing Breakout - ZED-F9T (Qwiic) Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1ff6ad39b8c242a14296a76845e116cd?d=retro&s=20&r=pg) Nate], [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2088&name=GNSS+Timing+Breakout+-+ZED-F9T+%28Qwiic%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2088 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=GNSS+Timing+Breakout+-+ZED-F9T+%28Qwiic%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2088&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2088&t=GNSS+Timing+Breakout+-+ZED-F9T+%28Qwiic%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2088&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F0%2F8%2F8%2FGNSS_Timing_Breakout-Thumbnail.jpg&description=GNSS+Timing+Breakout+-+ZED-F9T+%28Qwiic%29+Hookup+Guide "Pin It")

## Introduction

Introducing the [SparkFun GNSS Timing Breakout - ZED-F9T (Qwiic)](https://www.sparkfun.com/products/18774), a unique entry into SparkFun\'s GNSS catalog featuring the ZED-F9T GNSS receiver from u-blox. The ZED-F9T provides up to 5 nanosecond timing accuracy under clear skies with no external GNSS correction making it perfect for applications where timing accuracy is imperative. Need an extremely accurate time reference to maximize the efficiency of your IoT network of 5G devices? The GNSS Timing Breakout - ZED-F9T could be the perfect solution.

[![SparkFun GNSS Timing Breakout - ZED-F9T (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/3/3/2/18774-SparkFun_GNSS_Timing_Breakout_-_ZED-F9T__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gnss-timing-breakout-zed-f9t-qwiic.html)

### [SparkFun GNSS Timing Breakout - ZED-F9T (Qwiic)](https://www.sparkfun.com/sparkfun-gnss-timing-breakout-zed-f9t-qwiic.html) 

[ GPS-18774 ]

The SparkFun GNSS Timing Breakout offers a unique entry into SparkFun\'s geospatial catalog featuring the ZED-F9T GNSS receive...

[ [\$309.95] ]

This breakout shares a similar design as the [SparkFun GPS-RTK-SMA Breakout](https://www.sparkfun.com/products/16481) to create a small but comprehensive development tool for ZED-F9T. The design includes a USB-C connector for primary power and communication, two Qwiic connectors for communicating over I^2^C using the SparkFun [Qwiic system](https://www.sparkfun.com/qwiic), three SMA connectors for the antenna and timing pulse signals as well as a host of PTH pins allowing direct interaction with most of the ZED-F9T\'s pinout.

### Required Materials

You will need the following materials along with the SparkFun GNSS Timing Breakout - ZED-F9T (Qwiic) to follow along with this tutorial.

#### GNSS Antenna

The ZED-F9T is a dual receiving GNSS receiver which means it can receive both L1 and L2 GNSS frequencies. To enable this, you will need an appropriate antenna such as those listed below:

[![GNSS Multi-Band L1/L2/L5 Surveying Antenna - TNC (SPK6618H)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/5/9/7/SparkFun_GNSS_SPK6618H_Triband_Antenna_-_2-1.png)](https://www.sparkfun.com/gnss-multi-band-l1-l2-l5-surveying-antenna-tnc-spk6618h.html)

### [GNSS Multi-Band L1/L2/L5 Surveying Antenna - TNC (SPK6618H)](https://www.sparkfun.com/gnss-multi-band-l1-l2-l5-surveying-antenna-tnc-spk6618h.html) 

[ GPS-21801 ]

The SPK6618H is the latest advancement in GNSS antenna technology allowing tri-band (L1/L2/L5) reception for GPS, GLONASS, Ga...

[ [\$169.95] ]

[![GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/1/15192-GNSS_Multi-band_Magnetic_Mount_Antenna_SMA_-_5m-01.jpg)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html)

### [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html) 

[ GPS-15192 ]

The ANN-MB-00 GNSS multi-band antenna is extremely unique from other GNSS/GPS antennas in that it is designed to receive both...

[ [\$109.95] ]

[![MagmaX2 Active Multiband GNSS Magnetic Mount Antenna - AA.200](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/0/7/0/17108-AA.200_____MagmaX2_Active_Multiband_GNSS_Magnetic_Mount_Antenna-01A.jpg)](https://www.sparkfun.com/magmax2-active-multiband-gnss-magnetic-mount-antenna-aa-200.html)

### [MagmaX2 Active Multiband GNSS Magnetic Mount Antenna - AA.200](https://www.sparkfun.com/magmax2-active-multiband-gnss-magnetic-mount-antenna-aa-200.html) 

[ GPS-17108 ]

The AA.200 antenna is an active multiband GNSS magnetic mount antenna that exhibits excellent gain and good radiation pattern...

**Retired**

[![GNSS Multi-Band L1/L2 Helical Antenna (SMA) BT-560](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/4/1/9/17383-GNSS_Multi-Band_L1_L2_Helical_Antenna__SMA__BT-560-01a.jpg)](https://www.sparkfun.com/gnss-multi-band-l1-l2-helical-antenna-sma-bt-560.html)

### [GNSS Multi-Band L1/L2 Helical Antenna (SMA) BT-560](https://www.sparkfun.com/gnss-multi-band-l1-l2-helical-antenna-sma-bt-560.html) 

[ GPS-17383 ]

The BT-560 antenna is a small, very light weight GNSS/GPS L1/L2 multiband antenna for GPS, GLONASS, Galileo, and BeiDou const...

**Retired**

A [low cost GNSS antenna](https://www.sparkfun.com/products/14986) *will* work and provide a basic fix but the advanced timing and positional accuracy features of the ZED-F9T will not be available without L2 support.

#### USB Cable

Basic use of the ZED-F9T either through a serial terminal or u-blox\'s u-center application needs a USB-C cable to connect the board to your computer:

[![Reversible USB A to C Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/4/15425-Reversible_USB_A_to_C_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html)

### [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html) 

[ CAB-15425 ]

These 0.8m cables have minor modifications that allow them to be plugged into their ports regardless of orientation on the US...

[ [\$6.50] ]

[![Reversible USB A to C Cable - 0.3m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/5/15426-Reversible_USB_A_to_C_Cable_-_0.3m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-3m.html)

### [Reversible USB A to C Cable - 0.3m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-3m.html) 

[ CAB-15426 ]

These 0.3m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the...

[ [\$5.50] ]

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

#### Arduino Examples Materials

For those who want to use the breakout board with the [SparkFun u-blox GNSS Arduino Library](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library), you\'ll need an Arduino microcontroller, Qwiic cable and USB-C cable to get started. We found the ESP32 works as a great transmitting option when creating a network of GNSS devices receiving time correction data from a ZED-F9T configured to act as a base station:

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![SparkFun Thing Plus - ESP32-S2 WROOM](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/6/2/17743-SparkFun_Thing_Plus_-_ESP32-S2_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html)

### [SparkFun Thing Plus - ESP32-S2 WROOM](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html) 

[ WRL-17743 ]

The SparkFun ESP32-S2 WROOM Thing Plus is a highly-integrated, Feather form-factor development board equipped with the 2.4 GH...

[ [\$24.50] ]

[![SparkFun u-blox library examples](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/8/8/SparkFun_u-blox_Library_Examples.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/8/8/SparkFun_u-blox_Library_Examples.png)

The SparkFun u-blox GNSS Arduino Library has a tremendous number of examples and features to demonstrate the power of our GNSS receivers. For the ZED-F9T specifically, be sure to view the **Time Pulse** examples. These will show you how to configure the time pulse settings for the two time pulse outputs.

While configuring the ZED-F9T over Qwiic from a microcontroller is pretty easy, many applications for timing require a set it and forget it mentality. Consider using [u-center](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox) from u-blox to configure your ZED-F9T over USB and then saving the configuration to BBR (battery backed RAM) so that the module comes on with the same settings at the next power on.

### Recommended Reading

Before getting started with the GNSS Timing Breakout you may want to read through these tutorials if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/serial-basic-hookup-guide)

### Serial Basic Hookup Guide 

Get connected quickly with this Serial to USB adapter.

[](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox)

### Getting Started with U-Center for u-blox 

Learn the tips and tricks to use the u-blox software tool to configure your GPS receiver.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2088&name=GNSS+Timing+Breakout+-+ZED-F9T+%28Qwiic%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2088 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=GNSS+Timing+Breakout+-+ZED-F9T+%28Qwiic%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2088&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2088&t=GNSS+Timing+Breakout+-+ZED-F9T+%28Qwiic%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2088&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F0%2F8%2F8%2FGNSS_Timing_Breakout-Thumbnail.jpg&description=GNSS+Timing+Breakout+-+ZED-F9T+%28Qwiic%29+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/hardware-assembly) [Arduino Examples](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/arduino-examples) [Using the ZED-F9T in Differential Timing Mode](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/using-the-zed-f9t-in-differential-timing-mode) [Resources and Going Further](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/gnss-timing-breakout---zed-f9t-qwiic-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [GNSS](https://learn.sparkfun.com/tutorials/tags/gnss)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]