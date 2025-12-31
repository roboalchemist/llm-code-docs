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
