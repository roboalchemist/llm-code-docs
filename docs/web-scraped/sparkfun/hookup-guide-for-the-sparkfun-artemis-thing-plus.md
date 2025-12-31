# Source: https://learn.sparkfun.com/tutorials/hookup-guide-for-the-sparkfun-artemis-thing-plus

## Introduction

Our Artemis line would not be complete without including the Feather-compatible [SparkFun Artemis Thing Plus](https://www.sparkfun.com/products/15574). With 21 GPIO Pins - all PWM and interrupt capable - there are 2 I^2^C buses available, as well as SPI and UART. We\'ve included the digital MEMS microphone that allows for always-on voice commands with TensorFlow and machine learning, and the [Qwiic](https://www.sparkfun.com/qwiic) connector makes using our Qwiic sensors as easy as plug and play!

[![SparkFun Thing Plus - Artemis](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/1/7/0/15574-SparkFun_Thing_Plus_-_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html)

### [SparkFun Thing Plus - Artemis](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html) 

[ WRL-15574 ]

The SparkFun Artemis Thing Plus takes our popular Feather footprint and adds in the powerful Artemis module for ultimate func...

[ [\$25.95] ]

### Required Materials

You\'ll need the Artemis Thing Plus and a USB C cable. Any USB C cable should work, including the one that probably came with your phone charger.

[![SparkFun Thing Plus - Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/1/7/0/15574-SparkFun_Thing_Plus_-_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html)

### [SparkFun Thing Plus - Artemis](https://www.sparkfun.com/sparkfun-thing-plus-artemis.html) 

[ WRL-15574 ]

The SparkFun Artemis Thing Plus takes our popular Feather footprint and adds in the powerful Artemis module for ultimate func...

[ [\$25.95] ]

[![USB 2.0 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/5/0/15092-USB_2.0_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/products/15092)

### [USB 2.0 Cable A to C - 3 Foot](https://www.sparkfun.com/products/15092) 

[ CAB-15092 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend checking out these tutorials before continuing:

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/designing-with-the-sparkfun-artemis)

### Designing with the SparkFun Artemis 

Let\'s chat about layout and design considerations when using the Artemis module.

[](https://learn.sparkfun.com/tutorials/artemis-development-with-arduino)

### Artemis Development with Arduino 

Get our powerful Artemis based boards (Artemis Nano, BlackBoard Artemis, and BlackBoard Artemis ATP) blinking in less than 5 minutes using the SparkFun Artemis Arduino Core!

## Hardware Overview

The Artemis Thing Plus has a wide range of functionality to get through, so let\'s have a look, shall we?

### Features:

- 1M Flash / 384k RAM
- 48MHz / 96MHz turbo available
- 21 GPIO Pins - all interrupt capable
- 21 PWM Channels
- Built in BLE radio
- 8 ADC channels with 14-bit precision
- 2 I^2^C buses
- 1 SPI bus
- 2 UARTs
- PDM Digital Microphone
- I^2^S Interface
- Qwiic Connector

[![High res photo of front of board](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Thing_Plus_-_Artemis-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/8/15574-SparkFun_Thing_Plus_-_Artemis-05.jpg)

⚡ **Warning:** All pins are **3.3V**. DO NOT expose the pins to 5V.\
\
The ADC on the Artemis is **0-2V**. Exposing an ADC pin to 3.3V will not harm the device but the ADC will saturate returning 16,383 (14-bit) for voltages greater than 2V.

### Serial and JTAG Programming

The RedBoard Artemis Thing Plus has two methods for programming. The most common is the USB C connector that operates as a USB to serial bridge. By simply pressing \'Upload\' in the Arduino IDE or \'make bootload\' from the SDK the firmware on Artemis is updated.

[![USB-C port for programming the Artemis Thing Plus](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_USBC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_USBC.jpg)

*Click the image for a closer look*

We use the CH340E on the RedBoard Artemis Thing Plus. The driver should automatically install on most operating systems. However, there is a wide range of operating systems out there. You may need to install drivers the first time you connect the chip to your computer\'s USB port or when there are operating system updates. For more information, check out our [How to Install CH340 Drivers Tutorial](https://www.sparkfun.com/ch340).

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

The second method is JTAG programming. An unpopulated JTAG footprint is available for more advanced users who need breakpoint level debugging. We recommend checking out our [JTAG section](https://www.sparkfun.com/categories/tags/jtag) for the compatible male header and a compatible JTAG programmer and debugger.

[![JTag ports for programming the Artemis Thing Plus](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_JTAG_Inset.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_JTAG_Inset.jpg)

*Click the image for a closer look*

### GPIO

The Artemis Thing Plus has 21 available GPIO pins on either side of the board. In addition, there are separate IO for a user button and LED. The LED pin supports PWM but the button\'s pin does not. The [Artemis Thing Plus Schematic](https://cdn.sparkfun.com/assets/6/f/0/5/9/ArtemisThingPlusSchematic.pdf) can give you more information on which of the Apollo3 pads are broken out for the Thing Plus. You can also cross reference this with the [Apollo3 Pad Map](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/8/Apollo3_Pad_Mapping.pdf).

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_GPIO.jpg "GPIO Rails")](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_GPIO.jpg)   [![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_Pin10andLED.jpg "Back View")](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_Pin10andLED.jpg)\

  *GPIO Pin Rails*                                                                                                                                                                                                                             *User Button and LED*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Click on either image for a closer look*

### Qwiic and I^2^C

The I^2^C pins on the Artemis Thing Plus are labeled SDA and SCL on the back of the board. They are controlled in the Arduino IDE using `Wire.begin()`, `Wire.read()`, etc. While pins 16/17 use Wire1, the Qwiic connector uses Wire so you can use SparkFun\'s [Qwiic ecosystem](https://www.sparkfun.com/qwiic) (there\'s over 50 boards and more every week!).

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_Qwiic.jpg "Front View")](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_Qwiic.jpg)   [![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_Qwiic_Back.jpg "Back View")](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_Qwiic_Back.jpg)\

  *Front View: Qwiic Connector and I^2^C Pins 16 and 17*                                                                                                                                                                                         *Back View: Pins 16/SDA1 and 17/SCL1*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Click on either image for a closer look*

### Mic and RTC

The Artemis excels at low power voice recognition. To enable this we\'ve included a PDM MEMS microphone on the board. Additionally, the Artemis module can operate an RTC given an external 32kHz crystal so we\'ve included that was well.

[![PDM Microphone and RTC on RedBoard Artemis Thing Plus](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_mic_rtc_labelled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/8/15574-SparkFun_Artemis_Thing_Plus_mic_rtc_labelled.jpg)

*Click the image for a closer look*

### Board Dimensions

All board dimensions are listed in inches. Overall the pcb measures 2.3x.9 inches with a slight overhang from the USB-C connector.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/8/Artemis_Thing_Plus_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/8/Artemis_Thing_Plus_Dimensions.png)

## Software Setup

The Artemis Thing Plus is capable of running both Arduino and the more advanced [Ambiq](https://ambiq.com/) HAL/SDK. Checkout these tutorials to get you up and blinking in 5 minutes!

[](https://learn.sparkfun.com/tutorials/artemis-development-with-arduino)

### Artemis Development with Arduino 

June 20, 2019

Get our powerful Artemis based boards (Artemis Nano, BlackBoard Artemis, and BlackBoard Artemis ATP) blinking in less than 5 minutes using the SparkFun Artemis Arduino Core!

[](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk)

### Using SparkFun Edge Board with Ambiq Apollo3 SDK 

March 28, 2019

We will demonstrate how to get started with your SparkFun Edge Board by setting up the toolchain on your computer, examining an example program, and using the serial uploader tool to flash the chip.

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\
[**SparkFun Artemis Forums**](https://forum.sparkfun.com/viewforum.php?f=167)