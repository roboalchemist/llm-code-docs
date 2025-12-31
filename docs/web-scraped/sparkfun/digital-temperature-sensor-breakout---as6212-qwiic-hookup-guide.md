# Source: https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Digital Temperature Sensor Breakout - AS6212 (Qwiic) Hookup Guide

# Digital Temperature Sensor Breakout - AS6212 (Qwiic) Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete], [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1989&name=Digital+Temperature+Sensor+Breakout+-+AS6212+%28Qwiic%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1989 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Digital+Temperature+Sensor+Breakout+-+AS6212+%28Qwiic%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1989&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1989&t=Digital+Temperature+Sensor+Breakout+-+AS6212+%28Qwiic%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1989&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F9%2F8%2F9%2FSparkFun_AS6212_Qwiic-Thumb.jpg&description=Digital+Temperature+Sensor+Breakout+-+AS6212+%28Qwiic%29+Hookup+Guide "Pin It")

## Introduction

The [SparkFun Digital Temperature Sensor Breakout - AS6212 (Qwiic)](https://www.sparkfun.com/products/18521) provides a combination of high temperature accuracy with excellent low power consumption using the AS6212 digital temperature sensor from ams AG. The AS6212 measures temperature with ±0.2°C accuracy between -10°C to 65°C (full measurement range is -40°C to 125°C), consumes an average of 6µA (0.1µA in standby) and communicates over I^2^C so naturally we put it on a Qwiic breakout to add to our ever expanding Qwiic system. All of this in a tiny IC package measuring 1.5mm x 1mm.

[![SparkFun Digital Temperature Sensor Breakout - AS6212 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/9/7/0/18521-SparkFun_Digital_Temperature_Sensor_Breakout_-_AS6212__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-breakout-as6212-qwiic.html)

### [SparkFun Digital Temperature Sensor Breakout - AS6212 (Qwiic)](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-breakout-as6212-qwiic.html) 

[ SEN-18521 ]

The AS6212 digital temperature sensor from AMS provides high-accuracy temperature data combined with excellent power consumpt...

[ [\$10.95] ]

### Required Materials

In order to follow along with this tutorial you\'ll need a few items along with the AS6212 breakout.

First off, the Digital Temperature Sensor Breakout - AS6212 (Qwiic) needs a controller like an Arduino development board or single-board computer (SBC) like a Raspberry Pi to communicate with the board. Click the button below to toggle to recommended Raspberry Pi and Qwiic Pi products.

[**Raspberry Pi Materials (Toggle)**]

Below are a few Arduino development boards SparkFun carries that are Qwiic enabled out of the box:

[![SparkFun Qwiic Pro Micro - USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/0/4/15795-Pro_Micro_C-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html)

### [SparkFun Qwiic Pro Micro - USB-C](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html) 

[ DEV-15795 ]

The SparkFun Qwiic Pro Micro adds a reset button, Qwiic connector, USB-C, and castellated pads to the miniaturized Arduino bo...

[ [\$23.95] ]

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

If you would prefer to use the Digital Temperature Sensor Breakout - AS6212 (Qwiic) with Python, control the breakout with a single-board computer like the Raspberry Pi\'s listed below:

[![Raspberry Pi 4 Model B (4 GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/2/2/15447-Raspberry_Pi_4_Model_B__4_GB_-01.jpg)](https://www.sparkfun.com/raspberry-pi-4-model-b-4-gb.html)

### [Raspberry Pi 4 Model B (4 GB)](https://www.sparkfun.com/raspberry-pi-4-model-b-4-gb.html) 

[ DEV-15447 ]

The 4 GB Raspberry Pi 4 features the ability to run two 4k resolution monitors, to run true Gigabit Ethernet operations, all ...

[ [\$64.95] ]

[![Raspberry Pi Zero W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/3/2/14277-01.jpg)](https://www.sparkfun.com/raspberry-pi-zero-w.html)

### [Raspberry Pi Zero W](https://www.sparkfun.com/raspberry-pi-zero-w.html) 

[ DEV-14277 ]

The Raspberry Pi Zero W is still the Pi you know and love, but at a largely reduced size of only 65mm long by 30mm wide and s...

[ [\$16.50] ]

[![Raspberry Pi Zero W (with Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/5/9/15470-Raspberry_Pi_Zero_WH-01.jpg)](https://www.sparkfun.com/raspberry-pi-zero-w-with-headers.html)

### [Raspberry Pi Zero W (with Headers)](https://www.sparkfun.com/raspberry-pi-zero-w-with-headers.html) 

[ DEV-15470 ]

The Raspberry Pi Zero W is still the Pi you know and love, but at a largely reduced size of only 65mm long by 30mm wide and n...

[ [\$17.60] ]

[![SparkFun Raspberry Pi 4 Desktop Kit - 2GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/2/16385-Raspberry_Pi_4_Desktop_Kit_-_2GB-01a.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-2gb.html)

### [SparkFun Raspberry Pi 4 Desktop Kit - 2GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-2gb.html) 

[ KIT-16385 ]

The SparkFun Raspberry Pi 4 Desktop Kit (2GB) includes everything you need to turn any monitor with an HDMI port into a deskt...

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

Along with a development board or SBC, you\'ll need at least one Qwiic cable. SparkFun carries a variety of lengths and types of Qwiic cables as seen here:

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

### Recommended Reading

In case you are not familiar with the Qwiic System, we recommend reading [here](https://www.sparkfun.com/qwiic) for an overview:

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend taking a look at the following tutorials if you aren\'t familiar with the concepts covered in them:

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

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1989&name=Digital+Temperature+Sensor+Breakout+-+AS6212+%28Qwiic%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1989 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Digital+Temperature+Sensor+Breakout+-+AS6212+%28Qwiic%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1989&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1989&t=Digital+Temperature+Sensor+Breakout+-+AS6212+%28Qwiic%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1989&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F9%2F8%2F9%2FSparkFun_AS6212_Qwiic-Thumb.jpg&description=Digital+Temperature+Sensor+Breakout+-+AS6212+%28Qwiic%29+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/hardware-assembly) [Qwiic AS6212 Arduino Library](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/qwiic-as6212-arduino-library) [Arduino Examples](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/arduino-examples) [Qwiic AS6212 Python Package](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/qwiic-as6212-python-package) [Python Examples](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/python-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/digital-temperature-sensor-breakout---as6212-qwiic-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Weather](https://learn.sparkfun.com/tutorials/tags/weather)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]