# Source: https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Qwiic Distance Sensor (VL53L1X, VL53L4CD) Hookup Guide

# Qwiic Distance Sensor (VL53L1X, VL53L4CD) Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/814545d7cad2a95dda668529c61c99d0?d=retro&s=20&r=pg) bboyho], [![](https://cdn.sparkfun.com/avatar/5c320824995fcd6990beaf7a3d3f6037?d=retro&s=20&r=pg) Elias The Sparkiest], [![](https://cdn.sparkfun.com/avatar/fde91fc929973498fdcfcfc9ccb086ab?d=retro&s=20&r=pg) Englandsaurus]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft784&name=Qwiic+Distance+Sensor+%28VL53L1X%2C+VL53L4CD%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft784 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Qwiic+Distance+Sensor+%28VL53L1X%2C+VL53L4CD%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft784&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft784&t=Qwiic+Distance+Sensor+%28VL53L1X%2C+VL53L4CD%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft784&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F7%2F8%2F4%2FSparkFun_Qwiic_Distance_Sensor_VL53L4CD_VL53L1X.gif&description=Qwiic+Distance+Sensor+%28VL53L1X%2C+VL53L4CD%29+Hookup+Guide "Pin It")

## Introduction

**Note:** This tutorial was originally written for the Qwiic Distance Sensor - VL53L1X. The Qwiic Distance Sensor - VL53L4CD is a cousin of the VL53L1X. Overall, the sensor functions the same except for a few differences in the specifications. We have included the VL53L4CD in this tutorial. If you are looking for a copy of the original tutorial, we recommend looking at the [Qwiic Distance Sensor VL53L1X Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-hookup-guide).

------------------------------------------------------------------------

