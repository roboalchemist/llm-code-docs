# Source: https://learn.adafruit.com/thermistor/using-a-thermistor.md

# Thermistor

## Using a Thermistor

## Connecting to a Thermistor
These thermistors are pretty hardy, you can strip the PVC insulation and stick the wires into a breadboard or solder to them directly. Of course you can cut or extend the wires. Since the resistance is pretty high (10Kohm) the wire resistance won't make a huge difference.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/569/medium800/temperature_thermbb.jpg?1396764109)

## Analog Voltage Reading Method

To measure the temperature, we need to measure the resistance. However, a microcontroller does not have a resistance-meter built in. Instead, it only has a voltage reader known as a analog-digital-converter. So what we have to do is convert the resistance into a voltage, and we'll do that by adding another resistor and connecting them in series. Now you just measure the voltage in the middle, as the resistance changes, the voltage changes too, according to the simple voltage-divider equation. We just need to keep one resistor fixed

Say the fixed resistor is&nbsp; **10K** &nbsp;and the variable resistor is called&nbsp; **R** &nbsp;- the voltage output ( **Vo** ) is:

**Vo = R / (R + 10K) \* Vcc**

Where&nbsp; **Vcc** &nbsp;is the power supply voltage (3.3V or 5V)

Now we want to connect it up to a microcontroller. Remember that when you measure a voltage ( **Vi** ) into an Arduino ADC, you'll get a number.

**ADC value = Vi \* 1023 / Varef**

So now we combine the two ( **Vo** &nbsp;=&nbsp; **Vi** ) and get:

ADC value =&nbsp;**R / (R + 10K) \* Vcc \* 1023 / Varef**

What is nice is that if you notice, if Vcc (logic voltage) is the same as the ARef, analog reference voltage, the values cancel out!

ADC value =&nbsp;**R / (R + 10K) \* 1023**

It doesn't matter what voltage you're running under. Handy!

Finally, what we really want to do is get that&nbsp; **R** &nbsp;(the unknown resistance). So we do a little math to move the&nbsp; **R** &nbsp;to one side:

**R = 10K / (1023/ADC - 1)**

_Lots of people have emailed me to tell me the above equation is wrong and the correct calculation is **R = 10K\*ADC / (1023 - ADC)**. Their equivalence is left as an exercise for the reader! ;)_

Great, lets try it out. Connect up the thermistor as shown:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/570/medium800/temperature_thermistor_bb.png?1396764132)

Connect one end of the 10K resistor to 5V, connect the other end of the 10K 1% resistor to one pin of the thermistor and the other pin of the thermistor to ground. Then connect Analog 0 pin to the 'center' of the two.

Now run the following sketch:

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Themistor/Example1/Example1.ino

You should get responses that correspond to the resistance of the thermistor as measured with a multimeter

If you are not getting correct readings, check that the 10K resistor is placed between VCC and A0, and the thermistor is between A0 and ground. Check you have a 10K Thermistor and that you are using a 'standard' NTC thermistor. On a "5V" microcontroller like classic Arduino or Metro 328, use 5V for the VCC pin. On 3.3V microcontrollers like Feather or Arduino Zero, use 3.3V for the VCC pin.

If, when you heat up the thermistor, the temperature reading goes down, check that you don't have the two resistors swapped and check that you are using an NTC not PTC thermistor.

## Better Readings

When doing analog readings, especially with a 'noisy' board like the arduino, we suggest two tricks to improve results. One is to use the 3.3V voltage pin as an analog reference and the other is to take a bunch of readings in a row and average them.

The first trick relies on the fact that the 5V power supply that comes straight from your computer's USB does a lot of stuff on the Arduino, and is almost always much noisier than the 3.3V line (which goes through a secondary filter/regulator stage!) It's easy to use, simply connect 3.3V to AREF and use that as the VCC voltage. Because our calcuations don't include the VCC voltage, you don't have to change your equation. You do have to set the analog reference but that's a single line of code

Taking multiple readings to average out the result helps get slightly better results as well, since you may have noise or fluctuations, we suggest about 5 samples.

Rewire as shown, the 10K resistor is still connected to the higher voltage, and the thermistor to ground

