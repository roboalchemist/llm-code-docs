# Source: https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Triple Axis Accelerometer Breakout - KX13x (Qwiic) Hookup Guide

# Triple Axis Accelerometer Breakout - KX13x (Qwiic) Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino], [![](https://cdn.sparkfun.com/avatar/fde91fc929973498fdcfcfc9ccb086ab?d=retro&s=20&r=pg) Englandsaurus], [![](https://cdn.sparkfun.com/avatar/5c320824995fcd6990beaf7a3d3f6037?d=retro&s=20&r=pg) Elias The Sparkiest]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1429&name=Triple+Axis+Accelerometer+Breakout+-+KX13x+%28Qwiic%29+Hookup+Guide+ "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1429 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Triple+Axis+Accelerometer+Breakout+-+KX13x+%28Qwiic%29+Hookup+Guide+&url=http%3A%2F%2Fsfe.io%2Ft1429&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1429&t=Triple+Axis+Accelerometer+Breakout+-+KX13x+%28Qwiic%29+Hookup+Guide+ "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1429&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F4%2F2%2F9%2FKX13x_Breakout-Thumbnail.jpg&description=Triple+Axis+Accelerometer+Breakout+-+KX13x+%28Qwiic%29+Hookup+Guide+ "Pin It")

## Introduction

