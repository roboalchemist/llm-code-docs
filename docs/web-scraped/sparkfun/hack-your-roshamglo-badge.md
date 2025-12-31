# Source: https://learn.sparkfun.com/tutorials/hack-your-roshamglo-badge

## Introduction

So you\'ve [put together your Roshamglo badge](https://learn.sparkfun.com/tutorials/roshamglo-hookup-guide), and now you want more? Well, we can help you with that. In addition to playing infrared (IR) Rock-Paper-Scissors, the Roshamglo board can be reprogrammed with user-created code.

[![SparkFun Roshamglo Badge Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/0/2/7/14130-05.jpg)](https://www.sparkfun.com/products/14130)

### [SparkFun Roshamglo Badge Kit](https://www.sparkfun.com/products/14130) 

[ KIT-14130 ]

The SparkFun Roshamglo is the new and fun way to play Rock-Paper-Scissors with your friends! The board uses the ATtiny84, and...

**Retired**

This will allow you to create your own applications for the badge. What can you make with some blinking lights, a five-way switch and IR communication? Well, how about a TV remote or a laser tag game, for starters.

### Required Materials

The only things you\'ll need to reprogram your Roshamglo badge are a fully constructed badge and a computer.

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/ir-communication)

### IR Communication 

This tutorial explains how common infrared (IR) communication works, as well as shows you how to set up a simple IR transmitter and receiver with an Arduino.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/how-to-install-an-attiny-bootloader-with-virtual-usb)

### How to Install an ATtiny Bootloader With Virtual USB 

With this, you will be able to upload Arduino sketches directly to the ATtiny84 over USB without needing to use a programming device (such as another Arduino or FTDI chip).

