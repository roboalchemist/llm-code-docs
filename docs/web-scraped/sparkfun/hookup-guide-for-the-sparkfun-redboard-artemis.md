# Source: https://learn.sparkfun.com/tutorials/hookup-guide-for-the-sparkfun-redboard-artemis

## Introduction

The [SparkFun RedBoard Artemis](https://www.sparkfun.com/products/15444) encapsulates all the lessons we\'ve learned through the years of improving on the original Arduino Uno while adding in the powerful Artemis module so that you can easily use the Cortex-M4F. Let\'s dive in!

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

### Required Materials

You\'ll need the RedBoard Artemis and a USB C cable. Any USB C cable should work, including the one that probably came with your phone charger. If you don\'t have a cable you can get a 3 foot one [here](https://www.sparkfun.com/products/15092) or a fancy reversible one [here](https://www.sparkfun.com/products/15424).

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

[![Reversible USB A to C Cable - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/3/15424-Reversible_USB_A_to_C_Cable_-_2m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html)

### [Reversible USB A to C Cable - 2m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html) 

[ CAB-15424 ]

These 2m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the U...

[ [\$10.50] ]

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

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

[](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk)

### Using SparkFun Edge Board with Ambiq Apollo3 SDK 

We will demonstrate how to get started with your SparkFun Edge Board by setting up the toolchain on your computer, examining an example program, and using the serial uploader tool to flash the chip.

[](https://learn.sparkfun.com/tutorials/designing-with-the-sparkfun-artemis)

### Designing with the SparkFun Artemis 

Let\'s chat about layout and design considerations when using the Artemis module.

[](https://learn.sparkfun.com/tutorials/artemis-development-with-arduino)

### Artemis Development with Arduino 

Get our powerful Artemis based boards (Artemis Nano, BlackBoard Artemis, and BlackBoard Artemis ATP) blinking in less than 5 minutes using the SparkFun Artemis Arduino Core!

## Hardware Overview

If you\'ve ever used an Arduino Uno before you should be pretty familiar with the various female headers and the barrel jack power. If you\'re new to Arduino boards, check out the [SparkFun RedBoard Qwiic tutorial](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide) for more information on many of the basic board functions you\'ll see on the Artemis RedBoard. In this tutorial we\'ll be covering the unique aspects of the RedBoard Artemis.

[![SparkFun RedBoard Artemis Front View](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun_RedBoard_HighResFront.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun_RedBoard_HighResFront.jpg)

⚡ **Warning:** All pins are **3.3V**. DO NOT expose the pins to 5V.\
\
The ADC on the Artemis is **0-2V**. Exposing an ADC pin to 3.3V will not harm the device but the ADC will saturate returning 16,383 (14-bit) for voltages greater than 2V.

### GPIO

Looking at the front of the Artemis RedBoard, you\'ll notice that alongside the female headers are plated through-holes. We\'ve found that while we enjoy the ease of using the headers, sometimes we just want to [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) directly to our board. To that end, we\'ve added the PTH rails. Note that these are NOT all ground pins - these pins have whatever functionality is labeled beside their female header companions.

[![Pin Rails on the Front of the Artemis RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-GPIO.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-GPIO.jpg)

### Serial and JTAG Programming

The RedBoard Artemis has two methods for programming. The most common is the USB C connector that operates as a USB to serial bridge. By simply pressing \'Upload\' in the Arduino IDE or \'make bootload\' from the SDK the firmware on Artemis is updated.

[![RedBoard Artemis USB C and JTAG ports](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-USBC-SerialProgramming-JTAG-Ports.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-USBC-SerialProgramming-JTAG-Ports.jpg)

*USB-C and JTAG footprints*

We use the CH340C on the RedBoard Artemis. The driver should automatically install on most operating systems. However, there is a wide range of operating systems out there. You may need to install drivers the first time you connect the chip to your computer\'s USB port or when there are operating system updates. For more information, check out our [How to Install CH340 Drivers Tutorial](https://www.sparkfun.com/ch340).

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

The second method is JTAG programming. An unpopulated JTAG footprint is available for more advanced users who need breakpoint level debugging. We recommend checking out our [JTAG section](https://www.sparkfun.com/categories/tags/jtag) for the compatible male header and a compatible JTAG programmer and debugger.

### Mic and RTC

The Artemis exceeds at low power voice recognition. To enable this we\'ve included a PDM MEMS microphone on the board. Additionally, the Artemis module can operate an RTC given an external 32kHz crystal so we\'ve included that was well.

[![PDM Microphone and RTC on RedBoard Artemis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-Microphone-RTC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-Microphone-RTC.jpg)

### Qwiic and I2C

The I^2^C pins on the Artemis are labeled SDA and SCL. They are controlled in the Arduino IDE using `Wire.begin()`, `Wire.read()`, etc. The same SDA/SCL pins are connected to the Qwiic connector so you can use SparkFun\'s [Qwiic ecosystem](https://www.sparkfun.com/qwiic) (there\'s over 50 boards and more every week!).

[![Qwiic connector on RedBoard Artemis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-Qwiic-I2C-Connectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-Qwiic-I2C-Connectors.jpg)

[] **Note:** The standard Arduino Uno has SDA/SCL additionally connected to A4/A5. A4/A5 on the Artemis are not I^2^C related, they are only Analog. SDA/SCL are digital pins 14/15 respectively. A4/A5 can be used as digital pins 20/21 respectively.

### Serial0, AREF, and USB Pads

On the rear of the RedBoard are some advanced features. Normally, an AREF pin is located between the SDA and GND pins. The Artemis module has no equivalent pin so we\'ve converted that pin to GND. If you have a shield that utilizes the AREF pin or just want to free it, you can cut the AREF jumper and the labeled \'GND\' located between SDA and GND will be left disconnected.

On Artemis, TX0/RX0 are used for bootloading new code and Serial.println() statements to the computer\'s terminal window. The CH340C takes care of the serial to USB conversion. However, if you need access to these pins, they\'re available. TX0/RX0 can be used as GPIO as well as special functions, but for most applications these pins are left as Serial for bootloading.

For users who are embedding the RedBoard Artemis into an enclosure the USB pads are exposed so that an external USB connector can be located at the edge of the enclosure and wired back to the USB pads.

[![Rear of RedBoard Artemis showing various SMD pads and jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-AREF-TX0-RX0-USBConnectorPads.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-AREF-TX0-RX0-USBConnectorPads.jpg)

### Busmaster Pads

One amazing aspect of the Artemis is the large number of SPI and I^2^C buses available. We at SparkFun decided that it would be better to have more PWM and ADC pins routed to the female headers on the front of the board, rather than extra I^2^C and SPI pins. But we just couldn\'t resist! We\'ve made Wire1/SPI1 and Wire3/SPI3 available to users through the SMD pads on the bottom of the board. These pins can be used as GPIO if needed and pins 28/29 are PWM enabled as well.

[] **Advanced Trick:** Do you just need a 2nd I^2^C port? The pins 12/13 can be reconfigured from SPI to be Wire0.

[] **Note:** A \'bus master\' is a series of pins that can be either an SPI bus or an I^2^C bus. For example, pins 8/9 can be SCL1/SDA1 or pins 8/9/10 can be SCK1/MISO1/MOSI1.

[![Bus master pads on rear of RedBoard Artemis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-BusMasterPads.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-BusMasterPads.jpg)

### Current Measurement Jumper

The Artemis can run as low as 6μA/MHz meaning the module can run at 48MHz at less than half a milliamp. To enable measurements and to isolate the power hungry devices (such as the LM317 voltage regulator) we\'ve added a NC (normally closed) jumper. By cutting the jumper the VDD trace to the module is interrupted. Soldering in a male jumper or wires into the accompanying holes will give you the ability to insert a current meter and precisely monitor how much current your application is consuming.

[![Current Measurement Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-CurrentMeasurementJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-CurrentMeasurementJumper.jpg)

For the vast majority of projects a wall adapter or USB power can be used. But when properly isolated the Artemis can run on a coincell battery for weeks! So we\'ve designed in a 20mm SMD coin cell footprint so that users can experiment with powering the Artemis from a standard CR2032. You can pickup the compatible coincell holder [here](https://www.sparkfun.com/products/11892).

[![Coin Cell Location](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-CoinCellBatteryPads.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-CoinCellBatteryPads.jpg)

### Bypass Jumper

USB C is wonderful. It\'s reversible and can source up to 2 amps at 5 volts without any power delivery (PD) negotiation. We\'ve included a 2A resettable fuse (often called a *PTC*) on the Artemis as a safety feature in case your project decides to consume inordinate amounts of power (And possibly begins to spark and set fire. That was fun wasn\'t it? Get it? SparkFun?). In the event the RedBoard begins to pull more than 2 amps from the USB source, the resettable fuse will automatically trigger and disconnect the board from the computer or power supply. This should protect your power source and the traces on your RedBoard.

However, there are plenty of legitimate projects that need more than 2A. We\'ve designed the power traces to withstand up to 2A with a 10C rise in temperature. If your power supply can provide adequate power, and you know what you are doing, you can close the BYP jumper circumventing the resettable fuse.

[![The bypass jumper on RedBoard Artemis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-BypassJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/5/15444-SparkFun-RedBoard-Artemis-BypassJumper.jpg)

## Software Setup

The RedBoard Artemis runs both Arduino and the more advanced Ambiq HAL/SDK. Checkout these tutorials to get you up and blinking in 5 minutes!

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