# Source: https://learn.adafruit.com/thermocouple/python-circuitpython.md

# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/python-circuitpython.md

# Source: https://learn.adafruit.com/thermocouple/python-circuitpython.md

# MAX31855 Thermocouple

## Python & CircuitPython

It's easy to use the&nbsp;MAX31855 sensor with Python and CircuitPython, and the&nbsp;[Adafruit CircuitPython MAX31855](https://github.com/adafruit/Adafruit_CircuitPython_MAX31855)&nbsp;module.&nbsp; This module allows you to easily write Python code that reads the&nbsp;temperature from the thermocouple.

You can use this sensor with any CircuitPython microcontroller board or with a computer that has GPIO and Python [thanks to Adafruit\_Blinka, our CircuitPython-for-Python compatibility library](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

# CircuitPython Microcontroller Wiring

First wire up a&nbsp;MAX31855 to your board exactly as shown on the previous pages for Arduino.&nbsp; Here's an example of wiring a Feather M0 to the sensor:

- **Board 3V** &nbsp;to&nbsp; **sensor&nbsp;Vdd**
- **Board GND** &nbsp;to&nbsp; **sensor GND**
- **Board SCK** &nbsp;to&nbsp; **sensor&nbsp;CLK**
- **Board MISO** &nbsp;to&nbsp; **sensor&nbsp;DO**
- **Board D5** to **sensor CS** (or any other free digital I/O pin)

![temperature___humidity_FeatherM0_MAX31855.png](https://cdn-learn.adafruit.com/assets/assets/000/059/076/medium640/temperature___humidity_FeatherM0_MAX31855.png?1534117069)

# Python Computer Wiring

Since there's _dozens_ of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).&nbsp;

Here's the Raspberry Pi wired with SPI:

- **Pi**  **3.3V** to **sensor**  **Vin**
- **Pi**  **GND** to **sensor**  **GND**
- **Pi**  **SCLK** to **sensor**  **CLK**
- **Pi**  **MISO** to **sensor**  **DO**
- **Pi**  **GPIO 5** to **sensor**  **CS**

![temperature___humidity_raspi_max31855_spi.png](https://cdn-learn.adafruit.com/assets/assets/000/059/075/medium640/temperature___humidity_raspi_max31855_spi.png?1534116815)

## CircuitPython Installation of MAX31855 Library

Next you'll need to install the&nbsp;[Adafruit CircuitPython MAX31855](https://github.com/adafruit/Adafruit_CircuitPython_MAX31855)&nbsp;library on your CircuitPython board

First make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://github.com/adafruit/circuitpython/releases)&nbsp;for your board.

Next you'll need to install the necessary libraries to use the hardware. You can do this in two ways:

1. **Easy:** In the example at the bottom of the page, click the blue "Download Project Bundle" button to get the example code and libraries for the version of CircuitPython you're using.

2. **Manual method:** &nbsp;carefully follow the steps to find and install these libraries from&nbsp;[Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle). For example the Circuit Playground Express guide has&nbsp;[a great page on how to install the library bundle](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-libraries)&nbsp;for both express and non-express boards.

Remember for non-express boards like the Trinket M0, Gemma M0, and Feather/Metro M0 basic you'll need to manually install the necessary libraries from the bundle:

- **adafruit\_max31855.mpy**
- **adafruit\_bus\_device**

Before continuing make sure your board's lib folder or root filesystem has the **adafruit\_max31855.mpy,** and **adafruit\_bus\_device**** &nbsp; **files and folders** &nbsp;**copied over.

Next[&nbsp;connect to the board's serial REPL](https://learn.adafruit.com/welcome-to-circuitpython/the-repl) so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

## Python Installation of MAX31855 Library

You'll need to install the Adafruit\_Blinka library that provides the CircuitPython support in Python. This **may** also require enabling I2C on your platform (even though this uses SPI not I2C) and verifying you are running Python 3. [Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)!

Once that's done, from your command line run the following command:

- `sudo pip3 install adafruit-circuitpython-max31855`

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

## CircuitPython & Python Usage

To demonstrate the usage of the sensor we'll initialize it and read the temperature.&nbsp; First initialize the&nbsp;SPI connection and library by running:

```python
import board
import digitalio
import adafruit_max31855
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
max31855 = adafruit_max31855.MAX31855(spi, cs)
```

Now you can read the&nbsp; **temperature** &nbsp;property to retrieve the temperature from the sensor in degrees Celsius:

```
print('Temperature: {} degrees C'.format(max31855.temperature))
```

![](https://cdn-learn.adafruit.com/assets/assets/000/048/106/medium800/temperature_Screen_Shot_2017-11-10_at_3.00.50_PM.png?1510354866)

That's all there is to reading temperature with the&nbsp;MAX31855 and CircuitPython code!

## Full Example Code
https://github.com/adafruit/Adafruit_CircuitPython_MAX31855/blob/main/examples/max31855_simpletest.py

- [Previous Page](https://learn.adafruit.com/thermocouple/arduino-code.md)
- [Next Page](https://learn.adafruit.com/thermocouple/f-a-q.md)

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
