# Source: https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython.md

# Source: https://learn.adafruit.com/rgb-lcd-shield/circuitpython.md

# Source: https://learn.adafruit.com/thermistor/circuitpython.md

# Source: https://learn.adafruit.com/ir-sensor/circuitpython.md

# Source: https://learn.adafruit.com/photocells/circuitpython.md

# Source: https://learn.adafruit.com/rgb-lcd-shield/circuitpython.md

# Source: https://learn.adafruit.com/thermistor/circuitpython.md

# Source: https://learn.adafruit.com/ir-sensor/circuitpython.md

# Source: https://learn.adafruit.com/photocells/circuitpython.md

# Source: https://learn.adafruit.com/thermistor/circuitpython.md

# Thermistor

## CircuitPython

It's easy to use a thermistor with CircuitPython and your board's built-in analog to digital converters.&nbsp; Just like with the Arduino example on the previous page you can connect the thermistor to a board's analog input and read the resistance.&nbsp; As the temperature changes the resistance changes and you can convert that resistance into a precise temperature value with Python code!

Before you get started it will help to [familiarize yourself with analog inputs in CircuitPython](../../../../circuitpython-basics-analog-inputs-and-outputs).

Next wire up a thermistor to your board exactly as shown on the previous page.&nbsp; You need a fixed resistor (typically 10 kilo-ohms) connected from an analog input up to 3.3V.&nbsp; Then connect one pin from the thermistor to the same analog input and the other pin to your board's ground.&nbsp; In this example we'll use analog input A1 on a Feather M0 basic.

