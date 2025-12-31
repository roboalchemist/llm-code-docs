# Source: https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide

## Introduction

The [SparkFun ESP32 Thing](https://www.sparkfun.com/products/13907) is a comprehensive development platform for [Espressif\'s ESP32](https://espressif.com/en/products/hardware/esp32/overview), their super-charged version of the popular [ESP8266](https://www.sparkfun.com/products/13711). Like the 8266, the ESP32 is a WiFi-compatible microcontroller but adds nearly 30 I/O pins. The ESP32's power and versatility will make it the foundation of IoT and connected projects for many years to come.

[![SparkFun ESP32 Thing](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/5/6/4/13907-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing.html)

### [SparkFun ESP32 Thing](https://www.sparkfun.com/sparkfun-esp32-thing.html) 

[ DEV-13907 ]

The SparkFun ESP32 Thing is a comprehensive development platform for Espressif's ESP32, their super-charged version of the ...

[ [\$30.85] ]

The SparkFun ESP32 Thing equips the ESP32 with everything necessary to program, run, and develop on the wonderchip. In addition to the WiFi SoC, the Thing includes an [FTDI FT231x](https://www.sparkfun.com/products/13263), which converts USB to serial, and allows your computer to program and communicate with the microcontroller. It also features a **lithium-polymer (LiPo) battery charger**, so your ESP32 project can be truly wireless. Additionally, the board includes a handful of LEDs and buttons to aid in your development.

### Covered In This Tutorial

This hookup guide serves as a primer on all things ESP32 Thing. It documents hardware features of the board, including a handful of assembly tips. Then it will delve into firmware development \-- including demonstrating how to add ESP32 support to the popular **Arduino** IDE.

The tutorial is broken up into a handful of sections, which you can navigate through using the menu on the right. Those sections include:

- [Hardware Overview](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide#hardware-overview) \-- An examination of the ESP32 Thing\'s hardware layout and features, including an introduction to the ESP32\'s I/O capabilities.
- [Assembly Tips](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide#assembly-tips) \-- Quick soldering tips and tricks.
- [Installing via Arduino IDE Boards Manager](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide#installing-via-arduino-ide-boards-manager) \-- How to add ESP32 support using the Arduino Boards Manager.
- [Installing the ESP32 Arduino Core](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide#installing-the-esp32-arduino-core) \-- How to add ESP32 support to your computer\'s Arduino development environment.
- [Arduino Example: Blink](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide#arduino-example-blink) \-- Verify that your ESP32 Thing and Arduino board definitions work with the classic blink sketch.
- [Arduino Example: WiFi](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide#arduino-example-wifi) \-- Connect your ESP32 to a local WiFi network, and start IoT\'ing.
- [Using the Arduino Add-on](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide#using-the-arduino-addon) \-- Tips to help you get started creating Arduino sketches of your own.

**Not Yet Implemented**\
The Arduino board definitions for the ESP32 are still a work in progress. There are a handful of peripherals and features that have yet to be implemented, including:\
\
\* Analog Input (`analogRead([pin])`)\
\* Analog Ouptut (`analogWrite([pin], [value])`)\
\* WiFi Server and WiFI UDP\
\* Real-Time Clock\
\* Touch-controller interface\
\
These peripherals are available (if, also, still in their infancy) in the [IoT Development Framework](https://github.com/espressif/esp-idf) for the ESP32. If your application requires analog input, RTC, or any of the features above, consider giving the [ESP-IDF](https://github.com/espressif/esp-idf) a try!

### Bill of Materials

The ESP32 Thing includes *almost* everything you\'ll need to begin using and programming the WiFi/BT SoC. In fact, the only required extra is a [Micro-B USB Cable](https://www.sparkfun.com/products/10215). The ESP32 Thing\'s USB interface can be used to both power and program the chip. Once you\'re done programming the chip, a [5V Micro-B USB Wall Adapter](https://www.sparkfun.com/products/15311) can be used to power the board.

[![Wall Adapter Power Supply - 5VDC, 2A (USB Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/4/TOL-15311-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-usb-micro-b.html)

### [Wall Adapter Power Supply - 5VDC, 2A (USB Micro-B)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-usb-micro-b.html) 

[ TOL-15311 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA USB Micro-B wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![USB Micro-B Cable - 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/3/0/13244-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6.html)

### [USB Micro-B Cable - 6\"](https://www.sparkfun.com/usb-micro-b-cable-6.html) 

[ CAB-13244 ]

This is a USB 2.0 type A to Micro-B 5-pin black cable. You know, the mini-B connector that usually comes with cell phones, Ca...

[ [\$2.50] ]

[![SparkFun Cerberus USB Cable - 6ft](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/3/9/12016-01.jpg)](https://www.sparkfun.com/products/12016)

### [SparkFun Cerberus USB Cable - 6ft](https://www.sparkfun.com/products/12016) 

[ CAB-12016 ]

You\'ve got the wrong USB cable. It doesn\'t matter which one you have, it\'s the wrong one. But what if you could have the righ...

**Retired**

As an alternative power source, the ESP32 Thing includes support for [single-cell lithium-polymer (LiPo)](https://www.sparkfun.com/search/results?term=lithium%20polymer&tab=products) batteries, which plug into the board\'s white 2-pin JST connector. LiPo\'s are perfect for projects on-the-go, or those that just need a little extra umph. The board includes a **LiPo charger** \-- the rechargeable batteries can be juiced back up by plugging the Thing into a 5V USB source.

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/8/13857-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-400mah.html)

### [Lithium Ion Battery - 400mAh](https://www.sparkfun.com/lithium-ion-battery-400mah.html) 

[ PRT-13851 ]

This is a very small, extremely lightweight battery based on Lithium Ion chemistry, with the highest energy density currently...

[ [\$7.98] ]

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

Finally, to connect the ESP32\'s 28 I/O pins to external components, you\'ll need to do some soldering. [Soldering tools](https://www.sparkfun.com/categories/49), including an [iron](https://www.sparkfun.com/products/9507) and [solder](https://www.sparkfun.com/products/9325), are a must for any electronics workbench. And either [headers](https://www.sparkfun.com/products/116) or [wire](https://www.sparkfun.com/products/11375) are our recommended mate for soldering into the Thing\'s pins.

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

### Suggested Reading

It may look intimidating, but the ESP32 Thing \-- especially when you take advantage of its Arduino compatibility \-- is a perfect IoT foundation for electronics users of all experience levels. There are, however, a few concepts you should be familiar with before venturing further into this tutorial. If any of the concepts below sound foreign to you, consider reading through that tutorial first:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

## Looking to get hands-on with ESP32?

We\'ve got you covered!

[![SparkFun ESP32 Thing](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/6/4/13907-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing.html)

### [SparkFun ESP32 Thing](https://www.sparkfun.com/sparkfun-esp32-thing.html) 

[ DEV-13907 ]

The SparkFun ESP32 Thing is a comprehensive development platform for Espressif's ESP32, their super-charged version of the ...

[ [\$30.85] ]

[![Thing Stackable Header Set](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/7/9/14311-01.jpg)](https://www.sparkfun.com/esp32-thing-stackable-header-set.html)

### [Thing Stackable Header Set](https://www.sparkfun.com/esp32-thing-stackable-header-set.html) 

[ PRT-14311 ]

These headers are made to work with the SparkFun ESP32 Thing to connect to ESP32 Shield boards.

[ [\$2.50] ]

[![SparkFun ESP32 Thing Power Control Shield](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/6/6/14155-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing-power-control-shield.html)

### [SparkFun ESP32 Thing Power Control Shield](https://www.sparkfun.com/sparkfun-esp32-thing-power-control-shield.html) 

[ DEV-14155 ]

The SparkFun ESP32 Thing Power Control Shield enables the ESP32 Thing to switch up to 5A of a DC load, providing a wide varie...

**Retired**

[![SparkFun ESP32 Thing Motion Shield](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/8/14430-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing-motion-shield.html)

### [SparkFun ESP32 Thing Motion Shield](https://www.sparkfun.com/sparkfun-esp32-thing-motion-shield.html) 

[ DEV-14430 ]

The SparkFun ESP32 Thing Motion Shield is a versatile, motion-sensing addition to our ESP32 Thing.

**Retired**

[See all Espressif products](https://www.sparkfun.com/categories/279)

## Hardware Overview

Espressif\'s ESP32 is one of the most unique microcontrollers on the market. Its laundry list of features include:

- Dual-core Tensilica LX6 microprocessor
- Up to 240MHz clock frequency
- 520kB internal SRAM
- Integrated 802.11 BGN WiFi transceiver
- 2.2 to 3.6V operating range
- 2.5 µA sleep current under hibernation
- 32 GPIO
- 10-electrode capacitive touch support
- Hardware accelerated encryption (AES, SHA2, ECC, RSA-4096)

The ESP32 Thing is designed to surround the ESP32 with everything necessary to run and program the microcontroller, plus a few extra goodies to take advantage of the chip\'s unique features.

[![Annotated top diagram](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/top-annotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/top-annotated.jpg)

### Peripherals and I/O

The ESP32 features your standard fare of hardware peripherals, including:

- 18 [analog-to-digital converter](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) (ADC) channels
- 3 [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) interfaces
- 3 [UART](https://learn.sparkfun.com/tutorials/serial-communication) interfaces
- Two [I^2^C](https://learn.sparkfun.com/tutorials/i2c) interfaces
- 16 [PWM](https://learn.sparkfun.com/tutorials/pulse-width-modulation) outputs
- 2 digital-to-analog converters (DAC)
- Two I2S interfaces

And, thanks to the chip\'s **pin multiplexing** feature, those peripherals can be connected to just about any of the 28 broken out I/O pins. That means *you* decide which pins are RX, TX, MISO, MOSI, SCLK, SDA, SCL, etc.

There are, however, a few hardware features \-- namely the ADC and DAC \-- which are assigned static pins. The graphical reference below helps demonstrate where you can find those peripherals (click to embiggen!).

[![Graphical Datasheet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/ESP32ThingV1a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/ESP32ThingV1a.pdf)

*Click the image for a closer look.*

One I^2^C, two of the UART interfaces, and one of the SPI interfaces can be assigned to any pin your project requires.

#### Input Only Pins: 34-39

Pins 34, 35, 36, 37, 38 and 39 *cannot* be configured as outputs, but they can be used as either digital inputs, analog inputs, or for other unique purposes. Also note that they **do not have internal pull-up or pull-down resistors**, like the other I/O pins.

GPIO pins 36-39 are an integral part of the ultra low noise pre-amplifier for the ADC -- they are wired up to 270pF capacitors, which help to configure the sampling time and noise of the pre-amp.

[![Schematic close up of pins 34-39](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/schematic-crop-34-39.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/schematic-crop-34-39.png)

*From the [ESP32 Thing Schematic](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32-thing-schematic.pdf): GPIO 36-39 are tied together with caps. Those and pins 34 and 35 are input only!*

### Powering the ESP32 Thing

The two main power inputs to the ESP32 Thing are **USB** and a **single-cell lithium-polymer (LiPo)** battery. If both USB and the LiPo are plugged into the board, the onboard charge controller will charge the LiPo battery at a rate of up to 500mA.

The ESP32\'s operating voltage range is 2.2 to 3.6V. Under normal operation the ESP32 Thing will power the chip at 3.3V. The I/O pins are **not 5V-tolerant**! If you interface the board with 5V (or higher) components, you\'ll need to do some [level shifting.](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide)

The **3.3V regulator** on the ESP32 Thing can **reliably supply up to 600mA**, which should be more than enough overhead for most projects. The ESP32 can pull as much as 250mA during RF transmissions, but we\'ve generally measured it to consume around 150mA \-- even while actively transmitting over WiFi. The output of the regulator is also broken out to the sides of the board \-- the pins labeled \"3V3.\" These pins can be used to supply external components.

[![ESP32 power inputs/outputs](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32-power-signals.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32-power-signals.jpg)

In addition to USB and battery connectors, the **VBAT**, and **VUSB** pins are all broken out to both sides of the board. These pins can be used as an alternative supply input to the Thing. The maximum, allowable voltage input to VUSB is 6V, and VBAT should not be connected to anything other than a LiPo battery. Alternatively, if you have a regulated voltage source between 2.2V and 3.6V, the \"3V3\" lines can be used to directly supply the ESP32 and its peripherals.

### Board Dimensions

The board is 2.32\"x1.00\".

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/f/f/7/2/d/SparkFun_ESP32_Thing_-_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/f/f/7/2/d/SparkFun_ESP32_Thing_-_Board_Dimensions.png)

## Assembly Tips

The ESP32 Thing ships without anything soldered into the header pins \-- ensuring that you can mold the board to best fit your project. To use the chip\'s pins you\'ll need to solder *something* to the I/O and power rail vias broken out to either side of the board.

New to soldering? Check out our [Through-Hole Soldering Tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) for a quick introduction!

*What* you solder to the ESP32 Thing\'s I/O pins is completely up to you. The header rows are breadboard-compatible, so you may want to solder [male headers](https://www.sparkfun.com/products/116) in. (Mildly satisfying: the ESP32 Thing\'s pair of 20-pin headers means you can get the most out of our 40-pin header strips.)

[![ESP32 Thing with male headers soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/esp32-thing_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32-thing_2.jpg)

Then plug it into the breadboard, hanging the USB and LiPo connectors off the end, and start wiring!

[![ESP32 Thing breadboard action shot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/esp32-thing-project.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32-thing-project.jpg)

*All those wires and components, and there are still plenty of GPIO left to use!*

Alternatively, [female headers](https://www.sparkfun.com/products/115) (you may need two separate strips to solder all 40 pins), [right-angle headers](https://www.sparkfun.com/products/553), or [stranded wire](https://www.sparkfun.com/products/11375) are all good options, depending on your project\'s needs.

## Installing via Arduino IDE Boards Manager

Good news! Espressif has added support for the Arduino Boards Manager and by installing this way, you get the benefit of a slew of great built-in examples. Instructions for installing via the board manager can be found at [espressif\'s Arduino-ESP32 Read the Docs](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html).

[Read the Docs: Installation Instructions using Arduino IDE Boards Manager](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)

For more information on installing boards via the Arduino Board Manager, check out the [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide) tutorial.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

September 9, 2020

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

If you are familiar with installing boards via the Arduino IDE Boards Manager, the url to add is:

    language:bash
    https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

**Note:** The old json file was linked to `https://dl.espressif.com/dl/package_esp32_index.json`. Make sure to update the link in your Board Manager to the latest json file from GitHub as linked above.

[] **Warning:** If you have previously installed the ESP32 Arduino Core via the instructions in Install Option 2, we strongly recommend removing the associated folders before installing via the boards manager.\
\
To remove previous arduino core installs for the esp32, start by finding your ***\.../Arduino/hardware*** folder. This can be located by looking at your Sketchbook location under **File** \> **Preferences**.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/Preferences-hardwareFolderLocation.png "Sketchbook location in Preferences")](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/Preferences-hardwareFolderLocation.png)

\
\
Go to this location in your finder and delete the **esp32** folder.\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32_folder.png "esp32 folder to be deleted")](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32_folder.png)

\
Once you have deleted the **esp32** folder, you can then install using the **Arduino Boards Manager**.

If you have successfully installed the ESP32 core to your Arduino IDE, you should see the following under **Tools** with the **ESP32 Dev Module** selected:

[![Tools menu with Board: ESP32 Dev Module option selected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/ESP32BoardsManagerInstall.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/ESP32BoardsManagerInstall.png)

## Installing the ESP32 Arduino Core

For the more advanced or adventurous route, you can skip the Arduino IDE Boards Manager and install the ESP32 Arduino Core. The pair of Tensilica cores in the ESP32 are Xtensa-based -- not your standard ARM or AVR. Fortunately, there is still a GNU compiler available for the ESP32, which opens up a world of possible development environment (IDE) set ups! The rest of this section covers setting up the Arduino IDE with ESP32 support.

In abstracting away a lot of the complicated overhead, the Arduino IDE for the ESP32 also eliminates access to some of the SoC\'s more advanced features. If you\'d like to try your hand at setting up a more **advanced toolchain** for the ESP32, we recommend checking out [Espressif\'s esp-idf GitHub repository](https://github.com/espressif/esp-idf). The esp-idf -- short for IoT Development Framework -- is Espressif\'s software development kit (SDK) for the ESP32.

### Installing the ESP32 Core

Espressif\'s official ESP32 Arduino core is hosted [here on GitHub](https://github.com/espressif/arduino-esp32). They have a fairly [simple set of installation directions](https://github.com/espressif/arduino-esp32/blob/master/README.md#installation-instructions) to help.

#### Clone or Download the Core

To install the ESP32 board definitions, you\'ll need download the contents of the esp32-arduino repository, and place them in a \"hardware/espressif/esp32\" directory in your [Arduino sketchbook directory](https://www.arduino.cc/en/Guide/Environment#toc7). You can either download those files using the [git command line tool](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), or by downloading them from GitHub.

Alternatively, these files can be installed in your Arduino's base directory. On Windows, that may be `C:/Program Files (x86)/Arduino/hardware` and on Mac that may be `/Applications/Arduino.app/Contents/Java/hardware`.

**If you have git**, open a terminal, navigate to your Arduino sketchbook, and type:

    mkdir hardware
    cd hardware
    mkdir espressif
    cd espressif
    git clone https://github.com/espressif/arduino-esp32.git esp32

Those commands will make a \"hardware\" and \"espressif\" directories, then download the arduino-esp32 GitHub repository into an \"esp32\" folder.

[![Example terminal commands](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/esp32-arduino-command-line.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32-arduino-command-line.png)

If you **don\'t have git**, [click here to download the core](https://github.com/espressif/arduino-esp32/archive/master.zip) (or click \"Download\" \> \"Download ZIP\" on the GitHub page), and unzip it to an espressif/esp32 directory in your Arduino sketchbook.

[![Windows folder installation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/esp32-folder-windows.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32-folder-windows.png)

\"boards.txt\", \"platform.txt\", and the cores, doc, tools, etc. folders should all live in the esp32 directory.

#### Install the Xtensa and ESP32 Tools

To compile code for the ESP32, you need the Xtensa GNU compiler collection (GCC) installed on your machine. **Windows users** can run **get.exe**, found in the \"esp32/tools\" folder.

[![Location of get.exe](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/esp32-get-folder-windows.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32-get-folder-windows.png)

*Windows users can run \"get.exe\" to download the ESP32 software tools.*

Mac and Linux users should run the [tools/get.py](https://github.com/espressif/arduino-esp32/blob/master/tools/get.py) python script to download the tools. Using a terminal, navigate to the **esp32/tools** folder. Then type:

    python get.py

The \"get.py\" python script will download the Xtensa GNU tools and the ESP32 software development kit (SDK), and unzip them to the proper location. You should see a few new folders in the \"tools\" directory, including \"sdk\" and \"xtensa-esp32-elf\" once it\'s done.

## Arduino Example: Blink

With the ESP32 Arduino core installed, you\'re ready to begin programming. If you haven\'t already, **plug the ESP32 Thing into your computer** using a micro-B USB cable.

[![ESP32 Thing plugged into breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/esp32-thing-breadboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/esp32-thing-breadboard.jpg)

#### FTDI Drivers

If you\'ve never connected an FTDI device to your computer before, you may need to install drivers for the USB-to-serial converter. Check out our [How to Install FTDI Drivers tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) for help with the installation.

Once the board is plugged in (and drivers installed), it should be assigned a unique port identifier. On Windows machines, this will be something like \"COM#\", and on Macs or Linux computers it will come in the form of \"/dev/tty.usbserial-XXXXXX.\"

### Select the Board and Port

Once the ESP32 Arduino core is installed, you should see an \"ESP32 Dev Module\" option under your \"Tools\" \> \"Board\" menu. Select that.

[![Arduino board select](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/arduino-board-select.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/arduino-board-select.png)

Then select your ESP32 Thing\'s serial port under the \"Tools\" \> \"Port\" menu.

[![Arduino port select](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/arduino-port-select.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/arduino-port-select.png)

You can also select the \"Upload Speed\". 921600 baud \-- the fastest selectable rate \-- will get the code loaded onto your ESP32 the fastest, but may fail to upload once-in-a-while. (It\'s still way worth it for the speed increase!)

### Loading Blink

To make sure your toolchain and board are properly set up, we\'ll upload the simplest of sketches \-- Blink! The LED attached to GPIO 5 is perfect for this test. Plus, with the ESP32 attached to your computer, it\'s a good time to test out serial. Copy and paste the example sketch below, into a fresh Arduino sketch:

    language:c
    int ledPin = 5;

    void setup()
    

    void loop()
    

With everything setup correctly, upload the code! Once the code finishes transferring, **open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics)** and set the baud rate to **115200**. You should see \"Hello, world\"\'s begin to fly by.

If the blue LED remains dimly lit, it\'s probably still sitting in the bootloader. After uploading a sketch, you may need to **tap the RST button** to get your ESP32 Thing to begin running the sketch.

[![Example serial port output](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/serial-port-example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/serial-port-example.png)

You may also notice that when the ESP32 boots up it prints out a long sequence of debug messages. These are emitted every time the chip resets \-- always at 115200 baud.

## Arduino Example: WiFi

The ESP32 Arduino core includes a handful of WiFi examples, which demonstrate everything from [scanning for nearby networks](https://github.com/espressif/arduino-esp32/blob/master/libraries/WiFi/examples/WiFiScan/WiFiScan.ino) to sending data to a client server. You can find the examples under the **File** \> **Examples** \> **WiFi** menu.

Here\'s another example using the WiFi library, which demonstrates how to connect to a nearby WiFi network and poll a remote domain (http://example.com/) as a client:

    language:c
    #include <WiFi.h>

    // WiFi network name and password:
    const char * networkName = "YOUR_NETWORK_HERE";
    const char * networkPswd = "YOUR_PASSWORD_HERE";

    // Internet domain to request from:
    const char * hostDomain = "example.com";
    const int hostPort = 80;

    const int BUTTON_PIN = 0;
    const int LED_PIN = 5;

    void setup()
    

    void loop()
    
    }

    void connectToWiFi(const char * ssid, const char * pwd)
    

      Serial.println();
      Serial.println("WiFi connected!");
      Serial.print("IP address: ");
      Serial.println(WiFi.localIP());
    }

    void requestURL(const char * host, uint8_t port)
    
      Serial.println("Connected!");
      printLine();

      // This will send the request to the server
      client.print((String)"GET / HTTP/1.1\r\n" +
                   "Host: " + String(host) + "\r\n" +
                   "Connection: close\r\n\r\n");
      unsigned long timeout = millis();
      while (client.available() == 0) 
      
      }

      // Read all the lines of the reply from server and print them to Serial
      while (client.available()) 
      

      Serial.println();
      Serial.println("closing connection");
      client.stop();
    }

    void printLine()
    

Make sure you fill in the `networkName` and `networkPswd` variables with the name (SSID) and password of your WiFi network! Once you\'ve done that and uploaded the code, open your **serial monitor**.

[![WiFi example serial terminal output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/7/wifi-example-serial.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/wifi-example-serial.png)

After your ESP32 connects to the WiFi network, it will wait for you to press the \"0\" button. Tapping that will cause the ESP32 to make an HTTP request to [example.com](http://example.com). You should see a string of HTTP headers and HTML similar to the screenshot above.

## Using the Arduino Addon

Before we leave you, here are a few tips, tricks, and gotcha\'s to look out for while you\'re using the ESP32 Arduino core.

### Pin Mapping

The pin number you use for `digitalWrite([pin], [value])` or `digitalRead([pin])` should match those printed onto the board. You can also reference the [graphical datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/ESP32ThingV1a.pdf), if the tiny numbers are a strain on the eyes.

Both I^2^C interfaces are supported by the **Wire library**. The SDA and SCL pins are assigned, by default, to pins 21 and 22.

  I^2^C Signal   ESP32 Pin
  -------------- -----------
  SDA            21
  SCL            22

And the **SPI library** should support all three possible SPI interfaces. By default, here are the pin mappings for those interfaces:

  SPI Signal   ESP32 Pin
  ------------ -----------
  MOSI         23
  MISO         19
  SCLK         18
  SS           5

In addition to SPI and I^2^C, the Arduino core also supports interrupts on any pin with the `attachInterrupt()` function.

### Not Yet Implemented

The Arduino board definitions for the ESP32 are still a work in progress. There are a handful of peripherals and features that have yet to be implemented, including:

- Analog Input (`analogRead([pin])`)
- Analog Ouptut (`analogWrite([pin], [value])`)
- WiFi Server and WiFI UDP
- Real-Time Clock
- Touch-controller interface

These peripherals are available (if, also, still in their infancy) in the [IoT Development Framework](https://github.com/espressif/esp-idf) for the ESP32. If your application requires analog input, RTC, or any of the features above, consider giving the ESP-IDF a try!