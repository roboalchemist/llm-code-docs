# Source: https://learn.adafruit.com/tsl2561/arduino-code.md

# TSL2561 Luminosity Sensor

## Arduino Code

To use this sensor and calculate Lux, there's a lot of very hairy and unpleasant math. [You can check out the math in the datasheet](http://learn.adafruit.com/tsl2561/downloads) but really, its not intuitive or educational - its just how the sensor works. So we took care of all the icky math and wrapped it up into a nice Arduino library.

# Install Adafruit\_TSL2561 library

To begin reading sensor data, you will need to [install the Adafruit\_TSL2561 library (code on our github repository)](https://github.com/adafruit/Adafruit_TSL2561). It is available from the Arduino library manager so we recommend using that.

From the IDE open up the library manager...

![](https://cdn-learn.adafruit.com/assets/assets/000/050/310/medium800/adafruit_products_managelib.png?1516383384)

And type in **adafruit tsl2561** to locate the library. Click **Install**

![](https://cdn-learn.adafruit.com/assets/assets/000/050/312/medium800/adafruit_products_tsl256.png?1516383468)

# Install Adafruit\_Sensor

The TSL2561 library uses the [Adafruit\_Sensor support backend](https://github.com/adafruit/Adafruit_Sensor) so that readings can be normalized between sensors.

Search the library manager for **Adafruit Unified Sensor** and install that too (you may have to scroll a bit)

![](https://cdn-learn.adafruit.com/assets/assets/000/050/311/medium800/adafruit_products_sensor.png?1516383410)

Now you can run the **File-\>Examples-\>Adafruit\_TSL2561-\>sensorapi** example program which will read and calculate the lux readings for you.

Open up the serial monitor at 9600 baud to see the measurements. Use a lamp or your hand to illuminate/shade the sensor to see the values change.

![](https://cdn-learn.adafruit.com/assets/assets/000/004/405/medium800/light_tsl2561output.png?1396812008)

The library is fairly simple to use. The first line of code in the example is the 'constructor' where you can supply the **I2C ADDR** (in case you want to change it), and a unique ID to attach to this sensor (you can just leave this to the default value of 12345 for now). By modifying the I2C address we can have up to three TSL2561 sensors connected on the same board:

```
// The address will be different depending on whether you leave
// the ADDR pin float (addr 0x39), or tie it to ground or vcc. In those cases
// use TSL2561_ADDR_LOW (0x29) or TSL2561_ADDR_HIGH (0x49) respectively
Adafruit_TSL2561 tsl = Adafruit_TSL2561(TSL2561_ADDR_FLOAT, 12345);
```

Next up, you will want to configure the sensor with the **gain** and **integration time**.   
  
You can have either a gain of 0 (no extra gain, good in low light situations) or a gain of 16 which will boost the light considerably in dim situations.  
  
You can also change the integration time, which is how long it will collect light data for. The longer the integration time, the more precision the sensor has when collecting light samples.  
  
New to v2.0 of the driver, there is also an **auto-gain** option that is useful when measuring in mixed lighting-situations. This will automatically enable or disable the gain depending on the light level. This is still an experimental feature and the trigger levels to switch may need to be tweaked, but this should be useful to collect light both indoors and outdoors without having to change the code yourself.

```
/**************************************************************************/
/*
    Configures the gain and integration time for the TSL2561
*/
/**************************************************************************/
void configureSensor(void)
{
  /* You can also manually set the gain or enable auto-gain support */
  // tsl.setGain(TSL2561_GAIN_1X);      /* No gain ... use in bright light to avoid sensor saturation */
  // tsl.setGain(TSL2561_GAIN_16X);     /* 16x gain ... use in low light to boost sensitivity */
  tsl.enableAutoRange(true);          /* Auto-gain ... switches automatically between 1x and 16x */
  
  /* Changing the integration time gives you better sensor resolution (402ms = 16-bit data) */
  tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);      /* fast but low resolution */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_101MS);  /* medium resolution and speed   */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_402MS);  /* 16-bit data but slowest conversions */

  /* Update these values depending on what you've set above! */  
  Serial.println("------------------------------------");
  Serial.print  ("Gain:         "); Serial.println("Auto");
  Serial.print  ("Timing:       "); Serial.println("13 ms");
  Serial.println("------------------------------------");
}
```

By default, the driver will return light in standard SI lux units, which are a result of some complex calculations based on both photo diodes on the TSL2561 (one for full spectrum and one for IR). The sensitivity of the two diodes can be seen in the chart below:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/586/medium800/light_tsl2561spectrum.gif?1447976265)

When you're ready to get your measurement in standard SI lux units, simply call **getEvent** with a reference to the 'sensors\_event\_t' object where the sensor data will be stored. This example assumes we are using the 'tsl' instance of Adafruit\_TSL2561 at the top of the example code:

```
  /* Get a new sensor event */ 
  sensors_event_t event;
  tsl.getEvent(&amp;event);
 
  /* Display the results (light is measured in lux) */
  if (event.light)
  {
    Serial.print(event.light); Serial.println(" lux");
  }
  else
  {
    /* If event.light = 0 lux the sensor is probably saturated
       and no reliable data could be generated! */
    Serial.println("Sensor overload");
  }

```

This function will return a reading in SI lux units, which is probably the easiest unit to understand when working with light.  
  
If you wish to manually read the individual photo diodes, though, you can still do this in the latest library by calling the **getLuminosity** function, and passing in two variables where the sensor data will be stored:

```
uint16_t broadband = 0;
uint16_t infrared = 0;

/* Populate broadband and infrared with the latest values */
getLuminosity (&amp;broadband, &amp;infrared);
```

That's it! The example should be easy to understand and work into your own projects from here!

- [Previous Page](https://learn.adafruit.com/tsl2561/wiring-the-tsl2561-sensor.md)
- [Next Page](https://learn.adafruit.com/tsl2561/python-circuitpython.md)

## Featured Products

### Adafruit TSL2561 Digital Luminosity/Lux/Light Sensor Breakout

[Adafruit TSL2561 Digital Luminosity/Lux/Light Sensor Breakout](https://www.adafruit.com/product/439)
The TSL2561 luminosity sensor is an advanced digital light sensor, ideal for use in a wide range of light situations. Compared to low cost CdS cells, this sensor is more precise, allowing for exact lux calculations and can be configured for different gain/timing ranges to detect light ranges...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/439)
[Related Guides to the Product](https://learn.adafruit.com/products/439/guides)
### Flora Lux Sensor - TSL2561 Light Sensor

[Flora Lux Sensor - TSL2561 Light Sensor](https://www.adafruit.com/product/1246)
Add light-reactive sensing to your wearable Flora project with this high precision Lux sensor. The TSL2561 luminosity sensor is an advanced digital light sensor, ideal for use in a wide range of light situations. Compared to low cost CdS cells, this sensor is more precise, allowing for exact...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1246)
[Related Guides to the Product](https://learn.adafruit.com/products/1246/guides)

## Related Guides

- [Adafruit TSC2046 SPI Resistive Touch Screen Controller](https://learn.adafruit.com/adafruit-tsc2046-spi-resistive-touch-screen-controller.md)
- [PM2.5 Air Quality Sensor](https://learn.adafruit.com/pm25-air-quality-sensor.md)
- [Adafruit Metro M7 with microSD](https://learn.adafruit.com/adafruit-metro-m7-microsd.md)
- [Adafruit VL53L4CX Time of Flight Distance Sensor](https://learn.adafruit.com/adafruit-vl53l4cx-time-of-flight-distance-sensor.md)
- [LED Glasses Custom Animated Graphics with Sprites](https://learn.adafruit.com/led-glasses-custom-animated-graphics-with-sprites.md)
- [WiFi Music Alert Box ](https://learn.adafruit.com/wifi-music-alert-box.md)
- [Adafruit Stepper + DC Motor FeatherWing](https://learn.adafruit.com/adafruit-stepper-dc-motor-featherwing.md)
- [Adafruit PyRuler](https://learn.adafruit.com/adafruit-pyruler.md)
- [Adafruit PDM Microphone Breakout](https://learn.adafruit.com/adafruit-pdm-microphone-breakout.md)
- [Adafruit DC Power BFF](https://learn.adafruit.com/adafruit-dc-power-bff.md)
- [Adafruit Sensirion SHTC3 - Temperature & Humidity Sensor Breakout](https://learn.adafruit.com/adafruit-sensirion-shtc3-temperature-humidity-sensor.md)
- [Programmable 12v Outdoor Cafe Lights](https://learn.adafruit.com/programmable-12v-outdoor-cafe-lights.md)
- [Adafruit AS7341 10-Channel Light / Color Sensor Breakout](https://learn.adafruit.com/adafruit-as7341-10-channel-light-color-sensor-breakout.md)
- [Adafruit STSPIN220 Stepper Motor Driver Breakout Board](https://learn.adafruit.com/adafruit-stspin220-stepper-motor-driver-breakout-board.md)
- [Adafruit PiCowbell CAN Bus for Pico](https://learn.adafruit.com/adafruit-picowbell-can-bus-for-pico.md)
