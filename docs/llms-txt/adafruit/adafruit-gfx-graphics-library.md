# Source: https://learn.adafruit.com/adafruit-gfx-graphics-library.md

# Adafruit GFX Graphics Library

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/001/304/medium800/lcds___displays_ID797tri_LRG.jpg?1396770841)

The **Adafruit\_GFX library for Arduino** provides a common syntax and set of graphics functions for all of our LCD and OLED displays and LED matrices. This allows Arduino sketches to easily be adapted between display types with minimal fuss…and any new features, performance improvements and bug fixes will immediately apply across our complete offering of color displays.

Adafruit\_GFX always works together with an _additional_ library unique to each specific display type. These can be installed using the **Arduino Library Manager**. From the Arduino “Sketch” menu, select “Include Library,” then “Manage Libraries…”

![](https://cdn-learn.adafruit.com/assets/assets/000/067/406/medium800/graphic_lcds_manage-libraries.png?1544574799)

In the Arduino Library Manager window, search for a display’s driver type (e.g. “SSD1325”) and the appropriate Adafruit library can be found in the results. Required companion libraries (“dependencies,” like Adafruit\_GFX or Adafruit\_BusIO) now get installed **automatically**. If using an older version of the Arduino IDE, you’ll have to search for and install those additional libraries manually.

![](https://cdn-learn.adafruit.com/assets/assets/000/067/407/medium800/graphic_lcds_adafruit-gfx-library-manager.png?1544574825)

Some of the libraries that operate alongside Adafruit\_GFX include:

- [RGBmatrixPanel](https://github.com/adafruit/RGB-matrix-Panel "Link: https://github.com/adafruit/RGB-matrix-Panel"), for our [16x32](http://www.adafruit.com/products/420) and [32x32](http://www.adafruit.com/products/607) RGB LED matrix panels.
- [Adafruit\_TFTLCD](https://github.com/adafruit/TFTLCD-Library "Link: https://github.com/adafruit/TFTLCD-Library"), for our 2.8" [TFT LCD touchscreen breakout](http://www.adafruit.com/products/335) and [TFT Touch Shield for Arduino](http://www.adafruit.com/products/376).
- [Adafruit\_HX8340B](https://github.com/adafruit/Adafruit-HX8340B), for our [2.2" TFT Display with microSD](http://www.adafruit.com/products/797).
- [Adafruit\_ST7735](https://github.com/adafruit/Adafruit-ST7735-Library), for our [1.8" TFT Display with microSD](http://www.adafruit.com/products/358).
- [Adafruit\_PCD8544](https://github.com/adafruit/Adafruit-PCD8544-Nokia-5110-LCD-library), for the [Nokia 5110/3310 monochrome LCD](http://www.adafruit.com/products/338).
- [Adafruit-Graphic-VFD-Display-Library](https://github.com/adafruit/Adafruit-Graphic-VFD-Display-Library), for our [128x64 Graphic VFD](https://www.adafruit.com/products/773).
- [Adafruit-SSD1331-OLED-Driver-Library-for-Arduino](https://github.com/adafruit/Adafruit-SSD1331-OLED-Driver-Library-for-Arduino) for the [0.96" 16-bit Color OLED w/microSD Holder](http://www.adafruit.com/products/684).
- [Adafruit\_SSD1306](https://github.com/adafruit/Adafruit_SSD1306) for the Monochrome [128x64](https://www.adafruit.com/products/326) and [128x32](https://www.adafruit.com/products/661) OLEDs.

And many others, except for some very early “retired” products. Remember, just search for the display driver type in the Arduino Library manager, install, and the rest is automatic now.

The libraries are written in C++ for Arduino but could easily be ported to any microcontroller by rewriting the low-level pin access functions.

# The Old Way

Much older versions of the Arduino IDE software require installing libraries manually; the Arduino Library Manager did not yet exist. If using an early version of the Arduino software, this might be a good time to upgrade. Otherwise, [this tutorial explains how to install and use Arduino libraries](http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries). Here are links to download the GFX and BusIO libraries directly (use the links above to get the corresponding display-specific libraries):

[Download Adafruit_GFX Library](https://github.com/adafruit/Adafruit-GFX-Library/archive/master.zip)
[Download Adafruit_BusIO Library](https://github.com/adafruit/Adafruit_BusIO/archive/master.zip)
# Accessing GFX Functions

Any Arduino sketch using Adafruit\_GFX needs to **#include two libraries**. You’ll see this in most examples, near the top of the code.&nbsp;The first, `Adafruit_GFX.h`, declares a common set of graphics functions such as shapes and colors (explained on subsequent pages). The second _completely depends_ on whatever display you’re using…it might be&nbsp;`Adafruit_ST7789.h`&nbsp;(for certain color displays), `Adafruit_SSD1306.h`&nbsp;(for certain monochrome OLEDs) or _something else…_the guide or product page for the display will tell you which library to install. The very top of a sketch then usually resembles something like this:

```cpp
#include &lt;Adafruit_GFX.h&gt;    // Core graphics library
#include &lt;Adafruit_ST7789.h&gt; // Hardware-specific library for ST7789
```

- [Next Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/coordinate-system-and-units.md)

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
