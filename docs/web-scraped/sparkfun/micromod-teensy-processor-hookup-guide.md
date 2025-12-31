# Source: https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroMod Teensy Processor Hookup Guide

# MicroMod Teensy Processor Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1266&name=MicroMod+Teensy+Processor+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1266 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+Teensy+Processor+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1266&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1266&t=MicroMod+Teensy+Processor+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1266&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F6%2F6%2FMM_Teensy_PB_Thumb.jpg&description=MicroMod+Teensy+Processor+Hookup+Guide "Pin It")

## Introduction

The SparkFun [MicroMod Teensy Processor](https://www.sparkfun.com/products/16402) leverages the awesome computing power of the NXP iMXRT1062 chip and pairs it with the M.2 MicroMod connector to allow you to plug it into your choice of compatible MicroMod Carrier Board. The computing power of the ARM Cortex-M7 processer operates at clock speeds up to 600MHz with 16MB of Flash memory and 1024K RAM.

[![SparkFun MicroMod Teensy Processor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/1/3/2/16402-SparkFun_MicroMod_Teensy_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html)

### [SparkFun MicroMod Teensy Processor](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html) 

[ DEV-16402 ]

This board leverages the awesome computing power of the NXP iMXRT1062 chip (ARM Cortex-M7) and pairs it with the M.2 MicroMod...

[ [\$24.95] ]

On top of excellent processing power and speed, the Teensy Processor offers a plethora of interface options including seven serial UART ports as well as four I^2^C buses and two SPI ports. Along with these standard interfaces, the Teensy Processor Board also features USB Host and Device capability up to 480Mbit/s, a CAN-Bus and a digital audio interface.

Teensy is a registered trademark of [PJRC](https://www.pjrc.com/). The MicroMod Teensy is a collaboration between [PJRC](https://www.pjrc.com/) and SparkFun.

### Required Materials

Along with your MicroMod Teensy Processor, you\'ll need a Carrier Board to plug your Processor into. SparkFun offers a variety of MicroMod Carrier Boards to fit your project\'s needs:

[![SparkFun MicroMod ATP Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/1/2/16885-SparkFun_MicroMod_ATP_Carrier_Board-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html)

### [SparkFun MicroMod ATP Carrier Board](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html) 

[ DEV-16885 ]

If you need a \"lot\" of GPIO with a simple to program, ready to go to market module, the ATP is the fix you need.

[ [\$20.50] ]

[![SparkFun MicroMod Data Logging Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/5/0/16829-SparkFun_MicroMod_Data_Logging_Carrier_Board-01A.jpg)](https://www.sparkfun.com/sparkfun-micromod-data-logging-carrier-board.html)

### [SparkFun MicroMod Data Logging Carrier Board](https://www.sparkfun.com/sparkfun-micromod-data-logging-carrier-board.html) 

[ DEV-16829 ]

The MicroMod Data Logging Carrier offers a low-power data logging platform using the MicroMod system allowing you to choose y...

[ [\$22.95] ]

[![SparkFun MicroMod Input and Display Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/9/2/2/16985-SparkFun_MicroMod_Input_and_Display_Carrier_Board-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-input-and-display-carrier-board.html)

### [SparkFun MicroMod Input and Display Carrier Board](https://www.sparkfun.com/sparkfun-micromod-input-and-display-carrier-board.html) 

[ DEV-16985 ]

Add data, input, & visibility to your project with a 2.4\" TFT display, 6 addressable LEDs, onboard voltage regulator, 6 pin I...

[ [\$61.50] ]

[![SparkFun MicroMod Weather Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/0/3/16794-SparkFun_MicroMod_Weather_Carrier_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-micromod-weather-carrier-board.html)

### [SparkFun MicroMod Weather Carrier Board](https://www.sparkfun.com/sparkfun-micromod-weather-carrier-board.html) 

[ SEN-16794 ]

The MicroMod Weather Carrier Board periphery for the MicroMod ecosystem that allows you to create your own weather station wi...

**Retired**

You\'ll also need a USB-C cable to connect the Carrier to your computer and if you want to add some Qwiic breakouts to your MicroMod project you\'ll want at least one Qwiic cable. Below are some options for both of those cables:

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

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

Depending on which Carrier Board you choose, you may need a few extra peripherals to take full advantage of them. Refer to the Carrier Boards\' respective Hookup Guides for specific recommendations.

### Suggested Reading

The SparkFun MicroMod ecosystem offers a unique way to allow users to customize their project to their needs. Do you want to send your weather data via a wireless signal (e.g. Bluetooth or WiFi)? There\'s a MicroMod Processor for that. Looking to instead maximize efficiency and processing power? You guessed it, there\'s a MicroMod Processor for that. If you are not familiar with the MicroMod ecosystem, take a look here:

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading here for an overview:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend reading through the following tutorials if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy)

### Getting Started with the Teensy 

Basic intro to the Teensy line of products, with soldering and programming suggestions.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1266&name=MicroMod+Teensy+Processor+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1266 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+Teensy+Processor+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1266&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1266&t=MicroMod+Teensy+Processor+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1266&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F6%2F6%2FMM_Teensy_PB_Thumb.jpg&description=MicroMod+Teensy+Processor+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/hardware-assembly) [Software Setup](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/software-setup) [Arduino Example: Blink](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/arduino-example-blink) [Troubleshooting](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/troub) [Resources and Going Further](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/resources-and-going-further)

[Comments [9]](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/micromod-teensy-processor-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [MicroMod](https://learn.sparkfun.com/tutorials/tags/micromod)
  - [Teensy](https://learn.sparkfun.com/tutorials/tags/teensy)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]