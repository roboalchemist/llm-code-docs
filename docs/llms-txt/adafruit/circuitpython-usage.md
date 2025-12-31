# Source: https://learn.adafruit.com/12mm-led-pixels/circuitpython-usage.md

# Source: https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-usage.md

# Source: https://learn.adafruit.com/12mm-led-pixels/circuitpython-usage.md

# Source: https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-usage.md

# Monochrome OLED Breakouts

## CircuitPython Usage

Warning: 

It's easy to use OLEDs with Python and the [Adafruit CircuitPython DisplayIO SSD1306](https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306) module.&nbsp; This module allows you to easily write Python code to control the display.

To demonstrate the usage, we'll initialize the library and use Python code to control the OLED from the board's Python REPL.

# I2C Initialization

If your display is connected to the board using I2C (like if using a Feather and the FeatherWing OLED) you'll first need to initialize the I2C bus. &nbsp;First import the necessary modules:

```
import board
```

Now for either board run this command to create the I2C instance using the default SCL and SDA pins (which will be marked on the boards pins if using a Feather or similar Adafruit board):

```
i2c = board.I2C()
```

After initializing the I2C interface for your firmware as described above, you can create an instance&nbsp;of the `I2CDisplayBus`:

```auto
import displayio
import i2cdisplaybus
import adafruit_displayio_ssd1306

# Release any previously allocated resources
displayio.release_displays()

display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3c)
```

Finally, you can pass the `display_bus` in and create an instance&nbsp;of the SSD1306 I2C driver by running:

```auto
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
```

Now you should be seeing an image of the REPL. Note that the last two parameters to the&nbsp;`SSD1306`&nbsp;class initializer are the&nbsp; **width** &nbsp;and&nbsp; **height** &nbsp;of the display in pixels. &nbsp;Be sure to use the right values for the display you're using!

### Initializing with CircuitPython 9

Because displayio has grown so much since it was first written, it has been split up into separate modules to make better use of space on boards with limited storage. Due to splitting things up, the initialization has changed slightly in CircuitPython 9.

```auto
import displayio
import i2cdisplaybus
import adafruit_displayio_ssd1306

# Release any previously allocated resources
displayio.release_displays()

display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
```

## 128 x 64 size OLEDs (or changing the I2C address)

If you are using a 128x64 display, the I2C address&nbsp;is probably&nbsp;different (`0x3d`), unless you've changed it by soldering some jumpers:

```auto
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3d)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
```

## Adding hardware reset pin

If you have a `reset` pin (which may be required if your OLED does not have an auto-reset chip like the FeatherWing) also pass in a reset pin like so:

```auto
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3c, reset=board.D9)
```

At this point the I2C bus and display are initialized. **Skip down to the example code section.**

# SPI Initialization

If your display is connected to the board using SPI you'll first need to initialize the SPI bus.&nbsp;

If you're using a microcontroller board, run the following commands:

```auto
import board
import displayio
import fourwire
import adafruit_displayio_ssd1306

# Release any previously allocated resources
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D5
tft_dc = board.D6
tft_reset = board.D9

display_bus = fourwire.FourWire(spi, command=tft_dc, chip_select=tft_cs,
                                 reset=tft_reset, baudrate=1000000)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
```

The parameters to the FourWire initializer are the pins connected to the display's&nbsp; **DC** ,&nbsp; **CS,** and **reset**. Because we are using keyword arguments, they can be in any position.&nbsp; Again make sure to use the right pin names as you have wired up to your board!

Note that the last two parameters to the&nbsp;`SSD1306`&nbsp;class initializer are the&nbsp; **width** &nbsp;and&nbsp; **height** &nbsp;of the display in pixels. Be sure to use the right values for the display you're using!

# Example Code
https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306/blob/main/examples/displayio_ssd1306_simpletest.py

Let's take a look at the sections of code one by one.&nbsp;We start by importing the `board` so that we can initialize&nbsp;SPI,&nbsp;`displayio`,(`FourWire` or `I2CDisplayBus` depending on your display),`terminalio` for the font, a `label`, and the&nbsp;`adafruit_displayio_ssd1306`&nbsp;driver.

```auto
import board
import displayio

# from fourwire import FourWire
import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus

import adafruit_displayio_ssd1306
```

Next we release any previously used displays. This is important because if the microprocessor is reset, the display pins are not automatically released and this makes them available for use again.

```
displayio.release_displays()
```

Next we define the reset line, which will be used for either SPI or I2C.

```
oled_reset = board.D9

```

If you're using I2C, you would use this section of code.&nbsp;We set the I2C object to the board's I2C with the easy shortcut function&nbsp;`board.I2C()`. By using this function, it finds the SPI module and initializes using the default SPI parameters.&nbsp;We also set the display bus to `I2CDisplay` which makes use of the I2C bus.

