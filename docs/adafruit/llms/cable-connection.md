# Source: https://learn.adafruit.com/barcode-scanner/cable-connection.md

# Barcode Scanner

## Cable Connection

Because these scanners are used for so many industries: checkout counters, manufacturing, inventory, shipping, etc. they are designed to be very configurable and flexible. The first thing you will have to pick out is the cable.&nbsp; **The raw scanner doesnt come with a cable** &nbsp;instead there is a 'ethernet' port on the back (its not really ethernet, it just looks like it) where you can have up to 10 wires come out. These wires carry the different interface wires.![](https://cdn-learn.adafruit.com/assets/assets/000/000/872/medium800/shipping_port.jpg?1396766136)

The following interefaces are supported:

- **USB** &nbsp;(+5V, ground, D+ and D-)
- **PS/2 keyboard 'wedge'&nbsp;** (goes between keyboard and computer, inserts keypresses)
- **RS-232** &nbsp;(+-10V serial)
- **IBM 46xx&nbsp;** (for point of sale computers, rare for other uses)

For our use, we like USB the most because its the most flexible. However, you may want to use these for an embedded project - say where it connects directly to an AVR/PIC/ARM or whatever, you'll probably want to go with the RS232 interface for the ultra simplicity or PS/2 if you don't mind a little extra parsing

You'll need two things to change the interface, one is the proper cable (you can make your own but its a real pain, you'll probably want to just buy it) and a power supply if necessary. RS-232 requires a power supply, but the others do not.

This is the USB cable, for example:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/873/medium800/shipping_cable.jpg?1396766126)

- [Previous Page](https://learn.adafruit.com/barcode-scanner/overview.md)
- [Next Page](https://learn.adafruit.com/barcode-scanner/configure.md)

## Related Guides

- [Digital Shipping Scales](https://learn.adafruit.com/digital-shipping-scales.md)
