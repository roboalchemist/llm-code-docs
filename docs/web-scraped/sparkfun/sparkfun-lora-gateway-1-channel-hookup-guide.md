# Source: https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun LoRa Gateway 1-Channel Hookup Guide

# SparkFun LoRa Gateway 1-Channel Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom], [![](https://cdn.sparkfun.com/avatar/92955b303c984cbfe9a72102a670afc7?d=retro&s=20&r=pg) Liquid Soulder]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft826&name=SparkFun+LoRa+Gateway+1-Channel+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft826 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+LoRa+Gateway+1-Channel+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft826&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft826&t=SparkFun+LoRa+Gateway+1-Channel+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft826&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F2%2F6%2F15006-SparkFun_LoRa_Gateway_-_1-Channel__ESP32_-01.jpg&description=SparkFun+LoRa+Gateway+1-Channel+Hookup+Guide "Pin It")

## Introduction

**Heads up!** Warning - TTN v.3 does not support single channel gateways like this one on account of them causing network issues for other multi channel gateways; \"crippling\" some might say. This is because as they are not, necessarily, LoRaWAN-compliant. They are, however, a great way to begin exploring the world of LoRa. Most of the hookup guide references using The Things Network to which TTN requests a LoRaWAN gateway with a minimum of 8 channel support. At this time, SparkFun is working on a revision of the tutuorial, but we can only recommend using this product as an ESP32 development board.

