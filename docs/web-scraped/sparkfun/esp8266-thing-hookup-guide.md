# Source: https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- ESP8266 Thing Hookup Guide

# ESP8266 Thing Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft365&name=ESP8266+Thing+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft365 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=ESP8266+Thing+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft365&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft365&t=ESP8266+Thing+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft365&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F6%2F5%2Fproduct-angled.jpg&description=ESP8266+Thing+Hookup+Guide "Pin It")

## Introduction

Over the past year, the ESP8266 has been a growing star among IoT or WiFi-related projects. It\'s an extremely cost-effective WiFi module, that \-- with a little extra effort \-- can be programmed just like any microcontroller. Unfortunately, the ESP8266 has mostly only been available in a [tiny, modular form](https://www.sparkfun.com/products/17146), which, with limited I/O and a funky pin-out, can be difficult to build a project around.

[![WiFi Module - ESP8266 (4MB Flash)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/1/2/7/17146-WiFi_Module_-_ESP8266__4MB_-01.jpg)](https://www.sparkfun.com/wifi-module-esp8266-4mb-flash.html)

### [WiFi Module - ESP8266 (4MB Flash)](https://www.sparkfun.com/wifi-module-esp8266-4mb-flash.html) 

[ WRL-17146 ]

The ESP8266 WiFi Module is a self contained SOC with integrated TCP/IP protocol stack that can give any microcontroller acces...

[ [\$7.50] ]

*The ESP8266 WiFi module. Great for piggybacking onto an Arduino, hard to build a project around.*

SparkFun\'s new development board for the ESP8266 breaks out all of the module\'s pins, and comes equipped with a LiPo charger, power supply, and all of the other supporting circuitry it requires. We lovingly call it [the Thing](https://www.sparkfun.com/products/13231) \-- it\'s the perfect foundation for your Internet of Things.

[![SparkFun ESP8266 Thing](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/4/0/0/13231-01.jpg)](https://www.sparkfun.com/sparkfun-esp8266-thing.html)

### [SparkFun ESP8266 Thing](https://www.sparkfun.com/sparkfun-esp8266-thing.html) 

[ WRL-13231 ]

The SparkFun ESP8266 Thing is a breakout and development board for the ESP8266 WiFi SoC -- a leading platform for IoT or WiF...

[ [\$19.95] ]

[![SparkFun ESP8266 Thing Starter Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/2/5/15258-ESP8266_Thing_Starter_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-esp8266-thing-starter-kit.html)

### [SparkFun ESP8266 Thing Starter Kit](https://www.sparkfun.com/sparkfun-esp8266-thing-starter-kit.html) 

[ KIT-15258 ]

This starter kit has everything you need to get started with the ESP8266 Thing board. Solder on some headers (iron not inclu...

[\$30.95] [ [\$14.25] ]

*Having trouble viewing the videos? Try resizing the video by clicking on the shortcut to view the product showcase in full screen.*

### Covered in this Tutorial

This tutorial will familiarize you with all things SparkFun Thing. It\'s split into sections, which cover:

- [Hardware Overview](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/hardware-overview) \-- A quick rundown of the Thing\'s **components and pinout**.
- [Powering the Thing](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/powering-the-thing) \-- The Thing can be powered through either USB or a LiPo battery.
- [Programming the Thing](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/programming-the-thing) \-- Interface a 3.3V FTDI Basic with the Thing to program it.
- [Hardware Assembly](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/hardware-assembly) \-- Tips and recommendations on what to solder to the Thing\'s I/O pins.
- [Installing the ESP8266 Arduino Addon](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/installing-the-esp8266-arduino-addon) \-- The Thing can be programmed using Arduino! Just follow the instructions here to install the board definitions.
- [Example Sketch: AP Web Server](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/example-sketch-ap-web-server) \-- Set the Thing up as an access point and use it to serve web pages.
- [Using the Arduino Addon](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/using-the-arduino-addon) \-- There are a few key differences between programming the Thing and any other Arduino board.

### Required Materials

To follow along with this tutorial, and get up-and-running with the Thing, you may need a few extra tools and materials. This wishlist includes everything we use in this tutorial to program and use the Thing if you are ordering the board individually:

### Suggested Reading

Before continuing on with this tutorial, you may want to familiarize yourself with some of these topics if they\'re unfamiliar to you:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft365&name=ESP8266+Thing+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft365 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=ESP8266+Thing+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft365&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft365&t=ESP8266+Thing+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft365&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F6%2F5%2Fproduct-angled.jpg&description=ESP8266+Thing+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/hardware-overview) [Powering the Thing](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/powering-the-thing) [Programming the Thing](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/programming-the-thing) [Hardware Assembly](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/hardware-assembly) [Installing the ESP8266 Arduino Addon](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/installing-the-esp8266-arduino-addon) [Example Sketch: Blink](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/example-sketch-blink) [Example Sketch: AP Web Server](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/example-sketch-ap-web-server) [Using the Arduino Addon](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/using-the-arduino-addon) [More ESP8266 Thing Examples](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/more-esp8266-thing-examples) [Resources and Going Further](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/resources--going-further)

[Comments [62]](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [ESP8266](https://learn.sparkfun.com/tutorials/tags/esp8266)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]