# Source: https://learn.adafruit.com/bmp085/using-the-bmp085.md

# Bosch BMP085 Breakout Board

## Using the BMP (API v1)

Danger: 

To use this sensor and calculate the altitude and barometric pressure, there's a lot of very hairy and unpleasant math. You can check out the math in the datasheet but really, its not intuitive or educational - its just how the sensor works. So we took care of all the icky math and wrapped it up into a nice Arduino library.   
  
[You can find the Arduino library repository on github](https://github.com/adafruit/Adafruit-BMP085-Library) To install it, click this button to download the compressed ZIP file then install it. [This guide](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use) will help you with the install process if you have never installed an Arduino library.

[Download the Adafruit_BMP085 Arduino Library (API v1)](https://github.com/adafruit/Adafruit-BMP085-Library/archive/master.zip)
The same driver is used for both the BMP085 and BMP180!

Restart the IDE  
  
Now you can run this first example sketch

```
#include "Wire.h"
#include "Adafruit_BMP085.h"
 
Adafruit_BMP085 bmp;
 
void setup() {
  Serial.begin(9600);
  bmp.begin();  
}
 
void loop() {
    Serial.print("Temperature = ");
    Serial.print(bmp.readTemperature());
    Serial.println(" *C");
 
    Serial.print("Pressure = ");
    Serial.print(bmp.readPressure());
    Serial.println(" Pa");
 
    Serial.println();
    delay(500);
}
```

Then open up the serial monitor at 9600 baud. The sketch will continuously print out the temperature in **°C** and pressure in **Pa** (Pascals). You can test that the sensor is measuring variations in temperature and pressure by placing your fingertip over the open port hole in the top of the sensor. The temperature and pressure will increase as you can see here:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/485/medium800/weather_bmp085temppress.gif?1447975839)

## Altitude Measurements
Since we know that pressure drops as we gain altitude (that's why air is so thin on mountain-tops) we can compute the current altitude knowing the pressure and temperature. Again, there's a bit of hairy math involved, [you can read about the calculations on wikipedia (where this graph is from)](http://en.wikipedia.org/wiki/Barometric_pressure "Link: http://en.wikipedia.org/wiki/Barometric\_pressure"). ![](https://cdn-learn.adafruit.com/assets/assets/000/000/486/medium800/weather_Atmospheric_Pressure_vs.png?1396763486)

With the Arduino library, we take care of that for you! Simply run this sketch which will return the current altitude based on the pressure.```
#include "Wire.h"
#include "Adafruit_BMP085.h"
 
Adafruit_BMP085 bmp;
 
void setup() {
  Serial.begin(9600);
  bmp.begin();  
}
 
void loop() {
    Serial.print("Temperature = ");
    Serial.print(bmp.readTemperature());
    Serial.println(" *C");
 
    Serial.print("Pressure = ");
    Serial.print(bmp.readPressure());
    Serial.println(" Pa");
 
    // Calculate altitude assuming 'standard' barometric
    // pressure of 1013.25 millibar = 101325 Pascal
    Serial.print("Altitude = ");
    Serial.print(bmp.readAltitude());
    Serial.println(" meters");
 
    Serial.println();
    delay(500);
}
```

Run the sketch to see the calculated altitude.![](https://cdn-learn.adafruit.com/assets/assets/000/000/487/medium800/weather_currentaltitude.gif?1447975848)

For example, according to the sensor we are 21.5m below sea level. Only problem is, I know for a fact that our current location is not below sea level! So what's wrong with the sensor? Turns out the sensor is just fine. The problem is that the pressure at sea level changes with the weather. So we need to 'normalize' the sensor, and let it know what the sea-level pressure is. You can look up the current sea level pressure on any weather site.![](https://cdn-learn.adafruit.com/assets/assets/000/000/488/medium800/currentweather.gif?1447975859)

Unfortunately there are half-dozen different units of pressure. here we see it in inches, that's technically "Mercury Inches" or "Hg Inches We need it in Pascals,[so we'll convert it!](http://www.engineeringtoolbox.com/pressure-units-converter-d_569.html)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/489/medium800/weather_conversion.gif?1447975867)

OK so that's 101,964 Pascals. Open up the&nbsp; **Examples-\>BMP085test** example from the Arduino IDE menubar and edit the line where you pass in the 'corrected' altitude.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/490/medium800/weather_correctaltitude.gif?1447975876)

Now it will print out the correct altitude! 30 meters which is a lot better.![](https://cdn-learn.adafruit.com/assets/assets/000/000/491/medium800/weather_correctedaltitude.gif?1447975885)

- [Previous Page](https://learn.adafruit.com/bmp085/using-the-bmp085-api-v2.md)
- [Next Page](https://learn.adafruit.com/bmp085/downloads.md)

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
