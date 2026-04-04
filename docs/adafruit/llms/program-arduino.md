# Source: https://learn.adafruit.com/internet-of-things-printer/program-arduino.md

# Internet of Things Printer

## Program Arduino

Danger: 

Gutenbird is a <u>big</u> program, nearly filling the Arduino’s entire program space. We’ve gone to great lengths to help it fit, but if you add a lot of new functionality of your own it may run into an issue…  
  
If the code compiles but fails to upload on an R1 or R2 Arduino Uno, you’re seeing an obscure bug in the board’s bootloader when dealing with very large programs. There are a couple of workarounds for this:

- **FIX 1:** If you build a lot of projects and have an Arduino Uno R3 handy, swap it out. Dedicate the R3 board for Gutenbird and use the R2 for the majority of Arduino projects that aren’t quite so demanding. This is the easiest option, <u>if</u> you have the spare board.
- **FIX 2:** Update the bootloader on the older Uno using directions on Arduino.cc. A second Arduino is required during the upgrade, and there’s a small risk of “bricking” your R1/R2 board, so this option is best left to advanced users.

# Edit Code…
- You'll now need to edit the Gutenbird sketch to match all your particular settings. First, copy and paste the four authentication strings from your Twitter application page to the corresponding spots in the software, keeping the quotes around them. **The order of these strings in the code does not match the order on the Twitter form — be sure to copy each to the correct position!**

