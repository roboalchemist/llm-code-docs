# Source: https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide

## Introduction

The [LSM9DS1](https://www.sparkfun.com/products/13284) is a versatile, motion-sensing system-in-a-chip. It houses a 3-axis [accelerometer](https://learn.sparkfun.com/tutorials/accelerometer-basics), 3-axis [gyroscope](https://learn.sparkfun.com/tutorials/gyroscope), and 3-axis magnetometer \-- **nine degrees of freedom (9DOF)** in a single [IC](https://learn.sparkfun.com/tutorials/integrated-circuits)! Each sensor in the LSM9DS1 supports a wide range of\...ranges: the accelerometer\'s scale can be set to ± 2, 4, 8, or 16 *g*, the gyroscope supports ± 245, 500, and 2000 °/s, and the magnetometer has full-scale ranges of ± 2, 4, 12, or 16 gauss. The IMU-in-a-chip is so cool we put it on a quarter-sized breakout board.

[![SparkFun 9DoF IMU Breakout - LSM9DS1](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/3/3/13284-02.jpg)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-lsm9ds1.html)

### [SparkFun 9DoF IMU Breakout - LSM9DS1](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-lsm9ds1.html) 

[ SEN-13284 ]

The SparkFun LSM9DS1 Breakout is a versatile, motion-sensing system-in-a-chip. It houses a 3-axis accelerometer, 3-axis gyros...

**Retired**

The LSM9DS1 is equipped with a digital interface, but even that is flexible: it supports both [I^2^C](https://learn.sparkfun.com/tutorials/i2c) and [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi), so you\'ll be hard-pressed to find a microcontroller it doesn\'t work with.

### Covered In This Tutorial

This tutorial is devoted to all things LSM9DS1. We\'ll introduce you to the chip itself, then the breakout board. Then we\'ll switch over to example code, and show you how to interface with the board using an Arduino and our [LSM9DS1 Arduino library](https://github.com/sparkfun/SparkFun_LSM9DS1_Arduino_Library).

The tutorial is split into the following pages:

- [LSM9DS1 Overview](https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide#lsm9ds1-overview) \-- An overview of the LSM9DS1, examining its features and capabilities.
- [Breakout Board Overview](https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide#breakout-board-overview) \-- This page examines the LSM9DS1 Breakout Board \-- topics like the pinout, jumpers, and schematic are covered.
- [Hardware Assembly](https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide#hardware-assembly) \-- Assembly tips and tricks, plus some information about the breakout\'s dimensions.
- [Hardware Hookup](https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide#hardware-hookup) \-- Example I^2^C and SPI wiring diagrams.
- [Instlaling the Arduino Library](https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide#installing-the-arduino-library) \-- How to install the **Arduino library**, and use a simple example sketch to verify that your hookup works.
- [Using the Arduino Library](https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide#using-the-arduino-library) \-- An overview of the SFE_LSM9DS1 Arduino library\'s functions and variables.

### Required Materials

This tutorial explains how to use the LSM9DS1 Breakout Board with an Arduino. To follow along, you\'ll need the following materials:

[![Example hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/3/example-hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/example-hookup.jpg)

- [LSM9DS1 Breakout Board](https://www.sparkfun.com/products/13284)
- [Arduino UNO](https://www.sparkfun.com/products/11021), [RedBoard](https://www.sparkfun.com/products/11575), or another [Arduino-compatible board](https://learn.sparkfun.com/tutorials/arduino-comparison-guide)
- [Straight Male Headers](https://www.sparkfun.com/products/116) \-- Or wire. Something to connect between the breakout and a breadboard.
- [Breadboard](https://www.sparkfun.com/products/12002) \-- Any size (even mini) should do.
- [M/M Jumper Wires](https://www.sparkfun.com/products/11026) \-- To connect between Arduino and breadboard.

**The LSM9DS1 is a 3.3V device!** Supplying voltages greater than \~3.6V can permanently damage the IC. As long as your Arduino has a 3.3V supply output, and you\'re OK with using I^2^C, you shouldn\'t need any extra level shifting. But if you want to use SPI, you may need a [level shifter](https://www.sparkfun.com/products/12009).

A logic level shifter is required for any 5V-operating Arduino (UNO, RedBoard, Leonardo, etc). If you use a 3.3V-based \'duino \-- like the [Arduino Pro 3.3V](https://www.sparkfun.com/products/10914) or [3.3V Pro Mini](https://www.sparkfun.com/products/11114) \-- there is no need for level shifting.

### Suggested Reading

If you\'re not familiar with some of the concepts below, we recommend checking out that tutorial before continuing on.

- [Accelerometer Basics](https://learn.sparkfun.com/tutorials/accelerometer-basics)
- [Gyroscopes](https://learn.sparkfun.com/tutorials/gyroscope)
- [Serial Peripheral Interface (SPI)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)
- [Inter-IC Communication (I^2^C)](https://learn.sparkfun.com/tutorials/i2c)
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)
- [Bi-Directional Level Shifter Hookup Guide](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide)

## LSM9DS1 Overview

The LSM9DS1 is one of only a handful of IC\'s that can measure three key properties of movement \-- angular velocity, acceleration, and heading \-- in a single IC.

The [gyroscope](https://learn.sparkfun.com/tutorials/gyroscope) can measure **angular velocity** \-- that is \"how fast, and along which axis, am I rotating?\" Angular velocities are measured in **degrees per second** \-- usually abbreviated to DPS or °/s. The LSM9DS1 can measure up to ± 2000 DPS, though that scale can also be set to either 245 or 500 DPS to get a finer resolution.

An [accelerometer](https://learn.sparkfun.com/tutorials/accelerometer-basics) measures **acceleration**, which indicates how fast velocity is changing \-- \"how fast am I speeding up or slowing down?\" Acceleration is usually either measured in m/s^2^ (meters per second per second) or *g*\'s (gravities \[about 9.8 m/s^2^\]). If an object is sitting motionless it feels about 1 *g* of acceleration towards the ground (assuming that ground is on earth, and the object is near sea-level). The LSM9DS1 measures its acceleration in *g*\'s, and its scale can be set to either ± 2, 4, 8, or 16 *g*.

Finally, there\'s the [magnetometer](http://en.wikipedia.org/wiki/Magnetometer), which measures the power and direction of **magnetic fields**. Though they\'re not easily visible, magnetic fields exist all around us \-- whether you\'re holding a tiny ferromagnet or feeling an attraction to [Earth\'s magnetic field](http://en.wikipedia.org/wiki/Earth%27s_magnetic_field). The LSM9DS1 measures magnetic fields in units of **gauss** (Gs), and can set its measurement scale to either ± 4, 8, 12, or 16 Gs.

By measuring these three properties, you can gain a great deal of knowledge about an object\'s movement and orientation. 9DOF\'s have tons and tons of applications. Measuring the force and direction of Earth\'s magnetic field with a magnetometer, you can approximate your **heading**. An accelerometer in your phone can measure the direction of the force of gravity, and estimate **orientation** (portrait, landscape, flat, etc.). Quadcopters with built-in gyroscopes can look out for sudden rolls or pitches, and correct their momentum before things get out of hand.

[![Axis labels for the LSM9DS1 IC](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/3/lsm9ds1_axes.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/lsm9ds1_axes.png)

*Axis orientations of the LSM9DS1 IC. Note the IC\'s polarity-marking dot (for some reason they rotated the magnetometer in the datasheet).*

The LSM9DS1 measures each of these movement properties in three dimensions. That means it produces **nine pieces of data**: acceleration in x/y/z, angular rotation in x/y/z, and magnetic force in x/y/z. The LSM9DS1 Breakout has labels indicating the accelerometer and gyroscope axis orientations, which share a [right-hand rule](https://en.wikipedia.org/wiki/Right-hand_rule) relationship with each other. Note that, according to the datasheet, the x and y axes of the magnetic sensor are flipped (the image above is copied from the datasheet).

The LSM9DS1 is, in a sense, two IC\'s smashed into one package \-- like if you combined an [LSM6DS3 accel/gryo](http://www.st.com/web/en/catalog/sense_power/FM89/SC1448/PF261181) with an [LSM303DLMTR accel/mag](https://www.sparkfun.com/products/10888). One half of the device takes care of all-things gyroscope and accelerometer, and the other half manages solely the magnetometer. In fact, a few of the control pins are dedicated to a single sensor \-- there are **two chip select pins** (CS_AG for the accel/gyro and CS_M for the mag) and **two serial data out pins** (SDO_AG and SDO_M).

### Choose Your Own Adventure: SPI or I^2^C

In addition to being able to measure a wide variety of movement vectors, the LSM9DS1 is also multi-featured on the communication interface end. It supports both [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) and [I^2^C](https://learn.sparkfun.com/tutorials/i2c), so you should have no difficulty finding a microcontroller that can talk to it.

SPI is generally the easier of the two to implement, but it also requires more wires \-- four versus I^2^C\'s two.

Because the LSM9DS1 supports both methods of communication, **some pins have to pull double-duty**. The *Serial Data Out* (SDO) pin for example, does just that for SPI mode, but if you\'re using the device over I^2^C it becomes an address selector. The *chip select* (CS_M and CS_AG) pins activate SPI mode when low, but if they\'re pulled high the device assumes I^2^C communication. In the section below we discuss each of the LSM9DS1\'s pins, watch out for those pins that support both interfaces.

For much more detailed information about the IC, we encourage you to [check out the datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/LSM9DS1_Datasheet.pdf)!

## Breakout Board Overview

Now that you know everything you need to about the LSM9DS1 IC, let\'s talk a bit about the breakout board it\'s resting on. On this page we\'ll discuss the pins that are broken out, and some of the other features on the board.

### The Pinout

In total, the LSM9DS1 Breakout breaks out 13 pins.

[![Top image](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/board_top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/board_top.jpg)

The bare-minimum connections required are broken out on the left side of the board. These are the power and I^2^C pins (the communication interface the board defaults to):

Pin Label

Pin Function

Notes

GND

Ground

0V voltage supply

VDD

Power Supply

Supply voltage to the chip. Should be regulated between **2.4V and 3.6V.**

SDA

SPI: MOSI\
I^2^C: Serial Data

SPI: Device data in (MOSI)\
I^2^C: Serial data (bi-directional)

SCL

Serial Clock

I^2^C and SPI serial clock.

The remaining pins are broken out on the other side. These pins break out SPI functionality and interrupt outputs:

+-----------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pin Label             | Pin Function                       | Notes                                                                                                                                                           |
+=======================+====================================+=================================================================================================================================================================+
| DEN                   | Gyroscope Data Enable              | Mostly unknown. The LSM9DS1 datasheet doesn\'t have much to say about this pin.                                                                                 |
+-----------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| INT2                  | Accel/Gyro Interrupt 2             | INT1 and INT2 are programmable interrupts for the accelerometer and gyroscope. They can be set to alert on over/under thresholds, data ready, or FIFO overruns. |
+-----------------------+------------------------------------+                                                                                                                                                                 |
| INT1                  | Accel/Gyro Interrupt 1             |                                                                                                                                                                 |
+-----------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| INTM                  | Magnetometer Interrupt             | A programmable interrupt for the magnetometer. Can be set to alert on over-under thresholds.                                                                    |
+-----------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RDY                   | Magnetometer Data Ready            | An interrupt indicating new magnetometer data is available. Non-programmable.                                                                                   |
+-----------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CS M                  | Magnetometer Chip Select           | This pin selects between I^2^C and SPI on the magnetometer. Keep it HIGH for I^2^C, or use it as an (active-low) chip select for SPI.\                          |
|                       |                                    | **HIGH (1)**: SPI idle mode / **I^2^C enabled**\                                                                                                                |
|                       |                                    | **LOW (0)**: **SPI enabled** / I^2^C disabled.                                                                                                                  |
+-----------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CS AG                 | Accel/Gyro Chip Select             | This pin selects between I^2^C and SPI on the accel/gyro. Keep it HIGH for I^2^C, or use it as an (active-low) chip select for SPI.\                            |
|                       |                                    | **HIGH (1)**: SPI idle mode / **I^2^C enabled**\                                                                                                                |
|                       |                                    | **LOW (0)**: **SPI enabled** / I^2^C disabled.                                                                                                                  |
+-----------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDO M                 | SPI: Magnetometer MISO\            | In SPI mode, this is the magnetometer data output (SDO_M).\                                                                                                     |
|                       | I^2^C: Magnetometer Address Select | In I^2^C mode, this selects the LSb of the I^2^C address (SA0_M)                                                                                                |
+-----------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDO AG                | SPI: Accel/Gyro MISO\              | In SPI mode, this is the accel/gryo data output (SDO_AG).\                                                                                                      |
|                       | I^2^C: Accel/Gryo Address Select   | In I^2^C mode, this selects the LSb of the I^2^C address (SA0_AG)                                                                                               |
+-----------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Power Supply

The VDD and GND pins are where you\'ll supply a voltage and 0V reference to the IC. The breakout board does not regulate this voltage, so make sure it falls within the allowed supply voltage range of the LSM9DS1: **2.4V to 3.6V**. Below is the electrical characteristics table from the datasheet.

[![Electrical characteristics](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/3/electrical-characteristics.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/electrical-characteristics.png)

The communication pins are not 5V tolerant, so they\'ll need to be regulated to within a few mV of VDD.

Another very cool thing about this sensor is how **low-power** it is. In normal operation \-- with every sensor turned on \-- it\'ll pull around **4.5mA**.

#### Communication

CS_AG, CS_M, SDO_AG, SDO_M, SCL, and SDA are all used for the I^2^C and SPI interfaces. The function of these pins depends upon which of the two interfaces you\'re using.

If you\'re using using **I^2^C** here\'s how you might configure these pins:

- Pull CS_AG and CS_M HIGH. This will set both the accel/gyro and magnetometer to I^2^C mode.
- Set SDO_AG and SDO_M either HIGH or LOW. These pins set the I^2^C address of the gyro and accel/mag sensors.
- Connect SCL to your microcontroller\'s SCL pin.
- Connect SDA to your microcontroller\'s SDA pin.
- The board has a built-in 10kΩ pull-up resistor on both SDA and SCL lines. If that value is too high, you can add a second resistor in parallel to divide the pull-up resistance down (another 10kΩ in parallel, for example, would create an equivalent 5kΩ resistance).

Or, if you\'re using **SPI**:

- Connect CS_AG and CS_M to two individually controllable pins on your microcontroller. These chip-selects are active-low \-- when the pin goes LOW, SPI communication with either the accel/gyro (CS_AG) or magnetometer (CS_M) is enabled.
- SDO_AG and SDO_M are the serial data out pins. In many cases you\'ll want to connect them together, and wire them to your microcontroller\'s **MISO** (master-in, slave-out) pin.
- Connect SCL to your microcontroller\'s **SCLK** (serial clock) pin.
- Connect SDA to your microcontroller\'s **MOSI** (master-out, slave-in) pin.

#### Interrupts

There are a variety of interrupts on the LSM9DS1. While connecting up to these is not as critical as the communication or power supply pins, using them will help you get the most out of the chip.

The accelerometer- and gyroscope-specific interrupts are **INT1** and **INT2**. These can both be programmed to interrupt as either active-high or active-low, triggering on events like data ready or when an acceleration or angular rotation exceeds a set threshold.

**DRDY** and **INTM** are devoted magnetometer interrupts. DRDY will go low when new magnetometer readings are available. INTM is a little more customizable \-- it can be used to trigger whenever magnetic field readings exceed a threshold on a set axis.

### The Jumpers

Flipping the LSM9DS1 breakout over reveals a trio of two-way, surface mount jumpers. Each of these jumpers comes **closed**. Their purpose is to **automatically put the LSM9DS1 into I^2^C mode**.

[![Jumpers on breakout](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/board_bottom.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/board_bottom.jpg)

*The three two-way jumpers on the back of the board. Follow the labels to see which pin they pull up.*

Each of these jumpers pulls a pair of pins up to VDD, through a 10kΩ resistor. The middle pad of the jumper connects to the resistor, and the edge pads connect to a pin (follow the labels to find out which one). You can see how those jumpers match up on the [schematic](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/SparkFun-LSM9DS1-Breakout-schematic.pdf):

[![Jumpers on schematic](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/schematic-jumpers.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/schematic-jumpers.png)

The top jumper connects CS_AG and CS_M to a pull-up \-- this\'ll set the LSM9DS1 to I^2^C mode. The middle jumper pulls up SDO_AG and SDO_M, which sets the I^2^C address of the chip. Finally, the far-left jumper adds pull-up resistors to the I^2^C communication pins \-- SDA and SCL.

The intention of these jumpers is to make it as easy-as-possible to use the board; using as few wires as possible. If you\'re using the breakout with I^2^C, you can ignore the four SDO and CS pins.

To disable any of these jumpers, whip out your [handy hobby knife](https://www.sparkfun.com/products/9200), and carefully cut the small traces between middle pad and edge pads. Even if you\'re using SPI, though, the jumpers shouldn\'t hinder your ability to communicate with the chip.

## Hardware Assembly

On this page we\'ll discuss assembly hints. There\'s really not much to assembling the breakout board \-- the real key is [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) *something* into the breakout holes.

### Solder Something

To get a solid electrical and physical connection to the LSM9DS1 Breakout, you\'ll need to solder either connectors or wires to the break-out pins. What, exactly, you solder into the board depends on how you\'re going to use it.

If you\'re going to use the breakout board in a [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) or similar 0.1\"-spaced perfboard, we recommend soldering [straight male headers](https://www.sparkfun.com/products/116) into the pins (there are also [long headers](https://www.sparkfun.com/products/10158) if you need \'em).

[![I2C and power pins soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/3/headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/headers.jpg)

If you\'re only going to use the I^2^C interface \-- and ignore the interrupts \-- you can get away with soldering just the four-pin header.

If you\'re going to mount the breakout into a tight place, you may want to opt for soldering wires ([stranded](https://www.sparkfun.com/products/11375) or [solid-core](https://www.sparkfun.com/products/11367)) into the pins.

### Mounting the Breakout

Because the LSM9DS1 senses motion, it\'s important (for most applications, at least) to keep it pinned in place. So the boards have four mounting holes toward the corners. The drill holes are 0.13\" in diameter, so they should accommodate any [4/40 screw](https://www.sparkfun.com/products/10453).

[![LSM9DS1 Breakout dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/3/board_dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/board_dimensions.png)

Consult the [EAGLE PCB design files](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/SparkFun-LSM9DS1-Breakout_EAGLE.zip) to find out more about the Breakout\'s dimensions.

## Hardware Hookup

The LSM9DS1 will work over either I^2^C or SPI. Here are some example wiring diagrams, demonstrating how to wire up each interface.

### I^2^C Hardware Hookup

Out-of-the-box, the board is configured for an I^2^C interface, as such we recommend using this hookup if you\'re otherwise agnostic. All you need is four wires!

[![Arduino I2C Fritzing Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/3/Arduino_LSM9DS1_i2c_Fritzing_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/Arduino_LSM9DS1_i2c_Fritzing_bb.png)

*Connecting the LSM9DS1 to a RedBoard via I^2^C.*

This hookup relies on all of the **jumpers** on the back of the board being set (as they should be, unless they\'ve been sliced). If the jumpers have been cut, connect all four CS and SDO pins to 3.3V.

No level shifters even though the Arduino\'s I/O pins are 5V? Well, I^2^C is a funny interface: pins aren\'t directly pulled high by a GPIO, instead an open-drain MOSFET relies on pull-up resistors to create a logic high. Because the breakout board pull-up resistors are stronger (less resistance) than the Arduino\'s internal pull-ups, the voltage on the logic pins will be much closer to 3.3V (though a little higher) than 5V \-- within a tolerable range. Just make sure you power the breakout off of the Arduino\'s 3.3V power rail!

### SPI Hardware Hookup

For the SPI hookup, we\'ll use the Arduino\'s hardware SPI pins \-- 11 (MOSI), 12 (MISO), and 13 (SCLK) \-- in addition to two digital pins of your choice (for the chip selects).

#### 3.3V Arduino w/ SPI

If you\'re using a 3.3V Arduino, like the [3.3V/8MHz Pro Mini](https://www.sparkfun.com/products/11114), you can hook the microcontroller pins directly up to the LSM9DS1.

[![Arduino Pro Mini 3.3V LSM9DS1 Fritzing Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/3/Arduino_Pro_Mini_3V3_LSM9DS1_SPI_Fritzing_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/Arduino_Pro_Mini_3V3_LSM9DS1_SPI_Fritzing_bb.png)

#### 5V Arduino w/ SPI

If you\'re using a 5V Arduino, you\'ll also need to grab a level shifter to keep the SPI signals within the tolerable voltage range. You could use the [SparkFun Bi-Directional Logic Level Converter](https://www.sparkfun.com/products/12009) for example:

[![5V Arduino Logic Level Converter and LSM9DS1 SPI Fritzing Circuit ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/3/Arduino_LLC_LSM9DS1_9DOF_SPI_Fritzing_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/Arduino_LLC_LSM9DS1_9DOF_SPI_Fritzing_bb.png)

(Unless you enjoy wire-tangles, the I^2^C or 3.3V SPI hookups are recommended.)

## Installing the Arduino Library

We\'ve written a full-featured Arduino library to help make interfacing with the LSM9DS1\'s gyro, accelerometer, and magnetometer as easy-as-possible. Visit the [GitHub repository](https://github.com/sparkfun/SparkFun_LSM9DS1_Arduino_Library) to download the most recent version of the library, or click the link below:

[Download the SparkFun LSM9DS1 Arduino Library](https://github.com/sparkfun/SparkFun_LSM9DS1_Arduino_Library/archive/master.zip)

For help installing the library, check out our [How To Install An Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library). You\'ll need to move the *SparkFun_LSM9DS1_Arduino_Library* folder into a *libraries* folder within your Arduino sketchbook.

### The LSM9DS1_Basic_I2C Example

To verify that your hookup works, load up the LSM9DS1_Basic_I2C example by going to **File** \> **Examples** \> **LSM9DS1 Breakout** \> **LSM9DS1_Basic_I2C**. (If you\'re using the SPI hookup, load the LSM9DS1_Basic_SPI example instead.)

The default values set by this sketch should work for a fresh, out-of-the-box LSM9DS1 Breakout \-- it assumes all of the jumpers on the backside are closed. Upload the sketch, then open up your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics), setting the baud rate to **115200**. You should see something like this:

[![Example serial monitor output](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/Arduino_serial_monitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/Arduino_serial_monitor.jpg)

The current reading from each axis on each sensor is printed out, then those values are used to estimate the sensor\'s orientation. Pitch is the angle rotated around the y-axis, roll is the board\'s rotation around the x-axis, and heading (i.e. yaw) is the sensor\'s rotation around the z-axis. Try rotating the board (without pulling out any wires!) to see how the values change.

## Using the Arduino Library

To help demonstrate the library\'s functionality, a handful of examples are included which range from basic to more advanced. To begin to get a feel for the library\'s API, try loading up some of the other examples. The comments at the top of the sketch will instruct you on any extra hookup that may be required to use interrupts or other features.

On this page we\'ll quickly run down some of the more basic, fundamental concepts implemented by the library.

### Setup Stuff

To enable the library, you\'ll need to **include** it, and you also need to include the [SPI](http://arduino.cc/en/Reference/SPI) and [Wire](http://arduino.cc/en/reference/wire) libraries:

    language:c
    #include <SPI.h> // SPI library included for SparkFunLSM9DS1
    #include <Wire.h> // I2C library included for SparkFunLSM9DS1
    #include <SparkFunLSM9DS1.h> // SparkFun LSM9DS1 library

Make sure the SPI and Wire includes are above the \"SparkFunLSM9DS1\" (even though you\'ll only be using one of the two interfaces).

#### Constructor

The constructor creates an instance of the LSM9DS1 class. Once you\'ve created the instance, that\'s what you\'ll use to control the breakout from there on. This single line of code is usually placed in the **global** area of your sketch.

The constructor should be left without any parameters:

    language:c
    // Use the LSM9DS1 class to create an object. [imu] can be
    // named anything, we'll refer to that throught the sketch.
    LSM9DS1 imu;

#### Setting Up the Interface

The LSM9DS1 has tons of settings to be configured. Some are minute, others are more critical. The three most critical settings we\'ll need to configure are the **communication interface** and the device addresses. To configure these values, we\'ll make calls to the IMU\'s `settings` struct.

Here\'s an example that sets the IMU up for I^2^C mode, with the default (high) I^2^C addresses:

    language:c
    // SDO_XM and SDO_G are both pulled high, so our addresses are:
    #define LSM9DS1_M   0x1E // Would be 0x1C if SDO_M is LOW
    #define LSM9DS1_AG  0x6B // Would be 0x6A if SDO_AG is LOW
    ...
    imu.settings.device.commInterface = IMU_MODE_I2C; // Set mode to I2C
    imu.settings.device.mAddress = LSM9DS1_M; // Set mag address to 0x1E
    imu.settings.device.agAddress = LSM9DS1_AG; // Set ag address to 0x6B

Alternatively, if you\'re using SPI mode, the `imu.settings.device.mAddress` and `imu.settings.device.agAddress` values become the **chip select pins**. For example, if you\'re using SPI mode with CS_AG connected to D10 and CS_M connected to D9, your setting configuration would look like this:

    language:c
    imu.settings.device.commInterface = IMU_MODE_SPI; // Set mode to SPI
    imu.settings.device.mAddress = 9; // Mag CS pin connected to D9
    imu.settings.device.agAddress = 10; // AG CS pin connected to D10

Configuring any value from the `imu.settings.device` can\'t take place in the global are of a sketch. If you get a compilation error, like `'imu' does not name a type`, you may have those in the wrong place \-- put them in `setup()`.

#### begin()-ing and Setting Sensor Ranges

Once you\'ve created the LSM9DS1 object, and configured its interface, call the `begin()` member function to initialize the IMU.

The `begin()` function will take the settings you\'ve adjusted in the previous step, and attempt to communicate with and initialize the sensors. You can check the return value of `begin()` to verify whether or not the set up was successful \-- it will return `0` if something goes wrong.

    language:c
    if (!imu.begin())
    

Once `begin()` has returned a success, you can start reading some sensor values!

### Reading and Interpreting the Sensors

What good is the sensor if you can\'t get any data from it!? Here are the functions you\'ll need to get acceleration, rotation speed, and magnetic field strength data from the library.

#### readAccel(), readGyro(), and readMag()

These three functions \-- `readAccel()`, `readGyro()`, and `readMag()` \-- poll the LSM9DS1 to get the most up-to-date readings from each of the three sensors.

The read functions don\'t take any parameters, and they don\'t return anything, so how do you get that data? After the function runs its course, it\'ll update a set of **three class variables**, which will have the sensor data you desire. `readAccel()` will update `ax`, `ay`, and `az`, `readGyro()` will update `gx`, `gy`, and `gz`, and `readMag()` will update `mx`, `my`, and `mz`. Here\'s an example:

    language:c
    imu.readAccel(); // Update the accelerometer data
    Serial.print(imu.ax); // Print x-axis data
    Serial.print(", ");
    Serial.print(imu.ay); // print y-axis data
    Serial.print(", ");
    Serial.println(imu.az); // print z-axis data

*An example of reading and printing all three axes of accelerometer data.*

Those values are all **signed 16-bit integers**, meaning they\'ll range from -32,768 to 32,767. That value doesn\'t mean much unless you know the scale of your sensor, which is where the next functions come into play.

#### calcAccel(), calcGyro(), and calcMag()

The library keeps track of each sensor\'s scale, and it implements these helper functions to make translating between the raw ADC readings of the sensor to actual units easy.

`calcAccel()`, `calcGyro()`, and `calcMag()` all take a single parameter \-- a signed 16-bit integer \-- and convert to their respective units. They all **return a float value**, which you can do with as you please.

Here\'s an example of printing calculated gyroscope values:

    language:c
    imu.readGyro(); // Update gyroscope data
    Serial.print(imu.calcGyro(imu.gx)); // Print x-axis rotation in DPS
    Serial.print(", ");
    Serial.print(imu.calcGyro(imu.gy)); // Print y-axis rotation in DPS
    Serial.print(", ");
    Serial.println(imu.calcGyro(imu.gz)); // Print z-axis rotation in DPS

### Setting Sensor Ranges and Sample Rates

Some of the more commonly altered attributes in the IMU are the sensor ranges and output data rates. These values can be configured, once again, by setting a value in the `settings` struct.

For example, to set the IMU\'s accelerometer range to ±16g, gyroscope to ±2000 °/s, and magnetometer to ±8 Gs, do something like this:

    language:c
    imu.settings.accel.scale = 16; // Set accel range to +/-16g
    imu.settings.gyro.scale = 2000; // Set gyro range to +/-2000dps
    imu.settings.mag.scale = 8; // Set mag range to +/-8Gs
    imu.begin(); // Call begin to update the sensor's new settings

The output data rates are a bit more abstract. These values can range from 1-6, where 1 is the slowest update rate and 6 is the fastest.