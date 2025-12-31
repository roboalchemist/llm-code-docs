# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---console-block

## Introduction

The [Console Block](https://www.sparkfun.com/products/13039) is one of the simplest ways to power and communicate with an Intel Edison. Utilizing the FTDI 231X, this creates a USB to serial bridge that is level shifted to the proper 1.8V required by the Edison. The Console is found on UART2. This block is also capable of providing power to the Edison as well as other stacked Blocks.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/Console_ISOscaled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/Console_ISOscaled.jpg)

*Console Block*

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Edison adventure include:

- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)
- [Serial Terminal Basics](https://learn.sparkfun.com/tutorials/terminal-basics)

## Board Overview

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/2/Console_Annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/Console_Annotated.png)

*Console Block Functional Diagram TOP*

- USB Micro B - The USB port provides power and a console access port to an Intel Edison Stack. This Block supplies a voltage to the Edison and other Blocks through the VSYS line at 4V. This voltage may vary up to +/-0.1V depending on load.

- Power Button - The power switch is connected to the \"PWRBTN\" line on the Edison. This gives the user the ability to place an Edison in sleep or power down the module completely. This does not affect power to other Blocks in the stack.

- Power LED - The power LED illuminates when power is present on VSYS. This can come from the Console Block, or any other powered Block in the stack.

- Data LEDs - The Data LEDs help the user identify if the console is active. This is a feature commonly found on our [FTDI breakout](https://www.sparkfun.com/products/9716).

- LED Jumpers - If power consumption is an issue, cut each jumper to disable LEDs

- Expansion Header - The 70-pin Expansion header breaks out the functionality of the Intel Edison. This header also passes signals and power throughout the stack. These function much like an [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields).

## Using the Console Block

To use the console Block, attach an Intel Edison to the back of the board, or add it to your current stack. Blocks can be stacked without hardware, but it leaves the expansion connectors unprotected from mechanical stress.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/2/Edison_Block_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/Edison_Block_Tutorial-06.jpg)

*Console Block Installed*

We have a nice [Hardware Pack](https://www.sparkfun.com/products/13187) available that gives enough hardware to secure three blocks and an Edison.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/EdisonHardware.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/EdisonHardware.jpg)

[*Intel Edison Hardware Pack*](https://www.sparkfun.com/products/13187)

### Connecting to the Console

Once you have connected your hardware, plug the [Micro USB cable](https://www.sparkfun.com/products/10215) into the Block. If you do not have FTDI drivers currently installed, you\'ll need to download and install them before using your Edison. Visit our [tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) for instructions on how to install the drivers. After you have ensured that the drivers are installed and your device is running, open your favorite terminal program and point it to the USB-serial connection. We have another tutorial to explain [terminal programs and how to use them](https://learn.sparkfun.com/tutorials/terminal-basics).

The standard Baud Rate is 115200bps.

Once a terminal is active you are ready to explore!

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/ConsoleTerminalView.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/ConsoleTerminalView.PNG)

### Using the Power Button

The power button on the Edison brings a unique feature commonly not found on single board computers. The power button behaves much like the power buttons on desktop and laptop computers.

- While powered, Holding the power button for \~10 seconds will power down the Edison.
- While un-powered, pressing the power button momentarily will reboot the Edison.
- While powered, pressing the power button momentarily will place the Edison in sleep mode.
- While in sleep mode, pressing the power button momentarily will wake the Edison.