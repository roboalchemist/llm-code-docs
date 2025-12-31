# Source: https://learn.sparkfun.com/tutorials/integrated-circuits

## Introduction

Integrated circuits (ICs) are a keystone of modern electronics. They are the heart and brains of most circuits. They are the ubiquitous little black \"chips\" you find on just about every circuit board. Unless you\'re some kind of crazy, analog electronics wizard, you\'re likely to have at least one IC in every electronics project you build, so it\'s important to understand them, inside and out.

[![Example of ICs on a PCB](https://cdn.sparkfun.com/assets/d/8/a/b/5/51dc69f2ce395fab63000000.png)](https://cdn.sparkfun.com/assets/d/8/a/b/5/51dc69f2ce395fab63000000.png)

*Integrated circuits are the little black \"chips\", found all over embedded electronics.*

An IC is a collection of electronic components \-- [resistors](https://learn.sparkfun.com/tutorials/resistors), [transistors](https://learn.sparkfun.com/tutorials/transistors), [capacitors](https://learn.sparkfun.com/tutorials/capacitors), etc. \-- all stuffed into a tiny chip, and connected together to achieve a common goal. They come in all sorts of flavors: single-circuit logic gates, op amps, 555 timers, voltage regulators, motor controllers, microcontrollers, microprocessors, FPGAs\...the list just goes on-and-on.

### Covered in this Tutorial

- The make-up of an IC
- Common IC packages
- Identifying ICs
- Commonly used ICs

### Suggested Reading

Integrated circuits are one of the more fundamental concepts of electronics. They do build on some previous knowledge, though, so if you aren\'t familiar with these topics, consider reading their tutorials first\...

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/diodes)

### Diodes 

A diode primer! Diode properties, types of diodes, and diode applications.

[](https://learn.sparkfun.com/tutorials/polarity)

### Polarity 

An introduction to polarity in electronic components. Discover what polarity is, which parts have it, and how to identify it.

[](https://learn.sparkfun.com/tutorials/capacitors)

### Capacitors 

Learn about all things capacitors. How they\'re made. How they work. How they look. Types of capacitors. Series/parallel capacitors. Capacitor applications.

[](https://learn.sparkfun.com/tutorials/transistors)

### Transistors 

A crash course in bi-polar junction transistors. Learn how transistors work and in which circuits we use them.

## Inside the IC

When we think integrated circuits, little black chips are what come to mind. But what\'s inside that black box?

[![Internal view of an IC](https://cdn.sparkfun.com/r/600-600/assets/7/a/6/9/c/51c0d009ce395feb33000000.jpg)](https://cdn.sparkfun.com/assets/7/a/6/9/c/51c0d009ce395feb33000000.jpg)

*The guts of an integrated circuit, visible after [removing the top](https://www.sparkfun.com/news/384).*

The real \"meat\" to an IC is a complex layering of semiconductor wafers, copper, and other materials, which interconnect to form transistors, resistors or other components in a circuit. The cut and formed combination of these wafers is called a **die**.

[![Overview of internal IC](https://cdn.sparkfun.com/r/400-400/assets/e/f/1/b/8/51c0d009ce395ff933000000.jpg)](https://cdn.sparkfun.com/assets/e/f/1/b/8/51c0d009ce395ff933000000.jpg)

*An overview of an IC die.*

While the IC itself is tiny, the wafers of semiconductor and layers of copper it consists of are incredibly thin. The connections between the layers are very intricate. Here\'s a zoomed in section of the die above:

[![Microscopic view of an IC](https://cdn.sparkfun.com/assets/b/0/2/6/4/51c0d456ce395f0334000000.jpg)](https://cdn.sparkfun.com/assets/b/0/2/6/4/51c0d456ce395f0334000000.jpg)

An IC die is the circuit in its smallest possible form, too small to solder or connect to. To make our job of connecting to the IC easier, we package the die. The IC package turns the delicate, tiny die, into the black chip we\'re all familiar with.

## IC Packages

The package is what encapsulates the integrated circuit die and splays it out into a device we can more easily connect to. Each outer connection on the die is connected via a tiny piece of gold wire to a **pad** or **pin** on the package. Pins are the silver, extruding terminals on an IC, which go on to connect to other parts of a circuit. These are of utmost importance to us, because they\'re what will go on to connect to the rest of the components and wires in a circuit.

There are many different types of packages, each of which has unique dimensions, mounting-types, and/or pin-counts.

[![Package variety chart](https://cdn.sparkfun.com/assets/a/9/8/b/8/51c1ea70ce395f5f0d000000.jpg)](https://cdn.sparkfun.com/assets/c/7/a/1/9/51e0633cce395f867b000000.jpg)

### Polarity Marking and Pin Numbering

All ICs are [polarized](https://learn.sparkfun.com/tutorials/polarity/integrated-circuit-polarity), and every pin is unique in terms of both location and function. This means the package has to have some way to convey which pin is which. Most ICs will use either a **notch** or a **dot** to indicate which pin is the first pin. (Sometimes both, sometimes one or the other.)

[![Package with notch/dot labeled](https://cdn.sparkfun.com/assets/8/7/3/1/6/51c1ee09ce395f421f000000.png)](https://cdn.sparkfun.com/assets/8/7/3/1/6/51c1ee09ce395f421f000000.png)

Once you know where the first pin is, the remaining pin numbers increase sequentially as you move counter-clockwise around the chip.

[![DIP pin numbering](https://cdn.sparkfun.com/assets/f/0/a/1/f/51c206efce395f0f0d000003.png)](https://cdn.sparkfun.com/assets/f/0/a/1/f/51c206efce395f0f0d000003.png)

### Mounting Style

One of the main distinguishing package type characteristics is the way they mount to a circuit board. All packages fall into one of two mounting types: through-hole (PTH) or surface-mount (SMD or SMT). **Through-hole** packages are generally bigger, and much easier to work with. They\'re designed to be stuck through one side of a board and soldered to the other side.

**Surface-mount** packages range in size from small to minuscule. They are all designed to sit on one side of a circuit board and be soldered to the surface. The pins of a SMD package either extrude out the side, perpendicular to the chip, or are sometimes arranged in a matrix on the bottom of the chip. ICs in this form factor are not very \"hand-assembly-friendly.\" They usually require [special tools](https://learn.sparkfun.com/tutorials/electronics-assembly) to aid in the process.

### DIP (Dual in-line packages)

DIP, short for dual in-line package, is the most common through-hole IC package you\'ll encounter. These little chips have two parallel rows of pins extending perpendicularly out of a rectangular, black, plastic housing.

[![DIP package example](https://cdn.sparkfun.com/r/600-600/assets/8/b/d/d/d/51dc7161ce395f8303000000.png)](https://cdn.sparkfun.com/assets/8/b/d/d/d/51dc7161ce395f8303000000.png)

*The 28-pin [ATmega328](https://www.sparkfun.com/products/9061) is one of the more popular DIP-packaged microcontrollers (thanks, Arduino!).*

Each of the pins on a DIP IC are spaced by 0.1\" (2.54mm), which is a standard spacing and perfect for fitting into [breadboards](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) and other prototyping boards. The overall dimensions of a DIP package depend on its pin count, which may be anywhere from four to 64.

The area between each row of pins is perfectly spaced to allow DIP ICs to straddle the center area of a breadboard. This provides each of the pins its own row in the board, and it makes sure they don\'t [short](https://learn.sparkfun.com/tutorials/what-is-a-circuit/short-and-open-circuits) to each other.

[![DIP chips on a breadboard](https://cdn.sparkfun.com/r/600-600/assets/1/5/4/e/9/51c1e4eece395f1c1f000000.png)](https://cdn.sparkfun.com/assets/1/5/4/e/9/51c1e4eece395f1c1f000000.png)

Aside from being used in breadboards, DIP ICs can also be **soldered into PCBs**. They\'re inserted into one side of the board and soldered into place on the other side. Sometimes, instead of soldering directly to the IC, it\'s a good idea to **socket** the chip. Using sockets allows for a DIP IC to be removed and swapped out, if it happens to \"let its blue smoke out.\"

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/b/f/b/4/9/51e0773dce395f8560000000.jpg)](https://cdn.sparkfun.com/assets/b/f/b/4/9/51e0773dce395f8560000000.jpg)

*A regular [DIP socket](https://www.sparkfun.com/products/7940) (top) and a [ZIF socket](https://www.sparkfun.com/products/9175) with and without an IC.*

### Surface-Mount (SMD/SMT) Packages

There is a huge variety of surface-mount package types these days. In order to work with surface-mount packaged ICs, you usually need a custom printed circuit board ([PCB](https://learn.sparkfun.com/tutorials/pcb-basics)) made for them, which has a matching pattern of copper on which they\'re soldered.

Here are a few of the more common SMD package types out there, ranging in hand-solderability from \"doable\" to \"doable, but only with special tools\" to \"doable only with *very* special, usually automated tools\".

#### Small-Outline (SOP)

Small-outline IC (SOIC) packages are the surface-mount cousin of the DIP. It\'s what you\'d get if you bent all the pins on a DIP outward, and shrunk it down to size. With a steady hand, and a close eye, these packages are among the easiest SMD parts to hand solder. On SOIC packages, each pin is usually spaced by about 0.05\" (1.27mm) from the next.

The SSOP (shrink small-outline package) is an even smaller version of SOIC packages. Other, similar IC packages include TSOP (thin small-outline package) and TSSOP (thin-shrink small-outline package).

[![Example of SSOP mounted, quarter added for size-comparison](https://cdn.sparkfun.com/r/600-600/assets/9/e/4/5/6/51c32e10ce395fdc13000000.png)](https://cdn.sparkfun.com/assets/9/e/4/5/6/51c32e10ce395fdc13000000.png)

*A 16-Channel Multiplexer ([CD74HC4067](https://www.sparkfun.com/products/299)) in a 24-pin SSOP package. Mounted on a board in the middle (quarter added for size-comparison).*

A lot of the more simple, single-task-oriented ICs like the [MAX232](https://www.sparkfun.com/products/589) or [multiplexers](https://www.sparkfun.com/products/299) come in SOIC or SSOP forms.

#### Quad Flat Packages

Splaying IC pins out in all four directions gets you something that might look like a quad flat package (QFP). QFP ICs might have anywhere from eight pins per side (32 total) to upwards of seventy (300+ total). The pins on a QFP IC are usually spaced by anywhere from 0.4mm to 1mm. Smaller variants of the standard QFP package include thin (TQFP), very thin (VQFP), and low-profile (LQFP) packages.

[![TQFP example package](https://cdn.sparkfun.com/r/400-400/assets/8/3/6/3/b/51dc6e21ce395f0807000000.png)](https://cdn.sparkfun.com/assets/8/3/6/3/b/51dc6e21ce395f0807000000.png)

*The [ATmega32U4](https://www.sparkfun.com/products/11181) in a 44-pin (11 on each side) TQFP package.*

If you sanded the legs off a QFP IC, you get something that might look like a **quad-flat no-leads (QFN)** package. The connections on QFN packages are tiny, exposed pads on the bottom corner edges of the IC. Sometimes they wrap around, and are exposed on both the side and bottom, other packages only expose the pad on the bottom of the chip.

[![Example of QFN package](https://cdn.sparkfun.com/r/600-600/assets/b/4/a/1/7/51dc6f5bce395fc963000006.png)](https://cdn.sparkfun.com/assets/b/4/a/1/7/51dc6f5bce395fc963000006.png)

*The multitalented [MPU-6050]() IMU sensor comes in a relatively tiny QFN package, with 24 total pins hiding on the bottom edge of the IC.*

Thin (TQFN), very thin (VQFN), and micro-lead (MLF) packages are smaller variations of the standard QFN package. There are even dual no-lead (DFN) and thin-dual no-lead (TDFN) packages, which have pins on just two of the sides.

Many microprocessors, sensors, and other modern ICs come in QFP or QFN packages. The popular [ATmega328](https://www.sparkfun.com/products/9261) microcontroller is offered in both a TQFP package and a QFN-type (MLF) form, while a tiny [accelerometer](https://learn.sparkfun.com/tutorials/accelerometer-basics)/[gyroscope](https://learn.sparkfun.com/tutorials/gyroscope) like the [MPU-6050](https://www.sparkfun.com/products/10937) comes in a miniscule QFN form.

#### Ball Grid Arrays

Finally, for really advanced ICs, there are ball grid array (BGA) packages. These are amazingly intricate little packages where little balls of solder are arranged in a 2-D grid on the bottom of the IC. Sometimes the solder balls are attached directly to the die!

[![Example of BGA package](https://cdn.sparkfun.com/assets/0/8/7/c/4/51dc6d9bce395f2103000000.png)](https://cdn.sparkfun.com/assets/0/8/7/c/4/51dc6d9bce395f2103000000.png)

BGA packages are usually reserved for advanced microprocessors, like those on the [pcDuino](https://www.sparkfun.com/products/11712) or [Raspberry Pi](https://www.sparkfun.com/products/11546).

If you can hand solder a BGA-packaged IC, consider yourself a master solderer. Usually, to put these packages onto a PCB requires an automated procedure involving pick-and-place machines and reflow ovens.

## Common ICs

Integrated circuits are prevalent in so many forms across electronics, it\'s hard to cover everything. Here are a few of the more common ICs you might encounter in educational electronics.

### Logic Gates, Timers, Shift Registers, Etc.

Logic gates, the building blocks of much more ICs themselves, can be packaged into their own integrated circuit. Some logic gate ICs might contain a handful of gates in one package, like this quad-input AND gate:

[![Logic gate pinout](https://cdn.sparkfun.com/r/300-300/assets/5/b/9/9/b/51dc7fb8ce395f1d1c000000.png)](https://cdn.sparkfun.com/assets/5/b/9/9/b/51dc7fb8ce395f1d1c000000.png)

Logic gates can be connected inside an IC to create timers, counters, latches, shift registers, and other basic logic circuitry. Most of these simple circuits can be found in DIP packages, as well as SOIC and SSOP.

### Microcontrollers, Microprocessors, FPGAs, Etc.

Microcontrollers, microprocessors, and FPGAs, all packing thousands, millions, even billions of transistors into a tiny chip, are all integrated circuits. These components exist in a wide range in functionality, complexity, and size; from an 8-bit microcontroller like the [ATmega328](https://www.sparkfun.com/products/9061) in an [Arduino](https://www.sparkfun.com/products/11021), to a complex 64-bit, multi-core microprocessor organizing activity in your computer.

These components are usually the largest IC in a circuit. Simple microcontrollers can be found in packages ranging from DIP to QFN/QFP, with pin counts lying somewhere between eight and a hundred. As these components grow in complexity, the package gets equally complex. [FPGAs](https://www.sparkfun.com/products/11838) and complex [microprocessors](https://www.sparkfun.com/products/11712) can have upwards of a thousand pins and are only available in advanced packages like QFN, LGA, or BGA.

### Sensors

Modern digital sensors, like temperature sensors, [accelerometers](https://learn.sparkfun.com/tutorials/accelerometer-basics), and [gyroscopes](https://learn.sparkfun.com/tutorials/gyroscope) all come packed into an integrated circuit.

These ICs are usually smaller than the microcontrollers, or other ICs on a circuit board, with pin counts in the three to twenty range. DIP sensor ICs are becoming a rarity, as modern components are usually found in QFP, QFN, even BGA packages.