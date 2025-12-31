# Source: https://learn.adafruit.com/mini-thermal-receipt-printer/bitmap-printing.md

# Mini Thermal Receipt Printers

## Bitmap Printing

This printer can produce bitmaps, which can add a touch of class to a receipt with your logo or similar.

The first step is to get the image prepared. The printer can only do monochrome (1-bit) images, and the maximum width is 384 pixels.&nbsp;We suggest starting with a small bitmap (100 pixels or less on each side) and then experimenting to get the size and look you want.

A few steps are required to prepare an image for printing. For Windows users, there’s a nice graphical user interface for this. For Mac and Linux, different tools are used…not as visually slick, but they do the job well.

Danger: 

## Windows
Use an image editing program to save your image as a 1-bit BMP — in Windows, the built-in&nbsp; **Paint** &nbsp;program will suffice.  
  
Download, install and run **[LCD Assistant](http://en.radzio.dxp.pl/bitmap_converter/)**. This program is for Windows only but does a really fantastic job! Load the BMP file you previously generated (in Paint, etc.). The file&nbsp;<u>must</u> be in BMP format — the software won’t read PNG, GIF, etc. Then a couple of settings need to be adjusted…

![](https://cdn-learn.adafruit.com/assets/assets/000/001/955/medium800/components_lcd-assistant.png?1396777773)

First, in the “Byte orientation” section of the settings, select “Horizontal” (item A in the image above).  
  
Second (item B above), you may need to change the Width setting.&nbsp;Because this software (and the thermal printer) handle images in horizontal groups of eight&nbsp;pixels, if the image width is not a multiple of 8, it will be truncated (cropped) to the nearest smaller 8-pixel boundary. For example, with the 75 pixel wide image above, the output will be cropped to only 72 pixels wide, losing some data from the right edge.&nbsp;To avoid this, **increase this number to the next multiple of 8** (that would be 80 for the example above), and the output will be padded with blank pixels to cover the gap. Remember the number you use here, you’ll need it later.  
  
The image height does not need to be adjusted this way, only width.  
  
Set the table name to something short but&nbsp;descriptive (e.g. “adalogo” above), then select Save Output from the File menu. Give the file a similarly brief but descriptive name, ending in “.h” (e.g. “adalogo.h”).  
  
To get this file into your Arduino sketch, select “Add File…” from the Sketch menu. This will add a new tab to your code. Your original code is still there under the leftmost tab.  
  
A couple of small changes are now needed in both tabs. First, at the top of the&nbsp;file containing the new table data, change “const unsigned char” to “static const uint8\_t PROGMEM” as shown below:

![](https://cdn-learn.adafruit.com/assets/assets/000/026/979/medium800/components_progmem.png?1438715537)

Next, in the tab containing the main body of your code, add an “include” statement to reference the new file:

```
#include "adalogo.h"
```

Check the **A\_printertest** example sketch if you’re not sure how to include the code properly.

You can now output the image by calling **printBitmap(width, height, tablename)**, where **width** and **height** are the dimensions of the image in pixels (if you changed the image width to a multiple of 8 as previously described, use that number, not the original image size), and **tablename** is the name of the array in the new tab (e.g. “adalogo” above).

![](https://cdn-learn.adafruit.com/assets/assets/000/001/957/medium800/components_bitmap-print.jpg?1396777794)

Having a graphical user interface is nice, but some of these extra steps can be confusing and error-prone. If you prefer, the technique below for Mac and Linux works in Windows as well.

## Mac and Linux
The conversion tool for Mac and Linux doesn’t include a fancy GUI, but it works well and avoids several steps (and potential mis-steps). The source image doesn’t need to be in BMP format — most image formats can be read natively — and the output can be added to a sketch with no&nbsp;further editing. It works for Windows as well, if you’d rather use this method.  
  
First, if you don’t already have the **Processing** language installed, [download it from processing.org](http://processing.org). Processing&nbsp;looks almost exactly like the Arduino IDE, but it’s for writing code for your normal computer, not a microcontroller. This can be a little confusing to first-timers, so if something doesn’t seem to compile, make sure you’re running code in the right environment: _Arduino_ for for the Arduino board, _Processing_ for your computer.

Danger: 

The Adafruit\_Thermal library folder that you previously downloaded contains a sub-folder called&nbsp; **processing**. Inside that is a sketch called&nbsp; **bitmapImageConvert.pde**. Load this into Processing and press RUN (the triangle button).  
  
You’ll be prompted to select an image using the system’s standard file selection dialog. The program runs for just a brief instant, and will create a new file alongside the original image file. For example, if you selected an image called “adalogo.png”, there will be a new file called “adalogo.h” in the same location. This file contains code to add to your Arduino sketch. You shouldn’t need to edit this file unless you want to change the variable names within.  
  
To get this file into your Arduino sketch, select “Add File…” from the Sketch menu. This will add a new tab to your code. Your original code is still there under the leftmost tab.  
  
Next, in the tab containing the main body of your code, add an “include” statement to reference the new file:

```
#include "adalogo.h"
```

Check the&nbsp; **A\_printertest** &nbsp;example sketch if you’re not sure how to include the code properly.

If the source image was called adalogo.png, then the resulting .h file (adalogo.h) will contain three values called adalogo\_width, adalogo\_height and adalogo\_data, which can be passed directly and in-order to the printBitmap() function, like this:

```
printBitmap(adalogo_width, adalogo_height, adalogo_data);
```

- [Previous Page](https://learn.adafruit.com/mini-thermal-receipt-printer/printing-text.md)
- [Next Page](https://learn.adafruit.com/mini-thermal-receipt-printer/barcode-printing.md)

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
