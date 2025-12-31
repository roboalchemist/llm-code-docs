# Source: https://learn.sparkfun.com/tutorials/softpot-hookup-guide

## Introduction

Soft potentiometers are very thin and very unique [potentiometers](https://learn.sparkfun.com/tutorials/resistors/all#pot). Instead of a knob or physical slider, the softpot\'s wiper is any object \-- a finger, pen cap, stylus, etc \-- that can slide across its sensor membrane. Softpots can be used as position sensors in CNC machines, volume control sliders in custom stereos, throttles for drones, or in any project that requires linear movement sensing.

[![SoftPot Membrane Potentiometer - 50mm](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/4/1/08680-03-L.jpg)](https://www.sparkfun.com/softpot-membrane-potentiometer-50mm.html)

### [SoftPot Membrane Potentiometer - 50mm](https://www.sparkfun.com/softpot-membrane-potentiometer-50mm.html) 

[ SEN-08680 ]

These are very thin variable potentiometers. By pressing down on various parts of the strip, the resistance linearly changes ...

[ [\$8.95] ]

Like any potentiometer, the softpot is a three terminal device. The middle pin is the wiper, and the other two terminals are the high and low ends of the resistive element. By supplying the outer terminals with a power and ground connection, the middle terminal can be used to produce a variable voltage.

### Suggested Materials

This tutorial serves as a quick primer on soft potentiometers, and demonstrates how to hook them up and use them. In addition to the softpot, the following materials are recommended:

**[Arduino Uno](https://www.sparkfun.com/products/11021)** \-- We\'ll be using the Arduino\'s analog-to-digital converter to read in the variable voltage of the softpot. Any Arduino-compatible development platform \-- be it a [RedBoard](https://www.sparkfun.com/products/12757), [Pro](https://www.sparkfun.com/products/10914) or [Pro Mini](https://www.sparkfun.com/products/11113) \-- can substitute.

**[Breadboard](https://www.sparkfun.com/products/12002) and [Jumper Wires](https://www.sparkfun.com/products/11026)** \-- The soft pot three terminals are breadboard compatible. The breadboard is used as an intermediary device between sensor and jumper wires to the Arduino.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

**[Force Sensitive Resistor Adapter](https://www.sparkfun.com/categories/tags/amphenol-fci)** \-- While the FSR terminals are breadboard-compatible, we\'ve found that it may be loose in the breadboard. For those looking for a way to make a more secure connection without soldering, try looking at the associated Amphenol pin adapters. You will need a pair of [needle nose pliers](https://www.sparkfun.com/products/8793) to clamp the the adapter down.

[![Amphenol FCI Clincher Connector (2 Position, Female)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/3/3/14194-01.jpg)](https://www.sparkfun.com/amphenol-fci-clincher-connector-2-position-female.html)

### [Amphenol FCI Clincher Connector (2 Position, Female)](https://www.sparkfun.com/amphenol-fci-clincher-connector-2-position-female.html) 

[ COM-14194 ]

These Clincher connectors from Amphenol FCI can be used to terminate Flat Flexible Cables (FFCs) to an easy-to-use standard h...

[ [\$2.95] ]

[![Amphenol FCI Clincher Connector (2 Position, Male)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/3/4/14195-01.jpg)](https://www.sparkfun.com/amphenol-fci-clincher-connector-2-position-male.html)

### [Amphenol FCI Clincher Connector (2 Position, Male)](https://www.sparkfun.com/amphenol-fci-clincher-connector-2-position-male.html) 

[ COM-14195 ]

These Clincher connectors from Amphenol FCI can be used to terminate Flat Flexible Cables (FFCs) to an easy-to-use standard h...

[ [\$2.95] ]

[![Amphenol FCI Clincher Connector (3 Position, Female)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/3/5/14196-01.jpg)](https://www.sparkfun.com/amphenol-fci-clincher-connector-3-position-female.html)

### [Amphenol FCI Clincher Connector (3 Position, Female)](https://www.sparkfun.com/amphenol-fci-clincher-connector-3-position-female.html) 

[ COM-14196 ]

These Clincher connectors from Amphenol FCI can be used to terminate Flat Flexible Cables (FFCs) to an easy-to-use standard h...

[ [\$1.75] ]

[![Amphenol FCI Clincher Connector (3 Position, Male)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/3/6/14197-01.jpg)](https://www.sparkfun.com/amphenol-fci-clincher-connector-3-position-male.html)

### [Amphenol FCI Clincher Connector (3 Position, Male)](https://www.sparkfun.com/amphenol-fci-clincher-connector-3-position-male.html) 

[ COM-14197 ]

These Clincher connectors from Amphenol FCI can be used to terminate Flat Flexible Cables (FFCs) to an easy-to-use standard h...

[ [\$1.50] ]

### Suggested Reading

SoftPot\'s are a great entry-level component for beginners, but there are still a few basic electronics concepts you should be familiar with. If any of these tutorial titles sound foreign to you, consider skimming through that content first.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

## SoftPot Overview

Softpots come in a variety of sizes. The SparkFun catalog sports [50mm](https://www.sparkfun.com/products/8680), [200mm](https://www.sparkfun.com/products/8679), and [500mm](https://www.sparkfun.com/products/8681) long softpot strips. You can also find circular, arc-shaped, or other uniquely-shaped softpots in the market.

[![SoftPot Membrane Potentiometer - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/4/0/08679-03-L.jpg)](https://www.sparkfun.com/softpot-membrane-potentiometer-200mm.html)

### [SoftPot Membrane Potentiometer - 200mm](https://www.sparkfun.com/softpot-membrane-potentiometer-200mm.html) 

[ SEN-08679 ]

These are very thin variable potentiometers. By pressing down on various parts of the strip, the resistance linearly changes ...

[ [\$13.95] ]

[![SoftPot Membrane Potentiometer - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/4/1/08680-03-L.jpg)](https://www.sparkfun.com/softpot-membrane-potentiometer-50mm.html)

### [SoftPot Membrane Potentiometer - 50mm](https://www.sparkfun.com/softpot-membrane-potentiometer-50mm.html) 

[ SEN-08680 ]

These are very thin variable potentiometers. By pressing down on various parts of the strip, the resistance linearly changes ...

[ [\$8.95] ]

[![SoftPot Membrane Potentiometer - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/4/2/08681-03-L.jpg)](https://www.sparkfun.com/softpot-membrane-potentiometer-500mm.html)

### [SoftPot Membrane Potentiometer - 500mm](https://www.sparkfun.com/softpot-membrane-potentiometer-500mm.html) 

[ SEN-08681 ]

These are very thin variable potentiometers. By pressing down on various parts of the strip, the resistance linearly changes ...

[ [\$27.50] ]

The 50mm and 200mm softpot\'s feature a **10kΩ overall resistance** between the outer-two terminals, while the larger 500mm softpot measures in at **20kΩ**.

Placing your wiper at the base of the soft pot will effect a nearly 0Ω resistance between the middle pin and pin 1 (indicated by the arrow). When the wiper reaches the far end of the soft pot, the resistance will approach 10kΩ. And, if the wiper is in the middle, the resistance should be around 5kΩ.

[![Resistance along soft pot](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/4/resistance-diagram-3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/4/resistance-diagram-3.png)

The softpot is generally linear across the entire sensor area, so any math you\'ll do to determine a wiper\'s position should be relatively simple!

## Hardware Assembly

The sensors have solder tabs that are stapled through a flexible substrate to make contact with the semi-conductive material. Depending on your project application and skill set, there are a few methods of connecting to the sensor. Some assembly may be required to connect to the pins reliably.

[![Solder Tabs on Force Sensitive Resistor](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Solder-Tab-Crimped-Force-Sensitive-Resistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Solder-Tab-Crimped-Force-Sensitive-Resistor.jpg)

### Breadboard Compatible Tabs

For prototyping and testing, these solder tabs can be inserted into a breadboard or female jumper wires. Here are two examples with the flex and soft potentiometer sensors.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Flex Sensor Inserted Vertically on Breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_09_01.jpg)](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-9-using-a-flex-sensor)   [![SoftPot Inserted Vertically on Breadboard Flush Against the Table](https://cdn.sparkfun.com/r/900-900/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-04.jpg)](https://learn.sparkfun.com/tutorials/sik-keyboard-instrument)
  *Flex Sensor Inserted Vertically on Breadboard with Space to Bend*                                                                                                                                                                                             *SoftPot Inserted Vertically on Breadboard Flush Against the Table*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Tip:** You can also use the **2.54mm pitch screw terminal** to connect the sensors on a breadboard. However, using two screw terminals side by side for sensors with three solder tabs can make it a tight fit due to the housing. Additionally, they were meant to be soldered into a PCB and the screw terminals may not sit securely in a breadboard socket like a square header pin. **IC hooks** are another option but are only meant as a temporary connection. Any small bumps can cause the IC hook to become loose and disconnect. Using the IC hooks with the sensor for long term projects may not be most secure. [**Alligator clips** can also be used to connect](https://learn.sparkfun.com/tutorials/using-the-sparkfun-picoboard-and-scratch#fsr) to the solder tabs. However, alligator clip\'s teeth can damage the flexible substrate or cause shorts due to the three solder tabs being close to each other.\
\

[![Alligator Clip with Pigtail (4 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/3/2/6/13191-01.jpg)](https://www.sparkfun.com/alligator-clip-with-pigtail-4-pack.html)

### [Alligator Clip with Pigtail (4 Pack)](https://www.sparkfun.com/alligator-clip-with-pigtail-4-pack.html) 

[ CAB-13191 ]

This is a 4 pack of wires that are pre-terminated with an alligator clip on one end and a hookup pigtail on the other. Alliga...

[ [\$4.75] ]

[![IC Hook with Pigtail](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/9/6/09741-01.jpg)](https://www.sparkfun.com/ic-hook-with-pigtail.html)

### [IC Hook with Pigtail](https://www.sparkfun.com/ic-hook-with-pigtail.html) 

[ CAB-09741 ]

These are good quality IC test hooks with a male connection wire. Instead of a single hook, these have two hooks that are cap...

[ [\$5.75] ]

[![Screw Terminals 2.54mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/2/0/4/10571-01.jpg)](https://www.sparkfun.com/screw-terminals-2-54mm-pitch-2-pin.html)

### [Screw Terminals 2.54mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-2-54mm-pitch-2-pin.html) 

[ PRT-10571 ]

These are simple 2-position screw terminals with 2.54mm pitch pins. Rated up to 150V @ 6A, this terminal can accept 30 to 18A...

[ [\$0.95] ]

### Soldering to Tabs

**Warning!** The flexible substrate and semi-conductive material are sensitive to heat. The force sensitive resistors from Interlink are more sensitive compared to other flexible sensors. There is a risk of damaging the sensor when soldering to the solder tabs. We only recommend this for **advanced users** that have adjusted their soldering iron for lower temperatures.

When integrating it into a long term project and installation, there is an option to solder wires or a PCB directly to the solder tabs. However, excessive heat can melt the material and damage the sensor due to the limitations in the flexible substrate and the semi-conductive material. Below is an example of the flex sensor soldered to a PCB from our production assembly technicians.

[![Flex Sensor Soldered on PCB for Qwiic Flex Glove Controller](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/14666-SparkFun_Qwiic_Flex_Glove_Controller-Solder-Tabs-Soldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/14666-SparkFun_Qwiic_Flex_Glove_Controller-Solder-Tabs-Soldered.jpg)

While you can solder to the SofPot\'s solder tabs, we only recommended for **advanced users** that have experience with soldering. For those soldering to the SoftPot , you would need to solder at a lower temperature and ensure that the soldering iron is not heating the tab for no more than 1 second. Any longer and you can damage the material and semi-conductive material. The force sensitive resistor in particular is more susceptible to damage compared to the flex sensors and SoftPot.

**Tip:** For advanced users that are interested in the challenge, try checking out the following forum post and instructions from Digi-Key. While they use a force sensitive resistor, the steps to solder to a flex sensor\'s solder tabs are the same.\
\

- [Digi-Key Forums: How to solder Interlink Electronics FSR sensor](https://forum.digikey.com/t/how-to-solder-interlink-electronics-fsr-sensor/555)
- [How to Solder Wire to FSR Sensors](https://media.digikey.com/pdf/Data%20Sheets/Interlink%20Electronics.PDF/FSR400_Soldering_Instr.pdf)

### Amphenol CFI Clincher Connector

As an alternative, users can use the Amphenol FCI Clincher connector to make a reliable connection to the sensor and provide a small amount of strain relief on the crimped connector. This is recommended for those that have not soldered before and are using the sensors in an long term projects beyond the breadboard or in a classroom setting. The connector was designed to crimp pins on flexible printed circuits as an alternative to applying heat to heat sensitive components such as the semi-conductive material or conductive ink.

[![Clincher connector on the Force Sensitive Resistor, Flex Sensor, and SoftPot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Flex_Force_Sensitive_SoftPot_Sensor_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Flex_Force_Sensitive_SoftPot_Sensor_Clincher_Connector.jpg)

##### Crimping the Clincher Connector

We\'ll be using the male Clincher connector to crimp down on the flex sensor. However, the instructions listed below can be applied to any two or three pin flexible sensor as well.

To connect, you will need to cut off the solder tabs on the sensor. Make sure to cut as close to the solder tabs as possible. You can have issues connecting to the semi-conductive material if you cut off too much of the sensor. The length of the semi-conductive pads on the SoftPot is smaller than the force sensitive resistor and flex sensor.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Cutting Solder Tabs Off Flex Sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Cut_Solder-Tabs_Flex_Sensor_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Cut_Solder-Tabs_Flex_Sensor_Clincher_Connector.jpg)   [![Cutting Solder Tabs Off Slide Pot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Cut_Solder-Tabs_Slide_Pot_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Cut_Solder-Tabs_Slide_Pot_Clincher_Connector.jpg)
  *Cutting Solder Tabs Off Flex Sensor*                                                                                                                                                                                                                                    *Cutting Solder Tabs Off Slide Pot*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After cutting the staples off, insert the sensor in the respective Clincher connector. Make sure to align the semi-conductive material with the new staples or you may create a short. Depending on the sensor, you may have less semi-conductive material to work with. The SoftPot will have smaller pads to work with after cutting the solder tabs off as shown on the image to the right.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Inserting the Flex Sensor into the 2-Pin Clincher Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Insert_Flex_Sensor_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Insert_Flex_Sensor_Clincher_Connector.jpg)   [![Inserting the SoftPot Sensor into the 3-Pin Clincher Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Insert_Slide_Pot_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Insert_Slide_Pot_Clincher_Connector.jpg)
  *Inserting the Flex Sensor into the 2-Pin Clincher Connector*                                                                                                                                                                                                                  *Inserting the SoftPot Sensor into the 3-Pin Clincher Connector*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once you have aligned the sensor, we recommend adding a piece of tape to hold down the sensor with the Clincher connector to prevent the sensor from moving around when clamping the connector down.

[![Flex Sensor Held Against Clincher Connector with Tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Tape_Flex_Sensor_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Tape_Flex_Sensor_Clincher_Connector.jpg)

We recommend using a flush, slip joint plier to clamp the connector down. As you can see from the image, the force is being applied on the center of the latch and staples instead of along the grooves on the side of the connector. The force sensitive resistor will be easier to clamp down compared to the other flexible substrates on the flex sensor and SoftPot. You will hear a small but satisfying pop when the crimp pins bite through the sensor.

[![Flush Slip Joint Pliers Used to Apply Uniform Force Against Tab in the Middle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Flush_Narrow_Slip_Joint_Plier_Flex_Sensor_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Flush_Narrow_Slip_Joint_Plier_Flex_Sensor_Clincher_Connector.jpg)

Otherwise, needle nose pliers can be used to clamp the staples to the sensor. Close the tab to hold the crimp pins against the semi-conductive material. Then make sure to carefully apply force on the center from each corner (while avoiding the grooves on the side).

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Hold_Down_Clincher_Connector.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Plier_Flex_Sensor_Clincher_Connector_1.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Plier_Flex_Sensor_Clincher_Connector_2.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Plier_Flex_Sensor_Clincher_Connector_3.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Plier_Flex_Sensor_Clincher_Connector_4.jpg)

[[]](#carousel-6954f8265420d) [[]](#carousel-6954f8265420d)

1.  ::: 
    :::

2.  ::: 
    :::

3.  ::: 
    :::

4.  ::: 
    :::

5.  ::: 
    :::

If you apply force incorrectly with needle nose pliers, there is a risk of damaging the plastic housing. The image on the right shows the Clincher connector housing damaged even though the crimp pins are making contact with the SoftPot.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Pliers applied incorrectly to the Clincher connector.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Incorrect_Use_Pliers_Clincher_Connector_Housing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Incorrect_Use_Pliers_Clincher_Connector_Housing.jpg)   [![Clincher connector\'s housing damaged for the SoftPot.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Damaged_Clincher_Connector_Housing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Damaged_Clincher_Connector_Housing.jpg)
  *Pliers applied incorrectly to the Clincher connector.*                                                                                                                                                                                                                                      *Clincher connector\'s housing damaged for the SoftPot.*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Tip:** If you have issues pushing down on the tab to crimp the pins simultaneously, you can individually crimp the pins with needle nose pliers. Just make sure to be careful so that the grooves are not damaged. Here\'s an example from Provancher.\
\

[Flex-circuit Soldering & Assembly Tutorial and Notes](https://my.mech.utah.edu/~wil/tutorials/flexCirc_soldering_tutorial/Flex_circuit_Soldering_Tutorial.html)

When finished, remove the tape from the back. To test, you can [use a multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/) to determine if the sensor has a short or is able change in resistance. You can also connect the sensor to your circuit using jumper wires to check if the sensor is working as expected.

[![Clincher connector on the Force Sensitive Resistor, Flex Sensor, and SoftPot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Flex_Force_Sensitive_SoftPot_Sensor_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Flex_Force_Sensitive_SoftPot_Sensor_Clincher_Connector.jpg)

## Example Circuit

By supplying a voltage to the outer pins of the SoftPot, we can generate a variable voltage on the middle wiper pin. Here\'s an example hookup:

[![Fritzing example circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/4/example_circuit_bb-pulldown.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/4/example_circuit_bb-pulldown.png)

A 10kΩ resistor between the wiper and ground pulls the SoftPot\'s analog output signal down. This ensures that the sensor\'s output value doesn\'t \"float\" \-- a term we use when the voltage of a signal is bouncing around with no real certainty.

By connecting pin 1 to ground and pin 3 to 5V, we cause the voltage on the middle pin to rise from 0V to 5V as the wiper moves from the bottom of the softpot (towards the terminals) to the top. Reversing the power supply can swap that relationship around.

## Example Code

Here is a simple Arduino example based on the circuit above. Copy and paste this into your Arduino IDE, then upload!

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /******************************************************************************
    SoftPot_Example.ino
    Example sketch for SparkFun's soft membrane potentiometer
      (https://www.sparkfun.com/products/8680)
    Jim Lindblom @ SparkFun Electronics
    April 28, 2016

    - Connect the softpot's outside pins to 5V and GND (the outer pin with an arrow
    indicator should be connected to GND). 
    - Connect the middle pin to A0.

    As the voltage output of the softpot changes, a line graph printed to the
    serial monitor should match the wiper's position.

    Development environment specifics:
    Arduino 1.6.7
    ******************************************************************************/
    const int SOFT_POT_PIN = A0; // Pin connected to softpot wiper

    const int GRAPH_LENGTH = 40; // Length of line graph

    void setup() 
    

    void loop() 
    
      Serial.println("> (" + String(softPotADC) + ")");

      delay(500);
    }

After uploading, **open your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux)**, and set the baud rate to 9600 bps.

Then actuate the softpot by sliding a finger, pencil eraser, tool grip, or anything slide-able across the sensing area of the potentiometer.

[![Softpot slider in action](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/4/softpot-action.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/4/softpot-action.jpg)

A series of line graphs should begin flowing by in the serial monitor.

[![Serial monitor example](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/4/softpot-serial-monitor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/4/softpot-serial-monitor.png)

The raw ADC reading is also printed out after each reading. Take that, and start building sliding control systems of your own!