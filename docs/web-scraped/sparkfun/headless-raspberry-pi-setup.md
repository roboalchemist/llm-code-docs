# Source: https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup

## Introduction

A \"headless\" computer is one that operates without a monitor, keyboard, or mouse. The [Raspberry Pi](https://www.sparkfun.com/raspberry_pi) works great as an inexpensive computer that can help people learn to program and create fun, interesting projects (without many repercussions if you break something\--just reflash the SD card!). The one downside is that as a computer (as opposed to a microcontroller), it requires a monitor, keyboard, and mouse to work, which can quickly increase the costs of acquiring the necessary components.

[![Raspberry Pi setup with a monitor, keyboard, and mouse](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_RPi_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_RPi_Tutorial-01.jpg)

*To use a Raspberry Pi, you often need a monitor, keyboard, and mouse*

The Raspberry Pi can be extremely useful for projects that do not require a monitor, keyboard, or mouse. The downside is that setting up the Pi to connect to the Internet, expand the filesystem, and run code generally requires these computer accessories.

[![Headless Raspberry Pi project using just an LED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_RPi_Twitter_Monitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_RPi_Twitter_Monitor.jpg)

*An example of a simple headless Raspberry Pi project: [Twitter Monitor](https://learn.sparkfun.com/tutorials/raspberry-pi-twitter-monitor)*

This tutorial will show you three different ways you can configure your Raspberry Pi without the need for a monitor, keyboard, or mouse.

- **Serial Terminal** - This requires extra hardware in the form of a serial-to-USB adapter, but it is by far the most robust way to connect, as you are not relying on any network setup.
- **Ethernet with Static IP Address** - This method requires a Linux operating system to change some files on the Raspberry Pi image. You can give the Raspberry Pi a static IP address and then use an Ethernet cable (or WiFi) to log in.
- **WiFi with DHCP** - You will need to have access to your router to find your Raspberry Pi\'s IP address in order to log in via SSH. As a result, this may not be the best option in school or office environments.

Certainly, there are more ways to connect to the Raspberry Pi. These show three common approaches to get you started interacting with a headless operating system on the Pi.

### Required Materials

To follow along with this tutorial, you will need a Raspberry Pi, power supply, and micro SD card. Note that no monitor, keyboard, or mouse is required! Any extra hardware needed will be listed in the specific section.

**Note:** The [Raspberry Pi Zero W](https://www.sparkfun.com/products/14277) should also work with this tutorial, if you want a smaller option for your project.

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless)

### Getting Started with the Raspberry Pi Zero Wireless 

Learn how to setup, configure and use the smallest Raspberry Pi yet, the Raspberry Pi Zero - Wireless.

## Flashing the OS

The Raspberry Pi has several options available for operating systems. It\'s often recommended that beginners start with NOOBS, as that walks the user through the necessary steps of installing an operating system. However, it usually requires a monitor to see the selection process, so we\'ll be creating an image of Raspbian manually. Additionally, we\'ll be using Raspbian Lite, which saves us space and time by not including the desktop (i.e. the graphical interface). Because we\'re creating a headless image, we\'ll be doing everything through the command line!

To start, download the latest version of Raspbian Lite.

[Download Latest Version of Raspbian Lite](https://downloads.raspberrypi.org/raspbian_lite_latest)

**Note:** This tutorial was created with Raspbian Stretch Lite (version: March 2018). Using a different version may require performing different steps than what\'s shown in this tutorial. If you would like to download the March 2018 version of Raspbian Lite, it can be found below.\
\

[Raspbian Stretch (version: March 2018) Download (ZIP)](http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2018-03-14/2018-03-13-raspbian-stretch-lite.zip)

\

Unzip the **.zip** file using your program of choice. You should have a *2018-03-13-raspbian-stretch-lite.img* file in a new folder.

To flash the image to your SD card, we recommend the program [Etcher](https://etcher.io/). Download and install it. Plug your SD card into your computer (using a [microSD USB Reader](https://www.sparkfun.com/products/13004) if necessary), and run Etcher. It will walk you through selecting the OS image file, selecting your SD card reader, and then flashing it.

[![Using Etcher to flash an SD card](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/etcher_process.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/etcher_process.gif)

Once that\'s done, you will need to make a choice: how do you want to interact with your Raspberry Pi? Without a monitor, keyboard, and mouse, you have a few choices:

- **[Serial Terminal]()** - Requires extra hardware
- **[SSH with a Static IP Address]()** - Requires Linux to modify files on the SD card
- **[SSH with a Dynamic IP Address]()** - Requires access to your router to find the Raspberry Pi\'s IP address

## Serial Terminal

If you would like to access your Raspberry Pi using the least amount of software work, you will need some extra hardware. Two of the pins on the Raspberry Pi offer transmit and receive data for [serial communication](https://learn.sparkfun.com/tutorials/serial-communication). With a small change to a file on the boot sector of the SD card, a command line terminal will be broadcast over this serial line, and you can enter commands to control Linux, write programs, etc.

If the other methods do not work to gain access to your Raspberry Pi or you lose your video out signal, using the serial terminal is a great way to see if your Raspberry Pi is still working and to debug any problems you might have.

You will need a USB to serial converter for this to work. We recommend:

[![Jumper Wires - Connected 6\" (M/F, 20 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/6/1/2/12794-00.jpg)](https://www.sparkfun.com/jumper-wires-connected-6-m-f-20-pack.html)

### [Jumper Wires - Connected 6\" (M/F, 20 pack)](https://www.sparkfun.com/jumper-wires-connected-6-m-f-20-pack.html) 

[ PRT-12794 ]

These are 6\" long jumper wires terminated as male to female. Use these to jumper from any male or female header on any board....

[ [\$2.75] ]

[![SparkFun Beefy 3 - FTDI Basic Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/7/6/13746-01.jpg)](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html)

### [SparkFun Beefy 3 - FTDI Basic Breakout](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html) 

[ DEV-13746 ]

This is SparkFun Beefy 3 FTDI Basic Breakout for the FTDI FT231X USB to serial IC. The pinout of this board matches the FTDI ...

[ [\$18.95] ]

Alternatively, you could use a [USB to TTL Serial Cable](https://www.sparkfun.com/products/12977). Note that if you are using the Raspberry Pi Zero W, you will need to solder a [header](https://www.sparkfun.com/products/14275) onto the GPIO port.

**Caution!** The GPIO pins on the Raspberry Pi are NOT 5V tolerant. That means you must use a 3.3V USB-to-serial converter.

### Enable the Serial Terminal

In versions of the Raspberry Pi after 3 (e.g. 3 Model B, 3 Model B+, Zero W), the processor contains two hardware UARTs. One is dedicated to the Bluetooth module, while the other is a less-featured \"mini UART.\" This mini UART is broken out on pins 8 and 10 and can be used as a serial terminal into Linux.

The problem is that the mini UART\'s clock is tied to the variable clock speed of the graphics processing unit (GPU). We need to set a static system clock in order to use the mini UART as a serial terminal. This can potentially disable some features (e.g. overclocking or power-saving mode), but it should not affect normal operation. See [here](https://www.raspberrypi.org/documentation/configuration/uart.md) to learn more about the mini UART.

With your SD card still plugged into your computer, browse to the *boot* partition, and find the *config.txt* file.

[![config.txt in the boot partition](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_01.png)

Use your text editor of choice to modify the file (on Windows, something like [Notepad++](https://notepad-plus-plus.org/) is recommended). Add

    language:bash
    enable_uart=1

to the end of the document.

[![Add enable_uart=1 to config.txt](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_02.png)

Save and exit.

### Hardware Connections

Take a look at the pinout for the Raspberry Pi 3.

[![Raspberry Pi 3 pinout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Raspberry_Pi_3_Pinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Raspberry_Pi_3_Pinout.png)

You\'ll see that pins 8 and 10 are connected to UART transmit (TXD) and receive (RXD), respectively. We\'ll need to connect GND (Raspberry Pi) to GND (USB to serial converter), TXD to RXI, and RXD to TXO. Note that we do not need to connect any power pins (3.3V or 5V).

[![Raspberry Pi 3 serial terminal connections to FTDI board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Raspberry_Pi_Serial_Connections.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Raspberry_Pi_Serial_Connections.png)

### Log In

Connect the USB to serial converter to your computer, and connect the wall adapter to the Raspberry Pi\'s PWR (USB micro B) port.

[![Raspberry Pi connected to a computer using a USB to serial converter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_RPi_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_RPi_Tutorial-02.jpg)

Choose a serial terminal based on your operating system ([here are some options](https://learn.sparkfun.com/tutorials/terminal-basics/)).

If you are using Windows, you will need to know the COM port number connected to your USB to serial adapter, which can be found in the Device Manager.

[![PuTTY configuration to connect to a Raspberry Pi over serial](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_03.png)

Change the settings as necessary to match the following:

- **Baud rate:** 115200 bps
- **Data bits:** 8
- **Parity:** None
- **Stop bits:** 1
- **Flow Control:** None

Open the connection, and press [enter]. You should be presented with a login prompt.

[![Serial terminal connection to the Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_04.png)

Enter the following credentials (default login):

- **Username:** pi
- **Password:** raspberry

You should be logged in at the command prompt and ready to type Linux commands!

[![Logged in to the Raspberry Pi over a serial console](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_05.png)

## Ethernet with Static IP Address

If you do not want to use the serial terminal or want to be able to log in to your Raspberry Pi over a network connection, you can give your Pi a static IP address, connect it to your network (or to your computer via a crossover/Ethernet cable), and log in via SSH.

**Note:** Windows and Mac cannot access the filesystem partition of the Raspberry Pi image on the SD card. As a result, you will need access to a computer with a Linux operating system. If you don\'t have a Linux computer nearby, you can make a Live CD (or bootable USB drive) to temporarily boot into Linux to make the necessary file changes on the SD card. Once you have edited the necessary files, you can switch to another operating system.

### Set Up Static IP Address

Plug the micro SD card (with the flashed Raspbian image) into your Linux computer. Most modern versions of Linux should automatically mount both partitions (*boot* and *rootfs*). You will need superuser privileges to edit the files on *rootfs*. Open a command prompt and edit */etc/dhcpcd.conf* in *rootfs*.

Navigate to the *rootfs* directory (wherever your Linux distro has mounted it):

    language:bash
    cd /media/<USERNAME>/rootfs

Edit the *dhcpcd.conf* file:

    language:bash
    sudo nano /etc/dhcpcd.conf

Scroll down to the bottom of the file and add the following lines:

    language:bash
    interface eth0

    static ip_address=192.168.4.2/24
    static routers=192.168.4.1
    static domain_name_servers=192.168.4.1

[![Setting a static IP address on the Raspberry Pi rootfs partition](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_06.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_06.png)

Save and exit by pressing [ctrl] + [x ] and [y] when asked if you would like to save.

### Enable SSH

In 2016, much of the Internet slowed to a crawl as a result of the IoT DDoS attack brought about by the Mirai botnet. In response to vulnerable IoT systems with default username and password logins, the Raspberry Pi Foundation decided to disable the SSH connection by default on all future releases of Raspbian. As a result, we now need to enable SSH so we can log in over a network connection. You can read more about the reasonings for this [here](https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/).

Luckily, this is easy to do. With the SD card still plugged in, navigate to the *boot* partition and create a blank file named \"ssh\" in that directory.

Still in the console, enter the following commands:

    language:bash
    cd ../boot
    touch ssh

You should see an empty file named \"ssh\" appear in the root *boot* partition.

[![Create an empty ssh file in the boot partition to enable SSH connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_07.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_07.png)

Unmount the SD card from your host computer and insert it into the Raspberry Pi.

### Configure Your Host Computer\'s IP Address

Plug an Ethernet cable into the Raspberry Pi and the other end into your computer. Technically, we should be using a crossover cable, but since the late 1990s, most computers are capable of [automatically detecting and configuring for crossover](https://en.wikipedia.org/wiki/Ethernet_crossover_cable#Automatic_crossover).

[![Raspberry Pi connected to computer using an Ethernet cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_RPi_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_RPi_Tutorial-03.jpg)

Configure your host computer to have an Ethernet static IP address with the following properties:

    language:bash
    IP Address: 192.168.4.1
    Subnet Mask: 255.255.255.0
    Default Gateway: 192.168.4.1

Instructions to set up a static IP address for the following operating systems: [Windows](https://www.howtogeek.com/howto/19249/how-to-assign-a-static-ip-address-in-xp-vista-or-windows-7/), [Mac](http://www.macinstruct.com/node/550), [Linux (Ubuntu)](https://www.howtoforge.com/linux-basics-set-a-static-ip-on-ubuntu).

### Connect Over SSH

Secure Shell (SSH) gives us a terminal into an operating system over a network and encrypts the traffic, giving us a level of security. Depending on your host operating system, you have a number of options available to you.

#### Windows

[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) is an easy-to-use SSH, Telnet, and Serial terminal client. Open PuTTY, and set the *Host Name* to `192.168.4.2` and *Port* to `22`.

[![Using PuTTY to connect to a Raspberry Pi with a static IP address](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_08.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_08.png)

Click **Open**. If asked about chaching a host key, click **Yes**.

#### Mac and Linux

The easiest way to connect to another computer over SSH is to use the *ssh* command line tool built into most distributions of Linux and Mac OS. Simply open up a terminal and type:

    language:bash
    ssh 192.168.4.2

**Update:** Users may need to use `ssh pi@<"IP Address">`, where `pi` predefines the login *username*.

### Log In

Once SSH connects, enter the default login credentials:

- **Username:** pi
- **Password:** raspberry

You should be presented with a command prompt, if all goes well.

[![Logging into a Raspberry Pi over SSH](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_09.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_09.png)

## WiFi with DHCP

If you don\'t want to mess with extra hardware or use Linux to modify the Raspbian filesystem, then you may want to consider having the Raspberry Pi connect to your local WiFi access point, finding its IP address, and logging in over SSH.

**Note:** You will need access to your WiFi access point (or router) to determine your Raspberry Pi\'s IP address. In an enterprise environment (e.g. office or school), this might be difficult or impossible to accomplish without consulting with your IT department.

### Enable WiFi

With the SD card plugged into your computer, navigate to the *boot* partition. In the root directory, create a file named *wpa_supplicant.conf*. The next time you boot up your Raspberry Pi, this file will automatically be moved to the */etc/wpa_supplicant/* directory in the filesystem.

[![wpa_supplicant file in the Raspberry Pi boot partition](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_10.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_10.png)

Edit the file using your text editor of choice (on Windows, something like [Notepad++](https://notepad-plus-plus.org/) is recommended). Copy in the following text. Change **\\** to your ISO country code found [here](https://www.iso.org/obp/ui/#search) (for the United States, this is *US*). Change **\\** to the SSID of your WiFi network and **\\** to the WiFi network\'s password.

    language:bash
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=<YOUR TWO LETTER COUNTRY CODE>

    network=

Save and exit.

### Enable SSH

In 2016, much of the Internet slowed to a crawl as a result of the IoT DDoS attack brought about by the Mirai botnet. In response to vulnerable IoT systems with default username and password logins, the Raspberry Pi Foundation decided to disable the SSH connection by default on all future releases of Raspbian. As a result, we now need to enable SSH so we can log in over a network connection. You can read more about the reasonings for this [here](https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/).

In the *boot* partition, simple create an empty file with the name **ssh**.

[![Create an empty file named ssh in the boot partition to enable SSH](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_11.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_11.png)

Unmount the SD card from your host computer and insert it into the Raspberry Pi.

### Find the Raspberry Pi\'s IP Address

Power on your Raspberry Pi and wait for it to connect to your WiFi network. Open up your wireless router\'s configuration page (for example, by typing in *192.168.1.1* into a browser window). From there, find your router\'s DHCP lease table and make a note of your Raspberry Pi\'s IP address.

[![Screenshot of DHCP lease table with IP address for Raspberry Pi in WiFi router](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_12.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_12.png)

### Connect Over SSH

Secure Shell (SSH) gives us a terminal into an operating system over a network and encrypts the traffic, giving us a level of security. Depending on your host operating system, you have a number of options available to you.

#### Windows

[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) is an easy-to-use SSH, Telnet, and Serial terminal client. Open PuTTY, and set the *Host Name* to the IP address we found in the previous step and *Port* to `22`.

[![Using PuTTY to connect to a Raspberry Pi with a static IP address](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_08.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_08.png)

Click *Open*. If asked about caching a host key, click *Yes*.

#### Mac and Linux

The easiest way to connect to another computer over SSH is to use the *ssh* command line tool built into most distributions of Linux and Mac OS. Simply open up a terminal and type:

    language:bash
    ssh <IP ADDRESS FROM PREVIOUS STEP>

### Log In

Once SSH connects, simply enter the default login credentials:

- **Username:** pi
- **Password:** raspberry

You should be presented with a command prompt, if all goes well.

[![Connected to the Raspberry Pi over SSH wit PuTTY](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_13.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/0/Headless_Raspberry_Pi_screen_13.png)