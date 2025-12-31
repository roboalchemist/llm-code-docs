# Source: https://learn.sparkfun.com/tutorials/qwiic-mux-hookup-guide

## Introduction

**PCA9548A and TCA9548A?** The SparkX version of the Qwiic Mux breakout used the PCA9548A. The SparkFun red version uses the TCA9548A. Overall, both should be functionally the same with a [few minor differences](https://learn.sparkfun.com/tutorials/qwiic-mux-hookup-guide#hardware-overview).

The Qwiic Mux - TCA9548A [(v1)](https://www.sparkfun.com/products/14685) and [(v1.1)](https://www.sparkfun.com/products/16784) enable communication with multiple I^2^C devices that have the same address. The IC is simple to interface with and also has 8 configurable addresses of its own, this allows you to put 64 I^2^C buses on a single bus!

[![SparkFun Qwiic Mux Breakout - 8 Channel (TCA9548A)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/9/0/14685-SparkFun_Qwiic_Mux_Breakout_-_8_Channel__TCA9548A_-01.jpg)](https://www.sparkfun.com/products/14685)

### [SparkFun Qwiic Mux Breakout - 8 Channel (TCA9548A)](https://www.sparkfun.com/products/14685) 

[ BOB-14685 ]

The SparkFun Qwiic Mux Breakout enables communication with multiple I2C devices that have the same address that makes it simp...

**Retired**

[![SparkFun Qwiic Mux Breakout - 8 Channel (TCA9548A)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/6/8/9/16784-SparkFun_Qwiic_Mux_Breakout_V2_-_8_Channel__TCA9548A_-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-mux-breakout-8-channel-tca9548a.html)

### [SparkFun Qwiic Mux Breakout - 8 Channel (TCA9548A)](https://www.sparkfun.com/sparkfun-qwiic-mux-breakout-8-channel-tca9548a.html) 

[ BOB-16784 ]

The SparkFun Qwiic Mux Breakout enables communication with multiple I2C devices that have the same address that makes it simp...

[ [\$6.95] ]

**Revision Update:** In the latest revision of the Qwiic MUX, we have made a few changes to improve the board, listed below. If users are unsure about which version they purchased, please refer to the pictures of the most prominent changes, shown below.

- We have added a pass-through Qwiic connector.
  - The power LED was moved to accommodate the additional Qwiic connector.
- We have updated the I^2^C pull-up resistor jumper to a cuttable trace.
- We have widened the trace for the 3.3V power.
- There is a ***v11*** label on the back of the board.
- The silk screen labels have been updated.

[![added connector](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Qwiic_Mux_pass-through_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Qwiic_Mux_pass-through_2.jpg)\
*Added Qwiic connector to make board daisy-chainable.*

[![v11 marking](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Qwiic_Mux_v11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Qwiic_Mux_v11.jpg)\
*The **v11** label on the back.*

In this tutorial we\'ll go over how to talk to sensors on different channels of your MUX breakout board. The application of this is pretty straightforward so things won\'t get too fancy.

### Required Materials

You\'ll need a few additional items to get started with the Qwiic Mux. The [RedBoard Qwiic](https://www.sparkfun.com/products/15123) is for the Arduino examples and the [Qwiic pHAT](https://www.sparkfun.com/products/15351) is for the Raspberry Pi example (see note below). You may already have a few of these items, so feel free to modify your cart based on your needs. Additionally, there are also [alternative parts] options that are available as well (*click button below to toggle options*).

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

[![SparkFun Qwiic pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/9/15351-SparkFun_Qwiic_pHAT_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/products/15351)

### [SparkFun Qwiic pHAT for Raspberry Pi](https://www.sparkfun.com/products/15351) 

[ DEV-15351 ]

The SparkFun Qwiic pHAT for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and still ...

**Retired**

Qwiic compatible microcontrollers:

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun Thing Plus - SAMD51](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/2/7/14713-SparkFun_Thing_Plus_-_SAMD51-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html)

### [SparkFun Thing Plus - SAMD51](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html) 

[ DEV-14713 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun SAMD51 Thing Plus is one of our most powerful microcontroller boards yet!

[ [\$25.50] ]

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

In addition we also offer, Qwiic compatible stackable shields for microcontrollers and pHATs for single board computers (like the [Raspberry Pi boards](https://www.sparkfun.com/categories/395)) that don\'t include a Qwiic connector.

[![SparkFun Qwiic Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/5/1/14495-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-adapter.html)

### [SparkFun Qwiic Adapter](https://www.sparkfun.com/sparkfun-qwiic-adapter.html) 

[ DEV-14495 ]

The SparkFun Qwiic Adapter provides the perfect means to make any old I^2^C board into a Qwiic enabled board.

[ [\$1.60] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

[![SparkFun Qwiic Shield for Photon](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/2/6/14477-01.jpg)](https://www.sparkfun.com/products/14477)

### [SparkFun Qwiic Shield for Photon](https://www.sparkfun.com/products/14477) 

[ DEV-14477 ]

The SparkFun Qwiic Shield for Photon is an easy-to-assemble board that provides a simple way to incorporate the Qwiic System ...

**Retired**

[![SparkFun Qwiic HAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/5/14459-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-hat-for-raspberry-pi.html)

### [SparkFun Qwiic HAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-hat-for-raspberry-pi.html) 

[ DEV-14459 ]

The SparkFun Qwiic HAT for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and still u...

[ [\$6.95] ]

[![SparkFun Qwiic SHIM for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/3/9/9/16385-15794-SparkFun_Qwiic_SHIM_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html)

### [SparkFun Qwiic SHIM for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html) 

[ DEV-15794 ]

The SparkFun Qwiic SHIM for Raspberry Pi is a small, easily removable breakout that easily adds a Qwiic connector to your Ras...

[ [\$1.95] ]

[![SparkFun Servo pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/2/7/15316-SparkFun_Servo_pHAT_for_Raspberry_Pi-01b.jpg)](https://www.sparkfun.com/sparkfun-servo-phat-for-raspberry-pi.html)

### [SparkFun Servo pHAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-servo-phat-for-raspberry-pi.html) 

[ DEV-15316 ]

The SparkFun Servo pHAT for Raspberry Pi allows your Raspberry Pi to control up to 16 servo motors in a straightforward manne...

[ [\$13.95] ]

[![SparkFun Qwiic pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/9/15351-SparkFun_Qwiic_pHAT_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/products/15351)

### [SparkFun Qwiic pHAT for Raspberry Pi](https://www.sparkfun.com/products/15351) 

[ DEV-15351 ]

The SparkFun Qwiic pHAT for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and still ...

**Retired**

You will also need a Qwiic cable to connect to your Qwiic Mux, choose a length that suits your needs.

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[**Alternative Parts (Toggle)**]

**Raspberry Pi Example:** If you don\'t already have them, you will need a [Raspberry Pi](https://www.sparkfun.com/products/14644) and [standard peripherals](https://www.sparkfun.com/categories/398). An example setup is listed below. ~~(*The Qwiic Mux and Python library have not been tested on the newly released Raspberry Pi 4 because we don\'t carry it in out catalog yet.*)~~

**Update:** This board and the Python package have been verified to work with the Raspberry Pi 4.

### Tools

Depending on your setup, you may need a hobby knife, soldering iron, solder, and/or [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

[![Slice Craft Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/7/1/14508-03.jpg)](https://www.sparkfun.com/products/14508)

### [Slice Craft Knife](https://www.sparkfun.com/products/14508) 

[ TOL-14508 ]

The Slice Craft Knife is a high end hobby knife perfect for precision cutting, scraping, and handling.

**Retired**

### Suggested Reading

If you\'re unfamiliar with jumper pads, I^2^C, Qwiic, or Python be sure to checkout some of these foundational tutorials.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

### Raspberry Pi SPI and I2C Tutorial 

Learn how to use serial I2C and SPI buses on your Raspberry Pi using the wiringPi I/O library for C/C++ and spidev/smbus for Python.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[](https://learn.sparkfun.com/tutorials/qwiic-phat-for-raspberry-pi-hookup-guide)

### Qwiic pHAT for Raspberry Pi Hookup Guide 

Get started interfacing your Qwiic enabled boards with your Raspberry Pi. The Qwiic pHAT connects the I2C bus (GND, 3.3V, SDA, and SCL) on your Raspberry Pi to an array of Qwiic connectors.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Qwiic Mux is intended for the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the [**Logic Levels**](https://learn.sparkfun.com/tutorials/logic-levels) and [**I^2^C**](https://learn.sparkfun.com/tutorials/i2c) tutorials before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

## Hardware Overview

**What is the difference between the PCA9548A and TCA9548A?** Very little. PCA is made by NXP, TCA is made by TI. PCA can operate from 2.3 to 5.5V, TCA can operate from 1.65 to 5.5V. Everything else is identical.

Let\'s look over a few characteristics of the TCA9548A so we know a bit more about how it behaves.

  **Characteristic**      **Range**
  ----------------------- -------------------------------------------------
  Operating Voltage       **1.65V - 5.5V**
  Operating Temperature   -40 - 85° C
  I^2^C Address           **0x70 (default)** up to 0x77 (see below table)

**Original Release:**The Qwiic input for the Mux is located at the top-center of the board, labeled `Main`, highlighted in the image below. The outputs are then located on the left and right sides of the board and are numbered accordingly.

[![Main Qwiic Port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/MAIN.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/MAIN.png)

**Revision Update:** There are two `Main` connectors on the revision to provide a pass through for the I^2^C bus connection. This allow the board to be daisy chained in between other Qwiic boards.

[![Updated passthrough connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/Qwiic_Mux_pass-through_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Qwiic_Mux_pass-through_2.jpg)

The onboard reset pin, highlighted below, is an active low input. Pulling reset low for at least 6 ns will restart the multiplexer.

[![Reset Pin](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/RST.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/RST.png)

The Qwiic Mux also allows you to change the last 3 bits of the address byte, allowing for 8 jumper selectable addresses if you happen to need to put more than one Mux on the same I^2^C port. The address can be changed by [adding solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) to any of the three **ADR** jumpers, shown in the image below.

[![Address Jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/ADR.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/ADR.png)

The below table shows which jumpers must be soldered together to change to the corresponding address.

  **I^2^C Address**   **ADR2**   **ADR1**   **ADR0**
  ------------------- ---------- ---------- ----------
  **0x70**            Open       Open       Open
  **0x71**            Open       Open       Closed
  **0x72**            Open       Closed     Open
  **0x73**            Open       Closed     Closed
  **0x74**            Closed     Open       Open
  **0x75**            Closed     Open       Closed
  **0x76**            Closed     Closed     Open
  **0x77**            Closed     Closed     Closed

**Original Release:**If you want to remove the pullup resistors from the I^2^C bus, simply remove the solder from the jumper highlighted in the below image.

[![Pullup Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/PU.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/PU.png)

**Revision Update:** If you want to remove the pullup resistors from the I^2^C bus, simply cut the jumper pad with a hobby knife. Be careful of the **3.3V** trace above the jumper pad. Cutting the trace probably won\'t destroy the board, as the trace also circles around through the Qwiic connector on the bottom. However, it will leave the trace exposed at the cut.

[![Pullup jumpter pad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/Qwiic_Mux_jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Qwiic_Mux_jumper.jpg)

## Hardware Assembly

**Support Tip:** Make sure that you are connecting the **Main** Qwiic connector to the Arduino board/shield or Raspberry HAT.

### Arduino Example

Just plug one end of the Qwiic cable into the **Main** connector on the Qwiic multiplexer breakout and the other end into Qwiic connector on your Qwiic enabled microcontroller. If it seems like it\'s too easy to use, but that\'s why we made it that way! Otherwise, if you chose to use a Qwiic shield/adapter, now would be the time to head on over to that tutorial to assemble the shield.

[Qwiic Shield for Arduino Photon Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

With the shield assembled, SparkFun\'s new Qwiic environment means that connecting the mux could not be easier. Just plug one end of the Qwiic cable into the Qwiic multiplexer breakout (***Main** connector*) and the other into the Qwiic Shield; then, you\'ll be ready to upload a sketch and figure out just how all those address sharing sensors are behaving.

[![Mux Connected to Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/SparkFun_Qwiic_Mux_Breakout_-_8_Channel__TCA9548A__Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/SparkFun_Qwiic_Mux_Breakout_-_8_Channel__TCA9548A__Hookup_Guide-03.jpg)

SparkFun RedBoard with the Qwiic shield connected the Qwiic Mux with a Qwiic cable.

Additionally, a few peripheral Qwiic Boards are attached to verify Qwiic Mux functionality.

**Revision Update:** Users can now daisy chain the Qwiic Mux in between other Qwiic boards.

[![Dasiy chain Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/assembly_arduino_updated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/assembly_arduino_updated.jpg)

### Raspberry Pi Examples

~~**Note:** This board and the Python package have not been tested on the newly released Raspberry Pi 4 because we don\'t carry it in out catalog yet.~~

**Update:** This board and the Python package have been verified to work with the Raspberry Pi 4.

With the Qwiic connector system, assembling the hardware is simple. In addition to the [Qwiic Mux](https://www.sparkfun.com/products/14685), you will need: a [Qwiic cables](https://www.sparkfun.com/products/15081), a [SparkFun Qwiic pHAT for Raspberry Pi](https://www.sparkfun.com/products/15351), and a [Raspberry Pi](https://www.sparkfun.com/products/14643) setup with the [Raspbian OS](https://www.sparkfun.com/products/13945), monitor, and [standard peripherals](https://www.sparkfun.com/categories/398). (\**If you are unfamiliar with the Qwiic pHAT, you can find the [Hookup Guide here](https://learn.sparkfun.com/tutorials/qwiic-phat-for-raspberry-pi-hookup-guide)*.)

**Note:** The peripheral Qwiic boards attached to the Qwiic Mux are not necessary for this hookup guide, but they are useful for customers looking to verify the functionality of the Qwiic Mux. Use channels 0, 4, and 7 for the examples below.

[![Hardware assembly with Raspberry Pi 3B with Qwiic pHAT](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/Assembly_Pi_Qwiic_pHat.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Assembly_Pi_Qwiic_pHat.jpg)

*Raspberry Pi 3B connected the Qwiic Mux with a Qwiic pHAT and Qwiic cable (and a few peripheral Qwiic Boards).*

**Revision Update:** Users can now daisy chain the Qwiic Mux in between other Qwiic boards.

[![Dasiy chain Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/assembly_pi_updated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/assembly_pi_updated.jpg)

Alternatively, you can also use another Qwiic adapter like the [Pi Servo pHat](https://www.sparkfun.com/products/15316) instead.

[![Hardware assembly with Raspberry Pi 3B with Pi Servo pHat](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/7/Assembly_Pi_Servo_pHat.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Assembly_Pi_Servo_pHat.jpg)

*Raspberry Pi 3 connected the Qwiic Mux with the Pi Servo pHat and Qwiic cable (and a few peripheral Qwiic Boards).*

**Note:** This tutorial assumes you are familiar with using a Raspberry Pi and you have the latest (full\... with recommended software) version of [Raspbian OS](https://www.raspberrypi.org/downloads/raspbian/) your Raspberry Pi. You can download the latest version of the Raspbian OS from the [Raspberry Pi Foundation website](https://www.raspberrypi.org/downloads/raspbian/). As of Feb. 13th 2019, we recommend the **Raspbian Stretch with desktop and recommended software** option.\
\
If this is your first time using a Raspberry Pi, please head over to the [Raspberry Pi Foundation website](https://www.raspberrypi.org/help/) to use their quickstart guides. We have listed a few of them here:\
\

1.  [Setting up your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up)

2.  [Using your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-using)

3.  [Documentation]:

    [Setup Documentation](https://www.raspberrypi.org/documentation/setup/)\
    [Installation Documentation](https://www.raspberrypi.org/documentation/installation/)\
    [Raspbian Documentation](https://www.raspberrypi.org/documentation/raspbian/)\
    [SD card Documentation](https://www.raspberrypi.org/documentation/installation/sd-cards.md)

## Arduino Example 

**Note:** This tutorial assumes you are familiar with Arduino products and you are using the latest stable version of the Arduino IDE on your desktop. If this is your first time using the Arduino IDE, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

SparkFun has written some example code to enable and disable ports on the Qwiic Mux. Go ahead and download this example code [here](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Qwiic_MUX_Shield_Examples4.zip).

[Qwiic Mux Example (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/7/Qwiic_MUX_Shield_Examples4.zip)

**Warning!** Make sure to have the **Mux_Control.ino** in the same folder when compiling the **Example1-BasicReadings.ino** sketch file. Otherwise, you may have issues uploading code.

Additionally, you will need to install the MMA8452Q Arduino library if you are using two MMA8452Q accelerometers. First, you'll need the Sparkfun MMA8452Q Arduino library. You can obtain these libraries through the Arduino Library Manager. Search for **Sparkfun MMA8452Q Accelerometer** by **SparkFun Electronics** to install the latest version. If you prefer downloading the libraries from the GitHub repository and manually installing it, you can grab them here:

[Download Sparkfun MMA8452Q Accelerometer (ZIP)](https://github.com/sparkfun/SparkFun_MMA8452Q_Arduino_Library/archive/main.zip)

### Arduino Example [Example1-BasicReadings.ino]

Opening `Example1-BasicReadings` will open two tabs in the Arduino IDE, the first example, and also `Mux_Control`. Let\'s take a look under the hood of `Mux_Control` to get an idea of what\'s going on. There are two functions here, `boolean enableMuxPort(byte portNumber)` and `boolean disableMuxPort(byte portNumber)` which is pretty much all we need to specify which channels we\'d like to talk to on the Mux. If we have a sensor on channel 0, we simply call `enableMuxPort(0)` to open that channel on the multiplexer. Then we\'ll take whatever reads and perform whatever actions we\'d like to the sensor on that channel. Once finished, we have to call `disableMuxPort(0)` to close communication on that channel so we don\'t accidentally perform actions on the sensor on that channel. The below example code shows how to read from two MMA8452Q accelerometers.

    language:c
    #include <Wire.h>
    #include <SparkFun_MMA8452Q.h> //From: https://github.com/sparkfun/SparkFun_MMA8452Q_Arduino_Library

    #define NUMBER_OF_SENSORS 2

    MMA8452Q accel[NUMBER_OF_SENSORS]; //Create an array of MMA8452Q sensors

    void setup()
    

      //Initialize all the sensors
      for (byte x = 0 ; x < NUMBER_OF_SENSORS ; x++)
      

      Serial.println("Mux Shield online");
    }

    void loop()
    

        disableMuxPort(x); //Tell mux to disconnect from this port
      }

      delay(1); //Wait for next reading
    }

With the example provided, you should be able to read two I^2^C sensors with the same address on the same bus! Try opening up the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) set to **115200** baud in order to read the sensor values.

## Arduino Library

We have also written a dedicated [Arduino Library](https://github.com/sparkfun/SparkFun_I2C_Mux_Arduino_Library) for the Qwiic Mux. It includes extra functions which you can use to (e.g.) enable or disable multiple ports in one call.

You can install the library via the Arduino Library Manager:

    language:c
    #include <SparkFun_I2C_Mux_Arduino_Library.h> //Click here to get the library: http://librarymanager/All#SparkFun_I2C_Mux

Or, if you want to, you can download and install it manually:

[Download Sparkfun I2C Mux Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_I2C_Mux_Arduino_Library/archive/master.zip)

Please see [Example2](https://github.com/sparkfun/SparkFun_I2C_Mux_Arduino_Library/blob/master/examples/Example2_DualDistance/Example2_DualDistance.ino) for a fancier way of creating your array of sensors, using a pointer to an array of pointers!

## Python Package Overview

**Note:** This example assumes you are using the latest version of Python (2 or 3). If this is your first time using Python or I^2^C hardware on a Raspberry Pi, please checkout our tutorial on [Python Programming with the Raspberry Pi](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi) and the [Raspberry Pi SPI and I2C Tutorial](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial).

\**On the Raspberry Pi, Python 2 and 3 are included with the Raspbian OS (with desktop and recommended software) image.*

**Support Tip:** Don\'t forget to double check that the hardware I^2^C connection is enabled on your Raspberry Pi or other single board computer.

We\'ve written a Python package to easily get setup and utilize the Qwiic Mux. However, before we jump into operating the multiplexer, let\'s take a closer look at the available functions in the Python package. You can install the `sparkfun-qwiic-tca9548a` Python package hosted by PyPi.

### Installation

To install the Python package for this product, it is recommended that users install the SparkFun Qwiic Python package, which installs all the available Python packages for our Qwiic products and includes the required I^2^C driver package. On systems that support PyPi installation via `pip3` (use `pip` for Python 2) is simple, using the following commands:

For **all users** (note: the user must have [**sudo**](https://en.wikipedia.org/wiki/Sudo) privileges):

    language:bash
    sudo pip3 install sparkfun-qwiic

For the **current user**:

    language:bash
    pip3 install sparkfun-qwiic

**Note:** Users can, alternatively, manually build or individually install the python package (*see instructions below*). The required I^2^C driver package will still need to be installed as well.

If you prefer to manually download and build the libraries from the [GitHub repository](https://github.com/sparkfun/Qwiic_TCA9548A_Py), you can grab them here (*\*Please be aware of any package dependencies. You can also check out the repository documentation page, hosted on [ReadtheDocs](https://qwiic-tca9548a-py.readthedocs.io).*):

[Download the SparkFun TCA9548A Python Package (ZIP)](https://github.com/sparkfun/Qwiic_TCA9548A_Py/archive/main.zip)

#### PyPi Installation

This repository is hosted on PyPi as the `sparkfun-qwiic-tca9548a package`. On systems that support PyPi installation via `pip3` (use `pip` for Python 2) is simple, using the following commands:

For **all users** (note: the user must have [**sudo**](https://en.wikipedia.org/wiki/Sudo) privileges):

    sudo pip3 install sparkfun-qwiic-tca9548a

For the **current user**:

    pip3 install sparkfun-qwiic-tca9548a

#### Local Installation

To install, make sure the `setuptools` package is installed on the system.

Direct installation at the command line (use `python` for Python 2):

    python3 setup.py install

To build a package for use with `pip3`:

    python3 setup.py sdist

A package file is built and placed in a subdirectory called dist. This package file can be installed using `pip3`.

    cd dist
    pip3 install sparkfun_qwiic_tca9548a-<version>.tar.gz

### Python Package Operation

Below is a description of the basic functionality of the Python package. This includes the package organization, built-in methods, and their inputs and/or outputs. For more details on how the Python package works, check out the [source code](https://github.com/sparkfun/Qwiic_TCA9548A_Py/blob/main/qwiic_tca9548a.py) and the [datasheet](https://cdn.sparkfun.com/assets/parts/1/2/2/5/2/TCA9548A_I2C_Multiplexer.pdf).

#### Dependencies

This Python package has a very few dependencies in the code, listed below:

    language:python
    import time                         # Time access and conversion package
    import qwiic_i2c                    # I2C bus driver package

#### Default Variables

The default variables, in the code, for this Python package are listed below:

    language:python
    #The name of this device
    _DEFAULT_NAME = "Qwiic Mux"

    _AVAILABLE_I2C_ADDRESS = [*range(0x70,0x77 + 1)]

#### Class

**`QwiicTCA9548A()`** or **`QwiicTCA9548A(i2caddr)`**\
This Python package operates as a class object, allowing new instances of that type to be made. An `__init__()` constructor is used that creates a connection to an I^2^C device over the I^2^C bus using the default or specified I^2^C address.

##### The Constructor

A constructor is a special kind of method used to initialize (assign values to) the data members needed by the object when it is created.

**`__init__(self, address = None, debug = None, i2c_driver = None)`**

Input: value

The value of the device address. If not defined, the Python package will use the default I^2^C address (**0x29**) stored under `_AVAILABLE_I2C_ADDRESS` variable. (*The other available addresses are configured with the jumpers on the board.*)

Output: Boolean

**True:** Connected to I^2^C device on the default (or specified) address.\
**False:** No device found or connected.

Input: *i2c_driver*

Loads the specified I^2^C driver; by default the [Qwiic I^2^C driver](https://github.com/sparkfun/Qwiic_I2C_Py) is used: `qwiic_i2c.getI2CDriver()`. Users should use the default I^2^C driver and leave this field blank.

#### Functions

A function that is an attribute of the class, which defines a method for instances of that class. In simple terms, they are objects for the operations (or methods) of the class.

**`.is_connected()`**\
Determine if the device is conntected to the system.

Output: Boolean

**True:** Connected to I^2^C device on the default (or specified) address.\
**False:** No device found or connected.

**`.disable_all()`**\
This method disables the connection of all channels on the Qwiic Mux.

**`.disable_channels(disable)`**\
This method disables the connection of specific channels on the Qwiic Mux.

Intput: Integer or List

Channel(s) to disable on the Qwiic Mux.\
**Range:** 0 to 7 (*\*The method will automatically convert an individual integer into a list.*)

**`.enable_all()`**\
This method enables the connection of specific channels on the Qwiic Mux.

**`.enable_channels(enable)`**\
This method enables the connection of specific channels on the Qwiic Mux.

Intput: Integer or List

Channel(s) to enable on the Qwiic Mux.\
**Range:** 0 to 7 (*\*The method will automatically convert an individual integer into a list.*)

**`.list_channels()`**\
This method lists all the available channels and their current configuration (enabled or disabled) on the Qwiic Mux.

### Upgrading the Package

In the future, changes to the Python package might be made. Updating the installed packages has to be done individually for each package (i.e. sub-modules and dependencies won\'t update automatically and must be updated manually). For the `sparkfun-qwiic-tca9548a` Python package, use the following command (use `pip` for Python 2):

For **all users** (note: the user must have [**sudo**](https://en.wikipedia.org/wiki/Sudo) privileges):

    language:bash
    sudo pip3 install --upgrade sparkfun-qwiic-tca9548a

For the **current user**:

    language:bash
    pip3 install --upgrade sparkfun-qwiic-tca9548a

## Python Examples 

The following examples are available in the [GitHub repository](https://github.com/sparkfun/Qwiic_TCA9548A_Py/tree/master/examples). To run the examples, simple download or copy the code into a file. Then, open/save the example file (if needed) and execute the code in [your favorite Python IDE](https://www.sparkfun.com/news/2706).

For example, with the default Python IDLE click **Run \> Run Module** or use the [F5] key. To terminate the example use the [Ctrl] + [C] key combination.

**Support Tip:** To check for changes in the channels of the Qwiic Mux, users can attach various Qwiic boards to the channels (as shown in the **Hardware Assembly** section). With the `i2ctools` package installed on Raspbian, users can verify whether the channels on the Qwiic Mux are enabled with the following command (in the Terminal):

`i2cdetect -y 1`

A table will be printed out in the terminal, listing the addresses of the available devices. By running this command before, between, and after the following examples, users can verify the changes in the enabled channels of the Qwiic Mux.

### Example 1

Users should run the first example after power up or reset of the board. In this example, channels 0 and 4 are enabled, there is a pause, and then channel 7 is enabled.

#### Import Dependencies

The first part of the code, imports the required dependencies to operate.

    language:python
    import qwiic
    import time

#### Initialize Constructor

This line instantiates an object for the device.

    language:python
    test = qwiic.QwiicTCA9548A()

#### Test Run

This section of the code, illustrates how to enable the I^2^C channels on the Qwiic Mux. First, it list all the channels on the Qwiic Mux and their configuration (enabled or disabled). (*\*On power up or reset all the channels will be disabled.*) The second part of the code, enables channels 0 and 4 using the list method. Then then the code pauses for a second before enabling channel 7. Once that task its complete, the code returns the final configuration of the channels. Users should expect to see channels 0, 4, and 7 enabled.

    language:python
    # List Channel Configuration
    test.list_channels()

    # Enable Channels 0 and 4
    test.enable_channels([0,4])

    # Pause 1 sec
    time.sleep (1)

    # Enable Channel 7
    test.enable_channels(7)

    # List Channel Configuration
    test.list_channels()

### Example 2

Users should run the first example before running this example. This example disables channels 0 and 4.

#### Import Dependencies

The first part of the code, imports the required dependencies to operate.

    language:python
    import qwiic
    import time

#### Initialize Constructor

This line instantiates an object for the device.

    language:python
    test = qwiic.QwiicTCA9548A()

#### Test Run

This section of the code, illustrates how to disable the I^2^C channels on the Qwiic Mux. First, it list all the channels on the Qwiic Mux and their configuration (enabled or disabled). (*\*From the previous example, channels 0, 4, and 7 should be enabled.*) The second part of the code, disables channels 0 and 4 using the list method. Then then the code returns the final configuration of the channels. Users should expect to see only channel 7 enabled.

    language:python
    # List Channel Configuration
    test.list_channels()

    # Enable Channels 0 and 4
    test.disable_channels([0,4])

    # List Channel Configuration
    test.list_channels()

## Troubleshooting Tips

Here are a few tips for troubleshooting this device.

### No Available Devices

Double check your connections. On a Raspberry Pi, you may get this is indicated with an `OSError: [Errno 121] Remote I/O error` readout.

On a Raspberry Pi, also make sure that the I^2^C hardware is enabled. This is usually indicated with an `Error: Failed to connect to I2C bus 1.` readout.

### Checking Your I^2^C Connection

A simple method to check if your Raspberry Pi can communicate over I^2^C with the Qwiic Mux, is to ping the I^2^C bus. On the latest releases of Raspbian Stretch, the `i2ctools` package should come pre-installed. If it isn\'t run the following command in the terminal:

    sudo apt-get install i2ctools

Once the `i2ctools` package is installed, you can ping the I^2^C bus with the following command in the terminal:

    i2cdetect -y 1

You should see a table printed out in the terminal. If the Qwiic Mux is connected/working properly you should see the address space for **0x70** marked with 70.