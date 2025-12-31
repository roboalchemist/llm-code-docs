# Source: https://learn.sparkfun.com/tutorials/level-shifter---8-channel-txs0108e-hookup-guide

## Introduction

The [SparkFun Level Shifter - 8 Channel (TXS0108E)](https://www.sparkfun.com/products/19626) features the TXS0108E^™^ 8-bit, bi-directional logic level translator from Texas Instruments to shift between devices running at different common microcontroller voltages such as 1.8V, 3.3V and 5V. The TXS0108E can transmit data between ports at max speeds of 110Mbps (push/pull) or 1.2Mbps (open drain) so you can use a 3.3V SPI device with a 5V microcontroller like the [SparkFun RedBoard Plus](https://www.sparkfun.com/products/18158) without sacrificing data transmission speeds.

[![SparkFun Level Shifter - 8 Channel (TXS0108E)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/2/9/6/19626-SparkFun_Level_Shifter_-_8_Channel__TXS01018E_-_SparkFun_Level_Shifter_-_8_Channel__TXS01018E_-01.jpg)](https://www.sparkfun.com/sparkfun-level-shifter-8-channel-txs0108e.html)

### [SparkFun Level Shifter - 8 Channel (TXS0108E)](https://www.sparkfun.com/sparkfun-level-shifter-8-channel-txs0108e.html) 

[ BOB-19626 ]

The SparkFun 8 Channel Level Shifter Breakout features the TXS0108E 8-bit, bi-directional logic level translator from Texas I...

[ [\$5.57] ]

In this guide we\'ll go over the specifications of the TXS0108E and how to wire it into a level shifting circuit.

### Required Materials

In order to follow along with this guide you\'ll need the devices you want to level shift between along with the TXS0108E Breakout. The example circuit in the Hardware Assembly section uses the following items to demonstrate shifting from a 5V microcontroller to a 3.3V SPI device:

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![SparkFun Triple Axis Accelerometer Breakout - KX134 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/6/6/1/17589-SparkFun_Triple_Axis_Accelerometer_Breakout_-_KX134__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-kx134-qwiic.html)

### [SparkFun Triple Axis Accelerometer Breakout - KX134 (Qwiic)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-kx134-qwiic.html) 

[ SEN-17589 ]

This SparkFun Triple-Axis Accelerometer Breakout is a simple Qwiic breakout for the KX134 digital accelerometer from Kionix.

[ [\$35.95] ]

### Required Tools

Using this breakout requires through-hole soldering so you may need some of the following tools and soldering accessories:

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

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

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Recommended Reading

This tutorial assumes readers have some know-how about the topics in the tutorials below. If you are not familiar with the concepts covered in them or need a refresher, we recommend reading through them before continuing with this guide:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

## Hardware Overview

Let\'s take a closer look at the TXS0108E level shifting IC and other components on this breakout.

### TXS0108E Level Shifter

The TXS0108E is an 8-channel, bi-directional, level shifting voltage translator that works in both open drain and push/pull operations. It accepts a supply voltage range of **1.4V** to **3.6V** on the A Port and **1.65V** to **5.5V** on the B Port (VCC_A ≤ VCC_B).

[![Front of the Level Shifter Breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/8/5/TXS01018E-Front.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/8/5/TXS01018E-Front.jpg)

The TXS0108E uses pass gate circuit architecture with integrated edge rate (one shot) accelerators to support data transmission speeds up to 1.2Mbps in open drain operation and up to 110Mbps in push/pull operation. It also has built in pull-up resistors for open drain applications so external resistors are not necessary. For complete information on the TXS0108E, refer to the [datasheet](https://cdn.sparkfun.com/assets/1/8/1/e/2/txs0108e.pdf).

### PTH Headers

The board breaks out out all the TXS0108E\'s pins to a pair of 0.1\"-spaced PTH headers; one for each port. The OE input pin is also broken out on the Port A \"side\" as it is referenced to VCCA. The board pulls OE `LOW` through a **110kΩ** resistor to disable the I/O pins by default. Make sure to tie the OE pin to VCCA to enable the device.

[![Back of the Level Shifter Breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/8/5/TXS01018E-Front.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/8/5/TXS01018E-Front.jpg)

### Board Dimensions

The SparkFun Level Shifter - 8 Channel (TXS0108E) measures 1.10\" x 0.50\" (27.94mm x 12.70mm).

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/8/5/TXS01018E-Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/8/5/TXS01018E-Dimensions.png)

## Hardware Assembly

In this section we\'ll demonstrate how to assemble this breakout into a level-shifting circuit between a 5V development board, the [RedBoard Plus](https://www.sparkfun.com/products/18158), and a 3.3V SPI device, the [SparkFun Triple Axis Accelerometer Breakout - KX134 (Qwiic)](https://www.sparkfun.com/products/17589). We\'ll use a [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) here to make building the level shifting circuit easier and to keep the connections as short as possible.

### Soldering Assembly

This breakout requires some through-hole soldering to integrate the board into a level-shifting circuit. Since the demo circuit uses a breadboard we\'ll solder a set of [breakaway male headers](https://www.sparkfun.com/products/116) to the board so we can easily plug it into the breadboard.

[![Headers soldered to breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/8/5/TXS01018E-Soldered_Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/8/5/TXS01018E-Soldered_Headers.jpg)

### Arduino Assembly

Plug the Level Shifter Breakout into the breadboard and then make connections to the board with wires. Leave the circuit unpowered while building the circuit to avoid damaging anything with a short or improper connection.

[![Completed Level Shifting circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/8/5/TXS01018E-Assembly2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/8/5/TXS01018E-Assembly2.jpg)

*Having trouble seeing the detail in the image? Click on it for a larger view.*

Reminder, VCC_A must be less than or equal to VCC_B and OE needs to connect to VCC_A. Our SPI device runs at **3.3V** so we connect the peripheral pins to channels on Port A and connect matching microcontroller signals to Port B.

## Troubleshooting

### Signal Oscillations

Some users may experience oscillations or \"ringing\" on communication lines (eg. SPI/I^2^C) that can inhibit communication between devices. Capacitance or inductance on the signal lines can cause the TXS0108E\'s edge rate accelerators to detect false rising/falling edges.

When using the TXS0108E, we recommend keeping your wires between devices as short as possible as during testing we found even a 6\" wire like our standard jumper wires can cause this oscillation problem. Also make sure to disable any pull-up resistors on connected devices. When level shifting between I/O devices, this shifter works just fine over longer wires.

The TXS0108E is designed for short distance, high-speed applications so if you need a level shifter for a communication bus over a longer distance, we recommend one of our other [level shifters](https://www.sparkfun.com/categories/361).

### Voltage Requirements and OE

Reminder, voltage supplied to VCC_A must be less than or equal to VCC_B. Also, the breakout pulls OE LOW so make sure to tie the OE pin to VCC_A to enable the TXS0108E.

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