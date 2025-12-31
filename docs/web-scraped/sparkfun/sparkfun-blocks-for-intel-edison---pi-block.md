# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---pi-block

## Introduction

The [Pi Block](https://www.sparkfun.com/products/13044) breaks out and level shifts several GPIO pins from the Intel Edison. It presents them in the same configuration as a Raspberry Pi Model B.

[![Intel Edison Pi Block](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/2/13044-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/2/13044-01.jpg)

*Pi Block*

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Edison adventure include:

- [Edison Getting Started Guide](/tutorials/edison-getting-started-guide)
- [Logic Levels](/tutorials/62)

## Board Overview

[![Annotated Pi Block functions](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/2/Pi_Block_annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/2/Pi_Block_annotated.png)

*Pi Block Functional Diagram*

- USB Power - used to provide 5V to Pi Block and power the Edison. Note that the data lines are not connected to the Edison.

- Power Button - The power switch is connected to the \"PWRBTN\" line on the Edison. This give the user the ability to place an Edison in sleep or power down the module completely. This does not affect power to other Blocks in the stack.

- Power LED - The power LED illuminates when power is present on VSYS. This can come from the onboard USB Power or any other powered Block in the stack.

- Expansion Header - The 70-pin Expansion header breaks out the functionality of the Intel Edison. This header also passes signals and power throughout the stack. These function much like an [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields).

- LED Jumper - If power consumption is an issue, cut this jumper to disable the power LED.

- VSYS Jumper - By default, a USB cable must be attached to the USB Power port to provide power to the 5V pins on the RPi B Header. You can power the Edison and Pi Block from another Block (e.g. [Base Block](https://www.sparkfun.com/products/13045)), but there will not be 5V on the pins labeled \"5V\". By closing this jumper, you can power the Edison and Pi Block from another Block, and \~4.2V (VSYS) will appear on the pins labeled \"5V\".

- RPi B Header - Same configuration as the old [Raspberry Pi Model B pinout](http://elinux.org/RPi_Low-level_peripherals#Model_A_and_B_.28Original.29).

## Using the Pi Block

To use the Pi Block, attach an Intel® Edison to the back of the board, or add it to your current stack. Blocks can be stacked without hardware, but it leaves the expansion connectors unprotected from mechanical stress.

[![Edison installed on Pi Block](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/2/Pi_Block_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/2/Pi_Block_Tutorial-01.jpg)

*Edison installed on Pi Block*

We have a nice [Hardware Pack](https://www.sparkfun.com/products/13187) available that gives enough hardware to secure three blocks and an Edison.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)

[*Intel Edison Hardware Pack*](https://www.sparkfun.com/products/13187)

**NOTE:** It is recommended to use a console communication block in conjunction with this block like ones found in the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison#console-communication-blocks). Once you have the Edison configured, you can remove the console communication block, power the Edison from the Pi Block, and [SSH into the Edison](https://learn.sparkfun.com/tutorials/edison-getting-started-guide#ssh-ing-into-the-edison).

You can put headers on the Edison side, which gives you easy access to the pin labels. Note that this pinout is mirrored from the Raspberry Pi Model B pinout.

[![Headers on top of Edison Pi Block](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/2/Pi_Block_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/2/Pi_Block_Tutorial-02.jpg)

*Headers on Edison side*

Alternatively, you can populate the back side of the Pi Block with headers. This method gives the same pinout as a Raspberry Pi Model B. You could, in theory, swap the Edison in for your Raspberry Pi on an existing project, or use Raspberry Pi accessories (e.g. [Pi Wedge](https://www.sparkfun.com/products/13091)).

[![Headers on bottom of Edison Pi Block](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/2/Pi_Block_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/2/Pi_Block_Tutorial-03.jpg)

*Or put headers on the back side of Pi Block*

### Using the Pi Block as an output device

If you want to use the Pi Block to control high power LEDs or relays, an external transistor or MOSFET will be required. It is possible to illuminate a small LED directly from the level shifter. It may not be as bright since the current output of the TXB0108 level converter is very low (\~5ma).

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/GPIOLoadDiagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/GPIOLoadDiagram.png)

*Connection Diagram for Load (LED, Motor, or Relay)*

In the terminal, we will demonstrate how to activate and use a GPIO pin as an output.

First navigate to the GPIO directory on the Edison.

    cd /sys/class/gpio

Select the GPIO pin to enable. In this case, we used GPIO 14, which is labeled \"GP14\" on the Pi Block.

    echo 14 > export

Navigate to the newly created GPIO directory.

    cd gpio14

If you type \"ls\", you should see a bunch of variables.

    active_low  direction   power       uevent
    device      edge        subsystem   value

Let\'s set the \"direction\" of the port to output

    echo out > direction

To confirm this, we will \"cat\" the value

    cat direction

You should see the \"out\" in the command line. Now the device is configured as an output. \"value\" is where the status of the pin is set, 1 for high, 0 for low.

    echo 1 > value

Testing with a multi-meter, small led, or oscilloscope, you should see a \"high\" status (3.3V) present on gpio14.

### Using the Pi Block as an input device

If you want the Pi Block to read switches, buttons, or other logic level inputs, you must pay attention to pull-up and pull-down resistors. The level converter on board is very weak. Here are two scenarios explained:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/ActiveHighCircuit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/ActiveHighCircuit.png)

*Connection Diagram for Active High Push Button*

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/ActiveLowCircuit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/ActiveLowCircuit.png)

*Connection Diagram for Active Low Push Button*

In the terminal, we will demonstrate how to activate and use a GPIO pin as an input configured as an active high.

First, navigate to the GPIO directory on the Edison.

    cd /sys/class/gpio

Select the GPIO pin to enable. In this case let us use GPIO 14.

    echo 14 > export

Navigate to the newly created GPIO directory.

    cd gpio14

If you type \"ls\", you should see a bunch of variables.

    active_low  direction   power       uevent
    device      edge        subsystem   value

Let\'s set the \"direction\" of the port to output.

    echo in > direction

To confirm this, we will \"cat\" the value.

    cat direction

You should see the \"in\" in the command line. Now the device is configured as an input. \"value\" is where the status of the pin is set, 1 for high, 0 for low.

    cat value

With a button pressed, you should see a 1. When the button is not pressed you should see a 0. Using the up arrow, you can recall previously run commands.

## C++ Examples

We\'re assuming that you\'re using the Eclipse IDE as detailed in our [Beyond Arduino](https://learn.sparkfun.com/tutorials/programming-the-intel-edison-beyond-the-arduino-ide) tutorial. If you aren\'t, you\'ll need to go to that tutorial to get up to speed.

#### Hardware Connection

Hardware support for this library is simple; one [basic red LED](https://www.sparkfun.com/products/9590) and one [momentary pushbutton](https://www.sparkfun.com/products/97). We\'re using a [2N3904 NPN transistor](https://www.sparkfun.com/products/521) to drive the LED, however, as the drive strength of the outputs on the Pi Block is quite weak. As you can see in the diagram, you\'ll also need a couple of [1kΩ resistors](https://www.sparkfun.com/products/8980) and a single [330Ω resistor](https://www.sparkfun.com/products/8377).

[![Intel Edison Pi Block connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/2/Pi_Block_Hookup_bba.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/2/Pi_Block_Hookup_bba.png)

While we\'ve used GPIO45 and GPIO46 in this example, this code can be used with any of the pins on the Pi breakout. The GPIO to MRAA pin map can be found in the [Resources and Going Further section](https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---pi-block#resources-and-going-further).

#### Code

Follow the instructions in the [programming tutorial](https://learn.sparkfun.com/tutorials/programming-the-intel-edison-beyond-the-arduino-ide#hello-world) to create a new project named \"SparkFun_Pi_Block_Example\". Once you\'ve created the project, open the \"SparkFun_Pi_Block_Example.cpp\" file and replace all the existing code with the code block below.

    language:c
      /****************************************************************
      Example file for SparkFun Pi Block Support

      14 Jul 2015- Mike Hord, SparkFun Electronics
      Code developed in Intel's Eclipse IOT-DK

      Modified on July 30, 2015 by Shawn Hymel, SparkFun Electronics

      This code requires the Intel mraa library to function; for more
      information see https://github.com/intel-iot-devkit/mraa

      This code is beerware; if you use it, please buy me (or any other
      SparkFun employee) a cold beverage next time you run into one of
      us at the local.
      ****************************************************************/

    #include "mraa.hpp"

    #include <iostream>
    #include <unistd.h>

    using namespace mraa;
    using namespace std;

    int main()
    
      }

      return MRAA_SUCCESS;
    }

#### Additional Examples

Because this block is just a GPIO access device, the existing MRAA GPIO examples can be used with it.

[![Example projects in the IDE](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/4/examples.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/4/examples.png)

When you create a new project in the Eclipse IDE, it will offer you the option of several starter projects. Some of them, noted above, are good examples of using the MRAA GPIO functions. They\'re more complex than what we\'ve provided here, however.

For full documentation of the C++ API for GPIO pins, please visit [the official MRAA documentation](http://iotdk.intel.com/docs/master/mraa/).