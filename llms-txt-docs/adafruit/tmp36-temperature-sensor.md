# Source: https://learn.adafruit.com/tmp36-temperature-sensor.md

# TMP36 Temperature Sensor

## Overview

An analog temperature sensor is pretty easy to explain, its a chip that tells you what the ambient temperature is!![](https://cdn-learn.adafruit.com/assets/assets/000/035/444/medium800/temperature_165-00.jpg?1473013495)

These sensors use a solid-state technique to determine the temperature. That is to say, they don't use mercury (like old thermometers),&nbsp;[bimetalic strips](http://en.wikipedia.org/wiki/Bimetallic_strip)&nbsp;(like in some home thermometers or stoves), nor do they use&nbsp;[thermistors&nbsp;](http://en.wikipedia.org/wiki/Thermistor)(temperature sensitive resistors). Instead, they use the fact as temperature increases, the voltage across a diode increases at a known rate. (Technically, this is actually the voltage drop between the base and emitter - the Vbe - of a transistor.) By precisely amplifying the voltage change, it is easy to generate an analog signal that is directly proportional to temperature. There have been some improvements on the technique but, essentially that is how temperature is measured.

The good news is all that complex calculation is done _inside_ the chip - it just spits out the temperature, ready for you to use!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/471/medium800/temperature_tmp36pinout.gif?1447975787)

Because these sensors have no moving parts, they are precise, never wear out, don't need calibration, work under many environmental conditions, and are consistant between sensors and readings. Moreover they are very inexpensive and quite easy to use.

## Some Basic Stats

These stats are for the temperature sensor in the Adafruit shop, the [Analog Devices TMP36](http://learn.adafruit.com/system/assets/assets/000/010/131/original/TMP35_36_37.pdf) (-40 to 150C).

It's very similar to the LM35/TMP35 (Celsius output, min 4v power) and LM34/TMP34 (Fahrenheit output). The reason we went with the '36 instead of the '35 or '34 is that this sensor has a very wide range and doesn't require a negative voltage to read sub-zero temperatures. Otherwise, the functionality is basically the same.

- **Size:** TO-92 package (about 0.2" x 0.2" x 0.2") with three leads
- **Price:** [$1.50 at the Adafruit shop](http://www.adafruit.com/index.php?main_page=product_info&cPath=35&products_id=165)
- **Temperature range:** -40°C to 150°C / -40°F to 302°F
- **Output range:** 0.1V (-40°C) to 2.0V (150°C) but accuracy decreases after 125°C
- **Power supply:** 2.7V to 5.5V only, 0.05 mA current draw
- **[Datasheet](http://learn.adafruit.com/system/assets/assets/000/010/131/original/TMP35_36_37.pdf)**

## How to Measure Temperature

Using the TMP36 is easy, simply connect the left pin to power (2.7-5.5V) and the right pin to ground. Then the middle pin will have an analog voltage that is directly proportional (linear) to the temperature. The analog voltage is independent of the power supply.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/472/medium800/temperature_tmp36graph.gif?1447975797)

To convert the voltage to temperature, simply use the basic formula:

**Temp in °C = [(Vout in mV) - 500**] **&nbsp;/ 10**

So for example, if the voltage out is 1V that means that the temperature is&nbsp;**((1000 mV - 500) / 10) = 50 °C**

If you're using a LM35 or similar, use line 'a' in the image above and the formula:&nbsp;**Temp in °C = (Vout in mV)****&nbsp;/ 10**

## Problems you may encounter with multiple sensors:
If, when adding more sensors, you find that the temperature is inconsistant, this indicates that the sensors are interfering with each other when switching the analog reading circuit from one pin to the other. You can fix this by doing two delayed readings and tossing out the first one  

[See this post for more information](http://www.adafruit.com/blog/2010/01/29/how-to-multiplex-analog-readings-what-can-go-wrong-with-high-impedance-sensors-and-how-to-fix-it/)

- [Next Page](https://learn.adafruit.com/tmp36-temperature-sensor/testing-a-temp-sensor.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### TMP36 - Analog Temperature sensor

[TMP36 - Analog Temperature sensor](https://www.adafruit.com/product/165)
Wide range, low power temperature sensor outputs an analog voltage that is proportional to the ambient temperature. To use, connect pin 1 (left) to power (between 2.7 and 5.5V), pin 3 (right) to ground, and pin 2 to analog in on your microcontroller. The voltage out is 0V at -50°C and...

In Stock
[Buy Now](https://www.adafruit.com/product/165)
[Related Guides to the Product](https://learn.adafruit.com/products/165/guides)

## Related Guides

- [All About Arduino Libraries](https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use.md)
- [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield.md)
- [DS1307 Real Time Clock Breakout Board Kit](https://learn.adafruit.com/ds1307-real-time-clock-breakout-board-kit.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Track Your Treats: Halloween Candy GPS Tracker](https://learn.adafruit.com/track-your-treats-halloween-candy-gps-tracker.md)
- [Arduino Lesson 10. Making Sounds](https://learn.adafruit.com/adafruit-arduino-lesson-10-making-sounds.md)
- [Adafruit Analog Accelerometer Breakouts](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts.md)
- [Adafruit VS1053 MP3/AAC/Ogg/MIDI/WAV Codec Breakout Tutorial](https://learn.adafruit.com/adafruit-vs1053-mp3-aac-ogg-midi-wav-play-and-record-codec-tutorial.md)
- [Ladyada's Learn Arduino - Lesson #1](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-1.md)
- [Adafruit Proto Screw Shield](https://learn.adafruit.com/adafruit-proto-screw-shield.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Arduino Lesson 7. Make an RGB LED Fader](https://learn.adafruit.com/adafruit-arduino-lesson-7-make-an-rgb-led-fader.md)
- [Trainable Robotic Arm](https://learn.adafruit.com/trainable-robotic-arm.md)
- [Adafruit Arduino Selection Guide](https://learn.adafruit.com/adafruit-arduino-selection-guide.md)
