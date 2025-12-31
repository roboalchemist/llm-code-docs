# Source: https://learn.adafruit.com/adafruit-gfx-graphics-library/coordinate-system-and-units.md

# Adafruit GFX Graphics Library

## Coordinate System and Units

Pixels — picture elements, the blocks comprising a digital image — are addressed by their horizontal (X) and vertical (Y) coordinates. The coordinate system places the origin (0,0) at the top left corner, with positive X increasing to the right and positive Y increasing downward. This is upside-down relative to the standard Cartesian coordinate system of mathematics, but is established practice in many computer graphics systems (a throwback to the days of raster-scan CRT graphics, which worked top-to-bottom). To use a tall “portrait” layout rather than wide “landscape” format, or if physical constraints dictate the orientation of a display in an enclosure, one of four rotation settings can also be applied, indicating which corner of the display represents the top left.

Also unlike the mathematical Cartesian coordinate system, points here have dimension — they are always one full integer pixel wide and tall.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/264/medium800/lcds___displays_coordsys.png?1396770439)

Coordinates are always expressed in pixel units; there is no implicit scale to a real-world measure like millimeters or inches, and the size of a displayed graphic will be a function of that specific display’s&nbsp;_dot pitch_&nbsp;or pixel density. If you’re aiming for a real-world dimension, you’ll need to scale your coordinates to suit. Dot pitch can often be found in the device datasheet, or by measuring the screen width and dividing the number of pixels across by this measurement.

The library will safely “clip” any graphics drawn off the edges of the screen. In fact this is done on purpose sometimes, as with scrolling text displays.

For color-capable displays, colors are represented as unsigned 16-bit values. Some displays may physically be capable of more or fewer bits than this, but the library operates with 16-bit values…these are easy for the Arduino to work with while also providing a consistent data type across all the different displays. The primary color components — red, green and blue — are all “packed” into a single 16-bit variable, with the most significant 5 bits conveying red, middle 6 bits conveying green, and least significant 5 bits conveying blue. That extra bit is assigned to green because our eyes are most sensitive to green light.&nbsp;_Science!_

&nbsp;

![](https://cdn-learn.adafruit.com/assets/assets/000/001/265/medium800/lcds___displays_colorpack.png?1396770449)

For the most common primary and secondary colors, we have this handy cheat-sheet that you can include in your own code. Of course, you can pick any of 65,536 different colors, but this basic list may be easiest when starting out:

```
// Color definitions
#define BLACK    0x0000
#define BLUE     0x001F
#define RED      0xF800
#define GREEN    0x07E0
#define CYAN     0x07FF
#define MAGENTA  0xF81F
#define YELLOW   0xFFE0 
#define WHITE    0xFFFF
```

Elsewhere: [here’s a detailed explanation of 16-bit “RGB565” colors](http://www.barth-dev.de/online/rgb565-color-picker/) that includes an interactive color picker (not compatible with all browsers).

For monochrome (single-color) displays, colors are always specified as simply&nbsp;1&nbsp;(set) or&nbsp;0&nbsp;(clear). The semantics of set/clear are specific to the type of display: with something like a luminous OLED display, a “set” pixel is lighted, whereas with a reflective LCD display, a “set” pixel is typically dark. There may be exceptions, but generally you can count on&nbsp;0&nbsp;(clear) representing the default background state for a freshly-initialized display, whatever that works out to be.

- [Previous Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/overview.md)
- [Next Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/graphics-primitives.md)

## Related Guides

- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
- [2.8" TFT Touchscreen](https://learn.adafruit.com/2-8-tft-touchscreen.md)
- [Adafruit 1.28" 240x240 Round TFT LCD](https://learn.adafruit.com/adafruit-1-28-240x240-round-tft-lcd.md)
- [Adafruit MacroPad RP2040](https://learn.adafruit.com/adafruit-macropad-rp2040.md)
- [USB + Serial RGB Backlight Character LCD Backpack](https://learn.adafruit.com/usb-plus-serial-backpack.md)
- [I2C/SPI LCD Backpack](https://learn.adafruit.com/i2c-spi-lcd-backpack.md)
- [Adafruit Grayscale 1.5" 128x128 OLED Display](https://learn.adafruit.com/adafruit-grayscale-1-5-128x128-oled-display.md)
- [Generating Text with ChatGPT, Pico W & CircuitPython](https://learn.adafruit.com/generating-text-with-chatgpt-pico-w-circuitpython.md)
- [HalloWing Flapping Bat](https://learn.adafruit.com/hallowing-flapping-bat.md)
- [CircuitPython OLED and Dual Knob Sketcher](https://learn.adafruit.com/circuitpython-oled-knob-sketcher.md)
- [Adafruit IO IOT Hub with the Adafruit FunHouse](https://learn.adafruit.com/adafruit-io-hub-with-the-adafruit-funhouse.md)
- [Adafruit 16x2 Character LCD + Keypad for Raspberry Pi](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi.md)
- [CircuitPython Hardware: SSD1306 OLED Display](https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display.md)
- [Adafruit 128x64 OLED FeatherWing ](https://learn.adafruit.com/adafruit-128x64-oled-featherwing.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
