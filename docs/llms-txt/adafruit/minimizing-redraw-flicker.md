# Source: https://learn.adafruit.com/adafruit-gfx-graphics-library/minimizing-redraw-flicker.md

# Adafruit GFX Graphics Library

## Minimizing Redraw Flicker

A common need in microcontroller projects is to **redraw all or part of a screen** , such as when showing **live readings from a sensor**. The least-code approach to this usually is to **erase** all or part of the screen (using `fillScreen()` or `fillRect()`) and **re-draw** everything in the affected area. This does the job, but the off-and-on appearance can be distracting, especially if these redraws occur frequently and it becomes a steady flicker.

This isn’t true of _all_ GFX-compatible devices. Some displays (most LED matrices and some monochrome OLED screens) don’t refresh until there’s specifically a `show()`, `display()` or `update()` call in one’s code (depending on the library), so this flicker is minimized or doesn’t occur. Mostly it’s an issue with color LCD or OLED screens, where graphics are rendered with every function call.

There are a couple of approaches one can use to minimize this effect. The first (and usually easiest) is suited to the **standard fixed-size GFX font** and is best for **Arduino Uno** and other memory-constrained microcontrollers. The other applies to **custom fonts and any other graphics primitives** , and is best for&nbsp;modern 32-bit microcontrollers with **ample RAM** &nbsp;(thought may still work on Uno for very small updates).

## Overwriting Text with the Built-In Font

This first method relies on the fact that the standard built-in font has uniformly-sized characters; it’s sometimes referred to as the “5 by 7” pixel font (though really 6x8 pixels to allow at least 1 pixel between adjacent characters, and for descenders on some lowercase characters like “g” or “p”). Then…

The `setTextColor()` function, which normally accepts a single argument (a color to use for subsequent text printing), can optionally accept a _second_ argument—a “background color” that applies to every pixel in the 6x8 box that’s _not_ part of the character shape. Normally each character box is transparent and only “foreground” pixels are set.

```cpp
display.setTextColor(foreground, background);
```

Here’s how that might be used in an Arduino sketch.&nbsp;Understand that **this is not a complete program** because **every type of display has a distinct setup procedure**.&nbsp;Complete examples for PyPortal are given at the bottom of this page, providing a starting point that can be adapted to other screen types.&nbsp;Look at the “graphicstest” example that accompanies most GFX-compatible libraries for insights.

```cpp
// This is an incomplete Arduino example to minimally show
// the text overwrite approach. A real program would #include
// a display library header and declare a global 'display'.

void setup() {
  // Likewise, display initialization would take place here.

  // On color LCDs, this is white text on black background:
  display.setTextColor(0xFFFF, 0x0000);
  // On monochrome OLEDs, these might be 1 and 0 instead.
}

void loop() {
  display.setCursor(0, 0); // Position at top-left corner
  display.print("Hello");  // Print a message
  delay(1000);             // Pause 1 second
  display.setCursor(0, 0); // Back to top-left corner
  display.print("World");  // Print another message, same length
  delay(1000);             // Pause 1 second
}
```

The sketch alternately prints “Hello” and “World” at the top-left corner of the screen; each pass erases the text that came before, there’s no need to explicitly erase that area. (Try removing the second argument to `setTextColor()` and watch what happens.)

This works because both messages are the same 5-character length (30x7 pixels at the default text size, 60x14 at size 2 and so forth). If the messages are different lengths, it’s necessary to **_pad_** a string with extra spaces to overwrite the old text underneath.

One way to do this is by declaring a **fixed-size character buffer** and then using C’s _formatted output_ via the `sprintf()` function. Let’s suppose a project will need up to 10 characters for each message. We begin by declaring a char array with **11** elements,&nbsp;because C strings _require_ a trailing NUL (0) byte at the end:

```cpp
char buf[11]; // 10 characters + NUL
```

Then we _format_ a string into that buffer using `sprintf()` (string-print-formatted), some examples of which could include:

```cpp
sprintf(buf, "%-10s", "Hello"); // Left-justified message
sprintf(buf, "%10s", "World");  // Right-justified message
sprintf(buf, "%10d", 42);       // Right-justified integer
```

And the buffer can then be passed to the normal `print()` or `println()` functions:

```auto
display.setCursor(x, y);
display.print(buf);
```

`sprintf()` has near infinite variety so we can’t give every possible example here. Since it’s a standard part of the C language, just searching around for “C formatted output” or just “sprintf” will turn up plenty of references. It’s quite potent! Note however that the Arduino implementation is somewhat scaled back to fit on a microcontroller; formatting floating-point values this way is not supported, for example.

