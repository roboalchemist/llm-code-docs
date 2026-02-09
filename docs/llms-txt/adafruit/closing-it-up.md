# Source: https://learn.adafruit.com/usb-snes-gamepad/closing-it-up.md

# USB SNES Gamepad

## Closing it Up

Now that the mouse and keyboard are working, we can close up the game pad. This is actually the toughest part of the project, as the enclosure has plastic standoffs that are in the way.One thing that will help is 'deribboning' the ribbon cable, so that it is easy to push around the wires.![gaming_deribbon.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/420/medium640/gaming_deribbon.jpg?1396762895)

Use sticky foam tape or hot glue to place the Teensy right at the top.![gaming_sticky1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/421/medium640/gaming_sticky1.jpg?1396762902)

Likewise, align the acellerometer so that it is as shown (otherwise you may have some flipped axes. You should put it near the middle but we didn't see any difference being in this location.![gaming_adxlstick.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/422/medium640/gaming_adxlstick.jpg?1396762908)

Finally, twist the USB cable so that it goes through the strain relief posts. If this makes it really tough to close you can probably skip it and just be careful not to yank!![gaming_cabletwist.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/423/medium640/gaming_cabletwist.jpg?1396762916)

As you close the case, use tweezers to poke the wires around inside so that they do not interfere with the standoffs.

We wanted to make sure we could update the code without going through the disassembly process, so we drilled a hole in the back right over where the button is, then used a paper clip to push the tiny button. You can also just solder two wires to GND and RST and bring these out of the case, when shorted it will start the bootloader.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/424/medium800/gaming_resethole.jpg?1396762921)

You're done! Enjoy your new toy, and modify the sketch if you need to change the key commands or mouse movements.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/425/medium800/gaming_done.jpg?1396762927)

- [Previous Page](https://learn.adafruit.com/usb-snes-gamepad/adding-the-accelerometer.md)

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
