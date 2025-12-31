# Source: https://learn.sparkfun.com/tutorials/lte-cat-m1nb-iot-shield-hookup-guide

## Introduction

The [SparkFun LTE Cat M1/NB-IoT Shield](https://www.sparkfun.com/products/14997) equips your Arduino or Arduino-compatible microcontroller with access to data networks across the globe. It adds wireless, high-bandwidth cellular functionality to your IoT project while maintaining low power consumption and a small footprint.

[![SparkFun LTE CAT M1/NB-IoT Shield - SARA-R4](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/3/0/9/14997-SparkFun_LTE_CAT_M1_NB-IoT_Shield_-_SARA-R4-01a.jpg)](https://www.sparkfun.com/sparkfun-lte-cat-m1-nb-iot-shield-sara-r4.html)

### [SparkFun LTE CAT M1/NB-IoT Shield - SARA-R4](https://www.sparkfun.com/sparkfun-lte-cat-m1-nb-iot-shield-sara-r4.html) 

[ CEL-14997 ]

The SparkFun LTE CAT M1/NB-IoT Shield equips your Arduino or Arduino-compatible microcontroller with access to data networks ...

[ [\$90.95] ]

You can either purchase the SparkFun LTE Cat M1/NB-IoT Shield individually, as in the link above, or packaged with a **Hologram SIM card**. The [Hologram](https://hologram.io/) SIM card provides global connectivity on an extremely reasonable pricing model. They also provide software tools like cloud data and SMS messaging and webhooks for routing data from your cell shield to popular web services.

[![SparkFun LTE CAT M1/NB-IoT Shield - SARA-R4 (with Hologram SIM Card)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/4/5/15087-SparkFun_LTE_CAT_M1_NB-IoT_Shield_-_SARA-R4__with_Hologram_SIM_Card_-01a.jpg)](https://www.sparkfun.com/sparkfun-lte-cat-m1-nb-iot-shield-sara-r4-with-hologram-sim-card.html)

### [SparkFun LTE CAT M1/NB-IoT Shield - SARA-R4 (with Hologram SIM Card)](https://www.sparkfun.com/sparkfun-lte-cat-m1-nb-iot-shield-sara-r4-with-hologram-sim-card.html) 

[ CEL-15087 ]

The SparkFun LTE CAT M1/NB-IoT Shield with Hologram SIM Card equips your Arduino-based device with access to data networks ac...

**Retired**

**Revision Update:** In the latest revision of the SparkFun LTE Cat M1/NB-IoT Shield, we have fixed the **AREF** pin that was accidentally tied to ground. If users are unsure about which version they purchased, please refer to the pictures of the updated changes, shown below.

[![pin difference](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/update-aref_close-up.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/update-aref.jpg)\
*The `AREF` pin is no longer connected to the ground plane with traces, unlike the `GND` pin next to it.*

[![version marking](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/version_mark.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/version_mark.jpg)\
*Version label on the bottom of the board (`v11`).*

At the heart of the LTE Cat M1/NB-IoT shield is a [u-blox SARA-R410M-02B](https://www.u-blox.com/en/product/sara-r4n4-series) LTE Cat M1/NB-IoT modem. Cat M1 (Category M1) and NB-IoT (Narrowband IoT) are both Low Power Wide Area Network (LPWAN) technologies that are designed to provide cellular communication to small IoT devices. They operate on LTE network bands just like most smartphones, and should be supported by most cellular network carriers.

The u-blox module commmunicates over a UART via a simple AT command set. We\'ve provided a library to help you get started with everything from **sending SMS text messages** to communicating with servers over a **TCP/IP connection**.

Both the module and library support an I^2^C GPS interface, so you can plug in a u-blox GPS module and start remotely tracking your project.

### Required Materials

In addition to the shield itself, we recommend the following items to follow along with this tutorial. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Arduino or Arduino-Compatible Development Board** \-- The LTE Cat M1/NB-IoT Shield is primarily designed to work as a\...shield. It should be compatible with most Arduino-type development boards, including the [Arduino Uno](https://www.sparkfun.com/products/11224), [SparkFun RedBoard](https://www.sparkfun.com/products/13975), [SparkFun BlackBoard](https://www.sparkfun.com/products/14669), and [SAMD21 Dev Breakout](https://www.sparkfun.com/products/13672).

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Arduino Uno - R3 SMD](https://cdn.sparkfun.com/r/140-140/assets/parts/6/8/1/6/Arduino_Uno_R3-_1.jpg)](https://www.sparkfun.com/arduino-uno-r3-smd.html)

### [Arduino Uno - R3 SMD](https://www.sparkfun.com/arduino-uno-r3-smd.html) 

[ DEV-11224 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$26.30] ]

[![SparkFun SAMD21 Dev Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/1/5/13672-01.jpg)](https://www.sparkfun.com/sparkfun-samd21-dev-breakout.html)

### [SparkFun SAMD21 Dev Breakout](https://www.sparkfun.com/sparkfun-samd21-dev-breakout.html) 

[ DEV-13672 ]

If you're ready to step your Arduino game up from older 8-bit/16MHz microcontrollers, the SparkFun SAMD21 Dev Breakout is a...

[ [\$29.95] ]

[![SparkFun BlackBoard](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/6/7/14669-BlackBoard-01.jpg)](https://www.sparkfun.com/products/14669)

### [SparkFun BlackBoard](https://www.sparkfun.com/products/14669) 

[ SPX-14669 ]

This was a great board but we made it better! Checkout the new version, \[BlackBoard C\](https://www.sparkfun.com/products/1509...

**Retired**

The shield can also be used as a breakout board for the u-blox SARA-R4 module, in which case nearly any microcontroller development board with a free UART should work. You can even use the shield\'s **USB interface** with a [Raspberry Pi](https://www.sparkfun.com/products/13825), [Raspberry Pi Zero](https://www.sparkfun.com/products/14277) or, really, any Windows/Mac/Linux device with a free USB port.

**Headers** \-- To connect the shield to your Arduino you\'ll need to solder headers into it. We recommend the [stackable R3 headers](https://www.sparkfun.com/products/11417), but [male headers](https://www.sparkfun.com/products/115) can also do the trick.

[![Arduino Stackable Header Kit - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/7/2/1/6/11417-01a.jpg)](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html)

### [Arduino Stackable Header Kit - R3](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html) 

[ PRT-11417 ]

These headers are made to work with the Arduino Uno R3, Leonardo and new Arduino boards going forward. They are the perfect h...

[ [\$2.75] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

**Soldering Tools** \-- You\'ll also need soldering tools to connect the headers to your shield. A [basic soldering iron](https://www.sparkfun.com/products/14456) and [solder](https://www.sparkfun.com/products/9163) should be enough.

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

**SIM card** \-- A **nano SIM** card will be required to provide connectivity for the LTE CAT-M1 Shield\'s u-blox module. If you\'ve purchased the [Hologram/SparkFun LTE Shield Combo](https://www.sparkfun.com/products/15087), then you\'re all set. Otherwise, there are a variety of connectivity suppliers including [AT&T](https://marketplace.att.com/products?tags=connectivity&tags=lte-m&tags=lte-na&tags=lte-intl), [T-Mobile](https://iot.t-mobile.com/pricing/), and [Verizon](https://www.verizonwireless.com/biz/plans/m2m-business-plans/).

#### Optional Materials

In addition to those required items, these bits and pieces can help add functionality to your LTE Shield, so you can take it even further:

**LiPo Battery** \-- The LTE Shield includes a LiPo battery charger. This LiPo can be used to power both your Arduino and the shield simultaneously. Any of the below batteries should work with the shield:

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

**Micro-B USB cable** \-- The shield\'s SARA-R4 module supports a USB interface, which can be used for both power and a communication interface. A [micro-B USB cable](https://www.sparkfun.com/products/10215) isn\'t required, but may be helpful if you want to power your project via USB or give the SARA-R4 module\'s USB interface a spin.

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

[![SparkFun Traveler microB Cable - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/6/9/14741-USB_micro-B_TPE_Cable_-_3_Foot-01.jpg)](https://www.sparkfun.com/products/14741)

### [SparkFun Traveler microB Cable - 1m](https://www.sparkfun.com/products/14741) 

[ CAB-14741 ]

Are you a traveler? Do you remove every ounce of extra weight from your gear? The SparkFun 1 meter Traveler microB cable is d...

**Retired**

[![SparkFun Rugged microB Cable - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/1/14742-USB_micro-B_Braided_Cable_-_3_Foot-01.jpg)](https://www.sparkfun.com/products/14742)

### [SparkFun Rugged microB Cable - 1m](https://www.sparkfun.com/products/14742) 

[ CAB-14742 ]

Is your laptop covered in stickers that hide the dents? Do you put your equipment through its paces? The SparkFun 1 meter Rug...

**Retired**

### Suggested Viewing

### Suggested Reading

This tutorial builds on a variety of electronics, programming, and engineering concepts. If any of the subjects of these tutorials sound foreign to you, consider checking them out before continuing on:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.

If you aren\'t familiar with the Qwiic system, we also recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

## Hardware Overview

It may not look like it, but there\'s a lot going on on the LTE Cat M1/NB-IoT Shield. This page covers all of the hardware features included on the board. Take a quick peruse through it to make sure you don\'t get tripped up by the UART- or power-select switches, the power/reset buttons, or the external USB and GPS interfaces.

~~**Oops!** We accidentally tied the `AREF` pin to **GND**. This shouldn\'t affect the overall functionality of the shield; however, it does affect the use of the analog pins on the microcontroller board (**A0** - **A5**).~~

**Update:** We have fixed the `AREF` pin issue with version `v11` of the shield.

[![Updated shield - version indicator](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/8/1/6/version_mark.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/version_mark.jpg)\
*Version marking on the bottom of the shield.*

### Power Supply

The u-blox SARA-R410M-02B module uses a relatively low amount of power. Peak current consumption is about **200mA** (a far cry from past cellular shields which occasionally pulled upwards of 2A) at a voltage supply of **3.3V**. Logic on the module is all 1.8V, but never fear \-- we\'ve included logic-level shifting included on-board (see the [Logic-Level Selection section](https://learn.sparkfun.com/tutorials/lte-cat-m1nb-iot-shield-hookup-guide#logiclevel) for more information).

[![Power supply highlighted \-- switch, LiPo, USB, and Arduino power header](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-power-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-power-02.jpg)

The shield is designed to take power from one of three sources:

1.  **Arduino** \-- The shield receives power from the Arduino\'s 5V supply pin.
2.  **LiPo Battery** \-- A 3.7-4.2V LiPo battery can be connected to the black 2-pin JST connector.
3.  **On-board micro-B USB connector** \-- A [micro-B USB cable](https://www.sparkfun.com/products/10215) can be connected from your computer or a USB wall wart to supply power to the shield. This may be useful if you\'re using the shield as more of a \"breakout board.\" (This connector can also be used to provide a USB interface to the u-blox module \-- see the [USB Interface section](https://learn.sparkfun.com/tutorials/lte-cat-m1nb-iot-shield-hookup-guide#USB-interface) below).

The **PWR_SEL** switch should be used to select the power source. In the **Arduino** position, the shield will **receive power from the Arduino**. In the **SHIELD** position, the **shield will supply power to the Arduino**.

#### LiPo Charging

The shield includes an MCP73831 LiPo charger, which is configured to power a single-cell LiPo battery at up to **500mA**.

The battery can be charged by either connecting a micro-B USB cable to the shield, or by connecting the shield to a powered Arduino and setting the PWR_SEL switch to ARDUINO.

### Power and Reset Buttons

The LTE Cat M1/NB-IoT Shield includes a pair of SPST buttons labeled **RESET** and **POWER**. These are connected directly to the SARA-R4 module\'s PWR_ON and RESET_N pins.

[![Hardware power and reset buttons, and Arduino pins highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-buttons.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-buttons.jpg)

By default the SARA-R4 module is turned off, to turn it on \-- as you might any other cell phone \-- you need to **hold the POWER button down for about 3 seconds**.

The RESET button resets the SARA-R4 module to its default configuration. In most cases you should not need to use this button. If you do, hold it down for at least 10 seconds while the module is on. Note that this button has no affect on the Arduino \-- it won\'t reset your sketch.

Both of these pins are also wired to the Arduino:

  Pin Function   Button Label   Arduino Pin   Description
  -------------- -------------- ------------- --------------------------------------------------------------------------
  Power On       POWER          5             Power the SARA-R4 module on or off. Hold for \~3 seconds.
  Reset          RESET          6             Reset the SARA-R4 module configuration to default. Hold for \>10 seconds

The library is designed to toggle the POWER pin if the shield is not communicating, so you may be able to avoid pressing this button at all.

### UART Interface

All communication between your Arduino and the SARA-R4 module will occur via an AT command interface over a simple UART \-- RX and TX pins.

[![hardware/software serial interfaces, select switch, and debug port](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-serial.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-serial.jpg)

Designed with a simple Arduino Uno in mind, this shield can either communicate with the SARA-R4 module via either a hardware or software serial interface. The **SERIAL** switch can either be set to **HARD** for hardware serial on pins 0/1 or **SOFT** for software serial on pins 8/9.

  ----------------- --------------------------------- ---------------------------------
                    Arduino Receive (Cell Transmit)   Arduino Transmit (Cell Receive)
  Software Serial   8                                 9
  Hardware Serial   0                                 1
  ----------------- --------------------------------- ---------------------------------

#### FTDI Header

The UART signals are also broken out to a 6-pin \"FTDI\" serial header. If you\'re not using the shield as a shield \-- more-so as a breakout \-- this header may be useful. You can connect any 3.3V or 5V USB-to-Serial converter (like the [Serial Basic](https://www.sparkfun.com/products/14050)) to this header, and directly communicate with the SARA-R4\'s UART.

This header is not affected by the SERIAL-select switch. External power must be supplied to the LTE shield \-- either via USB or LiPo battery.

### LED Indicators

A trio of LEDs are broken out between the USB and GPS connectors. The table below documents each of these LEDs color and indication:

  LED Label   LED Color   LED indication
  ----------- ----------- ------------------------------------------------------------------------------------------------------------------------------------
  PWR         Red         Power supplied to SARA-R4 module
  CHG         Yellow      LiPo battery charging (may illuminate if no battery is connected)
  NET         Blue        Cellular network status. Illuminates when the SARA-R4 module is connected to a cellular network. (Must be configured in software.)

The most important of these LEDs is the blue \"NET\" indicator. This LED will illuminate when your SARA-R4 module is properly configured, is connected to a SIM card, and is communicating with a cell network. By default, the pin SARA-R4 connected to this LED is not configured, but the library should take care of that upon initialization.

### [][Logic-Level Selection](#logiclevel)

The SARA-R4 module\'s GPIO pins all operate at **1.8V logic levels**. Fortunately, the shield includes level shifting which should convert either 3.3V or 5V signals to 1.8V.

On most Arduino, selection of the high end of the logic-level translation should be automatic. Voltage supplied from the Arduino\'s **IOREF** pin should set it. If so, ignore what comes next.

[![IOREF jumper](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-ioref.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-ioref.jpg)

If your Arduino **does not have an IOREF pin**, or does not supply a valid logic level on that pin, you should use the **IOREF** jumper to select your Arduino\'s logic level.

### GPS Port

If you want to easily add location-tracking to your project, the LTE Shield\'s Qwiic GPS port can connect to a handful of u-blox GPS modules. We\'re adding more compatible modules soon. For now, the supported modules are:

[![SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/5/1/4/15136-SparkFun_GPS-RTK2_Board_-_ZED-F9P__Qwiic_-03.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html)

### [SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html) 

[ GPS-15136 ]

The SparkFun GPS-RTK2 is a powerful breakout for the ZED-F9P module. The ZED-F9P is a top-of-the-line module for GNSS & GPS s...

[ [\$259.95] ]

[![SparkFun GPS Breakout - Chip Antenna, SAM-M8Q (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/4/8/15210-SparkFun_GPS_Breakout_-_Chip_Antenna__SAM-M8Q__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gps-breakout-chip-antenna-sam-m8q-qwiic.html)

### [SparkFun GPS Breakout - Chip Antenna, SAM-M8Q (Qwiic)](https://www.sparkfun.com/sparkfun-gps-breakout-chip-antenna-sam-m8q-qwiic.html) 

[ GPS-15210 ]

The SparkFun SAM-M8Q GPS Breakout is a high quality GPS board with equally impressive configuration options.

[ [\$43.95] ]

[![SparkFun GPS-RTK Board - NEO-M8P-2 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/2/0/15005-SparkFun_GPS-RTK__Qwiic__-_NEO-M8P-2-00.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-board-neo-m8p-2-qwiic.html)

### [SparkFun GPS-RTK Board - NEO-M8P-2 (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk-board-neo-m8p-2-qwiic.html) 

[ GPS-15005 ]

The SparkFun GPS-RTK Board is a powerful breakout for the NEO-M8P-2 module from u-blox. The NEO-M8P-2 is a top-of-the-line mo...

[\$269.95] [ [\$179.95] ]

The LTE Shield Arduino library includes support for reading this GPS module via the SARA-R4\'s AT command set.

Note that this Qwiic connector is only designed to support u-blox-based GPS modules. It does not support any other GPS modules or sensors.

### LTE Antenna

The LTE Shield includes a ceramic, SMD antenna \-- a [Molex 1462000001](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/1462000001-PS.pdf). The antenna has a gain of 3.8dBi around 1.7GHz to 2.7GHz.

If your project requires an external antenna, the onboard antenna can be disconnected and the included U.FL antenna can be used. To disconnect the onboard ceramic antenna, grab a [hobby knife](https://www.sparkfun.com/products/9200) and slice across the big metal pad near the U.FL connector \-- between the two, white, silkscreen dots as highlighted in the image below along a black line.

[![Internal Antenna Jumper Highlighted to Indicate Where to Cut ](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/14997-SparkFun_LTE_CAT_M1_NB-IoT_Shield_-_SARA-R4-04_Antenna_Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/14997-SparkFun_LTE_CAT_M1_NB-IoT_Shield_-_SARA-R4-04_Antenna_Jumper.jpg)

Once the [jumper has been cut](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces), add a solder jumper to connect the center pad to the pad located just above the u.FL connector, and [carefully connect the u.FL part of your external antenna](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl). Your setup should look like the image below.

[![Antenna jumper cut with u.fl antenna attached](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/hardware-overview-antenna-ufl.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-overview-antenna-ufl.jpg)

Once you\'ve adjusted the jumpers, it\'s safe to add your own antenna via a U.FL connector. A couple options include the [LTE Antenna 175mm Duck SMA Male - VT4GLTE-R-10](https://www.sparkfun.com/products/15054) and [LTE Antenna 100mm FPC u.FL - VT4GFIA-6](https://www.sparkfun.com/products/15053).

[![Interface Cable SMA to U.FL - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/2/09145-01b.jpg)](https://www.sparkfun.com/interface-cable-sma-to-u-fl.html)

### [Interface Cable SMA to U.FL - 100mm](https://www.sparkfun.com/interface-cable-sma-to-u-fl.html) 

[ WRL-09145 ]

This is a 4\" connector cable that interfaces U.FL RF connectors to regular SMA connectors. This cable is commonly used to con...

[ [\$5.75] ]

[![LTE Antenna 175mm Duck SMA Male - VT4GLTE-R-10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/9/7/15054-Antenna_LTE_175mm_Duck_SMA_Male_-_VT4GLTE-R-10-01.jpg)](https://www.sparkfun.com/lte-antenna-175mm-duck-sma-male-vt4glte-r-10.html)

### [LTE Antenna 175mm Duck SMA Male - VT4GLTE-R-10](https://www.sparkfun.com/lte-antenna-175mm-duck-sma-male-vt4glte-r-10.html) 

[ CEL-15054 ]

This high-gain duck antenna is designed for LTE devices that operate in the 690-960MHz and 1710-2690 MHz bands. Combined w...

[ [\$8.95] ]

[![LTE Antenna 100mm FPC U.FL - VT4GFIA-6](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/9/6/15053-Antenna_LTE_100mm_FPC_u.FL_-_VT4GFIA-6_-04.jpg)](https://www.sparkfun.com/products/15053)

### [LTE Antenna 100mm FPC U.FL - VT4GFIA-6](https://www.sparkfun.com/products/15053) 

[ CEL-15053 ]

This high-gain FPC (flexible PC) antenna is designed for LTE devices that operate in the 690-960MHz and 1710-2690 MHz bands....

**Retired**

### [][USB Interface](#USB-interface)

The SARA-R4 features a USB interface which, with the proper drivers installed, can provide your Raspberry Pi or, really, any other machine with a USB interface to Cat M1/NB-IoT. Using the LTE Shield\'s USB interface is almost as simple as plugging in a USB cable to your computers USB port.

Unfortunately, the UART and USB interfaces can not be used concurrently. To use the USB interface, **close the VUSB_DET** jumper on the back side of the board.

[![VUSB_DET Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/14997-SparkFun_LTE_CAT_M1_NB-IoT_Shield_-_SARA-R4-03_VUSB-DET_Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/14997-SparkFun_LTE_CAT_M1_NB-IoT_Shield_-_SARA-R4-03_VUSB-DET_Jumper.jpg)

## Hardware Hookup

To assemble the LTE Shield, you\'ll need basic soldering tools and skills. New to soldering? No worries! Check out our through-hole soldering tutorial.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

### Solder on Headers

To connect the SparkFun LTE Shield to your Arduino, you\'ll need to solder headers into the through-hole Arduino pins. We recommend either [Stackable headers](https://www.sparkfun.com/products/11417) \-- if you want to stack more shields on top \-- or [male headers](https://www.sparkfun.com/products/115).

Soldering into the two 8-pin, one 6-pin, and one 10-pin header should be enough to get your shield snugly fitting and electrically connected.

[![hardware hookup \-- stackable headers installed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/hardware-hookup-headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-hookup-headers.jpg)

**Heads up!** The AREF pin is currently tied to GND. If you are going to read the analog pins using a microcontroller, you will want to bend the pin out of the socket or cut the header.\
\

[![AREF pin rerouted and bent out of socket of an Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/LTE_Shield_tutorial-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/LTE_Shield_tutorial-09.jpg)

### Plug in a SIM Card

You\'ll also need to slide an activated SIM card into your shield. As you insert the SIM card, its \"notch\" should match the pattern on the board\'s silkscreen as well as that on the SIM card holder itself.

[![Inserting a SIM card](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/hardware-hookup-sim.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-hookup-sim.jpg)

Don\'t forget to activate your SIM if that\'s required by your network provider!

#### Activate Your Hologram SIM

If you\'re using a SIM card from Hologram, you\'ll need to follow a few quick steps to activate your SIM card.

1.  [Log in](https://dashboard.hologram.io/) to your Hologram account, or [create one](https://dashboard.hologram.io/account/register)

2.  Click the blue **+ Activate SIM** button in the upper-right-corner of your Dashboard.

    \

    [![Activate hologram SIM](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/hologram-activate-sim.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hologram-activate-sim.png)

    \

3.  Select your plan -- in most cases "Maker Flexible" is the way to go, but you can upgrade.

4.  Enter your SIM card's CCID. This number can be found printed on both your nano-SIM card and in the larger digits below the bar code. Then select continue.

5.  Next you can decide whether to enable auto-refill or not and continue. Finally, you'll be greeted with a summary page -- hit "Activate" and you're ready to go!

For more help activating your Hologram SIM card, check out their [Connect Your Device](https://hologram.io/docs/guide/connect/connect-device/) documentation.

### Supply Power

Once you\'ve soldered on the headers, and plugged in at least a SIM card. It\'s time to supply power and start LTE\'ing!

The shield can be powered via either an Arduino or the on-board USB or LiPo battery connectors. For the purposes of this tutorial, we\'d recommend powering via Arduino.

Set the PWR_SEL switch to ARDUINO. Plug the shield into your Arduino, then plug your Arduino into your computer via USB.

[![Powering shield and Arduino via Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/hardware-hookup-power-via-Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/hardware-hookup-power-via-Arduino.jpg)

Once plugged in, you should see the shield\'s red PWR LED illuminate (you may also see the yellow CHG LED turn on as well \-- even without a battery plugged in \-- no worries.) The blue NET LED will probably not turn on yet. For that, we need to configure the shield. And for that, we need the SparkFun LTE Shield Arduino Library. Read on!

## LTE Shield Arduino Library

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The SparkFun LTE Shield Arduino library is designed to simply interface your Arduino to the Cat M1/NB-IoT Shield. The shield handles everything from initialization (turning on the SARA-R4 module, configuring your network, setting GPIO modes) to sending/receiving SMS and communicating over a TCP network interface.

The SparkFun LTE Shield Library is available in the Arduino library manager. In the Arduino IDE, navigate to **Sketch** \> **Include Library** \> **Manage Libraries**. Then in the search box, begin searching for \"SparkFun LTE Shield.\" Once your search is narrowed down, select the SparkFun LTE Shield library and click \"Install.\"

[![Insatlling the LTE Shield Library via library manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/lte-shield-library-manager.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/lte-shield-library-manager.png)

Otherwise, you can manually download the library, navigate to [GitHub repository](https://github.com/sparkfun/SparkFun_LTE_Shield_Arduino_Library) and download the repository as a ZIP folder (or click the link below):

[Download the SparkFun LTE Shield Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_LTE_Shield_Arduino_Library/archive/master.zip)

To manually install the library via a ZIP folder, open Arduino, navigate to **Sketch** \> **Include Library** \> **Add .ZIP Library**, and select the ZIP folder you just downloaded.

## Example 0: Network Registration

The first example in this tutorial is the most critical. Here we demonstrate how to configure your LTE Shield\'s SARA-R4 module to communicate with your network of choice. This is a configuration that usually only needs to happen once. After you\'ve successfully run this sketch, your Arduino should be all set up for SMS and TCP/IP messaging.

To begin, load up this example by going to **File** \> **Examples** \> **SparkFun_LTE_Shield_Arduino_Library** \> **00_Register_Operator**.

[![Opening example 0](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/example_00_open_via_Arduino.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_00_open_via_Arduino.png)

Before uploading the sketch, you may need to adjust the value of `MOBILE_NETWORK_OPERATOR` and `APN`. The first variable, sent as a parameter to `lte.setNetwork`, defines the mobile network operator your LTE shield should configure itself to communicate with. It should be one of the below values:

    language:c
    // Network operator can be set to either:
    // MNO_SW_DEFAULT -- DEFAULT
    // MNO_ATT -- AT&T 
    // MNO_VERIZON -- Verizon
    // MNO_TELSTRA -- Telstra
    // MNO_TMO -- T-Mobile
    const mobile_network_operator_t MOBILE_NETWORK_OPERATOR = MNO_SW_DEFAULT;
    const String MOBILE_NETWORK_STRINGS[] = ;

Your access point name (APN), is provided by your SIM card provider. If you\'re using a Hologram SIM, this should be a string\'ed `"hologram"`. This value is provided to the `lte.setAPN()` function.

    language:c
    // APN -- Access Point Name. Gateway between GPRS MNO
    // and another computer network. E.g. \"hologram\"
    const String APN = "hologram";

After uploading the sketch, open up your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) to check the status of your shield\'s registration. This example is **interactive**. After possible network operators are scanned, you\'ll need to enter one of a handful of options to attempt connecting to that operator.

[![Registration example in terminal](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/registering-operator-serial-terminal.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/registering-operator-serial-terminal.gif)

You\'ll need to be a little patient after uploading this sketch. Depending on the state of your shield, it can take about 30 seconds for the sketch to initialize your shield. It can also take up to three minutes for the shield to scan for network operators in its area.

Some times your choice of network operator will be limited to a set of numerical-only options \-- a combination of **mobile country codes (MMC)** and **mobile network codes (MNC)**. For example, AT&T in the example above is an MCC/MNC combination of 310 and 410, respectively \-- that\'s the operator we select. (\"313 100\" is an AT&T First Responders Network and \"310 260\" is T-Mobile.)

#### Notes on Mobile Country Codes (MCC) and Mobile Network Codes (MNC)

Sometimes your choice of network operator will be limited to a set of numerical-only options. This will be a combination of **mobile country codes (MCC)** and **mobile network codes (MNC)**. For example, AT&T in the example above is an MCC/MNC combination of 310 and 410, respectively -- that's the operator we select. ("313 100" is an AT&T First Responders Network and "310 260" is T-Mobile.)

If you need to do some digging to discover which MMC/MNC is which, check out the searchable, comprehensive list at [mcc-mnc.com](http://www.mcc-mnc.com/) and/or [The Roaming Zone](http://www.roamingzone.com/mnc/).

**Note:** if you leave a region covered by a pair of country/network codes, you may need to reconfigure your shield using this sketch.

#### What\'s Going On at Start-Up

The LTE Shield can take a handful of seconds to start up if you\'ve just plugged it in and haven\'t triggered the power button.

As it initializes communication with the shield, the Arduino library must attempt to verify that the shield is on while also tuning the baud rate down from a potentially unknown baud rate (though, most likely, 115200 bps) to 9600 bps.

On start-up, the library will cycle through the SARA-R4\'s supported baud rates, and attempt to establish communication. This process may take up to 5 seconds. If the shield doesn\'t respond, the library will assume it\'s powered off. It will cycle the POWER button, then start the \"autobaud\" process over again.

In all, this process can take up to 30 seconds. You should end up with a SARA-R4 module configured at 9600 baud, and ready to begin LTE\'ing.

**Note: You can shorten this initial power-on time by manually turning on the SARA-R4\'s power (hold the POWER button down for \~3 seconds).**

### Initializing the LTE Shield Library

There are a few declarations and function calls you\'ll need in every LTE Shield library sketch.

#### Global Definitions

There\'s, of course, the library include statement:

    language:c
    #include <SparkFun_LTE_Shield_Arduino_Library.h>

If you\'re using a software serial port \-- as the examples demonstrate \-- you\'ll also need to define a `SoftwareSerial` object with RX on pin 8 and TX on pin 9:

    language:c
    // We need to pass a Serial or SoftwareSerial object to the LTE Shield 
    // library. Below creates a SoftwareSerial object on the standard LTE
    // Shield RX/TX pins:
    SoftwareSerial lteSerial(8, 9);

And, finally, you\'ll need to declare an `LTE_Shield` object, which we\'ll use throughout the sketch for SMS-sending, and TCP/IP interactions. This object optionally takes two parameters \-- the POWER and RESET Arduino pins. By default these parameters should match the shield defaults, so they are not usually required.

    language:c
    // Create a LTE_Shield object to be used throughout the sketch:
    #define POWER_PIN 5
    #define RESET_PIN 6
    LTE_Shield lte(POWER_PIN, RESET_PIN);

#### Setup Requirements

With your global variables declared, initializing the shield library is as simple as calling `lte.begin(SerialPort)`. SerialPort should either be the SoftwareSerial port you declared in globals, or a hardware serial port if that\'s supported by your Arduino board.

`begin()` will return `true` on a successful initialization of the shield or `false` if communication with the SARA-R4 module fails.

The examples in this library all assume a **software serial port** on pins 8 and 9. So the begin statement below should work.

    language:c
    if ( lte.begin(lteSerial) ) 

If, on the other hand, you\'re using a **hardware serial port** (on pins 0/1) to communicate with the shield, the begin statement below may be used:

    language:c
    if ( lte.begin(Serial1) ) 

The library will take care of all the `begin()`, `write()`, and `read()` functions provided by your serial port.

## Example 1: Send an SMS

Our next example in the LTE Shield Arduino library demonstrates how to send an SMS. Note that this example does require your SIM card\'s plan supports outbound SMS text messages \-- they may incur a fee, so be mindful of how often you run the sketch.

To load this sketch, navigate to **File** \> **Examples** \> **SparkFun LTE Shield Arduino Library** \> **01_SMS_Send**.

Before uploading the code, modify the value of `DESTINATION_NUMBER` to that of your desired text message destination.

    language:c
    // Set the cell phone number to be texted
    String DESTINATION_NUMBER = "11234567890";

Note that the SMS destination number should include the country code (e.g. \"`1`\" for US). For example, to text SparkFun (if SparkFun\'s corporate phones could receive SMS messages) at 303-284-0979, you\'d set the `DESTINATION_NUMBER` string to `"13032840979"`.

Once your destination phone number is set, upload the code and open your serial monitor (**9600** baud). In the serial monitor, **set the line-ending dropdown to \"Newline.\"**.

[![Sending a text message via the LTE Shield library](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_01_serial_monitor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_01_serial_monitor.png)

Then type a message and send it. After a few seconds you should see a text message appear on your destination phone.

### Using the Arduino Library\'s SMS-Send Functionality

The `sendSMS` function should be pretty straightforward to use. The function takes two parameters: a String\'ed phone number and a String\'ed message to send.

    language:c
    LTE_Shield_error_t LTE_Shield::sendSMS(String number, String message);

Consider building a String variable before sending it to the `sendSMS` function. You can add variables \-- including `digitalRead()`\'s and `analogRead()`\'s to the String by using the `String()` operator. The powerful [String object](https://www.arduino.cc/reference/en/language/variables/data-types/stringobject) includes easy concatenation with the `+=` operator (or [`concat()`](https://www.arduino.cc/reference/en/language/variables/data-types/string/functions/concat/)). For example:

    language:c
    String messageToSend;
    int time = millis();
    messageToSend = "A0 = " + String(analogRead(A0)); // Add A0 to 
    messageToSend += "\r\n"; // Create a new line
    messageToSend += "Time = " + String(time);
    lte.sendSMS(DESTINATION_NUMBER, messageToSend);

The `sendSMS` function does return an error/success response. Check for a return value of `LTE_SHIELD_SUCCESS` (set to 0) on success, or a value greater than 0 on an error.

## Example 2: Send a Hologram Message

Our next example demonstrates how to send a message to the Internet via the SARA-R4\'s support for TCP/IP protocols.

This example requires a Hologram SIM card and account. If you don\'t have a Hologram SIM, check out the last section of this example for tips on using the shield\'s TCP socket capabilities.

Load this example by opening **File** \> **Examples** \> **SparkFun LTE Shield Arduino Library** \> **02_TCP_Send_Hologram**.

Before uploading this example, you\'ll need your Hologram device\'s **device key**. This can be found in your Hologram dashboard. Navigate to your device, and click the \"DEVICE KEY +\" in the top-left-ish corner.

[![Finding the Hologram device key](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/example_02_hologram_device_key.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_02_hologram_device_key.png)

With that set, upload away! Then open the serial monitor at **9600** baud. As with the previous example, **set your line-ending setting to Newline**.

Open up your Hologram dashboard, then, from the serial monitor, type a message you\'d like to send to the Hologram messaging server.

[![Message from serial port to Hologram](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_02_serial_monitor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_02_serial_monitor.png)

After a few seconds, you should see the message appear in your device\'s Hologram dashboard.

[![Hologram message receive](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/example_02_hologram_receive.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_02_hologram_receive.png)

### Using TCP/IP Sockets

This example demonstrates how to use the LTE Shield\'s TCP/IP socket capabilities. [Sockets](https://en.wikipedia.org/wiki/Network_socket) are a very common interprocess communication tool for sending and/or receiving data across a variety of networking protocols. In this case, we\'ll be using socket to send data over a TCP network link. The SARA-R4 module supports up to seven concurrently-open sockets \-- usually we\'ll only need one-or-two at a time.

To begin, open a socket with the `socketOpen` function. This function takes one parameter \-- an indication of whether you want to open a TCP or UDP socket. Possible parameters are `LTE_SHIELD_TCP` or `LTE_SHIELD_UDP`.

    language:c
    int socket;
    socket = lte.socketOpen(LTE_SHIELD_TCP);
    if (socket < 0) 

`socketOpen` should return a value between 0 and 6. This is your socket \-- protect it well!

Once your socket is open, it\'s time to use it to connect to a server. For that, there\'s the `socketConnect` function. This function takes a socket number, URL or IP address, and port to connect to. In this example we use the socket received from `socketOpen` and use it to connect to hologram.io on port `9999`.

    language:c
    const char HOLOGRAM_URL [] = "cloudsocket.hologram.io";
    const unsigned int HOLOGRAM_PORT = 9999;
    if (lte.socketConnect(socket, HOLOGRAM_URL, HOLOGRAM_PORT) == LTE_SHIELD_SUCCESS) 

Once you\'re connected to the server, it\'s time to send some data! For that, there\'s the `socketWrite` function. This function takes, again, a socket, and a String\'ed message. You\'ll need to be careful with the message if you\'re sending it to the Hologram servers. It should be a JSON-encoded String of the format described here: <https://hologram.io/docs/reference/cloud/embedded/#send-a-message-to-the-hologram-cloud>. (See the example code for help constructing a compatible JSON string.)

    language:c
    String message = ""
    if (lte.socketWrite(socket, message) == LTE_SHIELD_SUCCESS) 

Finally, you can close a socket using the `socketClose` function. Sometimes a server will close the socket on its side, but it helps to sometimes be pre-emptive in your socket-closing.

    language:c
    if (lte.socketClose(socket) == LTE_SHIELD_SUCCES) 

## Example 3: Receive a Hologram Message

Now that you\'ve sent a message via TCP/IP services, this example demonstrates how to create a local listening socket on your LTE Shield to receive data.

Again, this example uses Hologram to send a message from a web portal down to the shield. If you don\'t have a Hologram SIM, consider checking out the library-how-to at the end.

To load up the TCP receive example go to **File** \> **Examples** \> **SparkFun LTE Shield Arduino Library** \> **03_TCP_Receive_Hologram**.

You shouldn\'t need to modify anything in this example. Just upload away! After uploading open up your serial monitor. Then open up your Hologram dashboard.

Next, from your device\'s Hologram dashboard type a message to send \*\*via Cloud Data\* and send that data message (keep the Port as 4010 and protocol as TCP).

[![Hologram send data](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/6/example_03_hologram_send.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_03_hologram_send.png)

After not too-long, you should see the message pop up in your Serial Monitor.

[![Serial monitor receive data from Hologram](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_03_serial_monitor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/example_03_serial_monitor.png)

### Listening, Callbacks, and Polling

This example builds on using sockets from the last example, and introduces a couple new concepts as well.

`socketListen` can be used after opening a socket to set up a listening port on the SARA-R4 module. This function takes a socket to use and a port to listen on \-- `4010` in this example.

    language:c
    if (lte.socketListen(socket, 4010) == LTE_SHIELD_SUCCESS) 

While a socket is open and listening, data comes into the SARA-R4 module asynchronously. To catch this data, the library implements a `poll` function, which should be called as often as possible in the `loop()`. `poll()` is designed to monitor the UART, and, if it sees data come in from a socket, relay that back to the Arduino sketch.

To pull in data from the `poll()` function, a callback is used. This callback should provide two parameters: an `int` socket and a `String` message. The example below demonstrates how to declare a socket-read callback, register it, and poll for data:

    language:c

    void processSocketRead(int socket, String message) 

    void setup() 

    void loop() 

This example also demonstrates a similar callback functionality to take action on an asynchronously-closed socket. `setSocketCloseCallback()` can be used to set a closed-socket callback. The callback should take a single parameter \-- the socket closed. The example uses this callback to re-open a listening socket if that\'s what the closed socket was.

## Troubleshooting

If you are running into trouble with your LTE shield, here are some troubleshooting tips and guides that may help you figure out what might be going on:

### Troubleshooting Resources

- [SparkFun Troubleshooting Tips](https://learn.sparkfun.com/tutorials/sparkfun-troubleshooting-tips)
- [Hologram Webpage](https://hologram.io/about-us/)
  - [Hologram Connectivity Guide](https://hologram.io/docs/guide/connect/connect-device/)
  - [Hologram SIM Card FAQ](https://help.hologram.io/hologram-iot-sim-card)
  - [Hologram Coverage Map](https://hologram.io/pricing/coverage/)
  - [Hologram Account/Billing FAQ](https://hologram.io/docs/guide/account/faq/)
  - [Hologram Data Plans](https://hologram.io/pricing/details/)

### Troubleshooting Steps

1.  To begin troubleshooting your shield, make sure you are following the hookup guide exactly.\
    \

    ::: 
    **Why?** The assembly instructions and example codes have been tested and are known to work. It will also be easier to narrow down the problem because any deviation from the hookup guide may be causing the issue(s).
    :::
2.  Use the [SparkFun Troubleshooting Tips](https://learn.sparkfun.com/tutorials/sparkfun-troubleshooting-tips) to do an initial check of any issues you may have missed. These include, but are not limited to:
    - Double checking your power. Use a multimeter to it is getting the right voltage or enough current?
    - Double check your soldering. Are there any cold joints?
    - Double checking your wiring or connections and use a multimeter to test all connections.
    - Do you have the right board selected in the Arduino IDE? Are you using the right COM port?
    - Double check the baud rate for the Serial Monitor.
    - Have you tried a different computer, USB cable, or microcontroller board?
    - etc.

    \
3.  Verify that your Hologram SIM card is activated. If you have reached the *free* 1MB data limit, you will need to wait for the next month/billing cycle or add a payment method for your account.
    \
4.  Check your area of coverage. Hologram has a wide variety of contract carriers, but they do not have coverage everywhere. If you or your project are in an area with low or minimal cellular coverage, you may run into issues because of that.
    \
5.  As part of our QC process, all shields should have been tested with a known working Hologram SIM card. However, here are a few tests and sketches you can run to verify the functionality of the board. (*\*These tests assume that you have already addressed the previous items 1-4 and you are testing the shield in the US. If you live outside of the US, you may need to modify the library for your carrier information.*)\
    \
    a.  Without the LTE shield, upload Blink to make sure your microcontroller is working.
    b.  **With the LTE shield on the RedBoard:**
        i.  Check the hardware connections for continuity, switch positions, make sure the SIM card is inserted fully, and check that there is power going to the LTE module. (i.e. Uploading code, while the switch is in the **SERIAL - \[HARD\]** position will cause issues.)
            \
        ii. Don\'t forget to use the push buttons to power/reset the LTE module.
            \
        iii. Run the **Serial_Passthrough** example code to verify the microcontroller can talk to the LTE shield.
             \
        iv. Run the [`Ping_SIM_card.ino`](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/6/Ping_SIM_Card.ino) ([] *Click Link*) to verify that you are reading the SIM card. You may need to run this sketch a few times, there were a small number of instances that is gave false negatives. However, a failure here could indicate that your SIM card isn\'t seated properly or there is a connection issue.
            \
        v.  Run the **00_Register_Operator** example sketch from the library. This will be the first sketch that tests the functionality of the LTE shield.
            - You may need to adjust the mobile network operator (MNO) setting on line 45.
            - You may also need to set the APN on line 51 .

            \
        vi. Run the **Network_Info** example sketch from the library. This sketch initializes the LTE module and checks that it can connect to a mobile network.
            - You may need to adjust the mobile network operator (MNO) setting on line 83.

### Frequently Asked Questions

#### Are the Hologram eUICC SIM Card\'s Special Features Supported with the LTE Cat M1/NB-IoT Shield?

The [Hologram enhanced eUICC SIM card \[ e.g. CEL-17117 \]](https://www.sparkfun.com/products/17117) will work with [SparkFun LTE CAT M1/NB-IoT Shield - SARA-R4 \[ e.g. CEL-14997 \]](https://www.sparkfun.com/products/14997) but the special eUICC features will not be operable with the shield at this current time.

If you need further assistance with these key features please visit the Hologram support forum:

- <https://community.hologram.io/>