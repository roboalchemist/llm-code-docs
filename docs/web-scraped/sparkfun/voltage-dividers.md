# Source: https://learn.sparkfun.com/tutorials/voltage-dividers

## Introduction

A **voltage divider** is a simple circuit which turns a large voltage into a smaller one. Using just two series resistors and an input voltage, we can create an output voltage that is a fraction of the input. Voltage dividers are one of the most fundamental circuits in electronics. If learning [Ohm\'s law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) was like being introduced to the ABC\'s, learning about voltage dividers would be like learning how to spell *cat*.

These are examples of potentiometers - variable resistors which can be used to create an adjustable voltage divider. We\'ll learn more about these soon.

[![Thumb Joystick](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/2/7/09032-03-L.jpg)](https://www.sparkfun.com/thumb-joystick.html)

### [Thumb Joystick](https://www.sparkfun.com/thumb-joystick.html) 

[ COM-09032 ]

Add arcade-style control to your project with this analog thumb joystick. If you have ever used a PlayStation 2 controller, y...

[ [\$5.25] ]

[![Trimpot 10K Ohm with Knob](https://cdn.sparkfun.com/r/140-140/assets/parts/3/8/2/3/09806-01.jpg)](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html)

### [Trimpot 10K Ohm with Knob](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html) 

[ COM-09806 ]

This 10K trimmable potentiometer has a small knob built right in and it\'s breadboard friendly to boot!

[ [\$1.25] ]

[![Rotary Potentiometer - Linear (10k ohm)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/9/4/09288-Rotary_Potentiometer_-_Linear__10k_ohm_-01.jpg)](https://www.sparkfun.com/rotary-potentiometer-linear-10k-ohm.html)

### [Rotary Potentiometer - Linear (10k ohm)](https://www.sparkfun.com/rotary-potentiometer-linear-10k-ohm.html) 

[ COM-09288 ]

An adjustable potentiometer can open up many interesting user interfaces. Turn the pot and the resistance changes. Connect VC...

[ [\$1.25] ]

[![Slide Pot - Small (10k Linear Taper)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/6/5/4/11620-01.jpg)](https://www.sparkfun.com/slide-pot-small-10k-linear-taper.html)

### [Slide Pot - Small (10k Linear Taper)](https://www.sparkfun.com/slide-pot-small-10k-linear-taper.html) 

[ COM-11620 ]

A simple slide potentiometer can go a long way. Rated at 10KOhm and 0.1W. Comes with solder tab connections. The pot has an o...

[ [\$0.95] ]

### Covered in this Tutorial

- What a voltage divider circuit looks like.
- How the output voltage depends on the input voltage and divider resistors.
- How voltage dividers behave in the real-world.
- Real-life voltage divider applications.

### Suggested Reading

This tutorial builds on basic electronics knowledge. If you haven\'t already, consider reading these tutorials:

- [What is a circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Series and Parallel Circuits](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [Analog vs Digital](https://learn.sparkfun.com/tutorials/analog-vs-digital)
- [How to Use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [Analog-to-Digital Conversion](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

## Ideal Voltage Divider

There are two important parts to the voltage divider: the circuit and the equation.

### The Circuit

A voltage divider involves applying a voltage source across a series of two resistors. You may see it drawn a few different ways, but they should always essentially be the same circuit.

[![Examples of voltage divider schematics](//cdn.sparkfun.com/r/600-600/assets/4/0/3/a/e/511948ffce395f7f47000000.png)](//cdn.sparkfun.com/assets/4/0/3/a/e/511948ffce395f7f47000000.png)

*Examples of voltage divider schematics. Shorthand, longhand, resistors at same/different angles, etc.*

We\'ll call the resistor closest to the input voltage (V~in~) R~1~, and the resistor closest to ground R~2~. The voltage drop across R~2~ is called V~out~, that\'s the divided voltage our circuit exists to make.

That\'s all there is to the circuit! V~out~ is our divided voltage. That\'s what\'ll end up being a fraction of the input voltage.

### The Equation

The voltage divider equation assumes that you know three values of the above circuit: the input voltage (V~in~), and both resistor values (R~1~ and R~2~). Given those values, we can use this equation to find the output voltage (V~out~):

[![Vout = Vin \* (R2 / (R1 + R2))](//cdn.sparkfun.com/assets/e/7/6/3/c/511968d9ce395f7c54000000.png)](//cdn.sparkfun.com/assets/e/7/6/3/c/511968d9ce395f7c54000000.png)

*Memorize that equation!*

This equation states that the output voltage is **directly proportional** to the **input voltage** and the **ratio of R~1~ and R~2~**. If you\'d like to find out where this comes from, check out [this section](https://learn.sparkfun.com/tutorials/voltage-dividers/all#extra-credit-proof) where the equation is derived. But for now, just write it down and remember it!

### Calculator

Have some fun experimenting with inputs and outputs to the voltage divider equation! Below, you can plug in numbers for V~in~ and both resistors and see what kind of output voltage they produce.

V~in~ =  V\
R~1~ =  Ω\
R~2~ =  Ω\
V~out~ =  V\

Or, if you adjust V~out~, you\'ll see what resistance value at R~2~ is required (given a V~in~ and R~1~).

### Simplifications

There are a few generalizations that are good to keep in mind when using voltage dividers. These are simplifications that make evaluating a voltage dividing circuit just a little easier.

[![Vout = Vin/2 if R1=R2](//cdn.sparkfun.com/assets/8/6/0/3/2/51197073ce395f5d6d000000.png)](//cdn.sparkfun.com/assets/8/6/0/3/2/51197073ce395f5d6d000000.png)

First, **if R2 and R1 are equal** then the output voltage is **half** that of the input. This is true regardless of the resistors\' values.

[![Vout=Vin if R2\>\>R1](//cdn.sparkfun.com/assets/3/4/f/4/6/5119730dce395f2353000000.png)](//cdn.sparkfun.com/assets/3/4/f/4/6/5119730dce395f2353000000.png)

If R~2~ is *much* larger (at least an order of magnitude) than R~1~, then the output voltage will be very close to the input. There will be very little voltage across R~1~.

[![Vout=0 if R2\<\<R1](//cdn.sparkfun.com/assets/0/1/c/9/0/5119730dce395f7153000001.png)](//cdn.sparkfun.com/assets/0/1/c/9/0/5119730dce395f7153000001.png)

Conversely, if R~2~ is much smaller than R~1~, the output voltage will be tiny compared to the input. Most of the input voltage will be across R~1~

## Applications

Voltage dividers have tons of applications, they are among the most common of circuits electrical engineers use. Here are just a few of the many places you\'ll find voltage dividers.

### Potentiometers

A potentiometer is a variable resistor which can be used to create an adjustable voltage divider.

[![A variety of pots](//cdn.sparkfun.com/assets/7/9/2/b/6/511ac70dce395f3245000000.png)](//cdn.sparkfun.com/assets/7/9/2/b/6/511ac70dce395f3245000000.png)

*A smattering of potentiometers. From top-left, clockwise: [a standard 10k trimpot](https://www.sparkfun.com/products/9288), [2-axis joystick](https://www.sparkfun.com/products/9032), [softpot](https://www.sparkfun.com/products/9074), [slide pot](https://www.sparkfun.com/products/11620), [classic right-angle](https://www.sparkfun.com/products/9939), and a [breadboard friendly 10k trimpot](https://www.sparkfun.com/products/9806).*

Internal to the pot is a single resistor and a wiper, which cuts the resistor in two and moves to adjust the ratio between both halves. Externally there are usually three pins: two pins connect to each end of the resistor, while the third connects to the pot\'s wiper.

[![Schematic symbol for a potentiometer](//cdn.sparkfun.com/r/400-400/assets/6/3/e/5/e/511ac8f5ce395f5846000000.png)](//cdn.sparkfun.com/assets/6/3/e/5/e/511ac8f5ce395f5846000000.png)

*A potentiometer schematic symbol. Pins 1 and 3 are the resistor ends. Pin 2 connects to the wiper.*

If the outside pins connect to a voltage source (one to ground, the other to V~in~), the output (V~out~ at the middle pin will mimic a voltage divider. Turn the pot all the way in one direction, and the voltage may be zero; turned to the other side the output voltage approaches the input; a wiper in the middle position means the output voltage will be half of the input.

Potentiometers come in a variety of packages, and have many applications of their own. They may be used to create a reference voltage, [adjust radio stations](https://www.sparkfun.com/products/11043), measure position on a [joystick](https://www.sparkfun.com/products/9032), or in tons of other applications which require a variable input voltage.

### []Reading Resistive Sensors

Many sensors in the real world are simple resistive devices. A [photocell](https://www.sparkfun.com/products/9088) is a variable resistor, which produces a resistance proportional to the amount of light it senses. Other devices like [flex sensors](https://www.sparkfun.com/products/8606?), [force-sensitive resistors](https://www.sparkfun.com/products/9375), and [thermistors](https://www.sparkfun.com/products/250), are also variable resistors.

It turns out voltage is really easy for microcontrollers (those with [analog-to-digital converters](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) - ADC's - at least) to measure. Resistance? Not so much. But, by adding another resistor to the resistive sensors, we can create a voltage divider. Once the output of the voltage divider is known, we can go back and calculate the resistance of the sensor.

For example, the photocell\'s resistance varies between 1kΩ in the light and about 10kΩ in the dark. If we combine that with a static resistance somewhere in the middle - say 5.6kΩ, we can get a wide range out of the voltage divider they create.

[![Photocell interface schematic](//cdn.sparkfun.com/assets/7/2/a/7/5/511acd39ce395f6746000000.png)](//cdn.sparkfun.com/assets/7/2/a/7/5/511acd39ce395f6746000000.png)

*Photocell makes up half of this voltage divider. The voltage is measured to find the resistance of the light sensor.*

  ----------------- ------------------- ------------------ ---------------------------- ------------
  **Light Level**   **R~2~ (Sensor)**   **R~1~ (Fixed)**   **Ratio R~2~/(R~1~+R~2~)**   **V~out~**
  Light             1kΩ                 5.6kΩ              0.15                         0.76 V
  Dim               7kΩ                 5.6kΩ              0.56                         2.78 V
  Dark              10kΩ                5.6kΩ              0.67                         3.21 V
  ----------------- ------------------- ------------------ ---------------------------- ------------

\

A swing of about 2.45V from light to dark. Plenty of resolution for most ADCs!

### Level Shifting

More complicated sensors may transmit their readings using heavier serial interfaces, like a [UART](../serial-communication), [SPI](../serial-peripheral-interface-spi), or [I2C](https://learn.sparkfun.com/tutorials/i2c). Many of those sensors operate at a relatively low voltage, in order to conserve power. Unfortunately, it\'s not uncommon that those low-voltage sensors are ultimately interfacing with a microcontroller operating at a higher system voltage. This leads to a problem of [level shifting](https://learn.sparkfun.com/tutorials/retired---using-the-logic-level-converter), which has a number of solutions including voltage dividing.

For example, an [ADXL345 accelerometer](https://www.sparkfun.com/products/9836) allows for a maximum input voltage of 3.3V, so if you try to interface it with an Arduino (assume operating at 5V), something will need to be done to step down that 5V signal to 3.3V. Voltage divider! All that\'s needed is a couple resistors whose ratio will divide a 5V signal to about 3.3V. Resistors in the 1kΩ-10kΩ range are usually best for such an application; let\'s

[![Breadboard example of level-shifting voltage dividers](//cdn.sparkfun.com/r/600-600/assets/a/4/0/5/8/51422598ce395f010e000000.png)](//cdn.sparkfun.com/assets/4/2/6/5/e/51422598ce395ff511000000.png)

*3.3kΩ resistors (orange, orange, red) are the R~2~\'s, 1.8kΩ resistors are the R~1~\'s. An example of voltage dividers in a [breadboard](https://learn.sparkfun.com/tutorials/breadboards), level shifting 5V signals to 3.24V. (Click to see a larger view).*

Keep in mind, this solution only works in one direction. A voltage divider alone will never be able to step a lower voltage up to a higher one.

### Application Dont\'s

As tempting as it may be to use a voltage divider to step down, say, a 12V power supply to 5V, **voltage dividers should not be used to supply power to a load**.

Any current that the load requires is also going to have to run through R~1~. The current and voltage across R~1~ produce power, which is dissipated in the form of heat. If that power exceeds the rating of the resistor (usually between ⅛W and 1W), the heat begins to become a major problem, potentially melting the poor resistor.

That doesn\'t even mention how inefficient a voltage-divider-power-supply would be. Basically, don\'t use a voltage divider as a voltage supply for anything that requires even a modest amount of power. If you need to drop down a voltage to use it as a power supply, look into voltage regulators or switching supplies.

## Extra Credit: Proof

If you haven\'t yet gotten your fill of voltage dividers, in this section we\'ll evaluate how Ohm\'s law is applied to produce the voltage divider equation. This is a fun exercise, but not super-important to understanding what voltage dividers do. If you\'re interested, prepare for some fun times with Ohm\'s law and algebra.

### Evaluating the circuit

So, what if you wanted to measure the voltage at V~out~? How could Ohm\'s law be applied to create a formula to calculate the voltage there? Let\'s assume that we know the values of V~in~, R~1~, and R~2~, so let\'s get our V~out~ equation in terms of those values.

Let\'s start by drawing out the currents in the circuit\--I~1~ and I~2~\--which we\'ll call the currents across the respective resistors.

[![Standard voltage divider circuit with currents drawn in](//cdn.sparkfun.com/r/300-300/assets/c/8/8/7/7/514208cbce395f1c12000000.png)](//cdn.sparkfun.com/assets/c/8/8/7/7/514208cbce395f1c12000000.png)

Our goal is to calculate V~out~, what if we applied Ohm\'s law to that voltage? Easy enough, there\'s just one resistor and one current involved:

[![Vout = R2 \* I2](//cdn.sparkfun.com/assets/d/5/c/5/3/514208cace395f750e000000.png)](//cdn.sparkfun.com/assets/d/5/c/5/3/514208cace395f750e000000.png)

Sweet! We know R~2~\'s value, but what about I~2~? That\'s an unknown value, but we do know a little something about it. We can assume (and this turns out to be a big assumption) that **I~1~ is equivalent to I~2~**. Alright, but does that help us? Hold that thought. Our circuit now looks like this, where *I* equals both I~1~ and I~2~.

[![Voltage divider with just a single current loop](//cdn.sparkfun.com/r/300-300/assets/5/4/6/4/7/514208cace395fd711000000.png)](//cdn.sparkfun.com/assets/5/4/6/4/7/514208cace395fd711000000.png)

What do we know about V~in~? Well, V~in~ is the voltage across both resistors R~1~ and R~2~. Those resistors are in series. Series resistors add up to one value, so we could say:

[![R = R1 + R2](//cdn.sparkfun.com/assets/c/2/e/6/1/514208cace395f3510000000.png)](//cdn.sparkfun.com/assets/c/2/e/6/1/514208cace395f3510000000.png)

And, for a moment, we can simplify the circuit to:

[![Further simpling the voltage divider circuit - combining R1 and R2](//cdn.sparkfun.com/assets/b/6/a/4/b/514209a3ce395f6c11000000.png)](//cdn.sparkfun.com/assets/0/b/6/a/c/514208cace395fa10d000000.png)

Ohm\'s law at its most basic! V~in~ = I \* R. Which, if we turn that *R* back into *R~1~ + R~2~*, can also be written as:

[![I = Vin/(R1 + R2)](//cdn.sparkfun.com/assets/a/0/8/8/4/514208cace395f1c11000000.png)](//cdn.sparkfun.com/assets/a/0/8/8/4/514208cace395f1c11000000.png)

And since I is equivalent to I~2~, plug that into our V~out~ equation to get:

[![Voltage divider equation! Vout = R2 \* (Vin/(R1+R2))](//cdn.sparkfun.com/assets/1/f/2/5/d/514208cace395f1d12000000.png)](//cdn.sparkfun.com/assets/1/f/2/5/d/514208cace395f1d12000000.png)

And that, my friends, is the voltage divider equation! The output voltage is a fraction of the input voltage, and that fraction is R~2~ divided by the sum of R~1~ and R~2~.

## Interested in learning more foundational topics?

See our **[Engineering Essentials](https://www.sparkfun.com/engineering_essentials)** page for a full list of cornerstone topics surrounding electrical engineering.

[Take me there!](https://www.sparkfun.com/engineering_essentials)

![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/multimeter-300.png)