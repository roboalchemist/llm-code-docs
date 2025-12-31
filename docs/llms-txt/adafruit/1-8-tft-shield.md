# Source: https://learn.adafruit.com/1-8-tft-display/1-8-tft-shield.md

# 1.8" TFT Display Breakout and Shield

## 1.8" TFT Shield V2

Let's take a tour of the 1.8" TFT Shield

![](https://cdn-learn.adafruit.com/assets/assets/000/065/534/medium800/arduino_compatibles_pinouts.jpg?1541981318)

# TFT Display
In the center is the 1.8" TFT display. This display is full color (16-bit RGB), 128x160 pixels, and has a backlight. The display receives data over SPI plus two pins:

- SCK - SPI Clock
- MOSI - SPI Data
- Digital 10 - Chip Select
- Digital 8 - Data/Command Select

The TFT reset is connected to the seesaw chip. The backlight is also PWM controlled by the seesaw chip. The 4 SPI+control pins, however, must be controlled directly by the Arduino

![arduino_compatibles_tft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/065/537/medium640/arduino_compatibles_tft.jpg?1541982620)

# Buttons & Joystick
In addition of the display, you also get a bunch of user-interface buttons.

In the top left is the **Reset** button, this will reset the shield and Arduino when pressed. It is connected directly to the Reset pins

There are three buttons labeled **A B C** below the TFT, these are connected to the seesaw chip. You can read the values over I2C

To the right of the TFT is a 5-way joystick. It can be pushed up/down/left/right and select (in). It is connected to the seesaw chip, you can read the joystick over I2C

![arduino_compatibles_buttons.jpg](https://cdn-learn.adafruit.com/assets/assets/000/065/539/medium640/arduino_compatibles_buttons.jpg?1541982710)

# SD Card
The micro SD card slot can be used to read/write data from any micro SD card using the Arduino libraries. The SD card is connected to the SPI pins as well as **Digital #4** for **Chip Select**

The SD card is not required for use, but it's handy for storing images

![arduino_compatibles_sd.jpg](https://cdn-learn.adafruit.com/assets/assets/000/065/540/medium640/arduino_compatibles_sd.jpg?1541982883)

# seesaw I2C Expander
Instead of taking up a bunch of GPIO pins to read the buttons and joystick, as well as controlling the TFT backlight, we use an I2C expander chip called the **seesaw**. It is connected to the SDA/SCL pins and can read/write pins with our library. This saves a ton of pins and then you can always use the I2C pins for other sensors, as long as the address doesnt conflict

&nbsp;

**Don't forget!** Since the seesaw chip is used for the TFT backlight and reset, **you need to activate it even if you are not reading the buttons or joystick.**

![arduino_compatibles_seesaw.jpg](https://cdn-learn.adafruit.com/assets/assets/000/065/542/medium640/arduino_compatibles_seesaw.jpg?1541983027)

- [Previous Page](https://learn.adafruit.com/1-8-tft-display/python-usage.md)
- [Next Page](https://learn.adafruit.com/1-8-tft-display/testing-the-shield.md)

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
