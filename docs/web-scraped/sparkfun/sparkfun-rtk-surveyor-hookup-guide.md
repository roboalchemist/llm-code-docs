# Source: https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun RTK Surveyor Hookup Guide

# SparkFun RTK Surveyor Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1ff6ad39b8c242a14296a76845e116cd?d=retro&s=20&r=pg) Nate], [ Ell C]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1463&name=SparkFun+RTK+Surveyor+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1463 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+RTK+Surveyor+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1463&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1463&t=SparkFun+RTK+Surveyor+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1463&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F4%2F6%2F3%2F17369-GPS_RTK_Surveyor_-_Enclosed-01.jpg&description=SparkFun+RTK+Surveyor+Hookup+Guide "Pin It")

## Introduction

The [RTK Surveyor](https://www.sparkfun.com/products/18443) from SparkFun is your one stop shop for high precision geolocation and surveying needs. For basic users, it's incredibly easy to get up and running and for advanced users, the RTK Surveyor is a flexible and powerful tool.

[![SparkFun RTK Surveyor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/8/7/9/17369-GPS_RTK_Surveyor_-_Enclosed-01.jpg)](https://www.sparkfun.com/sparkfun-rtk-surveyor.html)

### [SparkFun RTK Surveyor](https://www.sparkfun.com/sparkfun-rtk-surveyor.html) 

[ GPS-18443 ]

The SparkFun RTK Surveyor is an enclosed and ready to use GNSS receiver for centimeter-level positioning. No programming requ...

[ [\$427.95] ]

With just a few minutes of setup, the RTK Surveyor is one of the fastest ways to take centimeter grade measurements.

[![RTK Fix in SW Maps](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/3/SW_Maps_-_RTK_Fix_on_Pearl_St.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/3/SW_Maps_-_RTK_Fix_on_Pearl_St.jpg)

*An RTK Fix in SW Maps*

By connecting your phone to the RTK Surveyor over Bluetooth, your phone can act as the radio link to provide correction data as well as receive the NMEA output from the device. It's how \$10,000 surveying devices have been operating for the past decade - we just made it easier, smaller, and a lot cheaper.

### Required Materials

While the RTK Surveyor is nicely enclosed you will need a few cables and antennas to make everything work. We\'ll go into the specifics of how to hook things together but in general you will need to get a good quality L1/L2 antenna:

[![GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/7/4/17587-L1_L2_GNSS_antenna_TOP106-09-1.png)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html)

### [GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html) 

[ GPS-17751 ]

The TOP106 from TOPGNSS is a certified GNSS/GPS surveying antenna capable of receiving the L1/L2 bands for GPS, GLONASS, Gali...

[ [\$199.95] ]

[![Antenna Thread Adapter - 1/4in. to 5/8in.](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/4/2/7/17546-1_4in._to_5_8in._Adapter_for_5_8in._Thread-01.jpg)](https://www.sparkfun.com/antenna-thread-adapter-1-4in-to-5-8in.html)

### [Antenna Thread Adapter - 1/4in. to 5/8in.](https://www.sparkfun.com/antenna-thread-adapter-1-4in-to-5-8in.html) 

[ PRT-17546 ]

This aluminum adapter converts the very common 1/4\" thread found on camera tri-pods and mono-pods to the 5/8\" 11-TPI (threads...

[ [\$6.50] ]

[![Interface Cable - SMA Male to TNC Male (300mm)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/9/8/0/17833-Interface_Cable_-_SMA_Male_to_TNC_Male__300mm_-01.jpg)](https://www.sparkfun.com/interface-cable-sma-male-to-tnc-male-300mm.html)

### [Interface Cable - SMA Male to TNC Male (300mm)](https://www.sparkfun.com/interface-cable-sma-male-to-tnc-male-300mm.html) 

[ CAB-17833 ]

This is a 300mm long Male TNC to Male SMA cable. This is an excellent cable for connecting one of our RTK development boards ...

**Retired**

Depending on your setup you may want to use your phone for RTCM correction data. If a source is not available online, you will need a 2nd RTK Facet setup in base mode and a radio link connecting the Base to the Rover. We\'ll go into details but we designed RTK Facet to work with these 100mW 915MHz telemetry radios out of the box. You will also need an adapter cable between the Telemetry Radio and RTK Surveyor.

[![SiK Telemetry Radio V3 - 915MHz, 100mW](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/6/3/4/19032-SiK_Telemetry_Radio_V3_-_915MHz__100mW-01.jpg)](https://www.sparkfun.com/sik-telemetry-radio-v3-915mhz-100mw.html)

### [SiK Telemetry Radio V3 - 915MHz, 100mW](https://www.sparkfun.com/sik-telemetry-radio-v3-915mhz-100mw.html) 

[ WRL-19032 ]

The 915MHz SiK Telemetry Radio V3 is a lightweight and inexpensive open source radio platform that can allow for ranges of 30...

[ [\$149.95] ]

[![JST-GHR-04V to JST-GHR-06V Cable - 1.25mm pitch](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/2/2/17239-GHR-04V-S_to_GHR-06V-S_Cable_-_150mm-01.jpg)](https://www.sparkfun.com/jst-ghr-04v-to-jst-ghr-06v-cable-1-25mm-pitch.html)

### [JST-GHR-04V to JST-GHR-06V Cable - 1.25mm pitch](https://www.sparkfun.com/jst-ghr-04v-to-jst-ghr-06v-cable-1-25mm-pitch.html) 

[ CAB-17239 ]

This \~6\" cable is designed to connect our \[RTK Surveyor\](https://www.sparkfun.com/products/17369) product line to the popular...

[ [\$2.95] ]

To charge the RTK Surveyor you will need a USB C cable and a power supply. SparkFun carries a few options:

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

[![USB Wall Charger - 5V, 2A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/2/0/16893-USB_Wall_Charger_-_5V__2A-03.jpg)](https://www.sparkfun.com/usb-wall-charger-5v-2a.html)

### [USB Wall Charger - 5V, 2A](https://www.sparkfun.com/usb-wall-charger-5v-2a.html) 

[ TOL-16893 ]

This USB AC to DC power supply will do 5V at 2A!

[ [\$9.50] ]

[![USB-C Wall Adapter - 5.1V, 3A (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/4/7/16272-USB-C_Wall_Adapter_-_5.1V__3A__Black_-01.jpg)](https://www.sparkfun.com/usb-c-wall-adapter-5-1v-3a-black.html)

### [USB-C Wall Adapter - 5.1V, 3A (Black)](https://www.sparkfun.com/usb-c-wall-adapter-5-1v-3a-black.html) 

[ TOL-16272 ]

This is a USB Type-C Power Supply that is compatible with the Raspberry Pi 4.

[ [\$4.50] ]

### Suggested Reading

GNSS RTK is an incredible feat of engineering that has been made easy to use by powerful GNSS receivers such as the ZED-F9P by u-blox (the receiver inside RTK Surveyor). The process of setting up an RTK system will be covered in this tutorial but if you want to know more about RTK here are some good tutorials to brush up on:

[](https://learn.sparkfun.com/tutorials/what-is-gps-rtk)

### What is GPS RTK? 

Learn about the latest generation of GPS and GNSS receivers to get 14mm positional accuracy!

[](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox)

### Getting Started with U-Center for u-blox 

Learn the tips and tricks to use the u-blox software tool to configure your GPS receiver.

[](https://learn.sparkfun.com/tutorials/gps-rtk2-hookup-guide)

### GPS-RTK2 Hookup Guide 

Get precision down to the diameter of a dime with the new ZED-F9P from u-blox.

[](https://learn.sparkfun.com/tutorials/setting-up-a-rover-base-rtk-system)

### Setting up a Rover Base RTK System 

Getting GNSS RTCM correction data from a base to a rover is easy with a serial telemetry radio! We\'ll show you how to get your high precision RTK GNSS system setup and running.

[](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station)

### How to Build a DIY GNSS Reference Station 

Learn how to affix a GNSS antenna, use PPP to get its ECEF coordinates and then broadcast your own RTCM data over the internet and cellular using NTRIP to increase rover reception to 10km!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1463&name=SparkFun+RTK+Surveyor+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1463 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+RTK+Surveyor+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1463&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1463&t=SparkFun+RTK+Surveyor+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1463&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F4%2F6%2F3%2F17369-GPS_RTK_Surveyor_-_Enclosed-01.jpg&description=SparkFun+RTK+Surveyor+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/hardware-overview) [Hardware Overview - Advanced Features](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/hardware-overview---advanced-features) [Hardware Assembly](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/hardware-assembly) [Bluetooth and NTRIP](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/bluetooth-and-ntrip) [System Configuration](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/system-configuration) [Firmware Updates and Customization](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/firmware-updates-and-customization) [Troubleshooting](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/resources-and-going-further)

[Comments [23]](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-rtk-surveyor-hookup-guide/all) [Print]

- **Tags**
- - [Bluetooth](https://learn.sparkfun.com/tutorials/tags/bluetooth)
  - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [Enclosure](https://learn.sparkfun.com/tutorials/tags/enclosure)
  - [ESP32](https://learn.sparkfun.com/tutorials/tags/esp32)
  - [GNSS](https://learn.sparkfun.com/tutorials/tags/gnss)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [LEDs](https://learn.sparkfun.com/tutorials/tags/leds)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [Power](https://learn.sparkfun.com/tutorials/tags/power)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Satellite](https://learn.sparkfun.com/tutorials/tags/satellite)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]