```auto
# Use for I2C
i2c = board.I2C()
display_bus = I2CDisplayBus(i2c, device_address=0x3c, reset=oled_reset)
```

If you're using SPI, you would use this section of code. Don't forget to update the import section accordingly. We set the SPI object to the board's SPI with the easy shortcut function `board.SPI()`. By using this function, it finds the SPI module and initializes using the default SPI parameters. We set the OLED's&nbsp; **CS** (Chip Select), and&nbsp; **DC** (Data/Command)&nbsp;pins.&nbsp;We also set the display bus to FourWire which makes use of the SPI bus. The SSD1306 needs to be slowed down to 1MHz, so we pass in the additional baudrate parameter.

```auto
spi = board.SPI()
oled_cs = board.D5
oled_dc = board.D6
display_bus = FourWire(spi, command=oled_dc, chip_select=oled_cs,
                                 reset=oled_reset, baudrate=1000000)
```

In order to make it easy to change display sizes, we'll define a few variables in one spot here. We have the display width, the display height and the border size, which we will explain a little further below. If your display is something different than these numbers, change them to the correct setting.

```
WIDTH = 128
HEIGHT = 32     # Change to 64 if needed
BORDER = 5
```

Finally, we initialize the driver with a width of the **WIDTH** variable and a height of the **HEIGHT** variable. If we stopped at this point and ran the code, we would have a terminal that we could type at and have the screen update.

```
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

```

