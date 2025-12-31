# Source: https://learn.sparkfun.com/tutorials/modifying-your-el-wire-inverter

## Introduction

In this tutorial, we will modify the [12V EL wire inverter](https://www.sparkfun.com/products/10469) to power the EL Sequencer or EL Escudo Dos off a single power supply.

[![Soldering different Cable to 12V EL Inverter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/EL-Wire-Inverter-Hack-Cable-Soldering.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/EL-Wire-Inverter-Hack-Cable-Soldering.jpg)

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Heads up!** Depending on your setup, you could also use a 9v battery with adapter for remote applications.\
\

[![9V to Barrel Jack Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/6/2/09518-01.jpg)](https://www.sparkfun.com/9v-to-barrel-jack-adapter.html)

### [9V to Barrel Jack Adapter](https://www.sparkfun.com/9v-to-barrel-jack-adapter.html) 

[ PRT-09518 ]

This simple cable has so many uses! Plug the 9 volt battery clip onto a standard 9V battery and connect the other end to anyt...

[ [\$3.60] ]

[![9V Alkaline Battery](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/6/2/10218-01.jpg)](https://www.sparkfun.com/9v-alkaline-battery.html)

### [9V Alkaline Battery](https://www.sparkfun.com/9v-alkaline-battery.html) 

[ PRT-10218 ]

These are your standard 9 Volt alkaline batteries from Rayovac. Don\'t even think about trying to recharge these. Use them wit...

[ [\$2.40] ]

#### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49). You will also need a screwdriver and multimeter for testing.

[![Digital Multimeter - Basic](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/0/7/12966-01.jpg)](https://www.sparkfun.com/digital-multimeter-basic.html)

### [Digital Multimeter - Basic](https://www.sparkfun.com/digital-multimeter-basic.html) 

[ TOL-12966 ]

The digital multimeter (DMM) is an essential tool in every electronic enthusiasts arsenal. The SparkFun Digital Multimeter, h...

[ [\$21.50] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/getting-started-with-electroluminescent-el-wire)

### Getting Started with Electroluminescent (EL) Wire 

This guide will help you get started with electroluminescent (EL) wire, tape, panel, chasing wire, and bendable wire to let your project glow!

[](https://learn.sparkfun.com/tutorials/el-sequencerescudo-dos-hookup-guide)

### EL Sequencer/Escudo Dos Hookup Guide 

A basic guide to getting started with the SparkFun EL Sequencer and Escudo Dos to control electroluminescence (EL) wire, panels, and strips.

## Hacking Your EL Wire Inverter\'s Input

By default, the DC input on the 12V inverter has a connector that accepts a barrel jack connector. This is usually a great feature but we\'d rather have that input be a JST connector so we can hook it directly to the EL Sequencer/EL Escudo Dos off a single power supply. Don\'t worry, we can easily hack one in. Remove the QC sticker on the back of the 12V EL inverter. Using a Phillips screwdriver, open the inverter\'s enclosure.

[![12V Inverter and Screwdriver](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/Opening-12V-EL-Wire-Inverter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/Opening-12V-EL-Wire-Inverter.jpg)

Remove the screw and open the case. The PCB will look different depending on when you ordered the 12V inverter. The inverter on the left is from an older model as opposed to the one on the right. Regardless of how the PCBs look, they will still function the same.

[![Different 12V Inverter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/Different-12V-EL-Inverter-PCB-Backside.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/Different-12V-EL-Inverter-PCB-Backside.jpg)

Remove the board from the enclosure so that we can remove the existing wires connected to the barrel jack connector. The wires with the black sheath will be the ones that we will be [desoldering](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering). On newer 12V inverters, there should be some hot glue between the wires and PCB. This is for strain relief. If there is hot glue, carefully separate it from the cable and components on the 12V inverter. Desolder the wires connected by heating the pin or PTH pad. If necessary, give the PTH pad a [small bump on the table with the slap method](https://www.sparkfun.com/tutorials/339) to remove any solder before threading new wire through it. If the diode\'s pin is already soldered on the PTH pad, the wire would need to be soldered to the joint. Feel free to keep the wires connected to the barrel jack in your parts bin for a different project.

[![Desolder Wires from the DC Input](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/EL-Wire-Inverter-Hack-Cable-Soldering.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/EL-Wire-Inverter-Hack-Cable-Soldering.jpg)

Take note of what color wire is connected to the PTH and which side the wires were removed. The PCB may be different depending on when it was manufactured so there may not be any silkscreen indicating the input voltage for \"**+**\" and \"**-**\". The images in the center and far right did not have any silkscreen associated with the wiring. Usually the \"**+**\" is connected to the anode of the diode. In this case, we desoldered the wires from the PCB as shown in sample 3.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Inverter Sample 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/Different-12V-EL-Inverter_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/Different-12V-EL-Inverter_1.jpg)   [![Inverter Sample 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/Different-12V-EL-Inverter_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/Different-12V-EL-Inverter_2.jpg)   [![Inverter Sample 3](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/Different-12V-EL-Inverter_3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/Different-12V-EL-Inverter_3.jpg)
  *Sample 1*                                                                                                                                                                                                       *Sample 2*                                                                                                                                                                                                       *Sample 3*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Having a hard time viewing the images? Click on image for a closer view.*

Solder the new JST pigtail to the board. We\'ll be adding the wires to the bottom of the PCB. To be consistent with the wire colors for the input voltage, we will be connecting the red wire to the pad or pin that is connected to the diode\'s anode pin. Then we will be connecting the black wire to the other pad or pin that was desoldered.

[![Solder New Wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/EL-Wire-Inverter-Hack-Cable-Soldering.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/EL-Wire-Inverter-Hack-Cable-Soldering.jpg)

**Note:** This step is entirely optional. Add hot glue to secure the connection between the board and new pigtail similar to how the original wires were attached to the board. Just make sure to not add too much hot glue as it may cause problems when the PCB is placed back into its enclosure.\
\
[![Adding Hot Glue to Joint for Strain Relief](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/Hot-Glue-Wire-Strain-Relief-Electronics.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/Hot-Glue-Wire-Strain-Relief-Electronics.jpg)

Insert the board back into its respective enclosure while ensuring that the wires are between the openings. Re-insert the screw and tighten. Since the wire colors are the same, try labeling the EL inverter with a marker or tape to indicate the side that is the DC input and AC output. Usually the input voltage is closest to the switch.

[![Labeled Input and OUtput ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/0/12V-EL-Wire-Inverter-Labeled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/0/12V-EL-Wire-Inverter-Labeled.jpg)

Before powering up, insert jumper wire between your power adapter and DC input similar to how [EL wire was tested in the Getting Started Guide](https://learn.sparkfun.com/tutorials/getting-started-with-electroluminescent-el-wire#hardware-hookup---el). Since we are using the JST pigtail assembly, you will need to remove the mating connector for the JST. Add extra part to your parts bin for future projects! Keep in mind that the DC input has a polarity so VIN should be connected to the red wire and GND to black the wire. Then insert jumper wires between the AC output and EL Wire. If you need, feel free to add some electrical tape as a precaution when handling the AC output.

*[![Jumper Wire in JST Connector For Testing](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/5/Electroluminescent_EL_Wire_Electrical_Tape_Insulation.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/5/Electroluminescent_EL_Wire_Electrical_Tape_Insulation.jpg)*

Insert the wall adapter to an outlet (or add a 9V battery if you are using this in a remote setup) to the connection to test. Using the wires connecting to the DC input, touch the red wire to the center tip of the barrel jack and the black wire to the sleeve of the wall adapter. Flip the switch if you do not see the EL powering up. The EL wire should blink or stay on depending on the mode that is used.

[![EL Wire Powered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/5/10197-Action_EL_Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/5/10197-Action_EL_Wire.jpg)

**Note:** If you prefer, you could use a DC barrel jack adapter to provide a more secure connection to your power supply for testing as opposed to holding the power pins down against the barrel jack\'s center tip and sleeve.\
\

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

------------------------------------------------------------------------

Now that we have modified the EL Inverter, the next step is to use it with the EL Sequencer or EL Escudo Dos! Plug the DC input you just made into the \"DC TO INVERTER\" connector, plug the AC output into the \"AC FROM INVERTER\" connector, and we\'re ready to fire things up! For more information, check out the guide below to adjust the solder jumper on the board before connecting.

[](https://learn.sparkfun.com/tutorials/el-sequencerescudo-dos-hookup-guide)

### EL Sequencer/Escudo Dos Hookup Guide 

December 3, 2015

A basic guide to getting started with the SparkFun EL Sequencer and Escudo Dos to control electroluminescence (EL) wire, panels, and strips.