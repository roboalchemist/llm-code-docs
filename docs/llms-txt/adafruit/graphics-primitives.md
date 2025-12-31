# Source: https://learn.adafruit.com/adafruit-gfx-graphics-library/graphics-primitives.md

# Adafruit GFX Graphics Library

## Graphics Primitives

Each device-specific display library will have its own constructors and initialization functions. These are documented in the individual tutorials for each display type, or oftentimes are evident in the specific library header file. The remainder of this tutorial covers the common graphics functions that work the same regardless of the display type.  
  
The function descriptions below are merely&nbsp;_prototypes_&nbsp;— there’s an assumption that a display object is declared and initialized as needed by the device-specific library. Look at the example code with each library to see it in actual use. For example, **where we show&nbsp;print(1234.56), your actual code would place the object name before this, e.g. it might read&nbsp;screen.print(1234.56)**&nbsp;(if you have declared your display object with the name&nbsp;screen).

## Drawing pixels (points)

First up is the most basic pixel pusher. You can call this with X, Y coordinates and a color and it will make a single dot:

```
void drawPixel(uint16_t x, uint16_t y, uint16_t color);
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/267/medium800/lcds___displays_st7735pixel.jpg?1396770465)

## Drawing lines

You can also draw lines, with a starting and end point and color:

```
void drawLine(uint16_t x0, uint16_t y0, uint16_t x1, uint16_t y1, uint16_t color);
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/268/medium800/lcds___displays_line.png?1396770476)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/269/medium800/lcds___displays_st7735lines.jpg?1396770485)

For horizontal or vertical lines, there are optimized line-drawing functions that avoid the angular calculations:

```
void drawFastVLine(uint16_t x0, uint16_t y0, uint16_t length, uint16_t color);
void drawFastHLine(uint8_t x0, uint8_t y0, uint8_t length, uint16_t color);
```

## Rectangles

Next up, rectangles and squares can be drawn and filled using the following procedures. Each accepts an X, Y pair for the top-left corner of the rectangle, a width and height (in pixels), and a color.&nbsp;drawRect()&nbsp;renders just the frame (outline) of the rectangle — the interior is unaffected — while&nbsp;fillRect()&nbsp;fills the entire area with a given color:

```
void drawRect(uint16_t x0, uint16_t y0, uint16_t w, uint16_t h, uint16_t color);
void fillRect(uint16_t x0, uint16_t y0, uint16_t w, uint16_t h, uint16_t color);
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/270/medium800/lcds___displays_rect.png?1396770497)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/271/medium800/lcds___displays_st7735squares.jpg?1396770504)

To create a solid rectangle with a contrasting outline, use fillRect() first, then drawRect() over it.

## Circles

Likewise, for circles, you can draw and fill. Each function accepts an X, Y pair for the center point, a radius in pixels, and a color:

```
void drawCircle(uint16_t x0, uint16_t y0, uint16_t r, uint16_t color);
void fillCircle(uint16_t x0, uint16_t y0, uint16_t r, uint16_t color);
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/272/medium800/lcds___displays_circle.png?1396770516)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/273/medium800/lcds___displays_st7735circles.jpg?1396770524)

## Rounded rectangles

For rectangles with rounded corners, both draw and fill functions are again available. Each begins with an X, Y, width and height (just like normal rectangles), then there’s a corner radius (in pixels) and finally the color value:

