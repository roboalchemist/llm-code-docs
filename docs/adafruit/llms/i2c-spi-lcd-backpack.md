# Source: https://learn.adafruit.com/i2c-spi-lcd-backpack.md

# I2C/SPI LCD Backpack

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/118/700/medium800thumb/arduino_compatibles_292-04_1.jpg?1677078568)

Character LCDs are a fun and easy way to have your microcontroller project talk back to you. They are also common, and easy to get, available in tons of colors and sizes. [We've written tutorials on using character LCDs with an Arduino](http://learn.adafruit.com/character-lcds) (or similar microcontroller) but find that the number of pins necessary to control the LCD can be restrictive, especially with ambitious projects. We wanted to make a 'backpack' (add-on circuit) that would reduce the number of pins without a lot of expense.

![](https://cdn-learn.adafruit.com/assets/assets/000/122/968/medium800/adafruit_products_292-11.jpg?1690378204)

By using simple I2C and SPI input/output expanders we have reduced the number of pins, while still making it easy to interface with the LCD. Only 2 pins are needed for I2C, 3 for SPI. For Arduino and CircuitPython/Python users, we provide an easy-to-use library that is backwards compatible with projects using the '6 pin' wiring.

This backpack comes with a 2-pin and 3-pin terminal block as shown (you can snap it together to make a 5-pin terminal and then solder it to the backpack for easy wiring).

![](https://cdn-learn.adafruit.com/assets/assets/000/122/969/medium800/adafruit_products_292-09.jpg?1690378224)

This backpack will work with any 'standard' character LCD, from 8x1 to 20x4 sizes! As long as they have a 16-pin single-line connection header at the top. [We carry a few LCDs that work great](http://www.adafruit.com/category/63_96). We suggest using our blue white 20x4 or 16x2 LCDs. Note that it does not work with 16x2 OLED displays. You can try to connect our RGB 16x2 or 20x4 LCDs, but this backpack will not control the RGB backlight so you'll have to use the backpack only for the 14 digital IO pins (pins #1-14) and connect the backlight pins (#15-#18) directly to your microcontroller with 4 extra wires for color/PWM control as if they were just an RGB LED.

![](https://cdn-learn.adafruit.com/assets/assets/000/122/970/medium800/adafruit_products_292-13.jpg?1690378244)

 **NEW! As of February 8, 2023** - This backpack now comes with a big re-spin that makes lots of improvements:

- We've added a 3-5V boost circuit so you can use this backpack to control 5V LCDs even with 3V power and logic.
- The contrast potentiometer is a lot nicer and easier to twist using a small screwdriver
- Added [SparkFun qwiic](https://www.sparkfun.com/qwiic) compatible **[STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt)** connectors for the I2C bus **so you don't even need to solder the I2C and power lines.** Just wire up to your favorite micro using a [STEMMA QT adapter cable.](https://www.adafruit.com/?q=stemma%20qt%20cable) [QT Cable is not included, but we have a variety in the shop](https://www.adafruit.com/?q=stemma+qt+cable&sort=BestMatch).
- Functionality and size/shape are the same - mechanically and code-wise it is a drop-in replacement.
- We've also updated this PCB with [Adafruit Pinguin](https://github.com/adafruit/Adafruit_Pinguin) to make a lovely and legible silkscreen.

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/118/699/medium800/arduino_compatibles_lcds___displays_i2cwire_t.jpeg?1677080320)

- [Next Page](https://learn.adafruit.com/i2c-spi-lcd-backpack/pinouts.md)

## Primary Products

### i2c / SPI character LCD backpack - STEMMA QT / Qwiic

[i2c / SPI character LCD backpack - STEMMA QT / Qwiic](https://www.adafruit.com/product/292)
Character LCDs are a fun and easy way to have your microcontroller project talk back to you. They are also common, and easy to get, available in tons of colors and sizes. [We've written tutorials on using character LCDs with an Arduino](http://learn.adafruit.com/character-lcds)...

In Stock
[Buy Now](https://www.adafruit.com/product/292)
[Related Guides to the Product](https://learn.adafruit.com/products/292/guides)

## Featured Products

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

## Related Guides

- [ Faz-Wrench - Five Nights at Freddy's](https://learn.adafruit.com/faz-wrench.md)
- [Trinket Ultrasonic Rangefinder](https://learn.adafruit.com/trinket-ultrasonic-rangefinder.md)
- [No-Code Indoor Air Quality Monitor with Separate Display](https://learn.adafruit.com/no-code-indoor-air-quality-monitor-with-separate-display.md)
- [Trinket Temperature & Humidity LCD Display](https://learn.adafruit.com/trinket-temperature-humidity-lcd-display.md)
- [Light Meter](https://learn.adafruit.com/light-meter.md)
- [CircuitPython Hardware: ILI9341 TFT & FeatherWing](https://learn.adafruit.com/micropython-hardware-ili9341-tft-and-featherwing.md)
- [Raspberry Pi Thermal Camera](https://learn.adafruit.com/raspberry-pi-thermal-camera.md)
- [Adafruit NeoKey BFF](https://learn.adafruit.com/adafruit-neokey-bff.md)
- [Mini LED Matrix Audio Visualizer](https://learn.adafruit.com/mini-led-matrix-audio-visualizer.md)
- [Adafruit ISO1540 Bidirectional I2C Isolator](https://learn.adafruit.com/adafruit-iso1540-bidirectional-i2c-isolator.md)
- [Raspberry Pi Low-Light Long-Exposure Photography](https://learn.adafruit.com/raspberry-pi-hq-camera-low-light-long-exposure-photography.md)
- [Adafruit Radio Bonnets with OLED Display - RFM69 or RFM9X](https://learn.adafruit.com/adafruit-radio-bonnets.md)
- [PicoDVI Arduino Library: Video Out for RP2040 Boards](https://learn.adafruit.com/picodvi-arduino-library-video-out-for-rp2040-boards.md)
- [reef-pi Guide 5: Light Controller](https://learn.adafruit.com/reef-pi-lighting-controller.md)
- [Adafruit VL53L4CD Time of Flight Distance Sensor](https://learn.adafruit.com/adafruit-vl53l4cd-time-of-flight-distance-sensor.md)
