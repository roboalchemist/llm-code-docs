# Source: https://learn.adafruit.com/usb-snes-gamepad/programming-the-teensy.md

# USB SNES Gamepad

## Programming the Teensy

The Teensy uses the USB connection for programing, so we don't need a seperate AVR programmer. We will use the Teensyduino IDE, which is a patch to the Arduino IDE.

If you don't have it yet,&nbsp;[download & install the Arduino IDE software](http://www.arduino.cc/)

Next,&nbsp;[download the Teensyduino installer for your OS and run it, patching the Arduino IDE](http://pjrc.com/teensy/td_download.html "Link: http://pjrc.com/teensy/td\_download.html")

Finally, be sure to also grab[&nbsp;Teensyloader](http://pjrc.com/teensy/loader.html)&nbsp;which is a helper that talks to the Teensy for you.

## One Button Test

We'll start with the 'one button test' sketch, which will only listen for the 'Up' D-Pad button and output the letter 'u'

Understanding this code now will make it a lot easier to understand the later sketches that are much more complex!

[You can also grab this code (which may be updated!) at GitHub](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/master/USB_SNES_Gamepad/teensySNES_onebutton/teensySNES_onebutton.ino)

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/USB_SNES_Gamepad/teensySNES_onebutton/teensySNES_onebutton.ino

Now we'll upload this sketch to the Teensy. Make a new sketch and copy the code in. Select the&nbsp;**Teensy 2.0 (USB Keyboard/Mouse)**&nbsp;item from the Board menu.![](https://cdn-learn.adafruit.com/assets/assets/000/000/409/medium800/gaming_boardmenuteensy.gif?1447975498)

Make sure the Loader is running, if you see this:![](https://cdn-learn.adafruit.com/assets/assets/000/000/410/medium800/gaming_prebutton.gif?1447975508)

Press the tiny button to start the bootloader, so that it looks like this:![](https://cdn-learn.adafruit.com/assets/assets/000/000/411/medium800/gaming_postbutton.gif?1447975520)

Upload the sketch! You should see it sucessfully program the Teensy, and reboot. The OS will then alert you that it found an HID device.![](https://cdn-learn.adafruit.com/assets/assets/000/000/412/medium800/gaming_foundHID.gif?1447975530)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/413/medium800/gaming_keymouse.gif?1447975539)

And the device manager will now have an extra Keyboard and Mouse called&nbsp; **"HID Keyboard Device"** &nbsp;and&nbsp; **"HID-compliant mouse"** ![](https://cdn-learn.adafruit.com/assets/assets/000/000/414/medium800/gaming_teensydevmanager.gif?1447975551)

You should now be able to open up a text editor and carefully push the 'up' D-pad to generate 'u's!## All Button Test

Next we can upload the sketch that uses&nbsp;_all&nbsp;_the buttons so you can test each connection. It is much longer. [Download it from GitHub](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/master/USB_SNES_Gamepad/teensySNES_test1/teensySNES_test1.ino).

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/USB_SNES_Gamepad/teensySNES_test1/teensySNES_test1.ino

![](https://cdn-learn.adafruit.com/assets/assets/000/000/415/medium800/gaming_notepad.gif?1447975560)

You should test all the buttons, to make sure they all output characters.

This code is more involved since it has to listen to 12 buttons. You can see at the top where we define an array of all the buttons, and then the keys that correspond to the presses. In this case, we're using a simple one-to-one correspondence for keypresses, such as Up being 'u'. To adapt this code to allow for things like "Alt-F3" would be a little more complex.

The code supports up to 6 simultaneous keypresses.

- [Previous Page](https://learn.adafruit.com/usb-snes-gamepad/assemble-the-usb-snes-gamepad.md)
- [Next Page](https://learn.adafruit.com/usb-snes-gamepad/adding-the-accelerometer.md)

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
