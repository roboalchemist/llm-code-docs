# Source: https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- IoT RedBoard ESP32 Development Board Hookup Guide

# IoT RedBoard ESP32 Development Board Hookup Guide

[≡ Pages](#)

Contributors: [ Ell C], [![](https://cdn.sparkfun.com/avatar/935d3ed2b6c2516f85bce325946e6356?d=retro&s=20&r=pg) SparkFro]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2257&name=IoT+RedBoard+ESP32+Development+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2257 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=IoT+RedBoard+ESP32+Development+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2257&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2257&t=IoT+RedBoard+ESP32+Development+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2257&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F2%2F5%2F7%2F285808434_548438690244031_7008413248633042033_n.jpg&description=IoT+RedBoard+ESP32+Development+Board+Hookup+Guide "Pin It")

## Introduction

The [SparkFun IoT RedBoard](http://www.sparkfun.com/products/19177) is an ESP32 Development Board that includes everything but the kitchen sink! Espressif\'s ESP32 WROOM is a powerful WiFi and Bluetooth® MCU module that targets a wide variety of applications. At the core of this module is the ESP32-D0WDQ6 chip which is designed to be both scalable and adaptive. The IoT RedBoard can target a wide variety of applications, ranging from low-power sensor networks to the most demanding tasks, such as voice encoding, music streaming, and MP3 decoding. The IoT RedBoard also utilizes our handy Qwiic Connect System which means no soldering or shields are required to connect it to the rest of your system!

The USB-to-serial is achieved with a USB-C connector with through hole anchoring and the ubiquitous CH340G requiring fewer driver installs. We\'ve included 3.3V voltage translation and a [Qwiic connector](https://www.sparkfun.com/qwiic) to the edge of the board to allow for quick and seamless connection to our ever-growing line of I^2^C based [Qwiic products](https://www.sparkfun.com/qwiic#products). The board even includes a microSD socket if your application requires you to log and save data to a memory card. For remote power, we have included a 2-pin JST connector to attach a single cell, LiPo battery. There\'s also a built-in LiPo charge IC (MCP73831) and fuel gauge (MAX17048).

The operating system is freeRTOS with LwIP; TLS 1.2 with hardware acceleration is built in as well. Secure (encrypted) over the air (OTA) upgrade is also supported, so that users can upgrade their products even after their release, at minimum cost and effort.

Let\'s dive in and see what this baby can do!

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

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

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide)

### ESP32 Thing Plus Hookup Guide 

Hookup guide for the ESP32 Thing Plus (Micro-B) using the ESP32 WROOM\'s WiFi/Bluetooth system-on-chip in Arduino.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2257&name=IoT+RedBoard+ESP32+Development+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2257 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=IoT+RedBoard+ESP32+Development+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2257&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2257&t=IoT+RedBoard+ESP32+Development+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2257&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F2%2F5%2F7%2F285808434_548438690244031_7008413248633042033_n.jpg&description=IoT+RedBoard+ESP32+Development+Board+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/hardware-overview) [Hardware Hookup](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/hardware-hookup) [Software Setup and Programming](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/software-setup-and-programming) [Example 1: Blink](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/example-1-blink) [Example 2: WiFi](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/example-2-wifi) [Example 3: SD Card](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/example-3-sd-card) [Example 4: I2C](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/example-4-i2c) [Example 5: LiPo Fuel Gauge - MAX17048](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/example-5-lipo-fuel-gauge---max17048) [Troubleshooting](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/resources--going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [BLE](https://learn.sparkfun.com/tutorials/tags/ble)
  - [Bluetooth](https://learn.sparkfun.com/tutorials/tags/bluetooth)
  - [Bluetooth Low Energy](https://learn.sparkfun.com/tutorials/tags/bluetooth-low-energy)
  - [ESP32](https://learn.sparkfun.com/tutorials/tags/esp32)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Power](https://learn.sparkfun.com/tutorials/tags/power)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]