# Source: https://learn.adafruit.com/hacking-the-kinect/usb-analyzer.md

# Hacking the Kinect

## USB Analyzer

Reverse-engineering the Kinect is a little easier since we have a known-working system (Xbox 360). Instead of guessing commands, we can just see what commands the Xbox sends and 'replay them'![](https://cdn-learn.adafruit.com/assets/assets/000/000/076/medium800/gaming_beagle.jpg?1396760096)

This requires being able to listen into those commands, however. With protocols such as SPI, Serial, Parallel and i2c, you can listen in with any logic analyzer or oscilloscope. USB is fast/complex enough to require its own kind of logic analyzer. The one we'll be using is called the[&nbsp;Beagle480 from TotalPhase.](http://www.totalphase.com/products/beagle_usb480/)&nbsp;This is the 'high speed' USB analyzer, which we splurged on. (For many devices, Low/Full speed is fast enough, and there's a lower cost analyzer available.)

The USB analyzer acts as a 'tap' that plugs in between the Xbox and the Kinect. A computer is conneted as well. The computer receives all the data being transmitted into memory and logs it.

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/000/077/medium800/gaming_beagleend.jpg?1396760101)

From left to right there is a&nbsp; **DIN&nbsp;** connector, **&nbsp;USB A** &nbsp;connector and&nbsp; **USB B** &nbsp;connector. The Xbox connects to the USB B and the Kinect connects to the USB A. The DIN connector is for other kinds of data sniffing (like SPI or i2c).![](https://cdn-learn.adafruit.com/assets/assets/000/000/078/medium800/gaming_beagleend2.jpg?1396760107)

On the other side, a single B connector which goes to the listening computer

The best way we've found to get the right data is to make sure to get even the 'enumeration' (initialization) packets so plug in the listening computer and start up the software. Then plug in the other end to the devices you want to sniff.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/079/medium800/gaming_saving.jpg?1396760111)

## Lookin' at Logs
  
Since you probably don't have a USB analyzer, we have some logs that you can use to follow along with us.&nbsp;[Visit the GitHub repository and click the \*\*Downloads\*\* button](https://github.com/adafruit/Kinect/tree/master/USBlogs/)

Make yourself a sandwich, its a big file!

[Also download the Beagle Data Center software (Mac/Win/Linux)](http://www.totalphase.com/products/beagle_usb480/)&nbsp;and install it

OK now that you've eaten, lets open up the&nbsp; **enuminit**.tdc file. This is the full enumeration and initialization.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/080/medium800/gaming_startscreen.gif?1447974439)

Remember that when we log the data, there's&nbsp; **a lot** &nbsp;of it that we can then pare down!

Let start by remembering that there are&nbsp; **four devices** &nbsp;(hub, camera, mic, motor) but we only need to listen to one (motor). Click on the&nbsp; **Bus&nbsp;** tab on the lower right

![](https://cdn-learn.adafruit.com/assets/assets/000/000/081/medium800/gaming_businfo.gif?1447974450)

We have a few devices. Lets explore each one

If you click on&nbsp;**Unconfigured device (0)&nbsp;**you'll see that it was not captured. This is probably because I jiggled the cable when inserting it so it started to create a device and then got disconnected. Its not important.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/082/medium800/gaming_dev0.gif?1447974460)

Click on&nbsp; **(1)**&nbsp;This device is a&nbsp; **Class** &nbsp;device type USB Hub. That's the internal hub. We can ignore this as well.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/084/medium800/gaming_hub.gif?1447974469)

Device #4 has a PID of 688, that's in decimal. If we convert it to hex we get&nbsp; **0x02b0** &nbsp;- this is the Motor device!![](https://cdn-learn.adafruit.com/assets/assets/000/000/085/medium800/gaming_pid688.gif?1447974479)

Now we can filter so that only this device's logs are shown.![](https://cdn-learn.adafruit.com/assets/assets/000/000/086/medium800/gaming_filter.gif?1447974490)

Our log screen is much shorter now.![](https://cdn-learn.adafruit.com/assets/assets/000/000/087/medium800/gaming_control4.gif?1447974499)

You can see that there's some initialization and then just two repeating motifs: a 1 byte message alternated with a 10 byte message.

For the motor to move according to the xbox's wishes, there must be some command sent from the xbox to the kinect. Lets filter some more to see just commands sent&nbsp; **to&nbsp;** the device

![](https://cdn-learn.adafruit.com/assets/assets/000/000/088/medium800/gaming_filtering.gif?1447974509)

Go to the LiveFilter and select Host-to-Device.![](https://cdn-learn.adafruit.com/assets/assets/000/000/089/medium800/gaming_commands.gif?1447974518)

Now we've really pared it down. There are only&nbsp; **four&nbsp;** commands sent to the kinect motor, since the motor moves during initialization we can just try each one. Lets look at each command

Command 1 has a&nbsp; **bRequest** &nbsp;of 0x06 and a&nbsp; **wValue** &nbsp;of 4, the&nbsp; **wLength&nbsp;** is 0 which means no data is written, the entire command is the&nbsp; **Request** &nbsp;and&nbsp; **Value.**

![](https://cdn-learn.adafruit.com/assets/assets/000/000/090/medium800/gaming_command1.gif?1447974527)

Command #2 uses the same&nbsp; **bRequest** &nbsp;but with a different&nbsp; **wValue** &nbsp;of 0x01.![](https://cdn-learn.adafruit.com/assets/assets/000/000/091/medium800/gaming_command2.gif?1447974536)

Command #3 is a different&nbsp; **bRequest** &nbsp;of 0x31 and a&nbsp; **wValue** &nbsp;of 0xffd0.![](https://cdn-learn.adafruit.com/assets/assets/000/000/092/medium800/gaming_command3.gif?1447974546)

Command #4 is the same&nbsp; **bRequest** &nbsp;and a&nbsp; **wValue** &nbsp;of 0xfff0.![](https://cdn-learn.adafruit.com/assets/assets/000/000/093/medium800/gaming_command4.gif?1447974555)

Now we've determined there are two request commands we can send. One is 0x06 and the other is 0x31

Time to experiment!

- [Previous Page](https://learn.adafruit.com/hacking-the-kinect/fuzzing.md)
- [Next Page](https://learn.adafruit.com/hacking-the-kinect/command-number-1-and-2-led-blinky.md)

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
