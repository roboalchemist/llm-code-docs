# Source: https://learn.adafruit.com/thermocouple.md

# MAX31855 Thermocouple

## Overview

A thermocouple is a kind of temperature sensor.

Unlike [semiconductor temperature sensors such as the TMP36](http://learn.adafruit.com/tmp36-temperature-sensor) , thermocouples have no electronics inside them, they are simply made by welding together two metal wires. Because of a physical effect of two joined metals, there is a slight but measurable voltage across the wires that increases with temperature. The type of metals used affect the voltage range, cost and sensitivity, which is why we have a few different kinds of thermocouples. The main improvement of using a thermocouple over a semiconductor sensor or thermistor is that the temperature range is very much increased. For example, the TMP36 can go from -50 to 150°C, after that the chip itself can be damaged. Common thermocouples on the other hand, can go from -200°C to 1350°C (K type) and there are ones that can go above 2300°C!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/364/medium800/temperature_thermocouple_LRG.jpg?1396762464)

Thermocouples are often used in HVAC systems, heaters and boilers, kilns, etc. There are a few different kinds but this tutorial will discuss K type, which are very common and easier to interface with.

One difficulty in using them is that the voltage to be measured is very small, with changes of about 50 uV per °C (a uV is 1/1000000 Volts). While it is possible to read these voltages using a clean power supply and nice op-amps, there are other complications such as a non-linear response (its not always 50uV/°C) and cold-temperature compensation (the effect measured is only a differential and there must be a reference, just as ground is a reference for voltage). For that reason, we suggest only using an interface chip that will do the heavy lifting for you, allow you to easily integrate the sensor without as much pain. In this tutorial we will use a MAX6675 K-thermocouple interface chip which doesn't even require an ADC, spitting out a nice digital data signal of the temperature.

## Some Basic Stats

## This is for a K-type thermocouple with glass overbraiding

- **Size:** &nbsp;24 gauge, 1 meter long (you can cut it down if desired)
- **Price:&nbsp;** [$10 at the adafruit store](http://www.adafruit.com/index.php?main_page=product_info&cPath=35&products_id=270)
- **Temperature range:** &nbsp;-100°C to 500°C / -150 to 900°F (After this the glass overbraiding may be damaged)
- **Output range:&nbsp;** -6 to +20mV
- **Precision:** &nbsp;+-2°C
- **[Requires an amplifier such as MAX31855](http://www.adafruit.com/products/269 "Link: http://www.adafruit.com/products/269")**
- **Interface** :&nbsp;[MAX6675](https://www.analog.com/en/products/max6675.html) (discontinued),&nbsp;[MAX31855](http://www.adafruit.com/products/269), or [AD595](http://www.analog.com/en/sensors/analog-temperature-sensors/ad595/products/product.html)&nbsp;(analog)
- **[K Thermocouple Datasheet](https://sea.omega.com/temperature/Z/pdf/z204-206.pdf)**
- **[MAX6675 Datasheet](http://www.adafruit.com/datasheets/MAX6675.pdf)**
- **[MAX31855 Datasheet](http://www.adafruit.com/datasheets/MAX31855.pdf)**

- [Next Page](https://learn.adafruit.com/thermocouple/wiring-a-thermocouple.md)

## Primary Products

### Adafruit Universal Thermocouple Amplifier MAX31856 Breakout

[Adafruit Universal Thermocouple Amplifier MAX31856 Breakout](https://www.adafruit.com/product/3263)
Thermocouples are very sensitive, requiring a good amplifier with a cold-compensation reference, as well as calculations to handle any non-linearities. For a long time we've [suggested our MAX31855K breakout, which works great but is only for...](https://www.adafruit.com/products/269)

Out of Stock
[Buy Now](https://www.adafruit.com/product/3263)
[Related Guides to the Product](https://learn.adafruit.com/products/3263/guides)

## Featured Products

### Thermocouple Amplifier MAX31855 breakout board (MAX6675 upgrade)

[Thermocouple Amplifier MAX31855 breakout board (MAX6675 upgrade)](https://www.adafruit.com/product/269)
Thermocouples are very sensitive, requiring a good amplifier with a cold-compensation reference. The MAX31855K does everything for you, and can be easily interfaced with any microcontroller, even one without an analog input. This breakout board has the chip itself, a 3.3V regulator with 10uF...

In Stock
[Buy Now](https://www.adafruit.com/product/269)
[Related Guides to the Product](https://learn.adafruit.com/products/269/guides)
### Thermocouple Type-K Glass Braid Insulated

[Thermocouple Type-K Glass Braid Insulated](https://www.adafruit.com/product/270)
Thermocouples are best used for measuring temperatures that can go above 100 °C. This is a bare wires bead-probe which can measure air or surface temperatures. Most inexpensive thermocouples have a vinyl covering which can melt at around 200 °C, this one uses a fiberglass braid so it...

Out of Stock
[Buy Now](https://www.adafruit.com/product/270)
[Related Guides to the Product](https://learn.adafruit.com/products/270/guides)
### Thermocouple Type-K Glass Braid Insulated Stainless Steel Tip

[Thermocouple Type-K Glass Braid Insulated Stainless Steel Tip](https://www.adafruit.com/product/3245)
Thermocouples are best used for measuring temperatures that can go above 100°C. This is a bare wires stainless-steel tip probe which can measure air or surface temperatures. Most inexpensive thermocouples have a vinyl covering which can melt at around 200°C, this one uses a fiberglass...

In Stock
[Buy Now](https://www.adafruit.com/product/3245)
[Related Guides to the Product](https://learn.adafruit.com/products/3245/guides)

## Related Guides

- [Adafruit FT232H With SPI & I2C Devices](https://learn.adafruit.com/adafruit-ft232h-with-spi-and-i2c-libraries.md)
- [MicroPython Hardware: SPI Devices](https://learn.adafruit.com/micropython-hardware-spi-devices.md)
- [Connecting the MAX31855 Thermocouple Amplifier breakout to an Electric Imp](https://learn.adafruit.com/connecting-the-max31855-thermocouple-amplifier-breakout-to-an-electric-imp.md)
- [Google Docs Sensor Logging From Your PC](https://learn.adafruit.com/gdocs-sensor-logging-from-your-pc.md)
- [CircuitPython Libraries on Linux and the 96Boards DragonBoard 410c](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-96boards-dragonboard-410c.md)
- [MAX31855 Thermocouple Sensor Python Library](https://learn.adafruit.com/max31855-thermocouple-python-library.md)
- [Adding a Single Board Computer to Blinka](https://learn.adafruit.com/adding-a-single-board-computer-to-blinka.md)
- [CircuitPython I2C and SPI Under the Hood](https://learn.adafruit.com/circuitpython-basics-i2c-and-spi.md)
- [ Analog IC Insights On-the-Go by Maxim Integrated](https://learn.adafruit.com/maxim-app.md)
- [Adafruit 1-Wire Thermocouple Amplifier - MAX31850K](https://learn.adafruit.com/adafruit-1-wire-thermocouple-amplifier-max31850k.md)
- [Calibrating Sensors](https://learn.adafruit.com/calibrating-sensors.md)
- [Adafruit TE MS8607 PHT Sensor](https://learn.adafruit.com/adafruit-te-ms8607-pht-sensor.md)
- [Adafruit Sensirion SHT40, SHT41 & SHT45 Temperature & Humidity Sensors](https://learn.adafruit.com/adafruit-sht40-temperature-humidity-sensor.md)
- [Adafruit SHT4x Trinkey](https://learn.adafruit.com/adafruit-sht4x-trinkey.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
