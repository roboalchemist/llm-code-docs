# Source: https://learn.sparkfun.com/tutorials/8-pin-soic-to-dip-adapter-hookup-guide

## Introduction

The SparkFun [8-Pin SOIC to DIP Adapter](https://www.sparkfun.com/products/13655) is a small PCB that lets you adapt [SOIC packages](https://en.wikipedia.org/wiki/Small_Outline_Integrated_Circuit) into a DIP footprint. These are useful for modding and upgrading devices that use 8-pin DIP ICs, when the upgraded IC is only available in a SOIC footprint. You can also use it for prototyping, to make SOIC packages compatible with solderless breadboards.

[![SOIC Adapter Array](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/array-iso.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/array-iso.jpg)

The updated version of this adapter comes as a small array of PCBs \-- if you\'re adapting one chip, you\'re likely to adapt more than one. The PCBs easily snap apart, resulting in four individual boards.

The SOIC land pattern on the board has also been improved from its predecessor. The pads are very long, in order to accomodate both [narrow](https://en.wikipedia.org/wiki/Small_Outline_Integrated_Circuit#Narrow_SOIC_.28JEDEC.29) and [wide](https://en.wikipedia.org/wiki/Small_Outline_Integrated_Circuit#Wide_SOIC) packages. The SOIC lands are staked down with plated through-holes, to prevent lifting during rework. The SOIC is also contained entirely within the DIP outline, for situations with no extra clearance around the IC.

[![Old Vs. New](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/comparison.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/comparison.jpg)

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

- A SOIC-8 integrated circuit to adapt.
- The [8-pin SOIC to DIP adapter board](https://www.sparkfun.com/products/13655).
- Some [break away male headers](https://www.sparkfun.com/products/116).
- Some solder, either [leaded](https://www.sparkfun.com/products/9161) or [lead-free](https://www.sparkfun.com/products/9325).

### Tools

The following tools are also recommended.

- A [soldering iron](https://www.sparkfun.com/products/11704) with a [fine-point tip](https://www.sparkfun.com/products/10721).
- A magnifying glass or [loupe](https://www.sparkfun.com/products/9316).
- [Cross-lock](https://www.sparkfun.com/products/12572) tweezers.
- A [solderless breadboard](https://www.sparkfun.com/products/12043), to use as an assembly jig.

### Building An Adapter

#### Snap Boards Apart

The array of boards was scored when it was manufactured. If you bend along the scores, the boards snap apart easily.

[![Snap Apart](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/snapping.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/snapping.jpg)

#### Prepare To Solder

It\'s easiest to solder the IC in place before you mount the headers, so you don\'t have to work around the protruding pins.

If this is your first time soldering surface mount ICs, patience and a steady hand are the key to good solder joints.

- Neatness Counts \-- you want to put on enough solder to join the legs to the pads, but not so much that adjacent legs are accidentally bridged.
- Work Quickly \-- if you leave the hot soldering iron on the board too long, you risk burning the traces and pads off the board. You want the iron at a temperature where the solder flows almost immediately when you apply it to the iron. Somewhat counter-intuitively, a hotter iron can be less damaging than a cooler one \-- having the iron at a hotter temperature allows you to work more quickly, reducing the potential for damage.

#### Solder IC In Place

First, heat one corner land (aka pad) on the PCB.

[![Heating first pad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/first-pad.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/first-pad.jpg)

Once it\'s hot, flow a little solder onto it.

[![One Solder Blob](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/one-blob.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/one-blob.jpg)

Pin 1 of the IC is usually marked with a small dimple in the IC body, or that end of the chip is marked with a notch. Line these marks up with the corresponding marks in the silkscreen. The silkscreen actually has three marks, a notch at one end of the IC, a dot within the IC outline, and a dot just outside the IC (which remains visible once the IC is soldered down).

[![SOIC Pin1 Marks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/SOIC-pin-1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/SOIC-pin-1.png)

Grab the IC with the tweezers, and orient it over the footprint. Reheat the solder blob from the previous step, so the IC lead adheres to it. Press the IC down flat before the solder cools.

[![One Leg Soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/chip-one-leg.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/chip-one-leg.jpg)

At this point, it doesn\'t have to be a perfect solder fillet, but the IC should be sitting flat on the board, and all of the leads should align with the PCB pads. If the alignment isn\'t good, or if pin one is the wrong way around, reheat the solder, and adjust the placement. This becomes a lot harder to fix after more pads get soldered down.

With the chip properly aligned, you can work your way around the chip, soldering each lead. It works best if you use the tip of the soldering iron to heat the IC lead and the PCB land at the same time, then flow a tiny bit of solder to join them.

[![All Leads Soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/chip-no-pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/chip-no-pins.jpg)

When you get back to the first lead, you can reheat the joint, flow a little more solder, and make sure the leave a neat fillet.

#### Solder In Header Pins

With the IC in place, now you can solder on the header pins. It\'s easier if you have a jig that can hold the pins while you solder. It turns out that a solderless breadboard has a bunch of holes with the proper alignment!

Start by breaking off the 4-pin segments off the header. Insert them into the breadboard, two rows apart.

[![Pin in Breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/pins-in-breadboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/pins-in-breadboard.jpg)

Set the PCB over the headers. Take care to keep the pins aligned straight up and down.

[![PCB On Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/pcb-stet-on-pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/pcb-stet-on-pins.jpg)

Work your way around the PCB, soldering each pin from the top of the board. When it\'s complete, it should look like the board below.

[![Fully Assembled](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/assembled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/assembled.jpg)

#### Deflux

Once you\'ve finished soldering, look at the solder joints. If they appear to have a yellow or brown coating on or around them, the board has flux residue (under a magnifying glass, it might look like burnt sugar). Water soluble flux is acidic, and can cause problems with long-term reliability, so it\'s best to clean it off.

You\'ll have to check the documentation for your solder for the proper cleaning methodology. Some flux is water soluble, while some requires a solvent like isopropyl alcohol or acetone.

#### Verify

Before we jump into applications of the SOIC-to-DIP adapter board, let\'s take a moment to doublecheck our work.

A quick visual inspection can help spot solder bridges, or solder joints that didn\'t flow properly. It\'s also a good time for one last check, to make certain that pin one of the SOIC is properly oriented.

[![Whoops!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/solder-blob.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/solder-blob.jpg)

For a little extra confidence, you can also use a [multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter?_ga=1.108769729.273388466.1418147030) in [continuity mode](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter?_ga=1.108769729.273388466.1418147030#continuity), to verify that the legs of the SOIC are connected to the pins.

## Using The Adapter

### Adapter Orientation

The pins of the DIP footprint are rotated 90° in relation to the pins of the SOIC. We covered the pin-1 markings for the SOIC in the [assembly](https://learn.sparkfun.com/tutorials/8-pin-soic-to-dip-adapter-hookup-guide/assembly) section.

Pin 1 of the DIP footprint is marked two ways.

First, the solder pad for pin 1 is square, while the others are round.

[![DIP Pin 1, top](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/DIP-pin-1_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/DIP-pin-1_2.png)

Second, pins 1 and 8 are marked in the legend silkscreened on the bottom of the board.

[![DIP Pins, bottom](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/DIP-8-1-marks.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/DIP-8-1-marks.jpg)

### Case Studies

#### On a Breadboard

This adapter is useful when you want to build a breadboard prototype using a chip that\'s only available in SOIC. It allows the chip to properly fit the rows of the breadboard.

[![Breadboard Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/opamp-oscillator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/opamp-oscillator.jpg)

*Dual-opamp Oscillator On Breadboard*

#### Upgrading Old Devices

Another common use of a SIOC-to-DIP adapter is upgrading or modifying existing equipment.

At one time, this was a way to update the BIOS on a PC motherboard, though more recently DIP-8 EPROMS have been less prevalent, and surface-mount memories are more commonplace, which are usually reprogrammable without being removed from the motherboard.

Chip substitution is also a common practice among hi-fi and pro audio enthusiasts, sometimes called *chip rolling* or *POOGE*-ing (*P*rogressive *O*ptimization *O*f *G*eneric *E*quipment). Many of these devices are filled with single or dual operational amplifiers in DIP-8 packages. It can be an easy, inexpensive upgrade for an older device to put in newer opamps, which feature lower distortion, less intrinsic noise, and lower DC-offset. Sometimes these newer amplifiers are only available in surface-mount packages, such as the Texas Instruments [OPA1641/1642](http://www.ti.com/product/opa1642).

[![Modded PCB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/1/jims.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/jims.jpg)

When doing modifications of this sort, there are a couple of things to be aware of.

- First, note whether the original equipment has the IC in a socket. If so, it should be easy to remove the old chip, and install the adapter.
- If there is no socket, and the old IC is soldered directly to the board, take care in removing the old IC, to prevent damaging the PCB. It might be easier to cut the legs off the old IC, and desolder them one-by-one.
- If there wasn\'t a socket, you might consider installing one as part of the upgrade.
- Finally, note the orientation of the IC before you begin, so you can be certain to get the replacement in properly.