The counterpoint to using `sprintf()` is one of those _great power, great responsibility_ lessons. String and memory handling in C (and thus C++, and thus the whole Arduino ecosystem) is simplistic, and there’s nothing in place…other than your own self-discipline, you _hope…_to prevent exceeding the length of that `char` array, writing data willy-nilly into other RAM and leading to unexpected behavior or program crashes.

One approach to overwriting floating-point values is to use the normal Arduino `print()` function to the display, which accepts an optional argument specifying the number of digits after the decimal point, so the output is always the same size:

```cpp
float value = 3.14159;
display.print(value, 5); // Will ALWAYS be extended to X.XXXXX, even if 0's
```

Another approach, if numbers or messages to print may **vary in length** , is just to follow up with enough spaces to cover up any change in the number of characters. But this relies on there not being any other _stuff_ toward the right edge of the screen and isn’t suited to every situation:

```cpp
int value = 42;
display.setTextWrap(false); // Allow spaces to go off right edge
display.setCursor(0, 0);
display.print(value);
display.print("      ");    // Cover anything previously in this space
```

## Restoring Normal Text Drawing

To turn this off and draw normal “transparent” text, call `setTextColor()` with just the foreground color argument:

```cpp
display.setTextColor(foreground);
```

## Overwriting Text or Graphics Using an _Offscreen Canvas_

The above method has some advantages in that it requires minimal modification to existing programs—something that prints _once_ is easily adapted to print _repeatedly_—and that it&nbsp;fits well within modest microcontrollers like the Arduino Uno.

Where it _doesn’t_ work is with **custom fonts** , or with non-text elements like graphics or indicators.&nbsp;In fact, the optional second argument to `setTextColor()` (the background color) is simply _ignored_ when using custom fonts. This is on purpose and by design!&nbsp;With proportionally-spaced fonts, _strings will occupy different-sized regions,_ even if they contain the same number of characters…the overwrite technique simply can’t be relied on.

The method explained here uses some extra RAM. Most 32-bit microcontrollers have ample capacity for this, but the classic Uno may struggle in all but the simplest cases.

The GFX library can provide an _ **offscreen canvas.** _ It works just like drawing to a screen…except there’s no screen, just a grid of pixels in memory. The canvas can then be passed to another function (explained later), which _does_ draw it to the screen.

Flicker-free redraw then works like this:

- Create a canvas object; usually done just once, at program startup
- Then, each time a screen update is needed:
  - Clear the canvas
  - Print text or draw shapes to the canvas
  - Copy the canvas to the screen

A canvas _doesn’t_ need to match the size of the screen; if you’re just updating a rectangle, it only needs to be that size. That’s important because every pixel takes a little RAM. Also a program can have more than one canvas if needed.

There are different canvas _depths_ for 1, 8 and 16-bit color. We’ll focus on just 1 and 16 here; the 8-bit case is seldom seen.

The 1-bit canvas type—`GFXcanvas1`—provides two colors; _foreground and background,_ or _foreground and transparent,_ much like working with the built-in font and `setTextColor()`. For most single-color things like text, this is what you’d use.

A canvas might be declared in the global part of one’s sketch, before the `setup()` function, like so:

```auto
GFXcanvas1 canvas(width, height);
```

_width_ and _height_ should be the canvas dimensions, in pixels. Each pixel requires 1 bit of RAM…so for instance, 120x30 pixels = 3,600 bits = 450 bytes…plus a couple dozen bytes overhead for the `GFXcanvas1` structure itself.&nbsp;A single small canvas like that can _usually_ work in the modest 1.5K of an Arduino Uno, but complex programs, larger or multiple canvases, or color (explained later) require more capable devices.

Canvases use all the same drawing functions as normally provided by the GFX library. So, where one might use&nbsp;`display.fillScreen(0)` before, one can use `canvas.fillScreen(0)` instead (though the canvas is not a _screen,_ it’s helpful to keep the names uniform across everything). This applies to all the pixel, shape and text-drawing functions. With a `GFXcanvas1` object, drawing colors must be 1 (foreground or “set” pixel) or 0 (background or “clear” pixel).

So the idea here is to just wipe and redraw the _entire contents of the canvas_ each time a redraw is needed.&nbsp;Although GFX provides the `getTextBounds()` function, it just isn’t necessary to go to such fuss to be “optimal”—canvases are already super quick to work with.

As before, this example is incomplete and just highlights the important ideas here. A full working example for PyPortal (and adaptable to other screens) is given at the bottom of the page.

