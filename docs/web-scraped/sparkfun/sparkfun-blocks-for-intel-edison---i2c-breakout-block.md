# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---i2c-breakout-block

## Introduction and Overview

The [I2C Breakout Block](https://www.sparkfun.com/products/13034) is a simple way to integrate an I2C device with an Intel Edison stack. The I2C block has the ability to supply 3.3V or VSYS power to external I2C sensors. This opens up the Edison to the great variety of I2C devices we, and others, have to offer.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/1/I2CBlockTop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/1/I2CBlockTop.jpg)

*I2C Breakout Block*

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Edison adventure include:

- [Edison Getting Started Guide](/tutorials/edison-getting-started-guide)
- [I2C](/tutorials/i2c)

## Board Overview

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/1/I2CBlockAnnotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/1/I2CBlockAnnotated.png)

*I2C Block Functional Diagram TOP*

- I2C Port - Standard I2C port broken out. VOUT provides power based on Level Select position.

- Level Select - Provides level selection between 3.3V and VSYS levels on VOUT. Default 3.3V

- Expansion Header - The 70-pin Expansion header breaks out the functionality of the Intel Edison. This header also passes signals and power throughout the stack. These function much like an [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields).

## Using the I2C Breakout Block

To use the I2C Breakout Block, attach an Intel Edison to the back of the board or add it to your current stack. Blocks can be stacked without hardware, but it leaves the expansion connectors unprotected from mechanical stress.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/1/I2CBlockISO.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/1/I2CBlockISO.jpg)

*I2C Block Installed*

We have a nice [Hardware Pack](https://www.sparkfun.com/products/13187) available that gives enough hardware to secure three blocks and an Edison.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/6/EdisonHardware_1.jpg)

[*Intel Edison Hardware Pack*](https://www.sparkfun.com/products/13187)

NOTE: The I2C Breakout Block does not have console access or a power supply. It is recommended to use a console communication block in conjunction with this block like ones found in the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison#console-communication-blocks).

#### Example

In our example, we will show how to connect and scan for the [SparkFun RGB and Gesture Sensor](https://www.sparkfun.com/products/12787). [Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) a 4-pin section of our [Right Angle Break Away Male Headers](https://www.sparkfun.com/products/553) to the breakout board. Plug the board into the I2C Brekaout Block, and you\'re done with the hardware connection.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/1/SensorInstalled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/1/SensorInstalled.jpg)

*SparkFun RGB and Gesture Sensor Installed*

To find the I2C device in the console, type the following command. Note the I2C bus we will use is bus 1.

    i2cdetect -y -r 1

We see that the device appears on address 0x39 as expected.

         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- 39 -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --

To use the SparkFun RGB and Gesture Sensor in your project, you can modify the code from the [RGB and Gesture Sensor Hookup Guide](/tutorials/apds-9960-rgb-and-gesture-sensor-hookup-guide) to run on your Edison. Using the Arduino IDE for Edison, the demo should work out of the box!

### Using 5V Devices

There is a way to modify the I2C block to accept 5V logic. Cut the voltage select jumper, but do not re-connect to either VSYS or 3.3V. You will now need to supply your own 5V voltage (for your sensors) externally. You can solder a 5V supply to the center pad OR use the VOUT pin on the connector. Supplying 5V through the VOUT trace will allow you to plug sensors in without modification.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/1/5Vhack.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/1/5Vhack.png)