# Source: https://learn.sparkfun.com/tutorials/micromod-single-pair-ethernet-function-board---adin1110-hookup-guide

## Introduction

The [SparkFun MicroMod Single Pair Ethernet Function Board - ADIN1110](https://www.sparkfun.com/products/19038) introduces 10Base-T1L Single Pair Ethernet protocol into the SparkFun MicroMod ecosystem. Using the ADIN1110 Ethernet transceiver from Analog Devices Inc., this Function Board provides a development tool for long-range, 10Mb/s single-pair 10BASE-T1L Ethernet applications. The 10BASE-T1L Ethernet supported by the ADIN1110 is compatible with the 802.3cg IEEE^®^ standard, supports high bandwidth up to 10Mb/s and can send and receive data on connections over 1 kilometer long! We also have the [MicroMod Single Pair Ethernet Kit](https://www.sparkfun.com/products/24804) that includes nearly everything you need to get started prototyping a MicroMod Single Pair Ethernet connection. Just make sure to grab a pair of MicroMod Processor Boards.

[![SparkFun MicroMod Single Pair Ethernet Function Board - ADIN1110](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/6/4/9/19038-SparkFun_MicroMod_Single_Pair_Ethernet_Function_Board_-_ADIN1110-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-single-pair-ethernet-function-board-adin1110.html)

### [SparkFun MicroMod Single Pair Ethernet Function Board - ADIN1110](https://www.sparkfun.com/sparkfun-micromod-single-pair-ethernet-function-board-adin1110.html) 

[ COM-19038 ]

The SparkFun MicroMod Single Pair Ethernet Function Board introduces 10BASE-T1L Two-Wire Ethernet protocol into the SparkFun ...

[\$49.95] [ [\$26.47] ]

[![SparkFun MicroMod Single Pair Ethernet Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/2/5/0/9/5/KIT-24804-MicroMod-Single-Pair-Ethernet-Feature_1.jpg)](https://www.sparkfun.com/sparkfun-micromod-single-pair-ethernet-kit-kit-24804.html)

### [SparkFun MicroMod Single Pair Ethernet Kit](https://www.sparkfun.com/sparkfun-micromod-single-pair-ethernet-kit-kit-24804.html) 

[ KIT-24804 ]

The SparkFun MicroMod Single Pair Ethernet Kit demonstrates 10BASE-T1L Two-Wire Ethernet protocol into the SparkFun MicroMod ...

**Retired**

In this guide we\'ll cover the basics of 10BASE-T1L Single-Pair Ethernet (SPE), what to expect from the ADIN1110 and other hardware present on this Function Board, how to assemble a SPE circuit and use it with our ADIN1110 Arduino Library.

### Required Materials

The following materials are necessary for following along with this guide. All Function Boards require a Main Board and Processor to connect to each other. Depending on your application, you may need a Single or Dual Main Board:

[![SparkFun MicroMod Main Board - Double](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/4/2/5/20595-DEV_SparkFun_MicroMod_Main_Board_Double_v22-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-double.html)

### [SparkFun MicroMod Main Board - Double](https://www.sparkfun.com/sparkfun-micromod-main-board-double.html) 

[ DEV-20595 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with up to two...

[ [\$22.95] ]

[![SparkFun MicroMod Main Board - Single](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/7/7/20748-DEV_SparkFun_MicroMod_Main_Board_Single_v21-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html)

### [SparkFun MicroMod Main Board - Single](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html) 

[ DEV-20748 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with a single ...

[ [\$18.50] ]

A Processor Board is needed to act as a host controller for the Function Board:

[![SparkFun MicroMod Teensy Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/2/16402-SparkFun_MicroMod_Teensy_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html)

### [SparkFun MicroMod Teensy Processor](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html) 

[ DEV-16402 ]

This board leverages the awesome computing power of the NXP iMXRT1062 chip (ARM Cortex-M7) and pairs it with the M.2 MicroMod...

[ [\$24.95] ]

[![SparkFun MicroMod ESP32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/8/0/16781-SparkFun_MicroMod_ESP32_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html)

### [SparkFun MicroMod ESP32 Processor](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html) 

[ WRL-16781 ]

This board combines Espressif\'s ESP32 with our M.2 connector interface to bring a power-packed processor board into our Micro...

[ [\$19.95] ]

[![SparkFun MicroMod SAMD51 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/8/16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html)

### [SparkFun MicroMod SAMD51 Processor](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html) 

[ DEV-16791 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun MicroMod SAMD51 Processor Board is one powerful microcontroller packaged on a ...

[ [\$18.95] ]

[![SparkFun MicroMod Artemis Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/0/16401-SparkFun_MicroMod_Artemis_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html)

### [SparkFun MicroMod Artemis Processor](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html) 

[ DEV-16401 ]

Featuring the Artemis Module, this processor is capable of machine learning, Bluetooth, I2C, GPIO, PWM, SPI & packaged to fit...

[ [\$17.50] ]

Finally, a Single Pair Ethernet cable is required to connect the two MicroMod assemblies to each other:

[![Single Pair Ethernet Cable - 0.5m (Shielded)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/9/4/1/19312-Industrial_Ethernet_Cable_-_Shielded__1.64_-01.jpg)](https://www.sparkfun.com/single-pair-ethernet-cable-0-5m-shielded.html)

### [Single Pair Ethernet Cable - 0.5m (Shielded)](https://www.sparkfun.com/single-pair-ethernet-cable-0-5m-shielded.html) 

[ CAB-19312 ]

This 0.5m SPE cable enables Ethernet data transmissions by using only two wires and the simultaneous power supply for termina...

[ [\$21.75] ]

[ ![Single Pair Ethernet Cable - 20m (Shielded)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/9/9/5/19364-Industrial_Ethernet_Cable_-_Shielded__20m.jpeg) ]

### Single Pair Ethernet Cable - 20m (Shielded) 

[ CAB-19364 ]

This 20m SPE cable enables Ethernet data transmissions by using only two wires and the simultaneous power supply for terminal...

**Retired**

### Suggested Reading

The [MicroMod ecosystem](https://www.sparkfun.com/micromod) is a unique way to allow users to customize their project to their needs. If you aren\'t familiar with the MicroMod system, click on the banner below for more information.

[![MicroMod Logo](https://cdn.sparkfun.com/r/500-70/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)

\

You may also want to read the tutorials below if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

## Hardware Overview

In this section we\'ll take a closer look at the hardware on this Function Board along with a brief overview of what exactly 10BASE-T1L Single Pair Ethernet is and what benefits it provides.

### 10BASE-T1L Single Pair Ethernet

The 10BASE-T1L Single Pair Ethernet (SPE) standard uses just a single twisted pair for data as well as power. 10BASE-T1L Ethernet transmits data at speeds up to 10Mbps at distances up to 1.7km. With just a single pair, the cable is smaller and lighter making it ideal for remote monitoring or industrial applications connecting a large number of edge devices to a network connection.

For more information about 10BASE-T1L SPE, refer to [this article](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/6/A347176how-a-10base-t1l-mac-phy-simplifies-low-power-processor-ethernet-connectivity.pdf) on the communication protocol from Analog Devices or [this SparkFun news post](https://www.sparkfun.com/news/4637).

### ADIN1110

The ADIN1110 is an ultra-low power Ethernet transceiver for 10BASE-T1L IEEE Standard 802.3cg-2019 SPE.

[![Highlighting the ADIN1110 IC](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-IC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-IC.jpg)

It operates from a supply voltage of **1.8V** or **3.3V**. This Function Board runs the ADIN1110 in single-supply mode at **3.3V** (VDD_H and VVD_L are both powered at **3.3V**) and this allows for transmission amplitude of **2.4V**. For a complete overview of the ADIN1110 IC, refer to the [datasheet](https://cdn.sparkfun.com/assets/5/5/c/5/1/adin1110.pdf).

The ADIN1110 MAC supports 16 individual MAC addresses and communicates over both Open Alliance and generic SPI protocols. The ADIN1110 transmits data at half duplex when using generic SPI and full duplex when using the Open Alliance protocol. The IC also includes support for three LED outputs, a Link LED and two configurable general purpose LEDs. The Function Board breaks out all of those to LEDs on board. Read on to the LEDs section below for more information.

#### SPE Data Output

The Function Board routes the ADIN1110\'s data signal pairs through a TVS diode protection circuit and phase transformer from Würth Elektronik before terminating in a specialized T1 Industrial Jack for connection to a separate SPE device or network hub.

[![Highlighting SPE Data Output components](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-T1_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-T1_Output.jpg)

For more information about the TZ Industrial Jack, refer to the [datasheet](https://cdn.sparkfun.com/assets/8/3/1/2/1/PDF_DS_09452812800_EN.pdf).

### Power

The Function Board receives power from the Main Board it connects to. The Main Board can be powered either via USB or a connected LiPo battery. Reminder, this Function Board is not designed to send power over the Single Pair Ethernet connection.

### LEDs

This Function Board includes four LEDs labeled **PWR**, **LED 0**, **LED 1** and **LINK ST**.

[![Highlighting the LEDs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-LEDs.jpg)

- **PWR** - Power LED.
- **LED 0** - General purpose programmable LED. Active LOW. Default configuration turns the LED on when a link is established and blinks on activity.
- **LED 1** - General purpose programmable LED. Active LOW. Default configuration disables the LED.
- **LINK ST** - Link status LED. Active HIGH. LED illuminates with a valid link.

For detailed instructions on programming the general purpose LEDs, refer to the LED Control Register section of the [ADIN1110 Datasheet](https://cdn.sparkfun.com/assets/5/5/c/5/1/adin1110.pdf) or the [SparkFun ADIN1110 Arduino Library](https://github.com/sparkfun/SparkFun_ADIN1110_Arduino_Libary).

### Solder Jumpers

This function board has twelve solder jumpers. The table below outlines each jumper\'s label, function, default states and any notes about their use.

[![Photo highlighting the solder jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-Solder_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-Solder_Jumpers.jpg)

*Having trouble seeing the detail in the image? Click on it for a larger view.*

+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Label    | Default State  | Function                                                                                      | Notes                                                                                                                                                                                                                                                                                                                                    |
+==========+================+===============================================================================================+==========================================================================================================================================================================================================================================================================================================================================+
| SHLD     | CAP (See note) | Double jumper to select connector shield grounding option.                                    | Default connects the connector shield to ground through a 3.3nF capacitor. Switch to GND side to connect the shield directly to ground.                                                                                                                                                                                                  |
+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LED1     | CLOSED         | Completes LED1 configurable LED circuit.                                                      | Open to disable the labeled LED. Helps reduce the total current draw.                                                                                                                                                                                                                                                                    |
+----------+----------------+-----------------------------------------------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                          |
| LINKST   | CLOSED         | Completes the Link Status LED circuit.                                                        |                                                                                                                                                                                                                                                                                                                                          |
+----------+----------------+-----------------------------------------------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                          |
| LED0     | CLOSED         | Completes the LED0 configurable LED circuit.                                                  |                                                                                                                                                                                                                                                                                                                                          |
+----------+----------------+-----------------------------------------------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                          |
| PWR      | CLOSED         | Completes the Power LED circuit.                                                              |                                                                                                                                                                                                                                                                                                                                          |
+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TX2P4 EN | OPEN           | Pulls TX2P4_EN pin LOW.                                                                       | Controls the transmit amplitude mode. By default, this pin is LOW and allows both **1.0V** and **2.4V** p-p transmit levels. Pulling this pin high disables **2.4V** transmit level.^[1](#ADIN1110_Config)^                                                                                                                              |
+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWPD EN  | OPEN           | Pulls SWPD_EN pin LOW.                                                                        | Controls whether or not the ADIN1110 enters software power-down mode after reset. By default, the ADIN1110 starts autonegotiation after a reset. If the jumper is closed, the ADIN1110 remains in power-down mode after reset until it is configured over SPI. This allows software control over power-down mode.^[1](#ADIN1110_Config)^ |
+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MS SEL   | OPEN           | Sets the ADIN1110 to operate as a peripheral (slave) device on SPI.                           | Controls whether the ADIN1110 defaults to a controller or peripheral on the SPI bus.^[1](#ADIN1110_Config)^                                                                                                                                                                                                                              |
+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPI CFG1 | OPEN           | Sets the ADIN1110 to use OPEN Aliance SPI protocol with protection (if SPI_CFG0 is also LOW). |                                                                                                                                                                                                                                                                                                                                          |
+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPI CFG0 | OPEN           | Sets the ADIN1110 to use OPEN Aliance SPI protocol with protection (if SPI_CFG1 is also LOW). |                                                                                                                                                                                                                                                                                                                                          |
+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EWP      | OPEN           | EEPROM write protection.                                                                      |                                                                                                                                                                                                                                                                                                                                          |
+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MEAS     | CLOSED         | Ties VCC_IN to input on **3.3V** voltage regulator.                                           | Open to measure current draw of the board.                                                                                                                                                                                                                                                                                               |
+----------+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[**1.**](https://learn.sparkfun.com/tutorials/micromod-single-pair-ethernet-function-board---adin1110-hookup-guide/hardware-overview#ADIN1110_Config) Refer to page 16 of the [datasheet](https://cdn.sparkfun.com/assets/5/5/c/5/1/adin1110.pdf) for more information on the configuration pins.

### MicroMod Edge Connector and Pinout

The MicroMod ecosystem uses a polarized M.2 edge connector to provide a standardized electrical connection that is keyed to prevent incorrect connection between MicroMod boards. The attachment points for the screws prevent users from connecting a processor board into a function board slot and vice-versa.

[![Highlighting the M2 connector amd mounting points](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-M2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-M2.jpg)

#### MicroMod Pinout

This Function Board uses the following pins on a connected Processor Board:

- 3.3V & VCC
- Power enable
- SPI - ADIN1110 Communication
- I^2^C - EEPROM Comunication
- D0 (Slot 0) / D1 (Slot 1) - ADIN1110 Interrupt
- CS0 (Slot 0) / CS1 (Slot 1) - ADIN1110 Chip Select (SPI)

For the complete MicroMod Pinout and pins used by this function board, take a look at the tables below:

- [SPE Function Board - ADIN1110 Pinout Table](#SPEethernet)
- [MicroMod General Processor Pinout Table](#MMGen)
- [MicroMod General Pin Descriptions](#MMDescript)

**AUDIO**

**UART**

**GPIO/BUS**

**I^2^C**

**SDIO**

**SPI0**

**Dedicated**

+-----------------------------------------------------------+---------+------------+---------------------------------------------------------------+
| Function                                                  | Bottom\ |    Top   \ | Function                                                      |
|                                                           | Pin     | Pin        |                                                               |
+==========+==========+===========+=========================+=========+============+====================================+=========+===========+====+
|          |          |           | (Not Connected)         |         | **75**     | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | 3.3V                    | **74**  | **73**     | G5 / BUS5                          |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | RTC_3V_BATT             | **72**  | **71**     | G6 / BUS6                          |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI_CS1#  | SDIO_DATA3 (I/O)        | **70**  | **69**     | G7 / BUS7                          |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | SDIO_DATA2 (I/O)        | **68**  | **67**     | G8                                 |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | SDIO_DATA1 (I/O)        | **66**  | **65**     | G9                                 | ADC_D-  | CAM_HSYNC |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI_CIPO1 | SDIO_DATA0 (I/O)        | **64**  | **63**     | G10                                | ADC_D+  | CAM_VSYNC |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI COPI1 | SDIO_CMD (I/O)          | **62**  | **61**     | SPI_CIPO (I)                       |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI SCK1  | SDIO_SCK (O)            | **60**  | **59**     | SPI_COPI (O)                       | LED_DAT |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | AUD_MCLK (O)            | **58**  | **57**     | SPI_SCK (O)                        | LED_CLK |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
| CAM_MCLK | PCM_OUT  | I2S_OUT   | AUD_OUT                 | **56**  | **55**     | SPI_CS#                            |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
| CAM_PCLK | PCM_IN   | I2S_IN    | AUD_IN                  | **54**  | **53**     | I2C_SCL1 (I/O)                     |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
| PDM_DATA | PCM_SYNC | I2S_WS    | AUD_LRCLK               | **52**  | **51**     | I2C_SDA1 (I/O)                     |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
| PDM_CLK  | PCM_CLK  | I2S_SCK   | AUD_BCLK                | **50**  | **49**     | BATT_VIN / 3 (I - ADC) (0 to 3.3V) |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G4 / BUS4               | **48**  | **47**     | PWM1                               |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G3 / BUS3               | **46**  | **45**     | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G2 / BUS2               | **44**  | **43**     | CAN_TX                             |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G1 / BUS1               | **42**  | **41**     | CAN_RX                             |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G0 / BUS0               | **40**  | **39**     | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | A1                      | **38**  | **37**     | USBHOST_D-                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | GND                     | **36**  | **35**     | USBHOST_D+                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | A0                      | **34**  | **33**     | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | PWM0                    | **32**  | **31**     | Module Key                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | Module Key              | **30**  | **29**     | Module Key                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | Module Key              | **28**  | **27**     | Module Key                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | Module Key              | **26**  | **25**     | Module Key                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | Module Key              | **24**  | **23**     | SWDIO                              |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | UART_TX2 (O)            | **22**  | **21**     | SWDCK                              |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | UART_RX2 (I)            | **20**  | **19**     | UART_RX1 (I)                       |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | CAM_TRIG  | D1                      | **18**  | **17**     | UART_TX1 (0)                       |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | I2C_INT#                | **16**  | **15**     | UART_CTS1 (I)                      |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | I2C_SCL (I/0)           | **14**  | **13**     | UART_RTS1 (O)                      |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | I2C_SDA (I/0)           | **12**  | **11**     | BOOT (I - Open Drain)              |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | D0                      | **10**  | **9**      | USB_VIN                            |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SWO       | G11                     | **8**   | **7**      | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | RESET# (I - Open Drain) | **6**   | **5**      | USB_D-                             |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | 3.3V_EN                 | **4**   | **3**      | USB_D+                             |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | 3.3V                    | **2**   | **1**      | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+

  ----------------------------------------------------------------------------------------------------------------------------------------------------------
  Description                                                Function          Bottom\      Top   \   Function     Description
                                                                               Pin       Pin                       
  ---------------------------------------------------------- ----------------- --------- ------------ ------------ -----------------------------------------
                                                             (Not Connected)             **75**       GND          

                                                             \-                **74**    **73**       3.3V         Power Supply: 3.3-6V

                                                             \-                **72**    **71**       Power EN     Power Enable

                                                             \-                **70**    **69**       \-           

                                                             \-                **66**    **65**       \-           

                                                             \-                **64**    **63**       \-           

                                                             \-                **62**    **61**       \-           

                                                             \-                **60**    **59**       \-           

                                                             \-                **58**    **57**       \-           

                                                             \-                **56**    **55**       RESET        ADIN1110 Reset Button

                                                             \-                **54**    **53**       \-           

                                                             \-                **52**    **51**       \-           

                                                             \-                **50**    **49**       CS           ADIN1110 Chip Select

                                                             \-                **48**    **47**       INT          ADIN1110 Interrupt Pin

                                                             \-                **46**    **45**       GND          

                                                             \-                **44**    **43**       \-           

                                                             \-                **42**    **41**       \-           

  Write protection pin for the EEPROM. Pull low to enable.   EEPROM_WP         **40**    **39**       GND          

                                                             \-                **38**    **37**       \-           

  EEPROM I^2^C address configuration.                        EEPROM_A0         **36**    **35**       \-           

  EEPROM I^2^C address configuration.                        EEPROM_A1         **34**    **33**       GND          

  EEPROM I^2^C address configuration.                        EEPROM_A2         **32**    **31**       Module Key   

                                                             Module Key        **30**    **29**       Module Key   

                                                             Module Key        **28**    **27**       Module Key   

                                                             Module Key        **26**    **25**       Module Key   

                                                             Module Key        **24**    **23**       \-           

                                                             \-                **22**    **21**       I2C_SCL      I^2^C - Clock signal for EEPROM

                                                             \-                **20**    **19**       I2C_SDA      I^2^C - Data signal for EEPROM

                                                             \-                **18**    **17**       \-           

                                                             \-                **16**    **15**       \-           

                                                             \-                **14**    **13**       \-           

                                                             \-                **12**    **11**       \-           

                                                             \-                **10**    **9**        \-           

                                                             \-                **8**     **7**        POCI         SPI Peripheral Output/Controller Input.

                                                             \-                **6**     **5**        PICO         SPI Peripheral Input/Controller Output.

                                                             \-                **4**     **3**        SCK          SPI Clock Signal

                                                             \-                **2**     **1**        GND          
  ----------------------------------------------------------------------------------------------------------------------------------------------------------

Signal Group

Signal

I/O

Description

Voltage

Power

3.3V

I

3.3V Source

3.3V

GND

Return current path

0V

USB_VIN

I

USB VIN compliant to USB 2.0 specification. Connect to pins on processor board that require 5V for USB functionality

4.8-5.2V

RTC_3V_BATT

I

3V provided by external coin cell or mini battery. Max draw=100μA. Connect to pins maintaining an RTC during power loss. Can be left NC.

3V

3.3V_EN

O

Controls the carrier board\'s main voltage regulator. Voltage above 1V will enable 3.3V power path.

3.3V

BATT_VIN/3

I

Carrier board raw voltage over 3. 1/3 resistor divider is implemented on carrier board. Amplify the analog signal as needed for full 0-3.3V range

3.3V

Reset

Reset

I

Input to processor. Open drain with pullup on processor board. Pulling low resets processor.

3.3V

Boot

I

Input to processor. Open drain with pullup on processor board. Pulling low puts processor into special boot mode. Can be left NC.

3.3V

USB

USB_D±

I/O

USB Data ±. Differential serial data interface compliant to USB 2.0 specification. If UART is required for programming, USB± must be routed to a USB-to-serial conversion IC on the processor board.

USB Host

USBHOST_D±

I/O

For processors that support USB Host Mode. USB Data±. Differential serial data interface compliant to USB 2.0 specification. Can be left NC.

CAN

CAN_RX

I

CAN Bus receive data.

3.3V

CAN_TX

O

CAN Bus transmit data.

3.3V

UART

UART_RX1

I

UART receive data.

3.3V

UART_TX1

O

UART transmit data.

3.3V

UART_RTS1

O

UART ready to send.

3.3V

UART_CTS1

I

UART clear to send.

3.3V

UART_RX2

I

2nd UART receive data.

3.3V

UART_TX2

O

2nd UART transmit data.

3.3V

I2C

I2C_SCL

I/O

I^2^C clock. Open drain with pullup on carrier board.

3.3V

I2C_SDA

I/O

I^2^C data. Open drain with pullup on carrier board

3.3V

I2C_INT#

I

Interrupt notification from carrier board to processor. Open drain with pullup on carrier board. Active LOW

3.3V

I2C_SCL1

I/O

2nd I^2^C clock. Open drain with pullup on carrier board.

3.3V

I2C_SDA1

I/O

2nd I^2^C data. Open drain with pullup on carrier board.

3.3V

SPI

SPI_PICO

O

SPI Peripheral Input/Controller Output.

3.3V

SPI_POCI

I

SPI Peripheral Output/Controller Input.

3.3V

SPI_SCK

O

SPI Clock.

3.3V

SPI_CS#

O

SPI Chip Select. Active LOW. Can be routed to GPIO if hardware CS is unused.

3.3V

SPI/SDIO

SPI_SCK1/SDIO_CLK

O

2nd SPI Clock. Secondary use is SDIO Clock.

3.3V

SPI_PICO1/SDIO_CMD

I/O

2nd SPI Peripheral Input/Controller Output. Secondary use is SDIO command interface.

3.3V

SPI_POCI1/SDIO_DATA0

I/O

2nd SPI Controller Output/Peripheral Input. Secondary use is SDIO data exchange bit 0.

3.3V

SDIO_DATA1

I/O

SDIO data exchange bit 1.

3.3V

SDIO_DATA2

I/O

SDIO data exchange bit 2.

3.3V

SPI_CS1/SDIO_DATA3

I/O

2nd SPI Chip Select. Secondary use is SDIO data exchange bit 3.

3.3V

Audio

AUD_MCLK

O

Audio master clock.

3.3V

AUD_OUT/PCM_OUT/I2S_OUT/CAM_MCLK

O

Audio data output. PCM synchronous data output. I2S serial data out. Camera master clock.

3.3V

AUD_IN/PCM_IN/I2S_IN/CAM_PCLK

I

Audio data input. PCM syncrhonous data input. I2S serial data in. Camera periphperal clock.

3.3V

AUD_LRCLK/PCM_SYNC/I2S_WS/PDM_DATA

I/O

Audio left/right clock. PCM syncrhonous data SYNC. I2S word select. PDM data.

3.3V

AUD_BCLK/PCM_CLK/I2S_CLK/PDM_CLK

O

Audio bit clock. PCM clock. I2S continuous serial clock. PDM clock.

3.3V

SWD

SWDIO

I/O

Serial Wire Debug I/O. Connect if processor board supports SWD. Can be left NC.

3.3V

SWDCK

I

Serial Wire Debug clock. Connect if processor board supports SWD. Can be left NC.

3.3V

ADC

A0

I

Analog to digital converter 0. Amplify the analog signal as needed to enable full 0-3.3V range.

3.3V

A1

I

Analog to digital converter 1. Amplify the analog signal as needed to enable full 0-3.3V range.

3.3V

PWM

PWM0

O

Pulse width modulated output 0.

3.3V

PWM1

O

Pulse width modulated output 1.

3.3V

Digital

D0

I/O

General digital input/output pin.

3.3V

D1/CAM_TRIG

I/O

General digital input/output pin. Camera trigger.

3.3V

General/Bus

G0/BUS0

I/O

General purpose pins. Any unused processor pins should be assigned to Gx with ADC + PWM capable pins given priority (0, 1, 2, etc.) positions. The intent is to guarantee PWM, ADC and Digital Pin functionality on respective ADC/PWM/Digital pins. Gx pins do not guarantee ADC/PWM function. Alternative use is pins can support a fast read/write 8-bit or 4-bit wide bus.

3.3V

G1/BUS1

I/O

3.3V

G2/BUS2

I/O

3.3V

G3/BUS3

I/O

3.3V

G4/BUS4

I/O

3.3V

G5/BUS5

I/O

3.3V

G6/BUS6

I/O

3.3V

G7/BUS7

I/O

3.3V

G8

I/O

General purpose pin

3.3V

G9/ADC_D-/CAM_HSYNC

I/O

Differential ADC input if available. Camera horizontal sync.

3.3V

G10/ADC_D+/CAM_VSYNC

I/O

Differential ADC input if available. Camera vertical sync.

3.3V

G11/SWO

I/O

General purpose pin. Serial Wire Output

3.3V

### Board Dimensions

This Function Board uses the standard sizing for MicroMod Function Boards and measures 2.56\" x 1.48\" (65.02mm x 37.59mm) and the T1 jack protrudes roughly 0.15\" (3.81mm) from the edge of the board.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-Dimensions.png)

## Hardware Assembly

If you\'re not familiar with assembling boards using the MicroMod connection system, head over to the MicroMod Main Board Hookup Guide for information on inserting and securing your MicroMod Processor and Function Boards to the Main Board:

[](https://learn.sparkfun.com/tutorials/micromod-main-board-hookup-guide)

### MicroMod Main Board Hookup Guide 

November 11, 2021

The MicroMod Main Board - Single and Double are specialized carrier boards that allow you to interface a Processor Board with a Function Board(s). The modular system allows you to add an additional feature(s) to a Processor Board with the help of a Function Board(s). In this tutorial, we will focus on the basic functionality of the Main Board - Single and Main Board - Double.

### Single Pair Ethernet Basic Assembly

With the Function and Processor Boards connected to their respective Main Boards, we can complete the assembly of the Single Pair Ethernet circuit. For a basic SPE prototyping circuit either with your own setup or with the Single Pair Ethernet Kit, connect the two MicroMod assemblies together using a Single Pair Ethernet Cable and then power the two MicroMod Main Boards via USB-C like the photo below:

[![Basic SPE Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-Basic_Circuit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-Basic_Circuit.jpg)

### Demo Circuit Assembly

We\'ll be assembling a demo circuit that works with an example pair included in the ADIN1110 Arduino Library that sends environmental data recorded by the [SparkFun Atmospheric Sensor Breakout - BME280 (Qwiic)](http://www.sparkfun.com/products/15440) connected to one SPE MicroMod assembly to display on a [SparkFun 20x4 SerLCD - RGB Backlight (Qwiic)](https://www.sparkfun.com/products/16398) connected to the opposite SPE MicroMod assembly.

Connect the Qwiic boards to the Qwiic connector on their respective MicroMod Main Boards then plug the SPE cable into the T1 jacks on each Function Board. Once all of those are connected, power the MicroMod Main boards with USB-C cables. The completed demo circuit should look like the photo below:

[![Completed BME / LCD Demo Circuit Assembly](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-Demo_Circuit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/6/MM_SPE_ADIN1110-Demo_Circuit.jpg)

*Having trouble seeing the detail in the image? Click on it for a larger view.*

Now that our demo circuit is complete, we can move on to uploading the code to establish a SPE link and send data between the two MicroMod assemblies.

## Software Setup

**Note:** This library assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino or if you need a refresher, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### SparkFun ADIN1110 Arduino Library

The SparkFun ADIN1110 Arduino Library includes several examples to get started communicating between two ADIN1110 Function Boards. The library is hosted on [GitHub](https://github.com/sparkfun/SparkFun_ADIN1110_Arduino_Libary). Install the library through the Arduino Library Manager tool by searching for **\"SparkFun ADIN1110 Arduino Library\"**. Users who prefer to manually install it can grab it from the repository or download it directly by clicking the button below:

[SparkFun ADIN1110 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_ADIN1110_Arduino_Libary/archive/refs/heads/main.zip)

The SparkFun ADIN1110 Arduino Library includes a wide set of examples to demonstrate different ways to configure and use the ADIN1110. They include basic examples to get up and running as well as advanced examples for users who prefer to customize the performance and memory use in transmissions.

### Processor Arduino Board Definitions and Driver

Make sure you go through the Hookup Guide for your chosen Processor Board to install the latest Arduino board definitions and any necessary drivers:

[](https://learn.sparkfun.com/tutorials/micromod-esp32-processor-board-hookup-guide)

### MicroMod ESP32 Processor Board Hookup Guide 

October 21, 2020

A short hookup guide to get started with the SparkFun MicroMod ESP32 Processor Board.

[](https://learn.sparkfun.com/tutorials/micromod-stm32-processor-hookup-guide)

### MicroMod STM32 Processor Hookup Guide 

May 13, 2021

Get started with the MicroMod Ecosystem and the STM32 Processor Board!

[](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide)

### MicroMod Teensy Processor Hookup Guide 

July 1, 2021

Add the processing power and versatility of the Teensy to your MicroMod project following this guide for the SparkFun MicroMod Teensy Processor.

### Pin Connection Table

The table below helps show which pins the Function Board connects to depending on the slot it is connected to on a Main Board (Note: The Single Main Board connection is Slot 0):

**AUDIO**

**UART**

**GPIO/BUS**

**I^2^C**

**SDIO**

**SPI0**

**Dedicated**

Function Board\
Pin Name

I/O\
Direction

Main Board\'s\
Processor Pin

Slot 0

Slot 1

VCC

Input

\-

3.3V

Input

\-

GND

\-

\-

INT

D0

D1

CS

CS0

CS1

## Arduino Examples

The SparkFun ADIN1110 Arduino Library includes several sets of examples to get started communicating between ADIN1110 nodes. In this section we\'ll take a look at the Arduino example pair for the demo circuit shown in the Hardware Assembly section.

### Example Set 3 - Transmit BME280 / Receive LCD Display

**Note:** This example pair requires two additional libraries; the SparkFun BME280 Library and SparkFun SerLCD Library. Install them through the Arduino Library Manger tool or download them for manual install by clicking the buttons below:\
\

[SparkFun SerLCD Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_SerLCD_Arduino_Library/archive/refs/heads/master.zip)

\

[SparkFun BME280 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_BME280_Arduino_Library/archive/refs/heads/master.zip)

The Example 3 set (3a & 3b) work together to send environmental data from a BME280 connected to the transmitter MicroMod assembly to display on a LCD attached to the receiver MicroMod assembly.

Open an instance of the Arduino IDE for both boards and open the examples by going to **File/Examples/SparkFun ADIN1110 Arduino Library/Example 03A_TransmitStrBME280 / 03B_RxStrSerLCD**. Take note of the ports for both Processors to keep track of which board is which. Upload the examples to both boards and once a link is confirmed, the boards should start sending/receiving data between each other. If you do not see data or the LINK LEDs lighting up on both Function Boards, open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and reset both boards. The code will print out debug data that may help troubleshoot issues with the SPE link.

#### Example 3A - BME280 Transmit

Example 3A creates the frame parameters for sending data measured by the BME280 and then sends that data over to the receiver every five seconds by default. If the readings from the BME280 change beyond a specified threshold in between reports, the code overrides the five second delay and sends a force report.

#### Example 3B - LCD Receive

Example 3B readies the ADIN1110 to receive data from the BME280 on the other Function Board and then prints the data to a LCD connected to the MicroMod main board. When starting up, the display will print out \"Waiting for connection\" and then \"Connected\" once a link is established. After establishing the link, the display should update with new data every five seconds or more often if the transmit Function Board receives a force update due to large changes in readings from the BME280.

## Troubleshooting

Here are a couple of quick troubleshooting tips to use if you run into issues creating a link between ADIN1110\'s.

### Check Board/Library Versions

If you have any issues with the Arduino Library and a SparkFun MicroMod Processor, make sure you have the latest versions of both the Processor Board definitions and the Arduino Library.

### Reset Sequence

If the boards do not establish a link when running the example sets from the Arduino library, hold the RESET buttons on the Main Boards down at the same time. Release the RESET button on the receiving board (eg. the LCD circuit for the demo example) first and then release the RESET button on the transmitting after.

### General Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums: MicroMod](https://forum.sparkfun.com/viewforum.php?f=180) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[SparkFun Forums: MicroMod](https://forum.sparkfun.com/viewforum.php?f=180)