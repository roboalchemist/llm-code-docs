# Source: https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md

# RGB LED Matrix Basics

## Overview

This guide is for boards in the **ARDUINO ecosystem**.&nbsp;We have a [different guide for Raspberry Pi](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi), and another for [CircuitPython](https://learn.adafruit.com/rgb-led-matrices-matrix-panels-with-circuitpython).

Arduino Uno is limited to 32x16 pixels, single-buffered.

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/935/medium800/led_matrix_rgbmatrix.jpg?1396789179)

Bring a little bit of Times Square into your home with our RGB LED matrix panels. These panels are normally used to make video walls —&nbsp;here in New York we see them on the sides of buses and on bus stops —&nbsp;to display animations or short video clips. We thought they looked really cool so we picked up a few boxes from the factory. One has 512 bright RGB LEDs arranged in a 16x32 grid on the front, the other has 1024 LEDs in a 32x32 grid. On the back is a PCB with IDC connectors (one set for input, one for output: in theory you can chain these together) and 12 16-bit latches that allow you to drive the display with a 1:8 (16x32) or 1:16 (32x32) scan rate.

# **COMPATIBLE HARDWARE**

The following boards are **plug-and-play ready** with the RGB Matrix Shield and software mentioned in this guide:

- **Adafruit Metro M0**
- **Arduino Zero**
- **Arduino Uno** &nbsp;(or compatible ATmega328P boards) — **limited to 32x16 matrix** , no double-buffering (needed for flicker-free animation)

The following are supported by the software, but require **additional wiring or jumpers** to use the RGB Matrix Shield:

- **Arduino Mega** (or compatible ATmega2560 boards)
- **Adafruit Metro M4**
- **Adafruit Metro RP2350** (requires address pins {A, B, C, D} get jumper wires)

The following are **NOT supported** by the software or shield:

- **Arduino Leonardo** (or compatible ATmega32U4 boards) (though the same form factor, the Uno and Leonardo route different shield connections to the microcontroller)
- **Netduino** and other Arduino-alikes not mentioned in above lists (but other libraries or shields might exist elsewhere)
- **Teensy** (but see the **SmartLED** Shields and software for Teensy 3.X and 4.X, which provide excellent performance)
- **Raspberry Pi** (but there are different [Bonnets](https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi) and [HATs](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi) for this)

# **COMPATIBLE SOFTWARE**

The software support for driving the RGB matrix panels has evolved with time and the availability of newer, more powerful Arduino boards. **There are currently two different Arduino libraries.** Which library to use depends on the Arduino board being used.

