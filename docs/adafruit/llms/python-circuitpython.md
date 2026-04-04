# Source: https://learn.adafruit.com/character-lcds/python-circuitpython.md

# Source: https://learn.adafruit.com/tsl2561/python-circuitpython.md

# Source: https://learn.adafruit.com/thermocouple/python-circuitpython.md

# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/python-circuitpython.md

# Adafruit INA219 Current Sensor Breakout

## Python & CircuitPython

It's easy to use the INA219&nbsp;sensor with Python and CircuitPython, and the&nbsp;[Adafruit CircuitPython INA219](https://github.com/adafruit/Adafruit_CircuitPython_INA219)&nbsp;module.&nbsp; This module allows you to easily write Python code that reads the current&nbsp;and more from the sensor.

You can use this sensor with any CircuitPython microcontroller board or with a computer that has GPIO and Python [thanks to Adafruit\_Blinka, our CircuitPython-for-Python compatibility library](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

# CircuitPython Microcontroller Wiring

First wire up a INA219&nbsp;to your board exactly as shown on the previous pages for Arduino using an I2C interface. In addition connect some load to measure the current from in series to the sensor's **Vin-** and **Vin+** pins as [mentioned on the wiring page](../../../../adafruit-ina219-current-sensor-breakout/wiring#connect-to-the-circuit).

Here is an example of the STEMMA QT version connected to a Feather M4:

- **Board 3V** &nbsp;to&nbsp;**sensor VIN (red wire)**
- **Board GND** &nbsp;to&nbsp;**sensor GND (black wire)**
- **Board SCL** &nbsp;to&nbsp;**sensor SCL (yellow wire)**
- **Board SDA** &nbsp;to&nbsp;**sensor SDA (blue wire)**
- Connect **Vin+** to the **positive terminal of the power supply for the circuit under test**
- Connect **Vin-** to the **positive terminal or lead of the load**

![adafruit_products_INA219QT_Feather_STEMMA_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/104/422/medium640/adafruit_products_INA219QT_Feather_STEMMA_bb.jpg?1631131638)

![adafruit_products_INA219QT_Feather_breadboard_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/104/423/medium640/adafruit_products_INA219QT_Feather_breadboard_bb.jpg?1631131675)

Here's an example of the original version of the sensor wired up to a Feather M0:

- **Board 3V** &nbsp;to&nbsp; **sensor&nbsp;Vcc**
- **Board GND** &nbsp;to&nbsp; **sensor GND**
- **Board SCL** &nbsp;to&nbsp; **sensor&nbsp;SCL**
- **Board SDA** &nbsp;to&nbsp; **sensor&nbsp;SDA**

![adafruit_products_m0_ina219_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/048/265/medium640/adafruit_products_m0_ina219_bb.png?1534094899)

# Python Computer Wiring

Since there's _dozens_ of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).&nbsp;

In addition connect some load to measure the current from in series to the sensor's **Vin-** and **Vin+** pins as [mentioned on the wiring page](../../../../adafruit-ina219-current-sensor-breakout/wiring#connect-to-the-circuit).

Here's the Raspberry Pi wired to the STEMMA QT version of the sensor:

- **Pi 3V** &nbsp;to&nbsp;**sensor VIN (red wire)**
- **Pi GND** &nbsp;to&nbsp;**sensor GND (black wire)**
- **Pi SCL** &nbsp;to&nbsp;**sensor SCL (yellow wire)**
- **Pi SDA** &nbsp;to&nbsp;**sensor SDA (blue wire)**
- Connect **Vin+** to the **positive terminal of the power supply for the circuit under test**
- Connect **Vin-** to the **positive terminal or lead of the load**

![adafruit_products_INA219QT_RasPi_STEMMA_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/104/424/medium640/adafruit_products_INA219QT_RasPi_STEMMA_bb.jpg?1631131838)

![adafruit_products_INA219QT_RasPi_breadboard_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/104/426/medium640/adafruit_products_INA219QT_RasPi_breadboard_bb.jpg?1631131899)

Here's the Raspberry Pi wired to the original version of the sensor with I2C:

- **Pi 3V3** to **sensor Vcc**
- **Pi GND** to **sensor Gnd**
- **Pi SCL** to **sensor Scl**
- **Pi SDA** to **sensor Sda**

![adafruit_products_raspi_ina219_i2c_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/059/052/medium640/adafruit_products_raspi_ina219_i2c_bb.jpg?1534095144)

# CircuitPython Installation of INA219 Library

Next you'll need to install the&nbsp;[Adafruit CircuitPython INA219](https://github.com/adafruit/Adafruit_CircuitPython_INA219)&nbsp;library on your CircuitPython board.

First make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://github.com/adafruit/circuitpython/releases)&nbsp;for your board.

Next you'll need to install the necessary libraries&nbsp;to use the hardware--carefully follow the steps to find and install these libraries from&nbsp;[Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).&nbsp; For example the Circuit Playground Express guide has&nbsp;[a great page on how to install the library bundle](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries)&nbsp;for both express and non-express boards.

Remember for non-express boards like the Trinket M0, Gemma M0, and Feather/Metro M0 basic you'll need to manually install the necessary libraries from the bundle:

- **adafruit\_ina219.mpy**
- **adafruit\_bus\_device**

Before continuing make sure your board's **lib** folder or root filesystem has the&nbsp; **adafruit\_ina219.mpy,&nbsp;** and **&nbsp;adafruit\_bus\_device**** &nbsp; **files and folders** &nbsp;**copied over.

Warning: Before continuing make sure your board's lib folder has the adafruit\_ina219.mpy, and adafruit\_bus_device files and folders copied over.

Next[&nbsp;connect to the board's serial REPL](https://learn.adafruit.com/welcome-to-circuitpython/the-repl) so you are at the CircuitPython&nbsp; **\>\>\>** prompt.

# Python Installation of INA219 Library

You'll need to install the Adafruit\_Blinka library that provides the CircuitPython support in Python. This may also require enabling I2C on your platform and verifying you are running Python 3. [Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)!

Once that's done, from your command line run the following command:

- `sudo pip3 install adafruit-circuitpython-ina219`

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

# CircuitPython & Python Usage

To demonstrate the usage of the sensor we'll initialize it and read the&nbsp;current&nbsp;and more from the board's Python REPL. &nbsp;Run the following code to import the necessary modules and initialize the I2C connection with the sensor:

```
import board
import busio
import adafruit_ina219
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ina219.INA219(i2c)
```

Now you're ready to read values from the sensor using any of these functions:

- **shunt\_voltage** -&nbsp;The shunt voltage in volts.
- **bus\_voltage** - The bus voltage in volts.
- **current** -&nbsp;The current in milliamps.

```
print("Bus Voltage:   {} V".format(ina219.bus_voltage))
print("Shunt Voltage: {} mV".format(ina219.shunt_voltage / 1000))
print("Current:       {} mA".format(ina219.current))
```

That's all there is to using the INA219 with CircuitPython!

Here's a full example to print the voltage and current every second. Save this as **code.py** on your board's filesystem and check the output from the serial REPL.

# Full Example Code
https://github.com/adafruit/Adafruit_CircuitPython_INA219/blob/main/examples/ina219_simpletest.py

If you have more than one sensor at different I2C addresses (adjusted per the Addressing page), use the following syntax, using the addresses you chose:

```python
ina219a = INA219(i2c_bus, 0x40)
ina219b = INA219(i2c_bus, 0x41)
```

- [Previous Page](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/library-reference.md)
- [Next Page](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/wippersnapper.md)

## Featured Products

### INA219  High Side DC Current Sensor Breakout - 26V ±3.2A Max

[INA219  High Side DC Current Sensor Breakout - 26V ±3.2A Max](https://www.adafruit.com/product/904)
This breakout board will solve all your power-monitoring problems. Instead of struggling with two multimeters, you can just use the handy INA219 chip on this breakout to both measure both the high side voltage and DC current draw over I2C with ±1% precision.

**Please...**

In Stock
[Buy Now](https://www.adafruit.com/product/904)
[Related Guides to the Product](https://learn.adafruit.com/products/904/guides)
### STEMMA QT / Qwiic JST SH 4-pin Cable - 100mm Long

[STEMMA QT / Qwiic JST SH 4-pin Cable - 100mm Long](https://www.adafruit.com/product/4210)
This 4-wire cable is a little over 100mm / 4" long and fitted with JST-SH female 4-pin connectors on both ends. Compared with the chunkier JST-PH these are 1mm pitch instead of 2mm, but still have a nice latching feel, while being easy to insert and remove.

<a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/4210)
[Related Guides to the Product](https://learn.adafruit.com/products/4210/guides)
### STEMMA QT / Qwiic JST SH 4-pin to Premium Male Headers Cable

[STEMMA QT / Qwiic JST SH 4-pin to Premium Male Headers Cable](https://www.adafruit.com/product/4209)
This 4-wire cable is a little over 150mm / 6" long and fitted with JST-SH female 4-pin connectors on one end and premium Dupont male headers on the other. Compared with the chunkier JST-PH these are 1mm pitch instead of 2mm, but still have a nice latching feel, while being easy to insert...

Out of Stock
[Buy Now](https://www.adafruit.com/product/4209)
[Related Guides to the Product](https://learn.adafruit.com/products/4209/guides)
### Premium Male/Male Jumper Wires - 40 x 6" (150mm)

[Premium Male/Male Jumper Wires - 40 x 6" (150mm)](https://www.adafruit.com/product/758)
Handy for making wire harnesses or jumpering between headers on PCB's. These premium jumper wires are 6" (150mm) long and come in a 'strip' of 40 (4 pieces of each of ten rainbow colors). They have 0.1" male header contacts on either end and fit cleanly next to each other...

Out of Stock
[Buy Now](https://www.adafruit.com/product/758)
[Related Guides to the Product](https://learn.adafruit.com/products/758/guides)
### Full Sized Premium Breadboard - 830 Tie Points

[Full Sized Premium Breadboard - 830 Tie Points](https://www.adafruit.com/product/239)
This is a 'full-size' premium quality breadboard, 830 tie points. Good for small and medium projects. It's 2.2" x 7" (5.5 cm x 17 cm) with a standard double-strip in the middle and two power rails on both sides. You can pull the power rails off easily to make the...

In Stock
[Buy Now](https://www.adafruit.com/product/239)
[Related Guides to the Product](https://learn.adafruit.com/products/239/guides)
### Adafruit INA219 FeatherWing

[Adafruit INA219 FeatherWing](https://www.adafruit.com/product/3650)
The **INA219 FeatherWing** makes power-monitoring problems a thing of the past. Instead of struggling with two multimeters, you can just use the handy INA219&nbsp;chip on this breakout to&nbsp;measure both the high side voltage and DC current draw over I2C with 1% precision....

In Stock
[Buy Now](https://www.adafruit.com/product/3650)
[Related Guides to the Product](https://learn.adafruit.com/products/3650/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [WiFi Controlled Mobile Robot](https://learn.adafruit.com/wifi-controlled-mobile-robot.md)
- [Arduino Lesson 14. Servo Motors](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [Adafruit AirLift Shield - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-shield-esp32-wifi-co-processor.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [2.2" TFT Display](https://learn.adafruit.com/2-2-tft-display.md)
- [LED Lightbox](https://learn.adafruit.com/led-lightbox.md)
- [Arduino Prototyping Mounting Plate](https://learn.adafruit.com/arduino-prototyping-mounting-plate.md)
- [How to Choose a Microcontroller](https://learn.adafruit.com/how-to-choose-a-microcontroller.md)
- [Arduino Lesson 16. Stepper Motors](https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
