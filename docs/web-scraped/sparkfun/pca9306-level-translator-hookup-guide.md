# Source: https://learn.sparkfun.com/tutorials/pca9306-level-translator-hookup-guide

## PCA9306 Overview

**Heads up!** This is for the PCA9306 breakout v1. If you are using the v2, you\'ll want to [head over to the other tutorial](https://learn.sparkfun.com/tutorials/pca9306-logic-level-translator-hookup-guide-v2). The package used on the PCA9306 breakout v2 is different from the PCA9306 breakout v1.

The [PCA9306](https://www.sparkfun.com/products/11955) is a dual bidirectional voltage translator for the I^2^C-bus and SMBus. It works at a range of voltages between 1.0 and 5.0V and doesn\'t require a direction pin to function.

[![SparkFun Level Translator Breakout - PCA9306](https://cdn.sparkfun.com/r/600-600/assets/parts/8/4/3/0/11955-01.jpg)](https://www.sparkfun.com/products/11955)

### [SparkFun Level Translator Breakout - PCA9306](https://www.sparkfun.com/products/11955) 

[ BOB-11955 ]

This is a breakout board for the PCA9306 dual bidirectional voltage-level translator. Because different parts sometimes use d...

**Retired**

*PCA9306 Breakout Board*

This is a great board for shifting voltages between sensors and your microcontroller.

### Suggested Reading

These level converters are pretty easy to start using, but you may want to check out some of the additional reading material below if you are unfamiliar with logic level shifting or haven\'t worked with Arduino boards prior to this.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Hookup

The breakout board has seven pins that need to be connected to function properly. VREF1, SCL1, and SDA1 all connect to your lower voltage part. VREF2, SCL2, and SDA2 connect to your higher voltage part. The GND pin needs to be connected to ground in your system. The final through-hole on the board labeled NC does not need to be connected to anything.

To connect the board, solder headers into the through-holes, and use jumper wires between devices. Or, you could just solder some hookup wire to all your boards.

For this example, we are going to use an [Arduino Pro Mini 5V](https://www.sparkfun.com/products/11113) to connect to an [HMC5883L magnetometer breakout board](https://www.sparkfun.com/products/10530), which runs at 3.3V and communicates over I^2^C.

### Connections:

HMC5883L → PCA9306

- 3.3V → VREF1
- SCL → SCL1
- SDA → SDA1
- GND → GND

PCA9306 → Pro Mini (5V)

- VREF2 → 5V
- SCL2 → A5
- SDA2 → A4

Here is a Fritizing diagram showing the actual connections between the HMC5883L, the PCA9306 breakout and the Pro Mini.

[![Fritzing Diagram of hookups](https://cdn.sparkfun.com/r/600-600/assets/0/8/4/e/9/5294eb19ce395f223a8b4567.jpg)](https://cdn.sparkfun.com/assets/0/8/4/e/9/5294eb19ce395f223a8b4567.jpg)

*Fritzing diagram showing the connections between the three boards.*

The diagram shows the HMC5883L running off of a 3V power supply, and the Pro Mini running off of a 5V barrel jack connector. Keep in mind your power supplies could be different than the ones pictured above (for example, using a LiPo battery instead of AA batteries), but you will still need to have a power supply for the lower voltage side of the system and a separate supply for the higher voltage side.

Once you have the boards physically connected, you are good to go! You don\'t need to use any special code with the PCA9306 board, and you can simply use any example sketch available for your sensors. In this case, we are using the example [HMC5883.ino](http://sfecdn.s3.amazonaws.com/datasheets/Sensors/Magneto/HMC5883.pde) sketch.