The SparkFun [Triple Axis Accelerometer Breakout - KX134 (Qwiic)](https://www.sparkfun.com/products/17589) and [Triple Axis Accelerometer Breakout - KX132 (Qwiic)](https://www.sparkfun.com/products/17871) offer two high-speed additions to SparkFun\'s accelerometer selection featuring the KX134-1211 and KX132-1211 3-axis digital accelerometers from Kionix. The KX134 and KX132 both include a host of accelerometer features including Freefall detection, Directional Tap^™^ and Double-Tap^™^ detection, tilt orientation detection and more. The breakouts can interface with controllers using both I^2^C and SPI at high speeds so you can use it in either an existing Qwiic/I^2^C chain or SPI bus.

[![SparkFun Triple Axis Accelerometer Breakout - KX134 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/6/6/1/17589-SparkFun_Triple_Axis_Accelerometer_Breakout_-_KX134__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-kx134-qwiic.html)

### [SparkFun Triple Axis Accelerometer Breakout - KX134 (Qwiic)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-kx134-qwiic.html) 

[ SEN-17589 ]

This SparkFun Triple-Axis Accelerometer Breakout is a simple Qwiic breakout for the KX134 digital accelerometer from Kionix.

[ [\$35.95] ]

[![SparkFun Triple Axis Accelerometer Breakout - KX132 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/0/6/0/17871-SparkFun_Triple_Axis_Accelerometer_Breakout_-_KX132__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-kx132-qwiic.html)

### [SparkFun Triple Axis Accelerometer Breakout - KX132 (Qwiic)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-kx132-qwiic.html) 

[ SEN-17871 ]

This SparkFun Triple-Axis Accelerometer Breakout is a simple Qwiic breakout for the KX132 digital accelerometer from Kionix.

[ [\$15.50] ]

The KX134 is a low-power, 16-bit resolution 3-axis accelerometer capable of measuring ±8g/16g/32g/64g (user selectable) and has up to a 10kHz (max) output data rate making it ideal for high-g measurements as well as high-speed applications such as vibration sensing. The KX132 offers nearly the same data specifications at smaller acceleration (±2g/4g/8g/16g) ranges. At lower ranges the sensitivity can be set as high as 17367 counts/g (@±2g), so it\'s a great for applications looking for both high-speed data rates and high-sensitivity measurements at lower acceleration ranges.

**Note:** Any reference in this guide specific to either version of these breakouts will denote the version (KX132 or KX134) discussed. We\'ll use the terms \"KX13x Breakout(s)\" or \"KX13x\" when discussing subjects or specifications pertaining to both boards or both accelerometers.

### Required Materials

In order to follow along with this tutorial you\'ll need a few items along with your KX13x Breakout. First, you will need a microcontroller or single-board computer (SBC) like a Raspberry Pi to communicate with the board. Click the button below to toggle to recommended Raspberry Pi and Qwiic Pi products.

[**Raspberry Pi Materials (Toggle)**]

Below are a few Arduino development boards that come Qwiic-enabled out of the box:

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

[![SparkFun Qwiic Micro - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/0/15423-SparkFun_Qwiic_Micro_-_SAMD21-01b.jpg)](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html)

### [SparkFun Qwiic Micro - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html) 

[ DEV-15423 ]

The SparkFun Qwiic Micro is molded to fit our standard 1\" x 1\" Qwiic board size which makes it our smallest SAMD21 micro-cont...

[ [\$22.95] ]

If your preferred microcontroller does not have a Qwiic connector, you can add one using one of the following products:

[![SparkFun Qwiic Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/5/1/14495-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-adapter.html)

### [SparkFun Qwiic Adapter](https://www.sparkfun.com/sparkfun-qwiic-adapter.html) 

[ DEV-14495 ]

The SparkFun Qwiic Adapter provides the perfect means to make any old I^2^C board into a Qwiic enabled board.

[ [\$1.60] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

[![SparkFun Qwiic Shield for Arduino Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/6/16789-SparkFun_Qwiic_Shield_for_Arduino_Nano-05.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino-nano.html)

### [SparkFun Qwiic Shield for Arduino Nano](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino-nano.html) 

[ DEV-16789 ]

The SparkFun Qwiic Shield for Arduino Nano makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards...

[ [\$5.50] ]

[![SparkFun Qwiic Shield for Thing Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/7/16790-SparkFun_Qwiic_Shield_for_Thing_Plus-05.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-thing-plus.html)

### [SparkFun Qwiic Shield for Thing Plus](https://www.sparkfun.com/sparkfun-qwiic-shield-for-thing-plus.html) 

[ DEV-16790 ]

The SparkFun Qwiic Shield for Thing Plus makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards t...

[ [\$5.10] ]

If you would prefer to use the SparkFun Qwiic KX13x Python package with either board you\'ll instead want a single-board computer like the products listed below:

[![Raspberry Pi 4 Model B (4 GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/2/2/15447-Raspberry_Pi_4_Model_B__4_GB_-01.jpg)](https://www.sparkfun.com/raspberry-pi-4-model-b-4-gb.html)

### [Raspberry Pi 4 Model B (4 GB)](https://www.sparkfun.com/raspberry-pi-4-model-b-4-gb.html) 

[ DEV-15447 ]

The 4 GB Raspberry Pi 4 features the ability to run two 4k resolution monitors, to run true Gigabit Ethernet operations, all ...

[ [\$64.95] ]

[![SparkFun Raspberry Pi 4 Desktop Kit - 2GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/2/16385-Raspberry_Pi_4_Desktop_Kit_-_2GB-01a.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-2gb.html)

### [SparkFun Raspberry Pi 4 Desktop Kit - 2GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-2gb.html) 

[ KIT-16385 ]

The SparkFun Raspberry Pi 4 Desktop Kit (2GB) includes everything you need to turn any monitor with an HDMI port into a deskt...

**Retired**

[![NVIDIA Jetson Nano 2GB Developer Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/3/0/17244-NVIDIA_Jetson_Nano_2GB_Developer_Kit_a-01.jpg)](https://www.sparkfun.com/nvidia-jetson-nano-2gb-developer-kit.html)

### [NVIDIA Jetson Nano 2GB Developer Kit](https://www.sparkfun.com/nvidia-jetson-nano-2gb-developer-kit.html) 

[ DEV-17244 ]

The NVIDIA® Jetson Nano™ 2GB Developer Kit delivers the performance to run modern AI workloads at a small form factor, low...

**Retired**

[![SparkFun DLI Kit for Jetson Nano 2GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/3/1/17245-SparkFun_DLI_Kit_for_Jetson_Nano_2GB-01.jpg)](https://www.sparkfun.com/sparkfun-dli-kit-for-jetson-nano-2gb.html)

### [SparkFun DLI Kit for Jetson Nano 2GB](https://www.sparkfun.com/sparkfun-dli-kit-for-jetson-nano-2gb.html) 

[ KIT-17245 ]

The release of the Jetson Nano™ 2GB Developer Kit, NVIDIA® empowers developers, researchers, students, and hobbyists to ex...

**Retired**

SparkFun offers several options to add Qwiic connectors to single-board computers using the Raspberry Pi\'s 2x20 header:

[![SparkFun Qwiic HAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/5/14459-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-hat-for-raspberry-pi.html)

### [SparkFun Qwiic HAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-hat-for-raspberry-pi.html) 

[ DEV-14459 ]

The SparkFun Qwiic HAT for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and still u...

[ [\$6.95] ]

[![SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/5/8/8/15945-SparkFun_Qwiic_pHAT_V3.0_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-phat-v2-0-for-raspberry-pi.html)

### [SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-phat-v2-0-for-raspberry-pi.html) 

[ DEV-15945 ]

The SparkFun Qwiic pHAT V2 for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and sti...

[ [\$7.95] ]

[![SparkFun Qwiic SHIM for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/3/9/9/16385-15794-SparkFun_Qwiic_SHIM_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html)

### [SparkFun Qwiic SHIM for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html) 

[ DEV-15794 ]

The SparkFun Qwiic SHIM for Raspberry Pi is a small, easily removable breakout that easily adds a Qwiic connector to your Ras...

[ [\$1.95] ]

[![SparkFun Servo pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/2/7/15316-SparkFun_Servo_pHAT_for_Raspberry_Pi-01b.jpg)](https://www.sparkfun.com/sparkfun-servo-phat-for-raspberry-pi.html)

### [SparkFun Servo pHAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-servo-phat-for-raspberry-pi.html) 

[ DEV-15316 ]

The SparkFun Servo pHAT for Raspberry Pi allows your Raspberry Pi to control up to 16 servo motors in a straightforward manne...

[ [\$13.95] ]

At least one Qwiic cable is recommended to connect your KX13x Breakout to your microcontroller/SBC:

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

For users who wish to communicate with the KX13x Breakout using SPI, some through-hole soldering will be necessary. You may already have a few of these items but if not the tools and products below will help with that assembly:

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

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic):

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1429&name=Triple+Axis+Accelerometer+Breakout+-+KX13x+%28Qwiic%29+Hookup+Guide+ "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1429 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Triple+Axis+Accelerometer+Breakout+-+KX13x+%28Qwiic%29+Hookup+Guide+&url=http%3A%2F%2Fsfe.io%2Ft1429&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1429&t=Triple+Axis+Accelerometer+Breakout+-+KX13x+%28Qwiic%29+Hookup+Guide+ "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1429&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F4%2F2%2F9%2FKX13x_Breakout-Thumbnail.jpg&description=Triple+Axis+Accelerometer+Breakout+-+KX13x+%28Qwiic%29+Hookup+Guide+ "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/hardware-assembly) [KX13x Arduino Library](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/kx13x-arduino-library) [Arduino Examples](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/arduino-examples) [Qwiic KX13x Python Package](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/qwiic-kx13x-python-package) [Python Examples](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/python-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/resources-and-going-further)

[Comments [6]](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/discuss) [Single Page](https://learn.sparkfun.com/tutorials/triple-axis-accelerometer-breakout---kx13x-qwiic-hookup-guide-/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]