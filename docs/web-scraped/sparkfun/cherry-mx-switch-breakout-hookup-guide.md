# Source: https://learn.sparkfun.com/tutorials/cherry-mx-switch-breakout-hookup-guide

## Introduction

[Cherry MX Keyswitches](https://www.sparkfun.com/products/13834) are top-of-the-line mechanical keyboard switches. They\'re satisfyingly \"clicky\", reliable up to tens-of-millions of key presses, and an essential component in gaming and programming keyboards. To help make the switches more easily adaptable to breadboard or perfboard-based projects, we created the [SparkFun Cherry MX Switch Breakout](https://www.sparkfun.com/products/13773).

[![Cherry MX Switch Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/3/2/5/13773-01.jpg)](https://www.sparkfun.com/cherry-mx-switch-breakout.html)

### [Cherry MX Switch Breakout](https://www.sparkfun.com/cherry-mx-switch-breakout.html) 

[ BOB-13773 ]

Cherry MX Keyswitches are top-of-the-line mechanical keyboard switches. They're satisfyingly "clicky", reliable up to t...

[ [\$2.50] ]

[![Cherry MX Switch](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/4/3/1/13834-01.jpg)](https://www.sparkfun.com/cherry-mx-switch.html)

### [Cherry MX Switch](https://www.sparkfun.com/cherry-mx-switch.html) 

[ COM-13834 ]

Cherry MX Keyswitches are top-of-the-line mechanical keyboard switches. They're satisfyingly "clicky", reliable up to t...

[ [\$1.10] ]

In addition to breaking out the switch contacts to breadboard-compatible headers, the breakout also provides access to an optional switch-mounted LED. Plus, the pin break-outs are designed with keyboard matrix-ing in mind, so you can interconnect as many boards as you\'d like into a row-column configuration, keeping the I/O-pin requirements as low as possible.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Cherry MX Switch in action](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-03.jpg)   [![Matrixed Configuration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-11.jpg)
  *Cherry MX Switch in action*                                                                                                                                                                                                *Matrixed Configuration*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Cherry MX Switch Breakout is a perfect prototyping tool for input devices ranging from a single key to fully-custom 101-key keyboards.

### Covered In This Tutorial

This tutorial documents the SparkFun Cherry MX Switch Breakout, providing an overview of the breakout, plus some assembly and usage tips. It\'s broken down into a few sections, which you can navigate around using the buttons on the right.

Or use these links below to skip ahead:

1.  [Hardware Overview](https://learn.sparkfun.com/tutorials/cherry-mx-switch-breakout-hookup-guide#hardware-overview) \-- A breakdown of the Cherry MX Switch Breakout Board features.
2.  [Assembly Tips](https://learn.sparkfun.com/tutorials/cherry-mx-switch-breakout-hookup-guide#assembly-tips) \-- Tips for adding headers, wires, resistors, and diodes to the breakout board.
3.  [Testing the Circuit](https://learn.sparkfun.com/tutorials/cherry-mx-switch-breakout-hookup-guide#testing-the-circuit) \-- A simple circuit to test the switch, LED, and any other components you may add on.
4.  [Matrixing Breakouts](https://learn.sparkfun.com/tutorials/cherry-mx-switch-breakout-hookup-guide#matrixing-breakouts) \-- A guide to combining two or more breakout boards into a row/column matrix, and scanning them with an Arduino.

### Bill of Materials

In addition to the [Cherry MX Switch](https://www.sparkfun.com/products/13834) there are a few additional items you may want to add on to the [Breakout Board](https://www.sparkfun.com/products/13773).

**[3mm LEDs](https://www.sparkfun.com/categories/171)** can be placed inside the switch. Pick any color you please: [red](https://www.sparkfun.com/products/533), [green](https://www.sparkfun.com/products/9650), [yellow](https://www.sparkfun.com/products/532), or [cycling](https://www.sparkfun.com/products/11448).

[![LED - 3mm Cycling RGB (slow)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/3/0/2/11448-02b.jpg)](https://www.sparkfun.com/led-3mm-cycling-rgb-slow.html)

### [LED - 3mm Cycling RGB (slow)](https://www.sparkfun.com/led-3mm-cycling-rgb-slow.html) 

[ COM-11448 ]

These color-changing LEDs take the work out of creating crazy, flashy, blinky\... ness. Simply apply power and the LED will cy...

[ [\$0.60] ]

[![LED - Basic Red 3mm](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/3/00533-1.jpg)](https://www.sparkfun.com/led-basic-red-3mm.html)

### [LED - Basic Red 3mm](https://www.sparkfun.com/led-basic-red-3mm.html) 

[ COM-00533 ]

LEDs - those blinky things. A must have for power indication, pin status, opto-electronic sensors, and fun blinky displays. ...

[ [\$0.50] ]

[![LED - Basic Green 3mm](https://cdn.sparkfun.com/r/140-140/assets/parts/3/5/0/1/09650-01.jpg)](https://www.sparkfun.com/led-basic-green-3mm.html)

### [LED - Basic Green 3mm](https://www.sparkfun.com/led-basic-green-3mm.html) 

[ COM-09650 ]

LEDs - those blinky things. A must have for power indication, pin status, opto-electronic sensors, and fun blinky displays. ...

[ [\$0.50] ]

[![LED - Basic Yellow 3mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/7/3/00532-02-L.jpg)](https://www.sparkfun.com/led-basic-yellow-3mm.html)

### [LED - Basic Yellow 3mm](https://www.sparkfun.com/led-basic-yellow-3mm.html) 

[ COM-00532 ]

LEDs - those blinky things. A must have for power indication, pin status, opto-electronic sensors, and fun blinky displays. ...

[ [\$0.50] ]

The breakout board also provides a footprint for an optional **LED-current-limiting resistor**. 1/6W PTH resistors, like [these 330Ω\'s](https://www.sparkfun.com/products/11507), are recommended.

If you\'re matrixing multiple breakout boards together, you may want to add a **small-signal diode** to the board to help isolate the switches and prevent any possible \"ghosting\". Standard [1N4148 diodes](https://www.sparkfun.com/products/8588) should do the trick for this.

If you need to tie the board down, it has mounting holes designed to fit [2-56 screws](https://www.sparkfun.com/products/8992) and [nuts](https://www.sparkfun.com/products/8995).

[![Diode Small Signal - 1N4148](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/7/08589-03-L.jpg)](https://www.sparkfun.com/diode-small-signal-1n4148.html)

### [Diode Small Signal - 1N4148](https://www.sparkfun.com/diode-small-signal-1n4148.html) 

[ COM-08588 ]

This is a very common signal diode - 1N4148. Use this for signals up to 200mA of current.

[ [\$0.25] ]

[![Nut - Metal (2-56)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/2/1/08995-04.jpg)](https://www.sparkfun.com/nut-metal-2-56.html)

### [Nut - Metal (2-56)](https://www.sparkfun.com/nut-metal-2-56.html) 

[ PRT-08995 ]

\*\*Description\*\*: These are standard nuts with 2-56 thread. For use with 2-56 machine screws and five button pad set listed be...

[\$0.15] [ [\$0.04] ]

[![Screw - Flat Head (3/8\", 2-56)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/1/8/08992-02-L.jpg)](https://www.sparkfun.com/products/8992)

### [Screw - Flat Head (3/8\", 2-56)](https://www.sparkfun.com/products/8992) 

[ PRT-08992 ]

These are standard screws with 2-56 thread and 3/8\" long, recommended for the small button pad sets. Can be used with a 2-56 ...

**Retired**

[![Resistor 330 Ohm 1/6 Watt PTH - 20 pack](https://cdn.sparkfun.com/r/140-140/assets/parts/7/4/1/7/11507-02.jpg)](https://www.sparkfun.com/products/11507)

### [Resistor 330 Ohm 1/6 Watt PTH - 20 pack](https://www.sparkfun.com/products/11507) 

[ COM-11507 ]

1/6 Watt, +/- 5% tolerance PTH resistors. Commonly used in breadboards and perf boards, these 330Ohm resistors make excellent...

**Retired**

You\'ll need **soldering tools**, including a [soldering iron](https://www.sparkfun.com/products/9507) and [solder](https://www.sparkfun.com/products/9163). Other tools, like [wire strippers](https://www.sparkfun.com/products/12630), [flush cutters](https://www.sparkfun.com/products/11952), and a [third hand](https://www.sparkfun.com/products/9317), can also be helpful.

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Wire Strippers - 30AWG Hakko](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/1/2/12630-Hakko-Wire-Strippers-30AWG-Feature.jpg)](https://www.sparkfun.com/wire-strippers-30awg-hakko.html)

### [Wire Strippers - 30AWG Hakko](https://www.sparkfun.com/wire-strippers-30awg-hakko.html) 

[ TOL-12630 ]

It can be used as: Shears, Multi-diameter Wire stripper, pliers.

[ [\$13.95] ]

[![Flush Cutters - Xcelite](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/3/6/14782-Flush_Cutters_-_Xcelite-02.jpg)](https://www.sparkfun.com/products/14782)

### [Flush Cutters - Xcelite](https://www.sparkfun.com/products/14782) 

[ TOL-14782 ]

These are simple flush cutters from Excelite that give you a way to cut leads very cleanly and close to the solder joint.

**Retired**

Finally, [headers](https://www.sparkfun.com/products/116) or [wire](https://www.sparkfun.com/products/11367) will help connect the breakout board to your breadboard or development platform.

### Suggested Reading

This hookup guide relies on some beginner-level electronics knowledge. If any of the subjects below sound foreign to you, consider checking out that tutorial first:

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/diodes)

### Diodes 

A diode primer! Diode properties, types of diodes, and diode applications.

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

## Hardware Overview

While it may seem like a simple breakout, the Cherry MX Switch Breakout board is a little over-engineered. Here\'s a quick breakdown of the pin breakouts and additional features of the board.

[![Top of board annotated](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/top-annotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/top-annotated.jpg)

### Breakout Pin Labels

Up to four pins are used to interact with the Cherry MX Switch \-- two for the switch contacts and two for the optional LED. These pins are broken out on all sides of the board, labeled either \"1\", \"2\", \"+\", or \"-\". Those labels are short for:

  Pin Label   Pin Description
  ----------- ------------------
  1           Switch contact 1
  2           Switch contact 2
  \+          LED anode
  \-          LED cathode

If you only want to use the switch, the pins labeled \"1\" and \"2\" should be all you need. If you\'re integrating a 3mm LED, the LED\'s anode and cathode will be accessible on the \"+\" and \"-\" pins respectively.

#### Header Pairs

Every side of the breakout board is equipped with a four-pin header (don\'t confuse them with the diode or resistor pins), but not all of these headers are created equally! Two headers break out all four pins, while the other two headers *only* break out the LED anode and one of the switch contacts.

[![Switch headers labeled](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/headers-labeled.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/headers-labeled.png)

The pair of headers on the left and right sides of the board **break out all four pins**. These are intended for primary use. You can solder male pins into both of these headers, and plug the switch into a breadboard.

[![Example solder job on main headers on ly](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-02.jpg)

The pair of headers breaking *only* the LED anode and switch contact 1 are designed for keypad matrices, where multiple boards are connected in row/column pairs. More on this [later in the tutorial](https://learn.sparkfun.com/tutorials/cherry-mx-switch-breakout-hookup-guide#matrixing-breakouts).

## Assembly Tips

To use the breakout board, at a bare minimum you\'ll need to solder the Cherry MX Switch and either headers or wires to the \"1\" and \"2\" pins. [Male headers](https://www.sparkfun.com/products/116) work well for most breadboarding applications, while [solid-core](https://www.sparkfun.com/products/11367) or [stranded wire](https://www.sparkfun.com/products/11375) work well if you\'re wiring the breakout up to something afar.

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

There are plenty of other addon options, including a 3mm LED, current-limiting resistor, and switch isolating diodes, which are all documented below.

### 3mm LED

Most Cherry MX Switches \-- including the [blue, MX1A-E1NW](https://www.sparkfun.com/products/13834) switch we carry \-- have a recess in their body designed to fit a small [3mm LED](https://www.sparkfun.com/categories/171).

An \"A\" on the top side of the switch and a diode symbol on the backside both show the recommended polarity of the LED.

[![LED footprint in switch](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/switch-top-led.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/switch-top-led.jpg)

*The LED\'s recessed home in the switch. Note the \"A\" indicator for the LED\'s \"anode.\"*

To add an LED to the switch, insert the anode and cathode legs of the LED into their respective pins \-- the LED\'s longer, anode leg should be inserted into the \"A\" pin \-- then flip the board over, and solder the LED to the breakout board.

[![LED connected to breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-04.jpg)

#### Adding a Current-Limiting Resistor

If you\'re adding an LED to the switch, more likely than not, you\'ll need a current-limiting resistor. The breakout provides a resistor footprint, in-line with the LED. You\'ll find the resistor pads on the bottom-right corner of the board.

Small PTH resistors are recommended for this application -- **1/6W or 1/8W through-hole packages** work best. 1/4W resistors can be too large -- potentially interfering with any keycap that may be on the switch.

To connect an LED to the board, bend one of the resistor legs so it\'s parallel with the other. Then insert both legs into the board like so:

[![Resistor connected to board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-05.jpg)

You\'ll also need to **cut the \"R\" jumper** on the back side of the board, which might be easier to do before you solder anything. A [hobby knife](https://www.sparkfun.com/products/9200) and a steady hand should do the trick.

[![Resistor jumper location](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/resistor-jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/resistor-jumper.jpg)

By default, the board has a short across the current-limiting resistor. Cutting this jumper removes the short, and functionally adds the resistor to the circuit.

### Ghost-Prevention Diode

If you plan on interconnecting four-or-more breakouts \-- creating a row/column matrix of switches \-- you may also want to consider adding a **small-signal diode** to help prevent \"ghosting\". The [1N4148 small-signal diode](https://www.sparkfun.com/products/8588) is perfectly fit for this task.

#### Switch Matrix Ghosting

\"Ghosting\" is a problem that can adversely affect the detection of **multiple, simultaneous button presses**. Without diode protection, certain combinations of simultaneous button-presses can cause one-or-more un-actuated buttons to appear pressed (\"ghosted\"). The result is a false-positive key-press, which can cause undesired behavior in a project.

To avoid button ghosting, small-signal diodes can be placed in-circuit, after every key. The diode prevents a key\'s signal from \"backfeeding\" back through the line.

[![Ghost problem illustrated](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/row-col2x2-switches-shorted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/row-col2x2-switches-shorted.png)

While the diode does prevent ghosting, it does place certain restrictions on your button-press detection. It forces the switch contact on the diode\'s anode (positive) side to be at a higher voltage than the other contact, as the switch can only conduct meaningful current in one direction.

For more on keypad ghosting, check out [Byron\'s explanation in the Button Pad Hookup Guide](https://learn.sparkfun.com/tutorials/button-pad-hookup-guide#background).

A small, \"vertical\" diode footprint is broken out in the upper-right corner of the board. Near one of the pads in this footprint, a **small, white line** designates which pin should be connected to the **diode\'s cathode** (negative) pin.

To solder a diode into the board, bend the anode leg down, so it\'s parallel with the cathode leg. Then insert the diode into the board \-- making sure to place the cathode leg (usually indicated by a black bar) into the marked hole.

[![Diode added to breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-06.jpg)

You\'ll also need to **cut the \"D\" jumper** on the back side of the board \-- otherwise the diode will be shorted over. (This may be easier if you do it before soldering anything.)

[![Diode jumper location](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/diode-jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/diode-jumper.jpg)

Like the resistor, the breakout shorts across the diode. Cutting this jumper removes the short and functionally adds the diode to the circuit.

### Mounting Hole Size

A pair of mounting holes are provided on opposite corners of the breakout board. These holes are designed to fit **2-56 (3/8\")** screws. [Flat heads](https://www.sparkfun.com/products/8992) are recommended, though [rounded heads](https://www.sparkfun.com/products/8993) can work as well.

[![Screw - Phillips Head (3/8\", 2-56)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/1/9/08993-01.jpg)](https://www.sparkfun.com/screw-phillips-head-3-8-2-56.html)

### [Screw - Phillips Head (3/8\", 2-56)](https://www.sparkfun.com/screw-phillips-head-3-8-2-56.html) 

[ PRT-08993 ]

These are standard screws with 2-56 thread and 3/8\" long, recommended for the small button pad sets. Can be used with a 2-56 ...

[\$0.15] [ [\$0.05] ]

[![Nut - Metal (2-56)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/2/1/08995-04.jpg)](https://www.sparkfun.com/nut-metal-2-56.html)

### [Nut - Metal (2-56)](https://www.sparkfun.com/nut-metal-2-56.html) 

[ PRT-08995 ]

\*\*Description\*\*: These are standard nuts with 2-56 thread. For use with 2-56 machine screws and five button pad set listed be...

[\$0.15] [ [\$0.04] ]

[![Screw - Flat Head (3/8\", 2-56)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/1/8/08992-02-L.jpg)](https://www.sparkfun.com/products/8992)

### [Screw - Flat Head (3/8\", 2-56)](https://www.sparkfun.com/products/8992) 

[ PRT-08992 ]

These are standard screws with 2-56 thread and 3/8\" long, recommended for the small button pad sets. Can be used with a 2-56 ...

**Retired**

If you\'re going to be doing a lot of jamming on your keyboard, you\'ll want it tied down!

## Testing the Circuit

With just a power supply and a few wires, you can create a quick circuit to test out your switch, LED, resistor and diode. Wire up the **\"+\" pin to 5V** (or 3.3V). Then **connect \"-\" and \"1\"** together. And wire up **\"2\" to ground**. (If you didn\'t add a current-limiting resistor, make sure you add one externally! It can take the place of the wire from \"+\" to power, or 2 to ground.)

[![Breadboard test circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-01.jpg)

Now actuate the switch, and watch for the LED to illuminate.

Note that, if you\'ve added the ghosting diode, this is the only polarity in which the switch will work \-- pin 1 must be at a higher voltage than pin 2.

## Matrixing Breakouts

The Cherry MX Switch Breakout Board\'s are designed with switch matrix-ing in mind. By creating a row/column matrix of switches, you can save on potentially dozens of microcontroller I/O pins. A 64-key keyboard, for example, can be scanned with just 16 I/O pins.

### Key Spacing

While there is no specific standard for keyboard key spacing, most full-size keyboard keys are spaced by 3/4\" (0.75in) from center-to-center. Rows may be offset by either 3/8\" (0.375in) or 3/16\" (0.1875in), or not at all.

[![Typical keyboard offsets](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/z_011306keycapspacing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/z_011306keycapspacing.jpg)

*Typical keyboard row offsets. (Image courtesy of [The PC Guide](http://www.pcguide.com/ref/kb/const/capSize-c.html).)*

The breakout is designed to make typical key spacing as easy as possible. By cleverly jumping one board to the next, you can add any of the standard offsets to nearby rows.

[![standard keyboard spacing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/matrix-examples_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/matrix-examples_1.png)

So, plan out your keyboard, and grab a soldering iron!

### Creating a Key Matrix

To create a matrix of switches, arrange your boards as desired. Along the rows, line up the \"2\", \"1\", \"-\", and \"+\" labels. You will, however, **only connect the \"2\" and \"-\" pins across rows**. Solder your rows together first:

[![Row of three built up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-07.jpg)

There's not an easy method to soldering boards together. You'll probably need [wire strippers](https://www.sparkfun.com/products/12630) to split and cut [solid-core wire](https://www.sparkfun.com/products/11367) into tiny (\~3/8\") pieces. A [third hand](https://www.sparkfun.com/products/9317) can be a big-time help keeping boards stationary while you solder the little wires in place.

Once you\'ve created your rows, line up the **columns by matching the \"1\" and \"+\" pins**. There are three offset options available, as documented in the image above.

[![Two rows put together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-08.jpg)

Here is an example of a fully built-up 3x3 matrix. The middle row is offset from the top by 3/16\", and the bottom row is offset from the middle by 3/8\". This will make the middle row equivalent to a keyboard\'s A, S, and D keys, the top row Q, W, and E, and the bottom row Z, X, and C \-- we\'re making a 9-key keypad centered around WASD!

[![3x3 keyboard layout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-10.jpg)

Finish off the soldering job by connecting wires to the row and column pins you\'ll need access to. If you\'re not using any LEDs, you\'ll only need to solder to the \"1\" pins along the rows, and \"2\" pins along the columns.

[![3x3 keypad fully soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/Cherry_MX_Switch_Tutorial-11.jpg)

Don\'t forget to add your switches, and LEDs, resistors, or diodes, should your project require them!

### Keypad Scanning Arduino Code

Here\'s a simple Arduino sketch, designed to work with a 9-key, 3x3 matrix, but easily expandable for larger keypads.

The sketch assumes a circuit like this:

[![Example 9-key keypad hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/3/keypad-hookup-example_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/3/keypad-hookup-example_bb.png)

*It may look like a mess of wires, but \-- with 9 switches and LEDs \-- we\'ve at least turned 18 wires into 12.*

  Row/Column Name   Breakout Label   Arduino Pin
  ----------------- ---------------- -------------
  LED Row 1         \-               2
  LED Row 2         \-               3
  LED Row 3         \-               4
  LED Column 1      \+               5
  LED Column 2      \+               6
  LED Column 3      \+               7
  Switch Row 1      2                8
  Switch Row 2      2                9
  Switch Row 3      2                10
  Switch Column 1   1                11
  Switch Column 2   1                12
  Switch Column 3   1                13

Then copy this code and upload:

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /* Button/LED Matrix Scanning Example - 3x3 Keypad
       Code derived from Button Pad Hookup Guide Example 2
       by Byron Jacquot @ SparkFun Electronics
         https://learn.sparkfun.com/tutorials/button-pad-hookup-guide#exercise-2-monochrome-plus-buttons
    */
    //////////////////////
    // Config Variables //
    //////////////////////
    #define NUM_LED_COLS (3) // Number of LED columns (+, anode)
    #define NUM_LED_ROWS (3) // Number of LED rows (-, cathode)
    #define NUM_BTN_COLS (3) // Number of switch columns (isolating diode anode)
    #define NUM_BTN_ROWS (3) // Number of switch rows (isolating diode cathode)

    // Debounce built-in to the code. This sets the number of button
    // high or low senses that trigger a press or release
    #define MAX_DEBOUNCE (3)

    ////////////////////
    // Hardware Setup //
    ////////////////////
    static const uint8_t btnRowPins[NUM_BTN_ROWS] = ; // Pins connected to switch rows (2)
    static const uint8_t btnColPins[NUM_BTN_COLS] = ; // Pins connected to switch columns (1)
    static const uint8_t ledRowPins[NUM_LED_ROWS] = ; // Pins connected to LED rows (-)
    static const uint8_t ledColPins[NUM_LED_COLS] = ; // Pins connected to LED cols (+)

    //////////////////////
    // Global Variables //
    //////////////////////
    static bool LED_buffer[NUM_LED_COLS][NUM_LED_ROWS]; // Keeps track of LED states
    static int8_t debounce_count[NUM_BTN_COLS][NUM_BTN_ROWS]; // One debounce counter per switch

    void setup()
    
      }
      // Initialize the LED buffer
      for (uint8_t i = 0; i < NUM_LED_COLS; i++)
      
      }
    }

    void loop() 
    

    static void scan()
    
      }

      // Scan through switches on this row:
      for ( j = 0; j < NUM_BTN_COLS; j++)
      
          }
        }
        else // Otherwise, button is released
        
          }
        }
      }

      // Once done scanning, de-select the switch and LED rows
      // by writing them HIGH.
      digitalWrite(btnRowPins[currentRow], HIGH);
      digitalWrite(ledRowPins[currentRow], HIGH);

      // Then turn off any LEDs that might have turned on:
      for (i = 0; i < NUM_LED_ROWS; i++)
      

      // Increment currentRow, so next time we scan the next row
      currentRow++;
      if (currentRow >= NUM_LED_ROWS)
      
    }

    static void setupLEDPins()
    

      // LED select columns - Write HIGH to turn an LED on.
      for (i = 0; i < NUM_LED_COLS; i++)
      
    }

    static void setupSwitchPins()
    

      // Buttn select columns. Pulled high through resistor. Will be LOW when active
      for (i = 0; i < NUM_BTN_COLS; i++)
      
    }

Whenever you press a switch, the LED on that switch should also light up. Releasing the switch turns the LED off.

#### Adapting the Code

The code is adaptable for larger or smaller matrices, with a few modifications towards the top of the sketch.

Modify the number of rows or columns in the `Config Variables` section:

    language:c
    //////////////////////
    // Config Variables //
    //////////////////////
    #define NUM_LED_COLS (3) // Number of LED columns (+, anode)
    #define NUM_LED_ROWS (3) // Number of LED rows (-, cathode)
    #define NUM_BTN_COLS (3) // Number of switch columns (diode anode)
    #define NUM_BTN_ROWS (3) // Number of switch rows (diode cathode)

And/or convert the pin connections in the `Hardware Setup` section:

    language:c
    ////////////////////
    // Hardware Setup //
    ////////////////////
    static const uint8_t btnRowPins[NUM_BTN_ROWS] = ; // Pins connected to switch rows (2)
    static const uint8_t btnColPins[NUM_BTN_COLS] = ; // Pins connected to switch columns (1)
    static const uint8_t ledRowPins[NUM_LED_ROWS] = ; // Pins connected to LED rows (-)
    static const uint8_t ledColPins[NUM_LED_COLS] = ; // Pins connected to LED cols (+)

If you\'ve added **ghost-prevention diodes**, keep in mind that the switch\'s \"1\" pins (organized as the columns) must be at a higher potential than the row, \"2\" pins.

To scan the keypad matrix, we recommend pulling the row pins high using a pull-up resistor (often internal to I/O pins). Then progressively pulling the column pins to ground and checking which of the rows, if any, are pulled low as well.