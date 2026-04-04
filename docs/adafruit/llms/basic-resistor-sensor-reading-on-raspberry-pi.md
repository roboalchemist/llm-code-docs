# Source: https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md

# Basic Resistor Sensor Reading on Raspberry Pi

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/001/320/medium800/raspberry_pi_shade.jpg?1396770987)

We've already covered how to use an Analog-to-Digital Converter chip with a Pi. These chips are the best way to read analog voltages from the Pi. However, there's a way to read many sensors&nbsp; **without** an ADC! By measuring the sensor as a resistor that is used to 'fill up' a capacitor, we can count how long it takes. It's not nearly as precise as an ADC and its a little flakey (since it depends on the Pi timing&nbsp;itself which can vary based on how 'busy' the computer is)  
  
The way we do this is by taking advantage of a basic electronic property of resistors and capacitors. It turns out that if you take a capacitor that is initially storing no voltage, and then connect it to power (like 3.3V) through a resistor, it will charge up to the power voltage slowly. The bigger the resistor, the slower it is.&nbsp;  
  
This technique only works with sensors that act like resistors. however, there are quite a few fun sensors that act this way: [photocells](http://adafruit.com/products/161 "Link: http://adafruit.com/products/161"), [thermistors (temperature sensors)](http://adafruit.com/products/372 "Link: http://adafruit.com/products/372"), [flex sensors](http://adafruit.com/products/182 "Link: http://adafruit.com/products/182"),[force-sensitive resistors](http://adafruit.com/products/166 "Link: http://adafruit.com/products/166"), and many more.  
  
It cannot be used with sensors that have a pure analog output like [IR distance sensors](http://www.adafruit.com/products/164) or [analog&nbsp;accelerometers](http://www.adafruit.com/products/163).

- [Next Page](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/how-it-works.md)

## Featured Products

### Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM

[Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM](https://www.adafruit.com/product/3775)
The Raspberry Pi 3 Model B is the most popular Raspberry Pi computer made, and the Pi Foundation knows you can always make a good thing _better_! And what could make the Pi 3 better? How about a&nbsp;_faster_ processor, 5 GHz WiFi, and updated Ethernet chip with PoE capability?...

In Stock
[Buy Now](https://www.adafruit.com/product/3775)
[Related Guides to the Product](https://learn.adafruit.com/products/3775/guides)
### Photo cell (CdS photoresistor)

[Photo cell (CdS photoresistor)](https://www.adafruit.com/product/161)
CdS cells are little light sensors. As the squiggly face is exposed to more light, the resistance goes down. When it's light, the resistance is about ~1KΩ, when dark it goes up to ~10KΩ.

To use, connect one side of the photocell (either one, it's symmetric) to power...

In Stock
[Buy Now](https://www.adafruit.com/product/161)
[Related Guides to the Product](https://learn.adafruit.com/products/161/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### Assembled Pi Cobbler Plus - Breakout Cable

[Assembled Pi Cobbler Plus - Breakout Cable](https://www.adafruit.com/product/2029)
The Raspberry Pi B+ / Pi 2 / Pi 3 / Pi 4&nbsp;has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit card sized bomb of DIY joy. And while you can use most of our great Model B accessories by hooking up our [downgrade...](https://www.adafruit.com/product/1986)

In Stock
[Buy Now](https://www.adafruit.com/product/2029)
[Related Guides to the Product](https://learn.adafruit.com/products/2029/guides)
### Assembled Pi T-Cobbler Plus - GPIO Breakout

[Assembled Pi T-Cobbler Plus - GPIO Breakout](https://www.adafruit.com/product/2028)
 **This is the assembled version of the Pi T-Cobbler Plus. &nbsp;It only works with the Raspberry Pi Model Zero, A+, B+, Pi 2, Pi 3 & Pi 4!** (Any Pi with 2x20 connector)  
  
The Raspberry Pi has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit...

In Stock
[Buy Now](https://www.adafruit.com/product/2028)
[Related Guides to the Product](https://learn.adafruit.com/products/2028/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### Long Flex sensor

[Long Flex sensor](https://www.adafruit.com/product/182)
This sensor can detect flexing or bending in one direction. They were popularized by being used in the Nintendo PowerGlove as a gaming interface.  
  
These sensors are easy to use, they are basically resistors that change value based on how much they're&nbsp;flexed. If they're...

In Stock
[Buy Now](https://www.adafruit.com/product/182)
[Related Guides to the Product](https://learn.adafruit.com/products/182/guides)
### Round Force-Sensitive Resistor (FSR) -  0.3 ~ 10 Newton Force

[Round Force-Sensitive Resistor (FSR) -  0.3 ~ 10 Newton Force](https://www.adafruit.com/product/166)
FSRs are sensors that allow you to detect physical pressure, squeezing and weight. They are simple to use and low cost. This sensor is an Alpha MF01A-N-221-A01&nbsp;with 1/2 diameter sensing region.

We used to stock the Interlink model 402 FSR - the Alpha version is almost half the price...

In Stock
[Buy Now](https://www.adafruit.com/product/166)
[Related Guides to the Product](https://learn.adafruit.com/products/166/guides)

## Related Guides

- [Circadian Pi Desk Light](https://learn.adafruit.com/circadian-pi-desk-light.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [LoRa and LoRaWAN Radio for Raspberry Pi](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 4. GPIO Setup](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup.md)
- [CircuitPython Libraries on Linux and Google Coral](https://learn.adafruit.com/circuitpython-on-google-coral-linux-blinka.md)
- [Adafruit AMG8833 8x8 Thermal Camera Sensor](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor.md)
- [Adafruit's Raspberry Pi Lesson 13. Power Control](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-13-power-control.md)
- [Adafruit's Raspberry Pi Lesson 12. Sensing Movement](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Windows IoT Core Application Development: Headless Blinky](https://learn.adafruit.com/windows-iot-application-development-headless-application.md)
- [Adding Basic Audio Ouput to Raspberry Pi Zero](https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero.md)
- [Drive a 16x2 LCD with the Raspberry Pi](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi.md)
- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [Diet Raspberry Pi](https://learn.adafruit.com/diet-raspberry-pi.md)
