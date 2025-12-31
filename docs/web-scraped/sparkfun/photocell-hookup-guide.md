# Source: https://learn.sparkfun.com/tutorials/photocell-hookup-guide

## Introduction

[Photocells](https://www.sparkfun.com/products/9088) are light-sensitive, variable resistors. As more light shines of the sensor's head, the resistance between its two terminals decreases. They\'re easy-to-use, and an essential component in projects that require ambient-light sensing.

[![Mini Photocell](https://cdn.sparkfun.com/r/600-600/assets/parts/2/4/6/2/09088-02-L.jpg)](https://www.sparkfun.com/mini-photocell.html)

### [Mini Photocell](https://www.sparkfun.com/mini-photocell.html) 

[ SEN-09088 ]

This is a very small light sensor. A photocell changes (also called a \[photodetector\](http://en.wikipedia.org/wiki/Photodetec...

[ [\$1.75] ]

In pitch-black conditions, the photocell's resistance will be in the megaohm's (1.0MΩ+) range. Shining an LED on the sensor can drop the resistance to near-zero, but usually the resistance of the photocell falls between 8-20kΩ in normal lighting conditions.

By combining the photocell with a static resistor to create a [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers), you can produce a variable voltage that can be read by a microcontroller\'s analog-to-digital converter.

### Suggested Materials

This tutorial serves as a quick primer on resistive photocells\', and demonstrates how to hook them up and use them. Beyond the light sensor, the following materials are recommended:

**[Arduino Uno](https://www.sparkfun.com/products/11021)** \-- We\'ll be using the Arduino\'s analog-to-digital converter to read in the variable resistance of the photocell. Any Arduino-compatible development platform \-- be it a [RedBoard](https://www.sparkfun.com/products/13975), [Pro](https://www.sparkfun.com/products/10914) or [Pro Mini](https://www.sparkfun.com/products/11113) \-- can substitute.

**[Resistor Kit](https://www.sparkfun.com/products/10969)** \-- To turn the photocell\'s variable resistance into a readable voltage, we\'ll combine it with a static resistor to create a voltage divider. This resistor kit is handy for some trial-and-error testing to hone in on the most sensitive circuit possible.

**[Breadboard](https://www.sparkfun.com/products/12002) and [Jumper Wires](https://www.sparkfun.com/products/11026)** \-- The photocell\'s legs, like any through-hole resistor, can be bent and shaped to fit. We\'ll stick them and the resistor into a breadboard, then use the jumper wires to connect from breadboard to Arduino.

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

### Suggested Reading

Photocells are a great entry-level component for beginners, but there are still a few basic electronics concepts you should be familiar with. If any of these tutorial titles sound foreign to you, consider skimming through that content first.

[](https://learn.sparkfun.com/tutorials/light)

### Light 

Light is a useful tool for the electrical engineer. Understanding how light relates to electronics is a fundamental skill for many projects.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/voltage-dividers)

### Voltage Dividers 

Turn a large voltage into a smaller one with voltage dividers. This tutorial covers: what a voltage divider circuit looks like and how it is used in the real world.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

## Photocell Overview

The photocell, sometimes referred to as a photoresistor or light-dependent resistor (LDR), is a two-terminal, resistive component that increases or decreases its resistance depending on the light it senses. They\'re available in a variety of shapes, sizes, and form factors; the [mini photocell](https://www.sparkfun.com/products/9088) in our catalog features a 5x4.3mm head, and through-hole legs that can be soldered into a PCB or inserted into a breadboard.

[![Mini photocell dimensions](https://cdn.sparkfun.com/r/500-500/assets/parts/2/4/6/2/09088-01-L.jpg)](https://cdn.sparkfun.com//assets/parts/2/4/6/2/09088-01-L.jpg)

In pitch black conditions, the resistance of most photocells will measure in the megaohms range. The typical **light resistance** of photocells varies by component. The mini photocell, for example, usually produces a resistance between **8-20kΩ** in normal lighting conditions.

The graph below demonstrates the mini photocell\'s illumination and resistance relationship:

[![Mini photocell illuminance vs resistance](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/5/1/2/illuminance-vs-resistance.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/2/illuminance-vs-resistance.png)

*Light vs. Resistance graph from the [mini photocell datasheet](http://cdn.sparkfun.com/datasheets/Sensors/LightImaging/SEN-09088.pdf).*

As you can tell from the graph above, these sensor\'s aren\'t designed for absolute lux-measurement accuracy \-- they leave a lot of room for interpretation. But, by measuring the photocell\'s resistance, they can provide a relative idea of a room\'s lighting conditions, or tell us if the sun has risen or set.

## Example Circuit

To measure the photocell\'s resistance with a microcontroller\'s ADC, we actually have to use it to generate a variable voltage. By combining the photocell with a static resistor, we can create a [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers) that produces a voltage dependent on the photocell\'s resistance.

A static resistor value between 1kΩ and 10kΩ should pair well with the photocell. If you have a [resistor kit](https://www.sparkfun.com/products/10969), you may want to introduce some trial-and-error to hone in on that perfect static resistance.

In this example, we\'ll use a 4.7kΩ resistor to divide voltage with the photocell. Here\'s the example circuit:

[![Example circuit fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/2/example_circuit_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/2/example_circuit_bb.png)

And a schematic:

[![Example circuit schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/2/example_circuit_schem.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/2/example_circuit_schem.png)

The 4.7kΩ resistor on the ground side, and the photocell on the 5V side, means as the cell\'s **resistance increases** (meaning the sensor\'s surroundings are getting **darker**) the **voltage on A0 will decrease**.

## Example Program

Here is a simple Arduino example based on the circuit above. Copy and paste this into your Arduino IDE, then upload!

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /******************************************************************************
    Photocell_Example.ino
    Example sketch for SparkFun's photocell - light-variable resistor
      (https://www.sparkfun.com/products/9088)
    Jim Lindblom @ SparkFun Electronics
    April 28, 2016

    Create a voltage divider circuit combining a photocell with a 4.7k resistor.
    - The resistor should connect from A0 to GND.
    - The photocell should connect from A0 to 3.3V
    - Connect an LED to pin 13 (if there's not one built into your Arduino)
    As the resistance of the photocell increases (surroundings get darker), the
    voltage at A0 should decrease.

    Development environment specifics:
    Arduino 1.6.7
    ******************************************************************************/
    const int LIGHT_PIN = A0; // Pin connected to voltage divider output
    const int LED_PIN = 13; // Use built-in LED as dark indicator

    // Measure the voltage at 5V and the actual resistance of your
    // 47k resistor, and enter them below:
    const float VCC = 4.98; // Measured voltage of Ardunio 5V line
    const float R_DIV = 4660.0; // Measured resistance of 3.3k resistor

    // Set this to the minimum resistance require to turn an LED on:
    const float DARK_THRESHOLD = 10000.0;

    void setup() 
    

    void loop() 
    
    }

After uploading, **open your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux)**, and set the baud rate to 9600 bps.

Then trigger some changes in light; cover the photocell with your hand, turn your lights off, or shine a flashlight on the cell. You should see the voltage and resistance calculations vary with the light. If it gets darker, the resistance should go up. If it gets lighter, the resistance should go down.

[![FSR readings to serial monitor](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/2/photocell-serial-monitor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/2/photocell-serial-monitor.png)

If the values don\'t look correct to you, make sure the `R_DIV` variable at the top of the sketch is set to your static resistor\'s value.

When the sensed light gets too dark, the Arduino should turn on the pin 13 LED to try to brighten things up. By adjusting the `DARK_THRESHOLD` variable, you can change what lighting conditions trigger this LED illumination.