# Source: https://learn.sparkfun.com/tutorials/nrf52832-breakout-board-hookup-guide

## Introduction

The nRF52832 is [Nordic Semiconductor\'s](https://www.nordicsemi.com/eng/Products/Bluetooth-low-energy/nRF52832) latest multiprotocol radio system-on-chip (SoC). It\'s half microcontroller, with a list of features including 32 configurable I/O pins, SPI, I^2^C, UART, PWM, ADC\'s, 512kB flash, and 64kB RAM. And, it\'s half 2.4GHz multiprotocol radio, supporting **Bluetooth low energy** (BLE), **ANT**, and Nordic\'s proprietary 2.4GHz ultra low-power wireless communication \-- it even features on-chip NFC tag support.

[![SparkFun nRF52832 Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/5/2/13990-01.jpg)](https://www.sparkfun.com/sparkfun-nrf52832-breakout.html)

### [SparkFun nRF52832 Breakout](https://www.sparkfun.com/sparkfun-nrf52832-breakout.html) 

[ WRL-13990 ]

The nRF52832 is Nordic Semiconductor's latest multiprotocol radio System on Chip (SoC). It's half microcontroller, with a...

**Retired**

SparkFun\'s [nRF52832 Breakout](https://www.sparkfun.com/products/13990) provides easy access to all of the chip\'s features. It breaks out all of the nRF52\'s I/O pins, provides a 32.768kHz RTC crystal, a user-programmable button and LED, and a trace antenna to send and receive those 2.4GHz transmissions. Plus, to make the chip as easy-to-flash as possible, the breakout comes pre-programmed with a **serial bootloader**.

### Covered In This Tutorial

This tutorial is a comprehensive getting started guide for the SparkFun nRF52832 Breakout. It documents hardware features of the board, and includes tips on getting a computer set up for nRF52832 software development. Programming the chip via the serial bootloader using the Arduino IDE is the primary focus of the latter half of the tutorial.

### Bill of Materials

To follow along with this tutorial \-- and to get your nRF52832 Breakout up-and-running \-- you\'ll need a few additional components.

To **program the board**, we recommend interfacing the breakout board with a [SparkFun Beefy 3 - FTDI Basic Breakout](https://www.sparkfun.com/products/13746). In addition to providing a USB-to-serial programming interface, this board will also be able to fully-power the nRF52832 breakout. The less-beefy [3.3V FTDI Basic](https://www.sparkfun.com/products/9873) can also be used to program the board, but we recommend finding an alternative power supply to power the nRF52832 board. Whichever USB-to-serial converter you go with, don\'t forget the [USB cable](https://www.sparkfun.com/products/10215)!

[![SparkFun Beefy 3 - FTDI Basic Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/7/6/13746-01.jpg)](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html)

### [SparkFun Beefy 3 - FTDI Basic Breakout](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html) 

[ DEV-13746 ]

This is SparkFun Beefy 3 FTDI Basic Breakout for the FTDI FT231X USB to serial IC. The pinout of this board matches the FTDI ...

[ [\$18.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

To **interface** the nRF52832 Breakout with the FTDI, you\'ll need to solder a 6-pin strip of headers to the board\'s serial interface. We recommend [right-angle headers](https://www.sparkfun.com/products/553) for this job, but the [straight](https://www.sparkfun.com/products/116) or [long headers](https://www.sparkfun.com/products/12693) can also get it done. Grab some extra male headers \-- or even [female headers](https://www.sparkfun.com/products/115) \-- if you plan on connecting to any of the I/O pins.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Long Centered Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/4/2/7/12693-02.jpg)](https://www.sparkfun.com/break-away-headers-40-pin-male-long-centered-pth-0-1.html)

### [Long Centered Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-40-pin-male-long-centered-pth-0-1.html) 

[ PRT-12693 ]

This is a row of 40 break away headers spaced 0.1\" apart with long pins on both sides. This header is especially useful when ...

[ [\$1.50] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

Finally, to complete the Bluetooth connection, you\'ll need a **BLE-equipped smartphone**. This tutorial documents how to use the nRF52832 with Nordic\'s free, open-source [nRF Toolbox](https://www.nordicsemi.com/eng/Products/Nordic-mobile-Apps/nRF-Toolbox-App) and [nRF Connect](https://www.nordicsemi.com/eng/Products/Nordic-mobile-Apps/nRF-Connect-for-mobile-previously-called-nRF-Master-Control-Panel) apps, which are available on both iOS and Android devices.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![nRF Toolbox](https://cdn.sparkfun.com/r/100-100/assets/learn_tutorials/5/4/9/nRF-Toolbox-icon.png)](https://www.nordicsemi.com/eng/Products/Nordic-mobile-Apps/nRF-Toolbox-App) |                       | [![nRF Connect](https://cdn.sparkfun.com/r/100-100/assets/learn_tutorials/5/4/9/nRF-Connect_listitem.png)](https://www.nordicsemi.com/eng/Products/Nordic-mobile-Apps/nRF-Connect-for-mobile-previously-called-nRF-Master-Control-Panel) |
|                                                                                                                                                                                    |                       |                                                                                                                                                                                                                                          |
| [nRF Toolbox](https://www.nordicsemi.com/eng/Products/Nordic-mobile-Apps/nRF-Toolbox-App)                                                                                          |                       | [nRF Connect](https://www.nordicsemi.com/eng/Products/Nordic-mobile-Apps/nRF-Connect-for-mobile-previously-called-nRF-Master-Control-Panel)                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Suggested Reading

The nRF52832 Breakout is an intermediate-to-advanced level board, but don\'t let that scare you off! This tutorial should be able to walk you through getting started with the board regardless of your skill level. That said, we do recommend that you\'re familiar with the topics covered in these tutorials:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v)

### Using the Arduino Pro Mini 3.3V 

This tutorial is your guide to all things Arduino Pro Mini. It explains what it is, what it\'s not, and how to get started using it.

[](https://learn.sparkfun.com/tutorials/bluetooth-basics)

### Bluetooth Basics 

An overview of the Bluetooth wireless technology.

[](https://learn.sparkfun.com/tutorials/sparkfun-usb-to-serial-uart-boards-hookup-guide)

### SparkFun USB to Serial UART Boards Hookup Guide 

How to use the SparkFun FTDI based boards to program an Arduino and access another serial device over the hardware serial port, without unplugging anything!

## Hardware Overview

Nordic\'s nRF52832 is a system-on-chip (SoC) that combines an ARM Cortex-M4F microprocessor with a 2.4GHz multiprotocol radio. In addition to providing access to all of the chip\'s I/O pins, the breakout board also includes a handful of external components. The annotated image below summarizes the breakout board\'s features:

[![Annotated top diagram of nRF52832 Breakout](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nrf52832-top-annotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nrf52832-top-annotated.jpg)

### Powering the nRF52832 Breakout Board

The nRF52832 can operate on a power supply **between 1.7 and 3.6V**. The board also includes a 3.3V regulator with a maximum input of 6V, in case you want to power the board with batteries or a regulated wall supply.

The power input pins are located toward the bottom side of the board. Each of the header rows includes a \"GND\", \"VIN\" and \"3.3V\" supply input. The \"VCC\" and \"GND\" pins on the 6-pin serial header can also be used to power the board (assuming the jumper is closed, more on that later).

[![Power supply inputs](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nrf52832-power-inputs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nrf52832-power-inputs.jpg)

The **VIN pin** feeds into the on-board regulator, which brings the voltage down to 3.3V to supply the nRF52832. The regulator can supply up to 600mA \-- way more than the nRF52832 should ever need. If you\'re powering via regulator, you can use the 3.3V pins as outputs to supply external components.

Note that the **maximum input** to the 3.3V regulator (into the VIN pin) is **6V**!

Alternatively, you can skip the regulator and supply the nRF52832 directly by using the **3.3V pin**. Voltage supplied here doesn\'t necessarily have to be 3.3V \-- it can be anywhere between the SoC\'s 1.7V and 3.6V operating range \-- so you can use a coin cell battery, or a pair of alkaline batteries to power the chip.

The **red power LED** is tied to that \"3.3V\" bus as well. If it\'s lighting up, your nRF52832 should be getting power.

### 32 Multipurpose I/O Pins

The nrF52832\'s microprocessor features an array of hardware peripherals, including three [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) \-- configurable as either master or slave, two [I^2^C](https://learn.sparkfun.com/tutorials/i2c) interfaces, and a [UART](https://learn.sparkfun.com/tutorials/serial-communication) (with optional flow control). On top of the serial interfaces, the chip also features 8 [ADC](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) pins and three hardware [PWM](https://learn.sparkfun.com/tutorials/pulse-width-modulation) outputs. Each of the 32 I/O pins can be assigned almost any function, so you can move those interfaces around the board as you see fit.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

There are just a few functions that are assigned static pins:

- For your real-time counting (RTC) needs, a **32.768kHz crystal** is connected to pins 0 and 1.
- Pin 6 is connected to a **momentary push-button**, which serves an important function during bootloading.
- Pin 7 is tied to an **LED**. It\'s active-low, so pull the pin to ground to turn the LED on.
- Pins 26 and 27 were chosen as the RX and TX UART pins. They can be re-assigned in a user-application but are stuck as the serial pins during the bootloader\'s operation.
- Pin 21 also doubles as an active-low **reset** input.
- The nRF52832\'s **NFC** capability can be supported by an antenna connected to pins 9 and 10.

### Setting the Solder Jumpers

The back side of the nRF52832 Breakout is filled with jumpers to help you customize the operation of your board. They\'re labeled with an abbreviation of their purpose.

[![Board bottom side with jumpers highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nrf52832-bottom-annotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nrf52832-bottom-annotated.jpg)

The jumpers that default closed can be sliced open with a [hobby knife](https://www.sparkfun.com/products/9200), while those jumpers that default open can be closed with a small application of solder.

  Jumper Label   Default   Notes
  -------------- --------- ----------------------------------------------------------
  FTDI VCC-EN    Closed    Connects 6-pin serial header VCC to 3.3V bus.
  PWR-LED        Closed    Enables or disables the red power indicator LED.
  1/2 (NFC)      Open      Connects GPIO 9 and 10 to NFC antenna tuning capacitors.
  RTC-EN         Closed    Connects GPIO 0 and 1 to a 32.768kHz RTC crystal.

#### FTDI VCC-EN - Power via 6-Pin Serial Connector

This jumper controls whether or not an FTDI Breakout connected via the 6-pin serial connector can supply power to the nRF52832. By keeping this jumper to closed, you\'ll be able to power the nRF52832 with the same device used to program it.

You may want to cut the jumper if you\'re powering the board externally. Also consider opening the jumper if you\'re using a [3.3V FTDI Basic](https://www.sparkfun.com/products/9873) (the non-\"beefy\" version), which may not be able to source enough sustained power to supply the chip.

#### PWR-LED - Turn Off the Power LED

One of the nRF52832\'s most important features is its low-power capability. If your application needs to run for months on a single battery and you\'re making full-use of the nRF52832\'s ultra-low power sleep modes, the 1-2mA of current pulled by the LED may relatively dwarf the current draw of the microcontroller.

Cutting this jumper will effectively disable the power LED. You won\'t always have a visible power indicator, but you\'ll be able to save a lot of power!

#### 1 & 2 - NFC Antenna Tuning Capacitors

One of the most unique features of the nRF52832 is its NFC tag support \-- it can transmit data to a nearby NFC-compatible device, or even be programmed to wake-from-sleep in the presence of an NFC field.

To use the NFC feature, a 13.56 MHz antenna must be connected to GPIO pins 9 and 10. Most NFC antennae also require a pair of tuning capacitors between the antenna pins and ground. The NFC jumpers can be closed to connect each of the NFC antenna pins to a 180pF capacitor.

[![NFC tuning caps from schematic](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/5/4/9/nrf52832-schematic-tuningcaps.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nrf52832-schematic-tuningcaps.png)

*NFC tuning caps and enable jumpers, from the [nRF52832 Breakout schematic](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/sparkfun-nrf52832-breakout-schematic-v10.pdf).*

This cap value may not be perfect for every antenna, but it should support a relatively wide range of antenna inductances. We tested it successfully with an [Abracon ANFACA-4545-A01](http://www.digikey.com/product-detail/en/abracon-llc/ANFCA-4545-A01/535-12513-ND/4864622) and a [Pulse Electronics W7001](http://www.digikey.com/product-detail/en/pulse-electronics-corporation/W7001/553-2633-ND/4169647).

#### RTC-EN - Connect/Disconnect the 32.768kHz Crystal

The nRF52832 Breakout equips the chip with a 32.768kHz crystal \-- connected to GPIO pins 0 and 1. Unfortunately, those pins make up a quarter of the available ADC inputs. So, if your application doesn\'t require an RTC \-- and you need those pins to for another purpose \-- grab a hobby knife and cut the two traces between their pads to disconnect the crystal.

## Hardware Assembly

To program the chip, and to use any of the nRF52832\'s 32 I/O, you\'ll need to solder *something* to its headers. In the least, we recommend soldering [right-angle male headers](https://www.sparkfun.com/products/553) or [straight male headers](https://www.sparkfun.com/products/116) onto the six-pin serial header. Either of these will interface easily with the FTDI Basic and Beefy Breakouts.

[![six-pin right-angle header soldered into serial port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/9/assembly-serial-header.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/assembly-serial-header.jpg)

*Solder a six-pin right-angle header into the serial port to interface it with an FTDI Beefy 3.*

The remaining two rows of vias are breadboard-compatible, so you can solder male pins into both and have it straddle a breadboard.

[![male headers soldered into both header rows, making it breadboard-compatible](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/9/assembly-breadboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/assembly-breadboard.jpg)

*Solder straight male headers into the pair of header rows to make the breakout breadboard-compatible.*

Or you can solder [wire](https://www.sparkfun.com/products/11375), [female headers](https://www.sparkfun.com/products/115), or anything else your project requires into those remaining holes.

## Adding Arduino Compatibility

Arduino isn\'t the most powerful IDE out there, nor is it the most versatile, but it does make things easy if you\'re just getting started with a new platform. Fortunately, there\'s an nRF52 Arduino board addon available for just that purpose! This section details how to install the nRF52 Arduino libraries, cores, and tools.

### Download and Install the Board Package

The nRF52 Arduino cores are based on the great work by [sandeepmistry](https://github.com/sandeepmistry/arduino-nRF5). We\'ve added nRF52832 Breakout Board compatibility to his board files, and added an extra tool to enable serial bootloading.

To install support for the nRF52 board in Arduino, begin by opening your **Arduino preferences** (File \> Preferences). Then copy and paste the URL below into the \"Additional Board Manager URLs\" text box.

    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/nrf5/IDE_Board_Manager/package_sparkfun_index.json

[![Adding the additional board manager URL](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/arduino-board-add.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/arduino-board-add.png)

Then **hit OK**, and navigate to the **Tools** \> **Board** \> **Boards Manager\...** tool. A search for \"nRF52\" should turn up a **SparkFun nRF52 Boards** result. Select that and click install.

[![nRF52832 Board Manager installation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/9/arduino-nrf52-board-install.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/arduino-nrf52-board-install.png)

The install may take a few minutes \-- the package includes arm-gcc and a few other tools totaling around 100 MB. Once the installation is complete, go to **Tools** \> **Board** and select \"SparkFun nRF52832 Breakout\" under the \"Nordic Semiconductor nRF5 Boards\" section.

[![SparkFun nRF52832 Breakout Arduino Board selection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/9/arduino-board-selection.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/arduino-board-selection.png)

## Programming via Bootloader

The nRF52832 Breakout ships out with a pre-programmed serial bootloader, so you don\'t need a specialized JTAG programmer to load code onto it. You do, however, need an FTDI Basic (or an FTDI Basic -like device) to set up a serial interface between your computer and the breakout.

### Connecting the FTDI to the Breakout

The FTDI Basic mates up with the nRF52832\'s 6-pin serial header. Match up the \"BLK\" and \"GRN\" labels, and slide the boards together.

[![FTDI Beefy 3 connected, providing power and a programming interface](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/9/programming-ftdi-connected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/programming-ftdi-connected.jpg)

You should see the red power LED illuminate. If it doesn\'t power up, make sure you haven\'t disabled the FTDI-VCC EN jumper on the back of the board.

### Triggering the Bootloader

Unfortunately, the nRF52832 Breakout\'s bootloader doesn\'t feature an auto-reset function like many Arduino\'s. To decide whether to enter the bootloader or run its application code, the nRF52832 samples the state of GPIO 6 when it boots up. If pin 6 is LOW, it enters the bootloader, otherwise it boots into its programmed application

So, to boot the nRF52832 into its bootloader you must **reset the chip while holding down the pin 6 button**. In step-by-step form, the trick to resetting into the bootloader is:

1.  Press down on both the RESET and 06 buttons.
2.  Release reset.
3.  Verify that the blue (pin 7) LED begins blinking.
4.  Release the 06-labeled user button.

[![example button pressing to get into bootloader mode](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/reset-to-bootloader-600w.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/reset-to-bootloader-600w.gif)

While in bootloader mode, the nRF52832\'s blue LED on pin 7 should blink at increasing speed in what we call the \"timebomb\" sequence.

This is, admittedly, a little tricky and a lot annoying to perform before every program, but it\'s the trade-off we get for not programming via expensive JTAG programmers. Once you\'ve entered the bootloader, you can upload code to the chip via Arduino\'s \"Upload\" button.

### Upload Blink

Try loading up a basic blink example \-- setting the blinking pin to the on-board LED on pin 7 \-- and uploading. Here\'s some code to copy paste:

    language:c
    const int ledPin = 7;

    void setup()
    

    void loop()
    

**LED Polarity** -- The blue LED, attached to pin 7, is **active-low**. Writing the pin LOW will turn the LED on, and writing it HIGH will turn it off.

### Troubleshooting

If you get an upload error like this:

Failed to upgrade target. Error is: No data received on serial port. Not able to proceed.

Possible causes:

\- bootloader, SoftDevice or application on target does not match the requirements in the DFU package.\
- baud rate or flow control is not the same as in the target bootloader.\
- target is not in DFU mode. If using the SDK examples, press Button 4 and RESET and release both to enter DFU mode.

\
Make sure your nRF52832 Breakout\'s LED is blinking in a ticking-timebomb pattern \-- ensuring that it\'s in **bootloader mode**. If the chip is in the bootloader and still not accepting code, try **cycling power** to the breakout by disconnecting and reconnecting the FTDI Basic.

## BLEPeripheral Arduino Library

The nRF5 board definitions will allow you to program the nRF52832 and toggle its GPIO, but it doesn\'t include any Bluetooth support. For that, we recommend grabbing the [BLEPeripheral Arduino library](https://github.com/sandeepmistry/arduino-BLEPeripheral).

The BLEPeripheral library can be installed from Arduino\'s Library Manager. Simply go to **Sketch** \> **Include Library** \> **Manage Libraries\...**. In the search box, type \"BLEPeripheral\", select it, and click \"Install.\"

[![Installing the BLEPeripheral library](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/9/bleperipheral-install.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/bleperipheral-install.png)

Alternatively, the library can be installed by downloading the latest version from the [GitHub repository](https://github.com/sandeepmistry/arduino-BLEPeripheral). Follow along with our [Installing an Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) for help installing the library via this method.

## BLE Blink Example

Here are a few examples that show as bare-bones as possible what it takes to turn your nRF52832 Breakout into a BLE peripheral. This first example allows you to control the board\'s pin 7 LED from your smart phone \-- using the [nRF Connect app](https://www.nordicsemi.com/eng/Products/Nordic-mobile-Apps/nRF-Connect-for-mobile-previously-called-nRF-Master-Control-Panel). It\'s the Blink sketch of the BLE world!

To test the Bluetooth connection, you'll need to pair the breakout board with another Bluetooth-compatible device. Most modern smartphones can fit that bill.

You\'ll also need a BLE application installed on your phone -- something that lets you connect to devices and fiddle with or read their characteristics. There are a handful of Bluetooth debugging applications out there that can help get you started communicating via Bluetooth. [PunchThrough's LightBlue Explorer](https://itunes.apple.com/us/app/lightblue-explorer-bluetooth/id557428110?mt=8) is one of our favorite's, but it's only available for iOS. Nordic's [nRF Connect](https://www.nordicsemi.com/eng/Products/Nordic-mobile-Apps/nRF-Connect-for-mobile-previously-called-nRF-Master-Control-Panel) -- available for both iOS and Android devices -- is another good choice. That's what we'll document here.

### The Code

Copy and paste the code below into your Arduino IDE.

    language:c
    // Import libraries (BLEPeripheral depends on SPI)
    #include <SPI.h>
    #include <BLEPeripheral.h>

    //////////////
    // Hardware //
    //////////////
    #define LED_PIN    7 // LED on pin 7
    #define LED_ACTIVE LOW // Pin 7 LED is active low
    #define LED_DEFAULT LOW

    ///////////////////////
    // BLE Advertisments //
    ///////////////////////
    const char * localName = "nRF52832 LED";
    BLEPeripheral blePeriph;
    BLEService bleServ("1207");
    BLECharCharacteristic ledChar("1207", BLERead | BLEWrite);

    void setup() 
    

    void loop() 
    
    }

    void setupBLE()
    

Then upload the code to your Breakout, using the instructions from the previous section.

#### Use the nRF Connect to Test

Upon opening nRF Connect, you\'ll be presented with a list of nearby Bluetooth devices. If you\'re in the SparkFun offices \-- or otherwise surrounded by coworker\'s with way too many Bluetooth devices \-- your list may include page(s) of device names. Look for \"nRF52832 LED\", and click the \"Connect\" button next to that. (Note: until you connect to the breakout, it may, instead, advertise the name \"Arduino\".)

[![nRF Connect device list](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/5/4/9/nrfConnect-list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nrfConnect-list.png)

You can set the device name \-- replacing \"nRF52832 LED\" \-- with the `blePeripheral.setDeviceName([name])` function.

Click \"Connect\" on the nRF52832 LED device, and you\'ll be sent over to the \"Services\" view. From there, click \"Unknown Service\" \-- the UUID string should match that of the `bleServ` object in your example code.

This next interface takes some experimenting to figure out. The down arrows represent reads, the up arrows allow you to write to a characteristic, and the triple-down-arrow turns notify on or off. To begin, **tap the up arrow** next to the top \"unknown service\". This will allow you to control the state of the LED. In the box that opens up, try entering either `00` or `01`, which should turn the LED either off or on, respectively.

[![Writing a 0x01 to the LED characteristic](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/5/4/9/nRFConnect-write.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nRFConnect-write.png)

After tapping \"Send\" you should see the LED change state.

## BLE Button Example

This example demonstrates how to use the BLE read and notify features. It monitors the button on pin 6 of the nRF52832 Breakout. When the button state changes a BLE notification is sent.

### The Code

Using the BLEPeripheral library, upload this code to your Breakout:

    language:c
    // Import libraries (BLEPeripheral depends on SPI)
    #include <SPI.h>
    #include <BLEPeripheral.h>

    //////////////
    // Hardware //
    //////////////
    #define BTN_PIN    6 // BTN pin on 6
    #define BTN_ACTIVE LOW

    ///////////////////////
    // BLE Advertisments //
    ///////////////////////
    const char * localName = "nRF52832 Button";
    BLEPeripheral blePeriph;
    BLEService bleServ("1234");
    BLECharCharacteristic btnChar("1234", BLERead | BLENotify);

    void setup() 
    

    void loop()
    
    }

    void setupBLE()
    

#### Use the nRF Connect to Test

Use nRF Connect to connect to your nRF52832 Breakout \-- just like last time. This time the name of the device should change to nRF52832 Button (if it\'s still \"LED\", try connecting anyway \-- sometimes the local ID doesn\'t change until you\'ve connected to it).

Tap into the \"Unknown Service\" again, but, this time, try **tapping the single-down arrow** to read the service\'s characteristic. This will read the state of the nRF52832 Breakout\'s pin 6 button. While the button is un-actuated, the value of the property should be 0x01. If you can hold the button down while also tapping the single-down arrow, the value should change to 0x00.

[![Reading the nRF52832\'s button in nRF Connect](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/5/4/9/nrfConnect-button-notify.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/9/nrfConnect-button-notify.png)

*Activate notify by tapping the triple-down-arrow. Then when you press the button, the value should automatically update.*

You can also try setting the characteristic to **notify**, by tapping the **triple-down arrow**. In this mode, the value should automatically be notified when there\'s a change in state. Press and release the button to see the value change from 0x00 to 0x01.