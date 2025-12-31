# Source: https://learn.sparkfun.com/tutorials/sparkfun-environmental-sensor-breakout---bme68x-qwiic-hookup-guide

## Introduction

**Important Note:** In order to avoid contamination of its gas scanning capabilities, [[**DO NOT**]] touch the metallic casing of the BME688 sensor.

The [SparkFun Environmental Sensor - BME680 (Qwiic)](https://www.sparkfun.com/products/16466) is a breakout for the 4-in-1 BME680 gas sensor from [Bosch](https://www.bosch.us/). The BME680 combines a gas sensor with temperature, humidity and barometric pressure sensing for a complete environmental sensor in a single package. The gas sensor on the BME680 can detect a wide variety of volatile organic compounds (or VOC for short) to monitor indoor air quality. Combine that with precise temperature, humidity and barometric pressure and the BME680 can work as a completely standalone environmental sensor all in a 1\"x1\" breakout! The BME680 communicates over either I^2^C or SPI. As you would expect from the name, the BME680\'s I^2^C pins are broken out to a Qwiic connector so integrating it into the [SparkFun Qwiic System](https://www.sparkfun.com/qwiic) is a breeze. Simply plug it into a Qwiic-enabled microcontroller and you\'re well on your way to making your own weather station.

[![SparkFun Environmental Sensor Breakout - BME680 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/3/2/9/16466-SparkFun_Environmental_Sensor_Breakout_-_BME680__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-environmental-sensor-breakout-bme680-qwiic.html)

### [SparkFun Environmental Sensor Breakout - BME680 (Qwiic)](https://www.sparkfun.com/sparkfun-environmental-sensor-breakout-bme680-qwiic.html) 

[ SEN-16466 ]

This SparkFun Environmental Sensor is a breakout for the 4-in-1 BME680 gas sensor from Bosch.

[ [\$22.95] ]

[![SparkFun Environmental Sensor - BME688 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/6/9/6/19096-SparkFun_Environmental_Sensor_Breakout_-_BME688__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-environmental-sensor-bme688-qwiic.html)

### [SparkFun Environmental Sensor - BME688 (Qwiic)](https://www.sparkfun.com/sparkfun-environmental-sensor-bme688-qwiic.html) 

[ SEN-19096 ]

The SparkFun BME688 Environmental Sensor combines a gas scanning sensor with temperature, humidity, & barometric pressure sen...

[ [\$34.95] ]

The [Qwiic BME688 breakout board](https://www.sparkfun.com/products/19096) is an updated version of the [BME680 environmental sensor](https://www.sparkfun.com/products/16466) from Bosch. With the same features of the original BME680, the new BME688 also includes an additional gas scanning functionality to detect the presence of VSCs (i.e. hydrogen sulfide (H~2~S) compounds). The gas scanner operation can be manually customized or trained with the BME AI-Studio tool to detect target samples.

**Notes on AI Feature:**

- How is the BME688 different from the BME680?
  - The BME680 does not support AI features.
- Can we test the AI software it with the current BME680?
  - No, this is not possible, as the BME680 does not have the necessary gas scan function.
- While the [BME688 Qwiic board](https://www.sparkfun.com/products/16466) can be used with the [BME AI-Studio](https://www.bosch-presse.de/pressportal/de/en/bme-ai-studio-software-225349.html) and [BSEC2 Arduino library](https://github.com/BoschSensortec/Bosch-BSEC2-Library), for the AI functionality, it is recommended that users purchase the BME688 Evaluation Board *(Coming Soon)* for ease of use.

  :::: 
  ::: 
  :::
  ::::

### Required Materials

**Note:** To get started with the BME688, a RedBoard Qwiic is more than sufficient for the basic sensor functionality covered in this tutorial. However, the more advanced [BSEC2 Arduino library](https://github.com/BoschSensortec/Bosch-BSEC2-Library), with support for the BME688 AI functionality, is only compatible with some of the **ESP32 microcontrollers**, like the [ESP32 WROOM](https://www.sparkfun.com/products/15663).

*\*For more details, check out the [tested platforms section](https://github.com/BoschSensortec/Bosch-BSEC2-Library/blob/master/README.md#6-tested-boardcore-list) of the Arduino library and our Getting started with the BME AI-Studio guide (coming soon).*

To follow along with this guide you will need a microcontroller to communicate with the BME68x. Below are a few options that come Qwiic-enabled out of the box:

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

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

[![SparkFun Qwiic Shield for Arduino Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/6/16789-SparkFun_Qwiic_Shield_for_Arduino_Nano-05.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino-nano.html)

### [SparkFun Qwiic Shield for Arduino Nano](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino-nano.html) 

[ DEV-16789 ]

The SparkFun Qwiic Shield for Arduino Nano makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards...

[ [\$5.50] ]

[![SparkFun Qwiic Shield for Teensy](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/0/8/7/17119-SparkFun_Qwiic_Shield_for_Teensy-07.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-teensy.html)

### [SparkFun Qwiic Shield for Teensy](https://www.sparkfun.com/sparkfun-qwiic-shield-for-teensy.html) 

[ DEV-17119 ]

This shield provides an easy way to SparkFun\'s Qwiic ecosystem with your Teensy 4.0, 3.2, or LC board footprint.

[\$4.25] [ [\$1.40] ]

You will also want at least one Qwiic cable to connect your sensor to your microcontroller.

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

If you\'re unfamiliar with serial terminals, jumper pads, or I^2^C be sure to checkout some of these foundational tutorials.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Qwiic BME68x utilizes the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials (above) before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

## Hardware Overview

The heart of these breakout boards, Bosch\'s BME680 Gas Sensor, integrates four sensors (gas, pressure, temperature and humidity) into a tiny package. The BME68x measures just 3mm x 3mm x 0.93 mm and was specifically designed for applications that depend on a small footprint and low power consumption. This makes the BME68x a great choice for remote or mobile environmental sensing applications. We will highlight some of the unique aspects of the BME68x in this section but for a full overview of the sensor package, check out the datasheets:

- [BME680 Datasheet](https://cdn.sparkfun.com/assets/8/a/1/c/f/BME680-Datasheet.pdf)
- [BME688 Datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme688-ds000.pdf)

**BME688 Note:** The BME688 is a drop in replacement for the BME680; with the added gas scanning functionality and support for AI algorithms. The parameters in [highlighted in yellow], only apply to the BME688 sensor.

**How does the gas scanner work?** The gas sensor takes measurements with different sensitivities during one gas scan. In doing so, it can generate a profile *(or fingerprint)* for different gas mixtures. This can be modified and optimized with BME AI-Studio.

Characteristic

Description

Operating Voltage

- V~DD~: 1.71V to 3.6V (**Default on Qwiic System: 3.3V**)
- V~DDIO~: 1.2 to 3.6V

Operational Modes

**Sleep** (**Default**) and Forced (*low power; single measurement*)\
[Parallel (*Gas sensor heater operates in parallel to TPH measurement*)]

Interface

I²C and SPI

I²C Address

BME680: **0x77** (**Default**) or 0x76\
[BME688: **0x76** (**Default**) or 0x77]

Average current consumption

2.1 µA at 1 Hz humidity and temperature\
3.1 µA at 1 Hz pressure and temperature\
3.7 µA at 1 Hz humidity, pressure and temperature\
90 µA at ULP mode for p/h/T & air quality\
0.9 mA at LP mode for p/h/T & air quality\
[3.9 mA in standard gas scan mode]

Humidity Parameters

Range: 10 to 90 %RH\
Absolute Accuracy: ±3 %RH (from 20 - 80 %RH)\
Resolution: 0.008 %RH

Pressure Parameters

Range: 300 to 1100 hPa (30,000 - 110,000 Pa or approx. 4.35 - 15.95 PSI)\
Absolute Accuracy: ±0.6 hPa\
Resolution: 0.18 Pa

Temperature Parameters

Range: 0°C to 65°C (32°F to 149°F)\
Absolute Accuracy: ±(0.5 - 1.0)°C\
Resolution: 0.01°C

Gas Sensor Parameters

[F1 score for H₂S scanning: 0.92]\
[Standard scan speed: 10.8 s / scan]\
Sensor-to-sensor deviation: +/- 15% +/- 15\
Output data processing:

- Index for Air Quality (IAQ)
- bVOC-& CO₂-equivalents (ppm)
- [Gas scan result (%)]
- More listed in the **BSEC outputs** table:
  - *Table 14* in the [BME680 datasheet](https://cdn.sparkfun.com/assets/8/a/1/c/f/BME680-Datasheet.pdf)
  - *Table 20* in the [BME688 datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme688-ds000.pdf)

### Power

The BME68x accepts a supply voltage between **1.71 to 3.6V**. Power can be supplied to the board either through one of the Qwiic connectors or the dedicated **3.3V** and **GND** pins broken out on either side of the board.

[![BME680 Power Inputs Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/8/BME680_Power_Input.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME680_Power_Input.png)\
*BME680 (Click to enlarge)*

[![BME688 Power Inputs](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-power.jpg)\
*BME688 (Click to enlarge)*

### Qwiic and I^2^C Interface

The SparkFun Environmental Sensor - BME68x (Qwiic) communicates over I^2^C by default. We have routed the BME68x\'s I^2^C pins to two Qwiic connectors as well as broken them out to 0.1\"-spaced the header pins highlighted below.

[![BME680 Qwiic and I2C Interface Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/8/BME680_Qwiic_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME680_Qwiic_I2C.jpg)\
*BME680 (Click to enlarge)*

[![BME688 Qwiic and I2C Interface Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-i2c.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-i2c.jpg)\
*BME688 (Click to enlarge)*

**Note:** The default I^2^C address between the BME680 and BME688 Qwiic boards are different:

- BME680: **0x77**
- BME688: **0x76**

### Serial Peripheral Interface (SPI)

If you would prefer to communicate with your BME68x via [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi), we have broken those pins out as well to standard 0.1\"-spade header pins. Communicating over SPI requires more connections than I^2^C but is more versatile and can be faster. It is particularly helpful if you need to use more than two BME68x\'s in your circuit or if you have other devices using the same I^2^C addresses.

[![BME680 SPI Pins Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/8/BME680_SPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME680_SPI.jpg)\
*BME680 (Click to enlarge)*

[![BME688 SPI Pins Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-spi_split.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-spi_split.jpg)\
*BME688 (Click to enlarge)*

**BME688 SPI Jumpers:** In order to communicate with the BME688 Qwiic board over SPI, users will need to cut the `CSB` and `ADR` *(leave floating)* jumpers. *\*See the **CSB Jumper** section, below, for more information.*

**SPI Pin Nomenclature:** Users may not recognize the `COPI`/`CIPO` or `SDI`/`SDO` labels for SPI pins. SparkFun has joined with other members of OSHWA in a resolution to move away from using \"Master\" and \"Slave\" to describe signals between the controller and the peripheral. Check out [this page](https://www.sparkfun.com/spi_signal_names) for more on our reasoning behind this change. You can also see OSHWA\'s resolution [here](https://www.oshwa.org/a-resolution-to-redefine-spi-signal-names).

On the BME688 Qwiic board, the `CS` *(chip select)* pin is labeled with a `CSB` silkscreen, as annotated in the [BME688 datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme688-ds000.pdf).

### Solder Jumpers

The SparkFun Environmental Sensor - **BME680** (Qwiic) has three solder jumpers which can be modified to alter the functionality of the sensor. While, the SparkFun Environmental Sensor - **BME688** (Qwiic) has four solder jumpers which can be modified to alter the functionality of the sensor.

If you have never worked with solder jumpers or PCB traces before or would like a refresher, take a look at our [How to Work with Jumper Pads and PCB Traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) tutorial.

#### I^2^C Pull-Up Jumper

On the BME680 Qwiic board, the SDA/SDI and SCL/SCK pins are pulled to VDDIO (**3.3V**) through a pair of **4.7kΩ** (**2.2kΩ** on the BME688) resistors. The jumper is normally **closed** so to disable the pull-up resistors, simply sever the traces between the three pads using a hobby knife.

[![BME680 I2C Jumper Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/8/BME680_I2C_Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME680_I2C_Jumper.jpg)\
*BME680 (Click to enlarge)*

[![BME688 I2C Jumper Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-jumper_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-jumper_I2C.jpg)\
*BME688 (Click to enlarge)*

#### Power LED Jumper

This jumper connects the power LED to **3.3V** via a **1K Ohm** resistor. This jumper is normally **closed** so to disable the power LED, sever the trace between the two pads. This is particularly helpful for reducing the total current draw of your breakout for low-power applications.

[![BME680 Power LED Circuit highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/8/BME680_Power_LED.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME680_Power_LED.png)\
*BME680 (Click to enlarge)*

[![BME688 Power LED Circuit highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-jumper_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-jumper_LED.jpg)\
*BME688 (Click to enlarge)*

#### I^2^C Address Jumper

**Note:** The default I^2^C address between the BME680 and BME688 Qwiic boards are different. The jumper configuration and adjustment is also different.

This jumper sets the 7-Bit unshifted I^2^C address of the BME680 and is **open** by default. The default address is **0x77** and can be adjusted to **0x76** by closing this jumper.

[![Address Jumper Highlighted](https://cdn.sparkfun.com/r/360-360/assets/learn_tutorials/1/1/6/8/BME680_ADR_Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME680_ADR_Jumper.jpg)

*BME680 (Click to enlarge)*

This jumper sets the 7-Bit unshifted I^2^C address of the BME688 and sets the default address to **0x76** and can be adjusted to **0x77** by cutting and soldering the jumper over to the `0x77` pad.

[![BME688 Address Jumper Highlighted](https://cdn.sparkfun.com/r/360-360/assets/learn_tutorials/1/1/6/8/BME688-jumper_ADR.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-jumper_ADR.jpg)

*BME688 (Click to enlarge)*

#### CSB Jumper

This jumper only applies to the BME688 Qwiic board. The `CSB` pin is pulled up to V~DDIO~ in order to configure the board for I^2^C communication by default. In order to communicate with the sensor over SPI, the `CSB` jumper must be cut along with the `ADR` jumper *(leave floating)*. Once the `CSB` pin has been pulled low during SPI communication, the sensor will communicate over SPI until there is a power reset.

[![BME688 CSB jumper highlighted](https://cdn.sparkfun.com/r/360-360/assets/learn_tutorials/1/1/6/8/BME688-jumper_CSB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME688-jumper_CSB.jpg)

### Board Dimensions

This breakout fits the Qwiic standard sizing for breakouts. It is a 1\"x1\" square with two mounting holes that fit a 4-40 screw.

[![Qwiic BME680 board dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/8/BME680_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME680_Dimensions.png)\
*BME680 (Click to enlarge)*

[![Qwiic BME688 board dimensions](https://cdn.sparkfun.com/r/190-190/assets/learn_tutorials/1/1/6/8/qwiic_bme688_dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/qwiic_bme688_dimensions.png)\
*BME688 (Click to enlarge)*

Now that we have a thorough understanding of the hardware and features on the Environmental Sensor - BME680 (Qwiic), it\'s time to hook it up and start taking measurements.

## Hardware Assembly

**Important Notes:**

- In order to avoid contamination of its gas scanning capabilities, [[**DO NOT**]] touch the metallic casing of the BME688 sensor.
- At first sensor usage, minimum 48 hours of \"burn in\" should be made. Later, at each usage, 30 min. of functioning should passed before sensor data may be considered as valid.
  - To \"burn in\" the sensor, users just need to power the sensor for 48 hrs.

Using the Qwiic system, assembling the hardware is simple. All you need to do is connect your Environmental Sensor - BME68x (Qwiic) to your chosen development board with a Qwiic cable or [adapter cable](https://www.sparkfun.com/products/14425). Otherwise, you can use the I^2^C pins broken out if you do not have a Qwiic connector on your development board or if you do not want to use a Qwiic connection. If you are not using a Qwiic-enabled board, make sure your input voltage and logic are either running at **3.3V** or you are shifting the [logic level](https://learn.sparkfun.com/tutorials/logic-levels) from whatever logic your controller runs at to **3.3V** for the BME680.

[![BME680 Connected to a RedBoard Qwiic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/8/BME680_Connected_to_RedBoard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/BME680_Connected_to_RedBoard.jpg)

If you would prefer to communicate with the BME680 via SPI, you will need to connect to the SPI pins broken out on this board and route them to the respective pins for SPI communication on your development board (CIPO, COPI, SCK and CS). Also note that this breakout defaults to I^2^C mode so your code will need to toggle the CS pin **LOW** once on power up to enable SPI mode. The BME680 will remain in SPI mode until the next power cycle. The SPI examples further on in this guide do that automatically so it\'s only necessary to note for writing your own code.

**Note:** On the BME688 Qwiic board, users will need to cut the `ADR` and `CSB` jumpers to enable SPI communication. *(\*See the **Hardware Overview** section for more information.)*

**Note:** You may not recognize the COPI/CIPO labels for SPI pins. SparkFun has joined with other members of OSHWA in a resolution to move away from using \"Master\" and \"Slave\" to describe signals between the controller and the peripheral. Check out [this page](https://www.sparkfun.com/spi_signal_names) for more on our reasoning behind this change. You can also see OSHWA\'s resolution [here](https://www.oshwa.org/a-resolution-to-redefine-spi-signal-names).

Soldering to the pins is the best option for a secure connection but you can also create temporary connections to those pins for prototyping using something like these [IC Hooks](https://www.sparkfun.com/products/9741). If you are not familiar with through-hole soldering, take a look at this tutorial:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

With everything connected properly, we\'re ready to move on to uploading a sketch and start monitoring your environment!

## BME680 Arduino Library

**Note:** This library assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

For the scope of tutorial, we are going to use the BME680 Arduino Library created by SV-Zanshin. You can download it with the Arduino Library Manager by searching **\'BME680\'** and selecting the one authored by SV-Zanshin. Alternatively, you can grab the zip of the latest release (v1.0.3 as of this writing) below or you can download the most up to date version of the library from the [GitHub repository](https://github.com/SV-Zanshin/BME680).

[BME680 Arduino Library (ZIP)](https://github.com/SV-Zanshin/BME680/archive/v1.0.3.zip)

Once you have the library installed you can move on to uploading the examples and gathering environmental data.

**Note:** Users that are interested in the AI functionality of the **BME688** sensor can check out the [software available from the Bosch website](https://www.bosch-sensortec.com/software-tools/software/bme688-software/).

While the [BME688 Qwiic board](https://www.sparkfun.com/products/16466) can be used with the [BME AI-Studio](https://www.bosch-presse.de/pressportal/de/en/bme-ai-studio-software-225349.html) and [BSEC2 Arduino library](https://github.com/BoschSensortec/Bosch-BSEC2-Library), for the AI functionality, it is recommended that users purchase the BME688 Evaluation Board *(Coming Soon)* for ease of use.

## Arduino Examples

Now that the library is installed, we can move on to uploading some code. Before we discuss the individual examples, we\'ll cover some of the setup they perform for the BME68x.

The code configures the BME68x to perform oversampling for the temperature, humidity and pressure sensors and sets an IIR (infinite impulse response) filter for these sensors. This helps smooth out environmental data from any short term outliers. Finally, the setup also configures the temperature and time settings for the hot plate on the gas sensor. If you would like to adjust any of these settings, refer to the [BME680 Datasheet](https://cdn.sparkfun.com/assets/8/a/1/c/f/BME680-Datasheet.pdf)/[BME688 Datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme688-ds000.pdf) and the [library source files](https://github.com/SV-Zanshin/BME680/tree/master/src) for more information.

### I^2^C Demo

To open this example, head to **File** \> **Examples** \> **BME680** \> **I2CDemo**. Next, open the Tools menu and select your board (in our case, **Arduino Uno**) and the correct Port your board enumerated on.

Upload the code, open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) and set your baud rate to **115200**. You probably will see the code print out the successful initialization of the BME680 as well as the settings we discussed above and after that, you should see temperature, humidity, pressure, altitude and raw gas readings every five seconds.

[![Sample screenshot of I2C Demo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/8/I2CDemo_Screenshot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/8/I2CDemo_Screenshot.png)

**Note:** While the Arduino library automatically checks for the BME68x at both available addresses, users can also [specify a spacific address](https://github.com/Zanduino/BME680/blob/master/src/Zanshin_BME680.h#L157) in their code.

Users can change this line of code:

``` 
Copy Codewhile (!BME680.begin(I2C_STANDARD_MODE)) 
Copy Codewhile (!BME680.begin(I2C_STANDARD_MODE, 0x76)) ] touch the metallic casing of the BME688 sensor. Unfortunately, at this time, there are no recommendations or instructions for decontaminating the sensor once it has been touched.

### Gas Readings Interpretation

The library used in this tutorial only prints out the raw resistance values from the gas sensor on the BME680. You can use these values as a rough estimate of air quality where lower resistance values equate to a higher concentration of gases measured (and vice versa). If you want to get true Indoor Air Quality (IAQ) measurements from the BME680, we recommend taking a look at Bosch\'s [BSEC Arduino Library](https://github.com/BoschSensortec/BSEC-Arduino-library) which includes an algorithm to convert the resistance value to an IAQ value. For more information, refer to that library as well as sections 1.2 and 4.2 in the [BME680 Datasheet](https://cdn.sparkfun.com/assets/8/a/1/c/f/BME680-Datasheet.pdf). Calculated IAQ measurements are beyond the scope of this tutorial.

#### BME688 AI and Gas Scanning Features

In order to avoid contamination of its gas scanning capabilities, [[**DO NOT**]] touch the metallic casing of the BME688 sensor. Unfortunately, at this time, there are no recommendations or instructions for decontaminating the sensor once it has been touched.

At first sensor usage, minimum 48 hours of \"burn in\" should be made. Later, at each usage, 30 min. of functioning should passed before sensor data may be considered as valid. *(\*In their video for the BME688 evaluation board, Bosch recommends at least 24 hrs. to stabilize the sensors.)*

IAQ (Air quality index), target gas scanner selectivity, VOC, VSC data and other BME688 features may be accessed using the Bosch Sensortec Arduino libraries:

- [BME68x Arduino Library](https://github.com/BoschSensortec/Bosch-BME68x-Library)
- [BSEC2 Arduino Library](https://github.com/BoschSensortec/Bosch-BSEC2-Library)

The BME AI-Studio is only available for Win and Mac OS computers and the accompanying Bluetooth app is only available for Android phones. *\*For more information on the available software, please refer to the [Bosch\'s BME688 software page](https://www.bosch-sensortec.com/software-tools/software/bme688-software/).*

*\*For more information on these features, users can also reference the [FAQ page for the BME688](https://community.bosch-sensortec.com/t5/Knowledge-base/FAQs-BME688/ta-p/24822) on Bosch\'s forum.*

### Incorrect Temperature Data

You may notice some deviation from the true ambient temperature in your data as residual heat from the hot plate for the gas sensor in the BME68x0 can cause minor fluctuations in the observed temperature. The heating phase starts after temperature, pressure and humidity measurements are complete so there should be no heating *during* those measurements but subsequent readings may be skewed. The IIR filters can help here but if needed, you can compensate for this by measuring the average deviation and subtracting that from your temperature data.

### Incorrect Altitude Data

The altitude data is collected by converting the barometric pressure. This is a great tool for approximate altitude readings but things like weather patterns can affect the accuracy of the altitude. The examples use the standard measurement for pressure at sea level (1013.25 hPa) in the calculation so you may wish to adjust that with a corrected value for a more accurate altitude data. Refer to this [Wikipedia page](https://en.wikipedia.org/wiki/Atmospheric_pressure) and [this section](https://learn.sparkfun.com/tutorials/mpl3115a2-pressure-sensor-hookup-guide#pressure-vs-altimeter-setting) of our MPL3115 Pressure Sensor Hookup Guide for more information.

### Chip Select Definition

As we covered in the previous section, if you choose to communicate with the BME68x via SPI, make sure you are connecting to the correct pins on your development board (COPI, CIPO, SCK and CS) as well as modifying the Chip Select definition to the appropriate I/O pin used for CS on your controller. If you are not certain which pin is used for CS, refer to documentation for your particular development board.

**BME688 SPI Jumpers:** In order to communicate with the BME688 Qwiic board over SPI, users will need to cut the `CSB` and `ADR` *(leave floating)* jumpers. *\*See the **CSB Jumper** section in the **Hardware Overview** page, for more information.*

**Note:** You may not recognize the COPI/CIPO labels for SPI pins. SparkFun has joined with other members of OSHWA in a resolution to move away from using \"Master\" and \"Slave\" to describe signals between the controller and the peripheral. Check out [this page](https://www.sparkfun.com/spi_signal_names) for more on our reasoning behind this change. You can also see OSHWA\'s resolution [here](https://www.oshwa.org/a-resolution-to-redefine-spi-signal-names).

### Need Assistance?

[] **Need help with something not covered here?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.