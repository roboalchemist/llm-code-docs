# Source: https://learn.sparkfun.com/tutorials/nrf24l01-transceiver-hookup-guide

## Introduction

These breakout boards provide SPI access to the nRF24L01+ transceiver module from [Nordic Semiconductor](http://www.nordicsemi.com/). The transceiver operates at 2.4 GHz and with power supplies 3.3V-5V. It has 250kbps, 1Mbps and 2Mbps on-air data-rate options and is applicable for low-power applications. The breakout boards are available with an [on-board antenna](https://www.sparkfun.com/products/691) or an option to add an external antenna to the [RP-SMA connector](https://www.sparkfun.com/products/705).

[![SparkFun Transceiver Breakout - nRF24L01+](https://cdn.sparkfun.com/r/600-600/assets/parts/4/8/0/00691-01a.jpg)](https://www.sparkfun.com/products/691)

### [SparkFun Transceiver Breakout - nRF24L01+](https://www.sparkfun.com/products/691) 

[ WRL-00691 ]

This module uses the newest 2.4GHz transceiver from Nordic Semiconductor, the nRF24L01+. This transceiver IC operates in the ...

**Retired**

[![SparkFun Transceiver Breakout - nRF24L01+ (RP-SMA)](https://cdn.sparkfun.com/r/600-600/assets/parts/4/8/8/00705-01.jpg)](https://www.sparkfun.com/products/705)

### [SparkFun Transceiver Breakout - nRF24L01+ (RP-SMA)](https://www.sparkfun.com/products/705) 

[ WRL-00705 ]

The nRF24L01 module is the latest in RF modules from SparkFun. This module uses the 2.4GHz transceiver from Nordic Semiconduc...

**Retired**

### Required Materials

To follow along with this tutorial, we recommend you have access to the following materials. You may not need everything, depending on what you already have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend reviewing them before beginning to work with the nRF24L01+ Breakouts.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

## Hardware Overview

## Antenna Options

SparkFun carries two versions of the breakout, listed below.

### On-Board Chip Antenna

[![On-board Antenna](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/onboardstraightonCrop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/onboardstraightonCrop.jpg)

*[SparkFun Transceiver Breakout nRF24L01+ with chip antenna (WRL-00691)](https://www.sparkfun.com/products/691)*

The first version is the [SparkFun Transceiver Breakout - nRF24L01+ with chip antenna](https://www.sparkfun.com/products/691). The on-board chip antenna allows for a more compact version of the breakout. However, the smaller antenna also means a lower transmission range. Keep that in mind if you plan on mounting this board in an enclosure. The enclosure material may also decrease the range of this board, as you cannot move the antenna outside of any interference. This antenna should be suitable for most applications.

### RP-SMA

[![RP-SMA Antenna](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/rpsmaantennaCrop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/rpsmaantennaCrop.jpg)

*[SparkFun Transceiver Breakout - nRF24L01+ with RP-SMA antenna (WRL-00705)](https://www.sparkfun.com/products/705)*

If you need more range in your wireless connection or if you need to move your antenna outside an interference zone, we recommend the [RP-SMA antenna version of the breakout](https://www.sparkfun.com/products/705). You can learn more about SMA connectors [here](https://en.wikipedia.org/wiki/SMA_connector). This version works with the [RP-SMA 2.4GHz antenna](https://www.sparkfun.com/products/145) and its [larger counterpart](https://www.sparkfun.com/products/558). Because of the external antenna on this version of the breakout, it has a greater range than the on-board antenna version.

[![2.4GHz Duck Antenna RP-SMA](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/00145-02-L.jpg)](https://www.sparkfun.com/2-4ghz-duck-antenna-rp-sma.html)

### [2.4GHz Duck Antenna RP-SMA](https://www.sparkfun.com/2-4ghz-duck-antenna-rp-sma.html) 

[ WRL-00145 ]

2.4GHz Duck Antenna 2.2dBi with Reverse Polarized - SMA RF connector. Perfect for prototyping with our RF ICs. 50 ohm impedan...

[ [\$14.95] ]

[![2.4GHz Duck Antenna RP-SMA - Large](https://cdn.sparkfun.com/r/140-140/assets/parts/3/8/1/00558-1.jpg)](https://www.sparkfun.com/2-4ghz-duck-antenna-rp-sma-large.html)

### [2.4GHz Duck Antenna RP-SMA - Large](https://www.sparkfun.com/2-4ghz-duck-antenna-rp-sma-large.html) 

[ WRL-00558 ]

2.4GHz Large Duck Antenna 5dBi with Reverse Polarized - SMA RF connector. Perfect for prototyping with our RF ICs. 50 ohm imp...

[ [\$18.50] ]

## Pins

[![Labeled Pins](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/back_pins_crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/back_pins_crop.jpg)

*Broken out pins with labels*

While the nRF24L01+ IC has 20 pins available, our breakout board simplifies this down to the 8 pins required to get up and running. These pins are the same on both versions of the board. The pins function as follows:

- **GND** - Ground
- **IRQ** - Interrupt pin. This pin is active `LOW`.
- **MISO** - 3.3V-5V tolerant SPI slave output.
- **MOSI** - 3.3V-5V tolerant SPI slave input.
- **SCK** - 3.3V-5V tolerant SPI clock.
- **CSN** - 3.3V-5V tolerant SPI chip select.
- **CE** - 3.3V-5V tolerant chip enable. This pin toggles the nRF24L01+ IC between transmit (TX), receive (RX), standby, and power-down mode.
- **VCC** - This is VRAW and is regulated on-board down to 3.3V for the proper functionality of the nRF24L01+. Voltage range on this pin is **3.3V-7V**.

## Functionality

## Transmission Mode

The IC can either work in transmit or receive mode. This mode is determined by both the CE pin state, the PWR_UP register, and the PRIM_RX register. The following chart shows the various configurations.

**Transmission Mode Truth Table**

Mode

PWR_UP Register

PRIM_RX Register

CE Pin

FIFO State

RX Mode

1

1

1

\-

TX Mode

1

0

1

Data in TX FIFOs. Will empty all levels in TX FIFOs

TX Mode

1

0

Minimum 10μs high pulse

Data in TX FIFOs.Will empty one level in TX FIFOs.

Standby-II

1

0

1

TX FIFO empty.

Standby-I

1

\-

0

No ongoing packet transmission.

Power Down

0

\-

\-

\-

## Hardware Hookup

### Solder Connection Points

We recommend soldering headers to the nRF24L01+ board to allow you to prototype your circuit. To avoid interference with the antenna on the nRF24L01+, use [right-angle male headers](https://www.sparkfun.com/products/553).

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

If you need a review for PTH soldering, check out our [solder tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering).

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

### Connect the Wires

Now that you have your headers attached, you can plug in the jumper wires. Connect the RedBoard and nRF24L01 as listed.

RedBoard → nRF24L01+

- 5V → VCC
- GND → GND
- D8 → IRQ
- D9 → CE
- D10 → CSN
- D11 → MOSI
- D12 → MISO
- D13 → SCK

### Final Circuit

Once you have everything connected, your system should look like the following:

[![nRF24L01 Hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/0/nRF24L01Hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/nRF24L01Hookup.jpg)

*nRF24L01+ Circuit Assembly*

### Repeat!

Since these are radio modules, you\'ll need **at least two** modules to talk to each other. Duplicate the connections between another RedBoard and nRF24L01+ module. Don\'t forget to attach the antenna to your nRF24L01+ if you have the RP-SMA version.

## Arduino Code

There are a lot of libraries available for this module, but we recommend using the RF24 library, originally written by [maniacBug](https://github.com/maniacbug/RF24), and updated for Arduino 1.6x by [TMRh20](http://tmrh20.github.io/RF24/).

You can find the most up-to-date version of the library [here](https://github.com/TMRh20/RF24). Alternatively, you can download this zip and install it into your Arduino IDE libraries folder. If you need help with the library installation, please check out our [tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library).

[Download the RF24 Library](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/RF24.zip)

Once you have your code properly installed, open up *Examples → RF24 → GettingStarted.ino*.

Check out the User Configuration section of the code, and make sure you update yours as shown below.

    language:c
    /****************** User Config ***************************/
    /***      Set this radio as radio number 0 or 1         ***/
    bool radioNumber = 1;

    /* Hardware configuration: Set up nRF24L01 radio on SPI bus plus pins 9 & 10 */
    RF24 radio(9,10);

One radio should have the `radioNumber` set to `0` and the other should be set to `1`.

Upload the code to your Redboards. Once you have them both set up, you can open up two [terminals](https://learn.sparkfun.com/tutorials/terminal-basics) set at 115200 bps, 8-N-1, and you should see the following appear on the terminal.

    language:c
    RF24/examples/GettingStarted
    *** PRESS 'T' to begin transmitting to the other node

Press `T` in one terminal, press `R` in the other, and wait until you start seeing your radios communicating! You should see something similar in your terminal.

[![Terminal Output](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/TerminalOutput.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/0/TerminalOutput.JPG)

*Receiver output in the terminal.*