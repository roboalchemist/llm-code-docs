# Source: https://learn.sparkfun.com/tutorials/qwiic-shim-kit-for-raspberry-pi-hookup-guide

## Introduction

The [Qwiic SHIM Kit for Raspberry Pi](https://www.sparkfun.com/products/16987) gets you started with some of the basics surrounding I^2^C and Python on your Raspberry Pi. This tutorial will go over connecting Qwiic-enabled devices, installing their Python packages, and running the example code.

[![SparkFun Qwiic SHIM Kit for Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/9/2/5/16987-SparkFun_Qwiic_SHIM_Kit_for_Raspberry_Pi-01a.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shim-kit-for-raspberry-pi.html)

### [SparkFun Qwiic SHIM Kit for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-shim-kit-for-raspberry-pi.html) 

[ KIT-16987 ]

The SparkFun Qwiic SHIM Kit for Raspberry Pi comes with everything you need to turn your Raspberry Pi into a Qwiic enabled de...

**Retired**

### Required Materials

To follow along with this tutorial, you will also need a few pieces of hardware. Single board computers with the Raspberry Pi 40-pin GPIO standard header will work. We\'ll be using a Raspberry Pi throughout this tutorial. If you have not worked with a Raspberry Pi, we recommend pairing the Qwiic SHIM Kit with a Raspberry Pi 4 kit. At a minimum, you\'ll need a basic kit. However, if you need keyboard and mouse combination, we recommend getting the desktop kit.

[![SparkFun Raspberry Pi 4 Basic Kit - 4GB](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/1/0/1/16384-SparkFun_Raspberry_Pi_4_Basic_Kit_-_4GB-01a.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-basic-kit-4gb.html)

### [SparkFun Raspberry Pi 4 Basic Kit - 4GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-basic-kit-4gb.html) 

[ KIT-16384 ]

The Raspberry Pi 4 Basic Kit includes everything you\'ll need to get up and running with the Raspberry Pi 4 4GB.

**Retired**

[![SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/1/0/3/16386-Raspberry_Pi_4_Desktop_Kit_-_4GB-01b.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html)

### [SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html) 

[ KIT-16386 ]

The SparkFun Raspberry Pi 4 Desktop Kit (4GB) includes everything you need to turn any monitor with an HDMI port into a deskt...

**Retired**

#### Optional Materials

You have several options when it comes to working with the Raspberry Pi. Most commonly, the Pi is used as a standalone computer, which requires a monitor. The following parts can be used with the Pi 4 if you opt for a small display. To save on costs, the Pi can also be used as a [*headless* computer](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup/all) (without a monitor, keyboard, and mouse). This setup has a slightly more difficult learning curve, as you will need to use the *command-line interface* (CLI) from another computer.

[![Raspberry Pi LCD - 7\" Touchscreen](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/4/4/13733-01.jpg)](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html)

### [Raspberry Pi LCD - 7\" Touchscreen](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html) 

[ LCD-13733 ]

This 7\" Raspberry Pi Touchscreen LCD provides you with the ability to create a standalone device that can be utilized as a cu...

[ [\$88.30] ]

[![SmartiPi Touch 2](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/0/0/4/16302-SmartiPi_Touch_2-03.jpg)](https://www.sparkfun.com/smartipi-touch-2.html)

### [SmartiPi Touch 2](https://www.sparkfun.com/smartipi-touch-2.html) 

[ PRT-16302 ]

The SmartiPi Touch 2 is a case for the Official Raspberry Pi Display, Raspberry Pi and Raspberry Pi camera.

**Retired**

### Suggested Reading

If you aren\'t familiar with Qwiic, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend taking a look at some of our other tutorials and familiarizing yourself with some of these topics and parts. We will end up working with the Raspberry Pi and Python programming language.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-4-kit-hookup-guide)

### Raspberry Pi 4 Kit Hookup Guide 

March 14, 2020

Guide for hooking up your Raspberry Pi 4 Model B basic, desktop, or hardware starter kit together.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

June 27, 2018

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide)

### AVR-Based Serial Enabled LCDs Hookup Guide 

The AVR-based Qwiic Serial Enabled LCDs are a simple and cost effective solution to include in your project. These screens are based on the HD44780 controller, and include ATmega328P with an Arduino compatible bootloader. They accept control commands via Serial, SPI and I2C (via PTH headers or Qwiic connector). In this tutorial, we will show examples of a simple setup and go through each communication option.

[](https://learn.sparkfun.com/tutorials/sparkfun-9dof-imu-icm-20948-breakout-hookup-guide)

### SparkFun 9DoF IMU (ICM-20948) Breakout Hookup Guide 

How to use the SparkFun 9DoF ICM-20948 breakout board for your motion sensing projects. This breakout is ideal for wearable sensors and IoT applications.

[](https://learn.sparkfun.com/tutorials/qwiic-shim-for-raspberry-pi-hookup-guide)

### Qwiic SHIM for Raspberry Pi Hookup Guide 

Ever wanted to prototype I2C components on a Pi? Now you can!

## Hardware Assembly

The hardware that is included in this kit is a 16x2 SerLCD with RGB backlight, 9DoF IMU (ICM-20948), Qwiic SHIM, and Qwiic cables. The Qwiic connector color may vary. This should not affect the overall functionality of the boards.

[![Qwiic SHIM Kit](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/16987-SparkFun_Qwiic_SHIM_Kit_for_Raspberry_Pi-01a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/16987-SparkFun_Qwiic_SHIM_Kit_for_Raspberry_Pi-01a.jpg)

Connecting Qwiic devices to the Raspberry Pi makes it even easier than ever with the Qwiic SHIM. Slide the Qwiic SHIM into the Raspberry Pi\'s header so that the square PTH pad is aligned with pin 1.

[![Pi 4 with SHIM](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Raspberry_Pi_GPIO.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Raspberry_Pi_GPIO.jpg)

At this point, connect the Qwiic cable between the boards. Insert the shorter Qwiic cable between the Qwiic SHIM and 9DoF\'s Qwiic connectors. Then insert the longer Qwiic cable between the 9DoF and Qwiic SHIM. The length of the cable between the boards does not really matter so you could insert the cables any way that you would like as well.

[![Qwiic Cable between Qwiic Shim and SerLCD 16x2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Kit_Connected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Kit_Connected.jpg)

Then connect all the necessary peripherals to your Raspberry Pi. In this case, we connected a keyboard, mouse, HDMI monitor, and a power supply.

[![Power and Monitor Cable Connected Full Setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Kit_Raspberry_Pi_Powered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Kit_Raspberry_Pi_Powered.jpg)

## Configure Your Pi

We are going to assume that you already have a Raspberry Pi up and running with Raspbian. We\'ll also assume that it is connected to the Internet. If not, check out our starter kits and tutorials on setting up a Raspberry Pi.

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

Once you are set up, I highly recommend changing your password. At this point, we don\'t want unsavory characters sneaking into your system using the default login: (**username**: pi, **password**: raspberry).

#### Raspberry Pi Configuration [via Desktop GUI]

To change the password using the Desktop GUI, head to the **Raspberry Pi Start Menu** \> **Preferences** \> **Raspberry Pi Configuration** \> **System** \> **Change Password\...**

[![Raspberry Pi Configuration](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/1/Preferences_Raspberry_Pi.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/1/Preferences_Raspberry_Pi.png)

At this point, you can also head to the **Interfaces** tab and set I2C to **Enabled**. Once the settings have been changed, click **OK**.

[![Enable I2C Raspberry Pi Configuration](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Raspberry_Pi_Interface_Peripherals.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Raspberry_Pi_Interface_Peripherals.png)

You will need to restart your Pi before the settings can take effect. Head to **Raspberry Pi Start Menu** \> **Logout** \> **Reboot**

[![Raspberry Pi Logout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/2/Raspberry_Pi_Desktop_Logout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Raspberry_Pi_Desktop_Logout.png)

#### raspi-config Tool [via Terminal]

The [**raspi-config** tool](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide/all#configuring-the-pi) is a quick way to change your password as well as setup the network, language, keyboard, etc. Type the following command using the [command line](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) and then go through the menus to update your information.

    language:bash
    sudo raspi-config

You\'ll want to enable the [I^2^C](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#i2c-on-pi) pins using the tool to read the sensors on the I^2^C bus.

[![Enabling I2C on a Pi](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/9/i2c-menu2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/9/i2c-menu2.png)

*Raspi-config for I^2^C*

You will need to restart your Pi before the settings can take effect. After exiting raspi-config, let\'s reboot your Pi with the following command.

    language:bash
    sudo reboot

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

**Notice:** This tutorial was written with the following software versions.\
\

- Raspbian Pi OS Full (32-bit) version 10, Kernel version 5.4 (Released 12/2/2020)
- Python version 3.7.3
- pip 20.3.3 for Python 3.7

\
Other versions may affect how some of the steps in this guide are performed.

### Indentation

In many programming languages, we indent things to make things easier to read. In Python, those indents are part of the code. Instead of putting brackets around your loop or `if()` statements, you just [indent that entire chunk](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/programming-in-python#indent) with a leading whitespace. In other words, you have to make sure your indents are correct. I also recommend not using your keyboard\'s [TAB] button to indent as various programs will read it differently (and usually incorrectly).

### Commenting

Another thing to keep in mind is comments. In Python, the symbol \"`#`\" is used to denote that the line is a comment. Unlike many other languages there is [no official multi-line comment](https://dbader.org/blog/python-multiline-comment) available. So you\'ll just have to get use to typing `#` for each line when writing large comments.

### Python Versions and Installing PIP

There are also 2 [commonly used Python versions](https://wiki.python.org/moin/Python2orPython3). Even after Python 3 came out many people continued to use 2.7 for many years. Part of the reason is that Python 3 improved on some things and in the process made it not backwards compatible. As of [January 1st, 2020, Python 2 is no longer supported](https://www.python.org/doc/sunset-python-2/). For our example we will be using Python 3.7. To see what version of Python your Pi is using, open a [command line](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) and type each of the following commands individually to check.

    language:bash
    python --version
    python -m pip --version

If you are not using Python 3, then we\'ll need to open the **\*/.bashrc** file and add an alias.

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

To exit nano type [CTRL] + [X] and then hit [Y] when it asks you if you want to save and then [ENTER]. You can now either reboot or type the following to force the Pi to run the **\*.bashrc** file again.

    language:bash
    source ~/.bashrc

Once adjusted, type the following command to ensure that pip is up to date.

    language:bash
    python -m pip install --upgrade pip

## Python Library

We will also need to install the Qwiic Python libraries. This will automatically download a folder containing all the **Qwiic_Py** files and dependencies to your Raspberry Pi. Run the following command to [automatically install](https://github.com/sparkfun/qwiic_py#installation) the modules for the Qwiic sensors and SerLCD. To ensure that you are installing to the correct path for Python 3, make sure that you use `pip3`.

    language:bash
    sudo pip3 install sparkfun_qwiic

**Tip:** If you need to uninstall the library and start from scratch, simply use the `uninstall` with the command:\
\

``` bash
sudo pip3 uninstall sparkfun_qwiic
```

## Example: ICM-20948 Readings

To start, there are basic examples written in Python for the ICM-20948 and SerLCD. We\'ll go over one for each to see if the Qwiic-enabled devices are working as expected.

### Reading the Data with the ICM-20948

In your terminal window, type the following to download the basic example code from the [GitHub repository](https://github.com/sparkfun/Qwiic_9DoF_IMU_ICM20948_Py). Otherwise, you can manually download the example code.

    language:bash
    git clone https://github.com/sparkfun/Qwiic_9DoF_IMU_ICM20948_Py

Then navigate to examples folder by entering the following command.

    language:bash
    cd Qwiic_9DoF_IMU_ICM20948_Py/examples

Using the `ls` command will list the examples in the folder. As of the writing from this tutorial, there\'s only one so we will enter the following command to run the example.

    language:bash
    python ex1_qwiic_ICM20948.py

You should see an output similar to image below. Depending on how the sensor is oriented, the values might be different. Moving the sensor around will change the raw values in the terminal window. The window will probably be too small and wrap around to the next row. To slow the output down, stop the code by typing [CTRL] + [C] and adjust the value for the delay after the `print()` function where it says `time.sleep(0.03)` to a larger number. Once the code has been adjusted, try running the code again.

[![9DoF Readings Through Terminal](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Terminal_Python_9DoF_ICM-20948_readings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Terminal_Python_9DoF_ICM-20948_readings.png)

You could also navigate to the example folder, open the example in Thonny, and hit the Run button. The readings will show up in the shell.

[![Thonny IDE 9DoF ICM20948 Readings](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Thonny_Python_9DoF_ICM-20948_readings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Thonny_Python_9DoF_ICM-20948_readings.png)

## Example: SerLCD - Hello World!

### SerLCD: Hello World!

In your terminal window, type the following to download the basic example code from the [GitHub repository](https://github.com/sparkfun/Qwiic_SerLCD_Py).

    language:bash
    git clone https://github.com/sparkfun/Qwiic_SerLCD_Py

Then navigate to the examples folder by entering the following command.

    language:bash
    cd Qwiic_SerLCD_Py/examples

Using the `ls` command will list the examples in the folder. There are few examples in the folder but we\'re interested in only viewing the \"Hello World!\" example. Enter the following command to run the example.

    language:bash
    python ex1_qwiic_serlcd_hello_world.py

You should see the [familiar phrase \"Hello World!\"](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/hello-world) displayed in the terminal window with a counter increasing.

[![Output Terminal Window](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Terminal_Python_SerLCD_Hello_World.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Terminal_Python_SerLCD_Hello_World.png)

If you are using Thonny, you should see the same output in the Shell.

[![Output Thonny](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Thonny_Python_SerLCD_Hello_World.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Thonny_Python_SerLCD_Hello_World.png)

You should see the same message on the SerLCD with a counter increasing on the next row as well.

[![RGB Character Serial LCD Displaying Hello World with Counter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Kit_SerLCD_Hello_World_Raspberry_Pi.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Kit_SerLCD_Hello_World_Raspberry_Pi.jpg)

Sweet! There are several other examples available in the Qwiic_SerLCD_Py library. Try running the other examples listed in the examples folder to test by using the `python` command followed by the name of the python file.

[GitHub: Qwiic_SerLCD_Py \> examples](https://github.com/sparkfun/Qwiic_SerLCD_Py/tree/main/examples)

## Example: Combined SerLCD and ICM-20948

### Combined Example

This code combines a few of the examples together. The orientation of the 9DoF will control the RGB backlight. For simplicity, we will only display the name of the color. Try scaling the readings down before printing the accelerometer readings on the screen.

In your terminal window, type the following to download the combined example code from the [GitHub repository](https://github.com/sparkfun/Qwiic_SHIM_Kit).

    language:bash
    git clone https://github.com/sparkfun/Qwiic_SHIM_Kit

Then navigate to the examples folder by entering the following command.

    language:bash
    cd Qwiic_SHIM_Kit/examples

Enter the following command to run the combined example.

    language:bash
    python combined1_RGB_SerLCD_ICM20948.py

You can also copy the example below.

    language:python
    #!/usr/bin/env python3
    #-----------------------------------------------------------------------------
    # combined1_RGB_SerLCD_ICM20948.py
    #
    # Combined example to control the RGB LED on the SerLCD
    # based on the accelerometer readings on the ICM20948.
    #------------------------------------------------------------------------
    #
    # Written by  SparkFun Electronics, March 2020
    # 
    # This python library supports the SparkFun Electroncis qwiic 
    # qwiic sensor/board ecosystem on a Raspberry Pi (and compatible) single
    # board computers. 
    #
    # More information on qwiic is at https://www.sparkfun.com/qwiic
    #
    # Do you like this library? Help support SparkFun. Buy a board!
    #
    #==================================================================================
    # Copyright (c) 2019 SparkFun Electronics
    #
    # Permission is hereby granted, free of charge, to any person obtaining a copy 
    # of this software and associated documentation files (the "Software"), to deal 
    # in the Software without restriction, including without limitation the rights 
    # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
    # copies of the Software, and to permit persons to whom the Software is 
    # furnished to do so, subject to the following conditions:
    #
    # The above copyright notice and this permission notice shall be included in all 
    # copies or substantial portions of the Software.
    #
    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
    # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
    # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
    # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
    # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
    # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
    # SOFTWARE.
    #==================================================================================

    from __future__ import print_function
    import qwiic_serlcd
    import qwiic_icm20948
    import time
    import sys

    #create global variable to keep track of color when debugging
    ledColor = 1

    def runExample():

        print("\nSparkFun SerLCD and 9DoF ICM-20948 Sensor Example\n")
        myLCD = qwiic_serlcd.QwiicSerlcd()
        IMU = qwiic_icm20948.QwiicIcm20948()

        if myLCD.connected == False:
            print("The Qwiic SerLCD device isn't connected to the system. Please check your connection", \
                file=sys.stderr)
            return

        if IMU.connected == False:
            print("The Qwiic ICM20948 device isn't connected to the system. Please check your connection", \
                  file=sys.stderr)
            return

        myLCD.setBacklight(255, 255, 255) # Set backlight to bright white
        myLCD.setContrast(5)  # Set contrast. Lower to 0 for higher contrast.
        myLCD.clearScreen()   # Clear Screen - this moves the cursor to the home position as well
        myLCD.print("white")  # Write to color name to SerLCD

        time.sleep(0.5) # give a sec for system messages to complete

        IMU.begin()

        while True:
            #declare ledColor a global variable inside here to access it 
            global ledColor

            if IMU.dataReady():
                IMU.getAgmt() # read all axis and temp from sensor, note this also updates all instance variables

                #the following are the threshold values for each axis is pointing right-side up

                # anything above IMU.azRaw > 16000 is red
                # ledColor = 1
                aZPos = 16000

                # anything below IMU.azRaw < -16000 is blue
                # ledColor = 2
                aZNeg = -16000

                # anything above IMU.ayRaw > 16100 is green
                # ledColor = 3
                ayPos = 16100

                # anything below IMU.ayRaw < -16000 is green
                # ledColor = 4
                ayNeg = -16000

                # anything above IMU.axRaw > 16000 is magenta
                # ledColor = 5
                axPos = 16000

                # anything below IMU.axRaw < -16400 is cyan
                # ledColor = 6
                axNeg = -16400

                #adjust color of the LED based on the accelerometer's reading
                if IMU.azRaw > aZPos:
                    # Set LED red
                    myLCD.setBacklight(255, 0, 0) # Set backlight to bright white
                    ledColor = 1
                    myLCD.clearScreen()
                    myLCD.print("red")

                elif IMU.azRaw < aZNeg:
                    # Set LED blue
                    myLCD.setBacklight(0, 0, 255) # Set backlight to bright white
                    ledColor = 2
                    myLCD.clearScreen()
                    myLCD.print("blue")

                elif IMU.ayRaw > ayPos:
                    # Set LED yellow
                    myLCD.setBacklight(255, 255, 0) # Set backlight to bright white
                    ledColor = 3
                    myLCD.clearScreen()
                    myLCD.print("yellow")

                elif IMU.ayRaw < ayNeg:
                    # Set LED green
                    myLCD.setBacklight(0, 255, 0) # Set backlight to bright white
                    ledColor = 4
                    myLCD.clearScreen()
                    myLCD.print("green")

                elif IMU.axRaw > axPos:
                    # Set LED magenta
                    myLCD.setBacklight(255, 0, 255) # Set backlight to bright white
                    ledColor = 5
                    myLCD.clearScreen()
                    myLCD.print("magenta")

                elif IMU.axRaw < axNeg:
                    # Set LED cyan
                    myLCD.setBacklight(0, 255, 255) # Set backlight to bright white
                    ledColor = 6
                    myLCD.clearScreen()
                    myLCD.print("cyan")

                if ledColor == 1:
                    print("ledColor = red" ,'\n', '\n')
                elif ledColor == 2:
                    print("ledColor = blue" ,'\n', '\n')
                elif ledColor == 3:
                    print("ledColor = yellow" ,'\n', '\n')
                elif ledColor == 4:
                    print("ledColor = green" ,'\n', '\n')
                elif ledColor == 5:
                    print("ledColor = magenta" ,'\n', '\n')
                elif ledColor == 6:
                    print("ledColor = cyan" ,'\n', '\n')

                aX = IMU.axRaw
                aY = IMU.ayRaw
                aZ = IMU.azRaw
                gX = IMU.gxRaw
                gY = IMU.gyRaw
                gZ = IMU.gzRaw
                mX = IMU.mxRaw
                mY = IMU.myRaw
                mZ = IMU.mzRaw

                # Remove the `#` for the following lines to 
                # display accelerometer readings on SerLCD

                #myLCD.setCursor(8,0)
                #myLCD.print("aX")
                #myLCD.print(str(aX))

                #myLCD.setCursor(0,1)
                #myLCD.print("aY")
                #myLCD.print(str(aY))

                #myLCD.setCursor(8,1)
                #myLCD.print("aZ")
                #myLCD.print(str(aZ))

                print(\
                 ' aX:', ''.format(aX)\
                , ' \t, aY:', ''.format(aY)\
                , '\t, aZ:', ''.format(aZ)\
                , '\n gX:', ''.format(gX)\
                , '\t, gY:', ''.format(gY)\
                , '\t, gZ:', ''.format(gZ)\
                , '\n mX:', ''.format(mX)\
                , '\t, mY:', ''.format(mY)\
                , '\t, mZ:', ''.format(mZ)\
                , '\n'\
                )

                time.sleep(1) # small delay so that the screen doesn't flicker
            else:
                print("Waiting for data")
                time.sleep(0.5)

    if __name__ == '__main__':
        try:
            runExample()
        except (KeyboardInterrupt, SystemExit) as exErr:
            print("\nEnding Combined Example")
            sys.exit(0)

The terminal will begin displaying the current color and sensor readings.

[![Terminal Output of Combined Example](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Terminal_Python_SerLCD_RGB_9DoF_ICM-20948.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Terminal_Python_SerLCD_RGB_9DoF_ICM-20948.png)

If you are using Thonny, you will see the same output in the Shell.

[![Thonny Output of Combined Example](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Thonny_Python_SerLCD_RGB_9DoF_ICM-20948.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Thonny_Python_SerLCD_RGB_9DoF_ICM-20948.png)

If you check out the SerLCD with RGB backlight, the screen will display the color name and color backlight based on the accelerometer readings. The color will change depending on what axis is pointing up. Your setup may look slightly different depending on how you connected the Qwiic cables so be sure to reference the silkscreen for the accelerometer.

[![RGB Character Serial LCD Display Controlled by the ICM-20948\'s accelerometer readings ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Kit_RGB_LED_Serial_LCD_9DoF_ICM20948_Raspberry_Pi.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/2/Qwiic_SHIM_Kit_RGB_LED_Serial_LCD_9DoF_ICM20948_Raspberry_Pi.jpg)