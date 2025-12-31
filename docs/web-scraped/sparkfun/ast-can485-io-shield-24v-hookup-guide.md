# Source: https://learn.sparkfun.com/tutorials/ast-can485-io-shield-24v-hookup-guide

## Introduction

The [AST-CAN485 I/O Shield (24)](https://www.sparkfun.com/products/14598) is an Arduino shield that will allow the user to interface the [AST-CAN485 Dev Board](https://www.sparkfun.com/products/14483) with 24V inputs and outputs, which expands its usefulness into industrial systems.

[![SparkFun AST-CAN485 I/O Shield (24V)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/5/6/14598-SparkFun_AST-CAN485_I_O_Shield__24V_-01.jpg)](https://www.sparkfun.com/sparkfun-ast-can485-i-o-shield-24v.html)

### [SparkFun AST-CAN485 I/O Shield (24V)](https://www.sparkfun.com/sparkfun-ast-can485-i-o-shield-24v.html) 

[ DEV-14598 ]

The AST-CAN485 I/O Shield allows you to interface the AST-CAN485 Dev Board with 24V inputs and outputs, expanding its usefuln...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

Depending on your setup, you will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49) to solder pins to the AST-CAN485. You will also need a flat head and wire strippers to connect wires to the screw terminals.

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

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/1/14763-Wire_Strippers_-_758PL0066-03.jpg)](https://www.sparkfun.com/products/14763)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/14763) 

[ TOL-14763 ]

These are high grade wire strippers from Techni-Tool with a curved grip making them an affordable option if you need to remov...

**Retired**

### Suggested Reading

We recommend checking out the AST-CAN485 Hookup Guide to get started with the board. Depending on your setup, you may need to install custom libraries and board add-ons.

[](https://learn.sparkfun.com/tutorials/ast-can485-hookup-guide)

### AST-CAN485 Hookup Guide 

March 1, 2018

The AST CAN485 is a miniature Arduino in the compact form factor of the ProMini. In addition to all the usual features it has on-board CAN and RS485 ports enabling quick and easy interfacing to a multitude of industrial devices.

Also, if you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

## Hardware Overview

### Input Power

The AST-CAN485 I/O Shield provides a socket to break out all of the IO of the AST-CAN485 board. To make a secure connection to your industrial equipment, screw terminals come pre-soldered to the board to get you up and running in no time. The AST-CAN485 I/O Shield is designed to work in the industrial **24V** environment, but has a wide supply input range of **7-24V**. The board comes with input reverse voltage protection with a green and red status LEDs (green means power is connected properly, and red indicates reversed power, and blocks power to the rest of the board.

[![Power input highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-Power_Input_highlight_cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-Power_Input_highlight_cropped.jpg)

### 24 I/O Pins

At your disposal are four **24V** input channels with LEDs to indicate the input logic level, along with an additional four **24V** output channels with matching indicator LEDs.

[![24V input and output highlights](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-24V_input_output_highlight_cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-24V_input_output_highlight_cropped.jpg)

### RS-485 and CAN

Which do you prefer to use for your communication standard: RS-485 or CAN? Well it doesn\'t matter because as the name indicates, the CAN485 board will handle them both, and they\'re both broken out to the secure screw terminals as well!

[![RS-485 and CAN bus screw terminal highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-CAN_RS-485_highlight_cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-CAN_RS-485_highlight_cropped.jpg)

### SPI and I2C

If SPI and I2C are more in your wheelhouse, the CAN485 board breaks those out to screw terminals well, but you are limited to **5V** logic.

[![SPI and I2C screw terminal highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-SPI_I2C_highlight_cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-SPI_I2C_highlight_cropped.jpg)

### AST-CAN485 Pins

All of the **5V** logic level pins of the AST-CAN485 board are also broken out with an easy to read 2x13 pin header.

[![5V logic pin highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-5V_logic_highlight_cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-5V_logic_highlight_cropped.jpg)

### Pinouts

⚡ **Warning!** This board has pins that operate at **24V** as well as pins that operate at **5V**. Care should be taken during wiring as 24V has the potential to do significant damage to 5V circuits.

[![PinOuts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/6/7/24VIOShieldPinOut.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/24VIOShieldPinOut.png)

*Image courtesy of AST*

*Having a hard time seeing? Click the image for a closer look.*

## Hardware Hookup

The AST-CAN485 I/O shield comes with female headers pre-soldered. Insert the CAN485 as shown with the FTDI header close to the input power pins:

[![Insert the Shield into the AST CAN485](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/6/7/HardwareHookup24VIO.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/HardwareHookup24VIO.jpg)

### Powering The Shield

The shield requires **24V** power in order to function correctly. This can be supplied on any of the power terminals as shown below. Additional terminals are provided to allow powering of external devices.

There is reverse voltage protection on the 24V power terminals. The power status LED will show green for correctly wired power. If wired incorrectly, the LED will be red.

An integrated power supply regulates the 24V input power down to 5V which is used to provide power to the inserted CAN485 board. This 5V supply is also broken out to the terminals as shown.

[![Powering the Board](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-Power_Input_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/7/I_O_Shield-Power_Input_highlight.jpg)

## Software Setup and Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library or board add-on, please check out our [library installation guide](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) and instructions to install the [AST-CAN485 board add-on files](https://learn.sparkfun.com/tutorials/ast-can485-hookup-guide#software-installation).

This board is a shield for the AST-CAN485 development board and is not programmed directly. There is a library for the CAN485 which enables some board features and contains some examples. It can be downloaded from the [GitHub Repo](https://github.com/Atlantis-Specialist-Technologies/AST_V24IO_Arduino_Library) or by clicking the button below to manually install.

[AST V24IO Arduino Library (ZIP)](https://github.com/Atlantis-Specialist-Technologies/AST_V24IO_Arduino_Library/archive/master.zip)

### JTAG

One limitation of the shield is that JTAG debugging and Input *24V I1* cannot be used at the same time. Input *V24 I1* is connected to pin *A6* on the CAN485, this pin is also used for JTAG debugging. In order to use that input channel, JTAG debugging must be disabled. This is done automatically when calling the board initialization function provided by the library.

### Examples

The library also includes several examples which demonstrate the use of the board. After installing the library, open up one the examples listed in the folder **File \> Examples \> AST_V241O** through the Arduino IDE. Select the **CAN485** as the board, the COM port that it enumerated on, and hit upload to test.

- **BlinkOneOutput** \-- Turn 24V O1 (D4) on and off.
- **CycleOutputs** \-- Toggle all pins connected to the 24V output.
- **ReadInputs** \-- Read all 24V input pins and print to [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at a baud rate of `1000000`.
- **ReadInputsToOutputs** \-- Read the inputs and toggle outputs.