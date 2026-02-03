# Source: https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi.md

# Adafruit NFC/RFID on Raspberry Pi

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/001/535/medium800/raspberry_pi_MifareCardRead_600w.jpg?1396773159)

Interested in adding some NFC (near-field communication) fun and excitement to your Raspberry Pi? You're in luck!   
  
A big advantage of Linux is that it includes a large number of software “stacks” developed by the open source community, and you get to take advantage of all that hard work simply by using or installing the right library.   
  
NFC is no exception here, with [_libnfc_](https://github.com/nfc-tools/libnfc) having been around for a quite some time—in fact, it's the original reason the NFC Breakout was developed!&nbsp;libnfc is a library for **C programmers**. For Python and CircuitPython, there’s [an equivalent module](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/python-circuitpython).  
  
To get libnfc playing well with your Pi and your Adafruit NFC breakout you'll need to make some minor configuration changes to the system and install some code, but it's pretty painless, and this tutorial will show you everything you need to do to start writing your own NFC-enabled apps on the Pi!

**This guide assumes you have some version of Raspberry Pi OS already running, that the system is network-connected and so forth.&nbsp;We have [a series of tutorials for first-time users](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi/overview) if you need some help with those steps.**

- [Next Page](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/pi-serial-port.md)

## Featured Products

### 13.56MHz RFID/NFC tag assortment - Classic 1K

[13.56MHz RFID/NFC tag assortment - Classic 1K](https://www.adafruit.com/product/365)
One of each of our favorite 13.56MHz RFID/NFC Classic 1K tags - 5 in total!

- [Credit card size](http://www.adafruit.com/products/359)
- [1" diameter 'laundry' clear tag](http://www.adafruit.com/products/361)
- <a...></a...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/365)
[Related Guides to the Product](https://learn.adafruit.com/products/365/guides)
### 13.56MHz RFID/NFC Clear Keychain Fob - Classic 1K

[13.56MHz RFID/NFC Clear Keychain Fob - Classic 1K](https://www.adafruit.com/product/363)
This is a blank 13.56MHz RFID/NFC keychain fob - often used for keys but also an easy way to tag something. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be read by almost any 13.56MHz...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/363)
[Related Guides to the Product](https://learn.adafruit.com/products/363/guides)
### 13.56MHz RFID/NFC Bracelet - Classic 1K

[13.56MHz RFID/NFC Bracelet - Classic 1K](https://www.adafruit.com/product/921)
This is a blank 13.56MHz RFID/NFC silicone bracelet. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be read by almost any 13.56MHz RFID/NFC reader but make sure it can handle&nbsp;ISO/IEC...

In Stock
[Buy Now](https://www.adafruit.com/product/921)
[Related Guides to the Product](https://learn.adafruit.com/products/921/guides)
### 13.56MHz RFID/NFC Charm - Classic 1K

[13.56MHz RFID/NFC Charm - Classic 1K](https://www.adafruit.com/product/884)
This is a blank 13.56MHz RFID/NFC embedded in a phone charm&nbsp;- often used for train/bus passes but also found in other systems where a proximity card is desired. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/884)
[Related Guides to the Product](https://learn.adafruit.com/products/884/guides)
### 13.56MHz RFID/NFC Clear Tag - Classic 1K

[13.56MHz RFID/NFC Clear Tag - Classic 1K](https://www.adafruit.com/product/361)
This is a blank 13.56MHz Classic 'laundry' tag - often used for laundry or identification but also found in other systems where a small proximity card is desired. This one is clear! &nbsp;The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer...

Out of Stock
[Buy Now](https://www.adafruit.com/product/361)
[Related Guides to the Product](https://learn.adafruit.com/products/361/guides)
### 13.56MHz RFID/NFC White Tag - Classic 1K

[13.56MHz RFID/NFC White Tag - Classic 1K](https://www.adafruit.com/product/360)
This is a blank 13.56MHz RFID/NFC laundry tag&nbsp;- often used for laundry but also general tagging. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be read by almost any 13.56MHz RFID/NFC...

In Stock
[Buy Now](https://www.adafruit.com/product/360)
[Related Guides to the Product](https://learn.adafruit.com/products/360/guides)
### 13.56MHz RFID/NFC Card - Classic 1K

[13.56MHz RFID/NFC Card - Classic 1K](https://www.adafruit.com/product/359)
This is a blank 13.56MHz RFID/NFC card - often used for train/bus passes but also found in other systems where a proximity card is desired. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be...

In Stock
[Buy Now](https://www.adafruit.com/product/359)
[Related Guides to the Product](https://learn.adafruit.com/products/359/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)

## Related Guides

- [I2C Addresses and Troublesome Chips](https://learn.adafruit.com/i2c-addresses.md)
- [Collin's Lab: RFID](https://learn.adafruit.com/collins-lab-rfid.md)
- [Mystery Box: Remote Chess Board Puzzle Lock](https://learn.adafruit.com/mystery-box-remote-chess-board-puzzle-lock.md)
- [Raspberry Pi NFC Minecraft Blocks](https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks.md)
- [NFC Raspberry Pi Media Player](https://learn.adafruit.com/nfc-raspberry-pi-media-player.md)
- [Adafruit PN532 RFID/NFC Breakout and Shield](https://learn.adafruit.com/adafruit-pn532-rfid-nfc.md)
- [Adafruit's Raspberry Pi Lesson 9. Controlling a DC Motor](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-9-controlling-a-dc-motor.md)
- [Adafruit's Raspberry Pi Lesson 5. Using a Console Cable](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable.md)
- [Pi Box](https://learn.adafruit.com/pi-box.md)
- [Piezo Ring Tones with Raspberry Pi](https://learn.adafruit.com/piezo-ring-tones-with-raspberry-pi.md)
- [Cloud Cam: Internet-Connected Security Camera](https://learn.adafruit.com/cloud-cam-connected-raspberry-pi-security-camera.md)
- [Set up and Blink - MATLAB and Simulink with Raspberry Pi](https://learn.adafruit.com/how-to-use-matlab-and-simulink-with-raspberry-pi.md)
- [Battery Powered Raspberry Pi Displays w/RaspiRobot Shield](https://learn.adafruit.com/raspirobot-battery-powered-raspberry-pi-displays.md)
- [Adafruit's Raspberry Pi Lesson 13. Power Control](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-13-power-control.md)
- [Raspberry Pi Thermal Printer One Time Pads](https://learn.adafruit.com/raspberry-pi-thermal-printer-one-time-pads.md)
