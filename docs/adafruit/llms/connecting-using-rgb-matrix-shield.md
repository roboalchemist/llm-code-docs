# Source: https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-using-rgb-matrix-shield.md

# RGB LED Matrix Basics

## Connecting Using RGB Matrix Shield

This is the **preferred** method for pairing these matrices with an Arduino-sized board, as it’s quick and trouble-free.

The **Adafruit RGB Matrix Shield** works with the **Arduino Uno** and **Zero** , and the **Adafruit Metro M0** …and with one or more jumper wires can work with the **Metro M4** (and potentially other boards with this form factor, if a compatible Arduino library is available).

The shield does **_not_** &nbsp;directly work with the Arduino Mega — additional jumper wires are needed to pins off the shield — see the “Jumper Wires” page for pinouts, or consider making your own Mega proto shield for that board.

## Assembling the Partially Assembled Version
The shield comes with the button, terminal block, and the 16-pin header already soldered on. All you need to do is solder the headers!

The included headers should be installed from the underside and soldered from the top.

![led_matrices_RGBMS_top_header.jpg](https://cdn-learn.adafruit.com/assets/assets/000/120/965/medium640/led_matrices_RGBMS_top_header.jpg?1683909012)

![led_matrices_RGBMS_top_angle.jpg](https://cdn-learn.adafruit.com/assets/assets/000/120/966/medium640/led_matrices_RGBMS_top_angle.jpg?1683909028)

## Assembling the Original Version
The shield arrives unpopulated and you’ll need to do a little soldering to get it going.

Header pins are installed from the underside and soldered on top. Three components — a button, power terminal and 16-pin header — insert from the top and are soldered underneath.

**The 16-pin (8x2) header must be installed in the correct orientation!** The polarity notch is indicated on the silkscreen, or you can see in the photos above that the notch faces the digital I/O pins. If you install this backwards the matrix will not work!

![led_matrices_umpopulated.jpg](https://cdn-learn.adafruit.com/assets/assets/000/055/701/medium640/led_matrices_umpopulated.jpg?1529447599)

![led_matrices_populated.jpg](https://cdn-learn.adafruit.com/assets/assets/000/055/702/medium640/led_matrices_populated.jpg?1529447609)

## Powering the Shield

Power to the LED matrix can be connected to the shield’s screw terminals — red wire to +5Vout, black wire to GND — and the whole circuit is then powered from the Arduino’s DC jack or a USB cable at a safe and regulated 5 Volts.

## Metro M4 Usage
The shield requires a small modification to work with the Adafruit **Metro M4** :

- Use a small file or hobby knife to cut the PCB trace between the two pads indicated here.
- Solder a wire from the adjacent “CLK” pin to the “Analog In 4” pin.

![led_matrices_metro-m4-diagram.jpg](https://cdn-learn.adafruit.com/assets/assets/000/055/703/medium640/led_matrices_metro-m4-diagram.jpg?1529450576)

A corresponding change is required in one’s code — look for the “CLK” pin definition in any of the matrix examples…

```
#define CLK 8
```

And change the “8” to “A4”:

```
#define CLK A4
```

Warning: 

## Metro RP2350 Usage
Jumper Wires are needed for the four address pins A, B, C and D. The reason for this is those address pins on the shield align to the RP2350 Port 1. However all GPIOs need to be on Port 0 for this chip to work. This means each on the shield pins A0, A1, A2 and A3 need to have a trace cut and a small wire soldered re-routing the connections over to the D1, D11, D22 and D23 pins of the Metro RP2350.&nbsp;

```auto
Address Line   Shield Default   (Port 1, bad)   →   Rewired To    (Port 0, good)
-----------------------------------------------------------------------------
A              A0  (GPIO42)                     →   D1   (GPIO1, TX)
B              A1  (GPIO43)                     →   D11  (GPIO11)
C              A2  (GPIO44)                     →   D22  (GPIO22)
D              A3  (GPIO45)                     →   D23  (GPIO23)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/139/738/medium800/led_matrices_IMG_3748.jpeg?1758134481 Metro RP2350 RGB Matrix Shield)

## Metro RP2350 CircuitPython Shapes
```auto
import board
import displayio
import rgbmatrix
import framebufferio
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.triangle import Triangle

displayio.release_displays()

# Panel wiring with A→D1, B→D11, C→D22, D→D23
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=4,
    rgb_pins=[board.D2, board.D3, board.D4, board.D5, board.D6, board.D7],
    addr_pins=[board.D1, board.D11, board.D22, board.D23],  # rewired
    clock_pin=board.D8,
    latch_pin=board.D10,
    output_enable_pin=board.D9,
    doublebuffer=True
)
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

# Root group
root = displayio.Group()
display.root_group = root

# Background (black rectangle)
root.append(Rect(0, 0, display.width, display.height, fill=0x000000))

# Shapes
root.append(Circle(12, 16, 10, fill=0xFF0000))        # red circle left
root.append(Rect(26, 8, 14, 14, fill=0x00FF00))       # green square center
root.append(Triangle(42, 24, 50, 8, 58, 24, fill=0x0000FF))  # blue triangle right

# Done — shapes are static, nothing else needed
while True:
    pass
```

- [Previous Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/new-wiring.md)
- [Next Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-with-jumper-wires.md)

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