```cpp
// This is an incomplete Arduino example to minimally show
// the canvas drawing approach. A real program would #include
// a display library header and declare a global 'display',
// also including and enabling a custom font.

// Then, in ADDITION to all that, there's...
GFXcanvas1 canvas(120, 30); // 1-bit, 120x30 pixels

void setup() {
  // Display init and font select would take place here.
  // See later examples for that.

  // Text might exceed width of canvas, so disable wrapping:
  canvas.setTextWrap(false);
}

void loop() {
  canvas.fillScreen(0);    // Clear canvas (not display)
  canvas.setCursor(0, 24); // Pos. is BASE LINE when using fonts!
  canvas.print(millis());  // Print elapsed time in milliseconds
  // Copy canvas to screen at upper-left corner. As written here,
  // assumes a color LCD, hence the color values of 0xFFFF (white)
  // for foreground, 0x0000 (black) for background. Mono OLED can
  // use 1 and 0. BOTH colors must be specified to overwrite the
  // prior screen contents there.
  display.drawBitmap(0, 0, canvas.getBuffer(),
    canvas.width(), canvas.height(), 0xFFFF, 0x0000);
}
```

Notice how the fill, cursor and print operations are all performed on the `canvas` object, but the bitmap-drawing operation is done on the `display` object. It’s easy to confuse these; if something like a custom font doesn’t seem to be working, confirm you’ve set that for the canvas, not the display!

Because GFX “clips” graphics drawn to the canvas, this can be used for interesting effects like scrolling text within a rectangle in one section of a screen.

If you have multiple numbers or areas of the screen to update, _and_ these are all the same dimensions, a single canvas can be re-used among them; it’s not always necessary to allocate multiple distinct canvases, unless the size varies.

`drawBitmap()` works with all display types; the same function can be used with a `GFXcanvas1` regardless whether the screen is a 16-bit color TFT display or a black-and-white OLED.

## A Color Canvas

The 16-bit canvas type—`GFXcanvas16`—works much like a 16-bit LCD screen. Instead of foreground and background (or transparent) colors, one has the _whole 64K gamut of colors_ to work with. If you’re _only_ planning to draw text, you probably don’t need this, a `GFXcanvas1` will suffice, and you can specify any single color when copying to the display.

Like the 1-bit variety, this can be declared&nbsp;in the global part of one’s sketch, before the `setup()` function:

```auto
GFXcanvas16 canvas(width, height);
```

Unlike the 1-bit variety, `GFXcanvas16` uses _inordinate_ RAM; 2 bytes per pixel. That 120x30 pixel example from earlier now requires **7,200 bytes** …_way_ beyond the reach of the Arduino Uno’s 1.5K RAM, but practical for more modern microcontrollers to handle.

There are some differences when copying a color canvas to the screen. First, one now uses the `drawRGBBitmap()` function, which accepts mostly the same arguments but omits the foreground and background colors (since the canvas itself is now full color):

```auto
display.drawRGBBitmap(0, 0, canvas.getBuffer(), canvas.width(), canvas.height());
```

Second, `drawRGBBitmap()` _only_ works on color screens, unlike `drawBitmap()` which works across all display types. Color reduction is a subjective process and would incur a _lot_ of extra code, so this capability was omitted. Best to pair monochrome screens with `GFXcanvas1` instead.

## Examples

Here’s the simple “text overwrite” example as written for PyPortal. This could be adapted to other screens by changing the display declaration and initialization; see the “graphicstest” example that accompanies most display libraries.

```auto
// Simple (text overwrite) flicker-free example for PyPortal

#include &lt;Adafruit_GFX.h&gt;
#include &lt;Adafruit_ILI9341.h&gt;

#define TFT_D0        34 // Data bit 0 pin (MUST be on PORT byte boundary)
#define TFT_WR        26 // Write-strobe pin (CCL-inverted timer output)
#define TFT_DC        10 // Data/command pin
#define TFT_CS        11 // Chip-select pin
#define TFT_RST       24 // Reset pin
#define TFT_RD         9 // Read-strobe pin
#define TFT_BACKLIGHT 25

// ILI9341 screen with 8-bit parallel interface:
Adafruit_ILI9341 display(tft8bitbus, TFT_D0, TFT_WR, TFT_DC, TFT_CS, TFT_RST, TFT_RD);

void setup() {
  pinMode(TFT_BACKLIGHT, OUTPUT);       // PyPortal requires
  digitalWrite(TFT_BACKLIGHT, HIGH);    // turning on backlight

  display.begin();                      // Initialize and
  display.fillScreen(0x0000);           // clear display

  display.setTextColor(0xFFFF, 0x0000); // White text, black background
  display.setTextSize(2);               // 2X size text
}

void loop(void) {
  display.setCursor(0, 0); // Position at top-left corner
  display.print("Hello");  // Print a message
  delay(1000);             // Pause 1 second
  display.setCursor(0, 0); // Back to top-left corner
  display.print("World");  // Print another message, same length
  delay(1000);             // Pause 1 second
}
```

