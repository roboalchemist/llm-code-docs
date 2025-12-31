# Source: https://learn.sparkfun.com/tutorials/how-to-use-remote-desktop-on-the-raspberry-pi-with-vnc

## Introduction

If you like the idea of a headless computer setup for your [Raspberry Pi](https://www.sparkfun.com/raspberry_pi) (i.e. one without a keyboard, mouse, or monitor) but want access to the full graphical desktop, then you\'re in luck! By using a Virtual Network Computing (VNC) program, you can access a remote desktop over the network!

For schools and individuals that need to use the full desktop for certain applications (Scratch, creating your own graphical interface, etc.), using a VNC client to access your Raspberry Pi might be the way to go.

[![Using VNC to remotely access the Raspberry Pi desktop](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/VNC_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/VNC_Tutorial-02.jpg)

*Using RealVNC to access the Raspberry Pi\'s graphical desktop*

The good news is that Raspbian (the recommended Raspberry Pi operating system) comes with RealVNC installed by default. The bad news is that we need to enable it using some other means.

### Required Materials

To follow along with this tutorial, you will need a Raspberry Pi, power supply, and micro SD card. Note that no monitor, keyboard, or mouse is required!

**Note:** The [Raspberry Pi Zero W](https://www.sparkfun.com/products/14277) should also work with this tutorial, if you want a smaller option for your project.

### Optional Materials

All that being said, you can also use a keyboard, mouse, and monitor to enable the VNC server. Once you have enabled it, you will not need these accessories any more (unless you really want them).

[![Raspberry Pi LCD - 7\" Touchscreen](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/4/4/13733-01.jpg)](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html)

### [Raspberry Pi LCD - 7\" Touchscreen](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html) 

[ LCD-13733 ]

This 7\" Raspberry Pi Touchscreen LCD provides you with the ability to create a standalone device that can be utilized as a cu...

[ [\$88.30] ]

[![Multimedia Wireless Keyboard](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/2/6/14271-02.jpg)](https://www.sparkfun.com/multimedia-wireless-keyboard.html)

### [Multimedia Wireless Keyboard](https://www.sparkfun.com/multimedia-wireless-keyboard.html) 

[ WIG-14271 ]

With Single-Board Computers (SBCs) on the rise, it is a good idea to have an easy way to interface with them. Operating on a ...

[\$29.95] [ [\$19.95] ]

[![SmartiPi Touch](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/9/14059-06.jpg)](https://www.sparkfun.com/products/14059)

### [SmartiPi Touch](https://www.sparkfun.com/products/14059) 

[ PRT-14059 ]

The SmartiPi Touch is a case and stand for the official \[Raspberry Pi 7\" Touchscreen LCD\](https://www.sparkfun.com/products/1...

**Retired**

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

[] **Please note:** If you have trouble seeing any of the images throughout this tutorial, feel free to click on it to get a better look!

## Flashing the OS

The Raspberry Pi has several operating systems available for use, and beginners are often encouraged to use NOOBS to install the default Raspbian image. This guide will show you how to configure a headless version of Raspbian to be used with VNC. To do so, we\'ll be following along with parts of the [Headless Raspberry Pi Setup tutorial](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup), but note that we\'ll be using full *Raspbian* instead of *Raspbian Lite*, as we need the Linux X server that comes installed on the full version.

To start, download the latest version of Raspbian.

[Download Latest Version of Raspbian](https://downloads.raspberrypi.org/raspbian_latest)

**Note:** This tutorial was created with Raspbian Stretch (version: June 2018). Using a different version may require performing different steps than what\'s shown in this tutorial. If you would like to download the June 2018 version of Raspbian, it can be found below.\
\

[Raspbian Stretch (version: June 2018) Download (ZIP)](http://downloads.raspberrypi.org/raspbian/images/raspbian-2018-06-29/2018-06-27-raspbian-stretch.zip)

\

To flash the image to your SD card, we recommend the program [Etcher](https://etcher.io/). Download and install it. Plug your SD card into your computer (using a [microSD USB Reader](https://www.sparkfun.com/products/13004) if necessary), and run Etcher. Select your OS image file (no need to unzip it! just select your downloaded .zip file in Etcher), select your SD card reader, and click the **Flash!** button.

[![Using Etcher to flash an SD card](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/etcher_process.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/etcher_process.gif)

## Enable VNC

You will need to interact with your Pi in order to turn on the VNC server. To do this, you have several options:

- Connect a keyboard, mouse, and monitor. Click the **Terminal** icon on the top left of the desktop to open a terminal window.
- Follow [these instructions to open a terminal window over a Serial connection](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup#serial-terminal).
- Follow [these instructions to open a terminal window using SSH over Ethernet](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup#ethernet-with-static-ip-address)
- Follow [these instructions to open a terminal window using SSH over WiFi](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup#wifi-with-dhcp)

### (Optional) Install RealVNC

By default, Raspbian should come with a VNC server (RealVNC) installed. If you are using another operating system, you might need to install RealVNC. With most flavors of Debian (e.g. Raspbian is built on top of Debian), you should be able to use *apt-get* to install RealVNC. In a terminal, enter the following:

    language:shell
    sudo apt-get update
    sudo apt-get install real-vnc-server
    sudo apt-get install real-vnc-client

### Enable the VNC Server

You will need to go into the Raspberry Pi configuration tool to turn on the VNC server:

    language:shell
    sudo raspi-config

Select **Interfacing Option**, and then select **VNC**. On the next screen, select **Yes**, and press *enter* to save the changes.

[![Enable VNC on the Raspberry Pi](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-01.png)

Feel free to make any other changes you might like, including setting a new password and changing the keyboard layout.

Back in the *raspi-config* homescreen, press *right arrow* twice to select **Finish** and press *enter*.

## Use VNC Over a Local Network

If your host computer is on the same local network (e.g. connected to the same WiFi or Ethernet network), then you can make a direct VNC connection to your Raspberry Pi. This method has several up sides: it\'s the easier option, does not require signing up for a RealVNC account, and can be done on a closed network (i.e. one not connected to the Internet). The down side is that you must be on the same network to access your Pi (i.e. physically connected or through a VPN). This is a known as a *direct connection*.

If you want to to access your Raspberry Pi over the Internet, then see the [next section](https://learn.sparkfun.com/tutorials/how-to-use-remote-desktop-on-the-raspberry-pi-with-vnc#use-vnc-over-the-internet).

Still in your Raspberry Pi\'s terminal, enter the following command:

    language:shell
    ifconfig

Copy down the Raspberry Pi\'s IP address, which is given as a series of 4 numbers next to *inet*. If you are connected over WiFi, this will appear under the *wlan0* settings. If you are connected over Ethernet, this will appear under the *eth0* settings.

[![Find your Raspberry Pi\'s IP address](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-02.png)

On your host computer, head to the [RealVNC Viewer downloads page](https://www.realvnc.com/en/connect/download/viewer/) to download the VNC client (known as *VNC Viewer*) for your operating system. Install it, accepting all the defaults.

Open *VNC Viewer*. At the top address bar, enter the IP address of the Raspberry Pi (once again, make sure your host computer and Pi are on the same network!).

[![Connect to your Raspberry Pi from within the RealVNC VNC Viewer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/screen-03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-03.png)

Press *enter*, and click **Continue** when warned that \"VNC Server not recognized.\" You should be prompted with an *Authentication* window. If you did not change the login username and password for your Pi, your default login credentials are:

- **Username:** pi
- **Password:** raspberry

**Heads up:** it\'s highly recommended that you change your password! Anyone with access to your network could easily gain access to your Pi by trying the default username and password.

Once you successfully authenticate, you should be presented with your Raspberry Pi\'s graphical desktop. Now, you can do everything remotely as if you were sitting in front of your Pi with a keyboard, mouse, and monitor! If you hover your mouse over the top part of the window, you should see a drop-down box appear, giving you access to the various RealVNC settings, including closing the session.

[![Raspberry Pi desktop in the VNC viewer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/screen-04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-04.png)

## Use VNC Over the Internet

Using remote desktop on a local network is likely to offer a much faster and smoother experience, however, you can\'t necessarily guarantee you will have access to that network directly. Luckily, RealVNC allows us to log in to our computer over the Internet!

The other good news is that we don\'t have to go through the process of finding our Pi\'s IP address.

### Sign Up for a RealVNC Account

**Note:** Using RealVNC\'s cloud service means that we\'ll need to sign up for an account on their site. Also note that the cloud connection service is free for only non-commercial and educational purposes. See [RealVNC\'s pricing guide](https://manage.realvnc.com/en/pricing) for more details.

To start, sign up for an account (or sign in, if you already have one) on RealVNC\'s site [here](https://manage.realvnc.com/en/). Head to your *Account* page, and click **Activate** under the *Home* version of VNC Connect.

[![Signing up for a RealVNC account](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/screen-05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-05.png)

### Enable VNC Cloud Connection on the Pi

**Note:** You will need to have access to the graphical desktop for your Raspberry Pi for this next step. This can include using a keyboard, mouse, and monitor, or it can mean directly connecting with VNC over a local network. Only the *Enterprise* edition of RealVNC will allow you to enable the VNC cloud connection via command line.

Assuming you have VNC enabled on the Pi, click on the *VNC* logo in the top-right portion of the desktop. This will open the RealVNC settings window. In the top-right part of that window, click on the properties button, and select **Licensing\...**.

[![Enabling cloud connection for a Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/screen-06.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-06.png)

Leave *Sign in to your RealVNC account* selected, and click **Next**.

[![Signing in to a RealVNC account on a Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/screen-07.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-07.png)

Enter your RealVNC email and password, and click **Sign In**. On the next screen, change the connectivity method to *Direct and cloud connectivity*.

[![Assigning the Raspberry Pi to be part of a RealVNC team](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/screen-08.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-08.png)

Click **Next**. Review the settings and click **Apply**. If you get a pop-up warning you that permissions were granted without asking for a password, click **Close**. On the next screen, click **Done**.

### Remotely Control the Raspberry Pi

On your host machine, download and install the [RealVNC viewer](https://www.realvnc.com/en/connect/download/viewer/). Open the application, and click the **Sign in** button in the top-right. Enter your email and password, and click **Sign in**.

On the right side, you should see an address book (previously used connections) and something showing your \"Team\" (computers available for a VNC cloud connection). Click on your **Team**, and you should see your VNC-ready Raspberry Pi listed.

[![Finding your Raspberry Pi on the RealVNC Cloud](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/screen-09.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-09.png)

Double-click on your Raspberry Pi to connect to it. You should see a pop-up window explaining that the VNC server on your Raspberry Pi has been verified. Click **Continue**. You should be prompted with an Authentication window. If you did not change the login username and password for your Pi, your default login credentials are:

- **Username:** pi
- **Password:** raspberry

**Heads up:** it\'s highly recommended that you change your password! Anyone with access to your network could easily gain access to your Pi by trying the default username and password.

Once you have been authenticated, you should be presented with your Raspberry Pi\'s desktop. If you hover of the top part of the window, a drop-down should appear, giving you access to various settings for RealVNC, including a button to close the session.

[![Raspberry Pi desktop in the VNC viewer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/screen-04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/screen-04.png)

Another slick feature is the ability to control your Raspberry Pi from your smartphone or tablet! Download the VNC Viewer app from the [iTunes store](https://itunes.apple.com/us/app/vnc-viewer-remote-desktop/id352019548) or [Google Play](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android). Open the app, sign in, and connect to your Raspberry Pi!

[![Remote desktop into a Raspberry Pi from a smartphone](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/5/VNC_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/5/VNC_Tutorial-01.jpg)