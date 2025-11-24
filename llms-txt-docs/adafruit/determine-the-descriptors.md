# Source: https://learn.adafruit.com/hacking-the-kinect/determine-the-descriptors.md

# Hacking the Kinect

## Determine the Descriptors

The next best thing to do after you've determined the VID/PID is to identify the&nbsp; **descriptor** &nbsp;of the device. A descriptor is a sort of 'menu' of what the device can do and how it likes to transfer data. In general, each device has one descriptor._&nbsp;Sometimes_&nbsp;a device has more than one descriptor and you can choose which one you want but its not terribly common so we're just going to ignore it.A fantastic way to get the descriptor without having to write any software is to run&nbsp; **lsusb -vv&nbsp;** on a linux computer.&nbsp; (Try the "USB Prober" tool from Apple for Mac&nbsp;OS&nbsp;X or [USBView on Windows](https://msdn.microsoft.com/en-us/library/windows/hardware/ff560019%28v=vs.85%29.aspx))

Here is the output of&nbsp; **lsusb** &nbsp;for the NUI Motor

```
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass            0 (Defined at Interface level)
  bDeviceSubClass         0
  bDeviceProtocol         0
  bMaxPacketSize0        64
  idVendor           0x045e Microsoft Corp.
  idProduct          0x02b0
  bcdDevice            1.05
  iManufacturer           1 Microsoft
  iProduct                2 Xbox NUI Motor
  iSerial                 0
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength           18
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0
    bmAttributes         0xc0
      Self Powered
    MaxPower              100mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           0
      bInterfaceClass       255 Vendor Specific Class
      bInterfaceSubClass      0
      bInterfaceProtocol      0
      iInterface              0
Device Status:     0x0000
  (Bus Powered)
```

Let's see what we've got. You can see the VID and PID up there. Next we'll look at&nbsp; **bNumConfigurations** &nbsp;(how many different descriptors we have) and lucky for us the number is&nbsp; **1.&nbsp;** Next, look at the **Interface Descriptor** &nbsp;in particular,&nbsp; **bNumEndpoints** &nbsp;which is 0. This means there are no Endpoints.

Endpoints are a type of USB 'data pipe' - there are 4 kinds:

- **Bulk&nbsp;** Endpoints are for transferring a lot of data, like a disk drive. It's OK if it takes a little longer but we want big packets. This endpoint goes only in one direction (so to read and write you'd want two)
- **Interrupt** &nbsp;Endpoints are for transferring tiny amounts of data very quickly, like for a USB mouse. In this case, the device has to be responsive so we want fast movement. This endpoint goes only in one direction
- **Isochronous** &nbsp;Endpoints are for transferring a fair amount of data where the data must show up at the same time and if it can't it should just be dropped. This is for stuff like Audio and Video where timing is key. This endpoint goes only in one direction (so bidirectional audio for headphone and mic would have two EPs)
- **Control Endpoints** &nbsp;are this weird not-quite-an-Endpoint Endpoint. They are used to transfer small amounts of data to say turn a device on or off. They're very 'cheap' to develop, and every device has one even if its not mentioned.

For example, a serial port may have two Interrupt endpoints for transferring data in and out and then a control endpoint for setting the baud rate.

For more details we really do suggest reading everything at **[janaxelson.com](http://janaxelson.com/)** about USB as it's complex.

This motor device has no Endpoints, but that doesn't mean you can't communicate with it. It just means it only uses a bidirectional Control Endpoint. This isn't surprising, motors are slow and don't require a lot of data to control.

Contrast this to the Video/Camera device:

```
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass            0 (Defined at Interface level)
  bDeviceSubClass         0
  bDeviceProtocol         0
  bMaxPacketSize0        64
  idVendor           0x045e Microsoft Corp.
  idProduct          0x02ae
  bcdDevice            1.0b
  iManufacturer           2 Microsoft
  iProduct                1 Xbox NUI Camera
  iSerial                 3 A00366A08793039A
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength           32
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0
    bmAttributes         0xc0
      Self Powered
    MaxPower               16mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass       255 Vendor Specific Class
      bInterfaceSubClass    255 Vendor Specific Subclass
      bInterfaceProtocol    255 Vendor Specific Protocol
      iInterface              0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0bc0  2x 960 bytes
        bInterval               1
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x82  EP 2 IN
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0bc0  2x 960 bytes
        bInterval               1
Device Qualifier (for other device speed):
  bLength                10
  bDescriptorType         6
  bcdUSB               2.00
  bDeviceClass            0 (Defined at Interface level)
  bDeviceSubClass         0
  bDeviceProtocol         0
  bMaxPacketSize0        64
  bNumConfigurations      1
Device Status:     0x0001
  Self Powered
```

This device has two Isochronous endpoints&nbsp; **both** &nbsp;of which are&nbsp; **IN&nbsp;** type (data going&nbsp; **IN** to the computer). This makes sense: the Kinect has a IR depth camera and a normal VGA camera. Two cameras, two Endpoints. Of course, there is also a Control endpoint not mentioned here, the Control endpoint could be used to set stuff like aperture, gamma correction, any sort of built-in filter, etc.- [Previous Page](https://learn.adafruit.com/hacking-the-kinect/verify-the-vid-and-pid.md)
- [Next Page](https://learn.adafruit.com/hacking-the-kinect/making-a-driver.md)

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
