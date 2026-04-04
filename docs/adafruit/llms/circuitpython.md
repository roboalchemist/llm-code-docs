# Source: https://learn.adafruit.com/rgb-lcd-shield/circuitpython.md

# Source: https://learn.adafruit.com/thermistor/circuitpython.md

# Source: https://learn.adafruit.com/ir-sensor/circuitpython.md

# Source: https://learn.adafruit.com/photocells/circuitpython.md

# Photocells

## CircuitPython

It's easy to read how much light a photocell sees with CircuitPython and its [built-in analog input support](../../../../circuitpython-basics-analog-inputs-and-outputs/analog-to-digital-converter-inputs).&nbsp; By wiring the photocell to an analog input of your board you can read the voltage from it and see how it changes as the amount of light hitting the sensor changes too.

First wire up a photocell to your board as shown on the previous page for Arduino.&nbsp; You'll want to setup the same voltage divider with a **10 kilo-ohm resistor** circuit and feed the output into any analog input on your board (note the special method of reading photocells without an analog input is not currently supported by CircuitPython).

Here's an example of wiring a photocell to a Feather M0:

![](https://cdn-learn.adafruit.com/assets/assets/000/049/000/medium800/light_m0_photocell_bb.png?1512773081)

- **Board 3.3V** to **one&nbsp;leg of the photocell** (doesn't matter which leg).&nbsp; Note you want to use the voltage from your board that corresponds to the maximum analog input voltage.&nbsp; For Feather boards this is 3.3V, but for other boards it might be higher or lower--consult your board documentation to be sure.
- **10 kilo-ohm resistor** to the **other leg of the photocell.**
- **Board GND&nbsp;** to the **other leg of the 10 kilo-ohm resistor**.
- **Board A1** (or any other analog input) to the **junction of the photocell & 10 kilo-ohm resistor**.

Next&nbsp;[connect to the board's serial REPL&nbsp;](../../../../micropython-basics-how-to-load-micropython-on-a-board/serial-terminal)so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

Now import the&nbsp; **board** &nbsp;and&nbsp; **analogio** &nbsp;modules that allow you to read an analog input.&nbsp; Be sure you've read the&nbsp;[CircuitPython analog I/O guide](../../../../circuitpython-analog-inputs-and-outputs)&nbsp;for more background on using analog inputs too!

```
import board
import analogio
```

Create an analog input for the A1 pin connected to the photocell & resistor junction:

```
photocell = analogio.AnalogIn(board.A1)
```

At this point you can read the value property to get a reading of the light seen by the photocell.&nbsp; Try it:

```
photocell.value
```

![](https://cdn-learn.adafruit.com/assets/assets/000/049/001/medium800/light_Screen_Shot_2017-12-08_at_2.50.58_PM.png?1512773495)

Try covering the photocell with your hand to block the light it can see and read the value again:

```
photocell.value
```

![](https://cdn-learn.adafruit.com/assets/assets/000/049/002/medium800/light_Screen_Shot_2017-12-08_at_2.52.12_PM.png?1512773550)

Notice the value changed!&nbsp; When the sensor sees less light the value is reduced.&nbsp; The more light the sensor sees, the higher the value.

You might wonder, what's the range of possible values?&nbsp; It turns out for an analog input in CircuitPython the maximum values range from 0 to 65535 (or the maximum 16-bit unsigned integer value).&nbsp; If you shine an extremely bright light on the photocell you might see a value near 65k, and if you completely block the sensor you might see a value down near 0.

If you're curious you can also convert this value into a voltage that's higher or lower depending on how much light is hitting the sensor.&nbsp; Let's make a function to do this:

```
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage
volts = analog_voltage(photocell)
print('Photocell voltage: {0}V'.format(volts))
```

![](https://cdn-learn.adafruit.com/assets/assets/000/049/003/medium800/light_Screen_Shot_2017-12-08_at_2.56.40_PM.png?1512773820)

Cool!&nbsp; Notice the voltage increases up to near 3.3 volts as the light hitting the photocell increases.&nbsp; If you cover the photocell up and read the voltage you'll see it falls down near 0 volts.

You can use either the raw value or voltage to check how much light is hitting the photocell.&nbsp; Both will change proportionally to the amount of light hitting the sensor.

Here's a complete program that reads the photocell value and prints both the value and voltage every second.&nbsp; Save this as **main.py** on your board and open the serial output to see the printed values.&nbsp; Try shining light on the sensor or covering it up to see how the value and voltage change!

```
import time

import board
import analogio


# Initialize analog input connected to photocell.
photocell = analogio.AnalogIn(board.A1)

# Make a function to convert from analog value to voltage.
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

# Main loop reads value and voltage every second and prints them out.
while True:
    # Read the value, then the voltage.
    val = photocell.value
    volts = analog_voltage(photocell)
    # Print the values:
    print('Photocell value: {0} voltage: {1}V'.format(val, volts))
    # Delay for a second and repeat!
    time.sleep(1.0)
```

That's all there is to reading a photocell using an analog input with CircuitPython!

- [Previous Page](https://learn.adafruit.com/photocells/arduino-code.md)
- [Next Page](https://learn.adafruit.com/photocells/example-projects.md)

## Featured Products

### Photo cell (CdS photoresistor)

[Photo cell (CdS photoresistor)](https://www.adafruit.com/product/161)
CdS cells are little light sensors. As the squiggly face is exposed to more light, the resistance goes down. When it's light, the resistance is about ~1KΩ, when dark it goes up to ~10KΩ.

To use, connect one side of the photocell (either one, it's symmetric) to power...

In Stock
[Buy Now](https://www.adafruit.com/product/161)
[Related Guides to the Product](https://learn.adafruit.com/products/161/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Digital Multimeter

[Digital Multimeter](https://www.adafruit.com/product/71)
This is a basic multimeter, I've played with it a bunch and I think its a great addition to a toolbox. It's low cost and simple to use with a big clear display and all the measurements you need:

- AC/DC Voltage measurement
- Current measurement, from 1uA up to...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/71)
[Related Guides to the Product](https://learn.adafruit.com/products/71/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [Halloween Pumpkin](https://learn.adafruit.com/halloween-pumpkin.md)
- [Adafruit Proto Screw Shield](https://learn.adafruit.com/adafruit-proto-screw-shield.md)
- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [Arduino Lesson 12. LCD Displays - Part 2](https://learn.adafruit.com/adafruit-arduino-lesson-12-lcd-displays-part-2.md)
- [Silicone Robo-Tentacle](https://learn.adafruit.com/silicone-robo-tentacle.md)
- [Babel Fish](https://learn.adafruit.com/babel-fish.md)
- [Arduino Lesson 10. Making Sounds](https://learn.adafruit.com/adafruit-arduino-lesson-10-making-sounds.md)
- [Arduino Lesson 16. Stepper Motors](https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors.md)
- [Line Following Zumo Robot Using Simulink](https://learn.adafruit.com/line-following-zumo-robot-programmed-with-simulink.md)
- [Bluefruit LE Connect for iOS and Android](https://learn.adafruit.com/bluefruit-le-connect.md)
- [Adafruit 16-channel PWM/Servo Shield](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [Adafruit 1.14" 240x135 Color TFT Breakout LCD Display](https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout.md)
