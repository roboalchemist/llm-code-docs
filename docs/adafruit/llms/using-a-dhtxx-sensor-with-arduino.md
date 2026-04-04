# Source: https://learn.adafruit.com/dht/using-a-dhtxx-sensor-with-arduino.md

# DHT11, DHT22 and AM2302 Sensors

## Using a DHTxx Sensor with Arduino

To test the sketch, we'll use an Arduino. You can use any micrcontroller that can do microsecond timing, but since its a little tricky to code it up, we suggest verifying the wiring and sensor work with an Arduino to start.

You should have the [**Arduino IDE**](https://www.arduino.cc/en/Main/Software) software running at this time. Next it’s necessary to install our DHT library, which can be done though the Arduino Library Manager:

**Sketch→Include Library→Manage Libraries…**

Enter “ **dht** ” in the search field and look through the list for “ **DHT sensor library** by **Adafruit**.” Click the “Install” button, or “Update” from an earlier version.

![](https://cdn-learn.adafruit.com/assets/assets/000/069/265/medium800/weather_dht-lib-1.png?1547267322)

 **IMPORTANT:** &nbsp;As of version 1.3.0 of the DHT library you will also need to install the **Adafruit Unified Sensor** library, which is also available in the Arduino Library Manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/069/266/medium800/weather_dht-lib-2.png?1547267332)

Now load up the&nbsp; **Examples→DHT→DHTtester** &nbsp;sketch

![](https://cdn-learn.adafruit.com/assets/assets/000/000/579/medium800/weather_dhttester.gif?1447976216)

If you're using a&nbsp; **DHT11** &nbsp;sensor, comment out the line that sets the type:```
//#define DHTTYPE DHT22   // DHT 22  (AM2302)
```

and uncomment the line that says:```
#define DHTTYPE DHT11   // DHT 11
```

This will make the data appear correctly for the correct sensor. Upload the sketch!![](https://cdn-learn.adafruit.com/assets/assets/000/000/580/medium800/weather_dhtout.gif?1447976226)

You should see the temperature and humidity. You can see changes by breathing onto the sensor (like you would to fog up a window) which should increase the humidity.You can add as many DHT sensors as you line on individual pins, just add new lines such as

`DHT dht2 = DHT(pin, type);`

below the declaration for the initial `dht` object, and you can reference the new `dht2` whenever you like.

- [Previous Page](https://learn.adafruit.com/dht/connecting-to-a-dhtxx-sensor.md)
- [Next Page](https://learn.adafruit.com/dht/dht-circuitpython-code.md)

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
