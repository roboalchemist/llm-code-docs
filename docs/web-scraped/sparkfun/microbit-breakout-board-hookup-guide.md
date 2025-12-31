# Source: https://learn.sparkfun.com/tutorials/microbit-breakout-board-hookup-guide

## Introduction

The [micro:bit](https://www.sparkfun.com/products/14208), by itself, offers a vast array of possibilities and potential projects, considering it includes an onboard temperature sensor, accelerometer, compass, LED array, Bluetooth radio, and more. However, when you\'re ready to branch out beyond those initial capabilities, like connecting to an SD card for logging, or taking advantage of one of our many Qwiic boards, you\'ll need to break out some of the pins on the micro:bit\'s card edge connector. For that, we\'ve got you covered with the micro:bit Breakout Board.

[![SparkFun Qwiic micro:bit Breakout (with Headers)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/3/0/2/16446-SparkFun_micro-bit_Breakout__with_Headers_-02.jpg)](https://www.sparkfun.com/sparkfun-qwiic-micro-bit-breakout-with-headers.html)

### [SparkFun Qwiic micro:bit Breakout (with Headers)](https://www.sparkfun.com/sparkfun-qwiic-micro-bit-breakout-with-headers.html) 

[ BOB-16446 ]

The SparkFun Qwiic micro:bit Breakout with Headers is a board that connects to the BBC micro:bit and expands the capabilities...

[ [\$6.25] ]

There\'s also a [version without headers](https://www.sparkfun.com/products/16445), if you care to solder your own or use wires instead.

### Required Materials

To follow along with this project tutorial, you will need the following materials:

### Suggested Reading

If you have not yet used the micro:bit, check out this guide first.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit)

### Getting Started with the micro:bit 

September 2, 2021

The BBC micro:bit is a compact, powerful programming tool that requires no software installation. Read on to learn how to use it YOUR way!

If you aren\'t familiar with the Qwiic system and plan to use the Qwiic connectors on this breakout board, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

## Hardware Overview

The micro:bit Breakout board allows you to utilize all of the pins on the micro:bit and opens up some previously inaccessible communication ports, like [I^2^C](https://learn.sparkfun.com/tutorials/i2c) and [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi).

### Pins

Most of the micro:bit\'s pins can be configured for one or more functions.

[![Top-down diagram of the micro:bit breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/5/16446-SparkFun_micro-bit_breakout_wHeaders-Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/16446-SparkFun_micro-bit_breakout_wHeaders-Pins.jpg)

  Pin   Function 1   Function 2     Description
  ----- ------------ -------------- ------------------------------------
  GND                               Ground
  GND                               Ground
  3V3                               3.3V
  0     Analog In                   Connected to large pin 0
  1     Analog In                   Connected to large pin 1
  2     Analog In                   Connected to large pin 2
  3     Analog In    LED Column 1   Controls part of LED array
  4     Analog In    LED Column 2   Controls part of LED array
  5                  Button A       Connected to Button A on micro:bit
  6                  LED Column 9   Controls part of LED array
  7                  LED Column 8   Controls part of LED array
  8                                 Open GPIO pin
  9                  LED Column 7   Controls part of LED array
  10    Analog In    LED Column 3   Controls part of LED array
  11                 Button B       Connected to Button B on micro:bit
  12                                Open GPIO pin
  13    SCK                         GPIO or SPI clock
  14    MISO                        GPIO or SPI MISO
  15    MOSI                        GPIO or SPI MOSI
  16                                Open GPIO pin
  19    SCL                         GPIO or I^2^ clock
  20    SDA                         GPIO or I^2^ data

### Power Pin

The pin listed as **3V3** can be used as an input (regulated 3.3V, do not exceed 3.6V!) or an output if you plug a battery pack or USB into the micro:bit.

### LCn Pins

The pins labeled with LCn (e.g. LC1, LC8) refer to pins that are used to control the LED array on the front of the micro:bit. You can use them as GPIO, but you\'ll often get weird patterns to show up on the LEDs, or when you write to the LED array, you may see unexpected behavior. If you use them as GPIO, we recommend [disabling the LED display](https://pxt.microbit.org/reference/led/enable).

### Qwiic Connectors

We\'ve added a couple of Qwiic connectors on either side of the breakout board to take advantage of the I^2^C bus. For more information on the qwiic system, head on over to the [Qwiic Connect System Landing Page](https://www.sparkfun.com/qwiic).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/5/16446-SparkFun_micro-bit_breakout_wHeaders-QwiicConnectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/16446-SparkFun_micro-bit_breakout_wHeaders-QwiicConnectors.jpg)

### Board Outline

[![Outline of board 16446. Measurements in inches](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/5/16446-BoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/16446-BoardOutline.png)

*Click on the image for a closer view*

## Hardware Assembly

### Attach Headers

If you have the version of the breakout board without headers, solder some [breakaway headers](https://www.sparkfun.com/products/116) to the board. You can also solder [wire](https://www.sparkfun.com/products/11367) directly to the breakout.

[![Solder headers to the micro:bit Breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/5/Micro-Bit_v2_Update-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/Micro-Bit_v2_Update-01.jpg)

### Build Example Circuit

**Note:** The micro:bit must be facing up in order to make electrical connections to the pins.

To begin, let\'s light up an RGB LED. Attach the micro:bit to the breakout board, place the breakout board onto a breadboard, and connect an RGB LED through 330 Ω resistors. Use the image below to aid you in wire up the circuit.

Remember, LEDs are [polarized](https://learn.sparkfun.com/tutorials/polarity) parts and can only work properly in one orientation. The longest leg of the LED goes where the black GND wire is in the circuit.

[![micro:bit breakout board hookup Fritzing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/5/microbit_breakout_02_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/microbit_breakout_02_bb.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

## Example: Cycling Colors on an RGB LED

You can download the code from the emulator, or check out the project\'s page [here](https://pxt.microbit.org/79804-34692-16068-09932):

\
Copy the *.hex* file to your micro:bit drive, and you should see a fancy array of colors appear on your LED!

[![micro:bit cycling colors](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/Micro-bit_V2_Update_2.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/Micro-bit_V2_Update_2.gif)

## Example: Qwiic Sensor

With the addition of Qwiic connectors on the micro:bit breakout board, you can take advantage of the sensors in our [Qwiic Connect System](https://www.sparkfun.com/qwiic). Let\'s take a \"qwiic\" look at how to attach and use Qwiic boards.

You can download the code from the emulator, or check out the project\'s page [here](https://makecode.microbit.org/_Ryt5C4P8oJfj):

\
Copy the *.hex* file to your micro:bit drive and you should see the temperature start scrolling by on your micro:bit\'s LED array!

[![Temp is scrolling by on LED array](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/Qwiic_TMP117.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/Qwiic_TMP117.gif)

### Reading the sensor

There are a couple of things to point out here. In this example, we\'ve used the Qwiic TMP117 sensor. Somewhat superfluous, given that the micro:bit has an onboard temp sensor but it\'s easy and I happened to have one handy.

To read the sensor, you need to be able to access the I^2^C bus. In [MakeCode](https://makecode.microbit.org/), under **Pins-\>More**, you\'ll find the blocks for reading these pins.

[![Find the I2C functions under pins-\>more](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/5/Pins-More.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/5/Pins-More.png)

To determine the address, you\'ll need to find the address of your qwiic sensor (in this case, the TMP117\'s address is 0x48) and then convert that to decimal. I used a handy dandy calculator [here](https://www.rapidtables.com/convert/number/hex-to-decimal.html). The hookup guides for each qwiic sensor will have their default address, as well as information on the datatype.

The multiplication step after getting the data from the sensor is specific to the TMP117 and is just a conversion to make the data legible to us mere humans.

Voila! Now grab a qwiic sensor and get to hacking!

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