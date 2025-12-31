# Source: https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v

## Introduction

**Heads up!** This tutorial was written originally written for the Arduino Pro Mini 3.3V/8MHz. However, you can still use this as a guide to upload code for Arduino Pro Mini 5V/16MHz. To upload adjust the Processor in the Arduino IDE when uploading code to the 5V version board.

The original, true-blue [Arduino](https://www.sparkfun.com/products/11021) is open-source hardware, which means anyone is free to download the design files and spin their own version of the popular development board. SparkFun has jumped on this opportunity and created all sorts of Arduino variants, each with their own unique features, dimensions, and applications. Now one of those variants has landed in your hands; congratulations! It\'s a wild world out there in microcontroller-land, and you\'re about to take your first step away from the wonderful \-- though sometimes stifling \-- simplicity of the Arduino Pro Mini. There are two variants, the 5V/16MHz and the 3.3V/8MHz.

[![Arduino Pro Mini 328 - 5V/16MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/6/5/3/9/11113-01b.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html)

### [Arduino Pro Mini 328 - 5V/16MHz](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html) 

[ DEV-11113 ]

SparkFun\'s minimal design approach to Arduino. This is a 5V Arduino running the 16MHz bootloader.

[ [\$11.25] ]

[![Arduino Pro Mini 328 - 3.3V/8MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/6/5/4/0/11114-01.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html)

### [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html) 

[ DEV-11114 ]

SparkFun\'s minimal design approach to Arduino. This is a 3.3V Arduino running the 8MHz bootloader.

[ [\$11.25] ]

For the scope of this tutorial, we\'ll go over how to set up and use the [3.3V Arduino Pro Mini](https://www.sparkfun.com/products/11114), everything from assembling the tiny Arduino to programming it.

### Required Materials

To follow along, you\'ll need a few extra items. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. At a minimum you will need, some headers, USB cable, and FTDI. The FTDI Basic will be used to program (and power) the Pro Mini. The headers are optional, but they\'re our preferred way to interface other devices to the Pro Mini.

**Starter Kits:** If you are looking for additional components to prototype, check out some of the related starter kits.\
\

[![SparkFun Arduino Pro Mini Starter Kit - 5V/16MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/2/1/15254-SparkFun_Arduino_Pro_Mini_Starter_Kit_-_5V_16MHz-01.jpg)](https://www.sparkfun.com/products/15254)

### [SparkFun Arduino Pro Mini Starter Kit - 5V/16MHz](https://www.sparkfun.com/products/15254) 

[ KIT-15254 ]

What\'s blue, thin, and comes with everything you need to get started? The Pro Mini 5V Starter Kit!

**Retired**

[![SparkFun Arduino Pro Mini Starter Kit - 3.3V/8MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/2/4/15257-SparkFun_Arduino_Pro_Mini_Starter_Kit_-_3.3V_8MHz-01.jpg)](https://www.sparkfun.com/products/15257)

### [SparkFun Arduino Pro Mini Starter Kit - 3.3V/8MHz](https://www.sparkfun.com/products/15257) 

[ KIT-15257 ]

What\'s blue, thin, and comes with everything you need to get started? The Pro Mini 3.3V Starter Kit!

**Retired**

\

### Tools

Assembly of the Pro Mini also requires [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering). This is a great place to start soldering, if you\'ve never done it before! The joints are all easy, through-hole jobs. So grab a [soldering iron](https://www.sparkfun.com/products/9507), some [solder](https://www.sparkfun.com/products/9163) and [general soldering accessories](https://www.sparkfun.com/categories/49).

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

### Suggested Reading

This project tutorial builds on a few more conceptual tutorials. If you\'re not familiar with the subjects below, consider reading through their respective tutorials first:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/sparkfun-usb-to-serial-uart-boards-hookup-guide)

### SparkFun USB to Serial UART Boards Hookup Guide 

How to use the SparkFun FTDI based boards to program an Arduino and access another serial device over the hardware serial port, without unplugging anything!

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

**Note:** Besides the FTDI that is used in this tutorial, there are other USB-to-serial converters (e.g. [CH340](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers), CP210X, CY7C65213, etc.) that can be used to upload code to the Arduino Pro Mini. Make sure to check out the board and install the respective driver for your USB-to-serial converter.

## What It Is (and Isn\'t)

So what differentiates the Arduino Pro Mini from the Arduino Uno? Well, the most obvious difference is the form factor. The Pro Mini\'s pretty\...mini, measuring in at just 1.3x0.70\". It\'s about ⅙th the size of the Arduino Uno. The compact size is great for projects where you may need to fit the Arduino into a tiny enclosure, but it also means that the Pro Mini is **not physically compatible with Arduino shields** (you could still hard-wire the Mini up to any Arduino shield).

[![Pro Mini size comparison](https://cdn.sparkfun.com/assets/0/2/0/4/e/51eed447ce395f924b000000.png)](https://cdn.sparkfun.com/assets/0/2/0/4/e/51eed447ce395f924b000000.png)

*Comparing the size of a standard Arduino Uno with the (aptly named) Pro Mini.*

The Mini packs almost as much microprocessor-punch as the regular Arduino, but there are a few major hardware changes you should be aware of before you start adapting your project to the Mini. The first glaring hardware difference is the voltage that the Mini operates at: **3.3V**. Unlike the Arduino Uno, which has both a 5V and 3.3V regulator on board, the Mini only has one regulator. This means that if you\'ve got peripherals that only work at 5V, you might have to do some [level shifting](https://learn.sparkfun.com/tutorials/retired---using-the-logic-level-converter) before you hook it up to the Pro Mini (or you could go for the [5V variant](http://www.sparkfun.com/products/9218) of the Pro Mini).

Another major variation from the standard Arduino lies in the speed at which the ATmega328 runs. The Pro Mini 3.3V runs at **8MHz**, half the speed of an Arduino Uno. We put a slower resonator on the Mini to guarantee safe operation of the ATmega. That said, don\'t let the slower speed scare you away from using the Mini; 8MHz is still plenty fast, and the Mini will still be capable of controlling almost any project the Arduino Uno can.

[![Speed grades of ATmega328](https://cdn.sparkfun.com/r/600-600/assets/b/e/2/c/e/51eebc0bce395f3779000002.png)](https://cdn.sparkfun.com/assets/b/e/2/c/e/51eebc0bce395f3779000002.png)

One last missing piece of hardware is the Atmega16U2-based USB-to-Serial converter, and the USB connector that goes with it. All of the USB circuitry had to be eliminated for us to make the Pro Mini as small as possible. The absence of this circuit means an external component, the [FTDI Basic Breakout](http://www.sparkfun.com/products/9873) or any USB-to-serial converter, is required to upload code to the Arduino Pro Mini.

[![The FTDI Basic Breakout](https://cdn.sparkfun.com/r/400-400/assets/b/2/e/d/6/51eebc54ce395fc078000001.png)](http://www.sparkfun.com/products/9873)

**Note:** Besides the FTDI that is used in this tutorial, there are other USB-to-serial converters (e.g. [CH340](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers), CP210X, CY7C65213, etc.) that can be used to upload code to the Arduino Pro Mini. Make sure to check out the board and install the respective driver for your USB-to-serial converter.

### Schematic and Pin-out

The schematic of the Pro Mini can be broken down into three blocks: the voltage regulator, the ATmega328 and supporting circuitry, and the headers.

[![Schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/4/v14Scematic.png)](https://cdn.sparkfun.com/datasheets/Dev/Arduino/Boards/Arduino-Pro-Mini-v14.pdf)

The Pro Mini\'s pins surround three of the four sides. The pins on the short side are used for programming, they match up to the FTDI Basic Breakout. The pins on the other two sides are an assortment of power and GPIO pins (just like the standard Arduino).

[![Annotated Pro Mini pins](https://cdn.sparkfun.com/assets/5/8/e/6/5/51eec3b1ce395f4b4b000000.png)](https://cdn.sparkfun.com/assets/5/8/e/6/5/51eec3b1ce395f4b4b000000.png)

There are three different power-related pins: GND, VCC, and RAW. GND, obviously, is the common/ground/0V reference. RAW is the input voltage that runs into the regulator. The voltage at this input can be anywhere from 3.4 to 12V. The voltage at VCC is supplied directly to the Pro Mini, so any voltage applied to that pin should already be regulated to 3.3V.

Four pins are actually not located on the edge of the board: A4, A5, A6 and A7. Each of these analog pins is labeled on the back side of the board.

[![Back of board](https://cdn.sparkfun.com/assets/7/f/8/e/f/51eec494ce395f6f4c000000.png)](https://cdn.sparkfun.com/assets/7/f/8/e/f/51eec494ce395f6f4c000000.png)

A4 and A5\'s location may be very important if you plan on using [I^2^C](https://learn.sparkfun.com/tutorials/i2c) with the Pro Mini \-- those are the hardware SDA and SCL pins.

More information about pins can be found in our graphical datasheets. The pinout listed on both datasheets are the same. The only difference is the voltage and frequency that the board operates at.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Graphical Datasheet for the 5V/16Mhz Version](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/4/Graphical_Datasheet_Arduino_ProMini-5V_16MHzV2.png)](https://cdn.sparkfun.com/assets/d/5/2/f/0/ProMini16MHzv2.pdf)   [![Graphical Datasheet for the 3.3V/8MHz Version](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/4/Graphical_Datasheet_Arduino_ProMini-3_3V_8MHzV2.png)](https://cdn.sparkfun.com/assets/c/6/2/2/1/ProMini8MHzv2.pdf)
  *Graphical Datasheet for the 5V/16Mhz Version*                                                                                                                                                                                        *Graphical Datasheet for the 3.3V/8MHz Version*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Assembly

The Arduino Pro Mini doesn\'t look like much when you first get it; it\'s as bare-bones as can be. We\'ve left it up to you to [solder headers](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) or [wires](https://learn.sparkfun.com/tutorials/working-with-wire) into the open through-holes. There are a few things to make you aware of though.

First, decide how you want to connect the FTDI Basic Breakout to the Pro Mini\'s **programming header**. The programming header is a row of six pins on the side of the board, labeled \"BLK\", \"GND\", \"VCC\", \"RXI\", \"TXO\", and \"GRN\". Since the FTDI Basic board is equipped with a female header, it\'s usually best to equip your Mini\'s programming header with mating male headers, either [straight](http://www.sparkfun.com/products/116) or [right-angle](http://www.sparkfun.com/products/553).

[![Breadboarded Pro Mini](https://cdn.sparkfun.com/assets/7/7/6/1/5/51eec580ce395f7d4b000000.png)](https://cdn.sparkfun.com/assets/7/7/6/1/5/51eec580ce395f7d4b000000.png)

*This Pro Mini had male headers soldered into all pins, so it could slot directly into a breadboard. Notice the programming header pins are soldered \"upside-down\", to keep them accessible.*

**Warning:** Make sure to match the [logic levels](https://learn.sparkfun.com/tutorials/logic-levels/all) for the USB-to-Serial Converter and the Arduino Pro Mini that you are using. For FTDI\'s, there can be an option to adjust the logic levels to either 3.3V or 5V by [cutting a trace and adding a solder jumper](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all#cutting-a-trace-between-jumper-pads).

The remaining assembly choices are up to you. There are many options; you could solder in male headers to make it breadboard-compatible, [female headers](http://www.sparkfun.com/products/115) to make it compatible with [jumper wires](http://www.sparkfun.com/products/9387), or just solder [stranded-wire](https://www.sparkfun.com/products/11375) straight into the pins.

[![Uncertain 7-Cube assembly](https://cdn.sparkfun.com/assets/5/8/3/7/8/51eec60fce395f954b000000.png)](https://cdn.sparkfun.com/assets/5/8/3/7/8/51eec60fce395f954b000000.png)

*The Arduino Pro Mini in the [Uncertain 7-Cube Project](https://learn.sparkfun.com/tutorials/the-uncertain-7-cube) used a combination of right and straight male headers.*

Versatility is what makes this board so great, and you can assemble it in whatever way makes the most sense for your project.

## Powering

The most important factor in any project is [what\'s going to power it](https://learn.sparkfun.com/tutorials/how-to-power-a-project). The Pro Mini doesn\'t have a barrel jack, or any other obvious way to connect a power supply, so how do you power the thing?

Pick a power source that suits your project. If you want something that matches the compactness of the Pro Mini, a battery \-- [LiPo](http://www.sparkfun.com/products/339), [alkaline](http://www.sparkfun.com/products/9100), [coin cell](http://www.sparkfun.com/products/338), etc. \-- may be a good choice. Or you could use a [wall power supply](https://www.sparkfun.com/products/8269) along with a [barrel jack adapter](http://www.sparkfun.com/products/10288).

If you have a supply that\'s **greater than 3.3V** (but less than 12V), you\'ll want to connect that to the **RAW** pin on the Mini. This pin is akin to the VIN pin, or even the barrel jack, on the Arduino Uno. The voltage applied here is regulated to 3.3V before it gets to the processor.

If you already have a **regulated 3.3V source** from somewhere else in your project, you can connect that directly to the VCC pin. This will bypass the regulator and directly power the ATmega328. Don\'t forget to connect the grounds (GND) too!

There is a third power option that\'s only usually available while you\'re programming the Pro Mini. The FTDI Basic Breakout can be used to power the Mini via your computer\'s USB port. Keep in mind that this option may not be available when your project has entered the wild, absent from any computers or USB supplies.

[![FTDI powering and programming the Pro Mini](https://cdn.sparkfun.com/assets/9/6/5/5/b/51eec92ece395ffc4b000000.png)](https://cdn.sparkfun.com/assets/9/6/5/5/b/51eec92ece395ffc4b000000.png)

That leads us to the next section\...programming the Arduino Pro Mini.

**Heads up!** This tutorial was written originally written for the Arduino Pro Mini 3.3V/8MHz. If you are using an Arduino Pro Mini 5V/16MHz, you will be using a 5V FTDI. To upload adjust the Processor in the Arduino IDE when uploading code to the 5V version board.

**Warning:** Make sure to match the [logic levels](https://learn.sparkfun.com/tutorials/logic-levels/all) for the USB-to-Serial Converter and the Arduino Pro Mini that you are using. For FTDI\'s, there can be an option to adjust the logic levels to either 3.3V or 5V by [cutting a trace and adding a solder jumper](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all#cutting-a-trace-between-jumper-pads).

## Programming

### Arduino IDE

If you\'ve never used an Arduino before (how bold of you to go straight for the Mini!), you\'ll need to download the [Arduino IDE](http://arduino.cc/en/Main/Software). Check out our tutorial on [installing Arduino](https://learn.sparkfun.com/tutorials/installing-arduino-ide) for help on that subject.

### Drivers

If this is the first time that you have plugged the FTDI Basic Breakout into your computer, you may need to install drivers for it. Check out our [Installing FTDI Drivers tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) for help there as suggested earlier in the tutorial.

**Note:** Besides the FTDI that is used in this tutorial, there are other USB-to-serial converters (e.g. [CH340](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers), CP210X, CY7C65213, etc.) that can be used to upload code to the Arduino Pro Mini. Make sure to check out the board and install the respective driver for your USB-to-serial converter.

### Uploading Code

Once both Arduino and the FTDI drivers are installed, it\'s time to get programming. We\'ll start by uploading everyone\'s favorite sketch: **Blink**. Open up Arduino, then open the Blink sketch by going to *File \> Examples \> 01.Basics \> Blink*.

[![Opening Blink](https://cdn.sparkfun.com/assets/f/0/4/6/7/51eed021ce395f684b000000.png)](https://cdn.sparkfun.com/assets/f/0/4/6/7/51eed021ce395f684b000000.png)

Before we can upload the sketch to the Mini, you\'ll need to tell Arduino what **board** you\'re using. Go to *Tools \> Board* and select **Arduino Pro or Pro Mini**.

[![Tools \> Board \> Arduino Pro or Pro Mini](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/4/pro-mini-board-01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/4/pro-mini-board-01.png)

Then, go back up to **Tools \> Processor** and select **ATmega328 (3.3V, 8MHz)**. This tells Arduino to compile the code with an 8MHz clock speed in mind, that way the `delay(1000);` calls will actually delay one second.

[![Tools \> Processor \> ATmega328 (3.3V, 8MHz)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/4/pro-mini-board-02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/4/pro-mini-board-02.png)

**Heads up!** This tutorial was written originally written for the Arduino Pro Mini 3.3V/8MHz. If you are using an Arduino Pro Mini 5V/16MHz, you would select **ATmega328 5V/16MHz** under the Processor in the Arduino IDE when uploading code to the 5V version board.

You\'ll next need to tell Arduino which **serial port** your FTDI Basic Breakout has been assigned to. On Windows this will be something like COM2, COM3, etc. On Mac it\'ll look something like */dev/tty.usbserial-A6006hSc*.

[![Tools \> Port \> Select Port](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/4/pro-mini-port.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/4/pro-mini-port.png)

Finally, you\'re all set to upload the sketch to your Mini. Click on the **Upload** button (the right-pointing arrow). After a few moments you should see the red and green RX/TX LEDs on your FTDI board flash, followed by a "Done Uploading" message in Arduino\'s status bar. Voilà, Blinky! The Mini may be missing a few components, but it\'s got the most important component: LEDs!