# Source: https://learn.adafruit.com/i2c-spi-lcd-backpack/arduino-spi-use.md

# I2C/SPI LCD Backpack

## Arduino SPI Use

Another option for connecting is to use **SPI** , which is a simpler protocol. The good news about SPI is that its very simple and you can use **any** 3 pins to connect. You can share the **data** and **clock** pins with another device as long as they remain outputs, the **latch** pin should only be used for the backpack. So if you wanted 3 LCDs, for example, they would all have the same **data** and **clock** pins, but the **latch** pin would be different, for 5 pins total

Danger: 

The first thing you will need to do is to enable SPI. To do this, solder the **SPI Enable** solder jumper by heating up the pads with a soldering iron and soldering a blob onto both pins:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/894/medium800/lcds___displays_spiump.jpeg?1396777205)

This will switch the backpack over to SPI mode instead of I2C. If you want to go back to I2C, use wick or a solder sucker to remove the jumper

Next we will connect 5 wires,&nbsp; **5V** ,&nbsp; **GND** ,&nbsp; **DAT** ,&nbsp; **CLK** , and&nbsp; **LAT**.

- To match the example,&nbsp; **CLK** &nbsp;goes to to Digital 2
- **DAT** &nbsp;to Digital 3,
- **LAT** &nbsp;to Digital 4

Once we have the example sketch running you can of course change these to anything you'd like

- Connect&nbsp; **5V** &nbsp;and&nbsp; **GND** &nbsp;to the 5v and Ground Arduino power pins. If you are using a 3.3V Arduino, you still need to power the LCD with 5V power! You can use 3.3V logic just fine

