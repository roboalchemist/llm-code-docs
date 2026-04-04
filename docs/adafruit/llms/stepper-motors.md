# Source: https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors/stepper-motors.md

# Arduino Lesson 16. Stepper Motors

## Stepper Motors

Stepper motors use a cogged wheel and electro magnets to nudge the wheel round a 'step' at a time.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/496/medium800/learn_arduino_steppers.png?1396783806)

By energizing the coils in the right order, the motor is driven round. The number of steps that the stepper motor has in a 360 degree rotation is actually the number of teeth on the cog.

The motor we are using has 48 steps, but then the motor also incorporates a reduction gearbox of 1:16 that means that it needs 16 x 48 = 768 steps.

In this lesson, we do not use the common Red connection. This connection is only provided if you are using a different type of drive circuit that does not allow the current in each coil to be reversed. Having a center connection to each coil means that you can either energise the left or right side of the coil, and get the effect of reversing the current flow without having to use a circuit that can reverse the current.

Since we are using a L293D that is very good at reversing the current, we do not need this common connection, we can supply current in either direction to the whole of each of the coils.

- [Previous Page](https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors/arduino-code.md)
- [Next Page](https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors/other-things-to-do.md)

## Featured Products

### Small Reduction Stepper Motor - 5VDC 32-Step 1/16 Gearing

[Small Reduction Stepper Motor - 5VDC 32-Step 1/16 Gearing](https://www.adafruit.com/product/858)
This is a great first stepper motor, good for small projects and experimenting with steppers. This uni-polar motor has a built-in mounting plate with two mounting holes. There are only 32 steps (11.25 degree) per revolution, and inside is a 1/16&nbsp;reduction gear set. (Actually it's...

In Stock
[Buy Now](https://www.adafruit.com/product/858)
[Related Guides to the Product](https://learn.adafruit.com/products/858/guides)
### Dual H-Bridge Motor Driver for DC or Steppers - 600mA - L293D

[Dual H-Bridge Motor Driver for DC or Steppers - 600mA - L293D](https://www.adafruit.com/product/807)
Run four solenoids, two DC motors, or one bi-polar or uni-polar stepper with up to 600mA per channel using the L293D. These are perhaps better known as "the drivers in our Adafruit Motorshield". If you accidentally damaged the drivers in a shield, you can use one of these puppies to...

In Stock
[Buy Now](https://www.adafruit.com/product/807)
[Related Guides to the Product](https://learn.adafruit.com/products/807/guides)
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

- [Silicone Robo-Tentacle](https://learn.adafruit.com/silicone-robo-tentacle.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [Adafruit AirLift Shield - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-shield-esp32-wifi-co-processor.md)
- [RePaper eInk Development Board](https://learn.adafruit.com/repaper-eink-development-board.md)
- [Memories of an Arduino](https://learn.adafruit.com/memories-of-an-arduino.md)
- [Adafruit Proto Screw Shield](https://learn.adafruit.com/adafruit-proto-screw-shield.md)
- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
- [Adafruit IO Basics: NeoPixel Controller](https://learn.adafruit.com/adafruit-io-basics-neopixel-controller.md)
- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [How to Find Hidden COM Ports](https://learn.adafruit.com/how-to-find-hidden-com-ports.md)
- [Collin's Lab: MIDI](https://learn.adafruit.com/collins-lab-midi.md)
