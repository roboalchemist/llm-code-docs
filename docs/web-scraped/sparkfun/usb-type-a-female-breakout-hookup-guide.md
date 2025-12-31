# Source: https://learn.sparkfun.com/tutorials/usb-type-a-female-breakout-hookup-guide

## Introduction

If you have a microcontroller that can act as a USB host, then you will need a way to plug in USB cables and devices. The [USB Type A Female Breakout](https://www.sparkfun.com/products/12700) accepts a [Type A USB plug](http://en.wikipedia.org/wiki/USB#Host_and_Device_interface_receptacles) on one end and breaks out the 4 USB lines to a standard 0.100 inch header.

[![SparkFun USB Type A Female Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/9/4/4/0/12700-01.jpg)](https://www.sparkfun.com/sparkfun-usb-type-a-female-breakout.html)

### [SparkFun USB Type A Female Breakout](https://www.sparkfun.com/sparkfun-usb-type-a-female-breakout.html) 

[ BOB-12700 ]

This simple board breaks out a female USB type A connector\'s VCC, GND, D- and D+ pins to a 0.1\" pitch header. If you want to ...

[ [\$5.25] ]

NOTE: This tutorial uses the [mbed](http://mbed.org/) [LPC1768](https://www.sparkfun.com/products/9564), as it has a built-in USB host. However, the breakout board can be used for any platform that has a USB host.

### Covered In This Tutorial

In this tutorial, we will use the [mbed LPB1768](https://www.sparkfun.com/products/9564) and the [USB Type A Female Breakout](https://www.sparkfun.com/products/12700) to create a simple circuit that accepts a USB keyboard and prints pressed keys to a serial console.

### Required Materials

- [USB Type A Female Breakout](https://www.sparkfun.com/products/12700)
- [LPC1768](https://www.sparkfun.com/products/9564)
- [Male PTH headers](https://www.sparkfun.com/products/116)
- 2x 15kΩ resistors (if you don\'t have any, [10kΩ resistors](https://www.sparkfun.com/products/8374) will work for this)
- 5x [Jumper wires](https://www.sparkfun.com/products/11026) to connect from breadboard to Arduino.
- [Breadboard](https://www.sparkfun.com/products/9567) to tie everything together.
- USB Keyboard

### Suggested Reading

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [Getting started with the LPC1768](https://mbed.org/handbook/mbed-NXP-LPC1768-Getting-Started)

## Board Overview

The board is a simple breakout for USB lines.

[![USB Type A Female Breakout Board](https://cdn.sparkfun.com/assets/5/d/2/2/6/52f29ce3ce395f960b8b4567.jpg)](https://cdn.sparkfun.com/assets/5/d/2/2/6/52f29ce3ce395f960b8b4567.jpg)

*USB Type A Female Breakout front*

**GND** should be connected to the ground of the host circuit.

**D+** and **D-** are the differential pair lines for USB. They should be connected to D+ and D-, respectively, of the host circuit. Additionally, a 15kΩ pull-down resistor is needed on each D+ and D-.

**VCC** needs to be connected to a 5V supply (which could come from the host circuit, if available).

### Board Dimensions

The board is 1.00\" x 0.80\" with four mounting holes by each corner.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/c/8/8/f/c/SparkFun_USB_Type_A_Female_Breakout_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/c/8/8/f/c/SparkFun_USB_Type_A_Female_Breakout_Board_Dimensions.png)

## Hookup Example

### Assembly

To connect the USB breakout board, [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the [break away headers](https://www.sparkfun.com/products/116) to the 4 header holes on the board.

[![Header pins soldered onto USB Type A Female Breakout](https://cdn.sparkfun.com/r/600-600/assets/7/7/5/e/1/52f29ce5ce395f640a8b456d.jpg)](https://cdn.sparkfun.com/assets/7/7/5/e/1/52f29ce5ce395f640a8b456d.jpg)

*PTH headers on the USB breakout board*

### Connecting the USB Breakout Board

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/1/3/c/e/d/52f3c319ce395f904a8b4569.png)](https://cdn.sparkfun.com/assets/1/3/c/e/d/52f3c319ce395f904a8b4569.png)

*Basic hookup using an mbed LPC1768 and a breadboard*

For the LPC1768, make the following connections with jumper wires:

(USB Breakout → LPC1768)

- VCC → VU
- D- → D-
- D+ → D+
- GND → GND

Additionally, add 2 15kΩ pull-down resistors on the D+ and D- lines. Attach one resistor from D+ to GND, and attach another from D- to GND.

[![Completed mbed LPC1768 and USB breakout circuit](https://cdn.sparkfun.com/r/600-600/assets/a/c/7/6/6/52f29ce5ce395fa50a8b456b.jpg)](https://cdn.sparkfun.com/assets/a/c/7/6/6/52f29ce5ce395fa50a8b456b.jpg)

*USB Type A Female Breakout added to the mbed LPC1768*

## Example Code

We will use the mbed online editor and compiler for this example. First, navigate to [mbed.org](mbed.org), and login or create a profile.

[![mbed login](https://cdn.sparkfun.com/r/600-600/assets/4/8/f/d/a/52f1291bce395f7c248b4567.png)](https://cdn.sparkfun.com/assets/4/8/f/d/a/52f1291bce395f7c248b4567.png)

Once logged in, go to the [Handbook Homepage](http://mbed.org/handbook/Homepage), which contains all of the official mbed libraries.

[![mbed Handbook](https://cdn.sparkfun.com/r/600-600/assets/4/d/1/f/9/52f1291ace395f46228b4568.png)](https://cdn.sparkfun.com/assets/4/d/1/f/9/52f1291ace395f46228b4568.png)

Scroll down to find the [USB Host Keyboard library](http://mbed.org/handbook/USBHostKeyboard) under \"Communication Interfaces.\"

[![mbed USB Host Keyboard library](https://cdn.sparkfun.com/r/600-600/assets/0/7/e/2/c/52f12910ce395fac208b4568.png)](https://cdn.sparkfun.com/assets/0/7/e/2/c/52f12910ce395fac208b4568.png)

Click the \"Import Program\" button to load the library and example program into the online compiler.

[![mbed import program](https://cdn.sparkfun.com/r/600-600/assets/1/5/3/0/7/52f12914ce395f88218b4567.png)](https://cdn.sparkfun.com/assets/1/5/3/0/7/52f12914ce395f88218b4567.png)

Make sure you have \"Program\" selected from \"Import As:\", as we want to use the example program (select \"Library\" if you plan to write your own program using the library).

[![importing example mbed program](https://cdn.sparkfun.com/r/600-600/assets/9/0/b/b/3/52f128fece395fae208b4567.png)](https://cdn.sparkfun.com/assets/9/0/b/b/3/52f128fece395fae208b4567.png)

In the \"Program Workspace,\" select the \"USBHostKeyboard_HelloWorld\" folder and click \"Compile\" at the top. This will automatically compile the program and download a binary (.bin file) to your computer.

[![mbed compile USB keyboard example](https://cdn.sparkfun.com/r/600-600/assets/d/9/d/5/8/52f1291ace395f2c218b4567.png)](https://cdn.sparkfun.com/assets/d/9/d/5/8/52f1291ace395f2c218b4567.png)

Plug in the mbed microcontroller to your computer using a USB cable. The mbed should enumerate as a USB mass storage device. If you are using Windows, it will appear as if you plugged in a thumb drive.

Find where you downloaded the compiled .bin file and copy it to the root directory of your mbed device.

[![mbed copying compiled program](https://cdn.sparkfun.com/r/600-600/assets/0/4/c/9/8/52f12910ce395fc4228b4567.png)](https://cdn.sparkfun.com/assets/0/4/c/9/8/52f12910ce395fc4228b4567.png)

Press the reset button on the mbed system. This will reboot the mbed and load the .bin file to be immediately executed.

In addition to enumerating as a mass storage device, the mbed also has a built-in COM port. If you are on Windows, open up the Device Manager and locate the mbed Serial Port\'s COM number.

[![mbed COM port](https://cdn.sparkfun.com/r/600-600/assets/2/f/b/4/f/52f128fece395fa7218b4567.png)](https://cdn.sparkfun.com/assets/2/f/b/4/f/52f128fece395fa7218b4567.png)

Start the serial program of your choice (I will use [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) for this example) and select the COM port correseponding to the mbed device. Use 9600 baud, and click \"Open.\"

[![Configure PuTTY for the mbed](https://cdn.sparkfun.com/assets/3/a/1/0/9/52f128efce395fad208b4568.png)](https://cdn.sparkfun.com/assets/3/a/1/0/9/52f128efce395fad208b4568.png)

Once you establish a Serial connection to the mbed, you will be presented with a blank console.

[![blank Serial console](https://cdn.sparkfun.com/assets/4/6/8/2/b/52f128fece395f1d238b4567.png)](https://cdn.sparkfun.com/assets/4/6/8/2/b/52f128fece395f1d238b4567.png)

Plug in a USB keyboard to the USB Type A Female Breakout Board.

[![mbed LPC 1768 and USB keyboard](https://cdn.sparkfun.com/r/600-600/assets/d/4/1/2/e/52f29ce5ce395f070b8b456a.jpg)](https://cdn.sparkfun.com/assets/d/4/1/2/e/52f29ce5ce395f070b8b456a.jpg)

The Serial console should show the keyboard being enumerated. You can type, and keystrokes will appear in the console. If you unplug the keyboard, you should see a \"disconnected\" message.

**IMPORTANT**: Only letters and numbers are supported in this example program. Additionally, the program cannot discern multiple keystrokes (for example, if you hold \'1\', press \'2\', let go of \'2\', and let go of \'1\', you\'ll see \"111\" printed).

[![Testing the mbed USB keyboard program](https://cdn.sparkfun.com/assets/1/5/7/0/5/52f1291bce395f6e238b4567.png)](https://cdn.sparkfun.com/assets/1/5/7/0/5/52f1291bce395f6e238b4567.png)