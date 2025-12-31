# Source: https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun SAMD21 Pro RF Hookup Guide

# SparkFun SAMD21 Pro RF Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/5c320824995fcd6990beaf7a3d3f6037?d=retro&s=20&r=pg) Elias The Sparkiest]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft810&name=SparkFun+SAMD21+Pro+RF+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft810 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+SAMD21+Pro+RF+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft810&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft810&t=SparkFun+SAMD21+Pro+RF+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft810&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F1%2F0%2FAngled_SAMD21.jpg&description=SparkFun+SAMD21+Pro+RF+Hookup+Guide "Pin It")

## Introduction

The [SparkFun SAMD21 Pro RF](https://www.sparkfun.com/products/14916) is the fated meeting of a SAMD21 and a long-range RFM95W LoRa®-enabled radio. The outcome is a compact, blazing fast microcontroller with excellent point to point data transmission in the 915MHz ISM radio band with LoRa capabilities. In this tutorial we\'ll break down the capabilities of the development board, give you a brief introduction to LoRa and get you familiarized with the two Arduino libraries that will get you started with the radio and LoRaWan. If you\'re familiar with LoRaWan then skip ahead to the Hardware Overview, otherwise let\'s get started with a brief introduction to LoRaWAN.

[![SparkFun Pro RF - LoRa, 915MHz (SAMD21)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/4/6/5/15836-SparkFun_Pro_RF_-_LoRa__915MHz__SAMD21_-01.jpg)](https://www.sparkfun.com/sparkfun-pro-rf-lora-915mhz-samd21.html)

### [SparkFun Pro RF - LoRa, 915MHz (SAMD21)](https://www.sparkfun.com/sparkfun-pro-rf-lora-915mhz-samd21.html) 

[ WRL-15836 ]

The SparkFun Pro RF is a LoRa®-enabled wireless board that marries a SAMD21 and a long-range RFM95W to make a compact and ea...

[ [\$36.95] ]

**Revision Update:** In the latest revision of the SAMD21 Pro RF, we have made a few changes to improve the board, listed below. If users are unsure about which version they purchased, please refer to the pictures of the updated changes, shown below.

- Fixed the VDDCORE pin connection issue
- Broken out an LED jumper for low power applications
- Added PTH pins for software debug (SWD)

[![](https://cdn.sparkfun.com/r/250-250/assets/learn_tutorials/8/1/0/swd_pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/0/swd_pins.jpg)\
*IO and clock pins for SWD.*

[![led jumper](https://cdn.sparkfun.com/r/250-250/assets/learn_tutorials/8/1/0/led_jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/0/led_jumper.jpg)\
*Jumper for power LED.*

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Pycom LoRa and Sigfox Antenna Kit - 915MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/7/5/14676-LoPy_LoRa_Antenna-01.jpg)](https://www.sparkfun.com/products/14676)

### [Pycom LoRa and Sigfox Antenna Kit - 915MHz](https://www.sparkfun.com/products/14676) 

[ WRL-14676 ]

This universal Antenna Kit can also be used with LoPy, SiPy, LoPy4, and FiPy IoT development boards to talk over LoRa and Sig...

**Retired**

### Single Cell LiPo Batteries

You can power the SAMD21 Pro RF with any of our stocked LiPo Batteries that is above 500mAh.

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

### Tools

Depending on your setup, you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder - 1/4lb Spool (0.032\") Special Blend](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/9/3/10243-Solder_-_1_4lb_Spool__0.032___Special_Blend-01.jpg)](https://www.sparkfun.com/solder-1-4lb-spool-0-032-special-blend.html)

### [Solder - 1/4lb Spool (0.032\") Special Blend](https://www.sparkfun.com/solder-1-4lb-spool-0-032-special-blend.html) 

[ TOL-10243 ]

We don\'t want to hype this solder TOO much, but this could possibly be the best solder in the world. There, we\'ve said it. Th...

[ [\$28.50] ]

[![Weller WE1010 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/6/1/14734-Weller_WE1010_Soldering_Station_-01.jpg)](https://www.sparkfun.com/products/14734)

### [Weller WE1010 Soldering Station](https://www.sparkfun.com/products/14734) 

[ TOL-14734 ]

The WE1010 from Weller is a powerful 70 watt soldering station that is perfect for passionate hobbyists, DIYers, and anyone w...

**Retired**

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/1/14763-Wire_Strippers_-_758PL0066-03.jpg)](https://www.sparkfun.com/products/14763)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/14763) 

[ TOL-14763 ]

These are high grade wire strippers from Techni-Tool with a curved grip making them an affordable option if you need to remov...

**Retired**

### Suggested Reading

If you\'re not familiar with the following topics, or want a more in depth conversation related to the following, please follow the links below.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide)

### SAMD21 Mini/Dev Breakout Hookup Guide 

An introduction to the Atmel ATSAMD21G18 microprocessor and our Mini and Pro R3 breakout boards. Level up your Arduino-skills with the powerful ARM Cortex M0+ processor.

[](https://learn.sparkfun.com/tutorials/lorawan-with-prorf-and-the-things-network)

### LoRaWAN with ProRF and The Things Network 

Learn how to make a LoRaWAN node for your next long range IoT project and connect it to the internet with The Things Network!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft810&name=SparkFun+SAMD21+Pro+RF+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft810 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+SAMD21+Pro+RF+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft810&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft810&t=SparkFun+SAMD21+Pro+RF+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft810&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F1%2F0%2FAngled_SAMD21.jpg&description=SparkFun+SAMD21+Pro+RF+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/all) [Next Page →\
[Brief Introduction to LoRaWAN]](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/brief-introduction-to-lorawan)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/introduction) [Brief Introduction to LoRaWAN](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/brief-introduction-to-lorawan) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/hardware-overview) [Drivers (If You Need Them)](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/drivers-if-you-need-them) [Setting Up Arduino](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/setting-up-arduino) [Point to Point Radio Arduino Examples](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/point-to-point-radio-arduino-examples) [LoRaWAN Arduino Library and Example](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/lorawan-arduino-library-and-example) [Registering Your Node](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/registering-your-node) [Programming the SAMD21 Pro RF](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/programming-the-samd21-pro-rf) [Close the LoRaWAN Jumpers](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/close-the-lorawan-jumpers) [Decode Your Data](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/decode-your-data) [Using the Data](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/using-the-data) [Troubleshooting](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/resources-and-going-further)

[Comments [19]](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [LoRa](https://learn.sparkfun.com/tutorials/tags/lora)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]