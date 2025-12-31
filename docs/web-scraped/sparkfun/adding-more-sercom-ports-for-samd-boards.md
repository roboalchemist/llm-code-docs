# Source: https://learn.sparkfun.com/tutorials/adding-more-sercom-ports-for-samd-boards

## Introduction

SERCOM (Serial Communication) is a multiplexed serial configuration used on the SAMD21, SAMD51 and other boards. It allows you to select various serial functions for most of your pins. For example, the ATmega328 which has UART (RX/TX) on one pair of pins, I^2^C (SDA/SCL) on another set, and SPI (MOSI, MISO, SCK) on another set. The SAMD21 has 5 different internal ports which you can configure to use any combination of UART, I^2^C, and SPI. The SAMD21 and SAMD51 boards are becoming increasingly popular in part because of this feature. But how do you do it?

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

#### ARM-Based Microcontroller

For this tutorial we are going to use the RedBoard Turbo, but you should be able to follow along just fine with any of the SAMD21 boards below (or any not listed below).

[![SparkFun SAMD21 Mini Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/9/2/13664-01.jpg)](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html)

### [SparkFun SAMD21 Mini Breakout](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html) 

[ DEV-13664 ]

If you're ready to step your Arduino game up from older 8-bit/16MHz microcontrollers, the SparkFun SAMD21 Mini Breakout is ...

[ [\$24.95] ]

