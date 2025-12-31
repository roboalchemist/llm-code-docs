# Source: https://learn.adafruit.com/send-raspberry-pi-data-to-cosm.md

# Send Raspberry Pi Data to COSM

## Overview

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/350/medium800/raspberry_pi_pi-with-temp-sensor.jpg?1410964052)

The combination of connecting a Raspberry Pi to COSM makes creating a internet of things much easier than it has been in the past. The Pi with it's easy access to ethernet / WiFi and COSM's drop dead simple usability will graph all sensor data you send to it.   
  
This tutorial explains how to connect a analog temperature sensor to the Pi and use a small python script to upload that data for storage and graphing on COSM.

# To follow this tutorial you will need

- [MCP3008 DIP-package ADC converter chip](https://www.adafruit.com/products/856 "Link: https://www.adafruit.com/products/856")  
- [Analog Temperature Sensor TMP-36](http://www.adafruit.com/products/165 "Link: http://www.adafruit.com/products/165")
- [Adafruit Pi Cobbler](https://www.adafruit.com/products/914 "Link: https://www.adafruit.com/products/914") - follow the tutorial to assemble it
- [Half](https://www.adafruit.com/products/64 "Link: https://www.adafruit.com/products/64") or [Full-size breadboard](https://www.adafruit.com/products/239 "Link: https://www.adafruit.com/products/239")
- [Breadboarding wires](https://www.adafruit.com/category/82 "Link: https://www.adafruit.com/category/82")
- Raspberry Pi with a internet connection

_Hey, that photo up there has the GPIO cable in backwards - so when you wire it up don't follow that pic!_  

- [Next Page](https://learn.adafruit.com/send-raspberry-pi-data-to-cosm/connecting-the-cobbler-slash-mcp3008-slash-tmp36.md)

## Featured Products

### MCP3008 - 8-Channel 10-Bit ADC With SPI Interface

[MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://www.adafruit.com/product/856)
Need to add analog inputs? This chip will add 8 channels of 10-bit analog input to your microcontroller or microcomputer project. It's super easy to use and uses SPI so only 4 pins are required. We chose this chip as a great accompaniment to the Raspberry Pi computer because it's fun...

In Stock
[Buy Now](https://www.adafruit.com/product/856)
[Related Guides to the Product](https://learn.adafruit.com/products/856/guides)
### TMP36 - Analog Temperature sensor

[TMP36 - Analog Temperature sensor](https://www.adafruit.com/product/165)
Wide range, low power temperature sensor outputs an analog voltage that is proportional to the ambient temperature. To use, connect pin 1 (left) to power (between 2.7 and 5.5V), pin 3 (right) to ground, and pin 2 to analog in on your microcontroller. The voltage out is 0V at -50°C and...

In Stock
[Buy Now](https://www.adafruit.com/product/165)
[Related Guides to the Product](https://learn.adafruit.com/products/165/guides)
### Full Sized Premium Breadboard - 830 Tie Points

[Full Sized Premium Breadboard - 830 Tie Points](https://www.adafruit.com/product/239)
This is a 'full-size' premium quality breadboard, 830 tie points. Good for small and medium projects. It's 2.2" x 7" (5.5 cm x 17 cm) with a standard double-strip in the middle and two power rails on both sides. You can pull the power rails off easily to make the...

In Stock
[Buy Now](https://www.adafruit.com/product/239)
[Related Guides to the Product](https://learn.adafruit.com/products/239/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### GPIO Ribbon Cable for Raspberry Pi Model A and B - 26 pin

[GPIO Ribbon Cable for Raspberry Pi Model A and B - 26 pin](https://www.adafruit.com/product/862)
That new Raspberry Pi® Model A or B computer you just got has a row of 2x13 pin headers soldered on - those are the GPIO (general purpose input/output) pins and for those of us who like to hack electronics they are where the real fun is. By programming the Pi, you can twiddle those pins...

In Stock
[Buy Now](https://www.adafruit.com/product/862)
[Related Guides to the Product](https://learn.adafruit.com/products/862/guides)
### Adafruit Pi Box -  Enclosure for Raspberry Pi Model A or B

[Adafruit Pi Box -  Enclosure for Raspberry Pi Model A or B](https://www.adafruit.com/product/859)
 **Discontinued** - you can grab&nbsp;[Adafruit Pi Box Plus - Enclosure for RasPi Model B+/Pi 2/ Pi 3](https://www.adafruit.com/product/1985) instead!&nbsp;

**We're still selling this classic Adafruit case for those who specifically want it but <a...></a...>**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/859)
[Related Guides to the Product](https://learn.adafruit.com/products/859/guides)

## Related Guides

- [MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://learn.adafruit.com/mcp3008-spi-adc.md)
- [Skill Badge Requirements: Raspberry Pi](https://learn.adafruit.com/skill-badge-requirements-raspberry-pi.md)
- [PyPortal IoT Plant Monitor with AWS IoT and CircuitPython](https://learn.adafruit.com/pyportal-iot-plant-monitor-with-aws-iot-and-circuitpython.md)
- [Adafruit PMSA003I Air Quality Breakout](https://learn.adafruit.com/pmsa003i.md)
- [10" Raspberry Pi Desktop](https://learn.adafruit.com/10-raspberry-pi-desktop.md)
- [Adafruit BMP388 and BMP390 - Precision Barometric Pressure and Altimeter](https://learn.adafruit.com/adafruit-bmp388-bmp390-bmp3xx.md)
- [Little Desktop Connection Machine](https://learn.adafruit.com/little-connection-machine.md)
- [USB Audio Cards with a Raspberry Pi ](https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi.md)
- [Sparkle Motion Dance Shoes](https://learn.adafruit.com/sparkle-motion-dance-shoes.md)
- [CircuitPython on Raspberry Pi (Bare Metal / No OS)](https://learn.adafruit.com/circuitpython-on-raspberry-pi-bare-metal-no-os.md)
- [Jack-o-Theremin](https://learn.adafruit.com/jack-o-theremin.md)
- [Raspberry Pi Hosting Node-Red](https://learn.adafruit.com/raspberry-pi-hosting-node-red.md)
- [Adafruit's Raspberry Pi Lesson 2. First Time Configuration](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration.md)
- [MPR121 Capacitive Touch Sensor on Raspberry Pi & BeagleBone Black](https://learn.adafruit.com/mpr121-capacitive-touch-sensor-on-raspberry-pi-and-beaglebone-black.md)
- [Using OSC to Communicate with a Raspberry Pi](https://learn.adafruit.com/raspberry-pi-open-sound-control.md)
- [How to Scan and Detect I2C Addresses](https://learn.adafruit.com/scanning-i2c-addresses.md)
