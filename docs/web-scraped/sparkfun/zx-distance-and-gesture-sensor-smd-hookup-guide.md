# Source: https://learn.sparkfun.com/tutorials/zx-distance-and-gesture-sensor-smd-hookup-guide

## Introduction

The [ZX Distance and Gesture Sensor](https://www.sparkfun.com/products/13162) is a collaboration product with [XYZ Interactive](http://www.gesturesense.com/xyz/). The innovative people at XYZ Interactive have created a unique technology that allows for simple infrared (IR) beams to be used to detect an object\'s location in two dimensions.

The ZX Sensor is a touchless sensor that is capable of looking for simple gestures in the air above the sensor (e.g. swipe left or swipe right). Additionally, the sensor can also recognize the distance of an object away from the sensor at distances up to about 12 inches (30 cm), referred to as the \"Z\" axis, and the location of the object from side to side across the sensor in about a 6 inch (15 cm) span, referred to as the \"X\" axis.

[![ZX Distance and Gesture Sensor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/2/7/9/13162-01a.jpg)](https://www.sparkfun.com/zx-distance-and-gesture-sensor.html)

### [ZX Distance and Gesture Sensor](https://www.sparkfun.com/zx-distance-and-gesture-sensor.html) 

[ SEN-13162 ]

The ZX Distance and Gesture Sensor is a touchless sensor that is capable of looking for simple gestures. Developed in conjunc...

[ [\$28.50] ]

### Covered in This Tutorial

We can use I^2^C or UART to communicate with the ZX Sensor. In this tutorial, we will show you how to connect the sensor to an Arduino or Arduino-compatible board as well as a computer so you can start creating gestures to handle all our your daily tasks or add some interactive flair to your project.

### Materials Used

In addition to the sensor itself, you will need a few extra components to follow along with the Arduino examples:

If you would like to try the ZX Sensor on a Windows-based PC, you will need an FTDI Breakout:

[![SparkFun FTDI Basic Breakout - 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/2/9/09716-SparkFun_FTDI_Basic_Breakout_-_5V-01.jpg)](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-5v.html)

### [SparkFun FTDI Basic Breakout - 5V](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-5v.html) 

[ DEV-09716 ]

This is a basic breakout board for the FTDI FT232RL USB to serial IC. The pinout of this board matches the FTDI cable to work...

[ [\$19.51] ]

### Recommended Reading

There are a few concepts that you should be familiar with before getting started with the ZX Sensor. Consider reading some of these tutorials before continuing:

- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino) \-- Two of the examples use an Arduino to control the ZX Sensor
- [I^2^C](https://learn.sparkfun.com/tutorials/i2c) \-- I^2^C is the one of the protocols used by the ZX Sensor
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication) \-- We use serial communications to program the Arduino, view debugging information, and transmit data from the ZX Sensor
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) \-- The breadboard ties the Arduino to the ZX Sensor
- [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) \-- If you are programming an Arduino or using the ZX Sensor demo app, chances are you will need to use an FTDI

## Board Overview

The ZX Sensor works by bouncing infrared (IR) beams of light from the two LEDs on either side off of an object above the sensor. The bounced light returns to the receiver in the center of the sensor, and a microcontroller on the back of the sensor interprets the data. We can read the results using an I^2^C or UART connection.

### Pin Descriptions

The ZX Sensor gives us two ports to connect to: I^2^C and UART. You can see both ports are broken out to the 0.1\" thru holes. See the table below for a list of each pin and its function.

