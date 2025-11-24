# Source: https://learn.adafruit.com/monochrome-oled-breakouts/troubleshooting-2.md

# Monochrome OLED Breakouts

## Troubleshooting

### 

The OLED driver circuit needs a small amount of time to be ready after initial power. If your code tries to write to the display too soon, it may not be ready. It will work on reset since that typically does not cycle power. If you are having this issue, try adding a small amount of delay before trying to write to the OLED.

In Arduino, use **delay()** to add a few milliseconds before calling **oled.begin()**. Adjust the amount of delay as needed to see how little you can get away with for your specific setup.

### 

The display can have image burn in for any pixels left on over a long period of time - many days. Try to avoid having the display on constantly for that length of time.

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/python-usage-2.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/downloads.md)

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
