# Source: https://learn.sparkfun.com/tutorials/preassembled-40-pin-pi-wedge-hookup-guide

## Introduction

The [preassembled 40-pin Pi Wedge](https://www.sparkfun.com/products/13717) is the newest member in our Pi Wedge family. It\'s an excellent way to get those pesky Pi pins broken out to a breadboard so that they can easily be used.

[![SparkFun Pi Wedge](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/2/1/3/13717-Pi_Wedge.jpg)](https://www.sparkfun.com/sparkfun-pi-wedge.html)

### [SparkFun Pi Wedge](https://www.sparkfun.com/sparkfun-pi-wedge.html) 

[ BOB-13717 ]

This is the SparkFun Pi Wedge, a small board that connects to the 40-pin GPIO connector on the Raspberry Pi and breaks the pi...

[ [\$13.50] ]

*Check out the Pi Wedge in the product showcase at [2:47](https://youtu.be/0f5KykDQn6I?t=167)!*

This Pi Wedge is compatible with members of the Pi family with 40-pin GPIO headers, including

- The Raspberry Pi Model A+
- [The Raspberry Pi Model B+](https://www.sparkfun.com/products/12995)
- [The Raspberry Pi 2 Model B](https://www.sparkfun.com/products/13297)

It adapts the 40-pin GPIO connector on recent Pis to a breadboard-friendly form factor and rearranges the pins by similar function. Also, the GPIO pins are arranged in ascending order.

This version also comes fully assembled \-- no soldering is required!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/2/wedge-n-pi.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/2/wedge-n-pi.jpg)

*The Pi Wedge, shown with a Pi B+.*

### Covered in This Tutorial

- [Background](https://learn.sparkfun.com/tutorials/preassembled-40-pin-pi-wedgehookup-guide#background) \-- How the Pi Wedge came to be
- [Assembly](https://learn.sparkfun.com/tutorials/preassembled-40-pin-pi-wedgehookup-guide#assembly) \-- How to connect the FTDI, ribbon cable, and breadboard
- [Pin Mapping](https://learn.sparkfun.com/tutorials/preassembled-40-pin-pi-wedgehookup-guide#pin-mapping) \-- What the silkscreen on the Wedge represents
- [Logic Levels and Power](https://learn.sparkfun.com/tutorials/preassembled-40-pin-pi-wedgehookup-guide#logic-levels-and-power) \-- Electrical information about connecting to the Pi
- [Some additional resources](https://learn.sparkfun.com/tutorials/preassembled-40-pin-pi-wedgehookup-guide#resources--going-further)

But before you begin, check out these links and brush up on topics you may not be familiar with:

### Suggested Reading

- [How To Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [Setting Up a Boot Card](http://elinux.org/RPi_Easy_SD_Card_Setup)
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)

### Suggested Viewing

- Getting Started With The Raspberry Pi
  - [Part 1](https://www.youtube.com/watch?v=b6h95jNWg1g)
  - [Part 2](https://www.youtube.com/watch?v=6HeRyrr4i9k)
  - [Part 3](https://www.youtube.com/watch?v=1tEMRCtXALM)

## Background

In the process of developing projects like the [Twitter Monitor](https://learn.sparkfun.com/tutorials/raspberry-pi-twitter-monitor) and [Great American Tweet Race](https://twitter.com/Gr8AmTweetRace) around the Raspberry Pi, we found that we were experiencing some growing pains when trying to expand the Pi into a prototype that involved external hardware.

[![Bob Pease would be proud](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/6/IMG_20131101_145337.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/6/IMG_20131101_145337.jpg)

*There\'s a Pi somewhere in this ratsnest*

The Raspberry Pi Model B+ has a 40-pin connector that provides access to several communication interfaces, plus GPIO and power. But the connector doesn\'t have detailed labeling, and the native pin arrangement is somewhat scattershot. Pins used for similar functions aren\'t always grouped together, and power and ground pins are interspersed with no obvious pattern.

The pins also don\'t translate to a solderless breadboard very easily. Our first projects used a bunch of [F-M jumper wires](https://www.sparkfun.com/products/9385) that we just plugged into the header. They involved a lot of \"ratsnest jiggling\" when things stopped working.

#### Bootstrapping

In addition to the physical issues of using the I/O connector, getting started with a brand new Raspberry Pi B+ always seems to involve a chicken-and-egg situation. We just want to SSH into it, so we can use the command line. But in order to SSH to it, we need to know it\'s IP address\...and of course, the IP address is most easily learned by running `ifconfig` on the command line.

### The Solution

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/2/wedge_breadboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/2/wedge_breadboard.jpg)

*Meet the 40-Pin Pi Wedge*

The Pi Wedge B+ connects to the 40-pin GPIO connector, and breaks out the pins in a breadboard-friendly arrangement and spacing. It adds a pair of decoupling capacitors on the power supply lines, and it makes the initial bringup process easier - you can plug an [FTDI Basic](https://www.sparkfun.com/products/9873) module into the serial port.

## Assembly

### Contents

The Preassembleed Pi Wedge comes with the Wedge PCB, and a 40-pin ribbon cable.

### Connection

The 40-pin ribbon cable is used to connect the wedge to the Pi. This cable is polarized --- notice that the pin 1 marking is very subtle. On the Pi Wedge PCB end, the tooth on the cable will interface with the notch in the shrouded header. Insert the IDC cable into the Pi Wedge\'s polarized connector so that the cable extends away from the breadboard connection.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/2/ribbon-on-wedge.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/2/ribbon-on-wedge.jpg)

*Inserting the ribbon cable*

Insert the Wedge into the center of the breadboard so that each pin has their own row.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/4/Raspberry_Pi_2_Kit-02_cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/4/Raspberry_Pi_2_Kit-02_cropped.jpg)

Wedge inserted in breadboard.

The header on the Pi itself doesn\'t have anything to help guarantee the alignment. You\'ll need to take care that it gets connected properly. Pin 1 on the Pi is marked with a dog-eared corner on the silkscreened rectangle. The ribbon cable connector is embossed with (a barely visible) small triangle that marks pin 1. The first pin is also coded on the wire, such as the red markings in the photo below (though it may also be another color, such as black or dark blue). Insert the IDC cable to the Pi so that the cable extends away from the Pi.

[![Proper Orientation for the IDC Cable on the Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/2/ribbon-on-pi.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/2/ribbon-on-pi.jpg)

*Proper pin-1 orientation*

[**Note:**](#enclosure_limitations) If you are using an enclosure (like the Pi 4 heat sink case, you may want to consider using an extension header to properly connect the Pi Wedge\'s IDC cable to the Raspberry Pi\'s GPIO pins.\
\

[![Extended GPIO Header - Female (PTH, 0.1in., 2x20-Pin, 13.5mm/9.80mm)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/6/5/3/16764-2_X_20_Pin_Extended_GPIO_Header_-_Female_-_13.5mm_9.80mm-01.jpg)](https://www.sparkfun.com/extended-gpio-female-header-2x20-pin-13-5mm-9-80mm.html)

### [Extended GPIO Header - Female (PTH, 0.1in., 2x20-Pin, 13.5mm/9.80mm)](https://www.sparkfun.com/extended-gpio-female-header-2x20-pin-13-5mm-9-80mm.html) 

[ PRT-16764 ]

This 2x20 pin female header is meant to allow you to extend the reach of any board with the standard 2x20 GPIO pin footprint.

[ [\$3.25] ]

[![Extended GPIO Header - Female (PTH, 0.1in., 2x20-Pin, 16mm/7.30mm)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/6/5/2/16763-2X20_Pin_Extended_GPIO_Header_-_Female_-_16mm_7.30mm-01.jpg)](https://www.sparkfun.com/extended-gpio-female-header-2x20-pin-16mm-7-30mm.html)

### [Extended GPIO Header - Female (PTH, 0.1in., 2x20-Pin, 16mm/7.30mm)](https://www.sparkfun.com/extended-gpio-female-header-2x20-pin-16mm-7-30mm.html) 

[ PRT-16763 ]

This 2x20 pin female header is meant to allow you to extend the reach of any board with the standard 2x20 GPIO pin footprint.

[ [\$3.25] ]

Extension headers are also useful when stacking HAT\'s with other single board computers that utilize the Pi\'s standard 2x20 GPIO header like the Google Coral and NVIDIA Jetson.\
\
The [extension header with 9.80mm pin length \[ PRT-16764 \]](https://www.sparkfun.com/products/16764) is useful when sandwiching a PCB between a Pi and HAT. The header can also be used to sandwich a board betwen the Pi and Pi Wedge\'s IDC cable. The [extension header with 7.30mm pin length \[ PRT-16763 \]](https://www.sparkfun.com/products/16763) uses three plastic spacers which cover the pins more when using a HAT or the Pi Wedge\'s IDC cable.\
\

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Extension Header with 9.80mm Pin Length is Used to Help Stack the Qwiic SHIM and Servo pHAT on a Pi 4 with Heat Sink](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_2x20_Header_Stackable_Header_PCB_Sandwiched.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_2x20_Header_Stackable_Header_PCB_Sandwiched.jpg)   [![Extension Header with 7.30mm Pin Length is Used to Help Connect the Pi Wedge\'s IDC Cable to the Pi 4 with Heat Sink](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_2x20_Header_Stackable_Header_Pi_Wedge_Enclosure.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_2x20_Header_Stackable_Header_Pi_Wedge_Enclosure.jpg)
  *Extension Header with 9.80mm Pin Length is Used to Help Stack the Qwiic SHIM and Pi Servo HAT on a Pi 4 with Heat Sink*                                                                                                                                                                                                                                                          *Extension Header with 7.30mm Pin Length is Used to Help Connect the Pi Wedge\'s IDC Cable to the Pi 4 with Heat Sink*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The height of the enclosure and PCB varies depending on the design. The image below shows a Pi 3 in the enclosure. The overall height of the enclosure is lower than the Pi 4\'s heat sink enclosure, so one 2x20 extension header was needed when stacking the Qwiic pHAT v2.0 on the Pi. You may need to stack additional extension headers so that the boards have enough clearance when using other enclosures and PCBs sandwiched between the Pi and IDC cable.\
\

[![Using Stackable Header with Varying Enclosure Height](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_2x20_Header_Stackable_Header_Varying_Enclosure_Height.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/1/Raspberry_Pi_2x20_Header_Stackable_Header_Varying_Enclosure_Height.jpg)

If you decide to connect to the Pi using serial, you can insert a 3.3V FTDI to the Pi Wedge. The FTDI connector needs to be aligned correctly. Be sure to match up the \"GRN\" and \"BLK\" markings on both boards.

[![FTDI connected to Pi Wedge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/2/ftdi-plugged.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/2/ftdi-plugged.jpg)

*Proper 3.3V FTDI-Basic orientation*

Your setup will look similar to the image below. In this case, we used a Pi 3 in an enclosure.

[![Pi Wedge Setup with Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/3/Raspberry_Pi_3_Hookup_Guide-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/3/Raspberry_Pi_3_Hookup_Guide-07.jpg)

In the next section, we\'ll explore how the signals from the Pi are mapped to the Wedge.

## Pin Mapping

### Changes With the B+

When the Raspberry Pi foundation introduced the B+, they expanded the GPIO header from 26 to 40 pins. These changes have been carried forward by the A+ and Pi 2 Model B. The connector adds nine more GPIO pins plus the ID_SC and ID_SD pins to identify external peripherals, which you can learn more about in our [SPI and I2C tutorial](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial#i2c-0-on-40-pin-pi-boards).

### Signal Location

The Pi Wedge reorganizes the I/O pins on the Pi, putting similar functions on adjacent pins. The SPI, I2C and UART signals are all grouped near each other.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/2/PIN-LABELS.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/2/PIN-LABELS.png)

*Functional Groupings*

The pins are labeled, though the labels are short, to fit the space available on the PCB. The UART, SPI and I2C pins are marked with their communication bus functions, but they are also available as GPIO pins when configured in that mode.

The following table denotes the assignment of signals on the Pi Wedge, including the peripheral and alternate GPIO assignments where appropriate.

  ---------------- ------------------ ------------------- -------------------- --------------------------------- ------------------- ------------------ ----------------
   **Wedge Silk**   **Python (BCM)**   **WiringPi GPIO**        **Name**                   **Name**               **WiringPi GPIO**   **Python (BCM)**   **Wedge Silk**
        G17                17                  0           GPIO17 (GPIO_GEN0)         GPIO18 (GPIO_GEN1)                  1                  18               G18
        G16                16                 27                 GPIO16                     GPIO19                       24                  19               G19
        G13                13                 23                 GPIO13                     GPIO20                       28                  20               G20
        G12                12                 26                 GPIO12                     GPIO21                       29                  21               G21
         G6                6                  22                 GPIO06               GPIO22 (GPIO_GEN3)                  3                  22               G22
         G5                5                  21                 GPIO05               GPIO23 (GPIO_GEN4)                  4                  23               G23
         G4                4                   7           GPIO04 (GPIO_GCLK)         GPIO24 (GPIO_GEN5)                  5                  24               G24
        CE1                                   11           GPIO7 (SPI_CE1_N)          GPIO25 (GPIO_GEN6)                  6                  25               G25
        CE0                                   10           GPIO8 (SPI_CE0_N)                GPIO26                       25                  26               G26
        MOSI                                  12           GPIO10 (SPI_MOSI)          GPIO27 (GPIO_GEN2)                  2                  27               G27
        MISO                                  13           GPIO09 (SPI_MISO)          GPIO03 (SCL1, I2C)                  9                                   SCL
        SCK                              (no worky 14)      GPIO11 (SPI_CLK)          GPIO02 (SDA1, I2C)                  8                                   SDA
        RXI                                   16           GPIO15 (UART_RXD0)   GPIO0, ID_SC (I2C ID SC EEPROM)          31                                   IDSC
        TXO                                   15           GPIO14 (UART_TXDO)   GPIO1, ID_SD (I2C ID SD EEPROM)          30                                   IDSD
                                                                   5V                         5V                                                        
                                                                  3.3V                       3.3V                                                       
                                                                 GROUND                     GROUND                                                      
  ---------------- ------------------ ------------------- -------------------- --------------------------------- ------------------- ------------------ ----------------

*Pi Wedge B+ Pin-Function mapping*

**Heads up!** The pinout is with respect to the Pi Wedge. If you are looking for the pinout with respect to the Pi\'s header, check out the table in the Raspberry gPIo tutorial.\
\

[Raspberry gPIo: GPIO Pinout](https://learn.sparkfun.com/tutorials/raspberry-gpio#gpio-pinout)

## Logic Levels And Power

### Logic Levels

The Pi uses 3.3V logic levels, which are not 5V tolerant. Many peripheral devices are capable of running at 3.3V, but in the case that you need to interface with 5V devices, use a level shifter, such as the [TXB0104 breakout](https://www.sparkfun.com/products/11771).

### Communications

The signals on the 6-pin FTDI header are also limited to 3.3V logic levels. Be sure to use it with a [3.3V FTDI module](https://www.sparkfun.com/products/9873), and not a 5V one.

### Power

Understanding the Pi\'s power supply is critical to using it successfully, particularly when building it into a larger system.

The Raspberry Pi B+ is more efficient than it\'s predecessors, as it replaces the former chain of linear power regulators with switching regulators.

The most recently published schematics are for the [Raspberry Pi B+](http://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/README.md), and we\'re assuming that the Pi2 model B and A+ are similar. Inspecting those schematics, we see that 5V comes into the the board via connector J1 - it\'s a micro USB connector, but only the power and ground pins are connected. The 5V coming from this connector passes through a fuse and a transistor circuit that protects against power polarity mishaps, then continues around the board without any further regulation. The 5V connections on the Pi Wedge come straight from this line.

On the B+, the 5V goes to a dual switching regulator that further reduces it to 3.3V, and 1.8V. The regulated 3.3V is present on the I/O connector.

[![Power Regulation](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/5/Power-regulators.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/5/Power-regulators.png)

There are several power strategies that can be applied in a Pi deployment, depending on the overall needs and availability.

#### Power Through the GPIO Connector

The most obvious strategy for powering small external circuits is to get power directly from the GPIO connector. To power small circuits on your breadboard, you can run jumpers from the 5V or 3.3V and Ground pins on the wedge to the power rails on the breadboard.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/2/power-rail-ties.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/2/power-rail-ties.jpg)

*Jumpering power to the breadboard rails*

While this is the most immediate way to access power, it only extends to small circuits. The B+ itself is limited to 2A total from the 5V line, most of which is needed by the B+ itself. The [stated limit for the 3.3V pins is 50 mA](http://elinux.org/RPi_Low-level_peripherals#Power_pins).

If you\'re developing external circuitry, and the Pi resets when you\'re testing it, you may be exceeding the current limits. We saw this exact situation arise as we added SPI controlled 7-segment LED displays - if we illuminated one too many segments, the system crashed. For circuits with higher power draw, we\'ll need to explore some alternatives.

#### Daisy Chaining

The next power option is to connect each section of the circuit directly to the power supply. This means that the peripherals aren\'t constrained by the current limits of the fuses and regulators on the Pi itself.

[![daisy chained power](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/5/daisyBplus.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/5/daisyBplus.png)

*The peripherals are powered directly by the supply directly*

For peripherals that use 5V logic, they should also include [3.3V/5V logic level translation](https://learn.sparkfun.com/tutorials/logic-levels).

#### Back Power Through J8

As described above, a simple deployment can power peripherals via the 5V and 3.3V pins of J8, but it\'s also possible to apply power to the Pi via those lines. The Pi Foundation call this [\"back powering\"](https://github.com/raspberrypi/hats/blob/master/designguide.md#back-powering-the-pi-via-the-j8-gpio-header), and they have a number of recommendations for it\'s implementation.

[![Backpowering](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/5/backpowering-diagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/5/backpowering-diagram.png)

The first recommendation is to duplicate the fuse and MOSFET + BJT power protection circuit as seen on the Pi itself. This circuit is a variant on the \"ideal diode\" circuit.

[![Ideal Diode](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/5/zvd-circuit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/5/zvd-circuit.png)

It serves several purposes:

- Under ordinary circumstances, with power coming in via the micro-USB plug, the MOSFET is biased fully on, so there is only minimal voltage drop across it, where a typical Schottky or Silicon diode would drop 0.3V or more.
- Second, it prevents power from flowing if the power polarity at the micro-USB plug is incorrect.
- Third, if the board is powered via J8, it prevents power from being drawn from J1, to prevent contention if two supplies are present at the same time.

The other recommendation is that the HAT needs to be able to provide 5V, +/- 5%, with at least 1.3 A available for the Pi.