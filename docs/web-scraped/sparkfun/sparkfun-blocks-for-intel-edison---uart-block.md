# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---uart-block

## Introduction

The [UART Block](https://www.sparkfun.com/products/13040) provides a level shifted interface to the console port or second UART port. This is a great solution when USB is not an option. This allows the Edison module to be interfaced with legacy hardware by providing a protected signal interface. Using a [RS232 Shifter](https://www.sparkfun.com/products/449), it is possible to connect an Edison to RS232 devices commonly found in older automation equipment and instrumentation. The UART Block paired with a 5V Compatible FTDI device, such as our [FTDI Basic Breakout](https://www.sparkfun.com/products/9716), will power an Edison Stack.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/7/13040-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/7/13040-01.jpg)

*UART Block*

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Edison adventure include:

- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)
- [Serial Terminal Basics](https://learn.sparkfun.com/tutorials/terminal-basics)
- [Powering Your Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics)

## Board Overview

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/7/UARTAnnotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/7/UARTAnnotated.png)

*UART Block Functional Diagram*

- UART Header - Standard FTDI header with RX, TX, VCC, and GND broken out.

- Select Switch - Select between Console (UART2) and UART1

- Power Button - The power switch is connected to the \"PWRBTN\" line on the Edison. This give the user the ability to place an Edison in sleep or power down the module completely. This does not affect power to other Blocks in the stack.

- Power LED - The power LED illuminates when power is present on VSYS. This can come from the Console Block, or any other powered Block in the stack.

- LED Jumper - If power consumption is an issue, cut each jumper to disable LED

- Expansion Header - The 70-pin Expansion header breaks out the functionality of the Intel Edison. This header also passes signals and power throughout the stack. These function much like an [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields).

## Using the UART Block

To use the UART Block, attach an Intel Edison to the back of the board or add it to your current stack. Blocks can be stacked without hardware, but it leaves the expansion connectors unprotected from mechanical stress.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/7/20150114_164955.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/7/20150114_164955.jpg)

*UART Block Installed*

We have a nice [Hardware Pack](https://www.sparkfun.com/products/13187) available that gives enough hardware to secure three blocks and an Edison.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)

[*Intel Edison Hardware Pack*](https://www.sparkfun.com/products/13187)

### Using the Block in the Middle of a Stack

If you need to use the UART block in the middle of a stack, it may be necessary to file or sand the FTDI connector. The connector is slightly larger than the 3mm clearance allowed by the expansion connectors. It is preferred that the user place this Block a the bottom of a stack.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/7/File-sand_connector.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/7/File-sand_connector.png)

*File or Sand the Connector Here*

### Using the Block with our FTDI Accessories.

The UART Block can be used with our [5V FTDI Basic](https://www.sparkfun.com/products/9716).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/7/20150114_171655.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/7/20150114_171655.jpg)

*FTDI 5V Basic Installed*

### Connecting to the Console

Once you have connected your hardware to your UART -\> Serial device of choice, plug the USB side of the device into the USB port on your computer. If you do not have FTDI drivers currently installed, you\'ll need to download and install them before using your Edison. Visit our [tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) for instructions on how to install the drivers. After you have ensured that the drivers are installed and your device is running, open your favorite terminal program and point it to the USB-serial connection. We have another tutorial to explain [terminal programs and how to use them](https://learn.sparkfun.com/tutorials/terminal-basics).

The standard Baud Rate is 115200bps.

Once a terminal is active you are ready to explore!

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/ConsoleTerminalView.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/2/ConsoleTerminalView.PNG)

### Using the Power Button

The power button on the Edison brings a unique feature commonly not found on single board computers. The power button behaves much like the power buttons on desktop and laptop computers.

- While powered, Holding the power button for \~10 seconds will power down the Edison.
- While un-powered, pressing the power button momentarily will reboot the Edison.
- While powered, pressing the power button momentarily will place the Edison in sleep mode.
- While in sleep mode, pressing the power button momentarily will wake the Edison.