![](https://cdn-learn.adafruit.com/assets/assets/000/000/571/medium800/temperature_thermistor_bb2.png?1396764158)

This sketch takes those two improvements and integrates them into the demo, you will have better, more precise readings.Info: 

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Themistor/Example2/Example2.ino

## Converting to Temperature

Finally, of course, we want to have the temperature reading, not just a resistance! If you just need to do a quick comparison circuit (if temperature is below X do this, if its above Y do that), you can simply use the temperature/resistance table which correlates the resistance of the thermistor to the temperature.

However, you probably want actual temperature values.&nbsp;[To do that we'll use the Steinhart-Hart equation](http://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation)&nbsp;, which lets us do a good approximation of converting values. Its not as exact as the thermistor table (it is an approximation) but its pretty good around the temperatures that this thermistor is used.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/572/medium800/temperature_steinhart.png?1396764159)

However, this equation is fairly complex, and requires knowing a lot of variables that we don't have for this thermistor.&nbsp;[Instead we will use the simplified B parameter equation](http://en.wikipedia.org/wiki/Thermistor). ![](https://cdn-learn.adafruit.com/assets/assets/000/000/573/medium800/temperature_bequastion.png?1396764163)

For this one we only need to know&nbsp; **To&nbsp;** (which is room temperature, 25 °C = 298.15 K)&nbsp; **B** &nbsp;(in this case 3950, the coefficient of the thermistor), and&nbsp; **Ro** &nbsp;(the resistance at room temp, in this case 10Kohm). We plug in&nbsp; **R** &nbsp;(resistance measured) and get out&nbsp; **T** &nbsp;(temperature in Kelvin) which is easy to convert to °C

The following sketch will calculate °C for you

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Themistor/Example3/Example3.ino

![](https://cdn-learn.adafruit.com/assets/assets/000/000/574/medium800/temperature_tempreading.gif?1447976196)

For better precision, we suggest reading the exact value of the 'series 10K' it should be nearly exactly 10K but if you can get a better reading that will reduce your error.## How Accurate is the Reading?

You may notice that above, the temperature reading is 28.16°C - does that mean we have 0.01°C accuracy?&nbsp;Unfortunately&nbsp;no! The thermistor has error and the analog reading circuitry has error.

We can approximate the expected error by first taking into account the thermistor resistance error. The thermistor is correct to 1%, which means that at 25°C it can read 10,100 to 9900 ohms. At around 25°C a difference of 450 ohms represents 1°C so 1% error means about +-0.25°C (you may be able to calibrate this away by determining the resistance of the thermistor in a 0°C ice bath and removing any offset). You can also spring for a 0.1% thermistor which will reduce the possible resistance error down to +-0.03°C

Then there is the error of the ADC, for every bit that it is wrong the resistance (around 25°C) can be off by about 50 ohms. This isn't too bad, and is a smaller error than the thermistor error itself +-(0.1°C) but there is no way to calibrate it 'away' - a higher precision ADC (12-16 bits instead of 10) will give you more precise readings

In general, we think thermistors are higher precision than thermocouples, or most low cost digital sensors, but you will not get better than +-0.1°C accuracy on an Arduino with a 1% thermistor and we would suggest assuming no better than +-0.5°C.

# Self-Heating

If you have a 10K thermistor + 10K resistor connected between 5V and ground, you'll get about 5V / (10K + 10K) = 0.25mA flowing at all times. While this isn't a lot of current, it will heat up your thermistor as the 10K thermistor will be dissipating about 0.25mA \* 2.5V = 0.625 mW.

To avoid this heating, you can try connecting the 'top' of the resistor divider to a GPIO pin and set that pin HIGH when you want to read (thus creating the divider) and then LOW when you are in low power mode (no current will flow from 0V to ground)

- [Previous Page](https://learn.adafruit.com/thermistor/testing-a-thermistor.md)
- [Next Page](https://learn.adafruit.com/thermistor/circuitpython.md)

## Featured Products

### 10K Precision Epoxy Thermistor

[10K Precision Epoxy Thermistor](https://www.adafruit.com/product/372)
Need to measure something damp? This epoxy-coated precision 1% 10K thermistor is an inexpensive way to measure temperature in weather or liquids. The resistance in 25 °C is 10K (+- 1%). The resistance goes down as it gets warmer and goes up as it gets cooler. <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/372)
[Related Guides to the Product](https://learn.adafruit.com/products/372/guides)

## Related Guides

- [Adafruit Sensirion SHT40, SHT41 & SHT45 Temperature & Humidity Sensors](https://learn.adafruit.com/adafruit-sht40-temperature-humidity-sensor.md)
- [Compost Friend!](https://learn.adafruit.com/compost-optimization-machine.md)
- [No-Code DS18B20 Temperature Sensor with WipperSnapper](https://learn.adafruit.com/using-ds18b20-temperature-sensor-with-wippersnapper.md)
- [Adafruit MAX31856 Universal Thermocouple Amplifier](https://learn.adafruit.com/adafruit-max31856-thermocouple-amplifier.md)
- [Make It Hot or Cold](https://learn.adafruit.com/make-it-hot-or-cold.md)
- [Adafruit SHT4x Trinkey](https://learn.adafruit.com/adafruit-sht4x-trinkey.md)
- [PyGamer Thermal Camera with AMG8833](https://learn.adafruit.com/pygamer-thermal-camera-amg8833.md)
- [Adafruit AHT20 Temperature & Humidity Sensor](https://learn.adafruit.com/adafruit-aht20.md)
- [Adafruit HDC1008 Temperature and Humidity Sensor Breakout](https://learn.adafruit.com/adafruit-hdc1008-temperature-and-humidity-sensor-breakout.md)
- [Humidity and Temperature Monitor with E-Ink Display](https://learn.adafruit.com/humidity-and-temperature-monitor-redux-e-ink-display.md)
- [Adafruit TMP117 High Accuracy I2C Temperature Monitor](https://learn.adafruit.com/adafruit-tmp117-high-accuracy-i2c-temperature-monitor.md)
- [My Mini Race Car](https://learn.adafruit.com/my-mini-race-car.md)
- [Raspberry Pi Azure IoT Hub Dashboard with CircuitPython](https://learn.adafruit.com/raspberry-pi-iot-dashboard-with-azure-and-circuitpython.md)
- [Ikea Vindriktning Hack with QT Py ESP32-S3 and Adafruit IO](https://learn.adafruit.com/ikea-vindriktning-hack-with-qt-py-esp32-s3-and-adafruit-io.md)
- [Adafruit MLX90640 IR Thermal Camera](https://learn.adafruit.com/adafruit-mlx90640-ir-thermal-camera.md)
