# Source: https://learn.adafruit.com/monochrome-oled-breakouts/wiring-096-128x64-oled-display.md

# Monochrome OLED Breakouts

## Wiring OLD 0.96" 128x64 OLED

Info: 

## 128x64 Version 1.0 OLED
The version 1 128x64 OLED runs at 3.3V and does not have a built in level shifter so you'll need to use a level shifting chip to use with a 5V microcontroller. The following will assume that is the case. If you're running a 3.3V microcontroller system, you can skip the level shifter.We'll assume you want to use this in a breadboard, take a piece of 0.1" header 10 pins long.

![lcds___displays_headercut.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/692/medium640/lcds___displays_headercut.jpg?1396765068)

Place the header in a breadboard and then place the left hand side of the OLED on top.![lcds___displays_oledheader.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/694/medium640/lcds___displays_oledheader.jpg?1396765083)

And solder the pins

![lcds___displays_oledsoldered.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/697/medium640/lcds___displays_oledsoldered.jpg?1396765103)

We'll be using the internal charge pump so connect&nbsp; **VDD** &nbsp;and&nbsp; **VBAT&nbsp;** together (they will connect to 3.3V) **.&nbsp;** GND goes to ground.![lcds___displays_oledpower.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/700/medium640/lcds___displays_oledpower.jpg?1396765097)

Place a CD4050 level shifter chip so pin one is at the top.![lcds___displays_chipplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/701/medium640/lcds___displays_chipplace.jpg?1396765119)

Connect pin 10 to&nbsp; **D/C** &nbsp;pin 12 to **&nbsp;CLK&nbsp;** (SPI clock) and pin 15 to&nbsp; **DAT&nbsp;** (SPI data).![lcds___displays_chipwire1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/702/medium640/lcds___displays_chipwire1.jpg?1396765126)

Connect pin 2 to&nbsp; **RES** &nbsp;(reset) and pin 4 to&nbsp; **CS** &nbsp;(chip select). Pin 1 goes to 3.3V and pin 8 to ground.  
  
_( **Note** : If using the display with other SPI devices, D/C, CLK and DAT may be shared, but CS must be unique for each device.)_

![lcds___displays_chipwire2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/703/medium640/lcds___displays_chipwire2.jpg?1396765134)

You can connect the inputs of the level shifter to any pins you want but in this case we connected digital I/O&nbsp; **13** &nbsp;to pin 3 of the level shifter,&nbsp; **12** &nbsp;to pin 5,&nbsp; **11&nbsp;** to pin 9,&nbsp; **10** &nbsp;to pin 11 and&nbsp; **9&nbsp;** to pin 14. This matches the example code we have written. Once you get this working, you can try another set of pins.![lcds___displays_wired.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/704/medium640/lcds___displays_wired.jpg?1396765142)

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x32-i2c-display.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-wiring.md)

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
