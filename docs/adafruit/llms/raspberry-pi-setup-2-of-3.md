# Source: https://learn.adafruit.com/pi-wifi-radio/raspberry-pi-setup-2-of-3.md

# Raspberry Pi WiFi Radio

## Install Software Packages

Danger: 

Further configuration of the Raspberry Pi will take place over the network using SSH, not the keyboard and mouse.

- The SSH server should already be enabled on the Raspberry Pi — this was done during the initial raspi-config setup.
- On Mac or Linux systems, you can use a Terminal or xterm window.
- For Windows systems, you can [download PuTTY](http://www.putty.org).

The terminal command to access the system would be:  
  
**ssh pi@pandora.local** (or whatever hostname was configured) if using Netatalk

or:

**ssh pi@192.168.0.42** (or whatever the system’s actual numeric IP address is)  
  
You’ll be prompted for a password — use the password that you set up in&nbsp;raspi-config, or “raspberry” if you left the default. Additionally, the first time connecting you may be prompted regarding a host key for security…enter Y (or click Yes) when prompted.

## Update Installed Software
Once logged in, type the following at the command prompt:

```
sudo apt-get update
```

This updates the list of available software packages, and takes a couple of minutes (just do the “update,” _not_ “upgrade” — the latter can sometimes take _hours!_)

## Install Prerequisite Software
Several prerequisite software packages need to be installed, using&nbsp;different techniques.

First is a collection of code libraries, using the apt-get package manager:

```
sudo apt-get install git i2c-tools python-pexpect python-smbus libavfilter-dev libavformat-dev libcurl4-gnutls-dev libgcrypt-dev libjson-c-dev libao-dev
```

This takes a little while; there’s about 100 megabytes of stuff to download and install.

Now&nbsp;use _git_&nbsp;and _wget_ to install the rest. There’s our LCD radio UI, then a collection of Adafruit libraries for Raspberry Pi, and finally&nbsp; **pianobar** , a terminal-based Pandora client for Raspberry Pi. _Do not_ use the apt-get version of this, it’s out of date!

```
cd
git clone -b legacy https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
git clone https://github.com/adafruit/Python-WiFi-Radio
wget https://github.com/PromyLOPh/pianobar/archive/e945578ab22912049f1e547ce7b25b01089f7590.zip
unzip e945578ab22912049f1e547ce7b25b01089f7590.zip
```

 **Note the “-b legacy” on the first “git clone” line.** It’s required there. But _not_ on anything else.

Now some configuration…

First, link some of the Adafruit&nbsp;libraries into the radio software directory:

```
cd Python-WiFi-Radio
ln -s ../Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate/*.py .
```

(Note: there’s a space before the last period above. Don’t miss it. Copy and paste this exact line, if possible.)

Next, we’ll compile pianobar from source code:

```
cd ../pianobar-e945578ab22912049f1e547ce7b25b01089f7590
make
```

You might get a long list of compiler warnings. That’s fine, as long as the build _finishes._ Compiler _errors,_ on the other hand, will stop&nbsp;the build process. You might be missing a library from the apt-get sequence above, or something in the software may have changed since these instructions were written, in which case post in the [Adafruit Forums](https://forums.adafruit.com)&nbsp;for assistance.

Once compiled, install using:

```
sudo cp pianobar /usr/local/bin
```

Don’t worry about configuring this software yet; we’ll proceed there later. Just&nbsp;use the steps above to&nbsp;get it installed for now.

- [Previous Page](https://learn.adafruit.com/pi-wifi-radio/raspberry-pi-setup-1-of-3.md)
- [Next Page](https://learn.adafruit.com/pi-wifi-radio/raspberry-pi-setup-3-of-3.md)

## Featured Products

### Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM

[Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM](https://www.adafruit.com/product/3775)
The Raspberry Pi 3 Model B is the most popular Raspberry Pi computer made, and the Pi Foundation knows you can always make a good thing _better_! And what could make the Pi 3 better? How about a&nbsp;_faster_ processor, 5 GHz WiFi, and updated Ethernet chip with PoE capability?...

In Stock
[Buy Now](https://www.adafruit.com/product/3775)
[Related Guides to the Product](https://learn.adafruit.com/products/3775/guides)
### SD/MicroSD Memory Card (8 GB SDHC)

[SD/MicroSD Memory Card (8 GB SDHC)](https://www.adafruit.com/product/1294)
Add mega-storage in a jiffy using this 8 GB class 4 micro-SD card. It comes with a SD adapter so you can use it with any of our shields or adapters. Preformatted to FAT so it works out of the box with our projects. Tested and works great with our <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/1294)
[Related Guides to the Product](https://learn.adafruit.com/products/1294/guides)
### 5V 2.5A Switching Power Supply with 20AWG MicroUSB Cable

[5V 2.5A Switching Power Supply with 20AWG MicroUSB Cable](https://www.adafruit.com/product/1995)
Our all-in-one 5V 2.5 Amp + MicroUSB cable power adapter is the perfect choice for powering single-board computers like Raspberry Pi, BeagleBone, or anything else that's power-hungry!

This adapter was specifically designed to provide 5.25V, not 5V, but we still call it a 5V USB...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1995)
[Related Guides to the Product](https://learn.adafruit.com/products/1995/guides)
### Adafruit RGB Positive 16x2 LCD+Keypad Kit for Raspberry Pi

[Adafruit RGB Positive 16x2 LCD+Keypad Kit for Raspberry Pi](https://www.adafruit.com/product/1109)
This new Adafruit Pi Plate makes it easy to use an RGB 16x2 Character LCD. We really like the RGB Character LCDs we stock in the shop. (For RGB we have [RGB negative](http://www.adafruit.com/products/399) and [RGB positive](http://www.adafruit.com/products/398).)...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1109)
[Related Guides to the Product](https://learn.adafruit.com/products/1109/guides)
### Adafruit RGB Negative 16x2 LCD+Keypad Kit for Raspberry Pi

[Adafruit RGB Negative 16x2 LCD+Keypad Kit for Raspberry Pi](https://www.adafruit.com/product/1110)
This new Adafruit Pi Plate makes it easy to use an RGB 16x2 Character LCD. We really like the RGB Character LCDs we stock in the shop. (For RGB we have [RGB negative](http://www.adafruit.com/products/399) and [RGB positive](http://www.adafruit.com/products/398).)...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1110)
[Related Guides to the Product](https://learn.adafruit.com/products/1110/guides)
### Adafruit Blue&White 16x2 LCD+Keypad Kit for Raspberry Pi

[Adafruit Blue&White 16x2 LCD+Keypad Kit for Raspberry Pi](https://www.adafruit.com/product/1115)
This new Adafruit Pi Plate makes it easy to use a blue and white 16x2 Character LCD. [We really like the 16x2 Character LCDs we stock in the shop](http://www.adafruit.com/products/181). Unfortunately, these LCDs do require quite a few digital pins, 6 to control the LCD and then...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1115)
[Related Guides to the Product](https://learn.adafruit.com/products/1115/guides)
### Adafruit Raspberry Pi B+ / Pi 2 / Pi 3 Case - Smoke Base

[Adafruit Raspberry Pi B+ / Pi 2 / Pi 3 Case - Smoke Base](https://www.adafruit.com/product/2258)
It took awhile to perfect&nbsp;-&nbsp;but that's okay&nbsp;since we can now safely say that the Adafruit case for Raspberry Pi Model B+ / Pi 2 / Pi 3&nbsp;is The Single&nbsp;Greatest Raspberry Pi Model B+ Case Ever.

This enclosure&nbsp;was designed by Mike Doell - just like our...

In Stock
[Buy Now](https://www.adafruit.com/product/2258)
[Related Guides to the Product](https://learn.adafruit.com/products/2258/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)

## Related Guides

- [Adafruit Class Library for Windows IoT Core](https://learn.adafruit.com/adafruit-class-library-for-windows-iot-core.md)
- [Character LCD with Raspberry Pi or BeagleBone Black](https://learn.adafruit.com/character-lcd-with-raspberry-pi-or-beaglebone-black.md)
- [Adafruit 16x2 Character LCD + Keypad for Raspberry Pi](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi.md)
- [Onion Pi](https://learn.adafruit.com/onion-pi.md)
- [Monitor Your Home With the Raspberry Pi B+](https://learn.adafruit.com/monitor-your-home-with-the-raspberry-pi-b-plus.md)
- [Pi Hole Ad Detection Display with PiTFT](https://learn.adafruit.com/pi-hole-ad-pitft-tft-detection-display.md)
- [Introducing the Raspberry Pi 2 - Model B](https://learn.adafruit.com/introducing-the-raspberry-pi-2-model-b.md)
- [Setting up a Raspberry Pi as a WiFi Access Point](https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Adafruit RGB Matrix + Real Time Clock HAT for Raspberry Pi](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi.md)
- [Raspberry Pi as an Ad Blocking Access Point](https://learn.adafruit.com/raspberry-pi-as-an-ad-blocking-access-point.md)
- [Internet of Things Printer for Raspberry Pi](https://learn.adafruit.com/pi-thermal-printer.md)
- [Adafruit Prototyping Pi Plate](https://learn.adafruit.com/adafruit-prototyping-pi-plate.md)
- [Node.js Embedded Development on the Raspberry Pi](https://learn.adafruit.com/node-embedded-development.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
