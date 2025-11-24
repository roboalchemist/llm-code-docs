# Source: https://learn.adafruit.com/tmp36-temperature-sensor/tmp36-with-circuitpython.md

# TMP36 Temperature Sensor

## TMP36 with CircuitPython

With CircuitPython it's easy to read the TMP36 sensor using the [analog I/O module](../../../../circuitpython-basics-analog-inputs-and-outputs) and analog to digital converter built-in to your board.&nbsp; You can easily turn the TMP36 output voltage into a precise temperature reading with just a few lines of Python code.

To follow this page make sure to wire up the TMP36 sensor to your CircuitPython board as shown on the previous page.&nbsp; The A0 analog input will be used as the input from the TMP36's temperature output.&nbsp; Here's an example of a Feather M0 wired to the TMP36 on the A0 analog input:

 **Note:** The simple circuit just connecting the sensor to a board was found to give incorrect readings with CircuitPython because of the speed at which CircuitPython reads the analog value.

To fix this problem, add a 0.01uF or 0.1uF capacitor and a 47k resistor across the output and ground pins of the TMP36, shown below.

![](https://cdn-learn.adafruit.com/assets/assets/000/129/878/medium800/temperature___humidity_TMP36_bb.png?1715112497)

First&nbsp;[connect to the board's serial REPL&nbsp;](../../../../micropython-basics-how-to-load-micropython-on-a-board/serial-terminal)so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

Next import the necessary **board** and **analogio** modules:

```
import board
import analogio
```

Now create an analog input for the A0 pin on the board:

```
tmp36 = analogio.AnalogIn(board.A0)
```

At this point you can read the raw ADC value of the TMP36 sensor output.&nbsp; Like the analog I/O guide mentions this value will range from 0 to 65535 proportional to the voltage output by the sensor (from 0 to the analog reference voltage of your board, typically 3.3V to 5V).

For example try reading the raw ADC value:

```
tmp36.value
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/706/medium800/temperature_Screen_Shot_2017-10-27_at_5.06.49_PM.png?1509149220)

You can convert this value into a voltage (in millivolts) using a similar formula mentioned on the previous page.&nbsp; However there's one small change to increase the range of values from 1023 to 65535--this is necessary because CircuitPython uses a wider range of values for ADC inputs.&nbsp; In addition with CircuitPython you can directly access the board's analog reference voltage so one simple equation will work for both 3.3V and 5V references:

```
tmp36.value * (tmp36.reference_voltage * 1000 / 65535)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/820/medium800/temperature_Screen_Shot_2017-11-01_at_3.26.27_PM.png?1509575203)

Once you have the analog voltage value output by the TMP36 you can turn it into a temperature in degrees Celsius just like the previous page shows:

```
millivolts = tmp36.value * (tmp36.reference_voltage * 1000 / 65535)
(millivolts - 500) / 10
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/821/medium800/temperature_Screen_Shot_2017-11-01_at_3.28.00_PM.png?1509575296)

Let's make a function to perform this math for us and return the temperature in degrees Celsius:

```
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10

tmp36_temperature_C(tmp36)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/822/medium800/temperature_Screen_Shot_2017-11-01_at_3.30.01_PM.png?1509575430)

![](https://cdn-learn.adafruit.com/assets/assets/000/047/823/medium800/temperature_Screen_Shot_2017-11-01_at_3.30.13_PM.png?1509575441)

You can turn this into a complete program that reads and prints the temperature every second too.&nbsp; Save this as a **code.py** on your board and check the serial output:

```
import board
import analogio
import time


TMP36_PIN = board.A0  # Analog input connected to TMP36 output.


# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10


# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN)

# Loop forever.
while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a second before looping again.
    print("Temperature: {}C {}F".format(temp_C, temp_F))
    time.sleep(1.0)
```

- [Previous Page](https://learn.adafruit.com/tmp36-temperature-sensor/using-a-temp-sensor.md)
- [Next Page](https://learn.adafruit.com/tmp36-temperature-sensor/example-projects.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### TMP36 - Analog Temperature sensor

[TMP36 - Analog Temperature sensor](https://www.adafruit.com/product/165)
Wide range, low power temperature sensor outputs an analog voltage that is proportional to the ambient temperature. To use, connect pin 1 (left) to power (between 2.7 and 5.5V), pin 3 (right) to ground, and pin 2 to analog in on your microcontroller. The voltage out is 0V at -50°C and...

In Stock
[Buy Now](https://www.adafruit.com/product/165)
[Related Guides to the Product](https://learn.adafruit.com/products/165/guides)

## Related Guides

- [All About Arduino Libraries](https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use.md)
- [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield.md)
- [DS1307 Real Time Clock Breakout Board Kit](https://learn.adafruit.com/ds1307-real-time-clock-breakout-board-kit.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Track Your Treats: Halloween Candy GPS Tracker](https://learn.adafruit.com/track-your-treats-halloween-candy-gps-tracker.md)
- [Arduino Lesson 10. Making Sounds](https://learn.adafruit.com/adafruit-arduino-lesson-10-making-sounds.md)
- [Adafruit Analog Accelerometer Breakouts](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts.md)
- [Adafruit VS1053 MP3/AAC/Ogg/MIDI/WAV Codec Breakout Tutorial](https://learn.adafruit.com/adafruit-vs1053-mp3-aac-ogg-midi-wav-play-and-record-codec-tutorial.md)
- [Ladyada's Learn Arduino - Lesson #1](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-1.md)
- [Adafruit Proto Screw Shield](https://learn.adafruit.com/adafruit-proto-screw-shield.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Arduino Lesson 7. Make an RGB LED Fader](https://learn.adafruit.com/adafruit-arduino-lesson-7-make-an-rgb-led-fader.md)
- [Trainable Robotic Arm](https://learn.adafruit.com/trainable-robotic-arm.md)
- [Adafruit Arduino Selection Guide](https://learn.adafruit.com/adafruit-arduino-selection-guide.md)
