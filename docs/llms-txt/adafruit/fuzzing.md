# Source: https://learn.adafruit.com/hacking-the-kinect/fuzzing.md

# Hacking the Kinect

## Fuzzing

Now we can use Python + LibUSB to send Control Endpoint packets with the command

**ctrl\_transfer**** ( bmRequestType, bmRequest, wValue, wIndex, nBytes)**

This command can do both sending and receiving depending on what&nbsp; **bmRequestType&nbsp;** says (input or output). Still, there is a lot of options here. To send the right command you need to know the **RequestType** &nbsp;and the right&nbsp; **Request** &nbsp;and ther right&nbsp; **Value** &nbsp;as well as the&nbsp; **Index** &nbsp;and how many bytes to read or write.

If we were totally on our own, we would start by trying to read data from the device. This means we have to set the&nbsp; **RequestType** &nbsp;first

| Direction | Type | | | | Recipient |
| --- | --- | --- | --- | --- | --- |
| **D7** | **D6** | **D5** | **D4** | **D3** | **D2** | **D1** | **D0** |

For&nbsp; **bmRequestType** &nbsp;the value passed is very structured so that's not as hard to guess. ([See lvr.com for more information](http://www.beyondlogic.org/usbnutshell/usb6.shtml)&nbsp;)

- Bits 2, 3 and 4 are reserves so set them to 0.
- The direction is set by bit #7, 0 is a 'write' out to the device, 1 is a 'read' from the device
- The 'type' of message is two bits, 0 = Standard, 1 = Class, 2 = Vendor, 3 = Reserved. For many devices that are non-standard, you'll probably want 2 for vendor type. If its a more standard type of device, like a camera or mic, try 0 or 1. 3 Is unused
- The last two bits are usd to determine the recipient for the message 0 = Device, 1 = Interface, 2 = Endpoint, 3 = Other. Go with 0 to start, you can try 2 if there are other endpoints

The safest thing to do is read data (no way to overwrite anything or configure) you can do that by sending packets with&nbsp; **0b11000000** &nbsp;(Read Vendor data from Device) = 0xC0.

If I were to write a fuzzer, I'd start by setting&nbsp; **Index&nbsp;** to 0 and iterating through all the byte values (255 different values) of&nbsp; **bmRequest** &nbsp;and the first few hundred&nbsp; **wValues**. Its pretty safe to just read random data to a USB device. Start by reading one byte to see if anything shows up, then increase the value

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
 
# Let's fuzz around! 
 
# Lets start by Reading 1 byte from the Device using different Requests
# bRequest is a byte so there are 255 different values
for bRequest in range(255):
    try:
        ret = dev.ctrl_transfer(0xC0, bRequest, 0, 0, 1)
        print "bRequest ",bRequest
        print ret
    except:
        # failed to get data for this request
        pass
```

![](https://cdn-learn.adafruit.com/assets/assets/000/000/074/medium800/gaming_brequestiter.gif?1447974418)

Looks like **&nbsp;Request&nbsp;** values 0, 5, 16, 50, 54, 64, 80 and 112 all return some sort of data. The rest had nothing to read

Next we'll try to read more data by changing the last argument to 100 bytes

![](https://cdn-learn.adafruit.com/assets/assets/000/000/075/medium800/gaming_brequest100.gif?1447974427)

OK lots of data, but what does it mean? This is where some guessing based on the device itself would come in handy. I'm terribly lazy though and if given an option to avoid a lot of guesswork, I'll take it!- [Previous Page](https://learn.adafruit.com/hacking-the-kinect/installing-python-and-pyusb.md)
- [Next Page](https://learn.adafruit.com/hacking-the-kinect/usb-analyzer.md)

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
