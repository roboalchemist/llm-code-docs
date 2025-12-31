# Source: https://learn.sparkfun.com/tutorials/gnss-receiver-breakout---max-m10s-qwiic-hookup-guide

## Introduction

The [SparkFun u-blox MAX-M10S breakout](https://www.sparkfun.com/products/18037) is an ultra-low-power, high performance, miniaturized GNSS board that is perfect for battery operated applications that don\'t possess a lot of space, such as asset trackers and wearable devices. In this tutorial, we will quickly get you set up using the Qwiic ecosystem and Arduino so that you can start reading the output!

[![SparkFun GNSS Receiver Breakout - MAX-M10S (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/3/4/1/18037-SparkFun_GNSS_Receiver_Breakout_-_MAX-M10S__Qwiic_-01_Default.jpg)](https://www.sparkfun.com/sparkfun-gnss-receiver-breakout-max-m10s-qwiic.html)

### [SparkFun GNSS Receiver Breakout - MAX-M10S (Qwiic)](https://www.sparkfun.com/sparkfun-gnss-receiver-breakout-max-m10s-qwiic.html) 

[ GPS-18037 ]

The SparkFun MAX-M10S Breakout is an ultra-low-power, GNSS board that is perfect for battery operated applications that don\'t...

[ [\$45.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun GNSS Receiver Breakout - MAX-M10S (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/3/4/1/18037-SparkFun_GNSS_Receiver_Breakout_-_MAX-M10S__Qwiic_-01_Default.jpg)](https://www.sparkfun.com/sparkfun-gnss-receiver-breakout-max-m10s-qwiic.html)

### [SparkFun GNSS Receiver Breakout - MAX-M10S (Qwiic)](https://www.sparkfun.com/sparkfun-gnss-receiver-breakout-max-m10s-qwiic.html) 

[ GPS-18037 ]

The SparkFun MAX-M10S Breakout is an ultra-low-power, GNSS board that is perfect for battery operated applications that don\'t...

[ [\$45.95] ]

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/0/14986-GPS_GNSS_Magnetic_Mount_Antenna_SMA_-_3m-01.jpg)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html)

### [GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html) 

[ GPS-14986 ]

This exceptional GPS/GNSS antenna is designed for both GPS and GLONASS reception.

[ [\$16.50] ]

[![Reversible USB A to C Cable - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/3/15424-Reversible_USB_A_to_C_Cable_-_2m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html)

### [Reversible USB A to C Cable - 2m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html) 

[ CAB-15424 ]

These 2m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the U...

[ [\$10.50] ]

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

#### Additional GPS Antenna Options

Below are some other GPS antenna options.

[![GPS Embedded Antenna SMA](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/7/00177-01.jpg)](https://www.sparkfun.com/gps-embedded-antenna-sma.html)

### [GPS Embedded Antenna SMA](https://www.sparkfun.com/gps-embedded-antenna-sma.html) 

[ GPS-00177 ]

Embedded antenna for small, mobile applications. Basic unpackaged antenna with LNA. 5inch cable terminated with standard male...

[ [\$18.50] ]

[![GPS/GNSS Embedded Antenna - 1m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/1/14987-GPS_GNSS_Embedded_Antenna_SMA_-_1m-01a.jpg)](https://www.sparkfun.com/gps-gnss-embedded-antenna-1m-sma.html)

### [GPS/GNSS Embedded Antenna - 1m (SMA)](https://www.sparkfun.com/gps-gnss-embedded-antenna-1m-sma.html) 

[ GPS-14987 ]

This tri-band GNSS antenna is ideal for GPS L1, GLONASS L1, and Beidou B2 reception.

[ [\$95.95] ]

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you aren't familiar with the following concepts, we also recommend checking out a few of these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/serial-basic-hookup-guide)

### Serial Basic Hookup Guide 

Get connected quickly with this Serial to USB adapter.

[](https://learn.sparkfun.com/tutorials/redboard-plus-hookup-guide)

### RedBoard Plus Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Plus. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

## Hardware Overview

We\'ve broken out the u-blox MAX-M10S module to a breakout. This section highlights the relevant features of the board. For more information about the IC, check out the Resources and Going Further.

[![Top View of GNSS Receiver Breakout](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic_u-blox.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic_u-blox.jpg)

### Power

Power for this board should be **3.3V**. There is a 3.3V pin on the PTH header along the side of the board, but you can also provide power through the Qwiic connector.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View of Power Nets](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_Power.jpg)   [![Bottom View of Power Nets](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_Power.jpg)
  *Top View*                                                                                                                                                                                                                                                                            *Bottom View*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Communication Ports

**Note:** The MAX-M10S differs from other modules as it only has I^2^C and UART. It is important to note that the board does not have SPI pins.

[![Back of Board I2C and UART Ports, but no SPI](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic.jpg)

### Qwiic and I^2^C (a.k.a. DDC)

There are two PTHs labeled `SDA` and `SCL` which indicates the I^2^C data lines. Similarly, you can just use the Qwiic connector to provide power and connect to the I^2^C pins. The [Qwiic ecosystem](https://www.sparkfun.com/qwiic) is made for fast prototyping by removing the need for soldering. All you need to do is plug a Qwiic cable into the Qwiic connector and voila!

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View of I2C](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_I2C.jpg)   [![Bottom View of I2C](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_I2C.jpg)
  *Top View*                                                                                                                                                                                                                                                                 *Bottom View*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** The only I2C address for this and all u-Blox GPS products is **0x42**, though each can have their address changed through software.

### UART

For users that prefer to communicate over UART, we made sure to configure the UART pin grouping to an industry standard to ensure that it easily connects to a [Serial Basic](https://www.sparkfun.com/products/15096). Extra UART pins are also broken out on another edge of the board as well. The port is set to **38400 baud** as the default.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View of UART](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_UART.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_UART.jpg)   [![Bottom View of UART](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_UART.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_UART.jpg)
  *Top View*                                                                                                                                                                                                                                                                    *Bottom View*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Control Pins

These pins are used for various extra control of the MAX-M10S. The control pins are highlighted below.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View of Control Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_Control_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_Control_Pins.jpg)   [![Bottom View of Control Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_Control_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_Control_Pins.jpg)
  *Top View*                                                                                                                                                                                                                                                                                               *Bottom View*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- **PPS:** Pulse-per-second output pin. Begins blinking at 1Hz when module gets basic GPS/GNSS position lock.
- **[RST]:** Reset input pin. Pull this line low to reset the module.
- **[SAFE]:** Safeboot input pin. This is required for firmware updates to the module and generally should not be used or connected. To save on space, the silkscreen is labeled on the bottom of the board.
- **EINT:** Interrupt input/output pin. Can be configured using U-Center to bring the module out of deep sleep or to output an interrupt for various module states.

### SMA Connector for Antenna

The board is populated with an SMA connector for a secure connection to a patch antenna.

[![SMA Antenna](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_SMA_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_SMA_Connector.jpg)

### LEDs

The board includes two status LEDs as indicated in the image below.

[![LEDs](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_LEDs.jpg)

- **PPS:** The pulse per second LED will illuminate each second once a position lock has been achieved.
- **PWR:** The power LED will illuminate when 3.3V is provided either over the Qwiic bus or any of the 3.3V PTH pins.

### Jumpers

There are four jumpers on the back of the board. For more information, check out our [tutorial on working with jumper pads and PCB traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all) should you decide to cut the traces with a hobby knife.

[![Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Bottom_Jumpers.jpg)

- **PWR:** This is connected to the PWR LED on the top of the board. Cutting this disables the LED.
- **MEAS:** Short for current measurement. By default, the MEAs is closed. Cutting the jumper and soldering to the PTH pads will allows you to insert a current meter and precisely monitor the how much current your application is consuming.
- **PPS:** This is connected to the PPS LED on the top of the board. Cutting this disables the LED.
- **I^2^C:** The I^2^C jumpers are open by default. By adding solder to the jumpers, it will connect to the 2.2kΩ pull-up resistors for the I^2^C bus. Most of the time you can leave these alone unless your project requires you to [connect the pull-up resistors](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level).

### Backup Battery

The MS621FE rechargeable battery maintains the battery backed RAM (BBR) on the GNSS module. This allows for much faster position locks (a.k.a. hot start). The BBR is also used for module configuration retention. The battery is automatically trickle charged when power is applied and should maintain settings and GNSS orbit data for up to two weeks without power.

[![Backup Battery](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_Backup_Battery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic-Top_Backup_Battery.jpg)

### Board Dimensions

The overall length and width with the antenna connector is about 1.74\" x 1.20\". There are four mounting holes by each corner of the board.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/e/8/8/9/8/SparkFun_u-blox_MAX-M10S_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/e/8/8/9/8/SparkFun_u-blox_MAX-M10S_Board_Dimensions.png)

## Hardware Assembly

At a minimum, you will need to attach an external antenna to the MAX-M10S, supply 3.3V power, and connect to one of the board\'s peripherals.

### Attaching an External Antenna

Plug in one of our patch antennas with SMA connector to the GPS board. Secure the connection using the hex nut until it is finger-tight.

[![Finger Tightening the SMA GPS Antenna to the MAX-M10S](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic_Antenna.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic_Antenna.jpg)

### I^2^C

One method to communicate with the MAX-M10S is through I^2^C. The Qwiic connect system makes it quick and easy to connect the board to your system using a polarized cable. For embedded projects, you can use a Qwiic-enabled Arduino development board like the [RedBoard Plus](https://www.sparkfun.com/products/18158) and its [associated USB cable](https://www.sparkfun.com/products/15425). Then plug a Qwiic cable between the RedBoard Plus and the SparkFun MAX-M10S.

[![RedBoard Plus Connected to the MAX-M10S via Qwiic Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_-_MAX-M10S_Qwiic_RedBoard_Plus_Hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_-_MAX-M10S_Qwiic_RedBoard_Plus_Hookup.jpg)

**Note:** The RedBoard Plus includes a switch to adjust the logic levels to either 5V or 3.3V. It does not matter what side the switch is on for this setup to communicate with the MAX-M10S since there are logic level converters included before the Qwiic connector.

If you\'re going to be [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) to the through hole pins for I^2^C functionality, then just attach the following lines between your chosen microcontroller\'s I^2^C and the MAX-M10S:

- SDA to SDA
- SCL to SCL
- 3.3V to 3.3V
- GND to GND

### UART

A second method to communicate with the MAX-M10S is through its serial UART. You can directly connect the GPS to the computer by connecting a USB-to-serial converter to the industry standard serial connection (aka the \'FTDI\' pinout). In this case, we used an CH340 but you can use another USB-to-serial converter like an FTDI. Just make sure to match the silkscreen (GRN to GRN and BLK to BLK). For a secure connection, you\'ll need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) male header pins or wires to the MAX-M10S.

[![USB-to-Serial Converter to MAX-M10S](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic_Serial_UART_u-blox.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/9/18037-SparkFun_GNSS_Receiver_Breakout_MAX-M10S_Qwiic_Serial_UART_u-blox.jpg)

You could also connect the pins to a microcontroller like the RedBoard Plus as long as the switch for the logic levels are flipped to the 3.3V side before powering the board up. You\'ll need to do a little bit more work as opposed to using Qwiic connect system. You\'ll need to attach the following lines between your chosen microcontroller\'s UART and the MAX-M10S:

- Tx to Rx
- Rx to Tx
- 3.3V to 3.3V
- GND to GND

## Software Setup and Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)\
\
If you\'ve never connected an FTDI or CH340 to your computer before, you may need to install drivers for the USB-to-serial converter. Check out our [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) or [How to Install CH340 Drivers](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide#drivers-if-you-need-them) tutorial for help with the installation.

**Note:** We support two versions of the SparkFun u-blox GNSS library. [Version 2](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) and [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3). [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3) uses the u-blox Configuration Interface (VALSET and VALGET) to configure the module, instead of the deprecated UBX-CFG messages. For modules like the F9 and M10, we recommend upgrading to [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3). However, older modules like the M8 do not support the Configuration Interface. For those you will need to keep using [Version 2](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) of the library. We will continue to support both.

The SparkFun u-blox Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun u-blox GNSS v3**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3) to manually install.

[SparkFun u-blox Arduino Library v3 (ZIP)](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3/archive/main.zip)

There are several example sketches provided that utilize the I^2^C bus to get you up and receiving messages from space. We\'ll go over one of the examples in this tutorial.

**Note:** Some examples use the \'**MicroNMEA**\' library by **Steve Marple**. Make sure to install the library as well by searching for it in the Arduino library manager. You could also grab the zip here from the [GitHub repository](https://github.com/stevemarple/MicroNMEA) to manually install.\
\

[MicroNMEA Arduino Library (ZIP)](https://github.com/stevemarple/MicroNMEA/archive/master.zip)

**Warning:** This tutorial focuses on the Arduino Library for Arduino microcontrollers. Unfortunately for users using it with Python on a Raspberry Pi, [the Qwiic (I^2^C) is not supported in the Python Package due to issues with clock stretching](https://github.com/sparkfun/Qwiic_Ublox_Gps_Py/tree/master#qwiic_ublox_gps_py).

## Example Code

We\'re just going to look at Basics Example Two (i.e. \"**Example2_NMEAParsing.ino**\") which in my opinion, makes it clear the awesomeness of these GPS receivers. That is to say, talking to satellites and finding out where in the world you are.

    language:c
    #include <Wire.h> //Needed for I2C to GPS

    #include "SparkFun_u-blox_GNSS_v3.h" //Click here to get the library: http://librarymanager/All#SparkFun_u-blox_GNSS_v3
    SFE_UBLOX_GNSS myGNSS;

    void setup()
    

      //This will pipe all NMEA sentences to the serial port so we can see them
      myGNSS.setNMEAOutputPort(Serial);
    }

    void loop()
    

When you upload this code you\'ll have to wait \~24s to get a lock onto any satellites. After that first lock, the backup battery on the board will provide power to some internal systems that will allow for a **hot start** the next time you turn on the board. The **hot start** only lasts four hours, but allows you to get a lock within one second. After you get a lock the [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) will start listing longitude and latitude coordinates, as seen below. Make sure to set the serial monitor to **115200 baud**.

[![This image shows a screenshot of the Arduino Serial terminal spitting out latitude and longitude data.](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/9/nmeaCapture-ublox2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/9/nmeaCapture-ublox2.jpg)

*These are the coordinates for SparkFun HQ*

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)