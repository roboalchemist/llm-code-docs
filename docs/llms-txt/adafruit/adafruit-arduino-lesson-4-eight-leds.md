# Source: https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds.md

# Arduino Lesson 4. Eight LEDs and a Shift Register

## Overview

In this lesson, you will learn how to use eight large red LEDs with an Arduino without needing to give up 8 output pins!

![](https://cdn-learn.adafruit.com/assets/assets/000/002/101/medium800/learn_arduino_breadboard.jpg?1396779268)

Although you could wire up eight LEDs each with a resistor to an Arduino pin (like we did for an RGB LED in Lesson 2) you would rapidly start to run out of pins on your Arduino. If you don't have a lot of stuff connected to your 'duino it's OK to do so - but often times we want buttons, sensors, servos, etc and before you know it you've got no pins left. So, instead of doing that, you are going to use a chip called the **74HC595 Serial to Parallel Converter**. This chip has eight outputs (perfect) and three inputs that you use to feed data into it a bit at a time.   
  
This chip makes it a little slower to drive the LEDs (you can only change the LEDs about 500,000 times a second instead of 8,000,000 a second) but it's still really really fast, way faster than humans can detect, so it's worth it!

- [Next Page](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds/parts.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### 74HC595 Shift Register - 3 pack

[74HC595 Shift Register - 3 pack](https://www.adafruit.com/product/450)
Add lots more outputs to a microcontroller system with chainable shift registers. These chips take a serial input (SPI) of 1 byte (8 bits) and then output those digital bits onto 8 pins. You can chain them together so putting three in a row with the serial output of one plugged into the serial...

In Stock
[Buy Now](https://www.adafruit.com/product/450)
[Related Guides to the Product](https://learn.adafruit.com/products/450/guides)
### Diffused Red 5mm LED (25 pack)

[Diffused Red 5mm LED (25 pack)](https://www.adafruit.com/product/299)
Need some indicators? We are big fans of these diffused red LEDs, in fact we use them exclusively in our kits. They are fairly bright so they can be seen in daytime, and from any angle. They go easily into a breadboard and will add that extra zing to your project.

- Pack of 25...

In Stock
[Buy Now](https://www.adafruit.com/product/299)
[Related Guides to the Product](https://learn.adafruit.com/products/299/guides)
### Premium Male/Male Jumper Wires - 40 x 6" (150mm)

[Premium Male/Male Jumper Wires - 40 x 6" (150mm)](https://www.adafruit.com/product/758)
Handy for making wire harnesses or jumpering between headers on PCB's. These premium jumper wires are 6" (150mm) long and come in a 'strip' of 40 (4 pieces of each of ten rainbow colors). They have 0.1" male header contacts on either end and fit cleanly next to each other...

In Stock
[Buy Now](https://www.adafruit.com/product/758)
[Related Guides to the Product](https://learn.adafruit.com/products/758/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [74HC595 Shift Register](https://learn.adafruit.com/74hc595.md)
- [Adafruit 16-channel PWM/Servo Shield](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield.md)
- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [Mini Thermal Receipt Printers](https://learn.adafruit.com/mini-thermal-receipt-printer.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [Metal Inlay Capacitive Touch Buttons](https://learn.adafruit.com/metal-inlay-capacitive-touch-buttons.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Line Following Zumo Robot Using Simulink](https://learn.adafruit.com/line-following-zumo-robot-programmed-with-simulink.md)
- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
- [Adafruit AirLift Shield - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-shield-esp32-wifi-co-processor.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
- [Naughty or Nice Machine](https://learn.adafruit.com/naughty-or-nice-machine.md)
- [Smart Cocktail Shaker](https://learn.adafruit.com/smart-cocktail-shaker.md)
- [Arduino Tips, Tricks, and Techniques](https://learn.adafruit.com/arduino-tips-tricks-and-techniques.md)
