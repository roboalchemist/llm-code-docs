# Source: https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/new-wiring.md

# RGB LED Matrix Basics

## Connections

These panels are normally designed for _chaining_&nbsp;(linking end-to-end into larger displays)…the output of one panel connects to the input of the next, down the line.

With the limited RAM in an Arduino, chaining is seldom practical. Still, **it’s necessary to distinguish the input and output connections** on the panel…it won’t respond if we’re connected to the wrong socket.

Danger: Although the panels support chaining, this is VERY impractical on Arduino-class boards and our library DOES NOT SUPPORT it. A more powerful system like a Raspberry Pi may be a better choice for chained panels!

Flip&nbsp;the matrix over so you’re looking at the back, holding&nbsp;it with the two sockets&nbsp;situated at the **left and right edges** (not top and bottom).

On some panels, if you’re lucky, the sockets&nbsp;are&nbsp;labeled INPUT and OUTPUT (sometimes IN and OUT or similar), so it’s obvious which&nbsp;is the input socket.  
&nbsp;  
If INPUT is not labeled, look for one or more arrows pointing in the **horizontal** &nbsp;direction (ignore any vertical arrows, whether up or down). The horizontal arrows show the direction data moves from INPUT to OUTPUT — then you know which connector is which.  
&nbsp;  
If no such labels are present, a last option is to examine the plastic shroud around the connector pins. The key (notch) on the INPUT connector will face the outer edge of the panel (not the center).

![](https://cdn-learn.adafruit.com/assets/assets/000/023/772/medium800/led_matrix_orient.png?1426306203)

 **The arrangement of pins on the INPUT connector varies with matrix size and the batch in which it was produced…**

A **32x16** panel uses this pin arrangement. The labels might be slightly different, or the pins&nbsp;might not be labeled at all…but in either case, use this image for reference.

&nbsp;

Notice there are four ground connections. To ensure reliable performance, **_all four_ should be connected to GND** on the Arduino! A solderless breadboard is handy for making this split.

![led_matrix_socket1.png](https://cdn-learn.adafruit.com/assets/assets/000/023/767/medium640/led_matrix_socket1.png?1426305716)

Here’s the layout for **32x32** and **64x32** panels. We’ll call this “ **Variant A**.” Some panels use different labels, but the functions are identical.

&nbsp;

The layout is very similar to the 32x16 panel, with&nbsp;pin “D” replacing one ground connection.

&nbsp;

**This is the layout we’ll be referencing most often.**

&nbsp;

**If you have a 32x32 panel with _no pin labels at all,_ then use this layout.**

![led_matrix_socket2.png](https://cdn-learn.adafruit.com/assets/assets/000/023/768/medium640/led_matrix_socket2.png?1426305708)

Info: On the 64x32 2.5mm panels (product ID [5036](https://www.adafruit.com/product/5036)), the green and blue channels are swapped compared to the standard HUB75 pinout. When using with libraries, simply swap the pin numbers for G1, G2 with B1, B2 in software to flip them back around.

If you are using the CircuitPython `MatrixPortal` library, you do not need to swap pins explicitly. Instead, add this argument to the constructor: `MatrixPortal(..., color_order="RBG", ...)`. The default order is `"RGB"`, and this argument will swap the pins to match the specified `"RBG"` order.

“ **Variant B** ” for **32x32** and **64x32** panels.&nbsp; **The wiring is _identical_ to Variant A above, _only the labels_ are different.**

&nbsp;

Ground pins aren’t labeled, but still need to be connected.

&nbsp;

LAT (latch) is labeled STB (strobe) here. R1/G1/B1/R2/G2/B2 are changed to&nbsp;R0/G0/B0/R1/G1/B1…but again, no functional difference, it’s just ink.

![led_matrix_socket3.png](https://cdn-learn.adafruit.com/assets/assets/000/023/769/medium640/led_matrix_socket3.png?1426305755)

Our earliest **32x32** panels had a **two-socket** &nbsp;design, let’s call it “ **Variant C**.” All the same pin functions are present but the layout is very different.

&nbsp;

R/G/B on the **upper** &nbsp;socket correspond to R1/G1/B1 in Variant A. R/G/B on the **lower** &nbsp;socket correspond to R2/G2/B2.

&nbsp;

All the other signals (A/B/C/D/CLK/LAT/OE) need to be connected to **both** sockets — e.g. one pin on the Arduino drives both CLK pins, and so forth.

![led_matrix_socket4.png](https://cdn-learn.adafruit.com/assets/assets/000/023/770/medium640/led_matrix_socket4.png?1426305854)

# Connecting to Arduino

There are two or three methods for connecting a matrix to an Arduino:

1. **Jumper wires** inserted between Arduino headers and a ribbon cable — this works well for testing and prototyping, but is not durable.
2. The **Adafruit RGB Matrix Shield** makes connecting these panels to an Arduino as easy as can be, and is best for permanent installations.
3. One could build a **_proto shield_** &nbsp;to replicate the pinout of option #2. But given the Matrix Shield’s low cost, this might not be worth the effort nowadays.

These panels are normally run by very fast processors or FPGAs, not a 16 MHz Arduino.&nbsp;To achieve reasonable performance in this limited&nbsp;environment,&nbsp;our software is optimized by&nbsp; **tying&nbsp;specific signals to specific Arduino pins**. A _few_ control lines can be reconfigured, but others are very specific… **you can’t wire the whole thing willy-nilly.** The next pages demonstrate compatible wiring…one using the RGB Matrix Shield, the using&nbsp;jumper wires.

- [Previous Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/powering.md)
- [Next Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-using-rgb-matrix-shield.md)

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
