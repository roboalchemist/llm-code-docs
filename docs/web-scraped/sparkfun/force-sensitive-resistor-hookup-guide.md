# Source: https://learn.sparkfun.com/tutorials/force-sensitive-resistor-hookup-guide

## Introduction

Force-sensitive resistor\'s (FSR) are easy-to-use sensors designed for measuring the presence and relative magnitude of localized physical pressure.

[![Force Sensitive Resistor 0.5\"](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/6/7/09375-1.jpg)](https://www.sparkfun.com/force-sensitive-resistor-0-5.html)

### [Force Sensitive Resistor 0.5\"](https://www.sparkfun.com/force-sensitive-resistor-0-5.html) 

[ SEN-09375 ]

This is a force sensitive resistor with a round, 0.5\" diameter, sensing area.

[ [\$10.95] ]

[![Force Sensitive Resistor - Square](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/6/8/09376-1.jpg)](https://www.sparkfun.com/force-sensitive-resistor-square.html)

### [Force Sensitive Resistor - Square](https://www.sparkfun.com/force-sensitive-resistor-square.html) 

[ SEN-09376 ]

This is a force sensitive resistor with a square, 1.75x1.5\", sensing area.

[ [\$17.50] ]

[![Force Sensitive Resistor - Small](https://cdn.sparkfun.com/r/140-140/assets/parts/3/5/3/7/09673-01.jpg)](https://www.sparkfun.com/force-sensitive-resistor-small.html)

### [Force Sensitive Resistor - Small](https://www.sparkfun.com/force-sensitive-resistor-small.html) 

[ SEN-09673 ]

This is a small force sensitive resistor. It has a 0.16\" (4 mm) diameter active sensing area.

[ [\$10.95] ]

[![Force Sensitive Resistor - Long](https://cdn.sparkfun.com/r/140-140/assets/parts/3/5/3/8/09674-01.jpg)](https://www.sparkfun.com/force-sensitive-resistor-long.html)

### [Force Sensitive Resistor - Long](https://www.sparkfun.com/force-sensitive-resistor-long.html) 

[ SEN-09674 ]

This very long force sensitive resistor - over 2 feet - has a sensing area of 0.25x24\".

[ [\$30.95] ]

[![FlexiForce Pressure Sensor - 25lbs (1\" area)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/7/8/1/11207-01.jpg)](https://www.sparkfun.com/flexiforce-pressure-sensor-25lbs-1-area.html)

### [FlexiForce Pressure Sensor - 25lbs (1\" area)](https://www.sparkfun.com/flexiforce-pressure-sensor-25lbs-1-area.html) 

[ SEN-11207 ]

This is a \[piezoresistive\](http://www.google.com/url?sa=t&ct=res&cd=1&url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPiezoresisto...

[ [\$27.95] ]

[![FlexiForce Pressure Sensor - 100lbs.](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/4/6/08685-03-L.jpg)](https://www.sparkfun.com/flexiforce-pressure-sensor-100lbs.html)

### [FlexiForce Pressure Sensor - 100lbs.](https://www.sparkfun.com/flexiforce-pressure-sensor-100lbs.html) 

[ SEN-08685 ]

This is a \[piezoresistive\](http://www.google.com/url?sa=t&ct=res&cd=1&url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPiezoresisto...

[ [\$22.95] ]

[![FlexiForce Pressure Sensor - 1lb.](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/9/3/08685-03-L.jpg)](https://www.sparkfun.com/flexiforce-pressure-sensor-1lb.html)

### [FlexiForce Pressure Sensor - 1lb.](https://www.sparkfun.com/flexiforce-pressure-sensor-1lb.html) 

[ SEN-08713 ]

This is a \[piezoresistive\](http://www.google.com/url?sa=t&ct=res&cd=1&url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPiezoresisto...

[ [\$22.95] ]

[![FlexiForce Pressure Sensor - 25lbs.](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/9/2/08685-03-L.jpg)](https://www.sparkfun.com/flexiforce-pressure-sensor-25lbs.html)

### [FlexiForce Pressure Sensor - 25lbs.](https://www.sparkfun.com/flexiforce-pressure-sensor-25lbs.html) 

[ SEN-08712 ]

This is a \[piezoresistive\](http://www.google.com/url?sa=t&ct=res&cd=1&url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPiezoresisto...

[ [\$24.95] ]

The resistance of an FSR varies as the force on the sensor increases or decreases. When no pressure is being applied to the FSR, its resistance will be larger than 1MΩ. The harder you press on the sensor's head, the lower the resistance between the two terminals drops. By combining the FSR with a static resistor to create a [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers), you can produce a variable voltage that can be read by a microcontroller\'s analog-to-digital converter.

### Suggested Materials

This tutorial serves as a quick primer on FSR\'s and demonstrates how to hook them up and use them. Beyond a FSR of your choice, the following materials are recommended:

**[Arduino Uno](https://www.sparkfun.com/products/11021)** \-- We\'ll be using the Arduino\'s analog-to-digital converter to read in the variable resistance of the FSR. Any Arduino-compatible development platform \-- be it a [RedBoard](https://www.sparkfun.com/products/12757), [Pro](https://www.sparkfun.com/products/10914) or [Pro Mini](https://www.sparkfun.com/products/11113) \-- can substitute.

**[Resistor Kit](https://www.sparkfun.com/products/10969)** \-- To turn the FSR\'s variable resistance into a readable voltage, we\'ll combine it with a static resistor to create a voltage divider. This resistor kit is handy for some trial-and-error testing to hone in on the most sensitive circuit possible.

**[Breadboard](https://www.sparkfun.com/products/12002) and [Jumper Wires](https://www.sparkfun.com/products/11026)** \-- The FSR\'s terminals are breadboard-compatible. We\'ll stick in that and the resistor, then use the jumper wires to connect from breadboard to Arduino.

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

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

Analog components, like these FSRs, are a great sensor-reading entry-point for beginners, but there are a few electronics concepts you should be familiar with. If any of these tutorial titles sound foreign to you, consider skimming through that content first.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/voltage-dividers)

### Voltage Dividers 

Turn a large voltage into a smaller one with voltage dividers. This tutorial covers: what a voltage divider circuit looks like and how it is used in the real world.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

## FSR Overview

There are a variety of FSR options out there, and a few key characteristics to differentiate them: **size, shape, and sensing range**. Here\'s a quick overview of the sensors available from Interlink and Tekscan in our catalog. The sensors from Tekscan are much more stable, calibrated to a specific weight, and provide a much larger range.

  ------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                           Shape          Sensing Area        Min Pressure   Max Pressure
  ------------------------------------------------------------------------------ -------------- ------------------- -------------- ---------------
  ![](https://cdn.sparkfun.com/r/140-140/assets/parts/3/5/3/7/09673-01.jpg)\     Circular       7.62 mm dia\        0.1 kg\        1 kg\
  **Force Sensitive Resistor - Small\                                                           (0.3 in)            (0.22 lb)      (2.2 lb)
  (SEN-09673)**                                                                                                                    

  ![](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/6/7/09375-1.jpg)\      Circular       12.7 mm dia\        100 g\         10 kg\
  **Force Sensitive Resistor 0.5\"\                                                             (0.5 in)            (0.22 lb)      (22.04 lb)
  (SEN-09375)**                                                                                                                    

  ![](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/6/8/09376-1.jpg)\      Square         44.45 x 44.45 mm\   100 g\         10 kg\
  **Force Sensitive Resistor - Square\                                                          (1.75 x 1.75 in)\   (0.22 lb)      (22.04 lb)
  (SEN-09376)**                                                                                                                    

  ![](https://cdn.sparkfun.com/r/140-140/assets/parts/3/5/3/8/09674-01.jpg)\     Rectangular    6.35 x 609.6 mm\    100 g\         10 kg\
  **Force Sensitive Resistor - Long\                                                            (0.25 x 24.0 in)    (0.22 lb)      (22.04 lb)
  (SEN-09674)**                                                                                                                    

  ![](https://cdn.sparkfun.com/r/140-140/assets/parts/6/7/8/1/11207-03.jpg)\     Circular       2.54mm dia\         0 g\           \~11.34 kg\
  **FlexiForce Pressure Sensor - 25lbs (1\" area)\                                              (0.1 in)            (0 lb)         (25 lb)
  (SEN-11207)**                                                                                                                    

  ![](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/9/3/08685-03-L.jpg)\   Circular       9.53 mm dia\        0 g\           \~0.45 kg\
  **FlexiForce Pressure Sensor - 1lb.\                                                          (0.375 in)          (0 lb)         (1 lb)
  (SEN-08713)**                                                                                                                    

  ![](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/9/2/08685-03-L.jpg)\   Circular       9.53 mm dia\        0 g\           \~11.3398 kg\
  **FlexiForce Pressure Sensor - 25lbs.\                                                        (0.375 in)          (0 lb)         (25 lb)
  (SEN-08712)**                                                                                                                    

  ![](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/4/6/08685-03-L.jpg)\   Circular       9.53 mm dia\        0 g\           \~45.36 kg\
  **FlexiForce Pressure Sensor - 100lbs.\                                                       (0.375 in)          (0 lb)         (100 lb)
  (SEN-08685)**                                                                                                                    
  ------------------------------------------------------------------------------------------------------------------------------------------------

### Shape and Size

Most FSR\'s feature either a circular or rectangular sensing area. The square FSR is good for broad-area sensing, while the smaller circular sensors can provide more precision to the location being sensed.

The rectangular FSR\'s from Interlink include a small-ish [square 1.75 x 1.75\" sensor](https://www.sparkfun.com/products/9376) and a [long 0.25 x 24\" strip](https://www.sparkfun.com/products/9674). The rest of the sensors feature a circular sensing area.

### Sensing Range

Another key characteristic of the FSR is it\'s rated sensing range, which defines the minimum and maximum amounts of pressure that the sensor can differentiate between.

The lower the force rating, the more **sensitive** your FSR hookup has the potential to be. But! Any pressure beyond the sensor\'s maximum limit will be unmeasurable (and may damage the component). The [small 1kg-rated FSR](https://www.sparkfun.com/products/9673) will provide more sensitive readings from 0 to 1kg, but won\'t be able to tell the difference between a 2kg and 10kg weight.

### Force vs. Resistance

The graph below, figure 2 from the [Interlink FSR Integration Guide](https://www.sparkfun.com/datasheets/Sensors/Pressure/fsrguide.pdf), demonstrates the typical force-resistance relationship:

[![FSR force vs resistance](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/fsr-resistance-graph.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/fsr-resistance-graph.png)

The relationship is generally linear from 50g and up, but note what the relationship does below 50g, and even more-so below 20g. These sensor\'s have a **turn-on threshold** \-- a force that must be present before the resistance drops to a value below 10kΩ, where the relationship becomes more linear.

**FSR vs Load Cells:** These sensors are simple to set up and great for sensing pressure, but they aren't incredibly accurate. They're useful for sensing the presence of something, and the relative magnitude of that force, but they're not all that great at measuring weight (that's what [load cell's](https://www.sparkfun.com/products/10245) are for!).\
\

[](https://learn.sparkfun.com/tutorials/getting-started-with-load-cells)

### Getting Started with Load Cells 

June 11, 2015

A tutorial defining what a load cell is and how to use one.

## Hardware Assembly

The sensors have solder tabs that are stapled through a flexible substrate to make contact with the semi-conductive material. Depending on your project application and skill set, there are a few methods of connecting to the sensor. Some assembly may be required to connect to the pins reliably.

[![Solder Tabs on Force Sensitive Resistor](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Solder-Tab-Crimped-Force-Sensitive-Resistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Solder-Tab-Crimped-Force-Sensitive-Resistor.jpg)

### Breadboard Compatible Tabs

For prototyping and testing, these solder tabs can be inserted into a breadboard or female jumper wires. Here are two examples with the flex and soft potentiometer sensors.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Flex Sensor Inserted Vertically on Breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_09_01.jpg)](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-9-using-a-flex-sensor)   [![SoftPot Inserted Vertically on Breadboard Flush Against the Table](https://cdn.sparkfun.com/r/900-900/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-04.jpg)](https://learn.sparkfun.com/tutorials/sik-keyboard-instrument)
  *Flex Sensor Inserted Vertically on Breadboard with Space to Bend*                                                                                                                                                                                             *SoftPot Inserted Vertically on Breadboard Flush Against the Table*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Tip:** You can also use the **2.54mm pitch screw terminal** to connect the sensors on a breadboard. However, using two screw terminals side by side for sensors with three solder tabs can make it a tight fit due to the housing. Additionally, they were meant to be soldered into a PCB and the screw terminals may not sit securely in a breadboard socket like a square header pin. **IC hooks** are another option but are only meant as a temporary connection. Any small bumps can cause the IC hook to become loose and disconnect. Using the IC hooks with the sensor for long term projects may not be most secure. [**Alligator clips** can also be used to connect](https://learn.sparkfun.com/tutorials/using-the-sparkfun-picoboard-and-scratch#fsr) to the solder tabs. However, alligator clip\'s teeth can damage the flexible substrate or cause shorts due to the solder tabs being close to each other.\
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

While the [datasheet](https://www.sparkfun.com/datasheets/Sensors/Pressure/fsrguide.pdf) states that you can solder to the force sensitive resistor\'s solder tabs, we only recommended for **advanced users** that have experience with soldering. For those soldering to the force sensitive resistor, you would need to solder at a lower temperature and ensure that the soldering iron is not heating the tab for no more than 1 second. Any longer and you can damage the material and semi-conductive material. The force sensitive resistor in particular is more susceptible to damage compared to the flex sensors and SoftPot.

**Tip:** For advanced users that are interested in the challenge, try checking out the following forum post and instructions from Digi-Key:\
\

- [Digi-Key Forums: How to solder Interlink Electronics FSR sensor](https://forum.digikey.com/t/how-to-solder-interlink-electronics-fsr-sensor/555)
- [How to Solder Wire to FSR Sensors](https://media.digikey.com/pdf/Data%20Sheets/Interlink%20Electronics.PDF/FSR400_Soldering_Instr.pdf)

### Amphenol CFI Clincher Connector

As an alternative, users can use the Amphenol FCI Clincher connector to make a reliable connection to the sensor and provide a small amount of strain relief on the crimped connector. This is recommended for those that have not soldered before and are using the sensors in an long term projects beyond the breadboard or in a classroom setting. The connector was designed to crimp pins on flexible printed circuits as an alternative to applying heat to heat sensitive components such as the semi-conductive material or conductive ink.

[![Clincher connector on the Force Sensitive Resistor, Flex Sensor, and SoftPot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Flex_Force_Sensitive_SoftPot_Sensor_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Flex_Force_Sensitive_SoftPot_Sensor_Clincher_Connector.jpg)

##### Crimping the Clincher Connector

We\'ll be using the male Clincher connector to crimp down on the flex sensor. However, the instructions listed below can be applied to the force sensitive resistor as well.

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

[[]](#carousel-6954f6348da66) [[]](#carousel-6954f6348da66)

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

## Example Hardware Hookup

By creating a [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers) with the FSR and another resistor, you can create a variable voltage output, which can be read by a microcontroller's ADC input.

### Selecting a Static Resistor

The tricky part of voltage-dividing an FSR is selecting a static resistor value to pair with it. You don\'t want to overpower the maximum resistance of the FSR, but you also don\'t want the FSR\'s minimum resistance to be completely overshadowed either.

It helps to know what range of force you\'ll be reading. If your project\'s force-sensing covers the broad range of the FSR (e.g. 0.1-10kg), try to pick a static resistance in the middle-range of the FSR\'s resistive output \-- something in the middle of 200-6kΩ. 3kΩ, or a common resistor like **3.3kΩ**, is a good place to start.

**Short on Resistors?** If all you have is 10kΩ resistors (looking at you [Sensor Kit visitors](https://www.sparkfun.com/products/13754)), you can still make something close to 3k! Try putting **three 10kΩ\'s in [parallel](https://learn.sparkfun.com/tutorials/resistors#series-and-parallel-resistors)** to create a 3.33kΩ monster resistor. Or put three 330Ω resistors in **series** to create a 990Ω concoction, which will work pretty well too.

### Example Circuit

**Warning:** As stated on page 10 of the [Interlink FSR Integration Guide](https://www.sparkfun.com/datasheets/Sensors/Pressure/fsrguide.pdf), the FSR\'s flexible substrate is sensitive to heat. It is not recommended to solder directly to the exposed silver traces or apply high temperatures to the clamped pins for long periods of time. For users that do not have that much experience soldering, try using ZIF sockets or clamping the sensor with a [Force Sensitive Resistor Pin Adapter](https://www.sparkfun.com/categories/tags/amphenol-fci).

Here\'s a Fritzing diagram combining the Interlink FSR, 3.3kΩ resistor, three jumper wires and the Arduino. The circuit will be the same for TekScan. You\'ll just need to adjust the resistor value accordingly.

[![Fritzing circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/fritzing_example_bb_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/fritzing_example_bb_2.png)

And the schematic:

[![Fritzing schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/fritzing_example_schem.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/fritzing_example_schem.png)

This voltage divider will cause the voltage at A0 to increase as the resistance of the FSR decreases. When the FSR is left untouched, measuring as nearly an open circuit, the voltage at A0 should be zero. If you press as hard as possible on the FSR, the voltage should increase close 5V.

## Example Arduino Sketch

Here is a simple Arduino example based on the circuit above. Copy and paste this into your Arduino IDE, then upload!

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /******************************************************************************
    Force_Sensitive_Resistor_Example.ino
    Example sketch for SparkFun's force sensitive resistors
      (https://www.sparkfun.com/products/9375)
    Jim Lindblom @ SparkFun Electronics
    April 28, 2016

    Create a voltage divider circuit combining an FSR with a 3.3k resistor.
    - The resistor should connect from A0 to GND.
    - The FSR should connect from A0 to 3.3V
    As the resistance of the FSR decreases (meaning an increase in pressure), the
    voltage at A0 should increase.

    Development environment specifics:
    Arduino 1.6.7
    ******************************************************************************/
    const int FSR_PIN = A0; // Pin connected to FSR/resistor divider

    // Measure the voltage at 5V and resistance of your 3.3k resistor, and enter
    // their value's below:
    const float VCC = 4.98; // Measured voltage of Ardunio 5V line
    const float R_DIV = 3230.0; // Measured resistance of 3.3k resistor

    void setup() 
    

    void loop() 
    
      else
      
    }

After uploading, **open your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux)**, and set the baud rate to 9600 bps.

If you apply pressure to the FSR, you should see resistance and estimated pressure calculations begin to appear:

[![FSR readings to serial monitor](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/serial_monitor_output.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/serial_monitor_output.png)

Play with the circuit and see how high or low you can get the readings to be. If you have more resistors, try swapping larger or smaller values in for the 3.3kΩ to see if you can make the circuit more sensitive. Don\'t forget to change the value of `R_DIV` towards the top of the sketch if you do!