# Source: https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun Photodetector (MAX30101) Hookup Guide

# SparkFun Photodetector (MAX30101) Hookup Guide

[≡ Pages](#)

Contributors: [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1180&name=SparkFun+Photodetector+%28MAX30101%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1180 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Photodetector+%28MAX30101%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1180&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1180&t=SparkFun+Photodetector+%28MAX30101%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1180&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F8%2F0%2Fassembly_pi4.jpg&description=SparkFun+Photodetector+%28MAX30101%29+Hookup+Guide "Pin It")

## Introduction

The [SparkFun Photodetector - MAX30101 (Qwiic)](https://www.sparkfun.com/products/16474) is the successor to the [MAX30105 particle sensor](https://www.sparkfun.com/products/14045), a highly sensitive optical sensor. This tutorial will get you up and running to retrieve the raw data from the MAX30101 sensor.

[![SparkFun Photodetector Breakout - MAX30101 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/3/3/8/16474-SparkFun_Photodetector_Breakout_-_MAX30101__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-photodetector-breakout-max30101-qwiic.html)

### [SparkFun Photodetector Breakout - MAX30101 (Qwiic)](https://www.sparkfun.com/sparkfun-photodetector-breakout-max30101-qwiic.html) 

[ SEN-16474 ]

The SparkFun Photodetector Breakout is an updated version of the Particle Sensor Breakout including the MAX30101, a highly se...

[ [\$34.39] ]

The MAX30101 includes three LEDs and an optical detector in a single package, which can be utilized as a wearable, biosensor for pulse oximeter and heart-rate measurements. For accurate and reliable biometric readings, we recommend the [SparkFun Pulse Oximeter and Heart Rate Sensor](https://www.sparkfun.com/products/15219), which utilizes proprietary algorithms programmed on the MAX32664 Biometric Sensor Hub. Other possible applications include proximity sensing and particle detection by measuring the changes in light that is reflected back from the LEDs.

[[**☠ WARNING:** Our products are **[NOT]** intended to diagnose or treat any conditions.](https://www.sparkfun.com/terms)]

### Required Materials

The Qwiic Photodetector Sensor does need a few additional items for you to get started. The [RedBoard Qwiic](https://www.sparkfun.com/products/15123) will be used for the Arduino examples. A single board computer and the [Qwiic pHAT](https://www.sparkfun.com/products/15351) are required for the Python examples (see note below). You may already have a few of these items, including the required Qwiic cable, so feel free to modify your cart based on your needs. Additionally, there are also [alternative parts] options that are available as well (*click button below to toggle options*).

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

[![SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/5/8/8/15945-SparkFun_Qwiic_pHAT_V3.0_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-phat-v2-0-for-raspberry-pi.html)

### [SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-phat-v2-0-for-raspberry-pi.html) 

[ DEV-15945 ]

The SparkFun Qwiic pHAT V2 for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and sti...

[ [\$7.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

Qwiic Compatible Microcontrollers:

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

[![SparkFun Qwiic Shield for Arduino Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/7/8/9/16130-SparkFun_Qwiic_Shield_for_Arduino_Nano-01.jpg)](https://www.sparkfun.com/products/16130)

### [SparkFun Qwiic Shield for Arduino Nano](https://www.sparkfun.com/products/16130) 

[ DEV-16130 ]

The SparkFun Qwiic Shield for Arduino Nano makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards...

**Retired**

[![SparkFun Qwiic Shield for Thing Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/7/9/8/16138-SparkFun_Qwiic_Shield_for_Thing_Plus-01.jpg)](https://www.sparkfun.com/products/16138)

### [SparkFun Qwiic Shield for Thing Plus](https://www.sparkfun.com/products/16138) 

[ DEV-16138 ]

The SparkFun Qwiic Shield for Thing Plus makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards t...

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

[![SparkFun Auto pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/0/3/5/16328-SparkFun_Auto_pHAT_for_Raspberry_Pi-01b.jpg)](https://www.sparkfun.com/sparkfun-auto-phat-for-raspberry-pi.html)

### [SparkFun Auto pHAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-auto-phat-for-raspberry-pi.html) 

[ ROB-16328 ]

The Auto pHAT is an all in one package that focuses on quickly adding robot functionality and advanced support to your Raspbe...

[ [\$39.95] ]

[![SparkFun Qwiic pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/9/15351-SparkFun_Qwiic_pHAT_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/products/15351)

### [SparkFun Qwiic pHAT for Raspberry Pi](https://www.sparkfun.com/products/15351) 

[ DEV-15351 ]

The SparkFun Qwiic pHAT for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and still ...

**Retired**

[![SparkFun Top pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/0/0/3/16301-SparkFun_Top_pHAT_for_Raspberry_Pi-01a.jpg)](https://www.sparkfun.com/sparkfun-top-phat-for-raspberry-pi.html)

### [SparkFun Top pHAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-top-phat-for-raspberry-pi.html) 

[ DEV-16301 ]

Feeling Fancy? The SparkFun Top pHAT is the fundamental machine learning add-on for Raspberry Pi or any 2x20 GPIO SBC!

**Retired**

You will also need a Qwiic cable to connect to your MAX30101 (Qwiic), choose a length that suits your needs.

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

**Python Example:** If you don\'t already have them, you will need an SBC (single board computer) such as a [Raspberry Pi](https://www.sparkfun.com/products/14644) and [standard peripherals](https://www.sparkfun.com/categories/398) or [Jetson Nano](https://www.sparkfun.com/products/16271) and [standard peripherals](https://www.sparkfun.com/products/16389). An example setup is listed below.

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

[![NVIDIA Jetson Nano Developer Kit (V3)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/4/6/16271-NVIDIA_Jetson_Nano_Developer_Kit__V3_-01.jpg)](https://www.sparkfun.com/nvidia-jetson-nano-developer-kit-v3.html)

### [NVIDIA Jetson Nano Developer Kit (V3)](https://www.sparkfun.com/nvidia-jetson-nano-developer-kit-v3.html) 

[ DEV-16271 ]

The NVIDIA® Jetson Nano™ Developer Kit V3 delivers the performance to run modern AI workloads at a small form factor, low ...

**Retired**

[![SparkFun DLI Kit (without Jetson Nano)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/6/16389-SparkFun_DLI_Kit__without_Jetson_Nano_-01.jpg)](https://www.sparkfun.com/sparkfun-dli-kit-without-jetson-nano.html)

### [SparkFun DLI Kit (without Jetson Nano)](https://www.sparkfun.com/sparkfun-dli-kit-without-jetson-nano.html) 

[ KIT-16389 ]

With the release of the Jetson Nano Developer Kit (not included), NVIDIA® empowers developers, researchers, students, and ho...

**Retired**

#### [[**Rubber Band**]]

**Note:** For the heart beat plotter examples, users will require a small to medium size rubber band.

[![rubber band in use](https://cdn.sparkfun.com/r/600-200/assets/learn_tutorials/1/1/8/0/rubber_band_use.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/0/rubber_band_use.jpg)

[![rubber band](https://cdn.sparkfun.com/r/220-200/assets/learn_tutorials/1/1/8/0/rubber_band_top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/0/rubber_band_top.jpg)

### Suggested Reading

If you\'re unfamiliar with serial terminals, jumper pads, or I^2^C be sure to checkout some of these foundational tutorials. The MAX30105 is designed for a handful of uses including [Pulse Oximetry](https://en.wikipedia.org/wiki/Pulse_oximetry). If you\'re unfamiliar with optical pulse detection there are some very good application notes from [TI](http://www.ti.com/lit/an/slaa655/slaa655.pdf) and [NXP](http://www.nxp.com/files/32bit/doc/app_note/AN4327.pdf) that have great starter information.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/max30105-particle-and-pulse-ox-sensor-hookup-guide)

### MAX30105 Particle and Pulse Ox Sensor Hookup Guide 

The SparkFun MAX30105 Particle Sensor is a flexible and powerful sensor enabling sensing of distance, heart rate, particle detection, even the blinking of an eye. Get ready. Set. Shine!

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

[](https://learn.sparkfun.com/tutorials/sparkfun-pulse-oximeter-and-heart-rate-monitor-hookup-guide)

### SparkFun Pulse Oximeter and Heart Rate Monitor Hookup Guide 

Find out your oxygen saturation level or check out your heart rate using the MAX30101 biometric sensor and MAX32664 Biometric Hub via I2C!

[](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

### Raspberry Pi SPI and I2C Tutorial 

Learn how to use serial I2C and SPI buses on your Raspberry Pi using the wiringPi I/O library for C/C++ and spidev/smbus for Python.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[](https://learn.sparkfun.com/tutorials/qwiic-phat-for-raspberry-pi-hookup-guide)

### Qwiic pHAT for Raspberry Pi Hookup Guide 

Get started interfacing your Qwiic enabled boards with your Raspberry Pi. The Qwiic pHAT connects the I2C bus (GND, 3.3V, SDA, and SCL) on your Raspberry Pi to an array of Qwiic connectors.

[](https://learn.sparkfun.com/tutorials/working-with-qwiic-on-a-jetson-nano-through-jupyter-notebooks)

### Working with Qwiic on a Jetson Nano through Jupyter Notebooks 

We created a few Jupyter Notebooks to make using our Qwiic boards with your Jetson Nano even easier!

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Qwiic Photodetector utilizes the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials (above) before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

**Note:** First time Raspberry Pi users should also head over to the [Raspberry Pi Foundation website](https://www.raspberrypi.org/help/) and check out their quickstart guides:

- [Blog Post: Getting started with your Raspberry Pi](https://www.raspberrypi.org/blog/getting-started-raspberry-pi/)
- Raspberry Pi Foundation Getting Stared Guides:
  - [Getting started with Raspberry Pi Tutorial](https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started)
  - [Setting up your Raspberry Pi Tutorial](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up)
- MagPi Books and Guides:
  - [Article: Get started with your new Raspberry Pi](https://magpi.raspberrypi.org/articles/get-started-new-raspberry-pi)

  - [The Offical Raspberry Pi Beginner's Book (*December 2017*)](https://magpi.raspberrypi.org/books/beginners-1)

  - [Get Started with Raspberry Pi (*November 2019*)](https://magpi.raspberrypi.org/books/get-started)

  - The Offical Raspberry Pi Beginner's Guide: How to use your new computer

    [1st Edition (*December 2018*)](https://magpi.raspberrypi.org/books/beginners-guide)\
    [2nd Edition (*June 2019*)](https://magpi.raspberrypi.org/books/beginners-guide-2nd-ed)\
    [3rd Edition (*November 2019*)](https://magpi.raspberrypi.org/books/beginners-guide-3rd-ed)

We have also listed a few additional resources for users to familiarize themselves with the Raspberry Pi:

- [Using your Raspberry Pi Tutorial](https://projects.raspberrypi.org/en/projects/raspberry-pi-using)

- [Documentation]:

  [Setup Documentation](https://www.raspberrypi.org/documentation/setup/)\
  [Installation Documentation](https://www.raspberrypi.org/documentation/installation/)\
  [Raspbian Documentation](https://www.raspberrypi.org/documentation/raspbian/)\
  [SD card Documentation](https://www.raspberrypi.org/documentation/installation/sd-cards.md)

**Note:** First time Nvidia Jetson Nano users should also head over to the [Nvidia website](https://developer.nvidia.com/embedded/downloads#?search=Jetson%20Nano) and check out their guides and tutorials:

- [Jetson Nano Product Page](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
- [Support Resources](https://developer.nvidia.com/embedded/community/support-resources)
  - [Jetson Nano Getting Started Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)
    - [Jetson Projects and Learning](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#next)
      - [Jetson Community Projects](https://developer.nvidia.com/embedded/community/jetson-projects)
      - [Forum for Jetson Projects](https://forums.developer.nvidia.com/c/agx-autonomous-machines/jetson-embedded-systems/jetson-projects/78)
  - [Jetson Download Center](https://developer.nvidia.com/embedded/downloads)
    - [Jetson Download Center Archive](https://developer.nvidia.com/embedded/downloads/archive)
  - [Nvidia Jetson Tutorials](https://developer.nvidia.com/embedded/learn/tutorials)
    - [Nvidia Embedded Computing](https://developer.nvidia.com/embedded-computing)
  - [Jetpack Software Documentation](https://docs.nvidia.com/jetson/index.html)
  - [Jetson FAQ](https://developer.nvidia.com/embedded/faq)
  - [Wiki: Nvidia Jetson](https://elinux.org/Jetson)
    - [Wiki: Jetson Nano](https://elinux.org/Jetson_Nano)
  - [Jetson GPIO Python Package](https://github.com/NVIDIA/jetson-gpio)
- [User Manuals]:
  - [Jetson Nano Developer Kit: User Manual](https://developer.download.nvidia.com/embedded/L4T/r32-3-1_Release_v1.0/Jetson_Nano_Developer_Kit_User_Guide.pdf)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1180&name=SparkFun+Photodetector+%28MAX30101%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1180 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Photodetector+%28MAX30101%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1180&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1180&t=SparkFun+Photodetector+%28MAX30101%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1180&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F8%2F0%2Fassembly_pi4.jpg&description=SparkFun+Photodetector+%28MAX30101%29+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/hardware-assembly) [Arduino Library](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/arduino-library) [Arduino Examples](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/arduino-examples) [Python Package](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/python-package) [Python Examples](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/python-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/resources--going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-photodetector-max30101-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Biometrics](https://learn.sparkfun.com/tutorials/tags/biometrics)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [LEDs](https://learn.sparkfun.com/tutorials/tags/leds)
  - [Light](https://learn.sparkfun.com/tutorials/tags/light)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]