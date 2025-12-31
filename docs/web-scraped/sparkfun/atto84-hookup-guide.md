# Source: https://learn.sparkfun.com/tutorials/atto84-hookup-guide

## Introduction: The Littlest \'Duino

[![](https://cdn.sparkfun.com/assets/custom_pages/2/6/9/sparkx-logo.png)](https://www.sparkfun.com/sparkx)

\
**Experimental Products:** [SparkX products](https://www.sparkfun.com/sparkx) are rapidly produced to bring you the most cutting edge technology as it becomes available. These products are tested but come with no guarantees. Live technical support is not available for SparkX products.

Arduino and Arduino compatible dev boards are an awesome tool for developing an idea quickly but, being development boards, they\'re often a little more bulky and full featured than you really need. Having a USB interface and a bootloader is so nice, though, so we put together the bare minimum Arduino compatible breakout for integration into your small projects. We call it the [Atto84](https://www.sparkfun.com/products/14804).

[![Atto84 with Arduino Bootloader](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/0/6/3/14804-Atto84_with_Arduino_Bootloader-01b.jpg)](https://www.sparkfun.com/products/14804)

### [Atto84 with Arduino Bootloader](https://www.sparkfun.com/products/14804) 

[ SPX-14804 ]

Arduino and Arduino compatible dev boards are an awesome tool for developing an idea quickly but, being development boards, t...

**Retired**

The Atto84 is essentially a breakout board for the *absolutely minute* WQFN ATtiny84, but we\'ve done some work to make it easier to program. First off, we\'ve added a micro-USB connector and a firmware-based USB driver for the ATtiny that allows you to program the chip over USB. In addition, we\'ve created an Arduino board profile that combines this bootloader with an extremely full-featured ATtiny Arduino core.

Simply install the USB drivers on your computer, select the board profile from Arduino\'s Board Manager, and upload code to this board like any other Arduino style development board. In this hookup guide, you\'ll learn how to do exactly that!

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-solder-castellated-mounting-holes)

### How to Solder: Castellated Mounting Holes 

Tutorial showing how to solder castellated holes (or castellations). This might come in handy if you need to solder a module or PCB to another PCB. These castellations are becoming popular with integrated WiFi and Bluetooth modules.

[](https://learn.sparkfun.com/tutorials/how-to-install-an-attiny-bootloader-with-virtual-usb)

### How to Install an ATtiny Bootloader With Virtual USB 

With this, you will be able to upload Arduino sketches directly to the ATtiny84 over USB without needing to use a programming device (such as another Arduino or FTDI chip).

## Installing USB Drivers

The Atto84 is emulating USB 1.1 using two of its pins and the [V-USB driver](https://www.obdev.at/products/vusb/index.html). However, there are no common operating system drivers available that work with this custom USB class. As a result, we will need to install custom drivers in order to communicate with (and send our Arduino programs to) the Atto84. Choose your operating system below and follow the directions to install the driver.

**Note:** We did not write the USB firmware nor the driver. We simply packaged and modified them to work with the Atto84. The true geniuses are the fine folks who wrote [micronucleus](https://github.com/micronucleus/micronucleus) and [libusb](http://libusb.info/).

### Windows

Insert a micro-USB cable into the Atto84. Your PC will probably make a happy \"USB connected!\" chime and then inform you that there is an unknown device connected.

Download the SparkFun ATtiny USB drivers by clicking on the link below.

[Download Windows USB Drivers (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/sparkfun_attiny_usb_driver.zip)

Unzip the file. Open the Windows [Device Manager](http://www.mcci.com/mcci-v5/support/howtos1.html), and you should see an *Unknown device*. Right-click on *Unknown device* and select **Update Driver Software**.

[![Screeshot of the Device Manager window showing the right-click menu for a device called \"unknown device\". The \"Update Driver Software\...\" option is highlighted.](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_04.png)

In the pop-up window, click **Browse my computer for driver software**.

[![Screenshot of the \"Update Driver Software\" interface. The option labeled \"Browse my computer for driver software\" is highlighted.](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_05.png)

Click **Browse\...** and open the folder that contains the drivers you just unzipped. It will likely be the *sparkfun_attiny_usb_driver* folder.

[![Screenshot of the \"Browse for driver software on your computer\" interface. In the field labeled \"Search for driver software in this location:\" I\'ve typed the filepath to my sparkfun_attiny_usb_driver folder.](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_06.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_06.png)

Click **Next**. You may get a warning pop-up that says \"Windows can\'t verify the publisher of this driver software.\" That\'s OK. Just click **Install the driver software anyway**.

[![Windows Security prompt warning the user that the driver is unsigned. The \"Install this driver software anyway\" option is highlighted.](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_07.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_07.png)

You should see a notification that the *SparkFun ATtiny* driver was installed successfully. Close that window, and verify that your *Unknown device* now shows up as *SparkFun ATtiny* in the Device Manager.

[![Screenshot of the Device Manager window again, this time showing a device enumerating under \"libusb-win32 devices\" as \"SparkFun ATtiny\"](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_08.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_08.png)

### Mac OS

You\'ll need to install [Homebrew](https://brew.sh/) and use it to install [libusb](https://libusb.info/). Enter the following commands into a *Terminal*:

    language:bash
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew doctor
    brew install libusb-compat

### Linux

Good news! Linux doesn\'t require special drivers. However, you will need to do one of the following to be able to program the Atto84 from Arduino:

1\) When you download the Arduino IDE (next section), make sure you run it as *root*: `sudo ./arduino`

[![Very exciting screenshot of a terminal with \"sudo ./arduino\" typed in](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/arduino_as_root.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/arduino_as_root.png)

2\) Or, you can add some udev rules so that Linux enumerates your device with write permissions. Create a file in **rules.d**:

    language:bash
    sudo edit /etc/udev/rules.d/49-micronucleus.rules

Copy the following contents into that file:

    language:bash
    # UDEV Rules for Micronucleus boards including the Digispark.
    # This file must be placed at:
    #
    # /etc/udev/rules.d/49-micronucleus.rules    (preferred location)
    #   or
    # /lib/udev/rules.d/49-micronucleus.rules    (req'd on some broken systems)
    #
    # After this file is copied, physically unplug and reconnect the board.
    #
    SUBSYSTEMS=="usb", ATTRS=="16d0", ATTRS=="0753", MODE:="0666"
    KERNEL=="ttyACM*", ATTRS=="16d0", ATTRS=="0753", MODE:="0666", ENV="1"
    #
    # If you share your linux system with other users, or just don't like the
    # idea of write permission for everybody, you can replace MODE:="0666" with
    # OWNER:="yourusername" to create the device owned by you, or with
    # GROUP:="somegroupname" and mange access using standard unix groups.

Save and exit.

## Installing the Board Package

**Important!** Your Atto84 will only work with Arduino versions 1.6.10 and above. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Download and Install the Board Package

Because the Atto84 is not supported by the Arduino IDE by default, we need to add it manually. Open the Arduino program and go to **File \> Preferences**. Then copy and paste the URL below into the *Additional Board Manager URLs* text box.

If you\'re thinking \"I already have the SparkFun Board Profiles and I don\'t see any tiny boards!\" notice that we\'re specifically pointing to a branch of SparkFun\'s Arduino Boards repository called \"**\.../tiny**,\" not the main branch. If you copy/paste the URL below, you should have no troubles!

    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/tiny/IDE_Board_Manager/package_sparkfun_tiny_index.json

[![Screenshot of the Arduino IDE \"Preferences\" menu with the \"Additional Board Manager URLs\" field highlighted at the bottom of the window.](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_01.png)

Then hit OK, and navigate to the **Tools \> Board \> Boards Manager...** tool. A search for "tiny" should turn up a *SparkFun ATtiny Boards* result. Select that and click **Install**.

[![Screenshot of the Boards Manager window with \"tiny\" typed into the search bar. A package called \"SparkFun ATtiny Boards\" is in the results pane](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/roshamglo_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_02.png)

Once the installation is complete, go to **Tools \> Board** and select **SparkX Atto84 (ATtiny84, 3.3V, 8MHz)** under the *SparkFun ATtiny Boards* section.

[![Screenshot of the Arduino IDE showing the location of the \"SparkX Atto84\" board profile under Tools\>Board\>SparkFun ATtiny Boards](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/4/duinocap.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/4/duinocap.PNG)

## Tiny Tricks and Gotchas

### Tiny Tricks

Because the Atto84 is the bare-minimum of hardware that can be USB programmed, it does have a few quirks that you should be aware of. But first, let\'s talk about a few of the cool features that it inherits from SpenceKonde\'s ATTiny Core.

[![A diagram showing the pinout of the Atto84. Looking at the board from the top down, with the micro USB port in the 12 o\'clock position, the pin assignments are as follows: From top to bottom on the right-hand side: VCC, which is 5 volts maximum. Pin 0, which is also A0. Pin 1, which is also A1. Pin 2, which is also A2, Pin 3, which is also A3, Pin 8, which is also the built-in LED. On the left-hand side, from top to bottom the pins are as follows: GND. Pin 4, which is also A4, SCL and SCK. Pin 5, which is also A5, MISO and DO. Pin 7, which is also A7. Pin 6, which is also A6, MOSI, DI and SDA. Pin 11, which is the Reset Pin.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/4/pinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/4/pinout.png)

#### I²C Support

The ATTiny Core includes a special version of the Wire library that leverages the tiny84\'s hardware USI for I²C communication. This means that it will run any Wire-based code that you\'ve written for ATmega platforms like the Arduino Uno or the SparkFun RedBoard.

#### SPI Support

The ATtiny actually has hardware SPI support, so the Atto84 will work identically to the Uno in that respect.

#### Servos?

Yeah, why not? The tiny84 has plenty of timers and you\'ll find a copy of the Servo library included with the core!

### The \"Gotchas\"

Sounds great, right? It is, but there are a few catches that you should be aware of.

#### Power

There is **no power regulator** on the Atto84, so the input to VCC must be between **3.3V** and **5V**. Powering your project through the USB connector is a good, too.

#### Serial UART

The ATtiny doesn\'t have a hardware UART, so serial doesn\'t work the way you might expect. There is a custom library built in to the ATTiny Core called \"Serial\" which is actually an implementation of Software Serial. This works quite well but you do need to know its limitations. For instance, it\'s not full duplex, so sending and receiving at the same time will produce gibberish. Also, it does not implement V_USB, so if you want to do Serial debugging, you\'ll need to connect a separate USB-Serial adapter.

#### Uploading Code

Most USB Arduino boards can be forced into bootloader mode by the Arduino IDE during programming, but due to the limitations of V-USB, the Atto84 needs to be manually reset during programming. Every time the Atto84 restarts, it goes into bootloader mode for about 5 seconds. During this time, your computer will recognize it as a USB device. After 5 seconds, the Atto84 begins running user code. Unless your code also happens to be implementing V-USB, the computer will stop recognizing the device.

In order to get code onto the board, simply click the upload button in the Arduino IDE and wait for the \"uploading\...\" message to show. When the IDE says \"uploading,\" press the reset button on your Atto84. Don\'t worry, the timing isn\'t critical, the Micronucleus upload program gives you 30 seconds to press reset. After the board has reset and shows up as a USB device, your code will upload like normal!

**Note:** If you get an error message while uploading, it could be caused by a variety of reasons. The way we\'re uploading programs to Atto84 is actually hacked together, as we\'re [emulating USB](https://www.obdev.at/products/vusb/index.html) on the board, which many computers do not like. Here are some things to try if you do get an error:

- Try a different USB port
- Unplug other USB devices
- Close other programs that might be running
- Reinstall the [Atto84 USB driver](https://learn.sparkfun.com/tutorials/atto84-hookup-guide#installing-usb-drivers)
- Try a different computer

[![This image is an invisible square but it\'s here so that I can ask you a favor if you\'re enjoying this tutorial using a screen reader. I\'m trying to improve our site\'s accessibility, so I would love to hear your feedback about the image alt tags in this article. You can email me at nick.poole@sparkfun.com and please put the phrase \"image tags\" in the subject line. Thank you so much. Happy Hacking!](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/4/FFFFFF-0.0.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/4/FFFFFF-0.0.png)