# Source: https://learn.sparkfun.com/tutorials/sparkfun-satellite-transceiver-kit---swarm-m138-hookup-guide

## Introduction

Looking for a low-cost way to send and receive data messages via satellite? This is it! With a clear view of the sky, the Satellite Transceiver Breakout - Swarm M138 allows you to send and receive short messages. It works anywhere in the world, including the polar regions, far beyond the reach of WiFi and Cellular networks. It is perfect for a variety of low-bandwidth use cases: from connecting people and tracking vehicles, ships, or packages to relaying sensor data for agriculture, energy, and industrial IoT applications. The built-in GNSS receiver makes it perfect for many tracking applications.

We created the Satellite Transceiver Breakout to make using the Swarm M138 modem as easy as possible. Want to connect it to your laptop or Raspberry Pi and send and receive messages anywhere? You can absolutely do that. Want to hook it up to your Arduino board and send and receive messages via the modem\'s 3.3V UART Serial interface? You can absolutely do that too!

Let\'s get started!

[![SparkFun Satellite Transceiver Kit - Swarm M138](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/0/7/1/21218-Swarm-kit.jpg)](https://www.sparkfun.com/sparkfun-satellite-transceiver-kit-swarm-m138.html)

### [SparkFun Satellite Transceiver Kit - Swarm M138](https://www.sparkfun.com/sparkfun-satellite-transceiver-kit-swarm-m138.html) 

[ KIT-21287 ]

With a clear view of the sky, the Satellite Transceiver Breakout - Swarm M138 allows you to send and receive short messages.

**Retired**

### Suggested Reading

Want to read around the subject? You may find it useful to read these tutorials first:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

## What\'s In The Box?

The [SparkFun Satellite Transceiver Kit - Swarm M138](https://www.sparkfun.com/products/21287) contains everything you need to get started with the Swarm network:

[![Pictured are the box contents](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-kit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-kit.jpg)

*Having a hard time seeing? Click the image for a closer look.*

- Swarm M138 Modem
- SparkFun Satellite Transceiver Breakout
- Swarm VHF Antenna and SparkFun Ground Plane
- Molex adhesive u.FL GNSS Antenna
- 2 x 25mm u.FL cables, u.FL to SMA adapter and 2 x M2.5 screws

The M138 modem is a Mini-PCI Express (mPCIe) format board. Installing it is as easy as slotting it into the matching connector on the Breakout board and securing it in place with the two M2.5 screws. We\'ll talk about [Hardware Assembly](https://learn.sparkfun.com/tutorials/satellite-transceiver-breakout---swarm-m138---hookup-guide#hardware-assembly) in more detail below.

The modem has two u.FL antenna connections on it, one marked \"VHF\" (for the Very High Frequency signal used to communicate with the Swarm satellites) and a separate one for satellite navigation (marked \"GPS\"). You can, if you wish, connect the provided antennas directly to the u.FL connectors on the modem. Or, you can use the provided 25mm u.FL cables to connect the modem to the robust SMA connections on the Breakout.

The Swarm antenna is a purpose-designed coiled quarter-wave antenna tuned to the Swarm satellite frequencies. It does require a ground plane and so we\'ve included one of those in the box too! It comes with mounting holes to allow it to be secured to (e.g.): 2\" or 1.5\" antenna pole, a camera tripod, or a handrail.

Both antennas need to be located outdoors, with a clear view of the sky. But **the modem and breakout board are not weatherproof**. Depending on how you are going to weatherproof the boards, and where they are going to be located, you may find additional extension cables or GNSS antennas useful.

[![GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/0/14986-GPS_GNSS_Magnetic_Mount_Antenna_SMA_-_3m-01.jpg)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html)

### [GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html) 

[ GPS-14986 ]

This exceptional GPS/GNSS antenna is designed for both GPS and GLONASS reception.

[ [\$16.50] ]

[![Interface Cable - SMA Female to SMA Male (25cm)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/2/9/12861-01.jpg)](https://www.sparkfun.com/interface-cable-sma-female-to-sma-male-25cm.html)

### [Interface Cable - SMA Female to SMA Male (25cm)](https://www.sparkfun.com/interface-cable-sma-female-to-sma-male-25cm.html) 

[ WRL-12861 ]

This is a basic SMA (Sub-Miniature A) male to female connector cable. Each cable is 25cm (9.8\") long and has a 50Ω impedance...

[ [\$5.50] ]

[![Magnetic Mount SMA - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/2/4/1/19576-Action-2.jpg)](https://www.sparkfun.com/magnetic-mount-sma-2m.html)

### [Magnetic Mount SMA - 2m](https://www.sparkfun.com/magnetic-mount-sma-2m.html) 

[ GPS-19576 ]

When experimenting with GPS or RF it can be very handy to have the antenna on the top of your house or car with a clear view ...

[ [\$32.50] ]

[![SMA Male to SMA Female - 10m (RG174)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/5/4/5/17495-SMA_Male_to_SMA_female_RG174_10M-01.jpg)](https://www.sparkfun.com/sma-male-to-sma-female-10m-rg174.html)

### [SMA Male to SMA Female - 10m (RG174)](https://www.sparkfun.com/sma-male-to-sma-female-10m-rg174.html) 

[ CAB-17495 ]

This 10m (33\') SMA extension does a great job of connecting your receiver or radio to a distant antenna with as little RF los...

**Retired**

If you\'re going to connect the Breakout to your computer, laptop or Raspberry Pi, you\'re going to need a USB-C cable too:

[![Reversible USB A to C Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/4/15425-Reversible_USB_A_to_C_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html)

### [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html) 

[ CAB-15425 ]

These 0.8m cables have minor modifications that allow them to be plugged into their ports regardless of orientation on the US...

[ [\$6.50] ]

[![Reversible USB A to C Cable - 0.3m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/5/15426-Reversible_USB_A_to_C_Cable_-_0.3m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-3m.html)

### [Reversible USB A to C Cable - 0.3m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-3m.html) 

[ CAB-15426 ]

These 0.3m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the...

[ [\$5.50] ]

[![Reversible USB A to C Cable - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/3/15424-Reversible_USB_A_to_C_Cable_-_2m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html)

### [Reversible USB A to C Cable - 2m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html) 

[ CAB-15424 ]

These 2m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the U...

[ [\$10.50] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

Going to connect the Breakout to your Arduino board? You will probably need: break away headers and jumper wires. 2-pin jumpers will be useful for re-linking the CH340 connections later.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Jumper Wires Premium 6\" M/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/5/7/09140-02-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html)

### [Jumper Wires Premium 6\" M/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html) 

[ PRT-09140 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumper wires terminated as male to female. Use these to jumper fro...

[ [\$4.60] ]

[![Jumper - 2 Pin](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/0/7/09044-02-L.jpg)](https://www.sparkfun.com/jumper-2-pin.html)

### [Jumper - 2 Pin](https://www.sparkfun.com/jumper-2-pin.html) 

[ PRT-09044 ]

These are two pin jumpers (also called shunts) that will create an electrical connection between two pin headers. Commonly us...

[ [\$0.50] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

[![Jumper Wires Premium 12\" F/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/9/1/09389-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-12-f-f-pack-of-10.html)

### [Jumper Wires Premium 12\" F/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-12-f-f-pack-of-10.html) 

[ PRT-09389 ]

This is a SparkFun exclusive! These are 12\" long, 26 AWG jumper wires terminated as female to female. Use these to jumper fro...

[ [\$4.95] ]

[![Straight Header - Female (PTH, 0.1in., 8-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/9/8/11895-01.jpg)](https://www.sparkfun.com/header-8-pin-female-pth-0-1.html)

### [Straight Header - Female (PTH, 0.1in., 8-Pin)](https://www.sparkfun.com/header-8-pin-female-pth-0-1.html) 

[ PRT-11895 ]

These are standard 0.1\" spaced header pins that can be through-hole mounted. This header connects perfectly with most 8-pin m...

[ [\$0.80] ]

## Swarm Satellite

[Swarm\'s](https://swarm.space/) mission is to connect people and devices anywhere, at all times, at the lowest cost.

If you\'ve used satellite communication systems in the past, you\'ll know that the message costs can be high if you\'re sending a lot of data. Swarm are changing that. Their uniquely small satellites are the smallest operational satellites in space, at just ¼U (11 x 11 x 2.8 cm). Because of their small size, they cost much less to launch than most satellites, and these savings are passed along to their customers.

[![Swarm SpaceBees communicate with M138 Modem](https://cdn.sparkfun.com/assets/home_page_posts/4/8/6/0/unnamed__2_.png)](https://cdn.sparkfun.com/assets/home_page_posts/4/8/6/0/unnamed__2_.png)

Each Swarm modem requires a data plan to send and receive data. However, the cost of this is *much* lower than other networks. A data plan is an annual contract for USD \$60 per year (USD \$5 per month). Each plan includes 750 data packets per month. Each packet can be up to 192 Bytes in size. You can also stack up to 4 data plans, allowing a single modem to use 3000 packets (576 kBytes) per month. Please see the [Registering Your Swarm M138 Modem](%20https://swarm.space/registering-your-swarm-m138-modem/) for full details. Additionally, you can create or login to your Swarm account [here](https://bumblebee.hive.swarm.space/login).

Swarm provide global coverage over all regions, but there are regulatory restrictions for specific countries.\
\
The current list of approved countries / regions for the M138 Modem is: USA, Antarctica, Australia, Austria, Brazil, Canada, Colombia, Denmark, Georgia, Germany, Greenland, Iceland, Ireland, New Zealand, Netherlands, Spain, Sweden, United Kingdom and International Waters (12 nautical miles offshore).\
\
Swarm continues to grow this list of approved countries as quickly as possible. Customers will receive regular updates on approved regions through the [Swarm newsletter](https://swarm.space/contact/).

## Overview of the Swarm Network

When a SpaceBEE passes over any given location, it will send out beacon packets to Swarm Modems that are in their receiver state. The Modem's antenna will need to have a clear view of the sky, and a low RF noise environment to receive this satellite beacon.

*Format of a satellite beacon packet:*

    $RT RSSI=,SNR=,FDEV =,TS=,DI=*xx

Once the Modem receives this satellite beacon, it will attempt to transmit any queued transmission packets to the satellite. Message packets that are successfully received by the satellite will then be acknowledged by the satellite back to the Modem. The Modem will then discard the message packet from its outgoing transmission queue.

*The Swarm M138 Modem can store a maximum of 1000 outgoing message packets. Each message packet is held for a default duration of 48 hours, which is user configurable, after which the packet will be discarded if not transmitted.*

The satellite will then carry that message packet until it passes over a Swarm ground station. The satellite will downlink the message packet to the ground station after which the data will be routed to Swarm's cloud platform named the [Swarm Hive](https://bumblebee.hive.swarm.space/login). The user can then view their data on Hive, or extract that data using Swarm's [REST API](https://bumblebee.hive.swarm.space/apiDocs), or [webhooks](https://bumblebee.hive.swarm.space/delivery).

[![How Swarm satellite sends message to cloud platform Swarm Hive](https://cdn.sparkfun.com/assets/home_page_posts/4/8/6/0/unnamed__6_.png)](https://cdn.sparkfun.com/assets/home_page_posts/4/8/6/0/unnamed__6_.png)

*The Swarm Hive will retain data for 30 days before it is discarded, so it is best to pull that data from the Hive to reference it later. Swarm has a Python Script example that you can download by [clicking here](https://swarm.space/swarm-python-script-example/).*

## Hardware Overview

### Swarm M138 Modem

[![Pictured is the Swarm M 1 3 8 modem](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/5/1/19236-Satellite_Transceiver_Breakout_-_Swarm_M138-03_HRd_-_HG.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/5/1/19236-Satellite_Transceiver_Breakout_-_Swarm_M138-03_HRd_-_HG.jpg)

*Don\'t worry about that QR code. It doesn\'t go anywhere.*

At the heart of our product is a Swarm M138 satellite modem. This is a Mini-PCI Express Card containing both the satellite modem and a very capable u-blox GNSS receiver, all in one integrated package! It can operate from a wide range of supply voltages: 3.0V Min; 5.0V Max. Its standard 3.3V CMOS serial UART interface and NMEA-style command set makes it easy to integrate into your project.

The peak current draw during transmit depends on the supply voltage. Please see [Current Draw](https://learn.sparkfun.com/tutorials/satellite-transceiver-breakout---swarm-m138---hookup-guide#current-draw) below for more details.

### USB-C and CH340

[![Pictured are the U S B connector and C H 3 4 0 E interface](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-USBC-CH340.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-USBC-CH340.jpg)

Our board includes a USB-C interface for power and/or serial data, in addition to a full set of breakout pins. Want to plug it into your laptop or Raspberry Pi and use it to communicate out in the field? You can absolutely do that!

We\'ve included our standard CH340E interface chip to convert USB to serial. On Windows, you may need to install a driver and we have a tutorial to help with that:

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

You can power the board directly from USB-C or USB 3 ports, but not older USB 2.0 ports. Please see [Current Draw](https://learn.sparkfun.com/tutorials/satellite-transceiver-breakout---swarm-m138---hookup-guide#current-draw) below for more details.

We\'ve included a 2A resettable fuse too, just in case anything goes wrong.

### mPCIe Connector

   [![mPCIe connector on the Front of the Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-mPCIeConnector-Front.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-mPCIeConnector-Front.jpg)   [![Screw Fixings on the Back of the Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-mPCIeConnector-Back.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-mPCIeConnector-Back.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                         *mPCIe connector*                                                                                                                                                                                                                                               *Screw Fixings*

The M138 modem is a very nicely designed piece of kit. The mPCIe card-edge connection makes it really easy to integrate. Two M2.5 screws secure the modem in position.

### SMA Connections

[![Pictured are the u dot F L and S M A connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-SMAConnections.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-SMAConnections.jpg)

You can connect your antennas straight to the u.FL connectors on the modem itself. However, for a more robust connection, you may want to use the included 25mm u.FL cables to connect the modem to the two threaded SMA connections on the Breakout.

The \"VHF\" (Very High Frequency) connection is for the Swarm satellite antenna. Don\'t forget that the Swarm antenna requires a ground plane. There is one included in the box.

The \"GPS\" connection is for the *mandatory* GNSS satellite antenna. The modem will not work correctly unless it is aware of its location and the time, which it gets from GNSS. You can use the included Molex adhesive antenna, or you may prefer to use your own active or passive GNSS antenna. The Molex antenna is designed to be stuck to a window or another electrically-transparent surface. If you stick it to a ground plane or another conductive surface, you will not receive a signal. Peeling it off again is difficult, so please *think before you stick!*

### Power Circuitry

[![Pictured is the Breakout power circuitry](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-PowerCircuitry.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-PowerCircuitry.jpg)

The Breakout includes a dual \"ideal diode\" power mux circuit, allowing the modem to draw power from the USB connector or the VIN breakout pin with \~zero voltage drop. Two large 100 μF capacitors provide the necessary supply rail decoupling.

Please refer to [the schematic](https://cdn.sparkfun.com/assets/1/a/7/c/8/Schematic.pdf) for more details.

### LEDs

[![Pictured are the T X and R X L E Ds](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-LEDs.jpg)

The Breakout has TX and RX LEDs connected to the CH340 signals. These can be disabled if required by cutting the TX and RX jumpers on the bottom of the board.

## Breakout Pins

The table below describes the function of each of the Satellite Transceiver Breakout - Swarm M138 breakout pins:

[![Pictured are the breakout pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-BreakoutPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-BreakoutPins.jpg)

  Pin Name    Function             Description                                         Notes
  ----------- -------------------- --------------------------------------------------- --------------------------------------------------------------------------------------------------
  CH340 RXI   Input                CH340 USB Interface: Receive Data In.               Logic level is **3.3V**.
  TXO         Output               Swarm Serial (UART) Interface: Transmit Data Out.   Logic level is **3.3V**. By default this pin is linked to CH340 RXI. Open the jumper to isolate.
  CH340 TXO   Output               CH340 USB Interface: Transmit Data Out.             Logic level is **3.3V**.
  RXI         Input                Swarm Serial (UART) Interface: Receive Data In.     Logic level is **3.3V**. By default this pin is linked to CH340 TXO. Open the jumper to isolate.
  TX/RX       Output               Swarm TX / RX pin.                                  Logic level is **3.3V**. High during TX, low during RX.
  GPIO1       I/O (Configurable)   Swarm GPIO1 pin.                                    Logic level is **3.3V**. Can be configured in many different ways. See below for more details.
  VIN         Power                Power input.                                        3.0V Min. 5.0V Max.
  GND         Power                Power ground / 0V.                                  

Power can be provided via the USB connector or the VIN pin, or both. The modem will draw power from whichever voltage is higher. The on-board \"ideal diode\" power mux circuit allows both to be connected simultaneously.

The peak current draw during transmit depends on the supply voltage. Please see [Current Draw](https://learn.sparkfun.com/tutorials/satellite-transceiver-breakout---swarm-m138---hookup-guide#current-draw) below for more details.

By default:

- Modem **TXO** is connected to **CH340 RXI**
- Modem **RXI** is connected to **CH340 TXO**

You will need to open the jumper links on the back of the board to use the TXO and RXI pins directly.

[![Pictured are the T X O and R X I jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-BreakoutPinJumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-BreakoutPinJumpers.jpg)

You may find it useful to read this tutorial first:

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

### GPIO1

GPIO1 is a multi-function input/output pin. It can be configured into different modes via the **GP** command:

  Mode   Description
  ------ -----------------------------------------------------------------------------------
  0      Analog, pin is internally disconnected and not used (default)
  1      Analog ADC, pin can be read to measure input voltage (0-3.3V)
  2      Input, pin can be read as a general purpose digital input (High or Low)
  3      Input, low-to-high transition exits sleep mode
  4      Input, high-to-low transition exits sleep mode
  5      Output (Open Drain), set low as a general purpose digital output
  6      Output (Open Drain), set high as a general purpose digital output
  7      Output (Open Drain), low indicates unread messages pending for user
  8      Output (Open Drain), high indicates unread messages pending for user
  9      Output (Open Drain), low indicates unsent messages pending for transmit
  10     Output (Open Drain), high indicates unsent messages pending for transmit
  11     Output (Open Drain), low indicates unread or unsent messages
  12     Output (Open Drain), high indicates unread or unsent messages
  13     Output (Open Drain), low indicates sleep mode is active. Otherwise output is high
  14     Output (Open Drain), high indicates sleep mode is active. Otherwise output is low

We\'ve included both pull-up and pull-down resistors for GPIO1, configurable via a dual split pad jumper. By default, GPIO1 is pulled up to 3.3V so that the open drain output modes generate the correct logic level output. You can remove the pull-up by changing the jumper:

[![Pictured is the schematic for the G P I O 1 pin jumper](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/5/1/Breakout_GPIO1_Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/5/1/Breakout_GPIO1_Jumper.jpg)

GPIO1 can sink a maximum of 8mA.

### TX/RX

TX/RX is a push-pull output which is: high (3.3V) when the modem is transmitting; low (0V) when the modem is receiving or idle.

## Hardware Assembly

Assembling the M138 modem onto the Breakout is very easy:

- Remove the two M2.5 screws from the standoffs
  - We recommend the classic SparkFun reversible [mini-screw driver](https://www.sparkfun.com/products/9146), [MicroMod Screwdriver](https://www.sparkfun.com/products/19012), or the fancier [pocket screw driver set](https://www.sparkfun.com/products/12891) but any #00, #0, or #1 Phillip\'s head driver will work.
- Align the slot of the modem\'s mPCIe connection with the key of the Breakout connector
- Insert the modem at an angle into the connector
- The modem will stick up at a shallow angle
- Gently hold the modem down and secure with the two M2.5 screws

You can connect the Swarm and GNSS antennas directly to the modem:

[![Pictured are the two u dot F L antennas](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-antennae.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-antennae.jpg)

Or you may prefer to use the supplied u.FL cables to connect via the robust SMA connectors:

[![Pictured are the two u dot F L cables](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/6/21218-Swarm-action2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-action2.jpg)

Either way, you may find it useful to read this tutorial first:

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.

The Swarm antenna requires a ground plane for correct operation. That\'s why we included one in the box! Pass the female SMA connector through the hole in the ground plane and secure with the shakeproof washer and nut. Screw the Swarm antenna on top.

[![Pictured are the Swarm antenna and ground plane](https://cdn.sparkfun.com/assets/parts/1/8/8/6/3/19236-Satellite_Transceiver_Breakout_-_Swarm_M138-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/5/1/19236-Satellite_Transceiver_Breakout_-_Swarm_M138-08_HRb.jpg)

[![Pictured are the ground plane dimensions](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/5/1/Ground_Plane_Thumbnail.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/5/1/Ground_Plane.png)

*Having a hard time seeing? Click the image for a closer look.*

The ground plane has both grounded holes (holes with exposed tinned copper surround and through-hole plate) and plain through-holes (isolated). This allows you to connect the ground plane to any surrounding metalwork, or not, depending on your needs.

*For best results, place the VHF antenna and ground plane at least 1m above the ground, or any solid surfaces.*

The exposed finish is standard lead-free Hot Air Solder Levelled (HASL) plating. It will tarnish over time. You may wish to lacquer the board, with standard automotive spray lacquer, for longevity.

If you are using your own cables, check the SMA connector polarity. The Swarm antenna is standard polarity, not \"RP\" (Reverse Polarity):

[![Antenna with standard polarity SMA](https://cdn.sparkfun.com/assets/parts/1/8/8/6/3/19236-Satellite_Transceiver_Breakout_-_Swarm_M138-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/5/1/19236-Satellite_Transceiver_Breakout_-_Swarm_M138-02_HR.jpg)

Both antennas need to be located outdoors, with a clear view of the sky. But **the modem and breakout board are not weatherproof**. Depending on how you are going to weatherproof the boards, and where they are going to be mounted, you may find additional extension cables or GNSS antennas useful.

[![GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/0/14986-GPS_GNSS_Magnetic_Mount_Antenna_SMA_-_3m-01.jpg)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html)

### [GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html) 

[ GPS-14986 ]

This exceptional GPS/GNSS antenna is designed for both GPS and GLONASS reception.

[ [\$16.50] ]

[![Interface Cable - SMA Female to SMA Male (25cm)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/2/9/12861-01.jpg)](https://www.sparkfun.com/interface-cable-sma-female-to-sma-male-25cm.html)

### [Interface Cable - SMA Female to SMA Male (25cm)](https://www.sparkfun.com/interface-cable-sma-female-to-sma-male-25cm.html) 

[ WRL-12861 ]

This is a basic SMA (Sub-Miniature A) male to female connector cable. Each cable is 25cm (9.8\") long and has a 50Ω impedance...

[ [\$5.50] ]

[![Magnetic Mount SMA - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/2/4/1/19576-Action-2.jpg)](https://www.sparkfun.com/magnetic-mount-sma-2m.html)

### [Magnetic Mount SMA - 2m](https://www.sparkfun.com/magnetic-mount-sma-2m.html) 

[ GPS-19576 ]

When experimenting with GPS or RF it can be very handy to have the antenna on the top of your house or car with a clear view ...

[ [\$32.50] ]

[![SMA Male to SMA Female - 10m (RG174)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/5/4/5/17495-SMA_Male_to_SMA_female_RG174_10M-01.jpg)](https://www.sparkfun.com/sma-male-to-sma-female-10m-rg174.html)

### [SMA Male to SMA Female - 10m (RG174)](https://www.sparkfun.com/sma-male-to-sma-female-10m-rg174.html) 

[ CAB-17495 ]

This 10m (33\') SMA extension does a great job of connecting your receiver or radio to a distant antenna with as little RF los...

**Retired**

## Hardware Hookup - USB

Once you\'ve assembled the breakout and connected the antennas, connecting via USB is as simple as plugging in a USB cable!

You can power the board directly from USB-C or USB 3 ports, but not older USB 2.0 ports. Please see [Current Draw](https://learn.sparkfun.com/tutorials/satellite-transceiver-breakout---swarm-m138---hookup-guide#current-draw) below for more details.

Once USB is connected, the LEDs on the modem will indicate its status:

- Green:
  - During the bootup sequence, the green LED will be on solid for 3 seconds.
  - During normal operation after bootup and before shutdown, the green LED will blink 100ms every 5 seconds while the Modem is powered on. This is a "heartbeat" indication that the Modem is working as expected.
- Red:
  - After power is applied until the Modem begins booting, the red LED will be on solid for 10 seconds.
  - After bootup and while the Modem is acquiring a GPS fix, the red LED will flash quickly until a valid GPS fix has been found. Then the red LED will shut off during normal operation.
  - After waking up from sleep, and before a fresh GPS fix has been acquired, there will be a single red LED flash every 5 seconds (following the green LED flash) until a fresh GPS fix has been found. Then the red LED will again shut off during normal operation.
  - During the shutdown sequence, the red LED will be on solid until 3.3V power is removed from the board.
- Blue:
  - The blue LED will be on solid when the Modem is actively receiving from a Swarm satellite.

## Python User Interface

We\'ve written a Python3 PyQt5 GUI (Graphical User Interface) to let you get up and running with the M138 modem. You can find the source code and executables in the [dedicated GUI repo on GitHub](https://github.com/sparkfun/SparkFun_Swarm_M138_GUI).

[![Pictured is the python graphical user interface](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/5/1/Python3_PyQt5_GUI.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/5/1/Python3_PyQt5_GUI.png)

You will find full installation instructions in the repo.

Don\'t panic! The GUI will take a few seconds to open. Select the correct port from the drop-down list, click Open Port and away you go!

Click any of the pre-defined message buttons to send that message to the modem. Or enter your own message in the Message window and click Send Message to send it.

The modem message interface uses the same format as NMEA GNSS messages. They always start with a dollar and end with an asterix and a two character checksum. To make life easy, the GUI adds the \$, \* and checksum characters automatically. You do not need to include those!

The [Modem manual](https://cdn.sparkfun.com/assets/9/1/0/e/3/SwarmM138-Modem-Product-Manual.pdf) contains the full list of modem commands and messages.

You can test the communication interface by pressing the "Configuration Settings (CS)" button. The Modem's Device ID and Name will be displayed on the serial monitor in the format:

    $CS DI=<dev_ID> ,DN=<dev_name>*xx

The next step is to place the device in an outdoor location with a clear view of the sky, away from any sources of RF noise. Once the device is set up outdoors, use the "Receive Test 1Hz (RT 1)" predefined message in the Python3 GUI to measure the background RSSI. The background RSSI measurements will be updated once every second and represent the noise floor in the testing environment. The measured background RSSI value should be between -95 and -105 dBm for reliable communication on the network. A lower, more negative, value is preferred.

*The Modem will not be able to reliably communicate with the satellites if the reported background RSSI value is \> -93 dBm. Try moving the device to a different testing location to observe how the measured value changes.*

After confirming that the background RSSI is within the specified range, the next step is to queue some message packets on the Modem for transmission. The quickest way to queue messages for transmission is to use the predefined messages in the GUI shown at the bottom of the list. The message packets will be queued for transmission for a default hold time of 48 hours after which they will be discarded if not transmitted.

*The message packet hold time is user configurable for each transmission command. Please refer to the Swarm M138 Modem's [Product Manual](https://swarm.space/swarm-m138-modem-product-manual/) for more information, and for a full description of available commands.*

The queued transmission packets will be transmitted when a satellite passes over the device's location and beacons the Modem. The next satellite pass over your location can be predicted using the [Swarm Satellite Pass Checker](https://kube.tools.swarm.space/pass-checker/). There is also a YouTube video available that describes the pass checker's functionality in more detail available [here](https://www.youtube.com/watch?v=j8PceIrZ9Js).

To know if a satellite is attempting to communicate with the Modem, ensure that the "Receive Test 1Hz (RT 1)" command is enabled. Observe the serial monitor for satellite beacons in the format:

    $RT RSSI=<rssi_sat>,SNR=<snr>,FDEV=<fdev>,TS=<time>,DI=<sat_id>*xx 

The Modem will attempt to transmit queued message packets after receiving the satellite beacons. Each successful transmission will be acknowledged by the satellite and will be displayed on the serial monitor in the format:

    $TD SENT RSSI=<rssi_sat>,SNR=<snr>,FDEV=<fdev>,<msg_id>*xx

The transmitted data packet will then be visible on the [Swarm Hive](https://bumblebee.hive.swarm.space/login) shortly after transmission.

## Hardware Hookup - Breakout Pins

Want to connect the Breakout to your Arduino microcontroller board? You can absolutely do that too!

By default:

- The modem **TXO** breakout pin is connected to the **CH340 RXI** via a split pad jumper
- Likewise, the modem **RXI** is connected to **CH340 TXO**

You will need to open the jumper links on the back of the board when connecting the TXO and RXI pins to an Arduino board.

[![Pictured are the T X O and R X I jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-BreakoutPinJumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/6/21218-Swarm-BreakoutPinJumpers.jpg)

You will probably need: break away headers and jumper wires. 2-pin jumpers will be useful for re-linking the CH340 connections later.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Jumper Wires Premium 6\" M/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/5/7/09140-02-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html)

### [Jumper Wires Premium 6\" M/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html) 

[ PRT-09140 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumper wires terminated as male to female. Use these to jumper fro...

[ [\$4.60] ]

[![Jumper - 2 Pin](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/0/7/09044-02-L.jpg)](https://www.sparkfun.com/jumper-2-pin.html)

### [Jumper - 2 Pin](https://www.sparkfun.com/jumper-2-pin.html) 

[ PRT-09044 ]

These are two pin jumpers (also called shunts) that will create an electrical connection between two pin headers. Commonly us...

[ [\$0.50] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

[![Jumper Wires Premium 12\" F/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/9/1/09389-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-12-f-f-pack-of-10.html)

### [Jumper Wires Premium 12\" F/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-12-f-f-pack-of-10.html) 

[ PRT-09389 ]

This is a SparkFun exclusive! These are 12\" long, 26 AWG jumper wires terminated as female to female. Use these to jumper fro...

[ [\$4.95] ]

[![Straight Header - Female (PTH, 0.1in., 8-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/9/8/11895-01.jpg)](https://www.sparkfun.com/header-8-pin-female-pth-0-1.html)

### [Straight Header - Female (PTH, 0.1in., 8-Pin)](https://www.sparkfun.com/header-8-pin-female-pth-0-1.html) 

[ PRT-11895 ]

These are standard 0.1\" spaced header pins that can be through-hole mounted. This header connects perfectly with most 8-pin m...

[ [\$0.80] ]

Connect:

- GND to GND / 0V on your Arduino board
- VIN to 5V on your Arduino board
  - It is possible to connect VIN to 3.3V ***if*** your Arduino board can deliver enough current when the modem transmits
  - Please see [Current Draw](https://learn.sparkfun.com/tutorials/satellite-transceiver-breakout---swarm-m138---hookup-guide#current-draw) below for more details.
- TXO to the Serial / UART RX input on your Arduino board
- RXI to the Serial / UART TX output on your Arduino board

The TXO and RXI signals are 3.3V.

If you are using an old Arduino Uno or similar with 5V I/O pins, you will need to use a [logic level converter](https://www.sparkfun.com/products/12009) to convert the signals to 3.3V.

## Software Setup

Our [Swarm Arduino Library](https://github.com/sparkfun/SparkFun_Swarm_Satellite_Arduino_Library) makes it easy to get up and running with Swarm.

If you are new to Arduino and the IDE, this guide will get you up and running:

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

If you haven\'t installed an Arduino Library before, this is the guide you need:

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

- [Install the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- Click on ***Tools\\Manage Libraries\...*** to open the library manager
- In the search box, type ***SparkFun Swarm***
- Click the *Install* button to install the library

Alternatively, you can grab the library directly from [GitHub](https://github.com/sparkfun/SparkFun_Swarm_Satellite_Arduino_Library) or can download it as a zip file by clicking the button below:

[SparkFun Swarm Satellite Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Swarm_Satellite_Arduino_Library/archive/refs/heads/main.zip)

## Arduino Example: Get Firmware Version

The [SparkFun Swarm Satellite Arduino Library](https://github.com/sparkfun/SparkFun_Swarm_Satellite_Arduino_Library) contains a full set of [tried and tested examples](https://github.com/sparkfun/SparkFun_Swarm_Satellite_Arduino_Library/tree/main/examples) which will run on almost all Arduino boards (RAM permitting).

The code below is a stripped-down version of [Example3_getFirmwareVersion](https://github.com/sparkfun/SparkFun_Swarm_Satellite_Arduino_Library/blob/main/examples/Example3_getFirmwareVersion/Example3_getFirmwareVersion.ino). Copy and paste the code into a new window in the Arduino IDE:

    language:c
    #include <SparkFun_Swarm_Satellite_Arduino_Library.h> // http://librarymanager/All#SparkFun_Swarm_Satellite

    SWARM_M138 mySwarm;

    #define swarmSerial Serial1 // Use Serial1 to communicate with the modem. Change this if required.

    void setup()
    

      char *firmwareVersion = new char[SWARM_M138_MEM_ALLOC_FV]; // Create storage for the configuration settings

      mySwarm.getFirmwareVersion(firmwareVersion); // Get the firmware version

      Serial.print(F("The firmware version is: "));
      Serial.println(firmwareVersion);

      delete[] firmwareVersion; // Free the storage
    }

    void loop()
    

Save the file and click on the Upload button to upload the example onto your board.

Open ***Tools\\Serial Monitor*** to see the modem firmware version.

Check that the baud rate is set to **115200**.

## Message Transmit, Receive and Pass-Prediction

Message transmit via Swarm is a little different to (e.g.) the Iridium satellite network.

The Swarm satellite constellation is increasing rapidly, but is not yet complete. There may be times when there are no satellites overhead to receive your message. If you queue a message for transmission during one of these times, the message is stored in the modem and transmitted during the next satellite pass. If you monitor the responses in the GUI or via the Arduino Library examples, you will see a **\$TD SENT** notification when each message is transmitted. You can monitor how many unsent messages are still in the queue via the **\$MT C=U** message.

There are two ways to predict the next satellite pass:

- Via the online [Swarm Pass Checker](https://kube.tools.swarm.space/pass-checker/)
- Or by using the pass prediction examples in our [Arduino Library](https://github.com/sparkfun/SparkFun_Swarm_Satellite_Arduino_Library/tree/main/examples/Pass_Prediction)
  - The pass prediction code downloads the Swarm Two Line Element orbit parameters from [CelesTrak](https://celestrak.org/)
  - Cross-checks these with the Swarm Pass Checker
  - Produces a list of known \'good\' satellites for your location
  - The TLE orbit parameters are stored on microSD card for use offline (once downloaded, you do not need an Internet connection to perform a prediction)
  - If you want to, you could send updated TLEs to your remote Swarm-enabled equipment, *via Swarm message*, so it can refine its pass predictions!
  - The pass prediction examples were written for the [SparkFun Thing Plus C - ESP32 WROOM](https://www.sparkfun.com/products/18018): they use the ESP32\'s WiFi connection and the on-board microSD socket to store the TLE data
  - You can adapt the examples to work on other WiFi and microSD capable boards, such as the: [SparkFun MicroMod ESP32 Processor](https://www.sparkfun.com/products/16781); and the [SparkFun MicroMod Data Logging Carrier Board](https://www.sparkfun.com/products/16829)

Message receive via Swarm is significantly different to (e.g.) the Iridium satellite network.

\"Mobile Terminated\" messages are queued in the ground station and are passed to a satellite that is known to be passing over your modem\'s location. As a result, this can take tens of minutes, or hours in some circumstances, depending on your location and the timing of the satellite orbits. The message reception interval will decrease as the Swarm constellation increases.

If you are expecting to receive a message, make sure you have the Messages Received notifications enabled, via the **\$MM N=E** message. That way you will receive a notification as soon as the message arrives. Alternatively, you can poll how many unread messages are in the modem\'s buffer using the **\$MM C=U** message.

## Current Draw

The peak current drawn by the modem, during message transmit, depends on the supply voltage:

  Supply Voltage   Sleep Current   Receive Current            Transmit Current
  ---------------- --------------- -------------------------- ---------------------------------
  3.3V             80µA (Peak)     26mA (Typ.), 40mA (Peak)   850mA (Typ.), **1000mA (Peak)**
  5.0V             110µA (Peak)    25mA (Typ.), 45mA (Peak)   550mA (Typ.), **600mA (Peak)**

We strongly recommend powering the Breakout from 5.0V to reduce the peak current draw.

The TXO, RXI, TX/RX and GPIO1 signals remain 3.3V even when VIN is 5.0V. It is not possible to use 5.0V I/O under any circumstances. Doing so may damage your modem.

You can power the board directly from USB-C or USB 3 ports, but not older USB 2.0 ports. USB 2.0 (non-SuperSpeed) ports are limited to 500mA. You can still use our Breakout with USB 2.0, but you will need to connect additional power via the VIN and GND breakout pins.

On Raspberry Pi boards, the USB sockets are powered directly by the (USB) Power In connector. You can connect the Swarm Breakout to Raspberry Pi using USB provided that your power supply can deliver enough current for both the RPi and the Swarm M138 (during transmit). The official Raspberry Pi 5.1V 2.5A (12.5W) power adapter is a good choice.

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)