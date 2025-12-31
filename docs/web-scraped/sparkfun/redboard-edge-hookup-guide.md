# Source: https://learn.sparkfun.com/tutorials/redboard-edge-hookup-guide

## Introduction

The [RedBoard Edge](https://www.sparkfun.com/products/14525) is a nifty little rework of the [SparkFun RedBoard](https://www.sparkfun.com/products/13975) designed to be panel mounted in your custom project enclosure to allow for an easy way to make a clean, finished looking product. It has all the features of a normal RedBoard, allowing you to prototype on a RedBoard and easily move your project over to a RedBoard Edge without complication.

[![SparkFun RedBoard Edge](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/0/6/14525-SparkFun_RedBoard_Edge-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-edge.html)

### [SparkFun RedBoard Edge](https://www.sparkfun.com/sparkfun-redboard-edge.html) 

[ DEV-14525 ]

The SparkFun RedBoard Edge is a rework of the SparkFun RedBoard that has been designed to be panel mounted in your custom pro...

**Retired**

The RedBoard Edge is just as easy to use as a regular RedBoard, so it\'s still an excellent **learning platform** for physical computing.

The goal of this tutorial is to familiarize you with the RedBoard Edge so you\'ll be able to easily transfer over your RedBoard project when you\'re ready to go from a prototype to an enclosed product. Since it\'s basically a reshaped RedBoard, you may be able to glaze over parts of this tutorial if you\'re familiar with how the RedBoard works.

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

You will need a [RedBoard Edge](https://www.sparkfun.com/products/14525) and a [micro-B-to-A USB cable](https://www.sparkfun.com/products/10215). The USB interface serves two purposes: it powers the RedBoard Edge and allows you to upload programs to it.

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![SparkFun RedBoard Edge](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/6/0/6/14525-SparkFun_RedBoard_Edge-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-edge.html)

### [SparkFun RedBoard Edge](https://www.sparkfun.com/sparkfun-redboard-edge.html) 

[ DEV-14525 ]

The SparkFun RedBoard Edge is a rework of the SparkFun RedBoard that has been designed to be panel mounted in your custom pro...

**Retired**

You\'ll also need a computer \-- Mac, PC, or Linux will do \-- with the **Arduino IDE** installed on it. You can [download Arduino](http://arduino.cc/en/Main/Software) from their website. They\'ve got installation instructions there, but we\'ll also go over installation in this tutorial.

[Download the Arduino IDE](http://arduino.cc/en/Main/Software)

### Tools

Depending on your setup, you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

The RedBoard Edge aims to be as beginner friendly as a microcontroller platform can be. You can get by using it without an innate knowledge of [Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) or [How Electricity Works](https://learn.sparkfun.com/tutorials/what-is-electricity) (but a little understanding wouldn\'t hurt!). The board utilizes the Qwiic system so we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

Brushing up on your skills in I^2^C is also recommended, as all Qwiic sensors are I^2^C. If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## A Rearranged RedBoard

With the RedBoard Edge, we\'ve rearranged the RedBoard Programmed with Arduino to include everything \"user-facing\" (i.e. \"front\" side) on one side of the board, and everything \"project-facing\" on the other side of the board.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_User-Facing_Side.jpg "User-Facing Side (i.e. ")](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_User-Facing_Side.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Project-Facing_Side.jpg "Project-Facing Side")](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Project-Facing_Side.jpg)
  *User-Facing Side (i.e. \"Front\" Side)*                                                                                                                                                                                                                                         *Project-Facing Side*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below are images highlighting where all of the things you\'ve come to know and love on your regular old RedBoard have moved to. Pins have been grouped by function (PWM, ADC, SPI), with power rails for 5V and Ground running parallel to each grouping. There are also 4-pin power rails for 5V and 3.3V right next to the 5mm 2-pin screw terminal which is connected to VIN through the toggle switch on the user-facing side of the board.

### The User-Facing Side (i.e. \"Front\" Side)

#### micro-B USB

The RedBoard Edge can be powered via either the USB or barrel jack connectors. If you choose to power it via USB, the other end of the USB cable can be connected to either a computer or a (5V regulated) [USB wall charger](https://www.sparkfun.com/products/11456).

[![micro-B Connector](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_USB.jpg)

#### Barrel Jack for VIN

The power jack accepts a center-positive barrel connector with an outer diameter of 5.5mm and inner diameter of 2.1mm. Our [9V](https://www.sparkfun.com/products/298) and [12V wall adapters](https://www.sparkfun.com/products/9442) are good choices if you\'re looking to power the RedBoard this way. Any wall adapter connected to this jack should supply a **DC voltage between 7V and 15V**.

[![Barrel Jack](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Barrel_Jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Barrel_Jack.jpg)

#### Power Switch

The board has a switch to toggle power for the rest of the board. Note that the toggle switch will not disconnect USB power.

[![Power Switch](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Power_Switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Power_Switch.jpg)

#### Choosing Power for the RedBoard Edge

There are a few options to power the RedBoard Edge depending on your preference and project needs. USB is usually the easiest way to power the board, especially when you\'re programming it, because the USB interface is required for uploading code too. Why would you use the barrel jack? Usually, it\'s because you need more power. A USB port is usually only allowed to supply 500mA. If you need more than that a wall adapter may be your only choice.

It is acceptable to connect both a barrel jack and a USB connector at the same time. The RedBoard Edge has power-control circuitry to automatically select the best power source. As explained earlier, the toggle switch will not disconnect USB power.

#### Indication and Interfacing

All of the indication lights have been moved to the front side of the board, so you would be able to see them in your custom enclosure. From left to right, the indicator lights are connected to power, pin 13, TX, and RX, shown in the image below. The button on the far right of the board controls Reset.

[![LEDs and Reset Switch](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_StatusLEDs_Reset.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_StatusLEDs_Reset.jpg)

### The Project-Facing Side

#### Screw Terminals for VIN

This barrel connector is connected to the screw terminals on the project-facing side of the board through the toggle switch on the front of the board.

[![Screw Terminals for VIN](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Screw_Terminals.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Screw_Terminals.jpg)

#### PTH Power Pins

The board also comes with 5V, 3.3V, and GND pins throughout the board.

[![Voltage Rails](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Power_Rails.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Power_Rails.jpg)

#### Pin Grouping

The RedBoard Edge has its pins separated into three groups on the project facing side of the board (ADC, SPI, and PWM) which are highlighted in the image below. These pins have the same functions as their RedBoard counterparts so expect to be able to use them like you would on your regular old RedBoard. Each group of three rows has the pins broken out on the top row, a 5V rail in the middle row, and ground on the bottom row.

#### Analog Inputs

There are eight **analog inputs** on the analog header. These pins all have [analog-to-digital converters](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion), which can be used to read in an analog voltage between 0 and 5V. These are useful if you need to read the output of a potentiometer or other analog sensors. Only analog pins A0 through A5 can also serve as digital inputs and outputs.

[![ADC Pins](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_ADC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_ADC.jpg)

**Heads up!** The ADC pins on A6 and A7 are only for analog input. You will not be able to use a digital read or write on these pins.

#### Serial Peripheral Interface (SPI)

The center group of 4 pins is the [SPI Interface](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) where `pin 10 = SS`, `pin 11 = MOSI`, `pin 12 = MISO` and `pin 13 = SCK`.

[![SPI Pins](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_SPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_SPI.jpg)

#### Pulse Width Modulation (PWM)

The furthest right grouping of pins are the [Pulse-Width Modulation (PWM)](https://learn.sparkfun.com/tutorials/pulse-width-modulation) pins, which can be used to drive LED\'s or servos.

[![PWM Pins](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_PWM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_PWM.jpg)

### Headers

The RedBoard Edge does not come with headers on-board to allow you the option to be able to solder your finished circuit straight into the board. However, if you\'d like to use your Edge for something more along the lines of prototyping purposes, grab some headers.

Check out our [through hole soldering tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) if you have yet to solder headers to a board

[![With Headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/6/SparkFun_RedBoard_Edge_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/SparkFun_RedBoard_Edge_Hookup_Guide-01.jpg)

### Other Neat Features

#### Grounded Mounting Holes

One of the cool things about the RedBoard Edge is the ability to ground the board to your metal enclosure through the standoffs on the left side. You can choose to connect your enclosure ground to either the USB shield or the board\'s ground, or both. Simply add solder to the respective jumper pad and connect the enclosure to your board with any 4-40 screw.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_USB_Shield_Grounding_Mounting_Hole.jpg "USB Shield GND Mounting Hole")](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_USB_Shield_Grounding_Mounting_Hole.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Grounding_Mounting_Hole.jpg "GND Mounting Hole")](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Grounding_Mounting_Hole.jpg)
  *USB Shield GND Mounting Hole*                                                                                                                                                                                                                                                                     *GND Mounting Hole*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Qwiic Connector

We\'ve also added a Qwiic connector, sandwiched in there between the power and ADC pins, to allow the RedBoard Edge to interface with [SparkFun\'s Qwiic Ecosystem](https://www.sparkfun.com/qwiic).

[![Qwiic Connector](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Qwiic_Connector_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_Qwiic_Connector_I2C.jpg)

#### CH340G USB-to-Serial Converter

As opposed to using the FTDI for USB-to-serial conversion, the board uses the CH340G IC. One advantage is that it does not need a driver since most operating systems have the CDC drivers pre-installed. What this means is that you shouldn't need to install any extra software.

[![CH340G USB-to-Serial Converter](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_CH340G_USB-to-Serial_Converter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/14525-SparkFun_RedBoard_Edge-04_CH340G_USB-to-Serial_Converter.jpg)

## Download/Install Arduino

Before you plug the RedBoard Edge into your computer, you\'ll need to install Arduino first.

### Installing Arduino

To begin, head over to [Arduino\'s download page](http://arduino.cc/en/Main/Software) and grab the most recent, stable release of Arduino. Make sure you grab the version that matches your operating system.

[Download the Arduino IDE](http://arduino.cc/en/Main/Software)

The installation procedure is fairly straightforward, but it varies by OS. Here are some tips to help you along. We\'ve also written a separate [Installing Arduino tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide) if you get really stuck.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

#### Windows Install Tips

The Windows version of Arduino is offered in two options: an installer or a zip file. The **installer** is the easier of the two options, just download that, and run the executable file to begin installation. If you\'re prompted to install a driver during installation, select \"Don\'t Install\" (the RedBoard Edge doesn\'t use the same drivers). Don\'t forget which directory it installs to (defaults to \"Program Files/Arduino\").

[![Windows Installer](https://cdn.sparkfun.com/r/600-600/assets/1/6/d/f/a/522f7e7b757b7fe56d8b4567.png)](https://cdn.sparkfun.com/assets/1/6/d/f/a/522f7e7b757b7fe56d8b4567.png)

*Windows install steps. Click the image to get a bigger view.*

If, instead, you choose to download the **zip file** version of Arduino, you\'ll need to extract the files yourself. Don\'t forget which folder you extract the files into! We\'ll need to reference that directory when we install drivers.

#### Mac Install Tips

The Mac download of Arduino is only offered in a zip file version. After the download is finished, simply **double-click the .zip file** to unzip it.

[![Mac Install Screenshot](https://cdn.sparkfun.com/assets/3/4/1/7/b/52cc895fce395fe16e8b456a.jpg)](https://cdn.sparkfun.com/assets/3/4/1/7/b/52cc895fce395fe16e8b456a.jpg)

Following that, you\'ll need to **copy the Arduino application into your applications folder** to complete installation.

#### Linux Install Tips

As you Linux users are no doubt aware, there are many flavors of Linux out there, each with unique installation routines. Check out the [Linux section of the Installing Arduino tutorial](https://learn.sparkfun.com/tutorials/installing-arduino/linux) for some helpful links for an assortment of Linux distributions.

For Ubuntu and Debian users, installing Arduino should be as easy as running a little \"apt-get\" magic, with a command like:

    language:bash
    sudo apt-get update && sudo apt-get install arduino arduino-core  

And other Linux distros aren\'t too dissimilar from that.

------------------------------------------------------------------------

With Arduino downloaded and installed, the next step is to plug the RedBoard Edge in and install some drivers! Pretty soon you\'ll be blinking LEDs, reading buttons, and doing some physical computing!

## Drivers (If You Need Them)

The driver should automatically install on most operating systems. However, there is a wide range of operating systems out there. You may need to install drivers the first time you connect the chip to your computer\'s USB port or when there are operating system updates. For more information, check out our [How to Install CH340 Drivers Tutorial](https://www.sparkfun.com/ch340).

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

## Uploading Blink

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Now it\'s finally time to **open up the Arduino IDE Software**. You\'ll be presented with a window that looks a little something like this:

[![Arduino IDE annotated](https://cdn.sparkfun.com/assets/8/4/5/b/d/52309c7e757b7f522d8b4567.png)](https://cdn.sparkfun.com/assets/8/4/5/b/d/52309c7e757b7f522d8b4567.png)

Lets upload a **Blink sketch** to make sure our new RedBoard Edge setup is totally functional. Go up to the **File** menu in Arduino, then go to **Examples \> 01.Basics \> Blink** to open it up.

Before we can send the code over to the RedBoard Edge, there are a couple adjustments we need to make.

### Select a Board

This step is required to tell the Arduino IDE *which* of the [many Arduino boards](https://learn.sparkfun.com/tutorials/choosing-an-arduino-for-your-project) we have. Go up to the **Tools** menu. Then hover over **Board** and make sure **Arduino Uno** is selected.

[![Board Selection](https://cdn.sparkfun.com/assets/4/a/4/b/0/52309f4f757b7fbf2d8b4567.png)](https://cdn.sparkfun.com/assets/4/a/4/b/0/52309f4f757b7fbf2d8b4567.png)

### Select a Serial Port

Next up we need to tell the Arduino IDE which of our computer\'s serial ports the RedBoard is connected to. For this, again go up to **Tools**, then hover over **Serial Port** and select your RedBoard\'s COM port.

[![Port Selection](https://cdn.sparkfun.com/assets/b/e/0/0/c/52309f4f757b7fbd2d8b4567.png)](https://cdn.sparkfun.com/assets/b/e/0/0/c/52309f4f757b7fbd2d8b4567.png)

If you\'ve got more than one port, and you\'re not sure which of the serial ports is your RedBoard Edge, unplug it for a moment and check the menu to see which one disappears.

### Upload!

With all of those settings adjusted, you\'re finally ready to upload some code! Click the **Upload** button (the right-pointing arrow) and allow the IDE some time to compile and upload your code. It should take around 10-20 seconds for the process to complete. When the code has uploaded, you should see something like this in your console window:

[![Uploading Code](https://cdn.sparkfun.com/assets/a/0/5/7/0/5230a452757b7f512d8b4567.png)](https://cdn.sparkfun.com/assets/a/0/5/7/0/5230a452757b7f512d8b4567.png)

And if you look over to the RedBoard Edge, you should see the blue LED turn on for a second, off for a second, on for a second, off for a second\...ad infinitum (at least until it loses power). If you want to adjust the blink speed, try messing with the \"1000\" value in the `delay(1000);` lines. You\'re well on your way to becoming an Arduino programmer!

### Something Wrong?

Uh oh! If you didn\'t get a \"Done Uploading\" message, and instead got an error, there are a few things we can double-check.

If you got an `avrdude: stk500_getsync(): not in sync: resp=0x00` error in your console window.

[![Upload error](https://cdn.sparkfun.com/assets/9/a/6/f/b/5230a5fa757b7fcf2d8b4567.png)](https://cdn.sparkfun.com/assets/9/a/6/f/b/5230a5fa757b7fcf2d8b4567.png)

Either your serial port or board may be incorrectly set. Again, make sure **Arduino Uno** is the board selection (under the \"Tools \> Board\" menu). The serial port is usually the more common culprit here. Is the Serial Port correctly set (under the \"Tools \> Serial Port\" menu)? Did the drivers successfully install? To double check your RedBoard Edge\'s serial port, look at the menu when the board is plugged in, then unplug it and look for the missing port. If none of the ports are missing, you may need [drivers](https://learn.sparkfun.com/tutorials/serial-basic-hookup-guide#drivers-if-you-need-them).

## Panel Mounting

The RedBoard Edge was designed with panel mounting in mind, so let\'s look at how everything is laid out on the user-facing side so we can put holes in the proper places for a panel or enclosure.

[![Front of Edge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/6/SparkFun_RedBoard_Edge_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/SparkFun_RedBoard_Edge_Hookup_Guide-02.jpg)

The *RedBoardEdgePanel.svg* used for a panel mount should work well with a printer or maybe even a laser cutter. The file can be downloaded from the button below. Just make sure to unzip the file before using.

[Download RedBoardEdgePanel (ZIP)](https://cdn.sparkfun.com/assets/8/b/0/e/d/RedBoard_Edge_Panelmounting.zip)

**Note:** The USB hole in the **\*.svg** works for a low profile shroud USB which I was using. If you have a larger cable however, you may need to expand the USB cutout in GIMP or any other graphics software. To download, head over to GIMP\'s downloads page:

[Download GIMP](https://www.gimp.org/downloads/)

Once you\'ve created your front panel, it\'s easy to slide your RedBoard Edge through and secure it in place using the nut on the toggle switch. Look at that, my apartment smells of many burnt electronics and rich mahogany.

[![Mounted Edge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/6/SparkFun_RedBoard_Edge_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/6/SparkFun_RedBoard_Edge_Hookup_Guide-03.jpg)

### Mounting Hardware

If you\'d like to mount the RedBoard Edge to some sort of baseplate as well, you can attach the RedBoard Edge to your baseplate using 4-40 standoffs and screws to attach the RedBoard Edge to your baseplate. Keep in mind that grounding the board through the mounting holes will require metal standoffs.

[![Standoff Kit - 210 Piece](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/4/4/2/KIT-24115-210-Piece-Standard-Kit-Feature.jpg)](https://www.sparkfun.com/standoff-kit-210-piece.html)

### [Standoff Kit - 210 Piece](https://www.sparkfun.com/standoff-kit-210-piece.html) 

[ KIT-24115 ]

This 210 piece brass standoff kit insures you\'ll always have a set handy.

[ [\$18.50] ]

[![Standoff - Nylon (4-40; 3/8\"; 10 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/0/7/1/10927-03.jpg)](https://www.sparkfun.com/standoff-nylon-4-40-3-8-10-pack.html)

### [Standoff - Nylon (4-40; 3/8\"; 10 pack)](https://www.sparkfun.com/standoff-nylon-4-40-3-8-10-pack.html) 

[ PRT-10927 ]

These nylon standoffs are 3/8\" long and tapped for a 4-40 screw. These are great for mounting your board in an enclosure, or ...

[ [\$3.75] ]

[![Silicone Bumpers - Large (10x16.5mm, 4 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/1/6/0/10594-01.jpg)](https://www.sparkfun.com/silicone-bumpers-large-10x16-5mm-4-pack.html)

### [Silicone Bumpers - Large (10x16.5mm, 4 pack)](https://www.sparkfun.com/silicone-bumpers-large-10x16-5mm-4-pack.html) 

[ COM-10594 ]

Rubber feet raise your PCB or project up off your desk. This helps prevent short circuiting from bits of scrap wire floating ...

[ [\$1.10] ]

[![Standoff - Metal Hex (4-40; 3/8\"; 10 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/5/4/10463-01.jpg)](https://www.sparkfun.com/standoff-metal-hex-4-40-3-8-10-pack.html)

### [Standoff - Metal Hex (4-40; 3/8\"; 10 pack)](https://www.sparkfun.com/standoff-metal-hex-4-40-3-8-10-pack.html) 

[ PRT-10463 ]

Metal Hex Male/Female standoffs. #4-40 thread with 3/8\" shank and 3/16\" thread length. Can be stacked to create any length. ...

[ [\$4.75] ]

[![Screw - Phillips Head (1/2\", 4-40, 10 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/4/1/10452-02.jpg)](https://www.sparkfun.com/screw-phillips-head-1-2-4-40-10-pack.html)

### [Screw - Phillips Head (1/2\", 4-40, 10 pack)](https://www.sparkfun.com/screw-phillips-head-1-2-4-40-10-pack.html) 

[ PRT-10452 ]

Standard Philips-head 4-40 screws. They are 1/2\" long and come in packs of ten. This is the screw size we use in most of the ...

[ [\$1.60] ]

[![Screw - Phillips Head (1/4\", 4-40, 10 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/4/7/10453-01.jpg)](https://www.sparkfun.com/screw-phillips-head-1-4-4-40-10-pack.html)

### [Screw - Phillips Head (1/4\", 4-40, 10 pack)](https://www.sparkfun.com/screw-phillips-head-1-4-4-40-10-pack.html) 

[ PRT-10453 ]

There are your standard Philips-head 4-40 screws. They are 1/4\" long and come in packs of ten. This is the screw size we use ...

[ [\$1.75] ]

[![Screw - Phillips Head (1\", 4-40, 10 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/3/9/10450-02.jpg)](https://www.sparkfun.com/products/10450)

### [Screw - Phillips Head (1\", 4-40, 10 pack)](https://www.sparkfun.com/products/10450) 

[ PRT-10450 ]

Standard Philips-head 4-40 screws. They are 1\" long and come in packs of ten. This is the screw size we use in most of the ho...

**Retired**

[![Screw - Phillips Head (3/4\", 4-40, 10 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/4/0/10451-02.jpg)](https://www.sparkfun.com/products/10451)

### [Screw - Phillips Head (3/4\", 4-40, 10 pack)](https://www.sparkfun.com/products/10451) 

[ PRT-10451 ]

Standard Philips-head 4-40 screws. They are 3/4\" long and come in packs of ten. This is the screw size we use in most of the ...

**Retired**