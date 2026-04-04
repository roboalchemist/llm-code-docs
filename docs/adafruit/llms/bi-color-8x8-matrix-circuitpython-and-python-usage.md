# Source: https://learn.adafruit.com/adafruit-led-backpack/bi-color-8x8-matrix-circuitpython-and-python-usage.md

# Adafruit LED Backpacks

## CircuitPython and Python Usage

The following section will show how to control the LED backpack&nbsp;from the board's Python prompt / REPL. &nbsp;You'll walk through how to control the LED display and learn how to use the CircuitPython module built for the display.

First&nbsp;[connect to the board's serial REPL&nbsp;](https://learn.adafruit.com/welcome-to-circuitpython/the-repl)so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

## Initialization

First you'll need to initialize the I2C bus for your board.&nbsp; It's really easy, first import the necessary modules. In this case, we'll use `board` and `Matrix8x8x2`.

Then just use `board.I2C()` to create the I2C instance using the default SCL and SDA pins (which will be marked on the boards pins if using a Feather or similar Adafruit board).

Then to initialize the matrix, you just pass `i2c` in.

Warning: When using the STEMMA QT port, some board may have an alternate I2C such as board.STEMMA_I2C().

```python
import board
from adafruit_ht16k33.matrix import Matrix8x8x2

i2c = board.I2C()
matrix = Matrix8x8x2(i2c)
```

If you bridged the address pads on the back of the display, you could pass in the address. The addresses for the HT16K33 can range between 0x70 and 0x77 depending on which pads you have bridged, with 0x70 being used if you haven't bridged any of them. For instance, if you bridge only the **A0** pad, you would use `0x71` like this:

```python
matrix = Matrix8x8x2(i2c, address=0x71)
```

## Setting the Brightness

You can set the brightness of the display, but changing it will set the brightness of the entire display and not individual segments. If can be adjusted in 1/16 increments **between 0 and 1.0** with 1.0 being the brightest. So to set the display to half brightness, you would use the following:

```python
display.brightness = 0.5
```

## Setting the Blink Rate

You can set the blink rate of the display, but changing it will set the brightness of the entire display and not individual pixels. If can be adjusted in 1/4 increments&nbsp; **between 0 and 3** &nbsp;with 3 being the fastest blinking. So to set the display to blink at full speed, you would use the following:

```python
display.blink_rate = 3
```

## Setting Individual Pixels

To set individual pixels to specific colors, you simply treat the `matrix` object as a multidimensional list and set it to` matrix.LED_RED`,` matrix.LED_GREEN`,` matrix.LED_YELLOW` or` matrix.LED_OFF`.

```python
matrix[0, 0] = matrix.LED_RED
matrix[4, 4] = matrix.LED_GREEN
matrix[7, 7] = matrix.LED_YELLOW
matrix[7, 0] = matrix.LED_OFF
```

![](https://cdn-learn.adafruit.com/assets/assets/000/087/752/medium800/led_matrices_IMG_1545.jpeg?1580237559)

## Filling the Entire Matrix

To fill the entire matrix, just use the fill() function and pass in the color you want to set it to. For instance, if you wanted to set everything to green, you would use:

```python
matrix.fill(matrix.LED_GREEN)
```

## Shifting the Matrix

To shift the pixels on the matrix, there are 5 functions you can use. The main function, called shift(), is used to shift the pixels, up, down, left, right, or even diagonally. By passing a positive number, it will shift the pixels right/up and passing a negative number will shift them left/down. For instance:

```python
matrix.shift(2, 0)	# shift pixels to the right by 2
matrix.shift(-1, 0)	# shift pixels to the left by 1
matrix.shift(0, -3)	# shift pixels down by 3
matrix.shift(-2, 2)	# shift pixels left by 2 and up by 2
```

You can pass `True` as a third parameter to loop all the pixels that get shifted off over to the other side.

```python
matrix.shift(2, 0, True)	# loop pixels to the right by 2
matrix.shift(-1, 0, True)	# loop pixels to the left by 1
matrix.shift(0, -3, True)	# loop pixels down by 3
matrix.shift(-2, 2, True)	# loop pixels left by 2 and up by 2
```

Additionally, there are a few convenience functions that will shift the pixels by one. These can also be passed a value of `True` to loop the pixels.

```python
matrix.shift_up()		# Shift pixels up
matrix.shift_left()		# Shift pixels left
matrix.shift_down()		# Shift pixels down
matrix.shift_right()		# Shift pixels right
matrix.shift_up(True)		# Loop pixels up
matrix.shift_left(True)	# Loop pixels left
matrix.shift_down(True)	# Loop pixels down
matrix.shift_right(True)	# Loop pixels right
```

## Displaying an Image (Pillow Only)

Additionally, when using with the Raspberry Pi, you can use the Pillow library to display an image to the Matrix. The image will need to be the same exact size as the Matrix and should include pure Green, Red, or Yellow. Anything else will be considered to be **off**. In this case, it should be **8x8** pixels. As an example, you can save the image below as **myimage.png**.

![](https://cdn-learn.adafruit.com/assets/assets/000/087/755/medium800/led_matrices_squares-color.png?1580237815)

[Download Image](https://cdn-learn.adafruit.com/assets/assets/000/087/755/original/led_matrices_squares-color.png?1580237815)
Then if you want to display the image called **myimage.png** , you would use something like this:

```python
import board
from PIL import Image
from adafruit_ht16k33 import matrix

matrix = matrix.Matrix8x8x2(board.I2C())

image = Image.open("myimage.png")
matrix.image(image)
```

![](https://cdn-learn.adafruit.com/assets/assets/000/087/753/medium800/led_matrices_IMG_1544.jpeg?1580237590)

- [Previous Page](https://learn.adafruit.com/adafruit-led-backpack/bi-color-8x8-matrix-python-wiring-and-setup.md)
- [Next Page](https://learn.adafruit.com/adafruit-led-backpack/bi-color-24-bargraph.md)

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

In Stock
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

In Stock
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

In Stock
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

Out of Stock
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

In Stock
[Buy Now](https://www.adafruit.com/product/1911)
[Related Guides to the Product](https://learn.adafruit.com/products/1911/guides)
### Quad Alphanumeric Display - Blue 0.54" Digits w/ I2C Backpack

[Quad Alphanumeric Display - Blue 0.54" Digits w/ I2C Backpack](https://www.adafruit.com/product/1912)
Display, elegantly, 012345678 or 9! Gaze, hypnotized, at ABCDEFGHIJKLM - well it can display the whole alphabet. You get the point. This is a nice, bright alphanumeric display that shows letters and numbers in a beautiful blue hue. It's super bright and designed for viewing from distances...

In Stock
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

Out of Stock
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

- [LED Backpack Displays on Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/led-backpack-displays-on-raspberry-pi-and-beaglebone-black.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Raspberry Pi Physical Dashboard](https://learn.adafruit.com/raspberry-pi-physical-dashboard.md)
- [CircuitPython Hardware: LED Backpacks & FeatherWings](https://learn.adafruit.com/micropython-hardware-led-backpacks-and-featherwings.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
- [DIY Pocket LED Gamer - Tiny Tetris!](https://learn.adafruit.com/diy-3d-printed-handheld-pocket-game-tiny-tetris-snake.md)
- [RGB LED Matrix Cube with 25,000 LEDs](https://learn.adafruit.com/rgb-led-matrix-cube-for-pi.md)
- [Creating GIFs for SmartMatrix](https://learn.adafruit.com/creating-gifs-for-smartmatrix.md)
- [Adafruit CharliePlex LED Matrix Bonnet](https://learn.adafruit.com/adafruit-charlieplex-bonnet.md)
- [Connecting a 16x32 RGB LED Matrix Panel to a Raspberry Pi](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi.md)
- [MicroPython Displays: Drawing Text](https://learn.adafruit.com/micropython-displays-drawing-text.md)
- [Heart Rate Badge](https://learn.adafruit.com/heart-rate-badge.md)
- [16x24 LED Matrix](https://learn.adafruit.com/16x24-led-matrix.md)
- [Adafruit IS31FL3741](https://learn.adafruit.com/adafruit-is31fl3741.md)
