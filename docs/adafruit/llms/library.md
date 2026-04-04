# Source: https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/library.md

# RGB LED Matrix Basics

## RGBMatrix Library

Next up, load the **testshapes\_16x32** or **testshapes\_32x32** example sketch, which will test every drawing element available (again, you may need to edit the pin numbers for the 32x32 panel).

![](https://cdn-learn.adafruit.com/assets/assets/000/002/961/medium800/led_matrix_matrixshapes.jpg?1396789410)

The most simple thing you may want to do is draw a single pixel, we saw this introduced above.```
  // draw a pixel in solid white
  matrix.drawPixel(0, 0, matrix.Color333(7, 7, 7));
```

Next we will fill the screen with green by drawing a really large rectangle. The first two arguments are the top left point, then the width in pixels, and the height in pixels, finally the color```
  // fix the screen with green
  matrix.fillRect(0, 0, 32, 16, matrix.Color333(0, 7, 0));
```

Next we will draw just the outline of a rectangle, in yellow```
 // draw a box in yellow
  matrix.drawRect(0, 0, 32, 16, matrix.Color333(7, 7, 0));
```

Next you may want to draw lines. The **drawLine** procedure will draw a line in any color you want, we used this to draw a big X

```
  // draw an 'X' in red
  matrix.drawLine(0, 0, 31, 15, matrix.Color333(7, 0, 0));
  matrix.drawLine(31, 0, 0, 15, matrix.Color333(7, 0, 0));
```

The next shapes we draw are circles. You can draw the outline of a circle with **drawCircle** or fill a circle with **fillCircle**. The first two arguments are the center point, the third argument is the radius in pixels, finally the color to use.

```
  // draw a blue circle
  matrix.drawCircle(7, 7, 7, matrix.Color333(0, 0, 7));
 
  // fill a violet circle
  matrix.fillCircle(23, 7, 7, matrix.Color333(7, 0, 7));
```

 **fillScreen** allows you to fill the entire screen with a single color:

```
// fill the screen with 'black'
  matrix.fillScreen(matrix.Color333(0, 0, 0));
```

Finally, we draw the text that is shown up top as the demonstration image. We can use the **print** function, which you'll be familiar with from **Serial**. You can use **print** to print strings, numbers, variables, etc. However, we need to set up the printing before just going off and doing it! First, we must set the cursor location with **setCursor** which is where the top left pixel of the first character will go, this can be anywhere but note that text characters are 8 pixels high by default. Next **setTextSize** lets you set the size to 1 (8 pixel high) or 2 (16 pixel high for really big text!), you probably want just to stick with 1 for now. Lastly we can set the color of the text with **setTextColor**. Once this is all done, we can just use**print('1')** to print the character "1".

```
  // draw some text!
  matrix.setCursor(1, 0);   // start at top left, with one pixel of spacing
  matrix.setTextSize(1);    // size 1 == 8 pixels high
 
  // print each letter with a rainbow color
  matrix.setTextColor(matrix.Color333(7,0,0));
  matrix.print('1');
  matrix.setTextColor(matrix.Color333(7,4,0)); 
  matrix.print('6');
  matrix.setTextColor(matrix.Color333(7,7,0));
  matrix.print('x');
  matrix.setTextColor(matrix.Color333(4,7,0)); 
  matrix.print('3');
  matrix.setTextColor(matrix.Color333(0,7,0));  
  matrix.print('2');
 
  matrix.setCursor(1, 9);   // next line
  matrix.setTextColor(matrix.Color333(0,7,7)); 
  matrix.print('*');
  matrix.setTextColor(matrix.Color333(0,4,7)); 
  matrix.print('R');
  matrix.setTextColor(matrix.Color333(0,0,7));
  matrix.print('G');
  matrix.setTextColor(matrix.Color333(4,0,7)); 
  matrix.print("B");
  matrix.setTextColor(matrix.Color333(7,0,4)); 
  matrix.print("*");
```

![](https://cdn-learn.adafruit.com/assets/assets/000/002/962/medium800/led_matrix_rgbmatrix.jpg?1396789420)

- [Previous Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/test-example-code.md)
- [Next Page](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/how-the-matrix-works.md)

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
