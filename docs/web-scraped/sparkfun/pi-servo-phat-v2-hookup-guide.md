# Source: https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Pi Servo pHAT (v2) Hookup Guide

# Pi Servo pHAT (v2) Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete], [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft910&name=Pi+Servo+pHAT+%28v2%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft910 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Pi+Servo+pHAT+%28v2%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft910&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft910&t=Pi+Servo+pHAT+%28v2%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft910&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F9%2F1%2F0%2FAssembly_Servo.gif&description=Pi+Servo+pHAT+%28v2%29+Hookup+Guide "Pin It")

## Introduction

The [SparkFun Pi Servo pHAT](https://www.sparkfun.com/products/15316) provides your Raspberry Pi with 16 PWM channels that can be controlled over I^2^C. These channels are broken out in a header combination that is perfect for connecting servo motors. Additionally, the PWM channels can control other PWM devices as well.

[![SparkFun Servo pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/8/2/7/15316-SparkFun_Servo_pHAT_for_Raspberry_Pi-01b.jpg)](https://www.sparkfun.com/sparkfun-servo-phat-for-raspberry-pi.html)

### [SparkFun Servo pHAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-servo-phat-for-raspberry-pi.html) 

[ DEV-15316 ]

The SparkFun Servo pHAT for Raspberry Pi allows your Raspberry Pi to control up to 16 servo motors in a straightforward manne...

[ [\$13.95] ]

Furthermore, the Pi Servo pHAT can be used for a serial terminal connection to remotely control the Raspberry Pi, without the need for a monitor and keyboard (*header used by the Sphero RVR*). As an added bonus, we have provided a Qwiic connector for users to easily interface with the I^2^C bus using the [Qwiic system](https://www.sparkfun.com/qwiic). Who says you can\'t have it all?

### Required Materials

**Note:** Below are lists of products that you will need for this hookup guide. You may already have some of these products in your cart or at home; please, feel free to modify your cart as necessary.

------------------------------------------------------------------------

To get started with the Pi Servo pHAT, you will need a **Raspberry Pi board with headers**. There are several options that can be found under the [Raspberry Pi Board](https://www.sparkfun.com/categories/395) product category. Additionally, we also offer these boards in [various kits](https://www.sparkfun.com/categories/397).

[![Raspberry Pi 500+ (Unit Only)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/1/7/2/9/29821-RPi-500-Feature.jpg)](https://www.sparkfun.com/raspberry-pi-500-plus-unit-only.html)

### [Raspberry Pi 500+ (Unit Only)](https://www.sparkfun.com/raspberry-pi-500-plus-unit-only.html) 

[ DEV-29821 ]

The Raspberry Pi 500+ is an all-in-one personal computer built into a compact keyboard, now updated with a high-quality mecha...

[ [\$210.00] ]

[![Raspberry Pi 5 - 16GB](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/6/0/3/DEV-27446-Raspberry-Pi-5-16GB-Feature.jpg)](https://www.sparkfun.com/raspberry-pi-5-16gb.html)

### [Raspberry Pi 5 - 16GB](https://www.sparkfun.com/raspberry-pi-5-16gb.html) 

[ DEV-27446 ]

The next iteration of the Raspberry Pi single board computer featuring a 64-bit quad-core Arm Cortex-A76 processor running at...

[ [\$150.00] ]

[![Raspberry Pi 5 - 8GB](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/8/4/2/23551-Raspberry-Pi-5-8G-feature.jpg)](https://www.sparkfun.com/raspberry-pi-5-8gb.html)

### [Raspberry Pi 5 - 8GB](https://www.sparkfun.com/raspberry-pi-5-8gb.html) 

[ DEV-23551 ]

The next iteration of the Raspberry Pi single board computer featuring a 64-bit quad-core Arm Cortex-A76 processor running at...

[ [\$100.00] ]

[![Raspberry Pi Zero 2 W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/2/5/5/18713-Raspberry_Pi_Zero_2_W-01.jpg)](https://www.sparkfun.com/raspberry-pi-zero-2-w.html)

### [Raspberry Pi Zero 2 W](https://www.sparkfun.com/raspberry-pi-zero-2-w.html) 

[ DEV-18713 ]

The Raspberry Pi Zero 2 W is still the Pi you know and love, but at a largely reduced size of only 65mm long by 30mm wide and...

[ [\$17.25] ]

[![SparkFun Raspberry Pi Zero W Basic Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/5/9/14298_1.jpg)](https://www.sparkfun.com/products/14298)

### [SparkFun Raspberry Pi Zero W Basic Kit](https://www.sparkfun.com/products/14298) 

[ KIT-14298 ]

The Raspberry Pi Zero W can be a bit tricky to set up with its unique power and cable requirements. That\'s where this kit com...

**Retired**

[![SparkFun Basic Autonomous Kit for Sphero RVR](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/0/4/15302-SparkFun_Basic_Autonomous_Kit_for_Sphero_RVR-01.jpg)](https://www.sparkfun.com/products/15302)

### [SparkFun Basic Autonomous Kit for Sphero RVR](https://www.sparkfun.com/products/15302) 

[ KIT-15302 ]

The SparkFun Basic Autonomous Kit for Sphero RVR provides an expansion set of sensors to the Sphero RVR platform.

**Retired**

[![SparkFun Advanced Autonomous Kit for Sphero RVR ](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/0/5/15303-SparkFun_Advanced_Autonomous_Kit_for_Sphero_RVR-01.jpg)](https://www.sparkfun.com/products/15303)

### [SparkFun Advanced Autonomous Kit for Sphero RVR ](https://www.sparkfun.com/products/15303) 

[ KIT-15303 ]

The SparkFun Advanced Autonomous Kit for Sphero RVR provides tools for building a smart robotics platform with distance sensi...

**Retired**

[![Raspberry Pi 3 B+ Starter Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/9/7/15361-Raspberry_Pi_3_B__Starter_Kit-01.jpg)](https://www.sparkfun.com/products/15361)

### [Raspberry Pi 3 B+ Starter Kit](https://www.sparkfun.com/products/15361) 

[ KIT-15361 ]

The Raspberry Pi 3 B+ Starter Kit is a great way to gain a solid introduction to the small, credit-card-sized computer.

**Retired**

(*Some, but not all of our Raspberry Pi kits include a Raspberry Pi. Be sure to double check the **Includes** tab of the associated product page. Additionally, the Sphero RVR kits will include this Pi Servo pHAT.*).

------------------------------------------------------------------------

There are a few additionally accessories that you will need to use your Raspberry Pi.

You will need an **microSD Card, Power Supply, and USB-C Cable (*optional*)** at minimum to run your Raspberry Pi. There are two options for the microSD card, a NOOBS card that comes pre-flashed with the OS need to run your Raspberry Pi or a blank SD card that can be flashed using the files and instructions from the [Raspberry Pi Foundation page](https://www.raspberrypi.org/downloads/raspbian/).

[![microSD Card with Adapter - 32GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/0/2/14832-microSD_Card_with_Adapter_-_32GB__Class_10_-02.jpg)](https://www.sparkfun.com/microsd-card-with-adapter-32gb-class-10.html)

### [microSD Card with Adapter - 32GB (Class 10)](https://www.sparkfun.com/microsd-card-with-adapter-32gb-class-10.html) 

[ COM-14832 ]

This is a class 10 32GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

[\$26.95] [ [\$14.95] ]

[![microSD Card with Adapter - 64GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/0/3/14833-microSD_Card_with_Adapter_-_64GB__Class_10_-02.jpg)](https://www.sparkfun.com/products/14833)

### [microSD Card with Adapter - 64GB (Class 10)](https://www.sparkfun.com/products/14833) 

[ COM-14833 ]

This is a class 10 64GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

**Retired**

[![microSD Card - 16GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/9/4/15051-microSD_Card_-_16GB__Class_10_-01.jpg)](https://www.sparkfun.com/microsd-card-16gb-class-10.html)

### [microSD Card - 16GB (Class 10)](https://www.sparkfun.com/microsd-card-16gb-class-10.html) 

[ COM-15051 ]

This is a class 10 16GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

**Retired**

[![SparkFun Noobs Card for Raspberry Pi (16GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/9/5/15052-SparkFun_Noobs_Card_for_Raspberry_Pi__16GB_-05e.jpg)](https://www.sparkfun.com/sparkfun-noobs-card-for-raspberry-pi-16gb.html)

### [SparkFun Noobs Card for Raspberry Pi (16GB)](https://www.sparkfun.com/sparkfun-noobs-card-for-raspberry-pi-16gb.html) 

[ COM-15052 ]

This is a class 10, 16GB, micro SDHC card that has been pre-installed with the NOOBS operating system for the Raspberry Pi.

**Retired**

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/2/8/13831-01a.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html)

### [Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html) 

[ TOL-13831 ]

This is a high-quality switching \'wall wart\' AC to DC 5.1V 2,500mA USB Micro-B wall power supply manufactured specifically fo...

[ [\$13.95] ]

[![microSD USB Reader](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/5/8/13004-01.jpg)](https://www.sparkfun.com/microsd-usb-reader.html)

### [microSD USB Reader](https://www.sparkfun.com/microsd-usb-reader.html) 

[ COM-13004 ]

This is an awesome little microSD USB reader. Just slide your microSD card into the inside of the USB connector, then stick t...

**Retired**

(*To flash your own SD card, you will also want to grab a [microSD USB adapter](https://www.sparkfun.com/products/13004)*.)

------------------------------------------------------------------------

Last of all, to test the functionality of the Pi Servo pHAT you will want a [**servo motor**](https://www.sparkfun.com/categories/245).

[![Servo - Generic (Sub-Micro Size)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/2/09065-01a.jpg)](https://www.sparkfun.com/servo-generic-sub-micro-size.html)

### [Servo - Generic (Sub-Micro Size)](https://www.sparkfun.com/servo-generic-sub-micro-size.html) 

[ ROB-09065 ]

Here is a simple, low-cost, high quality servo for all your mechatronic needs. This servo is very similar in size and specifi...

[ [\$12.95] ]

[![Servo - Generic High Torque Continuous Rotation (Standard Size)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/1/1/09347-1.jpg)](https://www.sparkfun.com/servo-generic-high-torque-continuous-rotation-standard-size.html)

### [Servo - Generic High Torque Continuous Rotation (Standard Size)](https://www.sparkfun.com/servo-generic-high-torque-continuous-rotation-standard-size.html) 

[ ROB-09347 ]

Here, for all your mechatronic needs, is a simple, high quality continuous rotation servo motor. This servo is able to take i...

[ [\$20.50] ]

[![Servo - Hitec HS-85MG (Micro Size)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/3/1/1/11887-01b.jpg)](https://www.sparkfun.com/servo-hitec-hs-85mg-micro-size.html)

### [Servo - Hitec HS-85MG (Micro Size)](https://www.sparkfun.com/servo-hitec-hs-85mg-micro-size.html) 

[ ROB-11887 ]

The HS-85MG is able to take in 6 volts and deliver 49 oz-in. of maximum torque at 0.14sec/60°, and this guy is only about th...

[ [\$37.50] ]

[![Servo - Generic Metal Gear (Micro Size)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/9/8/14760-Servo_-_Generic_Metal_Gear__Micro_Size_-01.jpg)](https://www.sparkfun.com/servo-generic-metal-gear-micro-size.html)

### [Servo - Generic Metal Gear (Micro Size)](https://www.sparkfun.com/servo-generic-metal-gear-micro-size.html) 

[ ROB-14760 ]

Here is a simple, low-cost, high quality servo for all your mechatronic needs. This servo is able to take in 6 volts and deli...

[ [\$20.95] ]

(*Any \"standard\" 5V servo in our catalog should work. Keep in mind when purchasing, the continuous rotation servos behave differently from the normal servos.*)

------------------------------------------------------------------------

### Required Tools

No tools are required to used this product. However, you may need a soldering iron, solder, and/or general soldering accessories to solder modify the jumpers or solder on headers to your Raspberry Pi board (if it didn\'t come with them).

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

### Suggested Reading

Below are several tutorials and hookup guides covering various topics that we suggest users get familiar with before beginning this hookup guide. As a supplement, the hookup guides for the previous Pi Servo Hat are listed as well.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

### Raspberry Pi SPI and I2C Tutorial 

Learn how to use serial I2C and SPI buses on your Raspberry Pi using the wiringPi I/O library for C/C++ and spidev/smbus for Python.

[](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial)

### Hobby Servo Tutorial 

Servos are motors that allow you to accurately control the rotation of the output shaft, opening up all kinds of possibilities for robotics and other projects.

[](https://learn.sparkfun.com/tutorials/setting-up-the-pi-zero-wireless-pan-tilt-camera)

### Setting Up the Pi Zero Wireless Pan-Tilt Camera 

This tutorial will show you how to assemble, program, and access the Raspberry Pi Zero as a headless wireless pan-tilt camera.

[](https://learn.sparkfun.com/tutorials/pi-servo-hat-hookup-guide)

### Pi Servo Hat Hookup Guide 

This hookup guide will show you how to connect and use the Pi Servo Hat in a project.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless)

### Getting Started with the Raspberry Pi Zero Wireless 

Learn how to setup, configure and use the smallest Raspberry Pi yet, the Raspberry Pi Zero - Wireless.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Pi Servo pHAT also provides a Qwiic connector to take advantage of our new [Qwiic system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the [**Logic Levels**](https://learn.sparkfun.com/tutorials/logic-levels) and [**I^2^C**](https://learn.sparkfun.com/tutorials/i2c) tutorials before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft910&name=Pi+Servo+pHAT+%28v2%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft910 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Pi+Servo+pHAT+%28v2%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft910&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft910&t=Pi+Servo+pHAT+%28v2%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft910&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F9%2F1%2F0%2FAssembly_Servo.gif&description=Pi+Servo+pHAT+%28v2%29+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/hardware-assembly) [Python Package Overview](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/python-package-overview) [Python Examples](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/python-examples) [Python Examples (archived)](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/python-examples-archived) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/all) [Print]

- **Tags**
- - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Prototyping](https://learn.sparkfun.com/tutorials/tags/prototyping)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)
  - [Sphero](https://learn.sparkfun.com/tutorials/tags/sphero)
  - [Start a Project](https://learn.sparkfun.com/tutorials/tags/start-a-project)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]