# Source: https://learn.sparkfun.com/tutorials/qwiic-6dof---ism330dhcx-hookup-guide

## Introduction

Do you need 6 degrees of freedom? We do! Behold the [SparkFun Qwiic 6DoF - ISM330DHCX](https://www.sparkfun.com/products/19764) and the [SparkFun Micro 6DoF IMU Breakout - ISM330DHCX (Qwiic)](https://www.sparkfun.com/products/20176) - both of which are Qwiic enabled breakouts featuring STMicroelectronics\' ISM330DHCX; a high-performance 3D digital accelerometer and 3D digital gyroscope tailored for Industry 4.0 applications such as platform, optical image, and lens stabilization, robotics and industrial automation, navigations systems, and vibration monitoring and compensation.

[![SparkFun 6DoF IMU Breakout - ISM330DHCX (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/4/6/6/6DoFIMU_03a.jpg)](https://www.sparkfun.com/sparkfun-6dof-imu-breakout-ism330dhcx-qwiic.html)

### [SparkFun 6DoF IMU Breakout - ISM330DHCX (Qwiic)](https://www.sparkfun.com/sparkfun-6dof-imu-breakout-ism330dhcx-qwiic.html) 

[ SEN-19764 ]

The SparkFun Qwiic ISM330DHCX 6DoF IMU is a standard-sized, 1\"x1\" breakout featuring a high-performance 3D digital accelerome...

[ [\$25.50] ]

[![SparkFun Micro 6DoF IMU - ISM330DHCX (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/9/7/9/20176_Diag.jpg)](https://www.sparkfun.com/sparkfun-micro-6dof-imu-ism330dhcx-qwiic.html)

### [SparkFun Micro 6DoF IMU - ISM330DHCX (Qwiic)](https://www.sparkfun.com/sparkfun-micro-6dof-imu-ism330dhcx-qwiic.html) 

[ SEN-20176 ]

The SparkFun Qwiic Micro ISM330DHCX Six Degrees of Freedom IMU is a micro-sized 0.75in. by 0.30in. sensor featuring STMicroel...

[ [\$26.50] ]

Both of these accelerometers have a full-scale acceleration range of ±2/±4/±8/±16 g and a wide angular rate range of ±125/±250/±500/±1000/±2000/±4000 dps that enable its usage in a broad range of applications. An unmatched set of embedded features (Machine Learning Core, programmable FSM, FIFO, sensor hub, event decoding and interrupts) are enablers for implementing smart and complex sensor nodes which deliver high performance at very low power.

The full sized SparkFun Qwiic 6DoF - ISM330DHCX boasts the standard 1x1\" form factor, while the Micro 6DoF IMU breakout clocks in at a teeny tiny 0.75 x 0.3 inches!

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

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX.jpg "ISM330DHCX is in the center of the board")](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-Processor.jpg "ISM330DHCX is in the center of the board")](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-Processor.jpg)\

  *ISM330DHCX on the Qwiic 6DoF 1x1\" Breakout*                                                                                                                                                                            *ISM330DHCX on the Qwiic Micro 6DoF Breakout*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The ISM330DHCX can run in four different modes:

#### Mode 1

This is the default \"peripheral only\" mode. This mode allows you to use either I^2^C or SPI. By default, I^2^C is enabled with an address of 0x6B. By manipulating the associated jumper, you can change the I^2^C address to 0x6A (cut the power side and close the ground side) or switch to SPI mode (both jumpers open).

#### Mode 2

This mode enables a secondary I^2^C port that the 6DoF controls; up to 4 external sensors can be connected to the I^2^C controller interface of the device. External sensors communicate via the SCX and SDX (PICOX) lines - the SCX jumper will need to be opened.

#### Modes 3 & 4

In addition to the primary I²C peripheral interface or SPI (3- / 4-wire) serial interface, an auxiliary SPI (3- / 4-wire) serial interface is available for external device connections (i.e. camera module). Mode 3 is available for gyroscope only, Mode 4 is available for both gyroscope and accelerometer.

### Qwiic Connectors

Our [Qwiic Ecosystem](https://www.sparkfun.com/qwiic) makes sensors pretty much plug and play. There are two Qwiic connectors on the side of the Qwiic 6DoF - ISM330DHCX board and one Qwiic connector on the side of the Qwiic Micro 6DoF to provide power and I^2^C connectivity simultaneously.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_QwiicConnectors.jpg "Qwiic connectors on either side of the board")](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_QwiicConnectors.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-QwiicConnector.jpg "ISM330DHCX is in the center of the board")](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-QwiicConnector.jpg)\

  *Qwiic connectors on the Qwiic 6DoF 1x1\" Breakout*                                                                                                                                                                                                          *Qwiic connector on the Qwiic Micro 6DoF Breakout*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### GPIO

#### Power

Ideally, power will be supplied via the Qwiic connectors, but we\'ve also broken out plated through hole pins to supply 3.3V and Ground, should you prefer. Make sure to pay attention to logic levels - supply voltage to this board should range from **1.71 V to 3.6 V**.

[![Power pins are highlighted](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-PowerPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-PowerPins.jpg)

#### I^2^C

For flexibility, we\'ve broken out the I^2^C functionality as seen below. Primary I^2^C pins are broken out to SDA and SCL:

[![I2C pins are highlighted](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-I2CPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-I2CPins.jpg)

Secondary I^2^C pins are broken out to SDX/PICOX and SCX. These pins are used solely for Mode 2- Sensor Hub Mode - where the 6DoF reads other sensors. You must cut the PICOX and SCX jumpers on the back of the board in order to use this mode.

[![PICOX and SCX are highlihgted](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-SecondaryI2CPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-SecondaryI2CPins.jpg)

#### SPI

Like the I^2^C functionality, we\'ve also broken out the SPI functionality to PTH pins on either side of the board.

[![SPI pins are CS, SDA, and POCI](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-SPIPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-SPIPins.jpg)

#### OCS, PICOX, and POCIX

OCS is the enable pin for Modes 3 and 4. POCIX is used for one way communication in Mode 3, PICOX and POCIX are used for 2-way communication in Mode 4.

[![OCS, PICOX, and POCIX pins are highlighted](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-OCS-PICOX-POCIXPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-OCS-PICOX-POCIXPins.jpg)

#### Interrupt Pins: Qwiic 6DoF - ISM330DHCX

Interrupt generation can be sourced by the gyroscope or accelerometer; for interrupt-generation purposes, the accelerometer/gyroscope sensor has to be set in an active operating mode (not in Power-Down). In addition, the second interrupt pin can also generate signals for the accelerometer and gyroscope, but also for the temperature sensor.

The second interrupt (INT2) can also be configured as an *INPUT* to the 6DoF. This is primarily used in sensor-hub mode (Mode 2) as a way of signaling that data is ready on one of the attached sensors.

The interrupt generator can be configured to detect:

- Free-fall;
- Wake-up;
- 6D/4D orientation detection;
- Single-tap and double-tap sensing;
- Activity/Inactivity and Motion/Stationary recognition

[![Interrupt pins are highlighted](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-InterruptPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_GPIO-InterruptPins.jpg)

#### Interrupt Pin: Micro 6DoF IMU Breakout - ISM330DHCX (Qwiic)

We\'ve broken out a single PTH pin for Interrupt functionality on the Qwiic 6DoF - ISM330DHCX Micro Breakout.

[![Interrupt pin on the 6DoF Micro](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-InterruptPin.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-InterruptPin.jpg)

### Jumpers

#### I^2^C

Like our other Qwiic boards, the Qwiic 6DoF - ISM330DHCX comes equipped with pull-up resistors on the clock and data pins. If you are daisy-chaining multiple Qwiic devices, you will want to cut this jumper; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. To disable the pull up resistors, use an X-acto knife to cut the joint between the two jumper pads highlighted below.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_Jumper-I2C.jpg "I2C Jumper is highlighted on the back of the board")](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_Jumper-I2C.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-I2CJumper.jpg "I2C Jumper is highlighted on the back of the board")](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-I2CJumper.jpg)\

  *I^2^C Jumper on the Qwiic 6DoF 1x1\" Breakout*                                                                                                                                                                                                          *I^2^C Jumper on the Qwiic Micro 6DoF Breakout*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### LED

If power consumption is an issue, cutting this jumper will disable the Power LED on the front of the board.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_Jumper-LED.jpg "LED jumper is highlighted on the back of the board")](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_Jumper-LED.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-LEDJumper.jpg "LED jumper is highlighted on the back of the board")](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-LEDJumper.jpg)\

  *LED Jumper on the Qwiic 6DoF 1x1\" Breakout*                                                                                                                                                                                                            *LED Jumper on the Qwiic Micro 6DoF Breakout*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### I^2^C Address/SPI - Qwiic 6DoF

By default, I^2^C is enabled with an address of 0x6B. By manipulating this jumper, you can change the I^2^C address to 0x6A (cut the power side and close the ground side) or switch to SPI mode (both jumpers open).

[![6A vs 6B jumper is highlights on the back of the board](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_Jumper-6A6B.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_Jumper-6A6B.jpg)

#### I^2^C Address - Qwiic Micro 6DoF

SPI is not available on the Qwiic Micro Breakout, but you can select the I^2^C address on the back of the board by closing either side of this trace.

Address

1

VDD

0x6B

0

GND

0x6A

OPEN

SPI Not Supported

[![The I2C address jumper is just below the I2C Jumper on the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-InterruptJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_Micro6DoF_Qwiic-InterruptJumper.jpg)

#### SCX/PICOX

The SCX and PICOX pins are specific to Mode 2 and are used for peripheral communication. By default they are closed - to use Mode 2 you will need to cut both traces to open the jumper.

[![SCX and PICOX jumpers on the back of the board](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_Jumper-SCXPICOX.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_ISM330DHCX_Jumper-SCXPICOX.jpg)

### Board Outline

The Qwiic 6DoF - ISM330DHCX Breakout measures 1\" x 1\".

[![This board measures 1 inch by 1 inch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/8/4/19764_BoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/19764_BoardOutline.png)

The Micro 6DoF IMU Breakout - ISM330DHCX (Qwiic) measures 0.75\" x 0.3\".

[![This teensy little guy measures 0.75\" x 0.3\"](https://cdn.sparkfun.com/r/600-600/assets/b/d/d/6/d/6DoF_Qwiic_Micro_BoardOutline.png)](https://cdn.sparkfun.com/assets/b/d/d/6/d/6DoF_Qwiic_Micro_BoardOutline.png)

## Hardware Hookup

With the Qwiic connector system, assembling the hardware is simple. All you need to do is connect either your [SparkFun Qwiic 6DoF - ISM330DHCX](https://www.sparkfun.com/products/19764) or your [SparkFun Micro 6DoF IMU Breakout - ISM330DHCX (Qwiic)](https://www.sparkfun.com/products/20176) to the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) with a [Qwiic cable](https://www.sparkfun.com/products/15081). Otherwise, you can use the I^2^C pins of your microcontroller; just be aware of logic levels.

[![6DoF is connected to the redboard qwiic via a qwiic cable ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/8/4/6DoFIMU_05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/6DoFIMU_05.jpg)

[![6DoF Micro is connected to the redboard qwiic via a qwiic cable](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_ActionShot.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/20176_ActionShot.jpg)

## Software Setup and Programming

**Note:** Make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We\'ve written a simple Arduino library to quickly get started reading data from the ISM330DHCX. Install the library through the Arduino Library Manager tool by searching for **\"SparkFun Qwiic 6DoF - ISM330DHCX\"**. Users who prefer to manually install it can get the library from the [GitHub Repository](https://github.com/sparkfun/SparkFun_6DoF_ISM330DHCX_Arduino_Library) or download the ZIP by clicking the button below:

\

[SparkFun 6DoF ISM330DHCX Arduino Library](https://github.com/sparkfun/SparkFun_6DoF_ISM330DHCX_Arduino_Library/archive/refs/heads/main.zip)

## Examples

### Example 1 - Basic Reading

The first example initializes the 6DoF to communicate over I^2^C with default settings. Open the example by navigating to **File** **Examples \> SparkFun 6DOF ISM330DHCX \> example1_basic**. Select your Board and Port and click upload.

[![You can find example one by going to the File menu, then choose examples, SparkFun 6DoF ISM330DHCX, then example1_basic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/8/4/Example_1_Menu.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/Example_1_Menu.jpg)

Open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) after the upload completes with the baud set to **115200** to watch data print out.

[![You should see accelerometer and gyroscope readings flashing by](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/8/4/Example_1_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/8/4/Example_1_Output.jpg)

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.