**Note:** Please note that this tutorial is for [WRL-15006](https://www.sparkfun.com/products/15006). The tutorial is applicable for [WRL-18074](https://www.sparkfun.com/products/18074). The only difference is between the two SKUs is that the the ESP32-WROOM-32 module was updated from 4MB to 16MB.\
\
If you are using this with the older version \[[SPX-14893](https://www.sparkfun.com/products/14893)\], please refer to the [ESP32 LoRa 1-CH Gateway, LoRaWAN, and the Things Network](https://learn.sparkfun.com/tutorials/esp32-lora-1-ch-gateway-lorawan-and-the-things-network) tutorial.

So you\'ve designed an automatic shepherding robot but you still have to go out to the field to make sure it is working? Worry no more, you can use long-range radio to keep tabs on that \'bot through the internet of things! All you need is an interpreter to speak the language, and the [LoRa Gateway 1-Channel](https://www.sparkfun.com/products/18074) does just that.

[![SparkFun LoRa Gateway - 1-Channel (ESP32)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/3/8/8/18074-SparkFun_LoRa_Gateway_-_1-Channel__ESP32_-01.jpg)](https://www.sparkfun.com/sparkfun-lora-gateway-1-channel-esp32.html)

### [SparkFun LoRa Gateway - 1-Channel (ESP32)](https://www.sparkfun.com/sparkfun-lora-gateway-1-channel-esp32.html) 

[ WRL-18074 ]

The SparkFun 1-Channel LoRa Gateway is a powerful 3-network capable device thanks to an onboard ESP32 WROOM module and an RFM...

**Retired**

The LoRa Gateway 1-Channel is a monster 3-network capable device thanks to an ESP32 module and a RFM95W LoRa modem. The RFM95W handles the 915 MHz band while the ESP32 takes care of bluetooth and WiFi. One of the ideal uses is to convert LoRa (Long Range) radio messages into data packets that you can access via the web, but of course the flexibility it offers can be put to many more uses!

This guide will go over the hardware on the board, how to program it in Arduino, how to create a single channel LoRa gateway, and finally how to create a LoRa device on The Things Network.

### Required Materials

The LoRa Gateway 1-Channel can act as either a gateway or a device, but not both at the same time. To really be sure that your setup works as expected you should have another LoRa device to listen to, and/or another LoRa gateway to transmit to. The good news is that the LoRa Gateway 1-Channel can act as both so if you have two then you\'re all set.

If you only have one LoRa 1-Channel gateway then you can choose one of these products to test it:

[![SparkFun Pro RF - LoRa, 915MHz (SAMD21)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/6/5/15836-SparkFun_Pro_RF_-_LoRa__915MHz__SAMD21_-01.jpg)](https://www.sparkfun.com/sparkfun-pro-rf-lora-915mhz-samd21.html)

### [SparkFun Pro RF - LoRa, 915MHz (SAMD21)](https://www.sparkfun.com/sparkfun-pro-rf-lora-915mhz-samd21.html) 

[ WRL-15836 ]

The SparkFun Pro RF is a LoRa®-enabled wireless board that marries a SAMD21 and a long-range RFM95W to make a compact and ea...

[ [\$36.95] ]

[![LoRa Raspberry Pi Gateway with Enclosure](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/6/1/15336-LoRa_Raspberry_Pi_Gateway_with_Enclosure-01.jpg)](https://www.sparkfun.com/products/15336)

### [LoRa Raspberry Pi Gateway with Enclosure](https://www.sparkfun.com/products/15336) 

[ WRL-15336 ]

This LoRa Gateway has 8 channels, 15km line of sight range, & comes assembled with everything necessary for easy deployment i...

**Retired**

[![LoRa Raspberry Pi 4 Gateway with Enclosure](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/3/0/3/16447-LoRa_Raspberry_Pi_4_Gateway_with_Enclosure-01.jpg)](https://www.sparkfun.com/lora-raspberry-pi-4-gateway-with-enclosure.html)

### [LoRa Raspberry Pi 4 Gateway with Enclosure](https://www.sparkfun.com/lora-raspberry-pi-4-gateway-with-enclosure.html) 

[ WRL-16447 ]

This LoRa Gateway has 8 channels, 15km line of sight range, & comes assembled with everything necessary for easy deployment i...

**Retired**

[![SparkFun LoRa Gateway - 1-Channel (ESP32)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/3/8/8/18074-SparkFun_LoRa_Gateway_-_1-Channel__ESP32_-01.jpg)](https://www.sparkfun.com/sparkfun-lora-gateway-1-channel-esp32.html)

### [SparkFun LoRa Gateway - 1-Channel (ESP32)](https://www.sparkfun.com/sparkfun-lora-gateway-1-channel-esp32.html) 

[ WRL-18074 ]

The SparkFun 1-Channel LoRa Gateway is a powerful 3-network capable device thanks to an onboard ESP32 WROOM module and an RFM...

**Retired**

To program the LoRa Gateway 1-Channel you will need a [micro-B USB cable](https://www.sparkfun.com/products/10215) and a computer with the Arduino IDE installed. If you want to make a permanent installation away from your computer then consider powering it with a [USB wall adapter](https://www.sparkfun.com/products/11456) or [USB battery pack](https://www.sparkfun.com/products/14169).

### Tools

To use the 915 MHz radio on the gateway you will need an antenna - for which you have two choices. You may cut a length of solid-core wire to approx 3\" or use a 915 MHz antenna with a U.FL connector. If you choose the wire route then you will also need a [soldering iron and tools](https://www.sparkfun.com/categories/49) to attach your antenna to the board.

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

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

[![Pycom LoRa and Sigfox Antenna Kit - 915MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/7/5/14676-LoPy_LoRa_Antenna-01.jpg)](https://www.sparkfun.com/products/14676)

### [Pycom LoRa and Sigfox Antenna Kit - 915MHz](https://www.sparkfun.com/products/14676) 

[ WRL-14676 ]

This universal Antenna Kit can also be used with LoPy, SiPy, LoPy4, and FiPy IoT development boards to talk over LoRa and Sig...

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide)

### SparkFun Serial Basic CH340C Hookup Guide 

SparkFun Serial Basic Breakout takes advantage of USB-C and is an easy-to-use USB-to-Serial adapter based on the CH340C IC from WCH. With USB-C you can get up to three times the power delivery over the previous USB generation and has the convenient feature of being reversable.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft826&name=SparkFun+LoRa+Gateway+1-Channel+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft826 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+LoRa+Gateway+1-Channel+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft826&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft826&t=SparkFun+LoRa+Gateway+1-Channel+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft826&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F2%2F6%2F15006-SparkFun_LoRa_Gateway_-_1-Channel__ESP32_-01.jpg&description=SparkFun+LoRa+Gateway+1-Channel+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/hardware-overview) [Programming the ESP32 With Arduino](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/programming-the-esp32-with-arduino) [LoRaWAN Roadmap](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/lorawan-roadmap) [Single-Channel LoRaWAN Gateway](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/single-channel-lorawan-gateway) [Turning a Gateway Into a Device](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/turning-a-gateway-into-a-device) [Routing Into The Things Network](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/routing-into-the-things-network) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/resources-and-going-further)

[Comments [13]](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [ESP32](https://learn.sparkfun.com/tutorials/tags/esp32)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [LoRa](https://learn.sparkfun.com/tutorials/tags/lora)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]