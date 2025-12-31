# Source: https://learn.adafruit.com/adafruit-ultimate-gps.md

# Adafruit Ultimate GPS

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/031/842/medium800/gps_746_topkit.jpg?1461187930)

We carry a few different GPS modules here in the Adafruit shop, but none that satisfied our every desire - that's why we designed this little GPS breakout board. We believe this is the **Ultimate** GPS module, so we named it that. It's got everything you want and more:

- -165 dBm sensitivity, 10 Hz updates, 66 channels
- 5V friendly design and only 20mA current draw
- Breadboard friendly + two mounting holes
- RTC battery-compatible
- Built-in datalogging
- PPS output on fix
- Internal patch antenna + u.FL connector for external active antenna
- Fix status LED

Primary: Note there are two versions of the breakout board: one to wire to projects via serial lines & read from a microcontroller (#746) and one meant to connect to a USB cable to an appropriate computer (#4279) which is not programmable in Arduino. Be sure you find the directions for the version you are interested in.

The breakout is built around the MTK3339 chipset, a no-nonsense, high-quality GPS module that can track up to 22 satellites on 66 channels, has an excellent high-sensitivity receiver (-165 dB tracking!), and a built in antenna. It can do up to 10 location updates a second for high speed, high sensitivity logging or tracking. Power usage is incredibly low, only 20 mA during navigation.

![](https://cdn-learn.adafruit.com/assets/assets/000/031/843/medium800/gps_746_iso.jpg?1461187948)

## Ultimate GPS Breakout Board

**The Breadboard Breakout board comes with:** a ultra-low dropout 3.3V regulator so you can power it with 3.3-5VDC in, 5V level safe inputs, ENABLE pin so you can turn off the module using any microcontroller pin or switch, a footprint for optional CR1220 coin cell to keep the RTC running and allow warm starts and a tiny bright red LED. The LED blinks at about 1Hz while it's searching for satellites and blinks once every 15 seconds when a fix is found to conserve power. If you want to have an LED on all the time, we also provide the FIX signal out on a pin so you can put an external LED on.

## Ultimate GPS USB Board

**The USB Breakout board comes with:** 4-pin USB breakout for direct-soldering or connection to a USB host, two yellow receive/transmit LEDs let you know when data is being transmitted to or from the GPS module serial interface, a footprint for optional CR1220 coin cell to keep the RTC running and allow warm starts and a tiny bright red LED. The LED blinks at about 1Hz while it's searching for satellites and blinks once every 15 seconds when a fix is found to conserve power. If you want to have an LED on all the time, we also provide the FIX signal out on a pin so you can put an external LED on.

![](https://cdn-learn.adafruit.com/assets/assets/000/076/816/medium800/adafruit_products_4279_top_ORIG_2019_06.jpg?1560221463 Ultimate GPS USB Micro B board)

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/109/808/medium800/adafruit_products_UGPS_USB_C.jpg?1647550249 Ultimate GPS USB-C board)

## Antenna Usage
![](https://cdn-learn.adafruit.com/assets/assets/000/031/844/medium800/gps_746_demo.jpg?1461187956)

Two features that really stand out about version 3 MTK3339-based module is the external antenna functionality and the the built in data-logging capability. The module has a standard ceramic patch antenna that gives it -165 dB sensitivity, but when you want to have a bigger antenna, you can snap on any 3V active GPS antenna via the uFL connector. The module will automatically detect the active antenna and switch over! [Most GPS antennas use SMA connectors so you may want to pick up one of our uFL to SMA adapters.](http://www.adafruit.com/products/851 "Link: http://www.adafruit.com/products/851")   
  
The other cool feature of the new MTK3339-based module (which we have tested with great success) is the built in datalogging ability. Since there is a microcontroller inside the module, with some empty FLASH memory, the newest firmware now allows sending commands to do internal logging to that FLASH. The only thing is that you do need to have a microcontroller send the "Start Logging" command. However, after that message is sent, the microcontroller can go to sleep and does not need to wake up to talk to the GPS anymore to reduce power consumption. The time, date, longitude, latitude, and height is logged every 15 seconds and only when there is a fix. The internal FLASH can store about 16 hours of data, it will automatically append data so you don't have to worry about accidentally losing data if power is lost. It is not possible to change what is logged and how often, as its hardcoded into the module but we found that this arrangement covers many of the most common GPS datalogging requirements.

## [Pick one up today at the Adafruit shop!](http://www.adafruit.com/products/746 "Link: http://www.adafruit.com/products/746")
## Specifications:

Module specs:

- Satellites: 22 tracking, 66 searching
- Patch Antenna Size: 15mm x 15mm x 4mm
- Update rate: 1 to 10 Hz
- Position Accuracy: 1.8 meters
- Velocity Accuracy: 0.1 meters/s
- Warm/cold start: 34 seconds
- Acquisition sensitivity: -145 dBm
- Tracking sensitivity: -165 dBm
- Maximum Velocity: 515m/s
- Vin range: 3.0-5.5VDC
- MTK3339 Operating current: 25mA tracking, 20 mA current draw during navigation
- Output: NMEA 0183, 9600 baud default
- DGPS/WAAS/EGNOS supported
- FCC E911 compliance and AGPS support (Offline mode : EPO valid up to 14 days )
- Up to 210 PRN channels
- Jammer detection and reduction
- Multi-path detection and compensation

Breakout board details:

- Weight (not including coin cell or holder): 8.5g
- Dimensions (not including coin cell or holder): 25.5mm x 35mm x 6.5mm / 1.0" x 1.35" x 0.25"

If you purchased a module before March 26th, 2012 and it says MTK3329 on the silkscreen, you have the PA6B version of this breakout with the MT3329 chipset. The MTK3329 does not have built in datalogging. If your module has sharpie marker crossing out the MTK3329 text or there is no text, you have a PA6C MTK3339 with datalogging ability. If you have the version with "v3" next to the name, you have the PA6H which has PPS output and external-antenna support.

This tutorial assumes you have a '3339 type module.

- [Next Page](https://learn.adafruit.com/adafruit-ultimate-gps/pinouts.md)

## Featured Products

### Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates

[Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates](https://www.adafruit.com/product/746)
We carry a few different GPS modules here in the Adafruit shop, but none that satisfied our every desire - that's why we designed this little GPS breakout board. We believe this is the **Ultimate** GPS module, so we named it that. It's got everything you want and...

In Stock
[Buy Now](https://www.adafruit.com/product/746)
[Related Guides to the Product](https://learn.adafruit.com/products/746/guides)
### Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates

[Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates](https://www.adafruit.com/product/4279)
The Ultimate GPS module you know and love has a _glow-up_ to let it be easily used with any computer, not just microcontrollers! With the built-in USB-to-Serial converter, you can now plug-n-play the Ultimate GPS into your computer, laptop, embedded Linux computer, and more. Power and...

In Stock
[Buy Now](https://www.adafruit.com/product/4279)
[Related Guides to the Product](https://learn.adafruit.com/products/4279/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA

[GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA](https://www.adafruit.com/product/960)
Give your Ultimate GPS V3 a boost with this external active antenna. This GPS antenna draws about 10mA and will give you an additional 28 dB of gain. It's got a 5 meter long cable so it will easily reach wherever you need it to. The antenna is magnetic so it will stick to the top of a car...

In Stock
[Buy Now](https://www.adafruit.com/product/960)
[Related Guides to the Product](https://learn.adafruit.com/products/960/guides)
### SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable

[SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable](https://www.adafruit.com/product/851)
This RF adapter cable is super handy for anyone doing RF work. Often times, small electronics save space by having a pick-and-placeable u.FL connector (also called uFL, IPEX, IPAX, IPX, MHF, and AM). But most antennas have SMA or RP-SMA connectors on them. This little cable will bridge the...

In Stock
[Buy Now](https://www.adafruit.com/product/851)
[Related Guides to the Product](https://learn.adafruit.com/products/851/guides)
### CR1220 12mm Diameter - 3V Lithium Coin Cell Battery

[CR1220 12mm Diameter - 3V Lithium Coin Cell Battery](https://www.adafruit.com/product/380)
These are the highest quality & capacity batteries, the same as shipped with the iCufflinks,&nbsp;iNecklace, Datalogging and GPS Shields, GPS HAT, etc. One battery per order (you'll want one battery per cufflink or pendant.)  
  
Brand may vary but all battery brands are verified...

In Stock
[Buy Now](https://www.adafruit.com/product/380)
[Related Guides to the Product](https://learn.adafruit.com/products/380/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [2.8" TFT Touch Shield](https://learn.adafruit.com/2-8-tft-touch-shield.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [CircuitPython Libraries on Linux and the 96Boards DragonBoard 410c](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-96boards-dragonboard-410c.md)
- [Arduino Lesson 3. RGB LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [Adafruit VS1053 MP3/AAC/Ogg/MIDI/WAV Codec Breakout Tutorial](https://learn.adafruit.com/adafruit-vs1053-mp3-aac-ogg-midi-wav-play-and-record-codec-tutorial.md)
- [CircuitPython Libraries on Linux and the NVIDIA Jetson Nano](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-nvidia-jetson-nano.md)
- [Adafruit Optical Fingerprint Sensor](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor.md)
- [FTDI Friend](https://learn.adafruit.com/ftdi-friend.md)
- [IR Sensor](https://learn.adafruit.com/ir-sensor.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [A REST API for Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/a-rest-api-for-arduino-and-the-cc3000-wifi-chip.md)
- [Adafruit Proto Screw Shield](https://learn.adafruit.com/adafruit-proto-screw-shield.md)
