# Source: https://learn.adafruit.com/electroknit.md

# Electro-knit

## Overview

http://www.youtube.com/watch?v=GhnTSWMMtdU

The video above overviews the process which is detailed in this tutorial. Go from a digital image like this:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/747/medium800/braincrafts_adazoomed.gif?1447976396)

To a knitted object like this!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/748/medium800/braincrafts_adafabric.jpg?1396765521)

Working with these machines is very difficult. Before you begin, look at your life, and what choices brought you to this point. Are you proficient at using the knitting machine's normal functions? Can you read and run Python scripts? Have you ever done any serial communication between your computer and another device before? If you answered "no" to any of these questions, work on these skills first before attempting to follow this guide.  
  
Adventures in communicating with the Brother KH-930e knitting machine! The order of operations:

- [Make the FTDI interface cable](http://learn.adafruit.com/electroknit/cable)
- [Prepare the computer by downloading the software](http://learn.adafruit.com/electroknit/software)
- [Backup your Brother Knitting Machine's memory to your computer](http://learn.adafruit.com/electroknit/backup "Link: http://learn.adafruit.com/electroknit/backup")
- [View patterns from the machine's memory](http://learn.adafruit.com/electroknit/view)
- [Adding a new pattern from an image](http://learn.adafruit.com/electroknit/insert)
- [Load your new file back to the knitting machine](http://learn.adafruit.com/electroknit/upload "Link: http://learn.adafruit.com/electroknit/upload")

Much of this tutorial is directly adapted from [Steve Conklin's totally awesome knitting machine wiki page](http://www.antitronics.com/wiki/index.php?title=Electroknit_Technical_Information "Link: http://www.antitronics.com/wiki/index.php?title=Electroknit\_Technical\_Information")!&nbsp;

**Troubleshooting**

- If the RAM data has been corrupted, the screen will flash "888" and the machine will seem unresponsive. Hold down INPUT and STEP at the same time, and when the display should change. Perform a memory reset by hitting CE, 888, STEP.

**Outside resources**

- download the [PDF knitting machine manual](http://knittsings.com/knitting-machine-manuals/) (many other knitting machine manuals here as well)
- [Troubleshooting Brother machines](http://www.softbyte.co.uk/brothl1.htm#Troubleshooting%20Uploading%20and%20Downloading%20with%20Brother%20KH940,%20KH950i,%20KH965i,%20KH970) - includes how to do an 888 reset of memory
- [Good forum post](http://www.howtomendit.com/answers.php?id=124420) - includes what to do when all the machine will do is flash "888"
- [Newton's Yarns](http://www.newtons.com/brother_knitking.htm) - in Anaheim, CA, claims to carry Brother machines/accessories incl. KE-100 motor drive

- [Next Page](https://learn.adafruit.com/electroknit/cable.md)

## Featured Products

### FTDI Serial TTL-232 USB Cable

[FTDI Serial TTL-232 USB Cable](https://www.adafruit.com/product/70)
Just about all electronics use TTL serial for debugging, bootloading, programming, serial output, etc. But it's rare for a computer to have a serial port anymore. This is a USB to TTL serial cable, with a FTDI FT232RL usb/serial chip embedded in the head. It has a 6-pin socket at the end...

In Stock
[Buy Now](https://www.adafruit.com/product/70)
[Related Guides to the Product](https://learn.adafruit.com/products/70/guides)

## Related Guides

- [Firework Ignitor](https://learn.adafruit.com/electric-ignitor.md)
- [Fruit Jam Chyron](https://learn.adafruit.com/fruit-jam-chyron.md)
- [Walkmellotron: Cassette Player Mods](https://learn.adafruit.com/walkmellotron.md)
- [Build your own BeBox and run BeOS using Virtualbox](https://learn.adafruit.com/build-a-bebox-with-beos-and-virtualbox.md)
- [BLE Sniffer with nRF52840](https://learn.adafruit.com/ble-sniffer-with-nrf52840.md)
- [Commodore 64 - The Most Popular Retro Computer of All Time](https://learn.adafruit.com/commodore-64-retro-guide.md)
- [Modifying Servos for Continuous Rotation](https://learn.adafruit.com/modifying-servos-for-continuous-rotation.md)
- [Convert your Model M Keyboard to Bluetooth with Bluefruit EZ-Key HID](https://learn.adafruit.com/convert-your-model-m-keyboard-to-bluetooth-with-bluefruit-ez-key-hid.md)
- [PlayStation Spinner Controller](https://learn.adafruit.com/playstation-spinner-controller.md)
- [Pico Four Keypad](https://learn.adafruit.com/pico-four-key-macropad.md)
- [BlueLive: Livestream Studio switcher controller](https://learn.adafruit.com/bluelive.md)
- [Compiling a cross-compiler on Windows](https://learn.adafruit.com/compiling-a-cross-compiler-on-windows.md)
- [Open Source Protective Face Shield Designs](https://learn.adafruit.com/open-source-face-shield-designs.md)
- [Android Smart Home Mirror](https://learn.adafruit.com/android-smart-home-mirror.md)
- [Fog Machine with Motion Sensor and Adafruit IO](https://learn.adafruit.com/fog-machine-remote-trigger.md)