![](https://cdn-learn.adafruit.com/assets/assets/000/001/895/medium800/lcds___displays_spiwire_t.jpeg?1396777212)

## Install Adafruit\_LiquidCrystal

To begin reading sensor data, you will need to [use the Adafruit\_LiquidCrystal library.](https://github.com/adafruit/LiquidCrystal). You can install the&nbsp; **Adafruit\_LiquidCrystal**** &nbsp;**library for Arduino using the Library Manager in the Arduino IDE.

![](https://cdn-learn.adafruit.com/assets/assets/000/118/756/medium800/adafruit_products_Arduino_Open_Library_Manager.png?1677185017)

Click the&nbsp; **Manage Libraries ...** &nbsp;menu item, search for&nbsp; **Adafruit LiquidCrystal** and select the **Adafruit LiquidCrystal** &nbsp;library:

![](https://cdn-learn.adafruit.com/assets/assets/000/118/757/medium800/adafruit_products_lcdLib.png?1677185134)

If asked about any dependencies, click "Install All".

![](https://cdn-learn.adafruit.com/assets/assets/000/118/758/medium800/adafruit_products_depends.png?1677185250)

## Load Demo

Restart the IDE and load up the **Adafruit\_LiquidCrystal-\>HelloWorld\_SPI** demo

![](https://cdn-learn.adafruit.com/assets/assets/000/029/935/medium800/lcds___displays_demospi.png?1453416523)

Upload the sketch. You should see the backlight turn on when the Arduino resets. If you don't see any characters, adjust the **Contrast** trim potentiometer with a mini-screwdriver until you see the text clearly

The default HelloWorld sketch blinks the backlight as well as updating the text.

**If you see the backlight blinking that means your connection to the SPI port is OK but the contrast is too low or too high** , or the LCD data pins are not solidly connected.

Check the contrast first by gently twisting the mini trim potentiometer, if that doesn't help, recheck your soldering and resolder all 16 of the LCD pins!

![](https://cdn-learn.adafruit.com/assets/assets/000/001/896/medium800/lcds___displays_spiconnect_t.jpeg?1396777218)

Once you're done, you can remove the blinking LED backlight code:

> lcd.setBacklight(HIGH);  
> delay(500);  
> lcd.setBacklight(LOW);  
> delay(500);

- [Previous Page](https://learn.adafruit.com/i2c-spi-lcd-backpack/arduino-i2c-use.md)
- [Next Page](https://learn.adafruit.com/i2c-spi-lcd-backpack/python-circuitpython.md)

## Primary Products

### i2c / SPI character LCD backpack - STEMMA QT / Qwiic

[i2c / SPI character LCD backpack - STEMMA QT / Qwiic](https://www.adafruit.com/product/292)
Character LCDs are a fun and easy way to have your microcontroller project talk back to you. They are also common, and easy to get, available in tons of colors and sizes. [We've written tutorials on using character LCDs with an Arduino](http://learn.adafruit.com/character-lcds)...

In Stock
[Buy Now](https://www.adafruit.com/product/292)
[Related Guides to the Product](https://learn.adafruit.com/products/292/guides)

## Featured Products

### Standard LCD 20x4 + extras

[Standard LCD 20x4 + extras](https://www.adafruit.com/product/198)
Standard HD44780 LCDs are useful for creating standalone projects.

- 20 characters wide, 4 rows
- White text on blue background
- Connection port is 0.1" pitch, single row for easy breadboarding and wiring
- Single LED backlight with a resistor included, you can...

In Stock
[Buy Now](https://www.adafruit.com/product/198)
[Related Guides to the Product](https://learn.adafruit.com/products/198/guides)
### Standard LCD 16x2 + extras

[Standard LCD 16x2 + extras](https://www.adafruit.com/product/181)
Standard HD44780 LCDs are useful for creating standalone projects.

- 16 characters wide, 2 rows
- White text on blue background
- Connection port is 0.1" pitch, single row for easy breadboarding and wiring
- Pins are documented on the back of the LCD to assist...

In Stock
[Buy Now](https://www.adafruit.com/product/181)
[Related Guides to the Product](https://learn.adafruit.com/products/181/guides)

## Related Guides

- [ Faz-Wrench - Five Nights at Freddy's](https://learn.adafruit.com/faz-wrench.md)
- [Trinket Ultrasonic Rangefinder](https://learn.adafruit.com/trinket-ultrasonic-rangefinder.md)
- [No-Code Indoor Air Quality Monitor with Separate Display](https://learn.adafruit.com/no-code-indoor-air-quality-monitor-with-separate-display.md)
- [Trinket Temperature & Humidity LCD Display](https://learn.adafruit.com/trinket-temperature-humidity-lcd-display.md)
- [Light Meter](https://learn.adafruit.com/light-meter.md)
- [CircuitPython Hardware: ILI9341 TFT & FeatherWing](https://learn.adafruit.com/micropython-hardware-ili9341-tft-and-featherwing.md)
- [Raspberry Pi Thermal Camera](https://learn.adafruit.com/raspberry-pi-thermal-camera.md)
- [Adafruit NeoKey BFF](https://learn.adafruit.com/adafruit-neokey-bff.md)
- [Mini LED Matrix Audio Visualizer](https://learn.adafruit.com/mini-led-matrix-audio-visualizer.md)
- [Adafruit ISO1540 Bidirectional I2C Isolator](https://learn.adafruit.com/adafruit-iso1540-bidirectional-i2c-isolator.md)
- [Raspberry Pi Low-Light Long-Exposure Photography](https://learn.adafruit.com/raspberry-pi-hq-camera-low-light-long-exposure-photography.md)
- [Adafruit Radio Bonnets with OLED Display - RFM69 or RFM9X](https://learn.adafruit.com/adafruit-radio-bonnets.md)
- [PicoDVI Arduino Library: Video Out for RP2040 Boards](https://learn.adafruit.com/picodvi-arduino-library-video-out-for-rp2040-boards.md)
- [reef-pi Guide 5: Light Controller](https://learn.adafruit.com/reef-pi-lighting-controller.md)
- [Adafruit VL53L4CD Time of Flight Distance Sensor](https://learn.adafruit.com/adafruit-vl53l4cd-time-of-flight-distance-sensor.md)
