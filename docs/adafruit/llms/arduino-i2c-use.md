# Source: https://learn.adafruit.com/i2c-spi-lcd-backpack/arduino-i2c-use.md

# I2C/SPI LCD Backpack

## Arduino I2C Use

The first option we'll show is how to use the I2C interface on the backpack. We'll be showing how to connect with an Arduino, for other microcontrollers please see our MCP23008 library code for the commands to send to the I2C I/O expander. I2C is nice because it only uses two pins, and you can put multiple I2C devices on the same two pins.

So for example, you could have up to 8 LCD backpacks+LCDs all on two pins! The bad news is that you have to use the 'hardware' I2C pins. You can't change those pins and you can't use them for reading analog data. If you absolutely need those two pins, use SPI (see the next section).

For this, we'll need to connect four wires: GND, 5V, CLK (clock) and DAT (data) via the STEMMA QT connection or the terminal block pins.

![](https://cdn-learn.adafruit.com/assets/assets/000/118/710/medium800/arduino_compatibles_metroStemma_bb.jpg?1677081029)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/892/medium800/lcds___displays_i2cwire_t.jpeg?1396777195)

## Install Adafruit\_LiquidCrystal

To begin reading sensor data, you will need to download the Adafruit\_LiquidCrystal library from the Arduino library manager.

Open up the Arduino library manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/084/210/medium800/arduino_compatibles_library_manager_menu.png?1573774474)

Search for the&nbsp; **Adafruit LiquidCrystal&nbsp;** library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/211/medium800/arduino_compatibles_liquidcrystal.png?1573774499)

We also have a great tutorial on Arduino library installation at:  
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")

## Load Demo

Restart the IDE and load up the **Adafruit\_LiquidCrystal-\>HelloWorld\_i2c** demo

![](https://cdn-learn.adafruit.com/assets/assets/000/029/934/medium800/lcds___displays_i2cdemo.png?1453416384)

Upload the sketch. You should see the backlight turn on when the Arduino resets. If you don't see any characters, adjust the **Contrast** trim potentiometer with a mini-screwdriver until you see the text clearly

The default **HelloWorld** sketch blinks the backlight as well as updating the text.

**If you see the backlight blinking that means your connection to the I2C port is OK but the contrast is too low or too high** , or the LCD data pins are not solidly connected.

Check the contrast first by gently twisting the mini trim potentiometer, if that doesn't help, recheck your soldering and resolder all 16 of the LCD pins!  
  
Once you're done, you can remove the blinking LED backlight code:

> lcd.setBacklight(HIGH);  
> delay(500);  
> lcd.setBacklight(LOW);  
> delay(500);

![](https://cdn-learn.adafruit.com/assets/assets/000/001/893/medium800/lcds___displays_i2cconnect_t.jpeg?1396777200)

## Changing the I2C Address

If you want to have more than one LCD backpack device each one needs to have a unique 'address'. You can set the address by jumpering the **A0** &nbsp; **A1** &nbsp;and&nbsp; **A2** &nbsp;solder jumpers.&nbsp; By default, no jumpers are soldered, giving an address of **0x20** (offset **0** ). If you want to have an address of&nbsp; **0x23** (0x20 + offset **3** ) you would solder&nbsp; **A0** &nbsp;(bit 0) and&nbsp; **A1** (bit 1) for an address offset of "011" = 3 in binary.&nbsp;

![](https://cdn-learn.adafruit.com/assets/assets/000/118/882/medium800/adafruit_products_arduino_compatibles_addresses.jpg?1677247594)

Then, in the code change:

```
// Connect via i2c, default address #0 (A0-A2 not jumpered)
LiquidCrystal lcd(0);
```

to

```
// Connect via i2c, address #3 (A0&amp;A1 jumpered)
LiquidCrystal lcd(3);
```

- [Previous Page](https://learn.adafruit.com/i2c-spi-lcd-backpack/assembly.md)
- [Next Page](https://learn.adafruit.com/i2c-spi-lcd-backpack/arduino-spi-use.md)

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
