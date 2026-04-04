# Source: https://learn.adafruit.com/adafruit-ultimate-gps/pinouts.md

# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/pinouts.md

# Source: https://learn.adafruit.com/adafruit-led-backpack/pinouts.md

# Adafruit LED Backpacks

## Pinouts

![](https://cdn-learn.adafruit.com/assets/assets/000/115/303/medium800/led_matrices_QAB_pinouts_guide.jpg?1663879804)

![](https://cdn-learn.adafruit.com/assets/assets/000/115/314/medium800/led_matrices_QAB_original_pinouts_guide.jpg?1663885374)

There are a number of features on the 0.54" Alphanumeric Backpack.

# STEMMA QT Revision-Only Features

These features are only available on the STEMMA QT revision.

## STEMMA QT Connectors

The default I2C address is **0x70**.

The&nbsp;[**STEMMA QT connectors**](https://learn.adafruit.com/introducing-adafruit-stemma-qt) provide a solder-free way to connect this backpack to development boards with STEMMA QT connectors, or to other things, with[various associated accessories](https://www.adafruit.com/category/1018).

![led_matrices_QAB_STEMMA_QT.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/304/medium640/led_matrices_QAB_STEMMA_QT.jpg?1663879864)

## On LED and LED Jumper
- **On LED** - On the left side of the back of the board is a little green LED labeled **On**. This LED lights up when the board is successfully powered.
- **LED jumper** - To the right of the On LED is a jumper labeled **LED**. If you wish to disable the On LED, you can cut the trace between the two pads. To enable it again, use solder to reconnect the two pads.

![led_matrices_QAB_on_LED_and_jumper.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/313/medium640/led_matrices_QAB_on_LED_and_jumper.jpg?1663884948)

# Original and STEMMA QT Version Features

These features are available on both versions. There is one header pin difference between the two, which is explained in the next section. Everything else is the same.

## Header Pin Through-Hole Pads

If you prefer to use a breadboard, there are through-hole header pin pads along the top of the board in the middle.

The default I2C address is **0x70**.

 **On both versions:**

- **VIO/VCC** - This is power for the backpack. It can be 3V-5V. To power the backpack, give it the same power as the logic level of your microcontroller - e.g. for a 5V microcontroller like Arduino, use 5V.
- **GND** - This is common ground for power and logic.
- **SCL** - This is the I2C clock pin. Connect it to your microcontroller I2C clock line. This pin is level shifted so you can use 3-5V logic, and there's a&nbsp; **10K pullup** &nbsp;on this pin.
- **SDA** - This is the I2C data pin. Connect it to your microcontroller I2C data line. This pin is level shifted so you can use 3-5V logic, and there's a&nbsp; **10K pullup** &nbsp;on this pin.

![led_matrices_QAB_header_pins.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/305/medium640/led_matrices_QAB_header_pins.jpg?1663880455)

![led_matrices_QAB_header_pins_top.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/306/medium640/led_matrices_QAB_header_pins_top.jpg?1663880490)

![led_matrices_QAB_original_header_pins.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/307/medium640/led_matrices_QAB_original_header_pins.jpg?1663883889)

![led_matrices_QAB_original_header_pins_top.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/308/medium640/led_matrices_QAB_original_header_pins_top.jpg?1663883921)

Warning: Wiring VHi to 3v on the Stemma QT version will result in the display not activating.

 **On the STEMMA QT revision ONLY:**

- **VHi** - This pin allows you to provide 5V to only the 14-segment displays when using a 3V device to control the backpack. If you're using a 3V device and you want your displays to be brighter, you can maintain the 3V I2C power level, and connect 5V to the VHi pin to make the 14-segment displays have a brighter look.

**On the original version ONLY:**

- **Vi2c** - This is the I2C voltage, which sets the logic level to I2C. Connect this pin to the voltage pin on your device that matches the device's logic level. For example, if you're using a 3.3V microcontroller, connect it to 3.3V.

## Display Pin Through-Hole Pads
These two rows of through-hole pads are for soldering the alphanumeric LED displays onto the backpack. See the [Assembly page](https://learn.adafruit.com/adafruit-led-backpack/0-54-alphanumeric-assembly) for details on attaching the displays properly.

![led_matrices_QAB_display_pins.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/309/medium640/led_matrices_QAB_display_pins.jpg?1663884043)

![led_matrices_QAB_display_pins_top.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/310/medium640/led_matrices_QAB_display_pins_top.jpg?1663884454)

![led_matrices_QAB_original_display_pins.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/311/medium640/led_matrices_QAB_original_display_pins.jpg?1663884481)

![led_matrices_QAB_original_display_pins_top.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/312/medium640/led_matrices_QAB_original_display_pins_top.jpg?1663884545)

## HT16K33 Matrix Driver
The chip located in the center of the back of the backpack is the HT16K33 matrix driver, which drives the 14-segment LED displays.

![led_matrices_QAB_HT16K33.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/315/medium640/led_matrices_QAB_HT16K33.jpg?1663885964)

![led_matrices_QAB_original_HT16K33.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/316/medium640/led_matrices_QAB_original_HT16K33.jpg?1663885988)

## Address Jumper Pins
On the back of the board are **three address jumpers** , labeled **A0** , **A1** , and **A2**. These jumpers allow you to chain up to 8 of these boards on the same pair of I2C clock and data pins. To do so, you solder the jumpers "closed" in various combinations by connecting the two pads.

The default I2C address is **0x70**. The other address options can be calculated by “adding” the **A0/A1/A2** to the base of **0x70**.

![led_matrices_QAB_address_jumpers.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/317/medium640/led_matrices_QAB_address_jumpers.jpg?1663886388)

![led_matrices_QAB_original_address_jumpers.jpg](https://cdn-learn.adafruit.com/assets/assets/000/115/318/medium640/led_matrices_QAB_original_address_jumpers.jpg?1663886548)

 **A0** sets the lowest bit with a value of **1** , **A1** sets the next bit with a value of **2** and **A2** sets the next bit with a value of **4.** The final address is **0x7**** 0 + A2 + A1 + A0 **which would be** 0x77**.

So for example if **A2** is soldered closed and **A0** is soldered closed, the address is **0x70 + 4 + 1 = 0x75**.

 If only **A0** is soldered closed, the address is **0x70 + 1 = 0x71**

 If only **A1** is soldered closed, the address is **0x70 + 2 = 0x72**

 If only **A2** is soldered closed, the address is **0x70 + 4 = 0x74**

The table below shows all possible addresses, and whether the pin(s) should be high (closed) or low (open).

![](https://cdn-learn.adafruit.com/assets/assets/000/115/319/medium800/led_matrices_QAB_HT16K33_I2C_addresses.png?1663887143)

- [Previous Page](https://learn.adafruit.com/adafruit-led-backpack/0-54-alphanumeric.md)
- [Next Page](https://learn.adafruit.com/adafruit-led-backpack/0-54-alphanumeric-assembly.md)

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
