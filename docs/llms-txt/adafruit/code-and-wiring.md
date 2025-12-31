# Source: https://learn.adafruit.com/light-meter/code-and-wiring.md

# Light Meter

## Code & Wiring

First up is plugging the light sensor into the breadboard.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/268/medium800/light_LightMeterStep1.jpg?1396781144)

The next step is connecting the sensor to the Arduino:

- Sensor **GND pin** - black wire – Arduino **ground**  **pin**
- Sensor **VCC pin** - yellow wire – Arduino **3.3v**  **pin**
- Sensor **SCL pin** - green wire – Arduino **analog pin 5** (i2c clock line)
- Sensor **SDA pin** - blue wire – Arduino **analog pin 4** (i2c data line)

If you're using only the TSL2561 on your Arduino and no other I2C devices, its fine to connect it directly. If you have other I2C devices that run on 5V connected at the same time [you should use a i2c-compatible level shifter such as this one](http://www.adafruit.com/products/757) to shift both the SCL and SDA data. Connect the **HV** pin to 5V, the **LV** pin to 3.3V, grounds to ground, and connect **A1** and **B1** channels to the TSL SDA/SCL pins and **A2** and **B2** to the matching Arduino I2C pins  

![](https://cdn-learn.adafruit.com/assets/assets/000/002/269/medium800/light_LightMeterStep2.jpg?1396781153)

The LCD can now be added to the circuit. &nbsp;Since this project uses SPI mode to talk to the LCD, make sure the SPI solder enable jumper&nbsp;has been soldered.

- LCD backpack&nbsp; **GND pin** &nbsp;- black wire – Arduino&nbsp; **ground pin**
- LCD&nbsp;backpack&nbsp; **5V pin** &nbsp;- red wire – Arduino&nbsp; **A5V pin**
- LCD&nbsp;backpack&nbsp; **LAT pin&nbsp;** - orange wire – Arduino&nbsp; **digital pin 4** (SPI latch pin)
- LCD&nbsp;backpack&nbsp; **DAT pin** &nbsp;- blue wire –&nbsp;Arduino&nbsp; **digital pin 3** (SPI data pin)
- LCD&nbsp;backpack **&nbsp;CLK pin** &nbsp;- green wire –&nbsp;Arduino **&nbsp;digital pin 2** (SPI clock pin)  

![](https://cdn-learn.adafruit.com/assets/assets/000/002/270/medium800/light_LightMeterStep3.jpg?1396781165)

With all components added, the block diagram of the circuit looks like this:![](https://cdn-learn.adafruit.com/assets/assets/000/002/272/medium800/light_LightMeterSchematic.png?1396781215)

_Arduino Uno image courtesy of Fritzing_For my project, I’m gathering data at reasonably high light levels; so, I went with the following settings:

```
tsl.setGain(TSL2561_GAIN_0X);
tsl.setTiming(TSL2561_INTEGRATIONTIME_13MS);
```

If you are measuring low light levels, you may want to adjust these two lines accordingly:

```
tsl.setGain(TSL2561_GAIN_16X);
tsl.setTiming(TSL2561_INTEGRATIONTIME_402MS);
```

An additional area to highlight is how the sketch is printing the light level values:

```
snprintf_P(output_buffer, 6, PSTR("%5d"), (full_spectrum - ir_spectrum));
```

 **snprintf\_P** is a variant of sprintf that adds a couple of nice features. &nbsp;The ‘ **n** ’ indicates that you can specify a maximum number of bytes to write into the buffer; this helps protect against accidental buffer overruns. &nbsp;The ‘ **\_P** ’ indicates that the format string is read from program memory; this helps conserve RAM. &nbsp;In the invocation above, I’m using the companion macro **PSTR()** to keep the format string parameter in program memory.- [Previous Page](https://learn.adafruit.com/light-meter/overview-and-parts.md)
- [Next Page](https://learn.adafruit.com/light-meter/downloads.md)

## Featured Products

### Adafruit TSL2561 Digital Luminosity/Lux/Light Sensor Breakout

[Adafruit TSL2561 Digital Luminosity/Lux/Light Sensor Breakout](https://www.adafruit.com/product/439)
The TSL2561 luminosity sensor is an advanced digital light sensor, ideal for use in a wide range of light situations. Compared to low cost CdS cells, this sensor is more precise, allowing for exact lux calculations and can be configured for different gain/timing ranges to detect light ranges...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/439)
[Related Guides to the Product](https://learn.adafruit.com/products/439/guides)
### i2c / SPI character LCD backpack - STEMMA QT / Qwiic

[i2c / SPI character LCD backpack - STEMMA QT / Qwiic](https://www.adafruit.com/product/292)
Character LCDs are a fun and easy way to have your microcontroller project talk back to you. They are also common, and easy to get, available in tons of colors and sizes. [We've written tutorials on using character LCDs with an Arduino](http://learn.adafruit.com/character-lcds)...

In Stock
[Buy Now](https://www.adafruit.com/product/292)
[Related Guides to the Product](https://learn.adafruit.com/products/292/guides)
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
### 4-channel I2C-safe Bi-directional Logic Level Converter

[4-channel I2C-safe Bi-directional Logic Level Converter](https://www.adafruit.com/product/757)
Because the Arduino (and Basic Stamp) are 5V devices, and most modern sensors, displays, flashcards, and modes are 3.3V-only, many makers find that they need to perform level shifting/conversion to protect the 3.3V device from 5V. Here we've got a **&nbsp;4-channel I2C-safe...**

In Stock
[Buy Now](https://www.adafruit.com/product/757)
[Related Guides to the Product](https://learn.adafruit.com/products/757/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [I2C/SPI LCD Backpack](https://learn.adafruit.com/i2c-spi-lcd-backpack.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
- [Introducing Adafruit Trellis ](https://learn.adafruit.com/adafruit-trellis-diy-open-source-led-keypad.md)
- [Wireless Game Show Poppers for the Classroom!](https://learn.adafruit.com/wireless-game-show-poppers.md)
- [Adafruit INA219 Current Sensor Breakout](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout.md)
- [Naughty or Nice Machine](https://learn.adafruit.com/naughty-or-nice-machine.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [Adafruit Optical Fingerprint Sensor](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor.md)
- [Nokia 5110/3310 Monochrome LCD](https://learn.adafruit.com/nokia-5110-3310-monochrome-lcd.md)
- [Sending an SMS with Temboo](https://learn.adafruit.com/sending-an-sms-with-temboo.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [Arduino "Hunt The Wumpus"](https://learn.adafruit.com/arduino-hunt-the-wumpus.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
- [CircuitPython Libraries on Linux and the 96Boards DragonBoard 410c](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-96boards-dragonboard-410c.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
