# Source: https://learn.sparkfun.com/tutorials/ina169-breakout-board-hookup-guide

## Introduction

Have a project where you want to measure the current draw? Need to carefully monitor low current through an LED? The [INA169](https://www.sparkfun.com/products/12040) is the chip for you!

[![SparkFun Current Sensor Breakout - INA169](https://cdn.sparkfun.com/r/600-600/assets/parts/8/6/1/5/12040-01.jpg)](https://www.sparkfun.com/sparkfun-current-sensor-breakout-ina169.html)

### [SparkFun Current Sensor Breakout - INA169](https://www.sparkfun.com/sparkfun-current-sensor-breakout-ina169.html) 

[ SEN-12040 ]

The INA169 is a "high-side current monitor," which means that you place a resistor (a "shunt resistor") on the positi...

[ [\$13.93] ]

The INA169 is a \"high-side current monitor,\" which means that you place a resistor (a \"shunt resistor\") on the positive power rail and the INA169 measures the voltage drop across that resistor. The INA169 outputs a small current based on the measured voltage drop. If you place a resistor from the output of the INA169 to ground, you can measure the voltage at the output. With some basic math, the output voltage gives you the current through the shunt resistor.

### Covered In This Tutorial

In this tutorial, we cover how the board should be used. The Board Overview section covers some theory and math on how the current sensing works, so feel free to skip to the Hookup Example if you just want to see the board in action. The Hookup Example shows how to connect the board to an Arduino in order to measure the current through an LED, and the Example Code provides a quick Arduino sketch for displaying the measured current to the Serial Monitor.

### Required Materials

- [Arduino](https://www.sparkfun.com/products/11021), [RedBoard](https://www.sparkfun.com/products/11575) or any [Arduino-compatible](https://www.sparkfun.com/categories/242) board.
- [Male headers](https://www.sparkfun.com/products/116) to solder to the board and make it breadboard compatible.
- [Jumper wires](https://www.sparkfun.com/products/11026) to connect from breadboard to Arduino.
- [Breadboard](https://www.sparkfun.com/products/9567) to tie everything together.
- [Basic Red LED](https://www.sparkfun.com/products/9590) so we have something to light up.
- [330Ω Resistor](https://www.sparkfun.com/products/8377) to limit the current through the LED.

### Suggested Reading

- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [Resistors](https://learn.sparkfun.com/tutorials/resistors)
- [LEDs](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)
- [Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire)

## Board Overview

Take a look at the [schematic](https://learn.sparkfun.com/tutorials/how-to-read-a-schematic), and you will notice that the breakout board consists of a shunt resistor (R~S~), the INA169 chip, and an output resistor (R~L~). While R~S~ and R~L~ might appear to have 2 resistors, only one is populated on the board. If you would like to change the values of the resistors, you can replace them or put another resistor in parallel.

[![INA169 Breakout Schematic](https://cdn.sparkfun.com/assets/6/d/4/b/1/52827c00757b7f75648b4567.png)](https://cdn.sparkfun.com/assets/6/d/4/b/1/52827c00757b7f75648b4567.png)

*INA169 Current Sensing Breakout Schematic*

As current passes from V~IN+~ through R~S~ to V~IN-~, it creates a voltage drop across R~S~. The op-amp inside of the INA169 chip measures the difference between the V~IN+~ and V~IN-~ voltages and outputs a voltage based on that difference. The output of the op-amp is amplified through the internal transistor, which sources a current out of the INA169 chip. As that current passes through R~L~ to ground, a voltage level is generated at V~OUT~.

**IMPORTANT:** The INA169 is configured to measure DC only. The VIN+ pin must be at a higher potential than the VIN- pin, which means that the INA169 cannot measure AC.

### Measuring Current

The voltage at V~OUT~ can be measured using an oscilloscope or an analog-to-digital converter. A bit of math is needed to convert to the source current (I~S~):

[![alt text](https://cdn.sparkfun.com/assets/b/5/1/6/6/528285ae757b7fd3648b4568.gif)](https://cdn.sparkfun.com/assets/b/5/1/6/6/528285ae757b7fd3648b4568.gif)

***I~S~*** is the current we want to measure.

***V~OUT~*** is the voltage we measured at the output of the INA169.

***1kΩ*** is a constant resistance value we need to include due to the internals of the INA169.

***R~S~*** is the value of the shunt resistor. If you do not modify the board, then this is set at 10Ω.

***R~L~*** is the value of the output resistor. If you do not modify the board, then this is set at 10kΩ.

### Example

For example, let\'s say that you hook up the board and you measure 2.8V at V~OUT~. Plugging this into our equation, we would get:

[![alt text](https://cdn.sparkfun.com/assets/4/4/2/2/4/52828c74757b7faa358b4567.gif)](https://cdn.sparkfun.com/assets/4/4/2/2/4/52828c74757b7faa358b4567.gif)

This shows that you have 0.028A (or 28mA) flowing through your line.

### The Pinout

There are only 5 pins on the breakout board.

[![Pinout of INA169 Breakout Board](https://cdn.sparkfun.com/r/600-600/assets/5/0/a/4/2/528502c5757b7f5c468b456a.jpg)](https://cdn.sparkfun.com/assets/5/0/a/4/2/528502c5757b7f5c468b456a.jpg)

**GND** should be connected to ground of the circuit you are trying to measure

**VIN+** needs to be connected to the positive side of the source (e.g. battery, output pin, etc.)

**VIN-** needs to be connected to the positive side of the load (e.g. VCC on Arduino, positive side of an LED, etc.)

**VOUT** is the measured output and should be connected to something that measures voltage levels, such as a multimeter, oscilloscope, or an Arduino ADC pin

**VCC** is the supply power to the INA169, which needs to be connected to 3.3V, 5V, etc. This can be anywhere from 0 to 75V. Note that the V~OUT~ range depends on the voltage supplied by VCC.

In addition to the pins on VIN+ and VIN-, the board also has two large pads around R~S~, which are capable of taking alligator clips should you want to have a temporary hookup. Note that GND and VCC will still need to be connected for the board to function.

### Modifying Functionality

The INA169 cannot sense any differences across R~S~ greater than 500mV, and the output error increases once the voltage across R~S~ dips below 35mV. If you include the voltage drop across the internal transistor, this means that the default setup of the breakout board is limited to measuring a current range of about 3.5mA to 35mA.

If you would like to change that range, R~S~ and R~L~ can be replaced with resistors of different values. R~S~ can be removed and replaced with another resistor fairly easily. R~L~ is a bit more difficult as it is a small, surface mount resistor. Changing either of the resistors changes the equation from above.

With R~L~ at 10kΩ, changing R~S~ gives us the following ranges:

\

  ---------- -------------------------
   **R~S~**  **Current Sense Range**
     10Ω     3.5mA - 35mA
      1Ω     35mA - 350mA
     0.1Ω    350mA - 3.5A
  ---------- -------------------------

\

**IMPORTANT:** Be careful with the power rating on the resistor! If you choose a 0.1Ω resistor for R~S~ and expect to see 3.5A through it, this can result in 1.2W of heat being generated - way too much for your average ¼W resistor! You will need a resistor that can handle at least 2W. The following power resistors are recommended:\
\

- Ohmite 1Ω 1% 3W
- Ohmite 0.1Ω 1% 3W

### Board Dimensions

The board dimensions is 1.0\" x 1.0\" and includes 4x mounting holes by each corner of the board.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/7/9/e/d/d/SEN-12040_INA169_Current_Sense_Breakout_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/7/9/e/d/d/SEN-12040_INA169_Current_Sense_Breakout_Board_Dimensions.png)

## Hookup Example

### Assembly

You will need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) either [wires](https://www.sparkfun.com/products/11375) or [straight male headers](https://www.sparkfun.com/products/116) to the 5 header holes on the board. If you need to measure over 35mA, you will need to desolder the RS resistor and solder a lower value (e.g. 1Ω), higher power (e.g. 3W) resistor to the holes around RS.

[![Headers on the INA169 board](https://cdn.sparkfun.com/r/600-600/assets/c/b/f/5/1/528502ca757b7f18468b456a.jpg)](https://cdn.sparkfun.com/assets/c/b/f/5/1/528502ca757b7f18468b456a.jpg)

*Headers are optional but recommended if you are using a breadboard.*

### Connecting the INA169 Breakout Board

[![Simple circuit using the INA169](https://cdn.sparkfun.com/r/600-600/assets/2/f/1/7/f/528503df757b7f4e458b4567.png)](https://cdn.sparkfun.com/assets/2/f/1/7/f/528503df757b7f4e458b4567.png)

*Fritzing of the INA169 connected to an Arduino*

As shown in the diagram, connect the Arduino 5V to the INA169 VCC and the Arduino GND to the INA169 GND. To read the output voltage level, we need to run a jumper cable from the Arduino A0 to the INA169 VOUT pin.

Use a jumper wire to connect the INA169 VCC and VIN+ pins, as we want to power the LED with the Arduino 5V. If you use a different power source (other than the Arduino 5V or 3.3V) through VIN+ and VIN-, make sure you connect the ground of the power source to the ground of the INA169 board. Just ensure that the voltage level as measured from VIN+ to ground does not exceed 60V. Bad things will happen to the board if you do.

Connect a 330Ω resistor from the INA169 VIN- to the anode of the LED and a jumper wire from the LED\'s cathode to GND.

[![All the wires!](https://cdn.sparkfun.com/r/600-600/assets/c/d/1/7/c/528502c5757b7f20468b4567.jpg)](https://cdn.sparkfun.com/assets/c/d/1/7/c/528502c5757b7f20468b4567.jpg)

*Actual circuit example*

If you want to measure the current going to something else, you can use alligator clips on the bare metal pads around RS. Make sure that the INA169 board is inline with the positive power rail and that the INA169 GND is connected to the target\'s GND.

## Example Code

Open the Arduino program and paste the following code into the sketch:

    language:c
    /*
     11-14-2013
     SparkFun Electronics 2013
     Shawn Hymel

     This code is public domain but you buy me a beer if you use this 
     and we meet someday (Beerware license).

     Description:

     This sketch shows how to use the SparkFun INA169 Breakout
     Board. As current passes through the shunt resistor (Rs), a
     voltage is generated at the Vout pin. Use an analog read and
     some math to determine the current. The current value is
     displayed through the Serial Monitor.

     Hardware connections:

     Uno Pin    INA169 Board    Function

     +5V        VCC             Power supply
     GND        GND             Ground
     A0         VOUT            Analog voltage measurement

     VIN+ and VIN- need to be connected inline with the positive
     DC power rail of a load (e.g. an Arduino, an LED, etc.).

     */

    // Constants
    const int SENSOR_PIN = A0;  // Input pin for measuring Vout
    const int RS = 10;          // Shunt resistor value (in ohms)
    const int VOLTAGE_REF = 5;  // Reference voltage for analog read

    // Global Variables
    float sensorValue;   // Variable to store value from analog read
    float current;       // Calculated current value

    void setup() 

    void loop() 

Plug in the Arduino and upload the code. You should see the LED light up as soon as you apply power.

[![INA169 in action](https://cdn.sparkfun.com/r/600-600/assets/2/0/f/a/4/528502ca757b7fff458b4569.jpg)](https://cdn.sparkfun.com/assets/2/0/f/a/4/528502ca757b7fff458b4569.jpg)

*The INA169 will measure the current through the LED.*

Select the appropriate board (Arduino Uno in this case) from Tools-\>Board and the correct COM port from Tools-\>Serial Port. Click the upload button, and wait for the program to be compiled and uploaded to the Arduino. Open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) from Tools-\>Serial Monitor and you should see current measurements being printed.

[![Output of Serial Monitor](https://cdn.sparkfun.com/assets/9/2/7/6/6/5283cc52757b7f56508b4567.png)](https://cdn.sparkfun.com/assets/9/2/7/6/6/5283cc52757b7f56508b4567.png)

*If you are using a basic red LED, a 330Ω resistor, and a 5V supply, you should see 0.009A (9mA) on the Serial Monitor.*

If we want to verify this reading, we can use a multimeter to measure the voltage across the 330Ω resistor. You should see around 3V across the resistor. Using Ohm\'s Law, we can calculate the current flowing through the resistor and LED is 0.00909 A, which matches the reading from the INA169.