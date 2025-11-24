# Source: https://learn.adafruit.com/monochrome-oled-breakouts/python-usage-2.md

# Monochrome OLED Breakouts

## Python Usage

It's easy to use OLEDs with Python and the [Adafruit CircuitPython SSD1306](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306) module.&nbsp; This module allows you to easily write Python code to control the display.

You can use this sensor with any computer that has GPIO and Python [thanks to Adafruit\_Blinka, our CircuitPython-for-Python compatibility library](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

To demonstrate the usage, we'll initialize the library and use Python code to control the OLED from the board's Python REPL.

Since we are running full CPython on our Linux/computer, we can take advantage of the powerful Pillow image drawing library to handle text, shapes, graphics, etc. [Pillow is a gold standard in image and graphics handling, you can read about all it can do here](https://pillow.readthedocs.io/en/stable/).

# I2C Initialization

If your display is connected to the board using I2C (like if using a PiOLED or Bonnet) you'll first need to initialize the I2C bus. &nbsp;First import the necessary modules:

```
import board
import busio
```

Now for either board run this command to create the I2C instance using the default SCL and SDA pins of your I2C host:

```
i2c = busio.I2C(board.SCL, board.SDA)
```

After initializing the I2C interface for your firmware as described above you can create an instance&nbsp;of the SSD1306 I2C driver by running:

```
import adafruit_ssd1306
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
```

Note that the first two parameters to the `SSD1306_I2C` class initializer are the&nbsp; **width** &nbsp;and&nbsp; **height** &nbsp;of the display in pixels. &nbsp;Be sure to use the right values for the display you're using!

## 128 x 64 size OLEDs (or changing the I2C address)

If you are using a 128x64 display, the I2C address&nbsp;is probably&nbsp;different (`0x3d`), unless you've changed it by soldering some jumpers:

```
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3d)
```

## Adding hardware reset pin

If you have a reset pin (which may be required if your OLED does not have an auto-reset chip like the FeatherWing) also pass in a reset pin like so:

```
import digitalio

reset_pin = digitalio.DigitalInOut(board.D4) # any pin!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
```

At this point the I2C bus and display are initialized. **Skip down to the example code section.**

# SPI Initialization

If your display is connected to the board using SPI you'll first need to initialize the SPI bus:

```
import adafruit_ssd1306
import board
import busio
import digitalio

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
reset_pin = digitalio.DigitalInOut(board.D4) # any pin!
cs_pin = digitalio.DigitalInOut(board.D5)    # any pin!
dc_pin = digitalio.DigitalInOut(board.D6)    # any pin!

oled = adafruit_ssd1306.SSD1306_SPI(128, 32, spi, dc_pin, reset_pin, cs_pin)
```

Note the first two parameters to the `SSD1306_SPI` class initializer are the&nbsp; **width** &nbsp;and&nbsp; **height** &nbsp;of the display in pixels. &nbsp;Be sure to use the right values for the display you're using!

The next parameters to the initializer are the pins connected to the display's&nbsp; **DC** ,&nbsp; **reset** , and&nbsp; **CS** &nbsp;lines in that order. &nbsp;Again make sure to use the right pin names as you have wired up to your board!

# Example Code
https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/blob/main/examples/ssd1306_pillow_demo.py

Let's take a look at the sections of code one by one.&nbsp;We start by importing the `board` so that we can initialize&nbsp;SPI,&nbsp;`digitalio`, several&nbsp;`PIL`&nbsp;modules for Image Drawing, and the&nbsp;`adafruit_ssd1306`&nbsp;driver.

```
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
```

Next we define the reset line, which will be used for either SPI or I2C. If your OLED has auto-reset circuitry, you can set the `oled_reset` line to **None**

```
oled_reset = digitalio.DigitalInOut(board.D4)
```

In order to make it easy to change display sizes, we'll define a few variables in one spot here. We have the display width, the display height and the border size, which we will explain a little further below. If your display is something different than these numbers, change them to the correct setting.

```
WIDTH = 128
HEIGHT = 32     # Change to 64 if needed
BORDER = 5
```

If you're using I2C, you would use this section of code.&nbsp;We set the I2C object to the board's I2C with the easy shortcut function&nbsp;`board.I2C()`. By using this function, it finds the I2C module and initializes using the default I2C parameters. We also set up the oled with SSD1306\_I2C which makes use of the I2C bus.

```
# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c, reset=oled_reset)
```

If you're using SPI, you would use this section of code. We set the SPI object to the board's SPI with the easy shortcut function&nbsp;`board.SPI()`. By using this function, it finds the SPI module and initializes using the default SPI parameters. We set the OLED's&nbsp; **CS** (Chip Select), and&nbsp; **DC** (Data/Command)&nbsp;pins.&nbsp;We also set up the OLED with SSD1306\_SPI which makes use of the SPI bus.

```
# Use for SPI
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D5)
oled_dc = digitalio.DigitalInOut(board.D6)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)
```

Next we clear the display in case it was initialized with any random artifact data.

```
# Clear display.
oled.fill(0)
oled.show()
```

Next, we need to initialize PIL to create a blank image to draw on. Think of it as a virtual canvas. Since this is a monochrome display, we set it up for 1-bit color, meaning a pixel is either white or black. We can make use of the OLED's width and height properties as well. Optionally, we could have used our **WIDTH** and **HEIGHT** variables.

```
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

```

Now we start the actual drawing. Here we are telling it we want to draw a rectangle from `(0,0)`, which is the upper left, to the full width and height of the display. We want it both filled in and having an outline of white, so we pass 255 for both numbers.

```
# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
```

If we ran the code now, it would still show a blank display because we haven't told python to use our virtual canvas yet. You can skip to the end if you would like to see how to do that.&nbsp;This is what our canvas currently looks like in memory.

![](https://cdn-learn.adafruit.com/assets/assets/000/081/416/medium800/adafruit_products_PIL_white_box.jpeg?1569432344)

Next we will create a smaller black rectangle. The easiest way to do this is to draw another rectangle a little smaller than the full screen with no fill or outline&nbsp;and place it in a specific location. In this case, we will create a rectangle that is 5 pixels smaller on each side. This is where the **BORDER** variable comes into use. It makes calculating the size of the second rectangle much easier. We want the starting coordinate, which consists of the first two parameters, to be our BORDER value. Then for the next two parameters, which are our ending coordinates, we want to subtract our border value from the width and height. Also, because this is a zero-based coordinate system, we also need to subtract 1 from each number.

```
# Draw a smaller inner rectangle
draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
               outline=0, fill=0)
```

Here's what our virtual canvas looks like in memory.

![](https://cdn-learn.adafruit.com/assets/assets/000/081/417/medium800/adafruit_products_PIL_black_box.jpeg?1569432353)

Now drawing text with PIL is pretty straightforward. First we start by setting the font to the default system text. After that we define our text and get the size of the text. We're grabbing the size that it would render at so that we can calculate the center position. Finally, we take the font size and screen size to calculate the position we want to draw the text at and it appears in the center of the screen.

```
# Load default font.
font = ImageFont.load_default()

# Draw Some Text
text = "Hello World!"
(font_width, font_height) = font.getsize(text)
draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2),
          text, font=font, fill=255)

```

Finally, we need to display our virtual canvas to the OLED and we do that with 2 commands. First we set the image to the screen, then we tell it to show the image.

```
# Display image
oled.image(image)
oled.show()
```

Warning: 

Here's what the final output should look like.

![](https://cdn-learn.adafruit.com/assets/assets/000/081/421/medium800/adafruit_products_PIL_hello_world.jpeg?1569433250)

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/python-setup.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/troubleshooting-2.md)

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
