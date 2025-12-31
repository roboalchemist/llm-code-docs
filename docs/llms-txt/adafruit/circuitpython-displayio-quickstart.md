# Source: https://learn.adafruit.com/2-2-tft-display/circuitpython-displayio-quickstart.md

# Source: https://learn.adafruit.com/1-8-tft-display/circuitpython-displayio-quickstart.md

# Source: https://learn.adafruit.com/096-mini-color-oled/circuitpython-displayio-quickstart.md

# 0.96" mini Color OLED

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

## Required CircuitPython Libraries

To use this display with `displayio`, there is only one required library.

[Adafruit_CircuitPython_SSD1331](https://github.com/adafruit/Adafruit_CircuitPython_SSD1331/releases)
First, make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)&nbsp;for your board.

Next, you'll need to install the necessary libraries&nbsp;to use the hardware--carefully follow the steps to find and install these libraries from&nbsp;[Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).&nbsp; Our introduction guide has&nbsp;[a great page on how to install the library bundle](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries)&nbsp;for both express and non-express boards.

Remember for non-express boards, you'll need to manually install the necessary libraries from the bundle:

- **adafruit\_ssd1331**

Before continuing make sure your board's lib folder or root filesystem has the&nbsp; **adafruit\_ssd1331** &nbsp;file copied over.

## Code Example Additional Libraries

For the Code Example, you will need an additional library. We decided to make use of a library so the code didn't get overly complicated.

[Adafruit_CircuitPython_Display_Text](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text/releases)
Go ahead and install this in the same manner as the driver library by copying the&nbsp; **adafruit\_display\_text** folder over to the **lib** folder on your CircuitPython device.

## CircuitPython Code Example
https://github.com/adafruit/Adafruit_CircuitPython_SSD1331/blob/main/examples/ssd1331_simpletest.py

Let's take a look at the sections of code one by one.&nbsp;We start by importing the board so that we can initialize&nbsp;`SPI`,&nbsp;`displayio`,`terminalio` for the font, a `label`, and the&nbsp;`adafruit_ssd1331`&nbsp;driver.

```
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_ssd1331 import SSD1331
```

Next we release any previously used displays. This is important because if the Feather is reset, the display pins are not automatically released and this makes them available for use again.

```
    displayio.release_displays()
  
```

Next, we set the SPI object to the board's SPI with the easy shortcut function&nbsp;`board.SPI()`. By using this function, it finds the SPI module and initializes using the default SPI parameters.

```
spi = board.SPI()
tft_cs = board.D5
tft_dc = board.D6
```

In the next line, we set the display bus to FourWire which makes use of the SPI bus.

```
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D9)
```

Finally, we initialize the driver with a width of 96 and a height of 64. If we stopped at this point and ran the code, we would have a terminal that we could type at and have the screen update.

```
display = SSD1331(display_bus, width=96, height=64)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/079/311/medium800/arduino_compatibles_ssd1331-text-only.jpg?1565654654)

Next we create a background splash image. We do this by creating a group that we can add elements to and adding that group to the display. In this example, we are limiting the maximum number of elements to 10, but this can be increased if you would like. The display will automatically handle updating the group.

```auto
splash = displayio.Group(max_size=10)
display.root_group = splash
```

Next we create a Bitmap which is like a canvas that we can draw on. In this case we are creating the Bitmap to be the same size as the screen, but only have one color. The Bitmaps can currently handle up to 256 different colors. We create a Palette with one color and set that color to 0x00FF00 which happens to be green. Colors are Hexadecimal values in the format of RRGGBB. Even though the Bitmaps can only handle 256 colors at a time, you get to define what those 256 different colors are.

```
color_bitmap = displayio.Bitmap(96, 64, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00 # Bright Green
```

With all those pieces in place, we create a TileGrid by passing the bitmap and palette and draw it at&nbsp;`(0, 0)`&nbsp;which represents the display's upper left.

```
bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/079/312/medium800/arduino_compatibles_ssd1331-green.jpg?1565655750)

Next we will create a smaller purple square. The easiest way to do this is the create a new bitmap that is a little smaller than the full screen with a single color and place it in a specific location. In this case, we will create a bitmap that is 5 pixels smaller on each side. The screen is **96x64** , so we'll want to subtract 10 from each of those numbers.

We'll also want to place it at the position&nbsp;`(5, 5)` so that it ends up centered.

```
inner_bitmap = displayio.Bitmap(86, 54, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088 # Purple
inner_sprite = displayio.TileGrid(inner_bitmap,
                                  pixel_shader=inner_palette,
                                  x=5, y=5)
splash.append(inner_sprite)
```

Since we are adding this after the first square, it's automatically drawn on top. Here's what it looks like now.

![](https://cdn-learn.adafruit.com/assets/assets/000/079/314/medium800/arduino_compatibles_ssd1331-green-purple.jpg?1565655779)

Next let's add a label that says "Hello World!" on top of that. We're going to use the built-in Terminal Font. In this example, we won't be doing any scaling because of the small resolution, so we'll add the label directly the main group. If we were scaling, we would have used a subgroup.

Labels are centered vertically, so we'll place it at 32 for the Y coordinate, and around 12 pixels make it appear to be centered horizontally, but if you want to change the text, change this to whatever looks good to you. Let's go with some yellow text, so we'll pass it a value of `0xFFFF00`.

```
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=12, y=32)
splash.append(text_area)
```

Finally, we place an infinite loop at the end so that the graphics screen remains in place and isn't replaced by a terminal.

```
while True:
    pass
```

![](https://cdn-learn.adafruit.com/assets/assets/000/079/316/medium800/arduino_compatibles_ssd1331-hello-world.jpg?1565655819)

## Where to go from here

Be sure to check out this excellent&nbsp;[guide to CircuitPython Display Support Using displayio](https://learn.adafruit.com/circuitpython-display-support-using-displayio)

- [Previous Page](https://learn.adafruit.com/096-mini-color-oled/drawing-bitmaps.md)
- [Next Page](https://learn.adafruit.com/096-mini-color-oled/python-wiring-and-setup.md)

## Featured Products

### OLED Breakout Board - 16-bit Color 0.96" w/microSD holder

[OLED Breakout Board - 16-bit Color 0.96" w/microSD holder](https://www.adafruit.com/product/684)
We love our black and white monochrome displays but we also like to dabble with some color now and then. Our new 0.96" color OLED displays are perfect when you need an ultra-small display with vivid, high-contrast 16-bit color. The visible portion of the OLED measures 0.96" diagonal...

In Stock
[Buy Now](https://www.adafruit.com/product/684)
[Related Guides to the Product](https://learn.adafruit.com/products/684/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [OLED TRON Clock](https://learn.adafruit.com/oled-tron-clock.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [Programming Arduino with Android and Windows Tablets](https://learn.adafruit.com/programming-arduino-with-android-and-windows-tablets.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [Bluefruit LE Connect for iOS and Android](https://learn.adafruit.com/bluefruit-le-connect.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [Trellis 3D Printed Enclosure](https://learn.adafruit.com/trellis-3d-printed-enclosure.md)
