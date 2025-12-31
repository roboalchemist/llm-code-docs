# Source: https://learn.adafruit.com/adafruit-pn532-rfid-nfc/breakout-wiring.md

# Adafruit PN532 RFID/NFC Breakout and Shield

## Breakout Wiring

This part of the tutorial is specifically for the Breakout board. We show how to use it with SPI. The breakout also supports TTL serial and I2C but we don't have a tutorial for using it that way as SPI is the most cross-platform method to communicate  
  
If you're using the shield, check the next page

![](https://cdn-learn.adafruit.com/assets/assets/000/003/271/medium800/rfid___nfc_pn532_LRG.jpg?1396794680)

## Wiring the Breakout for SPI
The PN532 chip and breakout is designed to be used by 3.3V systems. To use it with a 5V system such as an Arduino, a level shifter is required to convert the high voltages into 3.3V. If you have a 3.3V embedded system you won't have to use the shifter of course!  
  
To begin, we'll solder in the header to the breakout board. You'll need two small 3-pin pieces of header and one 8-pin piece. You can break these off of a large piece.  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/711/medium800/rfid___nfc_breakplier.jpg?1396786067)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/712/medium800/rfid___nfc_breakclip.jpg?1396786076)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/713/medium800/rfid___nfc_jumperheader.jpg?1396786081)

Solder the two small pieces to the&nbsp; **SEL0** &nbsp;and&nbsp; **SEL1** &nbsp;pads. These are interface selectors for the chip. Depending on how the jumpers are inserted the chip will talk in TTL serial, i2c or SPI_.&nbsp;_Also solder a strip to the end so you can plug it into a breadboard.![](https://cdn-learn.adafruit.com/assets/assets/000/002/714/medium800/rfid___nfc_header.jpg?1396786089)

Wire up the 4050 level shifter chip to the Arduino as shown. The notch in the 4050 is at the 'top' in this image.

- Arduino digital pin **2** is connected to 4050 pin **9** (orange wire)
- Arduino digital pin **3** is connected to 4050 pin **11** (yellow wire)
- Arduino digital pin **4** is connected to 4050 pin **14** (green wire)

On the breakout board

- **3.3Vin** is connected to the Arduino **3.3V** pn
- **SCK** is connected to 4050 pin **10** (orange wire)
- **MISO** is connected to Arduino pin **5** (blue wire)
- **MOSI** is connected to 4050 pin **12** (yellow wire)
- **SSEL** is connected to 4050 pin **15&** (green wire)
- **GND** connects to Arduino **ground** (black wire)

Also connect 4050 pin #1 to **3.3V** and pin #8 to **ground**.

Click to see a larger image. The red power wire should be connected to the **3.3v** pin on the Arduino!

![](https://cdn-learn.adafruit.com/assets/assets/000/002/715/medium800/rfid___nfc_pn532wiring.jpg?1396786098)

Also, we need to select SPI as the interface so on **SEL1** place the jumper in the **ON** position. for **SEL0** place the jumper in the **OFF** position.  
  
That's it! Later on you can change what Arduino pins you are using but for the beginning test we suggest matching our wiring.

Danger: 

- [Previous Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/overview.md)
- [Next Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/shield-wiring.md)

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
