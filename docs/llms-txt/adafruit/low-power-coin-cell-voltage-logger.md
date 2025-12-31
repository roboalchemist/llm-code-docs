# Source: https://learn.adafruit.com/low-power-coin-cell-voltage-logger.md

# Low Power Coin Cell Voltage Logger

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/002/410/medium800/microcontrollers_testing.jpg?1396782792)

In developing our new [TIMESQUARE watch](http://www.adafruit.com/products/1106 "Link: http://www.adafruit.com/products/1106"),&nbsp;we knew that power use would be a hairy issue.&nbsp;The entire circuit, including an ATmega328P microcontroller and an 8x8 LED matrix, is powered from a single CR2032 lithium coin cell.&nbsp;We obsessed over different LED multiplexing arrangements and processor sleep modes, always trying to trim the power draw just a little bit more.  
  
With the right tools such as the [EEVblog&nbsp;μCurrent](http://adafruit.com/products/882) and a good multimeter, measuring the most&nbsp;minute current changes is a simple task. But translating this into battery longevity isn’t so cut-and-dried…the stated capacity in the battery&nbsp;datasheet&nbsp;assumes a small and constant load, while the watch current can vary greatly.&nbsp;What’s more, the relationship between current draw and battery longevity isn’t necessarily linear. This gets messy. Sometimes you just need to put math and theory aside, plug the thing in and observe the actual outcome.  
  
To that end, we built&nbsp;a test fixture to simulate a consistent use case:&nbsp;activating the watch display once per minute and monitoring the battery voltage as it declines, allowing us to objectively compare different versions of the watch software. The raw data is logged to an SD card for later review and conversion into nice graphs. So this is primarily a tutorial on using the Data Logging Shield for Arduino, but along the way&nbsp;there are some good ancillary tidbits on hardware and software.- [Next Page](https://learn.adafruit.com/low-power-coin-cell-voltage-logger/hardware.md)

## Featured Products

### EEVblog uCurrent - Precision nA Current Measurement Assistant

[EEVblog uCurrent - Precision nA Current Measurement Assistant](https://www.adafruit.com/product/882)
An essential companion when working on a ultra-low-power projects! If you've ever used a portable multimeter (even your $300 Fluke!) to measure sub-uA currents - say for a low power microcontroller or sensor project - you may notice that you're not getting the precision you expect, or...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/882)
[Related Guides to the Product](https://learn.adafruit.com/products/882/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
### Shield stacking headers for Arduino (R3 Compatible)

[Shield stacking headers for Arduino (R3 Compatible)](https://www.adafruit.com/product/85)
_“How could something so simple be so useful?”&nbsp;_

We heard once that&nbsp;in the 4th millennium B.C.&nbsp;some guy asked the person who invented the wheel that question.&nbsp; The person who invented the wheel’s answer, we were told, was...

In Stock
[Buy Now](https://www.adafruit.com/product/85)
[Related Guides to the Product](https://learn.adafruit.com/products/85/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### CR2032 Lithium Coin Cell Battery

[CR2032 Lithium Coin Cell Battery](https://www.adafruit.com/product/654)
A perfect match for our [sew-able coin cell holder](http://www.adafruit.com/products/653). This non-rechargeable coin cell is CR2032 sized: 20mm diameter, 3.2mm thick. It has a nominal voltage output of 3V (although it starts a little high at 3.2V and slowly drifts down to 2.5V as...

In Stock
[Buy Now](https://www.adafruit.com/product/654)
[Related Guides to the Product](https://learn.adafruit.com/products/654/guides)
### TIMESQUARE DIY Watch Kit - Red Display Matrix

[TIMESQUARE DIY Watch Kit - Red Display Matrix](https://www.adafruit.com/product/1106)
Show up stylish AND on time to any event with this awesome looking DIY watch. We have a few watch kits here at Adafruit but we finally have one that looks good and fits well, even for ladies and kids and others with smaller wrists and hands. Its got an 8x8 bit matrix display and a repurposed...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1106)
[Related Guides to the Product](https://learn.adafruit.com/products/1106/guides)

## Related Guides

- [Bluefruit LE Connect for iOS and Android](https://learn.adafruit.com/bluefruit-le-connect.md)
- [Adafruit 1.27" and 1.5" Color OLED Breakout Board](https://learn.adafruit.com/adafruit-1-5-color-oled-breakout-board.md)
- [How to Choose a Microcontroller](https://learn.adafruit.com/how-to-choose-a-microcontroller.md)
- [Trainable Robotic Arm](https://learn.adafruit.com/trainable-robotic-arm.md)
- [2.8" TFT Touch Shield](https://learn.adafruit.com/2-8-tft-touch-shield.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [Arduino "Hunt The Wumpus"](https://learn.adafruit.com/arduino-hunt-the-wumpus.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Trellis 3D Printed Enclosure](https://learn.adafruit.com/trellis-3d-printed-enclosure.md)
- [Arduino Ethernet + SD Card](https://learn.adafruit.com/arduino-ethernet-sd-card.md)
- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Programming Arduino with Android and Windows Tablets](https://learn.adafruit.com/programming-arduino-with-android-and-windows-tablets.md)
