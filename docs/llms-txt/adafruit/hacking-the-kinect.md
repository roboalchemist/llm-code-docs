# Source: https://learn.adafruit.com/hacking-the-kinect.md

# Hacking the Kinect

## Overview

Everyone has seen the&nbsp;[Xbox 360 Kinect hacked in a matter of days after our "open source driver" bounty](http://www.adafruit.com/blog/2010/11/10/we-have-a-winner-open-kinect-drivers-released-winner-will-use-3k-for-more-hacking-plus-an-additional-2k-goes-to-the-eff/)&nbsp;- here's how we helped the winner and here's how you can reverse engineer USB devices as well!

USB is a very complex protocol, much more complicated than Serial or Parallel, SPI and even I2C. USB uses only two wires but they are not used as 'receive' and 'transmit' like serial. Rather, data is bidirectional and differential - that is the data sent depends on the&nbsp;_difference&nbsp;_in voltage between the two data lines&nbsp; **D+** &nbsp;and&nbsp; **D-** &nbsp;If you want to do more USB hacking, you'll need to read&nbsp;[Jan Axelson's USB Complete books](http://janaxelson.com/)&nbsp;, they're easy to follow and discuss USB in both depth and breadth.

USB is also very structured. This is good for reverse engineering because it means that at least the format of packets is agreed upon and you won't have to deal with check-sums. The bad news is it means you have to have software assistance to decode the complex packet structure. The good news is that every computer now made has a USB host core, that does a lot of the tough work for you, and there are many software libraries to assist.

Today we're going to be reverse engineering the Xbox Kinect Motor, one part of the Kinect device.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/258/medium800/gaming_kinect.jpg?1396761550)

- [Next Page](https://learn.adafruit.com/hacking-the-kinect/verify-the-vid-and-pid.md)

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
