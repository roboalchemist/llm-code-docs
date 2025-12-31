# Source: https://learn.adafruit.com/pi-wifi-radio.md

# Raspberry Pi WiFi Radio

## Overview

### **PLEASE NOTE:** this guide is now&nbsp; **deprecated** …

- It relied on some _extremely_ finicky software (_pianobar_ and _libav_) which tended to break with each new operating system release…it’s a minor miracle we’ve even managed to patch it this far along!
- It relied on several now-deprecated Python libraries for the display (Adafruit\_CharLCDPlate, Adafruit\_I2C, etc.).
- It’s specific to the _Pandora_ streaming service, which is only available in the United States and a couple other countries.

That being said, if you’re in the US, already have the hardware sitting around and don’t mind sinking 30 minutes into a project that might not pan out, by all means give it a shot. It was pretty nifty when it worked.&nbsp;Please just understand that we will **no longer be providing technical support** for this project **nor any more updates** to this guide.&nbsp;It was last seen working with the&nbsp;2018-11-13 release of Raspbian Stretch Lite, if that’s any help in recreating the project.

There are other Pi audio guides available in the Adafruit Learning System that might serve you better nowadays:

- [Raspberry Pi Zero NPR One Radio](https://learn.adafruit.com/raspberry-pi-zero-npr-one-radio)
- [Raspberry Pi radio player with touchscreen](https://learn.adafruit.com/raspberry-pi-radio-player-with-touchscreen)
- [_Boomy_ Pi Airplay Boombox](https://learn.adafruit.com/boomy-pi-airplay)

![](https://cdn-learn.adafruit.com/assets/assets/000/007/372/medium800/raspberry_pi_piphi1.jpg?1396850566)

Raspberry Pi, the little _wonder-puter_ that’s taken the world by storm, is so affordable that we can create nifty single-purpose “appliances” around them without shame. Here’s our take on one of the more popular such applications: internet streaming media, the **_Pandora_** music service specifically.

_Pandora is now limited to users in the United States. It is **no longer available in other countries**.&nbsp;This guide is now deprecated and will **not** be updated for alternate services._

http://www.youtube.com/watch?v=uzUruw2Ppyk

With the addition of a small LCD, a few buttons and a USB wireless network adapter, the Raspberry Pi becomes an affordable self-contained music streamer that can be moved to any room of the house…wherever you need your tunes at the moment. Just connect power and speakers or headphones.

- [Next Page](https://learn.adafruit.com/pi-wifi-radio/parts-list.md)

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
