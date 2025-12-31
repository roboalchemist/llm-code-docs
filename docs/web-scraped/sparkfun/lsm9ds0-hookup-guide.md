# Source: https://learn.sparkfun.com/tutorials/lsm9ds0-hookup-guide

## Introduction

The [LSM9DS0](https://www.sparkfun.com/products/12636) is a versatile, motion-sensing system-in-a-chip. It houses a 3-axis [accelerometer](https://learn.sparkfun.com/tutorials/accelerometer-basics), 3-axis [gyroscope](https://learn.sparkfun.com/tutorials/gyroscope), and 3-axis magnetometer \-- **nine degrees of freedom (9DOF)** in a single [IC](https://learn.sparkfun.com/tutorials/integrated-circuits)! Each sensor in the LSM9DS0 supports a wide range of\...ranges: the accelerometer\'s scale can be set to ± 2, 4, 6, 8, or 16 *g*, the gyroscope supports ± 245, 500, and 2000 °/s, and the magnetometer has full-scale ranges of ± 2, 4, 8, or 12 gauss. The IMU-in-a-chip is so cool we put it on a breakout board.

[![SparkFun 9 Degrees of Freedom IMU Breakout - LSM9DS0](https://cdn.sparkfun.com/r/600-600/assets/parts/9/3/1/9/12636-01.jpg)](https://www.sparkfun.com/products/12636)

### [SparkFun 9 Degrees of Freedom IMU Breakout - LSM9DS0](https://www.sparkfun.com/products/12636) 

[ SEN-12636 ]

This is the LSM9DS0, a versatile motion-sensing system-in-a-chip that houses a 3-axis accelerometer, 3-axis gyroscope, and 3-...

**Retired**

The LSM9DS0 is equipped with a digital interface, but even that is flexible: it supports both [I^2^C](https://learn.sparkfun.com/tutorials/i2c) and [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi), so you\'ll be hard-pressed to find a microcontroller it doesn\'t work with.

### Covered In This Tutorial

This tutorial is devoted to all things LSM9DS0. We\'ll introduce you to the chip itself, then the breakout board. Then we\'ll switch over to example code, and show you how to interface with the board using an Arduino and our [SFE_LSM9DS0 Arduino library](https://github.com/sparkfun/SparkFun_LSM9DS0_Arduino_Library).

The tutorial is split into the following pages:

- [About the LSM9DS0](https://learn.sparkfun.com/tutorials/lsm9ds0-hookup-guide/about-the-lsm9ds0) \-- An overview of the LSM9DS0, examining its features and capabilities.
- [Breakout Overview](https://learn.sparkfun.com/tutorials/lsm9ds0-hookup-guide/breakout-overview) \-- This page covers the LSM9DS0 Breakout Board \-- topics like the pinout, jumpers, and schematic.
- [Hardware Assembly](https://learn.sparkfun.com/tutorials/lsm9ds0-hookup-guide/hardware-assembly) \-- Assembly tips and tricks, plus some information about the breakout\'s dimensions.
- [Basic Arduino Example](https://learn.sparkfun.com/tutorials/lsm9ds0-hookup-guide/basic-arduino-example) \-- How to install the **Arduino library**, and use a simple example sketch.
- [Advanced Arduino Example](https://learn.sparkfun.com/tutorials/lsm9ds0-hookup-guide/advanced-arduino-example) \-- A more advanced Arduino sketch \-- using the library \-- showing off features like switch the sensors\' scales and data rates.
- [Using the Arduino Library](https://learn.sparkfun.com/tutorials/lsm9ds0-hookup-guide/using-the-arduino-library) \-- An overview of the SFE_LSM9DS0 Arduino library.

### Required Materials

This tutorial explains how to use the LSM9DS0 Breakout Board with an Arduino. To follow along, you\'ll need the following materials:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/0/9/0/7/c/lsm9ds0-connected-to-arduino.jpg)](https://cdn.sparkfun.com/assets/0/9/0/7/c/lsm9ds0-connected-to-arduino.jpg)

- [LSM9DS0 Breakout Board](https://www.sparkfun.com/products/12636)
- [Arduino UNO](https://www.sparkfun.com/products/11021), [RedBoard](https://www.sparkfun.com/products/11575), or another [Arduino-compatible board](https://learn.sparkfun.com/tutorials/arduino-comparison-guide)
- [Straight Male Headers](https://www.sparkfun.com/products/116) \-- Or wire. Something to connect between the breakout and a breadboard.
- [Breadboard](https://www.sparkfun.com/products/12002) \-- Any size (even mini) should do.
- [M/M Jumper Wires](https://www.sparkfun.com/products/11026) \-- To connect between Arduino and breadboard.
- **Logic Level Converter** (any of the following could work)
  - [Bi-Directional Logic Level Converter](https://www.sparkfun.com/products/12009) \-- MOSFET-based level shifter (**this is what the tutorial uses**).
  - [PCA9306 Bi-Directional Voltage Translator](https://www.sparkfun.com/products/11955) \-- Solid I^2^C-focused level shifter.

A logic level shifter is required for any 5V-operating Arduino (UNO, RedBoard, Leonardo, etc). If you use a 3.3V-based \'duino \-- like the [Arduino Pro 3.3V](https://www.sparkfun.com/products/10914) or [3.3V Pro Mini](https://www.sparkfun.com/products/11114) \-- there is no need for level shifting.

### Suggested Reading

If you\'re not familiar with some of the concepts below, we recommend checking out that tutorial before continuing on.

- [Accelerometer Basics](https://learn.sparkfun.com/tutorials/accelerometer-basics)
- [Gyroscopes](https://learn.sparkfun.com/tutorials/gyroscope)
- [Serial Peripheral Interface (SPI)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)
- [Inter-IC Communication (I^2^C)](https://learn.sparkfun.com/tutorials/i2c)
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)
- [Bi-Directional Level Shifter Hookup Guide](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide)

## About the LSM9DS0

The LSM9DS0 is one of only a handful of IC\'s that can measure three key properties of movement \-- angular velocity, acceleration, and heading \-- in a single IC.

The [gyroscope](https://learn.sparkfun.com/tutorials/gyroscope) can measure **angular velocity** \-- that is \"how fast, and along which axis, am I rotating?\" Angular velocities are measured in **degrees per second** \-- usually abbreviated to DPS or °/s. The LSM9DS0 can measure up to ± 2000 DPS, though that scale can also be set to either 245 or 500 DPS to get a finer resolution.

An [accelerometer](tutorials/) measures **acceleration**, which indicates how fast velocity is changing \-- \"how fast am I speeding up or slowing down?\" Acceleration is usually either measured in m/s^2^ (meters per second per second) or *g*\'s (gravities \[about 9.8 m/s^2^\]). If an object is sitting motionless it feels about 1 *g* of acceleration towards the ground (assuming that ground is on earth, and the object is near sea-level). The LSM9DS0 measures its acceleration in *g*\'s, and its scale can be set to either ± 2, 4, 6, 8, or 16_g\_.

Finally, there\'s the [magnetometer](http://en.wikipedia.org/wiki/Magnetometer), which measures the power and direction of **magnetic fields**. Though they\'re not easily visible, magnetic fields exist all around us \-- whether you\'re holding a tiny ferromagnet or feeling an attraction to [Earth\'s magnetic field](http://en.wikipedia.org/wiki/Earth%27s_magnetic_field). The LSM9DS0 measures magnetic fields in units of **gauss** (Gs), and can set its measurement scale to either ± 2, 4, 8, or 12 Gs.

By measuring these three properties, you can gain a great deal of knowledge about an object\'s movement. 9DOF\'s have tons and tons of applications. Measuring the force and direction of Earth\'s magnetic field with a magnetometer, you can approximate your **heading**. An accelerometer in your phone can measure the direction of the force of gravity, and estimate **orientation** (portrait, landscape, flat, etc.). Quadcopters with built-in gyroscopes can look out for sudden rolls or pitches, and correct their momentum before things get out of hand.

[![9 degrees of freedom](https://cdn.sparkfun.com/r/600-600/assets/8/b/b/4/5/9DOF-3axes.png)](https://cdn.sparkfun.com/assets/8/b/b/4/5/9DOF-3axes.png)

The LSM9DS0 measures each of these movement properties in three dimensions. That means it produces **nine pieces of data**: acceleration in x/y/z, angular rotation in x/y/z, and magnetic force in x/y/z. On the breakout board, the z-axis runs normal to the PCB, the y-axis runs parallel to the short edge, and the x-axis is parallel to the long edge. Each axis has a positive and negative direction as well, noted by the direction of the arrow on the label.

The LSM9DS0 is, in a sense, two IC\'s smashed into one package \-- like if you combined an [L3G4200D gyro](https://www.sparkfun.com/products/10612) with an [LSM303DLMTR accel/mag](https://www.sparkfun.com/products/10888). One half of the device takes care of all-things gyroscope, and the other half manages both the accelerometer and magnetometer. In fact, a few of the control pins are dedicated to a single sensor \-- there are **two chip select pins** (CSG for the gyro and CSXM for the accel/mag) and **two serial data out pins** (SDOG and SDOXM).

### Choose Your Own Adventure: SPI or I^2^C

In addition to being able to measure a wide variety of movement vectors, the LSM9DS0 is also multi-featured on the hardware end. It supports both [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) and [I^2^C](https://learn.sparkfun.com/tutorials/i2c), so you should have no difficulty finding a microcontroller that can talk to it.

SPI is generally the easier of the two to implement, but it also requires more wires \-- four versus I^2^C\'s two.

Because the LSM9DS0 supports both methods of communication, **some pins have to pull double-duty**. The *Serial Data Out* pin for example, does just that for SPI mode, but if you\'re using the device over I^2^C it becomes an address selector. *Chip select* activates SPI mode when it\'s low, but if it\'s pulled high the device assumes I^2^C communication. In the section below we discuss each of the LSM9DS0\'s pins, pay close attention to those pins that support both interfaces.

------------------------------------------------------------------------

For much more detailed information about the IC, we encourage you to [check out the datasheet](https://cdn.sparkfun.com/assets/f/6/1/f/0/LSM9DS0.pdf)!

## Breakout Overview

Now that you know everything you need to about the LSM9DS0 IC, let\'s talk a bit about the breakout board it\'s resting on. On this page we\'ll discuss the pins that are broken out, and some of the other features on the board.

### The Pinout

In total, the LSM9DS0 Breakout breaks out 13 pins.

[![alt text](https://cdn.sparkfun.com/assets/7/f/7/9/1/top-view-pinout.jpg)](https://cdn.sparkfun.com/assets/7/f/7/9/1/top-view-pinout.jpg)

Here\'s an overview of each of the pin functions:

Pin Label

Pin Function

Notes

CSG

Chip Select Gyro

This pin selects between I^2^C and SPI on the gyro. Keep it HIGH for I^2^C, or use it as an (active-low) chip select for SPI.\
**HIGH (1)**: SPI idle mode / **I^2^C enabled**\
**LOW (0)**: **SPI enabled** / I^2^C disabled.

CSXM

Chip Select Accel/Mag (XM)

This pin selects between I^2^C and SPI on the XM. Keep it HIGH for I^2^C, or use it as an (active-low) chip select for SPI.\
**HIGH (1)**: SPI idle mode / **I^2^C enabled**\
**LOW (0)**: **SPI enabled** / I^2^C disabled.

SDOG

SPI: Gyroscope MISO\
I^2^C: Gyro address select

In SPI mode, this is the gyroscope data output (SDO_G).\
In I^2^C mode, this selects the LSb of the I^2^C address (SA0_G)

SDOXM

SPI: Accel/Mag MISO\
I^2^C: XM address select

In SPI mode, this is the XM data output (SDO_XM).\
In I^2^C mode, this selects the LSb of the I^2^C address (SA0_XM)

SCL

Serial Clock

I^2^C and SPI serial clock.

SDA

SPI: MOSI\
I^2^C:Serial Data

SPI: Device data in (MOSI)\
I^2^C: Serial data (bi-directional)

VDD

Power Supply

Supply voltage to the chip. Should be regulated between **2.4V and 3.6V**.

GND

Ground

0V voltage supply

DEN

Gyroscope Data Enable

Mostly unknown. The LSM9DS0 datasheet doesn\'t have much to say about this pin.

INTG

Gyro Programmable Interrupt

An interrupt that can be programmed as active high/low, push-pull, or open drain. It can trigger on over/under rotation speeds.

DRDYG

Gyroscope data ready

An interrupt that can indicate new gyro data is ready or buffer overrun.

INT1XM

Accel/Mag Interrupt 1

A programmable interrupt that can trigger on data ready, over-acceleration or \"taps\".

INT2XM

Accel/Mag Interrupt 2

A programmable interrupt that can trigger on data ready, over-acceleration or \"taps\".

\
These pins can all be classified into one of three categories: communication, interrupts, or power.

#### Power Supply

The VDD and GND pins are where you\'ll supply a voltage and 0V reference to the IC. The breakout board does not regulate this voltage, so make sure it falls within the allowed supply voltage range of the LSM9DS0: **2.4V to 3.6V**. Below is the electrical characteristics table from the datasheet.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/0/3/6/a/1/electrical-characteristics.jpg)](https://cdn.sparkfun.com/assets/0/3/6/a/1/electrical-characteristics.jpg)

The communication pins are not 5V tolerant, so they\'ll need to be regulated to within a few mV of VDD.

Another very cool thing about this sensor is how **low-power** it is. In normal operation \-- with every sensor turned on \-- it\'ll pull around **6.5mA**.

#### Communication

CSG, CSXM, SDOG, SDOXM, SCL, and SDA are all used for the I^2^C and SPI interfaces. The function of these pins depends upon which of the two interfaces you\'re using.

If you\'re using using **I^2^C** here\'s how you might configure these pins:

- Pull CSG and CSXM HIGH. This will set both the gyro and accel/mag to I^2^C mode.
- Set SDOG and SDOXM either HIGH or LOW. These pins set the I^2^C address of the gyro and accel/mag sensors.
- Connect SCL to your microcontroller\'s SCL pin.
- Connect SDA to your microcontroller\'s SDA pin.
- The board has a built-in 10kΩ pull-up resistor on both SDA and SCL lines. If that value is too high, you can add a second 10kΩ resistor in parallel to divide the pull-up resistance to about 5kΩ.

Or, if you\'re using **SPI**:

- Connect CSG and CSXM to two individually controllable pins on your microcontroller. These chip-selects are active-low \-- when the pin goes LOW, SPI communication with either the gyro (CSG) or accel/mag (CSXM) is enabled.
- SDOG and SDOXM are the serial data out pins. In many cases you\'ll want to connect them together, and wire them to your microcontroller\'s **MISO** (master-in, slave-out) pin.
- Connect SCL to your microcontroller\'s SCLK (serial clock) pin.
- Connect SDA to your microcontroller\'s **MOSI** (master-out, slave-in) pin.

#### Interrupts

There are a variety of interrupts on the LSM9DS0. While connecting up to these is not as critical as the communication or power supply pins, using them will help you get the most out of the chip.

The accelerometer- and magnetometer-specific interrupts are **INT1XM** and **INT2XM**. These can both be programmed to interrupt as either active-high or active-low, triggering on events like data ready, tap-detection, or when an acceleration or magnetic field passes a set threshold.

**DRDY** and **INTG** are devoted gyroscope interrupts. DRDY can be programmed to go high or low when new gyroscope readings are ready to read. INTG is a little more customizable, it can be used to trigger whenever angular rotation exceeds a threshold on any axis.

### The Jumpers

Flipping the LSM9DS0 breakout over reveals three two-way, surface mount jumpers. Each of these jumpers comes **closed**. Their purpose is to **automatically put the LSM9DS0 into I^2^C mode**.

[![Jumpers on breakout](https://cdn.sparkfun.com/assets/5/3/8/0/f/jumper-locations.jpg)](https://cdn.sparkfun.com/assets/5/3/8/0/f/jumper-locations.jpg)

*The three two-way jumpers on the back of the board. Follow the labels to see which pin they pull up.*

Each of these jumpers pulls a pair of pins up to VDD, through a 10kΩ resistor. The middle pad of the jumper connects to the resistor, and the edge pads connect to a pin (follow the labels to find out which one). You can see how those jumpers match up on the schematic:

[![Jumpers on schematic](https://cdn.sparkfun.com/r/600-600/assets/a/2/9/4/1/jumper-schematic.jpg)](https://cdn.sparkfun.com/assets/a/2/9/4/1/jumper-schematic.jpg)

The far-right jumper connects CSG and CSXM to a pull-up \-- this\'ll set the LSM9DS0 to I^2^C mode. The middle jumper pulls up SDOG and SDOXM, which sets the I^2^C address of the chip. Finally, the far-left jumper adds pull-up resistors to the I^2^C communication pins \-- SDA and SCL.

The intention of these jumpers is to make it as easy-as-possible to use the board; using as few wires as possible. If you\'re using the breakout with I^2^C, you can ignore the four SDO and CS pins.

To disable any of these jumpers, whip out your [handy hobby knife](https://www.sparkfun.com/products/9200), and carefully cut the small traces between middle pad and edge pads. Even if you\'re using SPI, though, the jumpers shouldn\'t hinder your ability to communicate with the chip.

------------------------------------------------------------------------

For more information about the breakout board, we encourage you to [check out the schematic](https://cdn.sparkfun.com/assets/8/c/c/4/9/lsm9ds0_breakout-v10-schematic-.pdf). Or, if you really want to delve into the anatomy of the PCB, you can [download the EAGLE files](https://cdn.sparkfun.com/assets/f/6/9/6/d/lsm9ds0-breakout-v10-EAGLE.zip).

## Hardware Assembly

On this page we\'ll discuss assembly hints. There\'s really not much to assembling the breakout board \-- the real key is [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) *something* into the breakout holes.

### Solder Something

To get a solid electrical and physical connection to the LSM9DS0 Breakout, you\'ll need to solder either connectors or wires to the break-out pins. What, exactly, you solder into the board depends on how you\'re going to use it.

If you\'re going to use the breakout board in a [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) or similar 0.1\"-spaced perfboard, we recommend soldering [straight male headers](https://www.sparkfun.com/products/116) into the pins (there are also [long headers](https://www.sparkfun.com/products/10158) if you need \'em).

[![Headers soldered into board](https://cdn.sparkfun.com/r/600-600/assets/7/f/d/5/e/headers-soldered.jpg)](https://cdn.sparkfun.com/assets/7/f/d/5/e/headers-soldered.jpg)

If you\'re going to mount the breakout into a tight place, you may want to opt for soldering wires ([stranded](https://www.sparkfun.com/products/11375) or [solid-core](https://www.sparkfun.com/products/11367)) into the pins.

### Mounting the Breakout

Because the LSM9DS0 senses motion, it\'s important (for most applications, at least) to keep in pinned in place. So the boards have a pair of mounting holes on the corners opposite the pins. The drill holes are 0.13\" in diameter, so they should accommodate any [4/40 screw](https://www.sparkfun.com/products/10453).

If you have any further dimension-related questions, hopefully the dimensional drawing below can answer them:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/c/d/f/1/e/PCB-dimensions.png)](https://cdn.sparkfun.com/assets/c/d/f/1/e/PCB-dimensions.png)

Consult the [EAGLE PCB design files](https://cdn.sparkfun.com/assets/f/6/9/6/d/lsm9ds0-breakout-v10-EAGLE.zip) to find out more about the Breakout\'s dimensions.

## Basic Arduino Example

This example will show you how to download and install the SFE_LSM9DS0 library, and use it in it\'s most basic form. We\'ll use I^2^C and ignore the interrupts, which means we\'ll be using as few wires and Arduino pins as possible.

### Download and Install the Library

We\'ve written a full-featured Arduino library to help make interfacing with the LSM9DS0\'s gyro and accelerometer/magnetometer as easy-as-possible. Visit the [GitHub repository](https://github.com/sparkfun/SparkFun_LSM9DS0_Arduino_Library) to download the most recent version of the library, or click the link below:

[Download the SFE_LSM9DS0 Arduino Library](https://github.com/sparkfun/SparkFun_LSM9DS0_Arduino_Library/archive/master.zip)

For help installing the library, check out our [How To Install An Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library). You\'ll need to move the *SFE_LSM9DS0* folder into a *libraries* folder within your Arduino sketchbook.

### Simple Hardware Hookup (I^2^C)

The library will work with either I^2^C or SPI. Since we\'re trying to be as frugal with our Arduino pins as possible, I^2^C it is! Here\'s a fritzing diagram for this example:

[![Redboard connected to LSM9DS0 via LLC](https://cdn.sparkfun.com/r/600-600/assets/1/5/9/9/9/simple-redboard_levelShift_bb.png)](https://cdn.sparkfun.com/assets/1/5/9/9/9/simple-redboard_levelShift_bb.png)

*Connecting the LSM9DS0 to a RedBoard via a [Bi-Directional Logic Level Converter](https://www.sparkfun.com/products/12009).*

This hookup relies on all of the **jumpers** on the back of the board being set (as they should be, unless they\'ve been sliced). If the jumpers have been disconnected, connect all four CS and SDO pins to 3.3V.

Since we\'re using I^2^C all we have to do is connect SDA to SDA and SCL to SCL. Unfortunately, since the LSM9DS0\'s **maximum operating voltage is 3.6V**, we need to use a [level shifting board](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide) to switch between 3.3V and 5V.

Alternatively, if you have a 3.3V-operating Arduino \-- like the [3.3V/8MHz Pro](https://www.sparkfun.com/products/10914) \-- you can connect SDA and SCL directly from microcontroller to sensor.

[![LSM9DS0 connected directly to Arduino Pro 3.3V](https://cdn.sparkfun.com/r/600-600/assets/9/8/9/2/b/simple-pro_bb.png)](https://cdn.sparkfun.com/assets/9/8/9/2/b/simple-pro_bb.png)

Heck, you can even mount the breakout board on top of the Arduino Pro. If you do this, you\'ll need to set A3 HIGH and A2 LOW. The sensor pulls little enough current that the Arduino\'s I/O pins can power it!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/4/0/8/3/b/lsm9ds0-on-arduino-pro.jpg)](https://cdn.sparkfun.com/assets/4/0/8/3/b/lsm9ds0-on-arduino-pro.jpg)

*The wireless hookup: mounting an LSM9DS0 on top of an Arduino Pro. Pull A2 LOW and A3 HIGH to power the breakout.*

### Open the LSM9DS0_Simple Example

Once you\'ve installed the library, open Arduino (or restart it if it was already open). You\'ll find this first example under the **File** \> **Examples** \> **SFE_LSM9DS0** \> **LSM9DS0_Simple**:

    language:c
    /*****************************************************************
    LSM9DS0_Simple.ino
    SFE_LSM9DS0 Library Simple Example Code
    Jim Lindblom @ SparkFun Electronics
    Original Creation Date: February 18, 2014
    https://github.com/sparkfun/LSM9DS0_Breakout

    The LSM9DS0 is a versatile 9DOF sensor. It has a built-in
    accelerometer, gyroscope, and magnetometer. Very cool! Plus it
    functions over either SPI or I2C.

    This Arduino sketch is a demo of the simple side of the
    SFE_LSM9DS0 library. It'll demo the following:
    * How to create a LSM9DS0 object, using a constructor (global
      variables section).
    * How to use the begin() function of the LSM9DS0 class.
    * How to read the gyroscope, accelerometer, and magnetometer
      using the readGryo(), readAccel(), readMag() functions and the
      gx, gy, gz, ax, ay, az, mx, my, and mz variables.
    * How to calculate actual acceleration, rotation speed, magnetic
      field strength using the calcAccel(), calcGyro() and calcMag()
      functions.
    * How to use the data from the LSM9DS0 to calculate orientation
      and heading.

    Hardware setup: This library supports communicating with the
    LSM9DS0 over either I2C or SPI. If you're using I2C, these are
    the only connections that need to be made:
        LSM9DS0 --------- Arduino
         SCL ---------- SCL (A5 on older 'Duinos')
         SDA ---------- SDA (A4 on older 'Duinos')
         VDD ------------- 3.3V
         GND ------------- GND
    (CSG, CSXM, SDOG, and SDOXM should all be pulled high jumpers on 
      the breakout board will do this for you.)

    If you're using SPI, here is an example hardware setup:
        LSM9DS0 --------- Arduino
              CSG -------------- 9
              CSXM ------------- 10
              SDOG ------------- 12
              SDOXM ------------ 12 (tied to SDOG)
              SCL -------------- 13
              SDA -------------- 11
              VDD -------------- 3.3V
              GND -------------- GND

    The LSM9DS0 has a maximum voltage of 3.6V. Make sure you power it
    off the 3.3V rail! And either use level shifters between SCL
    and SDA or just use a 3.3V Arduino Pro.   

    Development environment specifics:
        IDE: Arduino 1.0.5
        Hardware Platform: Arduino Pro 3.3V/8MHz
        LSM9DS0 Breakout Version: 1.0

    This code is beerware. If you see me (or any other SparkFun 
    employee) at the local, and you've found our code helpful, please 
    buy us a round!

    Distributed as-is; no warranty is given.
    *****************************************************************/

    // The SFE_LSM9DS0 requires both the SPI and Wire libraries.
    // Unfortunately, you'll need to include both in the Arduino
    // sketch, before including the SFE_LSM9DS0 library.
    #include <SPI.h> // Included for SFE_LSM9DS0 library
    #include <Wire.h>
    #include <SFE_LSM9DS0.h>

    ///////////////////////
    // Example I2C Setup //
    ///////////////////////
    // Comment out this section if you're using SPI
    // SDO_XM and SDO_G are both grounded, so our addresses are:
    #define LSM9DS0_XM  0x1D // Would be 0x1E if SDO_XM is LOW
    #define LSM9DS0_G   0x6B // Would be 0x6A if SDO_G is LOW
    // Create an instance of the LSM9DS0 library called `dof` the
    // parameters for this constructor are:
    // [SPI or I2C Mode declaration],[gyro I2C address],[xm I2C add.]
    LSM9DS0 dof(MODE_I2C, LSM9DS0_G, LSM9DS0_XM);

    ///////////////////////
    // Example SPI Setup //
    ///////////////////////
    /* // Uncomment this section if you're using SPI
    #define LSM9DS0_CSG  9  // CSG connected to Arduino pin 9
    #define LSM9DS0_CSXM 10 // CSXM connected to Arduino pin 10
    LSM9DS0 dof(MODE_SPI, LSM9DS0_CSG, LSM9DS0_CSXM);
    */

    // Do you want to print calculated values or raw ADC ticks read
    // from the sensor? Comment out ONE of the two #defines below
    // to pick:
    #define PRINT_CALCULATED
    //#define PRINT_RAW

    #define PRINT_SPEED 500 // 500 ms between prints

    void setup()
    

    void loop()
    

    void printGyro()
    

    void printAccel()
    

    void printMag()
    

    // Here's a fun function to calculate your heading, using Earth's
    // magnetic field.
    // It only works if the sensor is flat (z-axis normal to Earth).
    // Additionally, you may need to add or subtract a declination
    // angle to get the heading normalized to your location.
    // See: http://www.ngdc.noaa.gov/geomag/declination.shtml
    void printHeading(float hx, float hy)
    
      else if (hy < 0)
      
      else // hy = 0
      

      Serial.print("Heading: ");
      Serial.println(heading, 2);
    }

    // Another fun function that does calculations based on the
    // acclerometer data. This function will print your LSM9DS0's
    // orientation -- it's roll and pitch angles.
    void printOrientation(float x, float y, float z)
    

After uploading the code, open up your **serial monitor** and **set the baud rate to 115200 bps**. You should see something like this begin to stream by:

[![alt text](https://cdn.sparkfun.com/assets/3/9/7/1/5/serial_monitor-simple.png)](https://cdn.sparkfun.com/assets/3/9/7/1/5/serial_monitor-simple.png)

Each serial output blurb spits out the readings from all nine dimensions of movement. First the gyroscope readings (\"G: x, y, z\") in **degrees per second** (DPS). Then come three degrees of acceleration in ***g*\'s** (\"A: x, y, z\"), followed by the magnetic field readings (\"M: x, y, z\") in **gauss** (Gs).

Try moving your breadboard around (carefully, don\'t disconnect any wires!). Are the numbers changing? Check out the acceleration values \-- the axis normal to gravity should feel about 1 *g* of acceleration on it.

Does the **heading** output what you\'d expect? If north seems a few degrees off, you may need to adjust for your **declination**. That means adding or subtracting a constant number that correlates to your location on [this map](http://www.ngdc.noaa.gov/geomag/declination.shtml).

------------------------------------------------------------------------

That\'s all there is to it! If you want to get more out of the LSM9DS0 by using the interrupt outputs, check out the next page! Or check out the [Using the Arduino Library Page](./using-the-arduino-library) for help using the library.

## Advanced Arduino Example

The [basic example](./basic-arduino-example) is perfect if all you want to do is poll the LSM9DS0 a few times per second to get movement data, but what if you want to make use of the IMU\'s interrupt outputs? Using interrupts you can get read data in from the LSM9DS0 as soon as it\'s available. This example will show you how to get more out of your LSM9DS0 Breakout.

### Circuit Diagram

In addition to the SDA and SCL pins, this example will make use of the **DRDYG**, **INT1XM**, and **INT2XM** pins. Here\'s the hookup diagram:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/2/8/f/f/advanced-redboard_levelShift_bb.png)](https://cdn.sparkfun.com/assets/e/2/8/f/f/advanced-redboard_levelShift_bb.png)

Again, you\'ll need to use a logic level converter between SDAs and SCLs. There is no need for level shifting on the three interrupt lines \-- the 3.3V output from the LSM9DS0 will be enough to trigger a logic high on the Arduino (see [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)).

### Example Code: LSM9DS0_SerialMenus

Open up the *LSM9DS0_SerialMenus* example by going to **File** \> **Examples** \> **SFE_LSM9DS0** \> **LSM9DS0_SerialMenus**. Here\'s the code:

    language:c
    /*****************************************************************
    LSM9DS0_SerialMenus.ino
    SFE_LSM9DS0 Library Example Code: Interact With Serial Menus
    Jim Lindblom @ SparkFun Electronics
    Original Creation Date: February 14, 2014 (Happy Valentines Day!)
    https://github.com/sparkfun/LSM9DS0_Breakout

    This Arduino sketch is a demo of all things SEF_LSM9DS0 library.
    Once you attach all hardware, and upload the sketch, open your
    Serial monitor at 115200 BPS. Follow the menu prompts to either:
        1) Stream readings from the accelerometer.
        2) Stream readings from the gyroscope.
        3) Stream readings from the magnetometer.
        4) Set the scales of each sensor (e.g. +/-4g, 500DPS, 8Gs)
        5) Switch to/from calculated or raw data (e.g. ADC ticks or
            g's, DPS, and Gs)
        6) Set the output data rate of each sensor.

    Hardware setup: This library supports communicating with the
    LSM9DS0 over either I2C or SPI. In addition to those wires, this
    sketch demos how to use the interrupts. Here's what the I2C setup
    looks like:
        LSM9DS0 --------- Arduino
         CSG ------------- NONE (Pulled HIGH [indicates I2C mode])
         CSXM ------------ NONE (Pulled HIGH [indicates I2C mode])
         SDOG ------------ NONE (Pulled HIGH [sets I2C address])
         SDOXM ----------- NONE (Pulled HIGH [sets I2C address])
         SCL ---------- SCL (A5 on older 'Duinos')
         SDA ---------- SDA (A4 on older 'Duinos')
         VDD ------------- 3.3V
         GND ------------- GND
         DEN ------------- NONE (Not used in this example)
         INTG ------------ NONE (Not used in this example)
         DRDYG ------------ 4 (Could be any digital pin)
         INT1XM ----------- 3 (Could be any digital pin)
         INT2XM ----------- 2 (Could be any digital pin)

    The LSM9DS0 has a maximum voltage of 3.6V. Make sure you power it
    off the 3.3V rail! And either use level shifters between SCL
    and SDA or just use a 3.3V Arduino Pro.   

    Development environment specifics:
        IDE: Arduino 1.0.5
        Hardware Platform: Arduino Pro 3.3V/8MHz
        LSM9DS0 Breakout Version: 1.0

    This code is beerware; if you see me (or any other SparkFun 
    employee) at the local, and you've found our code helpful, please 
    buy us a round!

    Distributed as-is; no warranty is given.
    *****************************************************************/

    // The SFE_LSM9DS0 requires both the SPI and Wire libraries.
    // Unfortunately, you'll need to include both in the Arduino
    // sketch, before including the SFE_LSM9DS0 library.
    #include <SPI.h> // Included for SFE_LSM9DS0 library
    #include <Wire.h>
    #include <SFE_LSM9DS0.h>

    ///////////////////////
    // Example I2C Setup //
    ///////////////////////
    // SDO_XM and SDO_G are both grounded, therefore our addresses are:
    #define LSM9DS0_XM  0x1D // Would be 0x1E if SDO_XM is LOW
    #define LSM9DS0_G   0x6B // Would be 0x6A if SDO_G is LOW
    // Create an instance of the LSM9DS0 library called `dof` the
    // parameters for this constructor are:
    // [SPI or I2C Mode declaration], [gyro I2C address], [xm I2C address]
    LSM9DS0 dof(MODE_I2C, LSM9DS0_G, LSM9DS0_XM);

    ///////////////////////
    // Example SPI Setup //
    ///////////////////////
    //#define LSM9DS0_CSG  9  // CSG connected to Arduino pin 9
    //#define LSM9DS0_CSXM 10 // CSXM connected to Arduino pin 10
    //LSM9DS0 dof(MODE_SPI, LSM9DS0_CSG, LSM9DS0_CSXM);

    ///////////////////////////////
    // Interrupt Pin Definitions //
    ///////////////////////////////
    const byte INT1XM = 2; // INT1XM tells us when accel data is ready
    const byte INT2XM = 3; // INT2XM tells us when mag data is ready
    const byte DRDYG = 4;  // DRDYG tells us when gyro data is ready

    // A boolean to keep track of whether we're printing raw (ADC)
    // or calculated (g's, DPS, Gs) sensor data:
    boolean printRaw = true;

    void setup()
    

    void loop()
    

    void printAccel()
    
        else
        
      }
    }

    void printGyro()
    
        else
        
      }
    }

    void printMag()
    
        else
        
      }
    }

    // Here's a simple example function to calculate heading based on
    // magnetometer readings. This only works when the 9DOF is flat
    // (x-axis normal to gravity).
    float calcHeading(float hx, float hy, float hz)
    
      else if (hy < 0)
      
      else // hy = 0
      
    }

    // This function will print all data from all sensors at once.
    // It'll wait until every sensor interrupt triggers before
    // printing.
    void streamAll()
    
    }

    void setScale()
    

      Serial.println(F("Set gyroscope scale:"));
      Serial.println(F("\t1) +/- 245 DPS"));
      Serial.println(F("\t2) +/- 500 DPS"));
      Serial.println(F("\t3) +/- 2000 DPS"));
      while (Serial.available() < 1)
        ;
      c = Serial.read();
      switch (c)
      

      Serial.println(F("Set magnetometer scale:"));
      Serial.println(F("\t1) +/- 2GS"));
      Serial.println(F("\t2) +/- 4GS"));
      Serial.println(F("\t3) +/- 8GS"));
      Serial.println(F("\t4) +/- 12GS"));
      while (Serial.available() < 1)
        ;
      c = Serial.read();
      switch (c)
      
    }

    void setRaw()
    
      else
      
    }

    void setODR()
    

      Serial.println(F("Set Gyro ODR/Cutoff (Hz):"));
      Serial.println(F("\t1) 95/12.5 \t 8) 380/25"));
      Serial.println(F("\t2) 95/25   \t 9) 380/50"));
      Serial.println(F("\t3) 190/125 \t A) 380/100"));
      Serial.println(F("\t4) 190/25  \t B) 760/30"));
      Serial.println(F("\t5) 190/50  \t C) 760/35"));
      Serial.println(F("\t6) 190/70  \t D) 760/50"));
      Serial.println(F("\t7) 380/20  \t E) 760/100"));
      while (Serial.available() < 1)
        ;
      c = Serial.read();
      switch (c)
      

      Serial.println(F("Set Magnetometer ODR (Hz):"));
      Serial.println(F("\t1) 3.125 \t 4) 25"));
      Serial.println(F("\t2) 6.25  \t 5) 50"));
      Serial.println(F("\t3) 12.5  \t 6) 100"));
      while (Serial.available() < 1)
        ;
      c = Serial.read();
      switch (c)
      
    }

    void printMenu()
    

    void parseMenu(char c)
    
          break;
        case '5':
          setScale();
          break;
        case '6':
          setRaw();
          break;
        case '7':
          setODR();
          break;
      }
    }

Upload the code, then open up your serial monitor with the **baud rate set to 115200 bps**. Then just follow the menu prompts to interact with the sensor. You can stream the accelerometer, gyroscope, and magnetometer individually or together.

[![Serial menu interaction](https://cdn.sparkfun.com/assets/d/f/9/e/2/serialMenu-interaction.gif)](https://cdn.sparkfun.com/assets/d/f/9/e/2/serialMenu-interaction.gif)

Send any key to stop the streaming and bring the menu back.

There are also menu items that allow you to set the **range** and **data rates** of the sensors. Make sure you give those a spin, and see how they affect the output of the sensor.

## Using the Arduino Library

Those two basic and advanced tutorials show off everything that the SFE_LSM9DS0 library can do. If you\'re stumped on how to use the library, though, here are some of its key concepts and functions:

### Setup Stuff

To enable the library, you\'ll need to **include** it, and you also need to include the [SPI](http://arduino.cc/en/Reference/SPI) and [Wire](http://arduino.cc/en/reference/wire) libraries:

    language:c
    #include <SPI.h> // Included for SFE_LSM9DS0 library
    #include <Wire.h>
    #include <SFE_LSM9DS0.h>

Make sure the SPI and Wire includes are above the SFE_LSM9DS0.

#### Constructor

The constructor creates an instance of the LSM9DS0 class. Once you\'ve created the instance, that\'s what you\'ll use to control the breakout from there on. This single line of code is usually placed in the **global** area of your sketch.

The constructor tells the library three things: whether you\'re using I^2^C or SPI, and the addresses of the gyroscope and accelerometer/magnetomter sensors. If you\'re using I^2^C, those address are the 7-bit address defined in the datasheet

    language:c
    // SDO_XM and SDO_G are both grounded, so our addresses are:
    #define LSM9DS0_XM  0x1D // Would be 0x1E if SDO_XM is LOW
    #define LSM9DS0_G   0x6B // Would be 0x6A if SDO_G is LOW
    // Create an instance of the LSM9DS0 library called `dof` the
    // parameters for this constructor are:
    // [SPI or I2C Mode declaration],[gyro I2C address],[xm I2C add.]
    LSM9DS0 dof(MODE_I2C, LSM9DS0_G, LSM9DS0_XM);

*Declaring an LSM9DS0 object using I2C for communication.*

If you\'re using SPI, the gyro and accel/mag addresses should be the Arduino pin connected to each chip-select pin (CSG and CSXM).

    language:c
    #define LSM9DS0_CSG  9  // CSG connected to Arduino pin 9
    #define LSM9DS0_CSXM 10 // CSXM connected to Arduino pin 10
    LSM9DS0 dof(MODE_SPI, LSM9DS0_CSG, LSM9DS0_CSXM);

*Declaring an LSM9DS0 object using SPI for communication.*

Your LSM9DS0 class object can be named like any other variable. In our examples we called it *dof* \-- short and sweet.

#### begin()

Once you\'ve created an LSM9DS0 object, you can start using it! The first step is **initializing the sensor**, by using the `begin()` function. You can either call this function with no parameters, to get a good, default init:

    language:c
    // Initialize LSM9DS0, setting gyro scale to 245 DPS, accel to 2g, and mag to 2Gs.
    // Also set data rates to 95 Hz (gyro), 50 Hz (accel), and 50 Hz (mag).
    dof.begin();

Or, give it a whole set of parameters that set each sensors scale and data rate.

    language:c
    // Initialize LSM9DS0, setting gyro scale to 500 DPS, accel to +/-16g, and mag to 12Gs.
    // Also set data rates to 760 Hz (gyro), 1600 Hz (accel), and 100 Hz (mag) (lots of data!)
    dof.begin(G_SCALE_500DPS, A_SCALE_16G, M_SCALE_12GS, G_ODR_760_BW_100, A_ODR_1600, M_ODR_100);

There are a variety of options for the scale and data rate selections. Consult [SFE_LSM9DS0.h](https://github.com/sparkfun/LSM9DS0_Breakout/blob/master/Libraries/Arduino/SFE_LSM9DS0/SFE_LSM9DS0.h) to find out more.

### Reading and Interpreting the Sensors

What good is the sensor if you can\'t get any data from it!? Here are the functions you\'ll need to get acceleration, rotation speed, and magnetic field strength dat from the library.

#### readAccel(), readGyro(), and readMag()

These three functions \-- `readAccel()`, `readGyro()`, and `readMag()` \-- poll the LSM9DS0 to get the most up-to-date readings from each of the three sensors.

The read functions don\'t take any parameters, and they don\'t return anything, so how do you get that data? After the function runs its course, it\'ll update a set of **three class variables**, which will have the sensor data you so desire. `readAccel()` will update `ax`, `ay`, and `az`, `readGyro()` will update `gx`, `gy`, and `gz`, and `readMag()` will update `mx`, `my`, and `mz`. Here\'s an example:

    language:c
    dof.readAccel(); // Update the accelerometer data
    Serial.print(dof.ax); // Print x-axis data
    Serial.print(", ");
    Serial.print(dof.ay); // print y-axis data
    Serial.print(", ");
    Serial.println(dof.az); // print z-axis data

*An example of reading and printing all three axes of accelerometer data.*

Those values are all **signed 16-bit integers**, meaning they\'ll range from -32,768 to 32,767. That value doesn\'t mean much unless you know the scale of your sensor, which is where the next functions come into play.

#### calcAccel(), calcGyro(), and calcMag()

The library keeps track of each sensor\'s scale, and it implements these helper functions to make translating between the raw ADC readings of the sensor to actual units easy.

`calcAccel()`, `calcGyro()`, and `calcMag()` all take a single parameter \-- a signed 16-bit integer \-- and convert to their respective units. They all **return a float value**, which you can do with as you please.

Here\'s an example of printing calculated gyroscope values:

    language:c
    dof.readGyro(); // Update gyroscope data
    Serial.print(dof.calcGyro(dof.gx)); // Print x-axis rotation in DPS
    Serial.print(", ");
    Serial.print(dof.calcGyro(dof.gy)); // Print y-axis rotation in DPS
    Serial.print(", ");
    Serial.println(dof.calcGyro(dof.gz)); // Print z-axis rotation in DPS

------------------------------------------------------------------------

The library also implements functions to individually set a sensor\'s scale or data rate. For more help using the library, check out comments in the example code, or [delve into the library code itself](https://github.com/sparkfun/LSM9DS0_Breakout/tree/master/Libraries/Arduino/SFE_LSM9DS0).