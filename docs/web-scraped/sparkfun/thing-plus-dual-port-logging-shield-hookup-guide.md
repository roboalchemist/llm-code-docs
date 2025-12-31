# Source: https://learn.sparkfun.com/tutorials/thing-plus-dual-port-logging-shield-hookup-guide

## Introduction

The [Thing Plus Dual-Port Logging Shield](https://www.sparkfun.com/products/19217) is a Thing Plus/Feather compatible board that lets you access your microSD card over ***both*** SPI and USB-C! It is designed to be mounted on or under one of our [Thing Plus boards](https://www.sparkfun.com/thing_plus). You can log data to and read data from your microSD card over SPI as usual, using your favorite Arduino SD library. But you can also connect it to your computer via USB-C and read and write files at ***up to 35 MBytes/second***! The write speed is card-dependent but, in our tests, we\'ve routinely seen write speeds around 20MB/s. No more removing the microSD to read your data!

[![SparkFun Thing Plus Dual-Port Logging Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/8/4/1/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-01a.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-dual-port-logging-shield.html)

### [SparkFun Thing Plus Dual-Port Logging Shield](https://www.sparkfun.com/sparkfun-thing-plus-dual-port-logging-shield.html) 

[ DEV-19217 ]

The SparkFun Dual-Port Logging Shield is a Thing Plus/Feather-compatible board which allows you to access your microSD card o...

[ [\$32.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc)

### Alternating Current (AC) vs. Direct Current (DC) 

Learn the differences between AC and DC, the history, different ways to generate AC and DC, and examples of applications.

## Hardware Overview

### ATtiny841

The Dual-Port Logging Shield has an ATtiny841 microcontroller on it to act as an arbiter:

- If you power up your Thing Plus, the ATtiny841 will automatically put the Dual-Port Logging Shield into SPI mode, so your Arduino code can access the microSD card as normal
- If you power the Shield from your computer by connecting it via USB-C, the ATtiny841 will put the Shield into SDIO \"thumb drive\" mode. Your computer can then read and write data ***really quickly***!
- If you have both your Thing Plus powered up - *and* have your computer connected - then you can switch between the two modes by giving the ATtiny841 some very simple commands over I^2^C!

You can configure the ATtiny to automatically default to SPI mode or SDIO \"thumb drive\" mode if both power sources are powered up simultaneously. It\'s your choice!

[![ATtiny is the chip towards the bottom of the board in the middle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-ATTiny2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-ATTiny2.jpg)

### USB2241

The USB224x is a fully integrated, single chip solution capable of ultra high performance operation. Average sustained transfer rates exceeding 35 MB/s are possible if the media and host can support those rates. The USB224 includes provisions to read/write secure media formats.

[![The USB2241 is the larger chip in the middle of the board.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-USB2241-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-USB2241-1.jpg)

### Programming Footprint

Advanced users can change the shield\'s USB Vendor ID (VID), Product ID (PID), Manufacturer Name etc. by adding an optional 24C04 (512x8) EEPROM and configuring it with Microchip\'s USBDM tool.

[![Programming footprint is in the middle of the back of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-ProgrammingFootprint1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-ProgrammingFootprint1.jpg)

### microSD Card Slot

The USB2241, which provides the USB interface, supports FAT32, exFAT and NTFS on cards up to and including **32GB**. Cards larger than 32GB are not supported.

[![microSD card opens up to the right side of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-microSD1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-microSD1.jpg)

### USB-C

While attached to the Thing Plus, you can log data to and read data from your microSD card over SPI as usual. But you can also connect the shield directly to your computer via the USB-C port and read/write files directly.

[![USB-C port is at the top of the board, facing up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-USBC1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-USBC1.jpg)

### LEDs

There are two LEDs on the front of the board; PWR and ACT. PWR should be self-explanatory - it is the LED that lights up when there is power to the shield. ACT stands for activity monitor - this shows data movement on the shield in SDIO \"thumb drive\" mode.

[![The two LEDS are at the opposite side of the board from the USBC port. ACT is on the left, PWR on the right](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-LEDs1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-LEDs1.jpg)

### Jumpers

#### I2C

These split pads are closed by default to enable the shield\'s I^2^C pull-up resistors. Please be aware that, with the pull-ups enabled, the shield\'s VCC will try to back-feed power to the Thing Plus through the pull-ups on both boards. Opening the jumpers will prevent this.

[![I2C Jumper on the back of the board on the right side, just under the SDA and SCL pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-I2CJumper1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-I2CJumper1.jpg)

The default (unshifted) I^2^C address is 0x51 but is programmable via the code.

#### LEDS

Should you wish to disable either of the LEDs on the front of the board, cut the trace on the appropriate jumper.

[![LED jumpers are at the top of the back of the board, next to the mounting](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-ActPwrJumper1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-ActPwrJumper1.jpg)

#### Chip Select

By default, the microSD SPI chip select signal is connected to pin A5 on the Thing Plus. If you are already using that pin for something else, you can open the A5 jumper and close A4 or A3 instead.

[![The chip select jumpers are on the back of the board, on the left side, under the SCK pin](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-ChipSelect1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-ChipSelect1.jpg)

#### Serial

The ATtiny841 has a Serial (UART) interface but we only make limited use of it in the standard shield firmware. If you want to, you can connect the ATtiny serial pins to the standard Thing Plus Serial pins by closing the RXD and TXD jumpers. You will then see some diagnostic messages at 9600 baud when the ATtiny powers up. These jumpers are really there for any advanced users who want to write their own firmware for the ATtiny!

[![The serial jumpers are the top most jumpers on the left side of the back of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-SerialJumper1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-SerialJumper1.jpg)

#### SH

By default, the USB-C shield is connected to the shield GND (0V). You can isolate the shield if you want to by opening the SH jumper.

[![The shield jumper is at the bottom of the back of the board on the left side of the pads for the USBC connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-SHJumper1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-SHJumper1.jpg)

### Board Outline

[![Board measures 2.3\" by 0.90 inches](https://cdn.sparkfun.com/assets/6/4/0/d/f/Dimensions.png)](https://cdn.sparkfun.com/assets/6/4/0/d/f/Dimensions.png)

## Hardware Hookup

In order to use your Dual Port Logger as a shield, you\'ll need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) some headers on. My ESP32 Thing Plus has female headers already soldered on, so for this tutorial, we\'ve used male headers on the Dual Port Logging Shield like so:

[![Here the Thing Plus has female headers soldered on and the dual port logger shield has male headers soldered on.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-HG-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-HG-03.jpg)

Once you\'ve got all your headers properly soldered on, line up the pins and connect your Thing Plus and Shield like so:

[![Line up the male and female headers and gently press the shield and thing plus together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-HG-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-HG-01.jpg)

Tadaaaa! All ready for programming!

[![Two boards are connected and ready to rock!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-HG-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/19217-SparkFun_Thing_Plus_Dual-Port_Logging_Shield-HG-02.jpg)

## Software Installation

**Note:** The Dual Port Logging Shield Arduino examples assume you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The SparkFun Dual-Port Logging Shield Arduino Library can be downloaded with the Arduino library manager by searching \'**SparkFun Dual-Port Logging Shield Arduino Library**\' or you can grab the zip from here or from the [GitHub repository](https://github.com/sparkfun/SparkFun_Dual-Port_Logging_Shield_Arduino_Library) to manually install:

[SparkFun Dual-Port Logging Shield Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Dual-Port_Logging_Shield_Arduino_Library/archive/refs/heads/main.zip)

## Example 1: Read I2C Address/Firmware Version

Now that we\'ve got our hardware sorted out, let\'s have a look at some examples.

In this first example, we\'re just going to report out on our I^2^C address and Firmware Version.

To start, plug your Thing Plus with its Dual Port Logging Shield into your computer, open a new Arduino sketch, and click \"**File** \> **Examples** \> **SparkFun Dual-Port Logging Shield Arduino Library** \> **Example1_Read_I2CAddress_FirmwareVersion_DefaultMode**\".

[![Where to find example 1 in the file menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Find_Example_1_Final.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Find_Example_1_Final.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

***Note:*** If you are using an [Artemis Thing Plus](https://www.sparkfun.com/products/15574), you will need to change Wire to Wire1 in the example code!

Choose the correct Board and Port (as seen here):

[![For this example, we\'re using the Esp32 Thing Plus](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/ChooseBoardAndPort.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/ChooseBoardAndPort.png)

And then upload the code to your Thing Plus. When you open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with the correct baud, you should see something like the following:

[![Serial Monitor output lists I2C address, Firmware version, etc](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Example_1_Output_UpdatedAgain.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Example_1_Output_UpdatedAgain.png)

*Having a hard time seeing the details? Click the image for a closer look.*

## Example 2: Set I2C Address

Example 2 shows you how to change the I^2^C address of the shield. Let\'s bring it up in Arduino:

[![Where to find example 2 in the file menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Find_Example_2_Final.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Find_Example_2_Final.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

***Note:*** If you are using an [Artemis Thing Plus](https://www.sparkfun.com/products/15574), you will need to change Wire to Wire1 in the example code!

Make sure you select the correct board and port, and then smash that upload button. Once the code is compiled and uploaded, go ahead an open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics). You should see something like the following:

[![Sample output of Example 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Example_2_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Example_2_Output.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

## Example 3: Change Mode

There are different modes available for the Dual Port Logging Shield. Example three shows you how to change between SDIO (thumb drive) and SPI modes!

To start, let\'s pull up example 3 in Arduino.

[![Where to find example 3 in the menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Find_Example_3_Final.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Find_Example_3_Final.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

***Note:*** If you are using an [Artemis Thing Plus](https://www.sparkfun.com/products/15574), you will need to change Wire to Wire1 in the example code. You\'ll also need to change the Chip Select - for the Artemis Thing Plus, A5 is D24

Make sure you\'ve chosen the correct board and port (as seen in example 1) and then upload the code to your Thing Plus. When you open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with the correct baud, you should see something like the following:

[![Output shows the default mode and then puts the shield into SDIO mode for a USB drive](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Example_3_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Example_3_Output.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

Make sure your Dual Port Logger is ALSO plugged in, and when the example runs, you\'ll see an additional drive pop up like so:

[![Extra drive pops up as D: for me](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Example_3_Output_More.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Example_3_Output_More.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

## Example 4: Sleep SDIO

In this example, we\'re going to look at the deep sleep functionality, and like Example 3, this example will also bring up the Dual Port Logging Shield as a drive. Go ahead and bring up example 4 in Arduino:

[![Where to find Example 4 in the menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Find_Example_4_SDIO_Final.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Find_Example_4_SDIO_Final.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

***Note:*** If you are using an [Artemis Thing Plus](https://www.sparkfun.com/products/15574), you will need to change Wire to Wire1 in the example code!

Make sure you\'ve chosen the correct board and port (as seen in example 1) and then upload the code to your Thing Plus. When you open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with the correct baud, you should see something like the following:

[![Output shows putting the shield into deep sleep, then SDIO mode, then waits 30 seconds](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Example_4_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Example_4_Output.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

Make sure your Dual Port Logger is ALSO plugged in, and when the example runs, you\'ll see an additional drive pop up like so:

[![Check out that extra USB drive!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Example_4_Output_More.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Example_4_Output_More.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

## Example 5: Sleep SPI

Example 5 shows the Sleep cycle for SPI mode. Bring up the example in Arduino:

[![Where to find Example 5 in the menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Find_Example_5_Final.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Find_Example_5_Final.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

***Note:*** If you are using an [Artemis Thing Plus](https://www.sparkfun.com/products/15574), you will need to change Wire to Wire1 in the example code!

Make sure you\'ve chosen the correct board and port (as seen in example 1) and then upload the code to your Thing Plus. When you open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with the correct baud, you should see something like the following:

[![Example 5 output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Example_5_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Example_5_Output.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

## Example 6: Set Default Mode

If you run into a snag, setting things back to default is always a good way to go. This example will do just that!

Bring it on up in Arduino:

[![Where to find Example 6 in the menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Find_Example_6_Final.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Find_Example_6_Final.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

***Note:*** If you are using an [Artemis Thing Plus](https://www.sparkfun.com/products/15574), you will need to change Wire to Wire1 in the example code!

Make sure you\'ve chosen the correct board and port (as seen in example 1) and then upload the code to your Thing Plus. When you open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with the correct baud, you should see something like the following:

[![Example 6 output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/5/5/Example_6_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/5/5/Example_6_Output.jpg)

*Having a hard time seeing the details? Click the image for a closer look.*

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.