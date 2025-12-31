# Source: https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Qwiic Atmospheric Sensor (BME280) Hookup Guide

# Qwiic Atmospheric Sensor (BME280) Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete], [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft929&name=Qwiic+Atmospheric+Sensor+%28BME280%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft929 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Qwiic+Atmospheric+Sensor+%28BME280%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft929&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft929&t=Qwiic+Atmospheric+Sensor+%28BME280%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft929&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F9%2F2%2F9%2FAssembly_Raspberry_Pi.jpg&description=Qwiic+Atmospheric+Sensor+%28BME280%29+Hookup+Guide "Pin It")

## Introduction

The new [Qwiic Atmospheric Sensor (BME280)](https://www.sparkfun.com/products/15440) is an updated board revision of our [Atmospheric Sensor Breakout- BME280](https://www.sparkfun.com/products/13676) to make it Qwiic compatible. The [Qwiic connector system](https://www.sparkfun.com/qwiic) reduces the hassle of interfacing to the sensor via I^2^C, by utilizing polarized cables that are simple to use. The BME280 is great for measuring humidity, temperature, and barometric pressure.

[![SparkFun Atmospheric Sensor Breakout - BME280 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/1/4/15440-SparkFun_Atmospheric_Sensor_Breakout_-_BME280__Qwiic_-04a.jpg)](https://www.sparkfun.com/sparkfun-atmospheric-sensor-breakout-bme280-qwiic.html)

### [SparkFun Atmospheric Sensor Breakout - BME280 (Qwiic)](https://www.sparkfun.com/sparkfun-atmospheric-sensor-breakout-bme280-qwiic.html) 

[ SEN-15440 ]

The SparkFun BME280 Atmospheric Sensor Breakout is an easy way to measure barometric pressure, humidity, and temperature read...

[ [\$16.95] ]

In addition, we now provide a Python library for compatibility with single board computer (SBC) platforms like the [Raspberry Pi boards](https://www.sparkfun.com/categories/395). The Arduino library is shared from the preexisting hardware. The examples below, will demonstrate how to use the [Qwiic Atmospheric Sensor](https://www.sparkfun.com/products/15440) with a [RedBoard Qwiic](https://www.sparkfun.com/products/15123); and a [Raspberry Pi](https://www.sparkfun.com/products/14643) with the [Qwiic pHAT](https://www.sparkfun.com/products/15351) (and additional accessories) utilizing the Qwiic connection system.

Don\'t forget to check out this great video of Rob playing his **sparxophone** thanks to the help of the BME280!

### Required Materials

The Qwiic Atmospheric Sensor does need a few additional items for you to get started. The [RedBoard Qwiic](https://www.sparkfun.com/products/15123) is for the Arduino examples and the [Qwiic pHAT](https://www.sparkfun.com/products/15351) is for the Raspberry Pi example (see note below). You may already have a few of these items, so feel free to modify your cart based on your needs. Additionally, there are also [alternative parts] options that are available as well (*click button below to toggle options*).

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun Qwiic pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/9/15351-SparkFun_Qwiic_pHAT_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/products/15351)

### [SparkFun Qwiic pHAT for Raspberry Pi](https://www.sparkfun.com/products/15351) 

[ DEV-15351 ]

The SparkFun Qwiic pHAT for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and still ...

**Retired**

Qwiic compatible microcontrollers:

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

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

[![SparkFun Thing Plus - ESP32 WROOM](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/9/4/14689-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/products/14689)

### [SparkFun Thing Plus - ESP32 WROOM](https://www.sparkfun.com/products/14689) 

[ WRL-14689 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

**Retired**

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

[![SparkFun Qwiic pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/9/15351-SparkFun_Qwiic_pHAT_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/products/15351)

### [SparkFun Qwiic pHAT for Raspberry Pi](https://www.sparkfun.com/products/15351) 

[ DEV-15351 ]

The SparkFun Qwiic pHAT for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and still ...

**Retired**

You will also need a Qwiic cable to connect to your BME280 Qwiic, choose a length that suits your needs.

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

**Raspberry Pi Example:** If you don\'t already have them, you will need a [Raspberry Pi](https://www.sparkfun.com/products/14644) and [standard peripherals](https://www.sparkfun.com/categories/398). An example setup is listed below. (*This sensor and the Python library have not been tested on the newly released Raspberry Pi 4 because we don\'t carry it in out catalog yet.*)

[![Raspberry Pi 3 B+](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/2/8/14643-Raspberry_Pi_3_B_-02.jpg)](https://www.sparkfun.com/raspberry-pi-3-b.html)

### [Raspberry Pi 3 B+](https://www.sparkfun.com/raspberry-pi-3-b.html) 

[ DEV-14643 ]

The Raspberry Pi 3 B+ is here to provide you with the same Pi as before, but now with gigabit and PoE capable Ethernet!

[ [\$43.50] ]

[![Multimedia Wireless Keyboard](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/2/6/14271-02.jpg)](https://www.sparkfun.com/multimedia-wireless-keyboard.html)

### [Multimedia Wireless Keyboard](https://www.sparkfun.com/multimedia-wireless-keyboard.html) 

[ WIG-14271 ]

With Single-Board Computers (SBCs) on the rise, it is a good idea to have an easy way to interface with them. Operating on a ...

[\$29.95] [ [\$19.95] ]

[![pi-topCEED (Green)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/5/5/14035-03.jpg)](https://www.sparkfun.com/pi-topceed-green.html)

### [pi-topCEED (Green)](https://www.sparkfun.com/pi-topceed-green.html) 

[ KIT-14035 ]

The pi-topCEED is a DIY desktop computer that helps you start learning how to code, create awesome devices and take your know...

**Retired**

[![SparkFun Noobs Card for Raspberry Pi (16GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/9/5/15052-SparkFun_Noobs_Card_for_Raspberry_Pi__16GB_-05e.jpg)](https://www.sparkfun.com/sparkfun-noobs-card-for-raspberry-pi-16gb.html)

### [SparkFun Noobs Card for Raspberry Pi (16GB)](https://www.sparkfun.com/sparkfun-noobs-card-for-raspberry-pi-16gb.html) 

[ COM-15052 ]

This is a class 10, 16GB, micro SDHC card that has been pre-installed with the NOOBS operating system for the Raspberry Pi.

**Retired**

### Suggested Reading

If you\'re unfamiliar with jumper pads, I^2^C, Qwiic, or Python be sure to checkout some of these foundational tutorials. Also included, in this list, are past tutorials involving the BME280 sensor.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

### Raspberry Pi SPI and I2C Tutorial 

Learn how to use serial I2C and SPI buses on your Raspberry Pi using the wiringPi I/O library for C/C++ and spidev/smbus for Python.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[](https://learn.sparkfun.com/tutorials/qwiic-phat-for-raspberry-pi-hookup-guide)

### Qwiic pHAT for Raspberry Pi Hookup Guide 

Get started interfacing your Qwiic enabled boards with your Raspberry Pi. The Qwiic pHAT connects the I2C bus (GND, 3.3V, SDA, and SCL) on your Raspberry Pi to an array of Qwiic connectors.

[](https://learn.sparkfun.com/tutorials/sparkfun-bme280-breakout-hookup-guide)

### SparkFun BME280 Breakout Hookup Guide 

A guide for connecting the BME280 sensor to a microcontroller, and for using the SparkFun Arduino library.

[](https://learn.sparkfun.com/tutorials/ccs811bme280-qwiic-environmental-combo-breakout-hookup-guide)

### CCS811/BME280 (Qwiic) Environmental Combo Breakout Hookup Guide 

Sense various environmental conditions such as temperature, humidity, barometric pressure, eCO2 and tVOCs with the CCS811 and BME280 combo breakout board.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Qwiic Atmospheric Sensor utilizes the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the [**Logic Levels**](https://learn.sparkfun.com/tutorials/logic-levels) and [**I^2^C**](https://learn.sparkfun.com/tutorials/i2c) tutorials before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft929&name=Qwiic+Atmospheric+Sensor+%28BME280%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft929 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Qwiic+Atmospheric+Sensor+%28BME280%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft929&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft929&t=Qwiic+Atmospheric+Sensor+%28BME280%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft929&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F9%2F2%2F9%2FAssembly_Raspberry_Pi.jpg&description=Qwiic+Atmospheric+Sensor+%28BME280%29+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/hardware-assembly) [Arduino Library Overview](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/arduino-library-overview) [Arduino Example Code](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/arduino-example-code) [Python Package Overview](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/python-package-overview) [Python Example Code](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/python-example-code) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/resources--going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Science](https://learn.sparkfun.com/tutorials/tags/science)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)
  - [Weather](https://learn.sparkfun.com/tutorials/tags/weather)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]