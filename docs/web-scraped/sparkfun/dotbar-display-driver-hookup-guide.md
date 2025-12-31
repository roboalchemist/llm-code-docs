# Source: https://learn.sparkfun.com/tutorials/dotbar-display-driver-hookup-guide

## Introduction

The [LM3914](https://www.sparkfun.com/products/12694) and [LM3916](https://www.sparkfun.com/products/12695) are a two ICs in a series of monolithic, analog-controlled LED drivers. With these chips, all it takes is a single, **analog signal** to drive a string of 10+ LEDs, which can be configured into either **bar mode** (where all LEDs below a certain point turn on) or **dot mode** (with only a single LED on at a time). Hook them up properly, and you can create all sorts of nifty multi-LED displays, like an audio-visualizing [VU meter](http://en.wikipedia.org/wiki/VU_meter).

[![Example VU Meter - 4 IC\'s driving 40 LEDs](https://cdn.sparkfun.com/r/600-600/assets/a/0/1/5/4/52d81e7ece395f06448b456e.jpg)](https://cdn.sparkfun.com/assets/a/0/1/5/4/52d81e7ece395f06448b456e.jpg)

These two ICs are similar in pin-out and interface. They differ in how they map an analog signal to output LED. The LM3914 uses a **linear** output scale while the LM3916 uses a more **logarithmic VU (volume unit) scale**, which makes it well-suited to audio applications.

In this tutorial we\'ll [dig into the datasheet](https://learn.sparkfun.com/tutorials/dotbar-display-driver-hookup-guide/ic-overview) of these LED drivers to find out what makes them tick, and take a close look at the pinout of the 18-pin DIP chips. Finally, we\'ll show a pair of example circuits that show a [simple](https://learn.sparkfun.com/tutorials/dotbar-display-driver-hookup-guide/example-hookup---simple-dotbar-display) hookup and a more [advanced, cascaded](https://learn.sparkfun.com/tutorials/dotbar-display-driver-hookup-guide/example-hookup---cascading) hookup.

### Required Materials

If you want to follow along with this tutorial, here are the components we used to make our driver circuits:

- IC: 1x [LM3914](https://www.sparkfun.com/products/12694) for the simple circuit, 2-4x [LM3916](https://www.sparkfun.com/products/12695) for the cascaded circuit.
- Display: [5mm LEDs](https://www.sparkfun.com/products/9881) and/or 2-4 [Bar Graph LEDs](https://www.sparkfun.com/products/9935)
- A variety of resistors from the [Resistor Kit](https://www.sparkfun.com/products/10969)
- [Full-Size Breadboard](https://www.sparkfun.com/products/12615)
- [Potentiometer](https://www.sparkfun.com/products/9806) (or any sensor that can produce an analog signal)
- [Breadboard Jumper Wires](https://www.sparkfun.com/products/124)
- Power Supply:
  - [5V AC Adapter](https://www.sparkfun.com/products/8269) and [Barrel Jack Adapter](https://www.sparkfun.com/products/10288) -or-
  - [Breadboard Power Supply](https://www.sparkfun.com/products/10804) (with [male headers](https://www.sparkfun.com/products/116) soldered in)

### Suggested Reading

Working with these ICs is fairly simple \-- no crazy microcontrollers or programming required! Here are a few basic electronics concepts you should be familiar with, before moving forward:

- [Integrated Circuits (ICs)](https://learn.sparkfun.com/tutorials/integrated-circuits)
- [Analog vs. Digital](https://learn.sparkfun.com/tutorials/analog-vs-digital)
- [Light-Emitting Diodes (LEDs)](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)
- [Resistors](https://learn.sparkfun.com/tutorials/resistors)
- [Voltage Dividers](https://learn.sparkfun.com/tutorials/voltage-dividers)
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

## IC Overview

On this page we\'ll take a look at the pinout of the 18-pin LM3914/6. We\'ll also dig a little deeper to see what makes the ICs do what they do.

### The Pinout

The DIP (through-hole, dual-inline package) version of this chip has 18 pins, and both a dot and notch to indicate [polarity](https://learn.sparkfun.com/tutorials/polarity).

[![Chip pinout](https://cdn.sparkfun.com/assets/d/e/5/7/e/52d81a30ce395f27228b4569.png)](https://cdn.sparkfun.com/assets/d/e/5/7/e/52d81a30ce395f27228b4569.png)

Over half of the pins are in charge of driving the LEDs. The remaining pins are used for power, reference voltages, and control of the IC. Here is an overview of the chip\'s pinout:

  Pin \#   Pin Name    Pin Function                  Pin \#   Pin Name   Pin Function
  -------- ----------- -------------------------- -- -------- ---------- --------------------------------
  1        LED 1       First (lowest value) LED      18       LED 2      2nd LED
  2        V^−^        Ground                        17       LED 3      3rd LED
  3        V^+^        Supply voltage (3-25V)        16       LED 4      4th LED
  4        R~LO~       Divider low voltage           15       LED 5      5th LED
  5        Signal In   Analog signal in              14       LED 6      6th LED
  6        R~HI~       Divider high voltage          13       LED 7      7th LED
  7        Ref Out     Reference output voltage      12       LED 8      8th LED
  8        Ref Adj     Voltage reference adjust      11       LED 9      9th LED
  9        Mode        Dot/Bar mode select           10       LED 10     Last (higest analog input) LED

That may seem a daunting list of pins and reference voltages to supply, but in reality it can be very simple. Many of those pins can either be tied to ground, V~CC~, or even left floating. Other pins may require a resistor or two to set constant current or voltage values.

#### LED Outputs

The **LED outputs** are all open-collectors, so they sink current. Connect the **cathode** of an LED to these pins and tie the other pin of the LED \-- the **anode** \-- to your voltage supply. There is no need for current limiting resistors, as the chip takes care of current regulation.

#### Mode Select

The *Mode* pin allows you to select between \"bar\" mode and \"dot\" mode. In bar mode, all LEDs sequentially turn on. So, if the signal voltage is near max, *all* LEDs should be on. In \"dot\" mode just a single LED is on at any time. Connect mode directly to the power source for bar mode, and leave it floating for dot mode.

  Mode                             Mode Pin Setting
  -------------------------------- ------------------------------------------------------
  Bar Graph                        Tied directly to V^+^
  Dot Display                      Left floating (no connection)
  Dot Display (cascaded drivers)   Mode pin of first driver connected to pin 1 of next.

#### Setting the Analog Range with R~HI~ and R~LO~

The *R~HI~* (pin 6) and *R~LO~* (pin 4) pins are used to map the sensing range of the LM3914/6. *R~HI~* sets the maximum voltage, and *R~LO~* sets the minimum voltage.

These two pins can be connected to any voltage as long as it\'s 1.5V below the supply voltage (V^+^), and greater than 0V.

#### Setting LED Current with Ref Out

The current drawn out of the *Ref Out* pin (pin 7) sets the current that flows through each LED, so this pin can be used to adjust the **LED brightness**.

If a resistor (R~L~) is connected from that pin to ground, the current flowing through each LED will be about equal to this equation:

[![LED current equation](https://cdn.sparkfun.com/assets/f/1/8/0/4/52d57552ce395fe15d8b4567.)](https://cdn.sparkfun.com/assets/f/1/8/0/4/52d57552ce395fe15d8b4567.)

So, for example, if you have a 1kΩ resistor connected from pin 7 to ground, the LED current should be around 12.5 mA.

If you have a more complex circuit connected to this pin, remember that the voltage between *Ref Out* and *Ref Adj* pin (pin 8) should be 1.25V. And the LED current is equal to 10 times the current coming out of *Ref Out*.

### The Internals \-- A Chain of Comparators

**Note:** It\'s not critical to understand how these chips work, but it is a neat study into the internals of an [integrated circuit](https://learn.sparkfun.com/tutorials/integrated-circuits). Feel free to skip to the [next page](https://learn.sparkfun.com/tutorials/dotbar-display-driver-hookup-guide/example-hookup---simple-dotbar-display), if this looks a little too much like a Circuits I class.

The image below, from the [LM3914/6 datasheet](http://cdn.sparkfun.com/datasheets/Components/General%20IC/lm3914.pdf), provides an excellent overview of what\'s going on inside these chips:

[![LM3914/6 Block Diagram](https://cdn.sparkfun.com/r/600-600/assets/c/5/e/f/7/52d47451ce395f53338b4567.png)](https://cdn.sparkfun.com/assets/c/5/e/f/7/52d47451ce395f53338b4567.png)

Each LED is controlled by the output of a **comparator**, which is a very simple op amp circuit. If the voltage going into the + (non-inverting) pin is greater than that going into − (inverting), the comparator outputs a 1 (high, or, in this case the pin \"floats\"). If the − pin voltage is greater than +, the output of the comparator is a 0 (pulled towards ground).

[![Comparator input/output equation](https://cdn.sparkfun.com/r/300-300/assets/f/b/8/d/5/52d56383ce395f9f498b4567.png)](https://cdn.sparkfun.com/assets/f/b/8/d/5/52d56383ce395f9f498b4567.png)

*The input/output combinations of a comparator.*

Inside the chip, the analog control signal from pin 5 is connected to each of the inverting (−) inputs on the comparators. The non-inverting (+) inputs of the comparators are connected to a string of 1kΩ resistors, which create larger-and-larger [voltage dividers](https://learn.sparkfun.com/tutorials/voltage-dividers). The + voltage on the first comparator will be the **divider input voltage** (R~HI~ − R~LO~), while the + voltage on the last comparator is 1/10^th^ of that voltage.

To turn an LED on \-- meaning the comparator\'s output is 0 \-- the analog signal voltage must be greater than the divided input on a comparator. So a smaller signal voltage is required to turn on the first LED in comparison to any of the following.

### Voltage and Current Ratings

The LM3914/6 ICs have a very wide supply voltage range: anywhere from **1.8V to 18V**.

The voltage between the R~HI~ and R~LO~ pins can be anything between 0V (thought, that wouldn\'t be too useful) and **1.5V below the supply voltage**. So, if you\'re powering the chip at 5V, it\'ll only be able to map voltages between 0V and 3.5V.

Also, keep in mind the current that might be flowing through the chip. Each LED can take anywhere between 7 and 13 mA, and to supply the chip you\'ll need an additional 2 to 9 mA.

## Example Hookup - Simple Dot/Bar Display

On this page, we\'ll go over a very simple, single IC, 10 LED hookup. This will show you how to set the **LED current**, the **divider voltage**, and how to select between **dot or bar** display mode.

This circuit will work for both an LM3914 and LM3916. The only difference will be the of analog voltages required to turn on each of the LEDs.

### Breadboard and Schematic View

Here are a pair of diagrams that detail this simple layout. We\'ll assume the circuit is powered by 5V. If your supply voltage is different, some resistor values may need to change (see further below).

[![Simple circuit schematic view](https://cdn.sparkfun.com/r/600-600/assets/f/b/d/1/e/52d709fece395f4c6e8b4567.png)](https://cdn.sparkfun.com/assets/f/b/d/1/e/52d709fece395f4c6e8b4567.png)

*Schematic view of simple LM3914 circuit.*

[![Simple circuit breadboard view](https://cdn.sparkfun.com/r/600-600/assets/f/2/b/d/5/52d709a1ce395f0b1b8b4567.png)](https://cdn.sparkfun.com/assets/f/2/b/d/5/52d709a1ce395f0b1b8b4567.png)

*Breadboard view of LM3914 circuit.*

The **analog input** in this example is a potentiometer, which is good for testing, but boring otherwise. Feel free to substitute that for any analog sensor, or even an audio signal from a microphone or stereo.

The **switch** can be used to swap between **dot or bar mode**. If the mode pin is pulled high, the IC will be in bar mode. If that pin is left floating, the display works in dot mode.

Finally, the LEDs. Pick any combination of color or size that you like. These 10-output LED drivers are perfect for the [10-Segment Bar Graph LEDs](https://www.sparkfun.com/products/9935). Or you can choose a combination of any other LEDs you might have handy. [5mm LEDs](https://www.sparkfun.com/products/9881) are a bit too big to fit perfectly into this breadboard hookup, so you may have to creatively bend them to make them fit:

[![simple circuit photo](https://cdn.sparkfun.com/r/600-600/assets/0/a/e/7/8/52d80e6ece395f3c3d8b4569.jpg)](https://cdn.sparkfun.com/assets/0/a/e/7/8/52d80e6ece395f3c3d8b4569.jpg)

There is no need for current-limiting resistors, but make sure you have each LED connected in the correct direction (anode is connected to your power supply, cathode to IC pin).

There are a variety of options available for [powering the display](https://learn.sparkfun.com/tutorials/how-to-power-a-project). In the example above we used a [5V Wall Wart](https://www.sparkfun.com/products/8269) plugged into a [Barrel Jack Adapter](https://www.sparkfun.com/products/10288), with a pair of wires flowing from there to the breadboard. If you are using a breadboard, the [5V/3.3V Breadboard Power Supply](https://www.sparkfun.com/products/10804) might make your life easier.

### Setting the Reference Voltage and LED Current

The two resistors in this circuit are used to set both the **current** flowing through the LEDs, and the **high voltage** end of the voltage divider.

In this circuit, the R~HI~ pin is tied to our reference voltage output. To calculate that voltage, knowing your two resistor values, use this equation:

[![Vref equation](https://cdn.sparkfun.com/assets/1/9/4/4/9/52d704d0ce395fe86c8b456b.png)](https://cdn.sparkfun.com/assets/1/9/4/4/9/52d704d0ce395fe86c8b456b.png)

Then, knowing V~REF~, you can calculate the current through an LED with this equation:

[![LED current equation](https://cdn.sparkfun.com/assets/f/3/8/f/0/52d70467ce395f5c438b456b.png)](https://cdn.sparkfun.com/assets/f/3/8/f/0/52d70467ce395f5c438b456b.png)

In the circuit above, where R1 is 2.2kΩ and R2 is 3.3kΩ, V~REF~ will be about **3.4V** (safely 1.5V under the supply voltage). I~LED~ will be about **7.2mA** \-- a happy, medium current for most LEDs.

If you need to pick a wider or smaller range, you\'ll have to play with those resistor values, but the equations should hold true.

## Example Hookup - Cascading

By cascading these IC\'s you can create incredibly (almost overly) sensitive VU meters, driving 40 or even more LEDs.

[![40 LED VU Meter](https://cdn.sparkfun.com/r/600-600/assets/a/0/1/5/4/52d81e7ece395f06448b456e.jpg)](https://cdn.sparkfun.com/assets/a/0/1/5/4/52d81e7ece395f06448b456e.jpg)

*4 LM3916\'s chained together to produce a 40 LED VU meter.*

Here\'s how you could chain two of these drivers together:

[![cascade schematic](https://cdn.sparkfun.com/r/600-600/assets/e/d/7/c/4/52d71728ce395f7c5c8b456f.png)](https://cdn.sparkfun.com/assets/e/d/7/c/4/52d71728ce395f7c5c8b456f.png)

*Schematic of a dual LM3914/6 cascade.*

The mode pins are permanently tied to the 5V supply, which forces the displays into bar mode. A bit of extra wiring is required to get cascaded LM3914/6\'s into a proper dot mode. Check out the [datasheet](http://cdn.sparkfun.com/datasheets/Components/General%20IC/lm3914.pdf) (page 11) for help with that.

[![cascade breadboard](https://cdn.sparkfun.com/r/600-600/assets/b/d/0/e/5/52d7174fce395f13068b4569.png)](https://cdn.sparkfun.com/assets/b/d/0/e/5/52d7174fce395f13068b4569.png)

*Breadboard view of two cascaded LM3914/6\'s.*

In this example, we use the [bar graph LEDs](https://www.sparkfun.com/products/9935), which seem to be made for the LM3914/6. Make sure you connect the anodes of the LEDs to your supply voltage, and the cathode pins can be connected directly to the output pins on the driver.

The key to cascading is linking the *R~LO~* and *R~HI~* pins properly. *R~LO~* (pin 4) of the lowest IC in the chain should be connected to ground, and *R~HI~* (pin 6) of the highest IC in the chain should be connected to the maximum voltage in your sensing range. Between those two points, *R~HI~* of one IC should be connected to *R~LO~* of the next. This will chain each of those resistor strings inside the ICs together, to create a large set of highly sensitive voltage dividers inside the chips.

Following that process, you can chain even more of these ICs together to create some magnificient VU meters or other displays.