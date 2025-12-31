# Source: https://learn.sparkfun.com/tutorials/qwiic-dynamic-nfcrfid-tag-hookup-guide

## Introduction

The [SparkFun Qwiic Dynamic NFC/RFID Tag](https://www.sparkfun.com/products/21274) features the ST25DV64KC dynamic Near Frequency Communication (NFC) / Radio Frequency Identification (RFID) tag IC from STMicroelectronics^©^. The ST25DV64KC offers 64-kBit (8-kBytes) of EEPROM memory which can be accessed over both I2C and RF (NFC)! It\'s a state-of-the-art tag which conforms to ISO/IEC 15693 or NFC Forum Type 5 recommendations. You can read and write the tag\'s memory using NFC even while the tag is powered down or disconnected!

[![SparkFun Qwiic Dynamic NFC/RFID Tag](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/0/5/3/SparkFun_Dynamic_RFID_Tag-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-dynamic-nfc-rfid-tag.html)

### [SparkFun Qwiic Dynamic NFC/RFID Tag](https://www.sparkfun.com/sparkfun-qwiic-dynamic-nfc-rfid-tag.html) 

[ SEN-21274 ]

The SparkFun Qwiic Dynamic NFC/RFID Tag features the ST25DV64KC dynamic Near Frequency Communication (NFC) / Radio Frequency ...

[ [\$11.95] ]

In this guide we\'ll go into some detail on the ST25DV64KC IC and other hardware on this Qwiic breakout, how to assemble it into a Qwiic circuit and then install the SparkFun ST25DV64KC Arduino Library.

### Required Materials

To follow along with this guide you will need a microcontroller to communicate with the Qwiic Dynamic NFC/RFID Tag. Below are a few options that come Qwiic-enabled out of the box:

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![SparkFun Thing Plus - Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/1/7/0/15574-SparkFun_Thing_Plus_-_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html)

### [SparkFun Thing Plus - Artemis](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html) 

[ WRL-15574 ]

The SparkFun Artemis Thing Plus takes our popular Feather footprint and adds in the powerful Artemis module for ultimate func...

[ [\$25.95] ]

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

If your chosen microcontroller is not already Qwiic-enabled, you can add that functionality with one or more of the following items:

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![SparkFun Qwiic Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/5/1/14495-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-adapter.html)

### [SparkFun Qwiic Adapter](https://www.sparkfun.com/sparkfun-qwiic-adapter.html) 

[ DEV-14495 ]

The SparkFun Qwiic Adapter provides the perfect means to make any old I^2^C board into a Qwiic enabled board.

[ [\$1.60] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

[![SparkFun Qwiic Shield for Thing Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/7/16790-SparkFun_Qwiic_Shield_for_Thing_Plus-05.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-thing-plus.html)

### [SparkFun Qwiic Shield for Thing Plus](https://www.sparkfun.com/sparkfun-qwiic-shield-for-thing-plus.html) 

[ DEV-16790 ]

The SparkFun Qwiic Shield for Thing Plus makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards t...

[ [\$5.10] ]

You will also need at least one Qwiic cable to connect your sensor to your microcontroller.

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Optional Materials

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend taking a look at the following tutorials if you aren\'t familiar with the concepts covered in them. If you are using one of the Qwiic Shields listed above, you may want to read through their respective Hookup Guides as well before you get started with the Qwiic Dynamic NFC/RFID Tag.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/rfid-basics)

### RFID Basics 

Dive into the basics of Radio Frequency Identification (RFID) technology.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

[](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-shield-for-arduino-nano-hookup-guide)

### SparkFun Qwiic Shield for Arduino Nano Hookup Guide 

Hookup Guide for the SparkFun Qwiic Shield for Arduino Nano.

## Hardware Overview

Let\'s take a closer look at the ST25DV64KC and other hardware present on the Qwiic Dynamic NFC/RFID Tag.

### ST25DV64KC Dynamic NFC/RFID Tag

The ST25DV64KC from STMicroelectronics is a unique tag IC that communicates over both I^2^C and RF (NFC). It conforms to ISO/IEC 15693 (13.56 MHz frequency) and NFC Forum Type 5 recommendations.

[![Highlighting the ST25DV64KC IC.](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_ST25.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_ST25.jpg)

The ST25DV64KC includes 64 Kbit EEPROM for users to write and read data from, a general purpose output to act as an external interrupt reporting events such as RF field changes, RF activity, I^2^C writes and RF switch toggling over I^2^C. The IC has a supply voltage range of **1.8V** to **5.5V** though when in a Qwiic circuit it runs at **3.3V**. It also includes an energy harvesting pin capable of outputing µW of power with an RF field of sufficient strength. For a complete overview of the ST25DV64KC, refer to the [datasheet](https://cdn.sparkfun.com/assets/f/5/4/e/d/st25dv04kc-2450072.pdf).

The ST25DV64KC supports a fast transfer mode to send the contents of a 256 byte buffer between a device connected to the tag over I^2^C (refered to as the tag\'s Mailbox) and an RF device such as a reader or smartphone. This makes it so you can store data on the tag and have it available for reading by an RF device by simply bringing it into the RF read range, even if the tag is powered off. This data can also be password protected with a 64-bit value.

### Power and Communication Interfaces

The Qwiic Dynamic NFC/RFID Tag has two interfaces for powering and communicating with the ST25DV64KC: a pair of Qwiic connectors and a plated through hole (PTH) header.

#### Qwiic Connector

The board has a pair of Qwiic connectors to integrate it into a Qwiic ecosystem.

[![Highlighting the Qwiic connectors.](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Qwiic.jpg)

The Qwiic connectors route the SDA/SCL connections as well as 3.3V and Ground to power the board and communicate with the ST25DV64KC over I^2^C.

#### Plated Through Hole Header

The board has a 0.1\"-spaced PTH header that breaks out the power pins (3.3V and Ground), I^2^C interface (SDA/SCL), energy harvesting pin (VEH), and general purpose output pin (GPO).

[![Highlighting the PTH header.](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Pinout.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Pinout.jpg)

The Energy Harvesting Pin outputs an analog voltage when energy harvesting mode is enabled and in the presence of a strong enough RF field. Refer to section 5.5 of the [datasheet](https://cdn.sparkfun.com/assets/f/5/4/e/d/st25dv04kc-2450072.pdf) for specifics on using this pin. The General Purpose Output is an open-drain configurable pin used for interrupt events.

### Antenna

The board includes a PCB antenna for the ST25DV64KC to help boost the read range a bit. In our testing with a smart phone running an NFC reader app we found it had a range of a few centimeters.

[![Highlighting the PCB antenna.](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Antenna.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Antenna.jpg)

### LED

The sole LED on this board is a power status LED.

[![Highlighting the Power LED.](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_LED.jpg)

### Solder Jumpers

The board has three solder jumpers labeled **LED**, **GPO** and **I2C**. The table below outlines their labels, default state, functionality, and any notes regarding their use.

[![Highlighting the solder jumpers.](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Jumpers.jpg)

  Label   Default State   Function                                                                           Notes
  ------- --------------- ---------------------------------------------------------------------------------- ---------------------------------------
  LED     CLOSED          Completes the Power LED circuit.                                                   Open to disable the Power LED.
  GPO     CLOSED          Pulls the interrupt (GPO) pin HIGH through a **10kΩ** resistor.                    Open to disable the pullup resistor.
  I2C     CLOSED          Pulls the SDA/SCL lines to VCC (**3.3V**) through a pair of **2.2kΩ** resistors.   Open to disable the pullup resistors.

### Board Dimensions

The Qwiic Dynamic NFC/RFID Tag matches the standard Qwiic breakout size of 1\" x 1\" (25.4mm x 25.4mm) and has two mounting holes that fit a [4-40 screw](https://www.sparkfun.com/products/10453).

[![Board dimensions](https://cdn.sparkfun.com/r/600-600/assets/5/9/f/2/f/Qwiic_RFID_Tag.png)](https://cdn.sparkfun.com/assets/5/9/f/2/f/Qwiic_RFID_Tag.png)

## Hardware Assembly

Now that we\'re familiar with the hardware on the Qwiic Dynamic NFC/RFID Tag, it\'s time to assemble it into a Qwiic circuit.

### Basic Assembly

The Qwiic ecosystem makes building a circuit with the Qwiic Dynamic NFC/RFID Tag simple. Just use a Qwiic cable to connect the breakout to your development board like the image shown below:

[![Qwiic circuit assembled.](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Assembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/1/2/Dynamic_RFID_Tag_-_Assembly.jpg)

As a reminder, the Qwiic connectors only include the power pins and I^2^C lines so if you wish to use the Energy Harvesting pin or the General Purpose pin you\'ll need to solder to them or use something like these [IC Hooks](https://www.sparkfun.com/products/9741) for a temporary prototyping connection.

### Soldered Assembly

Users who prefer a traditional soldered connection should solder headers or wires to the Qwiic Dynamic NFC/RFID Tag and then make the appropriate connections to your development board. If you\'ve never soldered before or would like some tips, check out our [How to Solder Tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering).

## SparkFun ST25DV64KC Arduino Library

**Note:** This library assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The SparkFun ST25DV64KC Arduino Library provides an exhaustive collection of examples to take full advantage of the Qwiic Dynamic NFC/RFID Tag including reading and writing the user memory, controlling the read/write permissions, altering the read area sizes, and applying password control. On top of this the library includes examples showing how to use NDEF (NFC Forum Data Exchange Format) URI, WiFi, and Text records you can read with a smart phone. You\'ll need a compatible app on your phone like ST\'s \"NFC Tap\" App available on the [Apple^©^ App store](https://apps.apple.com/us/app/nfc-tap/id1278913597) or [Google^©^ Play](https://play.google.com/store/apps/details?id=com.st.st25nfc&hl=en_GB&gl=US).

Install the library into Arduino by searching for \"SparkFun ST25DV64KX Arduino Library\" in the Arduino Library Manager. Users who prefer to install the library manually can download it by clicking the button below:

[SparkFun ST25DV64KC Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_ST25DV64KC_Arduino_Library/archive/refs/heads/main.zip)

### Arduino Library Documentation

We have an in-depth guide for the library covering all examples as well as the complete API reference you can read through here:

[SparkFun ST25DV64KC Arduino Library - Documentation](https://docs.sparkfun.com/SparkFun_ST25DV64KC_Arduino_Library/)

## Troubleshooting

### General Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)