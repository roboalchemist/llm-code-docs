# Source: https://learn.sparkfun.com/tutorials/raspberry-pi-zero-helmet-impact-force-monitor

## Introduction

[] **Read Time:** \~ 15 minutes

[] **Build Time:** \~ 60 - 90 minutes

How much impact can the human body handle? Whether it\'s football, rock climbing, or a bicycle accident, knowing when to seek immediate medical attention after a collision is incredibly important, especially if there are no obvious signs of trauma. This tutorial will teach you how to build your very own impact force monitor!

[![System Alert](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/CoverPhoto-SystemALRTHelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/CoverPhoto-SystemALRTHelmetForceMonitor.jpg)

This open-source project uses a Raspberry Pi Zero W and an LIS331 accelerometer to monitor and alert the user of potentially dangerous G-forces. Of course, feel free to modify and adapt the system to suit your various citizen science needs.

**Note**: Build fun stuff with the Impact Force Monitor! However, please don\'t use it as a substitute for professional medical advice and diagnosis. If you feel that you have taken a serious fall, please visit a qualified and licensed professional for proper treatment.

### Suggested Video

### Suggested Reading

To keep this tutorial short n\' sweet (er, well, as much as possible), I\'m assuming you\'re starting with a functional Pi Zero W. Need some help? No problem! [Here\'s a full setup tutorial.](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless)

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless)

### Getting Started with the Raspberry Pi Zero Wireless 

July 13, 2017

Learn how to setup, configure and use the smallest Raspberry Pi yet, the Raspberry Pi Zero - Wireless.

We\'ll also be connecting to the Pi remotely (aka wirelessly). For a more thorough overview on this process [check out this tutorial on making a \"headless\" Raspberry Pi](http://foxbotindustries.com/intro-headless-raspberry-pi/):

[Intro to the (Headless) Raspberry Pi!](http://foxbotindustries.com/intro-headless-raspberry-pi/)

#### Stuck or Want to Learn More? Here Are Some Handy Resources:

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/raspberry-gpio)

### Raspberry gPIo 

How to use either Python or C++ to drive the I/O lines on a Raspberry Pi.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

### Raspberry Pi SPI and I2C Tutorial 

Learn how to use serial I2C and SPI buses on your Raspberry Pi using the wiringPi I/O library for C/C++ and spidev/smbus for Python.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

Also, check out the datasheet for the LIS331.

