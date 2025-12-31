# Source: https://learn.sparkfun.com/tutorials/sparkfun-triple-axis-accelerometer-breakout---bma400-qwiic-hookup-guide

## Introduction

The SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic) ([Standard](https://www.sparkfun.com/products/21208) and [Micro](https://www.sparkfun.com/products/21207)) offer a 3-axis acceleration sensor perfect for ultra low-power applications on a easy to use Qwiic breakout boards. The Qwiic system allows for integration into your I^2^C system with no soldering required. The standard size Qwiic breakout also includes 0.1\"-spaced PTH pins connected to the sensor\'s communication interface and interrupt pins for applications that require a traditional soldered connection.

[![SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/9/7/1/21208_SEN-_01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-bma400-qwiic.html)

### [SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-bma400-qwiic.html) 

[ SEN-21208 ]

he SparkFun Qwiic BMA400 Triple Axis Accelerometer Breakout offers a 3-axis acceleration sensor perfect for ultra-low-power a...

[ [\$10.50] ]

[![SparkFun Micro Triple Axis Accelerometer Breakout - BMA400 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/9/7/0/21207_SEN-_01.jpg)](https://www.sparkfun.com/sparkfun-micro-triple-axis-accelerometer-breakout-bma400-qwiic.html)

### [SparkFun Micro Triple Axis Accelerometer Breakout - BMA400 (Qwiic)](https://www.sparkfun.com/sparkfun-micro-triple-axis-accelerometer-breakout-bma400-qwiic.html) 

[ SEN-21207 ]

The SparkFun Qwiic BMA400 Micro Triple Axis Accelerometer Breakout offers a 3-axis acceleration sensor perfect for ultra-low-...

[ [\$10.50] ]

The BMA400 from Bosch Sensortech^©^ has a full scale acceleration range of ±2/±4/±8/±16g with exceptionally low current consumption of \< 14.5µA while operating at its highest performance settings. The sensor also includes a complete feature set for on-chip interrupts including step counter, activity recognition, orientation detection and tap/double tap.

This guide will go into detail on the features of the BMA400 and hardware on these boards as well as how to integrate it into a Qwiic circuit using the SparkFun BMA400 Arduino Library.

### Required Materials

To follow along with this guide you will need a microcontroller to communicate with the BMA400. Below are a few options that come Qwiic-enabled out of the box:

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![SparkFun Thing Plus - Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/1/7/0/15574-SparkFun_Thing_Plus_-_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html)

### [SparkFun Thing Plus - Artemis](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html) 

[ WRL-15574 ]

The SparkFun Artemis Thing Plus takes our popular Feather footprint and adds in the powerful Artemis module for ultimate func...

[ [\$25.95] ]

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

If your chosen microcontroller is not already Qwiic-enabled, you can add that functionality with one or more of the following items:

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![SparkFun Qwiic Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/5/1/14495-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-adapter.html)

### [SparkFun Qwiic Adapter](https://www.sparkfun.com/sparkfun-qwiic-adapter.html) 

[ DEV-14495 ]

The SparkFun Qwiic Adapter provides the perfect means to make any old I^2^C board into a Qwiic enabled board.

[ [\$1.60] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

[![SparkFun Qwiic Shield for Thing Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/7/16790-SparkFun_Qwiic_Shield_for_Thing_Plus-05.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-thing-plus.html)

### [SparkFun Qwiic Shield for Thing Plus](https://www.sparkfun.com/sparkfun-qwiic-shield-for-thing-plus.html) 

[ DEV-16790 ]

The SparkFun Qwiic Shield for Thing Plus makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards t...

[ [\$5.10] ]

You will also need at least one Qwiic cable to connect your sensor to your microcontroller.

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend taking a look at the following tutorials if you aren\'t familiar with the concepts covered in them. If you are using one of the Qwiic Shields listed above, you may want to read through their respective Hookup Guides as well before you get started with the SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic).

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

[](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-shield-for-arduino-nano-hookup-guide)

### SparkFun Qwiic Shield for Arduino Nano Hookup Guide 

Hookup Guide for the SparkFun Qwiic Shield for Arduino Nano.

## Hardware Overview

Let\'s take a closer look at the BMA400 and other hardware features on these Qwiic breakouts.

### BMA400 3-Axis Accelerometer

The BMA400 3-axis accelerometer from Bosch Sensortec is an ultra-low power motion sensor with a host of interrupt features making it ideal for battery-powered activity monitoring applications.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Highlighting the BMA400 on the standard Qwiic breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Sensor.jpg)   ![Highlighting the BMA400 on the Qwiic Micro breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/9/Qwiic_Micro_BMA400_-_Sensor.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The BMA400 features four user-selectable ranges of ±2/±4/±8/±16g and consumes just 14.5µA when measuring acceleration data at the highest performance settings. The BMA400 also includes a robust interrupt feature set:

- Auto Wakeup
- Auto Low Power
- Step Counter
- Activity Recognition (Running, Walking, Standing Still)
- Orientation Detection
- Tap and Double Tap

The sensor has two interrupt pins available for all of the above interrupt conditions. The table below outlines a few of the BMA400\'s sensing and operating parameters. For a full overview of the BMA400, refer to the [datasheet](https://cdn.sparkfun.com/assets/e/9/e/6/0/BMA400-Datasheet.pdf).

+-----------------------------+------+-------+------+-------+-------------------------------+
| Parameter                   | Min. | Typ.  | Max. | Units | Notes                         |
+=============================+:====:+:=====:+:====:+:=====:+===============================+
| Supply Voltage              | 1.72 | 1.8   | 3.6  | V     | Breakouts run BMA400 at 3.3V. |
+-----------------------------+------+-------+------+-------+-------------------------------+
| Normal Mode Current Draw    |      | 14.5  |      | µA    | Oversampling Rate set to 3    |
+-----------------------------+------+-------+------+       +-------------------------------+
| Low-Power Mode Current Draw |      | 0.850 |      |       | Oversampling Rate set to 0    |
+-----------------------------+------+-------+------+       +-------------------------------+
| Sleep Mode Current Draw     |      | 0.160 |      |       |                               |
+-----------------------------+------+-------+------+-------+-------------------------------+
| Acceleration Range          |      | ±2    |      | g     | Sensitivity of 1024LSB/g      |
|                             +------+-------+------+       +-------------------------------+
|                             |      | ±4    |      |       | Sensitivity of 512LSB/g       |
|                             +------+-------+------+       +-------------------------------+
|                             |      | ±8    |      |       | Sensitivity of 256LSB/g       |
|                             +------+-------+------+       +-------------------------------+
|                             |      | ±16   |      |       | Sensitivity of 128LSB/g       |
+-----------------------------+------+-------+------+-------+-------------------------------+
| Output Data Rate (ODR)      | 12.5 |       | 800  | Hz    | ODR in Low-Power mode is 25Hz |
+-----------------------------+------+-------+------+-------+-------------------------------+

### Communication Interfaces - I^2^C & SPI

The standard size version of these Qwiic breakouts communicates over I^2^C by default but also supports communicating using SPI. The Qwiic Micro version only supports I^2^C communication over the Qwiic connector on the board.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Highlighting the communication interfaces on the standard Qwiic breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Interfaces.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Interfaces.jpg)   ![Highlighting the communication interfaces on the Qwiic Micro breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/9/Qwiic_Micro_BMA400_-_Interfaces.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The standard size routes the I^2^C interface to a pair of Qwiic connectors as well as a 0.1\"-spaced PTH header for users who prefer SPI or a traditional soldered connection. The standard-size breakout routes both INT1 and INT2 to a pair of PTH pins. The Qwiic Micro routes only INT1 to a PTH pin.

Both boards set the BMA400\'s I^2^C address to **0x14** by default. Adjust the ADR jumper to change to the alternate address (**0x15**) or open it completely to use the SPI interface (Standard size only). More information on this jumper in the Solder Jumpers section below.

### Solder Jumpers

The Standard size breakout has four solder jumpers labeled **PWR**, **ADR**, **I2C**, and **CS**. The Micro size has all but the **CS** jumper as the Micro version does not support SPI. Instead, the Micro version pulls the CS pin to **3.3V**. The table below outlines the jumpers\' labels, default state, functionality, and any notes regarding their use.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Highlighting the solder jumpters on the standard Qwiic breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Solder_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Solder_Jumpers.jpg)   ![Highlighting the solder jumpers on the Qwiic Micro breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/9/Qwiic_Micro_BMA400_-_Solder_Jumpers.jpg)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Label   Default State   Function                                                                          Notes
  ------- --------------- --------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PWR     CLOSED          Completes the Power LED circuit.                                                  Open to disable the Power LED.
  ADR     SEE NOTE        Sets the sensor\'s I^2^C address.                                                 Address is 0x14 by default. Switch to 0x15 by severing the trace between the \"Center\" and \"Left\" pads and connecting the \"Center\" and \"Right\" pads. Leave open entirely to use the BMA400 over SPI (Standard size only.)
  I2C     CLOSED          Ties the SDA/SCL lines to VCC (3.3V) through a pair of 2.2kΩ resistors.           Open the jumper to disable the pull-up resistors on the I2C lines.
  CS\*    CLOSED          Pulls the BMA400\'s chip select (CS) pin to VCC (3.3V) through a 10kΩ resistor.   \*Standard size only. Open to disable the pull-up on CS.

### Board Dimensions

The boards match the Standard and Micro form-factors for Qwiic breakouts measuring 1\" x 1\" (Standard) and 0.5\" x 0.3\" (Micro). The Standard breakout has four mounting holes and the Micro has one. All mounting holes fit a size [4-40](https://www.sparkfun.com/products/10453) screw.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Standard Qwiic breakout dimensions.](https://cdn.sparkfun.com/r/600-600/assets/7/a/3/1/e/SparkFun_Triple_Axis_Accelerometer_Breakout_-_BMA400__Qwiic__Dimensions.png)](https://cdn.sparkfun.com/assets/7/a/3/1/e/SparkFun_Triple_Axis_Accelerometer_Breakout_-_BMA400__Qwiic__Dimensions.png)   ![Qwiic Micro breakout dimensions.](https://cdn.sparkfun.com/r/600-600/assets/6/8/c/2/2/SparkFun_Micro_Triple_Axis_Accelerometer_Breakout_-_BMA400__Qwiic__Dimensions.png)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Hardware Assembly

Now that we\'re familiar with the BMA400, we can start assembling our circuit.

### Qwiic/I^2^C Assembly

The fastest and easiest way to get started using the breakout is to connect the Qwiic connector on the breakout to a Qwiic-enabled development board like the SparkFun RedBoard Artemis with a Qwiic cable and as shown in the image below.

[![Completed Qwiic circuit with the RedBoard Artemis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Assembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Assembly.jpg)

If you would prefer a more secure and permanent connection with the Standard Size breakout, you can solder headers or wire to the PTH header on the board.

### SPI Assembly (Standard Size Only)

Setting the breakout up to communicate with the sensor over SPI requires completely opening the ADR jumper and we recommend soldering to the PTH header to make the connections. If you are not familiar with through-hole soldering, take a read through this tutorial:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

Along with tools for soldering, you\'ll need either some hookup wire or headers and jumper wires. Sever the trace between the \"Center\" and \"Right\" pads of the ADR jumper to switch to SPI mode. After opening this jumper, connect the breakout to your controller\'s SPI bus pins.

Remember, the BMP384 operates at **3.3V logic** so make sure to connect to a board running at the same [logic level](https://learn.sparkfun.com/tutorials/logic-levels) like the [RedBoard Artemis](https://www.sparkfun.com/products/15444) or use a [level shifter](https://www.sparkfun.com/categories/361) to adjust it to the correct voltage.

[![Highlighting the ADR jumper on the Standard BMA400 Breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Address_Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/9/Qwiic_BMA400_-_Address_Jumper.jpg)

*Open the ADR jumper completely to use SPI.*

## BMA400 Arduino Library

**Note:** This library assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The SparkFun BMA400 Arduino Library is based off the API for the sensor from Bosch to let users get started reading data from the sensor and using the various interrupt options. Install the library through the Arduino Library Manager tool by searching for **\"SparkFun BMA400\"**. Users who prefer to manually install the library can download a copy of it from the GitHub repository by clicking the button below:

[SparkFun BMA400 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_BMA400_Arduino_Library/archive/refs/heads/main.zip)

### Library Functions

The list below outlines and describes the functions available in the SparkFun BMA400 Arduino Library. For detailed information on the available parameters and use of all functions, refer to the [.cpp file in the library](https://github.com/sparkfun/SparkFun_BMA400_Arduino_Library/blob/main/src/SparkFun_BMA400_Arduino_Library.cpp).

#### Sensor Initialization and Configuration

- `int8_t BMA400::beginI2C(uint8_t address, TwoWire& wirePort);` - Initialize the sensor over I^2^C at the specified address and port.
- `int8_t BMA400::beginSPI(uint8_t csPin, uint32_t clockFrequency);` - Initialize the sensor over SPI with the specified Chip Select pin and clock frequency.
- `int8_t setMode(uint8_t mode);` - Set the power mode.
- `int8_t getMode(uint8_t* mode);` - Returns the setting for power mode.
- `int8_t setAutoWakeup(bma400_auto_wakeup_conf* config);` - Enable Auto Wakeup.
- `int8_t setAutoLowPower(bma400_auto_lp_conf* config);` - Enable Auto Low Power
- `int8_t setRange(uint8_t range);` - Set the measurement range.
- `int8_t getRange(uint8_t* range);` - Returns the value stored for measurement range.
- `int8_t setODR(uint8_t odr);` - Set the output data rate.
- `int8_t getODR(uint8_t* odr);` - Returns the value stored for output data rate.
- `int8_t setOSRLP(uint8_t osrLP);` - Set the output data rate for Low Power.
- ` int8_t getOSRLP(uint8_t* osrLP);` - Returns the value stored for output data rate for Low Power.
- `int8_t setDataSource(uint8_t source);` - Set the data source filter. Options are Default with variable ODR, 100Hz ODR, and 100Hz with 1Hz bandwidth.
- `int8_t getDataSource(uint8_t* source);` - Returns the value for data source.
- `int8_t setFilter1Bandwidth(uint8_t bw);` - Set the low pass filter bandwidth.
- `int8_t getFilter1Bandwidth(uint8_t* bw);` - Returns the value set for low pass filter bandwidth.
- `int8_t getStepCount(uint32_t* count, uint8_t* activityType);` - Returns the number of steps measured along with activity type (Still, Walk, and Run).
- `int8_t selfTest();` - Runs self test to determine if the sensor is behaving correctly.

#### Sensor Data

- `int8_t getSensorData(bool sensorTime = false);` - Requests acceleration data from the BMA400. This must be called to update the data structure.
- `int8_t getTemperature(float* temp);` - Returns the temperature data recorded in °C.

#### Interrupt Control and Feature Selection

- `int8_t setInterruptPinMode(bma400_int_chan channel, uint8_t mode);` - Set the interrupt pin mode. Options are push/pull and active high/low.
- `int8_t enableInterrupt(bma400_int_type intType, bool enable);` - Enable interrupt condition.
- `int8_t getInterruptStatus(uint16_t* status);` - Returns interrupt status flags for the various interrupt conditions (wakeup, activity, step, etc.).
- `int8_t setDRDYInterruptChannel(bma400_int_chan channel);` - Select the interrupt pin for the data ready interrupt condition.
- `int8_t setGeneric1Interrupt(bma400_gen_int_conf* config);` - Set the generic 1 interrupt configuration.
- `int8_t setGeneric2Interrupt(bma400_gen_int_conf* config);` - Set the generic 2 interrupt configuration.
- `int8_t setOrientationChangeInterrupt(bma400_orient_int_conf* config);` - Set the orientation change interrupt configuration.
- `int8_t setTapInterrupt(bma400_tap_conf* config);` - Set the tap interrupt configuration.
- `int8_t setStepCounterInterrupt(bma400_step_int_conf* config);` - Set the step counter interrupt configuration.
- `int8_t setActivityChangeInterrupt(bma400_act_ch_conf* config);` - Set the activity change interrupt configuration.
- `int8_t setWakeupInterrupt(bma400_wakeup_conf* config);` - Set the device wakeup interrupt configuration.

#### FIFO Buffer Control

- `int8_t setFIFOConfig(bma400_fifo_conf* config);` - Enable and configure the FIFO buffer.
- `int8_t getFIFOLength(uint16_t* numData);` - Set the number of samples to store in the FIFO buffer.
- `int8_t getFIFOData(BMA400_SensorData* data, uint16_t* numData);` - Pull data stored in FIFO buffer.
- `int8_t flushFIFO();` - Flush the FIFO buffer.

## Arduino Examples

The BMA400 Arduino Library includes twelve examples covering all major features of the accelerometer. In this section we\'ll take a closer look at three of them.

### Example 1 - Basic Readings I^2^C

Example 1 demonstrates how to set the BMA400 up to communicate basic motion data over I^2^C. Open the example by navigating to **File \> Examples \> SparkFun BMA400 Arduino Library \> Example01_BasicReadingsI2C**. Select your Board and Port and click Upload. Open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) after the upload completes with the baud set to **115200** to watch motion data print out.

If you have adjusted the ADR jumper to change to the alternate I^2^C address for the BMA400 comment/uncomment the line with the correct value:

    language:c
    uint8_t i2cAddress = BMA400_I2C_ADDRESS_DEFAULT; // 0x14
    //uint8_t i2cAddress = BMA400_I2C_ADDRESS_SECONDARY; // 0x15

The example attempts to initialize the sensor with default settings in I^2^C at the specified address. If it cannot initialize properly, the code prints out an error in over serial:

    language:c
    while(accelerometer.beginI2C(i2cAddress) != BMA400_OK)
        

If you see this error, double check the sensor is connected properly and set to the correct I^2^C address and reset the development board or re-upload the code.

The loop polls the BMA400 for acceleration data every 20ms using the \'getSensorData();\' function and prints out acceleration for all three axes in g\'s:

    language:c
    void loop()
    

Move the sensor around in different directions and watch the acceleration data change with the motion.

### Example 6 - Motion Detection

Example 6 - Motion Detection demonstrates how to configure one of the BMA400\'s interrupt pins (INT1) to trigger when the sensor detects motion over 1g on the Z axis.

The code defaults to use \'D2\' as the interrupt pin on a connected development board. If your development board does not support external interrupts on \'D2\' change the value here:

    language:c
    int interruptPin = 2;

If you\'re not sure which pins on your board support external interrupts, [this reference page](https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/) has lists available interrupt pins for most common Arduino development boards.

After initializing the BMA400 over I^2^C, the code configures the interrupt feature:

    language:c
    bma400_gen_int_conf config =
        ;
        accelerometer.setGeneric1Interrupt(&config);

        // Here we configure the INT1 pin to push/pull mode, active high
        accelerometer.setInterruptPinMode(BMA400_INT_CHANNEL_1, BMA400_INT_PUSH_PULL_ACTIVE_1);

        // Enable generic 1 interrupt condition
        accelerometer.enableInterrupt(BMA400_GEN1_INT_EN, true);

        // Setup interrupt handler
        attachInterrupt(digitalPinToInterrupt(interruptPin), bma400InterruptHandler, RISING);

This configures INT1 to operate in push/pull mode and active HIGH whenever the BMA400 reports motion the Z axis over 1g among other settings. It also enables the interrupt condition and sets up the interrupt handler.

The main loop waits for an interrupt event to happen and prints out whenever an interrupt occurs and motion is detected.

### Example 10 - Step Counter

Example 10 - Step Counter shows how to use the BMA400\'s Step Counter feature commonly found in smart watches and other activity monitors. The sensor handles step detection and counting so we\'ll leave those settings as default. They can technically be altered but we do not recommend it as it\'s not well documented and can cause unpredictable behavior.

After initializing the sensor, we select and configure INT1 for interrupts and enable step counting:

    language:c
    bma400_step_int_conf config =
        ;
        accelerometer.setStepCounterInterrupt(&config);

        // Here we configure the INT1 pin to push/pull mode, active high
        accelerometer.setInterruptPinMode(BMA400_INT_CHANNEL_1, BMA400_INT_PUSH_PULL_ACTIVE_1);

        // Enable step counter interrupt condition. This must be set to enable step
        // counting at all, even if you don't want interrupts to be generated.
        // In that case,  set the interrupt channel above to BMA400_UNMAP_INT_PIN
        accelerometer.enableInterrupt(BMA400_STEP_COUNTER_INT_EN, true);

        // Setup interrupt handler
        attachInterrupt(digitalPinToInterrupt(interruptPin), bma400InterruptHandler, RISING);

The main loop checks for a step detection interrupt event and prints the step count and activity type over serial. Try moving the sensor around or attach it to your wrist to simulate a smart watch and walk/run around. You should see the data update with new step values and activity states.

## Troubleshooting

### General Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\