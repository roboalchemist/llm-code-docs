# Source: https://learn.adafruit.com/adafruit-led-backpack/circuitpython-and-python-usage-197dcbfa-4ccf-4b98-a152-3982411df681.md

# Adafruit LED Backpacks

## CircuitPython and Python Usage

The following section will show how to control the LED backpack&nbsp;from the board's Python prompt / REPL. &nbsp;You'll walk through how to control the LED display and learn how to use the CircuitPython module built for the display.

First&nbsp;[connect to the board's serial REPL&nbsp;](https://learn.adafruit.com/welcome-to-circuitpython/the-repl)so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

## Initialization

First you'll need to initialize the I2C bus for your board.&nbsp; It's really easy, first import the necessary modules. In this case, we'll use `board` and `BigSeg7x4`.

Then just use `board.I2C()` to create the I2C instance using the default SCL and SDA pins (which will be marked on the boards pins if using a Feather or similar Adafruit board).

Then to initialize the display, you just pass `i2c` in.

Warning: When using the STEMMA QT port, some board may have an alternate I2C such as board.STEMMA_I2C().

```python
import board
from adafruit_ht16k33.segments import BigSeg7x4

i2c = board.I2C()
display = BigSeg7x4(i2c)
```

If you bridged the address pads on the back of the display, you could pass in the address. The addresses for the HT16K33 can range between 0x70 and 0x77 depending on which pads you have bridged, with 0x70 being used if you haven't bridged any of them. For instance, if you bridge only the **A0** pad, you would use `0x71` like this:

```python
display = BigSeg7x4(i2c, address=0x71)
```

## Setting the Brightness

You can set the brightness of the display, but changing it will set the brightness of the entire display and not individual segments. If can be adjusted in 1/16 increments **between 0 and 1.0** with 1.0 being the brightest. So to set the display to half brightness, you would use the following:

```python
display.brightness = 0.5
```

## Setting the Blink Rate

You can set the blink rate of the display, but changing it will set the brightness of the entire display and not individual segments. If can be adjusted in 1/4 increments **between 0 and 3** with 3 being the fastest blinking. So to set the display to blink at full speed, you would use the following:

```python
display.blink_rate = 3
```

## Printing Text

To print text to the display, you just use the print function. For the 7-segment display, valid characters are 0-9, letters A-F, and a hyphen. So if we want to print ABCD, we would use the following:

```python
display.print("ABCD")
```

## Printing Numbers

Printing numbers is done similar to printing text, except without the quotes, though you can still print numbers in a string as well.

```python
display.print(1234)
```

## Printing Hexidecimal Values

To print hexidecimal values, you use the `print_hex` function:

```python
display.print_hex(0x1A2B)
```

## Setting Individual Characters

To set individual characters, you simply treat the `display` object as a list and set it to&nbsp;the value that you would like.

```python
display[0] = '1'
display[1] = '2'
display[2] = 'A'
display[3] = 'B'
```

## Setting Individual Segments

To set individual segments to turn on or off, you would use the set\_digit\_raw function to pass the digit that you want to change and the bitmask. This can be really useful for creating your own characters. The bitmask corresponds to the following diagram. The highest bit is not used, so an X represents that spot to indicate that.

![](https://cdn-learn.adafruit.com/assets/assets/000/088/408/medium800/led_matrices_set_pixel_raw.png?1581626276)

The bitmask is a single 8-bit number that can be passed in as a single Hexidecimal, Decimal, or binary number. This will use a couple different methods to display `8E8E`:

```python
display.set_digit_raw(0, 0xFF)
display.set_digit_raw(1, 0b11111111)
display.set_digit_raw(2, 0x79)
display.set_digit_raw(3, 0b01111001)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/087/750/medium800/led_matrices_set_digit_raw_example.jpeg?1580237134)

## Filling all Segments

To fill the entire display, just use the fill() function and pass in either 0 or 1 depending on whether you want all segments off or on. For instance, if you wanted to set everything to on, you would use:

```python
display.fill(1)
```

## Scrolling Display Manually

If you want to scroll the displayed data to the left, you can use the `scroll()` function. You can pass in the number of places that you want to scroll. The right-most digit will remain unchanged and you will need to set that manually. After scrolling, you will need to call the show function. For example if you wanted to print an A and then scroll it over to spaces, you would do the following.

```python
display.print("A")
display.scroll(2)
display[3] = " "
display.show()
```

## Displaying the Colon

There are a couple of different ways to display a colon on the 7-segment display. The first and easiest way is to use the print function:

```python
display.print("12:30")
```

The other way to control it is to access the colon with the colons property and set index 0 to `True` or `False`:

```python
display.colons[0] = False
```

## Setting the Left-Side Dots

There are a couple of different ways to set the left-side dots on the large 7-segment display. The first way is to use the colons property like above:

```python
display.colons[1] = False
```

If you would like to set the dots individually, you can do that using the `top_left_dot` and `bottom_left_dot` properties and set them to `True` or `False`:

```python
display.top_left_dot = True
display.bottom_left_dot = True
```

## Setting the AM/PM Indicator

If you would like to set the upper-right dot, you can do this using the `ampm` property:

```python
display.ampm = True
```

## Displaying an Automatic Scrolling Marquee

To make displaying long text easier, we've added a marquee function. You just pass it the full string. Optionally, you can pass it the amount of delay between each character. This may be useful for displaying a phone number, words using only letters A-F, or other numeric data:

```python
display.marquee('Deadbeef ')
```

![](https://cdn-learn.adafruit.com/assets/assets/000/087/751/medium800thumb/led_matrices_marquee.jpg?1580237154)

By default it is 0.25 seconds, but you can change this by providing a second parameter. You can optionally pass&nbsp;`False`&nbsp;for a third parameter if you would not like to have it loop. So if you wanted each character to display for half a second and didn't want it to loop, you would use the following:

```python
display.marquee('Deadbeef', 0.5, False)
```

- [Previous Page](https://learn.adafruit.com/adafruit-led-backpack/python-wiring-and-setup-d74df15e-c55c-487a-acce-a905497ef9db.md)
- [Next Page](https://learn.adafruit.com/adafruit-led-backpack/bi-color-8x8-matrix.md)

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
