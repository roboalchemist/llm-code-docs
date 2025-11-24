# Source: https://learn.adafruit.com/tsl2561/python-circuitpython.md

# TSL2561 Luminosity Sensor

## Python & CircuitPython

It's easy to use the TSL2561&nbsp;sensor with Python and CircuitPython, and the&nbsp;[Adafruit CircuitPython TSL2561](https://github.com/adafruit/Adafruit_CircuitPython_TSL2561)&nbsp;module.&nbsp; This module allows you to easily write Python code that reads the luminosity&nbsp;and more from the sensor.

You can use this sensor with any CircuitPython microcontroller board or with a computer that has GPIO and Python [thanks to Adafruit\_Blinka, our CircuitPython-for-Python compatibility library](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

# CircuitPython Microcontroller Wiring

First wire up a TSL2561&nbsp;to your board exactly as shown on the previous pages for Arduino using an I2C connection. &nbsp;Here's an example of wiring a Feather M0 to the sensor with I2C:

- **Board 3V** &nbsp;to&nbsp; **sensor VIN**
- **Board GND** &nbsp;to&nbsp; **sensor GND**
- **Board SCL** &nbsp;to&nbsp; **sensor&nbsp;SCL**
- **Board SDA** &nbsp;to&nbsp; **sensor&nbsp;SDA** 

![adafruit_products_light_m0_tsl2561_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/059/036/medium640/adafruit_products_light_m0_tsl2561_bb.png?1533931616)

# Python Computer Wiring

Since there's _dozens_ of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).&nbsp;

Here's the Raspberry Pi wired with I2C:

- **Pi 3V3** to **sensor VIN**
- **Pi GND** to **sensor GND**
- **Pi SCL** to **sensor SCK**
- **Pi SDA** to **sensor SDA**

![adafruit_products_raspi_tsl2561_i2c_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/059/035/medium640/adafruit_products_raspi_tsl2561_i2c_bb.jpg?1533930811)

# CircuitPython Installation of TSL2561 Library

Next you'll need to install the&nbsp;[Adafruit CircuitPython TSL2561](https://github.com/adafruit/Adafruit_CircuitPython_TSL2561)&nbsp;library on your CircuitPython board.

First make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://github.com/adafruit/circuitpython/releases)&nbsp;for your board.

Next you'll need to install the necessary libraries&nbsp;to use the hardware--carefully follow the steps to find and install these libraries from&nbsp;[Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).&nbsp; For example the Circuit Playground Express guide has&nbsp;[a great page on how to install the library bundle](../../../../adafruit-circuit-playground-express/installing-libraries)&nbsp;for both express and non-express boards.

Remember for non-express boards like the Trinket M0, Gemma M0, and Feather/Metro M0 basic you'll need to manually install the necessary libraries from the bundle:

- **adafruit\_tsl2561.mpy**
- **adafruit\_bus\_device**

You can also download the&nbsp; **adafruit\_tsl2561.mpy** &nbsp;from&nbsp;[its releases page on Github](https://github.com/adafruit/Adafruit_CircuitPython_TSL2561/releases).

Before continuing make sure your board's lib folder or root filesystem has the&nbsp; **adafruit\_tsl2561.mpy,&nbsp;** and **&nbsp;adafruit\_bus\_device**** &nbsp; **files and folders** &nbsp;**copied over.

Next&nbsp;[connect to the board's serial REPL&nbsp;](../../../../micropython-basics-how-to-load-micropython-on-a-board/serial-terminal)so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

# Python Installation of TSL2561 Library

You'll need to install the Adafruit\_Blinka library that provides the CircuitPython support in Python. This may also require enabling I2C on your platform and verifying you are running Python 3. [Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)!

Once that's done, from your command line run the following command:

- `sudo pip3 install adafruit-circuitpython-tsl2561`

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

# CircuitPython and Python Usage

To demonstrate the usage of the sensor we'll initialize it and read the luminosity&nbsp;from the board's Python REPL. &nbsp;Run the following code to import the necessary modules and initialize the I2C connection with the sensor:

```
import board
import busio
import adafruit_tsl2561
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)
```

Now you're ready to read values from the sensor using any of these properties:

- **lux** &nbsp;- The computed light lux value measured by the sensor.
- **broadband** &nbsp;-&nbsp;The broadband channel value.
- **infrared** &nbsp;-&nbsp;The infrared channel value.
- **luminosity** -&nbsp;A 2-tuple of broadband and infrared channel values.

```
print('Lux: {}'.format(sensor.lux))
print('Broadband: {}'.format(sensor.broadband))
print('Infrared: {}'.format(sensor.infrared))
print('Luminosity: {}'.format(sensor.luminosity))
```

![](https://cdn-learn.adafruit.com/assets/assets/000/048/284/medium800/light_Screen_Shot_2017-11-16_at_6.17.04_PM.png?1510885056)

In addition there are some properties you can both read and write to change how the sensor works:

- **gain** -&nbsp;Get and set the gain of the light sensor. &nbsp;A value of 0 is low gain mode, and a value of 1 is high gain / 16x mode.
- **integration\_time** - Get and set the integration time of the sensor. &nbsp;A value 0 is 13.7ms, 1 is 101ms, 2 is 402ms, and 3 is manual mode.

```
# Set high gain mode.
sensor.gain = 1
# Set 402ms integration time.
sensor.integration_time = 2
```

![](https://cdn-learn.adafruit.com/assets/assets/000/048/285/medium800/light_Screen_Shot_2017-11-16_at_6.18.06_PM.png?1510885310)

That's all there is to using the TSL2561&nbsp;sensor with CircuitPython!

Here's a complete example of reading the light value every second. &nbsp;Save this as a **code.py** on your board and look at the output in the serial monitor:

# Full Example Code
https://github.com/adafruit/Adafruit_CircuitPython_TSL2561/blob/main/examples/tsl2561_simpletest.py

- [Previous Page](https://learn.adafruit.com/tsl2561/arduino-code.md)
- [Next Page](https://learn.adafruit.com/tsl2561/downloads.md)

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
