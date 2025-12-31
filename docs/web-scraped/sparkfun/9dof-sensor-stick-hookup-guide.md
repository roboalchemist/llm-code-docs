# Source: https://learn.sparkfun.com/tutorials/9dof-sensor-stick-hookup-guide

## Introduction

The [9DoF Sensor Stick](https://www.sparkfun.com/products/13944) is an easy-to-use 9 degrees of freedom IMU. The sensor used is the LSM9DS1, the same sensor used in the [SparkFun 9 Degrees of Freedom IMU Breakout](https://www.sparkfun.com/products/13284), but is slimmed down to be only 0.9\"x0.4\".

[![SparkFun 9DoF Sensor Stick](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/6/3/3/13944-01.jpg)](https://www.sparkfun.com/sparkfun-9dof-sensor-stick.html)

### [SparkFun 9DoF Sensor Stick](https://www.sparkfun.com/sparkfun-9dof-sensor-stick.html) 

[ SEN-13944 ]

The SparkFun 9DoF Sensor Stick is an easy-to-use 9 Degrees of Freedom IMU. The Sensor Stick deftly utilizes the LSM9DS1 motio...

**Retired**

### Required Materials

To follow along with this hookup guide, you will need the following:

### Suggested Reading

Before getting started, you may find the following links useful:

[](https://learn.sparkfun.com/tutorials/pull-up-resistors)

### Pull-up Resistors 

A quick introduction to pull-up resistors - whey they\'re important, and how/when to use them.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/gyroscope)

### Gyroscope 

Gyroscopes measure the speed of rotation around an axis and are an essential part in determines ones orientation in space.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

Let\'s go over the 9DoF Sensor Stick in detail.

[![9DoF Sensor Stick](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/2/13944-02crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/2/13944-02crop.jpg)

#### LSM9DS1 Details:

- 3 acceleration channels, 3 angular rate channels, 3 magnetic field channels
- ±2/±4/±8/±16 g linear acceleration full scale
- ±4/±8/±12/±16 gauss magnetic full scale
- ±245/±500/±2000 dps angular rate full scale
- I^2^C serial interface
- Operating Voltage: **3.3V**

### Pull-up Resistors

This breakout board has built-in 4.7 kΩ pull up resistors for I^2^C communications. If you\'re hooking up multiple I^2^C devices on the same bus, you may want to disable/enable the pull-up resistors for one or more boards. On the 9DoF Sensor Stick, the pull-ups are enabled by default. To disable them, simply use a [hobby knife](https://www.sparkfun.com/products/9200) to cut the traces connecting the left and right pads of the jumper labeled **I2C PU** on the back of the board. This will disconnect the resistors on the I^2^C bus from VCC.

[![i2c pullup jumper](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/2/9DoF_Sensor_Stick_Bottom_i2c_hightlight2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/2/9DoF_Sensor_Stick_Bottom_i2c_hightlight2.jpg)

### Changing I^2^C Addresses

If you\'re using multiple Sensor Sticks, or have a device that\'s already using the default addresses of the Sensor Stick, you\'ll want to change addresses to avoid having multiple devices try to talk over one another. The **default address for the magnetometer is 0x1E** and the **default address for the accelerometer and gyroscope is 0x6B**. To change the addresses, you\'ll want to use a [hobby knife](https://www.sparkfun.com/products/9200) to cut the trace between center and top pads and use solder to short the center and bottom pads. This will change the address of the **magnetometer** to **0x1C** and the **accelerometer and gyroscope** to **0x6A**.

[![address jumper](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/2/9DoF_Sensor_Stick_Bottom_addr_highlight2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/2/9DoF_Sensor_Stick_Bottom_addr_highlight2.jpg)

## Hardware Connections

### Connecting the 9DoF Sensor Stick to an Arduino

Wiring the Sensor Stick is very easy! We recommend [soldering](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) four [male headers](https://www.sparkfun.com/products/116) to the sensor stick. You can also directly solder [wires](https://www.sparkfun.com/products/11375) to the board to fit your application\'s needs.

### Power

This board runs on **1.9V to 3.6V**. Be sure to power the board from the 3.3V pin! I^2^C uses an open drain signaling, so there is no need to use level shifting; the 3.3V signal will work to communicate with the Arduino and will not exceed the maximum voltage rating of the pins on the LSM9DS1.

### Connections to the Arduino

The 9DoF Sensor Stick has only four pins. We\'ll be connecting VCC and GND to the normal power pins, and the remaining two pins are used for I^2^C communication. If you\'re using a newer board that has SDA and SCL broken out, you can connect the SDA and SCL pins from the Sensor Stick directly to those pins. If you\'re using an older board, SDA and SCL are pins A4 and A5 respectively.

- VCC → 3.3V
- GND → GND
- SDA → SDA/A4
- SCL → SCL/A5

Your circuit should look something like this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/2/9DoF_Sesnor_Stick_Fritzing_noblkline.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/2/9DoF_Sesnor_Stick_Fritzing_noblkline.jpg)

## Installing the Arduino Library

We\'ve written a full-featured Arduino library to help make interfacing with the LSM9DS1\'s gyro, accelerometer, and magnetometer as easy-as-possible. Visit the [GitHub repository](https://github.com/sparkfun/SparkFun_LSM9DS1_Arduino_Library) to download the most recent version of the library, or click the link below:

[Download the SparkFun LSM9DS1 Arduino Library](https://github.com/sparkfun/SparkFun_LSM9DS1_Arduino_Library/archive/master.zip)

For help installing the library, check out our [How To Install An Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library). You need to move the *SparkFun_LSM9DS1_Arduino_Library* folder into a *libraries* folder within your Arduino sketchbook or use the Library Manger to install.

### The LSM9DS1_Basic_I2C Example

To verify that your hookup works, load up the LSM9DS1_Basic_I2C example by going to **File** \> **Examples** \> **LSM9DS1 Breakout** \> **LSM9DS1_Basic_I2C**.

The default values set by this sketch should work for a fresh, out-of-the-box 9DoF Sensor Stick \-- it assumes both of the address jumpers haven\'t been modified. Upload the sketch, then open up your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics), setting the baud rate to **115200**. You should see something like this:

[![Example serial monitor output](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/Arduino_serial_monitor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/Arduino_serial_monitor.jpg)

The current reading from each axis on each sensor is printed out, then those values are used to estimate the sensor\'s orientation. Pitch is the angle rotated around the y-axis, roll is the board\'s rotation around the x-axis, and heading (i.e. yaw) is the sensor\'s rotation around the z-axis. Try rotating the board (without pulling out any wires!) to see how the values change.