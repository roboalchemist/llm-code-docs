# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---gpio-block

## Introduction and Overview

The [General Purpose Input/Output (GPIO) Block](https://www.sparkfun.com/products/13038) breaks out the simple GPIO functionality of the Intel Edison. Using selectable level shifters, it is possible to use VSYS or 3.3v logic levels with this Block.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/gpio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/gpio.jpg)

*GPIO Block*

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Edison adventure include:

- [Edison Getting Started Guide](/tutorials/edison-getting-started-guide)
- [Logic Levels](/learn_tutorials/62)

## Board Overview

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/6/GPIOBlockAnnotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/GPIOBlockAnnotated.png)

*GPIO Block Functional Diagram*

- Level Select - Jumper selects GPIO reference voltage, Can be set to 3.3v or VSYS
- Power Pins - Raw access to power pins on Edison
  - GND - Ground pin for all blocks and Edison
  - VSYS - Raw input for Edison and all Blocks.
  - Normal output (with power blocks) 4.0V-4.1V.
  - You can power an Edison through this pin. Acceptable voltages 3.3V-4.5V
  - 1.8v - 1.8v supplied by Edison internal power supply
  - 3.3v - 3.3v supplied by Edison internal power supply
- General GPIO - Genaral use GPIO pins.
- GPIO/UART1 - GPIO pins that can also be used as a second UART. (Useful for GPS receivers and other serial devices)
- GPIO/PWM - GPIO pins capable of generating PWM waveforms. (Useful for LED dimming and Motor control)
- Expansion Header - The 70-pin Expansion header breaks out the functionality of the Intel Edison. This header also passes signals and power throughout the stack. These function much like an [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields).

## Using the GPIO Block

To use the GPIO Block, attach an Intel® Edison to the back of the board, or add it to your current stack. Blocks can be stacked without hardware, but it leaves the expansion connectors unprotected from mechanical stress.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/6/Edison_Block_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/Edison_Block_Tutorial-05.jpg)

*GPIO Block Installed*

We have a nice [Hardware Pack](https://www.sparkfun.com/products/13187) available that gives enough hardware to secure three blocks and an Edison.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)

[*Intel Edison Hardware Pack*](https://www.sparkfun.com/products/13187)

NOTE: The GPIO Block does not have console access or a voltage regulator. It is recommended to use a console communication block in conjunction with this block like ones found in the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison#console-communication-blocks).

### Using the GPIO Block as an output device

If you want to use the GPIO Block to control high power LED\'s or Relays, an external transistor or MOSFET will be required. It is possible to illuminate a small LED directly from the level shifter. It may not be as bright since the current output of the TXB0108 level converter is very low (\~5ma).

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/GPIOLoadDiagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/GPIOLoadDiagram.png)

*Connection Diagram for Load (LED, Motor, or Relay)*

In the terminal we will demonstrate how to activate and use a GPIO pin as an output.

First navigate to the GPIO directory on the Edison.

    cd /sys/class/gpio

Select the GPIO pin to enable. In this case, we used GPIO 14.

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

### Using the GPIO Block as an input device.

If you want the GPIO Block to read switches, buttons, or other logic level inputs, you must pay attention to pull-up and pull-down resistors. The level converter on board is very weak. Here are two scenarios explained:

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