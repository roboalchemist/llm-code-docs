# Source: https://learn.adafruit.com/2-2-tft-display/adafruit-gfx-library.md

# 2.2" TFT Display

## Adafruit GFX Library

We've written a full graphics library specifically for this display which will get you up and running quickly. The code is written in C/C++ for Arduino but is easy to port to any microcontroller by rewritting the low level pin access functions. Here are some of the functions we've included in the library.  
  
The TFT LCD library is based off of the Adafruit GFX graphics core library. GFX has many ready to go functions that should help you start out with your project. Its not exhaustive and we'll try to update it if we find a really useful function. Right now it supports pixels, lines, rectangles, circles, round-rects, triangles and printing text as well as rotation.  
  
[Read more about it here!](http://learn.adafruit.com/adafruit-gfx-graphics-library)  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/927/medium800/lcds___displays_triangles.jpeg?1396777510)

## Bitmaps
In this example, we'll show how to display a 220x176 pixel full color bitmap from a microSD card.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/928/medium800/lcds___displays_rose.jpeg?1396777517)

We have an example sketch in the library showing how to display full color bitmap images stored on an SD card. You'll need a [microSD card such as this one](http://www.adafruit.com/products/102 "Link: http://www.adafruit.com/products/102"). You'll also need to be running Arduino 1.0 or later, as the SD library was updated.  
  
You'll also need an image. [We suggest starting with this bitmap of a rose](http://learn.adafruit.com/system/assets/assets/000/010/144/original/rose.bmp). If you want to later use your own image, use an image editing tool and crop your image to no larger than 160 pixels high and 128 pixels wide. Save it as a 24-bit color **BMP** file - it must be 24-bit color format to work, even if it was originally a 16-bit color image - becaue of the way BMPs are stored and displayed!  
  
Names for bitmap files **must not exceed 8 characters with a 3 character extension**. "mybitmap.bmp" is fine. "myotherbitmap.bmp" is too long and will not be readable by the SD file system.  
  
Copy the **rose.bmp** to the microSD card and insert it into the back of the breakout board.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/929/medium800/lcds___displays_back.jpeg?1396777527)

Wire up the TFT according to the high-speed SPI diagram above. Test that your wiring is correct by uploading the graphics test sketch with the high speed SPI line uncommented and the flexible-low-speed wiring commented.![](https://cdn-learn.adafruit.com/assets/assets/000/001/930/medium800/lcds___displays_wire.jpeg?1396777533)

Once you are sure that the TFT is wired correctly, add the two wires for talking to the SD card. Connect **CDCS** (the unconnected pin in the middle) to digital pin&nbsp; **4** (you can change this later to any pin you want) that's the orange wire below. Connect **MISO** (last unconnected pin) to the Arduino's hardware SPI **MISO** pin, that's the white wire below. For Classic arduinos, this is pin **12**. For Mega's this is pin **50**. You can't change the **MISO** pin, its fixed in the chip hardware.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/931/medium800/lcds___displays_bmpwire.jpeg?1396777543)

Now load the **bitmap** example sketch into the Arduino. It should display the parrot image. If you have any problems, check the serial console for any messages such as not being able to initialize the microSD card or not finding the image.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/932/medium800/rose.bmp?1346246874)

- [Previous Page](https://learn.adafruit.com/2-2-tft-display/arduino-code.md)
- [Next Page](https://learn.adafruit.com/2-2-tft-display/bitmaps.md)

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
