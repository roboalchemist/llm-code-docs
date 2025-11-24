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

- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [OLED TRON Clock](https://learn.adafruit.com/oled-tron-clock.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [Programming Arduino with Android and Windows Tablets](https://learn.adafruit.com/programming-arduino-with-android-and-windows-tablets.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [Bluefruit LE Connect for iOS and Android](https://learn.adafruit.com/bluefruit-le-connect.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [Trellis 3D Printed Enclosure](https://learn.adafruit.com/trellis-3d-printed-enclosure.md)
