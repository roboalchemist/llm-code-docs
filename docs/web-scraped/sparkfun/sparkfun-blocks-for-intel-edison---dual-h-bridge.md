# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---dual-h-bridge

## Introduction

SparkFun\'s [H-Bridge Block for Edison](https://www.sparkfun.com/products/13043) adds a two-channel low-voltage low-current h-bridge (the [Toshiba TB6612](https://www.sparkfun.com/products/9457)) to your stack. The block can be configured to draw power either from the VSYS supply of the stack or from an external supply connected to the header on the block.

[![H-bridge hero shot](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/2/13043-01Cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/2/13043-01Cropped.jpg)

*Dual H-Bridge Block*

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Edison adventure include:

- [Programming the Edison](https://learn.sparkfun.com/tutorials/programming-the-intel-edison-beyond-the-arduino-ide) - This tutorial assumes you are **not** using the Arduino IDE, so you\'ll want to familiarize yourself with C++ development on the Edison.
- [Powering Your Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics)
- [PWM](https://learn.sparkfun.com/tutorials/pulse-width-modulation?_ga=1.68681495.725448541.1330116044)

## Board Overview

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/2/H-bridgeAnnotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/2/H-bridgeAnnotated.png)

*Dual H-Bridge Block Functional Diagram*

- Motor Outputs - Two DC motor outputs. Motor A and B

- Motor Power Input - External power input for DC motors. Limit to 15v DC.

- VSYS -\> VIN - Close this jumper to power Motors off VSYS. Use caution to not overdraw power supply capabilities.

- Expansion Header - The 70-pin Expansion header breaks out the functionality of the Intel Edison. This header also passes signals and power throughout the stack. These function much like an [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields).

## Using the Dual H-Bridge Block

To use the Dual H-Bridge Block simply attach an Intel Edison to the back of the board or add it to your current stack. Blocks can be stacked without hardware but it leaves the expansion connectors unprotected from mechanical stress.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/2/13043-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/2/13043-04.jpg)

*Dual H-Bridge Block Installed*

We have a nice [Hardware Pack](https://www.sparkfun.com/products/13187) available that gives enough hardware to secure three blocks and an Edison.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)

[*Intel Edison Hardware Pack*](https://www.sparkfun.com/products/13187)

NOTE: The Dual H-Bridge Block does not have console access or a voltage regulator. It is recommended to use a console communication block in conjunction with this block like ones found in the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison#console-communication-blocks).

## C++ Code Example

We\'re assuming that you\'re using the Eclipse IDE as detailed in our [Beyond Arduino](https://learn.sparkfun.com/tutorials/programming-the-intel-edison-beyond-the-arduino-ide) tutorial. If you aren\'t, you\'ll need to go to that tutorial to get up to speed.

### Getting Started

Follow the instructions in the [programming tutorial](https://learn.sparkfun.com/tutorials/programming-the-intel-edison-beyond-the-arduino-ide#hello-world) to create a new project named \"SparkFun_H-Bridge_Edison_Block_Example\". Once you\'ve created the project, open the project files on disk (hint: you can find the path to the project by choosing \"Properites\" from the project menu), and copy the three source files found in the [Edison H-Bridge Block CPP library GitHub repository](https://github.com/sparkfun/SparkFun_H-Bridge_Block_for_Edison_CPP_Library) into the \"src\" directory.

[Download a zip file of the repository](https://github.com/sparkfun/SparkFun_H-Bridge_Block_for_Edison_CPP_Library/archive/master.zip)

### Hardware Connection

For this example, we have two [small DC motors with gearboxes](https://www.sparkfun.com/products/12143) attached to the outputs. The image below shows how to build the circuit. It\'s up to you whether you want to drive the motors with an external supply. I\'ve shown one here, but I\'ve had perfectly good luck closing the supply jumper and pulling the current for these motors directly from the stack\'s VSYS rail, even when powering it over USB.

[![Hookup diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/2/h-bridge.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/2/h-bridge.png)

### Code

Everything you need to know is in the comments.

    language:c
    #include <unistd.h>

    #include "mraa.h"
    #include "SparkFun_TB6612_Edison.h"
    #include <iostream>
    #include <iomanip>
    using namespace std;

    int main()