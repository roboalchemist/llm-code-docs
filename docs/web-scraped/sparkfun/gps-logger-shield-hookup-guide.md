# Source: https://learn.sparkfun.com/tutorials/gps-logger-shield-hookup-guide

## Introduction

The [SparkFun GPS Logger Shield](https://www.sparkfun.com/products/13750) equips your Arduino with access to a GPS module, µSD memory card socket, and all of the other peripherals you\'ll need to turn your Arduino into a position-tracking, speed-monitoring, altitude-observing wonder logger.

[![GPS Logger Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-action-shot-01.jpg)](https://www.sparkfun.com/products/13750)

The shield is based around a [GP3906-TLP GPS Module](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/GP3906-TLP_DataSheet_Rev_A01.pdf) \-- a 66-channel GPS receiver featuring a MediaTek MT3339 architecture and an up to 10Hz update rate. The GPS module will stream constant position updates over a simple [serial UART](https://learn.sparkfun.com/tutorials/serial-communication), which you can then log to a [µSD card](https://www.sparkfun.com/products/11609) and/or use for other position or time-tracking purposes.

Everything on the shield is highly configurable: A switch allows you to select the GPS module\'s UART interface between either hardware or software ports, the µSD card operates over a hardware SPI port, which should be compatible with most Arduino layouts, and extra prototyping space should allow you to add those last, few components you need to complete your project.

### Covered In This Tutorial

This tutorial aims to document all things GPS Logger Shield related, including both the hardware and software required to get it up-and-running. It\'s split into the following sections:

- **[Hardware Overview](https://learn.sparkfun.com/tutorials/gps-logger-shield-hookup-guide#hardware-overview)** \-- An overview of the schematic, layout, and features of the SparkFun GPS Logger Shield.
- **[Hardware Setup](https://learn.sparkfun.com/tutorials/gps-logger-shield-hookup-guide#hardware-setup)** \-- Tip for assembling the GPS Logger Shield to best match your project needs.
- **Example Arduino Sketches**
  - **[GPS Serial Passthrough](https://learn.sparkfun.com/tutorials/gps-logger-shield-hookup-guide#example-sketch-gps-serial-passthrough)** \-- A simple sketch you can use to verify functionality of your GPS Logger Shield, and get an idea of what kind of data the GP3906 GPS module produces.
  - **[TinyGPS++ Serial Streaming](https://learn.sparkfun.com/tutorials/gps-logger-shield-hookup-guide#example-sketch-tinygps-serial-streaming)** \-- Using the TinyGPS++ Arduino library to parse the GPS module\'s NMEA strings into latitude, longitude, altitude, speed, and more.
  - **[µSD Card GPS Logging](https://learn.sparkfun.com/tutorials/gps-logger-shield-hookup-guide#example-sketch-sd-card-gps-logging)** \-- Finally, we\'ll plug the parsed GPS data into a CSV file and save it to a µSD card.

### Suggested Materials

There are a few extra components you\'ll need to get the GPS Logger Shield fully up-and-running:

Most importantly, you\'ll need an **Arduino or Arduino-compatible development board**. The GPS\'s serial and µSD SPI ports should be compatible with almost all Arduino-sized development boards. That includes classics, like the [Arduino Uno](https://www.sparkfun.com/products/11021) and [SparkFun RedBoard](https://www.sparkfun.com/products/12757), and newer models, like the [Arduino Leonardo](https://www.sparkfun.com/products/11286), [Genuino 101](https://www.sparkfun.com/products/13788), and [SparkFun SAMD21 Dev Breakout](https://www.sparkfun.com/products/13672).

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![SparkFun SAMD21 Dev Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/1/5/13672-01.jpg)](https://www.sparkfun.com/sparkfun-samd21-dev-breakout.html)

### [SparkFun SAMD21 Dev Breakout](https://www.sparkfun.com/sparkfun-samd21-dev-breakout.html) 

[ DEV-13672 ]

If you're ready to step your Arduino game up from older 8-bit/16MHz microcontrollers, the SparkFun SAMD21 Dev Breakout is a...

[ [\$29.95] ]

[ ![Arduino Leonardo with Headers](https://cdn.sparkfun.com/r/140-140/assets/parts/6/9/5/3/11286-01a.jpg) ]

### Arduino Leonardo with Headers 

[ DEV-11286 ]

Arduino is an open-source physical computing platform based on a simple i/o board and a development environment that implemen...

**Retired**

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/9/5/1/8/12757-01.jpg)](https://www.sparkfun.com/products/12757)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/products/12757) 

[ DEV-12757 ]

At SparkFun we use many Arduinos and we\'re always looking for the simplest, most stable one. Each board is a bit different an...

**Retired**

We also **highly recommend a [12mm Coin Cell Battery](https://www.sparkfun.com/products/337)**, which fits into the GPS Shield\'s battery holder. The GP3906 GPS module requires some sort of voltage on its battery supply input. If you don\'t have a battery, make sure you read the [VBAT section](https://learn.sparkfun.com/tutorials/gps-logger-shield-hookup-guide#GP3906-VBAT) of the hardware overview carefully.

[![Coin Cell Battery - 12mm (CR1225)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/6/3/00337-01.jpg)](https://www.sparkfun.com/coin-cell-battery-12mm-cr1225.html)

### [Coin Cell Battery - 12mm (CR1225)](https://www.sparkfun.com/coin-cell-battery-12mm-cr1225.html) 

[ PRT-00337 ]

CR1225 lithium metal 3V 12mm 47mAh coin cell batteries. Perfect small battery for miniature sensor node applications. Thes...

[ [\$2.25] ]

You\'ll also need to **solder some headers** into the shield, to create a solid mechanical and electrical connection between it and the Arduino. We recommend the [Arduino R3 Stackable Header Pack](https://www.sparkfun.com/products/11417), but a set of [male headers](https://www.sparkfun.com/products/116) may also suit your needs.

[![Arduino Stackable Header Kit - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/7/2/1/6/11417-01a.jpg)](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html)

### [Arduino Stackable Header Kit - R3](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html) 

[ PRT-11417 ]

These headers are made to work with the Arduino Uno R3, Leonardo and new Arduino boards going forward. They are the perfect h...

[ [\$2.75] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

[![MicroSD Card with Adapter - 8GB](https://cdn.sparkfun.com/r/140-140/assets/parts/7/6/3/6/11609-02a.jpg)](https://www.sparkfun.com/products/11609)

### [MicroSD Card with Adapter - 8GB](https://www.sparkfun.com/products/11609) 

[ COM-11609 ]

This is an 8 gig microSD memory card. It\'s perfect for massive datalogging without taking up a lot of space. These microSD ca...

**Retired**

Finally, if you intend on logging the GPS data to a µSD card, you may want to grab a [µSD Card and SD Adapter](https://www.sparkfun.com/products/11609). The Arduino SD library should support most µSD cards formatted with FAT16 or FAT32 file systems.

### Suggested Reading

This is a beginner-level tutorial \-- and the GPS Logger Shield is a beginner-friendly product \-- but there are a few concepts you should be comfortable with before continuing on. If any of these subjects sound unfamiliar, considering reading those tutorials before continuing on.

- [GPS Basics](https://learn.sparkfun.com/tutorials/gps-basics) \-- This tutorial is a great primer on the wonders of GPS. Learn how we get find our position on the globe by listening to (at least) four satellites send a timestamp and aerial position.
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication) \-- The GP3906 communicates via a simple, serial UART. This tutorial will familiarize you with serial-related concepts like RX, TX, and baud rate.
- [How to Solder: Through-Hole Soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) \-- If you\'ve never soldered before, now\'s a great time to start, and this is a great tutorial to learn from.
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) \-- We\'ll use a pair of fantastic Arduino libraries to log GPS data to an SD card.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

## Hardware Overview

For a quick overview of the components and features of the GPS Logger Shield, refer to the image below:

[![Annotated GPS Shield image](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/hardware-annotated-gps-shield-top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/hardware-annotated-gps-shield-top.jpg)

The rest of this section will dive into some of the more critical components of the shield, including power supply requirements and UART and SPI interface configurations.

### [] Powering the GPS Logger Shield

The GPS Logger Shield\'s main voltage supply is taken from the **Arduino 5V** header pin. This voltage is regulated down to 3.3V, which is supplied to both the GPS module and the µSD card.

These two components should consume around 30mA on average, but they may very occasionally spike to upwards of 100mA.

#### Logic-Level Shifting

The shield includes a [TXB0108 8-Channel Level Shifter](https://www.sparkfun.com/products/11771), which shifts voltage levels between the Arduino and 3.3V GPS UART and µSD SPI signals. Regardless of whether your Arduino runs at 5V or 3.3V, you shouldn\'t have to concern yourself with shifting voltages between either component.

The Arduino-side logic-level voltage is set by the **IOREF pin**, which most Arduino development boards connect to either 5V or 3.3V.

**⚡ If your Arduino board doesn\'t have an IOREF pin**, or if no voltage is supplied on that pin, you will need to set the IOREF voltage manually. The shield includes a jumper on the back-side of the board, labeled **IOREF-SEL**, which you can use to set the IOREF voltage to either 3.3V or 5V.

[![](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/hardware-ioref-jumper-03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/hardware-ioref-jumper-03.png)

If your Arduino board doesn\'t have an IOREF pin, set this jumper to match your desired logic level.

#### [] GP3906 Battery Supply (VBAT)

The GP3906 is a great, little module, but it has one, big quirk: A **supply voltage between 2.0-4.3V is required** on the VBAT pin. If you have a [12mm coin cell battery](https://www.sparkfun.com/products/337), supplying that voltage is as easy as pushing it into the battery socket. When you insert the battery, make sure you slot it in ***+* side facing up**.

[![Plugging battery into the GPS Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-battery-plug.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-battery-plug.jpg)

If you don\'t have a battery handy, there are a few workarounds. You can grab a soldering iron, and **short the 3V3-Batt jumper**, next to the battery socket.

[![Batt/3V3 jumper closed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-battery-jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-battery-jumper.jpg)

*If you don\'t have a 12mm battery, shorting the 3V3/Batt jumper will at least keep your GPS module functional.*

Or you can wire the broken out **VBAT pin** to any voltage supply between 2.0-4.3V.

**⚡ VBAT Supply Required:** The GP3906 requires some form of voltage supply on its VBAT pin, whether that be an actual battery, or simply the 3.3V regulator output. If your the GPS LED isn\'t at least blinking (or illuminated) when the shield is powered up, that may indicate lack of supply to the VBAT port (or a dead battery).

Supplying the GP3906 with a backup battery supply ensures that its real-time clock (RTC) will continue to tick, even when the rest of the board is powered off. That allows the module to get faster GPS fixes when it initially powers up. It doesn\'t consume a lot of power \-- we\'ve measured around 5-6µA, \-- so a 12mm coin cell battery could keep the board \"running\" (in sleep mode) for about a year.

### GPS Pin Breakout\'s

Most of the GPS input, output, and power pins are connected to *something* on the GPS Logger Shield, but they\'re all also broken out to this 8-pin header.

[![GPS Pin breakout\'s highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/hardware-gps-breakout.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/hardware-gps-breakout.jpg)

Here\'s a quick overview of each pin and its function:

  Pin Label   In/Out   Board Connection          Pin Description
  ----------- -------- ------------------------- --------------------------------------------------------------------
  GND         In       Ground                    GPS module ground (0V reference)
  PPS         Out                                1 pulse-per-second time reference
  EN          In                                 Active-high chip-enable -- pull low to reset or turn off
  RX          In       Arduino TX/D9             Serial data input
  TX          Out      Arduino RX/D8             Serial data output
  FIX         Out      GPS Fix LED               GPS fix indicator -- blinks before a fix, HIGH once a fix is valid
  VBAT        In       12mm coin cell socket     Backup power -- keeps the RTC running (2.0-4.3V input range)
  3V3         In       On-board 3.3V regulator   3.3V power supply input

The **PPS** and **EN** pins are left unconnected. You\'re free to wire them up to any Arduino pin should you need either a pulse-per-second signal, or extra control of the GPS module\'s operation.

### Selecting the Serial Port

The GPS module communicates via a simple, UART (serial) interface. The **UART-select switch** allows you to switch that interface between either the Arduino\'s hardware UART \-- on pins D0 and D1 \-- or a [SoftwareSerial](https://www.arduino.cc/en/Reference/SoftwareSerial) port on pins D8 and D9.

[![UART-select switch](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/hardware-uart-switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/hardware-uart-switch.jpg)

Should you need a reference, this table shows the map between GPS module and Arduino UART(s):

  GPS Pin   Arduino Software UART Pin   Arduino Hardware UART Pin
  --------- --------------------------- ---------------------------
  RX        9                           1 (TX)
  TX        8                           0 (RX)

If you\'re using an Arduino Uno or any development board with one, pre-occupied hardware UART, you may be forced to use the software serial port. Fortunately, the GPS module\'s baud rate defaults to a slow, steady **9600 bps**, which SoftwareSerial shouldn\'t have a problem handling.

If you need to move the software serial port pins, they can be custom-routed to any other pin by **cutting the solder jumpers** between pins GPS-RX and D8 and/or GPS-TX and D9.

[![Software UART-select jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/GPS_SoftwareSerialJumpers2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/GPS_SoftwareSerialJumpers2.jpg)

Once those jumpers are cut, you can wire the GPS-RX and GPS-TX pins to any other pins you\'d like.

### Selecting the µSD SPI Pins

On older Arduino boards, finding the SPI port was pretty simple \-- it\'d be on pins 10-13, mapping out to CS, MOSI, MISO, and SCLK respectively. On more recent Arduino board releases, however, these pins are just as likely to be found on *only* the 6-pin, 2x3 SPI header. The GPS Logger Shield maps the µSD SPI pins to both of these headers, in order to support as many development boards as possible.

A trio of three-way solder jumpers can be used to modify which Arduino pins are routed to the µSD card\'s SPI I/O\'s.

[![SPI-select jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/GPS_SPIJumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/GPS_SPIJumpers.jpg)

The middle pad of these jumpers carries the signal to/from the µSD card. The pads toward the inside of the board carry signals to the SPI header, and the pads toward the outside carry signals to pins 10-13.

**Boards that map SPI to pins 10-13** include the Arduino Uno, RedBoard, Arduino Pro\'s, and most ATmega328P-based boards. If you\'re using any of these boards, it should be safe to leave the jumper\'s untouched (as they\'re also, likely, shorted together on the Arduino).

**Boards that *only* map SPI to the 2x3 SPI header** include the Arduino Leonardo (and other most ATmega32U4-based boards), Arduino Due, and the Arduino Zero (and most ATSAMD21-based boards). On these boards, you\'ll need to cut the solder jumpers connecting the middle pad to the D11-, D12-, and D13-side pads. The µSD_CS connected to pin D10 can be defined on any pin so it does not have to be modified.\
\
Check below for more information about the \*\*µSD SPI Jumpers\*\*.

### Power and GPS Fix Status LEDs

This pair of LEDs on the corner of the shield are a handy tool for initial troubleshooting. The **red PWR** LED is attached to the output of the shield\'s on-board 3.3V regulator. If the shield is getting power, this LED should be on.

The **blue GPS FIX** LED is connected the GP3906\'s \"3D_FIX\" pin. It can be used to identify whether the GPS module has a proper fix or not. When you initially power the shield up, the LED should blink \-- indicating it\'s trying to find a fix. Once the LED turns solidly on, you can rest assured that your GPS module has a good fix on your location.

[![3D Fix pin operation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-fix-led-datasheet.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-fix-led-datasheet.png)

*The GP3906\'s 3D_Fix pin operation. The LED will be on when the GPS fix is valid, and blinking at 1/2 Hz otherwise.*

Both of these LEDs have **solder jumpers** underneath, should you find the need to disable either of them. A quick slice between the pads is all it takes to remove them from the circuit. This might be useful if you\'re using the GPS Logger Shield in a low-power application, where even the handful of milliamps consumed by the LEDs means months off a project\'s battery lifetime.

## Hardware Setup

Assembly of the GPS Logger Shield mostly comes down to soldering *something* to all of the 6, 8, and 10-pin Arduino headers. We usually recommend [Arduino R3 Stackable Headers](https://www.sparkfun.com/products/11417) for this job, but [male headers](https://www.sparkfun.com/products/116) can work \-- as long as this is the top board in a shield stack.

[![Stackable headers soldered into the shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-headers-soldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-headers-soldered.jpg)

If your application requires use of the **6-pin, 2x3 SPI header**, you may also want to solder [female headers](https://www.sparkfun.com/products/115) to those pins (make sure they\'re pointing down, and slot easily into your Arduino\'s male SPI pins).

If you\'ve never soldered an Arduino shield before, check out our [Arduino Shield Assembly tutorial](https://learn.sparkfun.com/tutorials/arduino-shields-v2#installing-headers-preparation) for some tips.

### Pre-Flight Checklist

Before you get the go-ahead for GPS Shield\'ing, make sure you double-check these common pitfalls one last time:

#### Battery (VBAT) Power Supply

Make sure you have a reliable power source supplying the GPS module\'s VBAT pin. If you have a shiny, new [12mm coin cell battery](https://www.sparkfun.com/products/337) plugged in, that\'s perfect. Otherwise, make sure you\'ve either shorted the 3.3V/VBAT jumper, or are supplying something to the GPS module\'s *VBAT* breakout.

[![Battery plugged in](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-battery-in.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-battery-in.jpg)

#### UART Selected

Make sure you have the UART-select switch pointing towards your preferred UART. If you\'re using an **Uno, Redboard, or any other ATmega328P-based Arduino**, you\'ll most likely need to have the switch pointing towards **SW-UART**, assuming the hardware UART is used for programming and serial debugging.

If you\'re using an ATmega328-based Arduino, no matter what your sketch ends up doing, **the switch must be in the SW-UART position during any programming upload**.

If you\'re using a **Leonardo** (ATmega32U4-based boards), **Zero** (ATSAMD21-based boards), or any other Arduino that has a dedicated and free hardware UART on pins 0/1, we recommend leaving the switch in the **HW-UART** position.

#### µSD SPI Jumpers

Planning on logging data to a µSD card? Make sure the SPI jumpers are set accordingly. If you\'re using an Uno, Redboard, or any other ATmega328P-based Arduino, you can probably leave the jumpers untouched. SPI should be broken out to *both* pins 10-13 and the SPI header anyway.

If you\'re using a **Leonardo** (ATmega32U4-based boards), **Zero** (ATSAMD21-based boards), or any other Arduino that doesn\'t break the SPI signals to pins 10-13, you\'ll want to **cut the three SPI-select jumpers** between the middle pad and the D11-D13 pins. That will free up those pins for other purposes in your project. The µSD_CS connected to pin D10 can be defined on any pin so it does not have to be modified.

[![SPI jumpers cut for Leonardo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-spi-headers-cut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-spi-headers-cut.jpg)

*Looking closely, you\'ll see traces cut on all three SPI lines between the middle pad and D11, D12, and D13. That disconnects the µSD lines from those pins \-- leaving them connected to the SPI header.*

If you\'re relying on the SPI port from the 2x3-pin ICSP header, don\'t forget to solder headers to the SPI port!

## Software Serial and SPI On Other Microcontrollers

### Software Serial

The demo code was originally designed for the ATmega328P on the Arduino Uno. If you were using it with ATmega2560 (i.e. Arduino Mega 2560) or ATmega32U4 (i.e. Arduino Leonardo, Pro Micro 5V/16MHz, Pro Micro 3.3V/8Mhz, FioV3, etc.), you would need to re-configure the software serial pin definitions and adjust the connections. Not all the pins can support change interrupts for a serial Rx pin depending on what Arduino microcontroller is used. You will need to redefine pin definitions and reroute the connection.

For more information about the limitations, try looking at the Arduino reference language for the Software Serial library.

[Arduino Software Serial Library](https://www.arduino.cc/en/Reference/SoftwareSerial)

#### Redefining for Software Serial Pins

To use the GPS logger shield on an Arduino Mega 2560, you would just need to adjust the software serial pin definitions in the code where it says:

    language:c
    #define ARDUINO_GPS_RX 9 // Arduino RX pin connected to GPS TX
    #define ARDUINO_GPS_TX 8 // Arduino TX pin connected to GPS RX

Let\'s change the software serial pins by using the analog pins A9 and A8, respectively.

    language:c
    #define ARDUINO_GPS_RX A9 // Arduino RX pin connected to GPS TX
    #define ARDUINO_GPS_TX A8 // Arduino TX pin connected to GPS RX

#### Rerouting for Software Serial Pins

Once you adjust the code, make sure to rewire your connections. Cut across the trace between the plated through holes using a [hobby knife](https://www.sparkfun.com/products/9200). There is a red solder mask above the trace so make sure that the trace is completely cut.

[![Software UART-select jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/GPS_SoftwareSerialJumpers2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/GPS_SoftwareSerialJumpers2.jpg)

Once the trace has been cut, solder header pins or wires to the plated through holes. To easily switch between different development boards, female headers were added.

[![Female Headers Added to Software Serial and SPI Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/GPSLoggerShieldAltSerialPins_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/GPSLoggerShieldAltSerialPins_1.png)

Once soldered, two [male to male jumper wires](https://www.sparkfun.com/products/8431) were added to the through hole pins closest to GPS-Rx and GPS-Tx. With the rewired connects, GPS-Tx was rerouted to pin A9 and GPS-Rx was rerouted to pin A8. While not necessary, the yellow jumper wire was added to easily reroute the SPI\'s CS pin to another I/O with the data logging example.

[![Software Serial Pins Rerouted with Jumper Wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/SoftwareSerial_Reroutedwith_JumperWires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/SoftwareSerial_Reroutedwith_JumperWires.jpg)

### SPI

The demo code was originally designed for the ATmega328P on the Arduino Uno. You would only need to worry about adjusting the SPI pins if you were using the *CSV_Logger_TinyGPSPlus.ino* logging example. Just like software serial, you would need to reroute the connection.

For more information about the limitations, try looking at the reference language for the SPI library.

[Arduino SPI Library](https://www.arduino.cc/en/Reference/SPI)

#### Rerouting for SPI Pins

To use the GPS Logger Shield on the Arduino Mega 2560, you would just need to reroute the SPI pins. Using a hobby knife, cut the trace between the center and right pads for MOSI, MISO, and SCK.

[![SPI jumpers cut for Leonardo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-spi-headers-cut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-spi-headers-cut.jpg)

*Looking closely, you\'ll see traces cut on all three SPI lines between the middle pad and D11, D12, and D13. That disconnects the µSD lines from those pins \-- leaving them connected to the SPI header.*

Once cut you have the option of soldering one 2x3 female header or two 1x3 stackable headers to the ICSP pins.

[![Stackable Header - Female (PTH, 0.1in., 3-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/2/7/13875-02.jpg)](https://www.sparkfun.com/stackable-header-3-pin-female-0-1.html)

### [Stackable Header - Female (PTH, 0.1in., 3-Pin)](https://www.sparkfun.com/stackable-header-3-pin-female-0-1.html) 

[ PRT-13875 ]

This is a simple 3 pin female PTH header. This header is in a configuration that makes it ideal to be used with the \[MyoWare ...

[ [\$0.95] ]

[![Straight Header - Female (PTH, 0.1in., 2x3-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/2/1/13010-01a.jpg)](https://www.sparkfun.com/header-2x3-female-0-1.html)

### [Straight Header - Female (PTH, 0.1in., 2x3-Pin)](https://www.sparkfun.com/header-2x3-female-0-1.html) 

[ PRT-13010 ]

This is a simple 2x3 female PTH header.

[ [\$0.50] ]

Make sure to solder from the top side of the shield so that the female header pins face down toward the Arduino\'s ICSP pins.

[![ICSP Pins Soldered to Shield Facing Down Toward the Arduino\'s Male ICSP Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/GPSLoggerICSPHeader_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/GPSLoggerICSPHeader_1.png)

Once the headers are soldered, stack it on the Arduino Mega 2560 and reroute the software serial pins. The CS pin can be cut and rerouted to another pin on the microcontroller. However, the default trace on pin 10 will still work.

[![Software Serial Pins Rerouted with Jumper Wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/SoftwareSerial_Reroutedwith_JumperWires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/SoftwareSerial_Reroutedwith_JumperWires.jpg)

## Example Sketch: GPS Serial Passthrough

Now that your hardware is all set up, we have three pieces of example code to give you a taste of the GPS Logger Shield\'s functionality. This first example isn\'t all that useful, but it will, at least, make sure everything\'s working. Plus it\'ll show you the raw ugliness of [NMEA GPS strings](https://learn.sparkfun.com/tutorials/gps-basics#message-formats) and make you appreciate great libraries like [TinyGPS](http://arduiniana.org/libraries/tinygps/) even more.

This example doesn\'t require any additional libraries. Simply plug the shield into your Arduino and upload the example code. We\'ve got a couple examples, depending on which Arduino and/or serial port you\'re using.

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### SoftwareSerial Port Example

If you\'re using an Arduino Uno, Redboard, any other ATmega328P-based Arduino, and have the UART-select switch in the **SW-UART** position, upload this piece of example code to your Arduino:

    language:c
        /******************************************************************************
    Basic_Passthrough_Software.ino
    Basic Software Serial GPS Passthrough
    By Jim Lindblom @ SparkFun Electronics
    February 9, 2016
    https://github.com/sparkfun/GPS_Shield

    This example uses SoftwareSerial to communicate with the GPS module on
    pins 8 and 9. SoftwareSerial should work on most Arduinos, but it's a
    necessity on Arduino Uno's, RedBoard's and any other Arduino
    based around an ATmega328P.

    After uploading the code, open your serial monitor, set it to 9600 baud, and
    watch the GPS module's NMEA strings begin to flow by. See if you can pick
    out the latitude and longitude.

    Resources:
    SoftwareSerial Library (included with Arduino)

    Development/hardware environment specifics:
    Arduino IDE 1.6.7
    GPS Logger Shield v2.0 - Make sure the UART switch is set to SW-UART
    Arduino Uno, RedBoard, Pro, etc.
    ******************************************************************************/

    #include <SoftwareSerial.h> // Include the SoftwareSerial library
    #define ARDUINO_GPS_RX 9 // Arduino RX pin connected to GPS TX
    #define ARDUINO_GPS_TX 8 // Arduino TX pin connected to GPS RX
    #define GPS_BAUD_RATE 9600 // The GPS Shield module defaults to 9600 baud
    // Create a SoftwareSerial object called gps:
    SoftwareSerial gpsPort(ARDUINO_GPS_TX, ARDUINO_GPS_RX);

    // We'll also define a more descriptive moniker for the Serial Monitor port.
    // This is the hardware serial port on pins 0/1.
    #define SerialMonitor Serial

    void setup() 
    

    void loop() 
    

Copy and paste the above code into your Arduino IDE. You can also download all of the example sketches from our GitHub repository.

[Download GPS Shield Examples](https://github.com/sparkfun/GPS_Shield/archive/master.zip)

This example uses the [SoftwareSerial](https://www.arduino.cc/en/Reference/SoftwareSerial) library to communicate with the GPS module, and leaves the hardware serial port for debugging with the serial monitor.

### Hardware Serial Port Example

If you\'re using an Arduino Leonardo, Arduino Due, Arduino Zero, or any other Arduino with a free UART on pins 0/1, set the UART-select switch to **HW-UART**, and upload this example:

    language:c
        /******************************************************************************
    Basic_Passthrough_Hardware.ino
    Basic Hardware Serial GPS Passthrough
    By Jim Lindblom @ SparkFun Electronics
    February 9, 2016
    https://github.com/sparkfun/GPS_Shield

    This example uses an Arduino's hardware serial port -- on pins 0 and 1 -- to
    communicate with the GPS module. 

    Hardware serial should work on any Arduino's with a free hardware serial 
    UART on pins 0/1. That includes Arduino Leonardo, Zero, Due, and SparkFun's
    SAMD21 Dev Board.

    After uploading the code, open your serial monitor, set it to 9600 baud, and
    watch the GPS module's NMEA strings begin to flow by. See if you can pick
    out the latitude and longitude.

    Development/hardware environment specifics:
    Arduino IDE 1.6.7
    GPS Logger Shield v2.0 - Make sure the UART switch is set to HW-UART
    Arduino Leonardo, Arduino Zero, Arduino Due, SparkFun SAMD21 Dev Board, etc
    ******************************************************************************/

    #define GPS_BAUD_RATE 9600 // The GPS Shield module defaults to 9600 baud

    // Define the serial monitor port. On the Leonardo this is 'Serial'
    //  but on other boards this may be 'SerialUSB'
    #define SerialMonitor Serial // e.g. Arduino Leonardo
    // Define the harware serial port on pins 0/1. On the Leonardo this is 'Serial1'
    //  but on other boards this may be 'Serial'
    #define gpsPort Serial1 // e.g. Arduino Leonardo
    // See https://www.arduino.cc/en/Reference/Serial to find out which Serial ports
    //  you should use in the defines above.

    void setup() 
    

    void loop() 
    

You *may* have to alter either or both of the serial port `#defines` at the top of the code. Refer to your development board\'s datasheet or product info page for more information on which serial port is which.

### Using the Serial Passthrough Sketch

Once you\'ve uploaded the sketch, open up your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and set the baud rate to 9600. You should immediately begin to see GPS NMEA data begin to flow by at a rate of 1Hz.

For example, one set of strings may look like:

    $GPRMC,235316.000,A,4003.9040,N,10512.5792,W,0.09,144.75,141112,,*19
    $GPGGA,235317.000,4003.9039,N,10512.5793,W,1,08,1.6,1577.9,M,-20.7,M,,0000*5F
    $GPGSA,A,3,22,18,21,06,03,09,24,15,,,,,2.5,1.6,1.9*3E

If you don\'t see anything in the serial monitor, make sure the UART-select switch is in the correct position. Also double check that the blue \"GPS Fix\" LED is at least blinking. If it\'s not, the module may not be receiving power. Don\'t forget to supply VBAT!

If you\'re still not having any luck, get in touch with our [technical support team](https://www.sparkfun.com/technical_assistance).

------------------------------------------------------------------------

[NMEA strings](https://en.wikipedia.org/wiki/NMEA_0183) are the standard message format produced by almost all GPS receivers. They can relay all sorts of information including the time, latitude, longitude, altitude, and number of satellites visible, but unless you\'re an incredibly fast parser, these sentences will mostly mean nothing. Fortunately, the Arduino can read those strings, parse them for you, and give you more human-readable pieces of data.

## Example Sketch: TinyGPS Serial Streaming

A couple of our favorite GPS-parsing Arduino libraries are [TinyGPS](http://arduiniana.org/libraries/tinygps/) and [TinyGPS++](http://arduiniana.org/libraries/tinygpsplus/). These libraries simplify the task of parsing the excessive NMEA strings, leaving us with just the few bits of data we care about.

You will need to install the libraries in your Arduino IDE. Visit the links above to download them. Reference our [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) tutorial for any additional library-installing help you may need.

### TinyGPS++ Example

Here\'s a quick example, which uses the TinyGPS++ library to parse NMEA strings for position, altitude, time, and date. Copy and past the code below into your Arduino IDE and upload to your board.

    language:c
    /******************************************************************************
      TinyGPSPlus_GPS_Shield.ino
      TinyGPS++ Library Example for the SparkFun GPS Logger Shield
      By Jim Lindblom @ SparkFun Electronics
      February 9, 2016
      https://github.com/sparkfun/GPS_Shield

      This example uses SoftwareSerial to communicate with the GPS module on
      pins 8 and 9. It uses the TinyGPS++ library to parse the NMEA strings sent
      by the GPS module, and prints interesting GPS information to the serial
      monitor.

      After uploading the code, open your serial monitor, set it to 9600 baud, and
      watch for latitude, longitude, altitude, course, speed, date, time, and the
      number of visible satellites.

      Resources:
      TinyGPS++ Library  - https://github.com/mikalhart/TinyGPSPlus/releases
      SoftwareSerial Library

      Development/hardware environment specifics:
      Arduino IDE 1.6.7
      GPS Logger Shield v2.0 - Make sure the UART switch is set to SW-UART
      Arduino Uno, RedBoard, Pro, etc.
    ******************************************************************************/

    #include <TinyGPS++.h> // Include the TinyGPS++ library
    TinyGPSPlus tinyGPS; // Create a TinyGPSPlus object

    #define GPS_BAUD 9600 // GPS module baud rate. GP3906 defaults to 9600.

    // If you're using an Arduino Uno, RedBoard, or any board that uses the
    // 0/1 UART for programming/Serial monitor-ing, use SoftwareSerial:
    #include <SoftwareSerial.h>
    #define ARDUINO_GPS_RX 9 // GPS TX, Arduino RX pin
    #define ARDUINO_GPS_TX 8 // GPS RX, Arduino TX pin
    SoftwareSerial ssGPS(ARDUINO_GPS_TX, ARDUINO_GPS_RX); // Create a SoftwareSerial

    // Set gpsPort to either ssGPS if using SoftwareSerial or Serial1 if using an
    // Arduino with a dedicated hardware serial port
    #define gpsPort ssGPS  // Alternatively, use Serial1 on the Leonardo

    // Define the serial monitor port. On the Uno, and Leonardo this is 'Serial'
    //  on other boards this may be 'SerialUSB'
    #define SerialMonitor Serial

    void setup()
    

    void loop()
    

    void printGPSInfo()
    

    // This custom version of delay() ensures that the tinyGPS object
    // is being "fed". From the TinyGPS++ examples.
    static void smartDelay(unsigned long ms)
     while (millis() - start < ms);
    }

    // printDate() formats the date into dd/mm/yy.
    void printDate()
    

    // printTime() formats the time into "hh:mm:ss", and prints leading 0's
    // where they're called for.
    void printTime()
    

You may need to adjust the `gpsPort` and `SerialMonitor` defines near the top of the sketch. As it is, the sketch is set up to use the SoftwareSerial port.

After uploading the code, open up your serial monitor to watch the parsed GPS data stream by.

If your module doesn\'t have a good GPS fix, you\'ll probably see a lot of 0\'s stream by; the time should be incrementing, although it\'ll be incorrect (unless you plugged your Arduino in at exactly midnight!).

If you can find a way to take your computer and Arduino setup outside, that\'ll be your best bet for getting a fix. Otherwise, try to take it near an open window. The better view it has of the sky, the better chance it\'ll have to find the four satellites it needs.

A successful, fixed GPS stream will look something like this:

    Lat: 40.090422
    Long: -105.184534
    Alt: 5243.77
    Course: 295.56
    Speed: 0.01
    Date: 26/1/2016
    Time: 20:19:34
    Sats: 6

For more information on using the TinyGPS++ Library, check out the [project homepage](http://arduiniana.org/libraries/tinygpsplus/).

## Example Sketch: µSD Card GPS Logging 

Now that we have good GPS data, the final step is to start logging it to a µSD card.

Like the last example, this sketch uses [TinyGPS++](http://arduiniana.org/libraries/tinygpsplus/), it also uses Arduino\'s built-in [SD library](https://www.arduino.cc/en/Reference/SD).

Upload the following code onto your Arduino.

    language:c
        /******************************************************************************
      CSV_Logger_TinyGPSPlus.ino
      Log GPS data to a CSV file on a uSD card
      By Jim Lindblom @ SparkFun Electronics
      February 9, 2016
      https://github.com/sparkfun/GPS_Shield

      This example uses SoftwareSerial to communicate with the GPS module on
      pins 8 and 9, then communicates over SPI to log that data to a uSD card.

      It uses the TinyGPS++ library to parse the NMEA strings sent by the GPS module,
      and prints interesting GPS information - comma separated - to a newly created
      file on the SD card.

      Resources:
      TinyGPS++ Library  - https://github.com/mikalhart/TinyGPSPlus/releases
      SD Library (Built-in)
      SoftwareSerial Library (Built-in)

      Development/hardware environment specifics:
      Arduino IDE 1.6.7
      GPS Logger Shield v2.0 - Make sure the UART switch is set to SW-UART
      Arduino Uno, RedBoard, Pro, etc.
    ******************************************************************************/

    #include <SPI.h>
    #include <SD.h>
    #include <TinyGPS++.h>

    #define ARDUINO_USD_CS 10 // uSD card CS pin (pin 10 on SparkFun GPS Logger Shield)

    /////////////////////////
    // Log File Defintions //
    /////////////////////////
    // Keep in mind, the SD library has max file name lengths of 8.3 - 8 char prefix,
    // and a 3 char suffix.
    // Our log files are called "gpslogXX.csv, so "gpslog99.csv" is our max file.
    #define LOG_FILE_PREFIX "gpslog" // Name of the log file.
    #define MAX_LOG_FILES 100 // Number of log files that can be made
    #define LOG_FILE_SUFFIX "csv" // Suffix of the log file
    char logFileName[13]; // Char string to store the log file name
    // Data to be logged:
    #define LOG_COLUMN_COUNT 8
    char * log_col_names[LOG_COLUMN_COUNT] = ; // log_col_names is printed at the top of the file.

    //////////////////////
    // Log Rate Control //
    //////////////////////
    #define LOG_RATE 5000 // Log every 5 seconds
    unsigned long lastLog = 0; // Global var to keep of last time we logged

    /////////////////////////
    // TinyGPS Definitions //
    /////////////////////////
    TinyGPSPlus tinyGPS; // tinyGPSPlus object to be used throughout
    #define GPS_BAUD 9600 // GPS module's default baud rate

    /////////////////////////////////
    // GPS Serial Port Definitions //
    /////////////////////////////////
    // If you're using an Arduino Uno, RedBoard, or any board that uses the
    // 0/1 UART for programming/Serial monitor-ing, use SoftwareSerial:
    #include <SoftwareSerial.h>
    #define ARDUINO_GPS_RX 9 // GPS TX, Arduino RX pin
    #define ARDUINO_GPS_TX 8 // GPS RX, Arduino TX pin
    SoftwareSerial ssGPS(ARDUINO_GPS_TX, ARDUINO_GPS_RX); // Create a SoftwareSerial

    // Set gpsPort to either ssGPS if using SoftwareSerial or Serial1 if using an
    // Arduino with a dedicated hardware serial port
    #define gpsPort ssGPS  // Alternatively, use Serial1 on the Leonardo

    // Define the serial monitor port. On the Uno, and Leonardo this is 'Serial'
    //  on other boards this may be 'SerialUSB'
    #define SerialMonitor Serial

    void setup()
    
      updateFileName(); // Each time we start, create a new file, increment the number
      printHeader(); // Print a header at the top of the new file
    }

    void loop()
    
          else // If we failed to log GPS
          
        }
        else // If GPS data isn't valid
        
      }

      // If we're not logging, continue to "feed" the tinyGPS object:
      while (gpsPort.available())
        tinyGPS.encode(gpsPort.read());
    }

    byte logGPSData()
    

      return 0; // If we failed to open the file, return fail
    }

    // printHeader() - prints our eight column names to the top of our log file
    void printHeader()
    
        logFile.close(); // close the file
      }
    }

    // updateFileName() - Looks through the log files already present on a card,
    // and creates a new file with an incremented file index.
    void updateFileName()
    
        else // Otherwise:
        
      }
      SerialMonitor.print("File name: ");
      SerialMonitor.println(logFileName); // Debug print the file name
    }

You may need to edit the `gpsPort` and `SerialMonitor` objects, toward the top of the code to get the example to work correctly on your Arduino. The sketch defaults to using SoftwareSerial for the GPS, which should work for most boards \-- as long as the UART-Select switch is shifted towards SW-UART.

Before uploading the code, **plug a µSD card into your GPS Logger Shield**. Push it in gently until you hear a click. Then release, and let it latch into place.

[![uSD card plugged into the shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-sd-card-in.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-sd-card-in.jpg)

Once that\'s in place, upload and run! You can check the serial monitor for debugging data, or just trust that the logger is logging.

Once the GPS module gets a good fix, the Arduino will start logging longitude, latitude, altitude, speed, course, date, time, and the number of visible satellites into a CSV file. The data is set to log once every five seconds, but that\'s easily tunable if you need more or less data.

After letting it log for a bit, turn off your Arduino, load the SD card into your computer, and check for a `GPSLOG###.CSV` file. Open it up in a spreadsheet program, or just use a text editor to see what your Arduino logged.

[![CSV example screenshot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-log-csv-example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-log-csv-example.png)

Now really test the logger! Power your Arduino up with a battery (our [9V to Barrel Jack Adapter](https://www.sparkfun.com/products/9518) is handy for that)\...

[![Battery-powered Arduino/GPS Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/8/gps-action-shot-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/8/gps-action-shot-02.jpg)

\...and take your Arduino for a walk.