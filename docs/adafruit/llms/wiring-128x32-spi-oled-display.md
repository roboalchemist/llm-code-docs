# Source: https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x32-spi-oled-display.md

# Monochrome OLED Breakouts

## Wiring 128x32 SPI OLED display

## 128x32 SPI OLED
The 128x32 SPI OLED is very easy to get up and running because it has built in level shifting. First up, take a piece of 0.1" header 8 pins long.  
  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/124/medium800/lcds___displays_spi12832pins.jpg?1396769016)

Plug the header long end down into a breadboard and place the OLED on top. Solder the short pins into the OLED PCB.![](https://cdn-learn.adafruit.com/assets/assets/000/001/125/medium800/lcds___displays_spi12832solder.jpg?1396769023)

Finally, connect the pins to your Arduino -&nbsp; **GND** &nbsp;goes to ground,&nbsp; **Vin** &nbsp;goes to 5V,&nbsp; **DATA** &nbsp;to digital&nbsp; **9** ,&nbsp; **CLK** &nbsp;to digital&nbsp; **10** ,&nbsp; **D/C** &nbsp;to digital&nbsp; **11** ,&nbsp; **RST** &nbsp;to digital&nbsp; **13** &nbsp;and finally&nbsp; **CS** &nbsp;to digital&nbsp; **12.**  
  
_( **Note** : If using the display with other SPI devices, D/C, CLK and DAT may be shared, but CS must be unique for each device.)_&nbsp;&nbsp;  
  
This matches the example code we have written. Once you get this working, you can try another set of pins.&nbsp;&nbsp;  
  
Finally you can run the&nbsp; **File→Sketchbook→Libraries→Adafruit\_SSD1306→SSD1306\_128x32\_SPI&nbsp;example**  
  
  
Info: 

- [Previous Page](https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x64-oleds.md)
- [Next Page](https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x32-i2c-display.md)

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
