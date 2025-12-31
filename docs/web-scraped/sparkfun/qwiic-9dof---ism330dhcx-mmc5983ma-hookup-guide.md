# Source: https://learn.sparkfun.com/tutorials/qwiic-9dof---ism330dhcx-mmc5983ma-hookup-guide

## Introduction

The [SparkFun Qwiic 9DoF - ISM330DHCX, MMC5983MA](https://www.sparkfun.com/products/19895) combines the high-performance ISM330DHCX 3D digital accelerometer and gyroscope from STMicroelectronics with the highly sensitive triple-axis magnetometer by MEMSIC to give you an ultra powerful, easy to use, Qwiic enabled breakout board.

With a full scale acceleration range of ±2/±4/±8/±16 g and a wide angular rate range of ±125/±250/±500/±1000/±2000/±4000 dps, as well as an unmatched set of embedded features (Machine Learning Core, programmable FSM, FIFO, sensor hub, event decoding and interrupts), the ISM330DHCX delivers high performance at very low power. Add to that the MMC5983MA, which can measure magnetic fields within the full scale range of ±8 Gauss (G), with 0.25mG/0.0625mG per LSB resolution at 16bits/18bits operation mode and 0.4 mG total RMS noise level and you\'ve got 9 Degrees of Freedom on one tiny little breakout board.

[![SparkFun 9DoF IMU Breakout - ISM330DHCX, MMC5983MA (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/6/1/5/19895_Diag.jpg)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-ism330dhcx-mmc5983ma-qwiic.html)

### [SparkFun 9DoF IMU Breakout - ISM330DHCX, MMC5983MA (Qwiic)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-ism330dhcx-mmc5983ma-qwiic.html) 

[ SEN-19895 ]

The SparkFun 9DoF IMU Breakout combines a high-performance 6DoF IMU with the highly sensitive triple-axis magnetometer in a Q...

[ [\$45.74] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

## Hardware Overview

### ISM330DHCX 6DoF

The ISM330DHCX is a small, system-in-package from STMicroelectronics featuring a high-performance 3D digital accelerometer and 3D digital gyroscope capable of wide bandwidth, ultra-low noise and a selectable full-scale range of ±2/±4/±8/±16 g. The 3D gyroscope has an angular rate range of ±125/±250/±500/±1000/±2000/±4000 dps and offers superior stability over temperature and time along with ultra-low noise.

The ISM330DHCX as implemented in the 9DoF can run in two different modes:

#### Mode 1

This is the default \"peripheral only\" mode. This mode allows you to use either I^2^C or SPI. By default, I^2^C is enabled with an address of 0x6B. By manipulating the associated jumper, you can change the I^2^C address to 0x6A (cut the power side and close the ground side) or switch to SPI mode (both jumpers open).

#### Mode 2

This mode enables a secondary I^2^C port that the 6DoF controls; up to 4 external sensors can be connected to the I^2^C controller interface of the device. External sensors communicate via the SCX and SDX (PICOX) lines - the SCX jumper will need to be opened.

[![The ISM330DHCX is the IC in the middle of the board on the left side (with the GND pin on the upper left) ](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_ISM330DHCX1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_ISM330DHCX1.jpg)

### MMC5983MA

The MMC5983MA is an AEC-Q100 qualified, fully integrated 3-axis magnetic sensor with on-chip signal processing and integrated I^2^C/SPI bus. It has superior dynamic range and accuracy with ±8G FSR, 18bit operation, 0.4mG total RMS noise, and can enable heading accuracy of 0.5º. More information can be found in the [datasheet](https://cdn.sparkfun.com/assets/a/b/7/7/2/19921-09102019_MMC5983MA_Datasheet_Rev_A-1635338.pdf).

[![The MMC5983MA is the IC in the middle of the board on the right side (with the GND pin on the upper left)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_MMC5983MA1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_MMC5983MA1.jpg)

[] **Warning!** It should be noted that the Z axis for the ISM330DHCX and the MMC5983MA are calibrated from opposite directions. The ISM330DHCX Z axis functions as looking through from top to bottom. The MMC5983MA Z axis functions as looking from the bottom of the board through to the top. This is denoted by the \"MAG -Z\" labeled dot on the underside of the board.\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_MagZAxisDot.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_MagZAxisDot.jpg)

\

### Qwiic Connectors

Our Qwiic Ecosystem makes sensors pretty much plug and play. There\'s a Qwiic connector on either side of the Qwiic 9DoF - ISM330DHCX, MMC5983MA breakout to provide power and I^2^C connectivity simultaneously. The default I^2^C address for the ISM330DHCX is **0x6B**, and the I^2^C address for the MMC5983MA Magnetometer is **0x30**.

[![There are Qwiic connectors on either side of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_QwiicConnectors1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_QwiicConnectors1.jpg)

### Pins

#### Power

Ideally, power will be supplied via the Qwiic connectors, but we\'ve also broken out plated through hole pins to supply 3.3V and Ground, should you prefer. Make sure to pay attention to logic levels - supply voltage to this board should range from **1.71 V to 3.6 V**.

[![Power pins are on the upper left side of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_PowerPins1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_PowerPins1.jpg)

#### I^2^C

For flexibility, we\'ve broken out the I^2^C functionality as seen below. Primary I^2^C pins are broken out to SDA and SCL:

[![Primary I2C Pins are underneath the Ground and 3V3 pins](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_PrimaryI2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_PrimaryI2C.jpg)

Secondary I^2^C pins are broken out to SDX and SCX. These pins are used solely for Mode 2- Sensor Hub Mode - where the ISM330DHCX reads other sensors. You must cut the SDX and SCX jumpers on the back of the board in order to use this mode.

[![SCX and SDX pins are the bottom two pins on the right side of the front of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_SCX_SDX.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_SCX_SDX.jpg)

#### SPI

Like the I^2^C functionality, we\'ve also broken out the SPI functionality to PTH pins.

SPI Pins for the ISM330DHCX are broken out to SDA, POCI, and the ACS (Accelerometer Chip Select) highlighted here:

[![SDA and POCI are highlighted, as well as the Accelerometer\'s Chip Select](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_SPI_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_SPI_Pins.jpg)

SPI pins for the MMC5983MA are broken out to SDA, POCI, and the MCS (Magnetometer Chip Select) highlighted here:

[![SDA and POCI are highlighted, as well as the Magnetometer\'s Chip Select](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_MMC5983MA_SPI_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_MMC5983MA_SPI_Pins.jpg)

#### Interrupt

Interrupt functionality for the 6DoF accelerometer is available via two PTH pins - INT1 and INT2. INT2 can be configured to an Input/Output pin and can be used to synchronize data for Sensor Hub Mode.

[![Interrupt pins for the Accelerometer are o the top left side of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_ISM330DHCX_InterruptPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_ISM330DHCX_InterruptPins.jpg)

Interrupt functionality for the Magnetometer is available via the MINT pin.

[![Interrupt pin for the Magnetometer is on the left side of the board under the other two interrupt pins and is labeled MINT](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_MMC5983MA_InterruptPin.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_MMC5983MA_InterruptPin.jpg)

### Jumpers

#### LED

If power consumption is an issue, cutting this jumper will disable the Power LED on the front of the board.

[![LED jumper is on the bottom left of the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_LEDJumper1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_LEDJumper1.jpg)

#### I^2^C

Like our other Qwiic boards, the Qwiic Micro Magnetometer comes equipped with pull-up resistors on the clock and data pins. If you are daisy-chaining multiple Qwiic devices, you will want to cut this jumper; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. To disable the pull up resistors, use an X-acto knife to cut the joint between the two jumper pads highlighted here.

[![The I2C jumper is on the right side of middle on the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_I2CJumper1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_I2CJumper1.jpg)

#### I^2^C Address/SPI

By default, I^2^C is enabled with an address of 0x6B. By manipulating this jumper, you can change the I^2^C address to 0x6A (cut the power side and close the ground side) or switch to SPI mode (both jumpers open).

[![The I2C address jumper is on the back of the board below the I2C jumper](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_I2CAddressJumper1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_I2CAddressJumper1.jpg)

#### SCX/SDX

The SCX and SDX pins are specific to Mode 2 of the ISM330DHCX and are used for peripheral communication. By default they are closed - to use Mode 2 you will need to cut both traces to open the jumper.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_SCX-SDXJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_SCX-SDXJumper.jpg)

### Board Outline

Like many of our Qwiic Breakout Boards, the Qwiic 9DoF ISM330DHCX-MMC5983MA measures 1\" x 1\".

-\> [![Board Measures 1 inch by 1inch ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/1/6/19895_9DoF_BoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DoF_BoardOutline.png) \<-

## Hardware Hookup

With the Qwiic connector system, assembling the hardware is simple. All you need to do is connect your [SparkFun Qwiic 9DoF - ISM330DHCX,MMC5983MA](https://www.sparkfun.com/products/19895) to the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) with a [Qwiic cable](https://www.sparkfun.com/products/15081). Otherwise, you can use the I^2^C pins of your microcontroller; just be aware of logic levels.

[![Qwiic cable connects the 9Dof to a Redboard](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_ActionShot1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/6/19895_9DOFIMU_ActionShot1.jpg)

## Software Setup and Programming

**Note:** Make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Both the ICM330DHCX and the MMC5983MA have independent libraries available. You can install either of these libraries through the Arduino Library Manager tool by searching for **\"SparkFun MMC5983MA\"** or **\"SparkFun ISM330DHCX\"**. Users who prefer to manually install can get the libraries from either the GitHub Repositories here:

- [ISM330DHCX Arduino Library GitHub](https://github.com/sparkfun/SparkFun_6DoF_ISM330DHCX_Arduino_Library)
- [MMC5983MA Arduino Library GitHub](https://github.com/sparkfun/SparkFun_MMC5983MA_Magnetometer_Arduino_Library)

or by download the ZIP files by clicking one of the buttons below:

\

[SparkFun 6DoF ISM330DHCX Arduino Library](https://github.com/sparkfun/SparkFun_6DoF_ISM330DHCX_Arduino_Library/archive/refs/heads/main.zip)

[SparkFun Qwiic Micro Magnetometer - MMC5983MA Arduino Library](https://github.com/sparkfun/SparkFun_MMC5983MA_Magnetometer_Arduino_Library/archive/refs/heads/main.zip)

## Examples

The ISM330DHCX and the MMC5983MA each have their own Qwiic Breakout Boards - the [SparkFun 6DoF IMU Breakout - ISM330DHCX (Qwiic)](https://www.sparkfun.com/products/19764) or its Micro Version [SparkFun Micro 6DoF IMU - ISM330DHCX (Qwiic)](https://www.sparkfun.com/products/20176) and the [SparkFun Micro Magnetometer - MMC5983MA (Qwiic)](https://www.sparkfun.com/products/19921) along with corresponding hookup guides and examples.

See the linked tutorials listed below for examples:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/parts/1/9/4/6/6/6DoFIMU_03a.jpg "Qwiic 6DoF - ISM330DHCX Hookup Guide")](https://learn.sparkfun.com/tutorials/qwiic-6dof---ism330dhcx-hookup-guide#examples)   [![](https://cdn.sparkfun.com/assets/parts/1/9/6/5/3/19921_03.jpg "Qwiic Micro Magnetometer - MMC5983MA Hookup Guide")](https://learn.sparkfun.com/tutorials/qwiic-micro-magnetometer---mmc5983ma-hookup-guide#example-1-i2c-simple-measurement)\

  *[Qwiic 6DoF - ISM330DHCX Hookup Guide Examples](https://learn.sparkfun.com/tutorials/qwiic-6dof---ism330dhcx-hookup-guide#examples)*                                                               *[Qwiic Micro Magnetometer - MMC5983MA Hookup Guide Examples](https://learn.sparkfun.com/tutorials/qwiic-micro-magnetometer---mmc5983ma-hookup-guide#example-1-i2c-simple-measurement)*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.