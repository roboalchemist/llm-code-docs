# Source: https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi.md

# Using the BMP085/180 with Raspberry Pi or Beaglebone Black

## Overview

Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/693/medium800/raspberry_pi_BMP085_Breadboard_1K.png?1396775391)

The Raspberry Pi and Beaglebone Black include support for Python, which makes it easy to get access to a lot of low-level hardware and software stacks -- USB, TCP/IP, multiple file systems etc. This is a good thing since it means you don't need to wrap your head around all the obscure details that go along with these complex stacks or the implementation details of various serial buses: you can focus on getting your data off your sensor and into your project as quickly as possible. Hurray for abstraction!  
  
Most sensors tend to communicate with other devices based on one of three well-defined mechanisms: **I2C** , **SPI** or good old **analog output**. There are dozens of other serial buses and communication protocols out there (CAN, 1-Wire, etc.), and they all have their strengths and weaknesses, but I2C, SPI and analog cover the overwhelming majority of sensors you're likely to hook up to your development board.  
  
I2C is a particularly useful bus with the for two main reasons:

- It only requires two shared lines: **SCL** for the clock signal, and **SDA** for the bi-direction data transfers.  
- Each I2C device uses a unique 7-bit address, meaning you can have more than 120 unique I2C devices sharing the bus, and you can freely communicate with them one at a time on an as-needed basis.

This tutorial will show you how you can read data from the I2C-based BMP085 or BMP180 Barometric Pressure Sensor using Python on a Raspberry Pi or Beaglebone Black.  
# A Note on Distributions
Please note for the Raspberry Pi that this tutorial is based on [Occidentalis](http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/overview "Link: http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/overview"), Adafruit's own educational Linux distro for Pi. It should work just as well with the latest Wheezy distro, etc., but it hasn't yet been tested on anything else.   
  
For the Beaglebone Black this tutorial is based on the [Debian distribution](http://beagleboard.org/project/debian/) that's shipping with recent Beaglebone Black boards. If you're using an older Beaglebone Black with the Angstrom distribution it's highly recommended that you grab a micro SD card and load it with Debian! - [Next Page](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/configuring-the-pi-for-i2c.md)

## Featured Products

### BMP180 Barometric Pressure/Temperature/Altitude Sensor- 5V ready

[BMP180 Barometric Pressure/Temperature/Altitude Sensor- 5V ready](https://www.adafruit.com/product/1603)
This precision sensor from Bosch is the best low-cost sensing solution for measuring barometric pressure and temperature. Because pressure changes with altitude you can also use it as an altimeter! The sensor is soldered onto a PCB with a 3.3V regulator, I2C level shifter and pull-up resistors...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1603)
[Related Guides to the Product](https://learn.adafruit.com/products/1603/guides)
### Raspberry Pi Model B 512MB RAM

[Raspberry Pi Model B 512MB RAM](https://www.adafruit.com/product/998)
Adafruit ships the **Raspberry Pi Model B 512MB RAM** as of 10/18/2012.  
  
The Raspberry Pi® is a single-board computer developed in the UK by the Raspberry Pi Foundation with the intention of stimulating the teaching of basic computer science in schools. The Raspberry...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/998)
[Related Guides to the Product](https://learn.adafruit.com/products/998/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### BeagleBone Black Rev C - 4GB Flash - Pre-installed Debian

[BeagleBone Black Rev C - 4GB Flash - Pre-installed Debian](https://www.adafruit.com/product/1876)
Note: As of May 12, 2014 Adafruit is shipping Rev C. We have discontinued selling Rev B. There are no exchanges or "upgrades" for Rev B to Rev C.  
  
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C still has a blistering 1GHz processor and 512MB...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1876)
[Related Guides to the Product](https://learn.adafruit.com/products/1876/guides)
### BeagleBone Black Rev C - 4GB - Pre-installed Debian

[BeagleBone Black Rev C - 4GB - Pre-installed Debian](https://www.adafruit.com/product/1996)
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C has a blistering 1GHz AM3358 processor and 512MB onboard DDR3 RAM, two 46-pin headers, micro HDMI for audio/video output, USB ports, 10/100 Ethernet and other I/O features. The Rev C is an ultra-powered embedded...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1996)
[Related Guides to the Product](https://learn.adafruit.com/products/1996/guides)

## Related Guides

- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Modern Replacements for DHT11 and DHT22 Sensors](https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors.md)
- [Adding a Real Time Clock to Raspberry Pi](https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi.md)
- [Adafruit AHT20 Temperature & Humidity Sensor](https://learn.adafruit.com/adafruit-aht20.md)
- [Wood Case for Raspberry Pi 3](https://learn.adafruit.com/wood-case-for-raspberry-pi-3.md)
- [Adafruit DPI Display Kippah](https://learn.adafruit.com/adafruit-dpi-display-kippah-ttl-tft.md)
- [Adafruit's Raspberry Pi Lesson 6. Using SSH](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh.md)
- [3.5" PiTFT OctoPrint Rig](https://learn.adafruit.com/3-dot-5-pitft-octoprint-rig.md)
- [Adafruit TMP117 High Accuracy I2C Temperature Monitor](https://learn.adafruit.com/adafruit-tmp117-high-accuracy-i2c-temperature-monitor.md)
- [Instant Camera using Raspberry Pi and Thermal Printer](https://learn.adafruit.com/instant-camera-using-raspberry-pi-and-thermal-printer.md)
- [User-space SPI TFT Python Library - ILI9341](https://learn.adafruit.com/user-space-spi-tft-python-library-ili9341-2-8.md)
- [USB Audio Cards with a Raspberry Pi ](https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi.md)
- [micro:bit Lesson 4. Sensing Light](https://learn.adafruit.com/micro-bit-lesson-4-sensing-light-and-temperature.md)
- [No-Code Indoor Grow Monitor with PPFD and VPD Measurements](https://learn.adafruit.com/no-code-indoor-grow-monitor.md)
- [PyBadge Thermal Camera Case](https://learn.adafruit.com/pybadge-thermal-camera-case.md)