![](https://cdn-learn.adafruit.com/assets/assets/000/081/203/medium800/adafruit_products_repl.jpeg?1569015565)

Next we create a background splash image. We do this by creating a group that we can add elements to and adding that group to the display. In this example, we are limiting the maximum number of elements to 10, but this can be increased if you would like. The display will automatically handle updating the group.

```auto
splash = displayio.Group()
display.root_group = splash
```

Next we create a Bitmap that is the full width and height of the display. The Bitmap is like a canvas that we can draw on. In this case we are creating the Bitmap to be the same size as the screen, but only have one color. Although the Bitmaps can handle up to 256 different colors, the display is monochrome so we only need one. We create a Palette with one color and set that color to `0xFFFFFF` which happens to be white. If were to place a different color here, `displayio` handles color conversion automatically, so it may end up black or white depending on the calculation.

```
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF # White
```

With all those pieces in place, we create a TileGrid by passing the bitmap and palette and draw it at&nbsp;`(0, 0)`&nbsp;which represents the display's upper left.

```
bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/081/205/medium800/adafruit_products_white_box.jpeg?1569016237)

Next we will create a smaller black rectangle. The easiest way to do this is to create a new bitmap that is a little smaller than the full screen with a single color of `0x000000`, which is **black** , and place it in a specific location. In this case, we will create a bitmap that is 5 pixels smaller on each side. This is where the **BORDER** variable comes into use. It makes calculating the size of the second rectangle much easier. The screen we're using here is **128x64** and we have the BORDER set to **5&nbsp;** , so we'll want to subtract 10 from each of those numbers.

We'll also want to place it at the position&nbsp;`(5, 5)` so that it ends up centered.

```
# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH-BORDER*2, HEIGHT-BORDER*2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000 # Black
inner_sprite = displayio.TileGrid(inner_bitmap,
                                  pixel_shader=inner_palette,
                                  x=BORDER, y=BORDER)
splash.append(inner_sprite)
```

Since we are adding this after the first square, it's automatically drawn on top. Here's what it looks like now.

![](https://cdn-learn.adafruit.com/assets/assets/000/081/209/medium800/adafruit_products_black_box.jpeg?1569016337)

Next add a label that says "Hello World!" on top of that. We're going to use the built-in Terminal Font. In this example, we won't be doing any scaling because of the small resolution, so we'll add the label directly the main group. If we were scaling, we would have used a subgroup.

Labels are centered vertically, so we'll place it at half the HEIGHT for the Y coordinate and subtract one so it looks good. We use the `//` operator to divide because we want a whole number returned and it's an easy way to round it. We'll set the width to around 28 pixels make it appear to be centered horizontally, but if you want to change the text, change this to whatever looks good to you. Let's go with some white text, so we'll pass it a value of `0xFFFFFF`.

```
# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT//2-1)
splash.append(text_area)
```

Finally, we place an infinite loop at the end so that the graphics screen remains in place and isn't replaced by a terminal.

```
while True:
    pass
```

![](https://cdn-learn.adafruit.com/assets/assets/000/081/214/medium800/adafruit_products_hello_world.jpeg?1569016522)

If you've been following along with a FeatherWing or 128x32 OLED, this is what it should look like:

![](https://cdn-learn.adafruit.com/assets/assets/000/081/283/medium800/adafruit_products_featherwing.jpeg?1569109843)

## Where to go from here

Be sure to check out this excellent&nbsp;[guide to CircuitPython Display Support Using displayio](https://learn.adafruit.com/circuitpython-display-support-using-displayio)

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-setup.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/python-wiring.md)

## Featured Products

### Monochrome 1.3" 128x64 OLED graphic display - STEMMA QT / Qwiic

[Monochrome 1.3" 128x64 OLED graphic display - STEMMA QT / Qwiic](https://www.adafruit.com/product/938)
These displays are small, only about 1.3" diagonal, but very readable due to the high contrast of an OLED display. This display is made of 128x64 individual white OLED pixels, each one is turned on or off by the controller chip. Because the display makes its own light, no backlight is...

In Stock
[Buy Now](https://www.adafruit.com/product/938)
[Related Guides to the Product](https://learn.adafruit.com/products/938/guides)
### Monochrome 0.96" 128x64 OLED Graphic Display - STEMMA QT

[Monochrome 0.96" 128x64 OLED Graphic Display - STEMMA QT](https://www.adafruit.com/product/326)
These displays are small, only about 1" diagonal, but very readable due to the high contrast of an OLED display. This display is made of 128x64 individual white OLED pixels, each one is turned on or off by the controller chip. Because the display makes its own light, no backlight is...

Out of Stock
[Buy Now](https://www.adafruit.com/product/326)
[Related Guides to the Product](https://learn.adafruit.com/products/326/guides)
### Monochrome 128x32 SPI OLED graphic display

[Monochrome 128x32 SPI OLED graphic display](https://www.adafruit.com/product/661)
These displays are small, only about 1" diagonal, but very readable due to the high contrast of an OLED display. This display is made of 128x32 individual white OLED pixels, each one is turned on or off by the controller chip. Because the display makes its own light, no backlight is...

In Stock
[Buy Now](https://www.adafruit.com/product/661)
[Related Guides to the Product](https://learn.adafruit.com/products/661/guides)
### Monochrome 128x32 I2C OLED graphic display

[Monochrome 128x32 I2C OLED graphic display](https://www.adafruit.com/product/931)
These displays are small, only about 1" diagonal, but very readable due to the high contrast of an OLED display. This display is made of 128x32 individual white OLED pixels, each one is turned on or off by the controller chip. Because the display makes its own light, no backlight is...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/931)
[Related Guides to the Product](https://learn.adafruit.com/products/931/guides)
### Monochrome 0.91" 128x32 I2C OLED Display - STEMMA QT / Qwiic

[Monochrome 0.91" 128x32 I2C OLED Display - STEMMA QT / Qwiic](https://www.adafruit.com/product/4440)
These displays are small, only about 1" diagonal, but very readable due to the high contrast of an OLED display. This display is made of 128x32 individual white OLED pixels, each one is turned on or off by the controller chip. Because the display makes its own light, no backlight is...

In Stock
[Buy Now](https://www.adafruit.com/product/4440)
[Related Guides to the Product](https://learn.adafruit.com/products/4440/guides)

## Related Guides

- [MIDI for Makers](https://learn.adafruit.com/midi-for-makers.md)
- [CircuitPython Hardware: SSD1306 OLED Display](https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display.md)
- [Steampunk Cameo Necklace with OLED Display](https://learn.adafruit.com/steampunk-cameo-necklace.md)
- [SSD1306 OLED Displays with Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black.md)
- [Using QMK on RP2040 Microcontrollers](https://learn.adafruit.com/using-qmk-on-rp2040-microcontrollers.md)
- [4x4 Rotary Encoder MIDI Messenger](https://learn.adafruit.com/4x4-rotary-encoder-midi-messenger.md)
- [Using the TRRS Trinkey as an Assistive Technology Device](https://learn.adafruit.com/using-the-trrs-trinkey-as-an-assistive-technology-device.md)
- [USB MIDI Keyset Controller](https://learn.adafruit.com/midi-keyset.md)
- [Adafruit OLED Displays for Raspberry Pi](https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi.md)
- [Adafruit FT232H With SPI & I2C Devices](https://learn.adafruit.com/adafruit-ft232h-with-spi-and-i2c-libraries.md)
- [Monitor Your Greenhouse with a No-Code Environmental Sensor](https://learn.adafruit.com/monitor-your-greenhouse-with-a-no-code-environmental-sensor.md)
- [Pro Trinket Power Meter](https://learn.adafruit.com/pro-trinket-power-meter.md)
- [Toddler Timer](https://learn.adafruit.com/toddler-timer.md)
- [CircuitPython OLED and Dual Knob Sketcher](https://learn.adafruit.com/circuitpython-oled-knob-sketcher.md)
- [Adafruit 5x5 NeoPixel Grid BFF](https://learn.adafruit.com/adafruit-5x5-neopixel-grid-bff.md)
