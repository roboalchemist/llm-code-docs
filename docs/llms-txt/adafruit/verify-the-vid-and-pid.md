# Source: https://learn.adafruit.com/hacking-the-kinect/verify-the-vid-and-pid.md

# Hacking the Kinect

## Verify the VID & PID

The first place to start is to see what devices and "interfaces" or "configurations" are available for the USB device. The nicest way to do this is to use&nbsp; **lsusb** &nbsp;(Linux) or&nbsp; **system\_profiler** &nbsp;(Mac) which is a "list usb" program available for Linux and mac. Sadly, it does not exist for windows, so find a mac or linux computer or friend, you'll only need it for a minute! [[edit: a reader has notified us that [http://www.nirsoft.net/utils/usb\_devices\_view.html](http://www.nirsoft.net/utils/usb_devices_view.html) may do the trick!]]

For linux, run&nbsp; **lsusb -vv** &nbsp;(ultra verbose) for Mac, run&nbsp; **system\_profiler SPUSBDataType**

![](https://cdn-learn.adafruit.com/assets/assets/000/000/259/medium800/gaming_system_profiler.jpg?1396761558)

There's a bunch more stuff like USB keys and such installed but this is a good starting point. Note that the Kinect is actually 4 USB devices - a hub, a camera, a microphone (audio) and a motor. The hub is just an easy way for the device to combine three separate chips into a single cable. We'll be investigating the&nbsp; **Xbox NUI Motor** &nbsp;since its the simplest. Note the&nbsp; **Vendor ID = 0x045e** &nbsp;and&nbsp; **Product ID = 0x2b0.&nbsp;** Every type USB device must have a unique VID and PID. The VID is the manufacturer. In this case,&nbsp; **0x045e** &nbsp;is the VID for Microsoft. All Microsoft products will have that VID. Each product has a different PID, so all Kinect Motors use PID&nbsp; **0x02b0** &nbsp;this doesn't differ between two Kinects, they'll both have the same PID. The VID/PID are used as a way to have the proper driver find the product. Its a lot better than serial COM ports because COM ports change names but VID/PID are burned into the device firmware.- [Previous Page](https://learn.adafruit.com/hacking-the-kinect/overview.md)
- [Next Page](https://learn.adafruit.com/hacking-the-kinect/determine-the-descriptors.md)

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
