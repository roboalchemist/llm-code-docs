# Source: https://learn.sparkfun.com/tutorials/hookup-guide-for-the-qwiic-motor-driver

## Introduction

The [Qwiic Motor Driver](https://www.sparkfun.com/products/15451) takes all the great features of the Serial Controlled Motor Driver and mini-sizes them, adding [Qwiic](https://www.sparkfun.com/qwiic) ports for plug and play functionality. Boasting the same PSOC and 2-channel motor ports, the QWIIC Motor Driver is designed to communicate over I^2^C, but UART is also available.

[![SparkFun Qwiic Motor Driver](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/2/9/15451-SparkFun_Qwiic_Motor_Driver-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-motor-driver.html)

### [SparkFun Qwiic Motor Driver](https://www.sparkfun.com/sparkfun-qwiic-motor-driver.html) 

[ ROB-15451 ]

The SparkFun Qwiic Motor Driver takes all the features of the Serial Controlled Motor Driver and miniaturizes them, adding Qw...

[ [\$23.78] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend you read over these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one)

### Motors and Selecting the Right One 

Learn all about different kinds of motors and how they operate.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide)

### Bi-Directional Logic Level Converter Hookup Guide 

An overview of the Bi-Directional Logic Level Converter, and some example circuits to show how it works.

[](https://learn.sparkfun.com/tutorials/serial-controlled-motor-driver-hookup-guide)

### Serial Controlled Motor Driver Hookup Guide 

Hookup guide for the Serial Controlled Motor Driver

## Hardware Overview

Let\'s look at some of the various features of the hardware.

**Features:**

- 1.5 A peak drive per channel, 1.2 A steady state
- Operates from **3 to 11 volts** with 12v absolute max
- **3.3V** default VCC and logic
- 127 levels of DC drive strength.
- Controllable by I^2^C or TTL UART signals
- Direction inversion on a per motor basis
- Global Drive enable
- Exposed small heat sink shape
- Several I^2^C addresses, default UART bauds available

[![Front of Qwiic Motor Driver](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/15451-SparkFun_Qwiic_Motor_Driver-top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/15451-SparkFun_Qwiic_Motor_Driver-top.jpg)

### Power

There are two separate power circuits on this board . Power for the motors is supplied through the **VIN Connectors** - you can provide anywhere from **3.3V to 11V** to the \"MAX 11V\" and \"GND\" connections. Power for the PSOC and logic circuits is provided by the *3.3V* inputs on the Qwiic connectors. Both are needed for proper functioning.

[![VIn inputs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_vin.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_vin.jpg)

*Motor Power Ports: Ground (Left) - VIN(Right)*

### Qwiic Connectors

There are two Qwiic connectors on the board such that you can provide power or daisy-chain the boards should you choose to do so. If you\'re unfamiliar with our Qwiic system, head on over to our [Qwiic page](https://www.sparkfun.com/qwiic) to see the advantages!

[![Qwiic connectors on either side of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_qwiicPorts.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_qwiicPorts.jpg)

### Motor Ports

The screw pin terminals at the top of the board allow for two motor connections. They are labeled on the backside of the board.

[![Screw terminals for motor inputs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_screw_terminals_fandb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_screw_terminals_fandb.jpg)

*From left to right on the front: B2-B1-A2-A1*

+------------+------+-----------+----------------------------------------+-----------------------------+
|            |      |           |                                        | Function / Connection       |
+============+======+===========+========================================+=========+=========+=========+
| Group      | Name | Direction | Description                            | UART    | I^2^C   |         |
+------------+------+-----------+----------------------------------------+---------+---------+---------+
| Motor Port | A1   | O         | Winding of first addressable location  | Motor A winding             |
|            +------+-----------+----------------------------------------+-----------------------------+
|            | A2   | O         | Winding of first addressable location  | Motor A winding             |
|            +------+-----------+----------------------------------------+-----------------------------+
|            | B1   | O         | Winding of second addressable location | Motor B winding             |
|            +------+-----------+----------------------------------------+-----------------------------+
|            | B2   | O         | Winding of second addressable location | Motor B winding             |
+------------+------+-----------+----------------------------------------+-----------------------------+

### Jumpers

#### Jumper Usage Table

There are 2 sets of jumpers to configure on this board. There are pull-up enables for I^2^C and 4 **config** bits that select operational mode.

  Name              Description                     Usage
  ----------------- ------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  I^2^C Jumpers     I^2^C pull-up enable            Opening these disables theI^2^C pull-up resistors used for I^2^C communication. If multiple I^2^C devices are being used, these pull-ups should be disabled on all but **one** device. If UART is being used, the pull-up resistors should be disabled.
  Address Jumpers   Serial and function selection   The config bits are 4 bits that form a configuration nybble. A closed jumper is a \'1\' and an open jumper is a \'0\'. See config table for more information.

#### I^2^C Pull-Up Jumpers

[![I2C Jumpers on the lower right side of the back of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_i2c_pullup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_i2c_pullup.jpg)

#### Address Bits

The configuration is set by encoding a number into the 4 config bits on the bottom of the board. Close a jumper to indicate a 1, or leave it open to indicate a 0.

[![Address jumpers on the back of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_address_jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_address_jumpers.jpg)

Use this table to see what the user port, address, and expansion port will become in each configuration:

  Pattern    Mode             User Port   User Address   Expansion Port
  ---------- ---------------- ----------- -------------- ----------------
  0000       UART at 9600     UART        N/A            Master
  0011       I^2^C            I^2^C       0x58           Master
  0100       I^2^C            I^2^C       0x59           Master
  0101       I^2^C            I^2^C       0x5A           Master
  0110       I^2^C            I^2^C       0x5B           Master
  0111       I^2^C            I^2^C       0x5C           Master
  **1000**   **I^2^C**        **I^2^C**   **0x5D**       **Master**
  1001       I^2^C            I^2^C       0x5E           Master
  1010       I^2^C            I^2^C       0x5F           Master
  1011       I^2^C            I^2^C       0x60           Master
  1100       I^2^C            I^2^C       0x61           Master
  1101       UART at 57600    UART        N/A            Master
  1110       UART at 115200   UART        N/A            Master
  1111       N/A              Reserved    N/A            N/A

*Bold text is the default setting for the Qwiic Motor Driver*

### Thermal Conduction Area

The Qwiic Motor Driver is designed to operate small robot drive motors without a heatsink; we were able to run up to about 1.1A continuous current without going above 100°C. If you find that you need a heatsink, you can use our [Theragrip Thermal Tape](https://www.sparkfun.com/products/9771) to attach three [Small Heat Sinks](https://www.sparkfun.com/products/11510) across the thermal conduction area on the back of the board.

[![Thermal conduction area on the back of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_thermal.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_thermal.jpg)

If you need more information on how to determine whether or not you need a heat sink, kick on over to the [Serial Controlled Motor Driver Hookup Guide](https://learn.sparkfun.com/tutorials/serial-controlled-motor-driver-hookup-guide#hardware-overview) and scroll down to

*Typical Application Motors and Heat Sinking*.

[![Small heatsinks on the back of the Qwiic Motor Driver](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_heatsinks.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_heatsinks.jpg)

*Small Heatsinks on the back of the Qwiic Motor Driver*

### Board Dimensions

All measurements are in inches. The Qwiic Motor Driver PCB measures 1x1 inch, with slight overhangs for the power and motor screw terminals.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/Qwiic_Motor_driver_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/Qwiic_Motor_driver_Dimensions.png)

## Software Setup

**Note:** This code/library has been written and tested on Arduino IDE version 1.8.5. Otherwise, make sure you are using the latest stable version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing Arduino

If you haven\'t used the Arduino IDE before, head on over to our Installing the Arduino IDE tutorial to get set up:

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### Getting the Arduino Library

The Qwiic Motor Driver uses the same Arduino Library as the Serial Controlled Motor Driver (hereafter referred to as SCMD). To get the Arduino library, either download and install it from [Github](https://github.com/sparkfun/SparkFun_Serial_Controlled_Motor_Driver_Arduino_Library) or use the Arduino Library Manager.

**Download the Github repository**

Visit the [GitHub repository](https://github.com/sparkfun/SparkFun_Serial_Controlled_Motor_Driver_Arduino_Library) to download the most recent version of the library, or click the link below:

[Download the Arduino Library](https://github.com/sparkfun/SparkFun_Serial_Controlled_Motor_Driver_Arduino_Library/archive/master.zip)

**Use the library manager or install in the Arduino IDE**

In the Library Manager, search for

*Serial Controlled Motor Driver*. For help installing the library, check out our [How To Install An Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library).

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

January 11, 2013

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

## Experiment 1: Testing the Motors

Let\'s start by hooking up some motors and making sure they\'re running. Since the Qwiic Motor Driver uses the same PSOC as the Serial Controlled Motor Driver, the same examples will work with minor modifications.

⚡ **Note:** In lieu of using the external LiPo battery, it is also possible to use the **5V** and GND pins from the RedBoard Qwiic.

### Hardware Hookup

[![Hardware Hookup Fritzing image Experiment 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/Experiment1HookupFritzing-NoLine.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/Experiment1HookupFritzing-NoLine.jpg)

*Click the image for a closer look*

### Testing the Motors

The following test is essentially the *TwoMotorRobot.ino* example from the SCMD library, but with a few minor changes to account for the defaults of the Qwiic Motor Driver.

Copy and paste the following code into your Arduino browser and upload.

    language:c
    //This example drives a robot in left and right arcs, driving in an overall wiggly course.
    //  It demonstrates the variable control abilities. When used with a RedBot chassis,
    //  each turn is about 90 degrees per drive.
    //
    //  Pin 8 can be grounded to disable motor movement, for debugging.

    #include <Arduino.h>
    #include <stdint.h>
    #include "SCMD.h"
    #include "SCMD_config.h" //Contains #defines for common SCMD register names and values
    #include "Wire.h"

    SCMD myMotorDriver; //This creates the main object of one motor driver and connected peripherals.

    void setup()
    
      Serial.println( "ID matches 0xA9" );

      //  Check to make sure the driver is done looking for peripherals before beginning
      Serial.print("Waiting for enumeration...");
      while ( myMotorDriver.ready() == false );
      Serial.println("Done.");
      Serial.println();

      //*****Set application settings and enable driver*****//

      //Uncomment code for motor 0 inversion
      //while( myMotorDriver.busy() );
      //myMotorDriver.inversionMode(0, 1); //invert motor 0

      //Uncomment code for motor 1 inversion
      while ( myMotorDriver.busy() ); //Waits until the SCMD is available.
      myMotorDriver.inversionMode(1, 1); //invert motor 1

      while ( myMotorDriver.busy() );
      myMotorDriver.enable(); //Enables the output driver hardware

    }

    #define LEFT_MOTOR 0
    #define RIGHT_MOTOR 1
    void loop()
    
      for (int i = 255; i >= 0; i--)
      
      //Smoothly move the other motor up to speed and back
      for (int i = 0; i < 256; i++)
      
      for (int i = 255; i >= 0; i--)
      
    }

### What You Should See

The code goes through and establishes communication with the motor driver and then runs each motor in arcs, resulting in a \"wiggly pattern\".

Things to note:

- `Serial.begin` is periodically run until the returned ID word is valid.
- Setup waits for `isReady()` to become true before going on to the drive section
- One motor is inverted by command at setup. Do it here so you don\'t have to mess with it later.
- `enable()` is called to connect the drivers to the PWM generators.
- LEFT_MOTOR and RIGHT_MOTOR are defined to ease use of the `setDrive( ... )` function.

See the [Arduino Library Reference](https://learn.sparkfun.com/tutorials/serial-controlled-motor-driver-hookup-guide#arduino-library-reference) section of the Serial Controlled Motor Driver Hookup Guide for more information on the functions defined in the Arduino library.

## Experiment 2: Interactive Commands with UART

This example demonstrates the basic commands, plus some direct register access possible with only a UART available. This type of program could be easily run from a script from a more classic PC where I^2^C isn\'t available.

### Interactive UART

**Requirements**

- Computer serial terminal set to 9600 baud.
- Terminal set to send CR and LF (Carriage return and line feed).
- Config jumpers set to \'0000\', or all open.
- I^2^C PU jumper fully open
- [FTDI Basic](https://www.sparkfun.com/products/9873) or [Serial Basic](https://www.sparkfun.com/products/14050) - either will work but ensure you have the **3.3V** version

[![Address Jumper 3 and I2C Pullup Jumpers are cut](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_UART_cut_jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/15451-qwiic_motor_driver_UART_cut_jumpers.jpg)

*Make sure the Address Jumper 3 and I^2^C Pullup Jumpers are cut as you see here.*

Connect the FTDI to the Qwiic Motor Driver as you see in the Fritzing diagram below. Attach two motors to the driver, one between A1 and A2, and the other between B1 and B2.

[![Example 2 Fritzing image](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/3/4/Experiment2HookupFritzing-NoLine.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/4/Experiment2HookupFritzing-NoLine.jpg)

*Click the image for a closer look*

**Example Commands**

When you\'re ready, make sure you have the correct COM port selected in your Arduino IDE, open a Serial Monitor, and send the following commands:

\"R01\"

This will read the ID register and return 0xA9

\"M0F50\"

This will tell motor 0 to drive at half speed, forward \-- But nothing will happen yet!

\"E\"

This will enable all drivers. Motor 0 should begin spinning at half speed.

\"M1R100\"

This will tell motor 1 to drive at full speed in reverse. Now both should be spinning opposite directions.

\"D\"

D will disable both motors, which will stop spinning.

See the section [UART Commands](https://learn.sparkfun.com/tutorials/serial-controlled-motor-driver-hookup-guide#uart-commands) in the Serial Controlled Motor Driver Hookup Guide for a full command listing.

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.