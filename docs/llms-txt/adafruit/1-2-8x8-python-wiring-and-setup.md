# Source: https://learn.adafruit.com/adafruit-led-backpack/1-2-8x8-python-wiring-and-setup.md

# Adafruit LED Backpacks

## Python Wiring and Setup

# Wiring

It's easy to use LED Matrices with Python and the [Adafruit CircuitPython HT16K33](https://github.com/adafruit/Adafruit_CircuitPython_HT16K33) library.&nbsp; This library allows you to easily write Python code to control the display.

We'll cover how to wire the LED Matrix to your Raspberry Pi. First assemble your LED Matrix.

Since there's _dozens_ of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).&nbsp;

Connect the LED Matrix as shown below to your Raspberry Pi.

- **Raspberry Pi 3.3V&nbsp;** to **&nbsp;LED Matrix VIN**
- **Raspberry Pi GND&nbsp;** to **LED Matrix&nbsp;GND**
- **Raspberry Pi SCL&nbsp;** to **LED Matrix&nbsp;SCL**
- **Raspberry Pi SDA&nbsp;** to **LED Matrix&nbsp;SDA**

![led_matrices_raspberry-pi-1.2-8x8_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/086/930/medium640/led_matrices_raspberry-pi-1.2-8x8_bb.jpg?1579126784)

[Download Fritzing Object](https://cdn-learn.adafruit.com/assets/assets/000/087/061/original/raspberry-pi-1.2-8x8.fzz?1579283236)
# Setup

You'll need to install the Adafruit\_Blinka library that provides the CircuitPython support in Python. This may also require enabling I2C on your platform and verifying you are running Python 3. [Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)!

## Python Installation of HT16K33 Library

Once that's done, from your command line run the following command:

- `pip3 install adafruit-circuitpython-ht16k33`

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

If that complains about pip3 not being installed, then run this first to install it:

- `sudo apt-get install python3-pip`

## Pillow Library

We also need PIL, the Python Imaging Library, to allow using text with custom fonts. There are several system libraries that PIL relies on, so installing via a package manager is the easiest way to bring in everything:

- `sudo apt-get install python3-pil`

That's it. You should be ready to go.

- [Previous Page](https://learn.adafruit.com/adafruit-led-backpack/1-2-8x8-circuitpython-wiring-and-setup.md)
- [Next Page](https://learn.adafruit.com/adafruit-led-backpack/1-2-8x8-circuitpython-and-python-usage.md)

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
