# Source: https://learn.adafruit.com/2-8-tft-touchscreen.md

# 2.8" TFT Touchscreen

## Overview

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/003/024/medium800/lcds___displays_testbars1.jpg?1396790404)

Add some jazz & pizazz to your project with a color touchscreen LCD. This TFT display is big (2.8" diagonal) bright (4 white-LED backlight) and colorful (16-bit 262,000 different shades)! 240x320 pixels with individual pixel control, this has way more resolution than a black and white 128x64 display. As a bonus, this display has a resistive touchscreen attached to it already, so you can detect finger presses anywhere on the screen.![](https://cdn-learn.adafruit.com/assets/assets/000/003/025/medium800/lcds___displays_28tfttouchbreakoutwoof_LRG.jpg?1396790412)

This display has a controller built into it with RAM buffering, so that almost no work is done by the microcontroller. You'll need 8 digital data lines and 4 or 5 digital control lines to read and write to the display (12 lines total). 4 pins are required for the touch screen (2 digital, 2 analog) but because of the way resistive touch screens work, we can share pins with the LCD so the entire setup can be run by 12 pins (10 digital, 2 analog).  
  
Of course, we wouldn't just leave you with a datasheet and a "good luck!" - [we've written a full open source graphics library that can draw pixels, lines, rectangles, circles and text](https://github.com/adafruit/TFTLCD-Library) . We[also have a touch screen library that detects x, y and z (pressure)](https://github.com/adafruit/Touch-Screen-Library) and example code to demonstrate all of it. The code is written for Arduino but can be easily ported to your favorite microcontroller!  
  
 **[Pick one up today at the Adafruit Shop!](http://www.adafruit.com/index.php?main_page=product_info&cPath=37&products_id=335)**  
  
**Specifications:**
- 2.8" diagonal LCD TFT display
- 240x320 resolution, 16-bit (262,000) color
- [ILI9325 (datasheet)](http://www.adafruit.com/datasheets/ILI9325.pdf) or [ILI9328 (datasheet)](http://www.adafruit.com/datasheets/ILI9328.pdf) controller with built in video RAM buffer
- 8 bit digital interface, plus 4 or 5 control lines
- 5V compatible! Use with 3.3V or 5V logic
- Onboard 3.3V @ 150mA LDO regulator
- 4 white LED backlight, transistor connected so you can PWM dim the backlight
- 1x20 header for easy breadboarding, or 2x10 header for cable connection
- 4 x 0.125"/3mm mounting holes with tabs
- 4-wire resistive touchscreen

![](https://cdn-learn.adafruit.com/assets/assets/000/003/026/medium800/lcds___displays_headerready.jpg?1396790423)

![](https://cdn-learn.adafruit.com/assets/assets/000/003/027/medium800/lcds___displays_tftbackv.jpg?1396790433)

 **This guide is specifically for the TFT LCD** <u><b>breakout board</b></u> **. There's a** [**separate tutorial for the Arduino shield**](http://learn.adafruit.com/2-8-tft-touch-shield) **version of this display.**  
- [Next Page](https://learn.adafruit.com/2-8-tft-touchscreen/connection-options.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
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
### MicroSD card breakout board+

[MicroSD card breakout board+](https://www.adafruit.com/product/254)
Not just a simple breakout board, this microSD adapter goes the extra mile - designed for ease of use.

- Onboard 5v-\>3v regulator provides 150mA for power-hungry cards
- 3v level shifting means you can use this with ease on either 3v or 5v systems
- Uses a proper level...

In Stock
[Buy Now](https://www.adafruit.com/product/254)
[Related Guides to the Product](https://learn.adafruit.com/products/254/guides)

## Related Guides

- [Adafruit Motor Shield](https://learn.adafruit.com/adafruit-motor-shield.md)
- [Photocells](https://learn.adafruit.com/photocells.md)
- [Circuit Playground: D is for Diode](https://learn.adafruit.com/circuit-playground-d-is-for-diode.md)
- [Micro SD Card Breakout Board Tutorial](https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial.md)
- [0.96" mini Color OLED](https://learn.adafruit.com/096-mini-color-oled.md)
- [Halloween Pumpkin](https://learn.adafruit.com/halloween-pumpkin.md)
- [Multi-tasking the Arduino - Part 1](https://learn.adafruit.com/multi-tasking-the-arduino-part-1.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [Arduino Lesson 3. RGB LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [TTL Serial Camera](https://learn.adafruit.com/ttl-serial-camera.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [All About Arduino Libraries](https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use.md)
