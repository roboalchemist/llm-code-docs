# Source: https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x64-oleds.md

# Monochrome OLED Breakouts

## Wiring 128x64 OLEDs

## Solder Header
  
Before you start wiring, a strip of header must be soldered onto the OLED. It is not possible to "press-fit" the header, it must be attached!  
Start by placing an 8-pin piece of header with the&nbsp; **long** ends down into a breadboard for stability

![lcds___displays_headerplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/616/medium640/lcds___displays_headerplace.jpg?1396785089)

Place the OLED on top so all the short ends of the header stick thru the header pads

![lcds___displays_oledplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/617/medium640/lcds___displays_oledplace.jpg?1396785097)

Finish by soldering each of the 8 pins to the 8 pads!

![lcds___displays_solder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/618/medium640/lcds___displays_solder.jpg?1396785110)

# I2C or SPI

The nice thing about the 128x64 OLEDs is that they can be used with I2C (+ an optional reset line) or SPI. SPI is generally faster than I2C but uses more pins. It's also easier for some microcontrollers to use SPI. Anyways, you can use either one with this display

## Using with I2C

The display can be used with any I2C microcontroller. Because the I2C interface is for 'writing' to the display only, you'll still have to buffer the entire 512 byte frame in the microcontroller RAM - you can't read data from the OLED (even though I2C is a bidirectional protocol).

If you have the older non-STEMMA version of the OLED, you'll need to solder the two jumpers on the back of the OLED. **Both** must be soldered 'closed' for I2C to work!

![adafruit_products_lcds___displays_oledi2c.jpg](https://cdn-learn.adafruit.com/assets/assets/000/093/883/medium640/adafruit_products_lcds___displays_oledi2c.jpg?1596745237)

For the new STEMMA-capable version, the **J1** and **J2** jumpers are closed so that the display is **by default in I2C mode!**

**There's a typo on the board, to put it into SPI, _open_ the two jumpers (as they're closed by default)**

![adafruit_products_newoled.jpg](https://cdn-learn.adafruit.com/assets/assets/000/086/658/medium640/adafruit_products_newoled.jpg?1578330932)

## Converting From I2C to SPI Mode

The original version of this display was SPI by default, and you could convert to I2C with some light soldering. Many folks using these displays did not know how to solder, didn't own an iron or were not comfortable with soldering, so we converted the board to STEMMA QT 'plug and play' I2C so no soldering is required to use in I2C mode.

To convert it back to SPI is very easy, and requires a thin screwdriver or other sharp-tipped item **be careful not to cut towards you as always so you do not accidentally cut yourself!**

https://youtu.be/SXfV4e_jpf8

## Wiring It Up!
Info: 

Warning: 

Finally, connect the pins to your Arduino

- **GND** goes to ground **(black wire on STEMMA QT version)**
- **Vin** goes to 5V **(red wire on STEMMA QT version)**
- **Data** to I2C SDA (on the Uno, this is **A4** on the Mega it is **20** and on the Leonardo digital **2** ) **(blue wire on STEMMA QT version)**
- **Clk** to I2C SCL (on the Uno, this is **A5** on the Mega it is **21** and on the Leonardo digital **3** ) **(yellow wire on STEMMA QT version)**
- **RST** to digital **4** (you can change this pin in the code, later) (Not necessary on 0.96" STEMMA QT version)

This matches the example code we have written. Once you get this working, you can try a different Reset pin (you can't change the SDA and SCL pins).  
  
Finally you can run the **File→Sketchbook→Libraries→Adafruit\_SSD1306→SSD1306\_128x64\_i2c** example. If you wired the RST pin to a GPIO pin, change `#define OLED_RESET     -1`&nbsp; to the new pin number.

https://github.com/adafruit/Adafruit_SSD1306/blob/master/examples/ssd1306_128x64_i2c/ssd1306_128x64_i2c.ino

## Using with SPI
The breakouts are ready for SPI by default, but if you used them for I2C at some point, you'll need to remove the solder jumpers. Use wick or a solder sucker to make sure both are clear!  
If you have the older non-STEMMA version of the OLED, the breakouts are ready for SPI by default.

If you used them for I2C at some point, you'll need to remove the solder jumpers. Use wick or a solder sucker to make sure both are clear!

![lcds___displays_spijumpers.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/619/medium640/lcds___displays_spijumpers.jpg?1396785123)

If you have the newer STEMMA QT version **cut** the two jumpers instead!

![adafruit_products_938_bottom_demo_detail_orig_2020_01_720.jpg](https://cdn-learn.adafruit.com/assets/assets/000/086/687/medium640/adafruit_products_938_bottom_demo_detail_orig_2020_01_720.jpg?1578366507)

Finally, connect the pins to your Arduino -

- **GND** goes to ground
- **Vin** goes to 5V
- **DATA** to digital **9**
- **CLK** to digital **10**
- **D/C** to digital **11**
- **RST** to digital **13**
- **CS** to digital **12**

_( **Note** : If using the display with other SPI devices, D/C, CLK and DAT may be shared, but CS must be unique for each device.)_   
  
This matches the example code we have written. Once you get this working, you can try another set of pins.   
  
Finally you can run the **File→Sketchbook→Libraries→Adafruit\_SSD1306→SSD1306\_128x64\_spi** example

https://github.com/adafruit/Adafruit_SSD1306/blob/master/examples/ssd1306_128x64_spi/ssd1306_128x64_spi.ino

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/arduino-library-and-examples.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x32-spi-oled-display.md)

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

- [OLED TRON Clock](https://learn.adafruit.com/oled-tron-clock.md)
- [I2C Addresses and Troublesome Chips](https://learn.adafruit.com/i2c-addresses.md)
- [Monitor Your Greenhouse with a No-Code Environmental Sensor](https://learn.adafruit.com/monitor-your-greenhouse-with-a-no-code-environmental-sensor.md)
- [SSD1306 OLED Displays with Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black.md)
- [Adafruit FT232H With SPI & I2C Devices](https://learn.adafruit.com/adafruit-ft232h-with-spi-and-i2c-libraries.md)
- [MIDI Melody Maker](https://learn.adafruit.com/midi-melody-maker.md)
- [Steampunk Cameo Necklace with OLED Display](https://learn.adafruit.com/steampunk-cameo-necklace.md)
- [Using QMK on RP2040 Microcontrollers](https://learn.adafruit.com/using-qmk-on-rp2040-microcontrollers.md)
- [CircuitPython OLED and Dual Knob Sketcher](https://learn.adafruit.com/circuitpython-oled-knob-sketcher.md)
- [Gravity Falls Memory Gun](https://learn.adafruit.com/gravity-falls-memory-gun.md)
- [Pico W HTTP Server with CircuitPython](https://learn.adafruit.com/pico-w-http-server-with-circuitpython.md)
- [Adafruit Trinkey QT2040](https://learn.adafruit.com/adafruit-trinkey-qt2040.md)
- [Adafruit Airlift Bitsy Add-On - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-bitsy-add-on-esp32-wifi-co-processor.md)
- [Animated Flying Toaster OLED Jewelry](https://learn.adafruit.com/animated-flying-toaster-oled-jewelry.md)
- [Adafruit TCA9548A 1-to-8 I2C Multiplexer Breakout](https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout.md)
