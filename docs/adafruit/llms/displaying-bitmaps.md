# Source: https://learn.adafruit.com/1-8-tft-display/displaying-bitmaps.md

# 1.8" TFT Display Breakout and Shield

## Displaying Bitmaps

![](https://cdn-learn.adafruit.com/assets/assets/000/001/911/medium800/lcds___displays_18tftlcdparrot_LRG.jpeg?1396777379)

In this example, we'll show how to display a 128x160 pixel full color bitmap from a microSD card.  
  
We have an example sketch in the library showing how to display full color bitmap images stored on an SD card. You'll need a [microSD card such as this one](http://www.adafruit.com/products/102).

It's really easy to draw bitmaps. We have a library for it, Adafruit\_ImageReader, which can be installed through the Arduino Library Manager&nbsp;(Sketch→Include Library→Manage Libraries…). Enter “imageread” in the search field and the library is easy to spot:

![](https://cdn-learn.adafruit.com/assets/assets/000/078/309/medium800/arduino_compatibles_ImageReader.png?1563387756)

You'll also need an image. We suggest starting with this bitmap of a parrot.

[Download parrot.bmp](http://learn.adafruit.com/system/assets/assets/000/010/143/original/parrot.bmp)
If you want to later use your own image, use an image editing tool and crop your image to no larger than 160 pixels high and 128 pixels wide. Save it as a 24-bit color **BMP** file - it must be 24-bit color format to work, even if it was originally a 16-bit color image - because of the way BMPs are stored and displayed!

Copy the **parrot.bmp** to the microSD card and insert it into the micro SD card holder on your shield or breakout board.

![](https://cdn-learn.adafruit.com/assets/assets/000/019/567/medium800/lcds___displays_358scale_ORIG.jpg?1409949008)

# Breakout Wiring

**Shield users** can skip directly to the " **Example Sketch**" section.  
  
Wire up the TFT as described on the wiring & test page and add the two wires for talking to the SD card. Connect&nbsp; **CARD\_CS** (the unconnected pin in the middle) to digital pin **4** (you can change this later to any pin you want). Connect **MISO** (second from the right) to the Arduino's hardware SPI **MISO** pin. For Classic arduinos, this is pin **12**. For Mega's this is pin **50**. You can't change the **MISO** pin, it's fixed in the chip hardware.

![](https://cdn-learn.adafruit.com/assets/assets/000/078/307/medium800/arduino_compatibles_ST7735-160x128.png?1563387002)

# Example Sketch
If you have the breakout, open the&nbsp; **File→examples→Adafruit ImageReader Library→**** BreakoutST7735 - 160x128&nbsp;**example.

![arduino_compatibles_example-160x128.png](https://cdn-learn.adafruit.com/assets/assets/000/078/315/medium640/arduino_compatibles_example-160x128.png?1563389273)

If you have the shield, open the&nbsp; **File→examples→Adafruit ImageReader Library→**** ShieldST7735&nbsp;**example.

![arduino_compatibles_example-7735Shield.png](https://cdn-learn.adafruit.com/assets/assets/000/078/316/medium640/arduino_compatibles_example-7735Shield.png?1563389311)

Now upload the&nbsp;example sketch to the Arduino. It should display the parrot image. If you have any problems, check the serial console for any messages such as not being able to initialize the microSD card or not finding the image.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/915/medium800/lcds___displays_parrot.jpeg?1396777410)

- [Previous Page](https://learn.adafruit.com/1-8-tft-display/breakout-wiring-and-test.md)
- [Next Page](https://learn.adafruit.com/1-8-tft-display/circuitpython-displayio-quickstart-2.md)

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
