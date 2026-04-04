# Source: https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-with-jumper-wires.md

# RGB LED Matrix Basics

## Connecting with Jumper Wires

Danger: 

Ribbon cables and their corresponding headers are sometimes a&nbsp;topological puzzle. Here’s a trick to help keep track…

If you hold the ribbon cable flat — no folds — and with both connectors facing you, keys pointed the same direction — now there is a 1:1 correlation between the pins. The top-right&nbsp;pin on one plug links to the top-right&nbsp;on the other plug, and so forth.&nbsp;This holds true even if the cable has a doubled-over strain relief. **As long as the keys point the same way and the plugs face the same way, pins are in the same positions&nbsp;at both ends.**

![](https://cdn-learn.adafruit.com/assets/assets/000/023/920/medium800/led_matrix_cable1.png?1426541458)

Plugged into a socket on the LED matrix, one header now faces _away_ from you. If you double the cable back on itself (not a twist, but a fold)…to access a specific pin on the socket, the left and right columns are now mirrored (rows are in the same order — the red stripe provides a point of reference). You’re looking “up” into the plug rather than “down” into the socket.

For example, R1 (the top-left pin on the INPUT socket) appears at the top-_right_ of the exposed plug. You can jam a wire jumper in that hole to&nbsp;a corresponding pin on the Arduino…

![](https://cdn-learn.adafruit.com/assets/assets/000/023/921/medium800/led_matrix_cable2.png?1426541485)

So! From the prior page, refer to the socket that’s correct for your matrix type. The labels may be a little different (or none at all), but most are pretty close to what’s shown here.

&nbsp;

Then _swap the columns_ to find the correct position for a given signal.

![led_matrix_socket2.png](https://cdn-learn.adafruit.com/assets/assets/000/023/825/medium640/led_matrix_socket2.png?1426392340)

![led_matrix_plug2.png](https://cdn-learn.adafruit.com/assets/assets/000/023/826/medium640/led_matrix_plug2.png?1426392350)

 **Either end of the ribbon cable can be plugged into the matrix INPUT socket.** Notice below, the “key” faces the same way regardless.

With the free end of the ribbon toward the center of the matrix, the Arduino can be hidden behind it.

With the free end of the ribbon off the side, it’s easier to see both the front of the matrix and the Arduino simultaneously, for making additional connections or for troubleshooting.

![](https://cdn-learn.adafruit.com/assets/assets/000/023/929/medium800/led_matrix_ribbon-2ways-jumper.png?1426548655)

Using color-coded wires helps a _lot!_ If you don’t have colored wires, that’s okay, just pay close attention where everything goes. Our goal is a fully-populated plug like&nbsp;this:

![](https://cdn-learn.adafruit.com/assets/assets/000/023/922/medium800/led_matrix_jumpers.jpg?1426541597)

So! Let’s proceed with the wiring, in groups…

# Connect Ground Wires
 **32x32** and **64x32** matrices require **three** ground connections. **32x16** matrices have **four**.

&nbsp;

Current **Arduino Uno form-factor** &nbsp;boards have **three** ground pins (the third is next to pin 13). If you need additional ground connections — for a 32x16 matrix, or if using an older Arduino board with only 2 ground pins — a solderless breadboard is handy for linking all these pins.

&nbsp;

**Arduino Mega** boards have **five** ground pins. Same three as the Arduino Uno, plus two more next to pins 52 & 53.

![led_matrix_breadboard.jpg](https://cdn-learn.adafruit.com/assets/assets/000/023/824/medium640/led_matrix_breadboard.jpg?1426392323)

![led_matrix_plug-gnds.png](https://cdn-learn.adafruit.com/assets/assets/000/023/844/medium640/led_matrix_plug-gnds.png?1426484021)

![led_matrix_uno-gnds.png](https://cdn-learn.adafruit.com/assets/assets/000/023/847/medium640/led_matrix_uno-gnds.png?1426485631)

![led_matrix_mega-gnds.png](https://cdn-learn.adafruit.com/assets/assets/000/023/848/medium640/led_matrix_mega-gnds.png?1426485637)

# Upper RGB Data
Pins **R1** , **G1** and **B1** (labeled R0, B0 and G0 on some matrices) deliver data to the **top half** of the display.

&nbsp;

On the **Arduino Uno** and **Adafruit Metro (328, M0** or **M4)&nbsp;**boards, connect these to digital pins **2** , **3** and **4**.

&nbsp;

On **Arduino Mega** , connect to pins **24** , **25** and **26**.

![led_matrix_plug-rgb1.png](https://cdn-learn.adafruit.com/assets/assets/000/023/857/medium640/led_matrix_plug-rgb1.png?1426486361)

![led_matrix_uno-rgb1.png](https://cdn-learn.adafruit.com/assets/assets/000/023/858/medium640/led_matrix_uno-rgb1.png?1426486371)

![led_matrix_mega-rgb1.png](https://cdn-learn.adafruit.com/assets/assets/000/023/859/medium640/led_matrix_mega-rgb1.png?1426486393)

# Lower RGB Data
Pins **R2** , **G2** and **B2** (labeled R1, G1 and B1 on some matrices) deliver data to the **bottom half** of the display. These connect to the next three Arduino pins…

&nbsp;

On **Arduino Uno** and **Adafruit Metros** , that’s pins **5** , **6** and **7**.

&nbsp;

On **Arduino Mega** , pins **27** , **28** and **29**.

![led_matrix_plug-rgb2.png](https://cdn-learn.adafruit.com/assets/assets/000/023/846/medium640/led_matrix_plug-rgb2.png?1426484827)

![led_matrix_uno-rgb2.png](https://cdn-learn.adafruit.com/assets/assets/000/023/851/medium640/led_matrix_uno-rgb2.png?1426485688)

![led_matrix_mega-rgb2.png](https://cdn-learn.adafruit.com/assets/assets/000/023/852/medium640/led_matrix_mega-rgb2.png?1426485697)

# Row Select Lines
Pins **A** , **B** , **C** and **D** select which two rows&nbsp;of the display are&nbsp;currently lit. ( **32x16 matrices don’t have a “D” pin** — it’s connected to **ground** instead.)

&nbsp;

These connect to pins **A0** , **A1** , **A2** and (if D pin present) **A3**. This is the **same** &nbsp;for all boards.

![led_matrix_plug-rows.png](https://cdn-learn.adafruit.com/assets/assets/000/023/876/medium640/led_matrix_plug-rows.png?1426528173)

![led_matrix_uno-rows.png](https://cdn-learn.adafruit.com/assets/assets/000/023/912/medium640/led_matrix_uno-rows.png?1426539184)

# LAT Wire
The&nbsp; **LAT** &nbsp;signal connects to Arduino pin **10**.

This is the same for all boards.

The LAT (latch) signal marks the end of a row of data.

![led_matrix_plug-lat.png](https://cdn-learn.adafruit.com/assets/assets/000/023/913/medium640/led_matrix_plug-lat.png?1426540774)

![led_matrices_uno-lat-NEW.png](https://cdn-learn.adafruit.com/assets/assets/000/056/384/medium640/led_matrices_uno-lat-NEW.png?1530077713)

# OE Wire
 **OE** connects to Arduino pin **9**. This is the same for all boards.

OE (output enable) switches the LEDs off when transitioning from one row to the next.

![led_matrix_plug-oe.png](https://cdn-learn.adafruit.com/assets/assets/000/023/918/medium640/led_matrix_plug-oe.png?1426541287)

![led_matrices_uno-oe-new.png](https://cdn-learn.adafruit.com/assets/assets/000/056/385/medium640/led_matrices_uno-oe-new.png?1530077737)

# CLK Wire

Last one!

 **CLK** connects to…

- **Pin 8** on **Arduino Uno** , **Adafruit Metro 328** or **Metro M0**.
- **Pin 11** on **Arduino Mega**.
- **Pin A4** on **Adafruit Metro M4** (not shown, but you get the idea).

The CLK (clock) signal marks the arrival of each bit of data.

![led_matrix_plug-clk.png](https://cdn-learn.adafruit.com/assets/assets/000/023/915/medium640/led_matrix_plug-clk.png?1426541145)

![led_matrices_uno-clk-new.png](https://cdn-learn.adafruit.com/assets/assets/000/056/386/medium640/led_matrices_uno-clk-new.png?1530077773)

![led_matrices_mega-clk-new.png](https://cdn-learn.adafruit.com/assets/assets/000/056/387/medium640/led_matrices_mega-clk-new.png?1530077785)

That’s it. You can skip ahead to the “Test Example Code” page now.

- [Previous Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-using-rgb-matrix-shield.md)
- [Next Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-using-a-proto-shield.md)

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
