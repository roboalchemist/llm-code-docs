# Source: https://learn.adafruit.com/delorean-time-circuit/circuit-trickery.md

# DeLorean Time Circuit

## Circuit Trickery

![](https://cdn-learn.adafruit.com/assets/assets/000/001/308/medium800/lcds___displays_Address.jpg?1396770866)

These 4-digit displays can be assigned one of eight fixed I2C addresses via solder jumpers on the back. But the time circuit needs&nbsp;_nine_&nbsp;displays.&nbsp;A few possibilities were considered, including driving the one extra display “manually” with shift registers, or use a software I2C library and split the displays among multiple I2C buses.&nbsp;Either would require lots of library code changes and some intense concentration, but I was hit with a massive sinus headache at the time and really didn’t want to think about it.

Instead, exploiting the fact that we need just one way, write-only access to use the displays, I used a simple hardware hack to split the I2C bus to communicate with one row of three displays at a time (and saving some code by repeating the same addresses in each row).&nbsp;The I2C data line fans out to all the displays as normal, but the clock feeds the enable lines of a 74HC138 3-to-8 line decoder, and the microcontroller can then select which output line forwards the clock signal. The data on the other I2C buses is ignored without the corresponding clock.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/309/medium800/lcds___displays_Schematic.png?1396770879)

- [Previous Page](https://learn.adafruit.com/delorean-time-circuit/design-liberties.md)
- [Next Page](https://learn.adafruit.com/delorean-time-circuit/fabrication.md)

## Featured Products

### Adafruit 0.56" 4-Digit 7-Segment Display with I2C Backpack - Red

[Adafruit 0.56" 4-Digit 7-Segment Display with I2C Backpack - Red](https://www.adafruit.com/product/878)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/878)
[Related Guides to the Product](https://learn.adafruit.com/products/878/guides)
### Adafruit 0.56" 4-Digit 7-Segment Display w/ I2C Backpack - Green

[Adafruit 0.56" 4-Digit 7-Segment Display w/ I2C Backpack - Green](https://www.adafruit.com/product/880)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/880)
[Related Guides to the Product](https://learn.adafruit.com/products/880/guides)
### Adafruit 0.56" 4-Digit 7-Segment Display w/I2C Backpack - Yellow

[Adafruit 0.56" 4-Digit 7-Segment Display w/I2C Backpack - Yellow](https://www.adafruit.com/product/879)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/879)
[Related Guides to the Product](https://learn.adafruit.com/products/879/guides)
### ChronoDot - Ultra-precise Real Time Clock

[ChronoDot - Ultra-precise Real Time Clock](https://www.adafruit.com/product/255)
The **ChronoDot V3** is the latest version of macetech’s popular ChronoDot line of products. Designed during the Great Chip Shortage, it uses the newly-released MAX31328 temperature-compensated real-time clock chip. However, it remains pin- and code-compatible with the older...

In Stock
[Buy Now](https://www.adafruit.com/product/255)
[Related Guides to the Product](https://learn.adafruit.com/products/255/guides)
### Teensy (ATmega32u4 USB dev board) 2.0

[Teensy (ATmega32u4 USB dev board) 2.0](https://www.adafruit.com/product/199)
Discontinued - **you can grab** [Adafruit ItsyBitsy 32u4 - 5V 16MHz](https://www.adafruit.com/product/3677) **instead!**

The Teensy 2.0 is a complete USB-based microcontoller development system, in a very small footprint! All programming is done via the USB port. No...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/199)
[Related Guides to the Product](https://learn.adafruit.com/products/199/guides)
### Diffused Green 5mm LED (25 pack)

[Diffused Green 5mm LED (25 pack)](https://www.adafruit.com/product/298)
Need some indicators? We are big fans of these diffused green LEDs, in fact we use them exclusively in our kits. They are fairly bright so they can be seen in daytime, and from any angle. They go easily into a breadboard and will add that extra zing to your project.

- Pack of 25...

In Stock
[Buy Now](https://www.adafruit.com/product/298)
[Related Guides to the Product](https://learn.adafruit.com/products/298/guides)
### Diffused Red 5mm LED (25 pack)

[Diffused Red 5mm LED (25 pack)](https://www.adafruit.com/product/299)
Need some indicators? We are big fans of these diffused red LEDs, in fact we use them exclusively in our kits. They are fairly bright so they can be seen in daytime, and from any angle. They go easily into a breadboard and will add that extra zing to your project.

- Pack of 25...

In Stock
[Buy Now](https://www.adafruit.com/product/299)
[Related Guides to the Product](https://learn.adafruit.com/products/299/guides)

## Related Guides

- [Adafruit LED Backpacks](https://learn.adafruit.com/adafruit-led-backpack.md)
- [Mindfulness Clock OF DOOM](https://learn.adafruit.com/mindfulness-clock-of-doom.md)
- [Fidget Spinner Tachometer](https://learn.adafruit.com/fidget-spinner-tachometer.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Collin's Lab: Binary & Hex](https://learn.adafruit.com/collins-lab-binary-and-hex.md)
- [Personalized NextBus ESP8266 Transit Clock](https://learn.adafruit.com/personalized-esp8266-transit-clock.md)
- [Trinket React Counter](https://learn.adafruit.com/trinket-react-counter.md)
- [CircuitPython Hardware: LED Backpacks & FeatherWings](https://learn.adafruit.com/micropython-hardware-led-backpacks-and-featherwings.md)
- [Tap Tempo Trinket](https://learn.adafruit.com/tap-tempo-trinket.md)
- [Raspberry Pi Physical Dashboard](https://learn.adafruit.com/raspberry-pi-physical-dashboard.md)
- [LED Backpack Displays on Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/led-backpack-displays-on-raspberry-pi-and-beaglebone-black.md)
- [Cartoon Character Clock](https://learn.adafruit.com/cartoon-character-clock.md)
- [Feather ESP32-S3 TFT CircuitPython Day 2024 Countdown Clock](https://learn.adafruit.com/feather-esp32-s3-tft-circuitpython-day-2024-countdown-clock.md)
- [Moto 360 Teardown](https://learn.adafruit.com/moto-360-smartwatch-teardown.md)
- [Articulating Retina Monitor](https://learn.adafruit.com/articulating-retina-monitor.md)
