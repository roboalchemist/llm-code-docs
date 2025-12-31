# Source: https://learn.sparkfun.com/tutorials/flir-lepton-hookup-guide

## Introduction

**Note:** This tutorial was originally written for the FLiR Lepton \[KIT-13233\]. However, the FLiR Lepton 2.5 with Radiometry should function the same.

When our team found out that we'd be testing a Long Wave Infrared (LWIR) camera, there were two words that we couldn't stop saying: Predator Vision. That's right, we were finally going to be able to see the invisible world of heat, which would aid us greatly if we ever found ourselves hunting a team of special operatives in a remote jungle... or, you know, trying not to scald ourselves on a hot cup of tea.

As it happens, the [FLIR Lepton](https://www.sparkfun.com/products/13233) is an excellent little module for the price and Pure Engineering has done a bang up job spinning the breakout board and documentation.

[![FLiR Dev Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/4/0/9/13233-FLiR_Dev_Kit-01.jpg)](https://www.sparkfun.com/products/13233)

### [FLiR Dev Kit](https://www.sparkfun.com/products/13233) 

[ KIT-13233 ]

The FLiR Dev Kit includes a breakout as well as a Lepton® longwave infrared (LWIR) imager. With this kit you will be able to...

**Retired**

[![FLIR Radiometric Lepton Dev Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/4/5/14654-FLIR_Radiometric_Lepton_Dev_Kit-01.jpg)](https://www.sparkfun.com/products/14654)

### [FLIR Radiometric Lepton Dev Kit](https://www.sparkfun.com/products/14654) 

[ KIT-14654 ]

With the FLIR Radiometric Lepton Dev Kit you will be able to bring FLIR\'s thermal imaging reliability and power to your desir...

**Retired**

There are, however, a few minor "gotchas" in the setup process and so we figured it was best if we shared what we learned in playing with this thing. But first... A bit of theory\...

### Suggested Videos

*Having a hard time seeing the videos? Try viewing the videos in full screen mode.*

### Required Materials

To follow along with this tutorial, you will need the following hardware and software. You may not need everything though depending on what you have and your setup. Add the hardware to your cart, read through the guide, and adjust the cart as necessary.

#### Hardware

Today we'll be setting up the Raspberry Pi example code as provided by Pure Engineering and featured in our product videos. At a minimum, we'll be needing a [Raspberry Pi](https://www.sparkfun.com/products/13825)\... and not much else, actually. Just a handful of jumper wires as well as a monitor, keyboard, accompanying cables for your Raspberry Pi, and the FLIR Lepton camera of your choice.

Below is a wishlist of the suggested parts:

**Note:** To reduce the number of components used, you could wire the thermal camera straight to the Pi using [F/F jumper wires](https://www.sparkfun.com/products/11710). For a secure connection, you could also use [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) a custom Raspberry Pi hat using a prototyping board.\
\

[![Insulated GPIO Header - Female (PTH, 0.1in., 2x20-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/2/14017-07.jpg)](https://www.sparkfun.com/raspberry-pi-gpio-tall-header-2x20.html)

### [Insulated GPIO Header - Female (PTH, 0.1in., 2x20-Pin)](https://www.sparkfun.com/raspberry-pi-gpio-tall-header-2x20.html) 

[ PRT-14017 ]

This 2x20 \"tall\" header has the same number and spacing of pins as a Raspberry Pi and provides your board with the ability to...

[ [\$3.50] ]

[![Jumper Wires Premium 6\" F/F - 20 AWG (10 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/8/9/3/11710-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-f-f-20-awg-10-pack.html)

### [Jumper Wires Premium 6\" F/F - 20 AWG (10 Pack)](https://www.sparkfun.com/jumper-wires-premium-6-f-f-20-awg-10-pack.html) 

[ PRT-11710 ]

Jumper wires are awesome. Just a little bit of stranded core wire with a nice solid female connector on either end. They have...

[ [\$7.75] ]

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![SparkFun Snappable Protoboard](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/8/9/13268-01.jpg)](https://www.sparkfun.com/sparkfun-snappable-protoboard.html)

### [SparkFun Snappable Protoboard](https://www.sparkfun.com/sparkfun-snappable-protoboard.html) 

[ PRT-13268 ]

Sometimes it\'s nice to have a protoboard that\'s super long and skinny, super small, or just a bunch of holes. The SparkFun Sn...

[ [\$13.50] ]

**Heads up!** If you are getting the PureThermal 2: FLIR Lepton Smart I/O Board, the board does **not** include the FLIR Lepton camera module. However, this handles control of the camera and raw video data via USB. This is useful if you are attaching it to your computer and using it as a USB web camera.\
\

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![PureThermal 2 - FLIR Lepton Smart I/O Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/6/8/14670-PureThermal_2-_FLiR_Lepton_Dev_Board-01.jpg)](https://www.sparkfun.com/products/14670)

### [PureThermal 2 - FLIR Lepton Smart I/O Board](https://www.sparkfun.com/products/14670) 

[ DEV-14670 ]

The PureThermal 2 Smart I/O Board is a hackable thermal USB webcam breakout for the FLIR Lepton® thermal imaging camera core...

**Retired**

For more information on setting up the smart I/O board with your computer, check out the following videos related to your setup to install the official Lepton app.\
\

- [Windows](https://www.youtube.com/watch?v=RBpH03lyEF8)
- [Mac OS](https://www.youtube.com/watch?v=B4GrIk5Nd6E)
- Raspberry Pi

#### Software

The example code has been tested on a Raspberry Pi model B, but it should work fine on any model so long as you have [Raspbian](http://www.raspberrypi.org/downloads/) installed.

[Raspberry Pi: Raspbian Image](http://www.raspberrypi.org/downloads/)

You will also need to install the QT dev tools and example. Check out the **Software** later in the tutorial for more information.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing. This tutorial will assume you have a little bit of Raspberry Pi knowledge. If the Pi is new to you, have no fear. You can visit our [Installing Raspbian and DOOM tutorial](https://learn.sparkfun.com/tutorials/setting-up-raspbian-and-doom), if you need a primer. Also helpful is our [Raspberry Pi GPIO tutorial](https://learn.sparkfun.com/tutorials/raspberry-gpio). The Lepton uses [SPI communication](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) to send its video stream and it uses an [I^2^C-like Communication](https://learn.sparkfun.com/tutorials/i2c) protocol as the control interface. If you are unfamiliar with either of those communication methods, please visit the corresponding tutorials.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/setting-up-raspbian-and-doom)

### Setting up Raspbian (and DOOM!) 

How to load a Raspberry Pi up with Raspbian \-- the most popular Pi Linux distribution. Then download, compile, install and run the classic: Doom.

[](https://learn.sparkfun.com/tutorials/raspberry-gpio)

### Raspberry gPIo 

How to use either Python or C++ to drive the I/O lines on a Raspberry Pi.

## Theory

Electromagnetic radiation is all around (and within, and throughout) us and is comprised of everything from gamma radiation on the high frequency end to radio waves on the low frequency end. While most imaging sensors detect radiation in the visible spectrum (wavelengths from 380 to 700 nanometers), long wave infrared sensors detect radiation from 900 to 14,000 nanometers. This is known as the infrared spectrum, and it accounts for most of the thermal radiation emitted by objects near room temperature.

[![Electromagnetic Spectrum](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/500px-EM_spectrum.svg.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/500px-EM_spectrum.svg.png)

*Electromagnetic spectrum with visible light highlighted. Image courtesy of Wikimedia Commons.*

The sensor inside the FLiR Lepton is a **microbolometer** array. Microbolometers are made up of materials which change resistance as they're heated up by infrared radiation. By measuring this resistance, you can determine the temperature of the object that emitted the radiation and create a false-color image that encodes that data.

Thermal imaging of this type is often used in building inspection (to detect insulation leaks), automotive inspection (to monitor cooling performance), and medical diagnosis. Also, because of its ability to produce an image without visible light, thermal imaging is ideal for night vision cameras.

When it comes to robotics, thermal cameras are especially useful heat detectors because the image that they produce (by virtue of being, well, an image) can be processed using the same techniques and software as visible light images. Imagine using something like [OpenCV](http://opencv.org/) to track, not just color centroids, but heat centroids! That's right, you could be building heat-seeking robots right in your own home!

In fact, what are we waiting for? Let me give you the tour\...

## Hardware Overview

Listed below are some of the characteristics of the FLIR Lepton\'s specs. The cells highlighted in blue indicate the slight differences between the two versions of the FLIR Lepton camera module.

                                 FLIR Lepton             FLIR Lepton v2.5 w/ Radiometry
  ------------------------------ ----------------------- ------------------------------------------------
  **Resolution (h x v)**         80 pixels x 60 pixels   80 pixels x 60 pixels
  **Spectral Range**             8µm to 14µm             8µm to 14µm
  **Horizontal Field of View**   51°                     50°
  **Thermal Sensitivity**        \< 50mK                 \< 50mK
  **Frame Rate**                 \< 9Hz                  \< 9Hz
  **Control Interface**          I2C                     I2C
  **Video Interface**            SPI                     SPI
  **Promised Time to Image**     \< 0.5 sec              \< 1.2 sec (*\~0.5 sec in real world testing*)
  **Integral Shutter**                                   ✓
  Radiometry                     14-bit pixel value      14-bit pixel value, Kelvin
  **Operating Power**            \~150 mW                \~150 mW

## Hardware Hookup

⚡ **Warning:** It is worth mentioning that while the Lepton module isn't particularly sensitive to electrostatic discharge, it is a complex and relatively pricey component. You might want to take a few precautions while working with it so you don't accidentally zap it.

### Circuit Diagram

Connect the FLIR breakout to the Raspberry Pi GPIO according to the diagram below. If you need a refresher on how the GPIO pins are oriented, visit our [Raspberry Pi GPIO tutorial](https://learn.sparkfun.com/tutorials/raspberry-gpio#gpio-pinout). Make sure that your Lepton module is securely snapped into the socket on the breakout board.

[![Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/RPi-FLIR-Diag-FIXED.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/RPi-FLIR-Diag-FIXED.png)

**Heads up!** If you have issues getting the camera to work (i.e. you see a red square and no image) with pin 26, you may need to adjust the CS pin to pin 24 (next to the CLK pin) like this [tutorial from FLiR](https://lepton.flir.com/forums/topic/pylepton-overlay-guide-2-0-for-raspbian-pixel/).

There are several methods of connecting and mounting your system together. If you used a breadboard and LCD touchscreen with the Pi, your setup should look similar to the image below.

[![Raspbery Pi Flir Lepton Thermal camera Setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/9/Raspberry_Pi_FLIR_Lepton_Thermal_Imaging_Setup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/Raspberry_Pi_FLIR_Lepton_Thermal_Imaging_Setup.jpg)

Congratulations, that's the hardware part done. Now onto the software configuration!

## Software 

As I mentioned earlier, you'll want to have the Raspbian OS installed on your Raspberry Pi. Boot it up, and open the [Terminal](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) program. Our first matter of business will be enabling the Pi's SPI and I2C interfaces. Luckily, Raspbian makes this easy to do by including a utility called **raspi-config**. To run the utility just type:

    language:bash
    sudo raspi-config

You should be presented with the following screen as shown below. Click on the \"**Advanced Options**\" menu.

[![Raspberry Pi Software Configuration Tool Menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/9/2015-03-22-202105_1184x624_scrot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/2015-03-22-202105_1184x624_scrot.png)

*Having a hard time seeing the circuit? Click on the image for a closer look.*

Select SPI and follow the instructions on the following screens. After you\'ve completed the SPI steps, do the same thing for I2C. When you exit **raspi-config**, it will ask if you want to reboot. Go ahead and do it so that the changes we just made will stick.

[![Configure The Raspberry Pi\'s SPI and I2C](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/9/2015-03-22-202124_1184x624_scrot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/2015-03-22-202124_1184x624_scrot.png)

*Having a hard time seeing the circuit? Click on the image for a closer look.*

### QT Application

Pure Engineering's example code is a QT application so we'll need to get that dependency installed before we can compile it. Don't worry, it's easy to do. Make sure that the Pi has an Internet connection, and run the following command to install the QT dev tools:

    language:bash
    sudo apt-get install qt4-dev-tools

Which will look something like this\...

[![Command Prompt ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/9/2015-03-22-201434_1184x624_scrot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/2015-03-22-201434_1184x624_scrot.png)

### Raspberry Pi Video

Once installation is complete, go to the Pure Engineering [GitHub repo](https://github.com/PureEngineering/LeptonModule) to download the examples.

[GitHub \> GroupGets \> LeptonModule](https://github.com/PureEngineering/LeptonModule)

If you're familiar with git, you can do this from the command line. For most people, it's just as easy to browse to the above link, and click "Download ZIP". You can download the file to whatever directory you like, then `cd` to that directory in Terminal, and unzip it using the following command:

    language:bash
    unzip LeptonModule-master.zip 

[![Unzip LeptonModule](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/9/2015-03-22-202255_1184x624_scrot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/2015-03-22-202255_1184x624_scrot.png)

Now `cd` into the unzipped folder \"**LeptonModule-master**\". First, we need to \"make\" the Lepton SDK. Use the `cd` command to navigate to the \"**\.../software/raspberrypi_libs/leptonSDKEmb32PUB**\" directory and run the `make` command.

Once that process has completed, use the `cd ..` command twice to move back out of the folders. Then use the `cd` to move into the \"**\.../raspberrypi_video**\" directory. This directory contains all of the files you need to compile the example code. run `qmake && make`:

[![Compile](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/9/2015-03-22-202522_1184x624_scrot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/2015-03-22-202522_1184x624_scrot.png)

Congratulations! You\'ve just compiled the example code, and you\'re ready to run it. Simply type the following into your command line:

    language:bash
    sudo ./raspberrypi_video

**Troubleshooting Tip:** You may get an error like the one shown below: a red square in a blank window. If this is the case, *carefully* remove the Lepton module from the breakout board. That\'s right, pull it from the socket, while it\'s powered. Then (again, *very carefully*) pop it back into place. Images should start pouring in!\
\

[![Flir Lepton Red Box Error](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/9/2015-03-22-202835_1184x624_scrot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/2015-03-22-202835_1184x624_scrot.png)

\
Remember, if you have issues getting the camera to work with pin 26 on the Pi, you may need to adjust the CS pin to pin 24 (next to the CLK pin) like this [tutorial from FLiR](https://lepton.flir.com/forums/topic/pylepton-overlay-guide-2-0-for-raspbian-pixel/).

Aim the camera at something hot or step in front of it to begin viewing heat signatures!

[![Thermal Image of Nick drinking a cup of hot coffee](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/9/2015-03-22-202944_1184x624_scrot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/9/2015-03-22-202944_1184x624_scrot.png)

*Visualizing the insulating properties of my beard*