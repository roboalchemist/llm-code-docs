# Source: https://learn.adafruit.com/diy-8x2-lcd-shield/using-the-lcd-shield.md

# DIY 8x2 LCD Shield

## Using the LCD Shield

Our first test will be just to connect it up to power and see what happens. Plug it into an Arduino and power it up. You should see the following:![](https://cdn-learn.adafruit.com/assets/assets/000/000/962/medium800/lcds___displays_lcdstart.jpg?1396767440)

Make sure you tweak the contrast potentiometer, if the contrast is all the way down you may not see anything.

## Arduino Sketch
Now we must upload some sketch to the Arduino to talk to the LCD. Luckily the&nbsp; **LiquidCrystal** &nbsp;library is already built in. So we just need to load one of the examples and modify it for the pins we used.

If you've changed the pins, you'll want to make a handy table so you can update the sketch properly.

| **LCD pin name** | RS | EN | DB4 | DB5 | DB6 | DB7 |
| **Arduino pin #** | 11 | 12 | 7 | 8 | 9 | 10 |

Open up the **&nbsp;File-\>Examples-\>LiquidCrystal-\>HelloWorld&nbsp;** example sketch

Now we'll need to update the pins. Look for this line:

```
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
```

And change it to:```
LiquidCrystal lcd(11, 12, 7, 8, 9, 10);
```

To match the pin table we just made.

Now you can compile and upload the sketch, adjusting the contrast if necessary. (The image below is from a different fruity sketch but it will look similar).

![](https://cdn-learn.adafruit.com/assets/assets/000/000/963/medium800/lcds___displays_pineapple.jpg?1396767447)

- [Previous Page](https://learn.adafruit.com/diy-8x2-lcd-shield/headers-and-wiring.md)

## Featured Products

### Solid-Core Wire Spool - 25ft - 22AWG - Yellow

[Solid-Core Wire Spool - 25ft - 22AWG - Yellow](https://www.adafruit.com/product/289)
Perfect for bread-boarding, free wiring, etc. This spool of solid-core wire is easy to solder to. When bent it keeps its shape pretty well. We like to have a few spools of this stuff around. We suggest picking up wire strippers to match. Wire gauge is 22 AWG which we've found is the best...

In Stock
[Buy Now](https://www.adafruit.com/product/289)
[Related Guides to the Product](https://learn.adafruit.com/products/289/guides)
### 36-pin 0.1" Female header - pack of 5!

[36-pin 0.1" Female header - pack of 5!](https://www.adafruit.com/product/598)
Female header is like the duct tape of electronics. Its great for connecting things together, soldering to perf-boards, sockets for wires or break-away header, etc. We go through these guys real fast, and thought that given how handy they are, we'd offer them in a pack of five!  
<br...></br...>

In Stock
[Buy Now](https://www.adafruit.com/product/598)
[Related Guides to the Product](https://learn.adafruit.com/products/598/guides)
### Break-away 0.1" 36-pin strip male header - Black - 10 pack

[Break-away 0.1" 36-pin strip male header - Black - 10 pack](https://www.adafruit.com/product/392)
Breakaway header is like the duct tape of electronics. It's great for connecting things together, soldering to perf-boards, fits into any breakout or breadboard, etc. We go through these guys real fast, and thought that given how handy they are, we'd offer them in a pack of ten!<br...></br...>

In Stock
[Buy Now](https://www.adafruit.com/product/392)
[Related Guides to the Product](https://learn.adafruit.com/products/392/guides)
### Adafruit Proto Shield for Arduino Kit

[Adafruit Proto Shield for Arduino Kit](https://www.adafruit.com/product/51)
Works with the Uno! This prototyping shield is the best out there (well, we think so, at least). It works with UNO, NG, Diecimila and Duemilanove Arduinos. You can use it with a Leonardo but it will not break out the hardware SPI pins (they're only on the ISP connector underneath) or the...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/51)
[Related Guides to the Product](https://learn.adafruit.com/products/51/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Wireless Game Show Poppers for the Classroom!](https://learn.adafruit.com/wireless-game-show-poppers.md)
- [Adafruit Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps.md)
- [Arduino Lesson 4. Eight LEDs and a Shift Register](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [FTDI Friend](https://learn.adafruit.com/ftdi-friend.md)
- [A REST API for Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/a-rest-api-for-arduino-and-the-cc3000-wifi-chip.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [Bluefruit LE Connect for iOS and Android](https://learn.adafruit.com/bluefruit-le-connect.md)
- [Babel Fish](https://learn.adafruit.com/babel-fish.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Light Meter](https://learn.adafruit.com/light-meter.md)
- [Adafruit 16-channel PWM/Servo Shield](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield.md)
- [Halloween Pumpkin](https://learn.adafruit.com/halloween-pumpkin.md)
- [Naughty or Nice Machine](https://learn.adafruit.com/naughty-or-nice-machine.md)
