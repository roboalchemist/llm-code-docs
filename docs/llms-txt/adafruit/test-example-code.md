# Source: https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/test-example-code.md

# RGB LED Matrix Basics

## Test Example Code

We have example code ready to go for these displays. It does not work with every board out there. **See the “Compatible Hardware” lists on the opening page for guidance.**

Danger: 

Danger: 

 **Support for 32-bit microcontrollers — M4, RP2040, ESP32, etc. — is documented in** [a different library called _Protomatter,_ documented here](https://learn.adafruit.com/adafruit-protomatter-rgb-matrix-library) **.**

 **Arduino Uno support is limited to the 32x16 matrix, and only “single-buffered”** (i.e. no smooth animation), _despite_ any comments in the examples that might suggest otherwise.

_Over time, RAM required by the core Arduino code and the matrix-driving graphics libraries has increased…a few bytes here and there as bugs are fixed and features are added. Early on, 32x32 (or double-buffered 32x16)_ just barely _fit in the Arduino Uno’s RAM, with a few dozen bytes to spare for user code. This is no longer the case. But you might still see references to this in older code._

Some libraries need to be downloaded and installed: first is the [RGB Matrix Panel library](https://github.com/adafruit/RGB-matrix-Panel) (this contains the low-level code specific to this device), then the [Adafruit GFX Library](https://github.com/adafruit/Adafruit-GFX-Library) (which handles graphics operations common to many displays we carry) and [Adafruit BusIO](https://github.com/adafruit/Adafruit_BusIO).

Both libraries can be found and installed using the Arduino Library Manager ( **Sketch→Include Library→Manage Libraries…** ). Search for “gfx” and “rgb matrix panel” and install the corresponding Adafruit libraries.

![led_matrices_lib-gfx.png](https://cdn-learn.adafruit.com/assets/assets/000/056/430/medium640/led_matrices_lib-gfx.png?1530127536)

![led_matrices_lib-matrix.png](https://cdn-learn.adafruit.com/assets/assets/000/056/431/medium640/led_matrices_lib-matrix.png?1530127547)

Now you are ready to test! Open up the IDE and load **File→Examples→RGBmatrixPanel→testcolors\_16x32** (for the 16x32 panel) or **File→Examples→RGBmatrixPanel→colorwheel\_32x32** (for the 32x32 panel).&nbsp;There’s also a&nbsp; **testshapes\_32x64** example for boards with sufficient RAM.

**If using an Arduino Mega 2560,** in addition to wiring changes previously mentioned, you'll need to make a small change to each of the example sketches. This line:

```
#define CLK 8  // MUST be on PORTB! (Use pin 11 on Mega)
```

Should be changed to:

```
#define CLK 11
```

_(Any of digital pins 10-13 and 50-53 can be used for this function on the Mega, with the corresponding wiring change. The examples all reference pin 11.)_

If using an **Adafruit Metro M4** (_not_ M0 or 328), the CLK change would instead be:

```
#define CLK A4
```

After uploading, with the 16x32 panel you should see the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/959/medium800/led_matrix_allcolors.jpg?1396789390)

This is a test pattern that shows 512 colors (out of 4096) on the 512 pixels. Since there's no really elegant way to show a 3-dimensional color space (R/G/B) in two dimensions, there's just repeating grids of red/green with increasing blue. Anyways, this shows you the range of colors you can achieve!  
  
or, with the 32x32 panel:  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/960/medium800/led_matrix_rgbmatrix3232wheel_lrg.jpg?1396789401)

Now that you've got it working here are a few things to look for:  
  
The most useful line to look at is:  
```
      matrix.drawPixel(x, y, matrix.Color333(r, g, b));
```

which is where we actually draw to the display. This code only draws one pixel at a time. The **x** and **y** coordinates are the individual pixels of the display. **(0,0)** is in the top left corner, **(31, 15)** is in the bottom right (remember that we start counting at 0 here!). To create a color, you will want to use the helper funciton **Color333** which will take three 3-bit numbers and combine them into a single packed integer. So for example, the first argument, **r** can range from 0 to 7. Likewise for **g** and **b**. To make a pixel that is pure red, **r** would be 7 and **g, b** would be 0. To make a white pixel, set all to 7. To make a black (off) pixel, set the colors to 0. A similar function, **Color444** , accepts three 4-bit numbers for up to 4096 colors.  
  
Now we can open up the next example, which shows the rest of the library capabilities.

- [Previous Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-using-a-proto-shield.md)
- [Next Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/library.md)

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
