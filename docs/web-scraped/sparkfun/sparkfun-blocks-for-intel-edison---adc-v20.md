# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---adc-v20

## Introduction

**NOTE:** This tutorial applies to **V20** and **V21** of the ADC Block. V21 corrects the voltage noise and adds a locking header footprint for easier assembly with the [Edison SIK](https://www.sparkfun.com/edisonsik).

SparkFun's [ADC Block for the Intel Edison](https://www.sparkfun.com/products/13327) allows you to add four channels of I2C controlled ADC input to your Edison stack. These four channels can be used as single-ended inputs, or in pairs as differential inputs. A ground reference is provided for each channel.

The maximum resolution of the converters is 12 bits, or 11 bits bipolar in differential mode. Step sizes range from 125uV per count to 3mV per count.

[![ADC Block](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/0/13327-01New.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/0/13327-01New.jpg)

*ADC Block*

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Edison adventure include:

- [Programming the Edison](https://learn.sparkfun.com/tutorials/programming-the-intel-edison-beyond-the-arduino-ide) - This tutorial assumes you are **not** using the Arduino IDE, so you\'ll want to familiarize yourself with C++ development on the Edison.
- [Powering Your Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics)
- [Analog-to-digital conversion](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion?_ga=1.102293383.725448541.1330116044)

## Board Overview

[![Labeled image of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/4/0/Edison_ADC_New2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/0/Edison_ADC_New2.png)

*ADC Block Functional Diagram*

- Signal Inputs - Four single inputs are available. The reference voltage for each is produced internal to the ADC under software control; do not exceed 3.3V input to these pins!

- Differential Channel Setting Table - Use two inputs to create a differential pair. Useful for eliminating noise in some sensors or measuring very small signals. This table shows the channel options for the \"getDiffResult(channel)\" function.

- I2C Address Select - Apply solder to **only one** of the four jumpers to select the address. **Do not short two of these at once.** Bad stuff will happen.

- I2C Bus Select - Change **both** of these jumpers to select between routing the I^2^C signals to bus 6 or bus 1. Bus 1 is the default (and preferred) channel, as it has no other system devices on it. Bus 6 is shared with some internal devices, but if you wish to use this block with the Arduino IDE, you\'ll want to change these jumpers so the solder blobs connect the bottom pad with the center pad.

- 3.3V 150mA Supply - This supply provides an on-board reference for the ADC, and can power small sensors (for example, potentiometers or temperature sensors).

## Using the ADC Block

To use the ADC Block simply attach an Intel Edison to the back of the board or add it to your current stack. Blocks can be stacked without hardware but it leaves the expansion connectors unprotected from mechanical stress.

[![Installed block image](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/0/ADCBlockInstalledCrop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/0/ADCBlockInstalledCrop.jpg)

*ADC Block Installed*

We have a nice [Hardware Pack](https://www.sparkfun.com/products/13187) available that gives enough hardware to secure three blocks and an Edison.

[![Edison hardware kit](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)

[*Intel Edison Hardware Pack*](https://www.sparkfun.com/products/13187)

NOTE: The ADC Block does not have console access or a voltage regulator. It is recommended to use a console communication block in conjunction with this block like ones found in the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison#console-communication-blocks).

## C++ Code Examples

We\'re assuming that you\'re using the Eclipse IDE as detailed in our [Beyond Arduino](https://learn.sparkfun.com/tutorials/programming-the-intel-edison-beyond-the-arduino-ide) tutorial. If you aren\'t, you\'ll need to go to that tutorial to get up to speed.

#### Getting Started

Follow the instructions in the [programming tutorial](https://learn.sparkfun.com/tutorials/programming-the-intel-edison-beyond-the-arduino-ide#hello-world) to create a new project named \"SparkFun_ADC_Edison_Block_Example\". Once you\'ve created the project, open the project files on disk (hint: you can find the path to the project by choosing \"Properites\" from the project menu) and copy the three source files found in the [Edison ADC Block CPP library GitHub repository](https://github.com/sparkfun/SparkFun_ADC_Block_for_Edison_CPP_Library) into the \"src\" directory.

[Download a zip file of the repository](https://github.com/sparkfun/SparkFun_ADC_Block_for_Edison_CPP_Library/archive/master.zip)

#### Hardware Connection

For this example, we\'ve just got two 5k potentiometers connected between 3.3V and GND, with the wipers connected to channels 0 and 1.

V20 of the board adds a 3.3V reference supply (capable of sourcing up to 150mA, so it can power small sensors directly!).

[![Example circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/4/0/edison_adc_v20_example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/0/edison_adc_v20_example.png)

Of course, you can connect any other analog voltage signal in place of the potentiometers; we\'re using them because they\'re convenient to demonstrate the concepts.

#### Code

Everything you need to know is in the comments.

    language:cplusplus
    /****************************************************************
    Example file for SparkFun ADC Edison Block Support

    1 Jun 2015- Mike Hord, SparkFun Electronics
    Code developed in Intel's Eclipse IOT-DK

    This code requires the Intel mraa library to function; for more
    information see https://github.com/intel-iot-devkit/mraa

    This code is beerware; if you use it, please buy me (or any other
    SparkFun employee) a cold beverage next time you run into one of
    us at the local.
    ****************************************************************/

    #include "mraa.hpp"

    #include <iostream>
    #include <unistd.h>
    #include "SparkFunADS1015.h"

    using namespace std;

    // Declare a variable for our i2c object. You can create an
    //  arbitrary number of these, and pass them to however many
    //  slave devices you wish.
    mraa::I2c* adc_i2c;

    int main()