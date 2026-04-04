# Source: https://learn.adafruit.com/adafruit-ultimate-gps/battery-backup.md

# Adafruit Ultimate GPS

## Battery Backup

The GPS has a built in real time clock, which can keep track of time even when it power is lost and it doesn't have a fix yet. It can also help reduce fix times, if you expect to have a flakey power connection (say you're using solar or similar). To use the RTC, we need to attach a battery. There is a spot on the back for a&nbsp; **CR1220** &nbsp;sized battery holder. We provide the holder but the battery is not included. You can use any 12mm coin cell - these are popular and we also carry them in the Adafruit shop.

Normally, if the GPS loses power, it will revert to the factory default for baud rates, configuration, etc. A backup battery will mean that those defaults will not be lost!

The backup real-time-clock circuitry draws 7 uA (0.007 mA) so a CR1220 will last 40mAh / 0.007mA = 5,714 hours = 240 days continuously. The backup battery is only used when there's no main 3V power to the GPS, so as long as it's only used as backup once in a while, it will last years

![](https://cdn-learn.adafruit.com/assets/assets/000/001/385/medium800/gps_back.jpeg?1396771683)

## If you have a v1 or v2 module ONLY:
Before inserting a battery into the battery holder, first cut the trace between the two solder pads on the back, labeled RTC (this disconnects the VIN pin from the battery input) Use a multimeter with continuity checking to verify the two pads are no longer tied together.  
  
V3 modules do not have a trace to cut, they have a built-in diode!  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/386/medium800/gps_tracecut.jpeg?1396771689)

Remember, the GPS does not know what time zone you are in (even though it knows your location, there is no easy way to determine time zone without a massive lookup table) so all date/time data is in UTC (aka. Greenwich Mean Time) - You will have to write the code that converts that to your local time zone and account for Daylight Savings if required! Since that's pretty complicated, most people just stick to keeping everything in UTC

- [Previous Page](https://learn.adafruit.com/adafruit-ultimate-gps/pinouts.md)
- [Next Page](https://learn.adafruit.com/adafruit-ultimate-gps/external-antenna.md)

## Featured Products

### Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates

[Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates](https://www.adafruit.com/product/746)
We carry a few different GPS modules here in the Adafruit shop, but none that satisfied our every desire - that's why we designed this little GPS breakout board. We believe this is the **Ultimate** GPS module, so we named it that. It's got everything you want and...

In Stock
[Buy Now](https://www.adafruit.com/product/746)
[Related Guides to the Product](https://learn.adafruit.com/products/746/guides)
### Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates

[Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates](https://www.adafruit.com/product/4279)
The Ultimate GPS module you know and love has a _glow-up_ to let it be easily used with any computer, not just microcontrollers! With the built-in USB-to-Serial converter, you can now plug-n-play the Ultimate GPS into your computer, laptop, embedded Linux computer, and more. Power and...

In Stock
[Buy Now](https://www.adafruit.com/product/4279)
[Related Guides to the Product](https://learn.adafruit.com/products/4279/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA

[GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA](https://www.adafruit.com/product/960)
Give your Ultimate GPS V3 a boost with this external active antenna. This GPS antenna draws about 10mA and will give you an additional 28 dB of gain. It's got a 5 meter long cable so it will easily reach wherever you need it to. The antenna is magnetic so it will stick to the top of a car...

In Stock
[Buy Now](https://www.adafruit.com/product/960)
[Related Guides to the Product](https://learn.adafruit.com/products/960/guides)
### SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable

[SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable](https://www.adafruit.com/product/851)
This RF adapter cable is super handy for anyone doing RF work. Often times, small electronics save space by having a pick-and-placeable u.FL connector (also called uFL, IPEX, IPAX, IPX, MHF, and AM). But most antennas have SMA or RP-SMA connectors on them. This little cable will bridge the...

In Stock
[Buy Now](https://www.adafruit.com/product/851)
[Related Guides to the Product](https://learn.adafruit.com/products/851/guides)
### CR1220 12mm Diameter - 3V Lithium Coin Cell Battery

[CR1220 12mm Diameter - 3V Lithium Coin Cell Battery](https://www.adafruit.com/product/380)
These are the highest quality & capacity batteries, the same as shipped with the iCufflinks,&nbsp;iNecklace, Datalogging and GPS Shields, GPS HAT, etc. One battery per order (you'll want one battery per cufflink or pendant.)  
  
Brand may vary but all battery brands are verified...

Out of Stock
[Buy Now](https://www.adafruit.com/product/380)
[Related Guides to the Product](https://learn.adafruit.com/products/380/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [Ladyada's Learn Arduino - Lesson #2](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-2.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Wireless Game Show Poppers for the Classroom!](https://learn.adafruit.com/wireless-game-show-poppers.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials.md)
- [CircuitPython Libraries on Linux and ODROID C2](https://learn.adafruit.com/circuitpython-libaries-linux-odroid-c2.md)
- [2.2" TFT Display](https://learn.adafruit.com/2-2-tft-display.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
- [Halloween Pumpkin](https://learn.adafruit.com/halloween-pumpkin.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [Automatic Monitor Color Temperature Adjustment](https://learn.adafruit.com/automatic-monitor-color-temperature-adjustment.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Skill Badge Requirements: Microcontrollers](https://learn.adafruit.com/skill-badge-requirements-microcontrollers.md)
- [RePaper eInk Development Board](https://learn.adafruit.com/repaper-eink-development-board.md)
