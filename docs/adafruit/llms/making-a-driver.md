# Source: https://learn.adafruit.com/hacking-the-kinect/making-a-driver.md

# Hacking the Kinect

## Making a Driver

OK so back to our motor. We are ready to start sending data to it via the Control endpoint. For Mac and Linux type computers, a driver isn't necessary to send or receive data directly via USB.

For windows, however, there must be some sort of driver to 'grab' the device for us. Usually drivers are complex and have like, interfaces that plug into the operating system. Like the cameras would show up as a camera device, the microphones as an audio device. We're not quite ready for a detailed driver, what we'll do is make a 'shell driver' which has no operating system capabilities but does let us send commands to it from software.

Again, Mac/Linux people have this built into the&nbsp;OS&nbsp;kernel so skip this part if you don't use windows.

For our shell, we'll use&nbsp; **libusb** &nbsp;a USB library, which is available for windows as&nbsp;**[libusb-win32](http://sourceforge.net/projects/libusb-win32/)&nbsp;**go there and download it.

We'll run the&nbsp; **inf-wizard** &nbsp;(which will make our driver shell)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/069/medium800/gaming_libusbinfwiz.gif?1447974367)

The important part is entering in the matching VID and PID we found before.![](https://cdn-learn.adafruit.com/assets/assets/000/000/070/medium800/gaming_infdeets.gif?1447974378)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/071/medium800/gaming_infgenerated.gif?1447974387)

Now when you plug in the Kinect, it will attach itself the the LibUSB-win32 device driver.![](https://cdn-learn.adafruit.com/assets/assets/000/000/072/medium800/gaming_motordevice.gif?1447974396)

We didn't make matching drivers for the audio or camera so those are still driver-less.- [Previous Page](https://learn.adafruit.com/hacking-the-kinect/determine-the-descriptors.md)
- [Next Page](https://learn.adafruit.com/hacking-the-kinect/installing-python-and-pyusb.md)

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

- [Guitar Hero MIDI Controller](https://learn.adafruit.com/guitar-hero-midi-controller.md)
- [Commodore 64 - The Most Popular Retro Computer of All Time](https://learn.adafruit.com/commodore-64-retro-guide.md)
- [Use Docker to Compile Linux for ESP32-S3](https://learn.adafruit.com/docker-esp32-s3-linux.md)
- [Feather Guitar Hero Adapter](https://learn.adafruit.com/feather-guitar-hero-adapter.md)
- [BLE Cat Thermal Printer with MEMENTO](https://learn.adafruit.com/ble-cat-thermal-printer-with-memento.md)
- [Fruit Jam Mac Emulator](https://learn.adafruit.com/fruit-jam-mac-emulator.md)
- [How to Make Animated Graphics for Hologram Displays](https://learn.adafruit.com/how-to-make-animated-graphics-for-hologram-displays.md)
- [LED Matrix Wall Arcade for Pico-8](https://learn.adafruit.com/led-matrix-wall-arcade.md)
- [Run an X-Carve CNC Machine Wirelessly with a Raspberry Pi](https://learn.adafruit.com/control-an-xcarve-cnc-machine-wirelessly-with-a-raspberry-pi.md)
- [CircuitPython 2FA TOTP Authentication Friend](https://learn.adafruit.com/circuitpython-totp-otp-2fa-authy-authenticator-friend.md)
- [Flippy Floppy Drive Modification](https://learn.adafruit.com/flippy-floppy-drive-modification.md)
- [Authoring Playground Books with Bluefruit for iOS ](https://learn.adafruit.com/create-a-swift-playgroundbook-with-bluetooth-le.md)
- [SerenityOS - The dream of the '90s is alive!](https://learn.adafruit.com/serenityos-build-and-run-keep-the-90s-dream-alive.md)
- [Stand-alone programming AVRs using CircuitPython](https://learn.adafruit.com/stand-alone-programming-avrs-using-circuitpython.md)
- [Protect Your Online Accounts with Strong Passwords & Password Managers](https://learn.adafruit.com/protect-your-social-media-online-accounts-with-a-strong-password-manager.md)
