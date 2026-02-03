# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout.md

# Adafruit INA219 Current Sensor Breakout

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/104/390/medium800/adafruit_products_INA219_top.jpg?1631046311)

The&nbsp;INA219B&nbsp;breakout board and the INA219 FeatherWing will solve all your power-monitoring problems. Instead of struggling with two multimeters, you can use this breakout to measure both the high side voltage and DC current draw over I2C with 1% precision.&nbsp;

![](https://cdn-learn.adafruit.com/assets/assets/000/104/389/medium800/adafruit_products_INA219_top_header.jpg?1631046301)

As if that weren't enough, we've now also added[&nbsp;SparkFun qwiic](https://www.sparkfun.com/qwiic)&nbsp;compatible&nbsp;**[STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt)**&nbsp;connectors for the I2C bus **so you don't even need to solder the I2C and power lines.**

Just wire up to your favorite micro using a [STEMMA QT adapter cable.](https://www.adafruit.com/?q=stemma%20qt%20cable)&nbsp;The Stemma QT connectors also mean the INA219 can be used with our&nbsp;[various associated accessories.](https://www.adafruit.com/?q=JST%20SH%204)&nbsp;[QT Cable is not included, but we have a variety in the shop](https://www.adafruit.com/?q=stemma+qt+cable&sort=BestMatch).

![](https://cdn-learn.adafruit.com/assets/assets/000/104/391/medium800/adafruit_products_INA219_STEMMA_side.jpg?1631047192)

## Why the High Side?
Most current-measuring devices such as our current panel meter are only good for&nbsp;_low side_&nbsp;measuring. That means that unless you want to get a battery involved, you have to stick the measurement resistor between the target ground and true ground.   
  
Since the voltage drop across the resistor is proportional to the current draw, this means that the ground reference will change with varying current. &nbsp;Having a shifting ground reference can cause problems for many circuits.&nbsp;  
  
The&nbsp;INA219B&nbsp;chip is much smarter - it can handle high side current measuring, up to +26VDC, even though it is powered with 3 or 5V. It will also report back that high side voltage, which is great for tracking battery life or solar panels.&nbsp;  
![](https://cdn-learn.adafruit.com/assets/assets/000/071/472/medium800/adafruit_products_INA219_FeatherWing_Product.jpg?1550609735)

## How does it work?

A precision amplifier measures the voltage across the 0.1 ohm, 1% sense resistor.

Since the amplifier maximum input difference is ±320mV this means it can measure up to ±3.2 Amps. With the internal 12 bit ADC, the resolution at ±3.2A range is 0.8mA. With the internal gain set at the minimum of div8, the max current is ±400mA and the resolution is 0.1mA. Advanced hackers can remove the 0.1 ohm current sense resistor and replace it with their own to change the range (say a 0.01 ohm to measure up 32 Amps with a resolution of 8mA)&nbsp;

Danger: 

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/452/medium800/adafruit_products_ID904_LRG.jpg?1396783275)

- [Next Page](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/pinouts.md)

## Featured Products

### INA219  High Side DC Current Sensor Breakout - 26V ±3.2A Max

[INA219  High Side DC Current Sensor Breakout - 26V ±3.2A Max](https://www.adafruit.com/product/904)
This breakout board will solve all your power-monitoring problems. Instead of struggling with two multimeters, you can just use the handy INA219 chip on this breakout to both measure both the high side voltage and DC current draw over I2C with ±1% precision.

**Please...**

In Stock
[Buy Now](https://www.adafruit.com/product/904)
[Related Guides to the Product](https://learn.adafruit.com/products/904/guides)
### STEMMA QT / Qwiic JST SH 4-pin Cable - 100mm Long

[STEMMA QT / Qwiic JST SH 4-pin Cable - 100mm Long](https://www.adafruit.com/product/4210)
This 4-wire cable is a little over 100mm / 4" long and fitted with JST-SH female 4-pin connectors on both ends. Compared with the chunkier JST-PH these are 1mm pitch instead of 2mm, but still have a nice latching feel, while being easy to insert and remove.

<a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/4210)
[Related Guides to the Product](https://learn.adafruit.com/products/4210/guides)
### STEMMA QT / Qwiic JST SH 4-pin to Premium Male Headers Cable

[STEMMA QT / Qwiic JST SH 4-pin to Premium Male Headers Cable](https://www.adafruit.com/product/4209)
This 4-wire cable is a little over 150mm / 6" long and fitted with JST-SH female 4-pin connectors on one end and premium Dupont male headers on the other. Compared with the chunkier JST-PH these are 1mm pitch instead of 2mm, but still have a nice latching feel, while being easy to insert...

Out of Stock
[Buy Now](https://www.adafruit.com/product/4209)
[Related Guides to the Product](https://learn.adafruit.com/products/4209/guides)
### Premium Male/Male Jumper Wires - 40 x 6" (150mm)

[Premium Male/Male Jumper Wires - 40 x 6" (150mm)](https://www.adafruit.com/product/758)
Handy for making wire harnesses or jumpering between headers on PCB's. These premium jumper wires are 6" (150mm) long and come in a 'strip' of 40 (4 pieces of each of ten rainbow colors). They have 0.1" male header contacts on either end and fit cleanly next to each other...

Out of Stock
[Buy Now](https://www.adafruit.com/product/758)
[Related Guides to the Product](https://learn.adafruit.com/products/758/guides)
### Full Sized Premium Breadboard - 830 Tie Points

[Full Sized Premium Breadboard - 830 Tie Points](https://www.adafruit.com/product/239)
This is a 'full-size' premium quality breadboard, 830 tie points. Good for small and medium projects. It's 2.2" x 7" (5.5 cm x 17 cm) with a standard double-strip in the middle and two power rails on both sides. You can pull the power rails off easily to make the...

In Stock
[Buy Now](https://www.adafruit.com/product/239)
[Related Guides to the Product](https://learn.adafruit.com/products/239/guides)
### Adafruit INA219 FeatherWing

[Adafruit INA219 FeatherWing](https://www.adafruit.com/product/3650)
The **INA219 FeatherWing** makes power-monitoring problems a thing of the past. Instead of struggling with two multimeters, you can just use the handy INA219&nbsp;chip on this breakout to&nbsp;measure both the high side voltage and DC current draw over I2C with 1% precision....

In Stock
[Buy Now](https://www.adafruit.com/product/3650)
[Related Guides to the Product](https://learn.adafruit.com/products/3650/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [WiFi Controlled Mobile Robot](https://learn.adafruit.com/wifi-controlled-mobile-robot.md)
- [Arduino Lesson 14. Servo Motors](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [Adafruit AirLift Shield - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-shield-esp32-wifi-co-processor.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [2.2" TFT Display](https://learn.adafruit.com/2-2-tft-display.md)
- [LED Lightbox](https://learn.adafruit.com/led-lightbox.md)
- [Arduino Prototyping Mounting Plate](https://learn.adafruit.com/arduino-prototyping-mounting-plate.md)
- [How to Choose a Microcontroller](https://learn.adafruit.com/how-to-choose-a-microcontroller.md)
- [Arduino Lesson 16. Stepper Motors](https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
