# Source: https://learn.adafruit.com/adafruit-led-backpack/circuitpython-wiring-and-setup-2666a265-2d8e-4cde-bcb8-dadc29b6b8fa.md

# Adafruit LED Backpacks

## CircuitPython Wiring and Setup

# Wiring

It's easy to use LED 7-Segment Displays with CircuitPython and the [Adafruit CircuitPython HT16K33](https://github.com/adafruit/Adafruit_CircuitPython_HT16K33) library.&nbsp; This module allows you to easily write CircuitPython code to control the display.

You can use this sensor with any CircuitPython microcontroller board.

We'll cover how to wire the 7-Segment Display to your CircuitPython microcontroller board. First assemble your 7-Segment Display.

Connect the 7-Segment Display to your microcontroller board as shown below.

Danger: 

Warning: 

![](https://cdn-learn.adafruit.com/assets/assets/000/111/870/medium800/led_matrices_metro-m4-big-7-segment_bb.jpg?1653062791)

- **Microcontroller 3.3V&nbsp;** to **3.3v Bus**
- **3.3v Bus** to **7-Segment Display IO**
- **Microcontroller 5V&nbsp;** to **7-Segment Display&nbsp;VIN**
- **Microcontroller GND&nbsp;** to **7-Segment Display&nbsp;GND**
- **Microcontroller SCL&nbsp;** to **7-Segment Display&nbsp;SCL**
- **Microcontroller SDA&nbsp;** to **7-Segment Display&nbsp;SDA**
- **1K Resistor** between **3.3v Bus** and **7-Segment Display&nbsp;SCL**
- **1K Resistor** between **3.3v Bus** and **7-Segment Display SDA**

You can also use a STEMMA QT cable to connect any board with a STEMMA QT port to the updated display.

![](https://cdn-learn.adafruit.com/assets/assets/000/122/072/medium800/led_matrices_feather-rp2040-big-7-segment-stemma_bb.jpg?1687557296)

# Library Setup

To use the LED backpack&nbsp;with your&nbsp;[Adafruit CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/overview)&nbsp;board you'll need to install the&nbsp;[Adafruit\_CircuitPython\_HT16K33](https://github.com/adafruit/Adafruit_CircuitPython_HT16K33) library on your board.

First make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://github.com/adafruit/circuitpython/releases)&nbsp;for your board. &nbsp;Next you'll need to install the necessary libraries&nbsp;to use the hardware--read below and carefully follow the referenced steps to find and install these libraries from [Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).

## Bundle Install

For express boards that have extra flash storage, like the Feather/Metro M0 express and Circuit Playground express, you can easily install the necessary libraries with [Adafruit's CircuitPython bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle). &nbsp;This is an all-in-one package that includes the necessary libraries to use the LED backpack display with CircuitPython. For details on installing the bundle, read about [CircuitPython Libraries](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries).

Remember for non-express boards like the Trinket M0, Gemma M0, and Feather/Metro M0 basic you'll need to [manually install the necessary libraries](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries#non-express-boards-11-13) from the bundle:

- **adafruit\_ht16k33**
- **adafruit\_bus\_device**

If your board supports USB mass storage, like the M0-based boards, then simply drag the files to the board's file system.&nbsp;**Note on boards without external SPI flash, like a Feather M0 or Trinket/Gemma M0, you might run into issues on Mac OSX with hidden files taking up too much space when drag and drop copying,&nbsp;[see this page for a workaround](../../../../micropython-for-samd21/usb-mass-storage#mac-osx-file-copy-issues).**

Before continuing make sure your board's **lib** folder or root filesystem has at least the&nbsp; **adafruit\_ht16k33** and&nbsp; **adafruit\_bus\_device** &nbsp;folders/modules copied over.

![](https://cdn-learn.adafruit.com/assets/assets/000/087/098/medium800/led_matrices_circuitpy.png?1579297124)

- [Previous Page](https://learn.adafruit.com/adafruit-led-backpack/1-2-inch-7-segment-backpack-arduino-wiring-and-setup.md)
- [Next Page](https://learn.adafruit.com/adafruit-led-backpack/python-wiring-and-setup-d74df15e-c55c-487a-acce-a905497ef9db.md)

## Primary Products

### Adafruit Mini 8x8 LED Matrix w/I2C Backpack - Red

[Adafruit Mini 8x8 LED Matrix w/I2C Backpack - Red](https://www.adafruit.com/product/870)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/870)
[Related Guides to the Product](https://learn.adafruit.com/products/870/guides)
### Adafruit Mini 8x8 LED Matrix w/I2C Backpack - Yellow

[Adafruit Mini 8x8 LED Matrix w/I2C Backpack - Yellow](https://www.adafruit.com/product/871)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/871)
[Related Guides to the Product](https://learn.adafruit.com/products/871/guides)
### Adafruit Mini 0.8" 8x8 LED Matrix w/I2C Backpack - Yellow-Green

[Adafruit Mini 0.8" 8x8 LED Matrix w/I2C Backpack - Yellow-Green](https://www.adafruit.com/product/872)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/872)
[Related Guides to the Product](https://learn.adafruit.com/products/872/guides)
### Adafruit 0.56" 4-Digit 7-Segment Display with I2C Backpack - Red

[Adafruit 0.56" 4-Digit 7-Segment Display with I2C Backpack - Red](https://www.adafruit.com/product/878)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

Out of Stock
[Buy Now](https://www.adafruit.com/product/878)
[Related Guides to the Product](https://learn.adafruit.com/products/878/guides)
### Adafruit 0.56" 4-Digit 7-Segment Display w/I2C Backpack - Yellow

[Adafruit 0.56" 4-Digit 7-Segment Display w/I2C Backpack - Yellow](https://www.adafruit.com/product/879)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/879)
[Related Guides to the Product](https://learn.adafruit.com/products/879/guides)
### Adafruit 0.56" 4-Digit 7-Segment Display w/ I2C Backpack - Green

[Adafruit 0.56" 4-Digit 7-Segment Display w/ I2C Backpack - Green](https://www.adafruit.com/product/880)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/880)
[Related Guides to the Product](https://learn.adafruit.com/products/880/guides)
### Adafruit 0.56" 4-Digit 7-Segment Display w/ I2C Backpack - Blue

[Adafruit 0.56" 4-Digit 7-Segment Display w/ I2C Backpack - Blue](https://www.adafruit.com/product/881)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/881)
[Related Guides to the Product](https://learn.adafruit.com/products/881/guides)
### Adafruit Bicolor LED Square Pixel Matrix with I2C Backpack

[Adafruit Bicolor LED Square Pixel Matrix with I2C Backpack](https://www.adafruit.com/product/902)
What's better than a single LED? Lots of LEDs! A fun way to make a small colorful display is to use a [1.2" Bi-color 8x8 LED Matrix](http://www.adafruit.com/products/458). Matrices like these are 'multiplexed' - so to control all the 128 LEDs you need 24 pins....

Out of Stock
[Buy Now](https://www.adafruit.com/product/902)
[Related Guides to the Product](https://learn.adafruit.com/products/902/guides)
### Adafruit Mini 8x8 LED Matrix w/I2C Backpack - Blue

[Adafruit Mini 8x8 LED Matrix w/I2C Backpack - Blue](https://www.adafruit.com/product/959)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/959)
[Related Guides to the Product](https://learn.adafruit.com/products/959/guides)
### Adafruit 0.56" 4-Digit 7-Segment Display w/I2C Backpack - White

[Adafruit 0.56" 4-Digit 7-Segment Display w/I2C Backpack - White](https://www.adafruit.com/product/1002)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/1002)
[Related Guides to the Product](https://learn.adafruit.com/products/1002/guides)
### Adafruit 1.2" 8x8 LED Matrix Backpack

[Adafruit 1.2" 8x8 LED Matrix Backpack](https://www.adafruit.com/product/1048)
By popular request, you can now get our 8x8 LED backpacks without the LEDs! These backpacks feature an HT16K33 I2C LED driver, they're simple and easy to use - you can use&nbsp;[our very nice library for the backpacks to...](https://github.com/adafruit/Adafruit-LED-Backpack-Library)

In Stock
[Buy Now](https://www.adafruit.com/product/1048)
[Related Guides to the Product](https://learn.adafruit.com/products/1048/guides)
### Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Red

[Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Red](https://www.adafruit.com/product/1049)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/1049)
[Related Guides to the Product](https://learn.adafruit.com/products/1049/guides)
### Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Yellow

[Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Yellow](https://www.adafruit.com/product/1050)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/1050)
[Related Guides to the Product](https://learn.adafruit.com/products/1050/guides)
### Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Blue

[Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Blue](https://www.adafruit.com/product/1052)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/1052)
[Related Guides to the Product](https://learn.adafruit.com/products/1052/guides)
### Adafruit Mini 8x8 LED Matrix w/I2C Backpack - Ultra Bright White

[Adafruit Mini 8x8 LED Matrix w/I2C Backpack - Ultra Bright White](https://www.adafruit.com/product/1080)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/1080)
[Related Guides to the Product](https://learn.adafruit.com/products/1080/guides)
### Adafruit 1.2" 4-Digit 7-Segment Display w/I2C Backpack - Green

[Adafruit 1.2" 4-Digit 7-Segment Display w/I2C Backpack - Green](https://www.adafruit.com/product/1268)
What's better than a single LED? Lots of LEDs! A fun way to make a numeric display is to use a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). LED matrices like these are 'multiplexed' - so to control all the seven-segment LEDs you need 14 pins....

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1268)
[Related Guides to the Product](https://learn.adafruit.com/products/1268/guides)
### Adafruit 1.2" 4-Digit 7-Segment Display w/I2C Backpack - Yellow

[Adafruit 1.2" 4-Digit 7-Segment Display w/I2C Backpack - Yellow](https://www.adafruit.com/product/1269)
What's better than a single LED? Lots of LEDs! A fun way to make a numeric display is to use a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). LED matrices like these are 'multiplexed' - so to control all the seven-segment LEDs you need 14 pins....

In Stock
[Buy Now](https://www.adafruit.com/product/1269)
[Related Guides to the Product](https://learn.adafruit.com/products/1269/guides)
### Adafruit 1.2" 4-Digit 7-Segment Display w/I2C Backpack - Red

[Adafruit 1.2" 4-Digit 7-Segment Display w/I2C Backpack - Red](https://www.adafruit.com/product/1270)
What's better than a single LED? Lots of LEDs! A fun way to make a numeric display is to use a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). LED matrices like these are 'multiplexed' - so to control all the seven-segment LEDs you need 14 pins....

Out of Stock
[Buy Now](https://www.adafruit.com/product/1270)
[Related Guides to the Product](https://learn.adafruit.com/products/1270/guides)
### Small 1.2" 8x8 Ultra Bright White LED Matrix + Backpack

[Small 1.2" 8x8 Ultra Bright White LED Matrix + Backpack](https://www.adafruit.com/product/1614)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/1614)
[Related Guides to the Product](https://learn.adafruit.com/products/1614/guides)
### Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Pure Green

[Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Pure Green](https://www.adafruit.com/product/1632)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/1632)
[Related Guides to the Product](https://learn.adafruit.com/products/1632/guides)
### Adafruit Mini 0.8" 8x8 LED Matrix w/I2C Backpack - Pure Green

[Adafruit Mini 0.8" 8x8 LED Matrix w/I2C Backpack - Pure Green](https://www.adafruit.com/product/1633)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/1633)
[Related Guides to the Product](https://learn.adafruit.com/products/1633/guides)
### Bi-Color (Red/Green) 24-Bar Bargraph w/I2C Backpack Kit

[Bi-Color (Red/Green) 24-Bar Bargraph w/I2C Backpack Kit](https://www.adafruit.com/product/1721)
What's better than a single LED? Lots of LEDs! A fun way to make a small linear display is to use two 12-bar Bi-color bar-graphs. However, this LED bargraph is 'multiplexed' - so to control all the 48 LEDs you need a lot of pins. <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/1721)
[Related Guides to the Product](https://learn.adafruit.com/products/1721/guides)
### Small 1.2" 8x8 Ultra Bright Square Amber LED Matrix + Backpack

[Small 1.2" 8x8 Ultra Bright Square Amber LED Matrix + Backpack](https://www.adafruit.com/product/1854)
What's better than a single LED? Lots of LEDs! Matrices like these are 'multiplexed' - so to control 64 LEDs you need 16 pins. That's a lot of pins, and there are [driver chips like the MAX7219](//www.adafruit.com/products/453) that can control a matrix for you but...

In Stock
[Buy Now](https://www.adafruit.com/product/1854)
[Related Guides to the Product](https://learn.adafruit.com/products/1854/guides)
### Small 1.2" 8x8 Ultra Bright Square Yellow LED Matrix + Backpack

[Small 1.2" 8x8 Ultra Bright Square Yellow LED Matrix + Backpack](https://www.adafruit.com/product/1855)
What's better than a single LED? Lots of LEDs! Matrices like these are 'multiplexed' - so to control 64 LEDs you need 16 pins. That's a lot of pins, and there are [driver chips like the MAX7219](//www.adafruit.com/products/453) that can control a matrix for you but...

In Stock
[Buy Now](https://www.adafruit.com/product/1855)
[Related Guides to the Product](https://learn.adafruit.com/products/1855/guides)
### Small 1.2" 8x8 Bright Square Pure Green LED Matrix + Backpack

[Small 1.2" 8x8 Bright Square Pure Green LED Matrix + Backpack](https://www.adafruit.com/product/1856)
What's better than a single LED? Lots of LEDs! Matrices like these are 'multiplexed' - so to control 64 LEDs you need 16 pins. That's a lot of pins, and there are [driver chips like the MAX7219](//www.adafruit.com/products/453) that can control a matrix for you but...

In Stock
[Buy Now](https://www.adafruit.com/product/1856)
[Related Guides to the Product](https://learn.adafruit.com/products/1856/guides)
### Small 1.2" 8x8 Ultra Bright Square White LED Matrix + Backpack

[Small 1.2" 8x8 Ultra Bright Square White LED Matrix + Backpack](https://www.adafruit.com/product/1857)
What's better than a single LED? Lots of LEDs! Matrices like these are 'multiplexed' - so to control 64 LEDs you need 16 pins. That's a lot of pins, and there are [driver chips like the MAX7219](//www.adafruit.com/products/453) that can control a matrix for you but...

In Stock
[Buy Now](https://www.adafruit.com/product/1857)
[Related Guides to the Product](https://learn.adafruit.com/products/1857/guides)
### Adafruit 14-segment LED Alphanumeric Backpack - STEMMA QT

[Adafruit 14-segment LED Alphanumeric Backpack - STEMMA QT](https://www.adafruit.com/product/1910)
By popular request, you can now get our 14-segment LED backpacks without the LEDs! These backpacks feature an HT16K33 I2C LED driver, they're simple and easy to use - you can use [our very nice library for the backpacks to...](https://github.com/adafruit/Adafruit-LED-Backpack-Library)

In Stock
[Buy Now](https://www.adafruit.com/product/1910)
[Related Guides to the Product](https://learn.adafruit.com/products/1910/guides)
### Quad Alphanumeric Display - Red 0.54" Digits w/ I2C Backpack

[Quad Alphanumeric Display - Red 0.54" Digits w/ I2C Backpack](https://www.adafruit.com/product/1911)
Display, elegantly, 012345678 or 9! Gaze, hypnotized, at ABCDEFGHIJKLM - well it can display the whole alphabet. You get the point. This is a nice, bright alphanumeric display that shows letters and numbers in a beautiful red hue. It's super bright and designed for viewing from distances...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1911)
[Related Guides to the Product](https://learn.adafruit.com/products/1911/guides)
### Quad Alphanumeric Display - Blue 0.54" Digits w/ I2C Backpack

[Quad Alphanumeric Display - Blue 0.54" Digits w/ I2C Backpack](https://www.adafruit.com/product/1912)
Display, elegantly, 012345678 or 9! Gaze, hypnotized, at ABCDEFGHIJKLM - well it can display the whole alphabet. You get the point. This is a nice, bright alphanumeric display that shows letters and numbers in a beautiful blue hue. It's super bright and designed for viewing from distances...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1912)
[Related Guides to the Product](https://learn.adafruit.com/products/1912/guides)
### 16x8 1.2" LED Matrix + Backpack - Ultra Bright Round Green LEDs

[16x8 1.2" LED Matrix + Backpack - Ultra Bright Round Green LEDs](https://www.adafruit.com/product/2035)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2035)
[Related Guides to the Product](https://learn.adafruit.com/products/2035/guides)
### 16x8 1.2" LED Matrix+Backpack UltraBright Round YellowGreen LEDs

[16x8 1.2" LED Matrix+Backpack UltraBright Round YellowGreen LEDs](https://www.adafruit.com/product/2036)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2036)
[Related Guides to the Product](https://learn.adafruit.com/products/2036/guides)
### 16x8 1.2" LED Matrix + Backpack - Ultra Bright Round Red LEDs

[16x8 1.2" LED Matrix + Backpack - Ultra Bright Round Red LEDs](https://www.adafruit.com/product/2037)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2037)
[Related Guides to the Product](https://learn.adafruit.com/products/2037/guides)
### 16x8 1.2" LED Matrix + Backpack - Ultra Bright Round White LEDs

[16x8 1.2" LED Matrix + Backpack - Ultra Bright Round White LEDs](https://www.adafruit.com/product/2038)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2038)
[Related Guides to the Product](https://learn.adafruit.com/products/2038/guides)
### 16x8 1.2" LED Matrix + Backpack - Ultra Bright Round Blue LEDs

[16x8 1.2" LED Matrix + Backpack - Ultra Bright Round Blue LEDs](https://www.adafruit.com/product/2039)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2039)
[Related Guides to the Product](https://learn.adafruit.com/products/2039/guides)
### 16x8 1.2" LED Matrix + Backpack - Ultra Bright Square Blue LEDs

[16x8 1.2" LED Matrix + Backpack - Ultra Bright Square Blue LEDs](https://www.adafruit.com/product/2040)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2040)
[Related Guides to the Product](https://learn.adafruit.com/products/2040/guides)
### 16x8 1.2" LED Matrix + Backpack - Ultra Bright Square Amber LEDs

[16x8 1.2" LED Matrix + Backpack - Ultra Bright Square Amber LEDs](https://www.adafruit.com/product/2041)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2041)
[Related Guides to the Product](https://learn.adafruit.com/products/2041/guides)
### 16x8 1.2" LED Matrix + Backpack - Ultra Bright Square Green LEDs

[16x8 1.2" LED Matrix + Backpack - Ultra Bright Square Green LEDs](https://www.adafruit.com/product/2042)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2042)
[Related Guides to the Product](https://learn.adafruit.com/products/2042/guides)
### 16x8 1.2" LED Matrix + Backpack -Ultra Bright Square Yellow LEDs

[16x8 1.2" LED Matrix + Backpack -Ultra Bright Square Yellow LEDs](https://www.adafruit.com/product/2043)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2043)
[Related Guides to the Product](https://learn.adafruit.com/products/2043/guides)
### 16x8 1.2" LED Matrix + Backpack - Ultra Bright Square White LEDs

[16x8 1.2" LED Matrix + Backpack - Ultra Bright Square White LEDs](https://www.adafruit.com/product/2044)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2044)
[Related Guides to the Product](https://learn.adafruit.com/products/2044/guides)
### 16x8 1.2" LED Matrix + Backpack-Ultra Bright Round Orange LEDs

[16x8 1.2" LED Matrix + Backpack-Ultra Bright Round Orange LEDs](https://www.adafruit.com/product/2052)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

In Stock
[Buy Now](https://www.adafruit.com/product/2052)
[Related Guides to the Product](https://learn.adafruit.com/products/2052/guides)
### 16x8 1.2" LED Matrices+Backpack Round LEDs in Various Colors

[16x8 1.2" LED Matrices+Backpack Round LEDs in Various Colors](https://www.adafruit.com/product/2054)
What's better than a single LED? Lots of LEDs! And what's better than lots of LEDs?&nbsp; **TWO TIMES AS MANY LEDS!!!**

With the 16x8 LED Matrix Backpack we've doubled your project's matrix capacity by making it super easy to get two separate 8x8 matrices onto...

Out of Stock
[Buy Now](https://www.adafruit.com/product/2054)
[Related Guides to the Product](https://learn.adafruit.com/products/2054/guides)
### Adafruit 8x16 LED Matrix FeatherWing w/o Matrices

[Adafruit 8x16 LED Matrix FeatherWing w/o Matrices](https://www.adafruit.com/product/3090)
You will chirp with delight when you see how easy it is to make your very own 8x16 LED matrix display for any Feather. At 0.8" square, the little [8x8 matrices](https://www.adafruit.com/new/?q=8x8%20miniature%20LED%20matrix&) have everything a big LED matrix has,...

In Stock
[Buy Now](https://www.adafruit.com/product/3090)
[Related Guides to the Product](https://learn.adafruit.com/products/3090/guides)
### Adafruit 14-segment LED Alphanumeric backpack (same as P1910)

[Adafruit 14-segment LED Alphanumeric backpack (same as P1910)](https://www.adafruit.com/product/3322)
Just the backpack + 4pin header

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/3322)
[Related Guides to the Product](https://learn.adafruit.com/products/3322/guides)

## Featured Products

### Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Yellow-Green

[Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Yellow-Green](https://www.adafruit.com/product/1051)
What's better than a single LED? Lots of LEDs! A fun way to make a small display is to use an [8x8 matrix](https://www.adafruit.com/category/37_88) or a [4-digit 7-segment display](https://www.adafruit.com/category/37_103). Matrices like these are...

In Stock
[Buy Now](https://www.adafruit.com/product/1051)
[Related Guides to the Product](https://learn.adafruit.com/products/1051/guides)
### Small 1.2" 8x8 Ultra Bright Square Blue LED Matrix + Backpack

[Small 1.2" 8x8 Ultra Bright Square Blue LED Matrix + Backpack](https://www.adafruit.com/product/1853)
What's better than a single LED? Lots of LEDs! Matrices like these are 'multiplexed' - so to control 64 LEDs you need 16 pins. That's a lot of pins, and there are [driver chips like the MAX7219](//www.adafruit.com/products/453) that can control a matrix for you but...

In Stock
[Buy Now](https://www.adafruit.com/product/1853)
[Related Guides to the Product](https://learn.adafruit.com/products/1853/guides)

## Related Guides

- [DIY Pocket LED Gamer - Tiny Tetris!](https://learn.adafruit.com/diy-3d-printed-handheld-pocket-game-tiny-tetris-snake.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Raspberry Pi Physical Dashboard](https://learn.adafruit.com/raspberry-pi-physical-dashboard.md)
- [CircuitPython Hardware: LED Backpacks & FeatherWings](https://learn.adafruit.com/micropython-hardware-led-backpacks-and-featherwings.md)
- [Fidget Spinner Tachometer](https://learn.adafruit.com/fidget-spinner-tachometer.md)
- [Trinket / Gemma Space Invader Pendant](https://learn.adafruit.com/trinket-slash-gemma-space-invader-pendant.md)
- [Tap Tempo Trinket](https://learn.adafruit.com/tap-tempo-trinket.md)
- [LED Backpack Displays on Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/led-backpack-displays-on-raspberry-pi-and-beaglebone-black.md)
- [Sino:bit with Arduino](https://learn.adafruit.com/sino-bit-with-arduino.md)
- [Adafruit NeoTrellis](https://learn.adafruit.com/adafruit-neotrellis.md)
- [Sparkle Motion Skirt with 2D Mapping](https://learn.adafruit.com/sparkle-motion-skirt-with-2d-mapping.md)
- [Matrix Portal Money-Sensing Tip Jar](https://learn.adafruit.com/matrix-portal-money-sensing-tip-jar.md)
- [Tombstone Prop-Maker RP2040](https://learn.adafruit.com/tombstone-prop-maker-rp2040.md)
- [SmartMatrix Remote Controlled LED Art Display](https://learn.adafruit.com/smartmatrix-remote-controlled-led-art-display.md)
- [3D Printed Frame for Adafruit IS31FL3741 LED Glasses](https://learn.adafruit.com/3d-printed-frame-for-led-glasses-is31fl3741.md)
