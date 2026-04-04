# Source: https://learn.adafruit.com/flora-tv-b-gone/transistors.md

# Source: https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors/transistors.md

# Arduino Lesson 13. DC Motors

## Transistors

The small DC motor, is likely to use more power than an Arduino digital output can handle directly. If we tried to connect the motor straight to an Arduino pin, there is a good chance that it could damage the Arduino.

A small transistor like the PN2222 can be used as a switch that uses just a little current from the Arduino digital output to control the much bigger current of the motor.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/348/medium800/learn_arduino_transistor.png?1396782158)

The transistor has three leads. Most of the electricity flows from the Collector to the Emitter, but this will only happen if a small amount is flowing into the Base connection. This small current is supplied by the Arduino digital output.

The diagram below is called a schematic diagram. Like a breadboard layout, it is a way of showing how the parts of an electronic project are connected together.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/349/medium800/learn_arduino_schematic.jpg?1396782164)

The pin D3 of the Arduino is connected to the resistor. Just like when using an LED, this limits the current flowing into the transistor through the base.

There is a diode connected across the connections of the motor. Diodes only allow electricity to flow in one direction (the direction of their arrow).

When you turn the power off to a motor, you get a negative spike of voltage, that can damage your Arduino or the transistor. The diode protects against this, by shorting out any such reverse current from the motor.

- [Previous Page](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors/arduino-code.md)
- [Next Page](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors/other-things-to-do.md)

## Featured Products

### NPN Bipolar Transistors (PN2222) - 10 pack

[NPN Bipolar Transistors (PN2222) - 10 pack](https://www.adafruit.com/product/756)
Transistors are powerful little electronic switches, and we really like these NPN transistors whenever we need to control medium-power electronics such as small motors, solenoids, or IR LEDs. We find them so handy, they come in a pack of 10!

Each transistor is a general-purpose...

In Stock
[Buy Now](https://www.adafruit.com/product/756)
[Related Guides to the Product](https://learn.adafruit.com/products/756/guides)
### DC Toy / Hobby Motor - 130 Size

[DC Toy / Hobby Motor - 130 Size](https://www.adafruit.com/product/711)
These are standard '130 size' DC hobby motors. They come with a wider operating range than most toy motors: from 4.5 to 9VDC instead of 1.5-4.5V. This range makes them perfect for controlling with an Adafruit Motor Shield, or with an Arduino where you are more likely to have 5 or 9V...

In Stock
[Buy Now](https://www.adafruit.com/product/711)
[Related Guides to the Product](https://learn.adafruit.com/products/711/guides)
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
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [Programming Arduino with Android and Windows Tablets](https://learn.adafruit.com/programming-arduino-with-android-and-windows-tablets.md)
- [Arduino Lesson 16. Stepper Motors](https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors.md)
- [Arduino Lesson 4. Eight LEDs and a Shift Register](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds.md)
- [Arduino Lesson 3. RGB LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds.md)
- [2.2" TFT Display](https://learn.adafruit.com/2-2-tft-display.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [Memories of an Arduino](https://learn.adafruit.com/memories-of-an-arduino.md)
- [Arduino Lesson 7. Make an RGB LED Fader](https://learn.adafruit.com/adafruit-arduino-lesson-7-make-an-rgb-led-fader.md)
- [Arduino Ethernet + SD Card](https://learn.adafruit.com/arduino-ethernet-sd-card.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