[![ZX FRONT](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/13162_04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/13162_04.jpg)

Pin Label

Description

GRN

Not used

TXO

UART transmit out from the ZX Sensor

RXI

UART receive. Not used at this time.

VCC

3.3 - 5 V power supply

GND

Connect to ground

BLK

Not used, but connected to GND

DR

Data Ready. High when there is data to be read via I^2^C

CL

I^2^C clock

DA

I^2^C data

\

### Setting the Jumpers

The ZX Sensor has a couple of jumpers on the back of the board that can be opened or closed with a soldering iron.

[![ZX Sensor Back](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/13162_03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/13162_03.jpg)

#### I2C Pullups

The ZX Sensor, by default, comes with 4.7 kΩ pull-up resistors on the SDA and SCL I^2^C lines. Remove the solder on this jumper using solder wick to disconnect the pull-ups.

#### I2C Addr

By default, this jumper is open. Close it to change the I^2^C address of the sensor.

  Jumper   I^2^C Address
  -------- ---------------
  Open     0x10
  Closed   0x11

\

## Hardware Hookup

### Add Headers

[Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) a row of [male headers](https://www.sparkfun.com/products/116) to the nine headers holes on the board.

[![Placing sensor over male headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-01.jpg)

To keep the board from tilting while soldering, place the unused break away headers sideways under the board.

[![Soldering the header pins to the nine through holes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-02.jpg)

**Heads up!** Do not solder headers to the row of holes at the top of the board. Those are for programming the PIC microcontroller.

### Connect the Breakout Board

For the Arduino examples, we will be using I^2^C. Connect the breakout board to the following RedBoard pins:

[![ZX Sensor to Arduino Fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/5/zx_sensor_fritzing_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/zx_sensor_fritzing_bb.png)

ZX Sensor

RedBoard

VCC

5V

GND

GND

DR

2

CL

A5

DA

A4

\

Note that we connect the DR pin, but we will only use it in the [Arduino: Gesture Example](https://learn.sparkfun.com/tutorials/zx-distance-and-gesture-sensor-hookup-guide#arduino-gesture-example). DR stands for \"Data Ready,\" which is active high whenever data is ready to be read from the ZX Sensor. We can attach this to an Arduino interrupt so we don\'t have to continuously poll the sensor.

[![ZX Sensor connected to Redboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-03.jpg)

## Arduino Library Installation

All of the hard work for the ZX Sensor is being accomplished in the microcontroller on the sensor itself. All we need to do is read the results! We have created an Arduino library to make that even easier for you. Click the button to download the latest version of the ZX Sensor Arduino Library. You can also find the latest files in the [GitHub repository](https://github.com/sparkfun/ZX_Gesture_Sensor_SMD).

[Download the ZX Sensor Arduino Library!](https://github.com/sparkfun/SparkFun_ZX_Distance_and_Gesture_Sensor_Arduino_Library/archive/master.zip)

Unzip the downloaded file. Follow [this guide on installing Arduino libraries](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) to install the files as an Arduino library.

## Arduino: ZX Example

### Load the ZX Demo

Open up the Arduino program and select File → Examples → SparkFun_ZX_Distance_and_Gesture_Sensor → I2C_ZX_Demo.

[![I2C ZX Demo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/5/ZX_Demo.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/ZX_Demo.png)

Attach a [USB mini](https://www.sparkfun.com/products/11301) cable from your computer to the RedBoard. If you have not previously done so, [install the FTDI drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers).

For reference, here is the I2C_ZX_Demo.ino sketch.

    language:c
        /****************************************************************
        I2C_ZX_Demo.ino
        XYZ Interactive ZX Sensor
        Shawn Hymel @ SparkFun Electronics
        May 6, 2015
        https://github.com/sparkfun/SparkFun_ZX_Distance_and_Gesture_Sensor_Arduino_Library

        Tests the ZX sensor's ability to read ZX data over I2C. This demo
        configures the ZX sensor and periodically polls for Z-axis and X-axis data.

        Hardware Connections:

         Arduino Pin  ZX Sensor Board  Function
         ---------------------------------------
         5V           VCC              Power
         GND          GND              Ground
         A4           DA               I2C Data
         A5           CL               I2C Clock

        Resources:
        Include Wire.h and ZX_Sensor.h

        Development environment specifics:
        Written in Arduino 1.6.3
        Tested with a SparkFun RedBoard

        This code is beerware; if you see me (or any other SparkFun 
        employee) at the local, and you've found our code helpful, please
        buy us a round!

        Distributed as-is; no warranty is given.
        ****************************************************************/

        #include <Wire.h>
        #include <ZX_Sensor.h>

        // Constants
        const int ZX_ADDR = 0x10;  // ZX Sensor I2C address

        // Global Variables
        ZX_Sensor zx_sensor = ZX_Sensor(ZX_ADDR);
        uint8_t x_pos;
        uint8_t z_pos;

        void setup()  else 

          // Read the model version number and ensure the library will work
          ver = zx_sensor.getModelVersion();
          if ( ver == ZX_ERROR )  else 
          if ( ver != ZX_MODEL_VER ) 

          // Read the register map version and ensure the library will work
          ver = zx_sensor.getRegMapVersion();
          if ( ver == ZX_ERROR )  else 
          if ( ver != ZX_REG_MAP_VER ) 
        }

        void loop() 
            z_pos = zx_sensor.readZ();
            if ( z_pos != ZX_ERROR ) 
          }
        }

### Run

Make sure you have the correct serial port selected under Tools → Serial Port and \"Arduino Uno\" selected under Tools → Board. If you have never used the Arduino IDE before, [this turoial](https://learn.sparkfun.com/tutorials/installing-arduino-ide) should get you started.

Click the Upload button and wait for the program to finish uploading to the Arduino. Select Tools → Serial Monitor to open up the serial terminal. More info on the Serial Terminal can be found [here](https://learn.sparkfun.com/tutorials/terminal-basics). Note that the Serial Monitor settings are the default settings (9600, 8, n, 1). You should see a couple of messages noting that \"ZX Sensor initialization complete.\"

[![ZX Sensor initialization](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/ZX_Demo_init.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/ZX_Demo_init.png)

Hover your hand 4 to 10 inches (10 to 25 cm) above the sensor.

[![Hover](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-05.jpg)

Move your hand around above the sensor, and you should see Z (height above the sensor) and X (position side to side) appear in the serial terminal.

[![ZX Sensor showing position data](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/ZX_Demo_run.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/ZX_Demo_run.png)

**NOTE:** Z- and X- data is given as an unsigned integer between 0 and 240 (inclusive).

## Arduino: Gesture Example

### Load the Gesture Interrupt Demo

In addition to providing Z- and X- axis data about an object, the ZX Sensor is also capable of detecting simple gestures. To see an example of this, open File → Examples → SparkFun_ZX_Distance_and_Gesture_Sensor → I2C_Gesture_Interrupt.

[![ZX Sensor Gesture Demo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/5/Gesture_Demo.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/Gesture_Demo.png)

Here is the I2C_Gesture_Interrupt.ino sketch for reference.

    language:c
    /****************************************************************
    I2C_Gesture_Interrupt.ino
    XYZ Interactive ZX Sensor
    Shawn Hymel @ SparkFun Electronics
    May 6, 2015
    https://github.com/sparkfun/SparkFun_ZX_Distance_and_Gesture_Sensor_Arduino_Library

    Tests the ZX sensor's ability to read gesture data over I2C using 
    an interrupt pin. This program configures I2C and sets up an
    interrupt to occur whenever the ZX Sensor throws its DR pin high.
    The gesture is displayed along with its "speed" (how long it takes
    to complete the gesture). Note that higher numbers of "speed"
    indicate a slower speed.

    Hardware Connections:

     Arduino Pin  ZX Sensor Board  Function
     ---------------------------------------
     5V           VCC              Power
     GND          GND              Ground
     A4           DA               I2C Data
     A5           CL               I2C Clock
     2            DR               Data Ready

    Resources:
    Include Wire.h and ZX_Sensor.h

    Development environment specifics:
    Written in Arduino 1.6.3
    Tested with a SparkFun RedBoard

    This code is beerware; if you see me (or any other SparkFun 
    employee) at the local, and you've found our code helpful, please
    buy us a round!

    Distributed as-is; no warranty is given.
    ****************************************************************/

    #include <Wire.h>
    #include <ZX_Sensor.h>

    // Constants
    const int ZX_ADDR = 0x10;    // ZX Sensor I2C address
    const int INTERRUPT_NUM = 0; // Pin 2 on the UNO

    // Global Variables
    ZX_Sensor zx_sensor = ZX_Sensor(ZX_ADDR);
    volatile GestureType gesture;
    volatile bool interrupt_flag;
    uint8_t gesture_speed;

    void setup()  else 

      // Read the model version number and ensure the library will work
      ver = zx_sensor.getModelVersion();
      if ( ver == ZX_ERROR )  else 
      if ( ver != ZX_MODEL_VER ) 

      // Read the register map version and ensure the library will work
      ver = zx_sensor.getRegMapVersion();
      if ( ver == ZX_ERROR )  else 
      if ( ver != ZX_REG_MAP_VER ) 

      // Initialize interrupt service routine
      interrupt_flag = false;
      zx_sensor.clearInterrupt();
      attachInterrupt(INTERRUPT_NUM, interruptRoutine, RISING);
      Serial.println("Interrupts now configured. Gesture away!");
    }

    void loop() 
      }
    }

    void interruptRoutine() 

### Run

Upload the sketch, and open the Serial Monitor. You should see a message stating that initialization is complete.

[![ZX Sensor Gesture initialization](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/Gesture_init.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/Gesture_init.png)

Start with your hand off to one side (a \"side\" being the one of the infrared LEDs with the brass covers) about 4 to 10 inches (10 to 25 cm) above the sensor. Swipe your hand horizontally across the sensor so that your hand passes over the one infrared LED and then the next infrared LED.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-04.jpg)

If you performed the gesture correctly, you should see a message appear in the Serial Monitor.

[![Performing gestures with the ZX Sensor](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/Gesture_run.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/Gesture_run.png)

**NOTE:** The \"Speed\" of the gesture is a measure of how fast the gesture occurred. Note that the *lower* the number, the *faster* the gesture occurred (e.g. 3 being very fast and 25 being very slow).

### Supported Gestures

Here is a list of the currently supported gestures. Make sure each gesture begins outside of the range of the sensor, moves into the range of the sensor, and ends outside the range of the sensor.

  Gesture       Description
  ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Right Swipe   A swipe from the left side of the board to the right and out of range of the sensor. Make sure that your wrist/arm is not in the sensor\'s range at the end of the swipe!
  Left Swipe    A swipe from the right side of the board to the left and out of range of the sensor.
  Up Swipe      Object starts near the sensor, hovers for at least 1 second, and then moves up above and out of range of the sensor.
  No Gesture    The sensor could not correctly determine the gesture being performed.

\

## PC: ZX Example

The ZX Sensor, in addition to responding to I^2^C commands, continually transmits ZX data over its UART port. We can connect an [FTDI Breakout](https://www.sparkfun.com/products/9716) directly to the ZX Sensor and read the output. You can use [serial applications](https://learn.sparkfun.com/tutorials/terminal-basics) or the [screen command](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) (Linux or Mac) to view the output.

**NOTE:** You can use either 3.3 V or 5 V FTDI. 5 V gives you a bit better range with the sensor.

If you are on a Windows computer, you can use the demo application (linked below) provided by XYZ Interactive to test the ZX Sensor.

### Setup

Connect the FTDI Breakout board to the ZX Sensor. Ensure the pins on the FTDI Brekaout line up with the pins on the ZX Sensor (e.g. GRN connects to GRN and BLK connects to BLK). Connect the FTDI Breakout to your computer with a USB cable.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-06.jpg)

Download the ZX Demo application, and unzip it.

[Download the ZX Demo Application](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/ZX_Demo_V11.zip)

### Run

Double-click to run the ZX Demo application. Under \"Input:\" on the right side, drop down the list and select the COM port that corresponds to your FTDI Breakout (if you need a refresher on find the right COM port, check out [this section](https://learn.sparkfun.com/tutorials/terminal-basics/connecting-to-your-device) of the Terminal Basics tutorial). You do not need to choose an \"Output:\" port.

Click **Open** to connect to the FTDI Breakout.

[![ZX Sensor demo application](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/5/ZX_app.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/5/ZX_app.png)

Move your hand around above the sensor, and you should see the red ball move.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/1/Gesture_Sensor_Update-07.jpg)

Try out the other tabs in the application! The Z-Control tab lets your try moving your hand toward and away from the sensor, and the Gestures tab computes a few different gestures based on the Z- and X- data.