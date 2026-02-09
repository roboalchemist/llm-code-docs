# Source: https://learn.adafruit.com/usb-snes-gamepad/adding-the-accelerometer.md

# USB SNES Gamepad

## Adding the Accelerometer

Now we will add in the accelerometer to create a tilt-activated mouse. Nearly any accelerometer will do, but the easiest to use is an analog output one. The ADXL335 will work great. First we will power the chip by providing 3.3V (not 5.0V) and ground from the Teensy, then connect the three analog outputs (X Y and Z) to three analog inputs. Finally, we will add Mouse'ing code to the sketch so that Mouse movement events are sent when the controller is tilted.Cut a piece of ribbon cable down, we'll use Brown for Ground, Red for +3V, then Orange Yellow and Green for X Y and Z respectively.![gaming_adxlstrip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/416/medium640/gaming_adxlstrip.jpg?1396762869)

We tore the brown wire off so that it wouldnt be twisted.![gaming_adxlwires_t.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/417/medium640/gaming_adxlwires_t.jpg?1396762875)

The ADXL335 requires 3V power, so don't connect it to VCC (5V) instead, we'll use the 3V that the teensy provides - it uses that voltage for the USB communication, you can't draw more than maybe 20-40mA which is plenty for this but not enough for perhaps a bunch of LEDs! Brown connects to the second GND pin.![gaming_adxlpower.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/418/medium640/gaming_adxlpower.jpg?1396762880)

Next connect X Y and Z to F5, F4 and F1 (don't use F0!)![gaming_adxlxyz.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/419/medium640/gaming_adxlxyz.jpg?1396762888)

You should now try out the next sketch,&nbsp;**[teensySNES\_test2.ino](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/master/USB_SNES_Gamepad/teensySNES_test2/teensySNES_test2.ino)**&nbsp;which will move the mouse as you tilt the controller.

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/USB_SNES_Gamepad/teensySNES_test2/teensySNES_test2.ino

- [Previous Page](https://learn.adafruit.com/usb-snes-gamepad/programming-the-teensy.md)
- [Next Page](https://learn.adafruit.com/usb-snes-gamepad/closing-it-up.md)

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
