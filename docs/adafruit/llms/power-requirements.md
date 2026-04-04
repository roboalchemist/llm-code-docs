# Source: https://learn.adafruit.com/adafruit-motor-shield/power-requirements.md

# Source: https://learn.adafruit.com/monochrome-oled-breakouts/power-requirements.md

# Monochrome OLED Breakouts

## Power Requirements

## OLED Power Requirements
The OLED and driver require a 3.3V power supply and 3.3V logic levels for communication. The power requirements depend a little on how much of the display is lit but on average the display uses about 20mA from the 3.3V supply. Built into the OLED driver is a simple switch-cap charge pump that turns 3.3v-5v into a high voltage drive for the OLEDs. You can run the entire display off of one 3.3V supply or use 3.3V for the chip power and up to 4.5V for the OLED charge pump or 3.3V for the chip power and a 7-9V supply directly into the OLED high voltage pin.## 5V- ready 128x64 and 128x32 OLEDs  

Unless you have the older v1 128x64 OLED, you can rest assured that your OLED is 5V ready. All 1.3" 128x64 and the small 128x32 SPI and I2C are 5V ready, if you have a v2 0.96" 128x64 OLED with the 5V ready mark on the front, it's also 5V safe. If you have an older 0.96" OLED (see below) you'll need to take extra care when wiring it to a 5V micontroller. The OLED is designed to be 5V compatible so you can power it with 3-5V and the onboard regulator will take care of the rest.  
  
All OLEDs are safe to use with 3.3V logic and power.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/301/medium800/lcds___displays_spi12832solder.jpg?1396770813)

Simply connect&nbsp; **GND** &nbsp;to ground, and&nbsp; **Vin** &nbsp;to a 3 to 5V power supply. There will be a 3.3V output on the&nbsp; **3Vo** &nbsp;pin in case you want a regulated 3.3V supply for something else.

## 0.96" 128x64 OLED
The older 0.96" 128x64 OLED is a little more complex to get running as it is not 5V compatible by default, so you have to provide it with 3.3V power.![](https://cdn-learn.adafruit.com/assets/assets/000/001/302/medium800/lcds___displays_oledback.jpg?1396770824)

- **VDD** &nbsp;is the 3.3V logic power. This must be 3 or 3.3V
- **VBAT** &nbsp;is the input to the charge pump. If you use the charge pump, this must be 3.3V to 4.2V
- **VCC&nbsp;** is the high voltage OLED pin. If you're using the internal charge pump, this must be left unconnected. If you're not using the charge pump, connect this to a 7-9V DC power supply.

For most users, we suggest connecting&nbsp; **VDD** &nbsp;and **&nbsp;VBAT** &nbsp;together to 3.3V and then leaving&nbsp; **VCC** &nbsp;unconnected.

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/overview.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/arduino-library-and-examples.md)

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
