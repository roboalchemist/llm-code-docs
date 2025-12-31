# Source: https://learn.adafruit.com/2-2-tft-display/bitmaps.md

# 2.2" TFT Display

## Bitmaps

There is a built in microSD card slot into the breakout, and we can use that to load bitmap images! You will need a microSD card formatted **FAT16 or FAT32** (they almost always are by default).

![](https://cdn-learn.adafruit.com/assets/assets/000/049/594/medium800/arduino_compatibles_1480-09.jpg?1513983349)

It's really easy to draw bitmaps. We have a library for it, Adafruit\_ImageReader, which can be installed through the Arduino Library Manager&nbsp;(Sketch→Include Library→Manage Libraries…). Enter “imageread” in the search field and the library is easy to spot:

![](https://cdn-learn.adafruit.com/assets/assets/000/078/280/medium800/arduino_compatibles_ImageReader.png?1563381524)

Lets start by downloading this image of pretty flowers (pix by johngineer)

![](https://cdn-learn.adafruit.com/assets/assets/000/049/595/medium800/arduino_compatibles_purple.bmp?1513983409)

Copy **purple.bmp** into the base directory of a microSD card and insert it into the microSD socket in the breakout.   
  
You'll need to connect up the **SDCS** pin to **Digital 4** on your Arduino, and the&nbsp; **MISO** to&nbsp; **MISO** (or Digital #12 on an Uno) as well. In the below image, those are the extra purple & light blue wires

![](https://cdn-learn.adafruit.com/assets/assets/000/049/596/medium800/arduino_compatibles_sdcs.png?1513983529)

You may want to try the **SD library** examples before continuing, especially one that lists all the files on the SD card  
  
Now upload the **File→examples→Adafruit ImageReader Library→ShieldILI9341** example to your Arduino + breakout. You will see the flowers appear!

![](https://cdn-learn.adafruit.com/assets/assets/000/049/597/medium800/arduino_compatibles_1480-00.jpg?1513983564)

To make new bitmaps, make sure they are less than 240 by 320 pixels and save them in **24-bit BMP format**! They must be in 24-bit format, even if they are not 24-bit color as that is the easiest format for the Arduino. You can rotate images using the **setRotation()** procedure  
  
You can draw as many images as you want - dont forget the names must be less than 8 characters long. Just copy the BMP drawing routines below loop() and call

> **bmpDraw(bmpfilename, x, y);**

For each bitmap. They can be smaller than 320x240 and placed in any location on the screen.

![](https://cdn-learn.adafruit.com/assets/assets/000/049/598/medium800/arduino_compatibles_1480-05.jpg?1513983570)

- [Previous Page](https://learn.adafruit.com/2-2-tft-display/adafruit-gfx-library.md)
- [Next Page](https://learn.adafruit.com/2-2-tft-display/circuitpython-displayio-quickstart.md)

## Featured Products

### 2.2" 18-bit color TFT LCD display with microSD card breakout

[2.2" 18-bit color TFT LCD display with microSD card breakout](https://www.adafruit.com/product/1480)
This lovely little display breakout is the best way to add a small, colorful, and bright display to any project. Since the display uses 4-wire SPI to communicate and has its own pixel-addressable frame buffer, it can be used with every kind of microcontroller. Even a very small one with low...

In Stock
[Buy Now](https://www.adafruit.com/product/1480)
[Related Guides to the Product](https://learn.adafruit.com/products/1480/guides)
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

## Related Guides

- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [Arduino Lesson 3. RGB LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds.md)
- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Adafruit 16-channel PWM/Servo Shield](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [TTL Serial Camera](https://learn.adafruit.com/ttl-serial-camera.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
- [Adafruit 1.27" and 1.5" Color OLED Breakout Board](https://learn.adafruit.com/adafruit-1-5-color-oled-breakout-board.md)
- [Arduino Lesson 5. The Serial Monitor](https://learn.adafruit.com/adafruit-arduino-lesson-5-the-serial-monitor.md)
- [RePaper eInk Development Board](https://learn.adafruit.com/repaper-eink-development-board.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [Adafruit Proto Screw Shield](https://learn.adafruit.com/adafruit-proto-screw-shield.md)
- [Arduino Lesson 6. Digital Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs.md)
