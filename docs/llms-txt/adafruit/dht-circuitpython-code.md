# Source: https://learn.adafruit.com/dht/dht-circuitpython-code.md

# DHT11, DHT22 and AM2302 Sensors

## DHT CircuitPython Code

Warning: 

# Adafruit CircuitPython Module Install

To use the&nbsp;DHT sensor&nbsp;with your&nbsp;Adafruit CircuitPython&nbsp;board you'll need to install the&nbsp;[Adafruit\_CircuitPython\_DHT](https://github.com/adafruit/Adafruit_CircuitPython_DHT)&nbsp;module on your board.

First make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://circuitpython.org/downloads) for your board.

Next you'll need to install the necessary libraries&nbsp;to use the hardware--carefully follow the steps to find and install these libraries from&nbsp;[Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).&nbsp; Our introduction guide has&nbsp;[a great page on how to install the library bundle](../../../../welcome-to-circuitpython/circuitpython-libraries)&nbsp;for both express and non-express boards.

Remember for non-express boards like the, you'll need to manually install the necessary libraries from the bundle:

- **adafruit\_dht.mpy**

You can also download the&nbsp; **adafruit\_dht.mpy** &nbsp;from&nbsp;[its releases page on Github](https://github.com/adafruit/Adafruit_CircuitPython_DHT/releases).

Before continuing make sure your board's lib folder or root filesystem has the&nbsp; **adafruit\_dht.mpy&nbsp;** module&nbsp;copied over.

![](https://cdn-learn.adafruit.com/assets/assets/000/050/108/medium800/weather_dhtfile.png?1515800171)

# Wiring

DHT wiring is very simple:

- The left-most pin is **power**. We recommend powering from 5V (sometimes 3V is not enough) - this is OK even if you are using 3.3V logic
- The second pin is **data**. Connect a 10K pullup resistor from this pin to 3.3V. If you are using a DHT11 it's required. If you're using a DHT22 or AM2302 you can sometimes leave this off
- Skip the third pin
- The right-most pin is **ground**

Warning: 

Here's an example using a Trinket M0 - **you can use any CircuitPython board** , just check that the Data pin is `pulseio`-capable.

![weather_adafruit_gemma_dhtcirpy_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/050/100/medium640/weather_adafruit_gemma_dhtcirpy_bb.png?1515799704)

In this example we'll use a Feather M0 and DHT22 sensor connected to pin D6

![weather_m0_dht_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/050/101/medium640/weather_m0_dht_bb.png?1515799866)

[Fritzing Source](https://cdn-learn.adafruit.com/assets/assets/000/047/595/original/m0_dht.fzz?1508892874)
# Usage

To&nbsp;demonstrate the usage of the DHT sensor module you can connect to your board's serial REPL and run Python code to read the temperature and humidity.

Next&nbsp;[connect to the board's serial REPL&nbsp;](../../../../welcome-to-circuitpython/the-repl)so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

Next import the **board** and **adafruit\_dht** modules, these are necessary modules to initialize and access the sensor:

```
import board
import adafruit_dht
```

You may also want to try powering the DHT sensor from 5V (we found sometimes it really needs more power) but still having the 10K pull-up resistor to 3.3V volts)

Now create an instance of either the **DHT11** or **DHT22** class, depending on the type of sensor you're using (for the AM2302 sensor use the DHT22 class).&nbsp; You must pass in the pin which is connected to the signal line, for example a DHT22 or AM2302 sensor connected to board pin `D6` would need this code:

```
dht = adafruit_dht.DHT22(board.D6)
```

Note for a DHT11 sensor you'd instead use **adafruit\_dht.DHT11** in place of the **adafruit\_dht.DHT22** code above.

At this point you're all set and ready to start reading the temperature and humidity!&nbsp; You can do this by reading the **temperature** property which returns temperature in degrees Celsius:

```
dht.temperature
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/431/medium800/weather_Screen_Shot_2017-10-20_at_2.46.03_PM.png?1508536002)

To read the humidity grab the value of the **humidity** property, it will return the percent humidity as a floating point value from 0 to 100%:

```
dht.humidity
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/432/medium800/weather_Screen_Shot_2017-10-20_at_2.46.23_PM.png?1508536069)

In most cases you'll always get back a temperature or humidity value when requested, but sometimes if there's electrical noise or the signal was interrupted in some way you might see an exception thrown to try again.&nbsp; It's normal for these sensors to sometimes be hard to read and you might need to make your code retry a few times if it fails to read.&nbsp; However if you always get errors and can't ever read the sensor then double check your wiring (don't forget the pull-up resistor if needed!) and the power to the device.

# Example Code

Here's a full example sketch which also manages error-retry logic (which will happen once in a while.

**Don't forget to change the logic pin to whatever pin you're using!** Then save this as `main.py` on your CircuitPython board

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Gemma/Introducing_Gemma_M0/dht22/code.py

If you are using a DHT11, change the code to use a `adafruit_dht.DHT11(board.D2)` object.

Open the REPL to see the output! Breathe on the sensor to see it move temperature and humidity up (unless you are a White Walker in which case the temperature will go down)

![](https://cdn-learn.adafruit.com/assets/assets/000/050/105/medium800/weather_adafruit_gemma_dht.png?1515800078)

- [Previous Page](https://learn.adafruit.com/dht/using-a-dhtxx-sensor-with-arduino.md)
- [Next Page](https://learn.adafruit.com/dht/downloads.md)

## Featured Products

### DHT22  temperature-humidity sensor + extras

[DHT22  temperature-humidity sensor + extras](https://www.adafruit.com/product/385)
The DHT22 is a basic, low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air and spits out a digital signal on the data pin (no analog input pins needed). It's fairly simple to use but requires careful timing...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/385)
[Related Guides to the Product](https://learn.adafruit.com/products/385/guides)
### DHT11 basic temperature-humidity sensor + extras

[DHT11 basic temperature-humidity sensor + extras](https://www.adafruit.com/product/386)
 **Discontinued -**  **you can grab the&nbsp;** [DHT20 - AHT20 Pin Module - I2C Temperature and Humidity Sensor](https://www.adafruit.com/product/5183)&nbsp; **instead!&nbsp;**

The DHT11 is a basic, ultra low-cost digital temperature and humidity sensor. It uses...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/386)
[Related Guides to the Product](https://learn.adafruit.com/products/386/guides)
### AM2302 (wired DHT22)  temperature-humidity sensor

[AM2302 (wired DHT22)  temperature-humidity sensor](https://www.adafruit.com/product/393)
Discontinued - [**you can grab** AM2301B - Wired Enclosed AHT20 - Temperature and Humidity Sensor&nbsp; **instead!**](https://www.adafruit.com/product/5181)

The AM2302 is a wired version of the [DHT22](http://www.adafruit.com/products/385), in a large plastic...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/393)
[Related Guides to the Product](https://learn.adafruit.com/products/393/guides)

## Related Guides

- [Adafruit SGP30 TVOC/eCO2 Gas Sensor](https://learn.adafruit.com/adafruit-sgp30-gas-tvoc-eco2-mox-sensor.md)
- [Adafruit BME680](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas.md)
- [Using LoraWAN and The Things Network with CircuitPython](https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython.md)
- [Adafruit BME280 Humidity + Barometric Pressure + Temperature Sensor Breakout](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout.md)
- [Trinket Temperature & Humidity LCD Display](https://learn.adafruit.com/trinket-temperature-humidity-lcd-display.md)
- [PyLeap CLUE Barometer](https://learn.adafruit.com/pyleap-clue-barometer.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [CLUE Vertical Garden Weather Visualizer](https://learn.adafruit.com/clue-vertical-garden-weather-visualizer.md)
- [Adafruit BMP183 SPI Barometric Pressure & Altitude Sensor](https://learn.adafruit.com/adafruit-bmp183-spi-barometric-pressure-and-altitude-sensor.md)
- [Weather Display Matrix](https://learn.adafruit.com/weather-display-matrix.md)
- [ESP8266 WiFi Weather Station with Color TFT Display](https://learn.adafruit.com/wifi-weather-station-with-tft-display.md)
- [Adafruit VEML6070 UV Sensor Breakout](https://learn.adafruit.com/adafruit-veml6070-uv-light-sensor-breakout.md)
- [Adafruit HTU21D-F Temperature & Humidity Sensor](https://learn.adafruit.com/adafruit-htu21d-f-temperature-humidity-sensor.md)
- [IoT Temperature Logger with Analog Devices ADT7410, Feather and Adafruit IO](https://learn.adafruit.com/iot-temperature-logger-with-arduino-and-adafruit-io.md)
- [Adafruit BMP280 Barometric Pressure + Temperature Sensor Breakout](https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout.md)
