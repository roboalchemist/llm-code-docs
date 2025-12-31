# Source: https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- ESP8266 Thing Development Board Hookup Guide

# ESP8266 Thing Development Board Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft445&name=ESP8266+Thing+Development+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft445 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=ESP8266+Thing+Development+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft445&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft445&t=ESP8266+Thing+Development+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft445&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F4%2F5%2Fesp8266-angle-crop.jpg&description=ESP8266+Thing+Development+Board+Hookup+Guide "Pin It")

## Introduction

The ESP8266 is a cost-effective, and very capable WiFi-enabled microcontroller. Like any microcontroller, it can be programmed to blink LEDs, trigger relays, monitor sensors, or automate coffee makers, and with an integrated WiFi controller, the ESP8266 is a one-stop shop for almost any Internet-connected project. To top it all off, the ESP8266 is incredibly easy-to-use: firmware can be developed in Arduino and uploaded over a simple, serial interface.

To take advantage of all of those benefits, we\'ve created the [ESP8266 Thing Development Board](https://www.sparkfun.com/products/13711) \-- an ESP8266 development board, with an integrated FTDI USB-to-Serial chip.

[![SparkFun ESP8266 Thing - Dev Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/1/9/7/13711-01.jpg)](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board.html)

### [SparkFun ESP8266 Thing - Dev Board](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board.html) 

[ WRL-13711 ]

The SparkFun ESP8266 Thing Dev Board is a development board that has been solely designed around the ESP8266, with an integra...

[ [\$19.95] ]

[![SparkFun ESP8266 Thing Dev Starter Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/2/6/15259-ESP8266_Thing_Dev_Starter_Kit-01.jpg)](https://www.sparkfun.com/products/15259)

### [SparkFun ESP8266 Thing Dev Starter Kit](https://www.sparkfun.com/products/15259) 

[ KIT-15259 ]

This starter kit has everything you need to get started with the ESP8266 Thing Dev board. Solder on some headers (iron not i...

**Retired**

*Having trouble viewing the videos? Try resizing the video by clicking on the shortcut to view the product showcase in full screen.*

The ESP8266 Thing Development Board breaks out all of the module\'s pins, and the USB-to-serial converter means you don\'t need any peripheral components to program the chip. Just plug in a USB cable, download the Arduino board definitions, and start IoT-ing.

### Covered in this Tutorial

This tutorial will help you get your ESP8266 Thing Development Board from zero to Internet-controlled blinking. It\'s split into the following sections:

- [Hardware Overview](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/hardware-overview) \-- A quick rundown of the Thing Development Board\'s components and pinout.
- [Hardware Setup](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/hardware-setup) \-- Tips and recommendations on what to solder to the Thing Development Board\'s I/O pins.
- [Setting Up Arduino](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/setting-up-arduino) \-- What truly makes the ESP8266 so powerful is its potential for Arduino-compatibility.
- [Example Sketch: Web Server](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/example-sketch-web-server) \-- Run an HTTP server on the Thing. Use it to serve web pages, print status messages, and control LEDs!
- [Example Sketch: Blink with Blynk](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/example-sketch-blink-with-blynk) \-- One of our favorite new toys is the Blynk phone app, which allows you to toggle LEDs and monitor inputs with a simple multi-platform phone app.
- [Using the ESP8266 in Arduino](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/using-the-esp8266-in-arduino) \-- A few gotchya\'s to look out for when programming the ESP8266 in Arduino.

### Required Materials

If you are ordering the ESP8266 Thing Development individually, you will need a few components to get started. Beyond the ESP8266 Thing Development Board itself, all you should need to get started is a [micro-B USB Cable](https://www.sparkfun.com/products/10215), which will deliver power the board and set up our USB programming interface.

Depending on how you want to use the board, you may also want to add [male headers](https://www.sparkfun.com/products/116), [female headers](https://www.sparkfun.com/products/115), or hedge your bets with [10-pin stackable headers](https://www.sparkfun.com/products/11376).

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

[![Stackable Header - Female (PTH, 0.1in., 10-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/2/11376-01a.jpg)](https://www.sparkfun.com/arduino-stackable-header-10-pin.html)

### [Stackable Header - Female (PTH, 0.1in., 10-Pin)](https://www.sparkfun.com/arduino-stackable-header-10-pin.html) 

[ PRT-11376 ]

This is a 10-pin female header, with extra long legs \-- great for stacking R3-compatible Arduino shields! Pins are spaced...

[ [\$0.95] ]

**Heads up!** If you are looking for the development board with headers soldered, check out [WRL-13804](https://www.sparkfun.com/products/13804) with male headers soldered to the board as another option.\
\

[![SparkFun ESP8266 Thing - Dev Board (with Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/8/6/13804-01.jpg)](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board-with-headers.html)

### [SparkFun ESP8266 Thing - Dev Board (with Headers)](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board-with-headers.html) 

[ WRL-13804 ]

The SparkFun ESP8266 Thing Dev Board with Headers is a dev board that has been designed around the ESP8266, with an integrate...

[ [\$20.25] ]

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

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft445&name=ESP8266+Thing+Development+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft445 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=ESP8266+Thing+Development+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft445&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft445&t=ESP8266+Thing+Development+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft445&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F4%2F5%2Fesp8266-angle-crop.jpg&description=ESP8266+Thing+Development+Board+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/hardware-overview) [Hardware Setup](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/hardware-setup) [Setting Up Arduino](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/setting-up-arduino) [Example Sketch: Blink](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/example-sketch-blink) [Example Sketch: Web Server](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/example-sketch-web-server) [Example Sketch: Blink with Blynk](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/example-sketch-blink-with-blynk) [Using the ESP8266 in Arduino](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/using-the-esp8266-in-arduino) [Resources and Going Further](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/resources--going-further)

[Comments [26]](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Blynk](https://learn.sparkfun.com/tutorials/tags/blynk)
  - [ESP8266](https://learn.sparkfun.com/tutorials/tags/esp8266)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]