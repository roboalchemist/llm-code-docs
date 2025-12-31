# Source: https://learn.adafruit.com/1-8-tft-display/testing-the-shield.md

# 1.8" TFT Display Breakout and Shield

## Testing the Shield

You can test your assembled shield using the example code from the library.

Start by installing a bunch of libraries!

## Open the Arduino Library manager
![](https://cdn-learn.adafruit.com/assets/assets/000/065/547/medium800/arduino_compatibles_libmanager.png?1541983232)

Install the **Adafruit GFX Library**

![](https://cdn-learn.adafruit.com/assets/assets/000/065/548/medium800/arduino_compatibles_image.png?1541983286)

If using an older version of the Arduino IDE (pre-1.8.10), also locate and install the **Adafruit\_BusIO** library (newer versions do this automatically when using the Arduino Library Manager).

 **Adafruit ST7735 Library**

![](https://cdn-learn.adafruit.com/assets/assets/000/065/549/medium800/arduino_compatibles_image.png?1541983304)

 **Adafruit seesaw Library**

![](https://cdn-learn.adafruit.com/assets/assets/000/065/555/medium800/arduino_compatibles_image.png?1541983379)

[You can read more about installing libraries in our tutorial](http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries).  
  
Restart the Arduino IDE.

# 1.8" Shield with seesaw
If your shield looks like this, you have the 1.8" seesaw version (the most recent) which will work with just about any/all boards. For this version load up the **seesaw\_shield18\_test example**

![arduino_compatibles_pinouts.jpg](https://cdn-learn.adafruit.com/assets/assets/000/065/558/medium640/arduino_compatibles_pinouts.jpg?1541983638)

![](https://cdn-learn.adafruit.com/assets/assets/000/065/557/medium800/arduino_compatibles_image.png?1541983592)

Upload to your microcontroller, and open the serial port watcher at **9600** baud:

The sketch waits until the serial port is opened (you can make it auto-start once you know things are working by removing the `while (!Serial);` line

&nbsp;

Check that the seesaw chip is detected, you should see text display on the TFT after a quick draw test.

If you don't have an SD card inserted, it will fail to init the SD card, that's ok you can continue with the test

![arduino_compatibles_image.png](https://cdn-learn.adafruit.com/assets/assets/000/065/572/medium640/arduino_compatibles_image.png?1541984632)

Once you've gotten this far try pressing all the buttons on the board (except for RESET) to activate the invert-blinking loop.

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/065/645/medium800thumb/arduino_compatibles_ezgif-4-430b34d52a3b.jpg?1541985597)

[For more details about seesaw, check out our guide](https://learn.adafruit.com/adafruit-seesaw-atsamd09-breakout) - we made a nice wrapper for the 1.8" TFT to control the backlight and read buttons but it still might be useful to know the underlying protocol

## Displaying a Bitmap

If you have [parrot.bmp](http://learn.adafruit.com/system/assets/assets/000/010/143/original/parrot.bmp) stored on the SD card you will get a nice parrot display once the buttons have all been pressed

![](https://cdn-learn.adafruit.com/assets/assets/000/065/623/medium800/arduino_compatibles_image.png?1541985212)

- [Previous Page](https://learn.adafruit.com/1-8-tft-display/1-8-tft-shield.md)
- [Next Page](https://learn.adafruit.com/1-8-tft-display/circuitpython-displayio-quickstart.md)

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
