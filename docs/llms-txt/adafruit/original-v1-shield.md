# Source: https://learn.adafruit.com/1-8-tft-display/original-v1-shield.md

# 1.8" TFT Display Breakout and Shield

## Original V1 Shield

# Original V1.0 Shield
If your shield looks like this, you have the original 1.8" TFT shield which does not have a helper seesaw chip

![arduino_compatibles_lcds___displays_2013_05_03_IMG_1762-1024.jpg](https://cdn-learn.adafruit.com/assets/assets/000/008/416/medium640/arduino_compatibles_lcds___displays_2013_05_03_IMG_1762-1024.jpg?1541984351)

The shield uses the "Classic Arduino" SPI wiring and will perform best with Atmega 328-based Arduinos such as the Uno. It can work with other Arduinos but not very well.

Load up the **shieldtest** demo

![](https://cdn-learn.adafruit.com/assets/assets/000/065/559/medium800/arduino_compatibles_image.png?1541984486)

&nbsp;

If you are using an Arduino UNO, Duemilanove or compatible with the ATmega328 chipset, you don't have to do anything! If you're using a Mega, Leonardo, Due or other non-ATmega328 chipset, you'll have to make a modification  
  
To use with the shield, modify the example code pin definitions as follows.

Find these lines:

```
// Option 1 (recommended): must use the hardware SPI pins
// (for UNO thats sclk = 13 and sid = 11) and pin 10 must be
// an output. This is much faster - also required if you want
// to use the microSD card (see the image drawing example)
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS,  TFT_DC, TFT_RST);

// Option 2: use any pins but a little slower!
#define TFT_SCLK 13   // set these to be whatever pins you like!
#define TFT_MOSI 11   // set these to be whatever pins you like!
//Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);
```

Warning: 

The Example code has 2 options for defining the display object. **Uno, Duemilanove** and other Atmega 328-based processors can use the "Option 1" version of the constructor for best performance:

```
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS,  TFT_DC, TFT_RST);
```

 **Mega** and **Leonardo** users should use the "Option 2" version of the constructor for compatibility:

```
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);
```

Be sure to select only one option and comment out the other with a pair of //'s.

Now upload the sketch to see the graphical display!

- [Previous Page](https://learn.adafruit.com/1-8-tft-display/circuitpython-displayio-quickstart.md)
- [Next Page](https://learn.adafruit.com/1-8-tft-display/assembling-the-shield.md)

## Featured Products

### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
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
### 1.8" Color TFT LCD display with MicroSD Card Breakout

[1.8" Color TFT LCD display with MicroSD Card Breakout](https://www.adafruit.com/product/358)
This lovely little display breakout is the best way to add a small, colorful and bright display to any project. Since the display uses 4-wire SPI to communicate and has its own pixel-addressable frame buffer, it can be used with every kind of microcontroller. Even a very small one with low...

Out of Stock
[Buy Now](https://www.adafruit.com/product/358)
[Related Guides to the Product](https://learn.adafruit.com/products/358/guides)
### Adafruit 1.8" Color TFT Shield w/microSD and Joystick

[Adafruit 1.8" Color TFT Shield w/microSD and Joystick](https://www.adafruit.com/product/802)
This lovely little shield is the best way to add a small, colorful and bright display to any project. We took our popular 1.8" TFT breakout board and remixed it into an Arduino shield complete with microSD card slot and a 5-way joystick navigation switch and three selection buttons! Since...

In Stock
[Buy Now](https://www.adafruit.com/product/802)
[Related Guides to the Product](https://learn.adafruit.com/products/802/guides)
### 1.8" SPI TFT display, 160x128 18-bit color - ST7735R driver

[1.8" SPI TFT display, 160x128 18-bit color - ST7735R driver](https://www.adafruit.com/product/618)
We just love this little 1.8" TFT display, with true TFT color (up to 18-bits per pixel!), fine 160x128 resolution, two white LED backlight that runs on 3.3V and a very easy SPI interface that requires only 4 or 5 digital pins to send pixels to the display.  
  
**Please...**

Out of Stock
[Buy Now](https://www.adafruit.com/product/618)
[Related Guides to the Product](https://learn.adafruit.com/products/618/guides)

## Related Guides

- [Wave Shield](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [How to Build a Testing Jig](https://learn.adafruit.com/how-to-build-a-testing-fixture.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
- [Adafruit 1.27" and 1.5" Color OLED Breakout Board](https://learn.adafruit.com/adafruit-1-5-color-oled-breakout-board.md)
- [Arduino Lesson 15. DC Motor Reversing](https://learn.adafruit.com/adafruit-arduino-lesson-15-dc-motor-reversing.md)
- [TTL Serial Camera](https://learn.adafruit.com/ttl-serial-camera.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
