# Source: https://learn.adafruit.com/dht/connecting-to-a-dhtxx-sensor.md

# DHT11, DHT22 and AM2302 Sensors

## Connecting to a DHTxx Sensor

Luckily it is trivial to connect to these sensors, they have fairly long 0.1"-pitch pins so you can plug them into any breadboard, perfboard or similar.![](https://cdn-learn.adafruit.com/assets/assets/000/000/577/medium800/weather_dhtbreadboard.jpg?1396764191)

Likewise, it is fairly easy to connect up to the DHT sensors. They have four pins

1. **VCC** - red wire Connect to 3.3 - 5V power. Sometime 3.3V power isn't enough in which case try 5V power.
2. **Data out -** white or yellow wire  
3. Not connected
4. **Ground -** black wire  

Simply ignore pin 3, it's not used. You will want to place a 10 Kohm resistor between VCC and the data pin, to act as a medium-strength pull up on the data line. The Arduino has built in pullups you can turn on but they're very weak, about 20-50K

Info: 

This diagram shows how we will connect for the testing sketch. Connect data to pin 2, you can change it later to any pin.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/578/medium800/weather_dhtwiring.gif?1447976206)

If you have an AM2302

- [Previous Page](https://learn.adafruit.com/dht/overview.md)
- [Next Page](https://learn.adafruit.com/dht/using-a-dhtxx-sensor-with-arduino.md)

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
