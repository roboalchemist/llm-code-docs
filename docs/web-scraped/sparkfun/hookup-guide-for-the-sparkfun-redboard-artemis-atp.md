# Source: https://learn.sparkfun.com/tutorials/hookup-guide-for-the-sparkfun-redboard-artemis-atp

## Introduction

We affectionately refer to the [RedBoard Artemis ATP](https://www.sparkfun.com/products/15442) as the \"All The Pins!\" board, since it breaks out every single one of the Artemis Module\'s 48 GPIO pins into a familiar Mega-like form factor. On top of the RedBoard\'s improved power conditioning and USB to serial, we\'ve added a slew of features to help you take full advantage of the Artemis module\'s unique features. Let\'s have a look!!

[![SparkFun RedBoard Artemis ATP](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/1/7/15442-SparkFun_RedBoard_Artemis_ATP-05.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis-atp.html)

### [SparkFun RedBoard Artemis ATP](https://www.sparkfun.com/sparkfun-redboard-artemis-atp.html) 

[ DEV-15442 ]

The RedBoard Artemis ATP has 48 GPIO and this board breaks out all of them in an Arduino Mega format.

[ [\$30.95] ]

### Required Materials

You\'ll need the RedBoard Artemis ATP and a USB C cable. Any USB C cable should work, including the one that probably came with your phone charger.

[![SparkFun RedBoard Artemis ATP](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/7/15442-SparkFun_RedBoard_Artemis_ATP-05.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis-atp.html)

### [SparkFun RedBoard Artemis ATP](https://www.sparkfun.com/sparkfun-redboard-artemis-atp.html) 

[ DEV-15442 ]

The RedBoard Artemis ATP has 48 GPIO and this board breaks out all of them in an Arduino Mega format.

[ [\$30.95] ]

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

If you\'ve ever used an Arduino Mega before you should be pretty familiar with the various female headers and the barrel jack power. In this tutorial we\'ll be covering the unique aspects of the RedBoard Artemis ATP.

[![Front view of the SparkFun RedBoard Artemis ATP](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun_RedBoard_Artemis_HighResFront.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun_RedBoard_Artemis_HighResFront.jpg)

⚡ **Warning:** All pins are **3.3V**. DO NOT expose the pins to 5V.\
\
The ADC on the Artemis is **0-2V**. Exposing an ADC pin to 3.3V will not harm the device but the ADC will saturate returning 16,383 (14-bit) for voltages greater than 2V.

### GPIO

Remember our \"All the Pins!\" nickname? Well, we meant it. On the RedBoard Artemis ATP, not only have we broken out all the major pins with female headers, we\'ve added a secondary rail of plated through-holes alongside them to give you the choice of either plug and play or soldering directly to the board.

[![Pin rails on the front of the RedBoard Artemis ATP](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-GPIOPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-GPIOPins.jpg)

On the side of the board, instead of doubling the pin availability, we\'ve added a rail of ground pins for ease of use.

[![Ground pins highlighted next to pins 3, 36, 38, 37, and 44](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-GPIOPinsSide.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-GPIOPinsSide.jpg)

*Click on the image for a closer look*

### Serial and JTAG Programming

The RedBoard Artemis ATP has two methods for programming. The most common is the USB C connector that operates as a USB to serial bridge. By simply pressing \'Upload\' in the Arduino IDE or \'make bootload\' from the SDK the firmware on Artemis is updated.

We use the CH340C on the RedBoard Artemis ATP. The driver should automatically install on most operating systems. However, there is a wide range of operating systems out there. You may need to install drivers the first time you connect the chip to your computer\'s USB port or when there are operating system updates. For more information, check out our [How to Install CH340 Drivers Tutorial](https://www.sparkfun.com/ch340).

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

The second method is JTAG programming. We\'ve populated the JTAG footprint for more advanced users who need breakpoint level debugging. We recommend checking out our [JTAG section](https://www.sparkfun.com/categories/tags/jtag) for the compatible JTAG programmer and debugger.

[![RedBoard Artemis ATP USB C and JTAG ports](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-USBC-Serial-Connector_JTAG_Ports.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-USBC-Serial-Connector_JTAG_Ports.jpg)

*USB-C and JTAG footprints*

### Mic and RTC

The Artemis excels at low power voice recognition. To enable this we\'ve included a PDM MEMS microphone on the board. Additionally, the Artemis module can operate an RTC given an external 32kHz crystal so we\'ve included that was well.

[![PDM Microphone and RTC on RedBoard Artemis ATP](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-Microphone_and_RTC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-Microphone_and_RTC.jpg)

Pins 36 and 37 are connected to the onboard PDM MEMS microphone and are broken out on the upper right side of the ATP board. You can hookup a second PDM microphone to pins 36/37 or you can load PDM firmware onto the Artemis module and watch PDM traffic from the microphone(s). Notice the ground pins next to pins 36 and 37!

[![Pins 36 and 37 are on the upper right hand side of the front of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-Microphone_Pins_Broken_Out.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-Microphone_Pins_Broken_Out.jpg)

*Click on the image for a closer look*

If you have no plans to use the on-board microphones, pins 36 and 37 can be used as GPIO by cutting the jumpers on the back of the board.

[![Cut these two jumpers on the back of the board to use Pins 36 and 37 as GPIO](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-GPIO36-GPIO37_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-GPIO36-GPIO37_Jumpers.jpg)

### Qwiic and I2C

The I^2^C pins on the Artemis are labeled SDA and SCL. They are controlled in the Arduino IDE using `Wire.begin()`, `Wire.read()`, etc. The same SDA/SCL pins are connected to the Qwiic connector so you can use SparkFun\'s [Qwiic ecosystem](https://www.sparkfun.com/qwiic) (there\'s over 50 boards and more every week!).

[![Qwiic connector on RedBoard Artemis ATP and I2C Ports](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-Qwiic_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-Qwiic_I2C.jpg)

[] **Note:** The standard Arduino has SDA/SCL additionally connected to A4/A5. A4/A5 on the Artemis are not I^2^C related, they are only Analog. SDA/SCL are digital pins 14/15 respectively. A4/A5 can be used as digital pins 20/21 respectively.

### Serial0, AREF, and USB Pads

On the rear of the RedBoard ATP are some advanced features. Normally, an AREF pin is located between to the SDA and GND pins. The Artemis module has no equivalent pin so we\'ve converted that pin to GND. If you have a shield that utilizes the AREF pin or just want to free it, you can cut the AREF jumper and the labeled \'GND\' located between SDA and GND will be left disconnected.

On Artemis, TX0/RX0 are used for bootloading new code and Serial.println() statements to the computer\'s terminal window. The CH340C takes care of the serial to USB conversion. However, if you need access to these pins, they are available. TX0/RX0 can be used as GPIO as well as special functions, but for most applications these pins are left as Serial for bootloading.

For users who are embedding the RedBoard Artemis ATP into an enclosure, the USB pads are exposed so that an external USB connector can be located at the edge of the enclosure and wired back to the USB pads.

[![Back of RedBoard Artemis ATP showing various SMD pads and jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-AREF_Jumper-RX0-TX0-USBPads.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-AREF_Jumper-RX0-TX0-USBPads.jpg)

### Current Measurement Jumper

The Artemis can run as low as 6μA/MHz, meaning the module can run at 48MHz at less than half a milliamp. To enable measurements and to isolate the power hungry devices (such as the LM317 voltage regulator) we\'ve added a NC (normally closed) jumper. By cutting the jumper the VDD trace to the module is interrupted. Soldering in a male jumper or wires into the accompanying holes will give you the ability to insert a current meter and precisely monitor how much current your application is consuming.

For the vast majority of projects a wall adapter or USB power can be used. But when properly isolated the Artemis can run on a coincell battery for weeks! So we\'ve designed in a 20mm SMD coin cell footprint so that users can experiment with powering the Artemis from a standard CR2032. You can pickup the compatible coincell holder [here](https://www.sparkfun.com/products/11892).Be careful when soldering, the coincell silk screen pads are a bit larger than usual.

[![Current Measurement Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-Measurement_Jumper_Ports.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-Measurement_Jumper_Ports.jpg)

*Click the image for a closer look*

[![Coin Cell Battery Pads](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-CoinCellBatteryPads.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-CoinCellBatteryPads.jpg)

*Click the image for a closer look*

### Bypass Jumper

USB C is wonderful. It\'s reversible and can source up to 2 amps at 5 volts without any power delivery (PD) negotiation. We\'ve included a 2A resettable fuse (often called a *PTC*) on the Artemis as a safety feature in case your project decides to consume inordinate amounts of power (And possibly begins to spark and set fire. That was fun wasn\'t it? Get it? SparkFun?). In the event the RedBoard begins to pull more than 2 amps from the USB source, the resettable fuse will automatically trigger and disconnect the board from the computer or power supply. This should protect your power source and the traces on your RedBoard.

However, there are plenty of legitimate projects that need more than 2A. We\'ve designed the power traces to withstand up to 2A with a 10C rise in temperature. If your power supply can provide adequate power, and you know what you are doing, you can close the BYP jumper, thus circumventing the resettable fuse.

[![The bypass jumper on RedBoard Artemis ATP](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-BypassJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/15442-SparkFun-Artemis-ATP-BypassJumper.jpg)

### I/O Masters

You can have up to 6 I^2^C or SPI masters with the RedBoard Artemis ATP, and these pins are distributed across the board. Be sure to check out the good examples built into the Artemis Arduino core showing how to easily enable additional ports.

[![Example I2C sketches built into Artemis core](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/Artemis-I2C-Examples.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/7/Artemis-I2C-Examples.jpg)

In addition we\'ve listed each of the masters below with their associated pins. Check out the [Apollo3 PinMap](https://cdn.sparkfun.com/assets/8/2/3/3/c/Apollo3_Pad_Mapping.pdf) for more information.

  Master   SCK/SCL   MISO/SDA   MOSI
  -------- --------- ---------- ------
  **M0**   5         6          7
  **M1**   8         9          10
  **M2**   27        25         28
  **M3**   42        43         38
  **M4**   39        40         44
  **M5**   48        49         47

## Software Setup

The RedBoard Artemis ATP runs both Arduino and the more advanced [Ambiq](https://ambiq.com/) HAL/SDK. Checkout these tutorials to get you up and blinking in 5 minutes!

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