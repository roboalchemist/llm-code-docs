# Source: https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Simultaneous RFID Tag Reader Hookup Guide

# Simultaneous RFID Tag Reader Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1ff6ad39b8c242a14296a76845e116cd?d=retro&s=20&r=pg) Nate]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft613&name=Simultaneous+RFID+Tag+Reader+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft613 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Simultaneous+RFID+Tag+Reader+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft613&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft613&t=Simultaneous+RFID+Tag+Reader+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft613&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F1%2F3%2FRFID_Tutorial-02.jpg&description=Simultaneous+RFID+Tag+Reader+Hookup+Guide "Pin It")

## Introduction

The SparkFun [M6E Nano](https://www.sparkfun.com/products/16887) [Simultaneous RFID Tag Reader](https://www.sparkfun.com/products/14066) (SRTR for short) has numerous features that make it a huge leap forward over other RFID readers.

[![SparkFun Simultaneous RFID Reader - M6E Nano](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/9/1/6/14066-SparkFun_Simultaneous_RFID_Reader_-_M6E_Nano-01b.jpg)](https://www.sparkfun.com/sparkfun-simultaneous-rfid-reader-m6e-nano.html)

### [SparkFun Simultaneous RFID Reader - M6E Nano](https://www.sparkfun.com/sparkfun-simultaneous-rfid-reader-m6e-nano.html) 

[ SEN-14066 ]

The SparkFun Simultaneous RFID Reader is an Arduino-compatible board to get you started with the M6E Nano UHF RFID Reader.

**Retired**

The greatest feature is that the SRTR is able to read multiple tags at the same time. Additionally the read distance of tags is greatly increased (up to 16 feet!) from other readers. Did we mention you can write your own data to the tags? Oh yea, you can do that too.

## Suggested Materials

The SRTR was designed to work either with a USB to Serial connection to a computer or as a shield to an Arduino-compatible board. If you're just getting started we recommend you start with the serial connection to a computer so that you can use the [Universal Reader Assistant](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/using-the-universal-reader-assistant) software to experiment quickly with different tags and read distances. Then move to a microcontroller or single board computer. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### USB to Serial Connection

For a basic set-up using the SRTR with a USB-to-Serial connection, we recommend the following products.

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![SparkFun Serial Basic Breakout - CH340G](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/8/8/14050-01.jpg)](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340g.html)

### [SparkFun Serial Basic Breakout - CH340G](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340g.html) 

[ DEV-14050 ]

The SparkFun Serial Basic Breakout is an easy-to-use USB-to-Serial adapter based on the CH340G IC from WCH.

[ [\$9.25] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

### Arduino Shield Connection

If you're using the SRTR as a shield, we recommend the following materials.

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Arduino Stackable Header Kit - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/7/2/1/6/11417-01a.jpg)](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html)

### [Arduino Stackable Header Kit - R3](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html) 

[ PRT-11417 ]

These headers are made to work with the Arduino Uno R3, Leonardo and new Arduino boards going forward. They are the perfect h...

[ [\$2.75] ]

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