- [RGB matrix Panel](https://github.com/adafruit/RGB-matrix-Panel) - This is the older, original library and is covered later in this guide. Use this library with an **Arduino UNO** or **Arduino Mega**.
- [Adafruit Protomatter](https://github.com/adafruit/Adafruit_Protomatter) - This is a newer library covered in a [separate guide](https://learn.adafruit.com/adafruit-protomatter-rgb-matrix-library/overview). Use this library with an **Arduino Zero** , **Metro M0** , **Metro M4** , **RP2040** based board, **ESP32** based board, or other supported **32bit boards**. [See the Protomatter guide for more details.](https://learn.adafruit.com/adafruit-protomatter-rgb-matrix-library/overview)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/936/medium800/led_matrix_rgbmatrix3232_lrg.jpg?1396789186)

These panels require 12 or 13 digital pins (6 bit data, 6 or 7 bit control) and a good 5V power supply, at least&nbsp;a couple amps&nbsp;per panel. We suggest our 2A (or larger) regulated 5V adapters and either a terminal block DC jack, or solder a jack from our DC extension cord. Please read the rest of our tutorial for more details!  
  
Keep in mind that these displays are normally designed to be driven by FPGAs or other high speed processors; they do not have built in PWM control of any kind. Instead, you're supposed to redraw the screen over and over to 'manually' PWM the whole thing. On a 16 MHz Arduino, we managed to squeeze 12-bit color (4096 colors) but this display would really shine if driven by an FPGA, CPLD, Propeller, XMOS or other high speed multi-processor controller.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/937/medium800/led_matrix_plasma.jpg?1396789196)

Of course, we wouldn't leave you with a datasheet and a "good luck!" We have a full wiring diagrams and working Arduino library code with examples from drawing pixels, lines, rectangles, circles and text. You'll get your color blasting within the hour! On most Arduino-compatible boards, you'll need 12 digital pins, and about 800 bytes of RAM to hold&nbsp;the 12-bit color image (double that for the 32x32 matrix, double again for smooth double-buffered animation).

Danger: 

- [Next Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/powering.md)

## Featured Products

### Medium 16x32 RGB LED matrix panel - 6mm Pitch

[Medium 16x32 RGB LED matrix panel - 6mm Pitch](https://www.adafruit.com/product/420)
Bring a little bit of Times Square into your home with this 16 x 32 RGB LED matrix panel. These panels are normally used to make video walls, here in New York we see them on the sides of busses and bus stops, to display animations or short video clips. We thought they looked really cool so we...

In Stock
[Buy Now](https://www.adafruit.com/product/420)
[Related Guides to the Product](https://learn.adafruit.com/products/420/guides)
### 32x32 RGB LED Matrix Panel - 4mm Pitch

[32x32 RGB LED Matrix Panel - 4mm Pitch](https://www.adafruit.com/product/607)
Bring a little bit of Times Square into your home with this totally adorable 5 inch square 32 x 32 RGB LED matrix panel. These panels are normally used to make video walls, here in New York we see them on the sides of busses and bus stops, to display animations or short video clips. We thought...

In Stock
[Buy Now](https://www.adafruit.com/product/607)
[Related Guides to the Product](https://learn.adafruit.com/products/607/guides)
### 32x32 RGB LED Matrix Panel - 5mm Pitch

[32x32 RGB LED Matrix Panel - 5mm Pitch](https://www.adafruit.com/product/2026)
Bring a little bit of Times Square into your home with this sweet 32 x 32 square RGB LED matrix panel. These panels are normally used to make video walls, here in New York we see them on the sides of busses and bus stops, to display animations or short video clips. We thought they looked...

In Stock
[Buy Now](https://www.adafruit.com/product/2026)
[Related Guides to the Product](https://learn.adafruit.com/products/2026/guides)
### 32x32 RGB LED Matrix Panel - 6mm pitch

[32x32 RGB LED Matrix Panel - 6mm pitch](https://www.adafruit.com/product/1484)
Bring a little bit of Times Square into your home with this sweet 32 x 32 square RGB LED matrix panel. These panels are normally used to make video walls, here in New York we see them on the sides of busses and bus stops, to display animations or short video clips. We thought they looked...

In Stock
[Buy Now](https://www.adafruit.com/product/1484)
[Related Guides to the Product](https://learn.adafruit.com/products/1484/guides)
### 64x32 RGB LED Matrix - 3mm pitch

[64x32 RGB LED Matrix - 3mm pitch](https://www.adafruit.com/product/2279)
Bring a little bit of Times Square into your home with this sweet 64 x 32 square RGB LED matrix panel. These panels are normally used to make video walls, here in New York we see them on the sides of busses and bus stops, to display animations or short video clips. We thought they looked...

In Stock
[Buy Now](https://www.adafruit.com/product/2279)
[Related Guides to the Product](https://learn.adafruit.com/products/2279/guides)
### 64x32 RGB LED Matrix - 4mm pitch

[64x32 RGB LED Matrix - 4mm pitch](https://www.adafruit.com/product/2278)
Bring a little bit of Times Square into your home with this sweet 64 x 32 square RGB LED matrix panel. These panels are normally used to make video walls, here in New York we see them on the sides of busses and bus stops, to display animations or short video clips. We thought they looked...

Out of Stock
[Buy Now](https://www.adafruit.com/product/2278)
[Related Guides to the Product](https://learn.adafruit.com/products/2278/guides)
### 64x32 RGB LED Matrix - 5mm pitch

[64x32 RGB LED Matrix - 5mm pitch](https://www.adafruit.com/product/2277)
Bring a little bit of Times Square into your home with this sweet 64x32 square RGB LED matrix panel. These panels are normally used to make video walls, here in New York we see them on the sides of busses and bus stops, to display animations or short video clips. We thought they looked really...

In Stock
[Buy Now](https://www.adafruit.com/product/2277)
[Related Guides to the Product](https://learn.adafruit.com/products/2277/guides)
### 64x32 RGB LED Matrix - 6mm pitch

[64x32 RGB LED Matrix - 6mm pitch](https://www.adafruit.com/product/2276)
Bring a little bit of Times Square into your home with this sweet 64x32 square RGB LED matrix panel. These panels are normally used to make video walls, here in New York we see them on the sides of busses and bus stops, to display animations or short video clips. We thought they looked really...

In Stock
[Buy Now](https://www.adafruit.com/product/2276)
[Related Guides to the Product](https://learn.adafruit.com/products/2276/guides)

## Related Guides

- [Adafruit Metro M0 Express](https://learn.adafruit.com/adafruit-metro-m0-express.md)
- [Adafruit Metro M4 Express featuring ATSAMD51](https://learn.adafruit.com/adafruit-metro-m4-express-featuring-atsamd51.md)
- [CircuitPython 101: Basic Builtin Data Structures](https://learn.adafruit.com/basic-datastructures-in-circuitpython.md)
- [Adafruit Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Stream Deck controlled RGB Message Panel using Adafruit IO](https://learn.adafruit.com/stream-deck-controlled-rgb-message-panel-using-adafruit-io.md)
- [Memories of an Arduino](https://learn.adafruit.com/memories-of-an-arduino.md)
- [Matrix Portal Stained Glass with WLED](https://learn.adafruit.com/matrix-portal-stained-glass-with-wled.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
- [LED Matrix Sports Scoreboard](https://learn.adafruit.com/led-matrix-sports-scoreboard.md)
- [Creating MatrixPortal Projects with CircuitPython](https://learn.adafruit.com/creating-projects-with-the-circuitpython-matrixportal-library.md)
- [Introducing Adafruit Trellis ](https://learn.adafruit.com/adafruit-trellis-diy-open-source-led-keypad.md)
- [CircuitPython Hardware: Charlieplex LED Matrix](https://learn.adafruit.com/micropython-hardware-charlieplex-led-matrix.md)
- [CircuitPython Display Support Using displayio](https://learn.adafruit.com/circuitpython-display-support-using-displayio.md)
- [Arduino Lesson 16. Stepper Motors](https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors.md)
- [2.8" TFT Touchscreen](https://learn.adafruit.com/2-8-tft-touchscreen.md)
- [SmartMatrix Animated GIF Player](https://learn.adafruit.com/smartmatrix-animated-gif-player.md)
