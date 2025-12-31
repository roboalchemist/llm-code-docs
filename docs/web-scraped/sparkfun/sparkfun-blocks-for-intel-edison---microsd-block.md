# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---microsd-block

## Introduction

The [microSd Block](https://www.sparkfun.com/products/13041) is a great way to store larger files and data for or from your project. The microSD block allows the Edison to mount a [microSD card](https://www.sparkfun.com/products/11609) as an internal drive. Make a data logger or mobile file server with your Edison!

[![microSD Block](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/9/MicroSdBlock-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/9/MicroSdBlock-01.jpg)

*microSD Block*

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Edison adventure include:

- [Powering Your Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics)

## Board Overview

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/9/microSDAnnotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/9/microSDAnnotated.png)

*MicroSD Block Functional Diagram*

- Micro SD Socket - Insert Micro SD card here. Block does appropriate card detection and level shifting.

- Expansion Header - The 70-pin Expansion header breaks out the functionality of the Intel Edison. This header also passes signals and power throughout the stack. These function much like an [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields).

## Using the microSD Block

To use the microSD Block, attach an Intel Edison to the back of the board, or add it to your current stack. Blocks can be stacked without hardware, but it leaves the expansion connectors unprotected from mechanical stress.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/9/20150109_121835.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/9/20150109_121835.jpg)

*microSD Block Installed*

We have a nice [Hardware Pack](https://www.sparkfun.com/products/13187) available that gives enough hardware to secure three blocks and an Edison.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)

[*Intel Edison Hardware Pack*](https://www.sparkfun.com/products/13187)

NOTE: The microSD Breakout Block does not have console access or a power supply. It is recommended to use a console communication block in conjunction with this block like ones found in the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison#console-communication-blocks).

The simplest way to use the microSD Block is to boot your Edison stack with the card already installed. While booting, the Edison will automatically find and mount the SD card to the following directory. To see what\'s inside, type the following.

    cd /media/sdcard/

To safely unmount the SD card for removal, enter the following command.

    umount /media/sdcard

To insert a card after boot, simply insert the card. The Edison should automatically detect and mount the card.