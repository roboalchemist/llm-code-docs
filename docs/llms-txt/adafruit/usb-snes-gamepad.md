# Source: https://learn.adafruit.com/usb-snes-gamepad.md

# USB SNES Gamepad

## Overview

This project tutorial will show you how you can convert a console game pad into a USB keyboard mouse for playing games on your PC. The USB game pad can be used with nearly any software, such as a MAME emulator, game, simulation software, or for custom user interfaces.![](https://cdn-learn.adafruit.com/assets/assets/000/000/373/medium800/gaming_done.jpg?1396762559)

We'll start by turning the buttons of the game pad into keyboard buttons, so that pressing 'up' is converted into the 'U' key, for example. The firmware is easily adaptable, so you can adjust it for whatever software it will be used with.

Then we'll make the project more interesting by adding an accelerometer. This will allow the game pad to be used as a mouse by tilting it!

This tutorial including the original code and Portal video is by&nbsp;[Devlin Thyne](http://thyne.net/)! Rock!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/374/medium800/gaming_usbgamepadcontents_LRG.jpg?1396762568)

## What you'll need:

You'll need the following in order to build the project:

- [Game Pad Controller](http://www.adafruit.com/products/131) - We'll be using an SNES Controller
- [Teensy](http://www.adafruit.com/products/199) - This is a very small microcontroller board that can act as a keyboard/mouse
- [Triple-axis accelerometer](http://www.adafruit.com/products/163) - We'll be using the nice ADXL335 on a breakout board. You can skip this if you're not planning to add in the mouse capability
- [USB cable with mini-b connector](http://www.adafruit.com/products/260) - to attach to the Teensy for plugging into a computer!
- Ribbon cable - for all the soldering connections. Rainbow cable is the easiest to work with as its color coded

**If you want to build the entire project, [we have a project pack in the shop with all the parts listed above!](http://www.adafruit.com/products/241)**

You'll also need some basic hand tools such as screwdrivers, wire strippers, [soldering iron](http://www.adafruit.com/products/180), [solder](http://www.adafruit.com/products/145), [diagonal cutters](http://www.adafruit.com/products/152), vise or third hand tool, etc.

[All the code is on GitHub, including some extra sketches we've written](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/master/USB_SNES_Gamepad) so be sure to look there!

- [Next Page](https://learn.adafruit.com/usb-snes-gamepad/disassemble-the-snes-controller.md)

## Featured Products

### SNES Controller

[SNES Controller](https://www.adafruit.com/product/131)
A third-party SNES (Super Nintendo/Famicom) controller. Works great with Fuzeboxen as well!

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/131)
[Related Guides to the Product](https://learn.adafruit.com/products/131/guides)
### ADXL335 - 5V ready triple-axis accelerometer (+-3g analog out)

[ADXL335 - 5V ready triple-axis accelerometer (+-3g analog out)](https://www.adafruit.com/product/163)
We've updated our favorite triple-axis accelerometer to now have an on-board 3.3V regulator - making it a perfect choice for interfacing with a 5V microcontroller such as the Arduino. This breakout comes with 3 analog outputs for X, Y and Z axis measurements on a 0.75"x0.75"...

In Stock
[Buy Now](https://www.adafruit.com/product/163)
[Related Guides to the Product](https://learn.adafruit.com/products/163/guides)
### USB cable - A/MiniB

[USB cable - A/MiniB](https://www.adafruit.com/product/260)
This here is your standard A-miniB USB cable, for USB 1.1 or 2.0. Perfect for connecting a PC to your Teensy v2, USB Lipo charger w/Mini B connector, among other things.

Approximately 3 feet / 1 meter long

Color may vary!

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/260)
[Related Guides to the Product](https://learn.adafruit.com/products/260/guides)
### Teensy (ATmega32u4 USB dev board) 2.0

[Teensy (ATmega32u4 USB dev board) 2.0](https://www.adafruit.com/product/199)
Discontinued - **you can grab** [Adafruit ItsyBitsy 32u4 - 5V 16MHz](https://www.adafruit.com/product/3677) **instead!**

The Teensy 2.0 is a complete USB-based microcontoller development system, in a very small footprint! All programming is done via the USB port. No...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/199)
[Related Guides to the Product](https://learn.adafruit.com/products/199/guides)
### Premium Female/Male 'Extension' Jumper Wires - 20 x 6"

[Premium Female/Male 'Extension' Jumper Wires - 20 x 6"](https://www.adafruit.com/product/1954)
These Female/Male Extension jumper wires are handy for making wire harnesses or jumpering between headers on PCB's. These premium jumper wires are 6" (150mm) long and come in a 'strip' of 20 (2&nbsp;pieces of each of ten rainbow colors). They have 0.1" male header...

In Stock
[Buy Now](https://www.adafruit.com/product/1954)
[Related Guides to the Product](https://learn.adafruit.com/products/1954/guides)

## Related Guides

- [Adafruit Analog Accelerometer Breakouts](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts.md)
- [HID Reporter](https://learn.adafruit.com/hid-reporter.md)
- [Gravatars: What they are and how to add or change one](https://learn.adafruit.com/gravatars-what-they-are-and-how-to-add-or-change-one.md)
- [Two Player Game System for PyGamer and RFM69HCW Radio Wing](https://learn.adafruit.com/two-player-game-system-for-pygamer-and-rfm69hcw-radio-wing.md)
- [PyPortal 2FA TOTP Authentication Friend](https://learn.adafruit.com/pyportal-2fa-totp-authentication-friend.md)
- [Dragon Drop: a CircuitPython Game for MacroPad](https://learn.adafruit.com/dragon-drop-a-circuitpython-game-for-macropad.md)
- [NeoTrellis M4 Animated Dice Roller](https://learn.adafruit.com/neotrellis-dice.md)
- [Instagram Photo Frame](https://learn.adafruit.com/instagram-photo-frame.md)
- [BlueLive: Livestream Studio switcher controller](https://learn.adafruit.com/bluelive.md)
- [DIY Turbo Button Controller - HID Remapper](https://learn.adafruit.com/diy-turbo-button-controller-hid-remapper.md)
- [ESP32 PlayStation Controller](https://learn.adafruit.com/esp32-playstation-controller.md)
- [Fruit Jam Chyron](https://learn.adafruit.com/fruit-jam-chyron.md)
- [Custom Color Palettes for MakeCode Arcade Games](https://learn.adafruit.com/custom-color-palettes-for-makecode-arcade-games.md)
- [DIY Welded Bike Stand](https://learn.adafruit.com/diy-welded-bike-stand.md)
- [CircuitPython Stage game library](https://learn.adafruit.com/circuitpython-stage-game-library.md)
