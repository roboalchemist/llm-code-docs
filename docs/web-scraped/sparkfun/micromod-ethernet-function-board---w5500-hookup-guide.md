# Source: https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroMod Ethernet Function Board - W5500 Hookup Guide

# MicroMod Ethernet Function Board - W5500 Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2062&name=MicroMod+Ethernet+Function+Board+-+W5500++Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2062 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+Ethernet+Function+Board+-+W5500++Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2062&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2062&t=MicroMod+Ethernet+Function+Board+-+W5500++Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2062&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F0%2F6%2F2%2FMicroMod_W5500_Ethernet_Function-Thumbnail.jpg&description=MicroMod+Ethernet+Function+Board+-+W5500++Hookup+Guide "Pin It")

## Introduction

Integrate your MicroMod project into an Ethernet network including Power-over-Ethernet with the [SparkFun MicroMod Ethernet Function Board - W5500](https://www.sparkfun.com/products/18708). This Function Board uses the W5500 Ethernet control module from WIZnet and a DC/DC converter to configure a MicroMod assembly as a connected and powered device into an Ethernet network with Power-over-Ethernet (PoE) capabilities.

[![SparkFun MicroMod Ethernet Function Board - W5500](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/2/4/3/18708-SparkFun_MicroMod_Ethernet_Function_Board_-_W5500-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-ethernet-function-board-w5500.html)

### [SparkFun MicroMod Ethernet Function Board - W5500](https://www.sparkfun.com/sparkfun-micromod-ethernet-function-board-w5500.html) 

[ COM-18708 ]

Integrate your MicroMod project into an Ethernet network including Power-over-Ethernet with the SparkFun MicroMod Ethernet Fu...

**Retired**

The W5500 is a TCI/IP embedded Ethernet controller from WIZnet that uses SPI and supports up to 80 MHz speeds. We designed this Function Board to use the IEEE802.3af Alternative B power scheme which uses the spare pairs for power delivery, isolated from the data pairs. In this guide we\'ll highlight the capabilities of the W5500 and demonstrate how to use the MicroMod Ethernet Function Board to create an Ethernet network that can also be used for PoE.

### Required Materials

Following along with this tutorial requires a few items along with the MicroMod Ethernet Function Board. Depending on what you already have, you may not need all of the items listed below.

#### MicroMod Processor

All MicroMod systems require a Processor board to operate. SparkFun carries a variety of Processor boards suited for different applications. Select the Processor board that best suits your Ethernet projects\' needs:

[![SparkFun MicroMod Teensy Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/2/16402-SparkFun_MicroMod_Teensy_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html)

### [SparkFun MicroMod Teensy Processor](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html) 

[ DEV-16402 ]

This board leverages the awesome computing power of the NXP iMXRT1062 chip (ARM Cortex-M7) and pairs it with the M.2 MicroMod...

[ [\$24.95] ]

[![SparkFun MicroMod ESP32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/8/0/16781-SparkFun_MicroMod_ESP32_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html)

### [SparkFun MicroMod ESP32 Processor](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html) 

[ WRL-16781 ]

This board combines Espressif\'s ESP32 with our M.2 connector interface to bring a power-packed processor board into our Micro...

[ [\$19.95] ]

[![SparkFun MicroMod SAMD51 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/8/16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html)

### [SparkFun MicroMod SAMD51 Processor](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html) 

[ DEV-16791 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun MicroMod SAMD51 Processor Board is one powerful microcontroller packaged on a ...

[ [\$18.95] ]

[![SparkFun MicroMod STM32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/1/7/17713-SparkFun_MicroMod_STM32_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-stm32-processor-dev-17713.html)

### [SparkFun MicroMod STM32 Processor](https://www.sparkfun.com/sparkfun-micromod-stm32-processor-dev-17713.html) 

[ DEV-17713 ]

The SparkFun MicroMod STM32 Processor Board is ready to rock your MicroMod world with its ARM® Cortex®-M4 32-bit RISC core!

**Retired**

Note: Currently the Artemis and nRF52840 do not have built in Ethernet libraries in their Arduino cores. An external Arduino Ethernet library may work but at this time Ethernet is not supported on those Processors.

#### MicroMod Main Board

MicroMod Function Boards require at least one Main Board to work.

[![SparkFun MicroMod Main Board - Single](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/0/4/2/18575-SparkFun_MicroMod_Main_Board_-_Single-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-single-dev-18575.html)

### [SparkFun MicroMod Main Board - Single](https://www.sparkfun.com/sparkfun-micromod-main-board-single-dev-18575.html) 

[ DEV-18575 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with a single ...

**Retired**

[![SparkFun MicroMod Main Board - Double](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/0/4/3/18576-SparkFun_MicroMod_Main_Board_-_Double-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-double-dev-18576.html)

### [SparkFun MicroMod Main Board - Double](https://www.sparkfun.com/sparkfun-micromod-main-board-double-dev-18576.html) 

[ DEV-18576 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with up to two...

**Retired**

#### Peripheral Items

You\'ll also need a PoE power supply like a network hub or router, Ethernet cable, network hub/router or endpoint as well as a few other peripheral items to get your MicroMod Ethernet system up and running. If needed, add these items to your cart:

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

[![CAT 6 Cable - 3ft](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/9/2/08915-03.jpg)](https://www.sparkfun.com/cat-6-cable-3ft.html)

### [CAT 6 Cable - 3ft](https://www.sparkfun.com/cat-6-cable-3ft.html) 

[ CAB-08915 ]

This 3ft Category 6 (CAT 6) Ethernet cable is the solution to your internet working needs. With a speed of up to 500MHz you c...

[ [\$2.25] ]

### Tools

Assembling MicroMod systems requires a Phillips head screwdriver.

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

### Recommended Reading

The [MicroMod ecosystem](https://www.sparkfun.com/micromod) is a unique way to allow users to customize their project to their needs. If you aren\'t familiar with the MicroMod system, click on the banner below for more information.

[![MicroMod Logo](https://cdn.sparkfun.com/r/500-70/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)

\

You may also want to read the tutorials below if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2062&name=MicroMod+Ethernet+Function+Board+-+W5500++Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2062 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+Ethernet+Function+Board+-+W5500++Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2062&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2062&t=MicroMod+Ethernet+Function+Board+-+W5500++Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2062&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F0%2F6%2F2%2FMicroMod_W5500_Ethernet_Function-Thumbnail.jpg&description=MicroMod+Ethernet+Function+Board+-+W5500++Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/hardware-assembly) [Software Installation](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/software-installation) [Arduino Example](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/arduino-example) [Troubleshooting](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/micromod-ethernet-function-board---w5500-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [MicroMod](https://learn.sparkfun.com/tutorials/tags/micromod)
  - [Power](https://learn.sparkfun.com/tutorials/tags/power)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]