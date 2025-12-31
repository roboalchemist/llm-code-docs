# Source: https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi/hooking-everything-up.md

# Source: https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/hooking-everything-up.md

# Using the BMP085/180 with Raspberry Pi or Beaglebone Black

## Hooking Everything Up

Danger: 

# Raspberry Pi
To hook your Adafruit BMP085/BMP180 Breakout up to the Pi, you can use a Pi Cobbler as seen in the following wiring diagram: ![](https://cdn-learn.adafruit.com/assets/assets/000/001/692/medium800/raspberry_pi_BMP085_Breadboard_1K.png?1396775358)

Danger: 

# Beaglebone Black
To connect the BMP sensor to a Beaglebone Black you can use [any of the available I2C buses](http://beagleboard.org/Support/bone101 "Link: http://beagleboard.org/Support/bone101"), but the library will default to using I2C bus 1 with pin P9\_19 as SCL and P9\_20 as SDA as shown below: ![](https://cdn-learn.adafruit.com/assets/assets/000/017/543/medium800/raspberry_pi_bbb_bmp_bb.png?1403127617)

Make sure you aren't using any [device tree overlays](https://learn.adafruit.com/introduction-to-the-beaglebone-black-device-tree/overview "Link: https://learn.adafruit.com/introduction-to-the-beaglebone-black-device-tree/overview") which might interfere with the I2C pins. By default the standard device tree setup of the Debian distribution should expose the I2C bus 1 connections above without any extra work required.

Danger: 

- [Previous Page](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/configuring-the-pi-for-i2c.md)
- [Next Page](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/using-the-adafruit-bmp-python-library.md)

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
  
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C still has a blistering 1GHz processor and 512MB onboard DDR3...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1876)
[Related Guides to the Product](https://learn.adafruit.com/products/1876/guides)
### BeagleBone Black Rev C - 4GB - Pre-installed Debian

[BeagleBone Black Rev C - 4GB - Pre-installed Debian](https://www.adafruit.com/product/1996)
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C has a blistering 1GHz AM3358 processor and 512MB onboard DDR3 RAM, two 46-pin headers, micro HDMI for audio/video output, USB ports, 10/100 Ethernet and other I/O features. The Rev C is an ultra-powered embedded...

In Stock
[Buy Now](https://www.adafruit.com/product/1996)
[Related Guides to the Product](https://learn.adafruit.com/products/1996/guides)

## Related Guides

- [Raspberry Pi radio player with touchscreen](https://learn.adafruit.com/raspberry-pi-radio-player-with-touchscreen.md)
- [Adafruit PiTFT - 2.8" Touchscreen Display for Raspberry Pi](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi.md)
- [AD8495 Analog Output K-Type Thermocouple Amplifier](https://learn.adafruit.com/ad8495-thermocouple-amplifier.md)
- [Temperature and Humidity Sensing in Home Assistant with CircuitPython](https://learn.adafruit.com/temperature-and-humidity-sensing-in-home-assistant-with-circuitpython.md)
- [3D Printed Raspberry Pi A+ Case](https://learn.adafruit.com/3d-printed-raspberry-pi-a-plus-case.md)
- [RGB Matrix Portal Room CO2 Monitor](https://learn.adafruit.com/matrix-portal-room-co2-monitor.md)
- [Adafruit AMG8833 8x8 Thermal Camera Sensor](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor.md)
- [10" Raspberry Pi Desktop](https://learn.adafruit.com/10-raspberry-pi-desktop.md)
- [Networked Thermal Printer using Raspberry Pi and CUPS](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi.md)
- [Raspberry Pi NFC Minecraft Blocks](https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks.md)
- [Processing on the Raspberry Pi & PiTFT](https://learn.adafruit.com/processing-on-the-raspberry-pi-and-pitft.md)
- [Running Programs Automatically on Your Tiny Computer](https://learn.adafruit.com/running-programs-automatically-on-your-tiny-computer.md)
- [DHT Humidity Sensing on Raspberry Pi or Beaglebone Black with GDocs Logging](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.md)
- [Kali Linux on the Raspberry Pi with the PiTFT](https://learn.adafruit.com/kali-linux-on-the-raspberry-pi-with-the-pitft.md)
- [Adafruit SHT31-D Temperature & Humidity Sensor Breakout](https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout.md)
