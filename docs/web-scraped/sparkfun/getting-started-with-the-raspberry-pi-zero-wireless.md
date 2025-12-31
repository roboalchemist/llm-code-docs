# Source: https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless

## Introduction

The Raspberry Pi is a popular Single Board Computer (SBC) in that it is a full computer packed into a single board. Many may already familiar with the [Raspberry Pi 3](https://www.sparkfun.com/products/13825) and its predecessors, which comes in a form factor that has become as highly recognizable. The Raspberry Pi comes in an even smaller form factor. The introduction of the Raspberry Pi Zero allowed one to embed an entire computer in even smaller projects. This guide will cover the latest version of the Zero product line, the [Raspberry Pi Zero - Wireless](https://www.sparkfun.com/products/14277), which has an onboard WiFi module. While these directions should work for most any version and form factor of the Raspberry Pi, it will revolve around the Pi Zero W.

[![Raspberry Pi Zero W](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/2/3/2/14277-01.jpg)](https://www.sparkfun.com/raspberry-pi-zero-w.html)

### [Raspberry Pi Zero W](https://www.sparkfun.com/raspberry-pi-zero-w.html) 

[ DEV-14277 ]

The Raspberry Pi Zero W is still the Pi you know and love, but at a largely reduced size of only 65mm long by 30mm wide and s...

[ [\$16.50] ]

[![Raspberry Pi Zero W (with Headers)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/5/9/15470-Raspberry_Pi_Zero_WH-01.jpg)](https://www.sparkfun.com/raspberry-pi-zero-w-with-headers.html)

### [Raspberry Pi Zero W (with Headers)](https://www.sparkfun.com/raspberry-pi-zero-w-with-headers.html) 

[ DEV-15470 ]

The Raspberry Pi Zero W is still the Pi you know and love, but at a largely reduced size of only 65mm long by 30mm wide and n...

[ [\$17.60] ]

If you\'re looking for a starter pack, this kit includes everything you need to start using your Pi Zero W.

[![SparkFun Raspberry Pi Zero W Basic Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/2/3/3/1/9/23091-_KIT-_01.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-zero-w-basic-kit-kit-23091.html)

### [SparkFun Raspberry Pi Zero W Basic Kit](https://www.sparkfun.com/sparkfun-raspberry-pi-zero-w-basic-kit-kit-23091.html) 

[ KIT-23091 ]

The SparkFun Raspberry Pi Zero W Basic Kit provides everything you need to start with this miniaturized Pi without breaking t...

[ [\$53.50] ]

### Required Materials

To follow along with this tutorial, you will need the following items:

- [Raspberry Pi Zero W Basic Kit](https://www.sparkfun.com/products/23091)
- Monitor
- Keyboard
- Mouse (optional but suggested)
- USB hub (for more than one USB device)

### Suggested Reading

Here are some tutorials you may find interesting before continuing:

[](https://learn.sparkfun.com/tutorials/single-board-computer-benchmarks)

### Single Board Computer Benchmarks 

How to set up different benchmarking programs on single board computers or computing modules and run them. The results for various generations are shown on the subsequent pages.

[](https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images)

### SD Cards and Writing Images 

How to upload images to an SD card for Raspberry Pi, PCDuino, or your favorite SBC.

[](https://learn.sparkfun.com/tutorials/raspberry-gpio)

### Raspberry gPIo 

How to use either Python or C++ to drive the I/O lines on a Raspberry Pi.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

### Raspberry Pi SPI and I2C Tutorial 

Learn how to use serial I2C and SPI buses on your Raspberry Pi using the wiringPi I/O library for C/C++ and spidev/smbus for Python.

## Looking to get hands-on with Raspberry Pi?

We\'ve got you covered!

[![SparkFun Raspberry Pi Zero W Camera Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/0/3/4/16327-SparkFun_Raspberry_Pi_Zero_W_Camera_Kit_V2-01.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-zero-w-camera-kit.html)

### [SparkFun Raspberry Pi Zero W Camera Kit](https://www.sparkfun.com/sparkfun-raspberry-pi-zero-w-camera-kit.html) 

[ KIT-16327 ]

The SparkFun Raspberry Pi Zero W Camera Kit provides you with a pan/tilt camera controlled via a Raspberry Pi Zero W.

[ [\$99.95] ]

[![Raspberry Pi Zero W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/3/2/14277-01.jpg)](https://www.sparkfun.com/raspberry-pi-zero-w.html)

### [Raspberry Pi Zero W](https://www.sparkfun.com/raspberry-pi-zero-w.html) 

[ DEV-14277 ]

The Raspberry Pi Zero W is still the Pi you know and love, but at a largely reduced size of only 65mm long by 30mm wide and s...

[ [\$16.50] ]

[![Raspberry Pi Zero W (with Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/5/9/15470-Raspberry_Pi_Zero_WH-01.jpg)](https://www.sparkfun.com/raspberry-pi-zero-w-with-headers.html)

### [Raspberry Pi Zero W (with Headers)](https://www.sparkfun.com/raspberry-pi-zero-w-with-headers.html) 

[ DEV-15470 ]

The Raspberry Pi Zero W is still the Pi you know and love, but at a largely reduced size of only 65mm long by 30mm wide and n...

[ [\$17.60] ]

[![SparkFun Raspberry Pi Zero W Basic Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/3/1/9/23091-_KIT-_01.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-zero-w-basic-kit-kit-23091.html)

### [SparkFun Raspberry Pi Zero W Basic Kit](https://www.sparkfun.com/sparkfun-raspberry-pi-zero-w-basic-kit-kit-23091.html) 

[ KIT-23091 ]

The SparkFun Raspberry Pi Zero W Basic Kit provides everything you need to start with this miniaturized Pi without breaking t...

[ [\$53.50] ]

[See all Raspberry Pi products](https://www.sparkfun.com/categories/233)

## Hardware Overview

Let\'s go over some of the most noticeable differences between the Raspberry Pi Zero (and Pi Zero W) and the Raspberry Pi 3.

Both boards are identical in features except that the W has built in Wifi and Bluethooth. Getting started with the Pi Zero board can be a little more cumbersome than with the Pi 3 because many of the connectors need adapters to connect to standard size connectors. Otherwise, to get started, all you need is a uSD card with a Raspberry Pi image on it and power.

### Mini HDMI

Unlike the previous models of the Raspberry Pi which use a standard HDMI connector, the Zero uses a mini HDMI connector to save space. To connect the Zero to a monitor or television, you will need a mini HDMI to HDMI adapter or [cable](https://www.sparkfun.com/products/14274).

[![raspberry pi zero mini hdmi](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/miniHDMI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/miniHDMI.jpg)

### USB On-the-Go

The Raspberry Pi 3 and other models have traditionally had 2-4 standard size female USB connectors, which allowed for all variety of devices to connect including mice, keyboards, and WiFi dongles. Again to save space, the Zero has opted for a [USB On-the-Go (OTG)](https://en.wikipedia.org/wiki/USB_On-The-Go) connection. The Pi Zero uses the same Broadcom IC that powered the original Raspberry Pi A and A+ models. This IC connects directly to the USB port allowing for OTG functionality, unlike the Pi B, B+, 2 and 3 models, which use an onboard USB hub to allow for multiple USB connections.

To connect a device with a standard male USB connection, you will need a [USB OTG cable](https://www.sparkfun.com/products/14276). Plug the microUSB end into the Pi Zero, and plug your USB device into the standard female USB end.

[![raspberry pi zero usb otg](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/usb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/usb.jpg)

For use with other standard USB devices, it is recommended that you use a powered USB hub. Wireless keyboard and mouse combos work best as they have one USB dongle for both devices.

**Heads up!** You can use the [USB to micro-b adapter](https://www.sparkfun.com/products/14567) if you need to access the USB port on the Pi Zero.\
\

[![USB to micro-b Adapter between USB Device and Raspberry Pi Zero](https://cdn.sparkfun.com/r/300-300/assets/parts/1/2/7/0/1/14567-USB_to_Micro-B_Adapter-09.jpg)](https://www.sparkfun.com/products/14567)

### Power

Like other Pis, power is provided through a microUSB connector. Voltage supplied to the power USB should be in the range of **5-5.25V**.

[![raspberry pi zero power](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/power.jpg)

### microSD Card Slot

Another familiar interface is the microSD card slot. Insert your microSD cards that contains your Raspberry Pi image file here.

[![pi zero microSD card slot](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/uSDcard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/uSDcard.jpg)

### WiFi and Bluetooth

As with the Raspberry PI 3, the Zero W offers both 802.11n wireless LAN and Bluetooth 4.0 connectivity. This frees up many of the connections that would have been made over USB, such as a WiFi dongle and a USB keyboard and mouse if substituting a Bluetooth keyboard/mouse.

### Camera Connector

The Raspberry Pi Zero V1.3+ and all Zero Ws have an onboard camera connector. This can be used to attach the [Raspberry Pi Camera module](https://www.sparkfun.com/products/14028). However, the connector is a 22pin 0.5mm and different than the standard Pi. You will need a different [cable](https://www.sparkfun.com/products/14272) to connect the camera to the Pi Zero W.

[![pi zero camera connector](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/camera.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/camera.jpg)

### GPIO

As with all other models of the Raspberry Pi, there are a plethora of GPIO pins broken out, many of which other other functionality such as I^2^C. If you are using the GPIO header, you may want to consider soldering [headers](https://www.sparkfun.com/products/14275) to it.

[![raspberry pi zero gpio](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/gpio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/gpio.jpg)

### Additional Connections

Last, you may notice two sets of thruhole pads labeled TV and Run. The TV pads allow you to connect an RCA jack to the board instead of using the HDMI out. The Run pins connect to the chips reset pin and will either turn the board off or turn it back on once it has been shutdown. Connecting a button here is a good way to power cycle your board.

[![TV pads](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/tv.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/tv.jpg)

------------------------------------------------------------------------

For a complete description of each pin on the GPIO header and all the connectors on the PI Zero, consult the graphical datasheet below.

[![raspberry pi zero graphical datasheet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/6/PiZerov2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/PiZerov2.pdf)

*Click on the image to view the PDF.*

## Hardware Assembly

Depending on your use case, setup for the Pi Zero can be minimal, or it can be cumbersome due to smaller connectors on the Zero and the adapters needed to connect standard devices such as mice, keyboards, and monitors.

### Monitor

1.  To attach the Pi Zero to a Monitor or TV that has an HDMI input, attach a miniHDMI to HDMI cable or adapter to the miniHDMI connector on the Pi Zero. Connect the other end to the HDMI port on your monitor or television.

2.  Connect the USB OTG cable to the Pi Zero via the microUSB connector. If you have a keyboard/mouse combe, attach your dongle to the standard female USB end. If you have a separate mouse and keyboard, you will need a USB hub to attach both tto the USB OTG cable.

3.  Make sure that you have a valid Raspberry Pi image on your microSD card (more on this later). Insert the microSD card into the microSd slot.

4.  Power your Pi Zero via the microUSB power input.

------------------------------------------------------------------------

There are a few other connectors to point out but we won\'t be using. The Pi Zero has a 40 pin GPIO connector on the board that matches the pinout of the standard Pi 3. You can solder wires, headers or Pi Hats to this connector to access the GPIO pins or even power. The camera connector will allow you to connect the Raspberry Pi camera although it is worth noting that the connector is a 22pin 0.5mm and different than the standard Pi and will need a different [cable](https://www.sparkfun.com/products/14272) to connect the camera to the Pi.

## Installing the OS

Before powering on your Pi Zero W you\'ll need to flash an image of the Raspberry Pi OS (or if you prefer, a third party operating system that work with Raspberry Pi) to the microSD card included with the Basic Kit. The Raspberry Pi Foundation created a great tool called the Raspberry Pi Imager that makes downloading and flashing an OS image a microSD card simple. This section briefly goes over how use that tool to upload an image of the Raspberry Pi OS on your microSD card.

### Option 1: Raspberry Pi Imager

The Raspberry Pi Imager tool makes selecting and writing an image of a Raspberry Pi-compatible operating system to a microSD card way easier than it was in the past. All you need to do is select the OS and storage device and the tool takes care of the rest. Download the tool from Raspberry Pi\'s software page here:

[Get the Raspberry Pi Imager Tool Here!](https://www.raspberrypi.com/software/)

Once the tool is downloaded and installed on your computer, follow the steps below to complete the image installation:

- **Insert** the microSD card and SD adapter into the appropriate port on your computer.
- Open the **Raspberry Pi Imager**.
- Click the **Choose OS** button to select your preferred Operating System (this tutorial will use the default Raspberry Pi OS).
- Click the **Choose Storage** button and select your microSD\'s drive location.
- Click **Write**.

Writing the OS to the microSD card can take a few minutes depending on which version was selected and the speed of the port/microSD card. Once the write is finished, the tool should automatically perform the software ejection for the microSD card so you can remove it once the process completes.

**Note:** The software page also includes a link to a range of alternate operating systems for users who prefer to download and install them manually. For help manually writing and installing images, check out [this tutorial](https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images).

**Note:** At the time of writing, we initially recommended using NOOBS. However, the software is not currently being supported anymore. [From the Raspberry Pi Foundation:](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system)

> NOOBS, or New Out Of the Box Software to give it its full name, was an SD card-based installer for Raspberry Pi computers; we no longer recommend or support using NOOBS. Going forward, please use Raspberry Pi Imager.

For users that are still interested in NOOBS, you can check out the [GitHub repo](https://github.com/raspberrypi/noobs).

### Option 2: .img File

If you want something other than the basic Raspbian install or other options found on NOOBS, you will need to install your own image on the uSD card. This method is slightly more involved because you need a special \*.img file that not only puts your files on the card, but also sets up things like making the card bootable. The Raspberry Pi foundation has a handful of [images](https://www.raspberrypi.org/downloads/) like Ubuntu, OSMC (Open Source Media Center), and even Windows 10 IOT Core. A Google search will find many more including specialized images for certain tasks. If you\'ve never worked with Raspberry Pi before, we recommend Raspian. You can download the latest version using the link below.

[Download Latest Version of Raspbian](https://www.raspberrypi.com/software/operating-systems/)

**Heads up!** When installing Raspbian, you do not need to worry about which model Raspberry Pi you are using. However, other Raspberry Pi image files, such as OSMC or RetroPi, have images that are designed for different models, often distinguishing between the Pi 2 or 3 and older models. Because those Pis use a slightly different processor than the Zero, these images won\'t work. The good news is that the Zero line uses the same chip as the older Raspbery Pi A/A+/B/B+ models, so there are still a lot of images out there for it. Visit [this link](https://en.wikipedia.org/wiki/Raspberry_Pi#Specifications) for a breakdown of each Pi model.

To install your own image on your card, we recommend software called [Etcher](https://etcher.io/). These guys have taken all the different steps needed and put them all in one piece of software to take care of everything. Download your image, then run the program, select your image, select your uSD card drive, and then hit flash. Once it is done, remove your card and you are good to go. Once the image is installed, insert the card into the board and apply power.

[![Etcher Install](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/EtcherInstall.gif)](https://etcher.io/)

For Mac users, the [ApplePi Baker Software](https://www.tweaking4all.com/software/macosx-software/macosx-apple-pi-baker/) is a great way to upload a new image to an SD card. It will ask for an admin password upon startup. Select the SD card on the left plane, then upload your image iundet the Pi Ingrediants: IMG Recipe section. Click Restore Backup, wait for the progress bar to finish, and you\'re done. The program even ejects the card you, so can yank it right out and insert it into your Pi.

[![applepi baker](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/6/applepi_baker.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/applepi_baker.png)

For the rest of this tutorial, we\'ll assume you\'ve installed Raspbian either by installing the image directly or with Noobs. The tutorial should also work fine for most Linux based systems with a Graphical User Interface, but things might be in slightly different locations

## Using the Raspberry Pi OS

Now that you\'ve gotten your board up and running let\'s go over some basics of the Raspberry Pi OS. This section covers how to use the Pi via HDMI out to a monitor.

### Raspberry Pi OS

The Raspberry Pi OS is Linux based (to be specific it is a port of Debian Bullseye with the Raspberry Pi Desktop). Don\'t let that scare you too much. Gone are the days of having to remember lots of commands or that you need to type `:wq` to save and exit your text editor. The OS runs a desktop Graphical User Interface (GUI) similar to Windows or MacOS, and, while you will probably want to learn a few basic commands and shorcuts, you can usually get away with not using them.

#### Initial Boot

The first boot of the Pi with a fresh install of the OS takes a few minutes and the Pi will most likely restart at least once. Once the OS finishes initial setup, you should be greeted by a desktop setup similar to the image below:

[![Set Up Wizard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_PIXEL_Desktop_Init_Setup_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_PIXEL_Desktop_Init_Setup_1.png)

Follow the set up wizard to configure the location settings, set a new password, connect to WiFi, update the system and packages and more settings on the Pi. You can skip some of these steps but we strongly recommend at least setting the location and setting a new password. If you ever need to go back and update the settings, open them by going to the **Raspberry Pi Start Menu** \> **Preferences** \> **Raspberry Pi Configuration**.

[![Raspberry Pi Configuration from Start Menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_Configuration_Desktop.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_Configuration_Desktop.png)

This opens a pop up allowing you to update the region, monitor, keyboard, password, as well as turn on any peripheral interfaces like SPI and I^2^C.

[![Raspberry Pi Configuration](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/1/Preferences_Raspberry_Pi.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/1/Preferences_Raspberry_Pi.png)

**Warning:** We recommend changing your password from the default to secure your Raspberry Pi. Make sure to write down the password somewhere safe before saving! You can also change the username as well.

#### Update Software

In case you skipped the step in the set up wizard or need to update software packages in the future, we can update the software package on the Pi through the Command Line Interface (CLI). Access it by opening the terminal and type the following and hit [Enter]:

    language:bash
    sudo apt-get update

This command tells the Pi to retrieve the latest package information and tells the package manager what needs updating.

- `sudo` (also known as super user) is a command that you will see a lot, specifically with high security commands. It temporarily allows the user (if you're not already logged in as root) the ability to run these commands if your user name is in a list of users (\'sudoers\').

- `apt-get` is the package manager and `update` is the command we are giving it.

This downloads and upgrades all packages on the system and may take a while.

### Shutdown/Reboot

The desktop includes a standard shutdown button in the desktop main menu but you can also tell the Pi to shutdown through the CLI using this command:

    language:raspberrypi
    sudo shutdown -h now

- `shutdown` as you may guess, shuts down the machine. `now` tells it do perform the action immediately (`15` would tell the machine to shutdown in 15 minutes).

To reboot the Pi through the CLI send this command:

    language:bash
    sudo shutdown -r now

[][\[6\] ⚡**Warning:**](#shutdown) Removing power before properly shutting down will corrupt your Raspberry Pi\'s image. Make sure that you properly shut down before removing power from the Pi. Alternatively, you could write a [Python script to turn off the Pi using a GPIO](https://learn.sparkfun.com/tutorials/raspberry-pi-safe-reboot-and-shutdown-button).\
\

[](https://learn.sparkfun.com/tutorials/raspberry-pi-safe-reboot-and-shutdown-button)

### Raspberry Pi Safe Reboot and Shutdown Button 

April 20, 2020

Safely reboot or shutdown your Raspberry Pi to avoid corrupting the microSD card using the built-in general purpose button on the Qwiic pHAT v2.0!

### Other Useful Linux Commands

A few other useful commands for use in the terminal command line:

- `pwd` - Print Working Directory, if you not sure what folder you are in this will tell you where you are in the filesystem.

- `ls` - List, this will show you the contents of the folder. To show all files, including hidden ones, type `ls -a` to show all files/folders. Alternatively, typing `ls -al` will show you all files/folders as well as their permission settings.

- `cd` - this is how you change directories. `cd foldername` will move you to that folder. `cd ..` will back you up one level. `cd ~` will take you back to your home directory.

- `passwd` - this will allow you to change your password

- `man` - this stands for manual. Type man before a command to get a summary of how to use it.

- `nano` - this will open a basic text editor that is fairly easy to use.

## Troubleshooting

Having issues getting the Raspberry Pi to work? Check out this sticky note from the [Raspberry Pi Foundation\'s forum](https://www.raspberrypi.org/forums/index.php) for basic troubleshooting.

[Pi Foundation Forums: Basic Troubleshooting with the Raspberry Pi](https://www.raspberrypi.org/forums/viewtopic.php?t=58151)

Having problems with a piece of SparkFun hardware designed for the Raspberry Pi and interfacing it? Try checking out the [SparkFun forums](https://forum.sparkfun.com/) to see if we can assist.

[SparkFun Forums](https://forum.sparkfun.com/)