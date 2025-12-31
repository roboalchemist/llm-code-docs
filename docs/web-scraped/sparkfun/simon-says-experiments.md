# Source: https://learn.sparkfun.com/tutorials/simon-says-experiments

## Introduction

Now that you\'ve successfully made a [Simon Says board](https://www.sparkfun.com/products/10547) and thoroughly impressed all your friends at home, it\'s time to learn how to change your Simon Says board into your own unique project!! That\'s right, your Simon Says board is capable of doing MUCH more than playing the Simon Says game. It can be re-programmed to do whatever you like. In this tutorial we will:

- Set up your hardware to upload code.
- Set up the free Arduino IDE Software and FTDI drivers on your computer.
- Get some example code onto your Simon Says Board.
- Add a photocell and use Disco Mode!!

For the fourth part of the tutorial, we will show you how you can use your Simon Says board to detect light. This example will require a photocell, a 10K resistor and a soldering iron. However, you can still upload the example code and listen to disco mode (without soldering on the light sensor).

[![Simon Says and Photocell](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/FinalPhotelCellResistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/FinalPhotelCellResistor.jpg)

### Required Materials

In this tutorial, we will show you how to re-program your Simon Says board. We will guide you through setting up the software and hardware. To do this, you will need a PC or Mac. Assuming that you have one of the Simon Says boards soldered, we will require an additional three pieces of hardware to upload code to the microcontroller:

[![SparkFun FTDI Basic Breakout - 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/3/9/5/8/09873-01a.jpg)](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html)

### [SparkFun FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html) 

[ DEV-09873 ]

This is the newest revision of our \[FTDI Basic\](https://www.sparkfun.com/products/retired/8772). We now use a SMD 6-pin heade...

[ [\$18.50] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![SparkFun USB Mini-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/6/9/8/0/11301-01.jpg)](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html)

### [SparkFun USB Mini-B Cable - 6 Foot](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html) 

[ CAB-11301 ]

This is a USB 2.0 type A to Mini-B 5-pin cable. You know, the mini-B connector that usually comes with USB Hubs, Cameras, MP3...

[ [\$5.50] ]

### Required Tools

The following is a recommended list of materials you\'ll need to modify the board.

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

[![SparkFun Safety Glasses](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/0/8/11046-SparkFun_Safety_Glasses-02.jpg)](https://www.sparkfun.com/sparkfun-safety-glasses.html)

### [SparkFun Safety Glasses](https://www.sparkfun.com/sparkfun-safety-glasses.html) 

[ SWG-11046 ]

With these SparkFun Safety Glasses you\'ll have a pair of lightweight, economical, and stylish lenses to protect your precious...

[ [\$5.10] ]

[![Soldering Iron Stand](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/0/7/9477-BST-206-Soldering-Iron-Stand-Feature.jpg)](https://www.sparkfun.com/soldering-iron-stand.html)

### [Soldering Iron Stand](https://www.sparkfun.com/soldering-iron-stand.html) 

[ TOL-09477 ]

This is a simple soldering iron stand composed of a heavy-duty metal base and a reinforced spring holder. The base and holder...

[ [\$7.75] ]

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/voltage-dividers)

### Voltage Dividers 

Turn a large voltage into a smaller one with voltage dividers. This tutorial covers: what a voltage divider circuit looks like and how it is used in the real world.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/photocell-hookup-guide)

### Photocell Hookup Guide 

Hook a light-sensing photocell up to an Arduino to create an ambient light monitor.

[](https://learn.sparkfun.com/tutorials/simon-says-assembly-guide)

### Simon Says Assembly Guide 

No matter what flavor of the Simon Says Through-hole Soldering Kit you\'ve purchased, this tutorial is here to guide you through the entire build process.

## Hardware Assembly

To upload new code to the board, we need a mini-B USB Cable, FTDI basic Breakout, and a 1x6 row from a row of straight male headers.

**Note:** A 3.3V FTDI should be used.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/FTDIUSBCableHeader_5VBlank.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/FTDIUSBCableHeader_5VBlank.png)

If you bought a 40-pin strip of breakaway male headers from the website, you will have to break off a 6-pin section from the larger strip. You can cut these using some pliers, or snap them using your hands by bending the strip at the desired break-point.

[![1x6 Header Broken Off](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/Breakaway1x6.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/Breakaway1x6.jpg)

These 3 items will be the link between your Simon Says board and your computer. First, plug in the 6-pin male header into your FTDI basic board. Make sure to put the longer end of the headers into the FTDI like so:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/FTDIHeaderUpdate1_5VBlank.png "FTDI Header")](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/FTDIHeaderUpdate1_5VBlank.png)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/FTDIHeaderUpdate2_5VBlack.png "FTDI Header Connected")](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/FTDIHeaderUpdate2_5VBlack.png)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, plug in the USB cable into your computer. Then plug the other end into your FTDI basic board. You should notice that the RX and TX leds on the FTDI blink a few times. This indicates that your FTDI is communicating with your computer.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/USBCableFTDIHeaderUpdate1_5VBlank.png "USB FTDI")](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/USBCableFTDIHeaderUpdate1_5VBlank.png)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/USBCableFTDIHeaderUpdate2_5VBlank.png "USB FTDI Connected")](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/USBCableFTDIHeaderUpdate2_5VBlank.png)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** At this step, you may need to install some FTDI Drivers. Check out the software installation section for more information about installing FTDI drivers.

