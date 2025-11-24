# Source: https://learn.adafruit.com/hacking-the-kinect/bonus-accelerometer.md

# Hacking the Kinect

## Bonus Accelerometer!

We're going to go back and revisit the mysterious Read command 0x32 that we fuzzed with for a bit. Its also in the logs, be sure to set your filter to show both Host-to-Device and Device-to-Host since its a 'read' not a 'write'![](https://cdn-learn.adafruit.com/assets/assets/000/000/094/medium800/gaming_readpacket.gif?1447974566)

We were pretty close with our commands, it looks like we should be reading only 10 bytes. It also looks like the data doesn't really change much except for a bit further down…![](https://cdn-learn.adafruit.com/assets/assets/000/000/095/medium800/gaming_datachange.gif?1447974577)

The 7'th byte changes a lot right after we send it that&nbsp; **bRequest** &nbsp;0x31 (motor movement). That implies that this data read is somehow affected by the motor, possibly a motor feedback byte?

[Checking out a tear-down of the device (from iFixit)](http://www.ifixit.com/Teardown/Microsoft-Kinect-Teardown/4066/2)&nbsp;we see that&nbsp;[there is an 'inclinometer'/accelerometer](http://www.kionix.com/Product%20Sheets/KXSD9%20Product%20Brief.pdf)&nbsp;(Kionix KXSD9). The datasheet indicates it is used for image stabilization, and it has 3 axes (X Y and Z) with 10 bits of data per axis.

Lets continuously read that data

```
import usb.core
import usb.util
import sys
import time
 
# find our device
dev = usb.core.find(idVendor=0x045e, idProduct=0x02B0)
 
# was it found?
if dev is None:
    raise ValueError('Device not found')
 
dev.set_configuration()
 
while True:
    # Get data from brequest 0x32
    ret = dev.ctrl_transfer(0xC0, 0x32, 0x0, 0x0, 10)
    print map(hex, ret)
```

Shaking the Kinect while running the script you'll see clearly that the data changes with movement.

To identify the accelerometer axes, rotate it only one way at a time and note what changes. You can also see how this data is in bytes but the accelerometer data should be a signed word because there are flips from 0xfff7 to 0x0007 which would indicate a negative to positive conversion.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/096/medium800/gaming_bitflip.gif?1447974587)

We can cast two bytes to a signed value by 'hand' (in C this is a little easier, we know)```
import usb.core
import usb.util
import sys
import time
 
# find our device
dev = usb.core.find(idVendor=0x045e, idProduct=0x02B0)
 
# was it found?
if dev is None:
    raise ValueError('Device not found')
 
dev.set_configuration()
 
while True:
    # Get data from brequest 0x32
    ret = dev.ctrl_transfer(0xC0, 0x32, 0x0, 0x0, 10)
    #print map(hex, ret)
 
    x = (ret[2] &lt;&lt; 8) | ret[3]
    x = (x + 2 ** 15) % 2**16 - 2**15     # convert to signed 16b
    y = (ret[4] &lt;&lt; 8) | ret[5]
    y = (y + 2 ** 15) % 2**16 - 2**15     # convert to signed 16b
    z = (ret[6] &lt;&lt; 8) | ret[7]
    z = (z + 2 ** 15) % 2**16 - 2**15     # convert to signed 16b
 
    print x, "\t", y, "\t", z
```

Now when you run the script you'll see the signed data appear properly.![](https://cdn-learn.adafruit.com/assets/assets/000/000/097/medium800/gaming_signed.gif?1447974593)

- [Previous Page](https://learn.adafruit.com/hacking-the-kinect/command-number-3-and-4-lets-move.md)
- [Next Page](https://learn.adafruit.com/hacking-the-kinect/more-kinect-information.md)

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
