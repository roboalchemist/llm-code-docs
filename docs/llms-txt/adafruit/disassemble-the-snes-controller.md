# Source: https://learn.adafruit.com/usb-snes-gamepad/disassemble-the-snes-controller.md

# USB SNES Gamepad

## Disassemble the SNES Controller

We'll begin by disassembling the SNES controller.![gaming_snes.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/378/medium640/gaming_snes.jpg?1396762599)

There are 5 small phillips screws on the back. Once you lift the back off, you can remove the PCB. Be careful as there are tiny wires for the 'side' buttons so just make sure those pieces come out cleanly.![gaming_snesopen.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/379/medium640/gaming_snesopen.jpg?1396762604)

![gaming_snesopened.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/380/medium640/gaming_snesopened.jpg?1396762609)

Each button is made of 3 parts - theres the plastic part that you press, beneath that is the&nbsp;_elastomer_&nbsp;which is a rubber molded piece with a conductive bit that goes underneath the plastic part, and finally on the PCB there are two interdigitated and exposed traces. When the user presses the plastic button, it pushes down on the elastomer which then pushes the conductive rubber onto both traces, shorting them.

There is also a black blob in the middle. This blob is a chip that takes all the button inputs and then converts it into the way that the SNES wants to hear. Thats all fine, but we dont want to use the blob because we are going to make our own custom chip software. (Note that it would be pretty easy to make the Teensy 'talk' right to the blob using the SNES protocol but then you wouldn't be able to adapt this tutorial to other controllers, for that reason we're going to do it the 'hard way')

The question is now how can we listen to all the buttons?

![gaming_pcbout.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/381/medium640/gaming_pcbout.jpg?1396762619)

Well, luckily, almost all game pads are going to use a similar method for arranging the buttons. If you note carefully at the PCB, you'll see that each button is made of two traces, but that all of the buttons&nbsp;_share_&nbsp;one trace together.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/384/medium800/gaming_groundtrace.jpg?1396762635)

This is the&nbsp;_common_&nbsp;(ground) trace. If we were to make a schematic, it would look kinda like this:![](https://cdn-learn.adafruit.com/assets/assets/000/000/385/medium800/gaming_snes.png?1396762649)

 **Note that this is really just a symbolic schematic, the ground wire doesn't necessarily connect on the side thats indicated, we're just showing how all the buttons have a common ground pin!**

OK now this is straight forward,&nbsp;[if you are not sure how to read buttons with a microcontroller, we have a nice tutorial you might want to check out](http://www.ladyada.net/learn/arduino/lesson5.html)&nbsp;(in fact, we really suggest it as we'll be referring to concepts in that tutorial) Basically each button connects to an input of the microcontroller. We'll need a pull-up resistor, but luckily we can set the microcontroller's&nbsp;_internal_&nbsp;pullups (so we dont have to solder in 12 10K resistors!) Then the microcontroller can listen on each pin for a button press and when it is received, generate a keypress event.

- [Previous Page](https://learn.adafruit.com/usb-snes-gamepad/overview.md)
- [Next Page](https://learn.adafruit.com/usb-snes-gamepad/introducing-the-teensy-with-hid.md)

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
