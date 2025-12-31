# Source: https://learn.sparkfun.com/tutorials/micromod-stm32-processor-hookup-guide

## Introduction

We\'ve brought the power and precision of the STM32 Processor to the MicroMod ecosystem! Please welcome the [MicroMod STM32 Processor Board](https://www.sparkfun.com/products/21326)! With the high-performance Arm® Cortex®-M4 32-bit RISC core, Flash memory up to 1 Mbyte, up to 192 Kbytes of SRAM, a memory protection unit (MPU), high-speed embedded memories, up to 4 Kbytes of backup SRAM, and an extensive range of enhanced I/Os and peripherals, this board is ready to rock your MicroMod world. Let\'s dive in!

[![SparkFun MicroMod STM32 Processor](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/1/2/2/STM32F405-_01.jpg)](https://www.sparkfun.com/sparkfun-micromod-stm32-processor.html)

### [SparkFun MicroMod STM32 Processor](https://www.sparkfun.com/sparkfun-micromod-stm32-processor.html) 

[ DEV-21326 ]

The SparkFun MicroMod STM32 Processor Board is ready to rock your MicroMod world with its ARM® Cortex®-M4 32-bit RISC core!

[ [\$20.50] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

The SparkFun MicroMod ecosystem offers a unique way to allow users to customize their project to their needs. Do you want to send your weather data via a wireless signal (e.g. Bluetooth or WiFi)? There\'s a MicroMod Processor Board for that. Looking to instead maximize efficiency and processing power? You guessed it, there\'s a MicroMod Processor Board for that. If you are not familiar with the MicroMod ecosystem, take a look here:

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/micromod).

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend reading through the following tutorials if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

## Hardware Overview

### M.2 Connector

All of our MicroMod Processor boards come equipped with the **M.2 MicroMod Connector**, which leverages the [M.2 standard](https://en.wikipedia.org/wiki/M.2) and specification to allow you to install your MicroMod Processor board on your choice of carrier board.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_M2Front.jpg "M2 Connector")](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_M2Front.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_M2Back.jpg "M2 Connector")](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_M2Back.jpg)\

  *M.2 Connector from the Front*                                                                                                                                                                     *M.2 Connector from the Back*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### STM32F405

There is so much packed into this chip! As stated in the introduction, STMicroelectronics\' STM32F405RG family is based on the ARM Cortex M4 RISC core. At 168MHz, it provides very high performance, floating point single precision, a full set of DSP instructions, and a memory protection unit that enhances application security. For more information, refer to the [Datasheet](https://cdn.sparkfun.com/assets/4/c/b/0/2/stm32f405rg-1851084.pdf).

[![STM32 Arm Cortex is Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_Processor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_Processor.jpg)

### Power

Power is supplied by the carrier board, but it should be noted that all pins are **3.3V**.

⚡ **Warning:** All pins are **3.3V**. DO NOT expose the pins to 5V.\

### Boot and Reset Buttons

In order to upload code to the STM32 MicroMod Processor Board, you\'ll need these two buttons to put the board into Boot mode. Hold the **Boot** button down, press the **Reset** button (while still holding the **Boot** button), and then release the **Boot** button.

These pins will be on the carrier board. For this tutorial, we will show you the these pins on the MicroMod ATP Carrier board.

[![Boot and Reset buttons highlighted on ATP Carrier Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/17713-SparkFun-MicroMod-STM32-Processor_ResetBootButton.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/17713-SparkFun-MicroMod-STM32-Processor_ResetBootButton.jpg)

### Flash

To complement the STM32F405 processor, we\'ve added an additional 128Mb (16MB) serial flash memory chip.

[![Flash chip is highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_Flash.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_Flash.jpg)

### Status LED

[![Status LED is highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_StatusLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/21326-STM32F405-_StatusLED.jpg)

### MicroMod STM32F405 Processor Pin Functionality

The complete pin map can be found in the table below or you can refer to the [schematic](https://cdn.sparkfun.com/assets/8/a/a/7/3/MicroMod_STM32_Processor.pdf).

- [STM32 Processor Pinout Table](#STM32PB)
- [MicroMod General Pinout Table](#MMGen)
- [MicroMod General Pin Descriptions](#MMDescript)

**AUDIO**

**UART**

**GPIO/BUS**

**I^2^C**

**SDIO**

**SPI**

**Dedicated**

  -------------------------------------------------------------------------------------------------------------
  STM32 Pin   Primary Function          Bottom\      Top   \   Primary Function                     STM32 Pin
                                        Pin       Pin                                               
  ----------- ------------------------- --------- ------------ ------------------------------------ -----------
  \-          (Not Connected)                     **75**       GND                                  \-

  \-          3.3V                      **74**    **73**       G5 / BUS5                            PC13

  \-          \-                        **72**    **71**       G6 / BUS6                            PC2

  \-          \-                        **70**    **69**       \-                                   \-

  \-          \-                        **68**    **67**       \-                                   \-

  \-          \-                        **66**    **65**       \-                                   \-

  \-          \-                        **64**    **63**       G10/HOST_VBUS                        PB13

  \-          \-                        **62**    **61**       SPI_PICO (I)                         PA6

  \-          \-                        **60**    **59**       SPI_POCI (O)                         PA7

  \-          \-                        **58**    **57**       SPI_SCK (O)                          PA5

  PB4         AUD_OUT                   **56**    **55**       SPI_CS#                              PC4

  PB5         AUD_IN                    **54**    **53**       I2C_SCL1 (I/O)                       PB6

  PA4         AUD_LRCLK                 **52**    **51**       I2C_SDA1 (I/O)                       PB7

  PB3         AUD_BCLK                  **50**    **49**       BATT_VIN / 3 (I - ADC) (0 to 3.3V)   \-

  PC9         G4 / BUS4                 **48**    **47**       PWM1                                 PC7

  PC8         G3 / BUS3                 **46**    **45**       GND                                  \-

  PA0         G2 / BUS2                 **44**    **43**       CAN_TX                               PB9

  PA8         G1 / BUS1                 **42**    **41**       CAN_RX                               PB8

  PD2         G0 / BUS0                 **40**    **39**       GND                                  \-

  PB0         A1                        **38**    **37**       USBHOST_D-                           PB14

  \-          GND                       **36**    **35**       USBHOST_D+                           PB15

  PC5         A0                        **34**    **33**       GND                                  \-

  PC6         PWM0                      **32**    **31**       Module Key                           \-

  \-          Module Key                **30**    **29**       Module Key                           \-

  \-          Module Key                **28**    **27**       Module Key                           \-

  \-          Module Key                **26**    **25**       Module Key                           \-

  \-          Module Key                **24**    **23**       SWDIO                                PA13

  \-          \-                        **22**    **21**       SWCLK                                PA14

  \-          \-                        **20**    **19**       UART_RX1 (I)                         PA10

  PC1         D1                        **18**    **17**       UART_TX1 (0)                         PA9

  PB1         I2C_INT#                  **16**    **15**       \-                                   \-

  PB10        I2C_SCL (I/0)             **14**    **13**       \-                                   \-

  PB11        I2C_SDA (I/0)             **12**    **11**       BOOT# (I - Open Drain)               BOOT0

  PC0         D0                        **10**    **9**        \-                                   \-

  PB12        G11/HOST_ID               **8**     **7**        GND                                  \-

  \-          RESET# (I - Open Drain)   **6**     **5**        USB_D-                               PA11

  \-          \-                        **4**     **3**        USB_D+                               PA12

  \-          3.3V                      **2**     **1**        GND                                  \-
  -------------------------------------------------------------------------------------------------------------

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
|          |          | SPI_PICO1 | SDIO_DATA0 (I/O)        | **64**  | **63**     | G10                                | ADC_D+  | CAM_VSYNC |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI POCI1 | SDIO_CMD (I/O)          | **62**  | **61**     | SPI_PICO (I)                       |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI SCK1  | SDIO_SCK (O)            | **60**  | **59**     | SPI_POCI (O)                       | LED_DAT |           |    |
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

SPI_POCI

O

SPI Controller Output/Peripheral Input.

3.3V

SPI_PICO

I

SPI Controller Input/Peripheral Output.

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

SPI_POCI1/SDIO_CMD

I/O

2nd SPI Controller Output/Peripheral Input. Secondary use is SDIO command interface.

3.3V

SPI_PICO1/SDIO_DATA0

I/O

2nd SPI Peripheral Input/Controller Output. Secondary use is SDIO data exchange bit 0.

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

\

### Board Outline

The board takes advantage of the standard MicroMod form factor.

[![Board outline and measurements ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/board_outline_cropped.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/board_outline_cropped.png)

## Hardware Assembly

If you have not already, make sure to check out the [Getting Started with MicroMod: Hardware Hookup](https://learn.sparkfun.com/tutorials/getting-started-with-micromod#hardware-hookup) for information on inserting your Processor Board into your Carrier Board.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

October 21, 2020

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

After inserting the MicroMod STM32 processor board into a carrier board, your setup may look like the following:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/STM32_Hookup_Guides-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/STM32_Hookup_Guides-01.jpg)

Go ahead and secure the Processor Board by gently pressing it down and tightening the screw (not too much though).

[![Gently tightening the screw on the micromod carrier board to secure the processor ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/STM32_Hookup_Guides-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/STM32_Hookup_Guides-02.jpg)

## Software Setup and Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Arduino Board Definition

Installation for the STM32 MicroMod Processor is relatively straight-forward. You will want to install the board definitions via the Arduino Boards manager. Search for ***SparkFun STM32*** and you should see the option for the STM32 MicroMod Processor show up.

[![Boards Manager with SparkFun STM32 boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/STM32BoardsManagerInstall.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/STM32BoardsManagerInstall.jpg)

For more information on installing boards via the Arduino Board Manager, check out the [add-ons section of our Installing Arduino IDE tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide#board-add-ons-with-arduino-board-manager).

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### Install STM32Cube Programmer Software

In order to work with the STM32 MicroMod Processor, you\'ll need to install the STM32Cube Programmer. This is an all-in-one multi-OS software tool for programming STM32 products. It primarily provides the driver we need, but you can also program your board using this GUI.

[Get the STM32Cube Programmer Here](https://www.st.com/en/development-tools/stm32cubeprog.html#get-software)

### DFU Bootloader

As of this writing, SparkFun is using the DFU bootloader to upload code to the STM32 MicroMod Processor. In order to do so, you need to do the following:

- Press and hold down the Boot button
- Press and release the Reset button while continuing to press the Boot button
- Keep pressing the Boot button until the code is uploaded

## Examples

### Blink

Let\'s start with something basic - let\'s blink an LED. Go to **File**-\>**Examples**-\>**01.Basics**-\>**Blink**.

[![Blink Basics Example in the pulldown](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/5/BlinkExamplePulldown.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/9/5/BlinkExamplePulldown.png)

*Having a hard time seeing? Click the image for a closer look.*

\
\

Once you\'ve plugged your MicroMod Carrier Board with your MicroMod STM32 Processor into your computer, you\'ll need to go to your Tools menu and set up your options to look like the following:

[![Tools menu with STM32 Options](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/Tools-BoardSetup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/Tools-BoardSetup.jpg)

With everything setup correctly, you\'ll need to put the Carrier Board into *Boot Mode* in order to upload the code.

- Press and hold down the Boot button
- Press and release the Reset button while continuing to press the Boot button
- Release the Boot button and press the *Upload* button in your Arduino IDE

Once the code finishes transferring, you should see the STAT LED on the STM32 Processor Board begin to blink!

[![Status LED on the STM32 MicroMod Processor Board is blinking](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/STM32-01.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/STM32-01.gif)

If the blue LED remains dimly lit, it\'s probably still sitting in the bootloader. After uploading a sketch, you may need to **tap the RST button** to get your STM32 MicroMod Processor Board to begin running the sketch.

### I^2^C Scanner

The Qwiic Connect Ecosystem makes attaching sensors a breeze. That said, sometimes it\'s nice to be able to scan your I^2^C connections to find out the address of your sensor. That\'s what we\'ll do here!

Grab your MicroMod STM32 Processor Board and your Carrier Board, and attach a Qwiic Sensor to the Qwiic port on the Carrier like so:

[![STM32 Processor Board, Carrier Board, and Qwiic sensor attached](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/STM32_Hookup_Guides-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/STM32_Hookup_Guides-03.jpg)

Copy and paste the code below into a new Arduino sketch.

    language:c
    // --------------------------------------
    // I2C Scanner example using Wire1
    //
    //
    // This sketch tests the standard 7-bit addresses
    // Devices with higher bit address might not be seen properly.
    //

    #include <Wire.h>

    TwoWire Wire1(SDA1,SCL1); //Intialize Wire1 class

    void setup()
    

    void loop()
    
        else if (error==4)
            
      }
      if (nDevices == 0)
        Serial.println("No I2C devices found\n");
      else
        Serial.println("done\n");

      delay(5000);           // wait 5 seconds for next scan
    }

Make sure your options are all set up correctly in the *Tools* menu, and make sure you put the Carrier Board into *Boot Mode* in order to upload the code.

- Press and hold down the Boot button
- Press and release the Reset button while continuing to press the Boot button
- Release the Boot button and press the *Upload* button in your Arduino IDE

After uploading, open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and set the baud to **115200**. You should see a similar printout to the one shown below.

[![GIF of screen monitor showing that the qwiic sensor has been found and address 0x48](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/ScannerFindingTMP117.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/ScannerFindingTMP117.gif)

### UART Example

Let\'s have a quick look at an example using UART. If you\'re unfamiliar with Serial Output, go ahead and have a look at our [Serial Basic Tutorial](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide).

Grab your MicroMod STM32 Processor Board and your Carrier Board, and attach the Serial Basic Rx and Tx pins like so:

[![MicroMod ATP board with Serial Basic RX and TXX pins hooked up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/2/7/SparkFun_MicroMod_STM32_Processor_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/SparkFun_MicroMod_STM32_Processor_Tutorial-01.jpg)

*Click on the image for a closer view*

Copy and paste the code below into a new Arduino sketch.

    language:c
    // --------------------------------------
    // UART example using Serial1
    //
    //
    // This sketch prints "Hello World!" every second
    // using the secondary UART pins RX1 and TX1.
    //

    HardwareSerial Serial1(RX1, TX1); //Attach Serial1 to RX1 and TX1

    void setup() 
      Serial1.println("Goodnight moon!");

    }

    void loop() 

Make sure your options are all set up correctly in the *Tools* menu, and make sure you put the Carrier Board into *Boot Mode* in order to upload the code.

- Press and hold down the Boot button
- Press and release the Reset button while continuing to press the Boot button
- Release the Boot button and press the *Upload* button in your Arduino IDE

Once your code is uploaded, open up the Serial Monitor attached to your Serial Basic with the baud rate set to **115200** to see your output!

[![Gif of the serial output printing \"Hello World\" every second](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/SerialOutput.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/SerialOutput.gif)

## Troubleshooting

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

\

[SparkFun Forums: MicroMod](https://forum.sparkfun.com/viewforum.php?f=180)