# Source: https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds/using-internet-colors.md

# Arduino Lesson 3. RGB LEDs

## Using Internet Colors

If you have done any Internet programming, you will probably be aware that colors are often represented as a 'hex' number. For example the color red has the number #FF0000. You can find the numbers associated with a particular color using tables like these: [https://htmlcolorcodes.com/color-names/](https://htmlcolorcodes.com/color-names/)  
The six digits of the number are actually three pairs of numbers; the first pair being the red component of the color, the next two digits the green part and the final pair the blue part. Red is #FF0000, because its maximum red (FF is 255 in hex) and it has no green or blue part.  
  
It would be pretty useful to be able to dial up one of these color numbers so that it is displayed on the RGB LED.   
  
Let's try and make the color indigo (#4B0082).

![](https://cdn-learn.adafruit.com/assets/assets/000/002/094/medium800/learn_arduino_indigo.png?1396779215)

The red, green and blue parts of indigo are (in hex) 4B, 00 and 82 respectively. We can plug those into the 'setColor' function like this:

```
setColor(0x4B, 0x0, 0x82);  // indigo
```

We have used hex numbers for the three parts of the color by putting '0x' in front of them.   
  
Try adding a few colors of your own to the 'loop' function. Don't forget to add a delay after each one.

- [Previous Page](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds/arduino-sketch.md)
- [Next Page](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds/theory-pwm.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
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
### Diffused RGB (tri-color) LED

[Diffused RGB (tri-color) LED](https://www.adafruit.com/product/159)
Diffused 5mm tri-color LED with separate red, green and blue LED chips inside! Nice indicator, and fun to color-swirl. 60 degree viewing angle. We like diffused RGB LEDs because they color mix inside instead of appearing as 3 distinct LEDs.

These are Common-Anode type which means you...

In Stock
[Buy Now](https://www.adafruit.com/product/159)
[Related Guides to the Product](https://learn.adafruit.com/products/159/guides)

## Related Guides

- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Adafruit Motor Shield](https://learn.adafruit.com/adafruit-motor-shield.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [Arduino Lesson 5. The Serial Monitor](https://learn.adafruit.com/adafruit-arduino-lesson-5-the-serial-monitor.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [Circuit Playground: D is for Diode](https://learn.adafruit.com/circuit-playground-d-is-for-diode.md)
- [Wave Shield](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino.md)
- [Arduino Lesson 0. Getting Started](https://learn.adafruit.com/lesson-0-getting-started.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
- [RePaper eInk Development Board](https://learn.adafruit.com/repaper-eink-development-board.md)
- [Adafruit AirLift Shield - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-shield-esp32-wifi-co-processor.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [Babel Fish](https://learn.adafruit.com/babel-fish.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
