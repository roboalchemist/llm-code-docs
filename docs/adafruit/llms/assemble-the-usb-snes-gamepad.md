# Source: https://learn.adafruit.com/usb-snes-gamepad/assemble-the-usb-snes-gamepad.md

# USB SNES Gamepad

## Assemble the Gamepad

OK we're basically ready to go. The plan is to solder a single Ground wire to the common ground for all the buttons, then solder a seperate wire to each button (the not-ground side). The ground connects to the Teensy ground, the button wires connect to all the solder pads down the side. Then we'll write the code that listens to the button presses and converts them.

Cut off a strip of ribbon cable, about 4" long. Use diagonal cutters or fingernails to carefully nip and 'rip' the individual wires apart about 1" and then strip the ends and tin them with solder. Do this for both sides.![gaming_strip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/388/medium640/gaming_strip.jpg?1396762669)

I made this cable about 1" too long initially, but its always easy to make the cable&nbsp;_shorter_!![gaming_striptin.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/389/medium640/gaming_striptin.jpg?1396762675)

To connect to ground, we'll expose a little copper in the top left corner, this way we don't have the wire running underneath the elastomer.![gaming_scrape.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/390/medium640/gaming_scrape.jpg?1396762682)

![gaming_scraped.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/391/medium640/gaming_scraped.jpg?1396762689)

Solder the Black wire to the ground plane, we brought the wire through a hole.![gaming_groundsolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/392/medium640/gaming_groundsolder.jpg?1396762695)

![gaming_groundsoldered.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/393/medium640/gaming_groundsoldered.jpg?1396762705)

OK lets solder to the first button. The key is to remember to NOT solder to the same common pad but to the&nbsp;_opposite_&nbsp;pad! Solder the white wire to the 'up' button. There's almost always a hole you can feed the wire through!![gaming_up.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/395/medium640/gaming_up.jpg?1396762721)

Solder the gray wire to the Right pad, the purple wire to the Down pad and the blue wire to the Left pad.![gaming_dpad.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/396/medium640/gaming_dpad.jpg?1396762726)

From the back.![gaming_dpadback.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/397/medium640/gaming_dpadback.jpg?1396762733)

Then the orange wire goes to the L1 button, the yellow goes to Start and the green to Select.![gaming_startsel.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/398/medium640/gaming_startsel.jpg?1396762741)

![gaming_startselback.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/399/medium640/gaming_startselback.jpg?1396762748)

I didnt end up using the Red or Brown wires so I tore those off the ribbon. Now cut another piece the same size but with only the white, gray, purple, blue and green wires.

Connect white to B, gray to A, purple to X, blue to Y and green to R1.

![gaming_allbutton.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/401/medium640/gaming_allbutton.jpg?1396762756)

![gaming_allback.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/402/medium640/gaming_allback.jpg?1396762758)

If you haven't yet, now is a good time to desolder the SNES connector cable. We wont have space for it so just pull each wire as you heat the solder joint (or just cut them short, either way).![gaming_removecable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/403/medium640/gaming_removecable.jpg?1396762766)

OK! Now all the buttons are wired up, its time to attach them to the Teensy. Place the Teensy in a vise or carefully use a 'third hand' to hold it (grab by the USB connector).

First, solder the black wire to the ground pin.

![gaming_teensygnd.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/404/medium640/gaming_teensygnd.jpg?1396762770)

Next start soldering in all the ribbon cable wires, one after the other, without skipping any holes.![gaming_teensydpad.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/405/medium640/gaming_teensydpad.jpg?1396762778)

After the first ribbon cable, go to the second piece, starting with the white wire. The last green wire goes next to the blue one on the 'short' side.![gaming_teensybuttons.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/406/medium640/gaming_teensybuttons.jpg?1396762785)

![gaming_teensybuttons2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/407/medium640/gaming_teensybuttons2.jpg?1396762791)

Now we are ready to upload code to the Teensy and test out our work!![gaming_teensyusb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/408/medium640/gaming_teensyusb.jpg?1396762799)

- [Previous Page](https://learn.adafruit.com/usb-snes-gamepad/introducing-the-teensy-with-hid.md)
- [Next Page](https://learn.adafruit.com/usb-snes-gamepad/programming-the-teensy.md)

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