[LIS331 Datasheet](https://www.sparkfun.com/datasheets/Sensors/Accelerometer/LIS331HH.pdf)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[Helmet Impact Force Monitor Wish List](https://www.sparkfun.com/wish_lists/143353)

The items in the wishlist include:

- [Raspberry Pi Zero W Basic Kit](https://www.sparkfun.com/products/14298)
  - microSD Card w/ NOOBS OS
  - USB OTG Cable (micro-B to Female A USB)
  - Mini HDMI to HDMI
  - Micro-B Wall Adapter (5V)
  - *Also Recommended: USB Hub*
- [Raspberry Pi 3 Header Pins](https://www.sparkfun.com/products/14275)
- [LIS331 Accelerometer Breakout Board](https://www.sparkfun.com/products/10345)
- [Battery Pack w/ Micro-B Connector](https://www.sparkfun.com/products/14169)
- [LED - Basic Red 5mm](https://www.sparkfun.com/products/9590)
- [1kΩ Resistor](https://www.sparkfun.com/products/13760)
- 6\" [Heat Shrink Tube](https://www.sparkfun.com/products/9353) or Electrical Tape
- 4x [Header Pins](https://www.sparkfun.com/products/116)
  - 8x Pins for Accelerometer
  - 2x Pins for LED
- 6x [Female-to-Female Jumper Wires](https://www.sparkfun.com/products/8430)

### Tools

You will also need the following tools.

- [Soldering Iron, Solder, and Accessories](https://www.sparkfun.com/categories/49)
- Epoxy (Or Other Permanent, Non-Conductive Liquid Adhesive)
- *Scissors (Optional)*

## But Wait! What is Impact Force??

Fortunately, the term \"impact force\" is pretty straightforward: the amount of force in an impact. Like most things though, measuring it requires a more precise definition. The equation for impact force is:

[![Force Equation](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/ForceEquationLatex.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/ForceEquationLatex.png)

where *F* is the impact force, *KE* is the kinetic energy (energy of motion), and *d* is the impact distance, or how much the object crunches.

There are two key takeaways from this equation:

- Impact force is *directly proportional* to the kinetic energy, meaning that the **impact force increases if the kinetic energy increases**.
- Impact force is *inversely proportional* to impact distance, meaning that the **impact force decreases if the impact distance increases**. (This is why we have airbags: to increase the distance of our impact.)

Force is typically measured in Newtons (N), but impact force may be discussed in terms of a \"G-Force\", a number expressed as a multiple of *g*, or earth\'s gravitational acceleration (9.8 m/s\^2). When we use units of G-force, we are measuring an objects acceleration relative to free fall towards the earth. Technically speaking, *g* is an acceleration, not a force. However, it is useful when talking about collisions because acceleration (*the change in speed and/or direction*) is what damages the human body.

For this project, we\'ll use G-force units to determine if an impact is potentially dangerous and deserving of medical attention. [Research has found](https://hypertextbook.com/facts/2004/YuriyRafailov.shtml) that g-forces above 9G can be fatal to most humans (without special training), and 4-6G can be dangerous if sustained for more than a few seconds.

Knowing this, we can program our impact force monitor to alert us if our accelerometer measures a G-force above either of these thresholds. Hooray, science!

For more information, read about [impact force](https://en.wikipedia.org/wiki/Impact_(mechanics)) and [G-force](https://en.wikipedia.org/wiki/G-force) on Wikipedia!

## Configure the Pi Zero W

Gather your Raspberry Pi Zero and peripherals to configure the Pi to be headless!

[![Pi Zero Setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/PiZeroKit-2HelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/PiZeroKit-2HelmetForceMonitor.jpg)

- Connect the Pi to a monitor and associated peripherals (keyboard, mouse), plug in the power supply, and log in.

- Update software to keep your Pi speedy & secure. Open the [terminal window](https://learn.sparkfun.com/tutorials/terminal-basics) and type these commands:

  - Type and enter: `sudo apt-get update`

  - Type and enter: `sudo apt-get upgrade`

  - Reset: `sudo shutdown -r now`

### Enable WiFi, SSH, and I2C.

- Click the WiFi icon on the upper right corner of the desktop and connect to your WiFi network.

- In the terminal type this command to bring up the Pi\'s Software Configuration Tool: `sudo raspi-config`

[![Serial Terminal Interfacing Options](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/PiZero-RaspPiConfig1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/PiZero-RaspPiConfig1.jpg)

- Select \"*Interfacing Options*\", then \"*SSH*\", and choose \"*Yes*\" at the bottom to enable.

- Go back to \"*Interfacing Options*\", then \"*I2C*\", and select \"*Yes*\" to enable.

- In the terminal, install remote desktop connection software: `sudo apt-get install xrdp`

  - Type \'Y\' (yes) on your keyboard to both prompts.

  - Find the Pi\'s IP address by hovering over the WiFi connection (you might also want to write it down).

[![IP Address](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/PiZero-EasyIPAddr.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/PiZero-EasyIPAddr.jpg)

- Change the Pi\'s password with the `passwd` command.

### Restart the Pi and Log In Remotely.

We can now ditch the HDMI and peripherals, woohoo!

- Setup a remote desktop connection.

  - On a PC, open Remote Desktop Connection (or PuTTY if you\'re comfy with that).

  - For Mac/Linux, you can install this program or use a VNC program.

- Enter the IP for the Pi and click \"*Connect*\" (Ignore warnings about unknown device).

[![Remote Desktop Connection](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/RemoteDesktopConnection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/RemoteDesktopConnection.jpg)

- Log in to the Pi using your credentials and away we go!

## Build it: Electronics!

Here\'s the electrical schematic for this project:

[![Fritzing Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/ImpactForceMonitor-FritzingSchematic_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/ImpactForceMonitor-FritzingSchematic_bb.jpg)

**Note:** The LIS331 breakout board in the schematic is an older version \-- use the pin labels for guidance.

Here\'s the pinout for the Pi Zero W for reference:

[![Raspberry Pi Zero Graphical Datasheet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/6/PiZero_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/PiZero_1.pdf)

*Click on the image to view the PDF.*

### Connect the LIS331 Accelerometer to the Pi\'s GPIO

[Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) and carefully remove any flux residue on the accelerometer and Pi GPIO\'s header pins.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/LIS331-HeadersBackHelmetForceMonitor.jpg "Accelerometer Headers")](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/LIS331-HeadersBackHelmetForceMonitor.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/PiZero-Closeup_HeadersHelmetForceMonitor.jpg "Pi Zero Headers")](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/PiZero-Closeup_HeadersHelmetForceMonitor.jpg)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Then connect jumper wires between the LIS331 breakout board and Pi between the following pins:

  LIS331 Breakout Board   Raspberry Pi GPIO Pin
  ----------------------- -----------------------
  GND                     GPIO 9 (GND)
  VCC                     GPIO 1 (3.3V)
  SDA                     GPIO 3 (SDA)
  SCL                     GPIO 5 (SCL)

To make it easier to connect the sensor to the Pi Zero, a custom adapter was made by using a female header and jumper wires. Heat shrink was added after testing the connections.

[![Connect the LIS3311 to a Pi GPIO Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/PiZero-LIS331HelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/PiZero-LIS331HelmetForceMonitor.jpg)

### Add an Alert LED!

Solder a current limiting resistor to the negative LED leg (shorter leg) and add shrink wrap (or electrical tape) for insulation.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/LED-ResistorHelmetForceMonitor.jpg "Solder the Resistor and LED")](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/LED-ResistorHelmetForceMonitor.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/LED-ShrinkTubeHelmetForceMonitor.jpg "Shrink Tube")](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/LED-ShrinkTubeHelmetForceMonitor.jpg)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use two jumper cables or header pins to connect the positive LED leg to GPIO26 and the resistor to GND (header positions 37 and 39, respectively).

### Completed Setup

Connect the battery pack to the Pi\'s input power to complete the setup!

[![Completed Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/FullSystem-Electronics_OFFHelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/FullSystem-Electronics_OFFHelmetForceMonitor.jpg)

## Program It!

The Python code for this project is open-source! [Here\'s a link to the GitHub repository](https://github.com/jenfoxbot/ImpactForceMonitor).

[ImpactForceMonitor GitHub Repo](https://github.com/jenfoxbot/ImpactForceMonitor)

### For Folks New to Programming:

- Read through the program code and comments. Things that are easy to modify are in the \"`User Parameters`\" section at the top.

### For Folks More Comfortable w/ the Technical \'Deets:

- This program initializes the LIS331 accelerometer with default settings, including normal power mode and 50Hz data rate. Read through the [LIS331 datasheet](https://www.sparkfun.com/datasheets/Sensors/Accelerometer/LIS331HH.pdf) and modify initialization settings as desired.

### All:

- The maximum acceleration scale used in this project is 24G, because impact force gets big real quick!

- It is recommended to comment out the acceleration print statements in the main function when you are ready for full deployment.

Before you run the program, double check that the accelerometer address is **0x19**. Open the terminal window and install some helpful tools with this command:

    sudo apt-get install -y i2c-tools

Then run the *i2cdetect* program:

    i2cdetect -y 1

You\'ll see a table of I2C addresses displayed as shown in the image below. Assuming this is the only I2C device connected, the number you see (in this case: 19) is the accelerometer address! If you see a different number, take note and change in the program (variable `addr`).

[![Pi i2cdetect command line](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/Pi-I2C_DetectAddress.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/Pi-I2C_DetectAddress.jpg)

### Quick Overview

The program reads the x, y, and z acceleration, calculates a g-force, and then saves the data in two files (in the same folder as the program code) as appropriate:

- **AllSensorData.txt** \-- gives a timestamp followed by the g-force in the x, y, and z axes.
- **AlertData.txt** \-- same as above but only for readings that are above our safety thresholds (absolute threshold of 9G or 4G for more than 3 seconds).

G-forces above our safety thresholds will also turn on our alert LED and keep it on until we restart the program. Stop the program by typing \"**CTRL+c**\" (keyboard interrupt) in the command terminal.

Here\'s a photo of both data files created during testing:

[![Impact Force Data](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/AcclDataTextFiles-AllSensorData_and_AlertData.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/AcclDataTextFiles-AllSensorData_and_AlertData.jpg)

*Having a hard time seeing the data? Click the image for a closer look.*

## Test the System!

Open the terminal window, navigate to the folder where you saved the program code using the `cd` command.

    cd path/to/folder

Run the program using root privileges:

    sudo python NameOfFile.py

Check that the acceleration values in the x, y, and z-direction are printing to the terminal window, are reasonable, and turn on the LED light if the g-force is above our thresholds.

- To test, rotate the accelerometer so that the each axes point towards the earth and check that the measured values are either 1 or -1 (corresponds to acceleration due to gravity).

- Shake the accelerometer to make sure the readings increase (sign indicates direction of axis, we\'re most interested in the *magnitude* of the reading).

[![Testing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/FullSystem-ElectronicsON2HelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/FullSystem-ElectronicsON2HelmetForceMonitor.jpg)

## Install It!

Once everything is working correctly, let\'s make sure the impact force monitor can actually withstand impact!

### Secure Connections

Use heat shrink tube and/or coat the electrical connections for the accelerometer and LED in epoxy.

[![Heat Shrink Connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/LIS331-FullConnector1HelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/LIS331-FullConnector1HelmetForceMonitor.jpg)

For super durable, permanent installations, consider coating the whole shebang in epoxy: the Pi Zero, the LED, and the accelerometer (but NOT the Pi cable connectors or the SD card).

**Warning!** You can still access the Pi and do all the computer stuff, but a full coat of epoxy will prevent the use of the GPIO pins for future projects.\
\
Alternatively, you can make or purchase a custom case for the Pi Zero, although check for durability.

Secure to a helmet, your person, or a mode of transportation like your skateboard, bicycle, or cat\*!

**\*Note:** I originally meant to type \"car\", but figured an impact force monitor for a cat might also yield some interesting data (with kitty\'s consent, of course).

Fully test that the Pi is securely fastened or the GPIO pins may become loose causing the program to crash.

### Embedding the Circuit in a Helmet

Theres a few methods of embedding the circuit into a helmet. Here\'s my approach to a helmet installation:

If you have not already, connect battery to Pi (with battery off). Secure the accelerometer to the back of the Pi with nonconductive insulation in between (like bubble wrap or thin packing foam).

[![Bubble Wrap Insulation Between Sensor and Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/Installation-LIS331CloseUpHelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/Installation-LIS331CloseUpHelmetForceMonitor.jpg)

Measure the dimensions of the Pi Zero, accelerometer, LED, and battery connector combination. Add 10% on either side.

[![Measure Size of Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/Installation-Measurement1HelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/Installation-Measurement1HelmetForceMonitor.jpg)

Draw a cutout for the project on one side of the helmet, with the battery connector facing towards the top of the helmet. Cut out the padding in the helmet leaving a few millimeters (\~ 1/8 in.).

[![Cut Pocket in Helmet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/Installation-HelmetCutout1HelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/Installation-HelmetCutout1HelmetForceMonitor.jpg)

Place the sensor, Pi, and LED in the cutout. Cut pieces of the excess helmet padding or use packaging foam to insulate, protect, and hold the electronics in place.

[![Insert Electronics into Helmet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/Installation-Electronics3HelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/Installation-Electronics3HelmetForceMonitor.jpg)

Measure the battery\'s dimensions, add 10%, and follow the same cutout for the battery. Insert the battery into the pocket.

[![Battery Pocket in Helmet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/Installation-Battery1HelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/Installation-Battery1HelmetForceMonitor.jpg)

Repeat the insulation technique for the battery on the other side of the helmet.

[![Insert Battery into Helmet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/Installation-BatteryPaddingHelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/Installation-BatteryPaddingHelmetForceMonitor.jpg)

Hold the helmet padding in place with tape (your head will keep \'em in place when you are wearing it).

## Deploy!

Power up the battery pack!

[![Powered Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/Helmet-SystemON_closeupHelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/Helmet-SystemON_closeupHelmetForceMonitor.jpg)

Now you can remotely log into the Pi through SSH or remote desktop and run the program via the terminal. Once the program is running, it starts recording data.

When you disconnect from your home WiFi, the SSH connection will break, but the program should still log data. Consider connecting the Pi to your smartphone hotspot WiFi, or just log back in and grab the data when you get home.

[![Use Command Line to Start Program Remotely](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/FinalSystem-RunProgram.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/FinalSystem-RunProgram.jpg)

To access the data, remotely log into the Pi and read the text files. The current program will always append data to the existing files \-- if you want to delete data (like from testing), delete the text file (via the desktop or use the `rm` command in the terminal) or create a new file name in the program code (in User Parameters).

If the LED is on, restarting the program will turn it off.

Now go forth, have fun in life, and check on the data every so often if you happen to bump into something. Hopefully, it\'s a small bump but at least you\'ll know!

[![Monitoring](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/1/CoverPhoto-SystemONHelmetForceMonitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/1/CoverPhoto-SystemONHelmetForceMonitor.jpg)

## Adding More Features

Looking for improvements to the impact force monitor? It is outside the scope of the tutorial but try looking at the list below for ideas!

- Do some analysis on your g-force data in Python!
- The Pi Zero has Bluetooth and WiFi capabilities \-- write an App to send the accelerometer data to your smartphone! To get you started, here\'s a tutorial for a [Pi Twitter Monitor](https://learn.sparkfun.com/tutorials/raspberry-pi-twitter-monitor).
- Add in other [sensors](https://www.sparkfun.com/search/results?term=sensor), like a [temperature sensor](https://www.sparkfun.com/products/13314) or a [microphone](https://www.sparkfun.com/products/9868)\*!

**\*Note:** To hear the whooshing sounds associated with your acceleration! :D