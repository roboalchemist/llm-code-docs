# Source: https://learn.adafruit.com/adafruit-gfx-graphics-library/using-fonts.md

# Adafruit GFX Graphics Library

## Using Fonts

More recent versions of the Adafruit GFX library offer the ability to use alternate fonts besides the one standard fixed-size and -spaced face that’s built in. Several&nbsp;alternate fonts are included, plus there’s the ability to add new ones.

The included fonts are derived from the [GNU FreeFont](https://www.gnu.org/software/freefont/)&nbsp;project. There are three faces: “Serif” (reminiscent of Times New Roman), “Sans” (reminiscent of Helvetica or Arial) and “Mono” (reminiscent of Courier). Each is available in a few styles (bold, italic, etc.) and sizes. The included fonts are in a bitmap format, not scalable vectors, as it needs to work within the limitations of a small microcontroller.

![lcds___displays_specimens.png](https://cdn-learn.adafruit.com/assets/assets/000/029/279/medium640/lcds___displays_specimens.png?1450832251)

Located inside the “Fonts” folder inside Adafruit\_GFX, the included files (as of this writing) are:

```
FreeMono12pt7b.h		FreeSansBoldOblique12pt7b.h
FreeMono18pt7b.h		FreeSansBoldOblique18pt7b.h
FreeMono24pt7b.h		FreeSansBoldOblique24pt7b.h
FreeMono9pt7b.h			FreeSansBoldOblique9pt7b.h
FreeMonoBold12pt7b.h		FreeSansOblique12pt7b.h
FreeMonoBold18pt7b.h		FreeSansOblique18pt7b.h
FreeMonoBold24pt7b.h		FreeSansOblique24pt7b.h
FreeMonoBold9pt7b.h		FreeSansOblique9pt7b.h
FreeMonoBoldOblique12pt7b.h	FreeSerif12pt7b.h
FreeMonoBoldOblique18pt7b.h	FreeSerif18pt7b.h
FreeMonoBoldOblique24pt7b.h	FreeSerif24pt7b.h
FreeMonoBoldOblique9pt7b.h	FreeSerif9pt7b.h
FreeMonoOblique12pt7b.h		FreeSerifBold12pt7b.h
FreeMonoOblique18pt7b.h		FreeSerifBold18pt7b.h
FreeMonoOblique24pt7b.h		FreeSerifBold24pt7b.h
FreeMonoOblique9pt7b.h		FreeSerifBold9pt7b.h
FreeSans12pt7b.h		FreeSerifBoldItalic12pt7b.h
FreeSans18pt7b.h		FreeSerifBoldItalic18pt7b.h
FreeSans24pt7b.h		FreeSerifBoldItalic24pt7b.h
FreeSans9pt7b.h			FreeSerifBoldItalic9pt7b.h
FreeSansBold12pt7b.h		FreeSerifItalic12pt7b.h
FreeSansBold18pt7b.h		FreeSerifItalic18pt7b.h
FreeSansBold24pt7b.h		FreeSerifItalic24pt7b.h
FreeSansBold9pt7b.h		FreeSerifItalic9pt7b.h
```

Each filename starts with the face name (“FreeMono”, “FreeSerif”, etc.) followed by the style (“Bold”, “Oblique”, none, etc.), font size in points (currently 9, 12, 18 and 24 point sizes are provided) and “7b” to indicate that these contain 7-bit characters (ASCII codes “ ” through “~”); _8-bit fonts (supporting symbols and/or international characters) are not yet provided but may come later._

# Using GFX Fonts in Arduino Sketches

After #including the Adafruit\_GFX and display-specific libraries, include the font file(s) you plan to use in your sketch. For example:

```
#include &lt;Adafruit_GFX.h&gt;    // Core graphics library
#include &lt;Adafruit_TFTLCD.h&gt; // Hardware-specific library
#include &lt;Fonts/FreeMonoBoldOblique12pt7b.h&gt;
#include &lt;Fonts/FreeSerif9pt7b.h&gt;
```

Each font takes up&nbsp;a bit of program&nbsp;space; larger fonts typically&nbsp;require more room. This is a finite resource (about 32K max on an Arduino Uno for font data and _all of your sketch code_), so choose carefully. Too big and the code will refuse to compile (or in some edge cases, may compile but then won’t upload to the board). If this happens, use fewer or smaller fonts, or use the standard built-in font.

Inside these .h files are several data structures, including one main font structure which will usually have the same name as the font file (minus the .h). To select a font for subsequent graphics operations, use the setFont() function, passing the _address_ of&nbsp;this structure, such as:

```
tft.setFont(&amp;FreeMonoBoldOblique12pt7b);
```

Subsequent calls to tft.print() will now use this&nbsp;font. Most other attributes that previously worked with the built-in font (color, size, etc.) work similarly here.

To return to the standard fixed-size font, call setFont(), passing either NULL or no arguments:

```
tft.setFont();
```

You can see a complete example of custom fonts in action in the [MagTag Quotes Example](https://learn.adafruit.com/adafruit-magtag/quotes-example)&nbsp;source code. It’s really just a few extra lines compared to a “normal” GFX text program.

Some text attributes behave a little differently with these new fonts. Not wanting to break compatibility with existing code, the “classic” font continues to behave as before.

For example, whereas the cursor position when printing with the classic font identified the _top-left corner_ of the character cell, with new fonts the cursor position indicates the _baseline_ — the bottom-most row — of subsequent text. Characters may vary in size and width, and don’t necessarily begin at the exact cursor column (as in below, this character starts one pixel _left_ of the cursor, but others may be on or to the right of it).

When switching between built-in and custom fonts, the library will automatically shift the cursor position up or down 6 pixels as needed to continue along the same baseline.

![](https://cdn-learn.adafruit.com/assets/assets/000/029/277/medium800/lcds___displays_NewChar.png?1450831047)

 **One “gotcha” to be aware of with new fonts: there is no “background” color option…you can set this value but it will be ignored.**

### **_This is on purpose and by design._**

**The background color feature is sometimes used with the “classic” font to overwrite old screen contents with new data. This only works because those characters are a uniform size; that won’t work with proportionally-spaced fonts, where the bounds of a string can vary, and an indeterminate number of characters may overlap the same region.**

**To replace previously-drawn text when using a custom font, either:**

- **Use getTextBounds() to determine the smallest rectangle encompassing a string, erase the area using fillRect(), then draw new text:**

```
int16_t  x1, y1;
uint16_t w, h;

tft.getTextBounds(string, x, y, &amp;x1, &amp;y1, &amp;w, &amp;h);
```

getTextBounds expects a string, a starting cursor X&Y position (the current cursor position will not be altered), and addresses of two signed and two unsigned 16-bit integers. These last four values will then contain the upper-left corner and the width & height of the area covered by this text — these can then be passed directly as arguments to fillRect().

This will unfortunately “blink” the text when erasing and redrawing, but is unavoidable. The old scheme of drawing background pixels in the same pass only creates a new set of problems.

 **or:**

- **Create a GFXcanvas1 object (an offscreen bitmap) for a fixed-size area, draw custom text in there and copy to the screen using drawBitmap().**

```cpp
// In global declarations:
GFXcanvas1 canvas(128, 32); // 128x32 pixel canvas

// In code later:
canvas.println("I like cake");
tft.drawBitmap(x, y, canvas.getBuffer(), 128, 32, foreground, background); // Copy to screen
```

_This is illustrative of syntax, not a complete program —&nbsp;change `x`, `y`, `foreground` and `background` to the desired coordinates and color values suited to the display. Some displays also require an explicit display() or show() call to refresh the screen contents._

This will be flicker-free but requires&nbsp;more RAM (about 512 bytes for the 128x32 pixel canvas shown above), so it’s not always practical on AVR boards with only 2K. Arduino Mega or any 32-bit board should manage fine.

**See the “Minimizing Redraw Flicker” page for more info on using canvases.**

# Adding&nbsp;New Fonts

If you want to create new font sizes not included with the library, or adapt entirely new fonts, we have a command-line tool&nbsp;(in the “fontconvert” folder) for this. It should work on many Linux- or UNIX-like systems (Raspberry Pi, Mac OS X, maybe Cygwin for Windows, among others).

Building this tool requires the gcc compiler and [FreeType](http://www.freetype.org)&nbsp;library. Most Linux distributions include both by default. For others, you may need to install developer tools and download and [build FreeType from the source](http://download.savannah.gnu.org/releases/freetype/). Then edit the Makefile to match your setup before invoking “make”.

_fontconvert_ expects at least two arguments: a font filename (such as a scalable TrueType vector font) and a size, in points (72 points = 1 inch; the code presumes a screen resolution similar to the Adafruit 2.8" TFT displays). The output should be redirected to a .h file…you can call this whatever you like but I try to be somewhat descriptive:

```
./fontconvert myfont.ttf 12 &gt; myfont12pt7b.h
```

The GNU FreeFont files are not included in the library repository [but are easily&nbsp;downloaded](http://savannah.gnu.org/projects/freefont/). Or you can convert most any font you like.

**The name assigned to the font structure within&nbsp;this file is based on the _input_ filename and font size, not the output.** This is why I recommend using descriptive filenames incorporating the font base name, size, and "7b". Then the .h&nbsp;filename and font structure name can match.

The resulting .h file can be copied to the Adafruit\_GFX/Fonts folder, or you can import the file as a new tab in your Arduino sketch using the Sketch→Add File… command.

If in the Fonts folder, use this syntax when #including the file:

```
#include &lt;Fonts/myfont12pt7b.h&gt;
```

If a tab within your sketch, use this syntax:

```
#include "myfont12pt7b.h"
```

- [Previous Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/rotating-the-display.md)
- [Next Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/loading-images.md)

## Related Guides

- [AdaBox 019](https://learn.adafruit.com/adabox019.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
- [Adafruit 128x64 OLED Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi.md)
- [Adafruit IO IOT Hub with the Adafruit FunHouse](https://learn.adafruit.com/adafruit-io-hub-with-the-adafruit-funhouse.md)
- [HalloWing Flapping Bat](https://learn.adafruit.com/hallowing-flapping-bat.md)
- [CircuitPython OLED and Dual Knob Sketcher](https://learn.adafruit.com/circuitpython-oled-knob-sketcher.md)
- [Monochrome OLED Breakouts](https://learn.adafruit.com/monochrome-oled-breakouts.md)
- [4x4 Rotary Encoder MIDI Messenger](https://learn.adafruit.com/4x4-rotary-encoder-midi-messenger.md)
- [Pico W HTTP Server with CircuitPython](https://learn.adafruit.com/pico-w-http-server-with-circuitpython.md)
- [Capturing Camera Images with CircuitPython](https://learn.adafruit.com/capturing-camera-images-with-circuitpython.md)
- [WiFi OLED Display Badge](https://learn.adafruit.com/digital-display-badge.md)
- [Trinket Ultrasonic Rangefinder](https://learn.adafruit.com/trinket-ultrasonic-rangefinder.md)
- [PyPortal Adafruit Quote Book](https://learn.adafruit.com/pyportal-adafruit-quote-board.md)
- [2.8" TFT Touchscreen](https://learn.adafruit.com/2-8-tft-touchscreen.md)
- [Magic Storybook with ChatGPT](https://learn.adafruit.com/magic-storybook-with-chatgpt.md)
