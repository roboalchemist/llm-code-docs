# Source: https://learn.sparkfun.com/tutorials/sparkfun-usb-to-serial-uart-boards-hookup-guide

## Introduction

SparkFun has a line of USB to serial UART bridge products designed to allow a user to communicate with a serial UART through a common USB port. It is harder to find computers with serial UART ports on them these days, but super common to find serial devices. Many of the official Arduino and clones share a common interface. This interface is essentially the 6 pin Single-In-Line (SIL), 0.1" pitch version of FTDI\'s [TTL-232R cables](https://www.sparkfun.com/products/9717).

[![SmartBasic Hero Pic](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/6/12935-01cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/6/12935-01cropped.jpg)

The key change from the FTDI cables to our Arduino compatible boards is that we swapped pin 6 from RTS to DTR. This change was required to match Arduino\'s method of resetting the ATmega328P using the DTR signal.

[![FTDI Pinout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/6/FTDI_Arduino.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/6/FTDI_Arduino.png)

*Arduino compatible pinout is slightly different from the FTDI cable (pin 6)*

**Note** The signal difference on pin 6 may cause these devices to not be 100% compatible with devices designed for use with the FTDI TTL-232R cables.

### Advantages

Having a detachable USB to UART bridge comes with several advantages over boards like the [Arduino Uno](https://www.sparkfun.com/products/11224).

- Removing the computer interface makes the board smaller.
- You only need to buy the circuit once and can program many Arduinos.
- The bridge circuitry draws power (up to 500 mW) that\'s not needed in many installed applications. Removing this parasitic drain makes your project more power efficient & your batteries last longer.

### Suggested Reading

Before we get started, you might want to review this other tutorial:

- [Installing FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

## Hardware Tour

The interface to this line of boards is simple. One side has a TTL-232R cable compatible 6 pin SIL, 0.1" pitch female header. This side connects to the Arduino (TTL serial UART) board. We often use [right angle headers](https://www.sparkfun.com/products/553) on the [Arduino Pro Mini](https://www.sparkfun.com/products/11114) to make connecting a serial bridge trivial. Our boards have silkscreen labels of where the black and green wires of the FTDI TTL-232R cables would be.

[![Beefy 3 connected to an Arduino Pro Mini](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/6/Beefy_3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/6/Beefy_3.png)

*Fritzing diagram showing the connection between a USB to UART bridge and a Pro Mini*

[![6 pin SIL, 0.1" pitch](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/6/FTDI_SIL.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/6/FTDI_SIL.jpg)

*6 pin SIL, 0.1" pitch header at top of PCBA*

The other side has a USB mini-B or USB micro-B jack. A standard USB cable is used to connect this jack to a host computer.

This line of products comes in a few forms. Here is a table comparing the most common options.

  Name                                                                            Voltage   Current Limit                 Connector
  ------------------------------------------------------------------------------- --------- ----------------------------- -------------
  [SparkFun FTDI Basic Breakout - 5V](https://www.sparkfun.com/products/9716)     5.0 V     N/A^[1](#fn1)^         USB Mini-B
  [SparkFun FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/products/9873)   3.3 V     \< 50 mA                      USB Mini-B
  [Beefy 3](https://www.sparkfun.com/products/13746)                              3.3 V     \< 600 mA^[2](#fn2)^   USB Micro-B
  [LilyPad FTDI Basic Breakout - 5V](https://www.sparkfun.com/products/10275)     5.0 V     N/A^[1](#fn1)^         USB Mini-B

*Table 1. Comparison of Common SparkFun Offerings*

**Warning:** These boards are for prototyping ONLY. Unlike commercial devices, power negotiation and suspend mode do not occur, and it is possible to overload the USB host. Exercise caution when connecting a load, and *never connect a load that draws too much current.*

^1.\ \[5V\ is\ taken\ directly\ from\ V~BUS~\ and\ is\ *only\ limited\ by\ the\ USB\ host\ controller*.\][↩](#ref1 "Jump back to footnote 1 in the text.")^\
^2.\ \[This\ 3.3V\ regulator\ is\ powered\ directly\ from\ V~BUS~\ and\ is\ *only\ limited\ by\ the\ USB\ host\ controller*.\][↩](#ref1 "Jump back to footnote 1 in the text.")^

For a quick comparison of a few USB to Serial boards, check out this Enginursday blog post:

[](https://news.sparkfun.com/2451 "September 14, 2017: SparkFun offers several options in the USB-Serial arena. Today we'll attempt to demystify the differences between them.")

### Enginursday: Exploring Different USB-Serial Boards 

[September 14, 2017]

Read Post

## Connecting the USB to Serial UART Boards

These bridges have two connections. On one end there is a USB device connection. See [table 1](# "Jump to offering comparison table.") for more details on the exact connector for the specific product. This interface is USB 1.1 / USB 2.0 full-speed compatible. A standard USB A to some sort of B cable is used to connect the bridge to the computer.

The other connection is a 0.1\" pitch female header designed to connect to the microcontroller. Many of our products come with a compatible row of plated-through holes. These are designed to have 0.1\" male headers soldered in. Some cases will best be served with straight headers, other with right-angle headers. The desired connection varies from design to design as discussed [here](https://www.sparkfun.com/news/2027). Some products come prepopulated with these headers.

[![FTDI header prepopulated](https://cdn.sparkfun.com/assets/parts/1/0/6/5/0/13342-01.jpg)](https://cdn.sparkfun.com/assets/parts/1/0/6/5/0/13342-01.jpg)

*Prepopulated FTDI header example*