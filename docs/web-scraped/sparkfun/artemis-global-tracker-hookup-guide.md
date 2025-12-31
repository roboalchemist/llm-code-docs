# Source: https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Artemis Global Tracker Hookup Guide

# Artemis Global Tracker Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete], [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2000&name=Artemis+Global+Tracker+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2000 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Artemis+Global+Tracker+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2000&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2000&t=Artemis+Global+Tracker+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2000&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F0%2F0%2F0%2FAGT_Thumbnail.jpg&description=Artemis+Global+Tracker+Hookup+Guide "Pin It")

## Introduction

The [SparkFun Artemis Global Tracker](https://www.sparkfun.com/products/18712) provides a powerful tracking system combining remote short messaging via the Iridium satellite network with GPS tracking and environmental sensing all powered by the SparkFun [Artemis module](https://www.sparkfun.com/artemis). The Global Tracker design focuses on truly remote tracking, data collection and transmission so whether you\'re looking to transmit environmental data from the top of a mountain, send data from a traveling balloon, control and monitor remote equipment or maybe communicate in an emergency when other networks are not available; the Artemis Global Tracker may be just the right tool for your remote data project.

[![SparkFun Artemis Global Tracker](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/2/5/3/18712-SparkFun_Artemis_Global_Tracker-01.jpg)](https://www.sparkfun.com/sparkfun-artemis-global-tracker.html)

### [SparkFun Artemis Global Tracker](https://www.sparkfun.com/sparkfun-artemis-global-tracker.html) 

[ WRL-18712 ]

With a clear view of the sky, the Artemis Global Tracker allows you to send and receive short data messages thanks to the Iri...

[ [\$419.95] ]

The Artemis Global Tracker features an Iridium 9603N satellite transceiver, u-blox ZOE-M8Q GNSS module and MS8607 pressure, humidity and temperature sensor. We designed the Artemis Global Tracker with the idea of creating a robust data tracking module that works anywhere in the world, including the polar regions, far beyond the reach of WiFi and GSM networks.

### Required Materials

The Artemis Global Tracker (or AGT as we\'ll sometimes refer to it in this guide) requires a few external components to get up and running properly. First and foremost is a power supply. The AGT receives power via either USB-C, single-cell LiPo battery or an external solar panel or battery pack (max 6V). Take a look at the products below for power supply options for the AGT:

#### USB-C

[![Reversible USB A to C Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/4/15425-Reversible_USB_A_to_C_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html)

### [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html) 

[ CAB-15425 ]

These 0.8m cables have minor modifications that allow them to be plugged into their ports regardless of orientation on the US...

[ [\$6.50] ]

[![Reversible USB A to C Cable - 0.3m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/5/15426-Reversible_USB_A_to_C_Cable_-_0.3m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-3m.html)

### [Reversible USB A to C Cable - 0.3m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-3m.html) 

[ CAB-15426 ]

These 0.3m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the...

[ [\$5.50] ]

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

#### LiPo Battery

[![Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/6/0/6/17748-Lithium_Ion_Battery_-_1250_mAh__IEC62133_certified_-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html)

### [Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html) 

[ PRT-18286 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1250 mAh and is IE...

**Retired**

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

#### Solar Panel

[![Solar Panel - 2W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/4/8/13781-01.jpg)](https://www.sparkfun.com/products/13781)

### [Solar Panel - 2W](https://www.sparkfun.com/products/13781) 

[ PRT-13781 ]

Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...

**Retired**

[![Solar Panel - 3.5W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/4/9/13782-01.jpg)](https://www.sparkfun.com/products/13782)

### [Solar Panel - 3.5W](https://www.sparkfun.com/products/13782) 

[ PRT-13782 ]

Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...

**Retired**

[![Solar Panel - 6W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/5/0/13783-01.jpg)](https://www.sparkfun.com/products/13783)

### [Solar Panel - 6W](https://www.sparkfun.com/products/13783) 

[ PRT-13783 ]

Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...

**Retired**

[![Solar Panel - 9W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/5/1/13784-01.jpg)](https://www.sparkfun.com/products/13784)

### [Solar Panel - 9W](https://www.sparkfun.com/products/13784) 

[ PRT-13784 ]

Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...

**Retired**

**Note:** The Artemis Global Tracker uses a JST connector for both the LiPo and Solar Panel / Battery Pack power inputs. The panels listed above all terminate in a standard barrel jack so users need to modify the termination or use an adapter like this [Barrel Jack to JST Adapter](https://www.sparkfun.com/products/8734).

#### Antenna

The AGT also requires an external antenna for the 9603N and M8Q modules. The AGT routes both modules\' antenna pins to a shared SMA connector so to keep things simple, we recommend a *passive* antenna tuned for Iridium/GPS/GLONASS bands like the antenna shown below:

[![Iridium/GPS/GLONASS Passive Antenna](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/7/5/9/16838-Iridium_GPS_GLONASS_Passive_Antenna-03.jpg)](https://www.sparkfun.com/iridium-gps-glonass-passive-antenna.html)

### [Iridium/GPS/GLONASS Passive Antenna](https://www.sparkfun.com/iridium-gps-glonass-passive-antenna.html) 

[ GPS-16838 ]

The M1600HCT-P-SMA is an unique antenna combining the ability to communicate with the Iridium network while simultaneously re...

[ [\$70.95] ]

#### External Capacitors

Users powering the Artemis Global Tracker with a solar panel or lower-current power configurations need to attach a pair of external 10F capacitors like the ones below to provide the extra current for 9603N SBD transmissions:

[![Super Capacitor - 10F/2.5V](https://cdn.sparkfun.com/r/600-600/assets/parts/5/1/9/SuperCap.jpg)](https://www.sparkfun.com/super-capacitor-10f-2-5v.html)

### [Super Capacitor - 10F/2.5V](https://www.sparkfun.com/super-capacitor-10f-2-5v.html) 

[ COM-00746 ]

Yes you read that correctly - 10Farad capacitor. This small cap can be charged up and then slowly dissipated running an entir...

[ [\$4.95] ]

#### Satellite Network Line Rental

The Iridium modem requires a monthly rental service to exchange information with the Iridium satellite network. Set up an account with Rock7 [here](https://rockblock.rock7.com/Operations). You only pay for months in which you wish to use the modem. No annual contract is required. Line rental costs £12GBP (about \$15USD) per month and includes access to the RockBLOCK management system for managing your devices. The billing system is built-in, and allows you to pay for only what you use. Airtime for Iridium modems must be purchased from Rock Seven via the admin portal once the units are registered. You cannot use the devices with another Iridium airtime provider by default. If you would like to use it with another provider, you will need to pay an unlock fee of \$60USD per modem.

### Recommended Reading

Users who have never used the Artemis module or other Artemis boards may want to read through the following tutorials before getting started with the Artemis Global Tracker:

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.

[](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk)

### Using SparkFun Edge Board with Ambiq Apollo3 SDK 

We will demonstrate how to get started with your SparkFun Edge Board by setting up the toolchain on your computer, examining an example program, and using the serial uploader tool to flash the chip.

[](https://learn.sparkfun.com/tutorials/designing-with-the-sparkfun-artemis)

### Designing with the SparkFun Artemis 

Let\'s chat about layout and design considerations when using the Artemis module.

[](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide)

### Artemis Development with the Arduino IDE 

This is an in-depth guide on developing in the Arduino IDE for the Artemis module and any Artemis microcontroller development board. Inside, users will find setup instructions and simple examples from blinking an LED and taking ADC measurements; to more complex features like BLE and I2C.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2000&name=Artemis+Global+Tracker+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2000 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Artemis+Global+Tracker+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2000&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2000&t=Artemis+Global+Tracker+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2000&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F0%2F0%2F0%2FAGT_Thumbnail.jpg&description=Artemis+Global+Tracker+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/hardware-assembly) [Iridium and Artemis Software Setup](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/iridium-and-artemis-software-setup) [Artemis Global Tracker Arduino Examples](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/artemis-global-tracker-arduino-examples) [Artemis Global Tracker Configuration Tool](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/artemis-global-tracker-configuration-tool) [Troubleshooting](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/resources)

[Comments [0]](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/artemis-global-tracker-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Artemis](https://learn.sparkfun.com/tutorials/tags/artemis)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Satellite](https://learn.sparkfun.com/tutorials/tags/satellite)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Weather](https://learn.sparkfun.com/tutorials/tags/weather)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]