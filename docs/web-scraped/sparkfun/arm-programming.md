# Source: https://learn.sparkfun.com/tutorials/arm-programming

## Introduction

**Heads up!** This tutorial was written for ARM microcontrollers with SWD or JTAG pins. You will need a dedicated programmer (i.e. [J-Link EDU Mini](https://www.sparkfun.com/products/15345) or [J-Link EDU Base](https://www.sparkfun.com/products/15346)) to connect to the port. If you are using an AVR microcontroller with an Arduino bootloader using ICSP pins, you\'ll need to head on over to the [Installing an Arduino Bootloader](https://learn.sparkfun.com/tutorials/installing-an-arduino-bootloader) tutorial.

SparkFun has been a fan of Arduino for a long time. We\'ve programmed ATMega328s (and 168s, and 8s before that), written tutorials, and hacked all sorts of fun projects. But now the market is maturing and we are looking at a lot more ARM chips. One advantage of the newer chips is that they generally do not need a USB-to-serial adapter; instead they have USB built in (at least the ones we are using do). You still need to add a bootloader to use them with Arduino, and since ARM programmers are also a little more complicated than AVR programmers you\'ll want to invest in a stand alone programmer instead of trying to use the Uno you have laying around.

[] **Please Note:** Most SparkFun boards come pre-programmed. This tutorial is meant to provide information if you wish to re-program your board or change the bootloader.

A few ARM boards:

  ------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/parts/7/5/9/2/11589-01d.jpg)](https://www.sparkfun.com/products/11589)   [![](https://cdn.sparkfun.com/assets/parts/1/3/1/4/6/14870-Arduino_MKR_Vidor_4000-01.jpg)](https://www.sparkfun.com/products/14870)   [![](https://cdn.sparkfun.com/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/products/14812)   [![](https://cdn.sparkfun.com/assets/parts/1/1/0/9/2/13664-01.jpg)](https://www.sparkfun.com/products/13664)   [![](https://cdn.sparkfun.com/assets/parts/1/2/9/2/7/14713-SparkFun_Thing_Plus_-_SAMD51-04.jpg)](https://www.sparkfun.com/products/14713)
  *[The Due:](https://www.sparkfun.com/products/11589) Arduino\'s first ARM board*                              *[MKR Vidor 4000:](https://www.sparkfun.com/products/14870) One of Arduino\'s newer Arm boards*                                       *[RedBoard Turbo:](https://www.sparkfun.com/products/14812) One of SparkFun\'s newer boards*                                                                       *[SAMD21 Dev Mini:](https://www.sparkfun.com/products/13664) One of SparkFun\'s ARM boards*                    *[SAMD51 Thing Plus board:](https://www.sparkfun.com/products/14713) SparkFun\'s newest ARM board*
  ------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though, depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/pcb-basics)

### PCB Basics 

What exactly IS a PCB? This tutorial will breakdown what makes up a PCB and some of the common terms used in the PCB world.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-bootloader)

### Installing an Arduino Bootloader 

This tutorial will teach you what a bootloader is and why you would need to install or reinstall it. We will also go over the process of burning a bootloader by flashing a hex file to an Arduino microcontroller.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/integrated-circuits)

### Integrated Circuits 

An introduction to integrated circuits (ICs). Electronics\' ubiquitous black chips. Includes a focus on the variety of IC packages.

## What is an ARM?

Let\'s start with what an ARM processor is. They are used in everything from the Redboard Turbo to the Raspberry Pi to most cellphones, but that\'s a large range of performance. ARM is actually a unique business model. [Arm Holdings](https://www.arm.com/) does the design work for the cores and holds the patents/copyright/other legal things and then licenses the design out. The cores are then put into CPUs, microcontrollers, SOCs (System on Chip), etc. A company might decide they want to build a camera that uses the ARM core. They can license the core, maximize power efficiency, add some silicone for the camera sensor interface, and build the entire system onto a chip.

If you look around you\'ll actually see quite a few naming conventions. The v7 architectures lists 3 different profiles:

