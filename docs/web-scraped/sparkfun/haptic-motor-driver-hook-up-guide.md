# Source: https://learn.sparkfun.com/tutorials/haptic-motor-driver-hook-up-guide

## Introducing the Haptic Motor Driver 

Ready to add some good vibes to your project? Look no further than the [Haptic Motor Driver](https://www.sparkfun.com/products/14538). This board breaks out Texas Instruments\' DRV2605L haptic motor driver, which has some seriously cool features. Add meaningful feedback from your devices using the Haptic Motor Driver and an Arduino compatible device. This tutorial will get you up and running, or vibing, in no time with the I^2^C library for Arduino and example projects that give you the hardware setup and the code for various modes of operation.

[![SparkFun Haptic Motor Driver - DRV2605L](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/5/5/14538-SparkFun_Haptic_Motor_Driver-DRV2605L-01.jpg)](https://www.sparkfun.com/sparkfun-haptic-motor-driver-drv2605l.html)

### [SparkFun Haptic Motor Driver - DRV2605L](https://www.sparkfun.com/sparkfun-haptic-motor-driver-drv2605l.html) 

[ ROB-14538 ]

Ready to add some good vibes to your project? Look no further than the SparkFun Haptic Motor Driver. This board breaks out Te...

[ [\$11.95] ]

### Features

- Flexible Haptic and Vibration Driver for both ERM and LRA type motors
- I^2^C Controlled Digital Playback Engine
- Audio to Vibe
- PWM input with 0% to 100% Duty-Cycle Control Range
- Hardware Trigger Input
- Built-in Waveform Sequencer and Trigger

And that is just to name a few. See the [DRV2605L datasheet](https://cdn.sparkfun.com/datasheets/Robotics/drv2605l.pdf) for a complete list.

### Required Materials

You\'ll need a handful of extra parts to get the Haptic Motor Driver up-and-running. Below are the basic components used in this tutorial, if you want to follow along.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Vibration Motor](https://cdn.sparkfun.com/r/140-140/assets/parts/8/8/6/VibrationMotor-01-L.jpg)](https://www.sparkfun.com/vibration-motor.html)

### [Vibration Motor](https://www.sparkfun.com/vibration-motor.html) 

[ ROB-08449 ]

A vibration motor! This itty-bitty, shaftless vibratory motor is perfect for non-audible indicators. Use in any number of app...

[ [\$2.95] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

[![SparkFun Cerberus USB Cable - 6ft](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/3/9/12016-01.jpg)](https://www.sparkfun.com/products/12016)

### [SparkFun Cerberus USB Cable - 6ft](https://www.sparkfun.com/products/12016) 

[ CAB-12016 ]

You\'ve got the wrong USB cable. It doesn\'t matter which one you have, it\'s the wrong one. But what if you could have the righ...

**Retired**

A microcontroller that supports [I^2^C](https://learn.sparkfun.com/tutorials/i2c) is required to communicate with the DRV2605L and relay the data to the user by means of vibration. The [SparkFun RedBoard](https://www.sparkfun.com/products/12757) or [Arduino Uno](https://www.sparkfun.com/products/11021) are popular options for this role, but just about any microcontroller development board should work. (The firmware examples use an Arduino library, if that serves as any extra motivation to use an Arduino.)

[![Arduino Pro Mini 328 - 5V/16MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/3/9/11113-01b.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html)

### [Arduino Pro Mini 328 - 5V/16MHz](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html) 

[ DEV-11113 ]

SparkFun\'s minimal design approach to Arduino. This is a 5V Arduino running the 16MHz bootloader.

[ [\$11.25] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![SparkFun SAMD21 Mini Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/9/2/13664-01.jpg)](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html)

### [SparkFun SAMD21 Mini Breakout](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html) 

[ DEV-13664 ]

If you're ready to step your Arduino game up from older 8-bit/16MHz microcontrollers, the SparkFun SAMD21 Mini Breakout is ...

[ [\$24.95] ]

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

### Suggested Reading

The DRV2605L is designed for a handful of uses. The [Technical Documents](http://www.ti.com/product/DRV2605L/technicaldocuments) provided by Texas Instruments includes application notes, user guides, literature and blogs. The DRV2605L communicates over I^2^C. We've got a great library to make it easy to use. We're going to be using a breadboard to connect the breakout board to the RedBoard. If these subjects sound foreign to you consider browsing through these tutorials before continuing on.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview 

[![Haptic Motor Driver](https://cdn.sparkfun.com/assets/parts/1/1/8/4/7/14031-03.jpg)](https://cdn.sparkfun.com/assets/parts/1/1/8/4/7/14031-03.jpg)

### Parametrics

Parameter

Description

Min-Max Source Voltage

**2V - 5.2V.**

Special Features

Integrated Haptic Effects & Smart Loop Architecture.

Input Signal

PWM, Analog, I^2^C.

Maximum Output Voltage

10.4V.

Haptic Actuator Type

ERM & LRA type motors only.

Shut Down Current

4uA.

Quiescent Current

0.5mA - Important for your battery powered projects.

\

### Pin Descriptions

The SparkFun Haptic Motor Driver - DRV2605L breakout board provides 6 pins to provide power to the sensor and I^2^C bus.

[![Back of Haptic Motor Driver Breakout](https://cdn.sparkfun.com/assets/parts/1/1/8/4/7/14031-04.jpg)](https://cdn.sparkfun.com/assets/parts/1/1/8/4/7/14031-04.jpg)

Pin Label

Description

GND

Connect to ground.

VCC

Used to power the DRV2605L Haptic Motor Driver. Must be between 2.0 - 5.2V

SDA

I^2^C data

SCL

I^2^C clock

IN

Analog and PWM signal input

EN

Enable pin. Connect to VCC for most applications.

O-

Negative motor terminal.

O+

Positive motor terminal.

\

### Setting the Jumpers

On the front of the breakout board is a solder jumper:

- **I2C PU** \-- This is a 3-way solder jumper that is used to connect and disconnect the I^2^C pullup resistors. By default, this jumper is **closed**, which means that both SDA and SCL lines have connected pullup resistors on the breakout board. Use some [solder wick](https://www.sparkfun.com/products/9327) to open the jumper if you do not need the pullup resistors (e.g. you have pullup resistors that are located on the I^2^C bus somewhere else).

## ERM and LRA Motors

The DRV2605L is capable to driving two different types of motors. So what are they? How do they work? How are they different?

[Precision Microdrives](https://www.precisionmicrodrives.com/) published application notes on using both [Eccentric Rotating Mass, ERM](https://www.precisionmicrodrives.com/application-notes/ab-004-understanding-erm-vibration-motor-characteristics) and [Linear Resonant Actuator, LRA](https://www.precisionmicrodrives.com/application-notes/ab-020-understanding-linear-resonant-actuator-characteristics) type motors. The default firmware for the DRV2605L is set for use with ERM type motors. There are six effects libraries for the ERM type and only one for LRA.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/5/Capture2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/5/Capture2.PNG)

*Photo courtesy of https://www.precisionmicrodrives.com/*

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/5/Capture3.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/5/Capture3.PNG)

*Photo courtesy of https://www.precisionmicrodrives.com/*

The difference between the two motors is how the movement of a mass is displaced. LRA vibration motors require an AC signal, driving a sine waveform that is modulated to get multiple effects. ERM vibration motors use a DC motor with a counter weight attached. The DC voltage controls the speed of the motor.

> The ERM has an off-centre load, when it rotates the centripetal force causes the motor to move. The rotation is created by applying a current to the armature windings attached to the motor shaft. As these are inside a magnetic field created by the permanent magnets on the inside of the motor's body, a force is created causing the shaft to rotate. To ensure the rotation continues in the same direction, the current in the windings is reversed. This is achieved by using static metal brushes at the motor terminals, which connect to a commutator that rotates with the shaft and windings. The different segments of the commutator connect to the brushes during rotation and the current is reversed, maintaining the direction of rotation.
>
> In a similar method, LRAs use magnetic fields and electrical currents to create a force. One major difference is the voice coil (equivalent of the armature windings) remains stationary and the magnetic mass moves instead. The mass is also attached to a spring, which helps it return to the centre. Driving the magnetic mass up and down causes the displacement of the LRA and thereby the vibration force.^[1](#footnote)^

### **More Suggested Reading**

- [ERM Vibration Motors](https://www.precisionmicrodrives.com/application-notes/ab-004-understanding-erm-vibration-motor-characteristics)
- [LRA Vibration Motors](https://www.precisionmicrodrives.com/vibration-motors/linear-resonant-actuators-lras)
- [Haptics](http://www.ti.com/lit/ml/sszb151/sszb151.pdf)
- [Solutions for Haptics](http://www.nfpmotor.com/The%20Differences%20Between%20ERM%20and%20LRA%20Actuators.pdf)
- [How Devices Provide Haptic Feedback](https://blog.somaticlabs.io/how-devices-provide-haptic-feedback/)

[1]: \"AB-020 : UNDERSTANDING LINEAR RESONANT ACTUATOR CHARACTERISTICS.\" Application Note. Https://www.precisionmicrodrives.com. N.p., n.d. Web. 29 Nov. 2016.

## Using the SparFun DRV2605L Library

To use the SparkFun Haptic Motor Driver, you will need some supporting software. If you use Arduino, then you are in luck! We created an Arduino Library that makes the DRV2605L easy to use. To automatically install the library from the Arduino IDE simply navigate to **Sketch** \> **Include Library** \> **Manage Libraries\...** and search for **SparkFun Haptic Motor Driver**. Or you can grap the zip here from the GitHub repository to manually install:

[SparkFun Haptic Motor Driver Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Haptic_Motor_Driver_Arduino_Library/archive/refs/heads/master.zip)

The SparkFun DRV2605L library has every register defined, and simple functions can be called to create a custom haptic experience. Every register must be set (or use the default if that works for you). Use the [datasheet](https://cdn.sparkfun.com/datasheets/Robotics/drv2605l.pdf) to help you with the values that need to be written to the registers.

Going through the library header file, you\'ll see just about every register has a comment with its function and corresponding page number in the data sheet. This board is capable of operating in seven modes and can use either an LRA or ERM type motors. We will explore 2 of the modes \-- Internal Trigger mode, and PWM mode. From here it shouldn\'t take much to get the device working in other modes.

Let\'s explore each example in detail.

## Internal Trigger Mode

The internal trigger mode allows you to play a waveform or a custom waveform sequence from the ROM waveform memory. In this example we will play all 123 waveform effects by loading them in all eight waveform sequencer registers. This simple sketch will also help you become familiar with the effects library so you can start to build your own custom effects sequences. See page 60 of the [datasheet](http://www.ti.com/lit/ds/symlink/drv2605l.pdf) for the full list of waveform effects. Each library \-- listed on page 14 of the datasheet \-- has its own rated voltage, rise-time and brake-time.

### Parts Needed

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![SparkFun Haptic Motor Driver - DRV2605L](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/6/5/5/14538-SparkFun_Haptic_Motor_Driver-DRV2605L-01.jpg)](https://www.sparkfun.com/sparkfun-haptic-motor-driver-drv2605l.html)

### [SparkFun Haptic Motor Driver - DRV2605L](https://www.sparkfun.com/sparkfun-haptic-motor-driver-drv2605l.html) 

[ ROB-14538 ]

Ready to add some good vibes to your project? Look no further than the SparkFun Haptic Motor Driver. This board breaks out Te...

[ [\$11.95] ]

[![Vibration Motor](https://cdn.sparkfun.com/r/140-140/assets/parts/8/8/6/VibrationMotor-01-L.jpg)](https://www.sparkfun.com/vibration-motor.html)

### [Vibration Motor](https://www.sparkfun.com/vibration-motor.html) 

[ ROB-08449 ]

A vibration motor! This itty-bitty, shaftless vibratory motor is perfect for non-audible indicators. Use in any number of app...

[ [\$2.95] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

### Hardware Connection

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/5/simpleSketch.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/5/simpleSketch.png)

The hardware consists of the standard I^2^C connection and the enable (EN) pin must be pulled high.

### Arduino Program

    language:c
    #include <Sparkfun_DRV2605L.h> //SparkFun Haptic Motor Driver Library 
    #include <Wire.h> //I2C library 

    SFE_HMD_DRV2605L HMD; //Create haptic motor driver object 

    void setup() 
    
    void loop() 
    
        if (wave%64==0) // After the last register is used start over 
        
      }
     }

## PWM & Analog Input Mode Example: Light Vibes 

In this example project, we are going to control an ERM motor based on analog input from a photocell that gets mapped to a range from 0-255 and uses that result to set the pulse width modulation of an output pin connected to the IN/TRIG pin on the Haptic Motor Driver. This project will give haptic effects based on the amount of ambient light in an area.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/5/Untitled-2.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/5/Untitled-2.gif)

Waving your hand over the photoresistor turns off the motor, and, when you move your hand away, you can feel the ramping effects as the PWM signal increases with the amount of light detected.

### Parts Needed

In addition to the basics like hook-up wire, you\'ll also need the following parts:

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![SparkFun Haptic Motor Driver - DRV2605L](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/6/5/5/14538-SparkFun_Haptic_Motor_Driver-DRV2605L-01.jpg)](https://www.sparkfun.com/sparkfun-haptic-motor-driver-drv2605l.html)

### [SparkFun Haptic Motor Driver - DRV2605L](https://www.sparkfun.com/sparkfun-haptic-motor-driver-drv2605l.html) 

[ ROB-14538 ]

Ready to add some good vibes to your project? Look no further than the SparkFun Haptic Motor Driver. This board breaks out Te...

[ [\$11.95] ]

[![Mini Photocell](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/6/2/09088-02-L.jpg)](https://www.sparkfun.com/mini-photocell.html)

### [Mini Photocell](https://www.sparkfun.com/mini-photocell.html) 

[ SEN-09088 ]

This is a very small light sensor. A photocell changes (also called a \[photodetector\](http://en.wikipedia.org/wiki/Photodetec...

[ [\$1.75] ]

[![Vibration Motor](https://cdn.sparkfun.com/r/140-140/assets/parts/8/8/6/VibrationMotor-01-L.jpg)](https://www.sparkfun.com/vibration-motor.html)

### [Vibration Motor](https://www.sparkfun.com/vibration-motor.html) 

[ ROB-08449 ]

A vibration motor! This itty-bitty, shaftless vibratory motor is perfect for non-audible indicators. Use in any number of app...

[ [\$2.95] ]

[![Resistor 10K Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/1/6/14491-03.jpg)](https://www.sparkfun.com/resistor-10k-ohm-1-4-watt-pth-20-pack-thick-leads.html)

### [Resistor 10K Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://www.sparkfun.com/resistor-10k-ohm-1-4-watt-pth-20-pack-thick-leads.html) 

[ PRT-14491 ]

These are your run-of-the-mill 1/4 Watt, +/- 5% tolerance PTH resistors. Commonly used in breadboards and other prototyping a...

[ [\$1.50] ]

### The Circuit

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/5/PWMTEST_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/5/PWMTEST_bb.png)

### Arduino Sketch

    language:c
    // Control the vibration of an ERM motor
    // using PWM and a photoresistor. 

    #include <Sparkfun_DRV2605L.h>
    #include <Wire.h>

    SFE_HMD_DRV2605L HMD;
    const int analogInPin = A0;  // Analog input pin that the sensor is attached to
    const int analogOutPin = 9; // Analog output pin that the Haptic Motor Driver is attached to

    int sensorValue = 0;        // value read from the sensor
    int outputValue = 0;        // value output to the PWM (analog out)

    void setup() 
    
    void loop()