# Source: https://learn.adafruit.com/1-8-tft-display/circuitpython-displayio-quickstart-2.md

# 1.8" TFT Display Breakout and Shield

## CircuitPython Displayio Quickstart

You will need a board capable of running CircuitPython such as the Metro M0 Express or the Metro M4 Express. You can also use boards such as the Feather M0 Express or the Feather M4 Express. We recommend either the Metro M4 or the Feather M4 Express because it's much faster and works better for driving a display. For this guide, we will be using a Feather M4 Express. The steps should be about the same for the Feather M0 Express or either of the Metros. If you haven't already, be sure to check out our&nbsp;[Feather M4 Express](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/assembly)&nbsp;guide.

### Adafruit Feather M4 Express - Featuring ATSAMD51

[Adafruit Feather M4 Express - Featuring ATSAMD51](https://www.adafruit.com/product/3857)
It's what you've been waiting for, the Feather M4 Express featuring ATSAMD51. This Feather is fast like a swift, smart like an owl, strong like a ox-bird (it's half ox, half bird, OK?) This feather is powered by our new favorite chip, the **ATSAMD51J19** -&nbsp; with...

In Stock
[Buy Now](https://www.adafruit.com/product/3857)
[Related Guides to the Product](https://learn.adafruit.com/products/3857/guides)
![Angled shot of a Adafruit Feather M4 Express. ](https://cdn-shop.adafruit.com/640x480/3857-06.jpg)

## Preparing the Breakout

Before using the TFT Breakout, you will need to solder the headers or some wires to it. Be sure to check out the&nbsp;[Adafruit Guide To Excellent Soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering).&nbsp;After that the breakout should be ready to go.

## Wiring the Breakout to the Feather

- **3-5V VCC** connects to the Feather&nbsp; **3V** pin
- **GND** connects toFeather ground
- **SCK** connects to SPI clock. On the Feather that's **SCK**.
- **MISO** connects to SPI MISO. On the Feather that's **MI**
- **MOSI** connects to SPI MOSI. On the Feather that's **MO**
- **TFT\_CS** connects to our SPI Chip Select pin. We'll be using **Digital 5** but you can later change this to any pin
- **D/C** connects to our SPI data/command select pin. We'll be using **Digital 6** but you can later change this pin too.
- **RESET** &nbsp;connects to our reset pin. We'll be using **Digital 9** but you can later change this pin too.
- **LITE** connects to the Feather **3V** pin. This is the only display that this pin is required to be connected or the backlight won't work.

![](https://cdn-learn.adafruit.com/assets/assets/000/116/511/medium800/arduino_compatibles_tft_fritzing_circuit.png?1667858706)

[Download Fritzing Object](https://cdn-learn.adafruit.com/assets/assets/000/116/512/original/160x128-breakout-feather-m4-fritzing.zip?1667860723)
## Required CircuitPython Libraries

To use this display with `displayio`, there is only one required library.

[Adafruit_CircuitPython_ST7735R](https://github.com/adafruit/Adafruit_CircuitPython_ST7735R/releases)
First, make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)&nbsp;for your board.

Next, you'll need to install the necessary libraries&nbsp;to use the hardware--carefully follow the steps to find and install these libraries from&nbsp;[Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).&nbsp; Our introduction guide has&nbsp;[a great page on how to install the library bundle](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries)&nbsp;for both express and non-express boards.

Remember for non-express boards, you'll need to manually install the necessary libraries from the bundle:

- **adafruit\_st7735r**

Before continuing make sure your board's lib folder or root filesystem has the&nbsp; **adafruit\_st7735r** &nbsp;file copied over.

## Code Example Additional Libraries

For the Code Example, you will need an additional library. We decided to make use of a library so the code didn't get overly complicated.

[Adafruit_CircuitPython_Display_Text](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text)
Go ahead and install this in the same manner as the driver library by copying the&nbsp; **adafruit\_display\_text** folder over to the **lib** folder on your CircuitPython device.

## CircuitPython Code Example
https://github.com/adafruit/Adafruit_CircuitPython_ST7735R/blob/main/examples/st7735r_128x160_simpletest.py

Let's take a look at the sections of code one by one.&nbsp;We start by importing the board so that we can initialize&nbsp;`SPI`,&nbsp;`displayio`,`terminalio` for the font, a `label`, and the&nbsp;`adafruit_st7735r`&nbsp;driver.

```
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

Next we release any previously used displays. This is important because if the Feather is reset, the display pins are not automatically released and this makes them available for use again.

```
displayio.release_displays()<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

Next, we set the SPI object to the board's SPI with the easy shortcut function&nbsp;`board.SPI()`. By using this function, it finds the SPI module and initializes using the default SPI parameters.

```
spi = board.SPI()
tft_cs = board.D5
tft_dc = board.D6<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

In the next line, we set the display bus to FourWire which makes use of the SPI bus.

```
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D9)<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

Finally, we initialize the driver with a width of 160 and a height of 128. If we stopped at this point and ran the code, we would have a terminal that we could type at and have the screen update. Because we want to use the display horizontally and the default orientation is vertical, we rotate it 90 degrees. One other parameter that we provide is `bgr=True`&nbsp;and the reason for this is that the color ordering of certain displays is Blue, Green, Red rather than the usual Red, Green, Blue. It tell displayio the correct color ordering for this particular display.

```
display = ST7735R(display_bus, width=160, height=128, rotation=90, bgr=True)
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

![](https://cdn-learn.adafruit.com/assets/assets/000/079/478/medium800/arduino_compatibles_128x160-text.jpeg?1565887821)

Next we create a background splash image. We do this by creating a group that we can add elements to and adding that group to the display. In this example, we are limiting the maximum number of elements to 10, but this can be increased if you would like. The display will automatically handle updating the group.

```auto
splash = displayio.Group(max_size=10)
display.root_group = splash
```

Next we create a Bitmap which is like a canvas that we can draw on. In this case we are creating the Bitmap to be the same size as the screen, but only have one color. The Bitmaps can currently handle up to 256 different colors. We create a Palette with one color and set that color to 0x00FF00 which happens to be green. Colors are Hexadecimal values in the format of RRGGBB. Even though the Bitmaps can only handle 256 colors at a time, you get to define what those 256 different colors are.

```
color_bitmap = displayio.Bitmap(160, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00 # Bright Green<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

With all those pieces in place, we create a TileGrid by passing the bitmap and palette and draw it at&nbsp;`(0, 0)`&nbsp;which represents the display's upper left.

```
bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

![](https://cdn-learn.adafruit.com/assets/assets/000/079/479/medium800/arduino_compatibles_128x160-green.jpeg?1565887834)

Next we will create a smaller purple square. The easiest way to do this is the create a new bitmap that is a little smaller than the full screen with a single color and place it in a specific location. In this case, we will create a bitmap that is 5 pixels smaller on each side. The screen is **160x128** , so we'll want to subtract 10 from each of those numbers.

We'll also want to place it at the position&nbsp;`(5, 5)` so that it ends up centered.

```
inner_bitmap = displayio.Bitmap(150, 118, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088 # Purple
inner_sprite = displayio.TileGrid(inner_bitmap,
                                  pixel_shader=inner_palette,
                                  x=5, y=5)
splash.append(inner_sprite)<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

Since we are adding this after the first square, it's automatically drawn on top. Here's what it looks like now.

![](https://cdn-learn.adafruit.com/assets/assets/000/079/481/medium800/arduino_compatibles_128x160-green-purple.jpeg?1565887856)

Next let's add a label that says "Hello World!" on top of that. We're going to use the built-in Terminal Font and scale it up by a factor of two. To scale the label only, we will make use of a subgroup, which we will then add to the main group.

Labels are centered vertically, so we'll place it at 64 for the Y coordinate, and around 11 pixels make it appear to be centered horizontally, but if you want to change the text, change this to whatever looks good to you. Let's go with some yellow text, so we'll pass it a value of `0xFFFF00`.

```
text_group = displayio.Group(max_size=10, scale=2, x=11, y=64)
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area) # Subgroup for text scaling
splash.append(text_group)<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

Finally, we place an infinite loop at the end so that the graphics screen remains in place and isn't replaced by a terminal.

```
while True:
    pass<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div>
```

![](https://cdn-learn.adafruit.com/assets/assets/000/079/482/medium800/arduino_compatibles_128x160-hello-world.jpeg?1565887866)

## Where to go from here

Be sure to check out this excellent&nbsp;[guide to CircuitPython Display Support Using displayio](https://learn.adafruit.com/circuitpython-display-support-using-displayio)

- [Previous Page](https://learn.adafruit.com/1-8-tft-display/displaying-bitmaps.md)
- [Next Page](https://learn.adafruit.com/1-8-tft-display/python-wiring-and-setup.md)

## Featured Products

### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### 1.8" Color TFT LCD display with MicroSD Card Breakout

[1.8" Color TFT LCD display with MicroSD Card Breakout](https://www.adafruit.com/product/358)
This lovely little display breakout is the best way to add a small, colorful and bright display to any project. Since the display uses 4-wire SPI to communicate and has its own pixel-addressable frame buffer, it can be used with every kind of microcontroller. Even a very small one with low...

Out of Stock
[Buy Now](https://www.adafruit.com/product/358)
[Related Guides to the Product](https://learn.adafruit.com/products/358/guides)
### Adafruit 1.8" Color TFT Shield w/microSD and Joystick

[Adafruit 1.8" Color TFT Shield w/microSD and Joystick](https://www.adafruit.com/product/802)
This lovely little shield is the best way to add a small, colorful and bright display to any project. We took our popular 1.8" TFT breakout board and remixed it into an Arduino shield complete with microSD card slot and a 5-way joystick navigation switch and three selection buttons! Since...

In Stock
[Buy Now](https://www.adafruit.com/product/802)
[Related Guides to the Product](https://learn.adafruit.com/products/802/guides)
### 1.8" SPI TFT display, 160x128 18-bit color - ST7735R driver

[1.8" SPI TFT display, 160x128 18-bit color - ST7735R driver](https://www.adafruit.com/product/618)
We just love this little 1.8" TFT display, with true TFT color (up to 18-bits per pixel!), fine 160x128 resolution, two white LED backlight that runs on 3.3V and a very easy SPI interface that requires only 4 or 5 digital pins to send pixels to the display.  
  
**Please...**

Out of Stock
[Buy Now](https://www.adafruit.com/product/618)
[Related Guides to the Product](https://learn.adafruit.com/products/618/guides)

## Related Guides

- [Wave Shield](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [How to Build a Testing Jig](https://learn.adafruit.com/how-to-build-a-testing-fixture.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
- [Adafruit 1.27" and 1.5" Color OLED Breakout Board](https://learn.adafruit.com/adafruit-1-5-color-oled-breakout-board.md)
- [Arduino Lesson 15. DC Motor Reversing](https://learn.adafruit.com/adafruit-arduino-lesson-15-dc-motor-reversing.md)
- [TTL Serial Camera](https://learn.adafruit.com/ttl-serial-camera.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