```
void drawRoundRect(uint16_t x0, uint16_t y0, uint16_t w, uint16_t h, uint16_t radius, uint16_t color);
void fillRoundRect(uint16_t x0, uint16_t y0, uint16_t w, uint16_t h, uint16_t radius, uint16_t color);
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/274/medium800/lcds___displays_roundrect.png?1396770535)

Here’s an added bonus trick: because the circle functions are always drawn relative to a center pixel, the resulting circle diameter will always be an odd number of pixels. If an even-sized circle is required (which would place the center point&nbsp;_between_&nbsp;pixels), this can be achieved using one of the rounded rectangle functions: pass an identical width and height that are even values, and a corner radius that’s exactly half this value.

## Triangles

With triangles, once again there are the draw and fill functions. Each requires a full seven parameters: the X, Y coordinates for three corner points defining the triangle, followed by a color:

```
void drawTriangle(uint16_t x0, uint16_t y0, uint16_t x1, uint16_t y1, uint16_t x2, uint16_t y2, uint16_t color);
void fillTriangle(uint16_t x0, uint16_t y0, uint16_t x1, uint16_t y1, uint16_t x2, uint16_t y2, uint16_t color);
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/275/medium800/lcds___displays_triangle.png?1396770547)

## Characters and text

There are two basic string drawing procedures for adding text. The first is just for a single character. You can place this character at any location and with any color. An optional size parameter can be passed which scales the font by this factor (e.g. size=2 will render the default font at 10x16 pixels per character). It’s a little blocky that way but having just a single font helps keep the program size down.

