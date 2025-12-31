# Source: https://learn.sparkfun.com/tutorials/uh-oh-battery-level-indicator-hookup-guide

## Introduction

Anyone running a battery-powered project knows how frustrating it can be when a battery dies or runs too low to prevent brown-out conditions. The [TL431](https://www.sparkfun.com/products/11078) in the [Uh-Oh Battery Level Indicator Kit](https://www.sparkfun.com/products/11087) can help prevent these frustrations.

[![TL431 - Voltage Reference](https://cdn.sparkfun.com/r/600-600/assets/parts/6/4/6/8/11078-01.jpg)](https://www.sparkfun.com/products/11078)

### [TL431 - Voltage Reference](https://www.sparkfun.com/products/11078) 

[ COM-11078 ]

The TL431 is a three−terminal programmable shunt regulator diode. This monolithic IC voltage reference operates as a low te...

**Retired**

[![SparkFun \"Uh-oh\" Battery Level Indicator Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/6/4/9/5/11087-01.jpg)](https://www.sparkfun.com/products/11087)

### [SparkFun \"Uh-oh\" Battery Level Indicator Kit](https://www.sparkfun.com/products/11087) 

[ KIT-11087 ]

Under-powering a digital device can sometimes have pretty nasty consequences. Brown-out conditions can cause memory to get wr...

**Retired**

This guide will show you how to use your indicator after you have soldered it all together.

### Suggested Reading

This is a pretty basic kit, but if you need a refresher on using a multimeter, soldering, or electrical characteristics, please check out the tutorials below.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/voltage-dividers)

### Voltage Dividers 

Turn a large voltage into a smaller one with voltage dividers. This tutorial covers: what a voltage divider circuit looks like and how it is used in the real world.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/diodes)

### Diodes 

A diode primer! Diode properties, types of diodes, and diode applications.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

[](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

### How to Use a Multimeter 

Learn the basics of using a multimeter to measure continuity, voltage, resistance and current.

## Hookup Example

Once you have soldered your kit together, it\'s time to start monitoring your battery levels. For this example, we will be hooking up the indicator to a [3.7V lipo battery](https://www.sparkfun.com/products/341) that is powering an [Arduino Uno](https://www.sparkfun.com/products/11021). We will also be including a [Power Cell- LiPo Charger/Booster](https://www.sparkfun.com/products/11231) in the circuit, to ensure that we can recharge the battery when it reaches the low voltage limit.

### Connections:

Uno → PowerCell Charger

- 5V → VCC
- GND → GND

PowerCell Charger → Uh-Oh Indicator

- PowerCell + → Sys +
- PowerCell - → Sys -

Uh-Oh Indicator → Battery

- The JST connector on the battery is notched and corresponds to the notch on the Uh-Oh Indicator.

Here is a Fritzing diagram showing the actual connections between the Uno, the PowerCell, the Uh-Oh indicator, and the battery.

[![Uh-Oh Battery Indicator Hooked up to an Arduino Fritzing Diagram](https://cdn.sparkfun.com/r/500-500/assets/d/5/4/6/0/Uh-Oh_batteryHookUp_bb.jpg)](https://cdn.sparkfun.com/assets/d/5/4/6/0/Uh-Oh_batteryHookUp_bb.jpg)

[![Uh-Oh Battery Indicator Hooked up to an Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/4/Uh_Oh_Battery_Indicator_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/Uh_Oh_Battery_Indicator_Hookup_Guide-01.jpg)

Once you have everything hooked up, you will need to adjust the trimpot on the Uh-Oh indicator board to the voltage at which you would like to be notified.

## Setting the Threshold 

With everything hooked up correctly, it\'s time to fine-tune the battery indicator to your project\'s needs. To do this, you\'ll need a multimeter to read the [resistance](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/measuring-resistance) on the potentiometer, and thus set the voltage threshold at which the LED turns on.

First, if it\'s plugged in, **unplug the battery from the indicator**. We can only measure the resistance of the trimpot if there is no battery present.

There are two test points located on the board. They are label on the backside: **TP1** and **GND**.

[![test points](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/4/Uh_Oh_Battery_Indicator_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/Uh_Oh_Battery_Indicator_Hookup_Guide-02.jpg)

Grab your handy-dandy multimeter, and set it to read resistance. Place the positive probe on the TP1 point and the negative probe on GND.

[![probing test points](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/4/Uh_Oh_Battery_Indicator_Hookup_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/Uh_Oh_Battery_Indicator_Hookup_Guide-06.jpg)

Holding both probes in one hand, use your other hand to turn the potentiometer labeled \'Adj.\' Turn it until the multimeter is reading the desired resistance. Use the table below to help you find which voltage threshold you need, and thus which resistance. To calculate these values yourself or to find a value not listed on this table, visit the next section.\

  ----------------------- -------------------
  **Voltage Threshold**   **TP Resistance**
  3.0V                    8.3kΩ
  3.1V                    8.0kΩ
  3.2V                    7.8kΩ
  3.3V                    7.5kΩ
  3.4V                    7.3kΩ
  3.5V                    7.1kΩ
  3.6V                    6.9kΩ
  3.7V                    6.7kΩ
  ----------------------- -------------------

\

For example, if you want the LED to turn on when your LiPo battery reaches a voltage of 3.2V, then you need the resistance of the trimpot to be about 7.8kΩ.

[![Setting V threshold to 3.2V](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/4/Uh_Oh_Battery_Indicator_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/Uh_Oh_Battery_Indicator_Hookup_Guide-04.jpg)

## Calculating the Threshold

If you need a value not provided on the table int he previous section or if you want to better understand how the Uh-Oh Battery Indicator works, this section will go over how the indicator works.

In order to calculate the voltage threshold, we must consult the [schematic](http://cdn.sparkfun.com/datasheets/Kits/UhOh-v11_corrected.pdf) for the Uh-Oh Battery Indicator and the [datasheet](http://cdn.sparkfun.com/datasheets/Kits/TL431-D.pdf) for the TL431. These diagrams from the datasheet are particularly helpful. They show what is happening inside the TL431.

**Note that the R~1~ and R~2~ from this diagram are used in the voltage divider equation below and *NOT* the R~1~ listed on the schematic.**

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/4/datasheet.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/datasheet.jpg)

The battery indicator works as a simple [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers). The first bit of information needed is the forward voltage drop across the LED. In order to turn on, the LED needs *at least* 2.5V. This will serve as our V~out~ in the following voltage divider equation:

[![Vout = Vin \* (R2 / (R1 + R2))](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/CodeCogsEqn.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/CodeCogsEqn.gif)

\
The potentiometer used on this board is 10kΩ, so we can say

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/CodeCogsEqn_2_.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/CodeCogsEqn_2_.gif)

\
Thus,

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/res.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/res.gif)

\

After we plug those values in, we are left with this equation:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/2.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/2.gif)

\

Next, we need to figure out the V~in~. This is the value of the battery\'s voltage at which you want to be notified. For example, if you wanted the LED to turn on when the battery reaches a voltage of 3.25V, you would plug that value in for V~in~, and then solve for R~2~.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/3.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/3.gif)

\

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/4.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/4.gif)

\

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/5.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/4/5.gif)

\
Using the previous section as a guide, measure and turn the trimpot until your multimeter reads about 7,692Ω.

You can use this equation to calculate any battery voltage threshold!