![](https://cdn-learn.adafruit.com/assets/assets/000/001/260/medium800/adafruit_products_codeedits.png?1396770405)

- As written, the sketch will search for Tweets originating from Adafruit, but you can change this to any search string supported by the Twitter Search API. Refer to the SEARCH OPERATORS section of the [Twitter Developers Documentation](https://developer.twitter.com/ "Link: https://dev.twitter.com/docs/using-search") for guidance.
- Edit the Ethernet MAC address to match the value you previously wrote down from the sticker on your Arduino Ethernet board or shield.
- The code uses DHCP (which dynamically assigns an IP address) by default. If your network doesn't use DHCP, or if you just want to provide a fallback address in case of a problem, edit the IP Address value in the code.
- If using the Arduino Ethernet board, flip up the front face of the enclosure and connect an FTDI Friend or other USB-to-serial adapter to the programming header on the board. If using an Arduino Uno, use the USB port on the back of the box.

&nbsp;

![](https://cdn-learn.adafruit.com/assets/assets/000/001/261/medium800/adafruit_products_front-flap.jpg?1396770416)

- Select your board type and serial port from the Arduino IDE&nbsp;_Tools_&nbsp;menu, build the sketch and upload to the board. USB can now be disconnected; the box will operate standalone.  

- [Previous Page](https://learn.adafruit.com/internet-of-things-printer/twitter-setup.md)
- [Next Page](https://learn.adafruit.com/internet-of-things-printer/use-it.md)

## Primary Products

### Adafruit IoT Printer Project Pack "Internet of Things" printer

[Adafruit IoT Printer Project Pack "Internet of Things" printer](https://www.adafruit.com/product/717)
Build an "Internet of Things" connected mini printer that will do your bidding! This is a fun weekend project that comes with a beautiful laser cut case. Once assembled, the little printer connects to Ethernet to get Internet data for printing onto 2 1/4" wide receipt paper. The example sketch...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/717)
[Related Guides to the Product](https://learn.adafruit.com/products/717/guides)

## Featured Products

### Mini Thermal Receipt Printer

[Mini Thermal Receipt Printer](https://www.adafruit.com/product/597)
Add a mini printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an enclosure. This printer is ideal...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/597)
[Related Guides to the Product](https://learn.adafruit.com/products/597/guides)
### Thermal paper roll - 50' long, 2.25" wide

[Thermal paper roll - 50' long, 2.25" wide](https://www.adafruit.com/product/599)
A mini roll of thermal paper, this fits very nicely into our mini thermal printer. 2.25" wide (about 57mm) and 50 feet long (15 meters). BPA-free.  
  
[Perfect for use with our mini thermal printer!](http://www.adafruit.com/products/597)

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/599)
[Related Guides to the Product](https://learn.adafruit.com/products/599/guides)
### Adafruit METRO 328 - Arduino Compatible - with Headers

[Adafruit METRO 328 - Arduino Compatible - with Headers](https://www.adafruit.com/product/2488)
This is the&nbsp; **Adafruit METRO Arduino-Compatible - with&nbsp;headers.&nbsp;** It's a fully assembled and tested microcontroller and physical computing board with through-hole headers attached.&nbsp; If you don't want a&nbsp;Metro with the headers attached for...

In Stock
[Buy Now](https://www.adafruit.com/product/2488)
[Related Guides to the Product](https://learn.adafruit.com/products/2488/guides)
### Ethernet Shield for Arduino - W5500 Chipset

[Ethernet Shield for Arduino - W5500 Chipset](https://www.adafruit.com/product/2971)
The W5500 Ethernet Shield for Arduino from Seeed Studio is a great way to set up your projects with internet connectivity with just a single chip. &nbsp;Similar to the[Arduino Ethernet Shield](https://www.adafruit.com/product/201), but with a newer chipset, this ethernet shield...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2971)
[Related Guides to the Product](https://learn.adafruit.com/products/2971/guides)
### FTDI Friend with Micro USB Port + extras

[FTDI Friend with Micro USB Port + extras](https://www.adafruit.com/product/284)
Long gone are the days of parallel ports and serial ports. Now the USB port reigns supreme! But USB is hard, and you just want to transfer your every-day serial data from a microcontroller to computer. What now? Enter the FTDI Friend!

The FTDI Friend is a tweaked out FTDI FT232RL chip...

In Stock
[Buy Now](https://www.adafruit.com/product/284)
[Related Guides to the Product](https://learn.adafruit.com/products/284/guides)
### Rugged Metal On/Off Switch with Green LED Ring

[Rugged Metal On/Off Switch with Green LED Ring](https://www.adafruit.com/product/482)
These chrome-plated metal buttons are rugged and look real good while doing it! Simply drill a 16mm hole into any material up to 1/2" thick and you can fit these in place, there's even a rubber gasket to keep water out of the enclosure. On the front of the button is a flat metal...

In Stock
[Buy Now](https://www.adafruit.com/product/482)
[Related Guides to the Product](https://learn.adafruit.com/products/482/guides)
### Arduino Ethernet shield R3 with micro SD connector - Assembled

[Arduino Ethernet shield R3 with micro SD connector - Assembled](https://www.adafruit.com/product/201)
The Arduino Ethernet Shield R3 (assembled) allows an Arduino board to connect to the internet. It is based on the Wiznet W5100 ethernet chip (datasheet). The Wiznet W5100 provides a network (IP) stack capable of both TCP and UDP. It supports up to four simultaneous socket connections. Use the...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/201)
[Related Guides to the Product](https://learn.adafruit.com/products/201/guides)
### Arduino Uno Ethernet

[Arduino Uno Ethernet](https://www.adafruit.com/product/418)
 **As of 9/20/2012 Adafruit is currently shipping R3 of the Arduino Uno Ethernet**

Deep in the Swiss Alps, the top secret Arduino Super-collider has accelerated both an [Arduino UNO](https://www.adafruit.com/products/50) and <a...></a...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/418)
[Related Guides to the Product](https://learn.adafruit.com/products/418/guides)

## Related Guides

- [Mystery Box: NeoMatrix Mk I](https://learn.adafruit.com/mystery-box-neomatrix-mk-i.md)
- [A Z80 CP/M emulator for the SAMD51](https://learn.adafruit.com/z80-cpm-emulator-for-the-samd51-grand-central.md)
- [Echo 2-XL](https://learn.adafruit.com/echo-2-xl.md)
- [DC & USB Boarduino Kits](https://learn.adafruit.com/boarduino-kits.md)
- [Portable Solar Charging Tracker](https://learn.adafruit.com/portable-solar-charging-tracker.md)
- [Ladyada's Learn Arduino - Lesson #2](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-2.md)
- [Motorized Camera Slider MK3 ](https://learn.adafruit.com/motorized-camera-slider-mk3.md)
- [Adafruit VCNL4040 Proximity Sensor](https://learn.adafruit.com/adafruit-vcnl4040-proximity-sensor.md)
- [Ladyada's Learn Arduino - Lesson #1](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-1.md)
- [Trinket / Gemma IR Control](https://learn.adafruit.com/trinket-gemma-ir-remote-control.md)
- [Adafruit HUZZAH32 – ESP32 Breakout Board](https://learn.adafruit.com/huzzah32-esp32-breakout-board.md)
- [Adafruit HUZZAH ESP8266 breakout](https://learn.adafruit.com/adafruit-huzzah-esp8266-breakout.md)
- [FTDI Friend](https://learn.adafruit.com/ftdi-friend.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [IR Sensor](https://learn.adafruit.com/ir-sensor.md)
