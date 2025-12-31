# Source: https://learn.adafruit.com/monochrome-oled-breakouts/arduino-library-and-examples.md

# Monochrome OLED Breakouts

## Arduino Library & Examples

For all of the different kinds of small OLED monochrome displays, you'll need to install the Arduino libraries. The code we have is for any kind of Arduino, if you're using a different microcontroller, the code is pretty simple to adapt, the interface we use is basic bit-twiddling SPI or I2C

# Install Arduino Libraries

Using these OLEDs with Arduino sketches requires that two libraries be installed: **Adafruit\_SSD1306** , which handles the low-level communication with the hardware, and **Adafruit\_GFX** , which builds atop this to add graphics functions like lines, circles and text.

In recent versions of the Arduino IDE software (1.6.2 and later), this is most easily done through the Arduino Library Manager.

Open up the Arduino library manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/084/024/medium800/adafruit_products_library_manager_menu.png?1573518575)

Search for the&nbsp; **Adafruit SSD1306** &nbsp;library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/023/medium800/adafruit_products_ssd1306.png?1573518516)

Search for the&nbsp; **Adafruit GFX** &nbsp;library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/025/medium800/adafruit_products_gfx.png?1573518658)

If using an earlier version of the Arduino IDE (prior to 1.8.10), also locate and install **Adafruit\_BusIO** (newer versions will install this dependency automatically).

We also have a great tutorial on Arduino library installation here:  
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")

# Run Demo!

After installing the **Adafruit\_SSD1306** and **Adafruit\_GFX** library, restart the Arduino IDE. You should now be able to access the sample code by navigating through menus in this order: **File→Examples→**** Adafruit\_SSD1306→SSD1306...**

![](https://cdn-learn.adafruit.com/assets/assets/000/031/974/medium800/lcds___displays_Screenshot_1.png?1461689893)

After you've finished wiring the display as indicated on the following pages, load the example sketch to demonstrate the capabilities of the library and display.

[The OLED SSD1306 driver is based on the Adafruit GFX library which provides all the underlying graphics functions such as drawing pixels, lines, circles, etc. For more details about what you can do with the OLED check out the GFX library tutorial](http://learn.adafruit.com/adafruit-gfx-graphics-library "Link: http://learn.adafruit.com/adafruit-gfx-graphics-library")

![](https://cdn-learn.adafruit.com/assets/assets/000/000/705/medium800/lcds___displays_oled12864logo_LRG.jpg?1396765152)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/706/medium800/lcds___displays_oled12864chars_LRG.jpg?1396765158)

## Create Bitmaps with LCD Assistant

You can create bitmaps to display easily with the [LCD assistant software](http://en.radzio.dxp.pl/bitmap_converter/). First make your image using any kind of graphics software such as photoshop or Paint and save as a **Monochrome Bitmap (bmp)**

![](https://cdn-learn.adafruit.com/assets/assets/000/000/707/medium800/lcds___displays_bitmapmono.gif?1447976331)

Select the following options (You might also want to try **Horizontal** if **Vertical** is not coming out right)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/708/medium800/lcds___displays_bitmapconvert.gif?1447976341)

and import your monochrome bitmap image. Save the output to a&nbsp; **cpp** &nbsp;file![](https://cdn-learn.adafruit.com/assets/assets/000/000/709/medium800/lcds___displays_bitmapsave.gif?1447976348)

You can use the output directly with our example code![](https://cdn-learn.adafruit.com/assets/assets/000/000/710/medium800/lcds___displays_bitmapout.gif?1447976355)

## Create Bitmaps with image2cpp

image2cpp was created by GitHub user javl and provides a handy way to create bitmaps without installing any additional software. Just visit [https://javl.github.io/image2cpp/,](https://javl.github.io/image2cpp/) upload an image, put in any settings that you would like to use, select a format and generate the code. You can copy the code right into your sketch. If you're interested, you can view the source in their [GitHub repository](https://github.com/javl/image2cpp).

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/power-requirements.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x64-oleds.md)

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
