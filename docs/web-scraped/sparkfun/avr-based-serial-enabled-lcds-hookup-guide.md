# Source: https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- AVR-Based Serial Enabled LCDs Hookup Guide

# AVR-Based Serial Enabled LCDs Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft789&name=AVR-Based+Serial+Enabled+LCDs+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft789 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=AVR-Based+Serial+Enabled+LCDs+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft789&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft789&t=AVR-Based+Serial+Enabled+LCDs+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft789&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F7%2F8%2F9%2FTutorialThumbnail.jpg&description=AVR-Based+Serial+Enabled+LCDs+Hookup+Guide "Pin It")

## Introduction

[] **Heads up!** The latest versions of these LCDs have a Qwiic connector. The previous versions did not. Some of the pictures in this tutorial are from the previous version of the hardware, however because the change is rather minor, they are still relevant. The pinouts along the edge are still the same order and position (except for the left-most cluster of 4 PTH pins).

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/9/ADM1602N1.jpg "SerLCD hardware example showing qwiic connector on back side of PCB")](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/9/ADM1602N1.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/9/ADM1602N__V2.6.jpg "Older hardware example shoing no qwiic connector")](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/9/ADM1602N__V2.6.jpg)

  *Newer versions have qwiic connector!*                                                                                                                                                                                  *Older versions do not have a qwiic connector.*
                                                                                                                                                                                                                          
  Silk will look like \"ADM1602N1\".                                                                                                                                                                                      Silk will look like \"ADM1602N_v2.6\"
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Also note!** Throughout the tutorial, the name \"**SerLCD**\" will refer to the hardware. **OpenLCD** will refer to the firmware.

The [AVR-based serial enabled LCD (a.k.a. SerLCD)](https://www.sparkfun.com/products/16398) is a simple and cost effective solution for adding Liquid Crystal Displays (LCDs) into your project. The PCB design on the back of the screen includes an ATmega328P that handles all of the screen control. It can accept commands via serial, I^2^C and SPI. The latest versions also include a Qwiic connector for solder-less single-cable connection setup. This simplifies the number of wires needed and allows your project to display all kinds of text and numbers. We offer three varieties of the AVR-based Serial Enabled LCDs:

[![SparkFun 16x2 SerLCD - RGB Text (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/1/2/3/16397-SparkFun_16x2_SerLCD_-_RGB_Backlight__Qwiic_-05.jpg)](https://www.sparkfun.com/sparkfun-16x2-serlcd-rgb-text-qwiic.html)

### [SparkFun 16x2 SerLCD - RGB Text (Qwiic)](https://www.sparkfun.com/sparkfun-16x2-serlcd-rgb-text-qwiic.html) 

[ LCD-16397 ]

The SparkFun Qwiic SerLCD is a serial enabled LCD that provides a simple and cost effective solution for adding a 16x2 RGB on...

[ [\$32.50] ]

[![SparkFun 16x2 SerLCD - RGB Backlight (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/1/2/2/16396-SparkFun_16x2_SerLCD_-_RGB_Backlight__Qwiic_-05.jpg)](https://www.sparkfun.com/sparkfun-16x2-serlcd-rgb-backlight-qwiic.html)

### [SparkFun 16x2 SerLCD - RGB Backlight (Qwiic)](https://www.sparkfun.com/sparkfun-16x2-serlcd-rgb-backlight-qwiic.html) 

[ LCD-16396 ]

The SparkFun Qwiic SerLCD is a serial enabled LCD that provides a simple and cost effective solution for adding a 16x2 Black ...

[ [\$32.50] ]

[![SparkFun 20x4 SerLCD - RGB Backlight (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/1/2/4/16398-SparkFun_16x2_SerLCD_-_RGB_Backlight__Qwiic_-05.jpg)](https://www.sparkfun.com/sparkfun-20x4-serlcd-rgb-backlight-qwiic.html)

### [SparkFun 20x4 SerLCD - RGB Backlight (Qwiic)](https://www.sparkfun.com/sparkfun-20x4-serlcd-rgb-backlight-qwiic.html) 

[ LCD-16398 ]

The SparkFun Qwiic SerLCD is a serial enabled LCD that provides a simple and cost effective solution for adding a 20x4 Black ...

[ [\$42.95] ]

The firmware is fully opensource and available for download at the [GitHub repo here](https://github.com/sparkfun/OpenLCD):

[OpenLCD Firmware GitHub Repository](https://github.com/sparkfun/OpenLCD)

This allows for any customizations you may need. Uploading firmware (custom or updates), is easily done from the Arduino IDE using a [Serial Basic](https://www.sparkfun.com/products/14050). See [firmware update instructions](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/all#troubleshooting) in the troubleshooting section of this tutorial for more info.

Also note, the example code used below is all available in the repo (along with many more examples). Before beginning this tutorial, it\'s a good idea to clone the repository (or [download the entire repo as a zip](https://github.com/sparkfun/OpenLCD/archive/master.zip)), to grab all of the examples. But if you prefer, you can always use the \"COPY CODE\" button on each of the examples below.

Note that these all have identical firmware and can accept the same commands. However, you must adjust your display characters and cursor position as necessary for each model. Also note, there is a jumper on the back of each screen, and this \"tells\" the firmware how to correctly set the lines and columns for each screen.

### Required Materials

If you are using Qwiic, then you will only need a [Redboard Qwiic](https://www.sparkfun.com/products/15123), a [Qwiic cable](https://www.sparkfun.com/products/14427), and a [Micro-B USB cable](https://www.sparkfun.com/products/15429) for programming.

For non-qwiic setups, you may need the following materials in this wishlist. Depending on what you have, you may not need everything on this list. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49), and screw driver depending on your setup.

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/ascii)

### ASCII 

A brief history of how ASCII came to be, how it\'s useful to computers, and some helpful tables to convert numbers to characters.

[] **Note:** Click on any of the images in this tutorial for a closer look!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft789&name=AVR-Based+Serial+Enabled+LCDs+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft789 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=AVR-Based+Serial+Enabled+LCDs+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft789&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft789&t=AVR-Based+Serial+Enabled+LCDs+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft789&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F7%2F8%2F9%2FTutorialThumbnail.jpg&description=AVR-Based+Serial+Enabled+LCDs+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/hardware-overview) [Hardware Hookup - Initial](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/hardware-hookup---initial) [SparkFun SerLCD Library](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/sparkfun-serlcd-library) [Firmware Overview](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/firmware-overview) [Serial UART: Hardware Hookup](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/serial-uart-hardware-hookup) [Serial UART: Example Code - Basic](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/serial-uart-example-code---basic) [Serial UART: Example Code - Contrast Control with a Trimpot](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/serial-uart-example-code---contrast-control-with-a-trimpot) [Serial UART: Example Code - Backlight Control](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/serial-uart-example-code---backlight-control) [I2C: Hardware Hookup & Example Code - Basic](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/i2c-hardware-hookup--example-code---basic) [SPI: Hardware Hookup & Example Code - Basic](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/spi-hardware-hookup--example-code---basic) [Troubleshooting](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/resources-and-going-further)

[Comments [20]](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Displays](https://learn.sparkfun.com/tutorials/tags/displays)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [LEDs](https://learn.sparkfun.com/tutorials/tags/leds)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]