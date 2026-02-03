# Source: https://learn.adafruit.com/bmp085/using-the-bmp085-api-v2.md

# Bosch BMP085 Breakout Board

## Using the BMP (API v2)

This page is based on the new v2 of the BMP085 driver, which uses Adafruit's new [Unified Sensor Driver](http://learn.adafruit.com/using-the-adafruit-unified-sensor-driver/introduction). The driver provides better support for altitude calculations, and makes it easy to switch between the BMP085 and any other supported pressure sensor in your projects.  
  
If you haven't already done so, you'll need to install the [Adafrut\_Sensor library](https://github.com/adafruit/Adafruit_Sensor) on your system as well, since Adafruit\_BMP085 relies on this library to generate the sensor data in a universal manner.

# Using the BMP085 / BMP180

To use this sensor and calculate the altitude and barometric pressure, there's a lot of very hairy and unpleasant math. You can check out the math in the datasheet but really, its not intuitive or educational - its just how the sensor works. So we took care of all the icky math and wrapped it up into a nice Arduino library.   
  
[You can find the Arduino library repository on github](https://github.com/adafruit/Adafruit_BMP085_Unified "Link: https://github.com/adafruit/Adafruit\_BMP085\_Unified") To install it, click this button to download the compressed ZIP file then install it. [This guide](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use) will help you with the install process if you have never installed an Arduino library.

[Download the Adafruit_BMP085 Arduino Library (API v2)](https://github.com/adafruit/Adafruit_BMP085_Unified/archive/master.zip)
The same code is used for both the BMP085 and BMP180 (they are compatible!)

Restart the IDE  
  
Now you can run this first example sketch

```
#include &lt;Wire.h&gt;
#include &lt;Adafruit_Sensor.h&gt;
#include &lt;Adafruit_BMP085_U.h&gt;
   
Adafruit_BMP085_Unified bmp = Adafruit_BMP085_Unified(10085);

void setup(void) 
{
  Serial.begin(9600);
  Serial.println("Pressure Sensor Test"); Serial.println("");
  
  /* Initialise the sensor */
  if(!bmp.begin())
  {
    /* There was a problem detecting the BMP085 ... check your connections */
    Serial.print("Ooops, no BMP085 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
}

void loop(void) 
{
  /* Get a new sensor event */ 
  sensors_event_t event;
  bmp.getEvent(&amp;event);
 
  /* Display the results (barometric pressure is measure in hPa) */
  if (event.pressure)
  {
    /* Display atmospheric pressure in hPa */
    Serial.print("Pressure: "); Serial.print(event.pressure); Serial.println(" hPa");
  }
  else
  {
    Serial.println("Sensor error");
  }
  delay(250);
}
```

Then open up the serial monitor at 9600 baud. The sketch will continuously print out the pressure in **hPa** (hectoPascals). You can test that the sensor is measuring variations in pressure by placing your fingertip over the open port hole in the top of the sensor. The pressure will increase as you can see here:

![](https://cdn-learn.adafruit.com/assets/assets/000/009/115/medium800/weather_PressureBMP085.png?1396883445)

## Altitude Measurements
Since we know that pressure drops as we gain altitude (that's why air is so thin on mountain-tops) we can compute the current altitude knowing the pressure and temperature. Again, there's a bit of hairy math involved, [you can read about the calculations on wikipedia (where this graph is from)](http://en.wikipedia.org/wiki/Barometric_pressure). ![](https://cdn-learn.adafruit.com/assets/assets/000/009/116/medium800/weather_atmosphericpressure.png?1396883473)

With the Arduino library, we take care of that for you! Simply **update the 'void loop()' function above with the code below to get the altitude based on the pressure and temperature:**

```
void loop(void) 
{
  /* Get a new sensor event */ 
  sensors_event_t event;
  bmp.getEvent(&amp;event);
 
  /* Display the results (barometric pressure is measure in hPa) */
  if (event.pressure)
  {
    /* Display atmospheric pressue in hPa */
    Serial.print("Pressure:    ");
    Serial.print(event.pressure);
    Serial.println(" hPa");
    
    /* Calculating altitude with reasonable accuracy requires pressure    *
     * sea level pressure for your position at the moment the data is     *
     * converted, as well as the ambient temperature in degress           *
     * celcius.  If you don't have these values, a 'generic' value of     *
     * 1013.25 hPa can be used (defined as SENSORS_PRESSURE_SEALEVELHPA   *
     * in sensors.h), but this isn't ideal and will give variable         *
     * results from one day to the next.                                  *
     *                                                                    *
     * You can usually find the current SLP value by looking at weather   *
     * websites or from environmental information centers near any major  *
     * airport.                                                           *
     *                                                                    *
     * For example, for Paris, France you can check the current mean      *
     * pressure and sea level at: http://bit.ly/16Au8ol                   */
     
    /* First we get the current temperature from the BMP085 */
    float temperature;
    bmp.getTemperature(&amp;temperature);
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" C");

    /* Then convert the atmospheric pressure, SLP and temp to altitude    */
    /* Update this next line with the current SLP for better results      */
    float seaLevelPressure = SENSORS_PRESSURE_SEALEVELHPA;
    Serial.print("Altitude:    "); 
    Serial.print(bmp.pressureToAltitude(seaLevelPressure,
                                        event.pressure,
                                        temperature)); 
    Serial.println(" m");
    Serial.println("");
  }
  else
  {
    Serial.println("Sensor error");
  }
  delay(1000);
}
```

Run the sketch to see the calculated altitude.

![](https://cdn-learn.adafruit.com/assets/assets/000/009/117/medium800/weather_outputresults.png?1396883489)

The data above is reasonably close to what I'd expect at my location, but we can improve the accuracy by changing the reference sea level pressure, which will change depending on the weather conditions. **Every 1 hPa that we are off on the sea level pressure equals about 8.5 m of error in the altitude calculations!**  
  
Many weather sites, (particularly near major airports) will provide pressure readings. If you happened to be near Paris, France, for example, you might look up the [current air pressure at Charles de Gaulle airport](http://pt.weather-forecast.com/weather-stations/Charles-De-Gaulle-International-Airport), which we can see is 1009 hPa (a meaningful difference from the generoc 1013.25 hPa value we are plugging in via the **SENSORS\_PRESSURE\_SEALEVELHPA** macro):

![](https://cdn-learn.adafruit.com/assets/assets/000/009/118/medium800/weather_presure_cdg.png?1396883516)

Updating the following line to 1009 will give us a more accurate altitude:

```
float seaLevelPressure = 1009;
```

Danger: 

This now gives us the following results, which shows that calibrating for your local conditions is often worthwhile when working with low altitudes!

![](https://cdn-learn.adafruit.com/assets/assets/000/009/119/medium800/weather_Pressure_new.png?1396883528)

Just be careful looking for local mean pressure at sea level values, since the functions in the driver are expecting hPa units, not one of the dozens of other values you may encounter, but you should be able to [convert anything you find to hPa](http://www.engineeringtoolbox.com/pressure-units-converter-d_569.html) which is a standard SI unit.

- [Previous Page](https://learn.adafruit.com/bmp085/wiring-the-bmp085.md)
- [Next Page](https://learn.adafruit.com/bmp085/using-the-bmp085.md)

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
