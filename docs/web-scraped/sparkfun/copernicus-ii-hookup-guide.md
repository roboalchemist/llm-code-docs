# Source: https://learn.sparkfun.com/tutorials/copernicus-ii-hookup-guide

## Copernicus II Overview

The [Copernicus II GPS Module](https://www.sparkfun.com/products/11858) is a 12-channel receiver from Trimble. It has a small form factor, making it a great device for applications requiring precise GPS control. The DIP module board allows you to easily embed this into your projects by providing an easy to connect to interface.

The module supports NMEA, TSIP and TAIP protocols at 1 Hz. The board also is designed to interface with an SMA antenna.

[![SparkFun GPS Module - Copernicus II DIP (12 Channel)](https://cdn.sparkfun.com/r/600-600/assets/parts/8/2/5/6/11858-01.jpg)](https://www.sparkfun.com/sparkfun-gps-module-copernicus-ii-dip-12-channel.html)

### [SparkFun GPS Module - Copernicus II DIP (12 Channel)](https://www.sparkfun.com/sparkfun-gps-module-copernicus-ii-dip-12-channel.html) 

[ GPS-11858 ]

The \[Copernicus II\](http://www.sparkfun.com/products/10922) is a great GPS module from Trimble, but the SMD module prohibits ...

**Retired**

The module runs at 3.3V and consumes around 40mA at 3.0V. For the TSIP protocol, the module\'s default baud rate is 38400 bps, while it defaults to 4800 bps for the NMEA protocol. These settings are configurable. The module is permanently set to 8 data bits, no parity, 1 stop bits and no flow control.

### Suggested Reading

If you haven\'t worked with GPS before, or are unfamiliar with serial communication, you may want to read the following tutorials before continuing on with this module.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

## Hardware Hookup

To get started communicating with the Copernicus II, you will need to connect four pins on the module: VCC, GND, TX-B, and RX-B.

For our example, we will be connecting the module to a terminal window on the computer using an [3.3V FTDI Basic Board](https://www.sparkfun.com/products/9873), and will be using the [GPS Antenna Embedded SMA](https://www.sparkfun.com/products/177).

### Connections:

Copernicus II → 3.3V FTDI Basic

- VCC → 3.3V
- GND → GND
- TX-B → RXI
- RX-B → TXO

Take a look at the Fritzing diagram below showing the connections between the Copernicus II and the FTDI Basic based on the [pin descriptions from the datasheet](https://cdn.sparkfun.com/datasheets/Sensors/GPS/63530-10_Rev-B_Manual_Copernicus-II.pdf). In some cases, users needed to connect R2 to Vcc to operate but it should not be necessary.

[![Copernicus II Hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/9/GPS_Serial_Trimble_Copernicus_II_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/9/GPS_Serial_Trimble_Copernicus_II_Fritzing_bb.jpg)

**Heads up!** If you have the [**old** Copernicus I](https://www.sparkfun.com/products/retired/8146), the pinout and hookup is different. You old SKU for the part is GPS-8146 and can be distinguished with a \"*58052-00*\" printed on the IC. The Copernicus II should have \"*68340-00*\" printed on the IC.Check out the [old datasheet on page 23 for the Copernicus I](http://www.sparkfun.com/datasheets/GPS/Copernicus_Manual.pdf) for more information. [Users reported](https://www.sparkfun.com/products/retired/8146#comment-4eaad84b757b7fd351005f43) needing to connect XRST, BOOT, R2 and XSTANDY to VCC in order for the module to operate.\
\

![Copernicus I](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/9/GPS_Serial_Trimble_Copernicus_II_Fritzing_bb_bb.jpg)

## Talking to the Module

Once you have your boards connected, open up your favorite serial terminal program and connect to the appropriate COM port for your FTDI Basic. The connection settings should be 4800 bps, 8 data bits, no parity, 1 stop bit, and no flow control.

If your module is hooked up properly and has a lock, you should see a scrolling output like this.

[![Copernicus Module Output](https://cdn.sparkfun.com/assets/c/1/d/d/2/526aac92757b7fca528b4567.png)](https://cdn.sparkfun.com/assets/c/1/d/d/2/526aac92757b7fca528b4567.png)

*Copernicus II output in CoolTerm terminal window*

As you can see in the GPGGA output, the module is reading the position to be 4003.89135 N and 10512.58816 W, which happens to be SparkFun\'s headquarters. The module is also currently only seeing 2 satellites, and the location data being output is from the last value stored in the flash (shown by the GPS Quality Indicator of 7). The lack of additional data is due to testing this inside a large building like SparkFun where the signal fades in and out, so you should actually be getting more data from your module if testing near a window or outside with a clear view.

### Talking to a Microcontroller

If you\'re looking to add GPS to your Arduino project using the Copernicus, we suggest you look into the [Tiny GPS library](https://github.com/mikalhart/TinyGPS). This library is great for parsing out the data that you want to use in your project such as time, altitude, position, etc. There are plenty of resources involving this library around the web. A quick search should yield plenty of examples. If you need a refresher on how to install an Arduino library, instructions can be found [here](https://learn.sparkfun.com/tutorials/installing-an-arduino-library).