[](https://learn.sparkfun.com/tutorials/roshamglo-hookup-guide)

### Roshamglo Hookup Guide 

This tutorial provides everything you need to know to get started with the Roshamglo badge.

## Hardware Overview

**Note:** This is a repeat section from the [Roshamglo Hookup Guide](https://learn.sparkfun.com/tutorials/roshamglo-hookup-guide), but it could be useful if this is the first place you\'ve visited.

[![Roshamglo labels](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/0/Roshamglo_top_highlighted_labled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/0/Roshamglo_top_highlighted_labled.jpg)

The Roshamglo uses the following:

- ATtiny84
- IR LED
- IR receiver with built-in 38kHz demodulator
- USB programming
- Programmable red and green LED
- Power switch
- 5-way switch for input
- Reset switch
- 6 AAA PTH battery clips
- 3 AAA batteries for power

The brains behind the Roshamglo is an [ATtiny84](https://www.sparkfun.com/products/11232), a lightweight Arduino-compatible microcontroller. The ATtiny84 comes with the following:

- 8kB of flash memory for our program (\~6kB after the bootloader is installed)
- 512B of SRAM, which stores our variables used in our program
- 512B of EEPROM
- 12 I/O pins MAX (the Roshamglo breaks out 9 of these pins)
- 10-bit analog-to-digital converter, which can be used on 8 pins

For details about what each pin is able to do, refer to the table below.

  Pin   Analog or Digital   Additional Uses    Roshamglo Uses
  ----- ------------------- ------------------ ---------------------
  0     Both                Analog Reference   5-way switch down
  1     Both                \--                5-way switch right
  2     Both                \--                5-way switch up
  3     Both                \--                IR Receiver
  4     Both                SCK, SCL           5-way switch left
  5     Both                MISO, PWM          IR LED
  6     Both                MOSI, SDA, PWM     5-way switch center
  7     Both                PWM                Green LED
  8     Digital             PWM                Red LED

**Missing from the list are digital pins 9 and 10. The bootloader uses these two pins for USB programming.**

[![Jumpers and Pins Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/0/Roshamglo_top_jumpers_pins_highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/0/Roshamglo_top_jumpers_pins_highlighted.jpg)

Each of these pins has been broken out to the edge of the board to make customization easy! If you would like to use any of these pins for something other than what it\'s currently connected to, we provided jumpers that can easily be cut with a [hobby knife](https://www.sparkfun.com/products/9200). The only pins that do not have a jumper on them are the pins used for the five-way switch. The pins for the switch use the ATtiny\'s internal pull-up resistors, so as long as the switch is not closed, the pin can be configured in any way you\'d like without having to cut traces.

### One Important Feature Missing

If you hadn\'t noticed in the pin description, there was no mention of RX or TX pins. This is because, unfortunately, the ATtiny84 doesn\'t have a hardware UART. The UART is used for serial communication, whether it\'s for programming or printing messages to the serial window. You might be thinking, \"But doesn\'t the USB connector provide communication between the ATtiny and the computer?\" You\'re right; it does. To keep the bootloader size as small as possible, the bootloader only allows for USB programming. For serial debugging, you\'ll need a USB cable and a [USB-to-Serial adapter](https://www.sparkfun.com/products/14050), and the [SoftwareSerial library](https://www.arduino.cc/en/Reference/softwareSerial) to send messages to a computer. You can learn more about serial communication [here](https://learn.sparkfun.com/tutorials/serial-communication).

## Install USB Driver

Roshamglo is emulating USB 1.1 using two of its pins. However, there are no common operating system drivers available that work with this custom USB class. As a result, we will need to install custom drivers in order to communicate with (and send our Arduino programs to) the Roshamglo board. Choose your operating system below and follow the directions to install the driver.

**Note:** We did not write the USB firmware nor the driver. We simply modified them to work with Roshamglo. The true geniuses are the fine folks who wrote [micronucleus](https://github.com/micronucleus/micronucleus) and [libusb](http://libusb.info/).

### Windows

Make sure the Roshamglo board is **OFF**, hold the **Down** button (pull the five-way switch toward the *SparkFun* logo) and insert it into an available USB slot.

[![Plug Roshamglo into a USB slot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-01.jpg)

Once plugged in, the status LED should begin to quickly flash red in short bursts. This means the badge is in \"Bootloader Mode.\"

[![Flashing LED means it\'s in bootloader mode](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-02.jpg)

Download the SparkFun ATtiny USB drivers by clicking on the link below.

[Windows USB drivers](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/sparkfun_attiny_usb_driver.zip)

Unzip the file. Open the Windows [Device Manager](http://www.mcci.com/mcci-v5/support/howtos1.html), and you should see an *Unknown device*. Right-click on *Unknown device* and select **Update Driver Software**.

[![Updating driver for Roshamglo](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_04.png)

In the pop-up window, click **Browse my computer for driver software**.

[![Search for SparkFun USB drivers](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_05.png)

Click **Browse\...** and open the folder that contains the drivers you just unzipped. It will likely be the *sparkfun_attiny_usb_driver* folder.

[![Installing the USB drivers](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_06.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_06.png)

Click **Next**. You may get a warning pop-up that says \"Windows can\'t verify the publisher of this driver software.\" That\'s OK. Just click **Install the driver software anyway**.

[![Tell Windows we want to install the driver software anyway](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_07.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_07.png)

You should see a notification that the *SparkFun ATtiny* driver was installed successfully. Close that window, and verify that your *Unknown device* now shows up as *SparkFun ATtiny* in the Device Manager.

[![Successful installation of the SparkFun ATtiny USB driver](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_08.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_08.png)

### MacOS

You\'ll need to install [Homebrew](https://brew.sh/) and use it to install [libusb](http://www.libusb.org/). Enter the following commands into a *Terminal*:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew doctor
    brew install libusb-compat

### Linux

Good news! Linux doesn\'t require special drivers. However, you will need to do one of the following to be able to program Roshamglo from Arduino:

1\) When you download the Arduino IDE (next section), make sure you run it as *root*: `sudo ./arduino`

[![Running Arduino as root](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/arduino_as_root.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/arduino_as_root.png)

2\) Or, you can add some udev rules so that Linux enumerates your device with write permissions. Create a file in rules.d:

    sudo edit /etc/udev/rules.d/49-micronucleus.rules

Copy the following contents into that file:

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

## Adding Arduino Compatibility

Arduino is not a full-featured development environment, but it does allow us to prototype embedded programs quickly and easily. To begin, navigate to [Arduino\'s software page](https://www.arduino.cc/en/Main/Software) and download the Arduino IDE for your operating system.

[Download Arduino IDE](https://www.arduino.cc/en/Main/Software)

If you need help installing Arduino for your operating system, you can follow [this guide](https://learn.sparkfun.com/tutorials/installing-arduino-ide).

**Important!** Your Roshamglo board will only work with Arduino versions 1.6.10 and above.

### Download and Install the Board Package

**Note:** The JSON link was updated! Below is the old json link. I was updated in the branch containing the files. Make sure that you use the correct JSON link that is provided after this note!\
\

    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/tiny/IDE_Board_Manager/package_sparkfun_index.json

Because the Roshamglo board is not supported by the Arduino IDE by default, we need to add it manually. Open the Arduino program and go to **File \> Preferences**. Then copy and paste the URL below into the *Additional Board Manager URLs* text box.

    language:bash
    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/tiny/IDE_Board_Manager/package_sparkfun_tiny_index.json

[![Modifying the additional boards URL in Arduino](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_01.png)

Then hit OK, and navigate to the **Tools \> Board \> Boards Manager...** tool. A search for "tiny" should turn up a *SparkFun ATtiny Boards* result. Select that and click **Install**.

[![Installing the Sparkfun ATtiny Boards definitions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/roshamglo_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_02.png)

Once the installation is complete, go to **Tools \> Board** and select **Roshamglo (ATtiny84, 3.3V, 8MHz)** under the *SparkFun ATtiny Boards* section.

[![Selecting the ATtiny84 under the boards section in Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/roshamglo_03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/roshamglo_03.png)

## Make Something Blink

The Roshamglo board comes with two LEDs (a red LED and green LED built into one package), as well as a five-way switch (left, right, up, down and center). We can test that our Roshamglo board can be reprogrammed by writing and uploading a simple program.

Open the Arduino IDE and enter the following code:

    language:c
    void setup() 

    void loop() 

Click on the **Upload** button.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/Roshamglo_Hack_01a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/Roshamglo_Hack_01a.png)

If you are asked to save your work, click **Cancel** (save it if you want, but you don\'t need to save to compile and upload your code).

Wait until you see *Uploading* appear in the Arduino IDE.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/Roshamglo_Hack_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/Roshamglo_Hack_02.png)

Make sure the Roshamglo board is **OFF**, hold the *Down* button (pull the five-way switch toward the *SparkFun* logo) and insert it into an available USB port while continuing to hold the *Down* button.

[![Plug Roshamglo into a USB slot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-01.jpg)

Let go of the *Down* button, and the status LED should begin to quickly flash red in short bursts. This means the badge is in \"Bootloader Mode.\" You will need to do this every time you upload a new program to it.

[![Flashing LED means it\'s in bootloader mode](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-02.jpg)

After a moment, you should see *Done uploading* appear in Arduino.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/Roshamglo_Hack_03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/Roshamglo_Hack_03.png)

Remove the Roshamglo board from your computer. Slide the power switch to **ON**.

[![Turn on Roshamglo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-04.jpg)

And that\'s it! Your Arduino should begin flashing the green LED on and off every second.

[![Roshamglo blinking](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/5/Hacking_the_Roshamglo_Tutorial-03.jpg)

**Note:** If you get an error message while uploading, it could be caused by a variety of reasons. The way we\'re uploading programs to Roshamglo is actually hacked together, as we\'re [emulating USB](https://www.obdev.at/products/vusb/index.html) on the badge, which many computers do not like. Here are some things to try if you do get an error:

- Try a different USB port
- Unplug other USB devices
- Close other programs that might be running
- Reinstall the [Roshamglo USB driver](https://learn.sparkfun.com/tutorials/hack-your-roshamglo-badge#install-usb-driver)
- Try a different computer