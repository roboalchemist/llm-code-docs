# Source: https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/if-the-servo-misbehaves.md

# Arduino Lesson 14. Servo Motors

## If the Servo Misbehaves

Your servo may behave erratically, and you may find that this only happens when the Arduino is plugged into certain USB ports. This is because the servo draws quite a lot of power, especially as the motor is starting up, and this sudden high demand can be enough to drop the voltage on the Arduino board, so that it resets itself.

If this happens, then you can usually cure it by adding a high value capacitor (470uF or greater) between GND and 5V on the breadboard.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/415/medium800/learn_arduino_fritzing_with_cap.jpg?1396782854)

The capacitor acts as a reservoir of electricity for the motor to use, so that when it starts, it takes charge from the capacitor as well as the Arduino supply.

The longer lead of the capacitor is the positive lead and this should be connected to 5V. The negative lead is also often marked with a '-' symbol.

- [Previous Page](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/the-breadboard-layout-for-sweep.md)
- [Next Page](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/arduino-code-for-sweep.md)

## Featured Products

### Standard servo - TowerPro SG-5010

[Standard servo - TowerPro SG-5010](https://www.adafruit.com/product/155)
This high-torque standard servo can rotate approximately 180 degrees (90 in each direction). You can use any servo code, hardware, or library to control these servos. Good for beginners who want to make stuff move without building a motor controller with feedback & gearbox. Comes with 3...

In Stock
[Buy Now](https://www.adafruit.com/product/155)
[Related Guides to the Product](https://learn.adafruit.com/products/155/guides)
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
### Micro servo

[Micro servo](https://www.adafruit.com/product/169)
Tiny little servo can rotate approximately 180 degrees (90 in each direction) and works just like the standard kinds you're used to but _smaller_. You can use any servo code, hardware, or library to control these servos. Good for beginners who want to make stuff move without...

In Stock
[Buy Now](https://www.adafruit.com/product/169)
[Related Guides to the Product](https://learn.adafruit.com/products/169/guides)
### Standard Size - High Torque - Metal Gear Servo

[Standard Size - High Torque - Metal Gear Servo](https://www.adafruit.com/product/1142)
This high-torque standard servo now comes in a metal-gear flavor, for extra-high torque (10 kg\*cm!) and reliability! It can rotate at least 120 degrees (60 in each direction) with a classic 1.5-2.5ms pulse, but if you can extend your pulses it can go up to about 170 degrees - it varies a bit...

In Stock
[Buy Now](https://www.adafruit.com/product/1142)
[Related Guides to the Product](https://learn.adafruit.com/products/1142/guides)
### Micro Servo - MG90D High Torque Metal Gear

[Micro Servo - MG90D High Torque Metal Gear](https://www.adafruit.com/product/1143)
Add more power to your robot with this metal-geared MG90D&nbsp;servo. The tiny little servo can rotate approximately 90 degrees (45 in each direction) and works just like the standard kinds you're used to but _smaller_. You can use any servo code, hardware, or library to control...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1143)
[Related Guides to the Product](https://learn.adafruit.com/products/1143/guides)

## Related Guides

- [Arduino Tips, Tricks, and Techniques](https://learn.adafruit.com/arduino-tips-tricks-and-techniques.md)
- [Light Meter](https://learn.adafruit.com/light-meter.md)
- [Arduino Lesson 4. Eight LEDs and a Shift Register](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds.md)
- [Adafruit Arduino Selection Guide](https://learn.adafruit.com/adafruit-arduino-selection-guide.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [Photocells](https://learn.adafruit.com/photocells.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield.md)
- [Ladyada's Learn Arduino - Lesson #1](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-1.md)
- [Collin's Lab: MIDI](https://learn.adafruit.com/collins-lab-midi.md)
- [Arduino Lesson 7. Make an RGB LED Fader](https://learn.adafruit.com/adafruit-arduino-lesson-7-make-an-rgb-led-fader.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
