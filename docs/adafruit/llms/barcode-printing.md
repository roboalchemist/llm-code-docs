# Source: https://learn.adafruit.com/mini-thermal-receipt-printer/barcode-printing.md

# Mini Thermal Receipt Printers

## Barcode Printing

Thermal printers are really good at printing barcodes! This printer supports 11 different codes -&nbsp; **UPC A, UPC E, EAN13, EAN8, CODE39, I25, CODEBAR, CODE93, CODE128, CODE11** &nbsp;and&nbsp; **MSI**. It only supports linear (1-D) barcodes, and can’t generate 2-D barcodes like QR codes (although there is a hack you can do, see below!) Barcodes are generated “on the fly,” which is nice — you can customize the height and data included quite easily.

You can make a barcode by calling&nbsp;**printBarcode("barcodedata", BARCODETYPE)**,&nbsp;where the first string is the data to encode (e.g. a&nbsp;UPC code)&nbsp;and&nbsp; **BARCODETYPE** &nbsp;can be&nbsp; **UPC\_A, UPC\_E,&nbsp;**** EAN13, EAN8, CODE39, I25, CODEBAR, CODE93, CODE128, CODE11 **&nbsp;or&nbsp;** MSI**.

Some barcodes are very restricted — you can only put in 12 numbers, no characters. Others are very flexible and take nearly any character input.[&nbsp;Please check out the wikipedia list detailing kinds of barcodes&nbsp;](http://en.wikipedia.org/wiki/Barcodes#Linear_barcodes "Link: http://en.wikipedia.org/wiki/Barcodes#Linear\_barcodes")to pick the right one for your application.

The available range of barcodes varies with the printer firmware revision. Check Adafruit\_Thermal.h for a list of codes.

It’s also possible to print QR codes, if you’re willing to pre-generate them. This might be handy if you want to, let’s say, include a URL on the receipt and the URL doesn’t change.&nbsp;[You can generate QR codes at many sites including this one.](http://qrcode.kaywa.com/ "Link: http://qrcode.kaywa.com/")&nbsp;Use the smallest QR code size. The image will be in PNG format, so if you’re using the Windows LCD Assistant tool you’ll need to convert it to BMP first (Windows Paint works for this). Then you can convert and embed this in your Arduino sketch as previously described.

&nbsp;

![](https://cdn-learn.adafruit.com/assets/assets/000/001/958/medium800/components_qr-code.jpg?1396777795)

- [Previous Page](https://learn.adafruit.com/mini-thermal-receipt-printer/bitmap-printing.md)
- [Next Page](https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython.md)

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