Now you are ready to link your computer to your Simon Says board. First you must find the programming port on your Simon Says board. You will find it near one of the edges of the Simon Says board. It looks like 6x holes with nothing soldered into them. Below shows images of the FTDI header for the PTH and SMD versions.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::                                                                                                                                                                                      | [![](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/SimonSaysSMDFTDIHeader5.png "Simon Says SMD FTDI Header")](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/SimonSaysSMDFTDIHeader5.png) |
| [![](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/SimonSaysPTHFTDIHeader2.png "Simon Says PTH FTDI Header")](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/SimonSaysPTHFTDIHeader2.png) |                                                                                                                                                                                                          |
| :::                                                                                                                                                                                                      |                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *FTDI Header Location for the Simon Says PTH Version.*                                                                                                                                                   | *FTDI Header Location for the Simon Says SMD Version.*                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

To reprogram your board, you are going to push the 6-pin header (that is already plugged into your FTDI board) into this port. You will have to hold it at an angle to cause a temporary connection. You will also need to make sure you align it properly. If you flip your board upside down, then you should see that the holes are labeled with some white ink. Look for the two pins labeled, "GRN" and "BLK". These indicate the proper alignment of your FTDI board so that it is GRN to GRN and BLK to BLK.

[![Align Header with SIMON Programming Header](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/5/FTDISimonSaysProgrammingHeader.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/FTDISimonSaysProgrammingHeader.jpg)

## Software Installation

### Arduino IDE

The Simon Says board is programmable via the Arduino IDE. If this is your first time using an Arduino, please review our tutorial on installing the Arduino IDE.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### FTDI Drivers

If this is your first time using an FTDI, please review our tutorial on installing the FTDI drivers for your operating system.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

June 4, 2013

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

## Uploading to Simon Says

Now that you\'ve got your hardware setup, it\'s time to go back to the Arduino software and re-program your Simon Says Board. Before we can start re-programming there are just a couple settings we need to change in the software.

### Board Selection

First, click **\"Tools\"** from the menu at the top of the window. Then follow the options to select **Tools\>Board\>LilyPad Arduino w/ ATMega328**. This is so that the Arduino program knows that it\'s talking to a Simon Says board (the Simon Says board and this LilyPad have the same chip).

### COM Port Selection

Next, we need to tell Arduino which COM PORT we are going to use. (This is the communication channel that your FTDI breakout board is talking on). To do this, click **Tools\>Serial Port\>COM4**.

**Note**: You may have a different COM PORT option here. Do not select COM1 - your FTDI is not going to be on this COM PORT. Select the option directly below COM1.

### Power

Make sure your Simon Says board\'s \"Power\" switch is flipped to the ON position with batteries.

**Note:** The Simon Says board\'s FTDI header is not directly connected to the Vcc pin of your FTDI. This is why you need to have batteries inserted.

### Upload Button

As shown in the hardware assembly, hold your FTDI in place with the headers touching the plated through holes during upload and click on the "upload button" using any of the example codes provided in this tutorial. The upload button is the circular button at the top of the window with an arrow to the right. As long as there is sufficient contact between the header pins and the plated through holes, the compiled example code will be able to upload to the Simon Says board.

## Example: Blink, Button, or Buzzer

At this point, I would like to mention that any piece of code written in the Arduino IDE (such as the examples in the download above), are more commonly referred to as a \"Sketch\". The sketch is essentially a text document that you are writing and editing code within Arduino. When saving code in the Arduino IDE, it is saved as a \***.ino** file and called a \"Sketch\".

We have written 4 example pieces of code that can be used on the Simon Says Board. You can download them here:

[Simon Says Example Code Download](https://github.com/sparkfun/Simon-Says)

After downloading, unzip the files to your computer.

### Blink

On your Arduino window, click on **File\>Open\...** from the upper menu. Navigate to the folder with the example Simon Says code. This will probably be in your downloads folder similar to this directory: **\"C:\\Users\\\...\\Downloads\\Simon-Says-master\\Simon-Says-master\\Firmware\\Additional Experiments\"**. Since we are testing out the first example, click on the folder labelled *"SIMON_1_BLINK"*. Now double click on the file titled, *"SIMON_1_BLINK.ino"*. This file contains the Sketch (a.k.a. example code).

You should see a new Arduino window pop up with the sketch inside the Arduino IDE\'s editor window. Click on the upload button in the Arduino IDE, give it a few seconds, and you should see a LED begin to blink on your Simon Says board.

If so, congratulations!! You just successfully uploaded a new piece of code to your Simon Says board!!

**Note:** You can read the grey text used throughout the example code. Any text that is gray is known as [comments](https://www.arduino.cc/en/Reference/Comments), and will help you understand the code. Comments are actually ignored by the Arduino program, and will not be programmed onto your Simon Says board. The most important part of all this text is the code found at the bottom of the window. This is the actual code that makes it onto your Simon Says.

### Button

Try opening up the Simon Says experiment example 2. The file is titled, *\"SIMON_2_BUTTON.ino\"*. Upload the code to your board.

Try hitting the buttons. Pressing one of the buttons will change the state of an LED from OFF to ON. The LED will turn OFF after one second until the button is pressed again.

Again, you can read the grey comments to get a better understanding of how the code works. Try experimenting with the code to see if you can change the way the Simon Says board reads the button or turns on the LED. To help you out with hacking the Simon Says, here are a few notes about the pin locations of the Simon Says Plated Through Hole (PTH) version:

[![PTH Simon Button LED Locations](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/SimonSaysPTHTopView.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/SimonSaysPTHTopView.png)

If you happened to get the [Simon Says Surface Mount Device (SMD) version](https://www.sparkfun.com/products/retired/10935), the pin assignments are a little different. Here are the pin locations of the SMD version:

[![SMD Simon Button LED Locations](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/SimonSaysSMDTopView.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/SimonSaysSMDTopView.png)

**Note:** This code is based on the push button example in the SparkFun Inventor\'s Kit. Try looking at the [SIK: Push Buttons](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v33/experiment-5-push-buttons) example for more information.

### Buzzer

Try opening up the other Simon Says experiment example 3. The file is titled, *\"SIMON_3_BUZZER.ino\"*. Upload the code to your board.

Try hitting the buttons. Pressing one of the buttons will light the LED and trigger the buzzer to play a few notes. Make sure that the Sound switch is flipped to the *\"On\"* position.

Again, you can read the grey comments to get a better understanding of how the code works. Try experimenting with the [tone()](https://www.arduino.cc/en/Reference/Tone) function to see if you can change the way the Simon Says board plays a note. If you happened to get the Plated-through Hole (PTH) version: pins 4 and 7 are tied to the buzzer. If you happened to get the Surface Mount Device (SMD) version of the Simon Says, the pin assignments are a little different: pins 3 and 4 are tied to the buzzer.

**Note:** This example code is similar to the piezo buzzer example code in the SparkFun Inventor\'s Kit. Try looking at the [SIK: Using a Piezo Buzzer](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v33/experiment-11-using-a-piezo-buzzer) example for more information.

## Example: Disco Mode!

This part of this tutorial requires a couple more pieces of hardware and a soldering iron.

[![Mini Photocell](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/6/2/09088-02-L.jpg)](https://www.sparkfun.com/mini-photocell.html)

### [Mini Photocell](https://www.sparkfun.com/mini-photocell.html) 

[ SEN-09088 ]

This is a very small light sensor. A photocell changes (also called a \[photodetector\](http://en.wikipedia.org/wiki/Photodetec...

[ [\$1.75] ]

[![Resistor 10k Ohm 1/6th Watt PTH](https://cdn.sparkfun.com/r/140-140/assets/parts/8/3/1/08374-02-L.jpg)](https://www.sparkfun.com/resistor-10k-ohm-1-6th-watt-pth.html)

### [Resistor 10k Ohm 1/6th Watt PTH](https://www.sparkfun.com/resistor-10k-ohm-1-6th-watt-pth.html) 

[ COM-08374 ]

1/6th Watt, +/- 5% tolerance PTH resistor.

[ [\$0.10] ]

Using these parts and a little bit of code, we can detect light. This will be useful in detecting whether the lights are ON or OFF in a room. In the Disco Mode example code, we will have the Simon Says board only go into Disco Mode when the lights are off -- when it\'s time to get your boogie on!

First off, let\'s take a look at the two components. Do you recognize that resistor from building your Simon Says? It\'s the exact same component you soldered into place when you built up your kit!!

Next, let\'s take a look at the schematic for the light sensing circuit! Don\'t be scared -- it\'s actually quite simple! A [schematic](https://learn.sparkfun.com/tutorials/how-to-read-a-schematic) is a drawing that represents physical things. It shows us how we are going to connect the two components to the Simon Says board. The green lines represent "nets" or connections. The other symbols represent actual things (like the photocell and resistor). The last three things in the schematic represent pin-outs on the Simon Says board. (GND, A0, and 5V).

[![Voltage Divider](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/PhotoCellVoltageDivider.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/PhotoCellVoltageDivider.jpg)

Let\'s find these 3 holes on the Simon Says board. They are located on the bottom side underneath one of the batteries.

[![Analog Connection on Simon Says](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/A05VGNDPins_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/A05VGNDPins_1.jpg)

Next, let\'s twist the Photocell and resistor together in a way that will work with the schematic. Notice in the schematic how A0 is actually connected to both the photocell and the resistor. In order to solder this connection, it is helpful to twist one leg of the photocell and one leg of the resistor together. Make sure that there is enough room to insert the twisted pins into analog pin A0 before soldering.

Now we have essentially 3 legs that will solder into 3 pinouts on the Simon Says. Before we begin to solder, please check out this picture below that shows how the legs should connect to the Simon Says.

[![Twist and Connect Photoresistor && Resistor](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/A05VGNDPinsPhotoCellResistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/A05VGNDPinsPhotoCellResistor.jpg)

Notice how 5V and A0 are going to have to overlap. Be sure to remove your batteries before you start [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering). When you are finished soldering them into place, it should look something like this:

[![Soldered Connection](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/A05VGNDPinsPhotoCellResistorSoldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/A05VGNDPinsPhotoCellResistorSoldered.jpg)

You can bend it around the edge so that the photocell is facing up and will do a better job of detecting the light. Like so:

[![Bend Upward](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/FinalPhotelCellResistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/5/FinalPhotelCellResistor.jpg)

You are almost ready to upload the Disco Mode Code! First, put your batteries back in and turn your board ON. Then open up the Arduino Software and open *\"SIMON_DISCO_MODE.ino\"*. While holding your FTDI in place, click the upload button.

After the code is on there, try killing the lights and see if disco mode starts up!! If so, congratulations! You have just successfully completed your first embedded electronics project!

## Default Simon Says Game

If you\'d like to get your Simon Says back to playing the original game, head to the directory **\"\.../Simon-Says/Firmware/Simon_Says\"**. The *\"Simon_Game_Code.ino\"* will have the same default example code that we pre-program the chips with before they are packaged up in the kit. Make sure that the *\"hardware_versions.h\"* and *\"pitches.h\"* files are in the same folder when uploading.