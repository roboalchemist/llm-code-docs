# Source: https://learn.adafruit.com/096-mini-color-oled.md

# 0.96" mini Color OLED

## Overview

We love our black and white monochrome displays but we also like to dabble with some color now and then. Our new 0.96" color OLED displays are perfect when you need an ultra-small display with vivid, high-contrast 16-bit color. The visible portion of the OLED measures 0.96" diagonal and contains 96x64 RGB pixels, each one made of red, green and blue OLEDs. Each pixel can be set with 16-bits of resolution for a large range of colors. Because the display uses OLEDs, there is no backlight, and the contrast is very high (black is really black). We picked this display for its excellent color, this is the nicest mini OLED we could find!![](https://cdn-learn.adafruit.com/assets/assets/000/000/839/medium800/lcds___displays_684_LRG.jpg?1396766339)

This OLED uses the SSD1331 driver chip, which manages the display. You can talk to the driver chip using either 3 or 4-wire write-only SPI (clock, data, chip select, data/command and an optional reset pin) or standard 8-bit parallel 8080/6800 which also permits reading pixel data from the display. Our example code shows how to use SPI since for such a display, its plenty fast. Inlcuded on the fully assembled breakout is the OLED display and a small boost converter (required for providing 12V to the OLED) and a microSD card holder. Our example code shows how to read a bitmap from the uSD card and display it all via SPI.

The logic levels for the microSD ard and OLED are 3.3V max. In order to make this breakout usable for bidirectional 8-bit and SPI interfaces, we left out an on-board level shifter. However, we include a DIP chip 75LVC245 8-bit level converter chip and our tutorial shows how to wire it to an Arduino so that you can use the breakout with 5V logic such as that of an Arduino. If you have a 3.3V logic level microcontroller system, you can skip the level shifter.

Of course, we wouldn't just leave you with a datasheet and a "good luck!" - we've written a full open source graphics library that can draw pixels, lines, rectangles, circles, text and bitmaps as well as example code and a wiring tutorial. The code is written for Arduino but can be easily ported to your favorite microcontroller!

[Pick one up today from the adafruit shop!](http://www.adafruit.com/products/684)

 **Please note:** all OLEDs have a “half life” — their brightness naturally diminishes over time, albeit over _many thousands_ of hours.&nbsp;This makes them a poor choice for always-on 24/7/365 use. Best to **turn off the display** when inactive, or consider using a **color LCD** for continuously running projects.

- [Next Page](https://learn.adafruit.com/096-mini-color-oled/power.md)

## Featured Products

### OLED Breakout Board - 16-bit Color 0.96" w/microSD holder

[OLED Breakout Board - 16-bit Color 0.96" w/microSD holder](https://www.adafruit.com/product/684)
We love our black and white monochrome displays but we also like to dabble with some color now and then. Our new 0.96" color OLED displays are perfect when you need an ultra-small display with vivid, high-contrast 16-bit color. The visible portion of the OLED measures 0.96" diagonal...

In Stock
[Buy Now](https://www.adafruit.com/product/684)
[Related Guides to the Product](https://learn.adafruit.com/products/684/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [Adafruit Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [Arduino Lesson 15. DC Motor Reversing](https://learn.adafruit.com/adafruit-arduino-lesson-15-dc-motor-reversing.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [Arduino Lesson 9. Sensing Light](https://learn.adafruit.com/adafruit-arduino-lesson-9-sensing-light.md)
- [Low Power Coin Cell Voltage Logger](https://learn.adafruit.com/low-power-coin-cell-voltage-logger.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [Skill Badge Requirements: Microcontrollers](https://learn.adafruit.com/skill-badge-requirements-microcontrollers.md)
- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [DIY 8x2 LCD Shield](https://learn.adafruit.com/diy-8x2-lcd-shield.md)
- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
