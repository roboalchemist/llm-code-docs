# Source: https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide

## Introduction

[Arduino](https://learn.sparkfun.com/tutorials/what-is-an-arduino) is awesome. The boards are solid, the programming language and IDE are easy, and the community is awesome. But for a lot of electronics projects, an Arduino is overkill. If you\'re just blinking a few LEDs, and reading a single sensor, you can get the job done **smaller and cheaper** using a simple [IC](https://learn.sparkfun.com/tutorials/integrated-circuits), like the [ATtiny85](https://www.sparkfun.com/products/9378).

[![AVR 8 Pin 20MHz 8K 4A/D - ATtiny85](https://cdn.sparkfun.com/r/600-600/assets/parts/2/9/7/0/09378-1.jpg)](https://www.sparkfun.com/avr-8-pin-20mhz-8k-4a-d-attiny85.html)

### [AVR 8 Pin 20MHz 8K 4A/D - ATtiny85](https://www.sparkfun.com/avr-8-pin-20mhz-8k-4a-d-attiny85.html) 

[ COM-09378 ]

Atmel\'s itty-bitty ATtiny85 8-Bit Processor. 8K of program space, 6 I/O lines, and 4-channel 10 bit ADC. Runs up to 20MHz wit...

[ [\$3.50] ]

*Our hero! The ATtiny85.*

Unfortunately, the ATtiny85 doesn\'t have a well-known, ubiquitous development platform like Arduino\'s Uno or Leonardo. And 8kB of program space doesn\'t leave much room for a bootloader, so an extra programmer is usually required. On top of that, standard Arduino doesn\'t support the chip. That doesn\'t mean programming the ATtiny85 in Arduino isn\'t possible, though! Enter the [Tiny AVR Programmer](https://www.sparkfun.com/products/11460)\...

[![Tiny AVR Programmer](https://cdn.sparkfun.com/r/600-600/assets/parts/8/1/1/1/11801-01.jpg)](https://www.sparkfun.com/tiny-avr-programmer.html)

### [Tiny AVR Programmer](https://www.sparkfun.com/tiny-avr-programmer.html) 

[ PGM-11801 ]

The ATtiny45 and 85 are a couple of really cool little MCUs but did you know you can program them in Arduino? That\'s right, n...

[ [\$18.95] ]

The Tiny AVR Programmer is a general AVR programmer, but it\'s specifically designed to allow **quick-and-easy programming** of ATtiny85\'s (as well as 45\'s) compared to the [pocket AVR programmer](https://learn.sparkfun.com/tutorials/pocket-avr-programmer-hookup-guide?). It has an on-board socket, where the little 8-pin IC can be plugged in and directly programmed. No messy wires or soldering required! Once you\'ve programmed the ATtiny85, just remove it from the Programmer, and stick it into a [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) or prototyping board.

The Tiny AVR Programmer can also be used as a general purpose AVR programmer. It can directly program almost all AVR\'s (including the ATmega328 and ATmega32U4) whether they\'re on Arduino boards or in a breadboard.

### Covered In This Tutorial

In this hookup guide, we\'ll show how you can program ATtiny85\'s using the Tiny AVR Programmer and **Arduino**. We\'ll cover everything from driver installation to Arduino programming tips.

#### Required Materials

In addition to the [Tiny AVR Programmer](https://www.sparkfun.com/products/11801), you\'ll also need the following items to follow along with this tutorial:

- [ATtiny85](https://www.sparkfun.com/products/9378) \-- To be programmed by the programmer. *Remember, you can also use this to flash other AVR chips like the ATtiny84!*
- A computer or laptop with:
  - A free **USB Port**. A USB hub should work too.
  - [**Arduino IDE** installed](https://learn.sparkfun.com/tutorials/installing-arduino-ide).
- *Optional*:
  - [USB Extension Cable](https://www.sparkfun.com/products/518) \-- If your USB port is out of reach, this may help make the Programmer easier to reach.
  - [IC Test Clip - SOIC 8-Pin](https://www.sparkfun.com/products/13153) \-- If you are using a surface mount ATtiny, this handy dandy little clip makes it easy to program the microcontroller!
  - [Jumper Wires Premium M/F](https://www.sparkfun.com/products/9385) \-- Useful if you are connecting the Tiny AVR Programmer to another AVR microcontroller that is not the ATtiny85 or the IC Test Clip.

### Suggested Reading

- [Installing Arduino](https://learn.sparkfun.com/tutorials/installing-arduino-ide) \-- You\'ll need [Arduino](https://learn.sparkfun.com/tutorials/what-is-an-arduino) installed for the [Programming in Arduino](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide/programming-in-arduino) section of this tutorial. There is an ATtiny85 addon for Arduino, which enables you to program the tiny AVRs in the familiar Arduino interface.
- [Integrated Circuits](https://learn.sparkfun.com/tutorials/integrated-circuits) \-- This tutorial goes over the basic concepts of integrated circuits. The little black chips that the Tiny AVR Programmer is designed to program.
- [Polarity](https://learn.sparkfun.com/tutorials/polarity) \-- Specifically the [Integrated Circuits section](https://learn.sparkfun.com/tutorials/polarity/integrated-circuit-polarity). You should know all about IC notches and dots.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/polarity)

### Polarity 

An introduction to polarity in electronic components. Discover what polarity is, which parts have it, and how to identify it.

[](https://learn.sparkfun.com/tutorials/integrated-circuits)

### Integrated Circuits 

An introduction to integrated circuits (ICs). Electronics\' ubiquitous black chips. Includes a focus on the variety of IC packages.

## Board Overview

The image below provides a quick overview of the components on the Tiny AVR Programmer:

[![Programmer with annotated components](https://cdn.sparkfun.com/assets/c/c/3/1/8/52715ae8757b7f30048b4567.png)](https://cdn.sparkfun.com/assets/c/c/3/1/8/52715ae8757b7f30048b4567.png)

The \"brain\" of the Tiny AVR Programmer is an **ATtiny84** (not to be confused with the 85), \-- the 16-pin surface-mount chip \-- which comes preprogrammed with some firmware that makes it look like an AVR programmer. Unless you\'re writing custom AVR ISP firmware, you shouldn\'t ever have to mess with this chip. It\'s a black box. Program data comes into it from your computer, over USB, and it spits out the proper sequence of bytes to load that program into your ATtiny85.

In this tutorial, we\'ll mostly concern ourselves with the components on the right half of the board. The ATtiny85 programming socket, pin 0 LED, and prototyping pins.

### ATtiny85 Socket and Prototyping Pins

The socket and the pins broken out to the sides are what make the Tiny AVR Programmer unique. The 8-pin socket fits both the ATtiny85 and the ATtiny45 DIP packages. Just plug your IC-to-program into this socket, and a-programming you will go!

[![Programmer plugged into USB, ATtiny85 plugged into programmer](https://cdn.sparkfun.com/r/600-600/assets/1/5/f/9/9/527132e1757b7f632a8b4567.png)](https://cdn.sparkfun.com/assets/1/5/f/9/9/527132e1757b7f632a8b4567.png)

*A Tiny AVR Programmer with an ATtiny85 inserted.*

When plugging your ATtiny into the socket, take note of the **notch** on both the socket and the white silkscreen on the PCB. This should match the **polarity** of the ATtiny85. Usually the ATtiny85 has a **dot** next to pin 1 of the IC, this should be placed up **towards the notch**.

The *+*, *-*, and numerical **labels** on the side of the socket reference the pin numbers and voltage supply inputs of the ATtiny85. These pin numbers can be called in the Arduino IDE as we\'ll show later in this tutorial.

The 4-pin headers on either side of the socket help for prototyping the ATtiny85 out to external circuitry. You can easily plug [male jumper wires](https://www.sparkfun.com/products/11026) into these pins, which can be routed to breadboards or other prototyping circuits.

[![Using the prototyping pins](https://cdn.sparkfun.com/r/600-600/assets/2/4/1/d/2/52713322757b7fc8678b456a.png)](https://cdn.sparkfun.com/assets/2/4/1/d/2/52713322757b7fc8678b456a.png)

*An ATtiny85 being prototyped out to a [potentiometer](https://www.sparkfun.com/products/9806) (analog input), [button](https://www.sparkfun.com/products/97) (digital input), and [RGB LED](https://www.sparkfun.com/products/105) (analog/digital output).*

**Note:** The ATtiny85\'s I^2^C and SPI functionality cannot be used in this method because the pins are still tied to the SPI pins of the ATtiny84 used to program the chip. The IC needs to be removed from the programmer first.

The 4-pin headers can also be used to connect to surface mount ATtiny85\'s or other AVR microcontrollers that are on breadboards.

[![Tiny AVR Programmer Connected to surfacea mount ATtiny85 via the IC Test Clip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/2/Reprogramming_the_Lily_Tiny-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/Reprogramming_the_Lily_Tiny-01.jpg)

*Tiny AVR Programmer connected to an surface mount ATtiny85 that was sewn on fabric to [reprogram a LilyTiny](https://learn.sparkfun.com/tutorials/re-programming-the-lilytiny--lilytwinkle).*

Finally, there\'s an on-board **amber LED connected to pin 0** of the ATtiny85. This is super-helpful when you\'re uploading the \"Hello, world\" blink sketch to an ATtiny85.

------------------------------------------------------------------------

That covers the fundamental stuff on the Tiny AVR Programmer. If you plan on doing more advanced stuff with the board, or just want to know more, feel free to read on. Otherwise, skip ahead to the [next page](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide/driver-installation).

------------------------------------------------------------------------

### Output Programming Pins

The Tiny ISP Programmer is *not* limited to ATtiny85\'s. It\'s a full-fledged AVR programmer. This row of six pins can be connected to other AVRs via the standard 2x3- or 2x5-pin ISP headers. You could, for example, connect these pins to your Arduino Uno, Leonardo, etc. to re-flash a bootloader, or upload code using a programmer.

Refer to the pin labels in the image above if you\'re connecting the Tiny AVR Programmer to another AVR chip. Most AVR development boards break out either a 2x3 or 2x5 programming header, which have the following pin-outs:

[![AVR ISP Pinout](https://cdn.sparkfun.com/assets/d/8/9/c/9/527158c7757b7f17048b4567.png)](https://cdn.sparkfun.com/assets/d/8/9/c/9/527158c7757b7f17048b4567.png)

Just match up the labels on the Tiny Programmer to the pins on your AVR board/chip, and get ready to program!

### The Jumpers

There are two jumpers on the top side of the Tiny AVR Programmer: one is labeled *RST* and the other is *VCC*. Both of these jumpers affect the unpopulated 2x3 ICSP (in-circuit system programmer) header in the middle of the board. Unless you\'re planning on reprogramming the on-board [ATtiny84](https://www.sparkfun.com/products/11232), these jumpers and pins can generally be ignored.

The ***VCC* jumper** is **normally closed**. It controls the flow of power to the VCC pin on the ICSP header. When closed, power from USB will flow to the ICSP header. When open you\'ll need to supply power externally to that pin.

The ***RST* jumper** is **normally open**. When closed, this jumper connects the ATtiny84\'s reset pin to the to the 2x3 programming header. If you ever need to reprogram the ATtiny84 (which, for standard use cases, you shouldn\'t), you\'ll have to close this jumper to enable programming it.

------------------------------------------------------------------------

Enough talk. Let\'s start using the programmer. On the next few pages we\'ll cover driver installation (for Windows users) and show how you can use the Tiny AVR Programmer to program an ATtiny85 in Arduino.

## Driver Installation

Before you can start using the Tiny AVR Programmer, you may need to set it up on your computer. If you\'re using a **Mac or Linux** machine, you **don\'t need to install drivers**. Just plug the board in, and skip to the [Programming in Arduino page](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide/programming-in-arduino).

[Tiny AVR Programmer Hookup Guide - Programming in Arduino](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide/programming-in-arduino)

If you\'re using any version of **Windows**, you\'ve got a few steps to follow before you can join your Mac/Linux comrades. There are two sets of instruction for driver installation on this page. The [first is the easiest, quickest method,](#automatic-install) and should work for most everyone. The [second installation process](#manual-driver) is only required if the first one fails \-- it takes a more manual approach to the driver installation.

------------------------------------------------------------------------

### [][Automatically Install the Drivers with Zadig](#automatic-install)

To begin, **plug the Tiny AVR Programmer into your computer**. Upon initially connecting the board, Windows will try to automatically install the drivers. Some computers may be lucky, but most will turn up with a message notifying you that the driver install failed.

Click the link below to download the Zadig software and drivers:

[Download the Zadig USBtiny Drivers (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/zadig_v2.0.1.160.zip)

Use your favorite unzipper to extract the ZIP file. Don\'t forget where you put the extracted folder!

After you\'ve plugged the Tiny AVR Programmer into your computer and your machine has run through the process of checking for and failing to install drivers, proceed to the \"**zadig_v2.0.1.160**\" folder you just unzipped. Then **Run zadig.exe** software.

Zadig is a wonderful tool that can install the drivers on just about any Windows platform out there. Upon opening the program, you should be greeted with a window like this:

[![Zadig screenshot](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/zadig-01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/zadig-01.png)

There are a few options to verify before installing the driver:

- **Select the device** \-- The top dropbox controls which device you want to install the driver for. Hopefully you only have one option here, something like \"**Unknown Device #1**\". If you have more than one option, check your device manager to see if you can make sense of which is which (plugging and unplugging a device usually helps).
- **Select the driver** \-- Click the arrows in this box until you happen upon **libusb-win32 (vx.x.x.x)**, that\'s the driver we want to install.

After verifying those two selections, **click \"Install Driver\"**. The installation process can take a few minutes, but after you\'ve watched the scroll bar zoom by countless times, you should be greeted with a \"**The driver was installed successfully**\" message.

[![Zadig Successful Driver Install Message](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/1/4/AVR_Programmer_Zadig_usbtiny_Drivers_Installed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/AVR_Programmer_Zadig_usbtiny_Drivers_Installed.jpg)

### Zadig Driver Installation Issues

After installing the drivers, your computer may respond by indicating that the device was not installed correctly. Here are two methods of troubleshooting driver issues when installing with Zadig.\
\
📌 **Troubleshooting Tip:** In this case, the *WinUSB* drivers were selected instead of the *libusb-win32* drivers. To remedy the issue, simply go through the [guide again to reinstall the correct *libusb-win32* drivers](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide#automatic-install).\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/Zadig_AVR_Programmer__Drivers_Not_Installed_Correctly_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/Zadig_AVR_Programmer__Drivers_Not_Installed_Correctly_2.jpg)

\
📌 **Troubleshooting Tip:** In other cases, it may also initialize somewhere in your device manager as an **Unknown USB Device (Device Descriptor Request Failed)** even if you installed the correct drivers:\
\

[![](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/2/1/4/Zadig_AVR_Programmer_Drivers_Not_Installed_Correctly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/Zadig_AVR_Programmer_Drivers_Not_Installed_Correctly.jpg)

\
Try unplugging and replugging the Tiny AVR Programmer back into your USB port. Or switch out your USB extension cable for a known good. In some cases, your Tiny AVR Programmer may shows up under the **libusb-win32 devices** as an **Unknown Device #1**. If that is the case you should be good to go!\
\

[![](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/2/1/4/Driver_Recognized_under_libusb-win32_devices.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/Driver_Recognized_under_libusb-win32_devices.jpg)

**Well done!** You\'ve successfully installed the drivers on your computer. However, the driver still shows up as an **Unknown Device #1** (in some cases like the image below, the Tiny AVR Programmer may show up as **libusb-win32 devices** \> **FabISP**). But you know what it is! You can use the Zadig software to rename the USB port if you desire. With your programmer connected to your computer and the software open, navigate to the programmer\'s port. Select the checkbox next to **Edit**.\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Zadig_Rename_and_Reinstall_Device_Driver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Zadig_Rename_and_Reinstall_Device_Driver.jpg)

\
Type in the name for your port. It can be \"**USBtiny**\" or in this case. Make sure that the correct driver is selected.\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Zadig_USBtiny_Rename_Reinstall_Device_Driver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Zadig_USBtiny_Rename_Reinstall_Device_Driver.jpg)

\
Click **Reinstall Driver**. The driver will reinstall and you should see the same message that indicates that the drivers were successfully installed. You may need to unplug and replug the programmer to your computer to give it a second to refresh again.\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Zadig_Success_Rename_Reinstall_Device_Driver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Zadig_Success_Rename_Reinstall_Device_Driver.jpg)

\
Open up your device manager and you should see the device renamed!\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/0/Tiny_AVR_Programmer_Device_Manager.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Tiny_AVR_Programmer_Device_Manager.jpg)

If you were successful, close out of the Zadig program and [proceed to the next section](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide/programming-in-arduino)!

[Tiny AVR Programmer Hookup Guide - Programming in Arduino](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide/programming-in-arduino)

If Zadig didn\'t work for you, check out the instructions below for help manually installing the drivers.

------------------------------------------------------------------------

### [][Manually Installing the libUSB Drivers](#manual-driver)

### Step 1: Plug the Programmer In

To begin, locate an empty USB port on your computer, and plug the Tiny AVR Programmer into it. You\'ll probably want to have the programmer close by. If you\'re using a PC, or your USB ports aren\'t close by, a [USB Extension Cable](https://www.sparkfun.com/products/518) might help get the programmer into a more convenient spot on your desk.

### Step 2: Wait for Windows to Automatically Fail/Succeed

After plugging in your Tiny AVR Programmer, Windows will try to look for a driver that matches it. Keep an eye on the notification area in the bottom-right corner. Wait for Windows to try to install the driver on its own. There\'s a chance that, after searching, Windows will find the driver. If you get a *Device driver software installed successfully* notification (lucky you!), you can ignore the next few steps. But, if you got something like this:

[![Driver installation failed](https://cdn.sparkfun.com/assets/b/6/3/f/b/5270287b757b7f64668b4568.png)](https://cdn.sparkfun.com/assets/b/6/3/f/b/5270287b757b7f64668b4568.png)

Continue on to step 3\...

### Step 3: Download the Driver

If Windows couldn\'t find the driver for you, you\'ll need to download it. You can head over to the [Tiny AVR Programmer GitHub repository](https://github.com/sparkfun/Tiny-AVR-Programmer/tree/master/Drivers) and grab what you need there, or you can click the link below to download the zip file directly.

[Tiny AVR Programmer Drivers (ZIP)](https://cdn.sparkfun.com/datasheets/Dev/AVR/usbtinyisp_libusb_1.2.6.0.zip)

After downloading your driver, extract it from the zip folder. Don\'t forget where you put it!

#### Step 4: Open the Device Manager

To install the driver, you\'ll need to first [open up the *Device Manager*](https://learn.sparkfun.com/tutorials/terminal-basics/connecting-to-your-device#devmgmt). From the **Control Panel**, go to the **System and Security** section, click **System**, and click on **Device Manager**. (Alternatively you can **Run** ***devmgmt.msc***).

In the *Device Manager*, open up the *LibUSB-Win32 Devices* tree and you should find a *USBTinyProgrammer* with a yellow warning triangle hovering over the icon. This also may be located in \"**Other devices** \> **Unknown device**.

**Right-click** on the *USBTinyProgrammer* device, and select ***Update Driver Software\...***

[![The device manager](https://cdn.sparkfun.com/assets/b/a/3/d/2/5270287b757b7f88668b4567.png)](https://cdn.sparkfun.com/assets/b/a/3/d/2/5270287b757b7f88668b4567.png)

### Step 5: Driver Pointing

On the *Update Driver Software* window that appears, **select *Browse my computer for driver software***.

On the next window, *Browse for driver software on your computer*, set the driver search location to the folder you downloaded and unzipped in step 3.

[![Browse for drivers](https://cdn.sparkfun.com/r/600-600/assets/e/3/8/a/e/5270287c757b7fb5668b4567.png)](https://cdn.sparkfun.com/assets/e/3/8/a/e/5270287c757b7fb5668b4567.png)

Then **click *Next***, and the driver will begin updating. Shortly after that, though, a *Windows Security* window should pop up to let you know the driver isn\'t \"signed\". **Click *Install this driver software anyway***. We promise it won\'t damage your computer!

[![Windows Warning](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/4/driver-08.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/driver-08.png)

Then play the waiting game for a moment, and wait for a happy *Windows has successfully updated your driver software* window.

After closing that success window, your *Device Manager* should have an entry for ***USBtiny*** under *LibUSB-Win32 Devices*.

[![USBTiny Installed in Device Manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/4/driver-10.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/4/driver-10.png)

Congratulations! [Proceed over to the next section](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide/programming-in-arduino), and we\'ll start using the Programmer!

📌 **Drivers Still Not Installing?** If you are **still** having issues installing the drivers, try looking at this troubleshooting tip and driver from our technical support. The drivers work for both the Tiny AVR Programmer and Pocket AVR Programmer.\
\

[GitHub SparkFunTechSupport: \...\\PGM-11801](https://github.com/SparkfunTechSupport/Additional-files/tree/master/PGM-11801)

------------------------------------------------------------------------

Breathe easy now! Once you\'ve installed the USBtiny drivers on your computer, you shouldn\'t ever have to do it again. Now it\'s time to program something!

## Programming in Arduino

Everyone loves Arduino! The simplified language makes programming AVRs and more complicated microcontrollers incredibly easy. Unfortunately, Arduino doesn\'t have any built-in functionality to program tiny AVRs, but that doesn\'t mean we can\'t add it!

On this page we\'ll go over all of the steps necessary to enable ATtiny45/85 programming in Arduino, using the Tiny AVR Programmer.

### Step 0: Install Arduino

If you\'ve never used Arduino before (where have you been?!), make sure you follow our [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino) and [Installing Arduino](https://learn.sparkfun.com/tutorials/installing-arduino-ide) tutorials before continuing on.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### Step 1: Installing the ATtiny Add-On

The next step is to install the Attiny addon. The following steps in 1a and 1b will explain how to manually install the ATtiny board files for Arduino.

📌 **Tip:** For beginners, you can **automatically** install using the Arduino boards manager by following the directions in \"Installing the ATtiny Support in Arduino v1.6.4+.\"\
\

[High-Low Tech: Programming an ATtiny w/ Arduino 1.6 (or 1.0) - Installing ATtiny Support in Arduino 1.6.4](http://highlowtech.org/?p=1695)

#### Step 1a: Download the ATtiny Addon

To manually add ATtiny\'s to the standard Arduino IDE *Board* menu, you\'ll need to add a few files that help define the hardware. The latest ATtiny hardware definitions are kept in a [repository on GitHub](https://github.com/damellis/attiny).

[GitHub ATtiny Boards](https://github.com/damellis/attiny)

You can download them from there, or simply click on the archived links below (note: There are different files depending on which version of Arduino you are using):

- [ATtiny for Arduino 1.0.x](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/attiny-ide-1.0.x.zip)
- [ATtiny for Arduino 1.6.x](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/attiny-ide-1.6.x.zip)

Extract the ZIP folder, and don\'t forget where you put it!

#### Step 1b: Move the *attiny* Folder

There should be an *attiny* folder living within the *attiny-ide-1.x.x.zip* file you downloaded. **Copy** that folder and **paste** it into a folder called ***hardware*** within your **Arduino Sketchbook directory**.

If you\'re not sure where your Arduino sketchbook is, **open Arduino** and go to ***File*** \> ***Preferences***. The *Sketchbook location* should be the topmost entry in the *Preferences* dialog. By default, the sketchbook is usually an *Arduino* folder within your home folder (e.g. *C:\\Users\\userName\\Arduino* on Windows, or */Users/userName/Documents/Arduino* on Mac).

If there\'s not a *hardware* folder already in your Sketchbook **make one**. After placing the *attiny* folder in there, your directory structure should look a little something like this:

[![attiny and hardware folder directory structure](https://cdn.sparkfun.com/assets/a/7/e/9/4/5270287c757b7fc5658b456b.png)](https://cdn.sparkfun.com/assets/a/7/e/9/4/5270287c757b7fc5658b456b.png)

### Step 2: Open and Configure Arduino

Almost to the fun part! **Open Arduino**. If you opened Arduino in the last step, close it and restart it.

Under the ***Tools* \> *Board*** menu, you\'ll find the effects of the *attiny* folder. There should be twelve new entires in the board list, which allow you to program ATtiny45\'s, 85\'s, 44\'s and 84\'s. Each microcontroller can be set to a variety of clock speeds \-- internal 1MHz or 8MHz or external 20MHz.

If you\'re using a bare, previously untouched [ATtiny85](https://www.sparkfun.com/products/9378) select ***ATtiny85 (internal 1 MHz clock)***. Be careful selecting here, selecting the *8 MHZ* option will only make your sketch run slow, but selecting the *20 MHz* option can \"brick\" your ATtiny. **Do not select the *20 MHz* option unless you have an external clock attached!**

[![Arduino board selection](https://cdn.sparkfun.com/assets/0/9/e/5/7/5270287b757b7fbb658b4569.png)](https://cdn.sparkfun.com/assets/0/9/e/5/7/5270287b757b7fbb658b4569.png)

**Note:** Depending on your Arduino IDE version, you may need to individually select the **attiny\'s** **Processor** (i.e. **ATtiny85**) and **Clock** (i.e. **8MHz (internal)**).\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Arduino_Select_ATtiny_Processor_and_Clock.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Arduino_Select_ATtiny_Processor_and_Clock.jpg)

Unlike other Arduino boards, you don\'t have to select a *Serial Port* when using the Tiny AVR Programmer. But you do need to select a ***Programmer***. Under the *Tools* \> *Programmer* menu, select ***USBtinyISP***.

[![Arduino programmer selection](https://cdn.sparkfun.com/assets/5/0/5/c/1/5270287c757b7f40668b4567.png)](https://cdn.sparkfun.com/assets/5/0/5/c/1/5270287c757b7f40668b4567.png)

### Step 3: Plug in the ATtiny

Getting close to blinking! When you plug the ATtiny into your Programmer, make sure you get the [polarity](https://learn.sparkfun.com/tutorials/polarity) correct. The small, etched circle on the IC should line up with the \"notch\" on the Programmer\'s socket and silkscreen.

[![ATtiny85 polarity dot matches notch location](https://cdn.sparkfun.com/r/600-600/assets/3/f/5/f/4/52713369757b7ff7668b4567.png)](https://cdn.sparkfun.com/assets/3/f/5/f/4/52713369757b7ff7668b4567.png)

To get the IC into the socket, you may need to bend the legs on each side inwards a tad.

### Step 4: Upload Code!

Time for the Blink sketch! The Tiny AVR Programmer has an on-board LED, connected to the ATtiny, which we can use to verify that code on the IC is running. The LED is connected to pin 0 in the Arduino environment. Copy/paste this code into your Arduino window:

    language:c
    int blinkPin = 0;

    void setup()
    

    void loop()
    

Then click the ***Upload*** button just as you would with any Arduino board. The code will compile, and then it should upload insanely fast. That\'s the wonders of direct in-system programming for you. If successful, the on-board **amber LED should start blinking**.

**Note:** You can also upload using the Arduino IDE menu. Depending on your Arduino IDE version, you can select either **Sketch** \> **Upload Using Programmer** or **Sketch** \> **Upload Using Programmer**.

📌 **Troubleshooting Tip:** If you receive the following Arduino error, this might be due to the connection or an issue with the drivers.\
\

``` bash
avrdude: Error: Could not find USBtiny device (0x1781/0xc9f)
```

You should see this at the bottom of the Arduino IDE in the text console.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/0/Arduino_Error_Uploading_to_ATtiny85_Driver_Issue.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Arduino_Error_Uploading_to_ATtiny85_Driver_Issue.jpg)

\
If the issue is related to the connection, try unplugging/replugging the AVR programmer back into your USB cable or USB port. You also want to try a different USB cable.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/1/5/f/9/9/527132e1757b7f632a8b4567.png)](https://cdn.sparkfun.com/assets/1/5/f/9/9/527132e1757b7f632a8b4567.png)

\
Otherwise, the issue may be due to the drivers. This may be caused by the driver not being installed correctly, or there is a driver conflict. Open up your device manager to view the device. The image on the left shows the device showing up as the **libusb-win32 devices** \> **FabISP**. The image on the right shows the device showing up as **Other devices** \> **FabISP**.\
\

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Renaming_Device_Driver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Renaming_Device_Driver.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/AVR_Programmer_FabISP_Driver_Conflict.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/AVR_Programmer_FabISP_Driver_Conflict.jpg)
  *Conflicting Driver*                                                                                                                                                        *Driver Not Installed*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In either case, right click on the device and select **Uninstall device**.\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Uninstall_Conflicting_Programmer_Driver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Uninstall_Conflicting_Programmer_Driver.jpg)

\
You may see a window pop up similar to the image below. Click on the button labeled **Uninstall**. In some cases, Windows may provide an option to **\"Delete the driver software for this device.\"** if the option is provided, simply mark the checkbox before clicking on the button to uninstall.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/0/Uninstall_Conflicting_Device_Driver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/0/Uninstall_Conflicting_Device_Driver.jpg)

\
Unplug and replug the AVR programmer back to your computer\'s USB port. Head back to the Driver Installation section and follow the instructions to [Automatically Install the Drivers using Zadig](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide#automatic-install).\
\

[Driver Installation: Automatically Install the Drivers with Zadig](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide#automatic-install)

### Uploading Code the Hard Way

If you're looking for more control over your Tiny AVR Programmer -- and the AVR it's connected to -- follow along the [tutorial for the Pocket AVR Programmer](https://learn.sparkfun.com/tutorials/pocket-avr-programmer-hookup-guide#using-avrdude-via-command-line). While the tutorial was written for the Pocket AVR Programmer, it is functionally the same for the Tiny AVR Programmer. Just make sure to connect to the respective ICSP pins on the target AVR chip.

[![AVRDUDE via Command Lin](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/4/avrdude-not-installed.jpg)](https://learn.sparkfun.com/tutorials/pocket-avr-programmer-hookup-guide#using-avrdude-via-command-line)

*Using [AVRDUDE via Command Line](https://learn.sparkfun.com/tutorials/pocket-avr-programmer-hookup-guide#using-avrdude-via-command-line)*

## ATtiny85 Use Hints

The ATtiny85 isn\'t your everyday Arduino IC. It packs a lot of punch for its small size, but there are some things it can\'t do.

On this page, we\'ll provide a quick overview of the ATtiny85 as it pertains to Arduino and the Tiny AVR Programmer.

### Pinout

Just like any Arduino board, each I/O pin on the ATtiny85 is assigned a numerical identifier. These pins are documented on the board as well, but you can also refer to the image below if you forget.

[![ATtiny85 Pin Map](https://cdn.sparkfun.com/r/600-600/assets/f/8/f/d/9/52713d5b757b7fc0658b4567.png)](https://cdn.sparkfun.com/assets/f/8/f/d/9/52713d5b757b7fc0658b4567.png)

Each of the I/O pins on the ATtiny85 are capable of digital input and output. Beyond that, some pins have special functionality.

#### Analog Input and Output

There are **two analog outputs** and **three analog inputs**. Use them just as you would with any Arduino board. Use `analogWrite([pin], [0-255])` to do [PWM](https://learn.sparkfun.com/tutorials/pulse-width-modulation) output. This functionality is available on pins 0 and 1. For example:

    language:c
    int pwmPin = 0;

    pinMode(pwmPin, OUTPUT);

    for (int i=0; i<=255; i+=5)
    

And use `analogRead([pin])` to read an analog voltage between 0 and 5V, and turn it into a 10-bit representation of that voltage. Pins 2, 3, and 4 are capable of analog input, but, when using them as such, they should be referenced as **A1, A3, or A2** respectively. For example:

    language:c
    int pwmPin = 0;
    int analogInPin = A1;

    pinMode(pwmPin, OUTPUT);
    pinMode(analogInPin, INPUT);

    int analogIn = analogRead(analogInPin); // Read analog voltage on pin 2 (A1)

    analogWrite(pwmPin, analogIn / 4); // Output analog reading to dimmable LED

**Note:** For advanced users, you can modify the ATtiny85\'s timer/counter registers to increase the number of PWM channels available! You can get up to four PWM channels by following this tutorial here: [Technoblogy - Four PWM Outputs from the ATtiny85](http://www.technoblogy.com/show?LE0). The example just runs PWM on the ATtiny85. If you are trying to add more features outside of the PWM example, there might be some unexpected behaviors since it is modifying the timing registers.\
\
If you need to reset the chip, simply use the erase command with the Tiny AVR or Pocket AVR Programmer via command line to get it back to its previous state. Uploading code with the Arduino IDE will not be enough. Here is an example using the fuse bit settings for the LilyTwinkle\'s ATtiny85:\
\

    avrdude -c usbtiny -b 19200 -p t85 -v -e -U lfuse:w:0xe2:m -U hfuse:w:0xdf:m -U efuse:w:0xff:m -U lock:w:0xCF:m

After resetting the chip, you can proceed to upload code to the chip through the Arduino IDE as explained earlier.

#### No Serial (UART). Yes SPI and I^2^C.

You may notice, on the listing of special pin functions there are no UART RX\'s or TX\'s. That\'s because the ATtiny85 doesn\'t have a built in [hardware UART](https://learn.sparkfun.com/tutorials/serial-communication/uarts). If you try to compile any Arduino code with `Serial.begin(9600)`\'s or `Serial.print()`\'s you\'ll get an error.

So you\'re out one of the more useful Arduino debugging tools. You can\'t print to the Serial Monitor. But the ATtiny85 does still have [I^2^C](https://learn.sparkfun.com/tutorials/i2c) and [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi), which are much more commonly used for sensor communication these days. Unfortunately, the Arduino libraries for these interfaces haven\'t yet been written for the ATtiny85, but there are some user contributed libraries around the web. [USIi2c](http://playground.arduino.cc/Code/USIi2c) is an Arduino library which enables I^2^C on the ATtiny85.

There are other ATtiny85-focused libraries out there too. Like a [Servo8Bit](https://github.com/fri000/Servo8Bit), a servo library.

**Tip:** Looking for a quick reference guide for the ATtiny85? Click on the link below to download an image or PDF version from our resources!\
\

[![ATTiny85 Quick Reference](https://cdn.sparkfun.com/assets/0/4/1/4/a/Tiny_QuickRef_v2_2_1.png)](https://learn.sparkfun.com/resources/96)

### Prototyping with the Tiny AVR Programmer

There\'s only so much excitement you can get out of dimming a single, yellow LED. You\'ll eventually want to branch out, and start connecting your tiny85 to other electronic components. There are a few ways to do this.

The easiest, least permanent prototyping route is to use the **prototyping headers** on either side of the socket. You can connect standard, [male jumper wires](https://www.sparkfun.com/products/11026) to these pins, which can in turn be routed to breadboards or other components.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/2/4/1/d/2/52713322757b7fc8678b456a.png)](https://cdn.sparkfun.com/assets/2/4/1/d/2/52713322757b7fc8678b456a.png)

For more permanent projects, it\'s easy enough to gently **remove the IC from the socket**, and plug it into a PCB or breadboard. Eventually, once you\'ve iterated enough on your sketch, this is probably where you\'ll want to go. Eventually you arrive at finished designs like the [H2OhNo!](https://www.sparkfun.com/products/12069) or the [LectroCandle](https://www.sparkfun.com/products/9563).

### Surface Mount ATtiny85 SOIC Packages

Trying to reprogram an ATtiny85 with a SOIC Package? There are a few ways to connect. The easiest would be to use the IC test clip and M/F jumper wires.

[![Jumper Wires Premium 6\" M/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/5/7/09140-02-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html)

### [Jumper Wires Premium 6\" M/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html) 

[ PRT-09140 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumper wires terminated as male to female. Use these to jumper fro...

[ [\$4.60] ]

[![IC Test Clip - SOIC 8-Pin](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/2/3/7/13153-01.jpg)](https://www.sparkfun.com/ic-test-clip-soic-8-pin.html)

### [IC Test Clip - SOIC 8-Pin](https://www.sparkfun.com/ic-test-clip-soic-8-pin.html) 

[ COM-13153 ]

This is an IC Test Clip for 8-pin small outline integrated circuits (SOIC). This test clip assures a secure connection to all...

[ [\$41.50] ]

For more information, check out our tutorial on reprogramming ATtiny85\'s on the LilyTiny and LilyTwinkle.

[](https://learn.sparkfun.com/tutorials/re-programming-the-lilytiny--lilytwinkle)

### Re-Programming the LilyTiny / LilyTwinkle 

September 11, 2014

A quick tutorial showing how to reprogram the ATtiny85 IC found on the LilyTiny or LilyTwinkle boards.

If the programming pins are broken out on a standard 2x3 ICSP header, you could also solder together the ISP pogo adapter to temporarily connect to the chip. Or you could grab a few alligator test leads or IC hook to individually connect each programming pin to the Tiny AVR Programmer\'s machine headers.

[![IC Hook with Pigtail](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/9/6/09741-01.jpg)](https://www.sparkfun.com/ic-hook-with-pigtail.html)

### [IC Hook with Pigtail](https://www.sparkfun.com/ic-hook-with-pigtail.html) 

[ CAB-09741 ]

These are good quality IC test hooks with a male connection wire. Instead of a single hook, these have two hooks that are cap...

[ [\$5.75] ]

[![Alligator Clip with Pigtail (10 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/6/5/14303-Alligator_Clip_with_Pigtail__10_Pack_-01.jpg)](https://www.sparkfun.com/alligator-clip-with-pigtail-10-pack.html)

### [Alligator Clip with Pigtail (10 Pack)](https://www.sparkfun.com/alligator-clip-with-pigtail-10-pack.html) 

[ CAB-14303 ]

This is a 10-pack of wires that are pre-terminated with an alligator clip on one end and a male header on the other.

[ [\$9.25] ]

[![SparkFun ISP Pogo Adapter v2](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/7/5/6/233451-ISP-Pogo-Adapter-Reshoot-Feature.jpg)](https://www.sparkfun.com/sparkfun-isp-pogo-adapter-v2.html)

### [SparkFun ISP Pogo Adapter v2](https://www.sparkfun.com/sparkfun-isp-pogo-adapter-v2.html) 

[ KIT-23451 ]

The ISP Pogo Adapter, a simple and easy way to adapt pogo pins to a 6-pin ISP header allowing you to program an IC still with...

[ [\$15.50] ]