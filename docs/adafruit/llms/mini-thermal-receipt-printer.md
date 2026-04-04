# Source: https://learn.adafruit.com/mini-thermal-receipt-printer.md

# Mini Thermal Receipt Printers

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/001/942/medium800/components_thermalprinter_LRG.jpg?1396777649)

Add printing to any microcontroller project with these very cute thermal printers. Also known as receipt printers, they’re what you see at the ATM or grocery store.&nbsp;Now you can embed a little printer of your own into a project. These printers is ideal for interfacing with a microcontroller, you simply need a 3.3V to&nbsp;5V TTL serial output from your microcontroller to print text, barcodes, bitmap graphics, even a QR code!

These printers use very common 2.25" (58mm) wide thermal paper, available in the Adafruit shop&nbsp;or most office or stationery supply stores. You will also need a 5 Volt to 9 Volt regulated DC power supply that can provide 2 Amps or more&nbsp;during high-current printing&nbsp;—&nbsp;[our 5V 2A power supply will work very nicely](https://www.adafruit.com/products/276).

**[You can pick up a thermal printer pack including printer, paper, power supply and terminal-block adapter in the Adafruit shop!](http://www.adafruit.com/products/600 "Link: http://www.adafruit.com/products/600")**

Of course, we wouldn't leave you with a datasheet and a “good luck!” — this tutorial and matching Arduino library demonstrate the following:

- Printing with small, medium and large text
- **Bold,** &nbsp;<u>underline</u>&nbsp;and inverted&nbsp;text
- Variable&nbsp;line&nbsp;spacing
- Left, center and&nbsp;right justification
- Barcodes in the following standard formats:&nbsp; **UPC A, UPC E, EAN13, EAN8, CODE39, I25, CODEBAR, CODE93, CODE128, CODE11** &nbsp;and&nbsp; **MSI** &nbsp;- with adjustable barcode height
- Custom monochrome bitmap graphics
- How to print a QR code

## Models
Our _[**Mini Thermal Receipt Printer**](https://www.adafruit.com/product/597)_ is a popular choice as it accommodates a [full-length thermal roll (15m/50')](https://www.adafruit.com/product/599), meaning fewer paper changes.&nbsp;It’s also available in a [**starter pack**](https://www.adafruit.com/product/600) that includes a 5V power supply and DC jack adapter.

This model has a **3-pin serial interface** for connecting to 3.3V or 5V microcontrollers or Raspberry Pi.

![components_mini.jpg](https://cdn-learn.adafruit.com/assets/assets/000/117/073/medium640/components_mini.jpg?1671038975)

The [_ **Tiny Thermal Receipt Printer** _](https://www.adafruit.com/product/2751) is a bit more compact, accommodating shorter&nbsp;[10m/33' rolls](https://www.adafruit.com/product/2754).

What’s interesting and **unique to this model** is that it has _both_ a 5-pin serial header and a **USB port** , which can make for easier interfacing on Raspberry Pi.

![components_tiny.jpg](https://cdn-learn.adafruit.com/assets/assets/000/117/074/medium640/components_tiny.jpg?1671039054)

For the most compact and portable situations, the [_ **Nano Thermal Receipt Printer** _](https://www.adafruit.com/product/2752) is smaller still, accommodating a [5m/16' paper roll](https://www.adafruit.com/product/2755).

This one has a **5-pin header** &nbsp;for serial data and power.

![components_nano.jpg](https://cdn-learn.adafruit.com/assets/assets/000/117/075/medium640/components_nano.jpg?1671039078)

For the most peculiar situations not covered above, the&nbsp;[_ **Thermal Printer Receipt Guts** _](https://www.adafruit.com/product/2753) is _just the insides_ of a thermal printer.&nbsp;You will need to design and build an enclosure to mount the hardware and hold a paper roll…in principle, _any length_ roll can then work with this.

This unit has a **5-pin header** for serial data and power.

![components_guts.jpg](https://cdn-learn.adafruit.com/assets/assets/000/117/076/medium640/components_guts.jpg?1671039111)

The thermal paper rolls in the Adafruit shop are BPA-free and ready sized to each of the above units.&nbsp;You can also find compatible 2.25" (58mm) wide thermal paper at many office supply stores,&nbsp;though usually in 80–85 foot (25m) lengths that won’t fit as-is in any of these printers. With some patience you can re-roll these onto an empty spool, cutting when the roll reaches a suitable diameter.

**None of these small thermal printers&nbsp;have a cut feature; pull the finished print against the perforated edge.** The _Thermal Printer Guts_ has no perforated edge; you’ll need to design this into your enclosure.

Primary: 

- [Next Page](https://learn.adafruit.com/mini-thermal-receipt-printer/power.md)

## Primary Products

### Mini Thermal Receipt Printer

[Mini Thermal Receipt Printer](https://www.adafruit.com/product/597)
Add a mini printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an enclosure. This printer is ideal...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/597)
[Related Guides to the Product](https://learn.adafruit.com/products/597/guides)
### Tiny Thermal Receipt Printer - TTL Serial / USB

[Tiny Thermal Receipt Printer - TTL Serial / USB](https://www.adafruit.com/product/2751)
Add a _really small_ printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an enclosure. This...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2751)
[Related Guides to the Product](https://learn.adafruit.com/products/2751/guides)
### Nano Thermal Receipt Printer - TTL Serial

[Nano Thermal Receipt Printer - TTL Serial](https://www.adafruit.com/product/2752)
Add a _really really small_ printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2752)
[Related Guides to the Product](https://learn.adafruit.com/products/2752/guides)
### Thermal Receipt Printer Guts

[Thermal Receipt Printer Guts](https://www.adafruit.com/product/2753)
Add printing capability to any microcontroller project with **just the innards of a thermal printer.** Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into a...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2753)
[Related Guides to the Product](https://learn.adafruit.com/products/2753/guides)

## Featured Products

### Mini Thermal Receipt Printer Starter Pack

[Mini Thermal Receipt Printer Starter Pack](https://www.adafruit.com/product/600)
Hit the ground running (and printing!) with this starter pack that includes a thermal printer and all the extras and save a few dollars while you're at it.  
  
Includes:

- [A mini thermal receipt printer](http://www.adafruit.com/products/597) - with cables and...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/600)
[Related Guides to the Product](https://learn.adafruit.com/products/600/guides)
### Female DC Power adapter - 2.1mm jack to screw terminal block

[Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
If you need to connect a DC power wall wart to a board that doesn't have a DC jack - this adapter will come in very handy! There is a 2.1mm DC jack on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/368)
[Related Guides to the Product](https://learn.adafruit.com/products/368/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### Thermal paper roll - 50' long, 2.25" wide

[Thermal paper roll - 50' long, 2.25" wide](https://www.adafruit.com/product/599)
A mini roll of thermal paper, this fits very nicely into our mini thermal printer. 2.25" wide (about 57mm) and 50 feet long (15 meters). BPA-free.  
  
[Perfect for use with our mini thermal printer!](http://www.adafruit.com/products/597)

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/599)
[Related Guides to the Product](https://learn.adafruit.com/products/599/guides)
### Thermal Paper Roll - 33' long, 2.25"

[Thermal Paper Roll - 33' long, 2.25"](https://www.adafruit.com/product/2754)
A little roll of thermal paper! This fits very nicely into our&nbsp;[Tiny Thermal Receipt Printer](https://www.adafruit.com/products/2751). It's ~2.25" wide (about 57mm) and 33 feet long or about 10 meters.

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2754)
[Related Guides to the Product](https://learn.adafruit.com/products/2754/guides)
### Thermal Paper Roll - 16' long, 2.25"

[Thermal Paper Roll - 16' long, 2.25"](https://www.adafruit.com/product/2755)
A little roll of thermal paper! This fits very nicely into our [Nano Thermal Receipt Printer](https://www.adafruit.com/products/2752). It's ~2.25" wide (about 57mm) and 16 feet long or about 5 meters.

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2755)
[Related Guides to the Product](https://learn.adafruit.com/products/2755/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [How to Find Hidden COM Ports](https://learn.adafruit.com/how-to-find-hidden-com-ports.md)
- [Wireless Game Show Poppers for the Classroom!](https://learn.adafruit.com/wireless-game-show-poppers.md)
- [Adafruit Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Silicone Robo-Tentacle](https://learn.adafruit.com/silicone-robo-tentacle.md)
- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [Metal Inlay Capacitive Touch Buttons](https://learn.adafruit.com/metal-inlay-capacitive-touch-buttons.md)
- [Adafruit IO Basics: NeoPixel Controller](https://learn.adafruit.com/adafruit-io-basics-neopixel-controller.md)
- [Adafruit PN532 RFID/NFC Breakout and Shield](https://learn.adafruit.com/adafruit-pn532-rfid-nfc.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Adafruit INA219 Current Sensor Breakout](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout.md)
- [All About Arduino Libraries](https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use.md)