And here’s a “1-bit canvas”&nbsp;example as written for PyPortal, using a large and friendly font. Again, this could be adapted to other screens by changing the display declaration and initialization; see the “graphicstest” example that accompanies most display libraries.

```auto
// Fancy (offscreen canvas) flicker-free example for PyPortal

#include &lt;Adafruit_GFX.h&gt;
#include &lt;Adafruit_ILI9341.h&gt;
#include &lt;Fonts/FreeSerifBold18pt7b.h&gt;

#define TFT_D0        34 // Data bit 0 pin (MUST be on PORT byte boundary)
#define TFT_WR        26 // Write-strobe pin (CCL-inverted timer output)
#define TFT_DC        10 // Data/command pin
#define TFT_CS        11 // Chip-select pin
#define TFT_RST       24 // Reset pin
#define TFT_RD         9 // Read-strobe pin
#define TFT_BACKLIGHT 25

// ILI9341 screen with 8-bit parallel interface:
Adafruit_ILI9341 display(tft8bitbus, TFT_D0, TFT_WR, TFT_DC, TFT_CS, TFT_RST, TFT_RD);

GFXcanvas1 canvas(120, 30); // 1-bit, 120x30 pixels

void setup() {
  pinMode(TFT_BACKLIGHT, OUTPUT);       // PyPortal requires
  digitalWrite(TFT_BACKLIGHT, HIGH);    // turning on backlight

  display.begin();                      // Initialize and
  display.fillScreen(0x0000);           // clear display

  canvas.setFont(&amp;FreeSerifBold18pt7b); // Use custom font and
  canvas.setTextWrap(false);            // clip text to canvas
}

void loop(void) {
  canvas.fillScreen(0);    // Clear canvas (not display)
  canvas.setCursor(0, 24); // Pos. is BASE LINE when using fonts!
  canvas.print(millis());  // Print elapsed time in milliseconds
  // Copy canvas to screen at upper-left corner. As written here,
  // assumes a color LCD, hence the color values of 0xFFFF (white)
  // for foreground, 0x0000 (black) for background. Mono OLED can
  // use 1 and 0. BOTH colors must be specified to overwrite the
  // prior screen contents there.
  display.drawBitmap(0, 0, canvas.getBuffer(),
    canvas.width(), canvas.height(), 0xFFFF, 0x0000);
}
```

Once more, using a 16-bit canvas instead. This example doesn’t make good use of color in the canvas—it’s still just white text on a black background—and is mostly just to show how the drawing syntax is a little different.

```auto
// Fancy (offscreen color canvas) flicker-free example for PyPortal

#include &lt;Adafruit_GFX.h&gt;
#include &lt;Adafruit_ILI9341.h&gt;
#include &lt;Fonts/FreeSerifBold18pt7b.h&gt;

#define TFT_D0        34 // Data bit 0 pin (MUST be on PORT byte boundary)
#define TFT_WR        26 // Write-strobe pin (CCL-inverted timer output)
#define TFT_DC        10 // Data/command pin
#define TFT_CS        11 // Chip-select pin
#define TFT_RST       24 // Reset pin
#define TFT_RD         9 // Read-strobe pin
#define TFT_BACKLIGHT 25

// ILI9341 screen with 8-bit parallel interface:
Adafruit_ILI9341 display(tft8bitbus, TFT_D0, TFT_WR, TFT_DC, TFT_CS, TFT_RST, TFT_RD);

GFXcanvas16 canvas(120, 30); // 16-bit, 120x30 pixels

void setup() {
  pinMode(TFT_BACKLIGHT, OUTPUT);       // PyPortal requires
  digitalWrite(TFT_BACKLIGHT, HIGH);    // turning on backlight

  display.begin();                      // Initialize and
  display.fillScreen(0x0000);           // clear display

  canvas.setFont(&amp;FreeSerifBold18pt7b); // Use custom font
  canvas.setTextWrap(false);            // Clip text within canvas
}

void loop(void) {
  canvas.fillScreen(0x0000); // Clear canvas (not display)
  canvas.setCursor(0, 24);   // Pos. is BASE LINE when using fonts!
  canvas.print(millis());    // Print elapsed time in milliseconds
  // Copy canvas to screen at upper-left corner.
  display.drawRGBBitmap(0, 0, canvas.getBuffer(), canvas.width(), canvas.height());
}
```

- [Previous Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/loading-images.md)

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
