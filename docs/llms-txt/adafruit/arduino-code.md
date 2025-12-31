# Source: https://learn.adafruit.com/2-2-tft-display/arduino-code.md

# Source: https://learn.adafruit.com/12mm-led-pixels/arduino-code.md

# Source: https://learn.adafruit.com/character-lcds/arduino-code.md

# Source: https://learn.adafruit.com/tsl2561/arduino-code.md

# Source: https://learn.adafruit.com/photocells/arduino-code.md

# Source: https://learn.adafruit.com/thermocouple/arduino-code.md

# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/arduino-code.md

# Source: https://learn.adafruit.com/12mm-led-pixels/arduino-code.md

# Source: https://learn.adafruit.com/character-lcds/arduino-code.md

# Source: https://learn.adafruit.com/tsl2561/arduino-code.md

# Source: https://learn.adafruit.com/photocells/arduino-code.md

# Source: https://learn.adafruit.com/thermocouple/arduino-code.md

# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/arduino-code.md

# Source: https://learn.adafruit.com/thermocouple/arduino-code.md

# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/arduino-code.md

# Source: https://learn.adafruit.com/thermocouple/arduino-code.md

# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/arduino-code.md

# Source: https://learn.adafruit.com/thermocouple/arduino-code.md

# MAX31855 Thermocouple

## Arduino Code

If you're using an AD595 interface chip, you can simply connect the voltage output to an analog input on your microcontroller and do some basic math to multiply the 10 mV/°C input into numerical output.![](https://cdn-learn.adafruit.com/assets/assets/000/000/366/medium800/temperature_attached.jpg?1396762479)

If you're planning to use the MAX6675/MAX31855, there's a little more work to be done. First off, Vin and GND must connect to a 3-5V supply. Then the three data pins must connect to digital IO pins:

- **CLK&nbsp;** (clock) is an input to the MAX6675/MAX31855 (output from microcontroller) which indicates when to present another bit of data
- **DO&nbsp;** (data out) is an output from the MAX6675/MAX31855 (input to the microcontroller) which carries each bit of data
- **CS&nbsp;** (chip select) is an input to the MAX6675/MAX31855 (output from the microcontroller) which tells the chip when its time to read the thermocouple and output more data.

In the beginning of our sketches, we define these pins. For our examples **DO** connects to digital 3, **CS** connects to digital 4, and **CLK** connects to pin 5  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/303/medium800/temperature_cap.jpg?1396770831)

If you are using the MAX31855 v1.0 in a noisy environment, you may need to add a 0.01uF capacitor across the thermocouple leads.  
  
The MAX31855 does not support grounded thermocouples - if the sensor touches ground the chip will return an error

# Arduino Library

If you have an older MAX6675 breakout, download the&nbsp; **Adafruit MAX6675&nbsp;** library from the Arduino library manager.

If you have the newer MAX31855 breakout, download the&nbsp; **Adafruit MAX31855** library from the Arduino library manager.

Open up the Arduino library manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/084/483/medium800/temperature___humidity_1library_manager_menu.png?1574049141)

If you have a MAX6675 breakout, search for the&nbsp; **MAX6675&nbsp;** library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/484/medium800/temperature___humidity_max6675.png?1574049287)

If you have the MAX31855 breakout, search for the&nbsp; **Adafruit MAX31855&nbsp;** library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/486/medium800/temperature___humidity_max31855.png?1574049373)

Open up the **File**** -\> ****Examples-\>MAX6675/Adafruit\_MAX31855**** -\> ****serialthermocouple** sketch and upload it to your Arduino. Once uploaded, open up the serial port monitor to display the current temperatures in both Celsius and Fahrenheit.

We also have a great tutorial on Arduino library installation at:  
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")

