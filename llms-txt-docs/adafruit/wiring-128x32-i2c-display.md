# Source: https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x32-i2c-display.md

# Monochrome OLED Breakouts

## Wiring 128x32 I2C Display

## 128x32 I2C OLED
The 128x32 I2C OLED is very easy to get up and running because it has built in level shifting and regulator. First up, take a piece of 0.1" header 6 pins long.  
Plug the header long end down into a breadboard![lcds___displays_header.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/157/medium640/lcds___displays_header.jpg?1396769302)

Place the OLED on top

![lcds___displays_place.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/158/medium640/lcds___displays_place.jpg?1396769313)

Solder the short pins into the OLED PCB.![lcds___displays_soldered.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/159/medium640/lcds___displays_soldered.jpg?1396769320)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/160/medium800/lcds___displays_wiring.jpg?1396769328)

Finally, connect the pins to your Arduino

- **GND** &nbsp;goes to ground
- **Vin** &nbsp;goes to 5V
- **SDA** to I2C Data **SDA** pin (on the Uno, this is **A4** on the Mega it is&nbsp; **20&nbsp;** and on the Leonardo digital&nbsp; **2** )
- **SCL** &nbsp; to I2C Clock **SCL** pin (on the Uno, this is **A5** on the Mega it is&nbsp; **21&nbsp;** and on the Leonardo digital&nbsp; **3** )
- **RST** &nbsp;to digital&nbsp; **4** &nbsp; (you can change this pin in the code, later)

This matches the example code we have written. Once you get this working, you can change the RST pin. You cannot change the I2C pins, those are 'fixed' in hardware  
  
Finally you can run the&nbsp; **File→Sketchbook→Libraries→Adafruit\_SSD1306→SSD1306\_128x32\_i2c&nbsp;** example. If you wired the RST pin to a GPIO pin, change `#define OLED_RESET     -1`&nbsp; to the new pin number.

https://github.com/adafruit/Adafruit_SSD1306/blob/master/examples/ssd1306_128x32_i2c/ssd1306_128x32_i2c.ino

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x32-spi-oled-display.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/wiring-096-128x64-oled-display.md)

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
