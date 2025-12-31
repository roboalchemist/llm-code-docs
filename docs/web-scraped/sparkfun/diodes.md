# Source: https://learn.sparkfun.com/tutorials/diodes

## Introduction

Once you graduate from the simple, passive components that are [resistors](https://learn.sparkfun.com/tutorials/resistors), [capacitors](https://learn.sparkfun.com/tutorials/capacitors), and inductors, it\'s time to step on up to the wonderful world of semiconductors. One of the most widely used semiconductor components is the diode.

[![Diode](https://cdn.sparkfun.com/r/600-600/assets/1/c/d/c/e/5203f837757b7fcf2040674c.jpg)](https://cdn.sparkfun.com/assets/1/c/d/c/e/5203f837757b7fcf2040674c.jpg)

In this tutorial we\'ll cover:

- What is a diode!?
- Theory of diode operation
- Important diode properties
- Different types of diodes
- What diodes look like
- Typical diode applications

### Suggested Reading

Some of the concepts in this tutorial build on previous electronics knowledge. Before jumping into this tutorial consider reading (at least skimming) these first:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/what-is-electricity)

### What is Electricity? 

We can see electricity in action on our computers, lighting our houses, as lightning strikes in thunderstorms, but what is it? This is not an easy question, but this tutorial will shed some light on it!

[](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)

### Series and Parallel Circuits 

An introduction into series and parallel circuits.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

### How to Use a Multimeter 

Learn the basics of using a multimeter to measure continuity, voltage, resistance and current.

## Looking to explore different diodes?

We\'ve got you covered!

[![SparkFun Discrete Semiconductor Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/3/5/13682-01.jpg)](https://www.sparkfun.com/sparkfun-discrete-semiconductor-kit.html)

### [SparkFun Discrete Semiconductor Kit](https://www.sparkfun.com/sparkfun-discrete-semiconductor-kit.html) 

[ KIT-13682 ]

The SparkFun Discrete Semiconductor Kit addresses your needs of only needing one or a couple transistors without you needing ...

[ [\$19.50] ]

[![Diode Rectifier - 1A, 400V (1N4004)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/6/4/14884-Diode_Rectifier_-_1A__400V__1N4004_-01.jpg)](https://www.sparkfun.com/diode-rectifier-1a-400v-1n4004.html)

### [Diode Rectifier - 1A, 400V (1N4004)](https://www.sparkfun.com/diode-rectifier-1a-400v-1n4004.html) 

[ COM-14884 ]

This is a simple, subminiature size, axial lead mounted rectifier diode. The 1N4004 is rated for up to 1A/400V.

[ [\$0.25] ]

[![Diode Rectifier - 1A, 50V (1N4001)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/8/08588-02-L.jpg)](https://www.sparkfun.com/diode-rectifier-1a-50v-1n4001.html)

### [Diode Rectifier - 1A, 50V (1N4001)](https://www.sparkfun.com/diode-rectifier-1a-50v-1n4001.html) 

[ COM-08589 ]

This is a simple, subminiature size, axial lead mounted rectifier diode. The 1N4001 is rated for up to 1A/50V.

[ [\$0.25] ]

[![SparkFun Beginner Parts Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/1/5/13973-SparkFun_Beginner_Parts_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-beginner-parts-kit.html)

### [SparkFun Beginner Parts Kit](https://www.sparkfun.com/sparkfun-beginner-parts-kit.html) 

[ KIT-13973 ]

The SparkFun Beginner Parts Kit is a small container of frequently used parts that gives you all of the basic components you...

**Retired**

[See all diodes](https://www.sparkfun.com/categories/325)

------------------------------------------------------------------------

## Ideal Diodes

The key function of an **ideal** diode is to control the *direction* of current-flow. Current passing through a diode can only go in one direction, called the forward direction. Current trying to flow the reverse direction is blocked. They\'re like the one-way valve of electronics.

If the voltage across a diode is negative, no current can flow[\*](#idealNotReal), and the ideal diode looks like an open circuit. In such a situation, the diode is said to be *off* or **reverse biased**.

As long as the voltage across the diode isn\'t negative, it\'ll \"turn on\" and conduct current. Ideally[\*](#idealNotReal) a diode would act like a short circuit (0V across it) if it was conducting current. When a diode is conducting current it\'s **forward biased** (electronics jargon for \"on\").

[![Ideal diode graph](https://cdn.sparkfun.com/r/600-600/assets/3/9/7/0/3/5171b6eace395f673c000000.png)](https://cdn.sparkfun.com/assets/3/9/7/0/3/5171b6eace395f673c000000.png)

*The current-voltage relationship of an ideal diode. Any negative voltage produces zero current \-- an open circuit. As long as the voltage is non-negative the diode looks like a short circuit.*

\

+------------------+---------------------+----------------------+
| **Ideal Diode Characteristics**                               |
+------------------+---------------------+----------------------+
| Operation Mode   | On (Forward biased) | Off (Reverse biased) |
+------------------+---------------------+----------------------+
| Current Through  | I\>0                | I=0                  |
+------------------+---------------------+----------------------+
| Voltage Across   | V=0                 | V\<0                 |
+------------------+---------------------+----------------------+
| Diode looks like | Short circuit       | Open circuit         |
+------------------+---------------------+----------------------+

### Circuit Symbol

Every diode has **two terminals** \-- connections on each end of the component \-- and those terminals are **polarized**, meaning the two terminals are distinctly different. It\'s important not to mix the connections on a diode up. The positive end of a diode is called the **anode**, and the negative end is called the **cathode**. Current can flow from the anode end to the cathode, but not the other direction. If you forget which way current flows through a diode, try to remember the mnemonic *ACID*: \"anode current in diode\" (also *anode cathode is diode*).

The **circuit symbol** of a standard diode is a triangle butting up against a line. As we\'ll cover in the [later in this tutorial](types-of-diodes), there are a variety of diode types, but usually their circuit symbol will look something like this:

[![Diode circuit symbol](https://cdn.sparkfun.com/assets/d/6/b/f/a/5171b6bece395ff53c000000.PNG)](https://cdn.sparkfun.com/assets/d/6/b/f/a/5171b6bece395ff53c000000.PNG)

The terminal entering the flat edge of the triangle represents the anode. Current flows in the direction that the triangle/arrow is pointing, but it can\'t go the other way.

[![Examples of ideal diodes in circuits](https://cdn.sparkfun.com/r/600-600/assets/4/d/e/a/0/5171bcf8ce395f003d000000.png)](https://cdn.sparkfun.com/assets/4/d/e/a/0/5171bcf8ce395f003d000000.png)

Above are a couple simple diode circuit examples. On the left, diode D1 is forward biased and allowing current to flow through the circuit. In essence it looks like a short circuit. On the right, diode D2 is reverse biased. Current cannot flow through the circuit, and it essentially looks like an open circuit.

[]\*Caveat! Asterisk! Not-entirely-true\... Unfortunately, there\'s no such thing as an *ideal* diode. But don\'t worry! Diodes really are real, they\'ve just got a few characteristics which make them operate as a little less than our ideal model\...

------------------------------------------------------------------------

## Real Diode Characteristics

*Ideally*, diodes will block any and all current flowing the reverse direction, or just act like a short-circuit if current flow is forward. Unfortunately, actual diode behavior isn\'t quite ideal. Diodes do consume some amount of power when conducting forward current, and they won\'t block out all reverse current. Real-world diodes are a bit more complicated, and they all have unique characteristics which define how they actually operate.

### Current-Voltage Relationship

The most important diode characteristic is its current-voltage (*i-v*) relationship. This defines what the current running through a component is, given what voltage is measured across it. Resistors, for example, have a simple, linear *i-v* relationship\...[Ohm\'s Law](../voltage-current-resistance-and-ohms-law/ohms-law). The *i-v* curve of a diode, though, is entirely *non*-linear. It looks something like this:

[![Real diode i-v curve](https://cdn.sparkfun.com/r/600-600/assets/4/4/a/5/b/5175b518ce395f2d49000000.png)](https://cdn.sparkfun.com/assets/4/4/a/5/b/5175b518ce395f2d49000000.png)

*The current-voltage relationship of a diode. In order to exaggerate a few important points on the plot, the scales in both the positive and negative halves are not equal.*

Depending on the voltage applied across it, a diode will operate in one of three regions:

1.  **Forward bias**: When the voltage across the diode is positive the diode is \"on\" and current can run through. The voltage should be greater than the forward voltage (V~F~) in order for the current to be anything significant.
2.  **Reverse bias**: This is the \"off\" mode of the diode, where the voltage is less than V~F~ but greater than -V~BR~. In this mode current flow is (mostly) blocked, and the diode is off. A *very* small amount of current (on the order of nA) \-- called reverse saturation current \-- is able to flow in reverse through the diode.
3.  **Breakdown**: When the voltage applied across the diode is very large and negative, lots of current will be able to flow in the reverse direction, from cathode to anode.

### [] Forward Voltage

In order to \"turn on\" and conduct current in the forward direction, a diode requires a certain amount of positive voltage to be applied across it. The typical voltage required to turn the diode on is called the *forward voltage* (V~F~). It might also be called either the *cut-in voltage* or *on-voltage*.

As we know from the *i-v* curve, the current through and voltage across a diode are interdependent. More current means more voltage, less voltage means less current. Once the voltage gets to about the forward voltage rating, though, large increases in current should still only mean a very small increase in voltage. If a diode is fully conducting, it can usually be assumed that the voltage across it is the forward voltage rating.

[![Measuring forward voltage drop](https://cdn.sparkfun.com/r/600-600/assets/1/e/7/1/f/518182d5ce395fff12000000.jpg)](https://cdn.sparkfun.com/assets/1/e/7/1/f/518182d5ce395fff12000000.jpg)

*A [multimeter](https://learn.sparkfun.com/tutorials/retired---how-to-use-a-multimeter-) with a diode setting can be used to measure (the minimum of) a diode\'s forward voltage drop.*

A specific diode\'s V~F~ depends on what semiconductor material it\'s made out of. Typically, a silicon diode will have a V~F~ around **0.6-1V**. A germanium-based diode might be lower, around 0.3V. The *type* of diode also has some importance in defining the forward voltage drop; light-emitting diodes can have a much larger V~F~, while Schottky diodes are designed specifically to have a much lower-than-usual forward voltage.

### Breakdown Voltage

If a large enough negative voltage is applied to the diode, it will give in and allow current to flow in the reverse direction. This large negative voltage is called the **breakdown voltage**. Some diodes are actually designed to operate in the breakdown region, but for most normal diodes it\'s not very healthy for them to be subjected to large negative voltages.

For normal diodes this breakdown voltage is around -50V to -100V, or even more negative.

## Diode Datasheets

All of the above characteristics should be detailed in the datasheet for every diode. For example, this [datasheet](http://www.vishay.com/docs/81857/1n4148.pdf) for a 1N4148 diode lists the maximum forward voltage (1V) and the breakdown voltage (100V) (among a lot of other information):

[![1N4148 Datasheet Clipping](https://cdn.sparkfun.com/r/600-600/assets/f/a/8/d/7/51781a6dce395f010e000000.png)](https://cdn.sparkfun.com/assets/f/a/8/d/7/51781a6dce395f010e000000.png)

A datasheet might even present you with a very familiar looking current-voltage graph, to further detail how the diode behaves. This graph from the diode\'s datasheet enlarges the curvy, forward-region part of the *i-v* curve. Notice how more current requires more voltage:

[![1N4148 forward i-v curve](https://cdn.sparkfun.com/assets/0/2/2/c/c/51781965ce395f8350000000.png)](https://cdn.sparkfun.com/assets/0/2/2/c/c/51781965ce395f8350000000.png)

That chart points out another important diode characteristic \-- the maximum forward current. Just like any component, diodes can only dissipate so much power before they blow. All diodes should list maximum current, reverse voltage, and power dissipation. If a diode is subject to more voltage or current than it can handle, expect it to heat up (or worse; melt, smoke,\...).

Some diodes are well-suited to high currents \-- 1A or more \-- others like the 1N4148 small-signal diode shown above may only be suited for around 200mA.

------------------------------------------------------------------------

That 1N4148 is just a tiny sampling of all the different kinds of diodes there are out there. Next we\'ll explore what an amazing variety of diodes there are and what purpose each type serves.

## Types of Diodes

### Normal Diodes

#### Signal Diodes

Standard **signal diodes** are among the most basic, average, no-frills members of the diode family. They usually have a medium-high forward voltage drop and a low maximum current rating. A common example of a signal diode is the [1N4148](http://www.sparkfun.com/products/8588).

[![Diode Small Signal - 1N4148](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/6/7/08589-03-L.jpg)](https://www.sparkfun.com/diode-small-signal-1n4148.html)

### [Diode Small Signal - 1N4148](https://www.sparkfun.com/diode-small-signal-1n4148.html) 

[ COM-08588 ]

This is a very common signal diode - 1N4148. Use this for signals up to 200mA of current.

[ [\$0.25] ]

Very general purpose, it\'s got a typical forward voltage drop of 0.72V and a 300mA maximum forward current rating.

[![1N4148 image plus a mechanical drawing](https://cdn.sparkfun.com/assets/1/f/4/b/0/51781f40ce395ff110000000.png)](https://cdn.sparkfun.com/assets/1/f/4/b/0/51781f40ce395ff110000000.png)

*A small-signal diode, the 1N4148. Notice the black circle around the diode, that marks which of the terminals is the cathode.*

#### Power Diodes

A **rectifier or power diode** is a standard diode with a much higher maximum current rating. This higher current rating usually comes at the cost of a larger forward voltage. The [1N4001](http://www.sparkfun.com/products/8589) is an example of a power diode.

[![Diode Rectifier - 1A, 50V (1N4001)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/7/8/08588-02-L.jpg)](https://www.sparkfun.com/diode-rectifier-1a-50v-1n4001.html)

### [Diode Rectifier - 1A, 50V (1N4001)](https://www.sparkfun.com/diode-rectifier-1a-50v-1n4001.html) 

[ COM-08589 ]

This is a simple, subminiature size, axial lead mounted rectifier diode. The 1N4001 is rated for up to 1A/50V.

[ [\$0.25] ]

The 1N4001 has a current rating of 1A and a forward voltage of 1.1V.

[![1N4001 image](https://cdn.sparkfun.com/assets/b/e/b/4/1/517820f8ce395f190e000000.png)](https://cdn.sparkfun.com/assets/b/e/b/4/1/517820f8ce395f190e000000.png)

*A 1N4001 PTH diode. This time a gray band indicates which pin is the cathode.*

And, of course, most diode types come in surface-mount varieties as well. You\'ll notice that every diode has some way (no matter how tiny or hard to see) to indicate which of the two pins is the cathode.

[![Some SMD diodes](https://cdn.sparkfun.com/r/600-600/assets/c/1/6/e/5/518185c5ce395fcb07000000.jpg)](https://cdn.sparkfun.com/assets/c/1/6/e/5/518185c5ce395fcb07000000.jpg)

### Light-Emitting Diodes (LEDs!)

The flashiest member of the diode family must be the [light-emitting diode (LED)](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds). These diodes quite literally light up when a positive voltage is applied.

[![Examples of LEDs](https://cdn.sparkfun.com/r/600-600/assets/a/f/a/b/3/51818388ce395f8102000000.jpg)](https://cdn.sparkfun.com/assets/a/f/a/b/3/51818388ce395f8102000000.jpg)

*A handful of through-hole LEDs. From left to right: a [yellow 3mm](https://www.sparkfun.com/products/532), [blue 5mm](https://www.sparkfun.com/products/11372), [green 10mm](https://www.sparkfun.com/products/8861), [super-bright red 5mm](https://www.sparkfun.com/products/528), an [RGB 5mm](https://www.sparkfun.com/products/10820) and a [blue 7-segment LED](https://www.sparkfun.com/products/9191).*

Like normal diodes, LEDs only allow current through one direction. They also have a forward voltage rating, which is the voltage required for them to light up. The V~F~ rating of an LED is usually larger than that of a normal diode (1.2\~3V), and it depends on the color the LED emits. For example, the rated forward voltage of a [Super Bright Blue LED](http://www.sparkfun.com/products/529) is around 3.3V, while that of the equal size [Super Bright Red LED](http://www.sparkfun.com/products/528) is only 2.2V.

You\'ll obviously most-often find LEDs in lighting applications. They\'re blinky and fun! But more than that, their high-efficiency has lead to widespread use in street lights, displays, backlighting, and much more. Other LEDs emit a light that is not visible to the human eye, like infrared LEDs, which are the backbone of most remote controls. Another common use of LEDs is in optically isolating a dangerous high-voltage system from a lower-voltage circuit. Opto-isolators pair an infrared LED with a photosensor, which allows current to flow when it detects light from the LED. Below is an example circuit of an opto-isolator. Note how the schematic symbol for the diode varies from the normal diode. LED symbols add a couple arrows extending out from the symbol.

[![LED in an opto-isolator circuit](https://cdn.sparkfun.com/assets/3/5/4/2/a/5175bc8dce395f7c49000000.PNG)](https://cdn.sparkfun.com/assets/3/5/4/2/a/5175bc8dce395f7c49000000.PNG)

### Schottky Diodes

Another very common diode is the [Schottky diode](https://www.sparkfun.com/products/10926).

[![Schottky Diode](https://cdn.sparkfun.com/r/600-600/assets/parts/6/0/6/0/10926-01b.jpg)](https://www.sparkfun.com/schottky-diode.html)

### [Schottky Diode](https://www.sparkfun.com/schottky-diode.html) 

[ COM-10926 ]

Schottky diodes are known for their low forward voltage drop and a very fast switching action. This 1A 40V Schottky diode is ...

[ [\$0.30] ]

The semiconductor composition of a Schottky diode is slightly different from a normal diode, and this results in a much **smaller forward voltage drop**, which is usually between 0.15V and 0.45V. They\'ll still have a very large breakdown voltage though.

Schottky diodes are especially useful in limiting losses, when every last bit of voltage *must* be spared. They\'re unique enough to get a circuit symbol of their own, with a couple bends on the end of the cathode-line.

[![Schottky diode circuit symbol](https://cdn.sparkfun.com/r/200-200/assets/f/d/6/5/d/517701cace395fc048000000.png)](https://cdn.sparkfun.com/assets/f/d/6/5/d/517701cace395fc048000000.png)

### Zener Diodes

[Zener diodes](https://www.sparkfun.com/products/10301) are the weird outcast of the diode family. They\'re usually used to intentionally **conduct reverse current**.

[![Zener Diode - 5.1V 1W](https://cdn.sparkfun.com/r/600-600/assets/parts/4/7/0/4/10301-01.jpg)](https://www.sparkfun.com/products/10301)

### [Zener Diode - 5.1V 1W](https://www.sparkfun.com/products/10301) 

[ COM-10301 ]

Zener diodes are useful for creating a reference voltage or as a voltage stabilizer for low-current applications.These diodes...

**Retired**

Zener\'s are designed to have a very precise breakdown voltage, called the **zener breakdown** or **zener voltage**. When enough current runs in reverse through the zener, the voltage drop across it will hold steady at the breakdown voltage.

Taking advantage of their breakdown property, Zener diodes are often used to create a known reference voltage at exactly their Zener voltage. They can be used as a voltage regulator for small loads, but they\'re not really made to regulate voltage to circuits that will pull significant amounts of current.

Zeners are special enough to get their own circuit symbol, with wavy ends on the cathode-line. The symbol might even define what, exactly, the diode\'s zener voltage is. Here\'s a 3.3V zener diode acting to create a solid 3.3V voltage reference:

[![Zener 3.3V reference circuit](https://cdn.sparkfun.com/r/600-600/assets/5/0/a/0/f/5175bb7ace395fbe49000000.png)](https://cdn.sparkfun.com/assets/5/0/a/0/f/5175bb7ace395fbe49000000.png)

### Photodiodes

Photodiodes are specially constructed diodes, which capture energy from photons of light (see Physics, quantum) to generate electrical current. Kind of operating as an anti-LED.

[![Miniature Solar Cell - BPW34](https://cdn.sparkfun.com/r/600-600/assets/parts/3/2/9/6/09541-02.jpg)](https://www.sparkfun.com/miniature-solar-cell-bpw34.html)

### [Miniature Solar Cell - BPW34](https://www.sparkfun.com/miniature-solar-cell-bpw34.html) 

[ PRT-09541 ]

The BPW34 is a tiny, general purpose \[PiN photodiode\](http://en.wikipedia.org/wiki/PIN_diode). This photodiode has a ton of u...

[ [\$1.75] ]

*A BPW34 photodiode (not the quarter, the little thing on top of that). Get it under the sun and it can generate about few µW\'s of power!.*

Solar cells are the main benefactor of photodiode technology. But these diodes can also be used to detect light, or even communicate optically.

------------------------------------------------------------------------

## Diode Applications

For such a simple component, diodes have a huge range of uses. You\'ll find a diode of some type in just about every circuit. They could be featured in anything from a small-signal digital logic to a high voltage power conversion circuit. Let\'s explore some of these applications.

### Rectifiers

A rectifier is a circuit that converts [alternating current (AC) to direct current (DC)](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc). This conversion is critical for all sorts of household electronics. AC signals come out of your house\'s wall outlets, but DC is what powers most computers and other microelectronics.

Current in AC circuits literally *alternates* \-- quickly switches between running in the positive and negative directions \-- but current in a DC signal only runs in one direction. So to convert from AC to DC you just need to make sure current can\'t run in the negative direction. Sounds like a job for DIODES!

A **half-wave rectifier** can be made out of just a single diode. If an AC signal, like a sine wave for example, is sent through a diode any negative component to the signal is clipped out.

[![Half-wave rectifier in/out waveforms and circuit](https://cdn.sparkfun.com/r/600-600/assets/2/9/2/f/3/5176f4bfce395f3a61000000.png)](https://cdn.sparkfun.com/assets/2/9/2/f/3/5176f4bfce395f3a61000000.png)

*Input (red/left) and output (blue/right) voltage waveforms, after passing through the half-wave rectifier circuit (middle).*

A **full-wave bridge rectifier** uses four diodes to convert those negative humps in the AC signal into positive humps.

[![Full-wave bridge rectifier in/out waveforms and circuit](https://cdn.sparkfun.com/r/600-600/assets/d/2/2/3/b/5176fdc5ce395f5248000000.png)](https://cdn.sparkfun.com/assets/d/2/2/3/b/5176fdc5ce395f5248000000.png)

*The bridge rectifier circuit (middle), and the output wave form it creates (blue/right).*

These circuits are a critical component in AC-to-DC power supplies, which turn the wall outlet\'s 120/240VAC signal into 3.3V, 5V, 12V, etc. DC signals. If you tore apart a [wall-wart](https://www.sparkfun.com/products/8269), you\'d most likely see a handful of diodes in there, rectifying it up.

[![Diodes in a wall-wart](https://cdn.sparkfun.com/r/600-600/assets/8/f/7/9/e/518184dace395fb40c000000.jpg)](https://cdn.sparkfun.com/assets/8/f/7/9/e/518184dace395fb40c000000.jpg)

*Can you spot the four diodes making a bridge rectifier in this wall-wart?*

### Reverse Current Protection[]

Ever stick a battery in the wrong way? Or switch up the red and black power wires? If so, a diode might be to thank for your circuit still being alive. A diode placed in series with the positive side of the power supply is called a reverse protection diode. It ensures that current can only flow in the positive direction, and the power supply only applies a positive voltage to your circuit.

[![Reverse current protection circuit](https://cdn.sparkfun.com/r/600-600/assets/1/0/4/8/5/5175bb7ace395fa848000000.png)](https://cdn.sparkfun.com/assets/1/0/4/8/5/5175bb7ace395fa848000000.png)

This diode application is useful when a power supply connector isn\'t polarized, making it easy to mess up and accidentally connect the negative supply to the positive of the input circuit.

The drawback of a reverse protection diode is that it\'ll induce some voltage loss because of the forward voltage drop. This makes **Schottky diodes** an excellent choice for reverse protection diodes.

### Logic Gates

Forget transistors! Simple [digital logic gates](https://learn.sparkfun.com/tutorials/digital-logic/combinational-logic), like the AND or the OR, can be built out of diodes.

For example, a diode two-input OR gate can be constructed out of two diodes with shared cathode nodes. The output of the logic circuit is also located at that node. Whenever either input (or both) is a logic 1 (high/5V) the output becomes a logic 1 as well. When both inputs are a logic 0 (low/0V), the output is pulled low through the resistor.

[![Diode 2-input OR gate schematic](https://cdn.sparkfun.com/r/300-300/assets/f/0/b/d/f/517704aace395fda48000001.png)](https://cdn.sparkfun.com/assets/f/0/b/d/f/517704aace395fda48000001.png)

An AND gate is constructed in a similar manner. The *anodes* of both diodes are connected together, which is where the output of the circuit is located. Both inputs must be logic 1 forcing current to run towards the output pin and pull it high also. If either of the inputs are low, current from the 5V supply runs through the diode.

[![Diode 2-input AND gate schematic](https://cdn.sparkfun.com/r/300-300/assets/4/9/1/a/3/517704aace395fe448000000.png)](https://cdn.sparkfun.com/assets/4/9/1/a/3/517704aace395fe448000000.png)

For both logic gates, more inputs can be added by adding just a single diode.

### Flyback Diodes and Voltage Spike Suppression

Diodes are very often used to limit potential damage from unexpected large spikes in voltage. Transient-voltage-suppression (TVS) diodes are specialty diodes, kind of like zener diodes \-- lowish breakdown voltages (often around 20V) \-- but with very large power ratings (often in the range of kilowatts). They\'re designed to shunt currents and absorb energy when voltages exceed their breakdown voltage.

Flyback diodes do a similar job of suppressing voltage spikes, specifically those induced by an inductive component, like a motor. When current through an inductor suddenly changes, a voltage spike is created, possibly a very large, negative spike. A flyback diode placed across the inductive load, will give that negative voltage signal a safe path to discharge, actually looping over-and-over through the inductor and diode until it eventually dies out.

[![Flyback diode circuit](https://cdn.sparkfun.com/r/400-400/assets/9/8/6/0/f/51770c5bce395f3149000000.png)](https://cdn.sparkfun.com/assets/9/8/6/0/f/51770c5bce395f3149000000.png)

That\'s just a handful of applications for this amazing little semiconductor component.

------------------------------------------------------------------------

## Purchasing Diodes

Now that your *current* is flowing in the right direction, it\'s time to put your new knowledge to good use. Whether you\'re looking for a starting point or just stocking up, we\'ve got an Inventor\'s Kit as well individual diodes to choose from.

### Our recommendations:

[![Diode Small Signal - 1N4148](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/7/08589-03-L.jpg)](https://www.sparkfun.com/diode-small-signal-1n4148.html)

### [Diode Small Signal - 1N4148](https://www.sparkfun.com/diode-small-signal-1n4148.html) 

[ COM-08588 ]

This is a very common signal diode - 1N4148. Use this for signals up to 200mA of current.

[ [\$0.25] ]

[![Schottky Diode](https://cdn.sparkfun.com/r/140-140/assets/parts/6/0/6/0/10926-01b.jpg)](https://www.sparkfun.com/schottky-diode.html)

### [Schottky Diode](https://www.sparkfun.com/schottky-diode.html) 

[ COM-10926 ]

Schottky diodes are known for their low forward voltage drop and a very fast switching action. This 1A 40V Schottky diode is ...

[ [\$0.30] ]

[![Diode Rectifier - 1A, 50V (1N4001)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/8/08588-02-L.jpg)](https://www.sparkfun.com/diode-rectifier-1a-50v-1n4001.html)

### [Diode Rectifier - 1A, 50V (1N4001)](https://www.sparkfun.com/diode-rectifier-1a-50v-1n4001.html) 

[ COM-08589 ]

This is a simple, subminiature size, axial lead mounted rectifier diode. The 1N4001 is rated for up to 1A/50V.

[ [\$0.25] ]

[![SparkFun Inventor\'s Kit - V3.2](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/5/3/12060-01.jpg)](https://www.sparkfun.com/products/12060)

### [SparkFun Inventor\'s Kit - V3.2](https://www.sparkfun.com/products/12060) 

[ KIT-12060 ]

\*\*As you may have seen from \[our blog post\](https://www.sparkfun.com/news/2241), we recently moved our injection mold for SIK...

**Retired**

## Interested in learning more foundational topics?

See our **[Engineering Essentials](https://www.sparkfun.com/engineering_essentials)** page for a full list of cornerstone topics surrounding electrical engineering.

[Take me there!](https://www.sparkfun.com/engineering_essentials)

![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/multimeter-300.png)