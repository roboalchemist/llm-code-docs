# Source: https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-using-a-proto-shield.md

# RGB LED Matrix Basics

## Connecting Using a Proto Shield

As mentioned on the “Jumper” page: if you hold a&nbsp;ribbon cable flat — no folds — and with both connectors facing you, keys pointed the same direction — there’s&nbsp;is a 1:1 correlation between the pins. The top-right&nbsp;pin on one plug links to the top-right&nbsp;on the other plug, and so forth.&nbsp;This holds true even if the cable has a doubled-over strain relief. **As long as the keys point the same way and the plugs face the same way, pins are in the same positions&nbsp;at both ends.**

![](https://cdn-learn.adafruit.com/assets/assets/000/023/924/medium800/led_matrix_cable1.png?1426546582)

 **Either end of the ribbon cable can be plugged into the matrix INPUT socket.**

The&nbsp;free end of the ribbon can point toward the center of the matrix, or hang off the side…the pinout is still the same. Notice below the direction of the “key” doesn’t change.

![](https://cdn-learn.adafruit.com/assets/assets/000/023/928/medium800/led_matrix_ribbon-2ways.png?1426548204)

A dual-row header gets installed on the proto shield, similar to&nbsp;the connector on the matrix.&nbsp;Just like the ribbon cable lying flat, as long as these two headers are _aligned&nbsp;the same way,_ they’ll&nbsp; **match pin-for-pin** ; unlike the jumper wire method from the prior page, mirroring doesn’t happen.

![](https://cdn-learn.adafruit.com/assets/assets/000/023/939/medium800/led_matrix_aligned.png?1426554087)

Wires are&nbsp;then soldered from the header to specific Arduino pins on the proto shield. Try to keep wire lengths reasonably short to avoid signal interference.

Using color-coded wires helps a _lot!_ If you don’t have colored wires, that’s okay, just pay close attention where everything goes. Our goal is a proto shield something like&nbsp;this:

![](https://cdn-learn.adafruit.com/assets/assets/000/023/930/medium800/led_matrix_proto-example.jpg?1426549088)

It’s not necessary to install all the buttons and lights on the proto shield if you don’t want — just the basic header pins are&nbsp;sufficient.

For **Arduino form-factor boards** , using an [**Adafruit** proto shield](https://www.adafruit.com/product/2077): **if using a shrouded socket (like on the back of the matrix — with the notch so a ribbon cable only fits one way) you’ll need to place this near the “Reset” end of the shield.** The plastic shroud obscures&nbsp;a lot of pins. **Others’ proto shields may be laid out different** …look around for a good location before committing to solder.

For **Arduino Mega** with our [corresponding proto shield](https://www.adafruit.com/products/192): a shrouded socket fits best near the **middle** of the shield.

**Otherwise, you can use a plain 2x8-pin male header, or two 1x8 sections** installed side-by-side (as in the photo above). Since there’s no alignment key with this setup, you might want to indicate&nbsp;it with some tape or a permanent marker.

Depending on the make and model of proto shield, some pins are designed to connect in short rows. Others don’t. For the latter, strip a little extra insulation and bend the wire to wrap around the leg of the socket from behind, then solder.

![led_matrix_backside.jpg](https://cdn-learn.adafruit.com/assets/assets/000/023/940/medium640/led_matrix_backside.jpg?1426560083)

# Connect Ground Wires
 **32x32** and **64x32** matrices require **three&nbsp;** ground connections. **32x16** matrices have **four**.

&nbsp;

Most proto shields have _tons_ of grounding&nbsp;points, so you shouldn’t have trouble finding places to connect these.

![led_matrix_header-gnds.png](https://cdn-learn.adafruit.com/assets/assets/000/023/942/medium640/led_matrix_header-gnds.png?1426568010)

# Upper RGB Data
Pins **R1** , **G1** and **B1** (labeled R0, B0 and G0 on some matrices) deliver data to the **top half** of the display.

On the **Arduino Uno** and&nbsp;**Adafruit Metro (328, M0** or **M4)&nbsp;**boards, connect these to digital pins **2** , **3** and **4**.

On **Arduino Mega** , connect to pins **24** , **25** and&nbsp; **26**.

![led_matrix_header-rgb1.png](https://cdn-learn.adafruit.com/assets/assets/000/023/943/medium640/led_matrix_header-rgb1.png?1426565078)

# Lower RGB Data
Pins **R2** , **G2** and **B2** (labeled R1, G1 and B1 on some matrices) deliver data to the **bottom half&nbsp;** of the display. These connect to the next three Arduino pins…

On **Arduino Uno** and&nbsp; **Adafruit Metros** , that’s pins **5** , **6** and **7**.

On **Arduino Mega** , pins **27** , **28** and **29**.

![led_matrix_header-rgb2.png](https://cdn-learn.adafruit.com/assets/assets/000/023/944/medium640/led_matrix_header-rgb2.png?1426580512)

# Row Select Lines
Pins **A** , **B** , **C** and **D** select which two rows&nbsp;of the display are&nbsp;currently lit. ( **32x16 matrices don’t have a “D” pin** — it’s connected to **ground&nbsp;** instead.)

&nbsp;

These connect to pins **A0** , **A1** , **A2** and (if D pin present) **A3**. This is the **same** &nbsp;for both the&nbsp; **Arduino Uno** and **Mega**.

![led_matrix_header-rows.png](https://cdn-learn.adafruit.com/assets/assets/000/023/945/medium640/led_matrix_header-rows.png?1426580569)

# LAT Wire
For **32x32** and **64x32** matrices, **LAT** connects to Arduino pin **10**.

This is the same for all boards.

The LAT (latch) signal marks the end of a row of data.

![led_matrix_header-lat.png](https://cdn-learn.adafruit.com/assets/assets/000/023/946/medium640/led_matrix_header-lat.png?1426565395)

# OE Wire
 **OE** connects to Arduino pin **9**. This is the same for all boards.

OE (output enable) switches the LEDs off when transitioning from one row to the next.

![led_matrix_header-oe.png](https://cdn-learn.adafruit.com/assets/assets/000/023/948/medium640/led_matrix_header-oe.png?1426565436)

# CLK Wire

Last one!

 **CLK** connects to…

- **Pin 8** on **Arduino Uno** , **Adafruit Metro 328** or **Metro M0**.
- **Pin A4** on **Adafruit Metro M4**.
- **Pin 11** on **Arduino Mega**.

The CLK (clock) signal marks the arrival of each bit of data.

![led_matrix_header-clk.png](https://cdn-learn.adafruit.com/assets/assets/000/023/947/medium640/led_matrix_header-clk.png?1426565431)

Here’s that photo again of a completed shield. You can tell this is for a 32x16 matrix, because there are four ground connections (one of the long vertical strips is a ground bus — see the tiny jumpers there?).

The ribbon cable to the matrix would plug into this with the key facing left.

The colors and positions don’t quite match the examples above, but are close. G1 and G2 are yellow wires. LAT is the purple wire and should go to pin 10 now&nbsp;(we changed around some things in the Arduino library).

![](https://cdn-learn.adafruit.com/assets/assets/000/023/949/medium800/led_matrix_proto-example.jpg?1426565584)

- [Previous Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-with-jumper-wires.md)
- [Next Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/test-example-code.md)

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
