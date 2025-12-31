# Source: https://learn.adafruit.com/character-lcds/rgb-backlit-lcds.md

# Character LCDs

## RGB Backlit LCDs

[We now stock a few different RGB backlight LCDs](http://www.adafruit.com/category/63) . These LCDs work just like the normal character type, but the backlight has three LEDS (red/green/blue) so you can generate any color you'd like. Very handy when you want to have some ambient information conveyed.

After you've wired up the LCD and tested it as above, you can connect the LEDs to the PWM analog out pins of the Arduino to precisely set the color. The PWM pins are fixed in hardware and there's 6 of them but three are already used so we'll use the remaining three PWM pins. Connect the red LED (pin 16 of the LCD) to Digital 3, the green LED pin (pin 17 of the LCD) to digital 5 and the blue LED pin (pin 18 of the LCD) to digital 6. You do not need any resistors between the LED pins and the arduino pins because resistors are already soldered onto the character LCD for you!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/947/medium800/lcds___displays_rgblcdtest_t.jpg?1396767347)

Now upload this code to your Arduino to see the LCD background light swirl! ([Click here to see what it looks like in action](http://www.flickr.com/photos/adafruit/6002862732/ "Link: http://www.flickr.com/photos/adafruit/6002862732/")).

http://www.youtube.com/watch?v=M460s1A_vlQ

```
// include the library code:
#include &lt;LiquidCrystal.h&gt;
#include &lt;Wire.h&gt;
 
#define REDLITE 3
#define GREENLITE 5
#define BLUELITE 6
 
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);
 
// you can change the overall brightness by range 0 -&gt; 255
int brightness = 255;
 
void setup() {
  // set up the LCD's number of rows and columns: 
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("RGB 16x2 Display  ");
  lcd.setCursor(0,1);
  lcd.print(" Multicolor LCD ");
  
  pinMode(REDLITE, OUTPUT);
  pinMode(GREENLITE, OUTPUT);
  pinMode(BLUELITE, OUTPUT);

  brightness = 100;
}
 
 
void loop() {
  for (int i = 0; i &lt; 255; i++) {
    setBacklight(i, 0, 255-i);
    delay(5);
  }
  for (int i = 0; i &lt; 255; i++) {
    setBacklight(255-i, i, 0);
    delay(5);
  }
  for (int i = 0; i &lt; 255; i++) {
    setBacklight(0, 255-i, i);
    delay(5);
  }
}
 
 
 
void setBacklight(uint8_t r, uint8_t g, uint8_t b) {
  // normalize the red LED - its brighter than the rest!
  r = map(r, 0, 255, 0, 100);
  g = map(g, 0, 255, 0, 150);
 
  r = map(r, 0, 255, 0, brightness);
  g = map(g, 0, 255, 0, brightness);
  b = map(b, 0, 255, 0, brightness);
 
  // common anode so invert!
  r = map(r, 0, 255, 255, 0);
  g = map(g, 0, 255, 255, 0);
  b = map(b, 0, 255, 255, 0);
  Serial.print("R = "); Serial.print(r, DEC);
  Serial.print(" G = "); Serial.print(g, DEC);
  Serial.print(" B = "); Serial.println(b, DEC);
  analogWrite(REDLITE, r);
  analogWrite(GREENLITE, g);
  analogWrite(BLUELITE, b);
}
```

- [Previous Page](https://learn.adafruit.com/character-lcds/arduino-code.md)
- [Next Page](https://learn.adafruit.com/character-lcds/python-circuitpython.md)

## Featured Products

### Standard LCD 16x2 + extras

[Standard LCD 16x2 + extras](https://www.adafruit.com/product/181)
Standard HD44780 LCDs are useful for creating standalone projects.

- 16 characters wide, 2 rows
- White text on blue background
- Connection port is 0.1" pitch, single row for easy breadboarding and wiring
- Pins are documented on the back of the LCD to assist...

In Stock
[Buy Now](https://www.adafruit.com/product/181)
[Related Guides to the Product](https://learn.adafruit.com/products/181/guides)
### Assembled Standard LCD 16x2 + extras - White on Blue

[Assembled Standard LCD 16x2 + extras - White on Blue](https://www.adafruit.com/product/1447)
Standard HD44780 LCDs are useful for creating standalone projects. &nbsp;This product is similar to our [Standard LCD 16x2 display **but comes with the header soldered on!**](https://www.adafruit.com/products/181)

- 16 characters wide, 2 rows
- White text...

In Stock
[Buy Now](https://www.adafruit.com/product/1447)
[Related Guides to the Product](https://learn.adafruit.com/products/1447/guides)
### RGB backlight positive LCD 16x2 + extras

[RGB backlight positive LCD 16x2 + extras](https://www.adafruit.com/product/398)
This is a fancy upgrade to standard 16x2 LCDs, instead of just having blue and white, or red and black, this LCD has black characters on a full color RGB-backlight background! That means you can change the background color to anything you want - red, green, blue, pink, white, purple yellow,...

In Stock
[Buy Now](https://www.adafruit.com/product/398)
[Related Guides to the Product](https://learn.adafruit.com/products/398/guides)
### RGB backlight negative LCD 16x2 + extras

[RGB backlight negative LCD 16x2 + extras](https://www.adafruit.com/product/399)
This is a fancy upgrade to standard 16x2 LCDs, instead of just having blue and white, or red and black, this LCD has full color RGB characters on a dark/black background! That means you can change the character display colors to anything you want - red, green, blue, pink, white, purple yellow,...

In Stock
[Buy Now](https://www.adafruit.com/product/399)
[Related Guides to the Product](https://learn.adafruit.com/products/399/guides)
### Standard LCD 20x4 + extras

[Standard LCD 20x4 + extras](https://www.adafruit.com/product/198)
Standard HD44780 LCDs are useful for creating standalone projects.

- 20 characters wide, 4 rows
- White text on blue background
- Connection port is 0.1" pitch, single row for easy breadboarding and wiring
- Single LED backlight with a resistor included, you can...

In Stock
[Buy Now](https://www.adafruit.com/product/198)
[Related Guides to the Product](https://learn.adafruit.com/products/198/guides)
### RGB backlight positive LCD 20x4 + extras

[RGB backlight positive LCD 20x4 + extras](https://www.adafruit.com/product/499)
This is a fancy upgrade to standard 20x4 LCDs, instead of just having blue and white, or red and black, this LCD has black characters on a full color RGB background! That means you can change the display background color to anything you want - red, green, blue, pink, white, purple yellow,...

In Stock
[Buy Now](https://www.adafruit.com/product/499)
[Related Guides to the Product](https://learn.adafruit.com/products/499/guides)
### RGB backlight negative LCD 20x4 + extras

[RGB backlight negative LCD 20x4 + extras](https://www.adafruit.com/product/498)
This is a fancy upgrade to standard 20x4 LCDs, instead of just having blue and white, or red and black, this LCD has full color RGB characters on a dark/black background! That means you can change the character display colors to anything you want - red, green, blue, pink, white, purple yellow,...

Out of Stock
[Buy Now](https://www.adafruit.com/product/498)
[Related Guides to the Product](https://learn.adafruit.com/products/498/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
- [Adafruit VS1053 MP3/AAC/Ogg/MIDI/WAV Codec Breakout Tutorial](https://learn.adafruit.com/adafruit-vs1053-mp3-aac-ogg-midi-wav-play-and-record-codec-tutorial.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [How to Build a Testing Jig](https://learn.adafruit.com/how-to-build-a-testing-fixture.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [WiFi Controlled Mobile Robot](https://learn.adafruit.com/wifi-controlled-mobile-robot.md)
- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [RGB LCD Shield](https://learn.adafruit.com/rgb-lcd-shield.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