![](https://cdn-learn.adafruit.com/assets/assets/000/000/368/medium800/temperature_maxtest.gif?1447975488)

As you can see, its pretty simple to use the library, simply tell the sensor object what the clock, chip select and data pins are, then call&nbsp;**readCelsius()** or&nbsp;**readFahrenheit()**&nbsp;to get a floating point result.

# Adding a Display
A common request is to have the temperature output onto [a 'classic' character LCD such as the ones in this tutorial](http://learn.adafruit.com/character-lcds).  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/369/medium800/temperature_LCDThermocouple.jpg?1396762511)

For this wiring, we connected **CLK** to digital **3** , **CS** to digital **4** and **DO** to digital **5.** Once you get it working, you can change the pin connections in the sketch  
  
We have an example sketch for this as well. [First get the LCD working by following our tutorial](http://learn.adafruit.com/character-lcds). Now load up the new sketch **File-\>Examples**** -\> ****MAX31855**** \> ****lcdthermocouple** and plug in the thermocouple module as we did in the serial thermocouple test, you'll see the internal temperature and the thermocouple temperature displayed in Celsius

- [Previous Page](https://learn.adafruit.com/thermocouple/wiring-a-thermocouple.md)
- [Next Page](https://learn.adafruit.com/thermocouple/python-circuitpython.md)

## Primary Products

### Adafruit Universal Thermocouple Amplifier MAX31856 Breakout

[Adafruit Universal Thermocouple Amplifier MAX31856 Breakout](https://www.adafruit.com/product/3263)
Thermocouples are very sensitive, requiring a good amplifier with a cold-compensation reference, as well as calculations to handle any non-linearities. For a long time we've [suggested our MAX31855K breakout, which works great but is only for...](https://www.adafruit.com/products/269)

In Stock
[Buy Now](https://www.adafruit.com/product/3263)
[Related Guides to the Product](https://learn.adafruit.com/products/3263/guides)

## Featured Products

### Thermocouple Amplifier MAX31855 breakout board (MAX6675 upgrade)

[Thermocouple Amplifier MAX31855 breakout board (MAX6675 upgrade)](https://www.adafruit.com/product/269)
Thermocouples are very sensitive, requiring a good amplifier with a cold-compensation reference. The MAX31855K does everything for you, and can be easily interfaced with any microcontroller, even one without an analog input. This breakout board has the chip itself, a 3.3V regulator with 10uF...

Out of Stock
[Buy Now](https://www.adafruit.com/product/269)
[Related Guides to the Product](https://learn.adafruit.com/products/269/guides)
### Thermocouple Type-K Glass Braid Insulated

[Thermocouple Type-K Glass Braid Insulated](https://www.adafruit.com/product/270)
Thermocouples are best used for measuring temperatures that can go above 100 °C. This is a bare wires bead-probe which can measure air or surface temperatures. Most inexpensive thermocouples have a vinyl covering which can melt at around 200 °C, this one uses a fiberglass braid so it...

In Stock
[Buy Now](https://www.adafruit.com/product/270)
[Related Guides to the Product](https://learn.adafruit.com/products/270/guides)
### Thermocouple Type-K Glass Braid Insulated Stainless Steel Tip

[Thermocouple Type-K Glass Braid Insulated Stainless Steel Tip](https://www.adafruit.com/product/3245)
Thermocouples are best used for measuring temperatures that can go above 100°C. This is a bare wires stainless-steel tip probe which can measure air or surface temperatures. Most inexpensive thermocouples have a vinyl covering which can melt at around 200°C, this one uses a fiberglass...

In Stock
[Buy Now](https://www.adafruit.com/product/3245)
[Related Guides to the Product](https://learn.adafruit.com/products/3245/guides)

## Related Guides

- [Google Docs Sensor Logging From Your PC](https://learn.adafruit.com/gdocs-sensor-logging-from-your-pc.md)
- [Calibrating Sensors](https://learn.adafruit.com/calibrating-sensors.md)
- [CircuitPython Libraries on Linux and the 96Boards DragonBoard 410c](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-96boards-dragonboard-410c.md)
- [Connecting the MAX31855 Thermocouple Amplifier breakout to an Electric Imp](https://learn.adafruit.com/connecting-the-max31855-thermocouple-amplifier-breakout-to-an-electric-imp.md)
- [ Analog IC Insights On-the-Go by Maxim Integrated](https://learn.adafruit.com/maxim-app.md)
- [Adafruit 1-Wire Thermocouple Amplifier - MAX31850K](https://learn.adafruit.com/adafruit-1-wire-thermocouple-amplifier-max31850k.md)
- [Adding a Single Board Computer to Blinka](https://learn.adafruit.com/adding-a-single-board-computer-to-blinka.md)
- [MicroPython Hardware: SPI Devices](https://learn.adafruit.com/micropython-hardware-spi-devices.md)
- [CircuitPython I2C and SPI Under the Hood](https://learn.adafruit.com/circuitpython-basics-i2c-and-spi.md)
- [MAX31855 Thermocouple Sensor Python Library](https://learn.adafruit.com/max31855-thermocouple-python-library.md)
- [Adafruit FT232H With SPI & I2C Devices](https://learn.adafruit.com/adafruit-ft232h-with-spi-and-i2c-libraries.md)
- [MLX90640 Thermal Camera with Image Recording](https://learn.adafruit.com/mlx90640-thermal-image-recording.md)
- [EZ Make Oven](https://learn.adafruit.com/ez-make-oven.md)
- [Adafruit BME680](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas.md)
- [My Mini Race Car](https://learn.adafruit.com/my-mini-race-car.md)
