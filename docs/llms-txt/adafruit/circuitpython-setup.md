# Source: https://learn.adafruit.com/12mm-led-pixels/circuitpython-setup.md

# Source: https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-setup.md

# Monochrome OLED Breakouts

## CircuitPython Setup

# CircuitPython Installation of DisplayIO SSD1306 Library
Warning: 

To use the SSD1306 OLED with your&nbsp;Adafruit CircuitPython&nbsp;board you'll need to install the&nbsp;[Adafruit CircuitPython DisplayIO SSD1306](https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306)&nbsp;module on your board.

First make sure you are running the&nbsp;[latest version 5.0 or later of Adafruit CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)&nbsp;for your board.

Warning: 

Next you'll need to install the necessary libraries&nbsp;to use the hardware--carefully follow the steps to find and install these libraries from&nbsp;[Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases).&nbsp; Our CircuitPython starter guide has [a great page on how to install the library bundle](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries).

If you choose, you can manually install the libraries individually on your board:

- **adafruit\_displayio\_ssd1306**
- **adafruit\_bus\_device**

Before continuing make sure your board's lib folder or root filesystem has the **adafruit\_displayio\_ssd1306****.mpy and&nbsp; ****adafruit\_bus\_device**** &nbsp; **files and folders** &nbsp;**copied over.

Next[&nbsp;connect to the board's serial REPL](https://learn.adafruit.com/welcome-to-circuitpython/the-repl) so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

## Code Example Additional Libraries

For the Code Example, you will need an additional library. We decided to make use of a library so the code didn't get overly complicated.

[Adafruit_CircuitPython_Display_Text](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text/releases)
Go ahead and install this in the same manner as the driver library by copying the&nbsp; **adafruit\_display\_text** folder over to the **lib** folder on your CircuitPython device.

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-wiring.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-usage.md)

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
