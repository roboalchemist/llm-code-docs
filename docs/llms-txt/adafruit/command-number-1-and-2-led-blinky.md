# Source: https://learn.adafruit.com/hacking-the-kinect/command-number-1-and-2-led-blinky.md

# Hacking the Kinect

## Command #1 & 2 - LED blinky!

We'll edit our python code to just send command #1 and see what happens. From our logs we know that for sending commands from host-to-device, we should use&nbsp; **bRequestType** &nbsp;of 0x40 (verify this by looking at the&nbsp; **bmRequestType** &nbsp;bits of the command packets),&nbsp; **wIndex** &nbsp;and&nbsp; **wLength** &nbsp;of zero

For command #1, set&nbsp; **bRequest** &nbsp;to 0x06 and a&nbsp; **wValue** &nbsp;to 4. The final argument is now an empty array [] to indicate no data is transmitted

```
import usb.core
import usb.util
import sys
 
# find our device
dev = usb.core.find(idVendor=0x045e, idProduct=0x02B0)
 
# was it found?
if dev is None:
    raise ValueError('Device not found')
 
# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()
 
ret = dev.ctrl_transfer(0x40, 0x6, 0x1, 0, [])
print ret
```

We ran our python code and…nothing happened!

OK well maybe that was some initialization command. Lets replace it with the next command #2, set&nbsp; **bRequest** &nbsp;to 0x06 and a&nbsp; **wValue** &nbsp;to 1

**ret = dev.ctrl\_transfer(0x40, 0x6, 0x1, 0, [])**

We ran this command and the motor didn't move but the LED stopped blinking.

For fun we ran the previous command again and the LED started blinking again.

Now we have an idea: maybe this&nbsp; **bRequest** &nbsp;0x6 controls the LED?

On your own, continue this line of thought by trying different&nbsp; **wValue** s from 0 on up to see what other&nbsp; **wValues** &nbsp;do, keep track of them all in a notebook or project file.

- [Previous Page](https://learn.adafruit.com/hacking-the-kinect/usb-analyzer.md)
- [Next Page](https://learn.adafruit.com/hacking-the-kinect/command-number-3-and-4-lets-move.md)

## Featured Products

### Hacked Kinect - Skill badge, iron-on patch

[Hacked Kinect - Skill badge, iron-on patch](https://www.adafruit.com/product/582)
You can made a cool project using the (hacked) Kinect! Adafruit offers a fun and exciting "badges" of achievement for electronics, science and engineering. We believe everyone should be able to be rewarded for learning a useful skill, a badge is just one of the many ways to show and...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/582)
[Related Guides to the Product](https://learn.adafruit.com/products/582/guides)
### Beagle USB 12 - Low/Full Speed USB Protocol Analyzer

[Beagle USB 12 - Low/Full Speed USB Protocol Analyzer](https://www.adafruit.com/product/708)
USB complexity got you down? Need a hand with enumeration? Reverse engineering a USB device? You will fall in love with the Beagle 12 USB Analyzer. This hardware analyzer is completely non-intrusive, and is much better than flaky software analyzers. Perfect for when a problem is bad enough it...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/708)
[Related Guides to the Product](https://learn.adafruit.com/products/708/guides)
### Reverse Engineer - Skill badge, Lenticular printing + pin-on

[Reverse Engineer - Skill badge, Lenticular printing + pin-on](https://www.adafruit.com/product/489)
You can reverse engineer! This is the first lenticular (two-stage image) skill badge that we know of! It says reverse engineer forwards and backwards depending on the angle you view it at!  
  
**Note:** The edges of the badge will appear "white" at an angle,...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/489)
[Related Guides to the Product](https://learn.adafruit.com/products/489/guides)
### Reverse Engineer - Sticker!

[Reverse Engineer - Sticker!](https://www.adafruit.com/product/673)
You can reverse engineer! Adafruit offers&nbsp;fun and exciting stickers to celebrate achievement for electronics, science and engineering. We believe everyone should be able to be rewarded for learning a useful skill and&nbsp;a sticker is just one of the many ways to show and share.  
<br...></br...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/673)
[Related Guides to the Product](https://learn.adafruit.com/products/673/guides)

## Related Guides

- [USB SNES Gamepad](https://learn.adafruit.com/usb-snes-gamepad.md)
- [Ikea Vindriktning Hack with QT Py ESP32-S3 and Adafruit IO](https://learn.adafruit.com/ikea-vindriktning-hack-with-qt-py-esp32-s3-and-adafruit-io.md)
- [Reverse Engineering a Bluetooth Low Energy Light Bulb](https://learn.adafruit.com/reverse-engineering-a-bluetooth-low-energy-light-bulb.md)
- [LED Drone Matrix](https://learn.adafruit.com/led-matrix-drone.md)
- [Fruit Jam Chyron](https://learn.adafruit.com/fruit-jam-chyron.md)
- [Run an X-Carve CNC Machine Wirelessly with a Raspberry Pi](https://learn.adafruit.com/control-an-xcarve-cnc-machine-wirelessly-with-a-raspberry-pi.md)
- [Meowsic Cat Piano Line Out](https://learn.adafruit.com/meowsic-line-out.md)
- [Use Apple HomeKit Devices with itsaSNAP and Adafruit IO](https://learn.adafruit.com/use-apple-homekit-devices-with-itsasnap.md)
- [Instagram Photo Frame](https://learn.adafruit.com/instagram-photo-frame.md)
- [HID Reporter](https://learn.adafruit.com/hid-reporter.md)
- [Modifying Servos for Continuous Rotation](https://learn.adafruit.com/modifying-servos-for-continuous-rotation.md)
- [Fruit Jam Sega Genesis](https://learn.adafruit.com/fruit-jam-sega-genesis.md)
- [Walkmellotron: Cassette Player Mods](https://learn.adafruit.com/walkmellotron.md)
- [DIY USB Cable Aviation Connector Retro-Fit](https://learn.adafruit.com/aviation-connector-diy-usb-cables.md)
- [Feather Guitar Hero Adapter](https://learn.adafruit.com/feather-guitar-hero-adapter.md)
