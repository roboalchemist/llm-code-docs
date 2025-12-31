# Source: https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- 1W LoRa MicroMod Function Board Hookup Guide

# 1W LoRa MicroMod Function Board Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1ff6ad39b8c242a14296a76845e116cd?d=retro&s=20&r=pg) Nate], [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1996&name=1W+LoRa+MicroMod+Function+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1996 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=1W+LoRa+MicroMod+Function+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1996&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1996&t=1W+LoRa+MicroMod+Function+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1996&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F9%2F9%2F6%2Fassembly_complete.jpg&description=1W+LoRa+MicroMod+Function+Board+Hookup+Guide "Pin It")

## Introduction

**[Frequency Operation]**

This LoRa module can only be used in the **915MHz** [LoRaWAN](https://lora-alliance.org/) frequency band *(i.e. 902 to 928 MHz)*. It is not compatible with other frequency bands; double check the [frequency band used in your region](https://lora-alliance.org/resource_hub/rp2-102-lorawan-regional-parameters/). Check out these resources from The Things Network for an **unofficial** summary of [regional radio regulations](https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/) and list of the [regional frequency plans](https://www.thethingsnetwork.org/docs/lorawan/frequency-plans/).

The [1W LoRa MicroMod Function Board](https://www.sparkfun.com/products/18573) adds LoRa capabilities to your MicroMod project. It is intended to be used in conjunction with a [MicroMod processor board](https://www.sparkfun.com/micromod#processor_boards) and a [MicroMod main board](https://www.sparkfun.com/categories/tags/main-board), which provides the electrical interface between a [processor board](https://www.sparkfun.com/categories/tags/processor-board) and the [function board(s)](https://www.sparkfun.com/categories/tags/function-board).

[![SparkFun MicroMod LoRa Function Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/0/4/0/18573-SparkFun_MicroMod_LoRa_Function_Board-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-lora-function-board.html)

### [SparkFun MicroMod LoRa Function Board](https://www.sparkfun.com/sparkfun-micromod-lora-function-board.html) 

[ WRL-18573 ]

The SparkFun MicroMod LoRa Function Board provides LoRA and LoRaWAN capabilities to your MicroMod project.

**Retired**

Match up the board\'s M.2 edge connector to the slot of the M.2 connector and secure the function board with the screws provided with the main board.

Utilizing the 915M30S LoRa module from EBYTE, which is a 1W (30dBm) transceiver based around the SX1276 from Semtech. There is a robust edge mount RP-SMA connector for large LoRa (915MHz) antennas; with modification, a U.FL connector is also available. We\'ve successfully tested a 12 miles line-of-sight transmission with this module *(user results may vary)*.

With the MicroMod standardization, users no longer need to cross-reference schematics with datasheets, while fumbling around with jumper wires. Simply, match up the function board\'s M.2 edge connector to the slot of the M.2 connector on the main board and secure the function board with screws. All connections are hardwired to compatible pins of the processor board and the pin connections are standardized for the processor boards.

### Required Materials

To get started, users will need a few of the items listed below. *(You may already have a some of these items; read through the guide and modify your cart accordingly.)*

#### MicroMod Processor Board

A [processor board](https://www.sparkfun.com/categories/tags/processor-board) is required for the MicroMod system to operate. Users can choose a processor board, based upon their needs, to attach to the [MicroMod M.2 connector](https://www.sparkfun.com/products/16549) of the main board. Below, are few options:

[![SparkFun MicroMod Teensy Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/2/16402-SparkFun_MicroMod_Teensy_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html)

### [SparkFun MicroMod Teensy Processor](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html) 

[ DEV-16402 ]

This board leverages the awesome computing power of the NXP iMXRT1062 chip (ARM Cortex-M7) and pairs it with the M.2 MicroMod...

[ [\$24.95] ]

[![SparkFun MicroMod nRF52840 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/9/2/1/16984-SparkFun_MicroMod_nRF52840_Processor-04.jpg)](https://www.sparkfun.com/sparkfun-micromod-nrf52840-processor.html)

### [SparkFun MicroMod nRF52840 Processor](https://www.sparkfun.com/sparkfun-micromod-nrf52840-processor.html) 

[ WRL-16984 ]

The SparkFun MicroMod nRF52840 Processor offers a powerful combination of ARM Cortex-M4 CPU and 2.4 GHz Bluetooth transceiver...

[ [\$29.50] ]

[![SparkFun MicroMod STM32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/1/2/2/STM32F405-_01.jpg)](https://www.sparkfun.com/sparkfun-micromod-stm32-processor.html)

### [SparkFun MicroMod STM32 Processor](https://www.sparkfun.com/sparkfun-micromod-stm32-processor.html) 

[ DEV-21326 ]

The SparkFun MicroMod STM32 Processor Board is ready to rock your MicroMod world with its ARM® Cortex®-M4 32-bit RISC core!

[ [\$20.50] ]

[![SparkFun MicroMod STM32WB5MMG Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/2/6/8/21438-_DEV_MM_STM32WB-_01.jpg)](https://www.sparkfun.com/sparkfun-micromod-stm32wb5mmg-processor.html)

### [SparkFun MicroMod STM32WB5MMG Processor](https://www.sparkfun.com/sparkfun-micromod-stm32wb5mmg-processor.html) 

[ DEV-21438 ]

The MicroMod STM32WB5MMG Processor has a powerful combination of computing and wireless capabilities all on one Processor.

[ [\$19.95] ]

#### MicroMod Main Board

A [main board](https://www.sparkfun.com/categories/tags/main-board) provides the electrical connections between the function and processor boards to operate. Users can choose a main board based upon their needs. Below, are few options:

[![SparkFun MicroMod Main Board - Double](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/4/2/5/20595-DEV_SparkFun_MicroMod_Main_Board_Double_v22-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-double.html)

### [SparkFun MicroMod Main Board - Double](https://www.sparkfun.com/sparkfun-micromod-main-board-double.html) 

[ DEV-20595 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with up to two...

[ [\$22.95] ]

[![SparkFun MicroMod Main Board - Single](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/7/7/20748-DEV_SparkFun_MicroMod_Main_Board_Single_v21-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html)

### [SparkFun MicroMod Main Board - Single](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html) 

[ DEV-20748 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with a single ...

[ [\$18.50] ]

#### Required Hardware

A Phillips screw driver is necessary to attach the processor board and function board(s) to the main board. Additionally, a USB-C cable is needed to connect the main board to a computer. The LoRa function board also requires a LoRa antenna for the transceiver to operate.

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

Below, is a selection of our 915MHz frequency band [RP-SMA antennas](https://www.sparkfun.com/categories/78).

[![915MHz LoRa Antenna RP-SMA - 1/2 Wave 2dBi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/5/3/14876-915MHz_LoRa_1_2_Wave_2dBi_Antenna-03.jpg)](https://www.sparkfun.com/915mhz-lora-antenna-rp-sma-1-2-wave-2dbi.html)

### [915MHz LoRa Antenna RP-SMA - 1/2 Wave 2dBi](https://www.sparkfun.com/915mhz-lora-antenna-rp-sma-1-2-wave-2dbi.html) 

[ WRL-14876 ]

Increase your range with this 1/2 wave duck antenna. Designed for 860 to 960MHz it is ideal for distant LoRa nodes. Utilizes ...

[ [\$17.95] ]

[![915MHz LoRa Antenna RP-SMA - 1/4 Wave 2dBi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/5/2/14875-915MHz_LoRa_1_4_Wave_2dBi_Antenna-01.jpg)](https://www.sparkfun.com/915mhz-lora-antenna-rp-sma-1-4-wave-2dbi.html)

### [915MHz LoRa Antenna RP-SMA - 1/4 Wave 2dBi](https://www.sparkfun.com/915mhz-lora-antenna-rp-sma-1-4-wave-2dbi.html) 

[ WRL-14875 ]

A small 1/4 wave rubber duck antenna for LoRa or other 860-960MHz communication. Antenna has a center frequency of 915MHz and...

[ [\$18.95] ]

[![Pycom LoRa and Sigfox Antenna Kit - 915MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/7/5/14676-LoPy_LoRa_Antenna-01.jpg)](https://www.sparkfun.com/products/14676)

### [Pycom LoRa and Sigfox Antenna Kit - 915MHz](https://www.sparkfun.com/products/14676) 

[ WRL-14676 ]

This universal Antenna Kit can also be used with LoPy, SiPy, LoPy4, and FiPy IoT development boards to talk over LoRa and Sig...

**Retired**

#### Optional Hardware

A LoRa gateway provides internet connection for LoRaWAN network. Below are a few options from our [LoRa](https://www.sparkfun.com/categories/410) product category.

[![LoRa Raspberry Pi 4 Gateway with Enclosure](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/3/0/3/16447-LoRa_Raspberry_Pi_4_Gateway_with_Enclosure-01.jpg)](https://www.sparkfun.com/lora-raspberry-pi-4-gateway-with-enclosure.html)

### [LoRa Raspberry Pi 4 Gateway with Enclosure](https://www.sparkfun.com/lora-raspberry-pi-4-gateway-with-enclosure.html) 

[ WRL-16447 ]

This LoRa Gateway has 8 channels, 15km line of sight range, & comes assembled with everything necessary for easy deployment i...

**Retired**

[![Nebra Indoor HNT Hotspot Miner (915MHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/0/1/5/17843-Nebra_Indoor_HNT_Hotspot_Miner__915MHz_-01.JPG)](https://www.sparkfun.com/nebra-indoor-hnt-hotspot-miner-915mhz.html)

### [Nebra Indoor HNT Hotspot Miner (915MHz)](https://www.sparkfun.com/nebra-indoor-hnt-hotspot-miner-915mhz.html) 

[ WRL-17843 ]

Join The People\'s Network and help provide hundreds of square miles of wireless network coverage on Helium LongFi™ (LoRaWAN...

**Retired**

[![Nebra Outdoor HNT Hotspot Miner (915MHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/0/1/6/17844-Nebra_Outdoor_HNT_Hotspot_Miner__915MHz_-01.jpg)](https://www.sparkfun.com/nebra-outdoor-hnt-hotspot-miner-915mhz.html)

### [Nebra Outdoor HNT Hotspot Miner (915MHz)](https://www.sparkfun.com/nebra-outdoor-hnt-hotspot-miner-915mhz.html) 

[ WRL-17844 ]

Join The People\'s Network and help provide hundreds of square miles of wireless network coverage on Helium LongFi™ (LoRaWAN...

**Retired**

Users can also use other LoRa boards for peer-to-peer communication. Below are a few options from our [LoRa](https://www.sparkfun.com/categories/410) product category.

[![SparkFun Pro RF - LoRa, 915MHz (SAMD21)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/6/5/15836-SparkFun_Pro_RF_-_LoRa__915MHz__SAMD21_-01.jpg)](https://www.sparkfun.com/sparkfun-pro-rf-lora-915mhz-samd21.html)

### [SparkFun Pro RF - LoRa, 915MHz (SAMD21)](https://www.sparkfun.com/sparkfun-pro-rf-lora-915mhz-samd21.html) 

[ WRL-15836 ]

The SparkFun Pro RF is a LoRa®-enabled wireless board that marries a SAMD21 and a long-range RFM95W to make a compact and ea...

[ [\$36.95] ]

[![SparkFun LoRa Thing Plus - expLoRaBLE](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/5/5/8/17506-SparkFun_LoRa_Thing_Plus_____expLoRaBLE-01.jpg)](https://www.sparkfun.com/sparkfun-lora-thing-plus-explorable.html)

### [SparkFun LoRa Thing Plus - expLoRaBLE](https://www.sparkfun.com/sparkfun-lora-thing-plus-explorable.html) 

[ WRL-17506 ]

The SparkFun expLoRaBLE Thing Plus is a Feather form-factor development board with the NM180100 system in package (SiP), from...

[ [\$54.95] ]

[![915MHz LoRa Antenna RP-SMA - 1/4 Wave 2dBi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/5/2/14875-915MHz_LoRa_1_4_Wave_2dBi_Antenna-01.jpg)](https://www.sparkfun.com/915mhz-lora-antenna-rp-sma-1-4-wave-2dbi.html)

### [915MHz LoRa Antenna RP-SMA - 1/4 Wave 2dBi](https://www.sparkfun.com/915mhz-lora-antenna-rp-sma-1-4-wave-2dbi.html) 

[ WRL-14875 ]

A small 1/4 wave rubber duck antenna for LoRa or other 860-960MHz communication. Antenna has a center frequency of 915MHz and...

[ [\$18.95] ]

[![Interface Cable RP-SMA to U.FL - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/7/00662-1.jpg)](https://www.sparkfun.com/interface-cable-rp-sma-to-u-fl.html)

### [Interface Cable RP-SMA to U.FL - 100mm](https://www.sparkfun.com/interface-cable-rp-sma-to-u-fl.html) 

[ WRL-00662 ]

Commonly used to attach WiFi, Bluetooth, or nRFxxx based devices to a 2.4GHz antenna.

[ [\$4.95] ]

To modify the jumpers, users will need [soldering equipment](https://www.sparkfun.com/categories/49) and/or a [knife](https://www.sparkfun.com/categories/379).

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Chip Quik No-Clean Flux Pen - 10mL](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/5/14579-Chip_Quik_No-Clean_Flux_Pen_-_10mL-01.jpg)](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html)

### [Chip Quik No-Clean Flux Pen - 10mL](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html) 

[ TOL-14579 ]

This 10mL no-clean flux pen from Chip Quik is great for all of your solder, de-solder, rework, and reflow purposes!

[ [\$8.50] ]

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

### Suggested Reading

The [MicroMod ecosystem](https://www.sparkfun.com/micromod) is a unique way to allow users to customize their project to their needs. Click on the banner below for more information.

[![MicroMod Logo](https://cdn.sparkfun.com/r/500-70/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)

\

For users who aren\'t familiar with the following concepts, we also recommend reading the following tutorials before continuing.

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

[](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino)

### Processor Interrupts with Arduino 

What is an interrupt? In a nutshell, there is a method by which a processor can execute its normal program while continuously monitoring for some kind of event, or interrupt. There are two types of interrupts: hardware and software interrupts. For the purposes of this tutorial, we will focus on hardware interrupts.

[](https://learn.sparkfun.com/tutorials/sparkfun-explorable-hookup-guide)

### SparkFun expLoRaBLE Hookup Guide 

Check out our latest LoRaWAN development board with Bluetooth capabilities! With this guide, we\'ll get you passing data to The Things Network in no time.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[](https://learn.sparkfun.com/tutorials/designing-with-micromod)

### Designing with MicroMod 

This tutorial will walk you through the specs of the MicroMod processor and carrier board as well as the basics of incorporating the MicroMod form factor into your own PCB designs!

[](https://learn.sparkfun.com/tutorials/micromod-main-board-hookup-guide)

### MicroMod Main Board Hookup Guide 

The MicroMod Main Board - Single and Double are specialized carrier boards that allow you to interface a Processor Board with a Function Board(s). The modular system allows you to add an additional feature(s) to a Processor Board with the help of a Function Board(s). In this tutorial, we will focus on the basic functionality of the Main Board - Single and Main Board - Double.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1996&name=1W+LoRa+MicroMod+Function+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1996 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=1W+LoRa+MicroMod+Function+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1996&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1996&t=1W+LoRa+MicroMod+Function+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1996&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F9%2F9%2F6%2Fassembly_complete.jpg&description=1W+LoRa+MicroMod+Function+Board+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/hardware-overview) [Software Overview](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/software-overview) [Hadware Assembly](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/hadware-assembly) [Peer-to-Peer Example](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/peer-to-peer-example) [LoRaWAN Examples](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/lorawan-examples) [Resources and Going Further](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/1w-lora-micromod-function-board-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Communication](https://learn.sparkfun.com/tutorials/tags/communication)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [LoRa](https://learn.sparkfun.com/tutorials/tags/lora)
  - [MicroMod](https://learn.sparkfun.com/tutorials/tags/micromod)
  - [Prototyping](https://learn.sparkfun.com/tutorials/tags/prototyping)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]