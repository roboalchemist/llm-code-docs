# Source: https://learn.adafruit.com/diy-8x2-lcd-shield/headers-and-wiring.md

# DIY 8x2 LCD Shield

## Headers and Wiring

![](https://cdn-learn.adafruit.com/assets/assets/000/000/953/medium800/lcds___displays_headersprep.jpg?1396767377)

OK now that we are diagrammed out, I took the protoshield and soldered 2 7-pin headers at one end of the pcb. Note that they are not all the way to the edge, I left one row of holes so I could easily solder some wires. I also soldered a short piece of header (that comes with the shield kit) at the left so that the LCD will be propped up.![](https://cdn-learn.adafruit.com/assets/assets/000/000/954/medium800/lcds___displays_testfit.jpg?1396767385)

You can now do a test fit to verify how it will look. it hangs over a bit but thats OK by me.## Wiring the LCD
Since this is a parallel LCD, data will be sent to it over a&nbsp;_parallel&nbsp;_interface. That is, multiple bits at a time. These LCDs are designed for either a 8-bit or 4-bit interface. Since we'd like to save pins, lets go with the 4-bit interface! The data pins are name&nbsp; **D4** ,&nbsp; **D5** ,&nbsp; **D6** , and&nbsp; **D7**. Double-check your datasheet but almost all parallel LCDs have these pins numbered 4, 3, 2, and 1 respectively.  
| **1 (D7)** | **2 (D6)** |
| --- | --- |
| **3 (D5)** | **4 (D4)** |
| --- | --- |
| **5** | **6** |
| --- | --- |
| **7** | **8** |
| --- | --- |
| **9 (ENABLE)** | **10 (R/W)** |
| --- | --- |
| **11 (RS)** | **12 (CONTRAST)** |
| --- | --- |
| **13 (GND/VSS)** | **14 (+5V/VDD)** |
| --- | --- |

There's a lot of wiring to be done but we're going to go thru it very slowly so it shouldn't be too bad.

Lets connect these to the arduino thusly: D4 -\> Arduino pin #7, D5 -\> Arduino pin #8, D6 -\> Arduino pin #9, D7 -\> Arduino pin #10.

![lcds___displays_datawires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/956/medium640/lcds___displays_datawires.jpg?1396767397)

Since I wasnt sure of the wiring, I used the sockets on the protoshield. Once I test and verify they are correct, I'll solder them in!

Next are the two power wires. Parallel LCDs run off of +5V so you can just solder the Vcc wire to 5V and the ground wire to GND.

![lcds___displays_powerwires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/957/medium640/lcds___displays_powerwires.jpg?1396767404)

Next are the 2 control wires,&nbsp; **ENABLE** &nbsp;and&nbsp; **RS** &nbsp;which we connect to pins 12 and 11 respectively.![lcds___displays_controlwires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/958/medium640/lcds___displays_controlwires.jpg?1396767411)

Theres another control line called&nbsp; **R/W** &nbsp;that you can use to control whether you're reading or writing to the LCD. Since we'll just be writing, that pin can be connected to ground, saving another arduino pin.![lcds___displays_rwline.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/959/medium640/lcds___displays_rwline.jpg?1396767419)

The last wire is the contrast control, we need to connect a potentiometer to this to make the display visible. I dont know the specifics of the input current but I used a 10K potentiometer and it worked great.

One pin is connected to +5V, the pin on the other side is connected to ground and the middle pin is connected to the contrast line.

![lcds___displays_contrastpot.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/960/medium640/lcds___displays_contrastpot.jpg?1396767427)

Now place the LCD on top. Looks good!![lcds___displays_lcdplaced.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/961/medium640/lcds___displays_lcdplaced.jpg?1396767432)

Make sure you finish up the rest of the shield so you can plug it into an arduino. At least solder in the male headers.- [Previous Page](https://learn.adafruit.com/diy-8x2-lcd-shield/check-out-the-pins.md)
- [Next Page](https://learn.adafruit.com/diy-8x2-lcd-shield/using-the-lcd-shield.md)

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

- [Ladyada's Learn Arduino - Lesson #1](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-1.md)
- [Adafruit IO Basics: NeoPixel Controller](https://learn.adafruit.com/adafruit-io-basics-neopixel-controller.md)
- [Ladyada's Learn Arduino - Lesson #2](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-2.md)
- [Wave Shield](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino.md)
- [Adafruit Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps.md)
- [36mm LED Pixels](https://learn.adafruit.com/36mm-led-pixels.md)
- [Sending an SMS with Temboo](https://learn.adafruit.com/sending-an-sms-with-temboo.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [WiFi Controlled Mobile Robot](https://learn.adafruit.com/wifi-controlled-mobile-robot.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Adafruit Motor Shield](https://learn.adafruit.com/adafruit-motor-shield.md)
- [Arduino Lesson 16. Stepper Motors](https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors.md)
- [Trainable Robotic Arm](https://learn.adafruit.com/trainable-robotic-arm.md)
