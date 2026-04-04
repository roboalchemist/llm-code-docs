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

- [Open Source Protective Face Shield Designs](https://learn.adafruit.com/open-source-face-shield-designs.md)
- [Pico Bluetooth Keyboard Bridge](https://learn.adafruit.com/pico-bluetooth-keyboard-bridge.md)
- [Dimmable Li-Ion Halogen Bike Light](https://learn.adafruit.com/dimmable-li-ion-halogen-bike-light.md)
- [Installing IronOS on an MHP30 Mini Hot Plate (DEPRECATED)](https://learn.adafruit.com/installing-ironos-on-a-mhp30-mini-hotplate.md)
- [Getting Started with Braille Output for CircuitPython REPL](https://learn.adafruit.com/getting-started-braille-output-circuitpython-repl.md)
- [Meowsic Cat Piano Line Out](https://learn.adafruit.com/meowsic-line-out.md)
- [Instagram Photo Frame](https://learn.adafruit.com/instagram-photo-frame.md)
- [ESP32 PlayStation Controller](https://learn.adafruit.com/esp32-playstation-controller.md)
- [NeoPIO: Drive lots of LEDs with Raspberry Pi Pico](https://learn.adafruit.com/neopio-drive-lots-of-leds-with-raspberry-pi-pico.md)
- [Ikea Vindriktning Hack with QT Py ESP32-S3 and Adafruit IO](https://learn.adafruit.com/ikea-vindriktning-hack-with-qt-py-esp32-s3-and-adafruit-io.md)
- [See N Say Brain Transplant](https://learn.adafruit.com/see-n-say-brain-transplant.md)
- [DIY Welded Bike Stand](https://learn.adafruit.com/diy-welded-bike-stand.md)
- [Setting up an Open Speech Recording Website](https://learn.adafruit.com/setting-up-an-open-speech-recording-website.md)
- [Authoring Playground Books with Bluefruit for iOS ](https://learn.adafruit.com/create-a-swift-playgroundbook-with-bluetooth-le.md)
- [Adafruit Feather RP2040 with USB Type A Host](https://learn.adafruit.com/adafruit-feather-rp2040-with-usb-type-a-host.md)