[![SparkFun Pro RF - LoRa, 915MHz (SAMD21)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/6/5/15836-SparkFun_Pro_RF_-_LoRa__915MHz__SAMD21_-01.jpg)](https://www.sparkfun.com/sparkfun-pro-rf-lora-915mhz-samd21.html)

### [SparkFun Pro RF - LoRa, 915MHz (SAMD21)](https://www.sparkfun.com/sparkfun-pro-rf-lora-915mhz-samd21.html) 

[ WRL-15836 ]

The SparkFun Pro RF is a LoRa®-enabled wireless board that marries a SAMD21 and a long-range RFM95W to make a compact and ea...

[ [\$36.95] ]

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

[![SparkFun SAMD21 Dev Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/1/5/13672-01.jpg)](https://www.sparkfun.com/sparkfun-samd21-dev-breakout.html)

### [SparkFun SAMD21 Dev Breakout](https://www.sparkfun.com/sparkfun-samd21-dev-breakout.html) 

[ DEV-13672 ]

If you're ready to step your Arduino game up from older 8-bit/16MHz microcontrollers, the SparkFun SAMD21 Dev Breakout is a...

[ [\$29.95] ]

#### Serial Device and Prototyping Hardware

You\'ll also need a serial device. We will also be using a [16x2 Serial LCD Screen](https://www.sparkfun.com/products/14072) for our examples since it will accept commands over UART, SPI or I^2^C. You will need a way to connect your board to the screen as well, but those are the only components needed to follow along.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

[![Breadboard - Mini Modular (Red)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/2/7/12044-01.jpg)](https://www.sparkfun.com/breadboard-mini-modular-red.html)

### [Breadboard - Mini Modular (Red)](https://www.sparkfun.com/breadboard-mini-modular-red.html) 

[ PRT-12044 ]

This red Mini Breadboard is a great way to prototype your small projects! With 170 tie points there\'s just enough room to bui...

[ [\$4.50] ]

[![SparkFun 16x2 SerLCD - Black on RGB 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/2/5/14072-SparkFun_16x2_SerLCD_-_Black_on_RGB_3.3V-05.jpg)](https://www.sparkfun.com/products/14072)

### [SparkFun 16x2 SerLCD - Black on RGB 3.3V](https://www.sparkfun.com/products/14072) 

[ LCD-14072 ]

The SparkFun SerLCD is an AVR-based, serial enabled LCD that provides a simple and cost effective solution for adding a 16x2 ...

**Retired**

### Tools

Depending on your setup, you may need a soldering iron, solder, [general soldering accessories](https://www.sparkfun.com/categories/49) for boards without headers.

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide)

### SAMD21 Mini/Dev Breakout Hookup Guide 

An introduction to the Atmel ATSAMD21G18 microprocessor and our Mini and Pro R3 breakout boards. Level up your Arduino-skills with the powerful ARM Cortex M0+ processor.

[](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide)

### AVR-Based Serial Enabled LCDs Hookup Guide 

The AVR-based Qwiic Serial Enabled LCDs are a simple and cost effective solution to include in your project. These screens are based on the HD44780 controller, and include ATmega328P with an Arduino compatible bootloader. They accept control commands via Serial, SPI and I2C (via PTH headers or Qwiic connector). In this tutorial, we will show examples of a simple setup and go through each communication option.

[](https://learn.sparkfun.com/tutorials/redboard-turbo-hookup-guide)

### RedBoard Turbo Hookup Guide 

An introduction to the RedBoard Turbo. Level up your Arduino-skills with the powerful SAMD21 ARM Cortex M0+ processor!

### A Look at the RedBoard Turbo

Whenever a new board is added to the Arduino IDE it comes with a couple of variants files (**variant.h** and **variant.cpp**). These files define which pins are being used for what. They define where D0 maps to, where the `BUILT_IN_LED` goes, and which pins are assigned to things like UART, I^2^C, etc. Pretty much any of the SAMD21 or SAMD51 boards you come across should already have at least 1 UART, I^2^C, and SPI port defined in their variants file. It is usually easiest to just use those. But once in a while you will want to add another port. For example, you have an accelerometer that you want to use to measure vibrations on 2 different platforms. But the accelerometer only has one available I^2^C address. While you could use an I^2^C mux, you can also just add a second I^2^C port to your board.

Let\'s take a look at the RedBoard Turbo. As you can see there is an I^2^C port broken out at the top right. At the bottom, you\'ll also see the UART broken out and the pins labeled TX and RX. Finally, you\'ll see what is often referred to as the legacy ISP header. Originally, this SPI port was tied to one on the side of the board (the ATMega boards only had 1 SPI port) and was used to program the bootloader onto the board. Because a lot of shields use this as the primary SPI port, this is broken out as well. However, they are located a different SPI port than the one on the side for the RedBoard Turbo.

[![RedBoard Turbo with all Serial pins highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/8/RedBoardTurboSercom_SAMD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/8/RedBoardTurboSercom_SAMD.jpg)

**Heads up!** The RedBoard Turbo with the SAMD21 uses a different architecture. Compared to the Arduino Uno/RedBoard with an ATmega328P, there are no SPI pins on D10-D13 for the RedBoard Turbo.

Now let\'s take a closer look at the SAMD21 and start defining some terms.

- **[Serial](https://en.wikipedia.org/wiki/Serial_communication)** \-- Serial communication means one item or bit is sent at a time. This is in contrast to Parallel where multiple items are sent at once on different lines. UART, SPI, and I^2^C are all types of serial communication.
- **[UART (Universal Asynchronous Receiver/Transmitter)](https://learn.sparkfun.com/tutorials/serial-communication)** \-- This is what is commonly referred to as serial even though it is only one type of serial. With a TX (transmit) and RX (receive) line this communication protocol does not have a clock line. Also remember that what one device is transmiting the other device is receiving so you will want to connect your TX to RX and RX to TX.
  - **RX** \-- Receive line of a UART communication.
  - **TX** \-- Transmit line of a UART communication.
- **[SPI (Serial Peripheral Interface)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)** \-- This serial bus has both a line for the master to send data out and the slave to receive (MOSI), one for the slave to send and the master to receive (MISO), and a clock (SCK). The CS line is used to select which board is being talked to. In other words, a bus will have *3+n* wires. When a slave\'s CS line is selected, it knows the master is trying to talk to it. Because this is just a select line, it may or may not be included in a hardware serial interface.
  - **MOSI** \-- The master out, slave in line of an SPI bus.
  - **MISO** \-- The master in, slave out line of an SPI bus.
  - **SCK** \-- The clock line of an SPI bus.
  - **CS** \-- The cable select line of an SPI bus. Also, called slave select (SS).
- **[I^2^C (or I2C, Inter-Integrated Circuit)](https://learn.sparkfun.com/tutorials/i2c)** \-- This is a 2 wire serial interface that uses a clock and data line to pass information. Each device on the bus has a different address which the master will specifiy during communication. I^2^C buses require [pull-up resistors](https://learn.sparkfun.com/tutorials/pull-up-resistors) on both lines. Most SparkFun I^2^C boards have the pull-up resistors built in as well as a solder jumper to disable them.
  - **SDA** \-- This is the data line of an I^2^C bus.
  - **SCL** \-- This is the clock line of an I^2^C bus.
- **[SERCOM (Serial Communications)](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/samd21-overview#sercom)** \-- This is a the name of a serial communications port on the SAMD21 boards. Because of the SAMD21\'s pin multiplexing, each pin on the chip has multiple function. Therefore, each SERCOM port can use various pins.
- **Port**
  - **SERCOM Port** \-- The SAMD21 has 6 Serial Communication modules what can be configured in various ways. A port or module refers to one of them. This gives us 6 different communications options. Most of the SAMD21 boards use 4-5 of these to bring you 1 SPI, UART, and I^2^C bus and often use 1 or 2 more for a second SPI, and/or connecting to another chip on the board such as onboard flash or a WiFi module.
  - **Pad** \-- Each SERCOM Port will have 4 pads (0-4). In order to determine how to use a SERCOM port, we will need to figure out which pins are on which pads of our port. This is written in a variety of ways, for example pad 0 on SERCOM 1 may be written as SERCOM1/Pad\[0\], SERCOM1.0, or even 1:0.
  - **SAMD21 Port** \-- While Arduino gives names to all usable pins (often based on how they are configured) the chip manufacture does not assign pin numbers in such a way. Instead each pin has a port name. In the case of the SAMD21, the port names will have a letter (either A or B) and a number and look like this: PortA10, PortB08. Often for the sake of room, the Port will be abbreviated to the letter \'P\' and the names will look like this: PA10, PB08, etc.
- **Macro** \-- This is a predefined value in your code. Usually designated by the `#define` command. When looking at board definitions, you will see a lot of macros that have definitions defined elsewhere. The definitions are not as important and understanding what the macro is filling in for. For example, the macro `PIN_WIRE_SDA` is being used to define which pin you are using for SDA on a Wire (I^2^C) interface.
- **Multiplex (or mux for short)** \-- This is the practice of assigning many conflicting attributes to 1 item and being able to select which one you want. In this case, each pin on the SAMD21 chip is assigned many functions from analog inputs, to digital inputs, to timers, to various SERCOM ports. As we set up a SERCOM port we will need to spend some time selecting the correct feature in our mux.
- **Qwiic** \-- Qwiic is SparkFun\'s I^2^C interface. Get it, Qw**IIC**! This port connects to a board I^2^C port as well as providing power (3.3V). You will see it on quite a few boards including the Redboard Turbo. This is hard wired into the board\'s SDA and SCL pins so you can\'t change it.

## Datasheets - SAMD21

### Graphical Datasheet

Part of the trick of setting up SERCOM Ports is determining which pins go together. You can\'t just assign them Willy Nilly. The [SparkFun graphical datasheets](https://github.com/sparkfun/Graphical_Datasheets) do a pretty good job of summarizing them. We are going to start by looking at the Redboard Turbo and checking its graphical datasheet as well as the SAMD21 datasheet.

![RedboardTurbo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/1/Graphical_Datasheet_Simple.PNG)

The SparkFun graphical datasheets are great at giving you a quick one page overview of the features of your board. Above you see a simplified version of the Graphical Datasheet for the Redboard Turbo. As you can see the Turbo has 1x Serial port, 1x I^2^C port (which is also connected to the Qwiic connector) and 1x SPI ports (the legacy ISCP header).

### SAMD21 Datasheet

Looking at the [SAMD21 datasheet (page 21)](https://cdn.sparkfun.com/datasheets/Dev/Arduino/Boards/Atmel-42181-SAM-D21_Datasheet.pdf) under *I/O Multiplexing and Considerations*, we can start to see all the options each pin can have. We can select any of the columns for each pin. Specifically, we are looking at columns C and D. Also, it is worth noting that the chip on the Redboard Turbo is the SAMD21G18. As you can see there are other SAMD21 chip variants that have more or less pins. The \'**G**\' version is the one we want. As you can see, many of the pins have a 1 or 2 SERCOM ports available.

[![snapshot of SAMD Datasheet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/8/MuxTable.PNG)](https://cdn.sparkfun.com/datasheets/Dev/Arduino/Boards/Atmel-42181-SAM-D21_Datasheet.pdf)

*Click image for the full datasheet.*

### But What Pin Corresponds Where?

While you can check the schematic/board file to see what pin on the chip goes where, the best option is probably the **variant.cpp** file for your board. Let\'s look at this [file defined for the RedBoard Turbo](https://github.com/sparkfun/Arduino_Boards/blob/master/sparkfun/samd/variants/SparkFun_RedBoard_Turbo/variant.cpp). The file starts with a pretty large comment. While this is a good reference, keep in mind that people may choose not to update the comment for their board. Under the comment, you should see the Pin Descriptions. On the RedBoard Turbo, the pin definitions are broken out into sections to make it easier to read. The first section is D0-D13 staring with D0 and D1 which are the UART pins. You\'ll notice that the first arguments list the port and the pin on that port. The comment at the end also tells you what SERCOM port is being used. If we scroll through and find the pins that are using SERCOM pins, we\'ll find the following.

    language:c
    // 0..13 - Digital pins
    // ----------------------
    // 0/1 - SERCOM/UART (Serial1)
    , // RX: SERCOM0/PAD[3]
    , // TX: SERCOM0/PAD[2]

    // 20..21 I2C pins (SDA/SCL and also EDBG:SDA/SCL)
    // ----------------------
    , // SDA: SERCOM3/PAD[0]
    , // SCL: SERCOM3/PAD[1]

    // 22..24 - SPI pins (ICSP:MISO,SCK,MOSI)
    // ----------------------
    , // MISO: SERCOM4/PAD[0]
    , // MOSI: SERCOM4/PAD[2]
    , // SCK: SERCOM4/PAD[3]

    // 30..41 - Extra Pins
    // ----------------------
    // 30/31 - Extra UART
    , // 30/TX: SERCOM5/PAD[2]
    , // 31/RX: SERCOM5/PAD[3]

    // 32/33 I2C (SDA/SCL and also EDBG:SDA/SCL)
    , // SDA: SERCOM3/PAD[0]
    , // SCL: SERCOM3/PAD[1]

    // 34..37 - EDBG/SPI
    , // D12/MISO: SERCOM1/PAD[3]
    , // D11/MOSI: SERCOM1/PAD[0]
    , // D10/SS: SERCOM1/PAD[2]
    , // D13/SCK: SERCOM1/PAD[1]

Based on the code it looks like we are using SERCOM 0, 1, 3, 4, and 5. Any extra ports we use are going to have to use either SERCOM ports that are not already used or reuse one that is. Also, keep in mind that often unused ports are not removed. For example, this file lists D30 and D31 as an extra serial UART port. But, the board doesn\'t breakout D30 and D31 (but the SAMD21 development board did) so SERCOM 5 is actually free as well.

## Steps to Add a SERCOM Port

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We basically have 4x steps we are going to follow for each type of port we are going to add. The steps are the same for all types, but they are implemented a bit differently. Because the charts and datasheets are used for each type, they are listed at the end of the document. Make sure to have an extra window open when referencing the pins.

      1.) Figure out which pins to use.\
      2.) Add your code.\
      3.) Update the pin definitions based on the pin mux.\
      4.) Putting it all together.\

## Adding a UART

### 1.) Figure Out Which Pins to Use.

Let\'s start by checking out the [SERCOM.h](https://github.com/arduino/ArduinoCore-samd/blob/master/cores/arduino/SERCOM.h#L73) file in Arduino\'s SAMD21 core files. Specifically, we are looking at lines 73-86. You should see the code listed below. But what does it mean? There are 2 parts, the first part defines which pads you can use for an RX pad. It looks like you can use pads `0`, `1`, `2`, and `3` which is all of them. Next, it defines which pads you can use for TX. It looks like you can only use pads `0` and `2`. So, we\'ll need to keep that in mind when we select our pins.

    language:c
    typedef enum
     SercomRXPad;

    typedef enum
     SercomUartTXPad;

Since none of the boards I\'ve come across use SERCOM 2 for anything, we\'re going to use it for our examples. Let\'s start with TX since those pins are limited compared to the RX. We\'ll need to find which pins are on 2:0 or 2:2. [Looking at our charts](https://learn.sparkfun.com/tutorials/adding-more-sercom-ports-for-samd-boards#helpful-charts), you can see those pins are labeled as MISO, D4, D2, and D1/TX. Since MISO and D1/TX are already being used, that means we can use D2 or D4. Let\'s use D2 and see if we can put our new serial port right next to the original one. That means that RX should be on D3. It looks like D3 is on 2:1 so that will work.

### 2.) Add Your Code.

Next, lets figure out what code we need. Let\'s take a look at the [**variant.cpp** file](https://github.com/sparkfun/Arduino_Boards/blob/master/sparkfun/samd/variants/SparkFun_RedBoard_Turbo/variant.cpp#L213) again. Near the bottom, you\'ll see the following lines. This is what we are trying to duplicate in our code. The **variant.h** file defines all those macros, but their names give us a good idea of what should go there.

    language:c
    Uart Serial1( &sercom0, PIN_SERIAL1_RX, PIN_SERIAL1_TX, PAD_SERIAL1_RX, PAD_SERIAL1_TX ) ;
    Uart Serial( &sercom5, PIN_SERIAL_RX, PIN_SERIAL_TX, PAD_SERIAL_RX, PAD_SERIAL_TX ) ;
    void SERCOM0_Handler()
    

    void SERCOM5_Handler()
    

Let\'s start with the definition. Let\'s pick a name. \"`mySerial`\" sounds good. We also know we are going to use SERCOM 2, that RX will be on D3, TX on D2, and that D3 uses pad 1, and D2 uses pad 2. So we\'ll add the following to our code.

    language:c
    Uart mySerial(&sercom2, 3, 2, SERCOM_RX_PAD_1, UART_TX_PAD_2);

    void SERCOM2_Handler()
    

### 3.) Update the Pin Definitions Based on the Pin Mux.

Next, we need to set up the mux. Right now, D2 and D3 are defined as general I/O pins. We want them to act as SERCOM pins. The first thing we need to do is to add the pin peripheral library. Then we use the `pinPeripheral` commands to set up the pin definition.

    language:c
    #include "wiring_private.h" // pinPeripheral() function

    pinPeripheral(2, PIO_SERCOM); 
    pinPeripheral(3, PIO_SERCOM_ALT);

You\'ll notice that one uses the argument `PIO_SERCOM` and the other `PIO_SERCOM_ALT`. If you look on the datasheet, you\'ll notice that pins can have a SERCOM port listed under SERCOM or SERCOM-ALT. For D2, we are using the SERCOM port in the SERCOM column. For D3, we are using the SERCOM port in the SERCOM-ALT column.

### 4.) Putting It All Together.

Step 4 is running the code, testing, and troubleshooting. For this example, we are going to grab a serial LCD screen and connect it to our new serial UART port. Make sure that you have [soldered](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) headers to the LCD if you have not already.

[![Circuit Diagram SAMD21 SERCOM UART to SerLCD](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/8/SparkFun_Arduino_SAMD21_Configured_SERCOM_UART_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/8/SparkFun_Arduino_SAMD21_Configured_SERCOM_UART_Fritzing_bb.jpg)

The next step is to test out the UART port with the code listed below. The code is pretty bare bones and shows you where all your new code should go. Copy and paste the code in your Arduino IDE. Select your board, COM port, and hit upload.

    language:c
    /*********************************************************************
     * Sample code for setting up additional Serial ports on a SamD21 board
     * In this example the Redboard Turbo is used with the 16x2 SerLCD display
     * For more information on the SerLCD code check out the github repo
     * https://github.com/sparkfun/OpenLCD
     * https://www.sparkfun.com/products/14812
     * https://www.sparkfun.com/products/14072
     * By: Michelle Shorter - SparkFun Electronics
     * License: This code is public domain but you buy me a burger
     * if you use this and we meet someday (Beefware license).
     *********************************************************************/

    #include "wiring_private.h" // pinPeripheral() function
    //D2-TX, D3-RX
    Uart mySerial (&sercom2, 3, 2, SERCOM_RX_PAD_1, UART_TX_PAD_2);
    void SERCOM2_Handler()
    

    int i = 0;

    void setup() 

    void loop() 

## Adding an SPI

### 1.) Figure Out Which Pins to Use.

Let\'s start by checking out the [SERCOM.h](https://github.com/arduino/ArduinoCore-samd/blob/master/cores/arduino/SERCOM.h#L73) file in Arduino's SAMD21 core files. Specifically we are looking at lines 73-79 (yep, we looked at those when we added the UART) and lines 102-108. You should see the code listed below. But what does it mean? There are 2 parts, the first part defines which pads you can use for an RX (MISO) pad. It looks like you can use pads `0`, `1`, `2`, and `3` which is all of them. Next, it defines which pads you can use for TX (MOSI, and SCK) and in what configuration. So, we\'ll need to keep that in mind when we select our pins.

    language:c
    typedef enum
     SercomRXPad;

    //...

    typedef enum
     SercomSpiTXPad;

Since none of the boards I\'ve come across use SERCOM 2 for anything we\'re going to use it for our examples. Let\'s start with our outputs since those pins are limited compared to the MISO pins. It looks like SCK can only be on pad `1` or `3`, and MOSI can be on `0`, `2`, or `3` depending on the configuration. So, [looking at our table](https://learn.sparkfun.com/tutorials/adding-more-sercom-ports-for-samd-boards#helpful-charts), let\'s start by removing the pins that are not broken out to our board or already in use. That removes MISO, D38, D1/TX, and D0/RX, leaving use with D4, D3, D2, and D5. Any of those look like good options, but lets go with D3 for MISO, D5 for SCK, and D4 for MOSI. Again, we\'ll need to dig into our fancy charts to figure out what is where.

### 2.) Add Your Code.

Next lets figure out what code we need. Let\'s take a look at the [SPI.cpp](https://github.com/arduino/ArduinoCore-samd/blob/master/libraries/SPI/SPI.cpp#L261) file again. All the way near the bottom on line 261, you\'ll see the following line. This is what we are trying to duplicate in our code. The **variant.h** file defines all those macros, but their names give us a good idea of what should go there.

    language:c
     SPIClass SPI (&PERIPH_SPI, PIN_SPI_MISO, PIN_SPI_SCK, PIN_SPI_MOSI, PAD_SPI_TX, PAD_SPI_RX);

Let\'s start with the definition. Let\'s pick a name. \"`SPI2`\" sounds good. We also know we are going to use SERCOM 2, that we are going to use D3 for MISO, D5 for SCK, and D4 for MOSI. So, we\'ll add the following to our code.

    language:c
    SPIClass SPI2 (&sercom2, 3, 5, 4, SPI_PAD_0_SCK_3, SERCOM_RX_PAD_1);

### 3.) Update the Pin Definitions Based on the Pin Mux.

Next, we need to set up the mux. Right now, the pins are defined as general I/O pins. We want them to act as SERCOM pins. The first thing we need to do is to add the pin peripheral library. Then we use the `pinPeripheral` command to set up the pin defintion.

    language:c
    #include "wiring_private.h" // pinPeripheral() function

    SPI2.begin();
    pinPeripheral(3, PIO_SERCOM_ALT);
    pinPeripheral(4, PIO_SERCOM_ALT);
    pinPeripheral(5, PIO_SERCOM);

You\'ll notice that one uses the argument `PIO_SEROM` and the others `PIO_SERCOM_ALT`. If you look on the datasheet, you\'ll notice that pins can have a SERCOM port listed under SERCOM or SERCOM-ALT. For D5, we are using the SERCOM port in the SERCOM column. For D3 and D4, we are using the SERCOM port in the SERCOM-ALT column.

### 4.) Putting It All Together.

Step 4 is running the code, testing, and troubleshooting. For this example, we are going to grab a Serial LCD screen and connect it to our new SPI port. Make sure that you have [soldered](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) headers to the LCD if you have not already.

[![Circuit Diagram SAMD21 SERCOM SPI to SerLCD](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/8/SparkFun_Arduino_SAMD21_Configured_SERCOM_Serial_SPI-Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/8/SparkFun_Arduino_SAMD21_Configured_SERCOM_Serial_SPI-Fritzing_bb.jpg)

The next step is to test out the SPI port with the code listed below. The code is pretty bare bones and shows you where all your new code should go. The code also includes a pin definition for the `CSPIN`. Copy and paste the code in your Arduino IDE. Select your board, COM port, and hit upload.

    language:c
    /*********************************************************************
       Sample code for setting up additional Serial ports on a SamD21 board
       In this example the Redboard Turbo is used with the 16x2 SerLCD display
       For more information on the SerLCD code check out the github repo
       https://github.com/sparkfun/OpenLCD
       https://www.sparkfun.com/products/14812
       https://www.sparkfun.com/products/14072
       By: Michelle Shorter - SparkFun Electronics
       License: This code is public domain but you buy me a burger
       if you use this and we meet someday (Beefware license).
    **********************************************************************/
    #include <SPI.h>
    #include "wiring_private.h" // pinPeripheral() function
    #define CSPIN 6
    #define Time 25

    //D3-MISO, D4-MOSI, D5-SCK
    SPIClass SPI2 (&sercom2, 3, 5, 4, SPI_PAD_0_SCK_3, SERCOM_RX_PAD_1); 

    int i = 0;
    void setup() 

    void loop() 

    //Sends a string over SPI
    void spiSendString(char* data)
    

## Adding an I2C

### 1.) Figure Out Which Pins to Use.

Picking pins for I^2^C is a bit easier. SDA is always on Pad 0. SCL is always on Pad 1. That\'s it. In this case, when we look at our chart, we can immediately rule out MISO and D38 as those pins are used or not broken out. That means that D4 will be SDA and D3 will be SCL.

### 2.) Add Your Code.

Next, let\'s figure out what code we need. Let\'s take a look at the [Wire.cpp](https://github.com/arduino/ArduinoCore-samd/blob/master/libraries/Wire/Wire.cpp#L285) file in Arduino's SAMD21 core files. All the way near the bottom on line 285, you\'ll see the following line. This is what we are trying to duplicate in our code. The **variant.h** file defines all those macros, but their names give us a good idea of what should go there.

    language:c
    TwoWire Wire(&PERIPH_WIRE, PIN_WIRE_SDA, PIN_WIRE_SCL);

Let\'s start with the definition. Let\'s pick a name. \"myWire\" sounds good. We also know we are going to use SERCOM 2, that we are going to use D4 for SDA and D3 for SCL. So, we\'ll add the following to our code.

    language:c
    TwoWire myWire(&sercom2, 4, 3);

### 3.) Update the Pin Definitions Based on the Pin Mux.

Next, we need to set up the mux. Right now the pins are defined as general I/O pins. We want them to act as SERCOM pins. The first thing we need to do is to add the pin peripheral library. Then we use the `pinPeripheral` command to set up the pin definition.

    language:c
    #include "wiring_private.h" // pinPeripheral() function

    myWire.begin();
    pinPeripheral (4,PIO_SERCOM_ALT);
    pinPeripheral (3,PIO_SERCOM_ALT);

You\'ll notice that the code uses the argument `PIO_SERCOM_ALT`. If you look on the datasheet, you\'ll notice that pins can have a SERCOM port listed under SERCOM or SERCOM-ALT. In this case, both pins are under the SERCOM_ALT column, but if you are using a pin under the SERCOM column, use the argument \"`PIO_SEROM`\".

### 4.) Putting It All Together.

Step 4 is running the code, testing, and troubleshooting. For this example, we are going to grab a Serial LCD screen and connect it to our new I^2^C port. Make sure that you have [soldered](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) headers to the LCD if you have not already.

[![Circuit Diagram SAMD21 SERCOM I2C to SerLCD](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/8/SparkFun_SAMD21_Configured_SERCOM_Serial_I2C_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/8/SparkFun_SAMD21_Configured_SERCOM_Serial_I2C_Fritzing_bb.jpg)

The next step is to test out the I2C port with the code listed below. The code is pretty bare bones and shows you where all your new code should go. Copy and paste the code in your Arduino IDE. Select your board, COM port, and hit upload.

    language:c
    /*********************************************************************
       Sample code for setting up additional Serial ports on a SamD21 board
       In this example the Redboard Turbo is used with the 16x2 SerLCD display
       For more information on the SerLCD code check out the github repo
       https://github.com/sparkfun/OpenLCD
       https://www.sparkfun.com/products/14812
       https://www.sparkfun.com/products/14072
       By: Michelle Shorter - SparkFun Electronics
       License: This code is public domain but you buy me a burger
       if you use this and we meet someday (Beefware license).
    **********************************************************************/
    #include <Wire.h> 
    #include "wiring_private.h" // pinPeripheral() function

    //D4 SDA, D3 SCL
    TwoWire myWire(&sercom2, 4, 3);

    #define DISPLAY_ADDRESS1 0x72 //This is the default address of the OpenLCD

    int i = 0;
    void setup() 

    void loop() 

## Helpful Charts

I promised you some charts.

- Let\'s start with the SAM21 [datasheet](https://cdn.sparkfun.com/datasheets/Dev/Arduino/Boards/Atmel-42181-SAM-D21_Datasheet.pdf). Starting on page 21 under *I/O Multiplexing and Considerations*, you\'ll see all the pin definition including the mux options. This is really where everything comes from.
- Next are the [graphical datasheets](https://github.com/sparkfun/Graphical_Datasheets/tree/master/Datasheets). While these are available on the product pages of any board that has one, here they are as a neat little collection.

Now here are a few charts I made to help you out\...

### Arduino Pins on SAMD21

  --------------------------------------------------------------------------------------------------
  SERCOM   Port 0    Port 0 Alt   Port 1    Port 1 Alt   Port 2   Port 2 Alt   Port 3   Port 3 Alt
  -------- --------- ------------ --------- ------------ -------- ------------ -------- ------------
  0        D4        A3           D3        A4           D1       D8           D0       D9

  1        D11       Crystal      D13       Crystal      D10      SWCLK        D12,\    SWDIO
                                                                               RXLED    

  2        MISO      D4           D38       D3           D2       D1/TX        D5       D0/RX

  3        D20/SDA   D11/MOSI     D21/SCL   D13/SCK      USB      D10/SS,\     USB      D12/MISO,\
                                                                  D6                    D7

  4                  A1,\                   A2,\                  MOSI,\                SCK,\
                     MISO                   D38                   D2                    D4

  5                  D20/SDA,\              D21/SCL      D6       USB,\        D7       USB,\
                     A5                                           EDBGTX                EDBGRX
  --------------------------------------------------------------------------------------------------

*Note: The ISP header does not name the pins individually so it is referred to as ISP or the actual SPI pin names that are used on the board.*

*Note: A comma means there are 2 pins that can use that port. A slash denotes 2 different names for the same pin.*

*Note: Some pins are tied directly to the USB port or the Crystal and not available for use. They are labeled as such.*

### Arduino Boards

I also figured it might be nice to know which SERCOM ports are open on different Arduino boards. Below is a table that lists what SERCOM ports that are already assigned to a serial protocol for a few development boards.

  SERCOM Port                0         1     2                3     4     5
  -------------------------- --------- ----- ---------------- ----- ----- ----------------
  Zero                       Serial1   SPI                    I2C   ISP   Serial on EDBG
  MKR1000                    I2C       SPI   WinC1500 (SPI)               Serial1
  SAMD21 Development Board   Serial1   SPI                    I2C   ISP   Serial
  SAMD21 Mini Board          Serial1   SPI                    I2C         
  RedBoard Turbo             Serial1   SPI                    I2C   ISP   Flash