The [VL53L1X](https://www.sparkfun.com/products/14722) and [VL53L4CD](https://www.sparkfun.com/products/14722) are Time Of Flight (ToF) sensors. Both uses a VCSEL (vertical cavity surface emitting laser) to emit a [class 1](http://en.wikipedia.org/wiki/Laser_safety#Class_1) IR laser (940 nm) and time the reflection to the target. (You can't see the laser but cell phones can) What does all this mean? You can measure the distance to an object up to 4 meters away with millimeter resolution using the VL53L1X and up to 1.3 meters away with 1 millimeter resolution using the VL53L4CD! That's pretty incredible.

[![SparkFun Distance Sensor Breakout - 4 Meter, VL53L1X (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/9/4/8/14722-SparkFun_Distance_Sensor_Breakout-_4_Meter__VL53L1X__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-distance-sensor-breakout-4-meter-vl53l1x-qwiic.html)

### [SparkFun Distance Sensor Breakout - 4 Meter, VL53L1X (Qwiic)](https://www.sparkfun.com/sparkfun-distance-sensor-breakout-4-meter-vl53l1x-qwiic.html) 

[ SEN-14722 ]

This SparkFun Distance Sensor Breakout utilizes the VL53L1X next generation ToF sensor module to give you the highly accurate...

[ [\$29.95] ]

[![SparkFun Distance Sensor - 1.3 Meter, VL53L4CD (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/5/7/2/18993-SparkFun_Distance_Sensor_-_1.3_Meter__VL53L4CD__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-distance-sensor-1-3-meter-vl53l4cd-qwiic.html)

### [SparkFun Distance Sensor - 1.3 Meter, VL53L4CD (Qwiic)](https://www.sparkfun.com/sparkfun-distance-sensor-1-3-meter-vl53l4cd-qwiic.html) 

[ SEN-18993 ]

This SparkFun Distance Sensor Breakout utilizes the VL53L4CD next generation ToF sensor module to give you the highly accurat...

[ [\$22.45] ]

We've found the precision of the VL53L1X sensor to be 1mm but the accuracy is around ±5mm. The minimum read distance of this sensor is 4cm (or 40mm). For the VL53L4CD sensor, we\'ve to also found the precision to be 1mm but the accuracy is around ±7mm. The minimum read distance of this sensor is 1cm (or 10mm). In this hookup guide, we\'ll go over how to read distance, change ranging modes, and check the status of our range measurement along with the sample rate. We\'ll also check out how to display distance and speed over an LCD display.

### Required Materials

The Qwiic Distance Sensor does need a few additional items for you to get started. The [RedBoard Plus](https://www.sparkfun.com/products/18158) is for the Arduino examples and the [Qwiic SHIM](https://www.sparkfun.com/products/15794) is for the Raspberry Pi example (see note below). You may already have a few of these items, so feel free to modify your cart based on your needs. Additionally, there are also [alternative parts] options that are available as well (*click button below to toggle options*).

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![SparkFun Qwiic SHIM for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/3/9/9/16385-15794-SparkFun_Qwiic_SHIM_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html)

### [SparkFun Qwiic SHIM for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html) 

[ DEV-15794 ]

The SparkFun Qwiic SHIM for Raspberry Pi is a small, easily removable breakout that easily adds a Qwiic connector to your Ras...

[ [\$1.95] ]

Qwiic compatible microcontrollers:

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![SparkFun Thing Plus - SAMD51](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/2/7/14713-SparkFun_Thing_Plus_-_SAMD51-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html)

### [SparkFun Thing Plus - SAMD51](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html) 

[ DEV-14713 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun SAMD51 Thing Plus is one of our most powerful microcontroller boards yet!

[ [\$25.50] ]

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

In addition we also offer, Qwiic compatible stackable shields for microcontrollers and pHATs for single board computers (like the [Raspberry Pi boards](https://www.sparkfun.com/categories/395)) that don\'t include a Qwiic connector.

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

[![SparkFun Qwiic Shield for Photon](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/2/6/14477-01.jpg)](https://www.sparkfun.com/products/14477)

### [SparkFun Qwiic Shield for Photon](https://www.sparkfun.com/products/14477) 

[ DEV-14477 ]

The SparkFun Qwiic Shield for Photon is an easy-to-assemble board that provides a simple way to incorporate the Qwiic System ...

**Retired**

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

You will also need a Qwiic cable to connect to your Qwiic Distance Sensor, choose a length that suits your needs.

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

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

[**Alternative Parts (Toggle)**]

**Raspberry Pi Example:** If you don\'t already have them, you will need a [Raspberry Pi](https://www.sparkfun.com/products/14644) and [standard peripherals](https://www.sparkfun.com/categories/398). An example setup is listed below. (*The Qwiic Distance Sensor and Python library have not been tested on the newly released Raspberry Pi 4 because we don\'t carry it in out catalog yet.*)

### Suggested Reading

If you\'re unfamiliar with jumper pads, I^2^C, Qwiic, or Python be sure to checkout some of these foundational tutorials.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

### Raspberry Pi SPI and I2C Tutorial 

Learn how to use serial I2C and SPI buses on your Raspberry Pi using the wiringPi I/O library for C/C++ and spidev/smbus for Python.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[](https://learn.sparkfun.com/tutorials/qwiic-phat-for-raspberry-pi-hookup-guide)

### Qwiic pHAT for Raspberry Pi Hookup Guide 

Get started interfacing your Qwiic enabled boards with your Raspberry Pi. The Qwiic pHAT connects the I2C bus (GND, 3.3V, SDA, and SCL) on your Raspberry Pi to an array of Qwiic connectors.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

[](https://learn.sparkfun.com/tutorials/redboard-plus-hookup-guide)

### RedBoard Plus Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Plus. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Qwiic Distance Sensor is intended for the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the [**Logic Levels**](https://learn.sparkfun.com/tutorials/logic-levels) and [**I^2^C**](https://learn.sparkfun.com/tutorials/i2c) tutorials before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft784&name=Qwiic+Distance+Sensor+%28VL53L1X%2C+VL53L4CD%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft784 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Qwiic+Distance+Sensor+%28VL53L1X%2C+VL53L4CD%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft784&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft784&t=Qwiic+Distance+Sensor+%28VL53L1X%2C+VL53L4CD%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft784&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F7%2F8%2F4%2FSparkFun_Qwiic_Distance_Sensor_VL53L4CD_VL53L1X.gif&description=Qwiic+Distance+Sensor+%28VL53L1X%2C+VL53L4CD%29+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/hardware-assembly) [Arduino Library Overview](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/arduino-library-overview) [Arduino Example Code](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/arduino-example-code) [Python Package Overview](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/python-package-overview) [Python Examples](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/python-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/resources-and-going-further)

[Comments [7]](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-vl53l1x-vl53l4cd-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Prototyping](https://learn.sparkfun.com/tutorials/tags/prototyping)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]