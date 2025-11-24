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
