# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---base-block-

## Introduction

The [Base Block](https://www.sparkfun.com/products/13045) is a great foundation to any Edison stack. The Base is useful for mounting an Edison as a file system on a host computer or accessing the console port. The Base Block provides the same functionality as the [Intel® Edison and Mini Breakout](https://www.sparkfun.com/products/13025) board with the added capability of powering the Edison through the Console port, freeing the OTG port for device usage. Use this block to load new OS images or firmware.

[![base block](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/0/13045-01Crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/0/13045-01Crop.jpg)

*Base Block*

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Edison adventure include:

- [Powering Your Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics)

## Board Overview

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/0/BaseAnnotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/0/BaseAnnotated.png)

*Base Block Functional Diagram*

- USB OTG - The USB Micro AB port provides access to the Edison OTG port. This port is capable of providing power to an OTG device or power can be supplied to the Edison through this port.

- Console - The Micro USB B port provides power and a console access port to an Intel Edison Stack. This Block supplies a voltage to the Edison and other Blocks through the VSYS line at 4V. This voltage may vary up to +/-0.1V depending on load.

- Power Button - The power switch is connected to the \"PWRBTN\" line on the Edison. This gives the user the ability to place an Edison in sleep or power down the module completely. This does not affect power to other Blocks in the stack.

- Power LED - The power LED illuminates when power is present on VSYS. This can come from the Console Block, or any other powered Block in the stack.

- Data LEDs - The Data LEDs help the user identify if the console is active. This is a feature commonly found on our [FTDI breakout](https://www.sparkfun.com/products/9716).

- LED Jumpers - If power consumption is an issue, cut each jumper to disable LEDs

- Expansion Header - The 70-pin Expansion header breaks out the functionality of the Intel Edison. This header also passes signals and power throughout the stack. These function much like an [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields).

## Using the Base Block

To use the Base Block, attach an Intel Edison to the back of the board, or add it to your current stack. Blocks can be stacked without hardware, but it leaves the expansion connectors unprotected from mechanical stress.

[![Edison screwed to the Base Block](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/5/Smart_Mirror_Project-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/5/Smart_Mirror_Project-01.jpg)

*Base Block Installed*

We have a nice [Hardware Pack](https://www.sparkfun.com/products/13187) available that gives enough hardware to secure three blocks and an Edison.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/EdisonHardware.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/EdisonHardware.jpg)

[*Intel Edison Hardware Pack*](https://www.sparkfun.com/products/13187)

### Connecting to the Console

Once you have connected your hardware, plug the [Micro USB cable](https://www.sparkfun.com/products/10215) into the Block. If you do not have FTDI drivers currently installed, you\'ll need to download and install them before using your Edison. Visit our [tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) for instructions on how to install the drivers. After you have ensured that the drivers are installed and your device is running, open your favorite terminal program and point it to the USB-serial connection. We have another tutorial to explain [terminal programs and how to use them](https://learn.sparkfun.com/tutorials/terminal-basics).

The standard Baud Rate is 115200bps.

After you\'ve opened up the serial port, **try hitting enter** a couple times. If all goes well, the Edison should respond with a login prompt.

The default Edison login is **root**. There is no password\...yet. You can run `passwd`, if you want to set one now, but it will be wiped out when/if you update the firmware image. (See the [Edison Getting Started Guide](https://learn.sparkfun.com/tutorials/edison-getting-started-guide) for more info.)

Once you\'ve logged in you are ready to explore!

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/ConsoleTerminalView.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/ConsoleTerminalView.PNG)

### Using the OTG port

Intel has done a great job at making the OTG port functionality seamless. If you wish to access the Edison as a mass file storage device or network device, plug a USB Micro B cable into the OTG port from a host computer. The device should automatically appear.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/0/EdisonPopUp.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/0/EdisonPopUp.PNG)

You can also load new OS images to the Edison over the OTG port. See the [Loading Debian Ubilinux on the Edison](/tutorials/loading-debian-ubilinux-on-the-edison) tutorial for more details.

To use a USB device on the Edison, use our [USB OTG Cable](https://www.sparkfun.com/products/11604) and plug in your device. The Edison will supply the necessary power for small USB devices. To find your connected device enter the following command into a console session.

    lsusb

This should list any available USB devices installed.

### Using the Power Button

The power button on the Edison brings a unique feature commonly not found on single board computers. The power button behaves much like the power buttons on desktop and laptop computers.

- While powered, Holding the power button for \~10 seconds will power down the Edison.
- While un-powered, pressing the power button momentarily will reboot the Edison.
- While powered, pressing the power button momentarily will place the Edison in sleep mode.
- While in sleep mode, pressing the power button momentarily will wake the Edison.