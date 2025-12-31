# Source: https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-wiring.md

# Monochrome OLED Breakouts

## CircuitPython Wiring

It's easy to use OLEDs with CircuitPython and the [Adafruit CircuitPython DisplayIO SSD1306](https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306) module.&nbsp; This module allows you to easily write CircuitPython code to control the display.

You can use this sensor with any CircuitPython microcontroller board.

We'll cover how to wire the OLED to your CircuitPython microcontroller board. First assemble your OLED.

Connect the OLED to your microcontroller board as shown below.

## Adafruit OLED FeatherWing
- **Solder the Feather with female headers on top or stacking headers.**
- **Attach the OLED FeatherWing using the stacking method.**

![adafruit_products_FeatherM4_OLED_FeatherWing_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/585/medium640/adafruit_products_FeatherM4_OLED_FeatherWing_bb.jpg?1546450633)

## Adafruit 128x32 I2C OLED Display
- **Microcontroller 3V** to **OLED VIN**
- **Microcontroller GND** to **OLED GND**
- **Microcontroller SCL** to **OLED SCL**
- **Microcontroller SDA** to **OLED SDA**
- **Microcontroller D9** to **OLED RST**

![adafruit_products_FeatherM4_128_32_I2C_OLED_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/726/medium640/adafruit_products_FeatherM4_128_32_I2C_OLED_bb.jpg?1546721739)

## Adafruit 128x32 SPI OLED Display
- **Microcontroller 3V** to **OLED VIN**
- **Microcontroller GND** to **OLED GND**
- **Microcontroller SCK** to **OLED CLK**
- **Microcontroller MOSI** to **OLED Data**
- **Microcontroller D5** to **OLED CS**
- **Microcontroller D6** to **OLED D/C**
- **Microcontroller D9** to **OLED RST**

![adafruit_products_FeatherM4_128_32_SPI_OLED_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/727/medium640/adafruit_products_FeatherM4_128_32_SPI_OLED_bb.jpg?1546721926)

## Adafruit 0.96" 128x64 OLED Display STEMMA QT Version - I2C Wiring
 **You do not need to alter the jumpers on the back - I2C is the default configuration on this display!**

- **Microcontroller 3V** to **OLED Vin**  
- **Microcontroller GND** to **OLED Gnd**
- **Microcontroller SCL** to **OLED Clk**  
- **Microcontroller SDA** to **OLED Data**

Note: Connecting the OLED RST is not necessary as this revision added auto-reset circuitry so the RESET pin is not required.

![adafruit_products_0-96in_OLED_FeatherM4_STEMMA_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/093/882/medium640/adafruit_products_0-96in_OLED_FeatherM4_STEMMA_bb.jpg?1596745061)

## Adafruit 0.96" or 1.3" 128x64 OLED Display Original Version - I2C Wiring
Warning: 

- **Microcontroller 3V** to **OLED Vin**  
- **Microcontroller GND** to **OLED Gnd**
- **Microcontroller SCL** to **OLED Clk**  
- **Microcontroller SDA** to **OLED Data**  
- **Microcontroller D9** to **OLED Rst**

![adafruit_products_FeatherM4_128_64_I2C_OLED_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/737/medium640/adafruit_products_FeatherM4_128_64_I2C_OLED_bb.jpg?1546732943)

![adafruit_products_OLED_jumper_I2C.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/738/medium640/adafruit_products_OLED_jumper_I2C.jpg?1546732949)

![adafruit_products_FeatherM4_1_3_inch_128_64_I2C_OLED_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/755/medium640/adafruit_products_FeatherM4_1_3_inch_128_64_I2C_OLED_bb.jpg?1546737543)

![adafruit_products_1-3inch_128x64_oled_back.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/756/medium640/adafruit_products_1-3inch_128x64_oled_back.jpg?1546737562)

## Adafruit 0.96" or 1.3"&nbsp; 128x64 OLED Display - SPI Wiring
Warning: 

- **Microcontroller 3V** to **OLED Vin**
- **Microcontroller GND** to **OLED Gnd**  
- **Microcontroller SCK** to **OLED Clk**
- **Microcontroller MOSI** to **OLED Data**
- **Microcontroller D5** to **OLED CS**
- **Microcontroller D6** to **OLED DC**
- **Microcontroller D9** to **OLED Rst**

![adafruit_products_FeatherM4_128_64_SPI_OLED_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/740/medium640/adafruit_products_FeatherM4_128_64_SPI_OLED_bb.jpg?1546733303)

![adafruit_products_FeatherM4_1_3_inch_128_64_SPI_OLED_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/754/medium640/adafruit_products_FeatherM4_1_3_inch_128_64_SPI_OLED_bb.jpg?1546737464)

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/wiring-096-128x64-oled-display.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-setup.md)

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
