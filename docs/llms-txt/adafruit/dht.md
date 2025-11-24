# Source: https://learn.adafruit.com/dht.md

# DHT11, DHT22 and AM2302 Sensors

## Overview

This tutorial covers the low cost [DHT temperature & humidity sensors](http://www.adafruit.com/category/35_66 "Link: http://www.adafruit.com/category/35\_66"). These sensors are very basic and slow, but are great for hobbyists who want to do some basic data logging. The DHT sensors are made of two parts, a capacitive humidity sensor and a [thermistor](http://learn.adafruit.com/thermistor). There is also a very basic chip inside that does some analog to digital conversion and spits out a digital signal with the temperature and humidity. The digital signal is fairly easy to read using any microcontroller.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/576/medium800/weather_dhtsensors.jpg?1396764183)

## DHT11 vs DHT22

We have two versions of the DHT sensor, they look a bit similar and have the same pinout, but have different characteristics. Here are the specs:

**[DHT11](http://www.adafruit.com/products/386 "Link: http://www.adafruit.com/products/386")**

- Ultra low cost
- 3 to 5V power and I/O
- 2.5mA max current use during conversion (while requesting data)
- Good for 20-80% humidity readings with 5% accuracy
- Good for 0-50°C temperature readings ±2°C accuracy
- No more than 1 Hz sampling rate (once every second)
- Body size 15.5mm x 12mm x 5.5mm
- 4 pins with 0.1" spacing

**[DHT22](http://www.adafruit.com/products/385)/ [AM2302](https://www.adafruit.com/product/393) (Wired version)**

- Low cost
- 3 to 5V power and I/O
- 2.5mA max current use during conversion (while requesting data)
- Good for 0-100% humidity readings with 2-5% accuracy
- Good for -40 to 80°C temperature readings ±0.5°C accuracy
- No more than 0.5 Hz sampling rate (once every 2 seconds)
- Body size 15.1mm x 25mm x 7.7mm
- 4 pins with 0.1" spacing

As you can see, the&nbsp;[DHT22](http://www.adafruit.com/products/385) / [AM2302](https://www.adafruit.com/product/393) is a little more accurate and good over a slightly larger range. Both use a single digital pin and are 'sluggish' in that you can't query them more than once every second or two.

**You can pick up both the&nbsp;[DHT11](http://www.adafruit.com/products/386)&nbsp;and&nbsp;[DHT22](http://www.adafruit.com/products/385) or [AM2302](https://www.adafruit.com/product/393) from the adafruit shop!**

- [Next Page](https://learn.adafruit.com/dht/connecting-to-a-dhtxx-sensor.md)

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
- [NeoPixel Sprite Weather Display](https://learn.adafruit.com/neopixel-sprite-weather-display.md)
- [Bosch BMP085 Breakout Board](https://learn.adafruit.com/bmp085.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [PyPortal Weather Station](https://learn.adafruit.com/pyportal-weather-station.md)
- [Using LoraWAN and The Things Network with CircuitPython](https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython.md)
- [Purple Air AQI Display](https://learn.adafruit.com/purple-air-aqi-display.md)
- [Adafruit LPS25 and LPS22 Barometric Pressure and Temperature Sensors](https://learn.adafruit.com/adafruit-lps25-pressure-sensor.md)
- [Adafruit BMP280 Barometric Pressure + Temperature Sensor Breakout](https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [PyLeap CLUE Barometer](https://learn.adafruit.com/pyleap-clue-barometer.md)
- [Adafruit BMP183 SPI Barometric Pressure & Altitude Sensor](https://learn.adafruit.com/adafruit-bmp183-spi-barometric-pressure-and-altitude-sensor.md)
- [ESP8266 WiFi Weather Station with Color TFT Display](https://learn.adafruit.com/wifi-weather-station-with-tft-display.md)
- [Huzzah Weather Display](https://learn.adafruit.com/huzzah-weather-display.md)
- [Weather Display Matrix](https://learn.adafruit.com/weather-display-matrix.md)
