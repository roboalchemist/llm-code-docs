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
- [Adafruit MAX31856 Universal Thermocouple Amplifier](https://learn.adafruit.com/adafruit-max31856-thermocouple-amplifier.md)
- [Adafruit Swirly Aluminum Mounting Grid for 0.1" Spaced PCBs](https://learn.adafruit.com/swirly-grid.md)
- [Capacitive Touch with Conductive Fabric & Flora](https://learn.adafruit.com/capacitive-touch-with-conductive-fabric-and-flora.md)
- [Raspberry Pi Wifi-Controlled Cat Laser Toy](https://learn.adafruit.com/raspberry-pi-wifi-controlled-cat-laser-toy.md)
- [Adafruit's Raspberry Pi Lesson 6. Using SSH](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh.md)
- [Piezo Ring Tones with Raspberry Pi](https://learn.adafruit.com/piezo-ring-tones-with-raspberry-pi.md)
- [LED Backpack Displays on Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/led-backpack-displays-on-raspberry-pi-and-beaglebone-black.md)
- [Bluetooth LE MIDI Controller](https://learn.adafruit.com/bluetooth-le-midi-controller.md)
- [MCP9808 Temperature Sensor Python Library](https://learn.adafruit.com/mcp9808-temperature-sensor-python-library.md)
- [ulab: Crunch Numbers fast in CircuitPython](https://learn.adafruit.com/ulab-crunch-numbers-fast-with-circuitpython.md)
- [Using MPL3115A2 with CircuitPython](https://learn.adafruit.com/using-mpl3115a2-with-circuitpython.md)
- [Pi-Top Assembly ](https://learn.adafruit.com/pi-top-assembly.md)
- [Goose Game M4SK Controller](https://learn.adafruit.com/goose-game-m4sk-controller.md)
- [Bluefruit Playground App](https://learn.adafruit.com/bluefruit-playground-app.md)
- [Raspberry Pi SelfieBlock](https://learn.adafruit.com/selfieblock.md)
