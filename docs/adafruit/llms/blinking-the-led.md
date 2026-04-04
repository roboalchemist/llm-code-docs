# Source: https://learn.adafruit.com/adafruit-arduino-lesson-2-leds/blinking-the-led.md

# Arduino Lesson 2. LEDs

## Blinking the LED

With a simple modification of the breadboard, we could attach the LED to an output &nbsp;pin of the Arduino. Move the red jumper wire from the Arduino 5V connector to D13, as shown below:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/177/medium800/learn_arduino_fritzing_pin_13.jpg?1396780180)

Now load the 'Blink' example sketch from Lesson 1. You will notice that both the built-in 'L' LED and the external LED should now blink.

```
/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
```

Lets try using a different pin of the Arduino – say D7. Move the red jumper lead from pin D13 to pin D7 and modify the following line near the top of the sketch:

```
int led = 13;
```

so that it reads:

```
int led = 7;
```

Upload the modified sketch to your Arduino board and the LED should still be blinking, but this time using pin D7.  
  
In the next lesson, we will be using LEDs again, this time, the Arduino will be controlling the LED.

[Click Here for the Next Lesson](http://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds)
 **About the Author**  
  
Simon Monk is author of a number of books relating to Open Source Hardware. The following books written by Simon are available from Adafruit:&nbsp;[Programming Arduino](https://www.adafruit.com/products/1019),&nbsp;[30 Arduino Projects for the Evil Genius](https://www.adafruit.com/products/868)&nbsp;and&nbsp;[Programming the&nbsp;Raspberry Pi](https://www.adafruit.com/index.php?main_page=adasearch&q=programming+raspberry+pi "Link: https://www.adafruit.com/index.php?main\_page=adasearch&q=programming+raspberry+pi"). - [Previous Page](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds/moving-the-resistor.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Diffused Red 5mm LED (25 pack)

[Diffused Red 5mm LED (25 pack)](https://www.adafruit.com/product/299)
Need some indicators? We are big fans of these diffused red LEDs, in fact we use them exclusively in our kits. They are fairly bright so they can be seen in daytime, and from any angle. They go easily into a breadboard and will add that extra zing to your project.

- Pack of 25...

In Stock
[Buy Now](https://www.adafruit.com/product/299)
[Related Guides to the Product](https://learn.adafruit.com/products/299/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### Premium Male/Male Jumper Wires - 40 x 6" (150mm)

[Premium Male/Male Jumper Wires - 40 x 6" (150mm)](https://www.adafruit.com/product/758)
Handy for making wire harnesses or jumpering between headers on PCB's. These premium jumper wires are 6" (150mm) long and come in a 'strip' of 40 (4 pieces of each of ten rainbow colors). They have 0.1" male header contacts on either end and fit cleanly next to each other...

In Stock
[Buy Now](https://www.adafruit.com/product/758)
[Related Guides to the Product](https://learn.adafruit.com/products/758/guides)

## Related Guides

- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [Arduino Lesson 6. Digital Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs.md)
- [WiFi Candy Bowl Monitor](https://learn.adafruit.com/wifi-candy-bowl.md)
- [Arduino Lesson 12. LCD Displays - Part 2](https://learn.adafruit.com/adafruit-arduino-lesson-12-lcd-displays-part-2.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Silicone Robo-Tentacle](https://learn.adafruit.com/silicone-robo-tentacle.md)
- [Arduino Ethernet + SD Card](https://learn.adafruit.com/arduino-ethernet-sd-card.md)
- [Arduino Lesson 15. DC Motor Reversing](https://learn.adafruit.com/adafruit-arduino-lesson-15-dc-motor-reversing.md)
- [Arduin-o-Phone](https://learn.adafruit.com/arduin-o-phone-arduino-powered-diy-cellphone.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [Ladyada's Learn Arduino - Lesson #2](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-2.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [Arduino Lesson 4. Eight LEDs and a Shift Register](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds.md)
- [2.8" TFT Touch Shield](https://learn.adafruit.com/2-8-tft-touch-shield.md)