- **Cortex-A**: the Application profile
- **Cortex-R**: the Real-time profile
- **Cortex-M**: the Microcontroller profile

We are going to be looking at Cortex-Ms. The Cortex M0/M0+ and M1 are actually from the v6 architecture and can be considered a subset for the v7 profile. All that to say that we are going to be looking at programming the SamD21 on our Redboard Turbo (and other boards) as well as the SamD51 on the Thing Plus. The SAMD21 is an ARM Cortex-M0, where the SAMD51 is an ARM Cortex-M4F.

## Bootloaders

A bootloader is a small piece of code that looks at the programming port (in this case USB) to see if there is new code coming in. If there is, then it takes the code and puts it in a predetermined location. If there isn\'t, then it runs the code currently at that location.

Most Arduino boards have a bootloader that allows us to upload code over a USB port (or UART Serial connection). This way, once the bootloader is installed, we can program the board much easier. But sometimes we want to change the function of the bootloader, install a bootloader on a brand new board, or just skip the bootloader and install our code directly (makes it harder for other people to change the code on, say, a commercial product).

The bootloader we recommend using is the UF2 bootloader. You can go [here for more information on UF2 bootloaders](https://makecode.com/blog/one-chip-to-flash-them-all), or click on the button below to go to SparkFun\'s SAMD Bootloaders GitHub Repo:

[SparkFun SamD UF2 bootloaders](https://github.com/sparkfun/Arduino_Boards/tree/master/sparkfun/samd/bootloaders)

\
UF2 is a file format designed by Microsoft that stands for USB Flashing Format. This format was designed for PXT (also known as Microsoft MakeCode) and allows for programming boards over the Mass Storage Class (removable drive). The bootloader is also compatible with BOSSA which is what the Arduino IDE uses. In other words, UF2 lets you write MakeCode, use Circuit Python, and use the Arduino IDE, all in one bootloader.

Whether you use the UF2 bootloader or another bootloader, you\'re going to have to download the file. Make sure the file you download is compatible with the board/configuration you are using. Check out our [GitHub Respository](https://github.com/sparkfun/Arduino_Boards/tree/master/sparkfun/samd/bootloaders) for the SAMD bootloaders; the Turbo bootloader should work with these boards (you want the **\*.bin** file).

## JTAG and SWD

### Joint Test Action Group

**JTAG** stands for **Joint Test Action Group** (the group who defined the JTAG standard) and was designed as a way to test boards. JTAG allows the user to talk to the bits and pieces of the microcontroller. In many cases, this involves giving them a set of instructions or programming the board. The JTAG standard defines 5 pins:

- **TCK**: Test Clock
- **TMS**: Test Mode Select
- **TDI**: Test Data-In
- **TDO**: Test Data-out
- **TRST**: Test Reset *(Optional)*

The reduced pin count JTAG definition really only consists of 2 pins:

- **TMSC**: Test Serial Data
- **TCKS**: Test Clock

The 20 pin connector you see on some programmers was designed for JTAG and all those extra pin can be used for power, ground, and other things. While JTAG does not define a physical pin layout, there are a few common options. The 20 pin connector you see on Segger\'s J-Link EDU Base and Base Compact programmer is a good example.

[![JTAG Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/JTAG_Pinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/JTAG_Pinout.png)

### Serial Wire Debug

**Serial Wire Debug (SWD)** is really just a modification/implementation of JTAG specifically for ARM processors. SWD puts the 2 pins (SWDIO and SWCLK) on top of the JTAG pins allowing a user to use either JTAG or SWD without the need to breakout more pins.

[![SWD Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/SWD_Header.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/SWD_Header.png)

## Programmers and J-Link Software

There are a few different ARM programmers from Segger. If you are just getting started and don\'t plan on making any money off your project, then the EDU Mini is a great place to start. If you want something a bit more powerful, the J-Link Base EDU is a good option. If you are planning on making money, you cannot use the EDU versions, in which case I recommend the Base Compact that we carry. This is the cheapest Segger ARM programmer without an EDU license. There are plenty of higher end programmers as well, but based on their price, you are only going to grab those if you know exactly what features you need from them. But don\'t worry, all these are more than capable of programming our boards.

[![Segger J-Link EDU Mini](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/4/0/2/24078-J-Link-Mini-Feature.jpg)](https://www.sparkfun.com/segger-j-link-edu-mini.html)

### [Segger J-Link EDU Mini](https://www.sparkfun.com/segger-j-link-edu-mini.html) 

[ PGM-24078 ]

The J-Link EDU Mini is a stripped-down, budget-friendly model of the J-Link debug probe created for educational use.

[ [\$60.00] ]

[![J-Link EDU Base Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/3/15346-J-Link_EDU_Base-01.jpg)](https://www.sparkfun.com/products/15346)

### [J-Link EDU Base Programmer](https://www.sparkfun.com/products/15346) 

[ PGM-15346 ]

J-Link programmer for programming any ARM microconroller. Comes with an educational/ non-commercial license.

**Retired**

[![J-Link BASE Compact Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/4/15347-J-Link_Base_Compact-01.jpg)](https://www.sparkfun.com/products/15347)

### [J-Link BASE Compact Programmer](https://www.sparkfun.com/products/15347) 

[ PGM-15347 ]

Compact J-Link programmer for programming any ARM microconroller.

**Retired**

First step is to [download the J-Link Software](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack). This software is good for updating the firmware on the programmers. Go ahead and open the Jlink Configurator and see if your programmer needs an update. The J-Link Software packages has a lot of features you can dig into, but we aren\'t going to use them. Feel free to play around and explore the software and all the debugging has to offer.

[J-Link Software Download Page](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack)

## Hardware Hookup

Now it\'s time to hook things up. We will need to make sure that SWCLK and SWDIO are both connected to the microcontroller. On some of our larger boards, like the SAMD21 Dev board and the RedBoard Turbo, we managed to get the full 10 pin header. Our footprint shows a small dash where pin 1 goes. If you check the pinout above you\'ll notice that the notch goes on the same side as pin 1. You will probably want a [2x5 header](https://www.sparkfun.com/products/15362) to connect the cable to the board (you can either solder it on, or hold it on securely while programming).

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10 Pin Headers on Various SparkFun Boards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+=================================================================================================================================================================================+==========================================================================================================================================================================================+==============================================================================================================================================================================+
| [![SAMD21 Mini Programming Header](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/SamD21Mini.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/SamD21Mini.png) | [![SparkFun Turbo Programming Header](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/RedboardTurbo.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/RedboardTurbo.png) | [![SAMD21 Dev Programming Header](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/SamD21Dev.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/SamD21Dev.png) |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *SAMD21 Mini*                                                                                                                                                                   | *RedBoard Turbo*                                                                                                                                                                         | *SAMD21 Dev*                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

On other boards such as the ProRF or the SAMD51 Thing Plus you may have to dig into the schematic or board files to find the test points. There is at least one test point on all our boards since we program the boards after they are assembled and need access to them. Programming these might be a bit trickier without a jig, but I recommend holding a pair of jumper wires against the pads while uploading. It should only take a few seconds to program, but might be tricky and require an extra pair of hands.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Test Pads on the SparkFun SAMD51 Thing Plus Board                                                                                                                                                                                                                                                                                                                             |
+=====================================================================================================================================================================+=========================================================================================================================================================================================================+
| [![](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/SamD51_SWDIO_SWDCLK.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/SamD51_SWDIO_SWDCLK.png) | [![](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/14713-SparkFun_Thing_Plus_-_SAMD51-03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/14713-SparkFun_Thing_Plus_-_SAMD51-03.png) |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *SAMD51 Board with SWDIO above MISO and SWDCLK below MIOS*                                                                                                          | *Back of SAMD51 board showing the 2 testpads*                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Tip:** Try soldering pins from jumper wires, thin solid core wires, or 0Ω resistors to connect to the test points. We use this trick to [program an AVR microcontroller with ICSP pins broken out on test pads](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#connect-by-solder) similar like the image shown below.\
\

[![AVR microcontroller being reprogrammed with the help of jumper wires](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/programming-arduino.jpg)](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#connect-by-solder)\
\
*Jumper Wires Used to Help Program an AVR Chip via Test Pads*

With the [2x5 header](https://www.sparkfun.com/products/15362) soldered into the 10 pin headers, connecting to the RedBoard Turbo is fairly straightforward:

[![Plugged in programmer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/2/RedBoard_Turbo_with_Programmer_copy.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/RedBoard_Turbo_with_Programmer_copy.jpg)

⚡ **Don\'t forget to power your board!** Because of all the various power options, the J-LINK programmers will generally not power your board by default. That means you\'ll need to power it over USB, battery, or something else. Just make sure your board gets power (and ground).

## AVR Studio

Now that we\'ve gotten everything hooked up it is time to program. There are a few different options for programming. Atmel studio is a great option (assuming you are using an ATMEL ARM processor like the SAMD line). Atmel Studio also lets you write programs in C, and compile your code. The Arduino IDE also lets you compile and download a **\*.hex** file of your code. Make sure you [download](https://www.microchip.com/mplab/avr-support/atmel-studio-7) and [install](https://www.microchip.com/webdoc/GUID-ECD8A826-B1DA-44FC-BE0B-5A53418A47BD/index.html?GUID-8F63ECC8-08B9-4CCD-85EF-88D30AC06499) Atmel Studio (Windows 7 or later only)

[Download Atmel Studio 7](http://studio.download.atmel.com/7.0.1931/as-installer-7.0.1931-web.exe)

[Atmel Studio 7 Installation Instructions](https://www.microchip.com/webdoc/GUID-ECD8A826-B1DA-44FC-BE0B-5A53418A47BD/index.html?GUID-8F63ECC8-08B9-4CCD-85EF-88D30AC06499)

Let\'s go ahead and open Atmel Studio. Then we\'ll go to Tools and then Device Programming. From the drop down you\'ll need to select your programmer as well as your device (you might have to agree to the Terms of Use first). Then hit Apply and it should verify your programmer. Then go ahead and read the Device signature and Target Voltage, this make sure everything is being read correctly. Feel free to look around, you can get quite a bit of Tool Information as well as Device Information.

Next, we\'ll go to the ***Memories*** tab, you\'ll probably want to select \"Erase Flash before programming\", and then select the location of your bootloader or other code. Hit Program and you should be good to go after a second or 2.

[![J Links Device programming Memories window](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/AtmelStudioProgrammingClean.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/AtmelStudioProgrammingClean.PNG)

*Having a hard time seeing? Click the image for a closer look.*

## Troubleshooting

### Bootloader Protect Fuse Bits

If you get an error when trying to program, check the Fuses tab. On many of our boards we set the bootloader protection to protect from accidental overwriting. Basically this defines the size of the bootloader. Setting this value to 0x07 will set the bootloader size to 0 and allow you to write to that space.

[![Setting boot protection](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/BootloaderProtection.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/2/BootloaderProtection.png)

### Error Reading Device Signature and Flashing

If you receive the error below:

    language:bash
    Error: No device detected. Error 4109.

    Unable to enter programming mode. Verify device selection, interface settings, target power, security bit, and connections to the target device.

This may be due to a few things:

- clock speed is too high
  - try setting the the programmer to 1/4 of the frequency of the target device
- the wiring of the 2x5 header may be different depending on your programmer
  - check the user manual on the programmer and ensure that the pinout matches the target\'s header pins
  - ensure that the solder joints are good
- target device is not powered
  - since the programmer does not provide power, make sure you are providing power to your target device

In this particular case, it was due to the wiring of the 2x5 header on the Atmel JTAGICE3 port. It was different from the 2x5 header on the target device. The latest Atmel JTAGICE has two ports and an adapter to correctly connect to the 2x5 header.

[] **Need Help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)