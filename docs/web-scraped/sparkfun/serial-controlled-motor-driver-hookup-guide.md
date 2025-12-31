# Source: https://learn.sparkfun.com/tutorials/serial-controlled-motor-driver-hookup-guide

## Introduction

The [Serial Controlled Motor Driver](https://www.sparkfun.com/products/13911) (abbreviated SCMD for the rest of this guide) is a DC motor driver that\'s been designed to drive small DC motors with ease. It can be commanded by UART, I2C, or SPI communication, and it can drive a constant 1.2A load per motor (peak 1.5A) at 11V. Need more than two motors? Chain multiple SCMDs together and command them through the same serial interface. Need more current? Each board\'s output can be bridged to allow double current.

[![SparkFun Serial Controlled Motor Driver](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/5/7/6/13911-01.jpg)](https://www.sparkfun.com/sparkfun-serial-controlled-motor-driver.html)

### [SparkFun Serial Controlled Motor Driver](https://www.sparkfun.com/sparkfun-serial-controlled-motor-driver.html) 

[ ROB-13911 ]

The SparkFun Serial Controlled Motor Driver (SCMD) is a DC motor driver that's been designed to drive small DC motors with ...

**Retired**

This driver board was designed to be affordable, compact and have more features than previous versions of serial-controlled motor drivers. Its main advantage is the variability of drive levels making fine control adjustments a possibility.

**Features:**

- 1.5 A peak drive per channel, 1.2 A steady state
- Operates from 3 to 11 volts with 12v absolute max
- 3.3v default VCC and logic
- Max VCC in of 5.5v
- 127 levels of DC drive strength.
- Controllable by I2C, SPI, or TTL UART signals
- Direction inversion on a per motor basis
- Global Drive enable
- Expansion port utilizing I2C, allows 16 additional drivers
- Exposed TO-220 heat sink shape
- Several I2C addresses, default UART bauds available
- Bridgeable outputs
- Optional fail-safe and diagnostics available.
- Configurable expansion bus bit rate to 50, 100, or 400 kHz.
- Configurable expansion bus update rate from 1ms to 255ms, or by command only

### Covered In This Tutorial

This tutorial covers basic usage of the motor driver. It shows how to connect it to I2C, SPI, or UART at 3.3V levels, and how to attach more drivers to the controller and control them all independently. It also shows some common motors that can be used without heatsinks.

### Required Materials

This tutorial explains how to use the Serial Controlled Motor Driver Breakout Board with an Arduino or direct serial. To follow along, you\'ll need the following materials:

- [Redboard 328p board](https://www.sparkfun.com/products/12757) or [3.3V FTDI Basic](https://www.sparkfun.com/products/9873) \-- to communicate with the SCMD.
- Some DC motors, such as:
  - [Redbot style gearmotors](https://www.sparkfun.com/products/13302)
  - [Micro Gearmotor - 460RPM](https://www.sparkfun.com/products/12429)
  - [Standard Gearmotor - 303RPM](https://www.sparkfun.com/products/12147)

[![Hobby Motor - Gear](https://cdn.sparkfun.com/r/140-140/assets/parts/7/8/6/0/11696-01.jpg)](https://www.sparkfun.com/hobby-motor-gear.html)

### [Hobby Motor - Gear](https://www.sparkfun.com/hobby-motor-gear.html) 

[ ROB-11696 ]

This is our new Hobby Motor now with a 6mm, 10 tooth, gear to make your basic projects a little simpler to manage. It works w...

[ [\$2.75] ]

[![Hobby Gearmotor - 140 RPM (Pair)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/6/1/13302-01b.jpg)](https://www.sparkfun.com/hobby-gearmotor-140-rpm-pair.html)

### [Hobby Gearmotor - 140 RPM (Pair)](https://www.sparkfun.com/hobby-gearmotor-140-rpm-pair.html) 

[ ROB-13302 ]

These are a pair of hobby gearmotors from DAGU. These gearmotors are the same ones recommended for use in the Shadow Chassis ...

[ [\$7.50] ]

[![Micro Gearmotor - 460 RPM (6-12V)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/0/6/6/see_00_gearmotor-01.jpg)](https://www.sparkfun.com/micro-gearmotor-460-rpm-6-12v.html)

### [Micro Gearmotor - 460 RPM (6-12V)](https://www.sparkfun.com/micro-gearmotor-460-rpm-6-12v.html) 

[ ROB-12429 ]

These micro gearmotors are incredibly tough and feature full metal gears. They have a gear ratio of 50:1 and operate up to 12...

[ [\$23.50] ]

[![Standard Gearmotor - 303 RPM (3-12V)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/7/8/4/See_00_motor-02.jpg)](https://www.sparkfun.com/products/12147)

### [Standard Gearmotor - 303 RPM (3-12V)](https://www.sparkfun.com/products/12147) 

[ ROB-12147 ]

These standard gearmotors are incredibly tough and feature full metal gears to help you drive wheels, gears, or almost anythi...

**Retired**

Check out our entire offering of DC motors:

[DC Gearmotor Catalog](https://www.sparkfun.com/categories/247)

\

**Warning!** The SCMD is a 3.3V logic device! If you need to interface to 5V you\'ll need to use a logic level converter, or modify the SCMDs from stock to operate at 5V, and supply your own regulated 5V.\

[![SparkFun Logic Level Converter - Bi-Directional](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/2/2/12009-06.jpg)](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html)

### [SparkFun Logic Level Converter - Bi-Directional](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html) 

[ BOB-12009 ]

The SparkFun bi-directional logic level converter is a small device that safely steps down 5V signals to 3.3V AND steps up 3....

[ [\$3.95] ]

### Suggested Reading

If you aren't familiar with the following concepts, we recommend you read over these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one)

### Motors and Selecting the Right One 

Learn all about different kinds of motors and how they operate.

[](https://learn.sparkfun.com/tutorials/binary)

### Binary 

Binary is the numeral system of electronics and programming\...so it must be important to learn. But, what is binary? How does it translate to other numeral systems like decimal?

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide)

### Bi-Directional Logic Level Converter Hookup Guide 

An overview of the Bi-Directional Logic Level Converter, and some example circuits to show how it works.

[](https://learn.sparkfun.com/tutorials/hexadecimal)

### Hexadecimal 

How to interpret hex numbers, and how to convert them to/from decimal and binary.

## Terminology

This guide and related documentation uses a few terms with specific meanings. When *User* and *Expansion* are used, it is referring to the physical pins of the connection. When *Controller* and *Peripheral* are used, it matches the I2C behavior on the *expansion port*, and refers to the connected chain of SCMDs.

**Note:** SparkFun has joined with other members of OSHWA in a resolution to move away from using \"Master\" and \"Slave\" to describe signals between the controller and the peripheral. Check out [this page](https://www.sparkfun.com/spi_signal_names) for more on our reasoning behind this change. You can also see OSHWA\'s resolution [here](https://www.oshwa.org/a-resolution-to-redefine-spi-signal-names).

- **User Port** \-- Connects the user\'s project to the *controller* SCMD and is unused on *peripherals*.
- **Expansion Port** \-- Connects a single *controller* and up to 16 *peripherals*, and should never be connected to the user\'s project.
- **Controller** \-- The SCMD that is connected to the user\'s project. Also, it is the I2C controller on the *expansion port*
- **Peripheral** \-- A SCMD that is only connected to a *controller* SCMD by way of the *expansion port*.

*Note: The config in and out pins of the expansion port may sometimes be connected to the user\'s project for error checking and mitigation purposes.*

**Motor Polarity** \-- The driver and this document often omit motor polarity. This is because polarity to spin direction is not standardized, and it is assumed the user will attach them backwards 50% of the time. Each motor channel is independently configurable for what is thought of as \'forward\' spin by command. It is assumed that the user will first attach the motors, then decide which channels need to be inverted and **issue inversion settings at boot time.**

**Expansion Bus I2C Pull-Ups** \-- All controller SCMDs should have at least one set of pull-ups enabled for their expansion bus, even if no peripherals are present! The board\'s default state is disabled because pull-up resistors should be applied thoughtfully per design, but it means a single controller without peripherals will un-intuitively require the jumper to be closed.

**Motor Numbering** \-- The SCMD\'s silkscreen shows connections for motor \'A\' and motor \'B\' to prevent confusion within a programming environment where numbers are used to denote motors or drivers.

[![Motor numbering scheme](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/motornumbering2_updated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/motornumbering2_updated.jpg)

*Motor numbering scheme*

When somethings refers to a \'motor number\', the following scheme is used. The motor attached to the controller at position \'A\' will always be motor 0, and the \'B\' position, motor 1. The first peripheral device attached will have motors 2, and 3, at positions \'A\' and \'B\' respectively. Peripheral 2 will have motors 4, and 5, and so on.

When a SCMD is designated as bridged mode, it loses whatever motor is attached to the \'B\' position, and any information sent to control the \'A\' position will control both outputs synchronously, such as inversion or drive strength.

This is not to be confused with \'driver number\', which indicates which SCMD in the chain is being referenced.

## Hardware Overview

This section describes the basic parts of the hardware.

[![image of the various parts of the ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/FrontAnnotated01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/FrontAnnotated01.png)

*All of the components are populated on the top side of the board.*

Power is supplied through the **VIN Connection** and is regulated down to 3.3V for the PSoC and logic circuits. A **VCC rail** pin is provided for hackability.

The **Status LED** has a few things that it displays simultaneously:

- Emits a blip when it receives data from the controller.
- Flashes once every \~2.5 seconds to indicate nominal condition
- Flashes eight times per \~2.5 second period to indicate that the failsafe condition has occurred.

The **User Port** is designated for connection to the user\'s project (which will tell the motors what to do), and can be configured as UART, SPI, or I2C by jumper setting.

The **Expansion Port** is configured as I2C controller or peripheral based on jumper settings, and operates on a second I2C bus with only other motor drivers.

The microcontroller generates PWM signals that go straight to the **DRV8835** motor driver, which consists of 2 mosfet H-bridge driver circuits with thermal and current protection built in.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/RearAnnotated02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/RearAnnotated02.jpg)

*The bottom of the board contains user configuration jumpers and a large area to wick the heat.*

### Powering the SCMD

Provide **3.3V to 11V** to \"MAX 11V\" and \"GND\". Each has two through-holes for general use. They can be used to reduce connection resistance or to piggyback other devices, or can accept the leads of a large capacitor. The terminal is directly connected to the DRV8835\'s power input, and is also regulated down to 3.3V for the PSoC supply and logic levels. The driver can consume up to 3A of current so make sure these wires are short or heavier gauge, or both.

When peripherals are attached to the expansion port, they also require power from another source. Wire the \"MAX 11V\" and \"3.3V\" pins in parallel with the controller as shown in [Expansion Port Usage](https://learn.sparkfun.com/tutorials/serial-controlled-motor-driver-hookup-guide#example-3-two-slaves-5-motors-1-bridged-spi-control).

The VCC pin is an advanced feature that can be used to operate the SCMD at a different voltage, but isn\'t used for basic applications. See the [SCMD Datasheet](https://github.com/sparkfun/Serial_Controlled_Motor_Driver/blob/controller/Documentation/SCMD_Datasheet.pdf?raw=true) for more information.

### Jumper Usage Table

There are 4 sets of jumpers to configure on this board. There are pull-up enables for both user (**User PU**) and expansion bus (**Exp. PU**, default not-pulled up), A VCC disconnect jumper (**VCC Src**) to remove all logic from the on-board regulator, and 4 **config** bits that select operational mode.

  Name      Description                                     Usage
  --------- ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  VCC Src   Connects VCC rail (pin) to on-board regulator   Open to remove regulator from VCC rail. User must supply 1.8V to 5.5V to VCC pin
  User PU   I2C pull-up enable for User Port                Close all three pads to connect 4.7k resistors to SDA and SCL of user port
  Exp. PU   I2C pull-up enable for Expansion Port           Close all three pads to connect 4.7k resistors to SDA and SCL of expansion port. The expansion bus should have exactly one board with pull-ups enabled on it. A single controller without peripherals is technically a complete expansion bus, and thus the single controller needs these jumper pads bridged.
  Config    Serial and function selection                   The config bits are 4 bits that form a configuration nybble. A closed jumper is a \'1\' and an open jumper is a \'0\'. See config table for more information.

### Config Bits Table

The configuration is set by encoding a number into the 4 config bits on the bottom of the board. Close a jumper to indicate a 1, or leave it open to indicate a 0. Use this table to see what the user port, address, and expansion port will become in each configuration.

  Pattern   Mode             User Port   User Address   Expansion Port
  --------- ---------------- ----------- -------------- ----------------
  0000      UART at 9600     UART        N/A            Controller
  0001      SPI              SPI         N/A            Controller
  0010      Peripheral       N/A         N/A            Peripheral
  0011      I2C              I2C         0x58           Controller
  0100      I2C              I2C         0x59           Controller
  0101      I2C              I2C         0x5A           Controller
  0110      I2C              I2C         0x5B           Controller
  0111      I2C              I2C         0x5C           Controller
  1000      I2C              I2C         0x5D           Controller
  1001      I2C              I2C         0x5E           Controller
  1010      I2C              I2C         0x5F           Controller
  1011      I2C              I2C         0x60           Controller
  1100      I2C              I2C         0x61           Controller
  1101      UART at 57600    UART        N/A            Controller
  1110      UART at 115200   UART        N/A            Controller
  1111      N/A              Reserved    N/A            N/A

### Pin Connections

The function of the 0.1\" holes are explicitly indicated in this table, and are organized by physical location on the PCB.

+----------------+-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                |             |           |                                                   | Function / Connection                         |
+================+=============+===========+===================================================+===============+===============+===============+
| Group          | Name        | Direction | Description                                       | UART          | I2C           | SPI           |
+----------------+-------------+-----------+---------------------------------------------------+---------------+---------------+---------------+
| User Port      | RX,SCL,COPI | I         | Multi-function Serial                             | Data In (RX)  | SCL           | COPI          |
|                +-------------+-----------+---------------------------------------------------+---------------+---------------+---------------+
|                | TX,SDA,CIPO | IO        | Multi-function Serial                             | Data Out (TX) | SDA           | CIPO          |
|                +-------------+-----------+---------------------------------------------------+---------------+---------------+---------------+
|                | GND         | \-        | Ground                                            | Ground        | Ground        | Ground        |
|                +-------------+-----------+---------------------------------------------------+---------------+---------------+---------------+
|                | NC,SCL      | I         | SPI clock                                         | NC            | NC            | SCL           |
|                +-------------+-----------+---------------------------------------------------+---------------+---------------+---------------+
|                | NC,CS       | I         | SPI chip select                                   | NC            | NC            | CS            |
+----------------+-------------+-----------+---------------------------------------------------+---------------+---------------+---------------+
| Expansion Port | GND         | \-        | Ground                                            | Peripheral bus Ground                         |
|                +-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                | SDA         | IO        | I2C Data line                                     | Peripheral bus SCL                            |
|                +-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                | SCL         | I         | I2C Clock line                                    | Peripheral bus SDA                            |
|                +-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                | In          | I         | Config In. Peripheral aquire-address/enable       | Connects to upstream peripheral\*             |
|                +-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                | Out         | O         | Config Out. Enable next peripheral                | Connects to downstream peripheral\*           |
+----------------+-------------+-----------+---------------------------------------------------+-----------------------------------------------+
| Motor Port     | A1          | O         | Winding of first addressable location             | Motor A winding                               |
|                +-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                | A2          | O         | Winding of first addressable location             | Motor A winding                               |
|                +-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                | B1          | O         | Winding of second addressable location            | Motor B winding                               |
|                +-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                | B2          | O         | Winding of second addressable location            | Motor B winding                               |
+----------------+-------------+-----------+---------------------------------------------------+-----------------------------------------------+
| Power          | GND         | I         | Main system ground (two pads)                     | Supply ground                                 |
|                +-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                | MAX 11V     | I         | Motor driver raw voltage, regulator in (two pads) | Supply power                                  |
|                +-------------+-----------+---------------------------------------------------+-----------------------------------------------+
|                | VCC         | IO        | Regulator output or user supplied VCC             | NC                                            |
+----------------+-------------+-----------+---------------------------------------------------+-----------------------------------------------+

### Typical Application Motors and Heat Sinking

The SCMD is designed to operate small robot drive motors without a heatsink, up to about 500mA continuous current. Here\'s how some regular motors fair when used.

- [Hobby Gearmotor - 200 RPM (Pair)](https://www.sparkfun.com/products/13302) \-- RedBot style motors. These have low stall current and can be used without heatsinks.
- [Micro Gearmotor - 460RPM](https://www.sparkfun.com/products/12429) \-- These can be used without heatsinks.
- [Standard Gearmotor - 303RPM](https://www.sparkfun.com/products/12147) \-- Motors of this larger size can also be used without heatsinks.
- CPU fans \-- can be varied. Include a forward diode to prevent reverse voltage application. Some can draw a large amount of current! If the driver is getting too warm, a heatsink (or forced air) is required.
- [Vacuum Pump - 12V](https://www.sparkfun.com/products/10398) \-- These pumps can draw amps. The driver will need to have heatsinking.

### Determining if a heat sink is necessary

The temperature rise is related to the current load on the motor driver. To determine what your load is, attach the motor directly to a power supply and apply torque as will be done by the final application. Then use the chart below to determine if you need to heat sink. You can also stall the motor completely and measure the stall current (or use a multimeter to check the coil resistance, then do the math).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/temp_chart.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/temp_chart.png)

*Temperature rise as a function of total driver load*

This graph shows total current sourced by the SCMD from both channels. If using bridged mode, find your target current load on the X axis, then see what to expect from these configurations on the Y axis. If not using bridged mode, double the current of a single motor to find the worst case condition of both motors at max current, then use that instead.

The [TO-220 Heat Sink](https://www.sparkfun.com/products/121) and [Theragrip Thermal Tape](https://www.sparkfun.com/products/9771) were used to make the above graph, and work well to give yourself an extra amp of capability in a typical application.

## Example 1: Interactive UART Control with Peripherals

This example demonstrates the basic commands, plus some direct register access possible with only a UART available. This type of program could be easily run from a script from a more classic PC where I2C or SPI isn\'t available.

### User port as UART

**Requirements**

- Computer serial terminal set to 9600 baud.
- Terminal set to send CR and LF (Carriage return and line feed).
- Config jumpers set to \'0000\', or all open.
- Exp. PU jumper fully closed
- A 5V wall supply

Connect the FTDI to the SCMD using the diagram in \"Hardware Connections\", and power the SCMD from the wall supply. Attach two motors to the driver, one between A1 and A2, and the other between B1 and B2.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/Motor_Driver_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/Motor_Driver_Tutorial-01.jpg)

A SCMD ready to drive motors from UART command.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/jumpers5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/jumpers5.jpg)

*The controller is configured as UART (\"0000\"), and has pull up resistors enabled for the expansion bus.*

**Connections**

Connect the FTDI basic to the motor driver as follows. Notice that the both sides have RX that indicates data in, so the RX-TX serial lines must be crossed.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/UART_Connection2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/UART_Connection2.jpg)

Typing should now echo back to your terminal, pressing return should generate a new line (or error message), and commands can be entered. Skip forward to the [UART Commands](https://learn.sparkfun.com/tutorials/serial-controlled-motor-driver-hookup-guide#uart-commands), or, enter the following commands as a guided tour. You may notice some responses like \"inv\" and \"ovf\" if the data entered was no good.

**Example Commands**

When you\'re ready, send the following commands:

\"R01\"

This will read the ID register and return 0xA9

\"M01F50\"

This will tell motor 0 to drive at half speed, forward \-- But nothing will happen yet!

\"E\"

This will enable all drivers. Motor 0 should begin spinning at half speed.

\"M01R100\"

This will tell motor 1 to drive at full speed backwards. Now both should be spinning opposite directions.

\"M01S\"

This will cause motor 1 to reverse \"forward\" direction. Both should be spinning in the same direction now.

\"E\"

E again will disable both motors, which will stop spinning.

See the section \"UART Commands\" for a full command listing.

## UART Commands

### General:

The command parser is built to accept short strings of ascii data, compacted to reduce data transfer size while being easy to handle by standard UART hardware. The general form is a letter indicating which operation to perform followed by a series of numbers and letters, and finally a carriage return and line feed. As a string, an example command would be "M0F50\\r\\n".

### Return codes:

Overflow (\"**ovf**\"): The input buffer is filled (no command should be that long). Send delimiter to clear buffer

Invalid Syntax (\"**inv**\"): The first character in the command is not one of the defined prefixes.

Formatting Error (\"**fmt**\"): There was something generally wrong with the command, like it had the wrong number of characters or an out of range value was detected.

No Motor (\"**nom**\"): The motor\'s number is past the most downstream peripheral detected.

### Commands:

**Help:**

`"H"` or `"?"`\

Prints command reference to serial.

Example:\
`"H\r\n"` -- Drive controller motor B forward at 34%.\

**Drive motor:**

`"Mndl"`\
n = motor number, single or double digits\
d = direction, R or F\
l = level, 0 to 100

Example:\
`"M1F34\r\n"` -- Drive controller motor B forward at 34%.\
`"M2R80\r\n"` -- Drive peripheral motor A reverse at 80%.

**Invert motor polarity:**

`"MnI"`\
n = motor number, single or double digits

Example:\
`"M1I\r\n"` -- Invert the polarity of motor 1.

**Clear motor inversion:**

`"MnC"`\
n = motor number, single or double digits

Example:\
`"M1C\r\n"` -- Set polarity of motor 1 to default.

**Enable and disable Drivers** `"E"` and `"D"`\

The drivers boot in the disabled state so that other settings can be configured before beginning to drive the motors. Use these commands to enable and disable them.

Example:\
`"E\r\n"` -- Enable all outputs\
`"D\r\n"` -- Disable all outputs

**Bridge and un-bridge outputs**

`"Brr"` and `"Nrr"`\
rr = Motor driver number, 0 is controller, 1-16 is peripheral

This causes a motor driver to start or stop synchronous PWM on both \'A\' and \'B\' ports. Notice that the input is by board number, not motor number.

Example:\
`"B0\r\n"` -- Bridge controller\'s outputs `"B2\r\n"` -- Bridge the 2nd physical peripheral\'s outputs (motors 4&5) `"N0\r\n"` -- Un-bridge controller\'s outputs `"N2\r\n"` -- Un-bridge the 2nd physical peripheral\'s outputs (motors 4&5)

**Change the Baud Rate**

`"Un"`\
n = baud rate selection\

This command changes the bitrate of the UART. The serial terminal will need to be reconfigured after this command. The command reports new rate at old baud before changing to the new one.

Rates supported:\
1 -- 2400\
2 -- 4800\
3 -- 9600\
4 -- 14400\
5 -- 19200\
6 -- 38400\
7 -- 57600\
8 -- 115200

Examples:\
`"U3\r\n"` -- Set baud rate to 9600\
`"U8\r\n"` -- Set baud rate to 115200

**Write Register**

`"Wrrhh"`\
rr = two digit hex address\
hh = two digit hex data

Example:\
`"W20FF\r\n"` -- Write 0xFF to register 0x20 (MA_DRIVE).

**Read Register**

`"Rrr"`\
rr = two digit hex address

Example:\
`"R01\r\n"` -- Read address 0x01 (ID), bus will display \"A9\", ID word of 0xA9

**Arbitrary register access** Some of the more intricate features like bus settings and debug information can be accessed by reading from a user-facing memory space, called registers. Use the [SCMD datasheet](https://github.com/sparkfun/Serial_Controlled_Motor_Driver/blob/master/Documentation/SCMD_Datasheet.pdf) for mapping and function.

## Arduino Library Reference

Example 2 and 3 use the Arduino IDE and a RedBoard to communicate with the SCMD. This section outlines how to get it and how the functions themselves operate.

### Getting the Arduino Library

To get the Arduino library, download from Github, or use the Arduino Library Manager.

**Download the Github repository**

Visit the [GitHub repository](https://github.com/sparkfun/SparkFun_Serial_Controlled_Motor_Driver_Arduino_Library) to download the most recent version of the library, or click the link below:

[Download the Arduino Library](https://github.com/sparkfun/SparkFun_Serial_Controlled_Motor_Driver_Arduino_Library/archive/master.zip)

**Use the library manager or install in the Arduino IDE**

For help installing the library, check out our [How To Install An Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library).

If you don\'t end up using the manager, you\'ll need to move the *SparkFun_Serial_Controlled_Motor_Driver_Arduino_Library* folder into a *libraries* folder within your Arduino sketchbook.

### Operating the Library

The library is made such that new motor driver object is constructed without parameters, the user populates the public settings structure, then calls `.begin()` to start the wire library and apply the communication settings.

Example:

    language:c
    SCMD myMotorDriver; //This creates an instance of SCMD which will be bound to a single controller.

    void setup()
    

#### Settings

The main SCMD class has a public member which is named settings. To configure settings, use the format `myMotorDriver.settings.I2CAddress = (...);` then call `.begin()` to apply.

settings contains the following members:

- uint8_t commInterface \-- Set equal to I2C_MODE or SPI_MODE
- uint8_t I2CAddress \-- Set to address that controller is configured to in case of I2C usage
- uint8_t chipSelectPin \-- Set to chip select pin used on Arduino in case of SPI

### Classes and Structures

There are a few classes used in the library. The main class is called `SCMD`, which is the object that talks to the motor drivers. There are also a couple structs in use \-- `SCMDSettings` and `SCMDDiagnostics`. A `SCMDSettings` object named settings is present within the SCMD class for configuration.

#### SCMD

SCMD is used to declare a single chain of motor drivers at specified port and modes in settings. The contained functions are described in a later section.

    language:c
    class SCMD
    ;

#### SCMD Settings

SCMDSettings is an type for the settings member of SCMD. It is declared public to be configured by the user.

    language:c
    struct SCMDSettings
    ;

#### SCMD Diagnostics

SCMDDiagnostics contains a bunch of 8 bit values of data for use with getDiagnostics and getRemoteDiagnostics. Declared objects are passed as a reference to the diagnostic function and written by the collected data.

    language:c
    struct SCMDDiagnostics
    ;

### Functions

#### uint8_t begin( void );

Call after providing settings to start the wire library, apply the settings, and get the ID word (return value should be 0xA9). Don\'t progress unless this returns 0xA9!

#### bool ready( void );

This function checks to see if the SCMD is done booting and is ready to receive commands. Use this after .begin(), and don\'t progress to your main program until this returns true.

#### bool busy( void );

This function checks to see if the SCMD busy with an operation. Wait for busy to be clear before sending each configuration commands (not needed for motor drive levels).

#### void enable( void );

Call after .begin(); to allow PWM signals into the H-bridges. If any outputs are connected as bridged, configure the driver to be bridged before calling .enable();. This prevents the bridges from shorting out each other before configuration.

#### void disable( void );

Call to remove drive from the H-bridges. All outputs will go low.

#### void reset( void );

This resets the I2C hardware for Teensy 3 devices using the alternate library, and nothing otherwise.

#### void setDrive( uint8_t channel, uint8_t direction, uint8_t level );

This sets an output to drive at a level and direction.

- channel: Motor number, 0 through 33.
- direction: 1 or 0 for forward or backwards.
- level: 0 to 255 for drive strength.

#### void inversionMode( uint8_t motorNum, uint8_t polarity );

This switches the perceived direction of a particular motor.

- motorNum: Motor number, 0 through 33.
- polarity: 0 for normal and 1 for inverted direction.

#### void bridgingMode( uint8_t driverNum, uint8_t bridged );

This connects any board\'s outputs together controlling both from what was the \'A\' position.

- driverNum: Number of connected SCMD, 0 (controller) to 16.
- bridged: 0 for normal and 1 for bridged.

#### void getDiagnostics( SCMDDiagnostics &diagObjectReference );

This returns a diagnostic report from the controller.

- &diagObjectReference: Pass a local SCMDDiagnostics object that will be written into.

#### void getRemoteDiagnostics( uint8_t address, SCMDDiagnostics &diagObjectReference );

This returns a diagnostic report from a peripheral.

- address: address of intended peripheral. This starts at 0x50 for the first peripheral and goes up from there.
- &diagObjectReference: Pass a local SCMDDiagnostics object that will be written into.

#### void resetDiagnosticCounts( void );

Clears the diagnostic counts of a controller.

#### void resetRemoteDiagnosticCounts( uint8_t address );

Clears the diagnostic counts of a peripheral.

- address: address of intended peripheral. This starts at 0x50 for the first peripheral and goes up from there.

#### uint8_t readRegister(uint8_t offset);

Returns the contents of a memory location of the controller.

- offset: Memory address to read.

#### void writeRegister(uint8_t offset, uint8_t dataToWrite);

Writes data to a memory location of the controller.

- offset: Memory address to write.
- dataToWrite: Data to write to that address.

#### uint8_t readRemoteRegister(uint8_t address, uint8_t offset);

Returns the contents of a memory location of a peripheral.

- address: address of intended peripheral. This starts at 0x50 for the first peripheral and goes up from there.
- offset: Memory address to read.

#### void writeRemoteRegister(uint8_t address, uint8_t offset, uint8_t dataToWrite);

Writes data to a memory location of a peripheral.

- address: address of intended peripheral. This starts at 0x50 for the first peripheral and goes up from there.
- offset: Memory address to write.
- dataToWrite: Data to write to that address.

## Example 2: RedBot Retrofit (I2C control)

This example drives a robot in left and right arcs, driving in an overall wiggly course. It demonstrates the variable control abilities. When used with a RedBot chassis, each turn is about 90 degrees per drive.

**Requirements**

- [SparkFun RedBoard](https://www.sparkfun.com/products/12757) or Arduino compatible 328p device
- The [Arduino Library](https://github.com/sparkfun/SparkFun_Serial_Controlled_Motor_Driver_Arduino_Library)
- Config jumpers set to address 0x5A, or \'0101\', or positions 0 and 2 closed with 1 and 3 open. Other addresses can be selected by using the bit patters of 0x3 to 0xE, and appropriate address programmed into the 328p code.
- User PU jumper fully closed
- Exp. PU jumper fully closed

The 328p is now ready to communicate with the SCMD. Skip forward to the [Arduino Library](https://learn.sparkfun.com/tutorials/serial-controlled-motor-driver-hookup-guide#arduino-library-reference) section for API usage, or use one of the example sketches.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/Marshall_hookup_guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/Marshall_hookup_guide-01.jpg)

This [Shadow Chassis](https://www.sparkfun.com/products/13301) has been Red-trofitted with a RedBoard and SCMD

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/jumpers1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/jumpers1.jpg)

The connections made are shown here.

**Connections**

Connect the Arduino basic to the motor drvier as follows. The SDA and SCL pins are pulled up by the SCMD only, and should idle at 3.3V.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/I2C_Connection2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/I2C_Connection2.jpg)

**Example Code**

The example, also available from the drop-down menu in Arduino (It\'s called TwoMotorRobot), is as follows:

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

The example works by configuring the motor driver, then using `for` loops to ramp up and down the motor drive levels.

Things to note:

- begin is periodically ran until the returned ID word is valid.
- Setup waits for isReady() to become true before going on to the drive section
- One motor is inverted by command at setup. Do it here so you don\'t have to mess with it later.
- enable() is called to connect the drivers to the PWM generators.
- LEFT_MOTOR and RIGHT_MOTOR are defined to ease use of the setDrive( \... ) function.

## Example 3: Two Peripherals, 5 motors, 1 bridged (SPI control)

This demonstrates more advanced usage of the serial driver. Here, we have a couple peripherals attached, with one being configured as a bridged mode. This is a good example of how the motor numbering scheme works.

**Requirements**

- [SparkFun RedBoard](https://www.sparkfun.com/products/12757) or Arduino compatible 328p device
- The [Arduino Library](https://github.com/sparkfun/SparkFun_Serial_Controlled_Motor_Driver_Arduino_Library)
- A [Logic Level Converter](https://www.sparkfun.com/products/12009)
- Controller config jumpers set to \'0001\', or only position \'0\' closed.
- Peripheral config jumpers set to \'0010\', or only position \'1\' closed.
- Exp. PU jumper fully closed

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/Marshall_hookup_guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/Marshall_hookup_guide-04.jpg)

*The motor drivers are connected on a breadboard for test.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/jumpers2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/jumpers2.jpg)

*The controller is configured as SPI (\"0001\"), and has pull up resistors enabled for the expansion bus.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/jumpers3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/jumpers3.jpg)

*Peripherals boards should be set to \"0010\" with no pull up resistors enabled, as the controller is doing it.*

**Connections**

Connect the Arduino and Level Shifter to the motor drvier as follows. This connects to the standard SCL, COPI, and CIPO positions, and uses pin 10 as a chip select.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/SPI_LLC_gimp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/SPI_LLC_gimp.jpg)

*The user port connections for this example*

While this example will operate with only a controller, add peripherals to the expansion port to get the full experience.

The expansion port allows multiple SCMDs to be run from the same I2C address, SPI select line, or UART instance. The port can support up to 16 SCMDs set as peripheral by a common I2C interface, and daisy-chained config-in to config-out wiring

[![Peripheral Topology](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/peripheralTopology_updated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/peripheralTopology_updated.jpg)

*A diagram showing the expansion bus usage*

Notice that the expansion I2C lines are connected to a common bus while the config lines are connected from one board\'s \'Out\' to the next\'s \'In\'. More peripherals can be added onto the end of the chain.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/4/ExpI2CBasic_Connection.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/4/ExpI2CBasic_Connection.png)

*The expansion bus connections*

When power is applied, the controller will assign addresses to the peripherals. This may take a couple seconds. When complete, the peripherals should all have a faintly lit, blinking status LED indicating communication.

**Example Code**

The example, also available from the drop-down menu in Arduino (It\'s called DriverChainWithBridging), is as follows:

    language:c
    //This example demonstrates some of the more advanced usage of the motor driver.
    //It uses 3 motor drivers, with the controller attached as SPI.  One peripheral is bridged,
    //and the sketch test drives each motor. (There will be a break when the overtaken motor
    //channel is activated.)
    //
    //This also shows how to count the number of connected peripherals and report, as well as
    //arbitrary register access.

    #include <Arduino.h>
    #include <stdint.h>
    #include "SCMD.h"
    #include "SCMD_config.h" //Contains #defines for common SCMD register names and values
    #include "Wire.h"

    //#defines

    //Variables
    //***** Create the Motor Driver object*****//
    SCMD myMotorDriver;

    void setup()
    
      Serial.println( "ID matches 0xA9" );

      Serial.print("Waiting for enumeration...");
      while ( myMotorDriver.ready() == false );
      Serial.println("Done.");

      //  Report number of peripherals found
      uint8_t tempAddr = myMotorDriver.readRegister(SCMD_SLV_TOP_ADDR);
      if ( tempAddr >= START_SLAVE_ADDR )
      
      else
      

      //Configure bridging modes
      myMotorDriver.bridgingMode( 1, 1 ); //( DriverNum 1, bridged state = 1 )  This will bridge the first peripheral

      //Uncomment to set inversion

      //myMotorDriver.inversionMode(0, 1); //invert controller, channel A
      //myMotorDriver.inversionMode(1, 1); //invert controller, channel B
      //myMotorDriver.inversionMode(2, 1); //invert peripheral 1, channel A
      //    no need to configure motor 3, this position does nothing because the peripheral is bridged.
      //myMotorDriver.inversionMode(4, 1); //invert peripheral 2, channel A
      //myMotorDriver.inversionMode(5, 1); //invert peripheral 2, channel B

      //Enable the motors.
      myMotorDriver.enable();

      pinMode(8, INPUT_PULLUP);

    }

    void loop()
    
    }

The example works by counting through the 6 motor positions and commanding them forward, then back.

Things to note:

- Only a single SCMD object is used, all peripherals are accessed through the controller.
- begin is periodically ran until the returned ID word is valid.
- Setup waits for isReady() to become true before going on to the drive section
- Peripherals are counted by directly accessing the registers. ALL_CAPS_VALUES are #defined in SCMD_config.h.
- bridgingMode( \... ) is called to bridge, by number of motor driver (controller is driver 0).
- Motor 3 is excluded because the channel gets connected to motor 2 by brdiging. Though it can still be commanded, it will have no effect.
- enable() is called to activate the motors. This happens after the bridging configuration is set to protect the drivers.