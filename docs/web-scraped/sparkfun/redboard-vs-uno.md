# Source: https://learn.sparkfun.com/tutorials/redboard-vs-uno

## What Is The RedBoard?

[Arduino](https://learn.sparkfun.com/tutorials/what-is-an-arduino) is one of the most popular physical computing platforms available today. It\'s an amazing tool for both experienced and budding electronics enthusiasts. It\'s part hardware, part software, and part community; all of which come together to create a well-supported, solidly-designed electronics platform.

The best part: the entire Arduino project \-- both hardware and software \-- is open-source. The [schematics](http://arduino.cc/en/uploads/Main/Arduino_Uno_Rev3-schematic.pdf), hardware design files, and [source code](https://github.com/arduino/Arduino) are all freely available for viewing and modification. Released under a [Creative Commons Share Alike license](http://creativecommons.org/licenses/by-sa/3.0/), anyone is free to riff on the hardware design and produce their own version. That\'s what we\'ve done with the [RedBoard](https://www.sparkfun.com/products/11575). It still looks and acts just like an [Arduino Uno](https://www.sparkfun.com/products/11021), but is slightly modified to make the board better-suited to our purposes.

[![Arduino Uno PTH on the left, RedBoard on the right](https://cdn.sparkfun.com/r/600-600/assets/1/4/8/4/e/51af6992ce395f3150000000.png)](https://cdn.sparkfun.com/assets/1/4/8/4/e/51af6992ce395f3150000000.png)

*An [Arduino Uno PTH](https://www.sparkfun.com/products/11021) (left, blue) next to a [RedBoard](https://www.sparkfun.com/products/11575).*

Our [introductory video](http://www.youtube.com/watch?v=su0sYPqyV_w&feature=youtu.be&t=3m25s) glosses over some of what makes the RedBoard different from the Arduino Uno:

ReplaceMeOpen

ReplaceMeClose

In this tutorial, we\'ll take an in-depth look at the major similarities and differences between the two boards. Stated briefly, here\'s the key info:

#### Key Differences

- **USB connector**: Arduino Uno uses a USB type B connector, while the Redboard uses the smaller mini-B connector. Each connector requires a different USB cable.
- **USB-to-Serial Transciever**: The Arduino Uno uses an ATmega16U2 loaded with custom firmware to convert between USB and serial. The RedBoard uses the FTDI FT231X. This difference is only really prevalent when **installing drivers** because each requires a different driver file.
- **SMD vs PTH**: The Arduino Uno comes in two versions through-hole (PTH) or surface-mount (SMD). The RedBoard is only offered in SMD. The RedBoard takes this a step further, by making *every* component surface-mount. No sharp edges on the bottom of the board!
- **Color**: It won\'t have any real influence on the operation of the Arduino, but it certainly affects the board\'s swag-factor. Cool blue or ~~Ferarri~~ SparkFun red?
- **Price**: Because we manufacture the board in-house, here in Boulder, CO, we can afford to keep the price-tag a tad lower.

#### Key Similarities

- **ATmega328**: The main microprocessor on both boards is the popular ATmega328. This is they key-est of similarities.
- **IDE interaction/Board Selection Type**: The ATmega328 on both boards is loaded with the same bootloader (Optiboot). That means, when you program the board, you can still select *Arduino Uno* under the *Tools \> Board* menu.
- **Dimensions and Connector Layout**: Both boards are the same size and shape, and the female header connectors are all placed in the same locations. All shields and enclosures will be compatible with both boards.
- **Digital and Analog Pins**: Each board has 14 digital I/Os and 6 analog I/Os.
- **Operating Voltage**: Both boards operate at 5V, and have an on-board 3.3V regulator. They can be powered either through USB or with a 7-15V barrel jack power supply.

## Compare and Contrast

The RedBoard, Arduino Uno SMD, and Arduino Uno PTH have a lot in common. They really share more similarities than they do differences. Here\'s a tabled overview:

                              [RedBoard](https://www.sparkfun.com/products/11575)                                                                                               [Arduino Uno SMD](https://www.sparkfun.com/products/11224)                                                                                              [Arduino Uno PTH](https://www.sparkfun.com/products/11021)
  --------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  Top View                    [![](https://cdn.sparkfun.com/images/products/1/1/5/7/5/11575-04_medium.jpg)](https://cdn.sparkfun.com//images/products/1/1/5/7/5/11575-04.jpg)   [![](https://cdn.sparkfun.com/assets/3/3/3/3/3/51ae3283ce395f861b000000.png)](https://cdn.sparkfun.com/assets/9/7/9/9/3/51ae345ece395f515d000000.png)   [![](https://cdn.sparkfun.com/images/products/1/1/0/2/1/11021-02a_i_ma.jpg)](https://cdn.sparkfun.com//images/products/1/1/0/2/1/11021-02a.jpg)
  Bottom View                 [![](https://cdn.sparkfun.com/images/products/1/1/5/7/5/11575-03_medium.jpg)](https://cdn.sparkfun.com//images/products/1/1/5/7/5/11575-03.jpg)   [![](https://cdn.sparkfun.com/images/products/1/1/2/2/4/11224-03c_i_ma.jpg)](https://cdn.sparkfun.com//images/products/1/1/2/2/4/11224-03c.jpg)         [![](https://cdn.sparkfun.com//images/products/1/1/0/2/1/11021-03a_i_ma.jpg)](https://cdn.sparkfun.com//images/products/1/1/0/2/1/11021-03a.jpg)
  Dimensions                  2.7 x 2.1\" (68.58 x 53.34mm)                                                                                                                     2.7 x 2.1\" (68.58 x 53.34mm)                                                                                                                           2.7 x 2.1\" (68.58 x 53.34mm)
  Color                       Red                                                                                                                                               Blue/White                                                                                                                                              Blue/White
  USB Connector               Mini-B                                                                                                                                            Type B                                                                                                                                                  Type B
  USB-to-Serial Chip          FTDI FT231X                                                                                                                                       ATmega16U2 w/ custom firmware                                                                                                                           ATmega16U2 w/ custom firmware
  Drivers (Windows)           FTDI VCP Drivers                                                                                                                                  Arduino USB Driver                                                                                                                                      Arduino USB Driver
  Windows Compatibility       8 (32 & 64-bit), 7 (32 & 64-bit), Vista (32 & 64-bit), XP (32 & 64-bit), 2000, 98 [\*](http://www.ftdichip.com/FTDrivers.htm)                     8 (32 & 64-bit), 7 (32 & 64-bit), Vista (32 & 64-bit), XP (32 & 64-bit)                                                                                 8 (32 & 64-bit), 7 (32 & 64-bit), Vista (32 & 64-bit), XP (32 & 64-bit)
  Mac Compatibility           OS X, OS 9, OS 8                                                                                                                                  OS X                                                                                                                                                    OS X
  Linux Compatibility         Yes                                                                                                                                               Yes                                                                                                                                                     Yes
  Main Microprocessor         ATmega328                                                                                                                                         ATmega328                                                                                                                                               ATmega328
  MCU PTH or SMD              SMD                                                                                                                                               SMD                                                                                                                                                     PTH
  V~IN~ Range (Recommended)   7-15V                                                                                                                                             7-12V                                                                                                                                                   7-12V
  Operating Voltage           5V                                                                                                                                                5V                                                                                                                                                      5V
  Digital I/O Pins            14                                                                                                                                                14                                                                                                                                                      14
  Analog Inputs               6                                                                                                                                                 6                                                                                                                                                       6
  Arduino *Board* Selection   Arduino Uno                                                                                                                                       Arduino Uno                                                                                                                                             Arduino Uno
  Retail Price                \$24.95                                                                                                                                           \$29.95                                                                                                                                                 \$24.95

------------------------------------------------------------------------

Next we\'ll look in-depth at the most significant differences between the RedBoard and Arduino Uno.

## USB Connectors and Drivers

Both the Arduino Uno and Redboard interface with computers via USB, but the [connectors](../connector-basics/usb-connectors) are different. The Arduino Uno uses the larger, square-ish type-B connector. Type-B USB connectors are often found on USB printers, or other devices where size is not an issue.

[![Arduino Uno connector and cable](https://cdn.sparkfun.com/r/600-600/assets/7/2/1/1/0/51bf4313ce395f5c27000000.png)](https://cdn.sparkfun.com/assets/7/2/1/1/0/51bf4313ce395f5c27000000.png)

The RedBoard uses a **mini-B USB** connector. Mini-B connectors are lower-profile USB connectors, which might be found on cameras, MP3 players, and cell phones.

[![Redboard connector and cable](https://cdn.sparkfun.com/r/600-600/assets/5/0/1/c/8/51bf4313ce395fab26000000.png)](https://cdn.sparkfun.com/assets/5/0/1/c/8/51bf4313ce395fab26000000.png)

Obviously, you\'ll need a **cable** that matches the connector on the development board. The Arduino Uno would require an [A to B](https://www.sparkfun.com/products/512) cable, while a RedBoard would require an [A to mini-B](https://www.sparkfun.com/products/11301) cable (or you could cover both bases with a [Cerberus cable](https://www.sparkfun.com/products/11515)).

### USB-to-Serial Converter

The second difference between the boards is how they manage to convert USB coming from your computer into a [serial protocol](https://learn.sparkfun.com/tutorials/serial-communication) the Arduino can understand. Arduino serial communication is critical for **uploading sketches** and sending/receiving information via the **Serial Monitor**. The Uno uses an Atmel processor \-- the ATmega16U2 \-- loaded with custom firmware, to convert USB to (and from) serial.

Before the Arduino Uno was released [previous versions](http://arduino.cc/en/Main/Boards) of the development platfurm used a dedicated USB-to-serial transceiver: FTDI\'s FT232RL. Call us nostalgic, but we really preferred the robust reliability of the FT232RL over the ATmega16U2 solution. So when we designed our own version of the Arduino platform, we decided to revert back to the FT232RL for our USB-to-serial needs.

About 99% of the time these ICs should be of no concern to your everyday Arduino hacking. Once drivers are installed, each should transparently convert data between your Arduino and computer. The difference between the two USB/Serial transceivers is most apparent when you\'re first connecting the board to your computer.

### USB Driver Installation

For Windows users in particular, each board requires a unique **driver** to be installed before being usable. There are plenty of installation tutorials for both chips ([our guide on installing FTDI drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) and [Arduino\'s guide for theirs](http://arduino.cc/en/Guide/Windows)).

The most up-to-date version of the FTDI drivers can be downloaded directly from the [chip manufacturer\'s webpage](http://www.ftdichip.com/Drivers/VCP.htm) where they host [installation guides](http://www.ftdichip.com/Support/Documents/InstallGuides.htm) of their own. There should be no shortage of driver-installation support out there.

Once the board is connected to your computer and the drivers are installed, the two chips should be almost invisible. For the most part, we don\'t really care *how* the Arduino communicates with our computer, just that it does.

## SMD vs PTH

The Arduino Uno comes in two forms: [surface mount (SMD)](https://www.sparkfun.com/products/11224) and [through-hole (PTH)](https://www.sparkfun.com/products/11021). Both versions are very similar, the only significant difference comes from what package the ATmega328 processor comes in. SMD components are generally easier to mass assemble (though harder to manually assemble), so the SMD version of the Uno is either cheaper, more readily available, or both.

[![Arduino Uno SMD vs PTH](https://cdn.sparkfun.com/r/600-600/assets/4/9/7/a/e/51bf4313ce395f1027000000.png)](https://cdn.sparkfun.com/assets/4/9/7/a/e/51bf4313ce395f1027000000.png)

*An SMD Arduino Uno (left) and the regular PTH version. The ATmega328 processors are highlighted on each board, they look different, but are actually (pretty much) the same thing.*

The RedBoard is only offered in one form: surface mount. The design actually takes the SMD choice even further by making *every* component SMD (the Arduino UNO SMD still has PTH connectors, for example), but the main focus of the SMD vs. PTH debate centers around the package of the microcontroller (as highlighted in the image above).

### SMD Pros and Cons

#### Pros: No Snags, Lower Cost

The absence of PTH components on the RedBoard means a nice, smooth surface on the bottom of the board \-- there\'s no danger of being pricked by pointy solder joints.

[![Smooth back-side of RedBoard](https://cdn.sparkfun.com/r/600-600/assets/5/9/6/4/9/51b0dc7ece395f2817000002.png)](https://cdn.sparkfun.com/assets/5/9/6/4/9/51b0dc7ece395f2817000002.png)

On top of that, eliminating exposed joints on the bottom of the board also protects the components from accidental shorts. As any hobbyist with a messy desk could attest, stray wire clippings and other metals strewn across workbenches are a common source of accidental [short circuits](../what-is-a-circuit/short-and-open-circuits). [Standoffs](https://www.sparkfun.com/products/10927) or [Arduino holders](https://www.sparkfun.com/products/11235) will help prevent against this if you\'re using an Arduino board.

#### Con: Hard to Swap µCs

Microcontrollers (µCs) \-- in this case the ATmega328 \-- are usually the most expensive component in a design. A µC failure[\*](#astrisk) is hard to overcome, and it usually requires either replacing the component or just recycling the board.

[]The nice thing about the PTH Arduino is the ATmega328 is socketed, so *if* it blows up[\*](#astrisk) replacing the chip is as easy as prying it out and sticking in a [new one](https://www.sparkfun.com/products/10524).

The ability to easily remove the ATmega328 has other advantages as well. For example, if you\'re looking to build a project using the IC, you can prototype in the development board and eventually transfer the microcontroller out of the Uno to a custom board.

\*: Microcontroller failure on all of these boards is a big \"if\". The ATmega328 is a very resilient microcontroller. You really have to try to fry the IC, or even just a single I/O pin on it. A failure in the power circuitry (voltage regulators specifically) is much more likely.