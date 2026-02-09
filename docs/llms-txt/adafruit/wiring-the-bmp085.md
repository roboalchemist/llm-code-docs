# Source: https://learn.adafruit.com/bmp085/wiring-the-bmp085.md

# Bosch BMP085 Breakout Board

## Wiring the BMP

Since the BMP085 is a i2c sensor, its very easy to wire up. We'll be using an Arduino as an example but any microcontroller with i2c can be used. To start using with a solderless breadboard, we need to solder the header pins onto the breakout board.

We suggest plugging the header into a breadboard so the long pins are in the breadboard, and then laying the BMP085 breakout board on top. The photos show a v1 BMP085 sensor but this part is identical for both versions!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/481/medium800/weather_bmp085placed.jpg?1396763416)

Then solder all of the pins!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/482/medium800/weather_bmp085soldering.jpg?1396763422)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/483/medium800/weather_bmp085done.jpg?1396763429)

That's it! Now we can wire the board up to the microcontroller.![](https://cdn-learn.adafruit.com/assets/assets/000/000/484/medium800/weather_bmp085_bb.png?1396763462)

Connect the **VCC** pin to a **3.3V** power source. The V1 of the sensor breakout cannot be used with anything higher than 3.3V so don't use a 5V supply! V2 of the sensor board has a 3.3V regulator so you can connect it to either 3.3V or 5V if you do not have 3V available.

Connect **GND** to the ground pin.

Connect the **i2c SCL clock** pin to your i2c clock pin. On the classic Arduino Uno/Duemilanove/Diecimila/etc this is **Analog pin #5**

Connect the **i2c SDA data** pin to your i2c data pin. On the classic Arduino Uno/Duemilanove/Diecimila/etc this is **Analog pin #4**

Unfortunately, the i2c lines on most microcontrollers are fixed so you're going to have to stick with those pins.

You don't need to connect the **XCLR** (reset) or **EOC** (end-of-conversion) pins. If you need to speed up your conversion time, you can use the EOC as a indicator - in our code we just hang out and wait the maximum time possible.

- [Previous Page](https://learn.adafruit.com/bmp085/overview.md)
- [Next Page](https://learn.adafruit.com/bmp085/using-the-bmp085-api-v2.md)

## Featured Products

### BMP180 Barometric Pressure/Temperature/Altitude Sensor- 5V ready

[BMP180 Barometric Pressure/Temperature/Altitude Sensor- 5V ready](https://www.adafruit.com/product/1603)
This precision sensor from Bosch is the best low-cost sensing solution for measuring barometric pressure and temperature. Because pressure changes with altitude you can also use it as an altimeter! The sensor is soldered onto a PCB with a 3.3V regulator, I2C level shifter and pull-up resistors...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1603)
[Related Guides to the Product](https://learn.adafruit.com/products/1603/guides)
### BMP085 Barometric Pressure/Temperature/Altitude Sensor- 5V ready

[BMP085 Barometric Pressure/Temperature/Altitude Sensor- 5V ready](https://www.adafruit.com/product/391)
This precision sensor from Bosch is the best low-cost sensing solution for measuring barometric pressure and temperature. Because pressure changes with altitude you can also use it as an altimeter! The sensor is soldered onto a PCB with a 3.3V regulator, I2C level shifter and pull-up resistors...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/391)
[Related Guides to the Product](https://learn.adafruit.com/products/391/guides)
### Adafruit 10-DOF IMU Breakout - L3GD20H + LSM303 + BMP180

[Adafruit 10-DOF IMU Breakout - L3GD20H + LSM303 + BMP180](https://www.adafruit.com/product/1604)
This inertial-measurement-unit combines 3 of the best quality sensors available on the market to give you 11 axes of data: 3 axes of accelerometer data, 3 axes gyroscopic, 3 axes magnetic (compass), barometric pressure/altitude and temperature. We tested many different 'combination'...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1604)
[Related Guides to the Product](https://learn.adafruit.com/products/1604/guides)

## Related Guides

- [Adafruit NeoKey 5x6 Ortho Snap-Apart](https://learn.adafruit.com/adafruit-neokey-5x6-ortho-snap-apart.md)
- [No-Code DS18B20 Temperature Sensor with WipperSnapper](https://learn.adafruit.com/using-ds18b20-temperature-sensor-with-wippersnapper.md)
- [Storage humidity and temperature monitor](https://learn.adafruit.com/storage-humidity-and-temperature-monitor.md)
- [4x4 Rotary Encoder MIDI Messenger](https://learn.adafruit.com/4x4-rotary-encoder-midi-messenger.md)
- [Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor.md)
- [CircuitPython BLE Multi-Temperature Monitoring](https://learn.adafruit.com/circuitpython-multi-temperature-ble-monitoring.md)
- [Adafruit CAN Pal](https://learn.adafruit.com/adafruit-can-pal.md)
- [Huzzah Weather Display](https://learn.adafruit.com/huzzah-weather-display.md)
- [Adafruit AHT20 Temperature & Humidity Sensor](https://learn.adafruit.com/adafruit-aht20.md)
- [Adafruit LPS33/LPS35 Water Resistant Pressure Sensor](https://learn.adafruit.com/lps35hw-water-resistant-pressure-sensor.md)
- [DHT Humidity Sensing on Raspberry Pi or Beaglebone Black with GDocs Logging](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.md)
- [Adafruit STEMMA Non-Latching Mini Relay](https://learn.adafruit.com/adafruit-stemma-non-latching-mini-relay.md)
- [IoT Temperature Logger with Analog Devices ADT7410, Feather and Adafruit IO](https://learn.adafruit.com/iot-temperature-logger-with-arduino-and-adafruit-io.md)
- [Adafruit OV5640 Camera Breakouts](https://learn.adafruit.com/adafruit-ov5640-camera-breakout.md)
- [Adafruit SI1145 Breakout Board - UV index / IR / Visible Sensor](https://learn.adafruit.com/adafruit-si1145-breakout-board-uv-ir-visible-sensor.md)
