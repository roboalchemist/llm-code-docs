# Source: https://learn.adafruit.com/force-sensitive-resistor-fsr/overview.md

# Source: https://learn.adafruit.com/usb-snes-gamepad/overview.md

# Source: https://learn.adafruit.com/thermocouple/overview.md

# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/overview.md

# Source: https://learn.adafruit.com/smt-manufacturing/overview.md

# Source: https://learn.adafruit.com/adafruit-led-backpack/overview.md

# Source: https://learn.adafruit.com/beaglebone/overview.md

# Source: https://learn.adafruit.com/hacking-the-kinect/overview.md

# Source: https://learn.adafruit.com/el-wire/overview.md

# Source: https://learn.adafruit.com/ttl-serial-camera/overview.md

# Source: https://learn.adafruit.com/thermocouple/overview.md

# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/overview.md

# Source: https://learn.adafruit.com/smt-manufacturing/overview.md

# Source: https://learn.adafruit.com/adafruit-led-backpack/overview.md

# Source: https://learn.adafruit.com/beaglebone/overview.md

# Source: https://learn.adafruit.com/hacking-the-kinect/overview.md

# Source: https://learn.adafruit.com/el-wire/overview.md

# Source: https://learn.adafruit.com/ttl-serial-camera/overview.md

# Source: https://learn.adafruit.com/usb-snes-gamepad/overview.md

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
- [BLE Sniffer with nRF52840](https://learn.adafruit.com/ble-sniffer-with-nrf52840.md)
- [Personal and Portable ESP32-S2 Web Server](https://learn.adafruit.com/wordle-personal-esp32-s2-web-server.md)
- [NeoTrellis Light Painting](https://learn.adafruit.com/neotrellis-light-painting.md)
- [Cheekmate - a Wireless Haptic Communication System](https://learn.adafruit.com/cheekmate-wireless-haptic-communication.md)
- [Dimmable Li-Ion Halogen Bike Light](https://learn.adafruit.com/dimmable-li-ion-halogen-bike-light.md)
- [Getting Started with Braille Output for CircuitPython REPL](https://learn.adafruit.com/getting-started-braille-output-circuitpython-repl.md)
- [NeoPixel Arcade Buttons](https://learn.adafruit.com/neopixel-arcade-button.md)
- [Link's 3D Printed Wooden Sword](https://learn.adafruit.com/links-3d-printed-wooden-sword.md)
- [Fruit Jam Sega Genesis](https://learn.adafruit.com/fruit-jam-sega-genesis.md)
- [Build your own NeXT with a virtual machine](https://learn.adafruit.com/build-your-own-next-with-a-virtual-machine.md)
- [LED Matrix Wall Arcade for Pico-8](https://learn.adafruit.com/led-matrix-wall-arcade.md)
- [Adafruit USB Host FeatherWing with MAX3421E](https://learn.adafruit.com/adafruit-usb-host-featherwing-with-max3421e.md)
- [Flippy Floppy Drive Modification](https://learn.adafruit.com/flippy-floppy-drive-modification.md)
- [DIY Bluetooth Gamepad](https://learn.adafruit.com/diy-bluetooth-gamepad.md)
