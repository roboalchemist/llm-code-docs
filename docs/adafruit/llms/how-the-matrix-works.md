# Source: https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/how-the-matrix-works.md

# RGB LED Matrix Basics

## How the Matrix Works

There's no “official” documention out there on how these matrices work, and no public datasheets or spec sheets so we are going to try to document how they work.  
  
First thing to notice is that there are 512 RGB LEDs in a 16x32 matrix. Like pretty much every matrix out there, **you can't drive all 512 at once**. One reason is that would require a lot of current, another reason is that it would be really expensive to have so many pins. Instead, the matrix is divided into 8 interleaved sections/strips. The first section is the 1st 'line' and the 9th 'line' (32 x 2 RGB LEDs = 64 RGB LEDs), the second is the 2nd and 10th line, etc until the last section which is the 8th and 16th line. You might be asking, why are the lines paired this way? wouldnt it be nicer to have the first section be the 1st and 2nd line, then 3rd and 4th, until the 15th and 16th? The reason they do it this way is so that the lines are interleaved and look better when refreshed, otherwise we'd see the stripes more clearly.  
  
So, on the PCB are 12 LED driver chips. These are like 74HC595s but they have 16 outputs and they are constant current. 16 outputs \* 12 chips = 192 LEDs that can be controlled at once, and 64 \* 3 (R G and B) = 192. So now the design comes together: You have 192 outputs that can control one line at a time, with each of 192 R, G and B LEDs either on or off. The controller (say an FPGA or microcontroller) selects which section to currently draw (using A, B, and C address pins - 3 bits can have 8 values). Once the address is set, the controller clocks out 192 bits of data (24 bytes) and latches it. Then it increments the address and clocks out another 192 bits, etc until it gets to address #7, then it sets the address back to #0  
  
The only downside of this technique is that despite being very simple and fast, it has **no PWM control** built in! The controller can **only** set the LEDs **on or off**. So what do you do when you want full color? You actually need to draw the entire matrix over and over again at very high speeds to PWM the matrix manually. For that reason, you need to have a very fast controller (50 MHz is a minimum) if you want to do a lot of colors and motion video and have it look good.  
  
How quickly can we feed data to the matrix? Forum users Andrew Silverman and Ryan Brown have been [posting their progress](http://forums.adafruit.com/viewtopic.php?f=47&t=26130&start=0) driving the 16x32 matrix with an FPGA, and the limit appears to be somewhere between 40 and 50 MHz. Ryan writes: “I haven't validated 100% pixel correctness, but 50 MHz seems to work for me […] 67MHz definitely did not work.” He also provided this graph showing current draw relative to clock frequency:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/965/medium800/led_matrix_16x32ledmatrixcurrent.png?1396789475)

_Image above by rhb.me (CC By-NC-SA)_  
  
“Notice that the LED panel current consumption decreases as clock frequency increases. This suggests that the LED ‘on time’ is decreasing. I’m guessing this is caused by frequency-invariant delays in the LED driver shift registers.”- [Previous Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/library.md)
- [Next Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/faq.md)

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