```
void drawChar(uint16_t x, uint16_t y, char c, uint16_t color, uint16_t bg, uint8_t size);
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/276/medium800/lcds___displays_char.png?1396770557)

Text is very flexible but operates a bit differently. Instead of one procedure, the text size, color and position are set up in separate functions and then the print() function is used — this makes it easy and provides all of the same string and number formatting capabilities of [Arduino’s familiar Serial.print() and println() functions](https://www.arduino.cc/reference/en/language/functions/communication/serial/print/)! But you precede these with the display object instead of Serial.

```auto
void setCursor(int16_t x0, int16_t y0);
void setTextColor(uint16_t color);
void setTextColor(uint16_t color, uint16_t backgroundcolor);
void setTextSize(uint8_t size);
void setTextWrap(boolean w);
```

Begin with&nbsp;setCursor(x, y), which will place the top left corner of the text wherever you please. Initially this is set to (0,0) (the top-left corner of the screen). Then set the text color with&nbsp;setTextColor(color)&nbsp;— by default this is white. Text is normally drawn “clear” — the open parts of each character show the original background contents, but if you want the text to block out what’s underneath, a background color can be specified as an optional second parameter to setTextColor(). Finally,&nbsp;setTextSize(size)&nbsp;will multiply the scale of the text by a given integer factor. Below you can see scales of 1 (the default), 2 and 3. It appears blocky at larger sizes because we only ship the library with a single simple font, to save space.

Warning: For some OLED displays, 'display.setTextColor(WHITE, BLACK);' seems to work better than specifying 'display.setTextColor(0xFFFFFF, 0x000000);'

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/277/medium800/lcds___displays_text.jpg?1396770564)

After setting everything up, you can use&nbsp;print()&nbsp;or&nbsp;println()&nbsp;—&nbsp;_just like you do with [Serial printing](https://www.arduino.cc/reference/en/language/functions/communication/serial/print/)!_&nbsp;For example, to print a string, use&nbsp;print("Hello world")&nbsp;- that’s the first line of the image above. You can also use&nbsp;print()&nbsp;for numbers and variables — the second line above is the output of print(1234.56)&nbsp;and the third line is&nbsp;print(0xDEADBEEF, HEX).

By default, long lines of text are set to automatically “wrap” back to the leftmost column. To override this behavior (so text will run off the right side of the display — useful for scrolling marquee effects), use setTextWrap(false). The normal wrapping behavior is restored with setTextWrap(true).

## Extended Characters, CP437 and a Lurking Bug

The standard built-in font includes a number of symbols and accented characters outside the normal letters and numbers you’d use in print() strings. These can be accessed with drawChar(), passing an 8-bit value (0–255, though commonly expressed in hexadecimal, 0x00–0xFF) for the third argument.

The built-in font is based on the original IBM PC character set, known as [_Code Page 437_ (CP437 for short)](https://en.wikipedia.org/wiki/Code_page_437). Many embedded systems still use this as it’s compact and well established.

Years ago, when originally transcribing CP437 into the GFX library, one symbol was accidentally omitted. Nothing fatal, code runs fine, but _every subsequent symbol was then off by one_ compared to the “real” CP437 character set. By the time this was discovered, _so much code had been written_ — projects shared online but also in fixed media like books and magazines — that fixing the bug would _break every existing project that relied on those extended characters!_

So the error has been left in place, on purpose, but this creates a different issue if one is adapting code from elsewhere that relies on the _correct_ CP437 symbol values.

A compromise solution is a function that enables or disables the “real” CP437 sequence. **By default this is off,** the off-by-one order is used, so that all the old GFX projects in books work without modification. The correct order can be enabled with:

```auto
display.cp437(true);
```

Unless you need to switch back and forth, this typically only needs to be done one time, in the `setup()` function.

Here’s a map of the built-in character set, both the standard erroneous version, and the corrected version used when one calls `cp437(true)`. Notice this only affects the last five rows of symbols; everything prior to character 0xB0 is unaffected:

![](https://cdn-learn.adafruit.com/assets/assets/000/103/682/medium800/graphic_lcds_gfx-cp437-bug.png?1627933765)

_The presence of the extended Code Page 437 symbols is only guaranteed in the built-in font. Custom fonts (explained elsewhere) rarely include these._

Extended characters typically can’t be directly printed in code; most editors may support _Unicode_ strings but this _does not directly map to CP437._ Typically one calls the `write()` function with individual character numbers. The GFX library harkens back to an earlier time when Unicode support was not widespread.

Consider the German word _Schön_ (beautiful). One might print this like so:

```cpp
display.cp437(true);   // Use correct CP437 character codes
display.print("Scho"); // Print the plain ASCII first part
display.write(0x94);   // Print the o-with-umlauts
display.println("n");  // Print the last part
```

Likewise with accessing the math symbols…

```cpp
display.cp437(true);  // Use correct CP437 character codes
display.print("Temperature: ");
display.print(number);
display.write(0xF8);  // Print the degrees symbol
display.println();    // New line
```

Compiler support for _some_ (not all) 32-bit microcontrollers provides the `printf()` function, which can allow these characters to be placed inline via the `%c` (character) formatting identifier:

```auto
display.cp437(true);
display.printf("Temperature: %d%c\n", number, 0xF8);
display.printf("Sch%cn\n", 0x94);
```

This is nice and compact but _isn’t compatible with all microcontrollers,_ certainly not early Arduino Uno-class devices, so consider how you might be sharing code and use it with care.

**See the “[Using Fonts](../../../../adafruit-gfx-graphics-library/using-fonts)” page for additional text features in the latest GFX library.**

## Bitmaps

You can draw small monochrome (single color) bitmaps, good for sprites and other mini-animations or icons:

```
void drawBitmap(int16_t x, int16_t y, uint8_t *bitmap, int16_t w, int16_t h, uint16_t color);
```

This issues a contiguous block of bits to the display, where each '1' bit sets the corresponding pixel to 'color,' while each '0' bit is skipped. x, y is the top-left corner where the bitmap is drawn, w, h are the width and height in pixels.

The bitmap data _must_ be located in program memory using the PROGMEM directive. This is a somewhat advanced function and beginners are best advised to come back to this later. For an introduction, see the&nbsp;[Arduino tutorial on PROGMEM usage](http://arduino.cc/en/Reference/PROGMEM).

**[Here's a handy webtool for generating bitmap -\> memorymaps](http://javl.github.io/image2cpp/)**

## Clearing or filling the screen

The fillScreen() function will set the entire display to a given color, erasing any existing content:

```
void fillScreen(uint16_t color);
```

## Hardware-Specific functions

Some displays may have unique features like screen invert or hardware-based scrolling. Documentation for those functions can be found in the corresponding display-specific guide. Since these are not common features across all GFX-compatible displays, they are not described here.

- [Previous Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/coordinate-system-and-units.md)
- [Next Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/rotating-the-display.md)

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
