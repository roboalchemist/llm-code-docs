# Source: https://learn.sparkfun.com/tutorials/large-solderable-breadboard-hookup-guide

## Introduction

Solderless breadboards are great for prototyping. But they\'re not exactly mechanically robust. It seems like something, somewhere is always coming loose. Having a solderable board with a matching trace pattern allows you to make a prototype more solid without having to lay out a custom PCB.

[![Solderable Breadboard](https://cdn.sparkfun.com/assets/e/0/4/b/9/default.jpg)](https://cdn.sparkfun.com/assets/e/0/4/b/9/default.jpg)

At first glance, the [large solderable breadboard](https://www.sparkfun.com/products/12699) mirrors the hole pattern of a regular [large solderless breadboard](https://www.sparkfun.com/products/112). However, on closer inspection, you\'ll find that it has some extra features that should ease the transition from solderless to solderable board.

In this tutorial, we\'ll go over the features of the soderable breadboard, show you how to use it as the most basic level, and then show you more advanced examples.

### Suggested Reading:

- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire)
- [What is a Circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

## Quick Overview

I\'ve used a number of similar soderable breadboards through the years, but many of them left something to be desired. The common ones are made from brittle phenolic PCB material. The copper traces are thin, poorly adhered, and tend to peel off when you rework the board. And most problematically, the trace pattern doesn\'t always mimic a solderless breadboard \-- the power rails don\'t match, or the center has four holes instead of five. Moving a circuit from to the soldered board involved extra translation work.

The large solderless breadboard is intended to solve those issues. It is a real FR4 fiberglass board, with soldermask, plated through-holes, and the layout duplicates the connectivity of a solderless breadboard.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/2/f/0/5/3/Solderable_Breadboard_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/2/f/0/5/3/Solderable_Breadboard_Hookup_Guide-01.jpg)

*Closeup of the pattern at the center of the board.*

The center area of the breadboard mimics the hookup pattern of the solderless board - twin rows of 5 holes each, spaced 0.3\" apart, to accommodate DIP ICs. Like the equivalent solderless board, the solderable board has 63 columns. The row and column coordinates are labeled to match the solderless boards.

Compared to the solderless boards, this solderable board also offers more flexiblity in how the power supplies can be wired.

### Power Supply Background

A typical power supply provides a number of voltages to the attached circuitry. Each voltage is often referred to as a *rail*. [\*](#rail) The number of supply rails needed, and the voltages provided on each, depend on the sort of circuitry being deployed.

- To begin, every power supply has a \"ground\" rail. Ground is used as a 0V reference point, the voltage against which the others will be measured; it may not actually be connected to Earth.
- For many years, digital circuits used a single 5V rail. More recently, lower supply voltages have become common, primarily 3.3V, but sometimes even lower, such as 1.8V.
- Analog designs frequently use higher voltage bipolar power supplies, which provide mirror-image positive and negative rails. +/-12V and +/-15V are both common.
- A *mixed signal* design involves both analog and digital sections, and brings along the supply voltage requirements form each. A good example would be a PC power supply, that provides 3.3V and 5V for the digital logic, and +/-12V for things like disk drive motors and cooling fans.

On a solderless breadboard, there are usually a pair of supply rails at each edge, that run the length of the board (though sometimes they aren\'t totally continuous, split at the halfway point). They\'re frequently marked with \"+\" and \"-\" symbols, possibly also color coded red and blue. The breadboard doesn\'t make any assumptions about how the rails get used \-- it\'s up to the user to feed voltages to the rails.

So with that, lets explore how to configure the supply rails on this breadboard.

------------------------------------------------------------------------

[] \* I\'m having trouble finding a definitive etymology, but I believe the \"rail\" term stems from the use of the \"third rail\" to supply voltage on an electric railway, a usage that dates back to the 1880\'s.

## Optional Jumpers

With no further configuration, this board has 5 traces that run the length of the board. Four of them are the + and - traces at the top and bottom edges of the board, duplicating the equivalent points on a solderless board. The fifth of these traces runs down the \"gutter\" at the center of the board, intended for use as a ground.

These 5 traces meet with 5-pin 5mm screw terminals at each end of the board. The order of the terminals matches the order of the traces across the board. As seen below, the top screw terminal pin connects to the top \"-\" rail, the next screw terminal down meets the top \"+\" rail, and so on.

[![alt text](https://cdn.sparkfun.com/assets/e/0/4/b/9/default.jpg)](https://cdn.sparkfun.com/assets/e/0/4/b/9/default.jpg)

The board can be adapted with wire jumpers to accommodate a number of different voltage rail combinations.

The jumpers are as follows

- JG1, JG2, JG3, JG4 can be populated to tie the mounting holes to the ground trace. If you are mounting the board in a metal enclosure, it\'s good practice to ground the enclosure, and join the circuit ground to the enclosure.
- JG5 and JG6 can be used to join the - rails at the edges of the board to the ground track down the center of the board.
- TIE+ and TIE- connect the + and - rails on each side of the board, respectively. Just like a solderless board, these aren\'t connected by default, but this board provides an easier option to tie them together.

The board also accepts screw 5mm terminals for the power connections, which can be populated to match the rail configuration. If you\'d prefer a more solid connection than screw terminals provide, you can also solder wire directly to the pads.

The power connections and jumpers are duplicated at each end of the board. In most applications, you\'ll only need to use the connections at one end.

## Some Examples

### Digital Circuit With One Supply Rail

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/1/7/b/0/5/Solderable_Breadboard_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/1/7/b/0/5/Solderable_Breadboard_Hookup_Guide-02.jpg)

*Jumper details for single voltage, plus ground.*

If you\'re building a digital circuit with a single supply rail (typically 3.3V or 5V), make the following connections

- Bridge jumpers TIE+ and TIE-.
- Bridge jumpers JG5 or JG6.
- Install a 2 position 5MM screw terminal. As seen above
  - The red wire is the supply voltage.
  - The black wire is ground.

When you install components, they can pick up the supply voltage on either + rail, and ground on the - rails or at the center ground trace.

### Analog Circuit With Bipolar Rails

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/b/2/3/b/4/Solderable_Breadboard_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/b/2/3/b/4/Solderable_Breadboard_Hookup_Guide-03.jpg)

*Jumper details for bipolar supply voltages, plus ground.*

For an analog circuit with a bipolar power supply, configure the jumpers as follows

- Bridge jumpers TIE+ and TIE-.
- Install a 3 position 5MM screw terminal. As seen above
  - The red wire is the + supply voltage.
  - The blue wire is the - supply voltage.
  - The black wire is ground.

Components can pick up the positive supply voltage on either + rail, the negative supply voltage on either - rail, and ground on the center trace.

### Multiple Boards

If you\'re building a larger circuit using more than one of these boards, they can share a power supply. The most common configuration is known as \"star power distribution.\" The power supply forms the center of the system, and each board is connected directly to it.

[![Star Power](https://cdn.sparkfun.com/assets/2/0/4/0/b/star-power1_1.jpg)](https://cdn.sparkfun.com/assets/2/0/4/0/b/star-power1_1.jpg)

Or, redrawn for simplicity.

[![alt text](https://cdn.sparkfun.com/assets/0/3/f/9/5/star-power2.jpg)](https://cdn.sparkfun.com/assets/0/3/f/9/5/star-power2.jpg)

This configuration makes a direct connection between the supply and each board.