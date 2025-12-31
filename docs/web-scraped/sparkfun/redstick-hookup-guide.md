# Source: https://learn.sparkfun.com/tutorials/redstick-hookup-guide

## Introduction

The [SparkFun RedStick](https://www.sparkfun.com/products/13741) is a production version of the BadgerStick, which made an appearance at a trade show near you in the [BadgerHack Badge](https://learn.sparkfun.com/tutorials/badgerhack). This version carries an NCP1402 boost regulator (as seen in the [SparkFun 5.0v Step-Up Breakout Board](https://www.sparkfun.com/products/10968), so it can run at **16MHz** from a 6V down to a 2V input!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/2/2/RedStick-01_action.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/RedStick-01_action.jpg)

*The RedStick*

The RedStick operates as an Arduino Uno in the Arduino IDE!

### Covered in This Tutorial

- [Hardware Overview](https://learn.sparkfun.com/tutorials/redstick-hookup-guide#hardware-overview) \-- A tour of the PCB.
- [Powering the RedStick](https://learn.sparkfun.com/tutorials/redstick-hookup-guide#powering-the-redstick)
- [The Blink Sketch](https://learn.sparkfun.com/tutorials/redstick-hookup-guide#example-the-blink-sketch)
- [Using the 8x7 LED Array](https://learn.sparkfun.com/tutorials/redstick-hookup-guide#example-using-the-8x7-led-array) \-- The 8x7 LED array library has been updated to work on this board!
- [Adding a second voltage rail](https://learn.sparkfun.com/tutorials/redstick-hookup-guide#example-adding-a-second-voltage-rail) \-- How to build an LDO onto the RedStick.
- [Conclusion and Resources](https://learn.sparkfun.com/tutorials/redstick-hookup-guide#conclusion-and-resources)

### Suggested Reading

- [RedBoard Hookup Guide](https://learn.sparkfun.com/tutorials/redboard-hookup-guide) \-- The RedBoard and RedStick have many similarities. Learn the ins-and-outs of getting either up and running in the Arduino IDE in this tutorial.
- [BadgerHack](https://learn.sparkfun.com/tutorials/badgerhack) \-- The original BadgerStick (promo) documentation.
- [Charlieplexed 8x7 LED Array Github](https://github.com/sparkfun/BadgerArray) \-- If you would like more information on how the 8x7 LED array is programmed, check out the code files.

## Hardware Overview

The following lists the features of the RedStick:

- A boost regulator providing 5V to the Atmega328p from an input range of 2 to 6 volts.
- 16 MHz system clock (allowed because of the additional supply voltage)
- Uno compatible in the Arduino IDE. Simply select the board \"Arduino/Genuino Uno\" and go!
- USB end matches standard USB thickness and width.

What the RedStick is not:

- A RedBoard \-- it doesn\'t provide 3.3 volts, only 5.
- A battery charger \-- The RedStick turns off the battery when plugged into a USB port.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/2/2/described_hardware.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/described_hardware.png)

*Parts of the RedStick*

\

The following table lists all of the pins on the RedStick and their functionality.

  -----------------------------------------------------------------------------------------------------------------
  Pin Silk\               Function                               Notes
  ----------------------- -------------------------------------- --------------------------------------------------
  TX                      Serial transmit\                       This is serial data coming out of the RedStick.\

  RX                      Serial Receive\                        This is serial data coming in\

  2                       Digital\                               

  \~3                     Digital with PWM\                      

  4                       Digital                                

  \~5                     Digital with PWM\                      

  \~6                     Digital with PWM\                      

  7                       Digital                                

  8\                      Digital                                

  9                       Digital                                

  \~10                    Digital / PWM / SS\                    

  \~11\                   Digital / PWM / MOSI\                  SPI bus\

  12                      PWM / MISO\                            SPI bus\

  13                      Digital / SCK / LED\                   SPI bus\

  A0                      Digital / Analog\                      

  A1                      Digital / Analog\                      

  A2                      Digital / Analog\                      

  A3\                     Digital / Analog\                      

  A4\                     Digital / Analog / SDA\                I2C bus \-- some applications require pull-up\

  A5\                     Digital / Analog / SCL\                I2C bus\-- some applications require pull-up

  A6                      Analog\                                Analog only!\

  A7                      Analog                                 Analog only!

  RXI\                    Serial Receive\                        Electrically tied to RX\

  TXI                     Serial Transmit\                       Electrically tied to TX

  VCC\                    Microprocessor Power (Boost output)\   If using as input, supply regulated 5.0 v\

  GND                     Ground                                 

  \+                      Battery Positive\                      Supply 2.0 to 6.0 volts\

  \-                      Battery Negative\                      This is also GND\
  -----------------------------------------------------------------------------------------------------------------

## Powering the RedStick

The RedStick was designed to allow two sources of power.

- Power directly from the USB port.
- Power with 2-6 volts on the battery terminals.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/2/2/power_flow.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/power_flow.png)

*A block diagram showing how the power flows in this board*

### Functional Description

When power is applied to the USB port, it will not flow into the battery. Alternately, if the USB voltage is lower than the battery, power will not flow into the USB host.

To use AA cells, for example in a battery holder such as a [2xAA Holder with switch](https://www.sparkfun.com/products/9547), solder the wires directly into the battery terminal holes, matching red to positive.

To use a rechargeable battery, such as a [1 Ah Lithium Ion battery](https://www.sparkfun.com/products/339), solder a [JST connector](https://www.sparkfun.com/products/9749) into the smaller, 2mm spaced holes and attach the battery. Again match red with positive.

**Note on VCC:** It\'s conceivable that power might be applied to the VCC pin instead. This is OK as long as the input voltage is regulated while the USB and battery inputs are left open.

### Notes on DC-DC converters

The RedStick uses a boost circuit to convert a low voltage ( \> 2.0 volts DC ) to 5 volts DC. This DC-DC conversion is fairly common in today\'s world where a liner regulator is not efficient enough. This boost circuit measured around 83% efficient.

Here\'s a couple concepts to think about related to DC-DC converters

#### DC-DC converters and power

Ideally, DC-DC converters would be 100% efficient. In the math model, this means that power out = power in. So, if the converter is delivering 200mA at 5V, by the definition of electrical power, that\'s 1W (P = V \* I). If we\'re consuming 1W from the output, we must be supplying 1W to the input. If the input is a battery at 3V, supplying 1W, it must be supplying 330mA. That\'s more than we\'re getting out!

As the input voltage to a DC-DC converter drops, the current consumption increases to maintain the output load.

This also applies to LED and CCFL bulbs that aren\'t dimmer compatible. As the dimmer decreases the voltage, the current *increases* and fries the dimmer circuit because it was designed for resistive loads (incandescents) that behave as Ohm\'s law indicates.

#### Drawbacks of DC-DC converters

The appeal of DC-DC converters is the low cost of the completed circuit. This is because inductors are used in place of transformers. The inductors operate at a high frequency so that the size can be made small, which makes them cheap. The control circuitry is a logic system that chooses when, and how fast, to operate the inductor in order to build up the necessary voltage on the output. This switching frequency can be seen as ripple on the output side of the DC-DC converter, depending on the loading of the circuit.

This DC-DC converter produces between 30 and 170 mV ripple in the 5kHz to 250kHz range, with optimal performance between 2.5-4.5 volts (typical battery voltages).

## Example: The Blink Sketch

The RedStick comes with the blink sketch loaded and running, so the LED (pin 13) will toggle every second. This section shows how to get back to this basic sketch using the Arduino IDE.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/2/2/Badger-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/Badger-01.jpg)

*The RedStick running the blink application to insure basic function. In this photo, the RedStick is being powered from two AA cells.*

To re-load the sketch, select the Arduino/Genuino Uno board from the menu, select the basic example blink, and press upload.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/A_select_board.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/A_select_board.png)

*Selecting the Arduino Uno board. Don\'t forget to select your com port too if it wasn\'t auto-selected*

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/A_select_sketch.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/A_select_sketch.png)

*Select the blink.ino sketch from the basic examples menu*

Now compile and run! That\'s all there is to it!

## Example: Using the 8x7 LED Array

If you would like to use an [8x7 LED Array](https://www.sparkfun.com/products/13795) with the RedStick as with the BadgerStick, you can! The libraries have been updated to use F_CPU to set scroll speeds for 4, 8, and 16MHz boards.

[![Charlieplexed 8x7 LED Array](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_ProductCrop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_ProductCrop.jpg)

**Using a promo 8x7:** The original promo 8x7 LED array was designed for 3.3v operation but the RedStick operates at 5. Applying a 8x7 from a show (has badger logo on back) will have increased brightness and current consumption. For proper compatibility remove the 8 SMD resistors and replace with 82 ohms each, though it\'ll probably be ok if you choose not to alter it.

### Install the Arduino library

The 8x7 LED array has its own library. It is available as a github repository called [SparkFun_LED_Array_8x7_Arduino_Library](https://github.com/sparkfun/SparkFun_LED_Array_8x7_Arduino_Library). It is not part of the library manager and will need to be manually installed (Drop it in your /libraries folder).

For more information, view this [guide to installing Arduino libraries](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Run the example sketch

Under examples, select the 8x7 library, then the example sketch \"ScrollText\". This sketch displays scrolling text on the 8x7 LED array, but the library can also be used to draw individual pixels, shapes, and bitmaps.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/A_select_scroll.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/A_select_scroll.png)

*Selecting the example sketch*

Compile and run the sketch. The example text `Hello. :)` and `Let's scroll!` should scroll across the array. From this point the text can be changed, or the other features of the library can be used. Check out the [BadgerHack \'Make a Game\' section](https://learn.sparkfun.com/tutorials/badgerhack/all#make-a-game) for example code that uses the 8x7 API.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/2/2/Badger-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/Badger-04.jpg)

*The RedStick driving a modified 8x7 LED array (promo item). Here, it scrolls \":)\" as part of the example*

## Example: Adding a Second Voltage Rail

Not all projects are LEDs and digital logic. If you want to add devices that operate at voltages *other* than 5.0 volts, a low-dropout regulator (LDO) can be added to solve the problem. Here, I\'ve used basic components to attach a [BME280 atmospheric sensor](https://www.sparkfun.com/products/13676) to my RedStick. Of course, you could use a [breadboard power supply stick](https://www.sparkfun.com/products/10804). I didn\'t want the barrel jack and extra space used up, so I used discrete components.

This inexpensive wishlist gets you the regulator, plenty of caps, and plenty of proto board to get going.

### Build the LDO circuit

Build the following circuit. Remember to mind polarity on the electrolytic capacitor, that the pin ordering is kind of counter-intuitive, and that the TO-220\'s tab is connected to the pin 2 and not ground.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/2/2/VregCircuit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/VregCircuit.png)

### Connect the LDO circuit

To connect the LDO circuit to the RedStick,

- connect \"GND\" to a spare GND pin
- connect \"Input\" to VCC.

Now the \"Output\" is a regulated rail! In this case, 3.3 volts.

For this example, a BME280 is used. The BME280\'s ground is connected to the common GND pin while 3.3V is connected to the LDO\'s Output terminal. I2C serial lines are directly connected to the RedStick\'s A4 (SDA) and A5 (SCL) pins. The BME280\'s circuit board pulls these lines safely up to 3.3V.

### Run the example

Run the BME280\'s example sketches. For information on use of the BME280, see the [hookup guide](https://learn.sparkfun.com/tutorials/sparkfun-bme280-breakout-hookup-guide).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/2/2/RedStick-03_LDO.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/RedStick-03_LDO.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/2/2/RedStick-02_folded.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/2/RedStick-02_folded.jpg)

*The final product. This USB stick / BME280 combo is great for determining the local weather conditions, altough it\'s usually about 2 degrees Celsius hotter around my computer than in the center of a room*