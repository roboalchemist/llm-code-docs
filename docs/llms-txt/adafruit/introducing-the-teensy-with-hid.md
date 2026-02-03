# Source: https://learn.adafruit.com/usb-snes-gamepad/introducing-the-teensy-with-hid.md

# USB SNES Gamepad

## Introducing the Teensy with HID

So you may be wondering "heck, I should just grab an Arduino!" But a 'proper' Arduino can't do what we want, which is to appear as a keyboard. When you plug in an Arduino into your USB port, it shows up as a Serial device, which is fantastic for debugging or for interfacing to Processing. To listen to a Serial device, you need to open up Hyperterm or Zterm or the Arduino IDE's serial monitor. However, it does not act as actual&nbsp;_keyboard&nbsp;_where what it outputs goes to Microsoft Word or a video game.![](https://cdn-learn.adafruit.com/assets/assets/000/000/386/medium800/gaming_devicemanager.jpg?1396762655)

 **The Arduino is a USB serial port - it appears under Ports here, not under Keyboards!**  
  
For that, we need a different kind of chip, a chip that is_&nbsp;USB native!_&nbsp;USB native chips can act as USB serial ports, but they can also act as MIDI devices, keyboards, mice, audio devices, joysticks, etc. Nearly anything! A nice chip that does all this is the ATmega32U4 (the U is for usb!) .

The&nbsp;[Teensy](https://www.adafruit.com/product/199)&nbsp;2.0 is basically this chip, a USB connector, button and some other necessary things. It's very tiny (thus the name) and&nbsp;[has a fantastic programming interface that is basically the Arduino + a helper, it runs under Mac, Linux or Windows](http://pjrc.com/teensy/teensyduino.html "Link: http://pjrc.com/teensy/teensyduino.html").

Since this tutorial was written, a number of other 32U4 microcontroller boards have been developed including the large Arduino Leonardo and the smaller&nbsp;[Adafruit ItsyBitsy 32u4 - 5V 16MHz](https://www.adafruit.com/product/3677),&nbsp;[Adafruit ItsyBitsy 32u4 - 3V 8MHz](https://www.adafruit.com/product/3675), and&nbsp;[Adafruit Feather 32u4 Basic Proto](https://www.adafruit.com/product/2771), which can do similar things.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/387/medium800/gaming_teensyparts.jpg?1396762660)

- [Previous Page](https://learn.adafruit.com/usb-snes-gamepad/disassemble-the-snes-controller.md)
- [Next Page](https://learn.adafruit.com/usb-snes-gamepad/assemble-the-usb-snes-gamepad.md)

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
