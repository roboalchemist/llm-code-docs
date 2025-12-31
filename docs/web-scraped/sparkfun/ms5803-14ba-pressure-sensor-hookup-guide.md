# Source: https://learn.sparkfun.com/tutorials/ms5803-14ba-pressure-sensor-hookup-guide

## Introduction

**Heads up!** While the IC is capable of outputting data via I2C and SPI, the Arduino Library and example was only written to output via I2C! You\'ll need to modify the jumpers on the board for SPI mode by removing solder from the pull-up resistors jumper pads and close the other two jumpers. Additionally, you will need to write a library to communicate with the MS5803 in SPI mode if you plan on using this with Arduino.

The [MS5803-14BA](https://www.sparkfun.com/products/12909) is a pressure sensor with an I^2^C (\"Wire\") and SPI interface.

[![SparkFun Pressure Sensor Breakout - MS5803-14BA](https://cdn.sparkfun.com/r/600-600/assets/parts/9/8/1/1/12909-01a.jpg)](https://www.sparkfun.com/sparkfun-pressure-sensor-breakout-ms5803-14ba.html)

### [SparkFun Pressure Sensor Breakout - MS5803-14BA](https://www.sparkfun.com/sparkfun-pressure-sensor-breakout-ms5803-14ba.html) 

[ SEN-12909 ]

This is the MS5803-14BA Pressure Sensor Breakout, a high resolution pressure sensor with both an I2C and SPI interface.

[ [\$80.50] ]

Pressure sensors measure the absolute pressure of the fluid around them. This includes air, water, and anything else that acts like a viscous fluid. Depending on how you interpret the data, you can determine altitude, water depth, or any other tasks that require an accurate pressure reading.

### Covered in This Tutorial

We will show you how to connect this sensor to an Arduino microcontroller and use the included software library to get measurements out of the sensor. We\'ll also show you how to interpret the readings showing changes in altitude and water depth.

### Suggested Reading

This part is easy to use. But before you start, we recommend the following background knowledge:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Connecting the Hardware - I2C

In this example, we will communicate with the MS5803-14BA using the I2C interface.

### Connection Names

The MS5803-14BA Breakout Board breaks out seven connections from the IC. We traditionally call these connections \"pins\" because they come from the pins on the IC, but they are actually holes that you can solder [wires](https://www.sparkfun.com/products/11367) or [header pins](https://www.sparkfun.com/products/116) to.

[![Board Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/2/FrontView.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/2/FrontView.jpg)

We\'ll connect four of the seven pins on the board to your Arduino. The four pins you need are labeled **GND**, **VCC**, **SCL**, and **SDA**.

### Connecting Headers to the Board

You can use any method you like to make your connections to the board. For this example, we\'ll solder on a seven-pin length of [male-male header strip](https://www.sparkfun.com/products/116), and use [male-female jumper wires](https://www.sparkfun.com/products/9385) to connect the MS5803-14BA to your Arduino.

[Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) a 7-pin length of male-male header to the board. You can solder it to either side. The bottom is more useful for breadboards, and the top is more useful for jumper wires.

[![Headers Installed](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/1/3/2/HeadersInstalled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/2/HeadersInstalled.jpg)

### Connecting the Board to your Arduino

When you\'re done soldering, connect the GND, 3.3v, SDA, and SCL pins to your Arduino. Different Arduino models use different pins for the I^2^C interface; use the following chart to determine where to plug everything in.

IMPORTANT: Connect the power pins (3.3v and GND) **ONLY** to a 3.3V supply. Larger voltages will permanently damage the part. Note that because I^2^C uses [open drain drivers](https://learn.sparkfun.com/tutorials/i2c/i2c-at-the-hardware-level), it is safe to connect the I^2^C pins (DA and CL) to an I^2^C port on a 5V microprocessor.

MS5803-14BA label

Pin function

Arduino connection

**GND**

ground

**GND**

**3.3v**

3.3V power supply

**3.3V**

**SDA**

I^2^C data

Any pin labeled SDA, or:

  ------------------------------- --------
  Uno, RedBoard, Pro / Pro Mini   **A4**
  Mega, Due                       **20**
  Leonardo, Pro Micro             **2**
  ------------------------------- --------

**SCL**

I^2^C clock

Any pin labeled SCL, or:

  ------------------------------- --------
  Uno, RedBoard, Pro / Pro Mini   **A5**
  Mega, Due                       **21**
  Leonardo, Pro Micro             **3**
  ------------------------------- --------

[![Circuit Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/2/Connected-i2c.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/2/Connected-i2c.png)

Once you have the MS5803-14BA connected to your Arduino, we\'re ready to play with the software.

## Installing the Arduino Library

**Note:** This code/library has been written and tested on Arduino IDE version 1.6.4 . Otherwise, make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Libraries are collections of software functions geared towards a single purpose, such as communicating with a specific device. Arduino comes with a number of built-in libraries that help you do advanced tasks. We\'ve written an Arduino library called the **SparkFun MS5803-14BA Breakout Arduino Library** that allows you to easily talk to the MS5803 sensor. This library is not included with the stock Arduino software, but don\'t worry, installing new libraries is easy. You can obtain these libraries through the Arduino Library Manager. Search for **SparkFun MS5803** and you should be able to install the latest version. If you prefer downloading the libraries manually, you can grab them from the [GitHub repository](https://github.com/sparkfun/SparkFun_MS5803-14BA_Breakout_Arduino_Library):

[Download the SparkFun MS5803-14BA Breakout Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_MS5803-14BA_Breakout_Arduino_Library/archive/master.zip)

If you\'d like to interface the MS5803 to a microcontroller other than an Arduino, the C++ source code in the library and the information in the [datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Weather/ms5803_14ba.pdf) may be helpful when writing your own code.

Once you\'ve installed the library, restart the Arduino IDE and you should be ready to go.

## Example Sketches

### Running the Example Sketch

The library you just installed includes an example sketch that show basic operation of the MS5803. This are designed to be a starting point for writing your own code.

After you install the library, run the Arduino IDE, and open the following menu item: **File** / **Examples** / **SFE_MS5803_14BA** / **SFE_MS5803_14BA_I2C_Demo**.

**Note:** If you don\'t see this menu item, you may not have installed the library correctly, or didn\'t restart the Arduino IDE. Take another look at the [library installation page](https://learn.sparkfun.com/tutorials/ms5803-14ba-pressure-sensor-hookup-guide/installing-the-arduino-library) to see if you missed any steps.

[![Opening Example Code from the Arduino IDE Menu](https://cdn.sparkfun.com/assets/7/5/9/d/9/ArduinoLibMenu.png)](https://cdn.sparkfun.com/assets/7/5/9/d/9/ArduinoLibMenu.png)

When the example opens, upload it to your Arduino (remember to select the correct board type and serial port), and open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) to **9600 baud**. You should see some diagnostic information (if it can\'t find the device, double check your hardware connections) followed by measurement readings.

[![Example Output in the Serial Monitor](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/2/SensorOutput.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/2/SensorOutput.png)

### Writing Your Own Sketches

The comments and code in the example sketch should get you started when writing your own sketches. In many cases you should be able to copy and paste the example code into your own sketch.