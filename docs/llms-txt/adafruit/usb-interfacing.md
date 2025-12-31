# Source: https://learn.adafruit.com/barcode-scanner/usb-interfacing.md

# Barcode Scanner

## USB Interfacing

We like USB best for business/work usage because it has power and data and is fairly simple to use. USB can act in two modes:

- HID **keyboard** mode
- HID **raw data** mode

As you can imagine, keyboard mode the scanner shows up just as a keyboard and when you scan a barcode it 'types it in' to whatever window you're currently viewing. This is the default mode and its very easy to test and get started.

However, it requires that the user always has the right window up and in the right location for data-entry. For programs with windows, this is a little tough because dialog boxes can pop-up and its easy to click in the wrong place. We like using the raw data mode although its a little tougher to use. In this mode, we literally open up the raw USB connection to the scanner and grab the barcode data directly. This means we can run our scanner software in the background

Neither need drivers for any operating system which is handy.

**[For more details on raw USB connections, check out our Kinect hacking tutorial](http://learn.adafruit.com/hacking-the-kinect "Link: http://learn.adafruit.com/hacking-the-kinect")**

[Our code is adapted from this Wiimote project to read Wiimotes accelerometer/sensor data](http://pywiimote.googlecode.com/) . We only ported the windows part - hopefully someone who is inspired will port the mac/linux version.

You can download our code from our GitHub repo, see the Downloads section below.

Install Python 2.5, win32file and any other extras you need. Plug in your scanner, open up a command line and run **python test.py** in the uncompressed folder

![](https://cdn-learn.adafruit.com/assets/assets/000/000/875/medium800/shipping_scanned.gif?1447976597)

- [Previous Page](https://learn.adafruit.com/barcode-scanner/configure.md)
- [Next Page](https://learn.adafruit.com/barcode-scanner/stand.md)

## Related Guides

- [Digital Shipping Scales](https://learn.adafruit.com/digital-shipping-scales.md)
