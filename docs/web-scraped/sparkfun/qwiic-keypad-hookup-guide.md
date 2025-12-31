# Source: https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Qwiic Keypad Hookup Guide

# Qwiic Keypad Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete], [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft271&name=Qwiic+Keypad+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft271 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Qwiic+Keypad+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft271&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft271&t=Qwiic+Keypad+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft271&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F7%2F1%2FRedBoard.jpg&description=Qwiic+Keypad+Hookup+Guide "Pin It")

## Introduction

Keypads are very handy input devices, but who wants to tie up 7 GPIO pins, wire up a handful of pull-up resistors, and write firmware that wastes valuable processing time scanning the keys for inputs? Let's make the development process easier! The [SparkFun Qwiic Keypad](https://www.sparkfun.com/products/15290) comes fully assembled and uses the simple [Qwiic interface](https://www.sparkfun.com/qwiic). No soldering, no voltage translation, no figuring out which I^2^C pin is SDA or SCL, just plug and go!

[![SparkFun Qwiic Keypad - 12 Button](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/7/7/15290-SparkFun_Qwiic_Keypad_-_12_Button-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-keypad-12-button.html)

### [SparkFun Qwiic Keypad - 12 Button](https://www.sparkfun.com/sparkfun-qwiic-keypad-12-button.html) 

[ COM-15290 ]

The SparkFun Qwiic Keypad comes fully assembled and makes the development process for adding a 12 button keypad easy.

[ [\$13.50] ]

The Qwiic Keypad reads and stores the last 15 button presses in a First-In, First-Out (FIFO) stack, so you don't need to constantly poll the keypad from your microcontroller. This information, then, is accessible through the Qwiic interface. Qwiic Keypad even has a software configurable I^2^C address so you can have multiple I^2^C devices on the same bus.

### Required Materials

The [SparkFun Qwiic Keypad](https://www.sparkfun.com/products/15290) does need a few additional items for you to get started; a Qwiic enabled microcontroller and a Qwiic cable. You may already have a few of these items, so feel free to modify your cart based on your needs.

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

[![SparkFun Thing Plus - ESP32 WROOM](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/9/4/14689-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/products/14689)

### [SparkFun Thing Plus - ESP32 WROOM](https://www.sparkfun.com/products/14689) 

[ WRL-14689 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

**Retired**

Additional Hardware for Example 5

**Note:** If you want to do the Example 5, then you will need to solder and connect a wire to the INT and Pin 2 on the RedBoard Qwiic. You may already have a few of these items, so feel free to modify your cart based on your needs.

[![Hook-up Wire - White (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/6/08026-01.jpg)](https://www.sparkfun.com/hook-up-wire-white-22-awg.html)

### [Hook-up Wire - White (22 AWG)](https://www.sparkfun.com/hook-up-wire-white-22-awg.html) 

[ PRT-08026 ]

Standard 22 AWG solid White hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes ...

[ [\$2.95] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

### Suggested Reading

If you\'re unfamiliar with jumper pads or I^2^C be sure to checkout some of these foundational tutorials.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

**Note:** For a greater understanding of how the firmware works to multiplex the keys, check out these tutorials.

+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+-----------------+
| ::::::: tile-wrap                                                                                                                                 | ::::::: tile-wrap                                                                                                              | [Arduino Kepad Tutorials]\                                       |                 |
| ::::::                                                                                         | ::::::                                                                      | [Arduino Keypad Library](https://playground.arduino.cc/code/keypad)\         |                 |
| [](https://learn.sparkfun.com/tutorials/button-pad-hookup-guide)                                                                                  | [](https://learn.sparkfun.com/tutorials/multiplexer-breakout-hookup-guide)                                                     | [Arduino Keypad Tutorial](https://playground.arduino.cc/Main/KeypadTutorial) |                 |
|                                                                                                                                                   |                                                                                                                                |                                                                              |                 |
| :::: thumb-wrap                                                                                                                                   | :::: thumb-wrap                                                                                                                |                                                                              |                 |
| :::  | :::  |                                                                              |                 |
| :::                                                                                                                                               | :::                                                                                                                            |                                                                              |                 |
| ::::                                                                                                                                              | ::::                                                                                                                           |                                                                              |                 |
|                                                                                                                                                   |                                                                                                                                |                                                                              |                 |
| ### Button Pad Hookup Guide                                                                                      | ### Multiplexer Breakout Hookup Guide                                               |                                                                              |                 |
|                                                                                                                                                   |                                                                                                                                |                                                                              |                 |
| ::: description                                                                                                                                   | ::: description                                                                                                                |                                                                              |                 |
| An introduction to matrix scanning, using the SparkFun 4x4 Button Pad.                                                                            | How to use the 74HC4051 multiplexer breakout to drive eight LEDs, read eight button inputs, or monitor eight potentiometers.   |                                                                              |                 |
| :::                                                                                                                                               | :::                                                                                                                            |                                                                              |                 |
| ::::::                                                                                                                                            | ::::::                                                                                                                         |                                                                              |                 |
| :::::::                                                                                                                                           | :::::::                                                                                                                        |                                                                              |                 |
|                                                                                                                                                   |                                                                                                                                |                                                                              |                 |
| ::: clearfix                                                                                                                                      | ::: clearfix                                                                                                                   |                                                                              |                 |
| :::                                                                                                                                               | :::                                                                                                                            |                                                                              |                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+-----------------+

Additional Reading for Example 5

**Note:** If you want to do the Example 5, then you will need to solder and connect a wire to the INT and Pin 2 on the RedBoard Qwiic. If you are unfamiliar with through hole soldering or using interrupts, please check out these additional reading suggestions.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino)

### Processor Interrupts with Arduino 

What is an interrupt? In a nutshell, there is a method by which a processor can execute its normal program while continuously monitoring for some kind of event, or interrupt. There are two types of interrupts: hardware and software interrupts. For the purposes of this tutorial, we will focus on hardware interrupts.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Qwiic Keypad utilizes the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials (above) before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft271&name=Qwiic+Keypad+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft271 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Qwiic+Keypad+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft271&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft271&t=Qwiic+Keypad+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft271&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F7%2F1%2FRedBoard.jpg&description=Qwiic+Keypad+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/h) [Arduino Library](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/arduino-library) [Arduino Examples](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/arduino-examples) [Resources and Going Further](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/resources-and-going-further)

[Comments [6]](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [ATtiny](https://learn.sparkfun.com/tutorials/tags/attiny)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Input Devices](https://learn.sparkfun.com/tutorials/tags/input-devices)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Security](https://learn.sparkfun.com/tutorials/tags/security)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]