# Source: https://learn.sparkfun.com/tutorials/how-to-read-a-schematic

## Overview

Schematics are our map to designing, building, and troubleshooting circuits. Understanding how to read and follow schematics is an important skill for any electronics engineer.

This tutorial should turn you into a fully literate schematic reader! We\'ll go over all of the fundamental schematic symbols:

[![Schematic component overview](https://cdn.sparkfun.com/r/600-600/assets/6/8/6/d/1/51cdc767ce395f7558000002.png)](https://cdn.sparkfun.com/assets/6/8/6/d/1/51cdc767ce395f7558000002.png)

Then we\'ll talk about how those symbols are connected on schematics to create a model of a circuit. We\'ll also go over a few tips and tricks to watch out for.

### Suggested Reading

Schematic comprehension is a pretty basic electronics skill, but there are a few things you should know before you read this tutorial. Check out these tutorials, if they sound like gaps in your growing brain:

- [What is Electricity?](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [What is a Circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

![](https://cdn.sparkfun.com/assets/home_page_posts/3/1/9/0/collage-of-product.jpg)

## Expecting a Pay Wall? 

### Not Our Style. 

## Schematic Symbols (Part 1)

Are you ready for a barrage of circuit components? Here are some of the standardized, basic schematic symbols for various components.

### Resistors

The most fundamental of circuit components and symbols! [Resistors](https://learn.sparkfun.com/tutorials/resistors) on a schematic are usually represented by a few zig-zag lines, with **two terminals** extending outward. Schematics using international symbols may instead use a featureless rectangle, instead of the squiggles.

[![Resistor schematic symbols](https://cdn.sparkfun.com/assets/2/2/6/9/c/51cc9e55ce395f576d000000.png)](https://cdn.sparkfun.com/assets/2/2/6/9/c/51cc9e55ce395f576d000000.png)

#### Potentiometers and Variable Resistors

Variable resistors and potentiometers each augment the standard resistor symbol with an arrow. The variable resistor remains a two-terminal device, so the arrow is just laid diagonally across the middle. A potentiometer is a three-terminal device, so the arrow becomes the third terminal (the wiper).

[![Variable resistor symbols](https://cdn.sparkfun.com/assets/4/5/c/a/0/51cc9e55ce395fad69000001.png)](https://cdn.sparkfun.com/assets/4/5/c/a/0/51cc9e55ce395fad69000001.png)

### Capacitors

There are two commonly used [capacitor](https://learn.sparkfun.com/tutorials/capacitors) symbols. One symbol represents a [polarized](https://learn.sparkfun.com/tutorials/polarity) (usually electrolytic or tantalum) capacitor, and the other is for non-polarized caps. In each case there are two terminals, running perpendicularly into plates.

[![Capacitors symbols](https://cdn.sparkfun.com/assets/9/c/9/c/5/51cc9e55ce395fcd6c000000.png)](https://cdn.sparkfun.com/assets/9/c/9/c/5/51cc9e55ce395fcd6c000000.png)

The symbol with one curved plate indicates that the capacitor is polarized. The curved plate usually represents the cathode of the capacitor, which should be at a lower voltage than the positive, anode pin. A plus sign should also be added to the positive pin of the polarized capacitor symbol.

### Inductors

Inductors are usually represented by either a series of curved bumps, or loopy coils. International symbols may just define an inductor as a filled-in rectangle.

[![Inductor symbols](https://cdn.sparkfun.com/assets/3/f/a/4/0/51cca0f8ce395fa06c000001.png)](https://cdn.sparkfun.com/assets/3/f/a/4/0/51cca0f8ce395fa06c000001.png)

### Switches

[Switches](https://learn.sparkfun.com/tutorials/button-and-switch-basics) exist in many different forms. The most basic switch, a single-pole/single-throw (SPST), is two terminals with a half-connected line representing the actuator (the part that connects the terminals together).

[![Switch symbol](https://cdn.sparkfun.com/assets/3/5/4/2/a/51cc9e55ce395fa969000002.png)](https://cdn.sparkfun.com/assets/3/5/4/2/a/51cc9e55ce395fa969000002.png)

Switches with more than one throw, like the SPDT and SP3T below, add more landing spots for the the actuator.

[![SPDT and SP3T symbols](https://cdn.sparkfun.com/assets/f/a/b/3/3/51cc9e55ce395f7a6c000001.png)](https://cdn.sparkfun.com/assets/f/a/b/3/3/51cc9e55ce395f7a6c000001.png)

Switches with multiple poles, usually have multiple, alike switches with a dotted line intersecting the middle actuator.

[![DPDT symbol](https://cdn.sparkfun.com/assets/0/a/4/0/7/51cc9e55ce395fb072000000.png)](https://cdn.sparkfun.com/assets/0/a/4/0/7/51cc9e55ce395fb072000000.png)

### Power Sources

Just as there are many options out there for [powering your project](https://learn.sparkfun.com/tutorials/how-to-power-a-project), there are a wide variety of power source circuit symbols to help specify the power source.

#### DC or AC Voltage Sources

Most of the time when working with electronics, you\'ll be using constant voltage sources. We can use either of these two symbols to define whether the source is supplying direct current (DC) or alternating current (AC):

[![Voltage source symbols](https://cdn.sparkfun.com/assets/4/7/b/0/3/51cc9e55ce395f8f6d000001.png)](https://cdn.sparkfun.com/assets/4/7/b/0/3/51cc9e55ce395f8f6d000001.png)

#### Batteries

[Batteries](https://learn.sparkfun.com/tutorials/battery-technologies), whether they\'re those cylindrical, [alkaline AA\'s](https://www.sparkfun.com/products/9100) or rechargeable [lithium-polymers](https://www.sparkfun.com/products/339), usually look like a pair of disproportionate, parallel lines:

[![Battery symbols](https://cdn.sparkfun.com/assets/b/a/5/0/8/51cc9e54ce395ff06d000001.png)](https://cdn.sparkfun.com/assets/b/a/5/0/8/51cc9e54ce395ff06d000001.png)

More pairs of lines usually indicates more series cells in the battery. Also, the longer line is usually used to represent the positive terminal, while the shorter line connects to the negative terminal.

#### Voltage Nodes

Sometimes \-- on really busy schematics especially \-- you can assign special symbols to node voltages. You can connect devices to these **one-terminal** symbols, and it\'ll be tied directly to 5V, 3.3V, VCC, or GND (ground). Positive voltage nodes are usually indicated by an arrow pointing up, while ground nodes usually involve one to three flat lines (or sometimes a down-pointing arrow or triangle).

[![Voltage node symbols](https://cdn.sparkfun.com/assets/f/7/5/4/2/51cc9e55ce395fcc74000000.png)](https://cdn.sparkfun.com/assets/f/7/5/4/2/51cc9e55ce395fcc74000000.png)

## Schematic Symbols (Part 2)

### Diodes

Basic [diodes](https://learn.sparkfun.com/tutorials/diodes) are usually represented with a triangle pressed up against a line. Diodes are also [polarized](https://learn.sparkfun.com/tutorials/polarity), so each of the two terminals require distinguishing identifiers. The positive, anode is the terminal running into the flat edge of the triangle. The negative, cathode extends out of the line in the symbol (think of it as a - sign).

[![Diode symbol](https://cdn.sparkfun.com/assets/2/2/a/b/a/51cc9e56ce395fad6c000002.png)](https://cdn.sparkfun.com/assets/2/2/a/b/a/51cc9e56ce395fad6c000002.png)

There are a all sorts of different [types of diodes](../diodes/types-of-diodes), each of which has a special riff on the standard diode symbol. **Light-emitting diodes (LEDs)** augment the diode symbol with a couple lines pointing away. **Photodiodes**, which generate energy from light (basically, tiny solar cells), flip the arrows around and point them toward the diode.

[![LED and Photodiode symbols](https://cdn.sparkfun.com/assets/c/5/7/4/4/51cca2cace395f5e6d000000.png)](https://cdn.sparkfun.com/assets/c/5/7/4/4/51cca2cace395f5e6d000000.png)

Other special types of diodes, like Schottky\'s or zeners, have their own symbols, with slight variations on the bar part of the symbol.

[![Schottky and zener diode symbols](https://cdn.sparkfun.com/assets/1/6/9/2/0/51cca2cace395f6369000000.png)](https://cdn.sparkfun.com/assets/1/6/9/2/0/51cca2cace395f6369000000.png)

### Transistors

Transistors, whether they\'re BJTs or MOSFETs, can exist in two configurations: positively doped, or negatively doped. So for each of these types of transistor, there are at least two ways to draw it.

#### Bipolar Junction Transistors (BJTs)

BJTs are three-terminal devices; they have a collector (C), emitter (E), and a base (B). There are two types of BJTs \-- NPNs and PNPs \-- and each has its own unique symbol.

[![NPN and PNP BJT symbols](https://cdn.sparkfun.com/assets/9/8/4/c/5/51cca2f8ce395f6469000000.png)](https://cdn.sparkfun.com/assets/9/8/4/c/5/51cca2f8ce395f6469000000.png)

The collector (C) and emitter (E) pins are both in-line with each other, but the emitter should always have an arrow on it. If the arrow is pointing inward, it\'s a PNP, and, if the arrow is pointing outward, it\'s an NPN. A mnemonic for remembering which is which is \"NPN: **n**ot **p**ointing i**n**.\"

#### Metal Oxide Field-Effect Transistors (MOSFETs)

Like BJTs, MOSFETs have three terminals, but this time they\'re named source (S), drain (D), and gate (G). And again, there are two different versions of the symbol, depending on whether you\'ve got an n-channel or p-channel MOSFET. There are a number of commonly used symbols for each of the MOSFET types:

[![Variety of MOSFET symbols](https://cdn.sparkfun.com/r/600-600/assets/d/f/6/3/d/51cc9e55ce395fea4b000000.png)](https://cdn.sparkfun.com/assets/d/f/6/3/d/51cc9e55ce395fea4b000000.png)

The arrow in the middle of the symbol (called the bulk) defines whether the MOSFET is n-channel or p-channel. If the arrow is pointing in means it\'s a n-channel MOSFET, and if it\'s pointing out it\'s a p-channel. Remember: \"n is in\" (kind of the opposite of the NPN mnemonic).

### Digital Logic Gates

Our standard logic functions \-- AND, OR, NOT, and XOR \-- all have unique schematic symbols:

[![Standard logic functions](https://cdn.sparkfun.com/r/600-600/assets/3/5/8/2/d/51cc9e54ce395f7e69000000.png)](https://cdn.sparkfun.com/assets/3/5/8/2/d/51cc9e54ce395f7e69000000.png)

Adding a bubble to the output **negates** the function, creating NANDs, NORs, and XNORs:

[![Negated logic gates](https://cdn.sparkfun.com/r/600-600/assets/7/c/8/e/9/51cc9e55ce395f856d000000.png)](https://cdn.sparkfun.com/assets/7/c/8/e/9/51cc9e55ce395f856d000000.png)

They may have more than two inputs, but the shapes should remain the same (well, maybe a bit bigger), and there should still only be one output.

### Integrated Circuits

[Integrated circuits](https://learn.sparkfun.com/tutorials/integrated-circuits) accomplish such unique tasks, and are so numerous, that they don\'t really get a unique circuit symbol. Usually, an integrated circuit is represented by a rectangle, with pins extending out of the sides. Each pin should be labeled with both a number, and a function.

[![ATmega328, ATSHA204, and ATtiny45 IC symbols](https://cdn.sparkfun.com/r/600-600/assets/4/4/a/d/0/51cc9e55ce395f7f69000001.png)](https://cdn.sparkfun.com/assets/4/4/a/d/0/51cc9e55ce395f7f69000001.png)

*Schematic symbols for an ATmega328 microcontroller (commonly found on [Arduinos](https://learn.sparkfun.com/tutorials/what-is-an-arduino)), an ATSHA204 encryption IC, and an ATtiny45 MCU. As you can see, these components greatly vary in size and pin-counts.*

Because ICs have such a generic circuit symbol, the names, values and labels become very important. Each IC should have a value precisely identifying the name of the chip.

#### Unique ICs: Op Amps, Voltage Regulators

Some of the more common integrated circuits do get a unique circuit symbol. You\'ll usually see operation amplifiers laid out like below, with 5 total terminals: a non-inverting input (+), inverting input (-), output, and two power inputs.

[![Op amp symbols](https://cdn.sparkfun.com/assets/d/6/9/6/4/51cca328ce395f666d000001.png)](https://cdn.sparkfun.com/assets/d/6/9/6/4/51cca328ce395f666d000001.png)

*Often, there will be two op amps built into one IC package requiring only one pin for power and one for ground, which is why the one on the right only has three pins.*

Simple voltage regulators are usually three-terminal components with input, output and ground (or adjust) pins. These usually take the shape of a rectangle with pins on the left (input), right (output) and bottom (ground/adjust).

[![Voltage regulator symbols](https://cdn.sparkfun.com/r/600-600/assets/8/3/5/4/4/51cca328ce395f7a69000000.png)](https://cdn.sparkfun.com/assets/8/3/5/4/4/51cca328ce395f7a69000000.png)

### Miscellany

#### Crystals and Resonators

Crystals or resonators are usually a critical part of microcontroller circuits. They help provide a clock signal. Crystal symbols usually have two terminals, while resonators, which add two capacitors to the crystal, usually have three terminals.

[![Crystal and resonator symbols](https://cdn.sparkfun.com/assets/a/e/5/6/f/51ccac08ce395f776c000000.png)](https://cdn.sparkfun.com/assets/a/e/5/6/f/51ccac08ce395f776c000000.png)

#### Headers and Connectors

Whether it\'s for providing power, or sending out information, connectors are a requirement on most circuits. These symbols vary depending on what the connector looks like, here\'s a sampling:

[![Connector symbols](https://cdn.sparkfun.com/assets/e/3/7/a/d/51ccac08ce395f6569000000.png)](https://cdn.sparkfun.com/assets/e/3/7/a/d/51ccac08ce395f6569000000.png)

#### Motors, Transformers, Speakers, and Relays

We\'ll lump these together, since they (mostly) all make use of coils in some way. **Transformers** (not the [more-than-meets-the-eye](http://www.youtube.com/watch?v=nLS2N9mHWaw) kind) usually involve two coils, butted up against each other, with a couple lines separating them:

[![Transformer symbols](https://cdn.sparkfun.com/assets/f/b/e/a/f/51ccac08ce395fe06d000001.png)](https://cdn.sparkfun.com/assets/f/b/e/a/f/51ccac08ce395fe06d000001.png)

**Relays** usually pair a coil with a switch:

[![Relay symbol](https://cdn.sparkfun.com/assets/d/8/b/2/4/51ccac08ce395fac6d000001.png)](https://cdn.sparkfun.com/assets/d/8/b/2/4/51ccac08ce395fac6d000001.png)

**Speakers and buzzers** usually take a form similar to their real-life counterparts:

[![Speaker](https://cdn.sparkfun.com/assets/2/9/a/a/6/51ccac08ce395f8c2b000002.png)](https://cdn.sparkfun.com/assets/2/9/a/a/6/51ccac08ce395f8c2b000002.png)

And **motors** generally involve an encircled \"M\", sometimes with a bit more embellishment around the terminals:

[![Motor](https://cdn.sparkfun.com/assets/9/4/2/8/6/51ccac09ce395fc96c000001.png)](https://cdn.sparkfun.com/assets/9/4/2/8/6/51ccac09ce395fc96c000001.png)

#### Fuses and PTCs

Fuses and PTCs \-- devices which are generally used to limit large inrushes of current \-- each have their own unique symbol:

[![Fuse and PTC symbol](https://cdn.sparkfun.com/assets/1/a/1/d/2/51ccac08ce395fb16d000000.png)](https://cdn.sparkfun.com/assets/1/a/1/d/2/51ccac08ce395fb16d000000.png)

The PTC symbol is actually the generic symbol for a **thermistor**, a temperature-dependent resistor (notice the international resistor symbol in there?).

------------------------------------------------------------------------

No doubt, there are many circuit symbols left off this list, but those above should have you 90% literate in schematic reading. In general, symbols should share a fair amount in common with the real-life components they model. In addition to the symbol, each component on a schematic should have a unique name and value, which further helps to identify it.

## Name Designators and Values

One of the biggest keys to being schematic-literate is being able to recognize which components are which. The component symbols tell half the story, but each symbol should be paired with both a name and value to complete it.

### Names and Values

**Values** help define exactly what a component is. For schematic components like resistors, capacitors, and inductors the value tells us how many ohms, farads, or henries they have. For other components, like integrated circuits, the value may just be the name of the chip. Crystals might list their oscillating frequency as their value. Basically, the value of a schematic component calls out its **most important characteristic**.

Component **names** are usually a combination of one or two letters and a number. The letter part of the name identifies the type of component \-- *R*\'s for resistors, *C*\'s for capacitors, *U*\'s for integrated circuits, etc. Each component name on a schematic should be unique; if you have multiple resistors in a circuit, for example, they should be named R~1~, R~2~, R~3~, etc. Component names help us reference specific points in schematics.

The prefixes of names are pretty well standardized. For some components, like resistors, the prefix is just the first letter of the component. Other name prefixes are not so literal; inductors, for example, are *L*\'s (because current has already taken *I* \[but it starts with a *C*\...electronics is a silly place\]). Here\'s a quick table of common components and their name prefixes:

  Name Identifier   Component
  ----------------- --------------------------
  R                 Resistors
  C                 Capacitors
  L                 Inductors
  S                 Switches
  D                 Diodes
  Q                 Transistors
  U                 Integrated Circuits
  Y                 Crystals and Oscillators

\

Although theses are the \"standardized\" names for component symbols, they\'re not universally followed. You might see integrated circuits prefixed with *IC* instead of *U*, for example, or crystals labeled as *XTAL*\'s instead of *Y*\'s. Use your best judgment in diagnosing which part is which. The symbol should usually convey enough information.

## Reading Schematics

Understanding which components are which on a schematic is more than half the battle towards comprehending it. Now all that remains is identifying how all of the symbols are connected together.

### Nets, Nodes and Labels

Schematic nets tell you how components are wired together in a circuit. Nets are represented as lines between component terminals. Sometimes (but not always) they\'re a unique color, like the green lines in this schematic:

[![Example of nets on a schematic](https://cdn.sparkfun.com/r/600-600/assets/d/2/9/c/c/51cdbd5fce395fc80b000000.png)](https://cdn.sparkfun.com/assets/d/2/9/c/c/51cdbd5fce395fc80b000000.png)

#### [][Junctions and Nodes](#junction_node)

Wires can connect two terminals together, or they can connect dozens. When a wire splits into two directions, it creates a **junction**. We represent junctions on schematics with **nodes**, little dots placed at the intersection of the wires.

[![A node](https://cdn.sparkfun.com/r/300-300/assets/7/d/2/c/8/51cdb29dce395fa40b000000.png)](https://cdn.sparkfun.com/assets/7/d/2/c/8/51cdb29dce395fa40b000000.png)

Nodes give us a way to say that \"wires crossing this junction *are* connected\". The absences of a node at a junction means two separate wires are just passing by, not forming any sort of connection. (When designing schematics, it\'s usually good practice to avoid these non-connected overlaps wherever possible, but sometimes it\'s unavoidable).

[![Example of connected an disconnected nodes](https://cdn.sparkfun.com/r/600-600/assets/0/1/7/4/5/51cdb378ce395f4309000000.png)](https://cdn.sparkfun.com/assets/0/1/7/4/5/51cdb378ce395f4309000000.png)

#### Net Names

Sometimes, to make schematics more legible, we\'ll give a net a name and label it, rather than routing a wire all over the schematic. Nets with the same name are assumed to be connected, even though there isn\'t a visible wire connecting them. Names can either be written directly on top of the net, or they can be \"tags\", hanging off the wire.

[![Linked name tags](https://cdn.sparkfun.com/r/600-600/assets/6/0/2/4/e/51cdb9d0ce395f2c0b000000.png)](https://cdn.sparkfun.com/assets/6/0/2/4/e/51cdb9d0ce395f2c0b000000.png)

*Each net with the same name is connected, as in this [schematic](http://cdn.sparkfun.com/datasheets/BreakoutBoards/ft231x-breakout-v01.pdf) for an [FT231X Breakout Board](https://www.sparkfun.com/products/11736). Names and labels help keep schematics from getting too chaotic (imagine if all those nets were actually connected with wires).*

Nets are usually given a name that specifically states the purpose of signals on that wire. For example, power nets might be labeled \"VCC\" or \"5V\", while [serial communication](https://learn.sparkfun.com/tutorials/serial-communication) nets might be labeled \"RX\" or \"TX\".

### Schematic Reading Tips

#### Identify Blocks

Truly expansive schematics should be split into functional blocks. There might be a section for power input and voltage regulation, or a microcontroller section, or a section devoted to connectors. Try recognizing which sections are which, and following the flow of circuit from input to output. Really good schematic designers might even lay the circuit out like a book, inputs on the left side, outputs on the right.

[![Example of a sectioned schematic](https://cdn.sparkfun.com/r/600-600/assets/8/a/3/9/0/51cdbe19ce395f160b000001.png)](https://cdn.sparkfun.com/assets/8/a/3/9/0/51cdbe19ce395f160b000001.png)

*If the drawer of a schematic is really nice (like the engineer who designed this [schematic](http://cdn.sparkfun.com/datasheets/Dev/Arduino/Boards/RedBoard-v06.pdf) for the [RedBoard](https://www.sparkfun.com/products/11804)), they may separate sections of a schematic into logical, labeled blocks.*

#### Recognize Voltage Nodes

Voltage nodes are single-terminal schematic components, which we can connect component terminals to in order to assign them to a specific voltage level. These are a special application of net names, meaning all terminals connected to a like-named voltage node are connected together.

[![Annotated voltage node example](https://cdn.sparkfun.com/r/600-600/assets/1/e/8/c/c/51cdc629ce395f6b4f000000.png)](https://cdn.sparkfun.com/assets/1/e/8/c/c/51cdc629ce395f6b4f000000.png)

*Like-named voltage nodes \-- like GND, 5V, and 3.3V \-- are all connected to their counterparts, even if there aren\'t wires between them.*

The ground voltage node is especially useful, because so many components need a connection to ground.

#### Reference Component Datasheets

If there\'s something on a schematic that just doesn\'t make sense, try finding a datasheet for the most important component. Usually the component doing the most work on a circuit is an integrated circuit, like a microcontroller or sensor. These are usually the largest component, oft-located at the center of the schematic.

## Interested in learning more foundational topics?

See our **[Engineering Essentials](https://www.sparkfun.com/engineering_essentials)** page for a full list of cornerstone topics surrounding electrical engineering.

[Take me there!](https://www.sparkfun.com/engineering_essentials)

![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/multimeter-300.png)