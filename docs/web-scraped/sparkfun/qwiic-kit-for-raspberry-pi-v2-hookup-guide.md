# Source: https://learn.sparkfun.com/tutorials/qwiic-kit-for-raspberry-pi-v2-hookup-guide

## Introduction

**Note:** This tutorial is for the Qwiic Starter Kit for Rasberry Pi V2. For users with the Qwiic Starter Kit for Raspberry Pi V1, make sure to check out the [older tutorial](https://learn.sparkfun.com/tutorials/qwiic-kit-for-raspberry-pi-hookup-guide).

Welcome to the [Qwiic Kit for Raspberry Pi V2](https://www.sparkfun.com/products/21285) hookup guide. Here we are going to get started with some of the basics surrounding I^2^C and Python on your Raspberry Pi. Don\'t worry, we\'ve done most of the work with the Python Libraries we\'ve written for the boards in our Qwiic Kit. This kit should help you get started whether you just want to get data and display it on your Pi, display it on our OLED screen, or post it to the Internet.

[![SparkFun Qwiic Starter Kit for Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/0/6/9/21285-_KIT_SparkFun_Qwiic_Starter_Kit-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-starter-kit-for-raspberry-pi.html)

### [SparkFun Qwiic Starter Kit for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-starter-kit-for-raspberry-pi.html) 

[ KIT-21285 ]

The SparkFun Qwiic Kit for Raspberry Pi includes a shield with headers, three Qwiic-enabled breakout boards, and four cables ...

[ [\$61.95] ]

### Required Materials

To follow along with this tutorial, you will also need a few pieces of hardware listed in the wishlist. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Raspberry Pi

Single board computers with the Raspberry Pi 40-pin GPIO header will work. We\'ll be using a Raspberry Pi throughout this tutorial. If you have not worked with a Raspberry Pi, we recommend getting started with the Raspberry Pi desktop or starter kit. Below are a few options from the [catalog](https://www.sparkfun.com/categories/tags/raspberry-pi).

[![Raspberry Pi 4 Model B (4 GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/2/2/15447-Raspberry_Pi_4_Model_B__4_GB_-01.jpg)](https://www.sparkfun.com/raspberry-pi-4-model-b-4-gb.html)

### [Raspberry Pi 4 Model B (4 GB)](https://www.sparkfun.com/raspberry-pi-4-model-b-4-gb.html) 

[ DEV-15447 ]

The 4 GB Raspberry Pi 4 features the ability to run two 4k resolution monitors, to run true Gigabit Ethernet operations, all ...

[ [\$64.95] ]

[![SparkFun Raspberry Pi 4 Hardware Starter Kit - 4GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/5/16388-Raspberry_Pi_4_Hardware_Starter_Kit_-_4GB-01.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-hardware-starter-kit-4gb.html)

### [SparkFun Raspberry Pi 4 Hardware Starter Kit - 4GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-hardware-starter-kit-4gb.html) 

[ KIT-16388 ]

The SparkFun Raspberry Pi 4 Hardware Starter Kit provides a solid set of parts and instruction for working with the Pi 4 in a...

[ [\$164.95] ]

[![SparkFun Raspberry Pi 4 Basic Kit - 4GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/1/16384-SparkFun_Raspberry_Pi_4_Basic_Kit_-_4GB-01a.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-basic-kit-4gb.html)

### [SparkFun Raspberry Pi 4 Basic Kit - 4GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-basic-kit-4gb.html) 

[ KIT-16384 ]

The Raspberry Pi 4 Basic Kit includes everything you\'ll need to get up and running with the Raspberry Pi 4 4GB.

**Retired**

[![SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/3/16386-Raspberry_Pi_4_Desktop_Kit_-_4GB-01b.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html)

### [SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html) 

[ KIT-16386 ]

The SparkFun Raspberry Pi 4 Desktop Kit (4GB) includes everything you need to turn any monitor with an HDMI port into a deskt...

**Retired**

#### Optional Materials

You have several options when it comes to working with the Raspberry Pi. Most commonly, the Pi is used as a standalone computer, which requires a monitor, keyboard, and mouse (listed below). To save on costs, the Pi can also be used as a [*headless* computer](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup/all) (without a monitor, keyboard, and mouse). This setup has a slightly more difficult learning curve, as you will need to use the *command-line interface* (CLI) from another computer.

[![Raspberry Pi LCD - 7\" Touchscreen](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/4/4/13733-01.jpg)](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html)

### [Raspberry Pi LCD - 7\" Touchscreen](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html) 

[ LCD-13733 ]

This 7\" Raspberry Pi Touchscreen LCD provides you with the ability to create a standalone device that can be utilized as a cu...

[ [\$88.30] ]

[![Logitech K400 Plus Wireless Touch Keyboard](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/9/4/16300-Logitech_K400_Plus_Wireless_Touch_Keyboard-01.jpg)](https://www.sparkfun.com/logitech-k400-plus-wireless-touch-keyboard.html)

### [Logitech K400 Plus Wireless Touch Keyboard](https://www.sparkfun.com/logitech-k400-plus-wireless-touch-keyboard.html) 

[ WIG-16300 ]

The Logitech K400 Plus Wireless Touch Keyboard is a compact keyboard with an integrated touchpad that puts all your controls ...

[ [\$42.95] ]

[![Multimedia Wireless Keyboard](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/2/6/14271-02.jpg)](https://www.sparkfun.com/multimedia-wireless-keyboard.html)

### [Multimedia Wireless Keyboard](https://www.sparkfun.com/multimedia-wireless-keyboard.html) 

[ WIG-14271 ]

With Single-Board Computers (SBCs) on the rise, it is a good idea to have an easy way to interface with them. Operating on a ...

[\$29.95] [ [\$19.95] ]

### Suggested Reading

Before you get started, I recommend taking a look at some of our other tutorials and familiarizing yourself with some of these topics. We will end up working with the Raspberry Pi, Python programming language, and MQTT protocol to send data over the Internet.

[](https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images)

### SD Cards and Writing Images 

How to upload images to an SD card for Raspberry Pi, PCDuino, or your favorite SBC.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[](https://learn.sparkfun.com/tutorials/introduction-to-mqtt)

### Introduction to MQTT 

An introduction to MQTT, one of the main communication protocols used with the Internet of Things (IoT).

[](https://learn.sparkfun.com/tutorials/qwiic-phat-for-raspberry-pi-hookup-guide)

### Qwiic pHAT for Raspberry Pi Hookup Guide 

Get started interfacing your Qwiic enabled boards with your Raspberry Pi. The Qwiic pHAT connects the I2C bus (GND, 3.3V, SDA, and SCL) on your Raspberry Pi to an array of Qwiic connectors.

![Python Logo](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/3/python-logo-gray-bg.jpg)

## Qwiic Connect System

SparkFun\'s [Qwiic Connect System](https://www.sparkfun.com/qwiic) is a quick and easy way to connect I^2^C devices to your microcontroller. Because our Qwiic boards use a 4-pin JSH-SH connector, you don\'t need to solder. You just need a cable to connect your modules. The connector is polarized meaning you can\'t plug it in wrong. Additionally, you can daisy chain all your boards together.

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

I^2^C is a protocol that has been around for a while, it has a few advantages such as each device being on the same bus but each having a unique address. Messages are sent back and forth with an address and only the device with the correct address listens to the message. This is why we are able to daisy chain our sensors. Currently, a large number of sensors we find communicate over I^2^C, but what about the ones that don\'t? Well, some of our Qwiic board use other types of sensors and have a small microcontroller that reads the data and then outputs via I^2^C, so in other words you can make anything you want to be I^2^C. One thing to note is that each item on the bus must have its own address. Some sensors will have jumper pads that let you change the address (you usually have 2 or 4 options if this is the case), but not all do. This might make it difficult to have a lot of one sensor in a chain unless you have a dedicated [I^2^C mux](https://www.sparkfun.com/products/14685).

![no soldering](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/no-soldering.png)

### no soldering

Qwiic cables (4-pin JST) plug easily from development boards to sensors, shields, accessory boards and more, making easy work of setting up a new prototype.

![](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/polarized-connector.png)

### polarized connector 

There\'s no need to worry about accidentally swapping the SDA and SCL wires on your breadboard. The Qwiic connector is polarized so you know you'll have it wired correctly every time, right from the start.

![](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/daisy-chainable.png)

### daisy chain-able

It's time to leverage the power of the I^2^C bus! Most Qwiic boards will have two or more connectors on them, allowing multiple devices to be connected.

The Qwiic Connect System is designed to keep your projects moving. If you have I^2^C sensors that don\'t have a Qwiic connector on them, check out our [Qwiic adapter](https://www.sparkfun.com/products/14495). You might have to write your own Python library, but at least we\'ve made the connection easier for you.

## Hardware Overview

**[Revision Changes:](https://learn.sparkfun.com/tutorials/qwiic-kit-for-raspberry-pi-v2-hookup-guide#revision)** With the revision from the initial release of the the SparkFun Qwiic Starter Kit for Raspberry Pi, we have swapped out an individual board inside the kit, listed below. At the time of writing we used the Qwiic pHAT v1.0. The Qwiic pHAT v2.0 is functionally the same with additional features. Unfortunately, the CCS811 is EOL so the Environmental Combo Breakout CCS811/BME280 was removed from V2. Thus, a similar sensor (SGP40) was added. Since the BME280 is also broken out on the Atmospheric Sensor Breakout, it was also included in the kit.\
\

  ----------------------------------------------------------------------------------------------------------------
            Qwiic Kit for Raspberry Pi Kit SKU           Revision History
  ------------------------------------------------------ ---------------------------------------------------------
   [KIT-21285](https://www.sparkfun.com/products/21285)  \- Add Air Quality Sensor SGP40 (Qwiic).\
                                                         - Add Environmental Sensor Breakout - BME280 (Qwiic)\
                                                         - Add Additional Qwiic Cable\
                                                         - Remove Environmental Combo Breakout (CCS811/BME280).\
                                                         - Kit version number bumped up to V2.

   [KIT-16841](https://www.sparkfun.com/products/16841)  \- Switch to Qwiic pHAT v2.0

   [KIT-15367](https://www.sparkfun.com/products/15367)  \- Initial release with the Qwiic pHAT
  ----------------------------------------------------------------------------------------------------------------

Please refer to the following pictures if you are unsure.\
\

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![KIT-21285](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/21285-_KIT_SparkFun_Qwiic_Starter_Kit-_01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/21285-_KIT_SparkFun_Qwiic_Starter_Kit-_01.jpg)   [![KIT-16841](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/16841-SparkFun_Qwiic_Starter_Kit_for_Raspberry_Pi-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/16841-SparkFun_Qwiic_Starter_Kit_for_Raspberry_Pi-02.jpg%22%22)   [![KIT-21285](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/15367-SparkFun_Qwiic_Kit_for_Raspberry_Pi-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/15367-SparkFun_Qwiic_Kit_for_Raspberry_Pi-01.jpg)
  *KIT-21285*                                                                                                                                                                                                                    *KIT-16841*                                                                                                                                                                                                                                                *KIT-15367*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The hardware we are using for this kit (other than the Pi) is the [Qwiic pHAT V2.0](https://www.sparkfun.com/products/15945) which provides a Qwiic connector to your Raspberry Pi. This enables you to easily connect a variety of Qwiic-enabled Devices easily such as the [Proximity Sensor Breakout- VCNL4040](https://www.sparkfun.com/products/15177), [Atmospheric Sensor Breakout - BME280](https://www.sparkfun.com/products/15440), [Air Quality Sensor - SGP40](https://www.sparkfun.com/products/18345), and [Qwiic micro OLED breakout](https://www.sparkfun.com/products/14532).

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Proximity and Light Sensor (VCNL4040)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/15177-SparkFun_Proximity_Sensor_Breakout_-_20cm__VCNL4040__Qwiic_-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/15177-SparkFun_Proximity_Sensor_Breakout_-_20cm__VCNL4040__Qwiic_-02.jpg)   [![Temperature, Humidity, and Barometric Pressure Sensor (BME280)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/15440-SparkFun_Atmospheric_Sensor_Breakout_-_BME280__Qwiic_-01a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/15440-SparkFun_Atmospheric_Sensor_Breakout_-_BME280__Qwiic_-01a.jpg)   [![ Air Quality Sensor (SGP40)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/18345-SparkFun_Air_Quality_Sensor_Breakout_-_SGP40__Qwiic_-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/18345-SparkFun_Air_Quality_Sensor_Breakout_-_SGP40__Qwiic_-02.jpg)   [![MicroOLED Display](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/14532-SparkFun_Micro_OLED_Breakout__Qwiic_-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/14532-SparkFun_Micro_OLED_Breakout__Qwiic_-02.jpg)

  *Proximity and Light Sensor\                                                                                                                                                                                                                                                                                     *Temperature, Humidity, and Barometric Pressure Sensor\                                                                                                                                                                                                                                                                         *Air Quality Sensor\                                                                                                                                                                                                                                                                     *MicroOLED Display*
  (VCNL4040)*                                                                                                                                                                                                                                                                                                      (BME280)*                                                                                                                                                                                                                                                                                                                       (SGP40)*                                                                                                                                                                                                                                                                                 
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Hardware Hookup

Let\'s start with connecting the pHAT. The pHAT should fit on the Raspberry Pi like most Pi HATs, but it should also fit on compatible boards such as the [Nvidia Jetson Nano](https://www.sparkfun.com/products/15297), the [Google Coral board](https://www.sparkfun.com/products/15318), and others that use the standard 2x20 GPIO header. It will even work on the Raspberry Pi Zero W. Just line up the headers and connect the pHAT to your Raspberry Pi. If you have more questions on the Qwiic pHAT check out the [hookup guide](https://learn.sparkfun.com/tutorials/qwiic-phat-for-raspberry-pi-hookup-guide) for more information.

[![I2C Sensor connected to a Raspberry Pi via Qwiic pHAT](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Attaching_Qwiic-Enabled_Board_Raspberry_Pi_pHAT.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Attaching_Qwiic-Enabled_Board_Raspberry_Pi_pHAT.jpg)

Next, we are going to connect our boards. We\'ve given you a selection of different cable lengths to let you configure your boards however you like. So go ahead and daisy chain all your boards together (while you only need 1x Qwiic connector on the pHAT, you can use as many as you\'d like). It doesn\'t matter which order you connect them in (or which of the connectors on the board you use), as long as they all have a path to the Pi. Keep in mind that these cables are polarized and should only go in one direction (don\'t force it to go in the wrong direction). Your setup should look similar to the image below with the Qwiic-enabled devices daisy chained and stacked on a Raspberry Pi. Of course, you could also connect each board to each Qwiic connector as well.

[![Qwiic Enabled Boards Connected to a Pi via the Qwiic pHat](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Qwiic_Starter_Kit_V2_pHAT_Micro_OLED_Proximity_VCNL4040_Atmospheric_Humidity_Temperature_Pressure_BME280_Air_Quality__SGP40.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Qwiic_Starter_Kit_V2_pHAT_Micro_OLED_Proximity_VCNL4040_Atmospheric_Humidity_Temperature_Pressure_BME280_Air_Quality__SGP40.jpg)

When you are ready, connect the power supply and any peripherals (i.e. HDMI monitor, keyboard, mouse, etc.) to the Raspberry Pi.

**Note:** Make sure to watch where you place the Atmospheric Sensor - BME280. The sensor readings can be affected by the heat from the Raspberry Pi and can skew the ambient temperature sensor readings. If you are looking to measure the ambient temperature of the room, make sure to add some space between the Raspberry Pi and BME280.

## Configure Your Pi

We are going to assume you already have a Raspberry Pi up and running with Raspbian. We\'ll also assume that it is connected to the Internet. If not, check out our starter kits and tutorials on setting up a Raspberry Pi.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-4-kit-hookup-guide)

### Raspberry Pi 4 Kit Hookup Guide 

March 14, 2020

Guide for hooking up your Raspberry Pi 4 Model B basic, desktop, or hardware starter kit together.

Make sure to update the image so that we have the latest distribution. Enter the following commands in the [command line](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) individually to update your image.

    language:bash
    sudo apt-get update
    sudo apt-get dist-upgrade

**Note:** sudo stands for \"Super User Do\", it is a way to give you superuser powers from the command line. Be careful whenever using `sudo`.

### User Configuration Settings

Once you are set up, I highly recommend changing your password. At this point, we are going be dealing with the Internet of things and don\'t want unsavory characters sneaking into your system using the default login: (**username**: pi, **password**: raspberry).

The [**raspi-config** tool](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide/all#configuring-the-pi) is a quick way to change your password as well as setup the network, language, keyboard, etc. Type the following command using the [command line](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) and then go through the menus to update your information.

    language:bash
    sudo raspi-config

You\'ll want to enable the [I^2^C](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#i2c-on-pi) pins using the tool to read the sensors on the I^2^C bus.

[![Enabling I2C on a Pi](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/9/i2c-menu2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/9/i2c-menu2.png)

*Raspi-config for I^2^C*

**Note:** The previous Qwiic Kit for Raspberry Pi included the CCS811 which required you to use [I^2^C clock stretching](https://learn.sparkfun.com/tutorials/qwiic-kit-for-raspberry-pi-hookup-guide#i2c-clockstretch).

**Note:** Here are some more resources on setting up a Raspberry Pi including how to connect to the Pi through a serial connection as well as VNC into the Pi remotely. This can be handy if you want to update things in the future without having to lug out an extra monitor, keyboard, and mouse.\
\

[](https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images)

### SD Cards and Writing Images 

How to upload images to an SD card for Raspberry Pi, PCDuino, or your favorite SBC.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless)

### Getting Started with the Raspberry Pi Zero Wireless 

Learn how to setup, configure and use the smallest Raspberry Pi yet, the Raspberry Pi Zero - Wireless.

[](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup)

### Headless Raspberry Pi Setup 

Configure a Raspberry Pi without a keyboard, mouse, or monitor.

[](https://learn.sparkfun.com/tutorials/how-to-use-remote-desktop-on-the-raspberry-pi-with-vnc)

### How to Use Remote Desktop on the Raspberry Pi with VNC 

Use RealVNC to connect to your Raspberry Pi to control the graphical desktop remotely across the network.

## Python

**Notice:** This tutorial was written with Raspbian version \"June 2019\", Python version 3.7.3, and pip 19.1.1 for Python v3.7. Other versions may affect how some of the steps in this guide are performed.

Python is a great language, we actually have a [great tutorial](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/all) on getting started with Python programming on a Raspberry Pi that covers everything from picking an editor and getting the code to run, to syntax and error messages. I highly recommend reading it if you plan on writing your own code. If you just plan on running the example code and maybe making a few changes, we\'ll go through a few basic things here.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

June 27, 2018

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

### Indentation

In many programming languages, we indent things to make things easier to read. In Python, those indents are part of the code. Instead of putting brackets around your loop or `if()` statements, you just [indent that entire chunk](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/programming-in-python#indent) with a leading whitespace. In other words, you have to make sure your indents are correct. I also recommend not using your keyboard\'s [TAB] button to indent as various programs will read it differently (and usually incorrectly).

### Commenting

Another thing to keep in mind is comments. In Python, the symbol \"`#`\" is used to denote that the line is a comment. Unlike many other languages there is [no official multi-line comment](https://dbader.org/blog/python-multiline-comment) available. So you\'ll just have to get use to typing `#` for each line when writing large comments.

### Python Versions and Installing PIP

There are 2 [commonly used Python versions](https://wiki.python.org/moin/Python2orPython3). Even after Python 3 came out many people continued to use 2.7 for many years. Part of the reason is that Python 3 improved on some things and in the process made it not backwards compatible. For our example we will be using Python 3.7 (and the code will not run on 2.7). To see what version of Python your Pi is using, open a [command line](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) and type each of the following commands individually to check.

    language:bash
    python --version
    python -m pip --version

If you are not using Python 3, then we\'ll need to open the **\*.bashrc** file and add an alias.

First, you will need to update the python installation package by running the following command to install pip for Python 3. Execute the following commands.

    language:bash
    sudo apt-get install python3-pip

Type the following command to open the file.

    language:bash
    nano ~/.bashrc

Then add the following lines at the end. That should tell the computer whenever you want to run `python` to look for the file located at `/usr/bin/python3`.

    language:bash
    alias python='/usr/bin/python3'
    alias pip=pip3

[![Alias Python 3 and pip3](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/8/screen_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/8/screen_01.png)

To exit nano type [CTRL] + [X] and then hit [Y] when it asks you if you want to save and then [ENTER]. You can now either reboot or type the following to force the Pi to run the **\*/.bashrc** file again.

    language:bash
    source ~/.bashrc

Once adjusted, type the following command to ensure that pip is up to date.

    language:bash
    python -m pip install --upgrade pip

## Python Library

We will also need to install the Qwiic Python libraries. This will automatically download a folder containing all the **Qwiic_Py** files and dependencies to your Raspberry Pi. Run the following command to [automatically install](https://github.com/sparkfun/qwiic_py#installation) the modules for the Qwiic sensors and micro OLED. To ensure that you are installing to the correct path for Python 3, make sure that you use `pip3`.

    language:bash
    sudo pip3 install sparkfun_qwiic

**Tip:** If you need to uninstall the library and start from scratch, simply use the `uninstall` with the command. This is also for users that have the libraries installed and what to \"upgrade\" to the latest versions.\
\

``` bash
sudo pip3 uninstall sparkfun_qwiic
```

## Setting Up MQTT and Cayenne

MQTT is a messaging protocol that works great for IoT devices. Devices can post to a topic, and/or subscribe to a topic to receive information. Alex wrote a tutorial all about [MQTT](https://learn.sparkfun.com/tutorials/introduction-to-mqtt), which is a great read if you are unfamiliar with MQTT. Amongst other things, our setup is going to act as an MQTT client and publish information to an online service called Cayenne.

[](https://learn.sparkfun.com/tutorials/introduction-to-mqtt)

### Introduction to MQTT 

November 7, 2018

An introduction to MQTT, one of the main communication protocols used with the Internet of Things (IoT).

### Cayenne

What is Cayenne? [Cayenne](https://developers.mydevices.com/cayenne/features/) is a product from [myDevices](https://mydevices.com/) that allows you to not only display data on a dashboard but also set up triggers, monitor devices, control devices, etc. You can view your home\'s temperature remotely from their site (or app), but you can also tell it to text you when the temperature goes below 40 so you can figure out why your furnace isn\'t working. But don\'t worry, none of the exercises in this tutorial require you to give myDevices any money (or even a credit card).

+:---------------------------------------------------------------------------------------------------------------------------------------------------------------:+:---------------------------------------------------------------------------------------------------------------------------------:+
| [![Cayenne](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/cayenne-login-logo.png)](https://developers.mydevices.com/cayenne/features/) | [![myDevices](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/MyDevices_Logo.png)](https://mydevices.com/) |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| *Cayenne and myDevices Logos Courtesy of myDevices*                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

If you have not already, the first thing to do is make an account. Head over to Cayenne to sign up by clicking on the link below using one of the Raspberry Pi\'s Internet browsers. If you have an account, just make sure to [login in](https://accounts.mydevices.com/auth/realms/cayenne/protocol/openid-connect/auth?response_type=code&scope=email+profile&client_id=cayenne-web-app&state=JEDXXhKNBC84BFaPGkye8xacaefPvbwT99sCMLVP&redirect_uri=https%3A%2F%2Fcayenne.mydevices.com%2Fauth%2Fcallback).

[Log In with Cayenne](https://accounts.mydevices.com/auth/realms/cayenne/protocol/openid-connect/auth?response_type=code&scope=email+profile&client_id=cayenne-web-app&state=JEDXXhKNBC84BFaPGkye8xacaefPvbwT99sCMLVP&redirect_uri=https%3A%2F%2Fcayenne.mydevices.com%2Fauth%2Fcallback)

Once you have an account we\'re going to start by setting up the Raspberry Pi. This is a good introduction that provides you with some information on your Pi (RAM usage, temperature, network speed). It also allows you to remotely reset or shutdown you Pi, toggle I/O pins and even give you the IP address of your Pi. That is one of the nice things about Cayenne, it doesn\'t define devices based on IP address or network. You provide a small script and your Pi basically tells Cayenne where it is. This is helpful if you loose power, reset your device etc., and need to know the IP address to log back in remotely.

### Adding a Device in Cayenne

You\'ll be greeted with a few devices. Select the Raspberry Pi.

[![Set Up Pi Cayenne](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/7/Qwiic_Pi_Cayenne.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/7/Qwiic_Pi_Cayenne.jpg)

You\'ll be prompted with an image of the Raspberry Pi before continuing on. Hit on the **next** button.

[![Set Up Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/7/Set_Up_Your_Pi_Cayenne.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/7/Set_Up_Your_Pi_Cayenne.jpg)

You\'ll be provided with a few options. We\'ll be following option 2. Follow the instructions provided (Cayenne has very good [instructions in when setting up your Raspberry Pi](https://www.youtube.com/watch?time_continue=84&v=Qx0IHv-UR-0)).

[![Set Up via option 2 serial terminal](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/7/Terminal_SSH_Option_2_Cayenne.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/7/Terminal_SSH_Option_2_Cayenne.jpg)

At this point you should have a working Cayenne account. Type (or copy and paste using your mouse\'s right click) the first command and hit the [ENTER] button. The command will begin executing. When it is done, type (or copy and paste) the second command and hit the [ENTER] button. The process may take a few minutes. When the the command is finished executing, your Raspberry Pi will automatically restart.

After the reboot, open the browser back up and head back to Cayenne. Next, go back to adding a new device or widget. This time you are going to select the blue \"**Bring Your Own Thing**\" button.

[![Cayenne Device](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/7/NewDevice-Bring-Your-Own-Thing-Cayenne.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/7/NewDevice-Bring-Your-Own-Thing-Cayenne.png)

This will provide you with your MQTT username, password, and client ID, as well as the server information for our project. We\'ll use this information later. You might want to do this on your Pi which will make it easier to copy and paste these values into your code.

## Example Code

We\'ve written some example code to read the sensor data and display a few sensor values to the micro OLED. In your terminal window, type the following to download the demo code from the [GitHub repository](https://github.com/sparkfun/Qwiic-Kit-for-Pi).

    language:bash
    git clone https://github.com/sparkfun/Qwiic-Kit-for-Pi.git

Then navigate to folder by typing the following command in the command line.

    language:bash
    cd Qwiic-Kit-for-Pi/v2

[![Open example via Command Line](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Qwiic-Kit-Pi-Python-Demo-Command-Line-Path.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Qwiic-Kit-Pi-Python-Demo-Command-Line-Path.png)

You can also navigate to the folder **/home/pi/Qwiic-Kit-for-Pi/v2** to open the example in your favorite Python editor. In this case, we use opened the code in the Thonny editor.

[![Run Example via Python Editor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Raspberry_Pi_Qwiic_Starter_Kit_Python_Thonny_Cayenne.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Raspberry_Pi_Qwiic_Starter_Kit_Python_Thonny_Cayenne.png)

We recommend opening the example code in a Python editor to follow along before running the demo.

## Reading the Sensor Data

Now that we have everything physically hooked up and ready to go, we can set up our sensors and start reading data. First, the code will need to run through the condition statement to give the sensor values some time to take samples from the environment. At the top of the code, we set up a flag (i.e. `initialize`) and counter (i.e. `n`) to keep track of whether or not we have just started the Python script. Further down in the main code under the `for` loop, we\'ll take a few readings over a certain period of time. Once we have taken a few values, we\'ll update the flag so that we can take the reading once through the for loop. The variable `u` is used as a counter for logging data with Cayenne after a certain period of time later on in the code.

    language:python
    #These values are used to give BME280 and SGP40 some time to take samples and log data to Cayenne
    initialize=True
    n=2
    u=0
    .
    .
    .

            if initialize==True:
                print ("Initializing: BME280 and SGP40 are taking samples before printing and publishing data!")
                print (" ")

            else:
                #print ("Finished initializing")
                n=1 #set n back to 1 to read sensor data once in loop

            for n in range (0,n):
                #print ("n = ", n) #used for debugging for loop
                .
                .
                .

                #Give some time for the BME280 and SGP40 to initialize when starting up
                if initialize==True:
                    time.sleep(10)
                    initialize=False

### Reading the Sensors Values

Python does not require you to initialize and type your variables, we just get to go ahead and use them. We\'ve highlighted most of the user functions in the main code under the `for` loop below as well as a few of the configuration functions.

    language:python
                #Proximity Sensor variables - these are the available read functions
                proximity = prox.get_proximity()
                ambient = prox.get_ambient()
                white = prox.get_white()
                close = prox.is_close()
                .
                .
                .

                #BME280 sensor variables
                pressure = bme.get_reference_pressure() #in Pa
                altitudef = bme.get_altitude_meters()
                humidity = bme.read_humidity()
                tempf = bme.get_temperature_fahrenheit()
                .
                .
                .

                #SGP40 sensor variable
                voc_index = my_sgp40.get_VOC_index()
                .
                .
                .

Now that we\'ve read all our data, let\'s figure out what we want to do with it all. Our different outputs will each display a different set of variables based on the application. Feel free to comment out any variables you are not using in your code using a \"`#`\" or choose to display different variables. The actual code has a lot more variables and functions listed that you probably won\'t need.

## Displaying Data to Your Pi

Once we\'ve read the data from the 3 sensors it is time to display that information on the Pi\'s console, the OLED screen, and send the information to be displayed by Cayenne.

Let\'s dig into the code a bit deeper. This section goes over how to send the serial data to your Raspberry Pi\'s terminal window. The output can be displayed through a Python Editor\'s console.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Output via Command Line](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Demo-Command-Line-Sensor-Output_Running.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Demo-Command-Line-Sensor-Output_Running.png)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Demo-Thonny-Editor-Running.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Demo-Thonny-Editor-Running.png)
  *Running Demo via Command Line*                                                                                                                                                                                                                                                  *Running Demo via Thonny Editor*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Click on images for a closer look!*

### Comments and Libraries

Starting at the very first line you\'ll see a line of code that looks like a comment (comments start with `#`). This line actually tells us that we will by using Python 3 which is what is used for the Qwiic Pi libraries. After the header comment is a line to import a few libraries to help us keep things clean between Python 2 and Python 3. Next, we are going to add in a few libraries including an MQTT client, our Qwiic library, the time library, and the system library.

### Definitions

If you scroll down a bit you\'ll, see our Qwiic board definitions. As we add more libraries you\'ll want to periodically download those updates, each sensor has its own **\*.py** file or module. Inside that file you should find the class definition as well as all the functions. We can then setup that device in our code (the example code has already done this, but if you want to add new sensors from new libraries you\'ll need to do this yourself). Don\'t forget the `begin()` call to get your sensor up and running.

Then we get to the main part of our code, which is in a `while()` loop. This will loop forever (unless we exit out). Here is where we define and read the variables from the sensors as we talked about earlier. We do this every time through the loop so we always have new data. Next, we\'ll get into printing the data to the screen. We\'ve selected some of the variables to print out as well as the time. When you run this code, this information will all display on the console.

    language:python
    #printing time and some variables to the screen
    #https://docs.python.org/3/library/time.html
    #print (time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())) #24-hour time 
    print (time.strftime("%a %b %d %Y %I:%M:%S%p", time.localtime())) #12-hour time

    print ("BME280 \t | Temperature: %.1f \xb0F" %tempf)
    #print ("BME280 \t | Temperature: %.1f \xb0C" %tempc)
    print ("BME280 \t | Humidity: %.1f %%RH" %humidity)
    print ("BME280 \t | Pressure: %.2f hPa" %(pressure/100))
    #print ("BME280 \t | Altitude: %.2f m" %altitudem)
    print ("BME280 \t | Altitude: %.2f ft" %altitudef)

    print ("VCNL4040 | Distance Value: %.2f " %proximity)
    print ("VCNL4040 | Ambient Light: %.2f" %ambient)

    print ("SGP40 \t | VOC Index: %.2f" %voc_index)

    print (" ") #blank line for easier readability

## Displaying Data to Your OLED

Next, we are going to look at the Qwiic micro OLED screen. The OLED module should have the same functions as our OLED Arduino library, but they might look a bit different for Python. Let\'s start with a few basic commands\...

[![Qwiic micro OLED](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/2/7/6/2/14532-SparkFun_Micro_OLED_Breakout__Qwiic_-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/14532-SparkFun_Micro_OLED_Breakout__Qwiic_-02.jpg)

*Qwiic micro OLED Before Connecting to a Raspberry Pi*

### Initializing the Micro OLED

We start by defining our OLED screen like we did with our sensors at the top of the code as well as run the initilization.

    language:python
    oled = qwiic.QwiicMicroOLED()
    oled.begin()

### Clearing the Screen

Next, we are going to clear the screen. This actually will clear the entire buffer.

    language:python
    oled.clear(oled.ALL)

Then we can display the cleared screen. This will display what is in the buffer which at this point is nothing.

    language:python
    oled.display()

### Font Size

Next, we can set the font type. The module comes with 4 different fonts. Unless you just need to display 2-3 digits, I recommend sticking with font `0` or font `1` as they will give you enough room to display a few lines of information. This is the end of the commands we\'ll use to setup the screen at the beginning of the code

    language:python
    oled.set_font_type(1)

### Setting Cursor Position

When we are ready to actually print to the screen we\'ll set the cursor to the top left.

    language:python
    oled.set_cursor(0,0)

### Printing

Then we can print some text. When we print the temperature, we don\'t want to print all the decimal places, partly because the limit of the screen size. The \"int\" command takes the tempf variable and gives us an integer and then we can print that.

    language:python
    oled.print("Tmp:")
    oled.print(int(tempf))

If we want, we can move the cursor to a different line, print more data, etc.

### Displaying

Finally, we will want to display all of this to the screen.

    language:python
    oled.display()

Also, keep in mind you might want to add delays when using an OLED screen so that the information isn\'t flickering too fast. In this case, we already have a 5 second delay each time through the loop so we should be fine.

Because we already have the variables setup, we just need to pick a few we think would be useful and print them to our OLED display. We can get about 3 lines of code here comfortably, but you might want to change the font type and just display temperature so that you can view it from more than 12 inches away. Of course, you could also adjust the size of the font to `0` and line spacing to read more sensor readings. However, it will be harder to read on the small screen.

## More with Cayenne

Now let\'s look at the Cayenne part of our code. Sending data to the service will enable you to view the sensor readings on the Cayenne\'s dashboard.

[![Sensor Data on Cayenne](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-IoT-Cayenne-Sensor-Output-Environment.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-IoT-Cayenne-Sensor-Output-Environment.png)

### Credentials

Let\'s start with the the definitions. Remember the username, password, and client ID we got earlier? We are going to copy and paste these into the code for the respective `username`, `password`, and `clientid`. Now our code knows not only to post to Cayenne, but who\'s account and what project this is for.

    language:python
    username = "______ENTER_MQTT_USERNAME____"
    password = "______ENTER_MQTT_PASSWORD____"
    clientid = "___ENTER_CAYENNE_CLIENTE_ID___"
    mqttc=mqtt.Client(client_id = clientid)
    mqttc.username_pw_set(username, password = password)
    mqttc.connect("mqtt.mydevices.com", port=1883, keepalive=60)
    mqttc.loop_start()

### Topics

Next, we are going to setup our topics. Topics are how MQTT keeps track of what is what. Each topic gets a different channel which is the number at the end of the line. Otherwise, the code is exactly the same for each topic name. We just need to figure out once at the beginning what pieces of data we want to send.

    language:python
    #set MQTT topics (we are not setting topics for everything)
    topic_bme_temp = "v1/" + username + "/things/" + clientid + "/data/1"
    topic_bme_hum = "v1/" + username + "/things/" + clientid + "/data/2"
    topic_bme_pressure = "v1/" + username + "/things/" + clientid + "/data/3"
    topic_bme_altitude = "v1/" + username + "/things/" + clientid + "/data/4"

    topic_prox_proximity = "v1/" + username + "/things/" + clientid + "/data/5"
    topic_prox_ambient = "v1/" + username + "/things/" + clientid + "/data/6"

    topic_sgp40_voc_index = "v1/" + username + "/things/" + clientid + "/data/7"

### Publishing Sensor Data to the Cloud

Once in the main part of the code, we are going to publish data to each of those topics so Cayenne will see this. You\'ll notice we are using the topics we set up earlier, as well as setting the payload to the variable we want to send with it. We will send this when the counter reaches about `900`. This is about 15 minutes assuming that we set the delay to 1 second ( i.e. `time.sleep(1)`, which is not shown below) so that we utilize the Cayenne service as necessary and to make it easier to handle our data over a long period of time.

    language:python
    if u==900:
        #send data every 15 minutes to Cayenne, 15 minutes => ~900 seconds; u=900
        #publishing data to Cayenne (we are not publishing everything)
        mqttc.publish (topic_bme_temp, payload = tempf, retain = True)
        mqttc.publish (topic_bme_hum, payload = humidity, retain = True)
        mqttc.publish (topic_bme_pressure, payload = pressure, retain = True)
        mqttc.publish (topic_bme_altitude, payload = altitudef, retain = True)

        mqttc.publish (topic_prox_proximity, payload = proximity, retain = True)
        mqttc.publish (topic_prox_ambient, payload = ambient, retain = True)

        mqttc.publish (topic_sgp40_voc_index, payload = voc_index, retain = True)
        u=0 #reset to 0 to begin logging data after another 15 minutes

## Let\'s Run the Code Already!

OK, now that we\'ve updated our code to submit data to our Cayenne account and figured out which variables we want to send where we can run the code. Make sure you save your code (with your Cayenne account information and any other changes you wanted to make). Then open a terminal window and navigate to the folder where your code is if you have not already. Type the following command and [ENTER] to run the script. Our code actually runs a loop until we decide to cancel the program [CTRL] + [C].

    language:bash
    python qwiic_kit_for_pi_demo.py

[![Run Demo via Command Line](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Run-Demo-Command.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Run-Demo-Command.png)

Or hit the **Run** button in your Python editor to start executing the script. To stop, simply click on the **Stop** button with your mouse.

[![Run Demo via Python Editor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Run-Demo-Thonny-Editor_Highlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Run-Demo-Thonny-Editor_Highlighted.png)

Assuming you don\'t get any errors you should see some of the sensor data displayed on your screen.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Output via Command Line](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Demo-Command-Line-Sensor-Output_Running.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Demo-Command-Line-Sensor-Output_Running.png)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Demo-Thonny-Editor-Running.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-Python-Demo-Thonny-Editor-Running.png)
  *Running Demo via Command Line*                                                                                                                                                                                                                                                  *Running Demo via Thonny Editor*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Click on images for a closer look!*

If you look at the microOLED, you will also notice some of the BME280 sensor data on the display.

[![BME280 sensor data on the micro OLED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Qwiic_Starter_Kit_Powered_Displaying_Demo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Qwiic_Starter_Kit_Powered_Displaying_Demo.jpg)

**Note:** If you do not give the sensors enough time to start, the output for the BME280 and SGP40 may appear to be incorrect.\
\

``` bash
Tue Dec 20 2022 03:49:31PM
BME280   | Temperature: 76.2 °F
BME280   | Humidity: 12.3 %RH
BME280   | Pressure: 1013.25 hPa
BME280   | Altitude: -5256.14 ft
VCNL4040 | Distance Value: 1.00 
VCNL4040 | Ambient Light: 602.00
SGP40    | VOC Index: 96.00
```

You\'ll notice that the pressure and altitude may be off by about *40,000 Pa* and *10,000 ft*, respectively. This is normal. You\'ll need to give the sensors a few seconds to take a readings from the environment. Note that the output for the altitude in feet is **calculated** from the (barometric) pressure measurement to report the [equivalent] [**pressure altitude**](https://en.wikipedia.org/wiki/Pressure_altitude) based on an [atmospheric model](https://en.wikipedia.org/wiki/Reference_atmospheric_model). If you want more details on this subject, look into how an [altimeter](https://en.wikipedia.org/wiki/Altimeter) works.\
\
The SGP40 will take longer for the sensor values to stabilize. For the best results, let the SGP40 run for 24hrs to generate a \"history\" of the average VOC gas concentration in the room. For more information on the SGP40, check out the [SGP40 datasheet](https://cdn.sparkfun.com/assets/e/6/2/6/d/Sensirion_Gas_Sensors_SGP40_Datasheet.pdf), [Sensirion VOC Index for Experts](https://cdn.sparkfun.com/assets/e/9/3/f/e/GAS_AN_SGP40_VOC_Index_for_Experts_D1.pdf), [Sensirion SGP40 Design In Guide](https://cdn.sparkfun.com/assets/6/c/d/d/7/GAS_SGP4x_Design-In_Guide_D1.pdf), and [SGP40 Quick Testing Guide](https://cdn.sparkfun.com/assets/d/c/d/b/0/Sensirion_Gas_Sensors_Datasheet_GAS_AN_SGP40_Quick_Testing_Guide_D1.pdf).

You will also start seeing the green boxes popping up on Cayenne as well so you can add them to your dashboard and move them around.

[![Sensor Data on Cayenne](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-IoT-Cayenne-Sensor-Output-Environment.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-IoT-Cayenne-Sensor-Output-Environment.png)

Congratulations, you now know how to read Qwiic sensors on a Pi, display data to your Pi, display data on the Qwiic micro OLED screen, and get that information to display on the web. Try adjusting the code to send data to the web at a slower rate or calibrate the sensor readings for stable readings. Keep checking the Qwiic_Py repo for more Python libraries for our Qwiic boards or write your own and start experimenting.

## Customizing Data on Cayenne\'s Dashboard

Once Cayenne sees this data, you should get a green box pop up on your Cayenne dashboard. Click the \"**+**\" in the upper right hand corner to permanently add it to your dashboard. By default, the values will be displayed with the associated channel. You will need to head into the settings and assign a name to be displayed for each channel in order to easily read the sensor data. You can also assign an icon to the channel, drag and drop widgets, and resize each window if you prefer.

[![Sensor Output on Cayennealt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Qwiic-Kit-Pi-Cayenne-Greenboxes.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Qwiic-Kit-Pi-Cayenne-Greenboxes.png)

After customizing according to your personal preference, the channels may look similar to the image below.

[![Customized Channels on Cayenne](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-IoT-Cayenne-Sensor-Output-Environment.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/2/Pi-Qwiic-Kit-IoT-Cayenne-Sensor-Output-Environment.png)

### Triggers and Notifications

While we are not going to go into this in this tutorial, Cayenne will also let you setup triggers and other things to text you, email you, or change things on any of your other devices (such as turn on an I/O pin on the Pi). You can start playing with Cayenne and its various features. Just make sure you don\'t overwhelm your inbox with notifications by sending texts 100 times per second.

[![Additional Features with Cayenne](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/7/Trigger.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/7/Trigger.PNG)

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[SparkFun Forums](https://forum.sparkfun.com/)

Below are a few additional troubleshooting tips and tricks when using the Qwiic devices with a single board computer.

### The Demo Code is Not Running

If you are having trouble running the demo code, there are a few reasons why the Python script may not be executing. Below are two common reasons why the demo code may not be running.

### Library Not Installed

If the libraries are not installed properly, you may receive an error similar to the output below when trying to execute the Python script:

    language:bash
     Traceback (most recent call last):
      File "./qwiic_kit_for_pi_demo.py", line 24, in <module>
        import qwiic 
    ImportError: No module named 'qwiic'

The `ImportError` indicates that the module(s) was not installed properly. Make sure that the Python modules are installed on the Pi in order to run the demo.

### I^2^C Bus Not Turned On

If you receive an error similar to the one below, there may be something with the interface settings for the I^2^C bus.

    language:bash
    Error:  Failed to connect to I2C bus 1. Error: [Errno 2] No such file or directory
    Error connecting to Device: 60, 'NoneType' object has no attribute 'write_byte'
    Error:  Failed to connect to I2C bus 1. Error: [Errno 2] No such file or directory
    Traceback (most recent call last):
      File "/home/pi/Qwiic-Kit-for-Pi/qwiic_kit_for_pi_demo.py", line 50, in <module>
        bme.begin()
      File "/home/pi/.local/lib/python3.7/site-packages/qwiic_bme280.py", line 160, in begin
        chipID = self._i2c.readByte(self.address, self.BME280_CHIP_ID_REG)
      File "/home/pi/.local/lib/python3.7/site-packages/qwiic_i2c/linux_i2c.py", line 142, in readByte
        return self.i2cbus.read_byte_data(address, commandCode)
    AttributeError: 'NoneType' object has no attribute 'read_byte_data'

The `Error: Failed to connect to I2C bus 1. Error: [Errno 2] No such file or directory` at the beginning of the error indicates that the I^2^C bus is not turned on. Make sure to use the [**raspi-config**](https://learn.sparkfun.com/tutorials/qwiic-kit-for-raspberry-pi-hookup-guide#configure-your-pi) to ensure that I^2^C bus is turned on as opposed to using the graphical user interface.

### I^2^C Device Not Connected

If you receive an error similar to the one below, it means that the bus is having issues reading a sensor.

    language:bash
    Error connecting to Device: 60, [Errno 121] Remote I/O error
    Traceback (most recent call last):
      File "/home/pi/Desktop/New/qwiic_kit_for_pi_demo_v2a.py", line 54, in <module>
        bme.begin()
      File "/usr/local/lib/python3.7/dist-packages/qwiic_bme280.py", line 216, in begin
        chipID = self._i2c.readByte(self.address, self.BME280_CHIP_ID_REG)
      File "/usr/local/lib/python3.7/dist-packages/qwiic_i2c/linux_i2c.py", line 185, in readByte
        raise ioErr
      File "/usr/local/lib/python3.7/dist-packages/qwiic_i2c/linux_i2c.py", line 178, in readByte
        data = self.i2cbus.read_byte_data(address, commandCode)
      File "/usr/local/lib/python3.7/dist-packages/smbus2/smbus2.py", line 433, in read_byte_data
        ioctl(self.fd, I2C_SMBUS, msg)
    OSError: [Errno 121] Remote I/O error

The `OSError: [Errno 121] Remote I/O error` indicates that an I^2^C device is not connected to the bus. Make sure that the sensors and micro OLED are securely connected to the I^2^C bus. The demo code currently checks to see if the SGP40, BME280, VCNL4040, and micro OLED are connected to the Pi\'s I^2^C bus before executing.

------------------------------------------------------------------------

### I\'m Having Problems Getting the Qwiic_Py Library.

If you are having trouble installing the modules, you may receive this error:

    Could not install packages due to an EnvironmentError: 404 Client Error: Not Found for url: https://www.piwheels.org/simple/sparkfun-qwiic/

Make sure that you are connected to the Internet to install the modules. Also, make sure that you are using Python3 and pip3 with the correct alias as [stated earlier](https://learn.sparkfun.com/tutorials/qwiic-kit-for-raspberry-pi-hookup-guide#configure-your-pi).

If you receive this error when trying to install the modules:

    language:bash
    ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.7/dist-packages/sparkfun_qwiic_i2c-0.8.3.dist-info'
    Consider using the `--user` option or check the permissions.

This is due to your user permissions. Make sure to use `sudo` with your command:

    sudo pip install sparkfun_qwiic

Or `--user` to the command.

    language:bash
    pip install --user sparkfun_qwiic

### I Don\'t Want to Use Cayenne or Another 3rd Party Service.

That\'s perfectly alright, you can delete or comment out all the relevant commands as that is not will not affect the rest of the code.

### I Can\'t Connect to Cayenne.

Make sure you have copied your `username`, `password`, and `clientid` correctly from Cayenne into the code before executing the Python script. Also, ensure that you have a reliable connection to the Internet.

### How Do I Add [\_\_\_\_\_] Qwiic Sensor?

Right now we only have a few Qwiic sensors in the Qwiic Py library, but we are looking to keep adding more. Please periodically check back to see if the sensor you want is available. You can also check the Internet for existing Python code for that sensor or write your own library.