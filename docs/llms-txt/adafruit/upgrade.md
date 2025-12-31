# Source: https://learn.adafruit.com/arduino-tips-tricks-and-techniques/upgrade.md

# Arduino Tips, Tricks, and Techniques

## Upgrade

## Introduction

The 'brains' of the Arduino is a microcontroller called an ATmega. It is a product line from [ATMEL](http://www.atmel.com/) (a Norweigen chip company). Just like Intel & AMD release new & better chips each year, so does Atmel. The first versions of the Arduino (up to the NG) used an ATmega8 - a chip with 8K of flash memory and 1K of RAM. Then Atmel released the [ATmega168](http://www.adafruit.com/index.php?main_page=product_info&cPath=17&products_id=56), a drop-in replacement with 16K of flash and 1K of RAM - a really big improvement! Now there is the [ATmega328](http://www.adafruit.com/index.php?main_page=product_info&cPath=17&products_id=123) with 32K of flash and 2K of RAM.  
  
Updating and replacing your Arduino is easy and painless and costs only a few dollars. Your sketches will work just as before but with a little more breathing room.  
  
In order to perform this upgrade you will have to either purchase [a preprogrammed chip](http://www.adafruit.com/index.php?main_page=product_info&cPath=17&products_id=123) or program it yourself with a [AVR programmer](http://www.adafruit.com/index.php?main_page=product_info&cPath=16&products_id=46) or by 'bitbanging' it.

## Replace the Chip
First, **gently** pry the Arduino microcontroller from its socket using a small flat screwdriver or similar. Try to make sure the pins dont get bent. Put it in a safe place. Preferably in an anti-static bag.  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/517/medium800/learn_arduino_prychip.jpg?1396797590)

Next, prepare the new chip. The pins of ICs are a little skewed when they come from the factory, so they need to be bent in just a tiny bit, to be parallel. Grip the chip from the ends and use a table.![](https://cdn-learn.adafruit.com/assets/assets/000/003/518/medium800/learn_arduino_bendchip.jpg?1396797601)

Finally, replace the old chip, lining up all the pins and making sure that the notch in the chip matches the notch in the socket!## Download an Arduino IDE with ATmega328 compatibility
[Version 13 and up of the Arduino software supports the 328!](http://code.google.com/p/arduino/downloads/list)  
  
If you purchased a chip from Adafruit that shipped before Feb 5, 2009 the chip will have the baudrate set at 19200 (same as the older Arduinos). After Feb 5 the upgrade chips were changed to 57600 baud rate (3 times faster!) in order to be compatible with new Arduinos. If you have a 19200 baud rate chip you will have difficulty uploading. Simply quit the Arduino application and edit the file in the **hardware** folder named **boards.txt** and change the line from:  
```
atmega328.upload.speed=57600
```

to:```
atmega328.upload.speed=19200
```

If you're having problems please try BOTH just in case!- [Previous Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/bootloader.md)
- [Next Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/3-3v-conversion.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Arduino bootloader-programmed chip (Atmega328P)

[Arduino bootloader-programmed chip (Atmega328P)](https://www.adafruit.com/product/123)
This is a preprogrammed Atmega328P chip, useful if you want to make your own Arduino-compatible or repair a damaged chip on an exisiting Arduino UNO, Duemilanove, Diecimila, or NG!  
  
This chip is programmed with 'ADAboot', my version of the bootloader that is...

Out of Stock
[Buy Now](https://www.adafruit.com/product/123)
[Related Guides to the Product](https://learn.adafruit.com/products/123/guides)

## Related Guides

- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [WiFi Candy Bowl Monitor](https://learn.adafruit.com/wifi-candy-bowl.md)
- [Arduino Lesson 1. Blink](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