Any microcontroller or single board computer capable of **115200bps** will work (however the module can be configured to 9600bps). The [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) or [Arduino Uno](https://www.sparkfun.com/products/11021) are popular options for this role, but just about any microcontroller development board should work. (The firmware examples use an Arduino library, if that serves as any extra motivation to use an Arduino.) **You will want an external power supply to run the module at full power**. Please see the Power Supply Considerations section for more information.

### Additional Materials

To follow along with the examples in this tutorial, you will also want access to some UHF passive RFID tags, and optionally, an antenna for extended range, and an attachment cable.

[![UHF RFID Antenna (RP-TNC)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/2/8/14131-02a.jpg)](https://www.sparkfun.com/uhf-rfid-antenna-rp-tnc.html)

### [UHF RFID Antenna (RP-TNC)](https://www.sparkfun.com/uhf-rfid-antenna-rp-tnc.html) 

[ WRL-14131 ]

This is your solution when you absolutely, positively need to get the most out of an antenna for your next RFID project. This...

[ [\$48.50] ]

[![Interface Cable for RP-TNC to RP-SMA - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/2/9/14132-01a.jpg)](https://www.sparkfun.com/interface-cable-for-rp-tnc-to-rp-sma-1m.html)

### [Interface Cable for RP-TNC to RP-SMA - 1m](https://www.sparkfun.com/interface-cable-for-rp-tnc-to-rp-sma-1m.html) 

[ CAB-14132 ]

This is a very simple 1m long Male RP-TNC to Male RP-SMA cable. We like to use this cable to connect our ultra high-frequency...

[ [\$7.95] ]

[![Interface Cable RP-SMA to U.FL - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/7/00662-1.jpg)](https://www.sparkfun.com/interface-cable-rp-sma-to-u-fl.html)

### [Interface Cable RP-SMA to U.FL - 100mm](https://www.sparkfun.com/interface-cable-rp-sma-to-u-fl.html) 

[ WRL-00662 ]

Commonly used to attach WiFi, Bluetooth, or nRFxxx based devices to a 2.4GHz antenna.

[ [\$4.95] ]

[![UHF RFID Tag (Set of 5)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/4/9/14147-01.jpg)](https://www.sparkfun.com/products/14147)

### [UHF RFID Tag (Set of 5)](https://www.sparkfun.com/products/14147) 

[ WRL-14147 ]

Ever wanted to play with those newfangled RFID tags? Although it\'s been around for a while, the technology has been extremely...

**Retired**

[![UHF RFID Tag - Adhesive (Set of 5)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/5/4/14151-01.jpg)](https://www.sparkfun.com/products/14151)

### [UHF RFID Tag - Adhesive (Set of 5)](https://www.sparkfun.com/products/14151) 

[ WRL-14151 ]

Ever wanted to play with those newfangled RFID tags? Although it\'s been around for a while, the technology has been extremely...

**Retired**

[![UHF RFID Tags - Adhesive (5 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/0/3/2/TagStrip_01.jpg)](https://www.sparkfun.com/uhf-rfid-tags-adhesive-5-pack.html)

### [UHF RFID Tags - Adhesive (5 Pack)](https://www.sparkfun.com/uhf-rfid-tags-adhesive-5-pack.html) 

[ WRL-20228 ]

These paper-thin, adhesive EPCglobal Gen2 tags work with our RFID readers and can be stuck to practically anything.

**Retired**

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/rfid-basics)

### RFID Basics 

Dive into the basics of Radio Frequency Identification (RFID) technology.

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft613&name=Simultaneous+RFID+Tag+Reader+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft613 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Simultaneous+RFID+Tag+Reader+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft613&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft613&t=Simultaneous+RFID+Tag+Reader+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft613&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F1%2F3%2FRFID_Tutorial-02.jpg&description=Simultaneous+RFID+Tag+Reader+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/hardware-overview) [Hardware Hookup](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/hardware-hookup) [Using an External Antenna](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/using-an-external-antenna) [Power Supply Considerations](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/power-supply-considerations) [Thermal Considerations](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/thermal-considerations) [Software Options](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/software-options) [Using the Universal Reader Assistant](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/using-the-universal-reader-assistant) [Using the Arduino Library](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/using-the-arduino-library) [Example 1 - Constant Read](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/example-1---constant-read) [Example 2 - Read EPC](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/example-2---read-epc) [Example 3 - Write EPC](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/example-3---write-epc) [Example 4 - Read User Data](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/example-4---read-user-data) [Example 5 - Write User Data](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/example-5---write-user-data) [Examples 6, 7, 8 - Passwords](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/examples-6-7-8---passwords) [Example 9 - Read TID](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/example-9---read-tid) [Example 10 - Range Test](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/example-10---range-test) [Resources and Going Further](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/resources-and-going-further)

[Comments [86]](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Communication](https://learn.sparkfun.com/tutorials/tags/communication)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [RFID](https://learn.sparkfun.com/tutorials/tags/rfid)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Shields](https://learn.sparkfun.com/tutorials/tags/shields)
  - [Technology](https://learn.sparkfun.com/tutorials/tags/technology)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]