# Source: https://learn.adafruit.com/thermocouple/f-a-q.md

# MAX31855 Thermocouple

## F.A.Q.

### 

This is likely caused by the thermocouple wires being labled incorrectly. Try swapping the two thermocouple leads, even if yellow and red wires are in the right slots - we've seen some thermocouple where the wire colors are wrong.  

### 

The MAX31855 is surprisingly sensitive, we've found a good way to fix this is to place a 0.01uF to 0.1uF capacitor across the thermocouple leads (that is, place the capacitor into the blue terminal block, or solder to the bottom as shown below).

![](https://cdn-learn.adafruit.com/assets/assets/000/002/077/medium800/temperature_ThermocoupleCap.jpg?1396779025)

### 

K thermocouples are not precision temperature measurement devices! There will be offsets & differences between thermocouples. Most thermocouple thermometers have the offset corrected in software which is what we suggest. &nbsp;See this guide for tips on calibration: &nbsp;

[Sensor Calibration](../../../../calibrating-sensors/why-calibrate)

For precision temperature measurement, we suggest a 1% Thermistor.

### 

You can connect as many MAX31855's as you have pins. Simply share the CLK and DO pins of all the breakouts and have a unique CS pin for each one  
Then you can create new thermocouples using the following style:

> Adafruit\_MAX31855 thermocouple1(thermoCLK, thermoCS1, thermoDO);  
> Adafruit\_MAX31855 thermocouple2(thermoCLK, thermoCS2, thermoDO);  
> Adafruit\_MAX31855 thermocouple3(thermoCLK, thermoCS3, thermoDO);

You can also try having same CS and CLK pins but all different DO pins  

> Adafruit\_MAX31855 thermocouple1(thermoCLK, thermoCS, thermoDO1);  
> Adafruit\_MAX31855 thermocouple2(thermoCLK, thermoCS, thermoDO2);  
> Adafruit\_MAX31855 thermocouple3(thermoCLK, thermoCS, thermoDO3);

### 

The 31855 chip handles the linear range of the K-type thermocouples very well. &nbsp;It does not provide correction for the non-linearities that occur at the extremes of the measurement range. &nbsp;Thermocouple linearization for temperature extremes requires some curve fitting. &nbsp;See this guide for more information and example code:

[Thermocouple Linearization](../../../../calibrating-sensors/maxim-31855-linearization "MAX31855 Thermocouple Linearization")

- [Previous Page](https://learn.adafruit.com/thermocouple/python-circuitpython.md)
- [Next Page](https://learn.adafruit.com/thermocouple/project-examples.md)

## Primary Products

### Adafruit Universal Thermocouple Amplifier MAX31856 Breakout

[Adafruit Universal Thermocouple Amplifier MAX31856 Breakout](https://www.adafruit.com/product/3263)
Thermocouples are very sensitive, requiring a good amplifier with a cold-compensation reference, as well as calculations to handle any non-linearities. For a long time we've [suggested our MAX31855K breakout, which works great but is only for...](https://www.adafruit.com/products/269)

In Stock
[Buy Now](https://www.adafruit.com/product/3263)
[Related Guides to the Product](https://learn.adafruit.com/products/3263/guides)

## Featured Products

### Thermocouple Amplifier MAX31855 breakout board (MAX6675 upgrade)

[Thermocouple Amplifier MAX31855 breakout board (MAX6675 upgrade)](https://www.adafruit.com/product/269)
Thermocouples are very sensitive, requiring a good amplifier with a cold-compensation reference. The MAX31855K does everything for you, and can be easily interfaced with any microcontroller, even one without an analog input. This breakout board has the chip itself, a 3.3V regulator with 10uF...

Out of Stock
[Buy Now](https://www.adafruit.com/product/269)
[Related Guides to the Product](https://learn.adafruit.com/products/269/guides)
### Thermocouple Type-K Glass Braid Insulated

[Thermocouple Type-K Glass Braid Insulated](https://www.adafruit.com/product/270)
Thermocouples are best used for measuring temperatures that can go above 100 °C. This is a bare wires bead-probe which can measure air or surface temperatures. Most inexpensive thermocouples have a vinyl covering which can melt at around 200 °C, this one uses a fiberglass braid so it...

In Stock
[Buy Now](https://www.adafruit.com/product/270)
[Related Guides to the Product](https://learn.adafruit.com/products/270/guides)
### Thermocouple Type-K Glass Braid Insulated Stainless Steel Tip

[Thermocouple Type-K Glass Braid Insulated Stainless Steel Tip](https://www.adafruit.com/product/3245)
Thermocouples are best used for measuring temperatures that can go above 100°C. This is a bare wires stainless-steel tip probe which can measure air or surface temperatures. Most inexpensive thermocouples have a vinyl covering which can melt at around 200°C, this one uses a fiberglass...

In Stock
[Buy Now](https://www.adafruit.com/product/3245)
[Related Guides to the Product](https://learn.adafruit.com/products/3245/guides)

## Related Guides

- [Google Docs Sensor Logging From Your PC](https://learn.adafruit.com/gdocs-sensor-logging-from-your-pc.md)
- [Calibrating Sensors](https://learn.adafruit.com/calibrating-sensors.md)
- [CircuitPython Libraries on Linux and the 96Boards DragonBoard 410c](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-96boards-dragonboard-410c.md)
- [Connecting the MAX31855 Thermocouple Amplifier breakout to an Electric Imp](https://learn.adafruit.com/connecting-the-max31855-thermocouple-amplifier-breakout-to-an-electric-imp.md)
- [ Analog IC Insights On-the-Go by Maxim Integrated](https://learn.adafruit.com/maxim-app.md)
- [Adafruit 1-Wire Thermocouple Amplifier - MAX31850K](https://learn.adafruit.com/adafruit-1-wire-thermocouple-amplifier-max31850k.md)
- [Adding a Single Board Computer to Blinka](https://learn.adafruit.com/adding-a-single-board-computer-to-blinka.md)
- [MicroPython Hardware: SPI Devices](https://learn.adafruit.com/micropython-hardware-spi-devices.md)
- [CircuitPython I2C and SPI Under the Hood](https://learn.adafruit.com/circuitpython-basics-i2c-and-spi.md)
- [MAX31855 Thermocouple Sensor Python Library](https://learn.adafruit.com/max31855-thermocouple-python-library.md)
- [Adafruit FT232H With SPI & I2C Devices](https://learn.adafruit.com/adafruit-ft232h-with-spi-and-i2c-libraries.md)
- [MLX90640 Thermal Camera with Image Recording](https://learn.adafruit.com/mlx90640-thermal-image-recording.md)
- [EZ Make Oven](https://learn.adafruit.com/ez-make-oven.md)
- [Adafruit BME680](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas.md)
- [My Mini Race Car](https://learn.adafruit.com/my-mini-race-car.md)
