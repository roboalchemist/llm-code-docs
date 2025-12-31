# Source: https://learn.sparkfun.com/tutorials/sparkfun-arduino-protoshield-hookup-guide

## Introduction

[] **Heads Up!** This tutorial is for the latest version of the SparkFun Arduino ProtoShield. If you have an older version, please consult the retired [Arduino ProtoShield Quickstart Guide](https://learn.sparkfun.com/tutorials/arduino-protoshield-quickstart-guide)

The [SparkFun Arduino ProtoShield PCB](https://www.sparkfun.com/products/13819) and [ProtoShield kit](https://www.sparkfun.com/products/13820) lets you customize your own Arduino shield using whatever custom circuit you can come up with! This tutorial will go over its features, hardware assembly, and how to use shield.

[![SparkFun Arduino ProtoShield - Bare PCB](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/4/1/1/13819-SparkFun_ProtoShield-01.jpg)](https://www.sparkfun.com/sparkfun-arduino-protoshield-bare-pcb.html)

### [SparkFun Arduino ProtoShield - Bare PCB](https://www.sparkfun.com/sparkfun-arduino-protoshield-bare-pcb.html) 

[ DEV-13819 ]

The SparkFun Arduino ProtoShield is a bare PCB with no attached or included parts that lets you customize your own shield usi...

[ [\$6.95] ]

[![SparkFun ProtoShield Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/4/1/2/13820-SparkFun_ProtoShield_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-protoshield-kit.html)

### [SparkFun ProtoShield Kit](https://www.sparkfun.com/sparkfun-protoshield-kit.html) 

[ DEV-13820 ]

The SparkFun ProtoShield Kit lets you customize your own Arduino shield using whatever circuit you can come up with and then ...

[ [\$14.95] ]

### Suggested Materials

To follow along with this project tutorial, you will need the following materials. Depending on what you have, you may not need everything listed here. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You will need a soldering iron, solder, [general soldering accessories](https://www.sparkfun.com/categories/49), and the tools listed below for prototyping.

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Needle Nose Pliers](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/3/08793-03-L.jpg)](https://www.sparkfun.com/needle-nose-pliers.html)

### [Needle Nose Pliers](https://www.sparkfun.com/needle-nose-pliers.html) 

[ TOL-08793 ]

Mini Pliers. These are great little pliers! A must have for any hobbyist or electrical engineer. Crucial for inserting device...

[ [\$3.60] ]

[![Diagonal Cutters](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/4/08794-03-L.jpg)](https://www.sparkfun.com/diagonal-cutters.html)

### [Diagonal Cutters](https://www.sparkfun.com/diagonal-cutters.html) 

[ TOL-08794 ]

Mini Diagonal Cutters. These are great little cutters! A must have for clipping leads and extra solder tails. 4\" long.

[ [\$3.75] ]

[![Wire Strippers - 30AWG Hakko](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/1/2/12630-Hakko-Wire-Strippers-30AWG-Feature.jpg)](https://www.sparkfun.com/wire-strippers-30awg-hakko.html)

### [Wire Strippers - 30AWG Hakko](https://www.sparkfun.com/wire-strippers-30awg-hakko.html) 

[ TOL-12630 ]

It can be used as: Shears, Multi-diameter Wire stripper, pliers.

[ [\$13.95] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/using-the-bluesmirf)

### Using the BlueSMiRF 

How to get started using the BlueSMiRF and Bluetooth Mate Silvers.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/arduino-shields-v2)

### Arduino Shields v2 

An update to our classic Arduino Shields Tutorial! All things Arduino shields. What they are and how to assemble them.

### Suggested Viewing

## Hardware Overview

There is a lot going with the ProtoShield so it is useful to know what side we are referencing when soldering components to the board. We will refer to the top side based on the board\'s name on the upper right hand corner. The bottom will be the side with the jumpers.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/13819-SparkFun_ProtoShield-TopView.jpg "SparkFun Arduino ProtoShield Bottom View")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/13819-SparkFun_ProtoShield-TopView.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/13819-SparkFun_ProtoShield-BottomView.jpg "SparkFun Arduino ProtoShield Top View")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/13819-SparkFun_ProtoShield-BottomView.jpg)
  *Top View*                                                                                                                                                                                                                                     *Bottom View*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Stackable Headers for Arduino Uno R3 Footprint

The Arduino ProtosShield is based off the Arduino R3\'s footprint. Headers can be installed on the pins located closest to the edge of the board. You will notice that the location of the headers are highlighted in a rectangular silkscreen. For those using the stackable headers included in the kit, make sure to insert the header from the top side and solder from the bottom.

[![Arduino Uno R3 Footprint](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_R3_Footprint.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_R3_Footprint.jpg)

These pins are also broken out on the other side of its labeling. You will notice that the 1x10 header on the upper right side of the board is slightly offset from the Arduino R3 footprint. Don\'t worry, this was intentional so that you can place the board on a standard breadboard!

[![Arduino R3 Footprint Broken Out](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_R3_Footprint_BrokenOut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_R3_Footprint_BrokenOut.jpg)

### Prototyping Area

Next up is the sea of plated through holes. Look at all that great space for prototyping projects!

[![Prototyping Area](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_SeaofPTH.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_SeaofPTH.jpg)

#### Solderless Mini-Breadboard

Do you have a small circuit on a mini-breadboard connected to your RedBoard or Arduino Uno? The ProtoShield has a spot to place a mini-breadboard on top to keep everything together. Peel the adhesive off the mini-breadboard, align it to the silkscreen, and stack it on!

[![SolderLess Mini-Breadboard](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_MiniBreadboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_MiniBreadboard.jpg)

#### Solderable-Like Breadboard

Once you are done prototyping your circuit on the mini-breadboard, there is an option to solder the circuit directly to the board for a more secure connection. The bottom half of this area was designed with a breadboard in mind. You will not notice too much on the top side. Flip the board over and you will see open jumper pads between each through hole to make a connection like a breadboard. Once you add a component, simply add a solder jumper between holes to make a connection. For those that prefer the standard prototyping pads, we left the other side as is.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_SolderableBreadboard.jpg "Solderable-Like Breadboard (Top View)")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_SolderableBreadboard.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-BottomView_SolderabledBreadboardJumpers.jpg "Solderable-Like Breadboard w/ Open Jumpers (Bottom View)")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-BottomView_SolderabledBreadboardJumpers.jpg)
  *Solderable-Like Breadboard (Top View)*                                                                                                                                                                                                                                                   *Solderable-Like Breadboard w/ Open Jumpers (Bottom View)*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### ICSP [(MISO, MOSI, and SCK NC)]

Need to access the Arduino\'s ICSP pins? The pins are broken out if you do not want to remove the shield every time you need the ICSP pins or if you decide to stack another shield on top of the ProtoShield. You will need add two [1x3 stackable headers](https://www.sparkfun.com/products/13875).

[![SPI Pins (Not Connected)](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Snappable-NotConnectedSPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Snappable-NotConnectedSPI.jpg)

**Note:** The MISO, MOSI, and SCK pins are **not connected (NC)**.\
\
Additionally, there may not be enough room for a mini-breadboard if you decide to add 1x3 stackable headers to the ICSP pins and then stack an additional shield on top. You will need to go with a lower profile by soldering the circuit with wires to the ProtoShield.

⚡ **Oh snap!** This shield was designed for the Arduino Uno footprint. If you are using a variant with 3.3V logic level on the ICSP pin (i.e. [SAMD21 Development Board](https://www.sparkfun.com/products/13672) or [Arduino Pro 3.3V/8MHz](https://www.sparkfun.com/products/10914)), you will need to [cut the two traces](https://learn.sparkfun.com/tutorials/how-to-work-w-jumper-pads-and-pcb-traces) connecting to the 5V pin on the 1x3 ICSP header.

### Power

There are a few locations along the outside of the board for power and ground. Let\'s focus on the power rails in the prototyping area.

#### 5V Rail

Just below the silkscreen for the mini-breadboard is a 5V rail. This is connected to the **5V** pin from your Arduino.

[![5V Rail](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_5VRail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_5VRail.jpg)

#### VDD Rail (NC)

Need a different voltage? We squeezed a VDD rail just below. It is currently not connected to anything. We left it up to the user to connect to Arduino\'s 3.3V pin or another regulated voltage (i.e. 2.8V or 1.8V).

[![VDD Rail](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_VDDRail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_VDDRail.jpg)

#### GND Rail

Need to ground more circuits? There are few more ground connections on the board as indicated by the image below.

[![Ground Rail](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_GNDRail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Arduino_GNDRail.jpg)

### Reset Button

Stacking a shield on an Arduino can make it hard to reset the microcontroller. Like other Arduino shields, the reset button has been rerouted on the ProtoShield.

[![Reset Button](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/13819-SparkFun_ProtoShield-TopView_Reset.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/13819-SparkFun_ProtoShield-TopView_Reset.jpg)

### Software Serial UART Port

The SparkFun Arduino ProtoShield breaks out a software serial UART port. The pins are arranged in such a way as to connect to our [BlueSMiRF if you decide to go wireless](https://learn.sparkfun.com/tutorials/using-the-bluesmirf).

[![Software Serial UART ](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_SoftwareSerialUART.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_SoftwareSerialUART.jpg)

If you decide that you want to connect a different serial UART device (i.e. a UART-to-serial device like the [FTDI Basic Breakout](https://www.sparkfun.com/products/9716)) or use different pins for serial, we added closed jumpers on the back. Simply cut the traces and reroute the connection by adding wires to the headers.

[![Software Serial UART Jumper Pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-BottomView_SoftwareSerialUARTJumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-BottomView_SoftwareSerialUARTJumpers.jpg)

⚠ **Warning:** For users connecting a [FTDI Basic Breakout](https://www.sparkfun.com/products/9716), we recommend cutting the 5V jumper on the back to avoid conflicting voltages from the FTDI and the Arduino.

### Oh Snap! ProtoSnap-able Prototyping Hardware

The board includes prototyping hardware that is based on the ProtoSnap design. When you are finished testing and want to use bigger components, simply snap off the bottom of the board using pliers.

[![ProtoSnap-able](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Snappable-Prototyping-Components.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Snappable-Prototyping-Components.jpg)

#### 3mm LEDs (NC)

When viewing the board from the top, there are two locations for 3mm LEDs and their 330Ω current limiting resistors.

[![3mm LEDs (Not Conencted)](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Snappable-LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Snappable-LEDs.jpg)

**Note:** The LED pins **L1 and L2 are not connected (NC)**. To control, simply solder a wire from **L1** or **L2** to an I/O pin. Ground is currently connected to the rest of the shield between the mousebites. We left it up to the user to choose and solder these connections.

#### Momentary Pushbutton (NC)

There is a spot for a momentary pushbutton and 10kΩ pull up resistor on the other side of the LEDs.

[![Momentary Pushbutton (Not Connected)](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Snappable-MomentaryPushButton.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield-TopView_Snappable-MomentaryPushButton.jpg)

**Note:** The button **(SW2)** is not connected **(NC)**. To control, simply solder a wire from **SW2** to an I/O pin. 5V and ground are currently connected to the rest of the shield between the mousebites. We left it up to the user to connect.

## Hardware Assembly

### Headers

Grab a female stackable header and slide it from the top side of the ProtoShield. With your soldering hand, pull the header with your index finger and thumb toward the edge of the board. Using your other hand, push against the header using your index finger and grip the board with your thumb. Hold the header down with your middle finger.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Tutorial_Align_Header.jpg "Align Header to ProtoShield")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Tutorial_Align_Header.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Hold.jpg "Hold Header Down")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Hold.jpg)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Grab the soldering iron with your soldering hand and tack on one pin. Repeat for each header.

[![Tack on One Pin on the Header and Repeat](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Header.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Header.jpg)

### Buttons

Insert the buttons for reset and prototyping. You may need to bend the buttons to fit into the through holes. Careful not to snap off the prototyping area! Hold the button against the board and tack some solder on one pin.

[![Tack on the Buttons](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Tack_On_Button.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Tack_On_Button.jpg)

### LEDs

Find the 3mm LED\'s cathode side and align it with its silkscreen labeled with a \"**---**\" sign. Slide the LED in from the top side and tack on a pin. Repeat for the second LED.

[![Align the LED and Tack on a Pin](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Align_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Align_LED.jpg)

### Resistors

The kit includes resistors with two different values. There is one 10kΩ resistor \[color band = BROWN, BLACK, ORANGE, GOLD \] that is used as a pull-up resistor. The two 330Ω resistors \[color band = ORANGE, ORANGE, BROWN, GOLD\] are used to limit current to the LEDs.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/10kOhmColorCoding.jpg "10kOhm Color Coding")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/10kOhmColorCoding.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/330OhmColorCoding.jpg "330Ohm Color Coding")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/330OhmColorCoding.jpg)
  *10kΩ Pull-Up Resistor*                                                                                                                                                                 *330Ω Current Limiting Resistor*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let\'s start with the pull-up resistor. Bend the 10kΩ resistor\'s terminals.

[![Bend Resistor](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/BendResistor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/BendResistor.png)

Then slide the pins where it says \"**10k**\".

[![Add the 10kΩ Pull-Up Resistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Pull_Up_Resistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Pull_Up_Resistor.jpg)

Bend the terminals to hold the resistor in place for soldering. The resistor can get hot to the touch when holding the component down during soldering. At this point, feel free to grab a small piece of cardboard to hold the resistor down. When you are ready, tack one of the 10kΩ resistor\'s pins. Repeat for the 330Ω resistors.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Soldering_Cardboard_Protector.jpg "Piece of Cardboard to Hold Resistor Down when Soldering")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Soldering_Cardboard_Protector.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Pull_Up_Resistor.jpg "Tacking One Pin of the Pullup resistor")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Pull_Up_Resistor.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Check Alignment Before Soldering Away!

At this point, it would be good to check the alignment of the components. Make sure that they are flush against the board and they are in its correct location. Did you add solder for the components on the bottom side? All of the components included in the kit should be soldered on the side of the jumpers.

Everything good? Solder away! This is the fun part.

[![Solder All the Pins Down](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Away.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Away.jpg)

### Cut Excess Leads

Grab a flush cutter and trim off excess leads connected to the prototyping hardware. Careful not to cut off the stackable headers!

[![Cut Off Excess Leads](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Clip_Off_Excess_Leads.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Clip_Off_Excess_Leads.jpg)

### Finished ProtoShield

If you used water soluble flux, clean the board off. Otherwise, bask in the glow of your new ProtoShield for Arduino! Your board should look similar to the images below with the terminals soldered and cut.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Component_Alignment_1.jpg "Side View of Headers")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Component_Alignment_1.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Component_Alignment_2.jpg "Side View of Prototyping Hardware")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Component_Alignment_2.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Finished ProtoShield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/Minimum_Components_Soldered_on_SparkFun_ProtoShield_for_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/Minimum_Components_Soldered_on_SparkFun_ProtoShield_for_Arduino.jpg)

#### Customize

So what do you do from here? There are a few options! We left this up to the user to choose depending on personal preference. You can stick a mini-breadboard on the shield for prototyping small circuits. Additional headers can be added on however you would like for serial UART or in the prototyping area. For a lower profile, you can also [strip hookup wire](https://learn.sparkfun.com/tutorials/working-with-wire) and solder cables against the plated through holes.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Female_Headers_Mini_Breadboard.jpg "Customized with Mini-Breadboard and Headers")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Female_Headers_Mini_Breadboard.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Wires_Female_Header_Wires_Mini_Breadboard.jpg "Customized with Mini-Breadboard, Headers, and Hookup Wire")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Wires_Female_Header_Wires_Mini_Breadboard.jpg)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For those sandwiching the ProtoShield with another shield, you can solder two 1x3 stackable headers for the ICSP pins. If you choose this route, you will need to go with a lower profile, using wires to connect the circuit.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_ICSP_Pins_1x5JumperCable_CloseUp.jpg "ICSP Pins Close Up with Stackable Headers")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_ICSP_Pins_1x5JumperCable_CloseUp.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_ICSP_Pins_1x5JumperCable.jpg "ICSP Pins with Stackable Headers")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_ICSP_Pins_1x5JumperCable.jpg)
  *Close Up of ICSP Pins w/ Stackable Headers*                                                                                                                                                                                                                                                                            *ProtoShield w/ Stackable Headers*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚡ **Oh snap!** This shield was designed for the Arduino Uno footprint. If you are using a variant with 3.3V logic level on the ICSP pin (i.e. [SAMD21 Development Board](https://www.sparkfun.com/products/13672) or [Arduino Pro 3.3V/8MHz](https://www.sparkfun.com/products/10914)), you will need to [cut the two traces](https://learn.sparkfun.com/tutorials/how-to-work-w-jumper-pads-and-pcb-traces) connecting to the 5V pin on the 1x3 ICSP header.

#### Finished Prototyping?

If you are finished prototyping, you can remove the mini-breadboard and solder your custom circuit to the prototyping area for a more secure connection. Want to use a different LED or a bigger button in your project? You can snap off the prototyping area using [needle nose pliers](https://www.sparkfun.com/products/8793) and replace it with the hardware of your choice!

[![Big Dome Pushbutton - Red](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/1/7/09181-Big_Dome_Pushbutton_-_Red-01.jpg)](https://www.sparkfun.com/big-dome-pushbutton-red.html)

### [Big Dome Pushbutton - Red](https://www.sparkfun.com/big-dome-pushbutton-red.html) 

[ COM-09181 ]

It\'s the end of the world, and you need a button to press. This is it. A 100mm diameter (outside diameter) dome illuminated p...

[ [\$18.95] ]

[![Metal Pushbutton with Wires - Momentary (16mm, Red)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/4/4/6/11966-Metal-Pushbutton-Feature.jpg)](https://www.sparkfun.com/metal-pushbutton-momentary-16mm-red.html)

### [Metal Pushbutton with Wires - Momentary (16mm, Red)](https://www.sparkfun.com/metal-pushbutton-momentary-16mm-red.html) 

[ COM-11966 ]

This is a perfect choice if you are in need of a heavy duty push button! These metal push buttons are a very tough, small, pa...

[ [\$8.95] ]

[![Super Bright LED - Red 10mm](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/2/8/08862-Super_Bright_LED_-_Red_10mm-01.jpg)](https://www.sparkfun.com/super-bright-led-red-10mm.html)

### [Super Bright LED - Red 10mm](https://www.sparkfun.com/super-bright-led-red-10mm.html) 

[ COM-08862 ]

Huge 10mm through-hole LEDs. Mood light an entire wall!

[ [\$1.85] ]

[![NovelKeys Big Switch - Tactile](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/9/14583-NovelKeys_Big_Switch_-_Tactile-_03.jpg)](https://www.sparkfun.com/products/14583)

### [NovelKeys Big Switch - Tactile](https://www.sparkfun.com/products/14583) 

[ COM-14583 ]

Assembling your own custom keyboard is quickly becoming a fun hobby among computer enthusiasts, but what if you could build a...

**Retired**

## Example Code

**Note:** The following examples assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Blinking LED

Let\'s connect L1 to pin 13 using a wire. Assuming that you soldered to **L1**, connect it to pin 13.

  Prototyping Hardware   Arduino
  ---------------------- ---------
  L1                     13

Copy the code below and upload to your Arduino!

    language:c
    /*BLINKING AN LED

      Turn an LED on for one second, off for one second,
      and repeat forever.

      This sketch was written by SparkFun Electronics,
      with lots of help from the Arduino community.
      This example is based on the blinking an LED
      example in the SparkFun Inventor's Kit v3.3.

      This code is completely free for any use.
      Visit https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v33/experiment-1-blinking-an-led
      for more information.
      Visit http://www.arduino.cc to learn about the Arduino.

      Version 2.0 6/2012 MDG
    ******************************************************************************/

    // The LED is connected to digital pin 13
    // Change the pin number depending on 
    // what L1 is connected to.
    const int L1 = 13;

    void setup()
    

    void loop()
    

LED labeled as L1 should begin blinking.

[![Blink](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Blink.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Blink.jpg)

### Fading LED

Let\'s connect L2 to pin 6 and to fade in and out. Assuming that you soldered to **L2**, connect it to pin 6.

  Prototyping Hardware   Arduino
  ---------------------- ---------
  L2                     6

Copy the code below and upload to your Arduino!

    language:c
    /* Fading LED

      Use for-loops to smoothly vary the brightness of an LED

      This sketch was written by SparkFun Electronics,
      with lots of help from the Arduino community.
      This example is based on the Fading LEDs example
      in the LilyPad Development Board Activity Guide.

      This code is completely free for any use.
      Visit https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide/4-fading-leds
      for more information
      Visit http://www.arduino.cc to learn about the Arduino.

    ******************************************************************************/

    // Create integer variable for the LED pin we'll be using:
    const int L2 = 6;

    // Create a new integer variable called brightness:
    int brightness;

    void setup()
    

    void loop()
     below the for)
      // 4. a command to run before doing it again (brightness = brightness + 1)

      // Here's a for command which will start brightness at 0, check to see if it's less than
      // or equal to 255, run the commands after it, then add one to brightness and start over:

      for (brightness = 0; brightness <= 255; brightness = brightness + 1)
      

      // What if we want the LED to start at full brightness and fade to black?
      // We can easily set up the for loop to run in reverse:

      for (brightness = 255; brightness >= 0; brightness = brightness - 1)
      
    }

LED labeled as L2 should begin fading in and out. Try connecting and redifining the LED to another pin on your Arduino to see if you can still fade.

[![Blink](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Fade.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Fade.jpg)

### Momentary Push Button

Let\'s connect SW2 to pin 2 to read a push button. For feedback, we will be using both of the LEDs in our prototyping hardware. Assuming that you soldered to **SW2, L2, and L1**, connect it to their respective pins on 2, 6, and 13.

  Prototyping Hardware   Arduino
  ---------------------- ---------
  SW2                    2
  L2                     6
  L1                     13

Copy the code below and upload to your Arduino!

    language:c
    /*Momentary Push Button

      Use momentary pushbuttons for digital input

      This sketch was written by SparkFun Electronics,
      with lots of help from the Arduino community.
      This example is based on the push button
      example in the SparkFun Inventor's Kit v3.3

      This code is completely free for any use.
      Visit https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v33/experiment-5-push-buttons
      for more information.
      Visit http://www.arduino.cc to learn about the Arduino.

      Version 2.0 6/2012 MDG
      Version 2.1 9/2014 BCH
    ****************************************************************/

    const int SW2 = 2;  // pushbutton 1 pin
    const int L1 =  13;    // LED pin
    const int L2 =  6;     // LED pin

    int button1State;  // variables to hold the pushbutton states

    void setup()
    

    void loop()
    
      else 
    }

Pressing on the button should light up both LEDs simultaneously. Removing your finger from the button should turn them off.

[![Push Button LEDs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Momentary_Push_Button.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Momentary_Push_Button.jpg)

### Bluetooth Serial Passthrough

Let\'s try to send a character between two [BlueSMiRF Silvers](https://www.sparkfun.com/products/12577) (i.e. the RN42s). In this example, we will need two bluetooths, ProtoShields, and Arduinos. Assuming that the boards are soldered, connect the BlueSMiRFs to the Software Serial UART port. We will be using the default connection to software serial pins 10 and 11. Simply align the silkscreen as indicated in the hookup table below.

  BlueSMiRF Silver   ProtoShield Software Serial UART port
  ------------------ ---------------------------------------
  RX-I               RXI (D11)
  TX-O               TXO (D10)
  GND                GND (GND)
  VCC                VCC (5V)

⚡ **Oh snap!** This shield was designed for the BlueSMiRF footprint. If you are using the Bluetooth Mate, you will need to [cut the traces](https://learn.sparkfun.com/tutorials/how-to-work-w-jumper-pads-and-pcb-traces) and reroute the respective pins. For more information about the differences, make sure to check out the comparison in the [Using the BlueSMiRF](https://learn.sparkfun.com/tutorials/using-the-bluesmirf#hardware-overview) tutorial.

We will also be using the same connection to the prototyping hardware.

  Prototyping Hardware   Arduino
  ---------------------- ---------
  SW2                    2
  L2                     6
  L1                     13

Power both up, copy the code below, and upload to both Arduinos!

    language:c
    /*
      Example Bluetooth Serial Passthrough Sketch
      modified by: Ho Yun "Bobby" Chan
      date: May 17, 2018
      by: Jim Lindblom
      date: February 26, 2013
      SparkFun Electronics
      license: Public domain

      This example sketch converts an RN-42 bluetooth module to
      communicate at 9600 bps (from 115200), and passes any serial
      data between Serial Monitor and bluetooth module.
    ****************************************************************/

    #include <SoftwareSerial.h>

    int bluetoothTx = 10;  // TX-O pin of bluetooth mate, Arduino D10
    int bluetoothRx = 11;  // RX-I pin of bluetooth mate, Arduino D11

    SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);// (Arduino SS_RX = pin 10, Arduino SS_TX = pin 11)

    void setup()
    

    void loop()
    
      if (Serial.available()) // If stuff was typed in the serial monitor
      
      // and loop forever and ever!
    }

[![Arduino ProtoShield Bluetooth](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Bluetooth.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Bluetooth.jpg)

#### Discovering, Pair, and Autoconnecting Bluetooths

Once uploaded,

- open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) set at **9600 baud** with **No line ending**
- send **\$\$\$** and hit the **Send** button to set the bluetooth in command mode
- change the Arduino Serial Monitor from *No Line Ending* to **Newline**
- send the autoconnect command **sm,3**
- send the inquiry scan command **i** to scan for the other bluetooth in range

You should see something similar to the output below.

    language:bash
    CMD
    AOK
    Inquiry, COD=0
    Found 1
    000666643FBF,RN42-3FBF,1F00
    Inquiry Done

The other RN42 bluetooth that was in range came up with address of `000666643FBF`. You should see something similar when connecting a RN-41 or RN-42. Type the following command and change the address to the one that you obtained:

- **c,000666643FBF** and hit the **Send** button

This will pair and connect both bluetooths together. The address will be saved in memory and auto connect every time there is a power cycle. Open a serial terminal (since you can only have one Arduino Serial Monitor open at a time) set at **9600 baud** and connect the other Arduino/ProtoShield/BlueSMiRF. Sending any character from the Arduino Serial Monitor should pop up on the serial terminal and vice versa!

### Combining It All to Send a Message!

Let\'s send a simple message between the two bluetooths now that they are configured to autoconnect. Copy the code below, and upload to both Arduinos!

    language:c
    /*
      Example Serial Bluetooth Messenger
      by: Ho Yun "Bobby" Chan
      SparkFun Electronics
      date: May 16, 2018
      license: Public domain

      This example sketch converts an RN-42 bluetooth module to
      communicate at 9600 bps (from 115200). Assuming that the
      two bluetooths are paired and configured to autoconnect,
      a message is sent with the push of a button. Any 
      received characters from the other bluetooth will display 
      on the serial monitor. 

      This sketch was written by SparkFun Electronics.
      This example is based on the Example Bluetooth Serial 
      Passthrough Sketch by Jim Lindblom.

      This code is completely free for any use.
      Visit https://learn.sparkfun.com/tutorials/using-the-bluesmirf
      for more information.
    ****************************************************************/

    #include <SoftwareSerial.h>

    const int SW2 = 2;  // pushbutton 1 pin
    const int L1 =  13;    // LED pin for push button
    const int L2 =  6;     // LED pin for received character

    int button1State;  // variables to hold the pushbutton states

    int bluetoothTx = 10;  // TX-O pin of bluetooth mate, Arduino D10
    int bluetoothRx = 11;  // RX-I pin of bluetooth mate, Arduino D11

    SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);// (Arduino SS_RX = pin 10, Arduino SS_TX = pin 11)

    void setup()
    

    void loop()
    
      else 

      // If the bluetooth received any characters, print to the serial monitor
      if (bluetooth.available())
      
      else 
      // and loop forever and ever!
    }

Pressing a button on one of the Arduinos (as indicated by the blue mini-breadboard) should send a message and light up the LED labeled as L1 on the transmitting node. The receiving node (as indicated by the green mini-breadboard) will light up the LED labeled as L2 and print a message (in this case \"**Hi!**\") to a serial monitor or serial terminal. The other Arduino will to the same when you press on its button.

[![Sending a Saved Message](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Bluetooth_Messager.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_Bluetooth_Messager.jpg)

**Note:** Take turns pressing on the push buttons to transmit. The message may get garbled when both bluetooths are transmitting simultaneously.