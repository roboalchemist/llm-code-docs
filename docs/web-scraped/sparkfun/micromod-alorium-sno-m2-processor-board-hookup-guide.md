# Source: https://learn.sparkfun.com/tutorials/micromod-alorium-sno-m2-processor-board-hookup-guide

## Introduction

The [MicroMod Alorium Sno M2 Processor Board](https://www.sparkfun.com/products/18030) features the Snō System on Module (SoM) from Alorium Technology adapted to the MicroMod M.2 processor form factor. Snō\'s FPGA provides a reconfigurable hardware platform that hosts an 8-bit AVR instruction set, compatible with the ATmega328, making Snō fully compatible with the Arduino IDE. Snō SoM has a compact footprint, making it ideal for space-constrained applications and an obvious addition to our MicroMod form factor for prototyping.

Alorium Technology provides a library of custom logic called Xcelerator Blocks (XBs) through the Arduino IDE that accelerate specific functionality that is slow, problematic, or even impossible for an 8-bit microcontroller. This library includes XBs such as Servo Control, Quadrature, Floating Point Math, NeoPixel, and Enhanced Analog-to-Digital Converter. Alorium also notes a XB roadmap where future XBs will be implemented based on feedback from early adopters and new potential customers.

[![SparkFun MicroMod Alorium Sno M2 Processor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/2/5/8/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-alorium-sno-m2-processor.html)

### [SparkFun MicroMod Alorium Sno M2 Processor](https://www.sparkfun.com/sparkfun-micromod-alorium-sno-m2-processor.html) 

[ DEV-18030 ]

The SparkFun MicroMod Alorium Sno Processor features the Snō System on Module (SoM) adapted to the MicroMod M.2 processor fo...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![SparkFun MicroMod ATP Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/1/2/16885-SparkFun_MicroMod_ATP_Carrier_Board-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html)

### [SparkFun MicroMod ATP Carrier Board](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html) 

[ DEV-16885 ]

If you need a \"lot\" of GPIO with a simple to program, ready to go to market module, the ATP is the fix you need.

[ [\$20.50] ]

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

[![SparkFun MicroMod Alorium Sno M2 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/2/5/8/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-alorium-sno-m2-processor.html)

### [SparkFun MicroMod Alorium Sno M2 Processor](https://www.sparkfun.com/sparkfun-micromod-alorium-sno-m2-processor.html) 

[ DEV-18030 ]

The SparkFun MicroMod Alorium Sno Processor features the Snō System on Module (SoM) adapted to the MicroMod M.2 processor fo...

**Retired**

### Suggested Reading

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/micromod). We recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)   [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*                                                                                                                                        *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you aren't familiar with the following concepts, we also recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[](https://learn.sparkfun.com/tutorials/how-does-an-fpga-work)

### How Does an FPGA Work? 

The What, How, Why, and When of Field Programmable Gate Arrays, aka FPGAs

[](https://learn.sparkfun.com/tutorials/micromod-all-the-pins-atp-carrier-board)

### MicroMod All The Pins (ATP) Carrier Board 

Access All The Pins (ATP) of the MicroMod Processor Board with the Carrier Board!

## Hardware Overview

### M.2 Connector

All of our MicroMod Processor Boards come equipped with the **M.2 MicroMod Connector**, which leverages the [M.2 standard](https://en.wikipedia.org/wiki/M.2) and specification to allow you to install your MicroMod Processor Board on your choice of carrier board. Most of the pins use a common pinout to ensure cross platform compatibility.

[![M.2 Edge Connector Pins Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-M2Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-M2Connector.jpg)

### Alorium Technology Sno M2 Processor

The Alorium Technology Sno FPGA provides a reconfigurable hardware platform that hosts an ATmega328 instruction set compatible microcontroller. The FPGA also provides the ability to implement custom logic that accelerates specific functionality that is slow, problematic or even impossible for an 8-bit microcontroller.

[![The Alorium Sno Processor is the giant chip in the middle of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-Processor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-Processor.jpg)

### JTAG

The JTAG interface on Sno M2 is primarily used during manufacturing to load the production FPGA image. For advanced users, JTAG can be used for creating bare-metal FPGA designs and directly flashing a new image to the FPGA.

[] **Important Note:** Using JTAG to load the MAX10 FPGA with a custom image will erase the production Sno M2 functionality, permanently delete the integrated 8-bit microcontroller subsystem, and not allow recovery back to the factory production image.\
\
The Sno M2 FPGA has been designed to be modified and extended by using Alorium's OpenXLR8 Methodology. This flow provides a path to create custom XBs in the FPGA fabric that can easily interface to the on-chip microcontroller and preserve full factory functionality.\
\
[Learn More about OpenXLR8 here.](https://www.aloriumtech.com/openxlr8)

[![JTAG is highlighted on the upper left corner of the MicroMod board, with the M.2 connectors facing down. ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-JTAG.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-JTAG.jpg)

### FTDI

The FTDI facilitates USB communication - drivers for the FTDI chip may need to be installed. Please see the [How to Install FTDI drivers tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) if you need help installing these drivers.

[![FTDI chip is highlighted - it is the small square chip on the lower right side of the front of the board when the M2 connector is pointing down](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-FTDI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-FTDI.jpg)

### LEDs

There are two LEDs on the Sno Processor Board. An RX LED and a STAT LED.

[![The RX LED is along the upper left side of the board, the STAT LED is on the upper right side of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-BothLEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/18030-SparkFun_MicroMod_Alorium_Sno_Processor_Board-BothLEDs.jpg)

- **RX LED** - The RX LED indicates activity on the USB serial port.

- **STAT LED** - A STAT LED is added to the top side of the board. This is useful debugging or as a status indicator.

### MicroMod Alorium Sno M2 Processor Pin Functionality

The complete pin map is shown here or you can refer to the [schematic](https://cdn.sparkfun.com/assets/5/c/6/9/0/18030_MicroModAloriumSnoPB_Schematic.pdf). You can also download the PDF version of the pin map [here](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/PinOutMap.pdf).

[![Alorium\'s pin map](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/AloriumSnoM2PinMap.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/AloriumSnoM2PinMap.png)

*Click on image for a closer view of the pin map.*

*Pin Map courtesy of Alorium Technology*

### Board Dimensions

The board takes advantage of the standard MicroMod form factor.

[![Board Measures 1\" x 1\"](https://cdn.sparkfun.com/r/600-600/assets/4/d/2/7/3/18030_MicroModAloriumSnoPB_BoardOutline_Cropped.png)](https://cdn.sparkfun.com/assets/4/d/2/7/3/18030_MicroModAloriumSnoPB_BoardOutline_Cropped.png)

## Hardware Assembly

If you have not already, make sure to check out the [Getting Started with MicroMod: Hardware Hookup](https://learn.sparkfun.com/tutorials/getting-started-with-micromod#hardware-hookup) for information on inserting your Processor Board into your Carrier Board.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

October 21, 2020

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

After inserting the MicroMod Alorium Sno M2 processor board into a carrier board, your setup may look like the following.

[![MicroMod Alorium Sno M2 Inserted Into a Carrier Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/MicroMod_Alorium_Sno_Processor_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/MicroMod_Alorium_Sno_Processor_Hookup_Guide-03.jpg)

*Click on image for a closer view.*

Go ahead and secure the Processor Board by gently pressing it down and tightening the screw (not too much though).

[![Screwing down the processor board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/MicroMod_Alorium_Sno_Processor_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/MicroMod_Alorium_Sno_Processor_Hookup_Guide-02.jpg)

*Click on image for a closer view.*

For simplicity, we\'ll be using the MicroMod ATP Carrier Board to program the board. At a minimum, your setup should look like the image below with the MicroMod Alorium Sno M2 Processor Board.

[![MicroMod Sno Alorium in ATP Carrier](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/MicroMod_Alorium_Sno_Processor_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/MicroMod_Alorium_Sno_Processor_Hookup_Guide-01.jpg)

*Click on image for a closer view.*

## Software Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Install Arduino Board Definitions

In your Arduino IDE menu bar, go to **File** \> **Preferences** and locate the 'Additional Boards Manager URLs' input field. Paste the following URL into the "Additional Boards Manager URLs" input field:

    language:json
    https://raw.githubusercontent.com/AloriumTechnology/Arduino_Boards/master/package_aloriumtech_index.json

It should look something like the following:

[![Adding Alorium link to Preferences](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/ArduinoPreferences.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/ArduinoPreferences.png)

*Click on image for a closer view.*

### Install Alorium\'s XLR8 Board Package

Start by going to **Tools** \> **Board** \> **Boards Manager**. Type "Alorium," in the search field and you will see an option to install board files for Alorium Arduino compatible boards. Select the "Alorium XLR8 Boards" package and then click "Install".

[![Type in Alorium, and you should see Alorium XLR8 Family package. Install that. ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/AloriumXLR8FamilyPackage-Updated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/AloriumXLR8FamilyPackage-Updated.png)

*Click on image for a closer view.*

Go to **Tools** \> **Board**. You should see that a new section titled "Alorium XLR8 Family" now exists. Under this new heading should be the **Sno M2** board. You can select the \"Sno M2\" board just like you would normally select the "Arduino/Genuino Uno" board.

[![Choosing the M2 Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/ChooseXLR8Board-Correct.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/ChooseXLR8Board-Correct.png)

*Click on image for a closer view.*

After selecting the Sno M2, you will find a new menu item at **Tools** \> **FPGA Image**, where you will find a number of FPGA images that provide different operating speeds and different XB configurations.

[![Choosing FPGA Image](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/ChooseFPGA-Correct.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/ChooseFPGA-Correct.png)

*Click on image for a closer view.*

### XLR8 Libraries

Installing the XLR8 board support will also install a default set of libraries that are needed to take advantage of the extra capabilities of Snō. You can see these libraries listed in the **Sketch** \> **Include Library** menu.

There are additional libraries available that can be installed using the Library Manager. In the Arduino IDE, go to the menu **Sketch** \> **Include Library** \> **Manage Libraries**, which will open the Library Manager in a new window. Enter \"Alorium\" in the search bar and you will find the entries for the various XLR8 and Snō libraries available.

There are many libraries you can install to support a variety of our board functions and Xcelerator Blocks. For the purposes of this getting started guide, find the "XLR8Info" library and click on it.

[![Install XLR8Info Library](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/InstallXLR8InfoLibrary.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/InstallXLR8InfoLibrary.png)

*Click on image for a closer view.*

An **Install** button will appear for it. Click on the **Install** button, and when the installation is complete you will see that the library is now tagged as Installed.

After adding the library, you'll find it in the menu **Sketch** \> **Include Library**, under Contributed Libraries (You may need to re-start the IDE if you don't see it).

You'll also find some examples sketches in the **File** \> **Examples** menu, under the library name.

## Example 1: Blink

With the Sno Processor Board inserted into the M.2 slot and secured, plug your ATP board to your computer with a USB cable. Make sure you have the correct Board, FPGA Image, Upload Action, and Port as you see below.

[![Sno M2 board selected, 16MHz FPGA Image, and Send sketch to Snow M2 USB, are selected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/ChooseFPGA-Correct.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/ChooseFPGA-Correct.png)

*Click on image for a closer view.*

Go to **Tools** \> **Board** and select the Sno M.2. Then go to **File** \> **Examples** \> **01. Basics** and select *Blink*.

[![Select the Blink Example from the basics menu](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/BlinkExample-Updated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/BlinkExample-Updated.png)

*Click on image for a closer view.*

Upload the sketch as you see here:

[![Smash that upload button](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/BlinkUpload.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/BlinkUpload.png)

*Click on image for a closer view.*

If all goes well, you should see something like the gif below:

[![LED on the processor board should be blinking](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/MM_Sno_Alorium.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/MM_Sno_Alorium.gif)

## Example 2: Running with an Xcelerator Block (XB)

To run with the XLR8Info XB and library, do the following:

Connect Snō to your computer with a USB cable, and set up the Port and Serial Monitor as you normally would. Go to **Tools** \> **Port** and verify that Arduino IDE is connected to the XLR8 USB serial port.

Go to **Tools** \> **Board** and select the XLR8 board. Then go to **File** \> **Examples** \> **XLR8Info** and select \"GetXLR8Version\".

[![Find Examples, then XLR8Info, then GetXLR8Version](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/GetXLR8InfoExampleMenu.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/GetXLR8InfoExampleMenu.jpg)

*Click on image for a closer view.*

\
\

In the GetXLR8Version sketch window, click on the Upload button

[![Upload Button](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/UploadExample.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/UploadExample.png)

*Click on image for a closer view.*

Check the Serial Monitor window for the output, which should look like the output below. **Note that you will need to set the baud rate for the Serial Monitor to 115200 for this sketch to display output correctly**.

[![Get Info Example Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/7/GetInfoExampleOutput.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/7/GetInfoExampleOutput.jpg)

*Click on image for a closer view.*

## Troubleshooting

### General Troubleshooting Help & Technical Support

[] **Not working as expected and need help?**\
\
If you need technical assistance or more information regarding this or another SparkFun product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums: MicroMod](https://forum.sparkfun.com/viewforum.php?f=180) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[SparkFun Forums: MicroMod](https://forum.sparkfun.com/viewforum.php?f=180)