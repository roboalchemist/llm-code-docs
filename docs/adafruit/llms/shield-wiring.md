# Source: https://learn.adafruit.com/adafruit-pn532-rfid-nfc/shield-wiring.md

# Adafruit PN532 RFID/NFC Breakout and Shield

## Shield Wiring

## Solder the Headers
The first step is to solder the headers to the shield. Cut the header strip to length and insert the sections (long pins down) into an Arduino. Then place the shield on top and solder each pin.  
![](https://cdn-learn.adafruit.com/assets/assets/000/004/691/medium800/rfid___nfc_2013_03_01_IMG_1311-1024.jpg?1396815638)

![](https://cdn-learn.adafruit.com/assets/assets/000/003/272/medium800/rfid___nfc_ID789_LRG.jpg?1396794689)

## Using the Adafruit NFC Shield with I2C
The Adafruit NFC shield is designed to be used using the I2C by default. I2C only uses two pins (Analog 4 and 5 which are fixed in hardware and cannot be changed) to communicate and one pin as an 'interrupt' pin (Digital 2 - can be changed however). What is nice about I2C is that it is a 'shared' bus - unlike SPI and TTL serial - so you can put as many sensors as you'd like all on the same two pins, as long as their addresses don't collide/conflict. The Interrupt pin is handy because instead of constantly asking the NFC shield "is there a card in view yet? what about now?" constantly, the chip will alert us when a NFC target comes into the antenna range.  
  
The shield is drop-in compatible with any Classic Arduino (UNO, Duemilanove, Diecimilla, etc using the ATmega168 or '328) as well as any Mega R3 or later.   
  
[Mega R2 Arduinos work as well but you need to solder a wire from the](http://arduino.cc/en/Main/ArduinoBoardMega "Link: http://arduino.cc/en/Main/ArduinoBoardMega")**[SDA](http://arduino.cc/en/Main/ArduinoBoardMega)**[and&nbsp;](http://arduino.cc/en/Main/ArduinoBoardMega)**[SCL](http://arduino.cc/en/Main/ArduinoBoardMega)**[pin holes to the Mega's I2C pins on Digital #20 and #21](http://arduino.cc/en/Main/ArduinoBoardMega "Link: http://arduino.cc/en/Main/ArduinoBoardMega")  
# Using with the Arduino Leonardo and Yun
Info: 

Here are some photos of setting the IRQ pin to digital 6. First, use a sharp hobby knife to cut the trace from IRQ to 2

![](https://cdn-learn.adafruit.com/assets/assets/000/003/273/medium800/rfid___nfc_Screen_Shot_2012-08-01_at_6.23.03_PM.png?1396794774)

Solder a wire from IRQ to #6

![](https://cdn-learn.adafruit.com/assets/assets/000/003/274/medium800/rfid___nfc_Screen_Shot_2012-08-01_at_6.23.41_PM.png?1396794857)

- [Previous Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/breakout-wiring.md)
- [Next Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/arduino-library.md)

## Featured Products

### PN532 NFC/RFID controller breakout board

[PN532 NFC/RFID controller breakout board](https://www.adafruit.com/product/364)
The PN532 is the most popular NFC chip, and is what is embedded in pretty much every phone or device that does NFC. It can pretty much do it all, such as read and write to tags and cards, communicate with phones (say for payment processing), and 'act' like a NFC tag. If you want to do...

Out of Stock
[Buy Now](https://www.adafruit.com/product/364)
[Related Guides to the Product](https://learn.adafruit.com/products/364/guides)
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
### Adafruit PN532 NFC/RFID Controller Shield for Arduino + Extras

[Adafruit PN532 NFC/RFID Controller Shield for Arduino + Extras](https://www.adafruit.com/product/789)
We've taken our popular Adafruit PN532 breakout board and turned it into a shield - the perfect tool for any 13.56MHz RFID or NFC application. The Adafruit NFC shield uses the PN532 chip-set (the most popular NFC chip on the market) and is what is embedded in pretty much every phone or...

In Stock
[Buy Now](https://www.adafruit.com/product/789)
[Related Guides to the Product](https://learn.adafruit.com/products/789/guides)
### 13.56MHz RFID/NFC Card - Classic 1K

[13.56MHz RFID/NFC Card - Classic 1K](https://www.adafruit.com/product/359)
This is a blank 13.56MHz RFID/NFC card - often used for train/bus passes but also found in other systems where a proximity card is desired. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be...

In Stock
[Buy Now](https://www.adafruit.com/product/359)
[Related Guides to the Product](https://learn.adafruit.com/products/359/guides)
### 13.56MHz RFID/NFC White Tag - Classic 1K

[13.56MHz RFID/NFC White Tag - Classic 1K](https://www.adafruit.com/product/360)
This is a blank 13.56MHz RFID/NFC laundry tag&nbsp;- often used for laundry but also general tagging. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be read by almost any 13.56MHz RFID/NFC...

In Stock
[Buy Now](https://www.adafruit.com/product/360)
[Related Guides to the Product](https://learn.adafruit.com/products/360/guides)
### 13.56MHz RFID/NFC Clear Tag - Classic 1K

[13.56MHz RFID/NFC Clear Tag - Classic 1K](https://www.adafruit.com/product/361)
This is a blank 13.56MHz Classic 'laundry' tag - often used for laundry or identification but also found in other systems where a small proximity card is desired. This one is clear! &nbsp;The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer...

In Stock
[Buy Now](https://www.adafruit.com/product/361)
[Related Guides to the Product](https://learn.adafruit.com/products/361/guides)
### 13.56MHz RFID/NFC Sticker - Classic 1K

[13.56MHz RFID/NFC Sticker - Classic 1K](https://www.adafruit.com/product/362)
This is a blank 13.56MHz RFID/NFC sticker&nbsp;- often used for inventory uses but also wherever a sticker is desired. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be read by almost any...

In Stock
[Buy Now](https://www.adafruit.com/product/362)
[Related Guides to the Product](https://learn.adafruit.com/products/362/guides)

## Related Guides

- [How to Choose a Microcontroller](https://learn.adafruit.com/how-to-choose-a-microcontroller.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [Naughty or Nice Machine](https://learn.adafruit.com/naughty-or-nice-machine.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [Adafruit INA219 Current Sensor Breakout](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout.md)
- [Low Power Coin Cell Voltage Logger](https://learn.adafruit.com/low-power-coin-cell-voltage-logger.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [Adafruit Ultimate GPS Logger Shield](https://learn.adafruit.com/adafruit-ultimate-gps-logger-shield.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [Mini Thermal Receipt Printers](https://learn.adafruit.com/mini-thermal-receipt-printer.md)
- [Arduino Prototyping Mounting Plate](https://learn.adafruit.com/arduino-prototyping-mounting-plate.md)
- [LED Lightbox](https://learn.adafruit.com/led-lightbox.md)
- [NFC Ring Password Helper](https://learn.adafruit.com/nfc-ring-password-helper.md)
