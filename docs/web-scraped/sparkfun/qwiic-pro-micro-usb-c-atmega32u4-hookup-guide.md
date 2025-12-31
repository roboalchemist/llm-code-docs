# Source: https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide

## Introduction

**Heads up!** This is for the **Qwiic Pro Micro USB-C (ATmega32U4)** version. If you are looking for information about hardware on the *Pro Micros with the micro-b USB connector*, make sure to check out the older [Pro Micro & Fio V3 Hookup Guide](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide).

The [SparkFun Qwiic Pro Micro USB C](https://www.sparkfun.com/products/15795) is a really cool, little development board. It\'s an Arduino-compatible microcontroller, micro-sized, and it accomplishes with one single chip what old [Arduino Unos](https://www.sparkfun.com/products/11021), [Duemilanoves](https://www.sparkfun.com/products/retired/666), and Diecimeillas could never dream of: *true USB functionality*. In this tutorial, we\'ll check out the updated Qwiic Pro Micro and go through a few examples to get you started!

[![SparkFun Qwiic Pro Micro - USB-C](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/4/0/4/15795-Pro_Micro_C-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html)

### [SparkFun Qwiic Pro Micro - USB-C](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html) 

[ DEV-15795 ]

The SparkFun Qwiic Pro Micro adds a reset button, Qwiic connector, USB-C, and castellated pads to the miniaturized Arduino bo...

[ [\$23.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun Qwiic Pro Micro - USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/0/4/15795-Pro_Micro_C-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html)

### [SparkFun Qwiic Pro Micro - USB-C](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html) 

[ DEV-15795 ]

The SparkFun Qwiic Pro Micro adds a reset button, Qwiic connector, USB-C, and castellated pads to the miniaturized Arduino bo...

[ [\$23.95] ]

[![Reversible USB A to C Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/4/15425-Reversible_USB_A_to_C_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html)

### [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html) 

[ CAB-15425 ]

These 0.8m cables have minor modifications that allow them to be plugged into their ports regardless of orientation on the US...

[ [\$6.50] ]

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49) for a secure connection when using the plated through hole pads.

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

#### Prototyping Accessories

Depending on your setup, you may want to use IC hooks for a temporary connection. However, you will want to solder header pins to connect devices to the plated through holes for a secure connection.

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![IC Hook with Pigtail](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/9/6/09741-01.jpg)](https://www.sparkfun.com/ic-hook-with-pigtail.html)

### [IC Hook with Pigtail](https://www.sparkfun.com/ic-hook-with-pigtail.html) 

[ CAB-09741 ]

These are good quality IC test hooks with a male connection wire. Instead of a single hook, these have two hooks that are cap...

[ [\$5.75] ]

[![Female Stackable Header - 12-Pin](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/5/6/14322-02.jpg)](https://www.sparkfun.com/photon-stackable-header-12-pin.html)

### [Female Stackable Header - 12-Pin](https://www.sparkfun.com/photon-stackable-header-12-pin.html) 

[ PRT-14322 ]

These stackable headers are add a great deal of connectivity to your next project where you need 12, stackable, pins in a lin...

[ [\$0.75] ]

For those that want to take advantage of the Qwiic enabled devices, you\'ll want to grab a Qwiic cable.

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/1/14425-Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html)

### [Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-14425 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and a breadboard hookup...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

## Hardware Overview

Before we get into installing and using the Qwiic Pro Micro, let\'s quickly look at the board \-- examine its inputs, outputs, and other hardware quirks.

### Old School to New School

The Qwiic Pro Micro USBC is a revision of the original Pro Micro. Overall, it is functionally the same as the previous version. The board is the same size as the original Pro Micro but we added a few additional features by shrinking down some components on the board. The major changes to the board that you will notice include:

- Reset Button
- USB C
- Castellated Pads
- Qwiic Connector
- AP2112 3.3V Voltage Regulator

The benefit of the reset button is to quickly reset the board or place it into bootloader mode without the need to take out a piece of jumper wire. The USB micro-b connector has been replaced with the USB type C connector. The through hole pads have [castellated edges](https://learn.sparkfun.com/tutorials/how-to-solder-castellated-mounting-holes/) for each pin to add a lower profile in your projects should you decide build it into another assembly during production. Finally, a Qwiic connector is populated on the bottom of the board to easily add Qwiic enabled I^2^C devices.\

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Older 5V/16MHz Pro Micro](https://cdn.sparkfun.com/r/600-600/assets/parts/9/3/2/6/12640-02a.jpg "Older 5/V/16MHz Pro Micro")](https://www.sparkfun.com/products/12640?_ga=2.255509896.1441134867.1577121511-1728962999.1561997726)   [![Newer 5V/16MHz Qwiic Pro Micro](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/4/0/4/15795-Pro_Micro_C-04.jpg "Newer 5V/16MHz Qwiic Pro Micro")](https://www.sparkfun.com/products/15795)

  *Older 5V/16MHz\                                                                                                                                                                                                                        *Newer 5V/16MHz\
  Pro Micro*                                                                                                                                                                                                                              Qwiic Pro Micro USB C*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A subtle difference that you may not notice is the old Pro Micro used the MIC5219, which was able to handle a maximum voltage input of 16VDC. The new Qwiic Pro Micro uses the AP2112 3.3V voltage regulator which can handle a **maximum of 6V**. The output current is slightly higher in the Qwiic Pro Micro which peaks at about 600mA. You\'ll need to make sure to use an [appropriate voltage regulator and components](https://learn.sparkfun.com/tutorials/beginner-parts-kit-identification-guide#voltage-regulators) and regulate the voltage down.

For more information about the differences between the boards, make sure to pull up the schematic for both boards and read further below!

### The Pinout

All of the Qwiic Pro Micro\'s I/O and power pins are broken out to two, parallel headers. Some pins are for power input or output, other pins are dedicated I/O pins. Further, the I/O pins can have special abilities, like analog input. Here\'s a map of which pin is where, and what special hardware functions it may have:

[![Graphical Datasheet for Qwiic Pro Micro](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/4/QwiicProMicroUSB-C_ATmega32U4_Graphical_Datasheet.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/QwiicProMicroUSB-C_ATmega32U4_Graphical_Datasheet.png)

*Click on image for a closer view*

### Power

There are a variety of power and power-related nets broken out to connectors and through hole pads. Each pad has a castellated edge. The back of the board also has the USB pins broken out for power.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Castellated Power and Reset Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-Power.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-Power.png)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C_Back_Power.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C_Back_Power.png)
  *Castellated Power and Reset Pins*                                                                                                                                                                                *USB Power Pins*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These nets consist of the following:

- **V** is the voltage provided from the USB connector.
- **RAW** is the unregulated voltage input for the Qwiic Pro Micro. If the board is powered via USB (i.e. **V**), the voltage at this pin will be about 4.8V (USB\'s 5V minus a Schottky diode drop). On the other hand, if the board is powered externally, through this pin, the applied voltage can be up to **6V**.
- **5V** is the voltage supplied to the on-board ATmega32U4. This voltage will depend on whether you have the jumper set to **5V (by default)** or **3.3V**.
  - When the jumper is set to 5V, it is the voltage applied to the RAW pin. We suggest using a clean 5V power supply if you are connecting [5V devices to the I/O](https://learn.sparkfun.com/tutorials/logic-levels). If the board is powered through the \'RAW\' pin (or USB), this pin can be used as an **output** to supply 5V for other devices.
  - When the jumper is set to 3.3V, the output is 3.3V. If the board is powered through the \'RAW\' pin (or USB), this pin can be used as an **output** to supply 3.3V for other devices.
- **RST** can be used to **restart** the Qwiic Pro Micro. There is a built-in reset button to reset the Pro Micro. However, the pin is broken out if you need to access this pin externally. This pin is pulled high by a 10kΩ resistor on the board, and is **active-low**, so it must be connected to ground to initiate a reset. The Qwiic Pro Micro will remain \"off\" until the reset line is pulled back to high.
- **GND**, of course, is the common, ground voltage (0V reference) for the system.

#### I/O Pins

The Qwiic Pro Micro breaks out the I/O pins to plated through hole pads on the edge of the board. Each pad is castellated as well. On the back, there are additional pins to connect to the USB data pins.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Castellated IO Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-IO_Pins.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-IO_Pins.png)   [![USB Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-USB_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-USB_Pins.jpg)
  *Castellated I/O PTH Pads*                                                                                                                                                                               *USB Pads*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Pro Micro\'s I/O pins \-- 18 in all \-- are multi-talented. Every pin can be used as a **digital input or output**, for blinking LEDs or reading button presses. These pins are referenced in the Arduino IDE via an integer value between 0 and 21. (The A0-A3 pins can be referenced digitally using either their analog or digital pin number).

Nine pins feature [analog to digital converters (ADCs)](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) and can be used as **analog inputs**. These are useful for reading potentiometers or other analog devices using the `analogRead([pin])` function.

There are five pins with [pulse width modulation (PWM)](https://learn.sparkfun.com/tutorials/pulse-width-modulation) functionality, which allows for a form of **analog output** using the `analogWrite([pin], [value])` function. These pins are indicated on-board with a faint, white circle around the square pads.

There are hardware [UART (serial)](https://learn.sparkfun.com/tutorials/serial-communication), [I^2^C](https://learn.sparkfun.com/tutorials/i2c), and [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) pins available as well. These can be used to interface with digital devices like serial LCDs, XBees, IMUs, and other serial sensors.

The Pro Micro has five [external interrupts](http://arduino.cc/en/Reference/attachInterrupt), which allow you to instantly trigger a function when a pin goes either high or low (or both). If you attach an interrupt to an interrupt-enabled pin, you\'ll need to know the specific interrupt that pin triggers: pin 3 maps to interrupt 0 (INT0), pin 2 is interrupt 1 (INT1), pin 0 is interrupt 2 (INT2), pin 1 is interrupt 3 (INT3), and pin 7 is interrupt 4 (INT6).

#### On-Board LEDs

There are three LEDs on the Pro Micro. One red LED indicates whether **power** is present. The other two LEDs help indicate when data is transferring over USB. A yellow LED represents USB data coming *into* (RX) the Pro Micro, and a green LED indicates USB data going out (TX).

[![On Board LEDS](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-LEDs.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-LEDs.png)

### Jumpers

On the back of the board is a jumper that is able to select the system voltage. The default voltage for the board defaults to 5V. By [cutting the jumper pad](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces#cutting-a-trace-between-jumper-pads) and adding a solder to the between the center and right jumper pads, the system voltage will be set to 3.3V.

[![Selectable Power Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic_Pro_Micro_C-Jumpers.jpg)

### Board Dimensions

The board measures **1.30\" x 0.70\"**. Not included in the image below is the PCB thickness, which is **0.8mm**. This is thinner than a majority of the PCBs used for SparkFun original designs.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/4/SparkFun_Qwiic_Pro_Micro_C-Board_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/SparkFun_Qwiic_Pro_Micro_C-Board_Dimensions.png)

### How to Power the Qwiic Pro Micro USB C

As the Pro Micro\'s main feature is its innate USB functionality, the most common way to power it is via **USB**. If the jumper is set to the default 5V, the Qwiic Pro Micro will be powered directly from the USB bus. If the jumper is set to 3.3V, the board will regulate the 5V supply coming in from USB down to 3.3V. The other end of the USB cable can be connected to either a computer, USB hub, USB batteries, or a USB wall adapter, which can (in most cases) provide more power.

Alternatively, if your Qwiic Pro Micro is living out in the wild, out of reach of USB cables, it can be powered through either the \'**RAW**\' or \'**5V**\' pins. A supply going into those pins will provide power to the Qwiic Pro Micro. To be safe, it shouldn\'t be any higher than 6V. If the jumper is set to 3.3V, the voltage will be regulated down to 3.3V.

How, exactly, you [power your project](https://learn.sparkfun.com/tutorials/how-to-power-a-project) is up to you and the demands of your project. If you\'re making something battery powered, you could use a LiPo boost converter to power the board at 5V. Or you may want to set the jumper to 3.3V, which could be powered by a [LiPo battery](https://learn.sparkfun.com/tutorials/battery-technologies/lithium-polymer) or a couple [alkalines](https://learn.sparkfun.com/tutorials/battery-technologies/alkaline). Make sure to check out the following tutorials for more information.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

February 6, 2013

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

February 7, 2013

A tutorial to help figure out the power requirements of your project.

## Hardware Hookup

Header pins were left off the Qwiic Pro Micro to allow users the flexibility of connecting any type of 0.1\" header to the board. For temporary connections to the I/O pins, you could use IC hooks to test out the pins. However, you\'ll need to [solder headers or wires of your choice to the board](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) for a secure connection. For advanced users, you could also design a PCB to take advantage of the [castellated edges](https://learn.sparkfun.com/tutorials/how-to-solder-castellated-mounting-holes/all#introduction) for a lower profile. Here are a few tutorials to connect to the pads depending on your personal preference.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

February 8, 2013

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/how-to-solder-castellated-mounting-holes)

### How to Solder: Castellated Mounting Holes 

May 12, 2015

Tutorial showing how to solder castellated holes (or castellations). This might come in handy if you need to solder a module or PCB to another PCB. These castellations are becoming popular with integrated WiFi and Bluetooth modules.

**Note:** For advanced users taking advantage of the castellated edges, you can design a board with the Qwiic Pro Micro Eagle footprint should you decide to make a keyboard using the [Cherry MX Switch](https://www.sparkfun.com/categories/tags/cherry)!\
\

[GitHub SparkFun Eagle Library: SparkFun-Boards.lbr](https://github.com/sparkfun/SparkFun-Eagle-Libraries)

In order to power and upload to the board, you will simply need a USB C cable connected to your computer. For the scope of this tutorial, you\'ll get as far as example 1.

[![USB Cable connected to the Qwiic Pro Micro](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/4/Qwiic-Pro-Micro-C-Atmega32U4-USB-Cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic-Pro-Micro-C-Atmega32U4-USB-Cable.jpg)

To take advantage of the board\'s HID, we recommend some sort of input. The analog joystick provides a few inputs to test our the keyboard and mouse in example 2.

[![Example 2: HID Keyboard and Mouse using the Button and Analog Joystick Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/4/Fritzing_Atmega32U4_Qwiic_Pro_Micro_Example2_Analog_Joystick_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Fritzing_Atmega32U4_Qwiic_Pro_Micro_Example2_Analog_Joystick_bb.jpg)

[![HID JoystickJoystick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/4/Qwiic-Pro-Micro-C-Atmega32U4-Breadboard-HID-Analog-Joystick.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic-Pro-Micro-C-Atmega32U4-Breadboard-HID-Analog-Joystick.jpg)

### Qwiic Enabled Device

You can also easily connect a Qwiic enabled device to the Qwiic connector. Below is an example of a distance sensor connected to the Qwiic Pro Micro. If you have an installation with a kiosk\'s screensaver turned on, you could use the Qwiic Pro Micro to wake it up by moving a mouse if there is someone within a certain distance of the VL53L1X sensor.

[![Qwiic Device Connected to the Qwiic Pro Micro](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/4/Pro-Micro-C-Atmega32U4-Qwiic-Device-Distance-Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Pro-Micro-C-Atmega32U4-Qwiic-Device-Distance-Sensor.jpg)

## Installing Drivers (Windows)

Getting the Qwiic Pro Micro set up on your computer and in your Arduino environment can be difficult. Follow along on this page for a step-by-step guide through the driver installation and Arduino-enabling process.

### [][Windows Driver Installation](#windows_driver)

**Note:** On a Windows 10 OS, the driver should automatically install. You may not need to download the driver for the Atmega-32U4-based Arduino. If that is the case, you can move to [installing the board add-on](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide#windows_boardaddon) for the Arduino IDE.

#### Step 1: Download the Driver

Before plugging your board in, get a head start by downloading the drivers. Check the [GitHub Repository](https://github.com/sparkfun/Arduino_Boards/tree/main/sparkfun/avr/signed_driver) for the latest files. The same driver file works for both the Pro Micro and the Fio v3. The drivers for both the Fio and the Pro Micro are signed for Windows users. You can download them directly from the zipped file below.

[Fio and Pro Micro Drivers (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/SparkFun_ATmega32U4_Drivers_Git_commit_75570d5.zip)

**Note:** For the latest drivers, make sure to check the GitHub Repository.

**Unzip** that zip file, and don\'t forget where you\'ve left its contents. In that zip file, you should find the **.inf** and **.cat** files, which contains all the information Windows needs to install the Pro Micro\'s driver. The *sparkfun.inf* driver and *sparkfun.cat* digitally signed catalog file will be found in **../SparkFun_ATmega32U4_Drivers_Git_commit_75570d5** .

#### Step 2: Plug in the Qwiic Pro Micro

When you initially **plug the board in**, an \"Installing device driver software\" bubble notification should pop up in the lower-right corner of your taskbar. After the green dot circles the grey box a number of times, you'll probably get a sad bubble like this:

[![Driver install failed](https://cdn.sparkfun.com/assets/a/c/2/9/0/523a2153757b7f407d8b4571.PNG)](https://cdn.sparkfun.com/assets/a/c/2/9/0/523a2153757b7f407d8b4571.PNG)

Never fear! Windows just doesn\'t know where to find our driver.

**Note:** Some users have experienced issues when plugging the Pro Micro into a USB 3.0 port. If you experience issues on USB 3.0 ports, try switching to use a USB 2.0 port.

#### Step 3: Open the Device Manager

From here, the most straightforward way to install the driver is through the Device Manager. To get to the Device Manager, click the **Start** button, then open the **Control Panel**. In the Control Panel, click **System and Maintenance**, and then open the **Device Manager**.

Alternatively, you can open the **Run prompt** (Windows key+R) and type \'devmgmt.msc\' and click OK.

[![Run prompt opening device manager](https://cdn.sparkfun.com/assets/3/3/7/7/e/523b1c4f757b7f64208b4567.PNG)](https://cdn.sparkfun.com/assets/3/3/7/7/e/523b1c4f757b7f64208b4567.PNG)

In the Device Manager, expand the \'Other devices\' tree, where you should find a **\'USB IO Board\'** with a yellow warning sign over its icon. Right-click the \'USB IO Board\' and select **Update Driver Software\...**.

[![Updating driver in device manager](https://cdn.sparkfun.com/assets/b/e/f/1/d/523b1e59757b7f10218b4567.PNG)](https://cdn.sparkfun.com/assets/b/e/f/1/d/523b1e59757b7f10218b4567.PNG)

This should spawn an \'Update Driver Software - USB IO Board\' window.

#### Step 4: Finding the Driver

In the first window that pops up, click **\'Browse my computer for driver software\'**. On the next window, click **\'Browse\...\'** to search for the driver you just downloaded. It should be a folder named \'**Arduino_Boards-master**\', in a subdirectory noted in step 1. After you've selected the \'driver\' folder, click **OK**, then select **Next**.

[![Driver install steps 1 through 5](https://cdn.sparkfun.com/r/600-600/assets/3/d/9/4/9/523b286b757b7fed218b4568.PNG)](https://cdn.sparkfun.com/assets/3/d/9/4/9/523b286b757b7fed218b4568.PNG)

*Click on image for a closer view.*

Windows will attempt to do its driver install thing, but not before complaining about the driver being unsigned. It's safe to select **\'Install this driver software anyway\'** on the warning dialog.

After watching the progress bar beam by a few times, you should get a happy \'Windows has successfully updated your driver software\' window. And the \'Device Manager\' should have a new entry for the \'**SparkFun Pro Micro (COM ##)**\' if you have one of those) under the \'**Ports (COM & LPT)**\' tree.

[![Atmega-32U4 based Arduino Driver Installation](https://cdn.sparkfun.com/r/600-600/assets/6/4/e/5/5/523b286b757b7f03218b4568.PNG)](https://cdn.sparkfun.com/assets/6/4/e/5/5/523b286b757b7f03218b4568.PNG)

*Click on image for a closer view.*

Take note of which COM port your Qwiic Pro Micro was assigned. We'll need it soon.

## Installing Drivers (Mac and Linux)

If you\'re using Mac or Linux, follow the steps below to get your Pro Micro ready to go on your computer. We\'re not going to name names here, but installing the Qwiic Pro Micro on Mac OS X and Linux is *a lot* easier than on other OS\'s\...

When you initially plug your Qwiic Pro Micro into a Mac, it\'ll pop up a \"Keyboard Setup Assistant\" window. This stems from the Qwiic Pro Micro\'s ability to emulate an HID USB device (e.g. keyboards and mice) \-- the Mac thinks your Pro Micro is a human input device (which it could be! but isn\'t yet).

[![Mac keyboard setup assistant](https://cdn.sparkfun.com/assets/e/8/0/f/2/5240ada8757b7f09578b4567.png)](https://cdn.sparkfun.com/assets/e/8/0/f/2/5240ada8757b7f09578b4567.png)

There\'s nothing to configure in this window, so just click the big, red, \'**X**\' to close it.

That\'s all there is to it! The CDC (communication device class) portion of your Qwiic Pro Micro (the part that handles USB-to-serial conversion) should automatically install on your computer.

## Setting Up Arduino

**Note:** If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

We\'re still not completely ready for Arduino, but this is the final stretch. Before you can use the Qwiic Pro Micro in the Arduino IDE, you\'ll need to install the board (\*.brd) files for the Qwiic Pro Micro so the Arduino IDE will know how to communicate with your board. Jump to the section based on your operating system for instructions on how to install the board files so that you can select the **SparkFun Pro Micro, ATmega32U4 (5V, 16MHz)**.

- [Windows](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#windows_boardaddon)
- [Mac and Linux](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#mac_linux_boardaddon)

### [][Installing the Arduino Addon](#windows_boardaddon) [Windows]

#### Using the Board Manager

Since the release of Arduino 1.6.4, adding third party boards to the Arduino IDE is easily achieved through the board manager. If you\'re running an older version of Arduino (v1.6.3 or earlier), we recommend upgrading now. As always, you can download the latest version of Arduino from [arduino.cc](http://www.arduino.cc/en/Main/Software).

[Download the Arduino IDE](https://www.arduino.cc/en/main/software)

To begin, you\'ll need to point the Arduino IDE board manager to a custom URL. Open up Arduino, then go to the Preferences (**File** \> **Preferences**). Then, towards the bottom of the window, paste this URL into the \"Additional Board Manager URLs\" text box:

    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/main/IDE_Board_Manager/package_sparkfun_index.json

You can add multiple URLs by clicking the window icon, and pasting in one URL per line.

[![Adding Board Manager URL to Arduino preferences](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/4/Installing_Arduino_Boards_Add-Ons.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Installing_Arduino_Boards_Add-Ons.jpg)

Click OK. Then open the Board Manager by clicking Tools, then hovering over the Board selection tab and clicking Board Manager.

[![Select Arduino Board Manager](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Arduino_Board_Manager_Pro_Micro.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Arduino_Board_Manager_Pro_Micro.jpg)

Search for \'**sparkfun**\' in the Board Manager. You should see the **SparkFun AVR Boards** package appear. Click install, wait a few moments, and all the **\*.brd** files you\'ll need should be installed, indicated by the blue \'Installed\' that is printed next to the package.

[![Click on Install for the SparkFun AVR Boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/4/Arduino_Board_Manager_SparkFun_AVR_Boards.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Arduino_Board_Manager_SparkFun_AVR_Boards.jpg)

You should now be able to upload code to a number of SparkFun Arduino-compatible products, including the **SparkFun Pro Micro**.

[![Arduino SparkFun AVR Boards](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Arduino_Board_Selection_Pro_Micro.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Arduino_Board_Selection_Pro_Micro.jpg)

Notice there are two options for the Pro Micro - 8MHz and 16MHz. It\'s very important that you **select the Pro Micro option that matches your board\'s voltage and speed**. This should be listed under the **Tools** \> **Processor**. For the Qwiic Pro Micro, you will need to ensure that you select the **ATmega32U4 (5V, 16MHz)**.

[![Atmega32U4 Processor Selection in Arduino IDE](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Arduino_Processor_Selection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Arduino_Processor_Selection.jpg)

You should also see your Pro Micro\'s **COM port** under the \'**Tools** \> **Serial Port**\' menu. Select it, and head over to the [Example 1](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#example-1-blinkies-and-hello-world) page where we\'ll upload our first piece of code.

#### Manually Installing the \*.brd Files

If you are using an older version of the Arduino IDE and do not have access to the Arduino Board Manager, then you\'ll need to install the \*.brd files the old fashioned way.

To begin, [**download this zip folder**](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SparkFunBoard_Addons_Jan_16.zip), and unzip its contents into a **\'hardware\' directory** within your Arduino sketchbook.

**Note:** These Arduino addon files only work with **Arduino 1.5** and up. If you\'re using an earlier version of Arduino, either update (and get some cool new features), or download [the older version of the Addon](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SF32u4_boards-pre-1.6.zip).

Where\'s your Arduino sketchbook? Well, by default, it should an \'**Arduino**\' folder in your **home directory**, but to double check you can go to **File** \> **Preferences** within Arduino and check the \'*Sketchbook location*\' text box. Just make sure you close all Arduino windows once you\'re done.

[![Finding the sketchbook location](https://cdn.sparkfun.com/assets/9/8/7/9/3/523b2e28757b7f77208b4567.png)](https://cdn.sparkfun.com/assets/9/8/7/9/3/523b2e28757b7f77208b4567.png)

Once you\'ve unzipped that folder into the \'**hardware**\' folder within your Arduino sketchbook (you may actually have to create a hardware folder), your directory structure should look something like this:

[![Windows directory structure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/1/32u4_windows_directory.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/32u4_windows_directory.png)

The structure of this directory is critical \-- it should look something like \"**\.../Arduino/hardware/\[manufacturer\]/\[architecture\]**\", in this case `[manufacturer]` is \"**sparkfun**\", and `[architecture]` is \"**avr**.\"

    language:bash
    .../Arduino/hardware/sparkfun/avr

There\'s a lot going on in that addon, but one of the most important files is \'**boards.txt**\', which will add a few new entries to your \'**Tools** \> **Board**\' menu.

To double-check that the board definitions have been added to Arduino, **open up Arduino**, and check under the \'**Tools** \> **Board**\' menu. There should be some new entires for \'SparkFun Pro Micro\', \'SparkFun FioV3\', \'Qduino Mini\', and other 32U4-based boards.

[![Pro Micros showing up in Arduino board selection](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SparkFun_Atmega32u4__Arduino_Board_Selection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SparkFun_Atmega32u4__Arduino_Board_Selection.jpg)

Notice there are two options for the Pro Micro - 8MHz and 16MHz. It\'s very important that you **select the Pro Micro option that matches your board\'s voltage and speed**. This should be listed under the **Tools** \> **Processor**. For the Qwiic Pro Micro, you will need to ensure that you select the **ATmega32U4 (5V, 16MHz)**.

[![Atmega32U4 Processor Selection in Arduino IDE](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SparkFun_Atmega32u4__Arduino_Processor_Selection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SparkFun_Atmega32u4__Arduino_Processor_Selection.jpg)

You should also see your Pro Micro\'s **COM port** under the \'**Tools** \> **Serial Port**\' menu. Select it, and head over to the [Example 1](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#example-1-blinkies-and-hello-world) page where we\'ll upload our first piece of code.

### [][Installing the Arduino Addon](#mac_linux_boardaddon) [Mac and Linux]

Following these directions is critical to getting your Pro Micro supported within your Arduino environment!

#### Using the Board Manager

Since the release of Arduino v1.6.4, adding third party boards to the Arduino IDE is easily achieved through the board manager. If you\'re running an older version of Arduino (v1.6.3 or earlier), we recommend upgrading now. As always, you can download the latest version of Arduino from [arduino.cc](http://www.arduino.cc/en/Main/Software).

[Download the Arduino IDE](https://www.arduino.cc/en/main/software)

To begin, you\'ll need to point the Arduino IDE board manager to a custom URL. Open up Arduino, then go to the Preferences (**File** \> **Preferences**). Then, towards the bottom of the window, paste this URL into the \"Additional Board Manager URLs\" text box:

    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/main/IDE_Board_Manager/package_sparkfun_index.json

You can add multiple URLs by clicking the window icon, and pasting in one URL per line.

[![Adding Board Manager URL to Arduino preferences](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/5/arduino-board-manager-link.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/5/arduino-board-manager-link.png)

Click OK. Then open the Board Manager by clicking Tools, then hovering over the Board selection tab and clicking Board Manager.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/boardManager.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/boardManager.png)

Search for \'**sparkfun**\' in the Board Manager. You should see the **SparkFun AVR Boards** package appear. Click install, wait a few moments, and all the \*.brd files you\'ll need should be installed, indicated by the blue \'Installed\' that is printed next to the package.

[![Installing Boards Using the Boards Manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/1/SFEAVR.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SFEAVR.png)

You should now be able to upload code to a number of SparkFun Arduino-compatible products, including Pro Micro.

[![Arduino Board Selection](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SFEBoards.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SFEBoards.png)

#### Manually Installing the \*.brd Files

If you are using an older version of the Arduino IDE and do not have access to the Arduino Board Manager, then you'll need to install the \*.brd files the old fashioned way.

In order to use the Pro Micro in your Arduino IDE, you need to add a few board definition files to it. That\'s what we\'ll do in this section. Begin by [**downloading the Pro Micro addon files**](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SparkFunBoard_Addons_Jan_16.zip).

**Note:** These Arduino addon files only work with **Arduino 1.5** and up. If you\'re using an earlier version of Arduino, either update (and get some cool new features), or download [the older version of the Addon](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/SF32u4_boards-pre-1.6.zip).

With that downloaded, follow these steps to enable the Pro Micro in your Arduino environment:

1.  The addon files are supplied in a zip folder, so you\'ll need to **extract the files** within first.
2.  Find your **Arduino sketchbook folder**. If you don\'t know where it is, you can locate your sketchbook by looking at the preferences dialog in your Arduino IDE.
3.  If there isn\'t already one, create a folder in your sketchbook called \'**hardware**\'.
4.  Copy the \'sparkfun\' folder that was unzipped in the first step into the \'**hardware**\' folder.
    - Your directory structure should look something like \"**\.../Arduino/hardware/sparkfun/avr**.\"
5.  Restart Arduino, and look under the **Tools** \> **Board** menu. You should see a few new options, including SparkFun Pro Micro, SparkFun Fio V3, and Qduino Mini.

If the boards are visible, select the option that matches your board. If you have a Pro Micro, **make sure you select the correct operating speed and voltage** under **Tools** \> **Processor**! At this point, select the COM port that the Pro Micro enumerated on. Then head over to the next page where we\'ll upload our first sketch!

## Example 1: Blinkies and Hello World!

The Arduino-standard Blink sketch won\'t have any visible effect on the Pro Micro \-- **there\'s no LED on pin 13**. In fact, the only LEDs on the board are the power indicator, and RX/TX blinkies. Unlike other Arduino boards, though, we can control the RX/TX LEDs in our sketch. So let\'s get blinking!

### Upload the RX/TX Blinky, Hello World Sketch

Copy and paste the code below into the Arduino IDE. In the **Tools**, make sure to select **Board** \> **SparkFun Pro Micro** and **Processor** \> **ATmega32U4 (5V, 16MHz)**. Also, don\'t forget to select the COM port that your board enumerated to. Finally, upload ^[\[1\]](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#footnote1)^ it to your Qwiic Pro Micro USB-C.

    language:c
    /* Pro Micro Test Code
       by: Nathan Seidle
       modified by: Jim Lindblom
       SparkFun Electronics
       date: September 16, 2013
       license: Public Domain - please use this code however you'd like.
       It's provided as a learning tool.

       This code is provided to show how to control the SparkFun
       ProMicro's TX and RX LEDs within a sketch. It also serves
       to explain the difference between Serial.print() and
       Serial1.print().
    */

    int RXLED = 17;  // The RX LED has a defined Arduino pin
    // Note: The TX LED was not so lucky, we'll need to use pre-defined
    // macros (TXLED1, TXLED0) to control that.
    // (We could use the same macros for the RX LED too -- RXLED1,
    //  and RXLED0.)

    void setup()
    

    void loop()
    

With the code uploaded you should see the RX and TX LEDs take turns blinking on and off every second.

[![LEDs Blinking](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic-Pro-Micro-C-Atmega32U4-LED-Blink.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Qwiic-Pro-Micro-C-Atmega32U4-LED-Blink.gif)

You can also open up the [Arduino IDE\'s serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) (set to **9600 bps**) and see every programmer\'s [favorite two-word phrase](http://en.wikipedia.org/wiki/Hello_world_program).

[![Hello World](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Arduino_Serial_Monitor_Hello_World_ATmega32U4_Qwiic_Pro_Micro.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/Arduino_Serial_Monitor_Hello_World_ATmega32U4_Qwiic_Pro_Micro.jpg)

\

#### Understanding the Sketch

**RX LED**

The RX LED is tied to Arduino\'s pin 17. You can control it just as you would any other digital pin. Set it as an `OUTPUT`, and `digitalWrite([pin], [level])` it `HIGH` to turn the LED off or `LOW` to turn the LED on. Here\'s part of the code highlighted.

    language:c
    int RXLED = 17;  // The RX LED has a defined Arduino pin
    void setup()
    .
    .
    .
      digitalWrite(RXLED, LOW);   // set the RX LED ON
      digitalWrite(RXLED, HIGH);    // set the RX LED OFF

**TX LED**

The TX LED was not provided as an Arduino-defined pin, unfortunately, so you\'ll have to use a pair of macros to control it. `TXLED1` turns the LED on, and `TXLED0` turns the LED off. We could use the same macros for the RX LED too \-- `RXLED1` and `RXLED0`. Here\'s part of the code highlighted.

    language:c
    TXLED0; //TX LED is not tied to a normally controlled pin so a macro is needed, turn LED OFF
    TXLED1; //TX LED macro to turn LED ON

**Serial Monitor (`Serial`) vs Hardware Serial UART (`Serial1`)**

In that sketch, you\'ll also notice a pair of **Serial** initialization statements:

    language:c
      Serial.begin(9600); //This pipes to the serial monitor
      Serial.println("Initialize Serial Monitor");

      Serial1.begin(9600); //This is the UART, pipes to sensors attached to board
      Serial1.println("Initialize Serial Hardware UART Pins");

That \"`1`\" makes a huge difference. Think of the Qwiic Pro Micro having two separate serial ports. The one *without* the \"`1`\" is for communication to and from the computer over USB; this is what is visible in the Serial Monitor. The `Serial1` port is a bonafide, **hardware UART**, where your Qwiic Pro Micro can talk to any serial-enabled piece of hardware.

If you open up the **Serial Monitor**, you should only see \'`Hello world!`\' printed. \'`Hello! Can anybody hear me?`\' is being sent out over the hardware UART, where, presumably, nothing is listening. This begs the age-old question: \"If a Qwiic Pro Micro is saying \'Hello!\' over the hardware serial port, and nothing is there to hear it, does the Qwiic Pro Micro really say anything at all?\"

### Why Does My Board Re-Enumerate Every Upload?

In order to communicate serially, the Qwiic Pro Micro emulates a **virtual serial port**. Actually, it emulates two different serial ports \-- one for the bootloader, and one for the sketch. Since the bootloader and sketch run individually. Only one of these serial ports is visible at any one time.

When you click \'Upload\' in the Arduino IDE, the Qwiic Pro Micro resets itself and starts its **bootloader** program. (The bootloader is a low-level program on the Pro Micro which enables self-programming via serial.) To our operating system, the bootloader looks like a completely different device, so it gets its own serial port number. While the Qwiic Pro Micro is being programmed, the bootloader serial port will be open. When the sketch upload is finished, the bootloader will exit, that serial port will be closed, and the regular Qwiic Pro Micro serial port will open up.

What this all boils down to is the fact that you have to **be patient** with Pro Micros. Every time you upload a new sketch, your OS will need to work its driver magic before you can open up the COM port. This can take a few seconds after the code has finished uploading.

------------------------------------------------------------------------

[][\[1\]](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#footnote1) **Note for Windows users**: The first time you upload a sketch, it may fail and give you an error. On top of that, Windows will pop up that familiar \'*Device driver software was not successfully installed*\' notification. Don\'t let this worry you too much. If you get the error, wait about a minute, and try uploading again.

Hopefully the upload will succeed the second time, but if it continues to fail, check out the [how to enter the bootloader](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide/troubleshooting-and-faq#ts-reset) section of the FAQ. Windows needs to install the same driver we\'ve already installed for the Qwiic Pro Micro\'s bootloader, but it\'s unable to get everything set up before the bootloader exits.

## Example 2: HID Mouse and Keyboard

When the Pro Micro\'s were released, the most revolutionary feature (as far as Arduinos go) is its true USB functionality. The Pro Micro can be programmed to emulate any USB device you could imagine. You can even program it to act just like a mouse, keyboard, or other HID-class USB device.

### What is **HID**?

It\'s one of the many defined USB [device classes](http://en.wikipedia.org/wiki/USB#Device_classes). Every USB device is assigned a class, which defines what its general purpose is. There are loads of classes \-- printers, hubs, speakers, and webcams to mention a few, but in this example we\'ll be emulating HID \-- **Human Interface Device**. The ATmega32U4 takes care of the USB-hardware hurdle, but we\'ve still got to clear the firmware one. Time for some example code! We broke up the HID example into two parts.

- [Example 2a: USB Keyboard Made Simple](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#keyboard)
- [Example 2b: USB Mouse Functionality](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#mouse)

### [][Example 2a: USB Keyboards Made Simple](#keyboard)

To emulate a USB keyboard, we\'ll be making use of the `Keyboard` class. Here are some of the functions made available to use by this class:

- **`Keyboard.write(char)`** - This function will send a single character over USB. The character passed can be any standard, printable, ASCII-defined character: 0-9, a-z, A-Z, space, symbols, etc. Here\'s an example line of code:

  ``` c
  Keyboard.write('z') // This will send a single 'z' character to your computer.
  ```

- **`Keyboard.print(string)`** - If you need to perform a series a `Keyboard.write()`\'s, consider using just a single `Keyboard.print()`. This works similar to `Serial.print()` -- give it a string of characters and it\'ll send that stream of characters over USB. **`Keyboard.println(string)`** is also defined, if you want a newline/linefeed to close out your string. An example:

  ``` c
  Keyboard.print("Hello, world"); // This'll send your computer an 'H', followed by 'e', followed by...
  ```

- **`Keyboard.press(byte)`** and **`Keyboard.release(byte)`** give you more precise control over key presses. They do exactly what you\'d expect. One presses a button down, the other releases a button. Make sure you release any buttons you press, otherwise you\'ll encounter some wiggyness on your computer.

That\'s it. You don\'t need to include any libraries or anything, just invoke any of those functions. Here\'s an **example sketch** to try it out:

    language:c
    /* HID KeyBoard Example
       by: Jim Lindblom
       date: 1/12/2012
       license: MIT License - Feel free to use this code for any purpose.
       No restrictions. Just keep this license if you go on to use this
       code in your future endeavors! Reuse and share.

       This is very simplistic code that allows you to send a 'z' with
       a momentary pushbutton.
    */

    #include <Keyboard.h>
    int buttonPin = 9;  // Set a button to any pin

    void setup()
    

    void loop()
    
    }

In this sketch, **connecting pin 9 to ground** will make the Qwiic Pro Micro spit out a \'[z]\' character. If you have a simple, **momentary button** handy, tie one end to pin 9 and the other to ground. Otherwise, just use a wire to short 9 to GND.

After a `Keyboard.write()` or `Keyboard.print()` function has been performed by the Qwiic Pro Micro, your computer will have to decide what to do with it. What your computer does with that character, or string of characters, is entirely dependent on what program it\'s running at the time. If you have a text editor (Notepad, Word, TextEdit, etc.) open and active, it\'ll print it out there. Or you can try using the textbox below to test.

SparkFun Qwiic Pro Micro USB C Test Area

[**Warning!** Any text written in this textbox will be erased when you refresh this webpage!]

### [][Example 2b: USB Mouse Functionality](#mouse)

That covers about half of USB HID library. How about we add a mouse to the mix now? Implementing a USB HID mouse requires a few more functions, but it\'s still crazy simple. There are five functions provided by Arduino\'s HID class that can be used to implement a mouse:

- **`Mouse.move(x, y, wheel)`** tells the computer to move the mouse a certain number of pixels along either the x, y and/or wheel axis. Each variable can be any value between `-128` and `+127`, with negative numbers moving the cursor down/left, positive numbers move the right/up.\
  \

- **`Mouse.press(b)`** sends a down-click on a button or buttons. The button(s) will remain \"pressed\" until you call **`Mouse.release(b)`**. The `b` variable is a single byte, each bit of which represents a different button. You can set it equal to any of the following, or OR (\|) them together to click multiple buttons at once:\
  \
  - `MOUSE_LEFT` - Left mouse button\
  - `MOUSE_RIGHT` - Right mouse button\
  - `MOUSE_MIDDLE` - Middle mouse button\
  - `MOUSE_ALL` - All three mouse buttons\
    \

- **`Mouse.click(b)`** sends a down-click (press) followed immediately by an up-click (release) on button(s) `b`. For example, to click the left and right buttons simultaneously, try this:\
  \

  ``` c
  Mouse.click(MOUSE_LEFT | MOUSE_RIGHT); // Press and release the left and right mouse buttons
  ```

Here\'s some **example code** to show off these functions:

    language:c
    /* HID Joystick Mouse Example
       by: Jim Lindblom
       date: 1/12/2012
       license: MIT License - Feel free to use this code for any purpose.
       No restrictions. Just keep this license if you go on to use this
       code in your future endeavors! Reuse and share.

       This is very simplistic code that allows you to turn the
       SparkFun Thumb Joystick (http://www.sparkfun.com/products/9032)
       into an HID Mouse. The select button on the joystick is set up
       as the mouse left click.
    */
    #include <Mouse.h>
    int horzPin = A0;  // Analog output of horizontal joystick pin
    int vertPin = A1;  // Analog output of vertical joystick pin
    int selPin = 9;  // select button pin of joystick

    int vertZero, horzZero;  // Stores the initial value of each axis, usually around 512
    int vertValue, horzValue;  // Stores current analog output of each axis
    const int sensitivity = 200;  // Higher sensitivity value = slower mouse, should be <= about 500
    int mouseClickFlag = 0;

    //int invertMouse = 1;        //Invert joystick based on orientation
    int invertMouse = -1;         //Noninverted joystick based on orientation

    void setup()
    

    void loop()
    
      else if ((digitalRead(selPin)) && (mouseClickFlag)) // if the joystick button is not pressed
      
    }

This sketch is set up so that an [analog joystick](http://www.sparkfun.com/products/9032) connected to analog pins A0 and A1 can be used to move your mouse cursor.

The `loop()` of this code continuously monitors the horizontal and vertical analog values of the joystick and sends the `Mouse.move()` command based on what it reads. It\'ll move the mouse in steps, depending on what the sensitivity variable is set to. With sensitivity set to 2, the cursor will move in either 1 or 2 pixel steps. Depending on the orientation of the joystick, there is also an option to invert the mouse based on how the \"V\" is pointing by adjusting `invertMouse`.

The select switch on the joystick is used to control the mouse left click. Notice this code is using `Mouse.press()` and `Mouse.release()`, rather than just calling a single `Mouse.click()`. This requires a bit more coding, but it allows you to do things like drag-and-drop, double click, etc.

------------------------------------------------------------------------

For more HID example code, check out the Arduino-supplied examples under the **File** \> **Examples** \> **09.USB** menu. Or check out Arduino\'s reference language under USB for more information.

[Arduino Language Reference \> USB](https://www.arduino.cc/reference/en/#functions)

## Example 3: Qwiic Enabled HID Mouse and Keyboard

**Note:** If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

As another option, you can try to use a Qwiic device to take advantage of the HID class. We broke up the Qwiic HID examples into three parts. Depending on your application and personal preference, you could essentially use a different Qwiic enabled device.

- [Example 3a: HID Mouse with Qwiic Joystick](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#hid_mouse_qwiic)
- [Example 3b: HID Keyboard with Qwiic Keypad](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#hid_keyboard_qwiic)
- [Example 3c: Qwiic HID Mouse and Keyboard Combined](https://learn.sparkfun.com/tutorials/qwiic-pro-micro-usb-c-atmega32u4-hookup-guide#hid_mouse_keyboard_qwiic)

### [][Example 3a: HID Mouse with Qwiic Joystick](#hid_mouse_qwiic)

For the scope of this tutorial example, we will be using the Qwiic Joystick so that we do not need to solder any pins. Make sure to check out the [Qwiic Joystick Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide) before continuing on with the examples below.

[](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide)

### Qwiic Joystick Hookup Guide 

February 21, 2019

Looking for an easy way to implement a joystick to your next Arduino or Raspberry Pi project? This hookup guide will walk you through using the Qwiic Joystick with the Arduino IDE on a RedBoard Qwiic and in Python on a Raspberry Pi.

Copy and paste the code below into the Arduino IDE. Make sure to select the correct board and COM port that your respective board enumerated to.

    language:c
    /******************************************************************************
      Example_3a_Qwiic_Joystick_HID_Mouse.ino
      Written by: Ho Yun "Bobby" Chan
      Date: January 13, 2020
      Development Environment Specifics:
        Arduino IDE 1.8.9

      Description:
        Based on the Jim's Pro Micro "HID Mouse" and Wes' Qwiic Joystick "basic reading"
        examples, this example moves your computer's mouse based on the joystick's
        position. Pressing down on the joystick's will enable a mouse's left click.
        The left click will relese as soon as you stop pressing down on the joystick.

      Libraries:
        Mouse.h (included with Arduino IDE)
        Wire.h (included with Arduino IDE)
        SparkFun_Qwiic_Joystick_Arduino_Library.h (included in the src folder) http://librarymanager/All#SparkFun_joystick

      License:
        This code is released under the MIT License (http://opensource.org/licenses/MIT)

      ******************************************************************************/

    #include <Mouse.h>
    #include <Wire.h>

    #include "SparkFun_Qwiic_Joystick_Arduino_Library.h" //Click here to get the library: http://librarymanager/All#SparkFun_joystick
    JOYSTICK joystick;                                   //Create instance of this object

    int vertZero, horzZero;       // Stores the initial value of each axis, usually around 512
    int vertValue, horzValue;     // Stores current analog output of each axis
    const int sensitivity = 200;  // Higher sensitivity value = slower mouse, should be <= about 500
    int mouseClickFlag = 0;

    //int invertMouse = 1;        //Invert joystick based on orientation
    int invertMouse = -1;         //Noninverted joystick based on orientation

    //Debug mode, comment one of these lines out using a syntax
    //for a single line comment ("//"):
    #define DEBUG 0       //0 = HID only
    //#define DEBUG 1     //1 = HID with serial output

    void setup() 

      delay(1000);  // short delay to let outputs settle
      vertZero = joystick.getVertical();  // get the initial values
      horzZero = joystick.getHorizontal();  // Joystick should be in neutral position when reading these

      Mouse.begin(); //Init mouse emulation
    }

    void loop() 
      else if ((joystick.getButton()) && (mouseClickFlag)) // if the joystick button is not pressed
      

      //delay(200); //remove "//" on this line if you need a small delay
    }

Moving the Qwiic joystick will move your mouse on the screen. Pressing down on the button will cause a left mouse click. Once you stop pressing down on the joystick, it will release the left mouse click. Depending on the orientation for the vertical, you can invert the mouse\'s movement using the `invertMouse` variable at the beginning of the example code.

### [][Example 3b: HID Keyboard with Qwiic Keypad](#hid_keyboard_qwiic)

For the scope of this tutorial example, we will be using the Qwiic Keypad so that we do not need to solder any pins. Make sure to check out the [Qwiic Keypad Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide) before continuing on with the examples below.

[](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide)

### Qwiic Keypad Hookup Guide 

April 25, 2019

If you are tired of taking up GPIO pins, wiring a bunch of pull up resistors, and using firmware that scans the keys taking up valuable processing time\... check out the new Qwiic Keypad.

Copy and paste the code below into the Arduino IDE. Make sure to select the correct board and COM port that your respective board enumerated to.

    language:c
    /******************************************************************************
      Example_3b_Qwiic_Keypad_HID_Keyboard.ino
      Written by: Ho Yun "Bobby" Chan
      Date: February 6, 2020
      Development Environment Specifics:
        Arduino IDE 1.8.9

      Description:
        Based on the Jim's Pro Micro "HID Mouse" and Pete' Qwiic Keypad "read button"
        examples, this example outputs keyboard presses associated with the keypad.

      Libraries:
       Keyboard.h (included with Arduino IDE)
       Wire.h (included with Arduino IDE)
       SparkFun_Qwiic_Keypad_Arduino_Library.h (included in the src folder) http://librarymanager/All#SparkFun_keypad

      License:
        This code is released under the MIT License (http://opensource.org/licenses/MIT)

    ******************************************************************************/

    #include <Keyboard.h>
    #include <Wire.h>
    #include "SparkFun_Qwiic_Keypad_Arduino_Library.h" //Click here to get the library: http://librarymanager/All#SparkFun_keypad
    KEYPAD keypad1;                                    //Create instance of this object

    void setup() 
      Serial.print("Initialized. Firmware Version: ");
      Serial.println(keypad1.getVersion());
      Serial.println("Press a button: * to do a space. # to go to next line.");

      Keyboard.begin(); //Init keyboard emulation
    }

    void loop() 
      else if (button != 0)
      
        else if (button == '1') 
        else if (button == '2') 
        else if (button == '3') 
        else if (button == '4') 
        else if (button == '5') 
        else if (button == '6') 
        else if (button == '7') 
        else if (button == '8') 
        else if (button == '9') 
        else if (button == '#') 
        else if (button == '*') 
      }

      //Do something else. Don't call your Keypad a ton otherwise you'll tie up the I2C bus
      delay(25); //25 is good, more is better
    }

If you have a text editor (Notepad, Word, TextEdit, etc.) open and active from Example 2, press a button on the Qwiic Keypad. Or you can try using the textbox below to test. The outputs should be associated with each of the Qwiic keypad button press.

SparkFun Qwiic Pro Micro USB C Test Area

[**Warning!** Any text written in this textbox will be erased when you refresh this webpage!]

### [][Example 3c: Qwiic HID Mouse and Keyboard Combined](#hid_mouse_keyboard_qwiic)

This example combines 3a and 3b into one sketch. Copy and paste the code below into the Arduino IDE. Make sure to select the correct board and COM port that your respective board enumerated to.

    language:c
    /******************************************************************************
      Example_3c_Qwiic_HID_Mouse_Keyboard_Combined.ino
      Written by: Ho Yun "Bobby" Chan
      Date: February 6, 2020
      Development Environment Specifics:
        Arduino IDE 1.8.9

      Description:
        Based on the following examples:
          - Jim's Pro Micro "HID Mouse/Keyboard"
          - Wes' Qwiic Joystick "basic reading"
          - Pete's Qwiic Keypad "read button"

        This example controls the mouse with the Qwiic Joystick
        and keyboard presses associated with the Qwiic Keypad.
        The serial output is turned off so that Qwiic Pro Micro
        can respond faster.

      Libraries:
       Mouse.h (included with Arduino IDE)
       Keyboard.h (included with Arduino IDE)
       Wire.h (included with Arduino IDE)
       SparkFun_Qwiic_Joystick_Arduino_Library.h (included in the src folder) http://librarymanager/All#SparkFun_joystick
       SparkFun_Qwiic_Keypad_Arduino_Library.h (included in the src folder) http://librarymanager/All#SparkFun_keypad

      License:
        This code is released under the MIT License (http://opensource.org/licenses/MIT)

    ******************************************************************************/

    #include <Mouse.h>
    #include <Keyboard.h>
    #include <Wire.h>

    #include "SparkFun_Qwiic_Joystick_Arduino_Library.h" //Click here to get the library: http://librarymanager/All#SparkFun_joystick
    JOYSTICK joystick;                                   //Create instance of this object

    #include "SparkFun_Qwiic_Keypad_Arduino_Library.h" //Click here to get the library: http://librarymanager/All#SparkFun_keypad
    KEYPAD keypad1;                                    //Create instance of this object

    int vertZero, horzZero;       // Stores the initial value of each axis, usually around 512
    int vertValue, horzValue;     // Stores current analog output of each axis
    const int sensitivity = 150;  // Higher sensitivity value = slower mouse, should be <= about 500
    int mouseClickFlag = 0;

    //int invertMouse = 1;        //Invert joystick based on orientation
    int invertMouse = -1;         //Noninverted joystick based on orientation

    //Debug mode, comment one of these lines out using a syntax
    //for a single line comment ("//"):
    #define DEBUG 0       //0 = HID only
    //#define DEBUG 1     //1 = HID with serial output

    void setup() 
      if (keypad1.begin() == false) 

      delay(1000);  // short delay to let outputs settle
      vertZero = joystick.getVertical();  // get the initial values
      horzZero = joystick.getHorizontal();  // Joystick should be in neutral position when reading these

    #if DEBUG
      Serial.print("Initialized. Firmware Version: ");
      Serial.println(keypad1.getVersion());
      Serial.println("Press a button: * to do a space. # to go to next line.");
    #endif

      Mouse.begin(); //Init mouse emulation
      Keyboard.begin(); //Init keyboard emulation

    }//end setup

    void loop() 
      else if ((joystick.getButton()) && (mouseClickFlag)) // if the joystick button is not pressed
      

      if (button == -1) 

      else if (button != 0) 
        else if (button == '1') 
        else if (button == '2') 
        else if (button == '3') 
        else if (button == '4') 
        else if (button == '5') 
        else if (button == '6') 
        else if (button == '7') 
        else if (button == '8') 
        else if (button == '9') 
        else if (button == '#') 
        else if (button == '*') 
      }

      //Do something else. Don't call your Keypad a ton otherwise you'll tie up the I2C bus
      //Uncomment this if necessary but since we check the Qwiic Joystick it does not
      // appear to be an issue
      //delay(25); //25 is good, more is better

    }//end loop

The functionality should be the same when moving the joystick or pressing on the keypad\'s key. The serial output is turned off so that Qwiic Pro Micro can respond faster.

## Troubleshooting and FAQ

On this page you\'ll find troubleshooting tips and FAQs. Here\'s a directory of the subjects covered:

- **Troubleshooting**
  - [Serial Port Not Showing Up in \"Tools \> Board\" menu](#ts-serial)
  - [How to Reset to Bootloader](#ts-reset)
  - [How to Revive a \"Bricked\" Pro Micro](#ts-revive)
  - [Code Runs Upon Upload But Fails to Start After Power Cycle](#ts-brownout)
- **Frequently Asked Questions**
  - [What are VIDs and PIDs?](#faq-vid)
  - [How Can I Change the VID and PID on an ATmega32U4?](#faq-change-pid)
  - [Why Does my ATmega32U4 Board Show up Twice in the Device Manager?](#faq-twice)
  - [How Does the IDE Know Which COM Port to Use?](#faq-which)
  - [How Do I Reinstall the Bootloader?](#faq-reinstall)

------------------------------------------------------------------------

### [][Serial Port Not Showing Up in \'Tools \> Board\' Menu](#ts-serial)

The Qwiic Pro Micro can be a finicky little thing. There are a few series of events that can lead to its serial port being removed from the Arduino IDE\'s Serial Port selection menu. If you can\'t see your Pro Micro\'s serial port, give these steps a try:

1.  Close *all* Arduino windows. (Don\'t forget to save!)
2.  Unplug Qwiic Pro Micro from your computer.
3.  Wait a few seconds for the device to be detached.
4.  Plug Qwiic Pro Micro back in.
5.  Open Arduino back up, check the Serial Ports menu again.

### [][Reset to Bootloader](#ts-reset)

We ship the Qwiic Pro Micro with a modified version of the [Arduino Leonardo](https://www.sparkfun.com/products/11286) bootloader, with one major enhancement. When a Leonardo (or any device using the \"stock\" bootloader) is externally reset, it goes back into the bootloader\...and waits there eight seconds before it starts running the sketch. For some embedded projects, waiting eight seconds before a program runs isn\'t acceptable, so we modified the bootloader run time.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Arduino Leonardo](https://cdn.sparkfun.com/r/150-150/assets/learn_tutorials/1/1/1/4/11286-04a_Arduino_Leonardo_ATmega32U4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/11286-04a_Arduino_Leonardo_ATmega32U4.jpg)   [![Leonardo bootloader functionality](https://cdn.sparkfun.com/assets/a/c/5/3/f/523b7868757b7fbc468b4567.png)](https://cdn.sparkfun.com/assets/a/c/5/3/f/523b7868757b7fbc468b4567.png)

  *Arduino Leonardo*                                                                                                                                                                                                                      *Leonardo bootloader on\
                                                                                                                                                                                                                                          reset functionality.*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When a Qwiic Pro Micro is externally reset (by pulling the RST pin low), it\'ll only briefly (\<750ms) start the bootloader before continuing on to the sketch. If you need the bootloader to run longer, **resetting twice quickly** will get the Pro Micro to enter bootloader mode for eight seconds.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Pro Micro](https://cdn.sparkfun.com/r/150-150/assets/learn_tutorials/1/1/1/4/15795-Atmega32U4_Pro_Micro_C-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/15795-Atmega32U4_Pro_Micro_C-04.jpg)   [![Pro Micro bootloader functionality](https://cdn.sparkfun.com/assets/9/d/0/d/3/523b7867757b7f7b468b4569.png)](https://cdn.sparkfun.com/assets/9/d/0/d/3/523b7867757b7f7b468b4569.png)
  *Qwiic Pro Micro*                                                                                                                                                                                                          *Qwiic Pro Micro reset functionality. Press reset twice, quickly to enter bootloader mode.*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Resetting the Qwiic Pro Micro is now easier to reset with the built in reset button. Just press the reset button located next to the Qwiic connector two times. You can also connected the RST pin to ground to initiate a reset. This can be done with a small piece of wire, or an externally connected button.

[![Reset Button and Pin Locations](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/15795-Atmega32U4_Pro_Micro_C-Atmega32U4_Reset.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/4/15795-Atmega32U4_Pro_Micro_C-Atmega32U4_Reset.jpg)

Why would you need to enter bootloader mode in the first place. Glad you asked\...

### [][How to Revive a \"Bricked\" Pro Micro](#ts-revive)

Incorporating all of the USB tasks on a single chip is an awesome feature that makes the Pro Micro and boards like it truly unique. But it also places more stress on a single chip, and if anything goes wrong with that chip, the board becomes nearly unusable. It\'s not uncommon for Qwiic Pro Micro\'s to become \"bricked\" and unprogrammable. But, in most cases, the bricking is reversible!

*The* most common source of Qwiic Pro Micro \"bricking\" is uploading code to it with an **incorrectly set board** (e.g. programming a 16MHz/5V Pro Micro with the board set to 8MHz/3.3V). Also, make sure your sketch doesn\'t mess with the ATmega32U4\'s PLLCSR register, or any other register that sets up USB functionality on the ATmega32U4. The Pro Micro will actually take code compiled for the wrong operating speed, but when it tries to re-enumerate, you\'ll be greeted with a notification like this:

[![USB device not recognized](https://cdn.sparkfun.com/assets/a/7/2/d/3/523b7a11757b7fd5468b4567.png)](https://cdn.sparkfun.com/assets/a/7/2/d/3/523b7a11757b7fd5468b4567.png)

To revive the Pro Micro, you\'ll need to find a way to upload a sketch to it with the board option correctly set. We can do this with a little help from the bootloader.

First, you\'ll need to **set the serial port to the bootloader**. But that port is only visible when the board is in bootloader mode, so hit the reset button or pull the reset line low twice quickly to invoke the bootloader reset feature discussed above. **While the Pro Micro is in the bootloader** change the \'**Tools** \> **Serial Port**\' menu to the bootloader COM port. Quick! You\'ve only got eight seconds. On Windows, the bootloader\'s COM port number is usually one number higher than the Qwiic Pro Micro\'s regular port number.

With the serial port set, we\'re just about ready to re-upload our sketch. But first, **double check that the board is correctly set**. Then **reset to bootloader again**, and quickly upload your sketch. Again, you\'ll have to be quick\...you\'ve only got eight seconds. It may help to press the Upload keybind \-- [CTRL] + [U] / [CMD] + [U] \-- immediately after resetting.

It can take a few tries to get the timing right. Since the code has to compile first, it may help to **hit upload first** and then reset.

**Still having trouble getting that timing down?**

One of our customers (shout out to ***RichardDL***) has come up with a nifty solution (Windows only) to automate the bootloader process and program the board, by creating a batch file. Check out the details in [his forum post](https://community.sparkfun.com/t/reliable-program-load-to-pro-micro-using-bat-file/40399)!

### [][Code Runs After Upload But Fails to Start After Power Cycle](#ts-brownout)

We found that an ATmega32U4 (like the Pro Micro 3.3V/8MHz) can brown out when [outputting power to a boost converter](https://learn.sparkfun.com/tutorials/single-supply-logic-level-converter-hookup-guide#example-code). While code can run after uploading, a power cycle from the initial current draw to a boost converter is enough to cause the Pro Micro brown out. Thus causing the sketch to not run. This requires the user to toggle the reset button after a power cycle.

------------------------------------------------------------------------

### Frequently Asked Questions

If you\'re having technical difficulties with your Qwiic Pro Micro, see if any of the answers to these FAQs help. If not, please get in touch with our [tech support team](https://www.sparkfun.com/static/technical_assistance).

#### [][What are VID and PIDs?](#faq-vid)

VID is short for \'Vender Identification\' and PID is short for \'Part Identification\'. In other words, this pair of IDs defines the device. This is how your computer knows what you\'ve plugged in, what drivers to use with it, what COM port is assigned to it, etc. All native USB devices have a VID/PID.

All SparkFun ATmega32U4 boards share the same VID \-- 0x1B4F, and they all have unique PIDs. 5V Pro Micros lay claim to PIDs 0x9205 and 0x9206 (one for the bootloader, one for the sketch). 3.3V Pro Micros will show up as 0x9203 and 0x9204 for bootloader and sketch, respectively. And the Fio v3 has 0xF100 and 0xF101.

#### [][How Can I Change the VID and PID on an ATMega32U4 Board?](#faq-change-pid)

Every time you upload code the VID and PID are uploaded to the device. These values are located in the \'**boards.txt**\' file and will therefore be determined by the board you have selected. Keep in mind that if you select the wrong board you will get the wrong VID/PID uploaded which means the computer can't recognize, and program the board. The VID/PID for the bootloader is part of the bootloader file. To change this you will need to recompile the bootloader with the new VID/PID, and upload it.

#### [][Why Does my ATMega32U4 Board Show up Twice in Device Manager?](#faq-twice)

Both the bootloader and the sketch have their own VID/PIDs. When you plug in a board the bootloader starts running for a few seconds, and you will see the board show up in Device Manager based on those VID/PIDs. After a few seconds, the sketch will start running, and you will see Device Manager disconnect from the bootloader and connect to the sketch.

#### [][How Does the IDE Know Which COM Port to Use?](#faq-which)

When the IDE resets the board, the COM port is disconnected from the computer. The IDE then looks for a new COM port. This is the port it uses. This is one of those weird things Arduino did to get things to work on this chip.

#### [][How Do I Reinstall the Bootloader?](#faq-reinstall)

Check out or [reinstalling the bootloader tutorial](https://www.sparkfun.com/tutorials/247), which should work for both ATMega32U4 and ATMega328 boards. If you have the [tools](https://www.sparkfun.com/categories/7) to do so, reinstalling the bootloader is often easier then trying to stay in the bootloader. Since reinstalling the bootloader puts the board back in factory settings this will reset the VID/PID numbers allowing your board to work again.