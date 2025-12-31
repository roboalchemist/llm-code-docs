# Source: https://learn.adafruit.com/low-power-coin-cell-voltage-logger/other-lessons.md

# Low Power Coin Cell Voltage Logger

## Other Lessons

![](https://cdn-learn.adafruit.com/assets/assets/000/002/709/medium800/microcontrollers_bluesmoke.png?1396786057)

The key to making TIMESQUARE practical was to trim the power-down current as much as possible. Certainly, the running current is important too, but&nbsp;the power-down state is where the watch will spend most of its time by far. There may be idle times&nbsp;when it’s left in a drawer for days or weeks…maybe even months, though we hope not…and it has only a single coin cell to draw from. As you can imagine, considerable effort was spent testing and measuring&nbsp;sleep modes and disabling every possible peripheral to reduce the idle current.  
  
One of the more power-hungry peripherals on the ATmega 328P is the _brown-out detect_ circuit, which senses a low voltage condition and calls an interrupt function, the _brown-out reset_ (BOR) handler. This feature is used in products&nbsp;for such things as storing state information in EEPROM before gracefully shutting down. The BOR circuit is enabled by default on the Arduino…and this is very important.  
  
Certain Atmel chips…the 328P among them…can disable the brownout circuit in software (rather than&nbsp;configuration fuses), potentially saving many microamps of current. <u>If</u> you’re programming a “raw” chip via the ISP header, that’s fantastic…if you need to save every last bit of power, and <u>if</u> you don’t need the brownout detection, have at it. But if you’re using a bootloader-based programming system like Arduino, <u>disabling BOR can have disastrous results!</u>  
  
As the supply voltage dips below the brownout threshold, without BOR the chip will start to behave erratically, and may spontaneously jump to <u>any</u>&nbsp;random memory location. And if that code eventually leads into any bootloader function that erases or writes a flash page, the application — or much worse, the bootloader itself — can become corrupted, leaving no easy way to re-flash the watch.  
  
This is NOT the unlikely one-in-a-million change you might think!&nbsp;First, the watch WILL repeatedly brown out any time the battery runs low.&nbsp;Second, keep in mind that it _doesn’t_ have to jump _exactly_ to the start of a block-erasing function, just to any code that may _eventually_ lead there.&nbsp;The odds of this happening during an unprotected brownout seem to be about 1 percent…the phenomenon has been observed in the wild with other projects and even while developing this code…it’s a real thing! So BOR is left enabled to provide a proper safety net. If you’re programming for an Arduino bootloader-based board, you should too.  
  
Really, resist the allure of the nano-amps,&nbsp;DO NOT go blindly adding BOR-disabling code to your project, you'll regret it later. Just don't. Okay? Don't. Thanks.

- [Previous Page](https://learn.adafruit.com/low-power-coin-cell-voltage-logger/results.md)

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
