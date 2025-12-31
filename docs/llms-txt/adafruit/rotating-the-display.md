# Source: https://learn.adafruit.com/adafruit-gfx-graphics-library/rotating-the-display.md

# Adafruit GFX Graphics Library

## Rotating the Display

You can also rotate your drawing. Note that this will _not_ rotate what you already drew, but it will change the coordinate system for any new drawing. This can be really handy if you had to turn your board or display sideways or upside down to fit in a particular enclosure. In most cases this only needs to be done once, inside setup().

We can only rotate 0, 90, 180 or 270 degrees - anything else is not possible in hardware and is too taxing for an Arduino to calculate in software  

![](https://cdn-learn.adafruit.com/assets/assets/000/001/266/medium800/lcds___displays_rotated.jpg?1396770456)

```
void setRotation(uint8_t rotation);
```

The **rotation** parameter can be **0** , **1** , **2** or **3**. For displays that are part of an Arduino shield, rotation value 0 sets the display to a _portrait_ (tall) mode, with the USB jack at the top right. Rotation value 2 is also a portrait mode, with the USB jack at the bottom left. Rotation 1 is _landscape_ (wide) mode, with the USB jack at the bottom right, while rotation 3 is also landscape, but with the USB jack at the top left.

For other displays, please try all 4 rotations to figure out how they end up rotating as the alignment will vary depending on each display, in general the rotations move counter-clockwise

When rotating, the origin point (0,0) changes — the idea is that it should be arranged at the top-left of the display for the other graphics functions to make consistent sense (and match all the function descriptions above).

If you need to reference the size of the screen (which will change between portrait and landscape modes), use width() and height().

```
uint16_t width(); 
uint16_t height();
```

Each returns the dimension (in pixels) of the corresponding axis, adjusted for the display’s current rotation setting.

- [Previous Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/graphics-primitives.md)
- [Next Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/using-fonts.md)

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
