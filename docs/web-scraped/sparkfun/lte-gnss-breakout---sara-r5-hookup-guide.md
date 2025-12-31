# Source: https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- LTE GNSS Breakout - SARA-R5 Hookup Guide

# LTE GNSS Breakout - SARA-R5 Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino], [![](https://cdn.sparkfun.com/avatar/ea6398c8ad1d378f523ba26e9c5169ac?d=retro&s=20&r=pg) PaulZC]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1212&name=LTE+GNSS+Breakout+-+SARA-R5++Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1212 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=LTE+GNSS+Breakout+-+SARA-R5++Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1212&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1212&t=LTE+GNSS+Breakout+-+SARA-R5++Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1212&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F1%2F2%2FLTE_GNSS_Breakout-SARA-R5-Thumbnail.jpg&description=LTE+GNSS+Breakout+-+SARA-R5++Hookup+Guide "Pin It")

## Introduction

The SparkFun [LTE GNSS Breakout - SARA-R5](https://www.sparkfun.com/products/18031) provides a robust development tool for the SARA-R510M8S LTE-M module from u-blox.

[![SparkFun LTE GNSS Breakout - SARA-R5](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/2/6/0/18031-SparkFun_LTE_GNSS_Breakout_-_SARA-R5-01.jpg)](https://www.sparkfun.com/sparkfun-lte-gnss-breakout-sara-r5.html)

### [SparkFun LTE GNSS Breakout - SARA-R5](https://www.sparkfun.com/sparkfun-lte-gnss-breakout-sara-r5.html) 

[ GPS-18031 ]

The SARA-R5 LTE GNSS Breakout is a robust development tool for the u-blox\'s impressive SARA-R510M8S LTE-M / NB-IoT module. Pe...

**Retired**

The u-blox SARA-R510M8S module is a secure cloud LTE Cat M1, LTE Cat NB2 solution based on u-blox\'s UBX-R5 cellular chipset with an integrated u-blox M8 GNSS receiver chip and separate GNSS antenna interface. This breakout routes all of the functional pins on the R510M8S module to user interfaces (USB or plated-through hole) so you can take full advantage of all of the features available on this impressive LTE/GNSS module.

The SARA-R5\'s UART interface can be configured into one of five variants, providing connectivity over one or two UARTs. A separate USB port provides access to the SARA\'s trace log for diagnostic purposes. This breakout provides access to all three serial interfaces (UART1, UART2 and SARA Diag) via separate USB-C connections. All eight 3.3V serial signals are available on a 0.1\"-pitch breakout header.

The breakout ships with a [Hologram SIM card](https://www.sparkfun.com/products/17117). If you prefer to use your own SIM card, please check that your chosen service provider offers LTE-M coverage for your area before purchasing.

### Required Materials

In order to follow along with this tutorial you\'ll need the following items to use with the LTE GNSS Breakout - SARA-R5.

The primary interface for this breakout is over USB-C so you\'ll need at least one USB-C cable:

[![USB 2.0 Type-C Cable - 1 Meter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/3/4/16905-USB_-_C_to_C_cable-01.jpg)](https://www.sparkfun.com/usb-2-0-type-c-cable-1-meter.html)

### [USB 2.0 Type-C Cable - 1 Meter](https://www.sparkfun.com/usb-2-0-type-c-cable-1-meter.html) 

[ CAB-16905 ]

1 Meter USB Type C to Type C cable USB 2.0 data transfer capabilities.

[ [\$6.50] ]

[![Reversible USB A to C Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/4/15425-Reversible_USB_A_to_C_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html)

### [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html) 

[ CAB-15425 ]

These 0.8m cables have minor modifications that allow them to be plugged into their ports regardless of orientation on the US...

[ [\$6.50] ]

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

For those who prefer to use the LTE GNSS Breakout with our u-blox SARA-R5 Arduino Library, you\'ll need an Arduino development board:

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun Thing Plus - SAMD51](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/2/7/14713-SparkFun_Thing_Plus_-_SAMD51-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html)

### [SparkFun Thing Plus - SAMD51](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html) 

[ DEV-14713 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun SAMD51 Thing Plus is one of our most powerful microcontroller boards yet!

[ [\$25.50] ]

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

**Note:** The LTE GNSS Breakout runs at **3.3V** logic and requires some hardware modifications to work with an Arduino and the u-blox SARA-R5 Library. Read on to the [Hardware Assembly](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide#hardware-assembly) section for detailed instructions.

The breakout requires a pair of antennas, one for the LTE module and another for the GNSS receiver. The options below work with the LTE GNSS Breakout:

[![GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/1/15192-GNSS_Multi-band_Magnetic_Mount_Antenna_SMA_-_5m-01.jpg)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html)

### [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html) 

[ GPS-15192 ]

The ANN-MB-00 GNSS multi-band antenna is extremely unique from other GNSS/GPS antennas in that it is designed to receive both...

[ [\$109.95] ]

[![GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/0/14986-GPS_GNSS_Magnetic_Mount_Antenna_SMA_-_3m-01.jpg)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html)

### [GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html) 

[ GPS-14986 ]

This exceptional GPS/GNSS antenna is designed for both GPS and GLONASS reception.

[ [\$16.50] ]

[![LTE Hinged External Antenna - 698MHz-2.7GHz, SMA Male](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/8/7/16432-698MHz-2.7GHz_LTE_Hinged_External_Antenna__with_SMA_Male_Connector-01.jpg)](https://www.sparkfun.com/lte-hinged-external-antenna-698mhz-2-7ghz-sma-male.html)

### [LTE Hinged External Antenna - 698MHz-2.7GHz, SMA Male](https://www.sparkfun.com/lte-hinged-external-antenna-698mhz-2-7ghz-sma-male.html) 

[ CEL-16432 ]

Molex LTE/5G Cellular External Antennas are designed for 2G/3G/4G/5G modules and devices.

[ [\$12.95] ]

**Note:** The SMA connections are standard polarity: the connector on the LTE GNSS Breakout is female, the antenna connection needs to be standard male. Antennas with reverse-polarity connectors are not suitable for the LTE GNSS Breakout.

### Suggested Reading

If you aren\'t familiar with the following concepts you may want to check out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1212&name=LTE+GNSS+Breakout+-+SARA-R5++Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1212 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=LTE+GNSS+Breakout+-+SARA-R5++Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1212&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1212&t=LTE+GNSS+Breakout+-+SARA-R5++Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1212&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F1%2F2%2FLTE_GNSS_Breakout-SARA-R5-Thumbnail.jpg&description=LTE+GNSS+Breakout+-+SARA-R5++Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/hardware-assembly) [Software Setup](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/software-setup) [SARA-R5 Arduino Library](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/sara-r5-arduino-library) [Arduino Examples](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/arduino-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/lte-gnss-breakout---sara-r5-hookup-guide/all) [Print]

- **Tags**
- - [Cellular](https://learn.sparkfun.com/tutorials/tags/cellular)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]