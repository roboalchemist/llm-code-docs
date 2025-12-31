# Source: https://learn.sparkfun.com/tutorials/sparkfun-humidity-sensor-breakout---shtc3-qwiic-hookup-guide

## Introduction

Looking to keep a log of the climate in your greenhouse, create a humidor control system or want to track temperature and humidity data for a weather station project? The [SparkFun Humidity Sensor Breakout - SHTC3 (Qwiic)](https://www.sparkfun.com/products/16467) may be the perfect option for you! The SHTC3 is a low cost, easy-to-use, highly accurate digital humidity and temperature sensor. The SHTC3 communicates via I^2^C so, as you can tell by the name, we have broken out the pins on the sensor to Qwiic connectors so you can easily connect it to SparkFun\'s ever growing [Qwiic Ecosystem](https://www.sparkfun.com/qwiic).

[![SparkFun Humidity Sensor Breakout - SHTC3 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/3/3/0/16467-SparkFun_Humidity_Sensor_Breakout_-_SHTC3__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-humidity-sensor-breakout-shtc3-qwiic.html)

### [SparkFun Humidity Sensor Breakout - SHTC3 (Qwiic)](https://www.sparkfun.com/sparkfun-humidity-sensor-breakout-shtc3-qwiic.html) 

[ SEN-16467 ]

The SparkFun SHTC3 Humidity Sensor Breakout is a low cost, easy-to-use, highly accurate digital humidity and temperature sens...

[ [\$13.11] ]

In this guide we will highlight some of the unique features of this breakout, how to connect and use it as well as an Arduino library with four examples to get you started with your next environmental monitoring project.

### Required Materials

To follow along with this guide you will need a microcontroller to communicate with the SHTC3. Below are a few options that come Qwiic-enabled out of the box:

[![SparkFun Qwiic Pro Micro - USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/0/4/15795-Pro_Micro_C-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html)

### [SparkFun Qwiic Pro Micro - USB-C](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html) 

[ DEV-15795 ]

The SparkFun Qwiic Pro Micro adds a reset button, Qwiic connector, USB-C, and castellated pads to the miniaturized Arduino bo...

[ [\$23.95] ]

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

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

[![SparkFun Qwiic Shield for Arduino Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/7/8/9/16130-SparkFun_Qwiic_Shield_for_Arduino_Nano-01.jpg)](https://www.sparkfun.com/products/16130)

### [SparkFun Qwiic Shield for Arduino Nano](https://www.sparkfun.com/products/16130) 

[ DEV-16130 ]

The SparkFun Qwiic Shield for Arduino Nano makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards...

**Retired**

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

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them. If you are using one of the Qwiic Shields listed above, you may want to read through their respective Hookup Guides as well before you get started with the SparkFun Humidity Sensor Breakout - SHTC3 (Qwiic).\

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

The SHTC3 Humidity and Temperature Sensor from Sensirion is an highly accurate digital humidity and temperature sensor that communicates using the I^2^C protocol. It is designed to work exceptionally well in battery powered applications such as wearables or remote environmental monitoring. In this section we will cover the operating characteristics of the SHTC3 along with the hardware present on the breakout board.

### Sensor Specifications

The table below outlines some of the SHTC3\'s humidity and temperature sensor specifications. For a complete list and details about recommended operating conditions, review the [SHTC3 Datasheet](https://cdn.sparkfun.com/assets/0/0/1/3/0/Sensirion_Humidity_Sensors_SHTC3_Datasheet.pdf).

  **Parameter**                          **Value**
  -------------------------------------- -----------------
  Specified Humidity Range               0 to 100 %RH
  Specified Temperature Range            -40 to +125 °C
  Relative Humidity Accuracy Tolerance   ± 2.0%RH (Typ.)
  Temperature Accuracy Tolerance         ± 0.2°C (Typ.)

### Power

Power for the SHTC3 is provided over the Qwiic interface or if you would prefer you can power it with **1.62-3.6V** through the pins labeled **3.3V** and **GND**. We recommend powering the board with a regulated **3.3V** source, especially if you are using it with other Qwiic boards.

[![Power Input](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/9/SHTC3_Power_Input.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/9/SHTC3_Power_Input.jpg)

### Qwiic and I^2^C Interface

The SHTC3 communicates via I^2^C and these pins are broken out to the two Qwiic connectors on the board as well as the SDA and SCL pins. The SHTC3\'s I^2^C interface supports clock frequencies between **0** to **1MHz** with clock stretching to match the Fast Mode Plus specification. The I^2^C address is **0x70** (1110000 bin) and is hardware-defined. If you have other I^2^C devices with the same address or wish to use multiple SHTC3 breakouts on a single I^2^C bus, you\'ll want to use a multiplexer/mux. If you need to use more than one SHTC3 sensor or other devices sharing the same address in your project, consider using the [Qwiic Mux Breakout - 8-Channel](https://www.sparkfun.com/products/14685). Note, the Qwiic Mux Breakout\'s default I^2^C address is also **0x70** so it must be adjusted to work properly with the SHTC3.

[![Highlighting Qwiic and I2C Interface](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/9/SHTC3_Qwiic_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/9/SHTC3_Qwiic_I2C.jpg)

### Jumpers

If you have never worked with solder jumpers and PCB traces before or would like a quick refresher, check out our [How to Work with Solder Jumpers and PCB Traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) tutorial for detailed instructions and tips.

The SparkFun Humidity Sensor - SHTC3 (Qwiic) has two solder jumpers on the board labeled ***I2C*** and ***PWR*** (or PWRLED if you are looking at the schematic). The I^2^C jumper pulls the SDA and SCL pins to VDD (normally **3.3V**) through two **2.2K Ohm** resistors. If you have many peripheral devices on the same bus you may want to disable these by opening the jumper (assuming they are also operating at **3.3V** logic).

The PWRLED jumper connects the power LED to VDD (normally **3.3V**) through a **1K Ohm** resistor. To disable the power LED simply open the jumper by severing the trace between the two solder pads. This is particularly useful for lower power applications where current draw needs to be kept at a minimum.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Highlighting the Red Tactile Button](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/9/SHTC3_I2C_Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/9/SHTC3_I2C_Jumper.jpg)   [![Highlighting the Power LED Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/9/SHTC3_Power_LED_Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/9/SHTC3_Power_LED_Jumper.jpg)
  *I^2^C Jumper*                                                                                                                                                                                                   *Power LED Jumper*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Board Dimensions

This breakout is designed to our Qwiic standard 1x1\" sizing to easily stack with other Qwiic products. There are four mounting holes on the board that fit a 4-40 screw.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/9/SHTC3_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/9/SHTC3_Dimensions.png)

Now that we have a solid understanding of the hardware present on the breakout, we\'ll get it hooked up in the next section and move swiftly on to programming and talking to the sensor.

## Hardware Assembly

Using the Qwiic system, assembling the hardware is simple. All you need to do is connect your SparkFun Humidity Sensor Breakout - SHTC3 (Qwiic) to your chosen development board with a Qwiic cable or [adapter cable](https://www.sparkfun.com/products/14425). Otherwise, you can use the I^2^C pins broken out if you prefer. If you are not using a Qwiic-enabled board, make sure your input voltage and logic are either running at **3.3V** or you are running both controller and SHTC3 at the same [logic level](https://learn.sparkfun.com/tutorials/logic-levels).

[![SHTC3 connected to a RedBoard Qwiic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/9/SHTC3_Hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/9/SHTC3_Hookup.jpg)

If you prefer to use the PTH pins broken out on the Humidity Sensor you will need to either solder to them or, if you want a temporary connection for prototyping, these [IC Hooks](https://www.sparkfun.com/products/9741) are a perfect option to make that connection. If you are not familiar with through-hole soldering, take a look at this tutorial:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

With our SHTC3 connected to our microcontroller we can move on to writing some code to start monitoring temperature and humidity.

## SHTC3 Arduino Library

**Note:** This library assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The SparkFun SHTC3 Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun SHTC3**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_SHTC3_Arduino_Library):

[SparkFun SHTC3 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_SHTC3_Arduino_Library/archive/master.zip)

Once the library is installed, we can move on to working with the included example sketches and take some sensor readings.

### Example 1: Basic Readings

Open the first example by heading to **File** \> **Examples** \> **SparkFun SHTC3 Humidity and Temperature Sensor Library** \> **Example1_BasicReadings**. Select your board (in our case, the **Arduino/Genuino Uno**) and the COM port that it enumerated on. Then hit upload. Open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **115200** baud to start viewing the humidity and temperature!

Try holding your hand over the sensor or breathe lightly on to the SHTC3 and watch the values change.

### Example 2: Verify Checksums

This example is very similar to the Basic Readings but also enables and returns checksum data calculated by the sensor to ensure the data is valid. Open it by following the instructions for Example 1 but instead select **Example2_VerifyChecksums**. The checksum pass indicators are `passIDcrc`, `passRHcrc` and `passTcrc` for the sensor ID, relative humidity and temperature, respectively.

Using checksums is not absolutely necessary but can be helpful for troubleshooting any I^2^C communication errors. Once the code is uploaded, it will print out over serial all checksum data and whether or not it has passed or failed so you can identify if something such as the device ID is not returned properly.

### Example 3: Changing Options

The third example builds on the previous two and demonstrates how to configure the SHTC3 using the `setMode` function as well as selecting your Wire port and clock speed. Again, open the example by navigating to the SHTC library and selecting **Example2_ChangingOptions**.

Below are the available modes available on the SHTC3:

    language:c
    SHTC3_CMD_CSE_RHF_NPM = 0x5C24,   // Clock stretching, RH first, Normal power mode
    SHTC3_CMD_CSE_RHF_LPM = 0x44DE,   // Clock stretching, RH first, Low power mode
    SHTC3_CMD_CSE_TF_NPM = 0x7CA2,    // Clock stretching, T first, Normal power mode
    SHTC3_CMD_CSE_TF_LPM = 0x6458,    // Clock stretching, T first, Low power mode

    SHTC3_CMD_CSD_RHF_NPM = 0x58E0,   // Polling, RH first, Normal power mode
    SHTC3_CMD_CSD_RHF_LPM = 0x401A,   // Polling, RH first, Low power mode
    SHTC3_CMD_CSD_TF_NPM = 0x7866,    // Polling, T first, Normal power mode
    SHTC3_CMD_CSD_TF_LPM = 0x609C   // Polling, T first, Low power mode

By default, the code sets the SHTC3 up to use clock stretching, report temperature data first and run on low power mode. To change to another mode, refer to the settings above and change this line:

    language:c
    mySHTC3.setMode(SHTC3_CMD_CSE_TF_LPM) == SHTC3_Status_Nominal

Once you have selected which mode you want the SHTC3 to operate in, upload it and open a serial monitor to **115200** baud. You should see the checksum data print and then whether or not the `setMode` function was successful. Note that the code defaults to print out `"Choosing low-power measurements with T first: "` so if you use a different mode, you may want to alter that print statement to avoid confusion.

If all of that is successful, the code will start printing out humidity and temperature data.

### Example 4: Using Callback

The fourth example in the library demonstrates how to use the callback feature on the SHTC3. You may be wondering, what is a callback? It is a way that a library can provide a place for the user to do something. The library was written with a function that is called (nearly) every time a function is exited. How is that useful? You can overwrite the function with your own definition that allows you to do things like debug or watch the program execute.

Make a function with this signature:

    language:c
    void SHTC3_exitOp_Callback(SHTC3_Status_TypeDef status, bool inProcess, char * file, uint16_t line)

Then write in it some code that might help you. The example helps us watch the code execute by displaying the line number, file, and status every time that a function finishes.

Including these functions is particularly helpful for debugging but can be taxing on your processor and slow down your code.