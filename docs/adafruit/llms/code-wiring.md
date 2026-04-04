# Source: https://learn.adafruit.com/oled-tron-clock/code-wiring.md

# OLED TRON Clock

## Code & Wiring

The overall circuit is set up by following the wiring in the [tutorial on the monochrome 128×64 OLED](http://learn.adafruit.com/monochrome-oled-breakouts/wiring-096-128x64-oled-display "Link: http://learn.adafruit.com/monochrome-oled-breakouts/wiring-096-128x64-oled-display") and plugging the RTC breakout board directly into the Arduino as shown in [the DS1307 tutorial](http://learn.adafruit.com/ds1307-real-time-clock-breakout-board-kit).

![](https://cdn-learn.adafruit.com/assets/assets/000/002/266/medium800/lcds___displays_oled_clock_protoboard.jpg?1396781129)

The main sketch file handles reading the current time and drawing the rectangles. &nbsp;A second file contains the coordinates for each rectangle. &nbsp;The rectangles are broken up into three arrays -&nbsp;hour\_rects,&nbsp;minute\_rects, &&nbsp;second\_rects and ordered by the appropriate time value. &nbsp;The advantage of this approach is that modifying the design of the clock is as easy as adjusting the values in the appropriate array entry. &nbsp;The biggest downside was the increase in memory usage; I ended up keeping the arrays in program memory by declaring the arrays with the prog\_uint8\_t type and PROGMEM attribute:

```
prog_uint8_t hour_rects[12][4] PROGMEM = { ... };
```

Also, reading from the arrays required the use of an appropriate function:

```
pgm_read_byte_near(&amp;rectangles[i][0]);
```

- [Previous Page](https://learn.adafruit.com/oled-tron-clock/overview-and-parts.md)
- [Next Page](https://learn.adafruit.com/oled-tron-clock/downloads.md)

## Featured Products

### DS1307 Real Time Clock breakout board kit

[DS1307 Real Time Clock breakout board kit](https://www.adafruit.com/product/264)
**[We've upgraded this RTC breakout and made it even easier to use! Now available as a fully assembled board, it has the same components, chip, size, etc but you don't have to put it together. It's also less expensive! Check out...](https://www.adafruit.com/product/3296)**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/264)
[Related Guides to the Product](https://learn.adafruit.com/products/264/guides)
### Monochrome 0.96" 128x64 OLED Graphic Display - STEMMA QT

[Monochrome 0.96" 128x64 OLED Graphic Display - STEMMA QT](https://www.adafruit.com/product/326)
These displays are small, only about 1" diagonal, but very readable due to the high contrast of an OLED display. This display is made of 128x64 individual white OLED pixels, each one is turned on or off by the controller chip. Because the display makes its own light, no backlight is...

Out of Stock
[Buy Now](https://www.adafruit.com/product/326)
[Related Guides to the Product](https://learn.adafruit.com/products/326/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Monochrome 1.3" 128x64 OLED graphic display - STEMMA QT / Qwiic

[Monochrome 1.3" 128x64 OLED graphic display - STEMMA QT / Qwiic](https://www.adafruit.com/product/938)
These displays are small, only about 1.3" diagonal, but very readable due to the high contrast of an OLED display. This display is made of 128x64 individual white OLED pixels, each one is turned on or off by the controller chip. Because the display makes its own light, no backlight is...

In Stock
[Buy Now](https://www.adafruit.com/product/938)
[Related Guides to the Product](https://learn.adafruit.com/products/938/guides)

## Related Guides

- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Adalight Project Pack](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [CircuitPython Hardware: SSD1306 OLED Display](https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display.md)
- [Light Meter](https://learn.adafruit.com/light-meter.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [Wireless Game Show Poppers for the Classroom!](https://learn.adafruit.com/wireless-game-show-poppers.md)
- [I2C Addresses and Troublesome Chips](https://learn.adafruit.com/i2c-addresses.md)
- [IR Sensor](https://learn.adafruit.com/ir-sensor.md)
- [Pro Trinket Power Meter](https://learn.adafruit.com/pro-trinket-power-meter.md)
- [Adafruit PN532 RFID/NFC Breakout and Shield](https://learn.adafruit.com/adafruit-pn532-rfid-nfc.md)
- [Adafruit Music Maker Shield](https://learn.adafruit.com/adafruit-music-maker-shield-vs1053-mp3-wav-wave-ogg-vorbis-player.md)
- [How to program a Zumo Robot with Simulink](https://learn.adafruit.com/zumo-robot-control-with-simulink.md)
- [Arduino Lesson 1. Blink](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink.md)
