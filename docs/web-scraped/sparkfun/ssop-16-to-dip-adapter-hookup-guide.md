# Source: https://learn.sparkfun.com/tutorials/ssop-16-to-dip-adapter-hookup-guide

## Introduction

The SparkFun [16-Pin SSOP to DIP Adapter](https://www.sparkfun.com/products/13994) is a small PCB that lets you adapt 14 and 16-pin [SSOP packages](https://en.wikipedia.org/wiki/Small_Outline_Integrated_Circuit) to a DIP footprint. These are useful for modding and upgrading devices that use 16-pin DIP ICs, when the upgraded IC is only available in a SSOP footprint. You can also use it for prototyping, to make SSOP packages compatible with solderless breadboards.

[![SparkFun SSOP to DIP Adapter - 16-Pin](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/6/7/13994-01.jpg)](https://www.sparkfun.com/sparkfun-ssop-to-dip-adapter-16-pin.html)

### [SparkFun SSOP to DIP Adapter - 16-Pin](https://www.sparkfun.com/sparkfun-ssop-to-dip-adapter-16-pin.html) 

[ BOB-13994 ]

The SparkFun 16-Pin SSOP to DIP Adapter is a small PCB that lets you adapt SSOP packages into a DIP footprint. These small bo...

[ [\$4.25] ]

The updated version of this adapter comes as a dual array of PCBs \-- if you\'re adapting one chip, you\'re likely to adapt more than one. The PCBs easily snap apart, resulting in two individual boards.

The SSOP-16 land pattern on the board has also been improved from its predecessor. First, the SSOP and DIP pin numbering matches \-- both packages count counterclockwise from their respective pin 1. The board also fits in a standard 0.3\" wide DIP footprint. The pads are very long, to accomodate 3.9mm, 4.4mm and 5.3mm package widths. They are on 0.635mm centers, but, with careful installation, an IC with 0.65mm leads will also fit. The board is contained entirely within the DIP outline, for situations with no extra clearance around the IC. Finally, if you leave two pads disconnected, SSOP-14 packages also fit.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-02.jpg)

Old Vs New

### Suggested Reading

Check out any of the links below, if you are unfamiliar with a given topic.

- [PCB Basics](https://learn.sparkfun.com/tutorials/pcb-basics)
- [Integrated Circuits (ICs)](https://learn.sparkfun.com/tutorials/integrated-circuits)
- [SMD Footprint Creation Tutorial](https://learn.sparkfun.com/tutorials/designing-pcbs-smd-footprints)
- [How To Use A Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [SMD Soldering](https://www.sparkfun.com/tutorials/107)

## Assembly

Assembling the adapter is fairly straightforward, but there are a couple of tricks that make it easier.

### Materials

To build up an adapter, you\'ll need the following pieces.

- An SSOP-16 integrated circuit to adapt.
- The [16-pin SSOP to DIP adapter board](https://www.sparkfun.com/products/13994).
- Some [break away male headers](https://www.sparkfun.com/products/116) or [flip pins](https://www.sparkfun.com/products/14085).
- Some solder, either [leaded](https://www.sparkfun.com/products/9161) or [lead-free](https://www.sparkfun.com/products/9325).
- Solder flux, either liquid, or in a pen-type applicator.
- [Solder wick](https://www.sparkfun.com/products/8775), to help clean up excess solder.

### Tools

The following tools are also recommended.

- A [soldering iron](https://www.sparkfun.com/products/11704) with a [fine-point tip](https://www.sparkfun.com/products/10721).
- A magnifying glass or [loupe](https://www.sparkfun.com/products/9316).
- [Cross-lock](https://www.sparkfun.com/products/12572) tweezers.
- A [solderless breadboard](https://www.sparkfun.com/products/12043), to use as an assembly jig.

## Building An Adapter

### Snap Boards Apart

The array of boards was scored when it was manufactured. If you bend along the scores, the boards snap apart easily.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-03.jpg)

Snap Apart

### Prepare To Solder

It\'s easiest to solder the IC in place before you mount the headers, so you don\'t have to work around the protruding pins.

If this is your first time soldering surface mount ICs, patience and a steady hand are the key to good solder joints.

- Neatness Counts \-- you want to put on enough solder to join the legs to the pads, but not so much that adjacent legs are accidentally bridged.
- Work Quickly \-- if you leave the hot soldering iron on the board too long, you risk burning the traces and pads off the board. You want the iron at a temperature where the solder flows almost immediately when you apply it to the iron. Somewhat counter-intuitively, a hotter iron can be less damaging than a cooler one \-- having the iron at a hotter temperature allows you to work more quickly, reducing the potential for damage.

### Solder IC In Place

To install the IC, we\'ll be using a technique known as \"drag soldering.\" In drag soldering, we drag a blob of solder across the IC pins, depositing some on each as it goes by. If there\'s too much solder after dragging, we\'ll remove it with wick.

Before we show you how to drag solder, we want to emphasize the need for flux before starting, and the likelihood that you\'ll need some solder wick to clean up excess solder.

First, apply flux to the PCB. Flux cleans off the thin layer of oxidation the forms on the pads and allows molten solder to flow onto them.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-05.jpg)

*Applying Flux.*

Pin 1 of the IC is usually marked with a small dimple or notch in the IC body. Line these marks up with the corresponding marks in the PCB silkscreen. The silkscreen actually has three marks: a notch at one end of the IC, a dot within the IC outline, and a dot just outside the IC (which remains visible once the IC is soldered down).

To get started, flow a tiny bit of solder onto pads on opposite corners of the SSOP footprint.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-06.jpg)

*Solder on opposing corners.*

Grab the IC with the tweezers, and orient it over the footprint. Reheat one of the solder blobs from the previous step so the IC lead adheres to it. The solder should flow onto the IC legs, tacking the part in place. Press the IC down flat before the solder cools.

Then repeat this on the opposite leg, to hold the IC in place for the rest of the soldering operation.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-07.jpg)

*Corners tacked in place.*

When it\'s in place, doublecheck that the rest of the pins are reasonably aligned with their pads. If the placement needs adjustment, reheat one corner, and move the IC.

If you\'re careful and have a dainty soldering iron, you can proceed around the chip, soldering down each lead individually.

Of course, we\'re not especially dainty. The tip of our iron is gigantic compared to the lead pitch of an SSOP, so we\'re going to use a different technique, known as *drag soldering*.

To start drag soldering, heat a pin with the iron, then flow a blob of solder onto it. Once the solder flows, use the iron to drag the blob across the remaining leads.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/unnamed.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/unnamed.gif)

*Drag Soldering.*

As you drag the blob, it will adhere each pin to the corresponding pad.

When you reach the end of the line of pins, there might be some blob remaining, and there will probably be some excess solder bridging adjacent pins.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-08.jpg)

*Excess between leads.*

Use the solder wick to clean these up.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-09.jpg)

*.*

Repeat the process down the other side of the IC.

When you\'re done, take a moment to inspect your work. Check that each lead has a solder fillet to the pad underneath and that leads aren\'t shorted to their neighbors. It gets harder to touch things up once the pins have been soldered on.

### Solder In Header Pins

With the IC in place, now you can solder on the pins. We\'ll demonstrate using both plain break-sway headers and flip pins. Flip-pins are special pins that are the size and shape of regular DIP-IC legs. They fit in breadboards and IC sockets better than plain square-pin headers.

#### Regular Headers

Soldering in regular headers is easier if you have a jig that can hold the pins while you solder. It turns out that a solderless breadboard has a bunch of holes with the proper alignment!

Start by breaking 8-pin segments off the header. Insert them into the breadboard, two rows apart.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-12.jpg)

Pin in Breadboard

Set the PCB over the headers. Take care to keep the pins aligned straight up and down.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-13.jpg)

PCB On Pins

Work your way around the PCB, soldering each pin from the top of the board.

#### Flip Pins

Flip pins come packaged in a black plastic shroud, which keeps them aligned until they have been installed. The shroud also works as an assembly jig.

[![alt text](https://cdn.sparkfun.com/assets/parts/1/1/9/5/0/14085-01.jpg)](https://cdn.sparkfun.com/assets/parts/1/1/9/5/0/14085-01.jpg)

*Flip Pins.*

To start, stand two sets of flip pins up on your workbench. Then place the PCB on top of the pins. The tail on flip pins is as long as the PCB is thick \-- they won\'t protrude above the PCB.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-14.jpg)

*Assembling flip pins.*

Work your way around the board, soldering in each pin. Take care to keep the pins aligned perpendicular to the plane of the bench top. Once the pins have been soldered on, carefully slide the plastic pin aligner off, revealing the IC-type pins.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-15.jpg)

*Revealing the pins.*

### Deflux

Once you\'ve finished soldering, look at the solder joints. If they appear to have a yellow or brown coating on or around them, the board has flux residue (under a magnifying glass, it might look like amber or burnt sugar). Flux is acidic and can cause problems with long-term reliability, so it\'s best to clean it off.

You\'ll have to check the documentation for your solder for the proper cleaning methodology. Some flux is water soluble, while some requires a solvent like isopropyl alcohol or acetone.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-18.jpg)

*Defluxing.*

### Verify

Before we jump into applications of the SSOP-to-DIP adapter board, let\'s take a moment to doublecheck our work.

A quick visual inspection can help spot solder bridges or solder joints that didn\'t flow properly. It\'s also a good time for one last check, to make certain that pin one of the SSOP is properly oriented.

For a little extra confidence, you can also use a [multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter) in [continuity mode](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter#continuity) to verify that the legs of the SSOP are connected to the pads but not bridged to their neighbors.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-11.jpg)

*Continuity check.*

## Using The Adapter

### Adapter Orientation

The pins of the DIP footprint are rotated 90° in relation to the pins of the SSOP. We covered the pin-1 markings for the SSOP in the [assembly](https://learn.sparkfun.com/tutorials/ssop-16-to-dip-adapter-hookup-guide#assembly) section.

Pin 1 of the DIP footprint is marked two ways. The solder pad for pin 1 is square, while the others are round. It also has a small `1` in the silkscreen near the pad.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/top.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/top.png)

Pin markings, top

Pins 1 and 9 are also marked in the legend silkscreened on the bottom of the board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/bottom.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/bottom.png)

Pin markings, bottom

### Case Studies

#### On a Breadboard

This adapter is useful when you want to build a breadboard prototype using a chip that\'s only available in SSOP. It allows the chip to properly fit the rows of the breadboard.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-19.jpg)

Breadboard Example

#### Upgrading Old Devices

Another common use of a SSOP-to-DIP adapter is upgrading or modifying existing equipment\...or, as in this case, saving your bacon when you\'ve purchased components with the wrong footprint.

We\'re working on restoring an old [SparkFun Function Generator Kit](https://www.sparkfun.com/products/retired/10015) and needed a 74HC04 logic chip. When we ordered it, we didn\'t read the description carefully enough, and we got a 14-pin SSOP IC. Unfortunately, it needed to fit it into a DIP footprint on the board. Thankfully, we\'ve got an adapter board to help.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-20.jpg)

*14 pins in a 16-pin adapter.*

If you look closely, you\'ll notice two things in the above photo: first, the IC only has 14 pins on a 16-pin adapter board. Second, it is a wider SSOP package than we\'ve seen in the other examples. Thankfully, the land pattern on the PCB has extra-long pads to accommodate it.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-21.jpg)

*Installed in socket.*

Since the PCB already had a socket, we opted to use flip pins on the adapter. We\'re fitting a 14-pin chip on a 16-pin adapter, so we opted to keep pin-1 aligned on both pieces. This also means that the chip is two pins short \-- we\'re not using pins 8 and 9 on the adapter, and pins 10 through 16 on the adapter are off by two, connected to IC pins 8 to 14.