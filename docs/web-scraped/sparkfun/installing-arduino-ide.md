# Source: https://learn.sparkfun.com/tutorials/installing-arduino-ide

## Introduction

This tutorial will walk you through downloading, installing, and testing the [Arduino software](http://arduino.cc/en/Main/Software) (also known as the Arduino IDE - short for Integrated Development Environment). Before you jump to the page for your operating system, make sure you\'ve got all the right equipment.

[![Arduino Logo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/arduinoThumb.jpg)](http://arduino.cc/en/Main/Software)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

- A computer (Windows, Mac, or Linux)
- An Arduino-compatible microcontroller (anything from [this guide](https://www.sparkfun.com/standard_arduino_comparison_guide) should work)
- A USB A-to-B cable, or another appropriate way to connect your Arduino-compatible microcontroller to your computer (check out this [USB buying guide](https://www.sparkfun.com/pages/USB_Guide) if you\'re not sure which cable to get).

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/600-600/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![USB Cable A to B - 6 Foot](https://cdn.sparkfun.com/r/600-600/assets/parts/2/7/7/00512-USB_Cable_A_to_B_-_6_Foot-01.jpg)](https://www.sparkfun.com/usb-cable-a-to-b-6-foot.html)

### [USB Cable A to B - 6 Foot](https://www.sparkfun.com/usb-cable-a-to-b-6-foot.html) 

[ CAB-00512 ]

This is a standard issue USB 2.0 cable. This is the most common A to B Male/Male type peripheral cable, the kind that\'s usual...

[ [\$5.50] ]

### Suggested Reading

If you\'re new to Arduino in general, you\'ll want to check out this tutorial to familiarize yourself with everyone\'s favorite microcontroller platform.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

February 26, 2013

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

**Note:** There are several variants that use the Arduino Uno R3 footprint. Depending on the design, you may need to install additional drivers for your USB-to-serial converter before you are able to able to upload code to your microcontroller. For example, the [RedBoard uses an FTDI](https://www.sparkfun.com/products/13975) while the [RedBoard Plus uses the CH340](https://www.sparkfun.com/products/18158).\
\

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Atmega16U2 on the Arduino Uno R3](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/11021-Arduino-Uno-ATmega16U2_USB-to-Serial-Highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/11021-Arduino-Uno-ATmega16U2_USB-to-Serial-Highlighted.jpg)   [![FTDI on the RedBoard](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/15123-RedBoard-Qwiic-CH340_USB-to-Serial-Highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/15123-RedBoard-Qwiic-CH340_USB-to-Serial-Highlighted.jpg)   [![CH340 on the RedBoard Qwiic](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/13975-Arduino-RedBoard-FTDI_USB-to-Serial-Highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/13975-Arduino-RedBoard-FTDI_USB-to-Serial-Highlighted.jpg)

  *Atmega16U2 on the\                                                                                                                                                                                                                                                     *FTDI on the\                                                                                                                                                                                                                                           *CH340 on the\
  Arduino Uno R3*                                                                                                                                                                                                                                                         RedBoard*                                                                                                                                                                                                                                               RedBoard Qwiic*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Both use different drivers compared to the Arduino Uno R3. Make sure to look closely at your board and its respective hookup guide to determine USB-to-serial converter that is on board. You will probably have either an FTDI or CH340 populated on the board.\
\

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

Other boards using a different architecture like the [RedBoard Turbo (SAMD21)](https://www.sparkfun.com/products/14812) have a built-in USB communication, eliminating the need to have a separate piece of hardware. For more information, check out the blog post on drivers: [What Drives your SparkFun Inventor\'s Kit?](https://www.sparkfun.com/news/2979).

If you\'re ready to get started, click on the link in the column on the left that matches up with your operating system, or you can jump to your operating system here.

- [Windows](https://learn.sparkfun.com/tutorials/installing-arduino#windows)
- [Mac](https://learn.sparkfun.com/tutorials/installing-arduino#mac)
- [Linux](https://learn.sparkfun.com/tutorials/installing-arduino#linux)

## Downloading the Arduino IDE

You can [download the Arduino IDE](http://arduino.cc/en/Main/Software) from their website. They have [installation instructions](https://www.arduino.cc/en/Guide/HomePage), but we will also go over the installation process as well. Make sure you download the version that matches your operating system.

[Click for Arduino IDE Download Page](http://arduino.cc/en/Main/Software)

The installation procedure is fairly straightforward, but it does vary by OS. Here are some tips to help you along.

**Troubleshooting Tips**\

- We recommend using a computer with a full desktop operating system like Windows 7/10 ([**avoid**] Windows 8 if you can), Mac OSX, and certain flavors Linux (check the [Arduino FAQ page for compatibility](https://www.arduino.cc/en/Main/FAQ#toc12)).
  \
  - If you are not a technical or computer savy individual and you have your choice of computers, I highly recommend using a [**Windows 7, 10, or 11**] computer. You will usually run into the the least issues, if any, with these operating systems.

  \
- We do [**[NOT]**] recommend using a Chromebook, Netbook, tablet, phone, or the Arduino Web IDE in general. You will be responsible for troubleshooting any driver or Arduino Web IDE issues.
  \
- As of the writing of this tutorial (updated 12-14-2018), the most recent and stable release of the Arduino IDE is version 1.8.5. We recommend using that version of the Arduino IDE; you can download the [previous releases here](https://www.arduino.cc/en/Main/OldSoftwareReleases#previous).
  \
- Raspberry Pi users with Raspbian installed should use the **Linux ARM** download. We do not recommend using the command line installation. It will install the oldest release of Arduino, which is useless when it comes to installing new boards definitions or libraries.
  \
- For additional troubleshooting tips, here is a [troubleshooting guide from Arduino](https://www.arduino.cc/en/Guide/Troubleshooting).

## Windows

This page will show you how to install and test the Arduino software with a Windows operating system (Windows 10, Windows 7, Vista, and XP).

Go to the Arduino [download page](http://arduino.cc/en/Main/Software) and download the latest version of the Arduino software for Windows if you have not already.

[Click for Arduino IDE Download Page](http://arduino.cc/en/Main/Software)

### Installer

The Windows version of Arduino is offered in two options: an installer or a zip file. The **installer** is the easier of the two options, just download that, and run the executable file to begin the installation.

[![Windows 10 - Arduino Installation Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/4/Win_10-_Installation_Diagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Win_10-_Installation_Diagram.png)

*Windows install steps. Click the image to get a bigger view.*

When you\'re prompted to install a driver during installation, select \"Install\". This will install drivers for Arduino specific boards (like the Uno, Nano, etc.) that you may use in the future.

### ZIP

If you choose to download the **zip file** version of Arduino, you\'ll need to extract the files yourself. Don\'t forget which folder you extract the files into! You will need to run the executable Arduino file in the folder to start the Arduino IDE.

When the download is finished, un-zip it and open up the Arduino folder to confirm that yes, there are indeed some files and sub-folders inside. The file structure is important so don\'t be moving any files around unless you really know what you\'re doing.

**Note:** On Windows 10, there is an option to install Arduino through their app store. we do not recommend installing the Arduino IDE from the app store. You may run into issues because the OS will automatically update to the most recent release of the Arduino IDE, which may have unknown bugs.

### Connecting Your Arduino

Power up your Arduino by connecting your Arduino board to your computer with a USB cable (or FTDI cable if you\'re using an Arduino Pro). You should see the an LED labeled \'ON\' light up. ([this diagram](https://learn.sparkfun.com/tutorials/what-is-an-arduino/whats-on-the-board) shows the placement of the power LED on the UNO).

### Drivers [for Arduino Uno on Windows]

To install the drivers for the Arduino Uno, you will need to plug in your board to your computer\'s USB port. Once the board is connected, you will need to wait for Windows to begin it\'s driver installation process. After a few moments, the process will probably fail, despite its best efforts.

Open up a search, type in **Device Manager**, and hit [ENTER].

[![Search for Device Manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/8/Windows-Searching_for_device_manager.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/8/Windows-Searching_for_device_manager.jpg)

**Note:** Searching is the easiest method to open the Device Manager. However, there is more than one method of opening the device manager. The longer method is to click on the **Start Menu** \> **Windows System** \> **System and Security** \> **System** \> **Device Manager**.

Look under Ports (COM & LPT) tree. You should see an open port named \"**Arduino UNO (COMxx)**\". If there is no COM & LPT section, look under \"**Other devices**\" for \"**Unknown Device**. Right click on the \"**Arduino UNO (COMxx)**\" or \"**Unknown device**\" port and choose the \"**Update Driver Software**\" option.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Device_Manager_Unknown_Device.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Device_Manager_Unknown_Device.png)

Next, choose the \"**Browse my computer for Driver software**\" option

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Unknown_Device_Browse_my_computer_for_driver_software.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Unknown_Device_Browse_my_computer_for_driver_software.png)

Finally, navigate to the Arduino IDE folder. This should be where you unzipped the Arduino IDE (e.g. it should be similar to the following path with a different version number: *C:\\Program Files\\arduino-1.8.5\\drivers*). Depending on what version of Windows you have, you may be able to select the Uno\'s driver file, named \"**Arduino.inf**\", located in the \"**Drivers**\" folder (not the \"FTDI USB Drivers\" sub-directory). If you cannot see the **\*.inf** file, it is probably just hidden. You can select the \"**drivers**\" folder with the \"**include sub-folders**\" option selected instead.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_Select_Driver.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Select_Driver.png)

Windows will finish up the driver installation from there! Your computer will enumerate with a COM port. You may see a COM port number depending on what is currently saved in your computer. Try to remember what the number is when uploading. If not, you can always navigate back to the device manager and power cycle the Arduino to determine what number your Arduino enumerated on.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_Uno_COM_Port_Device_Manager.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Uno_COM_Port_Device_Manager.png)

For earlier versions of the Arduino boards (e.g. Arduino Duemilanove, Nano, or Diecimila) check out [this page](http://arduino.cc/en/Guide/Windows) for specific directions.

[Arduino.cc - Guide: Windows](http://arduino.cc/en/Guide/Windows)

### Drivers [for RedBoard on Windows]

Depending on your board, there may be different USB-to-serial converters on your board. If you are using a RedBoard you will need to go to the [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) tutorial. If you are using the or RedBoard Qwiic, you will need to go to the [How to Install CH340 Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) tutorial. Make sure to look closely at your board and its respective hookup guide to determine USB-to-serial converter that is on board.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

June 4, 2013

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

### Launch and Blink!

After following the appropriate steps for your software install, we are now ready to test your first program with your Arduino board! Launch the Arduino application. If you disconnected your board, plug it back in.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_IDE_Executable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Executable.jpg)

**Note:** Depending on your method of installing the Arduino IDE, the application may be on your desktop or the program folder.

Open the Blink example sketch by going to: **File** \> **Examples** \> **01.Basics** \> **Blink**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_Blink_Example.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Blink_Example.jpg)

Select the type of Arduino board you\'re using: **Tools** \> **Board** \> **Arduino Uno**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_Board_Selection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Board_Selection.jpg)

**Note:** As you move to other architectures, you may need to select a different board definition depending on your development board. For the Arduino Uno R3 and RedBoard development boards with ATmega328P, you can simply select **Arduino Uno**. Certain Arduino IDE versions may have you select **Arduino/ Genuino Uno**.

Select the serial/COM port that your Arduino is attached to: **Tools** \> **Port** \> **COMxx**. In this case it was *COM11*.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_IDE_Select_COM_Port.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Select_COM_Port.jpg)

**Note:** If you\'re not sure which serial device is your Arduino, take a look at the available ports, then unplug your Arduino and look again. The one that disappeared is your Arduino.

With your Arduino board connected, and the Blink sketch open, press the \"**Upload**\" button.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_IDE_Upload_Button.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Upload_Button.jpg)

After a second, you should see some LEDs flashing on your Arduino, followed by the message \"**Done Uploading**\" in the status bar of the Blink sketch.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_IDE_Done_Uploading.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Done_Uploading.jpg)

If everything worked, the onboard LED on your Arduino should now be blinking! You just programmed your first Arduino!

**Note:** Depending on the architecture and development board, the built-in LED may be defined on a different pin. You may need to adjust `LED_BUILTIN` or pin `13` to a different value before uploading.

### Troubleshooting

[This guide](http://arduino.cc/en/Guide/Windows) from Arduino has some more details and troubleshooting tips if you get stuck.

## Mac

This page will show you how to install and test the Arduino software on a Mac computer running OSX.

Go to the Arduino [download page](http://arduino.cc/en/Main/Software) and download the latest version of the Arduino software for Windows if you have not already.

[Click for Arduino IDE Download Page](http://arduino.cc/en/Main/Software)

When the download is finished your Mac should automatically un-zip the contents. This will probably in your **Downloads** folder.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Unzip_Arduino_IDE_Mac.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Unzip_Arduino_IDE_Mac.png)

You can leave the program in the **Downloads** folder or move it into your Applications folder.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_IDE_Applications_Folder_Mac.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Applications_Folder_Mac.png)

### Connecting Your Arduino

Power up your Arduino by connecting your Arduino board to your computer with a USB cable (or FTDI cable if you\'re using an Arduino Pro). You should see the an LED labeled \'ON\' light up. ([this diagram](https://learn.sparkfun.com/tutorials/what-is-an-arduino/whats-on-the-board) shows the placement of the power LED on the UNO).

### Drivers [for Arduino Uno on Mac]

For the Arduino Uno, you do not need to install drivers for Mac! You can skip on down and try uploading a blink sketch!

### Drivers [for RedBoard on Mac]

Depending on your board, there may be different USB-to-serial converters on your board. If you are using a RedBoard you will need to go to the [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) tutorial. If you are using the or RedBoard Qwiic, you will need to go to the [How to Install CH340 Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) tutorial. Make sure to look closely at your board and its respective hookup guide to determine USB-to-serial converter that is on board.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

June 4, 2013

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

### Launch and Blink!

After following the appropriate steps for your software install, we are now ready to test your first program with your Arduino board!

Launch the Arduino application wherever the program is located. If you disconnected your board, plug it back in.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Unzip_Arduino_IDE_Mac.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Unzip_Arduino_IDE_Mac.png)

Open the Blink example sketch by going to: **File** \> **Examples** \> **01.Basics** \> **Blink**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_Blink_Sketch_Mac.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Blink_Sketch_Mac.png)

Select the type of Arduino board you\'re using: **Tools** \> **Board** \> **Arduino Uno**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_IDE_Board_Select_Mac.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Board_Select_Mac.png)

**Note:** As you move to other architectures, you may need to select a different board definition depending on your development board. For the Arduino Uno R3 and RedBoard development boards with ATmega328P, you can simply select **Arduino Uno**. Certain Arduino IDE versions may have you select **Arduino/ Genuino Uno**.

Select the serial port that your Arduino is attached to: **Tools** \> **Port** \> **xxxxxx**. It\'ll probably look something like \"*/dev/tty.usbmodemfd131*\" or \"*/dev/tty.usbserial-131*\" but probably with a different number. In this case, it was */dev/cu.usbmodemFD131*.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_IDE_COM_Port_Select_Mac.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_COM_Port_Select_Mac.png)

**Note:** If you\'re not sure which serial device is your Arduino, take a look at the available ports, then unplug your Arduino and look again. The one that disappeared is your Arduino.

With your Arduino board connected and the Blink sketch open, press the \"**Upload**\" button.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Upload_Button_Mac.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Upload_Button_Mac.png)

After a second, you should see some LEDs flashing on your Arduino, followed by the message \"**Done Uploading**\" in the status bar of the Blink sketch.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Done_Uploading_Mac.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Done_Uploading_Mac.png)

If everything worked, the onboard LED on your Arduino should now be blinking! You just programmed your first Arduino!

**Note:** Depending on the architecture and development board, the built-in LED may be defined on a different pin. You may need to adjust `LED_BUILTIN` or pin `13` to a different value before uploading.

### Troubleshooting

If you\'re having problems, check out [this troubleshooting guide](http://arduino.cc/en/Guide/Troubleshooting) from Arduino.

## Linux

If you are a Linux user, you probably know that there are many different distribution \'flavors\' of Linux out there. Unsurprisingly, installing Arduino is slightly different for many of these distributions. Luckily, the Arduino community has done an excellent job of providing instructions for most of the popular versions. Click on the link below that covers your flavor of Linux:

- [ArchLinux](http://playground.arduino.cc/Linux/ArchLinux)
- [Debian](http://playground.arduino.cc/Linux/Debian)
- [Fedora](http://playground.arduino.cc/Linux/Fedora)
- [Gentoo](http://playground.arduino.cc/Linux/Gentoo)
- [MEPIS](http://playground.arduino.cc/Linux/MEPIS)
- [Mint](http://playground.arduino.cc/Linux/Mint)
- [openSUSE](http://playground.arduino.cc/Linux/OpenSUSE)
- [Puppy](http://playground.arduino.cc/Linux/Puppy)
- [Pussy](http://playground.arduino.cc/Linux/Pussy)
- [Slackware](http://playground.arduino.cc/Linux/Slackware)
- [Ubuntu](http://playground.arduino.cc/Linux/Ubuntu)
- [Xandros (Debian derivative) on Asus Eee PC](http://playground.arduino.cc/Linux/Xandros)

If the above directions did not work for you, or you don\'t see your distribution, try this [catch-all guide](http://playground.arduino.cc/Linux/All).

You can go to the [download page](http://arduino.cc/en/Main/Software) and download the latest version of Arduino for Linux (there are 32-bit and 64-bit versions available) when your system is properly set up.

[Click for Arduino IDE Download Page](http://arduino.cc/en/Main/Software)

**Note:** Raspberry Pi users with Raspbian installed should use the **Linux ARM** download. Do not use the command line installation process. For more information, please refer to this [blog post from Arduino](https://playground.arduino.cc/Linux/Raspbian).

### Connecting Your Arduino

Power up your Arduino by connecting your Arduino board to your computer with a USB cable (or FTDI cable if you\'re using an Arduino Pro). You should see the an LED labeled \'ON\' light up. ([this diagram](https://learn.sparkfun.com/tutorials/what-is-an-arduino/whats-on-the-board) shows the placement of the power LED on the UNO).

### ZIP

**Note:** You\'ll need to know if your Linux distribution is running on 32-bit or 64-bit when downloading the Arduino IDE. Type the following command in the serial terminal to determine what version your OS is running on.\
\

``` bash
uname -a
```

If you receive an output with `x86_64`, this indicates that it is a 64-bit OS.

Once you download the zip file version of Arduino, you\'ll need to extract the files yourself. Don\'t forget which folder you extract the files into! Once downloaded, [open a serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) and navigate to the Arduino program folder that was unzipped using the `cd` command and the folder path. In this case, we downloaded Arduino IDE v1.8.5, 64-bit version for the Ubuntu distribution. The path and folders may be different depending on the version that is downloaded. You may need to use the `ls` command to navigate.

    language:bash
    cd /Downloads/arduino-1.8.5-linux64/arduino-1.8.5

Once you are in the Arduino program folder, you\'ll need to enter the following command in the terminal window to install.

    language:bash
    ./install.sh

At this point, your terminal window will probably look like the following.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino-Install_Linux.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino-Install_Linux.png)

When finished, the Arduino IDE will be installed on the desktop!

### Drivers [for RedBoard on Linux]

For the Arduino Uno, you do not need to install drivers for Linux! You may need to change the COM port permissions which will be explained further below. You can skip on down and try uploading a blink sketch!

### Drivers [for RedBoard on Linux]

Depending on your board, there may be different USB-to-serial converters on your board. If you are using a RedBoard you will need to go to the [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) tutorial. If you are using the or RedBoard Qwiic, you will need to go to the [How to Install CH340 Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) tutorial. Make sure to look closely at your board and its respective hookup guide to determine USB-to-serial converter that is on board.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

June 4, 2013

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

### Launch and Blink!

After following the appropriate steps for your software install, we are now ready to test your first program with your Arduino board!

Launch the Arduino application. If you disconnected your board, plug it back in.

Open the Blink example sketch by going to: **File** \> **Examples** \> **01.Basics** \> **Blink**.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Blink_Linux.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_IDE_Blink_Linux.png)

Select the type of Arduino board you\'re using: **Tools** \> **Board** \> **Arduino Uno**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_Board_Selection_Linux.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Board_Selection_Linux.png)

**Note:** As you move to other architectures, you may need to select a different board definition depending on your development board. For the Arduino Uno R3 and RedBoard development boards with ATmega328P, you can simply select **Arduino Uno**. Certain Arduino IDE versions may have you select **Arduino/ Genuino Uno**.

Select the serial port that your Arduino is attached to: **Tools** \> **Port** \> **xxxxxx** (it\'ll probably look something like \"*/dev/ttyACM0*\" but probably with a different number)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/Arduino_COM_Port_Linux.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_COM_Port_Linux.png)

**Note:** If you\'re not sure which serial device is your Arduino, take a look at the available ports, then unplug your Arduino and look again. The one that disappeared is your Arduino.

With your Arduino board connected and the Blink sketch open, press the \"**Upload**\" button.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Upload_Button_Linux.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Upload_Button_Linux.png)

After a second, you should see some LEDs flashing on your Arduino, followed by the message \"**Done Uploading**\" in the status bar of the Blink sketch.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Done_Uploading_Linux.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_Done_Uploading_Linux.png)

**Troubleshooting Tip:** Having trouble uploading? If you receive the following error when uploading, this could be [due to a few reasons](https://support.arduino.cc/hc/en-us#upload). Most likely there is something with the user permissions if you have not used the Arduino Uno on your computer before.\
\

    avrdude: ser_open(): can't open device "/dev/ttyACM0" Permission denied Problem uploading to board.

You\'ll see the output at the bottom of the Arduino IDE.\
\

[![Arduino Upload Error Linux](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_COM_Port_Permissions_Error_Linux.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_COM_Port_Permissions_Error_Linux.png)

\
Try adjusting the permissions by opening a terminal window.\
\

    ls -l /dev/ttyACM*

You\'ll get something similar to the following output.\
\

    crw-rw---- 1 root dialout 188, 0 Jul 30 14:14 /dev/ttyACM0

Then type the following command where the *\<username\>* is your Linux account user. Make sure to enter your password to change the settings.\
\

    sudo usermod -a -G dialout <username>

You\'ll probably see something similar to the output below with a different username. In this case, our username was \"pdev.\"\
\

[![Linux Terminal Window](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_COM_Port_Permissions_Terminal.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/Arduino_COM_Port_Permissions_Terminal.png)

\
You\'ll need to restart your Linux for the changes to take effect. Since we are already in the terminal window, type the following command to restart your computer. Of course, you can use the GUI as well to restart if you prefer.\
\

    sudo reboot

If everything worked, the onboard LED on your Arduino should now be blinking! You just programmed your first Arduino!

**Note:** Depending on the architecture and development board, the built-in LED may be defined on a different pin. You may need to adjust `LED_BUILTIN` or pin `13` to a different value before uploading.

### Troubleshooting

The [Arduino Playground Linux section](http://playground.arduino.cc/Learning/Linux) is a great resource for figuring out any problems with your Arduino installation.

## Board Add-Ons with Arduino Board Manager

With Arduino v1.6.4+, a new boards manager feature makes it easy to add third-party boards (like the [SparkFun RedBoard, Digital Sandbox, and RedBot](https://github.com/sparkfun/Arduino_Boards#sparkfun-arduino-boards)) to the Arduino IDE.

[GitHub: SparkFun Arduino Boards](https://github.com/sparkfun/Arduino_Boards#sparkfun-arduino-boards)

To start, highlight and copy ([CTRL] + [C] / [CMD] + [C]) the text below for the boards manager URL. You\'ll need this to configure Arduino.

    language:bash
    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/main/IDE_Board_Manager/package_sparkfun_index.json

[![Additional Boards Manager URLs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/SparkFun_Arduino_Additional_Board_Manager_URLs_GitHub_JSON.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/SparkFun_Arduino_Additional_Board_Manager_URLs_GitHub_JSON.jpg)

**Heads Up:** GitHub has recently [moved away](https://github.com/github/renaming) from having default branches as \"`master`\" and changed the default to \"`main`\". SparkFun has followed this move as well. If you\'re unable to see a particular board inside of Arduino it may be that you are using the older \"`master`\" link. As a result, you will only see the previous changes on the old `master` branch. Please change to the \'`main`\' json url listed above and all should be well.

Open up Arduino:

- *Configure the Boards Manager*
  - For Windows and Linux, head to **File \> Preferences \> Additional Boards Manager URLs** and paste ([CTRL] + [V] / [CMD] + [V]) the link
  - For Macs, head to **Arduino \> Preferences \> Additional Boards Manager URLs** and paste ([CTRL] + [V] / [CMD] + [V]) the link
- Click on **Tools \> Board \> Boards Manager\...**
- Select the Type as \"**Contributed**\" from the drop down menu.
- Click on the **SparkFun AVR Boards** and then click **Install**.

That\'s it! Boards are all installed. This also gives you access to all of our library files as well through the built-in Library Manager tool in Arduino. Looking for more information about adding other custom boards? Check out the the following [tutorial to install other Arduino cores](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide).

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

September 9, 2020

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.