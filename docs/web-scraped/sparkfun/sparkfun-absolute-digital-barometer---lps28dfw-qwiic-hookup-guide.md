# Source: https://learn.sparkfun.com/tutorials/sparkfun-absolute-digital-barometer---lps28dfw-qwiic-hookup-guide

## Introduction

The SparkFun Absolute Digital Barometer - LPS28DFW (Qwiic) ([Standard Size](https://www.sparkfun.com/products/21221) and [Micro Size](https://www.sparkfun.com/products/21222)) offer a unique barometer breakout featuring the LPS28DFW from STMicroelectronics^©^. The LPS28DFW is an absolute barometer with a water-resistant package making it perfect for pressure measurement applications where the sensor is exposed to or even submerged in water^[1](#LPS28DFW_Note1)^.

[![SparkFun Absolute Digital Barometer - LPS28DFW (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/9/7/7/21221_SEN-_Barometer-_01.jpg)](https://www.sparkfun.com/sparkfun-absolute-digital-barometer-lps28dfw-qwiic.html)

### [SparkFun Absolute Digital Barometer - LPS28DFW (Qwiic)](https://www.sparkfun.com/sparkfun-absolute-digital-barometer-lps28dfw-qwiic.html) 

[ SEN-21221 ]

The SparkFun Qwiic LPS28DFW Absolute Digital Barometer offers a unique barometer breakout featuring the LPS28DFW from STMicro...

[ [\$19.95] ]

[![SparkFun Micro Absolute Digital Barometer - LPS28DFW (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/9/7/8/21222_SEN-_Mirco_Barometer-_01.jpg)](https://www.sparkfun.com/sparkfun-micro-absolute-digital-barometer-lps28dfw-qwiic.html)

### [SparkFun Micro Absolute Digital Barometer - LPS28DFW (Qwiic)](https://www.sparkfun.com/sparkfun-micro-absolute-digital-barometer-lps28dfw-qwiic.html) 

[ SEN-21222 ]

The SparkFun Qwiic LPS28DFW Micro Absolute Digital Barometer offers a unique barometer breakout featuring the LPS28DFW from S...

[ [\$20.95] ]

The sensor has two full-scale measurement ranges of 260 - 1260hPa and 260 - 4060hPa with an absolute pressure accuracy of 0.5hPa. The LPS28DFW is composed a piezoresistive pressure sensor with a metal lid and gel encasing to protect the sensing elements from water and other environmental hazards.

In this guide we\'ll cover the features and specifications of the LPS28DFW and other hardware present on these Qwiic breakouts as well as the Arduino library we have written to interact with the sensor.

[][**1.**](https://learn.sparkfun.com/tutorials/sparkfun-absolute-digital-barometer---lps28dfw-qwiic-hookup-guide#LPS28DFW_Note1) **Important!** While the LPS28DFW is protected from water, the rest of the components on these breakouts are not protected by any conformal coating and can be damaged by exposure to liquids. Users who intend to use these breakouts in applications where the board may be exposed to water or other liquids should apply conformal coating to the board prior to use.

### Required Materials

To follow along with this guide you will need a microcontroller to communicate with the LPS28DFW. Below are a few options that come Qwiic-enabled out of the box:

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

You will also need at least one Qwiic cable to connect the breakout to your microcontroller.

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

We would also recommend taking a look at the following tutorials if you aren\'t familiar with the concepts covered in them. If you are using one of the Qwiic Shields listed above, you may want to read through their respective Hookup Guides as well before you get started with the SparkFun Absolute Digital Barometer - LPS28DFW (Qwiic).

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

In this section we\'ll take a closer look at the LPS28DFW and other hardware on these Qwiic breakouts.

### LPS28DFW Absolute Pressure Sensor

The LPS28DFW from STMicroelectronics is a digital output absolute pressure sensor with a gel-filled metal lid protecting the sensing element from moisture making it ideal for applications such as water depth measurements or other pressure-sensing projects in wet environments.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Highlighting the LPS28DFW on the standard breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Sensor.jpg)   [![Highlighting the LPS28DFW on the micro breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/0/Qwiic_Micro_LPS28DFW_-_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/0/Qwiic_Micro_LPS28DFW_-_Sensor.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The LPS28DFW has two user-selectable measurement ranges (260 to 1260hPa and 260 to 4060hPa) with an absolute pressure accuracy of 0.5hPa and supports output data rates of 1 to 200Hz. The sensor supports communication over I^2^C and MIPI I3C^SM^ interfaces (though I3C communication is not covered in this guide or the Arduino Library). The table below outlines some of the parameters for the LPS28DFW. For a complete overview of the sensor, refer to the [datasheet](https://cdn.sparkfun.com/assets/a/4/0/b/b/LPS28DFW-Datasheet.pdf).

+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+
| Parameter                   | Min.   | Typ.   | Max.   | Units   | Notes                                                     |
+=============================+:======:+:======:+:======:+:=======:+===========================================================+
| Supply Voltage              | 1.7    | \-     | 3.6    | V       | Breakouts run the sensor at 3.3V                          |
+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+
| Supply Current              | \-     | 1.7    | \-     | µA      | Average Selection (AVG)=4 and Output Data Rate (ODR)=1Hz. |
|                             +--------+--------+--------+         +-----------------------------------------------------------+
|                             | \-     | 9.4    | \-     |         | AVG=128 and ODR=1Hz.                                      |
|                             +--------+--------+--------+         +-----------------------------------------------------------+
|                             | \-     | 0.9    | \-     |         | Sensor in power-down mode.                                |
+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+
| Operating Temperature Range | -40    | \-     | +85    | °C      |                                                           |
+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+
| Operating Pressure Range                                                                                                     |
+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+
| Mode 1                      | 260    | \-     | 1260   | hPa     |                                                           |
+-----------------------------+--------+--------+--------+         +-----------------------------------------------------------+
| Mode 2                      | 260    | \-     | 4060   |         |                                                           |
+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+
| Pressure Sensitivity                                                                                                         |
+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+
| Mode 1                      | \-     | 4096   | \-     | LSB/hPa |                                                           |
+-----------------------------+--------+--------+--------+         +-----------------------------------------------------------+
| Mode 2                      | \-     | 2048   | \-     |         |                                                           |
+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+
| Relative Pressure Accuracy                                       | Test Conditions:                                          |
+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+
| Mode 1                      | \-     | ±0.015 | \-     | hPa     | Temp. = 25°C Press.=800\~1100hPa                          |
+-----------------------------+--------+--------+--------+         +-----------------------------------------------------------+
| Mode 2                      | \-     | ±1     | \-     |         | Temp. = 25°C Press. = 2060\~4060hPa                       |
+-----------------------------+--------+--------+--------+---------+-----------------------------------------------------------+

### I^2^C Interface

The standard size routes the I^2^C interface to a pair of Qwiic connectors as well as a 0.1\"-spaced PTH header for users who prefer a traditional soldered connection. Both breakouts route the sensor\'s interrupt (INT) pin to a PTH pin.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Highlighting the communication interfaces on the standard breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Interfaces.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Interfaces.jpg)   [![Highlighting the communication interfaces on the micro breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/0/Qwiic_Micro_LPS28DFW_-_Interfaces.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/0/Qwiic_Micro_LPS28DFW_-_Interfaces.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Both boards set the LPS28DFW\'s I^2^C address to **0x5C** by default. Adjust the ADR jumper to change to the alternate address (**0x5D**) or open it completely to toggle the address using the ADR PTH pin (Standard size only). More information on this jumper in the Solder Jumpers section below.

### Solder Jumpers

Both LPS28DFW Qwiic breakouts have three solder jumpers labeled: **PWR**, **I2C**, and **ADR**. The table below outlines the jumpers\' label, default state, function, and any notes about their behavior.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Highlighting the communication interfaces on the standard breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Solder_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Solder_Jumpers.jpg)   [![Highlighting the communication interfaces on the micro breakout.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/0/Qwiic_Micro_LPS28DFW_-_Solder_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/0/Qwiic_Micro_LPS28DFW_-_Solder_Jumpers.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Label   Default State   Function                                                                  Notes
  ------- --------------- ------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PWR     CLOSED          Completes the Power LED circuit.                                          Open to disable the Power LED.
  I2C     CLOSED          Pulls the SDA/SCL lines to VCC (3.3V) through a pair of 10kΩ resistors.   Open to disable pull-up resistors on the I^2^C lines.
  ADR     SEE NOTE        Sets the I^2^C address of the LPS28DFW.                                   I^2^C address is 0x5C by default. Sever the trace connecting the center pad to the pad labeled 0x5C and connect it to the pad labeled 0x5D to change the address.

### Board Dimensions

The boards match the Standard and Micro form-factors for Qwiic breakouts measuring 1\" x 1\" (Standard) and 0.5\" x 0.3\" (Micro). The Standard breakout has four mounting holes and the Micro has one. All mounting holes fit a size [4-40](https://www.sparkfun.com/products/10453) screw.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Standard Qwiic breakout dimensions.](https://cdn.sparkfun.com/r/600-600/assets/1/c/b/d/c/SparkFun_Absolute_Digital_Barometer-LPS28DFW_Qwiic_Dimensions.png)](https://cdn.sparkfun.com/assets/1/c/b/d/c/SparkFun_Absolute_Digital_Barometer-LPS28DFW_Qwiic_Dimensions.png)   ![Qwiic Micro breakout dimensions.](https://cdn.sparkfun.com/r/600-600/assets/7/5/e/6/2/SparkFun_Micro_Absolute_Digital_Barometer-LPS28DFW_Qwiic_Dimensions.png)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Hardware Assembly

Now that we\'re familiar with the LPS28DFW breakouts, we can start assembling our circuit.

### Qwiic/I^2^C Assembly

The fastest and easiest way to get started using the breakouts is to connect the Qwiic connector on the breakout to a Qwiic-enabled development board like the SparkFun RedBoard Artemis with a Qwiic cable and as shown in the image below.

[![Completed Qwiic circuit with the RedBoard Artemis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Assembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Assembly.jpg)

If you would prefer a more secure and permanent connection with the Standard Size breakout, you can solder headers or wire to the PTH header on the board.

### Conformal Coating for Waterproofing

While the LPS28DFW\'s gel filled cap protects the sensing element from liquid and other environmental effects, the breakouts do not have any coating to protect the other components from damage due to exposure to liquids. A protective coating is required for applications that expose the board(s) to liquid. This tutorial on [customizing LilyPad LED colors](https://learn.sparkfun.com/tutorials/customizing-lilypad-led-colors#coat-your-leds) has tips on how to apply a conformal coating.

## LPS28DFW Arduino Library

**Note:** This library assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The SparkFun LPS28DFW Arduino Library provides a quick and easy way to get started configuring and measuring pressure data from the sensor. Install the library using the Arduino Library Manager tool by searching for **\"SparkFun LPS28DFW\"**. Users who prefer to manually install the library can download a copy of it from the [GitHub repository](https://github.com/sparkfun/SparkFun_LPS28DFW_Arduino_Library) by clicking the button below:

[SparkFun LPS28DFW Arduino Library](https://github.com/sparkfun/SparkFun_LPS28DFW_Arduino_Library/archive/refs/heads/main.zip)

### Library Functions

The list below outlines and describes the functions available in the SparkFun LPS28DFW Arduino Library. For detailed information on the parameters and use of all functions, refer to the [.cpp file in the library](https://github.com/sparkfun/SparkFun_LPS28DFW_Arduino_Library/blob/main/src/SparkFun_LPS28DFW_Arduino_Library.cpp).

#### Device Initialization and Configuration

- \'int32_t begin(uint8_t address = LPS28DFW_I2C_ADDRESS_DEFAULT, TwoWire& wirePort = Wire);\' - Begin communication with the sensor over I^2^ at the defined address and on the defined port. If no error occur, perform a soft reset and initialize the sensor.
- \'int32_t init();\' - Enables the BDU and IF_ADD_INC bits in the control registers.
- \'int32_t boot();\' - Enables the BOOT bit in the control registers
- \'int32_t reset();\' - Resets the sensor.
- \'int32_t setModeConfig(lps28dfw_md_t\* mode);\' - Configures the operation mode settings for the sensor including range and ODR.
- \'int32_t getModeConfig(lps28dfw_md_t\* mode);\' - Returns the operation mode settings.
- \'int32_t getStatus(lps28dfw_stat_t\* status);\' - Returns the sensor status bits such as data ready, overrun, etc.

#### Sensor Data

- \'int32_t getSensorData();\' - Get pressure data from the sensor.

#### Interrupt Control and Feature Selection

- \'int32_t setInterruptMode(lps28dfw_int_mode_t\* intMode);\' - Configures the interrupt pin to be either HIGH/LOW and LATCHED/PULSED.
- \'int32_t enableInterrupts(lps28dfw_pin_int_route_t\* intRoute);\' - Enables the data ready and FIFO interrupt conditions.
- \'int32_t getInterruptStatus(lps28dfw_all_sources_t\* status);\' - Returns the status of the interrupt flags.

#### FIFO Buffer Control

- \'int32_t setFIFOConfig(lps28dfw_fifo_md_t\* fifoConfig);\' - Sets the FIFO configuration parameters.
- \'int32_t getFIFOConfig(lps28dfw_fifo_md_t\* fifoConfig);\' - Returns settigs of FIFO buffer.
- \'int32_t getFIFOLength(uint8_t\* numData);\' - Returns the number of samples stored in the FIFO buffer (up to 128).
- \'int32_t getFIFOData(lps28dfw_fifo_data_t\* data, uint8_t numData);\' - Gets pressure data from the FIFO buffer.
- \'int32_t flushFIFO();\' - Clear all data from the FIFO buffer.

#### Reference Mode Control

- \'int32_t setReferenceMode(lps28dfw_ref_md_t\* mode);\' - Sets the sensor to operate in reference mode. When called it stores the latest pressure data as a reference pressure. The reference pressure can be used with Threshold Mode to trigger interrupts.
- \'int32_t setThresholdMode(lps28dfw_int_th_md_t\* mode);\' - Configures the sensor to trigger interrupts when the pressure measured exceeds a threshold relative to the defined reference pressure.
- \'int32_t getReferencePressure(int16_t\* pressRaw);\' - Returns the value stored for the reference pressure.

## Arduino Examples

Now let\'s take a closer look at a few of the examples included in the LPS28DFW Arduino Library.

### Example 1 - Basic Readings

The first example covers the basics of polling the LPS28DFW for pressure and temperature data over I^2^C. Open the example by navigating to **File \> Examples \> SparkFun LPS28DFW Arduino Library \> Example1_BasicReadings**. Select your Board and Port and click the Upload button. Once upload completes, open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with the baud set to **115200** and watch pressure and temperature data print out.

The code assumes the sensor uses the default I^2^C address so if you have adjusted the ADR jumper to switch to the alternate address, comment/uncomment the line with the correct value listed:

    language:c
    uint8_t i2cAddress = LPS28DFW_I2C_ADDRESS_DEFAULT; // 0x5C
    //uint8_t i2cAddress = LPS28DFW_I2C_ADDRESS_SECONDARY; // 0x5D

The example attempts to initialize the sensor with default settings in I^2^C at the specified address. If it cannot initialize properly, the code prints out an error in over serial:

    language:c
    while(pressureSensor.begin(i2cAddress) != LPS28DFW_OK)
        

If you see this error, double check the sensor is connected properly and set to the correct I^2^C address and reset the development board or re-upload the code.

The main loop gets temperature and pressure data measurements from the sensor every second:

    language:c
    

Try moving the sensor up and down to see the pressure data change.

### Example 3 - Interrupts

Example 3 shows how to set up and use data ready interrupts triggered by the sensor. The code defaults to use `D2` as the interrupt pin on a connected development board. If your board does not support external interrupts on `D2`, adjust this line:

    language:c
    int interruptPin = 2

If you\'re not sure which pins on your development board support external interrupts, [this reference page](https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/) lists usable digital pins for most common Arduino development boards.

After initializing the LPS28DFW, the code sets the ODR to 1Hz, configures the interrupt pin to operate in Data Ready mode and attaches the interrupt to the pin defined above (`D2`:

    language:c
    ps28dfw_md_t modeConfig =
        ;
        pressureSensor.setModeConfig(&modeConfig);

        // Configure the LPS28DFW interrupt pin mode
        lps28dfw_int_mode_t intMode =
        ;
        pressureSensor.setInterruptMode(&intMode);

        // Configure the LPS28DFW to trigger interrupts when measurements finish
        lps28dfw_pin_int_route_t intRoute =
        ;
        pressureSensor.enableInterrupts(&intRoute);

        // Setup interrupt handler
        attachInterrupt(digitalPinToInterrupt(interruptPin), lps28dfwInterruptHandler, RISING);
    }

The main loop waits for a Data Ready interrupt event to occur and then prints out the data from the sensor over serial.

### Example 5 - Reference Mode

Example 5 demonstrates how to set and use reference measurements to trigger interrupts from the LPS28DFW. Reference mode allows you to store a pressure value as a reference and then monitor the sensor\'s output to trigger an interrupt if it goes above or below the threshold value by a specified amount.

The reference value register is READ only so we cannot manually set the threshold value in the code. Instead, the code waits for the user to input they are ready to set the threshold value and then enter any key to trigger the event.

The code sets the over and under pressure thresholds to 1hPa above/below the stored reference pressure. If you want to adjust it, change the settings here:

    language:c
    lps28dfw_int_th_md_t thresholdMode =
        ;
        pressureSensor.setThresholdMode(&thresholdMode);

Note, the threshold value must be set in multiples of 16 when in Mode 1 (260-1260hPa) and multiples of 8 when in Mode 2 (260-4060hPa). For example, to set the pressure threshold to above/below 1hPa, set the `.threshold` to 16.

After uploading, open the serial monitor with the baud set to **115200** and get the sensor ready to take the threshold measurement. Wait for the prompt and press any key to set the value. If successful, you should see the serial printout below:

[![Screenshot of Example 5 taking reference data.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Example_5.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/0/Qwiic_LPS28DFW_-_Example_5.png)

Once the threshold is set, the main loop prints out temperature and pressure data and waits for an interrupt event to trigger if the pressure readings go above or below the threshold pressure by 1hPa.

## Troubleshooting

### Waterproofing the Breakouts

As mentioned previously, these breakouts do not have any coating on them to protect the components from water damage so users who intend to take advantage of the LPS28DFW\'s water resistant design will need to coat the breakout in a waterproof coating such as conformal coating. This tutorial on [customizing LilyPad LED colors](https://learn.sparkfun.com/tutorials/customizing-lilypad-led-colors#coat-your-leds) has tips on how to apply a conformal coating.

### Pressure Data as Altitude

If you want to use the pressure data from the LSP28DFW to determine the altitude of the sensor, refer to [this section](https://learn.sparkfun.com/tutorials/mpl3115a2-pressure-sensor-hookup-guide#pressure-vs-altimeter-setting) of our MPL3115A2 Breakout Hookup Guide for more information on how to manipulate and correctly interpret pressure data.

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

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)