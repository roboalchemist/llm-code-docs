# Source: https://learn.sparkfun.com/tutorials/ast-can485-wifi-shield-hookup-guide

## Introduction

What would make the AST-CAN485 even better? WiFi! In order to further the communications capabilities of the CAN485, we present the [AST-CAN485 Wifi Shield](http://www.sparkfun.com/products/14597). The shield is based on the Sparkfun ESP8266 thing and allows for a CAN485 module to communicate over Wifi.

[![SparkFun AST-CAN485 WiFi Shield ](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/5/4/14597-SparkFun_AST-CAN485_WiFi_Shield-01.jpg)](https://www.sparkfun.com/sparkfun-ast-can485-wifi-shield.html)

### [SparkFun AST-CAN485 WiFi Shield ](https://www.sparkfun.com/sparkfun-ast-can485-wifi-shield.html) 

[ WRL-14597 ]

The AST-CAN485 WiFi Shield provides a way for working wirelessly in automation, an environment famous for being noisy and unf...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

Depending on your setup, you will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49) to solder pins to the AST-CAN485. You will also need a flat head and wire strippers to connect wires to the screw terminals.

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

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/1/14763-Wire_Strippers_-_758PL0066-03.jpg)](https://www.sparkfun.com/products/14763)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/14763) 

[ TOL-14763 ]

These are high grade wire strippers from Techni-Tool with a curved grip making them an affordable option if you need to remov...

**Retired**

### Suggested Reading

We recommend checking out the AST-CAN485 Hookup Guide to get started with the board. Depending on your setup, you may need to install custom libraries and board add-ons.

[](https://learn.sparkfun.com/tutorials/ast-can485-hookup-guide)

### AST-CAN485 Hookup Guide 

March 1, 2018

The AST CAN485 is a miniature Arduino in the compact form factor of the ProMini. In addition to all the usual features it has on-board CAN and RS485 ports enabling quick and easy interfacing to a multitude of industrial devices.

If you aren't familiar with the following concepts, we also recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide)

### ESP8266 Thing Development Board Hookup Guide 

An overview of SparkFun\'s ESP8266 Thing Development Board - a development board for the Internet of Things.

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.

## Hardware Overview

### Input Power

The AST-CAN485 WiFi Shield provides screw terminals for your power, RS-485 signals, and CAN bus signals, presoldered to the board for fast and secure connections.

[![screw terminal highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-screw_terminal_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-screw_terminal_highlight.jpg)

The input voltage range is **7-24VDC**. The input voltage is regulated down to **5V** to supply power the CAN485 board, as well as **3.3V** to power the ESP8266.

[![Integrated power highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-integrated_power_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-integrated_power_highlight.jpg)

### ESP8266

Based on the [SparkFun ESP8266 Thing](https://www.sparkfun.com/products/13231), you can use either the PCB trace antenna, or the U.FL connector if housed in a metal enclosure.

[![ESP8266 highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-esp8266_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-esp8266_highlight.jpg)

### Programming Switch

Because the UARTs are connected together for the CAN485 board and the ESP8266, a switch is used to separate the RX and TX signals. When programing either the ESP8266 or CAN485 board, move the switch over to the PROG position, and after the upload is complete, toggle the switch to the RUN position.

[![Switch highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-prog_switch_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-prog_switch_highlight.jpg)

Speaking of programming, the ESP8266 runs off of **3.3V** logic, so to program the ESP8266, a **3.3V** USB to UART bridge is used.

[![FTDI programming header hightlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-FTDI_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-FTDI_highlight.jpg)

### AST-CAN485 Serial Port

A header breaks out the Software Serial port used by the CAN485. This can be used as a debugging serial port or to connect other devices.

[![Software Serial Highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-Software_Serial_header_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/SparkFun_AST-CAN485_WiFi_Shield-Software_Serial_header_highlight.jpg)

### Pinouts

The pinout for the WiFi Shield is shown below:

[![Listed PinOuts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/8/WifiShieldPinOuts.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/WifiShieldPinOuts.png)

*Image courtesy of AST*

⚡ **Warning!** This board has pins that operate at **24V** as well as pins that operate at **5V** and **3.3V**. Care should be taken during wiring as **24V** has the potential to do significant damage to **5V** and **3.3V** circuits.

### Schematic

The schematic below shows the layout of the interconnects between an inserted CAN485 module and the integrated ESP module.

[![Schematic of connection between inserted CAN485 module and the integrated ESP module](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/8/WifiShieldSchematic.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/WifiShieldSchematic.png)

*Image courtesy of AST*

The primary interface between the CAN485 and the ESP8266 is a serial port. It operates on hardware serial port 0 on the CAN485 rather than the traditional Software Serial port. The reason for this is that it enables higher speed communications between the two devices. The trade-off of this feature is that it uses the main serial port, which is also used to program the CAN485 and is broken out on its FTDI header. This means that in order to program the CAN485 module, while it is inserted, the serial port must be disconnected. For this reason, the mode selection switch was added which allows for the rx and tx lines to be disconnected. In a similar way, the same serial port is used to both program the ESP8266 and communicate with the CAN485. The mode selection switch also enables the ESP to be programmed by disconnecting it from the CAN485.

## Hardware Hookup

The AST-CAN485 WiFi Shield comes with headers pre-soldered to the board. Insert the CAN485 as shown with the CAN485\'s FTDI header close to the ESP8266.

[![WiFi Shield with CAN485 Inserted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/8/HardwareHookupWiFiShield.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/HardwareHookupWiFiShield.jpg)

### Powering The Board

The Shield can be powered through the screw terminals. While the power input is intended to be supplied with **24V**, an input voltage of **7-24V** may be used.

An integrated power supply regulates the **24V** input power down to **5V** which is used to provide power to the inserted CAN485 board. This is further regulated down to **3.3V** to power the ESP module.

It is also possible to power the board using the raw input pin of the CAN485 module. However, use of an external 24V supply is recommended and is the intended use case.

[![Providing power to the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/8/PoweringBoard.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/PoweringBoard.png)

*Image courtesy of AST*

⚡ **Warning!** This board has pins that operate at **24V** as well as pins that operate at **5V** and **3.3V**. Care should be taken during wiring as **24V** has the potential to do significant damage to **5V** and **3.3V** circuits.

## Software Setup and Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library or board add-on, please check out our [library installation guide](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) and instructions to install the [AST-CAN485 board add-on files](https://learn.sparkfun.com/tutorials/ast-can485-hookup-guide#software-installation).

### The Programming Mode Selection Switch

The ESP and CAN485 modules are connected using a hardware serial port. The same port is used to program either of the devices. It is therefore necessary to disconnect the serial port in order to program either of the devices. A selector switch is provided in order to make this possible.

If the selector switch is set to RUN, the ESP and CAN485 are connected via a serial port. If the switch is set to PROG, the serial port is disconnected and the devices may be programmed.

[![Programming Selector Port](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/ProgrammingSelectorPort.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/ProgrammingSelectorPort.jpg)

### Setup Arduino For ESP Programming

There are many options for programming ESP8266 based devices. The approach recommended by this guide is to make use of the ESP8266 Arduino Addon which has been developed by the ESP community. The Addon can be downloaded via the [GitHub Repository](https://github.com/esp8266/Arduino) or by clicking the button below.

[ESP8266 Github Repository (ZIP)](https://github.com/esp8266/Arduino/archive/master.zip)

This implementation is based on the ESP8266 Thing and the same setup instructions may be used. For more information, refer to the [ESP8266 Thing Hookup Guide](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide).

[](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide)

### ESP8266 Thing Development Board Hookup Guide 

November 5, 2015

An overview of SparkFun\'s ESP8266 Thing Development Board - a development board for the Internet of Things.

If you have not previously installed an Arduino library, please check out our installation guide.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

January 11, 2013

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

### Programming the ESP

The following process is followed in order to program the ESP module:

- Switch the mode selection switch to PROG.
- Insert a **3.3V** FTDI into the FTDI header.
- Hold down the ESP programming button and upload a sketch.
- Return the mode selection switch to RUN to reconnect the devices.

[![Programming the ESP Module](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/8/Figure9.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/Figure9.png)

*Programming the ESP Module*

*Image courtesy of AST*

### Programming the CAN485

The following process is followed in order to program the CAN485 module:

- Switch the mode selection switch to PROG.
- Connect a **5V** FTDI to the FTDI header on the CAN485 module.
- Upload a sketch
- Return the mode selection switch to RUN to reconnect the devices.

[![Programming the Inserted CAN485 Module](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/8/Figure10.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/8/Figure10.png)

*Programming Inserted CAN485 Module*

*Image courtesy of AST*

### Examples

The [WiFi Shield GitHub Repository](https://github.com/Atlantis-Specialist-Technologies/CAN485-WiFi-Shield/tree/master/Examples/BasicSerial) includes a few examples which demonstrate the use of the board. After downloading the repository, open up one the examples in the Arduino IDE. Select the **CAN485** as the board, the COM port that it enumerated on, and hit upload to test.

#### Basic Serial Example

This example demonstrates serial communication between and inserted CAN485 and the on board ESP8266. Each device has a built in LED which is controlled by the other device over the serial port. Operation is as follows:

- The CAN485 sends a command to the ESP every 100 ms.
- The ESP sets its LED on or off depending on the command.
- The ESP sends the same command back to the CAN485.
- The CAN485 sets its LED depending on the command received by the ESP.

In addition to the examples in the WiFi Shield GitHub Repository, there are a number of examples using the ESP8266 in the ESP Arduino Library. These are accessible in the Arduino IDE under **File**\>**Examples**. Examples may also be found in the [ESP Github Community Forum](https://github.com/esp8266).