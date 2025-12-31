# Source: https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Air Quality Sensor - SGP40 (Qwiic) Hookup Guide

# Air Quality Sensor - SGP40 (Qwiic) Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino], [ MAKIN-STUFF]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1792&name=Air+Quality+Sensor+-+SGP40+%28Qwiic%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1792 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Air+Quality+Sensor+-+SGP40+%28Qwiic%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1792&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1792&t=Air+Quality+Sensor+-+SGP40+%28Qwiic%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1792&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F7%2F9%2F2%2FQwiic_SGP40-Thumbnail.jpg&description=Air+Quality+Sensor+-+SGP40+%28Qwiic%29+Hookup+Guide "Pin It")

## Introduction

The [SparkFun Air Quality Sensor - SGP40 (Qwiic)](https://www.sparkfun.com/products/18345) is a robust metal oxide (MOx) based indoor air-quality measurement tool using the SGP40 gas sensor from Sensirion. The SGP40 is based on Sensirion\'s CMOSens^®^ technology that uses a MOx sensor with a temperature controlled micro hotplate and a humidity-compensated indoor air quality signal. The SGP40 is highly responsive and reports valid volatile organic compount (VOC) data within minutes of powering on the sensor.

[![SparkFun Air Quality Sensor - SGP40 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/6/8/0/18345-SparkFun_Air_Quality_Sensor_Breakout_-_SGP40__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-air-quality-sensor-sgp40-qwiic.html)

### [SparkFun Air Quality Sensor - SGP40 (Qwiic)](https://www.sparkfun.com/sparkfun-air-quality-sensor-sgp40-qwiic.html) 

[ SEN-18345 ]

The SparkFun SGP40 Air Quality Sensor provides a measurement of the quality of the air in your room or house.

[ [\$18.95] ]

The SGP40 outputs a digital value based on all VOC gases typically present in an indoor environment and this value can be combined with Sensirion\'s VOC Index Algorithm to provide responsive indoor air quality data. The SGP40 detects the relative intensity of VOC events in relation to the average readings in a 24hr period but does not return specific concentrations of VOC gases. Think of the SGP40 as a sensitive electronic nose for detecting VOCs in a room.

Users looking to measure specific gas concentrations may want to use the [SparkFun Air Quality Sensor - SGP30 (Qwiic)](https://www.sparkfun.com/products/16531) instead.

This guide will cover the SGP40 sensor and other hardware present on this breakout, how to connect it to a microcontroller and use the Arduino and Python libraries so by the end you\'ll be able to easily monitor VOC events indoors.

### Required Materials

To follow along with this guide you will need a microcontroller to communicate with the SGP40. Below are a few options that come Qwiic-enabled out of the box:

[![SparkFun Qwiic Pro Micro - USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/0/4/15795-Pro_Micro_C-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html)

### [SparkFun Qwiic Pro Micro - USB-C](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html) 

[ DEV-15795 ]

The SparkFun Qwiic Pro Micro adds a reset button, Qwiic connector, USB-C, and castellated pads to the miniaturized Arduino bo...

[ [\$23.95] ]

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

If your chosen microcontroller is not already Qwiic-enabled, you can add that functionality with one or more of the following items:

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

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

You will also need at least one Qwiic cable to connect your sensor to your microcontroller.

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

### Suggested Reading

If you aren\'t familiar with the Qwiic system, take a look [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend taking a look at the following tutorials if you aren\'t familiar with the concepts covered in them. If you are using one of the Qwiic Shields listed above, you may want to read through their respective Hookup Guides as well before you get started with the SparkFun Air Quality Sensor - SGP40 (Qwiic).

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

[](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-shield-for-arduino-nano-hookup-guide)

### SparkFun Qwiic Shield for Arduino Nano Hookup Guide 

Hookup Guide for the SparkFun Qwiic Shield for Arduino Nano.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1792&name=Air+Quality+Sensor+-+SGP40+%28Qwiic%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1792 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Air+Quality+Sensor+-+SGP40+%28Qwiic%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1792&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1792&t=Air+Quality+Sensor+-+SGP40+%28Qwiic%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1792&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F7%2F9%2F2%2FQwiic_SGP40-Thumbnail.jpg&description=Air+Quality+Sensor+-+SGP40+%28Qwiic%29+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/hardware-assembly) [SGP40 Arduino Library](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/sgp40-arduino-library) [Arduino Example](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/arduino-example) [SGP40 Python Package](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/sgp40-python-package) [Python Example](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/python-example) [Troubleshooting](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/air-quality-sensor---sgp40-qwiic-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]