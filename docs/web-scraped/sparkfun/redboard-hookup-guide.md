# Source: https://learn.sparkfun.com/tutorials/redboard-hookup-guide

## Introduction

The [SparkFun RedBoard](https://www.sparkfun.com/products/13975) is an Arduino-compatible development platform that enables quick-and-easy project prototyping. It can interact with real-world sensors, control motors, display information, and perform near-instantaneous calculations. It enables *anyone* to create unique, nifty projects like [two-wheel buggys](https://learn.sparkfun.com/tutorials/building-the-hub-ee-buggy), [custom music boxes](https://learn.sparkfun.com/tutorials/mp3-player-shield-music-box), and [dice gauntlets](https://learn.sparkfun.com/tutorials/dungeons-and-dragons-dice-gauntlet).

The RedBoard also serves as an excellent physical computing **learning platform**. We\'ve designed the RedBoard to be as easy-to-use as possible. It can be used to help teach both programming and electronics concurrently \-- two skills that are becoming significantly important in today\'s high-tech world.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

This tutorial aims to familiarize you with the RedBoard and help you get started using it. To begin we\'ll go over the ins and outs of the board, then we\'ll explain how to install in, and finally we\'ll go over how to use it with the Arduino software.

### Requirements

Of course, to follow along with this guide, you\'ll need a [RedBoard](https://www.sparkfun.com/products/13975). You\'ll also need a [mini-B-to-A USB cable](https://www.sparkfun.com/products/11301). The USB interface serves two purposes: it powers the RedBoard and allows you to upload programs to it.

You\'ll also need a computer \-- Mac, PC, or Linux will do \-- with the **Arduino IDE** installed on it. You can [download Arduino](http://arduino.cc/en/Main/Software) from their website. They\'ve got installation instructions there, but we\'ll also go over installation in this tutorial.

### Suggested Reading

The RedBoard aims to be as beginner-friendly as a microcontroller platform can be. You can get by using it without an innate knowledge of [Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) or [How Electricity Works](https://learn.sparkfun.com/tutorials/what-is-electricity) (but a little understanding wouldn\'t hurt!). Here are some subjects you should be familiar with, though:

- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [What is a Circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

## Meet the RedBoard

Below is an annotated image, and a quick overview, of all of the important stuff on the RedBoard:

[![Annotated image of RedBoard](https://cdn.sparkfun.com/assets/3/d/5/6/c/522f5cbd757b7f4f6e8b4567.png)](https://cdn.sparkfun.com/assets/3/d/5/6/c/522f5cbd757b7f4f6e8b4567.png)

### Supplying Power

The RedBoard can be powered via either the USB or barrel jack connectors. If you choose to power it via USB, the other end of the USB cable can be connected to either a computer or a (5V regulated) [USB wall charger](https://www.sparkfun.com/products/11456).

The power jack accepts a center-positive barrel connector with an outer diameter of 5.5mm and inner diameter of 2.1mm. Our [9V](https://www.sparkfun.com/products/298) and [12V adapters](https://www.sparkfun.com/products/9442) are good choices if you\'re looking to power the RedBoard this way. Any wall adapter connected to this jack should supply a **DC voltage between 7 and 15V**.

USB is usually the easiest way to power the board, especially when you\'re programming it, because the USB interface is required for uploading code too. Why would you use the barrel jack? Usually it\'s because you need more power. A USB port is usually only allowed to supply 500mA, if you need more than that a wall adapter may be your only choice.

[![USB and barrel jack wires connected](https://cdn.sparkfun.com/r/600-600/assets/7/e/d/a/3/5230c645757b7fe62c8b456d.png)](https://cdn.sparkfun.com/assets/7/e/d/a/3/5230c645757b7fe62c8b456d.png)

It is acceptable to connect both a barrel jack and a USB connector at the same time. The RedBoard has power-control circuitry to automatically select the best power source.

### Using the RedBoard Headers

All of the RedBoard\'s pins are broken out to 0.1\"-spaced female headers (i.e. connectors) on the outer edges of the board. Most pins are arranged into logical collections \-- there are headers dedicated to power inputs/outputs, analog inputs, and digital inputs.

The **digital pins** are the digital inputs and outputs of the Arduino. These are what you connect to buttons, LEDs, sensors, etc. to interface the Arduino with other pieces of hardware. Pins marked with a tilde (\~) can also serve as [analog outputs](https://learn.sparkfun.com/tutorials/pulse-width-modulation), which you can use to dim LEDs or run servo motors.

There are six **analog inputs** on the analog header. These pins all have [analog-to-digital converters](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion), which can be used to read in an analog voltage between 0 and 5V. These are useful if you need to read the output of a potentiometer or other analog sensors. All six analog pins can also serve as digital inputs and outputs.

The **power header** is mostly full of voltage supply pins. These pins are traditionally **used as power sources** for other pieces of hardware (like LEDs, potentiometers, and other circuits). The \'3.3V\' and \'5V\' pins are regulated 3.3V and 5V voltage sources. The \'GND\' pins are the common ground \-- the 0V reference for those voltage supplies. \'VIN\' is the input voltage, it\'ll be equal to the voltage of your input supply if you have a wall adapter connected. If nothing is connected to the barrel jack, and you\'re powering the board via USB, VIN should be around 5V.

#### Connecting to the Headers

There are a variety of wires, connectors, and other items that can be inserted into these headers to interface with the Arduino. [Jumper wires](https://www.sparkfun.com/products/11026) are a good option, if you want to connect the RedBoard up to other pieces of circuitry that may live on a breadboard.

[![RedBoard connected to breadboard via jumper wires](https://cdn.sparkfun.com/r/600-600/assets/0/9/9/4/e/5230c645757b7fa32c8b4568.png)](https://cdn.sparkfun.com/assets/0/9/9/4/e/5230c645757b7fa32c8b4568.png)

*A tangled assortment of [jumper wires](https://www.sparkfun.com/products/8431) run between the RedBoard headers and components on a [breadboard](https://www.sparkfun.com/products/11317). An [Arduino baseplate](https://www.sparkfun.com/products/11235) holds them all in one place.*

[Arduino shields](https://learn.sparkfun.com/tutorials/arduino-shields) are another popular way to interface with the RedBoard connectors. These Arduino-shaped boards piggyback onto the RedBoard, and connect to all four headers at once. Shields exist in hundreds of forms, they can add GPS, WiFi, MP3 decoding, and all sorts of other functionality to your Arduino.

[![Ethernet Shield on RedBoard](https://cdn.sparkfun.com/r/600-600/assets/f/9/8/b/b/5230c645757b7fb32d8b4568.png)](https://cdn.sparkfun.com/assets/f/9/8/b/b/5230c645757b7fb32d8b4568.png)

*An [Ethernet Shield](https://www.sparkfun.com/products/10864) piggybacks onto a RedBoard to help get it connected to the Internet.*

And there are plenty of other interfacing options too. If you have a 0.1\"-spaced connector, like a [Molex](https://www.sparkfun.com/products/9922), you can plug that right in. Or just [strip and cut](https://learn.sparkfun.com/tutorials/working-with-wire/how-to-strip-a-wire) some [wire](https://www.sparkfun.com/products/11367).

## Download/Install Arduino

Before you plug the RedBoard into your computer, you\'ll need to install Arduino first.

### Installing Arduino

To begin, head over to [Arduino\'s download page](http://arduino.cc/en/Main/Software) and grab the most recent, stable release of Arduino. Make sure you grab the version that matches your operating system.

### Download Arduino!

The installation procedure is fairly straightforward, but it varies by OS. Here are some tips to help you along. We\'ve also written a separate [Installing Arduino tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide) if you get really stuck.

#### Windows Install Tips

The Windows version of Arduino is offered in two options: an installer or a zip file. The **installer** is the easier of the two options, just download that, and run the executable file to begin installation. If you\'re prompted to install a driver during installation, select \"Don\'t Install\" (the RedBoard doesn\'t use the same drivers). Don\'t forget which directory it installs to (defaults to \"Program Files/Arduino\").

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

    sudo apt-get update && sudo apt-get install arduino arduino-core  

And other Linux distros aren\'t too dissimilar from that.

------------------------------------------------------------------------

With Arduino downloaded and installed, the next step is to plug the RedBoard in and install some drivers! Pretty soon you\'ll be blinking LEDs, reading buttons, and doing some physical computing!

## Install FTDI Drivers

Once you have downloaded and installed Arduino, it\'s time to **connect the RedBoard to your computer!** Before you can use the board, though, you\'ll need to install drivers.

### Windows Driver Installation

After initially plugging your RedBoard in, your computer will try to search for a compatible driver. It may actually succeed! The FTDI drivers are pretty common, so Windows Update may know a little something about them. If the drivers do automatically install, you should see a little bubble notification saying so:

[![Driver Success!](https://cdn.sparkfun.com/assets/4/1/7/3/b/522f9067757b7fd56d8b456b.png)](https://cdn.sparkfun.com/assets/4/1/7/3/b/522f9067757b7fd56d8b456b.png)

If your computer failed to find drivers, we\'ll have to install them manually. Check out our [Windows FTDI Driver Install guide](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers/windows---in-depth) for driver install instructions.

### Mac Driver Installation

If you\'re lucky, the FTDI drivers should automatically install on Mac OS X, otherwise you\'ll have to manually install the drivers. Check out the [Mac FTDI Driver Installation guide](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers/mac) for help installing the drivers.

[![Mac Driver installation](https://cdn.sparkfun.com/r/600-600/assets/1/3/a/0/a/522f96ed757b7f42098b4567.png)](https://cdn.sparkfun.com/assets/1/3/a/0/a/522f96ed757b7f42098b4567.png)

In short, the process involves heading over to the [FTDI driver website](http://www.ftdichip.com/Drivers/VCP.htm), and downloading the most up-to-date VCP drivers. Then you\'ll simply run the \"FTDIUSBSerialDriver_v2_2_18.dmg\" file you downloaded, and follow the installation prompts.

### Linux Driver Installation

Linux is actually pretty good about automatically installing the drivers. If you have any trouble, check out our [Linux FTDI Driver guide](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers/linux).

------------------------------------------------------------------------

Now it\'s time to breathe easy! You\'ll only have to run through this driver installation process once, the first time you connect the board to your computer. Now it\'s time to upload a sketch!

## Uploading Blink

Now it\'s finally time to **open up the Arduino software**. You\'ll be presented with a window that looks a little something like this:

[![Arduino IDE annotated](https://cdn.sparkfun.com/assets/8/4/5/b/d/52309c7e757b7f522d8b4567.png)](https://cdn.sparkfun.com/assets/8/4/5/b/d/52309c7e757b7f522d8b4567.png)

Lets upload a **Blink sketch** to make sure our new RedBoard setup is totally functional. Go up to the **File** menu in Arduino, then go to **Examples \> 01.Basics \> Blink** to open it up.

Before we can send the code over to the RedBoard, there are a couple adjustments we need to make.

### Select a Board

This step is required to tell the Arduino IDE *which* of the [many Arduino boards](https://learn.sparkfun.com/tutorials/arduino-comparison-guide) we have. Go up to the **Tools** menu. Then hover over **Board** and make sure **Arduino Uno** is selected.

[![Board Selection](https://cdn.sparkfun.com/assets/4/a/4/b/0/52309f4f757b7fbf2d8b4567.png)](https://cdn.sparkfun.com/assets/4/a/4/b/0/52309f4f757b7fbf2d8b4567.png)

### Select a Serial Port

Next up we need to tell the Arduino IDE which of our computer\'s serial ports the RedBoard is connected to. For this, again go up to **Tools**, then hover over **Serial Port** and select your RedBoard\'s COM port.

[![Port Selection](https://cdn.sparkfun.com/assets/b/e/0/0/c/52309f4f757b7fbd2d8b4567.png)](https://cdn.sparkfun.com/assets/b/e/0/0/c/52309f4f757b7fbd2d8b4567.png)

If you\'ve got more than one port, and you\'re not sure which of the serial ports is your RedBoard, unplug it for a moment and check the menu to see which one disappears.

### Upload!

With all of those settings adjusted, you\'re finally ready to upload some code! Click the **Upload** button (the right-pointing arrow) and allow the IDE some time to compile and upload your code. It should take around 10-20 seconds for the process to complete. When the code has uploaded, you should see something like this in your console window:

[![alt text](https://cdn.sparkfun.com/assets/a/0/5/7/0/5230a452757b7f512d8b4567.png)](https://cdn.sparkfun.com/assets/a/0/5/7/0/5230a452757b7f512d8b4567.png)

And if you look over to the RedBoard, you should see the blue LED turn on for a second, off for a second, on for a second, off for a second\...ad infinitum (at least until it loses power). If you want to adjust the blink speed, try messing with the \"1000\" value in the `delay(1000);` lines. You\'re well on your way to becoming an Arduino programmer!

### Something Wrong?

Uh oh! If you didn\'t get a \"Done Uploading\" message, and instead got an error, there are a few things we can double-check.

If you got an `avrdude: stk500_getsync(): not in sync: resp=0x00` error in your console window.

[![Upload error](https://cdn.sparkfun.com/assets/9/a/6/f/b/5230a5fa757b7fcf2d8b4567.png)](https://cdn.sparkfun.com/assets/9/a/6/f/b/5230a5fa757b7fcf2d8b4567.png)

Either your serial port or board may be incorrectly set. Again, make sure **Arduino Uno** is the board selection (under the \"Tools \> Board\" menu). The serial port is usually the more common culprit here. Is the Serial Port correctly set (under the \"Tools \> Serial Port\" menu)? Did the drivers successfully install? To double check your RedBoard\'s serial port, look at the menu when the board is plugged in, then unplug it and look for the missing port. If none of the ports are missing, you may need to go back to [driver installation](https://learn.sparkfun.com/tutorials/getting-started-with-the-redboard/install-ftdi-drivers).