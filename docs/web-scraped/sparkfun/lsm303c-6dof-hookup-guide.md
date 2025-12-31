# Source: https://learn.sparkfun.com/tutorials/lsm303c-6dof-hookup-guide

## Introduction

The [LSM303C](https://www.sparkfun.com/products/13303) is a 6 **d**egrees **o**f **f**reedom (6DOF) **i**nertial **m**easurement **u**nit (IMU) in a sigle package. It houses a 3-axis [accelerometer](https://learn.sparkfun.com/tutorials/accelerometer-basics), and a 3-axis [magnetometer](https://www.google.com/search?q=magnetometer&ie=utf-8&oe=utf-8). The range of each sensor is configurable: the accelerometer\'s scale can be set to ±2g, ±4g, ±6g, or ±8g, and the magnetometer has full-scale range of ±16 gauss.

[![SparkFun 6 Degrees of Freedom Breakout - LSM303C](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/6/4/13303-01.jpg)](https://www.sparkfun.com/products/13303)

### [SparkFun 6 Degrees of Freedom Breakout - LSM303C](https://www.sparkfun.com/products/13303) 

[ BOB-13303 ]

The LSM303C is a 6 Degrees of Freedom (6DOF) inertial measurement unit (IMU) in a single package, specifically developed as a...

**Retired**

The LSM303C supports [I^2^C](https://learn.sparkfun.com/tutorials/i2c) and [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi). This tutorial focuses on using this device in I^2^C mode, but will briefly describe how to use SPI.

### Covered In This Tutorial

First we\'ll introduce you to the breakout board. Then we\'ll switch over to example code and show you how to interface with the board using an Arduino and our [SparkFun LSM303C 6 DOF IMU Breakout Arduino Library](https://github.com/sparkfun/SparkFun_LSM303C_6_DOF_IMU_Breakout_Arduino_Library).

The tutorial is split into the following sections:

- [Breakout Board Overview](#hardware-overview) \-- This page examines the LSM303C Breakout Board \-- topics like the pinout, jumpers, and schematic are covered.
- [Hardware Assembly](#hardware-assembly) \-- How to assemble the hardware to run some example code.
- [Installing the Arduino Library](#installing-the-arduino-library) \-- How to install the Arduino library, and use a simple example sketch to verify that your hookup works.
- [Resources & Going Further](#resources--going-further) \-- Resources for learning and doing more with the LSM303C.

### Required Materials

This tutorial explains how to use the LSM303C Breakout Board with an Arduino. To follow along, you\'ll need the following materials:

**The LSM303C is a 2.5V device!** Supplying voltages greater than 4.8V can permanently damage the IC. InvenSense recommends running from **1.9V to 3.6V**. As long as your Arduino has a 3.3V supply output, you shouldn\'t need any extra level shifting. See our [logic level tutorial](tutorials/62) for more info if you aren\'t using a 3.3V system.

### Suggested Reading

If you\'re not familiar with some of the concepts below, we recommend checking out that tutorial before continuing on.

[](https://learn.sparkfun.com/tutorials/pull-up-resistors)

### Pull-up Resistors 

A quick introduction to pull-up resistors - whey they\'re important, and how/when to use them.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

### The Pinout

The LSM303C 6 DOF Breakout has 10 plated through hole connections.

[![LSM303C BOB top view](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/8/Straight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/8/Straight.jpg)

*Top View of LSM303C Breakout Board*

The following table summarizes all of the plated through hole connections on the breakout board:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Pin Label               Pin Function                          Notes
  ----------------------- ------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **GND**                 Ground reference                      +0V

  **VDD_IO**              Power supply for I/O pins             1.71V up to VDD + 0.1V

  **SDA/\                 I^2^C serial data\                    ST calls the second serial interface SPI, but it\'s really a half-duplex variant that uses the same pin for MISO and for MOSI. Note that all 3 data signals are the same pin.
  SDI/\                   SPI serial data input\                
  SDO**                   3-wire interface serial data output   

  **SCL/\                 I^2^C serial clock\                   100 or 400 kHz I^2^C\
  SCLK**                  SPI serial port clock                 Up to 10 MHz SPI

  **INT_XL**              Accelerometer interrupt signal        The functions, the threshold and the timing of this interrupt are configurable.

  **DRDY**                Data ready                            Configurable output to indicate when accelerometer or magnetometer data is ready.

  **CS_XL**               Accelerometer: SPI enable\            1: SPI idle mode / I2C communication enabled;\
                          I^2^C/SPI mode selection              0: SPI communication mode / I^2^C disabled

  **VDD**                 Power supply                          1.9V to 3.6V

  **CS_MAG**              Magnetometer: SPI enable\             1: SPI idle mode / I2C communication enabled;\
                          I^2^C/SPI mode selection              0: SPI communication mode / I2C disabled

  **INT_MAG**             Magnetometer interrupt signal         The functions, the threshold and the timing of this interrupt are configurable.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Power Supply

The LSM303C breakout has three power supply plated thru-hole connections: a 0V reference (**GND**), a core supply (**VDD**), and an IO supply (**VDD_IO**). The core of the IC can be powered from **1.9-3.6V**. The IO must be given a potential of at least 1.71V up to the core supply voltage plus 0.1V. This dual supply setup eliminates the need for external voltage level translation. A 3.3V rail can power most of the device while still being able to communicate with a 1.8V processor without drawing all of its power from that lower voltage rail.

### Communication

The LSM303C communicates over I^2^C or \'SPI\' using the same plated thru-hole connections. The implementation of \'SPI\' on the LSM303C isn\'t standard; it\'s a half-duplex variant. Standard SPI has a MOSI and a MISO signal. Both of these are found on the single SDA/SDI/SDO connection. The more common Arduino variants don\'t have hardware that directly supports this, so we are bit banging in our library. Your system may be compatible, so we didn\'t add external components to get the hardware to work with the Atmel SPI hardware. This connection is also used as the SDA connection for I^2^C. Testing showed that the implementation of this IO acts like an open-drain like is common with I^2^C. This means that a pull-up resistor is needed for both SPI and I^2^C. The breakout includes this pull-up. Both communication modes share the same clock line (SCL/SCLK).

The LSM303C is implemented as two separate cores on the same die. The accelerometer and magnetometer have their own chip select lines. In I^2^C mode, they have their own unique addresses. The accelerometer is at **0x1D**, and the magnetometer is at **0x1E**.

### Interrupts

There are a variety of interrupts on the LSM303C. The system can be configured to generate an interrupt signal for free-fall, motion detection and magnetic field detection. The actual function of the two interrupt pins (INT_XL & INT_MAG) are highly configurable through either the I^2^C or SPI interfaces. They can be active high or low, latching or non-latching, etc. This advanced topic won\'t be covered in this hookup guide. Please reference the [datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/8/DM00089896.pdf) for more information.

### The Jumper

In many cases, especially Arduino related, you won\'t have multiple lower voltage rails. For these cases we\'ve included SJ2. Your board comes with this jumper closed with a trace by default. This connects VDD_IO and VDD.

[![VDD & VDD_IO jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/8/Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/8/Jumper.jpg)

*Closeup of voltage jumper*

The intention of this jumper is to allow the end user to power use the board and begin developing right out of the box. To disable any of these jumpers, whip out your [handy hobby knife](https://www.sparkfun.com/products/9200), and carefully cut the small traces between the two pads. You may then connect VDD_IO to whatever power rial you desire.

## Hardware Assembly

### I^2^C Example

The basic use case for the LSM303C requires 4 connections to the µController or µProcessor; power, ground, I^2^C clock and data. The following images shows how we used a [SparkFun FTDI Basic Breakout](https://www.sparkfun.com/products/9873), and an [3.3V Arduino Pro Mini](https://www.sparkfun.com/products/11114) to power and interface to a [LSM303C 6 DOF Breakout board](https://www.sparkfun.com/products/13303).

[![LSM303C and Arduino Mini](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/8/LSM303C_IIC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/8/LSM303C_IIC.jpg)

*An LSM303C wired up to and Arduino Pro Mini for the MinimalistExample (IIC)*

Make connections to the breakout anyway that makes you happy. The board in the above photo has a [straight header](https://www.sparkfun.com/products/116) soldered to it. We could have used a right angle header, or wire, etc. **Please note that different mounting orientations will alter the orientation of the axes.** Make sure your code matches the physical orientation for your projects.

For this demo, we made the following connections:

  Arduino Pro Mini   LSM303C Breakout   Notes
  ------------------ ------------------ ---------------------------------
  VCC                VDD                +3.3V
  GND                GND                +0V
  SDA                SDA/SDI/SDO        Serial data @ +3.3V CMOS logic
  SCL                SCL/SCLK           Serial clock @ +3.3V CMOS logic

The whole system in our testing was powered via USB through the FTDI basic.

[![USB to FTDI to Pro Mini to I2C LSM303C Breakout Fritzing diagram](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/8/I2Cdrop.svg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/8/I2Cdrop.svg)

*Electrical connections for demo*

### SPI Example

Four hardware changes need to be made to interface the sensor using SPI. Move the SDA/SDI/SDO connection from SDA on the Arduino Pro Mini to digital pin 10, move the SCK/SCLK connection from SCL on the Arduino Pro Mini to digital pin 11, and add the two chip select lines.

  Arduino Pro Mini   LSM303C Breakout   Notes
  ------------------ ------------------ ----------------------------------------------
  VCC                VDD                +3.3V
  GND                GND                +0V
  Digital 10         SDA/SDI/SDO        Serial data @ +3.3V CMOS logic
  Digital 11         SCL/SCLK           Serial clock @ +3.3V CMOS logic
  Digital 12         CS_XL              Accelerometer chip select @ +3.3V CMOS logic
  Digital 13         CS_MAG             Magnetometer chip select @ +3.3V CMOS logic

[![SPI Hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/8/LSM303C_SPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/8/LSM303C_SPI.jpg)

*Example of a Pro Mini wired up for SPI*

\
[![USB to FTDI to Pro Mini to SPI LSM303C Breakout Fritzing diagram](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/8/SPIdrop.svg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/8/SPIdrop.svg)

*Connecting for SPI interface*

## Installing the Arduino Library

### Download and Install the Library

**Note:** This code/library has been written and tested on Arduino IDE version 1.8.9. Otherwise, make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Visit the [GitHub repository](https://github.com/sparkfun/SparkFun_LSM303C_6_DOF_IMU_Breakout_Arduino_Library) to download the most recent version of the libraries, or click the link below to manually install:

[Download the LSM303C Arduino Libraries (ZIP)](https://github.com/sparkfun/SparkFun_LSM303C_6_DOF_IMU_Breakout_Arduino_Library/archive/master.zip)

The example Arduino code allows you to do things like read the magnetometer in all 3 axis, read the accelerometer in all 3 axis, and read the temperature of the die in Fahrenheit and Celsius.

### Minimalist Example

Now, you can now run the example sketches. Open **File** ⇒ **Examples** ⇒ **SparkFun LSM303C 6 DOF IMU Breakout Arduino Library** ⇒ **MinimalistExample**. This sketch is a simple as possible other than a little error checking. We\'ll be using the example in I^2^C mode.

The setup function configures the [Arduino\'s serial port](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) to **57600 baud** and configures the LSM303C to some reasonable defaults.

``` 

LSM303C myIMU;

void setup() 
}
```

The loop function sequentially prints out the x, y, and z vales measured by the accelerometer, then the gyroscope, and then the magnetometer. This is followed up by the temperature of the die in degrees Celsius and Fahrenheit. All values are rounded to 4 digits past the decimal point.

``` 

void loop()

```

Here is some sample output:

``` 

Accelerometer:
 X = 56.7017
 Y = 42.7856
 Z = 946.2891

Gyroscope:
 X = nan
 Y = nan
 Z = nan

Magnetometer:
 X = -0.2051
 Y = 0.0527
 Z = 0.0742

Thermometer:
 Degrees C = 24.5000
 Degrees F = 76.1000
```

You may have noticed that gyro data is printed despite there not being a gyro on this board. If a value is not available, the library functions will return nan ([not a number](https://en.wikipedia.org/wiki/NaN)). In this case the LSM303C doesn\'t have a gyroscope, but it still returns a value for a consistent IMU interface. Any IMU library that implements the SparkFunIMU abstract class can be swapped out without having to change the code that uses the library. If at some point in the future it is determined that a project needs more or less degrees of freedom (and is coded with error checking) the code change is trivial. Change `#include "SparkFunLSM303C.h"` to `#include "SparkFun<some other sensor>.h"`, and `LSM303C myIMU;` to `<some other sensor> myIMU`. If for whatever reason the sensor doesn\'t have valid data ready for a sensor that does exist, it will also return nan. This indicates that the value is undefined.

### Configure Example

By default, the easy to configure example is configured exactly the same as the minimalist example. We\'ll be using the example in I^2^C mode. Here is the code that differentiates the two examples, the setup:

``` 

void setup() 
}
```

#### Configuring for SPI Mode

This setup function exposes all of the configuration options necessary to read the magnetometer and accelerometer. See the datasheet for more advanced configuration. To change a configuration option, uncomment the desired option in that section, and remove or comment out all other options in that section. For example, if you wanted to use the SPI interface, you would change that section to look like the following.

``` 

  ///// Interface mode options
    MODE_SPI,
    //MODE_I2C,
```

After uploading the sketch, open the serial monitor or your favorite terminal emulator and you should start seeing something similar to the following repeating over and over once per second.

``` 

Accelerometer:
 X = 64.5752
 Y = 31.4941
 Z = 943.1152

Magnetometer:
 X = -0.2085
 Y = 0.0425
 Z = 0.0972

Thermometer:
 Degrees C = 25.3750
 Degrees F = 77.6750
```

In the setup that this data capture came from, the breakout board was sitting roughly flat on a desk. This orients the z-axis parallel to the earths gravitational field of 1,000 mg. This is seen by the z-axis value of around 943. If the LSM303C were in free fall, the z-axis component would be 0 g, because it wouldn\'t be accelerating. Since the sensor isn\'t in free fall, it is measuring an effective acceleration of 1 g in the positive z direction up out of the table.

## More Library Details

### Common IMU Interface

This library does the C++ \'equivalent\' of implementing a common interface or template. It does this by implementing the pure virtual methods of the **SparkFunIMU** class. This strays from the pure definition of an abstract because not all of the methods are purely virtual. We\'ve strayed from this to give unimplemented methods a default behavior. *In less technical terms*, we\'ve provided a common set of basic functions that any IMU should have.

``` 

virtual float readGyroX()  
virtual float readGyroY()  
virtual float readGyroZ()  
virtual float readAccelX() 
virtual float readAccelY() 
virtual float readAccelZ() 
virtual float readMagX()   
virtual float readMagY()   
virtual float readMagZ()   
virtual float readTempC()  
virtual float readTempF()  
```

The LSM303C provides useful definitions for all of these methods except for the ones that read the gyroscope, since the LSM303C doesn\'t have a gyroscope. If you were to call `readGyroX()`, the default definition would be used, and it would return **N**ot **A** **N**umber (NAN). This is useful because, if you write your code to use these functions and later decide to use a different IMU that also implements this interface, you only have to change a few words, and all of the code will work with the new sensor.

### LSM303C Types

This library is written a little to the computer science object-oriented, encapsulation-type safety side, and a little less to the code size or speed optimized side. To provide type safety and improve readability, **LSM303CTypes.h** was written. In this header file, many types are defined, all registers are defined to types with descriptive names. As are all of the values you might want to write to the registers. Here is a simple example:

``` 

typedef enum
 I2C_ADDR_t
```

The first *keyword* there, `typedef`, is used in C and C++ to define more complex types out of existing types. In this case a type named `I2C_ADDR_t` is defined to be an enumeration with the `enum` keyword. An enumeration is a list of explicitly named integral type constants. They are guarenteed to be a variable large enough to hold an `int` type, but what they really are depends on the compiler. For **avr-gcc** there are compiler switches that can change the actual value used. In this case there are two valid values for a variable of type `I2C_ADDR_t`; `ACC_I2C_ADDR` and `MAG_I2C_ADDR`. `ACC_I2C_ADDR` is short for \"accelerometer (Inter-Integrated Circuit (I^2^C) address\". Arduino will interrpret that value to be `0x1D`.

Consider the following two function prototypes:

``` 

uint8_t  I2C_ByteWrite(I2C_ADDR_t, uint8_t, uint8_t);
uint8_t  I2C_ByteWrite(int, uint8_t, uint8_t);
```

Both versions of that function are capable of accepting the values `0x1D` and `0x1E`. The main difference is that the first prototype is type safe. The first parameter has to be of type `I2C_ADDR_t`. This type only has two valid values, `ACC_I2C_ADDR` and `ACC_I2C_ADDR`. If you try and pass any other value without explicitly casting it your code won\'t compile. You cannot make a mistake that can be loaded onto your Arduino. The avr-gcc toolchain that comes with the Arduino IDE will not let you make that mistake.

The first parameter of the second function prototype can be any `int`, including the values `0x1D` and `0x1E`, but not limited to those valid values. Sure your code could handle unexpected values, but what should it do about it? Strobe out an error message in Morse code on an LED? Lock up? This type unsafe code can allow runtime errors to get onto your microcontroller and cause strange bugs. The configure example was designed to show all of the common options, so referencing this header isn\'t typically needed. The extra complexity is 'hidden' away where you only see it if you go looking for it.

### Debug Macros

Also in the library is a header file named **DebugMacros.h**. As the name suggests this files contains the definitions of 4 macro functions used for debugging. This is a very simple tool hacked together for the use in developing this library, but is useful none the less. They don\'t follow the GNU coding style (case), so they blend in more like standard functions in an attempt to hide the complexity from the beginner programmer.

  --------------------------------------------------------------------------------------------------------------------------------
  Prototype                           Description
  ----------------------------------- --------------------------------------------------------------------------------------------
  debug_print(msg, \...)              Prints a labeled debug message to the serial monitor.\
                                      This macro function prepends the name of function & \'::\' to what Serial.print would do.\
                                      E.g. loop::Debug message

  debug_prints(msg, \...)             Very similar to the above function except it\'s shorter. No function label here.\
                                      Basically the same function as Serial.print().

  debug_println(msg, \...)            Very similar to the first macro function except it appends a newline character.

  debug_printlns(msg, \...)           Basically Serial.println(). No function label here.
  --------------------------------------------------------------------------------------------------------------------------------

These macro functions have a few advantages over the built in serial printing functions. The first is that all you have to do is change a single character to turn all of your debug statements on or off. They will be completely removed from the compiled code if turned off. This is done by defining `DEBUG` to be `1` (or non-zero) to enable the debug output. If `DEBUG` is defined to be `0`, all of the debug_print\<options\> statements will be removed from the code by the preprocessor before compilation. The place to define the `DEBUG` macro is at the top of **SparkFunLSM303C.cpp**.

Another useful trick they can be used for is generating something similar to a stack trace. To do this, simply add `debug_print(EMPTY);` to each function. Pretend that there are a bunch of functions defined. Here is a stripped down code example:

``` 

void loop()

void level_1_funct(void)

void level_2_funct(void)

```

Running the sketch containing this code would produce the following output:

`loop::level_1_funct::level_2_funct::Example error message`

Along with the message saying what went wrong the code provides an in order list of all of the functions that called it. This is helpful for tracing back where the error occurred. It tells all of the recent functions involved. This isn\'t as useful as a real stack trace, but it\'s worth the 20 lines of code.