![](https://cdn-learn.adafruit.com/assets/assets/000/047/590/medium800/temperature_m0_thermistor_bb.png?1508891194)

[Fritzing Source](https://cdn-learn.adafruit.com/assets/assets/000/047/591/original/m0_thermistor.fzz?1508891232)
Next&nbsp;[connect to the board's serial REPL&nbsp;](../../../../micropython-basics-how-to-load-micropython-on-a-board/serial-terminal)so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

You can import the necessary **board** and **analogio** modules by running:

```
import board
import analogio
```

Now create an analog input using the pin you've connected to the thermistor:

```
thermistor = analogio.AnalogIn(board.A1)
```

At this point you can read the raw ADC value from the thermistor:

```
thermistor.value
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/435/medium800/temperature_Screen_Shot_2017-10-20_at_3.47.11_PM.png?1508539646)

The raw value isn't very interesting to us though, we really want to convert it to a resistance and temperature value.&nbsp; One thing to note though is that this raw value will always be in the range from 0 to 65535, unlike in Arduino where it ranges from 0 to 1023.&nbsp; As the resistance of the thermistor changes (based on temperature changes) this raw value will change too.

Using the same equation as the previous page you can calculate the resistance of the thermistor:

```
R = 10000 / (65535/thermistor.value - 1)
print('Thermistor resistance: {} ohms'.format(R))
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/437/medium800/temperature_Screen_Shot_2017-10-20_at_3.54.00_PM.png?1508540059)

Remember if you're using a different size resistor your might need to change the equation above and the 10000 value inside it!

# Convert to Temperature

Converting the thermistor's resistance to temperature is just like you saw on the previous page with Arduino.&nbsp; You can use a special equation and some known parameters about the thermistor to perform this conversion in Python code.

First make sure you know these values for your thermistor (check its datasheet if available):

- **Ro** - The resistance at a nominal temperature value.&nbsp; This is typically 10,000 ohms.
- **To** - The temperature (in Celsius) at the nominal resistance value above.&nbsp; This is typically 25.0 degrees C.
- **Beta** - The beta coefficient value for the thermistor.&nbsp; Typically this is a value in the range of 3000-4000, for example 3950.

We can now solve the simplified B coefficient Steinhart-Hart equation mentioned on the previous page.&nbsp; Here's a function you can define to perform this math:

```
def steinhart_temperature_C(r, Ro=10000.0, To=25.0, beta=3950.0):
    import math
    steinhart = math.log(r / Ro) / beta      # log(R/Ro) / beta
    steinhart += 1.0 / (To + 273.15)         # log(R/Ro) / beta + 1/To
    steinhart = (1.0 / steinhart) - 273.15   # Invert, convert to C
    return steinhart
```

Now call the function and pass it the thermistor resistance that you calculated.&nbsp; You can pass in explicit Ro, To, and beta parameters too or use the defaults (10k, 25.0C, 3950):

```
R = 10000 / (65535/thermistor.value - 1)
steinhart_temperature_C(R)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/438/medium800/temperature_Screen_Shot_2017-10-20_at_4.09.40_PM.png?1508541085)

Or if you're passing in explicit Ro, To, beta parameters:

```
steinhart_temperature_C(R, Ro=10000.0, To=25.0, beta=3950)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/439/medium800/temperature_Screen_Shot_2017-10-20_at_4.12.04_PM.png?1508541136)

Now you have the temperature from the thermistor as a value in degrees Celsius!

# Thermistor Module

If you just want to read the value of a thermistor you can actually use a handy CircuitPython module to perform all the above calculations for you automatically.&nbsp; To use the&nbsp;thermistor module sensor&nbsp;with your&nbsp;[Adafruit CircuitPython](https://blog.adafruit.com/2017/01/09/welcome-to-the-adafruit-circuitpython-beta/)&nbsp;board you'll need to install the&nbsp;[Adafruit\_CircuitPython\_Thermistor](https://github.com/adafruit/Adafruit_CircuitPython_Thermistor)&nbsp;module on your board.&nbsp; **Remember this module is for Adafruit CircuitPython firmware and not MicroPython.org firmware!**

First make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://github.com/adafruit/circuitpython/releases)&nbsp;for your board.

Next you'll need to install the necessary libraries&nbsp;to use the hardware--carefully follow the steps to find and install these libraries from&nbsp;[Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).&nbsp; For example the Circuit Playground Express guide has&nbsp;[a great page on how to install the library bundle](../../../../adafruit-circuit-playground-express/installing-libraries)&nbsp;for both express and non-express boards.

Remember for non-express boards like the Trinket M0, Gemma M0, and Feather/Metro M0 basic you'll need to manually install the necessary libraries from the bundle:

- **adafruit\_thermistor.mpy**

Before continuing make sure your board's lib folder or root filesystem has the&nbsp; **adafruit\_thermistor.mpy&nbsp;** module&nbsp;copied over.

![](https://cdn-learn.adafruit.com/assets/assets/000/047/537/medium800/temperature_Screen_Shot_2017-10-23_at_4.11.39_PM.png?1508800330)

## Usage

To&nbsp;demonstrate the usage of the&nbsp;thermistor&nbsp; module you can connect to your board's serial REPL and run Python code to read the temperature and humidity.

First&nbsp;[connect to the board's serial REPL&nbsp;](../../../../micropython-basics-how-to-load-micropython-on-a-board/serial-terminal)so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

Next import the&nbsp; **board** &nbsp;and&nbsp; **adafruit\_thermistor** &nbsp;modules, these are necessary modules to initialize and access the sensor:

```
import board
import adafruit_thermistor
```

Now create an instance of the **Thermistor** class from the module.&nbsp; You'll need to know the Ro, To, and beta parameters for your thermistor just like when performing the math yourself.&nbsp; For example with the same thermistor setup as before you would run:

```
thermistor = adafruit_thermistor.Thermistor(board.A1, 10000.0, 10000.0, 25.0, 3950.0, high_side=False)
```

Let's break down all the parameters sent to the **Thermistor** initializer:

- **Analog input** - The first parameter is the name of the analog input connected to the thermistor, board pin A1 in this case.
- **Series resistance** &nbsp;- The second parameter is the value of the series resistor connected to the thermistor.&nbsp; If you're following this guide you want a value of 10,000 ohms.
- **Nominal resistance (Ro)** - The third parameter is the value of the thermistor's resistance at a nominal temperature.&nbsp; For the thermistor in this guide use the same 10,000 ohms value.
- **Nominal temperature (To)** - The fourth parameter is the value of the thermistor's temperature (in degrees Celsius) at a nominal resistance value.&nbsp; For the thermistor in this guide use the same 25.0 degree value.
- **Beta coefficient** - The fifth parameter is the beta coefficient for your thermistor, 3950 in this case.
- **High\_side boolean** - The sixth parameter is optional and indicates if the thermistor is connected on the high side or low side of the resistor voltage divider.&nbsp; For this guide we've actually wired up the thermistor on the low side, or from the ADC input down to ground.&nbsp; However for other boards and usage you might wire the thermistor the opposite way from the high side, or from ADC input up to 3.3V or 5V.&nbsp; The default value for this high\_side parameter is true but for the wiring in this guide we need to tell it that we're using low side wiring by setting high\_side to false.

Once the thermistor instance is created you can read the temperature property to get the temperature value in degrees Celsius:

```
thermistor.temperature
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/538/medium800/temperature_Screen_Shot_2017-10-23_at_4.21.51_PM.png?1508800928)

That's all you need to read the temperature of a thermistor with the thermistor module!&nbsp; Internally the module will do all the necessary Steinhart-Hart equation math for you.&nbsp; You can grab the temperature result and use it in your own programs to add temperature sensing!

- [Previous Page](https://learn.adafruit.com/thermistor/using-a-thermistor.md)

## Featured Products

### 10K Precision Epoxy Thermistor

[10K Precision Epoxy Thermistor](https://www.adafruit.com/product/372)
Need to measure something damp? This epoxy-coated precision 1% 10K thermistor is an inexpensive way to measure temperature in weather or liquids. The resistance in 25 °C is 10K (+- 1%). The resistance goes down as it gets warmer and goes up as it gets cooler. <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/372)
[Related Guides to the Product](https://learn.adafruit.com/products/372/guides)

## Related Guides

- [Adafruit Sensirion SHT40, SHT41 & SHT45 Temperature & Humidity Sensors](https://learn.adafruit.com/adafruit-sht40-temperature-humidity-sensor.md)
- [Compost Friend!](https://learn.adafruit.com/compost-optimization-machine.md)
- [No-Code DS18B20 Temperature Sensor with WipperSnapper](https://learn.adafruit.com/using-ds18b20-temperature-sensor-with-wippersnapper.md)
- [Adafruit MAX31856 Universal Thermocouple Amplifier](https://learn.adafruit.com/adafruit-max31856-thermocouple-amplifier.md)
- [Make It Hot or Cold](https://learn.adafruit.com/make-it-hot-or-cold.md)
- [Adafruit SHT4x Trinkey](https://learn.adafruit.com/adafruit-sht4x-trinkey.md)
- [PyGamer Thermal Camera with AMG8833](https://learn.adafruit.com/pygamer-thermal-camera-amg8833.md)
- [Adafruit AHT20 Temperature & Humidity Sensor](https://learn.adafruit.com/adafruit-aht20.md)
- [Adafruit HDC1008 Temperature and Humidity Sensor Breakout](https://learn.adafruit.com/adafruit-hdc1008-temperature-and-humidity-sensor-breakout.md)
- [Humidity and Temperature Monitor with E-Ink Display](https://learn.adafruit.com/humidity-and-temperature-monitor-redux-e-ink-display.md)
- [Adafruit TMP117 High Accuracy I2C Temperature Monitor](https://learn.adafruit.com/adafruit-tmp117-high-accuracy-i2c-temperature-monitor.md)
- [My Mini Race Car](https://learn.adafruit.com/my-mini-race-car.md)
- [Raspberry Pi Azure IoT Hub Dashboard with CircuitPython](https://learn.adafruit.com/raspberry-pi-iot-dashboard-with-azure-and-circuitpython.md)
- [Ikea Vindriktning Hack with QT Py ESP32-S3 and Adafruit IO](https://learn.adafruit.com/ikea-vindriktning-hack-with-qt-py-esp32-s3-and-adafruit-io.md)
- [Adafruit MLX90640 IR Thermal Camera](https://learn.adafruit.com/adafruit-mlx90640-ir-thermal-camera.md)
