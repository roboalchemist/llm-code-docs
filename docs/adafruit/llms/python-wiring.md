# Source: https://learn.adafruit.com/monochrome-oled-breakouts/python-wiring.md

# Monochrome OLED Breakouts

## Python Wiring

It's easy to use OLEDs with Python and the [Adafruit CircuitPython SSD1306](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306) module.&nbsp; This module allows you to easily write Python code to control the display.

We'll cover how to wire the OLED to your Raspberry Pi. First assemble your OLED.

Since there's _dozens_ of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).&nbsp;

Connect the OLED as shown below to your Raspberry Pi.

## Adafruit PIOLED
- **The PiOLED comes fully assembled. Simply plug into any Raspberry Pi as shown.**

![adafruit_products_raspi_pi_oled_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/735/medium640/adafruit_products_raspi_pi_oled_bb.jpg?1546730389)

## Adafruit 128x64 OLED Bonnet for Raspberry Pi
- **The OLED Bonnet comes fully assembled. Simply plug into the Raspberry Pi as shown.**

![adafruit_products_raspi0_oled_bonnet_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/736/medium640/adafruit_products_raspi0_oled_bonnet_bb.jpg?1546730556)

## Adafruit 128x32 I2C OLED Display
- **Pi 3.3V** to **OLED VIN**
- **Pi GND** to **OLED GND**
- **Pi SCL** to **OLED SCL**
- **Pi SDA** to **OLED SDA**
- **Pi GPIO4** to **OLED RST** (or any available GPIO pin)

![adafruit_products_raspi_128_32_i2c_oled_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/728/medium640/adafruit_products_raspi_128_32_i2c_oled_bb.jpg?1546722187)

## Adafruit 0.96" 128x64 OLED Display STEMMA QT Version - I2C Wiring
 **You do not need to alter the jumpers on the back - I2C is the default configuration on this display!**

- **Pi 3.3V** to **OLED Vin (red wire)**  
- **Pi GND** to **OLED Gnd (black wire)**  
- **Pi SCL** to **OLED Clk (yellow wire)**  
- **Pi SDA** to **OLED Data (blue wire)**  

Note: Connecting the OLED RST is not necessary as this revision added auto-reset circuitry so the RESET pin is not required.

![adafruit_products_128x64_STEMMA_Wiring_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/131/334/medium640/adafruit_products_128x64_STEMMA_Wiring_bb.png?1721258587)

## Adafruit 0.96" or 1.3" 128x64 OLED Display Original Version - I2C Wiring
 **You must solder two jumpers closed on the back of the display to use with I2C!**

&nbsp;

- **Pi 3.3V** to **OLED Vin**
- **Pi GND** to **OLED Gnd**
- **Pi SCL** to **OLED Clk**  
- **Pi SDA** to **OLED Data**  
- **Pi GPIO4** to **OLED Rst** (or any available GPIO pin)

![adafruit_products_raspi_128_64_i2c_oled_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/744/medium640/adafruit_products_raspi_128_64_i2c_oled_bb.jpg?1546733722)

![adafruit_products_OLED_jumper_I2C.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/745/medium640/adafruit_products_OLED_jumper_I2C.jpg?1546733818)

![adafruit_products_raspi_1_3_inch_128_64_i2c_oled_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/752/medium640/adafruit_products_raspi_1_3_inch_128_64_i2c_oled_bb.jpg?1546737342)

![adafruit_products_1-3inch_128x64_oled_back.jpg](https://cdn-learn.adafruit.com/assets/assets/000/068/753/medium640/adafruit_products_1-3inch_128x64_oled_back.jpg?1546737364)

## Adafruit 128x32 SPI OLED Display
- **Pi 3.3V** to **OLED VIN**
- **Pi GND** to **OLED GND**
- **Pi MOSI&nbsp;** to **OLED DATA**
- **Pi SCLK&nbsp;** to **OLED CLK**
- **Pi GPIO4** to **OLED RST** (or any available GPIO pin)
- **Pi GPIO5&nbsp;** to **OLED CS&nbsp;** (or any available GPIO pin)
- **Pi GPIO6** to **OLED DC&nbsp;** (or any available GPIO pin)

![adafruit_products_rpi_spi_128x32_oled.png](https://cdn-learn.adafruit.com/assets/assets/000/081/400/medium640/adafruit_products_rpi_spi_128x32_oled.png?1569376747)

## Adafruit 0.96" or 1.3" 128x64 OLED Display - SPI Wiring
- **Pi 3.3V** to **OLED VIN**
- **Pi GND** to **OLED GND**
- **Pi MOSI&nbsp;** to **OLED DATA**
- **Pi SCLK&nbsp;** to **OLED CLK**
- **Pi GPIO4** to **OLED RST** (or any available GPIO pin)
- **Pi GPIO5&nbsp;** to **OLED CS&nbsp;** (or any available GPIO pin)
- **Pi GPIO6** to **OLED DC&nbsp;** (or any available GPIO pin)

![adafruit_products_rpi_spi_128x64_oled.png](https://cdn-learn.adafruit.com/assets/assets/000/081/401/medium640/adafruit_products_rpi_spi_128x64_oled.png?1569376764)

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-usage.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/python-setup.md)

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
