# Source: https://learn.adafruit.com/thermistor.md

# Thermistor

## Overview

A thermistor is a&nbsp; **thermal resistor** &nbsp;- a resistor that changes its resistance with temperature. Technically, all resistors are thermistors - their resistance changes slightly with temperature - but the change is usually very very small and difficult to measure. Thermistors are made so that the resistance changes drastically with temperature so that it can be 100 ohms or more of change per degree!![](https://cdn-learn.adafruit.com/assets/assets/000/000/567/medium800/temperature_ntc10kepoxythermistor_LRG.jpg?1396764093)

There are two kinds of of thermistors, NTC (negative temperature coefficient) and PTC (positive temperature coefficient). In general, you will see NTC sensors used for temperature measurement. PTC's are often used as resettable fuses - an increase in temperature increases the resistance which means that as more current passes through them, they heat up and 'choke back' the current, quite handy for protecting circuits!

Thermistors have some benefits over other kinds of temperature sensors such as analog output chips ([LM35/TMP36](http://www.ladyada.net/learn/sensors/temp36.html) ) or digital temperature sensor chips (DS18B20) or [thermocouples](http://learn.adafruit.com/thermocouple/).

- First off, they are much much cheaper than all the above! A bare 5% thermistor is only 10 cents in bulk.
- They are also much easier to waterproof since its just a resistor.
- They work at any voltage (digital sensors require 3 or 5V logic).
- Compared to a thermocouple, they don't require an amplifier to read the minute voltages - you can use any microcontroller to read a thermistor.
- They can also be incredibly accurate for the price. For example, the 10K 1% thermistor in the shop is good for measuring with ±0.25°C accuracy! (Assuming you have an accurate enough analog converter)
- They are difficult to break or damage - they are much simpler and more reliable

On the other hand, they require a little more work to interpret readings, and they dont work at very high temperatures like thermocouples. Without a digital-to-analog converter on board, you might be better off with a digital temperature sensor.

Their simplicity makes them incredibly popular for basic temperature feedback control. For example, lets say you wanted to have a fan that turns on when the temperature gets high. You could use a microcontroller, a digital sensor, and have that control the relay. Or you could use the thermistor to feed the base of a transistor, as the temperature rises, the resistance goes down, feeding more current into the transistor until it turns on. (This is a rough idea, you would need a few more components to make it work)

Even if you do use a microcontroller or complex system, for the price you can't beat 'em!

**[You can pick up a 10K 1% waterproof thermistor in the Adafruit shop](http://www.adafruit.com/products/372)**

## Some Stats
[Here are technical details for the thermistor in our shop](http://www.adafruit.com/products/372 "Link: http://www.adafruit.com/products/372")
- **Resistance at 25°C:** &nbsp;10K ±1%
- **B25/50:** &nbsp;3950 ±1%
- **Thermal time constant** &nbsp;? 15 seconds
- **Thermistor temperature range** &nbsp;-55°C to 125°C
- **Wire temperature range** &nbsp;-55°C to 105°C
- **28 AWG PVC Wire**
- **Diameter: 3.5mm/0.13in**
- **Length: 18in/45cm**
- [Resistance/Temperature table](http://www.adafruit.com/datasheets/103_3950_lookuptable.pdf)

Note that even though the thermistor can go up to 125°C the cable itself maxes out at 105°C so this thermistor is not good for measuring very very hot liquids

- [Next Page](https://learn.adafruit.com/thermistor/testing-a-thermistor.md)

## Featured Products

### 10K Precision Epoxy Thermistor

[10K Precision Epoxy Thermistor](https://www.adafruit.com/product/372)
Need to measure something damp? This epoxy-coated precision 1% 10K thermistor is an inexpensive way to measure temperature in weather or liquids. The resistance in 25 °C is 10K (+- 1%). The resistance goes down as it gets warmer and goes up as it gets cooler. <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/372)
[Related Guides to the Product](https://learn.adafruit.com/products/372/guides)

## Related Guides

- [reef-pi Guide 1: Setup and Demonstration](https://learn.adafruit.com/reef-pi-installation-and-configuration.md)
- [Adafruit MCP9600 I2C Thermocouple Amplifier](https://learn.adafruit.com/adafruit-mcp9600-i2c-thermocouple-amplifier.md)
- [Calibrating Sensors](https://learn.adafruit.com/calibrating-sensors.md)
- [EMC2101 Fan Controller and Temperature sensor](https://learn.adafruit.com/emc2101-fan-controller-and-temperature-sensor.md)
- [Arm-based IoT Kit for Cloud IoT Core - Getting Started](https://learn.adafruit.com/raspberry-pi-3-and-sensor-kit-for-google-cloud-iot-core.md)
- [AM2315 - Encased I2C Temperature/Humidity Sensor](https://learn.adafruit.com/am2315-encased-i2c-temperature-humidity-sensor.md)
- [TMP006 Infrared Sensor Breakout](https://learn.adafruit.com/infrared-thermopile-sensor-breakout.md)
- [Adafruit MLX90640 IR Thermal Camera](https://learn.adafruit.com/adafruit-mlx90640-ir-thermal-camera.md)
- [MAX31855 Thermocouple Sensor Python Library](https://learn.adafruit.com/max31855-thermocouple-python-library.md)
- [Storage humidity and temperature monitor](https://learn.adafruit.com/storage-humidity-and-temperature-monitor.md)
- [Kombucha Thermostat with CircuitPython and Feather ](https://learn.adafruit.com/kombucha-thermostat-with-circuitpython-and-feather.md)
- [TMP36 Temperature Sensor](https://learn.adafruit.com/tmp36-temperature-sensor.md)
- [Monitor Your Greenhouse with a No-Code Environmental Sensor](https://learn.adafruit.com/monitor-your-greenhouse-with-a-no-code-environmental-sensor.md)
- [Adafruit TE MS8607 PHT Sensor](https://learn.adafruit.com/adafruit-te-ms8607-pht-sensor.md)
- [Using Melexis MLX90614 Non-Contact Sensors](https://learn.adafruit.com/using-melexis-mlx90614-non-contact-sensors.md)
