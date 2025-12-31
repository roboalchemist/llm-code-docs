# Source: https://learn.sparkfun.com/tutorials/measuring-internal-resistance-of-batteries

## Introduction

Batteries are incredibly useful devices for transforming chemical reactions into electrical energy. We use them every day in things like flashlights, cars, video game controllers, and so on. To learn how batteries work, check out the following video:

To get a more in-depth explanation of batteries, see this article:

[](https://learn.sparkfun.com/tutorials/what-is-a-battery)

### What is a Battery? 

May 3, 2016

An overview of the inner workings of a battery and how it was invented.

In this tutorial, we will make a crude battery out of a lemon, a zinc-plated screw, and a copper-plated coin. The metals in the screw and the coin react with the acid in the lemon to create a flow of electrons.

Lemons, in reality, make for poor batteries. One reason is that the zinc continues to react with the lemon without a circuit present. This means that the battery would only have a shelf life of a few hours.

Another factor is the **internal resistance** of the lemon battery. We will discuss internal resistance in the next section and why it is important for batteries.

### Required Materials

[![Parts needed to make a lemon battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-01.jpg)

- Lemon
- Zinc-plated nail or screw
- Penny (or other copper-coated piece of metal)
- [AA battery](https://www.sparkfun.com/products/9100)

In addition to these materials, you will need a way to measure voltage. A [multimeter](https://www.sparkfun.com/products/12966) will offer the best accuracy, but you can also build your own voltmeter from parts found in the [SparkFun Inventor\'s Kit](https://www.sparkfun.com/products/12060).

If you want to build your own voltmeter, here is what you will need:

### Tools

In addition, you will need a [hobby knife](https://www.sparkfun.com/products/9200) to cut a slit into the lemon.

### Suggested Reading

Before continuing with this project, we suggest you be familiar with a few concepts:

- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [What is a Circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Series and Parallel Circuits](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)
- [Voltage Dividers](https://learn.sparkfun.com/tutorials/voltage-dividers)
- [How to Use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)
- [Analog to Digital Conversion](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)
- [What Is a Battery?](https://learn.sparkfun.com/tutorials/what-is-a-battery)
- [SIK Guide: Reading a Potentiometer](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-2-reading-a-potentiometer)
- [SIK Guide: Using an LCD](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-15-using-an-lcd)

## Internal Resistance

When designing a circuit with a battery, we often assume that the battery is an ideal [voltage source](https://en.wikipedia.org/wiki/Voltage_source#Ideal_voltage_sources). This means that no matter how much or little load we attach to the battery, the voltage at the source\'s terminals will always stay the same.

[![Battery as ideal voltage source](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Internal_Resistance_02a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Internal_Resistance_02a.png)

*If we model this battery as an ideal voltage source, changing the value of R~L~ does not affect the voltage between the battery\'s terminals*

In reality, several factors can limit a battery\'s ability to act as an ideal voltage source. Battery size, chemical properties, age, and temperature all affect the amount of current a battery is able to source. As a result, we can create a better model of a battery with an *ideal voltage source and a resistor in series*.

[![Battery as ideal voltage source and inline resistor](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Internal_Resistance_01a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Internal_Resistance_01a.png)

*Batteries can be modeled as an ideal voltage source with a series resistor (labeled R~I~)*

We can measure the voltage of a battery across its terminals without any load connected. This is known as the [**open-circuit voltage**](https://en.wikipedia.org/wiki/Open-circuit_voltage) (V~OC~).

[![Voltage of a AA](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-02.jpg)

*Measuring the voltage of a AA alkaline cell with no load attached*

Note that because no current is flowing across the internal resistor, the voltage drop across it is 0 V. Therefore, we can assume that V~OC~ is equal to the voltage of the ideal voltage source in the battery.

[![Open circuit voltage](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Internal_Resistance_03a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Internal_Resistance_03a.png)

If we connect a load across the battery, the voltage across the terminals drops.

[![Voltage of a loaded AA](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-03.jpg)

*In this, we are measuring the voltage drop across a 4 Ω resistor*

This drop in voltage is caused by the [internal resistance](https://en.wikipedia.org/wiki/Internal_resistance) of the battery. We can calculate the internal resistance if we take readings of the open-circuit voltage and the voltage across the battery\'s terminals with a load attached.

To start, we create a diagram showing our circuit.

[![Loaded voltage](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Internal_Resistance_04b.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Internal_Resistance_04b.png)

*Here is our circuit. We want to calculate R~I~.*

We can plug in the loaded voltage we measured (V~L~) and the value of the resistor (R~L~) into Ohm\'s Law to get the current flowing through the circuit (I).

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_01.png)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_02a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_02a.png)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_03.png)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_04.png)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_05.png)

We also need to get the voltage across the internal resistor. We can do that using [Kirchhoff\'s Voltage Law](http://www.allaboutcircuits.com/textbook/direct-current/chpt-6/kirchhoffs-voltage-law-kvl/). Simplified for this circuit, we can say that the voltage drop across both resistors must add up to the voltage of the ideal voltage source.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_06.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_06.png)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_07.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_07.png)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_08.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_08.png)

Now that we know the voltage drop across the internal resistor and the current through it, we can use Ohm\'s Law again to find its resistance.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_09.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_09.png)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_10.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_10.png)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_11.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Eqn_11.png)

From this, we can see that the internal resistance (at this moment) of the AA cell is **0.273 Ω**.

**NOTE**: We can only take a snapshot of the internal resistance with this method. The internal resistance can vary with things like battery age and temperature. In 10 minutes, the resistance value might be different! A common AA alkaline battery might have anywhere between 0.1 Ω and 0.9 Ω internal resistance.

## Build a Voltmeter

**NOTE**: This part is optional if you already have access to a voltmeter or multimeter. That being said, it can be fun to build a voltmeter to understand how to use an analog-to-digital converter.

### Hardware Hookup

Connect the components as shown in the Fritzing diagram:

[![SIK voltmeter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/sik_voltmeter_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/sik_voltmeter_bb.png)

*Having a hard time seeing the circuit? Click on the Fritzing diagram to see a bigger image.*

Once you are done, you should have 2 wires hanging out from the side of your breadboard. These will be your probes for testing voltage across terminals.

Note that we have a 330 Ω resistor across the probes. This will act as our load for the first test.

### The Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /**
     * SparkFun Inventor's Kit Project
     * Voltmeter
     * Date: May 3, 2016
     * 
     * Description:
     *  Connect a resistor between A0 and GND to measure the loaded
     *  voltage across a voltage source, such as a battery. Remove
     *  the resistor to measure the open circuit voltage.
     *  
     *  NOTE: The voltmeter is only capable of sensing 0 - 5V.
     *  
     * License:
     *  Public Domain
     */

    #include <LiquidCrystal.h>

    // Constants
    int VOLTAGE_PIN = A0;

    // Global variables
    LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

    void setup() 

    void loop() 

### What You Should See

Once you have uploaded the code to the RedBoard, try touching the ends of the probes across the terminals of the AA battery. You should see a voltage reading appear on the LCD.

**IMPORTANT**: The voltmeter we just made cannot sense negative voltages! Make sure you touch the A0 probe (red wire) to the positive (+) terminal of the battery and the GND probe (black wire) to the negative (-) terminal of the battery.

[![Reading the voltage of a AA battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-07.jpg)

**NOTE**: If you cannot see text on the LCD, try turning the potentiometer\'s knob to adjust the LCD\'s contrast.

## Build a Lemon Battery

We get to build a battery! This is a crude fruit-based battery that will not last very long nor drive much current. However, it is useful for measuring internal resistance.

**IMPORTANT**: Please don\'t eat the fruit after you have made the battery! Zinc ions that are floating in the lemon juice certainly can\'t be healthy for you.

Insert the zinc screw or nail into one side of the lemon.

[![Make the anode in the lemon battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-04.jpg)

Use the hobby knife to cut a slit in the other end of the lemon.

[![Cut a slit for the penny](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-05.jpg)

Insert a penny into the slit so that half of the penny is still outside the lemon\'s skin.

[![Insert penny to make the cathode](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-06.jpg)

And that\'s it! We successfully created a battery. Make sure that the penny and screw cannot touch each other, or you will create a short circuit between the electrodes. While the short circuit will not start any fires, it will not produce a voltage for our experiments.

**NOTE**: If you would like the battery to last longer than a few hours, remove the screw. Even without a circuit connected, the screw will continue to oxidize in the presence of the lemon juice.

## Take Voltage Measurements

### Measurement Sheet

Create a table for recording voltages:

  --------------- ------------ ------------ --------------
  Voltages        330 Ω Load   10k Ω Load   Open Circuit
  Lemon Battery                             
  --------------- ------------ ------------ --------------

### 330 Ω Load

Touch the negative probe (black wire in the picture) to the anode (nail/screw) on the battery, and touch the positive probe (red wire in the picture) to the cathode (penny) terminal on the battery. Record the voltage under \"330 Ω Load.\"

[![Loaded voltage of the lemon battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-08.jpg)

**NOTE**: If you are using a multimeter for this exercise, we recommend using something like [alligator test leads](https://www.sparkfun.com/products/12978) to hold the resistor across the electrodes of the battery.

### 10k Ω Load

Replace the 330 Ω resistor with a 10k Ω. Repeat the process to measure the voltage across the battery. Record the voltage under \"10k Ω Load.\"

### Open Circuit Voltage

Remove the resistor from the breadboard and take another measurement. Record the voltage under \"Open Circuit.\"

[![Open circuit voltage of the lemon battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/7/Measuring_Internal_Resistance-09.jpg)

## Calculate the Internal Resistance

Using the voltage readings from the \"10k Ω Load\" and the \"No Load\" (open circuit), calculate the internal resistance of the lemon battery.

*Hint*: Refer to the [Internal Resistance](https://learn.sparkfun.com/tutorials/measuring-internal-resistance-of-batteries#internal-resistance) section to see how to calculate this value.

### Questions

1.  Does the internal resistance of the lemon battery seem high or low?
2.  What is the maximum current your lemon battery can provide? (*Hint*: imagine connecting a wire between the terminals. How much current would flow through the circuit?)
3.  Re-calculate the internal resistance using the \"330 Ω Load\" and \"No Load\" values. Does it match your first calculation? If not, what do you think would cause the difference?
4.  Perform the whole experiment again using a consumer-grade battery, such as a AA alkaline cell. What is the maximum current a AA can provide?