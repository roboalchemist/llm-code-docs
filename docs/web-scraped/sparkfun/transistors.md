# Source: https://learn.sparkfun.com/tutorials/transistors

## Introduction

Transistors make our electronics world go \'round. They\'re critical as a control source in just about every modern circuit. Sometimes you see them, but more-often-than-not they\'re hidden deep within the die of an [integrated circuit](https://learn.sparkfun.com/tutorials/integrated-circuits). In this tutorial we\'ll introduce you to the basics of the most common transistor around: the bi-polar junction transistor (BJT).

[![Introduction image](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/intro.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/intro.png)

In small, discrete quantities, transistors can be used to create simple electronic switches, [digital logic](https://learn.sparkfun.com/tutorials/digital-logic), and signal amplifying circuits. In quantities of thousands, millions, and even billions, transistors are interconnected and embedded into tiny chips to create computer memories, microprocessors, and other complex ICs.

### Covered In This Tutorial

After reading through this tutorial, we want you to have a broad understanding of how transistors work. We won\'t dig too deeply into semiconductor physics or equivalent models, but we\'ll get deep enough into the subject that you\'ll understand how a transistor can be **used as either a switch or amplifier**.

This tutorial is split into a series of sections, covering:

- [Symbols, Pins, and Construction](https://learn.sparkfun.com/tutorials/transistors/symbols-pins-and-construction) \-- Explaining the differences between the transistor\'s three pins.
- [Extending the Water Analogy](https://learn.sparkfun.com/tutorials/transistors/extending-the-water-analogy) \-- Going back to the water analogy to explain how a transistor acts like a valve.
- [Operation Modes](https://learn.sparkfun.com/tutorials/transistors/operation-modes) \-- An overview of the four possible operating modes of a transistor.
- [Applications I: Switches](https://learn.sparkfun.com/tutorials/transistors/applications-i-switches) \-- Application circuits showing how transistors are used as electronically controlled switches.
- [Applications II: Amplifiers](https://learn.sparkfun.com/tutorials/transistors/applications-ii-amplifiers) \-- More application circuits, this time showing how transistors are used to amplify voltage or current.

There are two types of basic transistor out there: bi-polar junction (BJT) and metal-oxide field-effect (MOSFET). In this tutorial we\'ll **focus on the BJT**, because it\'s slightly easier to understand. Digging even deeper into transistor types, there are actually two versions of the BJT: **NPN** and **PNP**. We\'ll turn our focus even sharper by limiting our early discussion to the NPN. By narrowing our focus down \-- getting a solid understanding of the NPN \-- it\'ll be easier to understand the PNP (or MOSFETS, even) by comparing how it differs from the NPN.

 

![Field Guide to Transistors](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/transistors.png)

 

### Suggested Reading

Before digging into this tutorial, we\'d highly recommend giving these tutorials a look-through:

- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) \-- An introduction to the fundamentals of electronics.
- [Electricity Basics](https://learn.sparkfun.com/tutorials/what-is-electricity) \-- We\'ll talk a bit about electricity as the flow of electrons. Find out how those electrons flow in this tutorial.
- [Electric Power](https://learn.sparkfun.com/tutorials/electric-power) \-- One of the transistors main applications is amplifying \-- increasing the power of a signal. Increasing power means we can increase either current or voltage, find out why in this tutorial.
- [Diodes](https://learn.sparkfun.com/tutorials/diodes) \-- A transistor is a semiconductor device, just like a diode. In a way, it\'s what you\'d get if you stacked two diodes together, and tied their anodes together. Understanding how a diode works will go a long way towards uncovering the operation of a transistor.

## Looking to explore transistors?

We\'ve got you covered!

[![SparkFun Discrete Semiconductor Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/3/5/13682-01.jpg)](https://www.sparkfun.com/sparkfun-discrete-semiconductor-kit.html)

### [SparkFun Discrete Semiconductor Kit](https://www.sparkfun.com/sparkfun-discrete-semiconductor-kit.html) 

[ KIT-13682 ]

The SparkFun Discrete Semiconductor Kit addresses your needs of only needing one or a couple transistors without you needing ...

[ [\$19.50] ]

[![Transistor - NPN, 50V 800mA (BC337)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/5/9/13689-01.jpg)](https://www.sparkfun.com/transistor-npn-50v-800ma-bc337.html)

### [Transistor - NPN, 50V 800mA (BC337)](https://www.sparkfun.com/transistor-npn-50v-800ma-bc337.html) 

[ COM-13689 ]

This is the BC337, an NPN silicon BJT (Bipolar Junction Transistor). This little transistor can help in your project by being...

[ [\$0.55] ]

[![Transistor - NPN, 60V 200mA (2N3904)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/9/00521-1.jpg)](https://www.sparkfun.com/transistor-npn-60v-200ma-2n3904.html)

### [Transistor - NPN, 60V 200mA (2N3904)](https://www.sparkfun.com/transistor-npn-60v-200ma-2n3904.html) 

[ COM-00521 ]

These are very common, high quality BJT NPN transistors made by ST Micro.

[ [\$0.55] ]

[![SparkFun Beginner Parts Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/1/5/13973-SparkFun_Beginner_Parts_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-beginner-parts-kit.html)

### [SparkFun Beginner Parts Kit](https://www.sparkfun.com/sparkfun-beginner-parts-kit.html) 

[ KIT-13973 ]

The SparkFun Beginner Parts Kit is a small container of frequently used parts that gives you all of the basic components you...

**Retired**

[See all transistors](https://www.sparkfun.com/categories/352)

------------------------------------------------------------------------

## Symbols, Pins, and Construction

Transistors are fundamentally three-terminal devices. On a bi-polar junction transistor (BJT), those pins are labeled **collector** (C), **base** (B), and **emitter** (E). The circuit symbols for both the NPN and PNP BJT are below:

[![NPN and PNP symbols](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/npn-pnp-symbols.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/npn-pnp-symbols.png)

The only difference between an NPN and PNP is the direction of the arrow on the emitter. The arrow on an NPN points out, and on the PNP it points in. A useful mnemonic for remembering which is which is:

## NPN: **N**ot **P**ointing i**N**

Backwards logic, but it works!

### Transistor Construction

Transistors rely on semiconductors to work their magic. A semiconductor is a material that\'s not quite a pure conductor (like copper wire) but also not an insulator (like air). The conductivity of a semiconductor \-- how easily it allows electrons to flow \-- depends on variables like temperature or the presence of more or less electrons. Let\'s look briefly under the hood of a transistor. Don\'t worry, we won\'t dig too deeply into quantum physics.

#### A Transistor as Two Diodes

Transistors are kind of like an extension of another semiconductor component: [diodes](https://learn.sparkfun.com/tutorials/diodes). In a way transistors are just two diodes with their cathodes (or anodes) tied together:

[![Transistors as two diodes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/transistors-as-diodes.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/transistors-as-diodes.png)

The diode connecting base to emitter is the important one here; it matches the direction of the arrow on the schematic symbol, and shows you **which way current is intended to flow** through the transistor.

The diode representation is a good place to start, but it\'s far from accurate. Don\'t base your understanding of a transistor\'s operation on that model (and definitely don\'t try to replicate it on a breadboard, it won\'t work). There\'s a whole lot of weird quantum physics level stuff controlling the interactions between the three terminals.

(This model *is* useful if you need to test a transistor. Using the diode (or resistance) test function on a [multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter), you can measure across the BE and BC terminals to check for the presence of those \"diodes\".)

#### Transistor Structure and Operation

Transistors are built by stacking three different layers of semiconductor material together. Some of those layers have extra electrons added to them (a process called \"doping\"), and others have electrons removed (doped with \"holes\" \-- the absence of electrons). A semiconductor material with *extra* electrons is called an **n-type** (*n* for negative because electrons have a negative charge) and a material with electrons removed is called a **p-type** (for positive). Transistors are created by either stacking an *n* on top of a *p* on top of an *n*, or *p* over *n* over *p*.

[![Simplified NPN construction](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/transistor-construction.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/transistor-construction.png)

*Simplified diagram of the structure of an NPN. Notice the origin of any acronyms?*

With some hand waving, we can say **electrons can easily flow from *n* regions to *p* regions**, as long as they have a little force (voltage) to push them. But flowing from a *p* region to an *n* region is really hard (requires a *lot* of voltage). But the special thing about a transistor \-- the part that makes our two-diode model obsolete \-- is the fact that **electrons *can* easily flow from the p-type base to the n-type collector as long as the base-emitter junction is forward biased** (meaning the base is at a higher voltage than the emitter).

[![Active transistor current flow](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/transistor-active-electrons.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/transistor-active-electrons.png)

The NPN transistor is designed to pass electrons from the emitter to the collector (so conventional current flows from collector to emitter). The emitter \"emits\" electrons into the base, which controls the number of electrons the emitter emits. Most of the electrons emitted are \"collected\" by the collector, which sends them along to the next part of the circuit.

A PNP works in a same but opposite fashion. The base still controls current flow, but that current flows in the opposite direction \-- from emitter to collector. Instead of electrons, the emitter emits \"holes\" (a conceptual absence of electrons) which are collected by the collector.

The transistor is kind of like an **electron valve**. The base pin is like a handle you might adjust to allow more or less electrons to flow from emitter to collector. Let\'s investigate this analogy further\...

------------------------------------------------------------------------

## Extending the Water Analogy

If you\'ve been reading a lot of electricity concept tutorials lately, you\'re probably used to [water](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc/alternating-current-ac) [analogies](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/voltage). We say that current is analogous to the flow rate of water, voltage is the pressure pushing that water through a pipe, and resistance is the width of the pipe.

[![water analogies for current, voltage, and resistance](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/water-analogy.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/water-analogy.png)

Unsurprisingly, the water analogy can be extended to transistors as well: a transistor is like a water **valve** \-- a mechanism we can use to **control the flow rate**.

There are three states we can use a valve in, each of which has a different effect on the flow rate in a system.

### 1) On \-- Short Circuit

A valve can be completely opened, allowing water to **flow freely** \-- passing through as if the valve wasn\'t even present.

[![Valve open, water flowing, short circuit](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/water-on.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/water-on.png)

Likewise, under the right circumstances, a transistor can look like a **short circuit** between the collector and emitter pins. Current is free to flow through the collector, and out the emitter.

### 2) Off \-- Open Circuit

When it\'s closed, a valve can completely **stop the flow** of water.

[![valve closed, water stopped, open circuit](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/water-off.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/water-off.png)

In the same way, a transistor can be used to create an **open circuit** between the collector and emitter pins.

### 3) Linear Flow Control

With some precise tuning, a valve can be adjusted to finely **control the flow rate** to some point between fully open and closed.

[![Valve half-open, water flow rate controlled](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/water-control.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/water-control.png)

A transistor can do the same thing \-- **linearly controlling the current** through a circuit at some point between fully off (an open circuit) and fully on (a short circuit).

From our water analogy, the width of a pipe is similar to the [resistance](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/resistance) in a circuit. If a valve can finely adjust the width of a pipe, then a transistor can finely adjust the resistance between collector and emitter. So, in a way, a transistor is like a **variable, adjustable resistor**.

### Amplifying Power

There\'s another analogy we can wrench into this. Imagine if, with the slight turn of a valve, you could control the flow rate of the [Hoover Dam\'s flow gates](http://en.wikipedia.org/wiki/File:HooverDamFrontWater.jpg). The measly amount of force you might put into twisting that knob has the potential to create a force thousands of times stronger. We\'re stretching the analogy to its limits, but this idea carries over to transistors too. Transistors are special because they can **amplify** electrical signals, turning a low-power signal into a similar signal of much higher power.

------------------------------------------------------------------------

Kind of. There\'s a lot more to it, but that\'s a good place to start! Check out the next section for a more detailed explanation of the operation of a transistor.

------------------------------------------------------------------------

## Operation Modes

Unlike [resistors](https://learn.sparkfun.com/tutorials/resistors), which enforce a linear relationship between voltage and current, transistors are non-linear devices. They have four distinct modes of operation, which describe the current flowing through them. (When we talk about current flow through a transistor, we usually mean **current flowing from collector to emitter of an NPN**.)

The four transistor operation modes are:

- **Saturation** \-- The transistor acts like a **short circuit**. Current freely flows from collector to emitter.
- **Cut-off** \-- The transistor acts like an **open circuit**. No current flows from collector to emitter.
- **Active** \-- The current from collector to emitter is **proportional** to the base current.
- **Reverse-Active** \-- Like active mode, the current is proportional to the base current, but it flows in reverse. Current flows from emitter to collector (not, exactly, the purpose transistors were designed for).

To determine which mode a transistor is in, we need to look at the voltages on each of the three pins, and how they relate to each other. The voltages from base to emitter (V~BE~), and the from base to collector (V~BC~) set the transistor\'s mode:

[![Mode Quadrants](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/mode-quadrants.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/mode-quadrants.png)

The simplified quadrant graph above shows how positive and negative voltages at those terminals affect the mode. In reality it\'s a bit more complicated than that.

Let\'s look at all four transistor modes individually; we\'ll investigate how to put the device into that mode, and what effect it has on current flow.

**Note:** The majority of this page focuses on **NPN transistors**. To understand how a PNP transistor works, simply flip the polarity or \> and \< signs.

#### Saturation Mode

Saturation is the **on mode** of a transistor. A transistor in saturation mode acts like a short circuit between collector and emitter.

[![Saturation mode model](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/3/mode_saturation-model.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/mode_saturation-model.png)

In saturation mode both of the \"diodes\" in the transistor are forward biased. That means V~BE~ must be greater than 0, *and* so must V~BC~. In other words, V~B~ must be higher than both V~E~ and V~C~.

[![Saturation mode voltage relations](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-saturation-voltages.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-saturation-voltages.png)

Because the junction from base to emitter looks just like a [diode](https://learn.sparkfun.com/tutorials/diodes/real-diode-characteristics#forward_drop), in reality, V~BE~ must be greater than a **threshold voltage** to enter saturation. There are many abbreviations for this voltage drop \-- V~th~, V~γ~, and V~d~ are a few \-- and the actual value varies between transistors (and even further by temperature). For a lot of transistors (at room temperature) we can estimate this drop to be about 0.6V.

Another reality bummer: there won\'t be perfect conduction between emitter and collector. A small voltage drop will form between those nodes. Transistor datasheets will define this voltage as **CE saturation voltage V~CE(sat)~** \-- a voltage from collector to emitter required for saturation. This value is usually around 0.05-0.2V. This value means that V~C~ must be slightly greater than V~E~ (but both still less than V~B~) to get the transistor in saturation mode.

#### Cutoff Mode

Cutoff mode is the opposite of saturation. A transistor in cutoff mode is **off** \-- there is no collector current, and therefore no emitter current. It almost looks like an open circuit.

[![Cutoff mode model](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/3/mode_cutoff-model.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/mode_cutoff-model.png)

To get a transistor into cutoff mode, the base voltage must be less than both the emitter and collector voltages. V~BC~ and V~BE~ must both be negative.

[![Cutoff mode voltage relations](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-cutoff_voltages.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-cutoff_voltages.png)

In reality, V~BE~ can be anywhere between 0V and V~th~ (\~0.6V) to achieve cutoff mode.

#### Active Mode

To operate in active mode, a transistor\'s V~BE~ must be greater than zero and V~BC~ must be negative. Thus, the base voltage must be less than the collector, but greater than the emitter. That also means the collector must be greater than the emitter.

[![V\_ \> V\_ \> V\_](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-active_voltages.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-active_voltages.png)

In reality, we need a non-zero **forward voltage drop** (abbreviated either V~th~, V~γ~, or V~d~) from base to emitter (V~BE~) to \"turn on\" the transistor. Usually this voltage is usually around 0.6V.

##### Amplifying in Active Mode

Active mode is the most powerful mode of the transistor because it turns the device into an **amplifier**. Current going into the base pin amplifies current going into the collector and out the emitter.

Our shorthand notation for the **gain** (amplification factor) of a transistor is *β* (you may also see it as *β~F~*, or *h~FE~*). β linearly relates the collector current (*I~C~*) to the base current (*I~B~*):

[![I\_ = \\beta I\_](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/beta_equation_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/beta_equation_1.png)

The actual value of *β* varies by transistor. It\'s usually **around 100**, but can range from 50 to 200\...even 2000, depending on which transistor you\'re using and how much current is running through it. If your transistor had a β of 100, for example, that\'d mean an input current of 1mA into the base could produce 100mA current through the collector.

[![Active mode model](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/3/mode-active-model_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/mode-active-model_2.png)

*Active mode model. V~BE~ = V~th~, and I~C~ = βI~B~.*

What about the emitter current, I~E~? In active mode, the collector and base currents go *into* the device, and the I~E~ comes out. To relate the emitter current to collector current, we have another constant value: **α**. α is the common-base current gain, it relates those currents as such:

[![I\_= \\alpha I\_](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/alpha_equation_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/alpha_equation_2.png)

α is usually *very* close to, but less than, 1. That means ***I~C~* is very close to, but less than *I~E~*** in active mode.

You can use β to calculate α, or vice-versa:

[![\\beta=\\frac](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/alpha_beta_equation_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/alpha_beta_equation_1.png)

If β is 100, for example, that means α is 0.99. So, if I~C~ is 100mA, for example, then I~E~ is 101mA.

#### Reverse Active

Just as saturation is the opposite of cutoff, reverse active mode is the opposite of active mode. A transistor in reverse active mode conducts, even amplifies, but current flows in the opposite direction, from emitter to collector. The downside to reverse active mode is the β (β~R~ in this case) is *much* smaller.

To put a transistor in reverse active mode, the emitter voltage must be greater than the base, which must be greater than the collector (V~BE~\<0 and V~BC~\>0).

[![V\_ \< V\_ \< V\_](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-reverse-voltage-3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-reverse-voltage-3.png)

Reverse active mode isn\'t usually a state in which you want to drive a transistor. It\'s good to know it\'s there, but it\'s rarely designed into an application.

### Relating to the PNP

After everything we\'ve talked about on this page, we\'ve still only covered half of the BJT spectrum. What about PNP transistors? PNP\'s work a lot like the NPN\'s \-- they have the same four modes \-- but everything is turned around. To find out which mode a PNP transistor is in, reverse all of the \< and \> signs.

For example, to put a PNP into saturation V~C~ and V~E~ must be higher than V~B~. You pull the base low to turn the PNP on, and make it higher than the collector and emitter to turn it off. And, to put a PNP into active mode, V~E~ must be at a higher voltage than V~B~, which must be higher than V~C~.

In summary:

Voltage relations

NPN Mode

PNP Mode

V~E~ \< V~B~ \< V~C~

Active

Reverse

V~E~ \< V~B~ \> V~C~

Saturation

Cutoff

V~E~ \> V~B~ \< V~C~

Cutoff

Saturation

V~E~ \> V~B~ \> V~C~

Reverse

Active

\

Another opposing characteristic of the NPNs and PNPs is the direction of current flow. In active and saturation modes, **current in a PNP flows from emitter to collector**. This means the emitter must generally be at a higher voltage than the collector.

------------------------------------------------------------------------

If you\'re burnt out on conceptual stuff, take a trip to the next section. The best way to learn how a transistor works is to examine it in real-life circuits. Let\'s look at some applications!

------------------------------------------------------------------------

## Applications I: Switches

One of the most fundamental applications of a transistor is using it to control the flow of power to another part of the circuit \-- using it as an electric switch. Driving it in either cutoff or saturation mode, the transistor can create the binary on/off effect of a switch.

Transistor switches are critical circuit-building blocks; they\'re used to make [logic gates](https://learn.sparkfun.com/tutorials/digital-logic), which go on to create microcontrollers, microprocessors, and other [integrated circuits](https://learn.sparkfun.com/tutorials/integrated-circuits). Below are a few example circuits.

### Transistor Switch

Let\'s look at the most fundamental transistor-switch circuit: an NPN switch. Here we use an NPN to control a high-power LED:

[![NPN switch to control an LED](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/3/npn-switch-led.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/npn-switch-led.png)

Our control input flows into the base, the output is tied to the collector, and the emitter is kept at a fixed voltage.

While a [normal switch](https://learn.sparkfun.com/tutorials/button-and-switch-basics) would require an actuator to be physically flipped, this switch is controlled by the voltage at the base pin. A microcontroller I/O pin, like those on an [Arduino](https://learn.sparkfun.com/tutorials/what-is-an-arduino), can be programmed to go high or low to turn the LED on or off.

When the voltage at the base is greater than 0.6V (or whatever your transistor\'s V~th~ might be), the transistor starts saturating and looks like a short circuit between collector and emitter. When the voltage at the base is less than 0.6V the transistor is in cutoff mode \-- no current flows because it looks like an open circuit between C and E.

The circuit above is called a **low-side switch**, because the switch \-- our transistor \-- is on the low (ground) side of the circuit. Alternatively, we can use a PNP transistor to create a high-side switch:

[![PNP switch example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/pnp-switch-motor_3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/pnp-switch-motor_3.png)

Similar to the NPN circuit, the base is our input, and the emitter is tied to a constant voltage. This time however, the emitter is tied high, and the load is connected to the transistor on the ground side.

This circuit works just as well as the NPN-based switch, but there\'s one huge difference: to turn the load \"on\", the base must be low. This can cause complications, especially if the load\'s high voltage (V~CC~ being 12V connecting to the emitter V~E~ in this picture) is higher than our control input\'s high voltage. For example, this circuit wouldn\'t work if you were trying to use a 5V-operating Arduino to switch off a 12V motor. In that case, it\'d be **impossible to turn the switch off** because V~B~ (connecting to the control pin) would always be less than V~E~ .

#### Base Resistors!

You\'ll notice that each of those circuits uses a series resistor between the control input and the base of the transistor. Don\'t forget to add this resistor! A transistor without a resistor on the base is like an LED with no [current-limiting resistor](https://learn.sparkfun.com/tutorials/resistors/example-applications#current-limiting).

Recall that, in a way, a transistor is just a pair of interconnected diodes. We\'re forward-biasing the base-emitter diode to turn the load on. The diode only needs 0.6V to turn on, more voltage than that means more current. Some transistors may only be rated for a maximum of 10-100mA of current to flow through them. If you supply a current over the maximum rating, the transistor might blow up.

The series resistor between our control source and the base **limits current into the base**. The base-emitter node can get its happy voltage drop of 0.6V, and the resistor can drop the remaining voltage. The value of the resistor, and voltage across it, will set the current.

[![Switching an LED with a transistor](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/switch-animated-600h.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/switch-animated-600h.gif)

The resistor needs to be large enough to effectively *limit* the current, but small enough to feed the base *enough* current. 1mA to 10mA will usually be enough, but check your transistor\'s datasheet to make sure.

### Digital Logic

Transistors can be combined to create all our fundamental [logic gates](https://learn.sparkfun.com/tutorials/digital-logic): AND, OR, and NOT.

(Note: These days MOSFETS are more likely to be used to create logic gates than BJTs. MOSFETs are more power-efficient, which makes them the better choice.)

#### Inverter

Here\'s a transistor circuit that implements an **inverter**, or NOT gate:

[![BJT inverter circuit](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/3/logic-inverter-circuit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/logic-inverter-circuit.png)

*An inverter built out of transistors.*

Here a high voltage into the base will turn the transistor on, which will effectively connect the collector to the emitter. Since the emitter is connected directly to ground, the collector will be as well (though it will be slightly higher, somewhere around V~CE(sat)~ \~ 0.05-0.2V). If the input is low, on the other hand, the transistor looks like an open circuit, and the output is pulled up to VCC

(This is actually a fundamental transistor configuration called **common emitter**. More on that later.)

#### AND Gate

Here are a pair of transistors used to create a **2-input AND gate**:

[![BJT AND circuit](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/3/logic-and-circuit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/logic-and-circuit.png)

*2-input AND gate built out of transistors.*

If either transistor is turned off, then the output at the second transistor\'s collector will be pulled low. If both transistors are \"on\" (bases both high), then the output of the circuit is also high.

#### OR Gate

And, finally, here\'s a **2-input OR gate**:

[![BJT OR circuit](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/3/logic-circuit-or.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/logic-circuit-or.png)

*2-input OR gate built out of transistors.*

In this circuit, if either (or both) A or B are high, that respective transistor will turn on, and pull the output high. If both transistors are off, then the output is pulled low through the resistor.

### H-Bridge

An H-bridge is a transistor-based circuit capable of **driving motors both clockwise and counter-clockwise**. It\'s an incredibly popular circuit \-- the driving force behind countless robots that must be able to move both forward *and* backward.

Fundamentally, an H-bridge is a combination of four transistors with two inputs lines and two outputs:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/h-bridge-circuit-600w.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/h-bridge-circuit-600w.gif)

*Can you guess why it\'s called an H bridge?*

(Note: there\'s usually quite a bit more to a well-designed H-bridge including flyback diodes, base resistors and Schmidt triggers.)

If both inputs are the same voltage, the outputs to the motor will be the same voltage, and the motor won\'t be able to spin. But if the two inputs are opposite, the motor will spin in one direction or the other.

The H-bridge has a truth table that looks a little like this:

  Input A   Input B   Output A   Output B   Motor Direction
  --------- --------- ---------- ---------- -------------------
  0         0         1          1          Stopped (braking)
  0         1         1          0          Clockwise
  1         0         0          1          Counter-clockwise
  1         1         0          0          Stopped (braking)

\

### Oscillators

An oscillator is a circuit that produces a periodic signal that swings between a high and low voltage. Oscillators are used in all sorts of circuits: from simply blinking an LED to the producing a clock signal to drive a microcontroller. There are lots of ways to create an oscillator circuit including quartz crystals, op amps, and, of course, transistors.

Here\'s an example oscillating circuit, which we call an **astable multivibrator**. By using **feedback** we can use a pair of transistors to create two complementing, oscillating signals.

[![Astable multivibrator](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/astable-multivibrator.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/astable-multivibrator.png)

Aside from the two transistors, the [capacitors](https://learn.sparkfun.com/tutorials/capacitors) are the real key to this circuit. The caps alternatively charge and discharge, which causes the two transistors to alternatively turn on and off.

Analyzing this circuit\'s operation is an excellent study in the operation of both caps and transistors. To begin, assume C1 is fully charged (storing a voltage of about V~CC~), C2 is discharged, Q1 is on, and Q2 is off. Here\'s what happens after that:

- If Q1 is on, then C1\'s left plate (on the schematic) is connected to about 0V. This will allow C1 to discharge through Q1\'s collector.
- While C1 is discharging, C2 quickly charges through the lower value resistor \-- R4.
- Once C1 fully discharges, its right plate will be pulled up to about 0.6V, which will turn on Q2.
- At this point we\'ve swapped states: C1 is discharged, C2 is charged, Q1 is off, and Q2 is on. Now we do the same dance the other way.
- Q2 being on allows C2 to discharge through Q2\'s collector.
- While Q1 is off, C1 can charge, relatively quickly through R1.
- Once C2 fully discharges, Q1 will be turn back on and we\'re back in the state we started in.

It can be hard to wrap your head around. You can find another excellent demo of this circuit [here](http://www.falstad.com/circuit/#%24+1+5.0E-6+81.92041607667615+68+5.0+50%0Ar+224+160+224+240+0+330.0%0Ar+304+160+304+240+0+47000.0%0Ar+384+160+384+240+0+47000.0%0Ar+464+160+464+240+0+330.0%0Ac+224+240+304+240+0+9.999999999999999E-6+1.4320522416531634%0Ac+384+240+464+240+0+9.999999999999999E-6+-3.032536053591649%0Aw+464+240+464+304+0%0At+384+320+464+320+0+1+-4.9331229468694815+-1.2687826252387493+100.0%0Aw+304+240+384+320+0%0Aw+384+240+304+320+0%0At+304+320+224+320+0+1+0.4685346516246693+0.6318042680390833+100.0%0Aw+224+240+224+304+0%0Ag+224+336+224+368+0%0Ag+464+336+464+368+0%0Ax+255+276+276+280+0+16+C1%0Ax+413+277+434+281+0+16+C2%0Ax+192+324+213+328+0+16+Q1%0Ax+478+326+499+330+0+16+Q2%0A162+464+96+464+160+1+2.1024259+1.0+0.0+0.0%0A162+224+96+224+160+1+2.1024259+1.0+0.0+0.0%0AR+176+96+176+128+0+0+40.0+5.0+0.0+0.0+0.5%0Aw+176+96+224+96+0%0Aw+224+96+304+96+0%0Aw+304+96+304+160+0%0Aw+304+96+384+96+0%0Aw+384+96+384+160+0%0Aw+384+96+464+96+0%0Ao+10+64+6+35+1.25+9.765625E-5+0+-1%0Ao+7+64+6+35+5.0+9.765625E-5+1+-1%0Ao+5+64+0+35+5.0+1.953125E-4+2+-1%0A).

By picking specific values for C1, C2, R2, and R3 (and keeping R1 and R4 relatively low), we can set the speed of our multivibrator circuit:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-astable-multivibrator.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/equation-astable-multivibrator.png)

So, with the values for caps and resistors set to 10µF and 47kΩ respectively, our oscillator frequency is about 1.5 Hz. That means each LED will blink about 1.5 times per second.

------------------------------------------------------------------------

As you can probably already see, there are *tons* of circuits out there that make use of transistors. But we\'ve barely scratched the surface. These examples mostly show how the transistor can be used in saturation and cut-off modes as a switch, but what about amplification? Time for more examples!

------------------------------------------------------------------------

## Applications II: Amplifiers

Some of the most powerful transistor applications involve amplification: turning a low power signal into one of higher power. Amplifiers can increase the voltage of a signal, taking something from the µV range and converting it to a more useful mV or V level. Or they can amplify current, useful for turning the µA of current produced by a [photodiode](https://www.sparkfun.com/products/9541) into a current of much higher magnitude. There are even amplifiers that take a current in, and produce a higher voltage, or vice-versa (called transresistance and transconductance respectively).

Transistors are a key component to many amplifying circuits. There are a seemingly infinite variety of transistor amplifiers out there, but fortunately a lot of them are based on some of these more primitive circuits. Remember these circuits, and, hopefully, with a bit of pattern-matching, you can make sense of more complex amplifiers.

### Common Configurations

Three of the most fundamental transistor amplifiers are: common emitter, common collector and common base. In each of the three configurations one of the three nodes is permanently tied to a common voltage (usually ground), and the other two nodes are either an input or output of the amplifier.

#### Common Emitter

Common emitter is one of the more popular transistor arrangements. In this circuit the emitter is tied to a voltage common to both the base and collector (usually ground). The base becomes the signal input, and the collector becomes the output.

[![Common emitter model](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/common-emitter-model.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/common-emitter-model.png)

The common emitter circuit is popular because it\'s well-suited for **voltage amplification**, especially at low frequencies. They\'re great for amplifying audio signals, for example. If you have a small 1.5V peak-to-peak input signal, you could amplify that to a much higher voltage using a slightly more complicated circuit, like:

[![Common emitter speaker amp](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/common-emitter-speaker-amplifier-02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/common-emitter-speaker-amplifier-02.png)

One quirk of the common emitter, though, is that it **inverts** the input signal (compare it to the inverter from the last page!).

#### Common Collector (Emitter Follower)

If we tie the collector pin to a common voltage, use the base as an input, and the emitter as an output, we have a common collector. This configuration is also known as an **emitter follower**.

[![Common collector model](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/common-collector-model.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/common-collector-model.png)

The common collector doesn\'t do any voltage amplification (in fact, the voltage out will be 0.6V lower than the voltage in). For that reason, this circuit is sometimes called a **voltage follower**.

This circuit does have great potential as a **current amplifier**. In addition to that, the high current gain combined with near unity voltage gain makes this circuit a great **voltage buffer**. A voltage buffer prevents a load circuit from undesirably interfering with the circuit driving it.

For example, if you wanted to deliver 1V to a load, you could go the easy way and use a [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers), or you could use an emitter follower.

[![Common collector 1V out](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/common-collector-voltage-source.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/common-collector-voltage-source.png)

As the load gets larger (which, conversely, means the resistance is lower) the output of the voltage divider circuit drops. But the voltage output of the emitter follower remains steady, regardless of what the load is. Bigger loads can\'t \"load down\" an emitter follower, like they can circuits with larger output impedances.

#### Common Base

We\'ll talk about common base to provide some closure to this section, but this is the least popular of the three fundamental configurations. In a common base amplifier, the emitter is an input and the collector an output. The base is common to both.

[![Common base model](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/common-base-model.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/common-base-model.png)

Common base is like the anti-emitter-follower. It\'s a decent voltage amplifier, and current in is about equal to current out (actually current in is slightly greater than current out).

The common base circuit works best as a **current buffer**. It can take an input current at a low input impedance, and deliver nearly that same current to a higher impedance output.

#### In Summary

These three amplifier configurations are at the heart of many more complicated transistor amplifiers. They each have applications where they shine, whether they\'re amplifying current, voltage, or buffering.

                     Common Emitter   Common Collector   Common Base
  ------------------ ---------------- ------------------ -------------
  Voltage Gain       Medium           Low                High
  Current Gain       Medium           High               Low
  Input Impedance    Medium           High               Low
  Output Impedance   Medium           Low                High

\

### Multistage Amplifiers

We could go on and on about the great variety of transistor amplifiers out there. Here are a few quick examples to show off what happens when you combine the single-stage amplifiers above:

#### Darlington

The Darlington amplifier runs one common collector into another to create a **high current gain** amplifier.

[![Darlington pair](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/darlington-pair.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/darlington-pair.png)

Voltage out is *about* the same as voltage in (minus about 1.2V-1.4V), but the current gain is the product of *two* transistor gains. That\'s β^2^ \-- upwards of 10,000!

The Darlington pair is a great tool if you need to drive a large load with a very small input current.

#### Differential Amplifier

A differential amplifier subtracts two input signals and amplifies that difference. It\'s a critical part of feedback circuits, where the input is compared against the output, to produce a future output.

Here\'s the foundation of the differential amp:

[![Differential amplifier \-- long tailed pair](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/differential-amplifier.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/differential-amplifier.png)

This circuit is also called a **long tailed pair**. It\'s a pair of common-emitter circuits that are compared against each other to produce a differential output. Two inputs are applied to the bases of the transistors; the output is a differential voltage across the two collectors.

#### Push-Pull Amplifier

A push-pull amplifier is a useful \"final stage\" in many multi-stage amplifiers. It\'s an energy efficient power amplifier, often used to drive loudspeakers.

The fundamental push-pull amp uses an NPN and PNP transistor, both configured as common collectors:

[![Push-pull amplifier](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/push-pull.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/push-pull.png)

The push-pull amp doesn\'t really amplify voltage (voltage out will be slightly less than that in), but it does amplify current. It\'s especially useful in bi-polar circuits (those with positive and negative supplies), because it can both \"push\" current into the load from the positive supply, and \"pull\" current out and sink it into the negative supply.

If you have a bi-polar supply (or even if you don\'t), the push-pull is a great final stage to an amplifier, acting as a buffer for the load.

### [] Putting Them Together (An Operational Amplifier)

Let\'s look at a classic example of a multi-stage transistor circuit: an [Op Amp](https://www.sparkfun.com/products/9456). Being able to recognize common transistor circuits, and understanding their purpose can get you a long way! Here is the circuit inside an [LM3558](https://www.sparkfun.com/datasheets/Components/General/LM358.pdf), a really simple op amp:

[![LM358 circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/3/lm358-schematic.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/lm358-schematic.png)

*The internals of an LM358 operational amplifier. Recognize some amplifiers?*

There\'s certainly more complexity here than you may be prepared to digest, however you might see some familiar topologies:

- Q1, Q2, Q3, and Q4 form the input stage. Looks a lot like an **common collector** (Q1 and Q4) into a **differential amplifier**, right? It just looks upside down, because it\'s using PNP\'s. These transistors help to form the input differential stage of the amplifier.
- Q11 and Q12 are part of the second stage. Q11 is a common collector and Q12 is a **common emitter**. This pair of transistors will buffer the signal from Q3\'s collector, and provide a high gain as the signal goes to the final stage.
- Q6 and Q13 are part of the final stage, and they should look familiar as well (especially if you ignore R~SC~) \-- it\'s a **push-pull**! This stage buffers the output, allowing it to drive larger loads.
- There are a variety of other common configurations in there that we haven\'t talked about. Q8 and Q9 are configured as a **current mirror**, which simply copies the amount of current through one transistor into the other.

After this crash course in transistors, we wouldn\'t expect you to understand what\'s going on in this circuit, but if you can begin to identify common transistor circuits you\'re on the right track!

------------------------------------------------------------------------

## Purchasing Transistors

Now that you\'re in control of the source of control, we recommend a SparkFun Inventor\'s Kit to bring your newly found knowledge to life. We\'ve also provided links to a semiconductor kit and single transistors to insert into your own projects.

### Our Recommendations:

[![SparkFun Discrete Semiconductor Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/3/5/13682-01.jpg)](https://www.sparkfun.com/sparkfun-discrete-semiconductor-kit.html)

### [SparkFun Discrete Semiconductor Kit](https://www.sparkfun.com/sparkfun-discrete-semiconductor-kit.html) 

[ KIT-13682 ]

The SparkFun Discrete Semiconductor Kit addresses your needs of only needing one or a couple transistors without you needing ...

[ [\$19.50] ]

[![N-Channel MOSFET 55V 30A](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/3/6/COM-24144-N-Channel-MOSFET-55V-30A-Feature.jpg)](https://www.sparkfun.com/n-channel-mosfet-55v-30a.html)

### [N-Channel MOSFET 55V 30A](https://www.sparkfun.com/n-channel-mosfet-55v-30a.html) 

[ COM-24144 ]

This is a common MOSFET with very low on-resistance and a control voltage (aka gate voltage) that is compatible with any 3-5V...

[ [\$1.50] ]

[![Transistor - NPN, 50V 800mA (BC337)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/5/9/13689-01.jpg)](https://www.sparkfun.com/transistor-npn-50v-800ma-bc337.html)

### [Transistor - NPN, 50V 800mA (BC337)](https://www.sparkfun.com/transistor-npn-50v-800ma-bc337.html) 

[ COM-13689 ]

This is the BC337, an NPN silicon BJT (Bipolar Junction Transistor). This little transistor can help in your project by being...

[ [\$0.55] ]

[ ![SparkFun Inventor\'s Kit Add-On Pack - v4.0](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/7/6/14310-01a.jpg) ]

### SparkFun Inventor\'s Kit Add-On Pack - v4.0 

[ KIT-14310 ]

With the Add-On Pack you will be able to incorporate some of the older parts that used to be included in the SIK that were re...

**Retired**

------------------------------------------------------------------------