# Source: https://learn.adafruit.com/chumby-hacker-board.md

# Chumby Hacker Board

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/002/350/medium800/microcomputers_chumbyhackerboard_1.0_lrg.jpeg?1396782173)

This page is a collection of mini-tutorials on doing stuff with the Chumby Hacker Board (for brevity we will refer to it as the CHB)! The CHB is a cool single board Linux computer that has much of the same hardware as the famous [Chumby One](http://www.chumby.com/). It's great for people who are experienced with Linux and want to have the power of a microcomputer with audio and video output while at the same time getting all the peripherals of a microcontroller such as analog-to-digital conversion, PWM outputs, sensors, bit twiddling, and broken-out GPIOs!  
  
While we believe that the CHB is a fairly easy-to-use Single Board Computer (SBC) having a pre-installed OS on the included uSD card, and ready drivers for the peripherals, its not designed for beginners! The board is best used by those with previous Linux experience: the good news is you don't have to have another Linux computer to set up the CHB but you should have familiarity with shells and shell scripting, gcc, make, dmesg, etc. We also suggest having had some poking around with microcontrollers such as BASIC Stamp, Arduino, AVR, PIC, 8051, etc. So that when we say "i2c" and "not 5v tolerant I/Os" you can follow along.  
  
**The CHB is not in any way officially supported by [Chumby Industries](http://www.chumby.com/)! Chumby has generously offered a [Forum](http://forum.chumby.com/viewforum.php?id=20) and [Wiki](http://wiki.chumby.com/mediawiki/index.php/Chumby_hacker_board) where they will try to share information but there is absolutely no tech support or guarantee that the CHB will meet your project needs. Please do not contact Chumby directly either by email or phone for help with your CHB. If you have questions, please post to their forums to receive help from others and the occasional assistance from a CHB developer.**  
  
Want to pick one up? [We have Chumby Hacker Boards and accessories in stock at the adafruit shop!](http://www.adafruit.com/index.php?main_page=index&cPath=46)

## Hardware Specs

- [Freescale iMX.233 processor](http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=i.MX233) running at 454 MHz
- 64 MB&nbsp;onboard RAM
- **Comes with 512&nbsp;MB uSD card with 100 MB Linux installation all ready to go**
- 3.3V I/O pins can talk to most sensors, motor drivers, etc. No struggling with 1.8V levels.
- Low power, fanless ARM926 core draws only 200-300 mA
- Onboard GL850G USB hub draws 100-200mA
- Built-in Lithium Ion/Polymer battery charger and 5V boost converter for portable projects
- **Three** USB port jacks!
- 1.5W mono 4-16 ohm speaker amplifier (0.1" JST onboard connector)
- Microphone input (0.05" JST onboard connector)
- LCD controller with 2mm output port
- 3.5mm A/V output jack with stereo audio and NTSC/PAL composite video
- Back of board has GPIO outputs on 0.1" header spacing, plug in an Arduino proto shield (Beta version only, Final boards don't have this)
- Quadrature encoder connections onboard
- 5-way joystick on-board
- MMA7455 3-axis +-2G to +-8G accelerometer on-board
- 3.3V TTL serial port for easy shell access
- Full GCC toolchain is ready for you to download and get crackin'!

## Mini Tutorials

- [Power supplies](http://learn.adafruit.com/chumby-hacker-board/power "Link: http://learn.adafruit.com/chumby-hacker-board/power") - How to power your Chumby Hacker board!
- [Serial port](http://learn.adafruit.com/chumby-hacker-board/connecting-with-ttl-serial "Link: http://learn.adafruit.com/chumby-hacker-board/connecting-with-ttl-serial") - How to connect to the serial terminal port for shell access
- [Compiler](http://learn.adafruit.com/chumby-hacker-board/compiler "Link: http://learn.adafruit.com/chumby-hacker-board/compiler") - Installing the Falconwing GCC toolchain
- [Accessing i2c](http://learn.adafruit.com/chumby-hacker-board/i2c-sensor "Link: http://learn.adafruit.com/chumby-hacker-board/i2c-sensor") - Connecting to i2c chips including the on-board accelerometer!
- [WiFi networking](http://learn.adafruit.com/chumby-hacker-board/wifi) - Getting to the Internet via wireless 802.11b/g (in progress)
- [Stand-Alone WiFi AP and SSH](http://www.ladyada.net/wiki/stand-alone_wifi_ap_and_ssh "Link: http://www.ladyada.net/wiki/stand-alone\_wifi\_ap\_and\_ssh") - Turn your CHB into a stand-alone DHCP server
- [Ethernet networking](http://learn.adafruit.com/chumby-hacker-board/ethernet) - Getting to the Internet via wired Ethernet
- [Audio](http://learn.adafruit.com/chumby-hacker-board/audio) - Playing audio through the headphone/AV jack and onboard 2W speaker amp
- [microSD](http://learn.adafruit.com/chumby-hacker-board/sd-card) - Cloning, copying and expanding the space on the card (in progress)
- [VGA](http://www.ladyada.net/wiki/chumbyhackerboard/vga) - VGA video out (totally in progress!)
- [EC2 instance for building full, from-scratch images of their own for the hacker board](http://wiki.chumby.com/index.php/Quickstarting_OE "Link: http://wiki.chumby.com/index.php/Quickstarting\_OE") - Thanks Chumby!

More info may be found at the official [Chumby Hacker Board Wiki](http://wiki.chumby.com/mediawiki/index.php/Chumby_hacker_board_beta)

## Pictures!
Click for large photos of the v1.0 PCBs  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/351/medium800/microcomputers_chumbyhackerboardfront_1.0_lrg.jpeg?1396782177)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/352/medium800/microcomputers_chumbyhackerboardback_1.0_lrg.jpeg?1396782184)

Click for large photos of the beta PCBs![](https://cdn-learn.adafruit.com/assets/assets/000/002/353/medium800/microcomputers_chumbyhackerboardfrontbig.jpeg?1396782192)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/354/medium800/microcomputers_chumbyhackerboardbackbig.jpeg?1396782200)

- [Next Page](https://learn.adafruit.com/chumby-hacker-board/power.md)

## Featured Products

### USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply

[USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply](https://www.adafruit.com/product/961)
Add lots more USB capability to your Raspberry Pi or computer using this powered USB 2.0 hub. It adds a full **seven powered ports** , all at USB 2.0 speeds so you can use video cameras and other high speed devices (cheaper hubs are v1.1 and not as fast!)  
  
The extra sauce...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/961)
[Related Guides to the Product](https://learn.adafruit.com/products/961/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### 2.1mm to 1.7mm DC jack adapter

[2.1mm to 1.7mm DC jack adapter](https://www.adafruit.com/product/411)
We're carrying this adapter primarily to allow Chumby Hacker Board users to adapt our nice [5V @ 2A power supply](http://www.adafruit.com/products/276) to their CHB. But you can use this adapter for anything else that has a 1.7mm DC jack, such as a PSP.

In Stock
[Buy Now](https://www.adafruit.com/product/411)
[Related Guides to the Product](https://learn.adafruit.com/products/411/guides)
### USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC

[USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC](https://www.adafruit.com/product/939)
This is the cutest little microSD card reader/writer - but don't be fooled by its adorableness! It's wicked fast and supports up to 64 GB SDXC cards! Simply slide the card into the edge and plug it into your computer. No drivers are required, it shows up as a standard 'Mass...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/939)
[Related Guides to the Product](https://learn.adafruit.com/products/939/guides)
### Ethernet Cable - 10 ft long

[Ethernet Cable - 10 ft long](https://www.adafruit.com/product/730)
We have so many Internet-connected goodies in the shop, we figured it's time to carry a cable so you can easily connect them up! This cable is 10 feet long, black and has all 8 wires installed. Perfect for use with the [BeagleBone](http://www.adafruit.com/products/513), <a...></a...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/730)
[Related Guides to the Product](https://learn.adafruit.com/products/730/guides)
### USB to TTL Serial Cable - Debug / Console Cable for Raspberry Pi

[USB to TTL Serial Cable - Debug / Console Cable for Raspberry Pi](https://www.adafruit.com/product/954)
The cable is easiest way ever to connect to your microcontroller/Raspberry Pi/WiFi router serial console port. Inside the big USB plug is a USB\<-\>Serial conversion chip and at the end of the 36" cable are four wire - red power, black ground, white RX into USB port, and green TX out...

In Stock
[Buy Now](https://www.adafruit.com/product/954)
[Related Guides to the Product](https://learn.adafruit.com/products/954/guides)
### FTDI Serial TTL-232 USB Cable

[FTDI Serial TTL-232 USB Cable](https://www.adafruit.com/product/70)
Just about all electronics use TTL serial for debugging, bootloading, programming, serial output, etc. But it's rare for a computer to have a serial port anymore. This is a USB to TTL serial cable, with a FTDI FT232RL usb/serial chip embedded in the head. It has a 6-pin socket at the end...

In Stock
[Buy Now](https://www.adafruit.com/product/70)
[Related Guides to the Product](https://learn.adafruit.com/products/70/guides)

## Related Guides

- [CircuitPython Libraries on MicroPython using the Raspberry Pi Pico](https://learn.adafruit.com/circuitpython-libraries-on-micropython-using-the-raspberry-pi-pico.md)
- [Hallowing Minotaur Maze](https://learn.adafruit.com/hallowing-minotaur-maze.md)
- [Raspberry Pi Azure IoT Hub Dashboard with CircuitPython](https://learn.adafruit.com/raspberry-pi-iot-dashboard-with-azure-and-circuitpython.md)
- [Adafruit 2.9" eInk Display Breakouts and FeatherWings](https://learn.adafruit.com/adafruit-2-9-eink-display-breakouts-and-featherwings.md)
- [Pi SSD Media Server](https://learn.adafruit.com/pi-ssd-media-server.md)
- [Creating Slideshows in CircuitPython](https://learn.adafruit.com/creating-slideshows-in-circuitpython.md)
- [Network Interface Failover using FONA](https://learn.adafruit.com/network-interface-failover-using-fona.md)
- [Matrix Keypad](https://learn.adafruit.com/matrix-keypad.md)
- [Native MP3 decoding on Arduino](https://learn.adafruit.com/native-mp3-decoding-on-arduino.md)
- [Raspberry Pi HQ Camera Case](https://learn.adafruit.com/raspberry-pi-hq-camera-case.md)
- [Articulated Pi Display V2 Mount](https://learn.adafruit.com/pi-wall-mount.md)
- [World's Smallest MAME Arcade Cabinet](https://learn.adafruit.com/worlds-smallest-mame-arcade-cabinet.md)
- [Raspberry Pi E-Ink Weather Station using Python](https://learn.adafruit.com/raspberry-pi-e-ink-weather-station-using-python.md)
- [Getting Started with Raspberry Pi Pico and CircuitPython](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython.md)
- [Adafruit QT Py and NeoPixel LEDs](https://learn.adafruit.com/qt-py-and-neopixel-leds.md)
