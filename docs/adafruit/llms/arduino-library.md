# Source: https://learn.adafruit.com/adafruit-pn532-rfid-nfc/arduino-library.md

# Adafruit PN532 RFID/NFC Breakout and Shield

## Arduino Library

## Which Library?

In the past there were two separate Arduino libraries for using the Adafruit NFC boards. &nbsp;One library supported the breakout over a SPI connection, and the other library supported the breakout or shield over an I2C connection. &nbsp;However both of these libraries have been merged into a single Arduino library, [Adafruit-PN532](https://github.com/adafruit/Adafruit-PN532/).

The Adafruit PN532 library&nbsp;has the ability to read MiFare cards, including the hard-coded ID numbers, as well as authenticate and read/write EEPROM chunks. &nbsp;It can work with both the breakout and shield using either a SPI or I2C connection.

## Library Installation

[Download the Adafruit PN532 library from github](https://github.com/adafruit/Adafruit-PN532). Uncompress the folder and rename the folder **Adafruit\_PN532**. Inside the folder you should see the **Adafruit\_PN532.cpp** and **Adafruit\_PN532.h** files. Install the **Adafruit\_PN532** library foler by placing it in your **_arduinosketchfolder_/libraries** folder. You may have to create the **libraries** subfolder if this is your first library. [You can read more about installing libraries in our tutorial](http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries).  
  
Restart the Arduino IDE. You should now be able to select **File \> Examples \> Adafruit\_PN532 \> readMifare** sketch.

**If you're using the NFC breakout with a SPI connection** that uses the wiring shown on previous pages you can immediately upload the sketch to the Arduino and&nbsp;skip down to the [Testing MiFare](../../../../adafruit-pn532-rfid-nfc/arduino-library#testing-mifare)&nbsp;section.

**If you're using the NFC shield, or are using the breakout with an I2C connection&nbsp;** then you must make a small change to configure the example for I2C. &nbsp;Scroll down to these lines near the top of the sketch:

```
// Uncomment just _one_ line below depending on how your breakout or shield
// is connected to the Arduino:

// Use this line for a breakout with a SPI connection:
Adafruit_PN532 nfc(PN532_SCK, PN532_MISO, PN532_MOSI, PN532_SS);

// Use this line for a breakout with a hardware SPI connection.  Note that
// the PN532 SCK, MOSI, and MISO pins need to be connected to the Arduino's
// hardware SPI SCK, MOSI, and MISO pins.  On an Arduino Uno these are
// SCK = 13, MOSI = 11, MISO = 12.  The SS line can be any digital IO pin.
//Adafruit_PN532 nfc(PN532_SS);

// Or use this line for a breakout or shield with an I2C connection:
//Adafruit_PN532 nfc(PN532_IRQ, PN532_RESET);
```

Change them so the second line is uncommented and the first line is commented. &nbsp;This will configure&nbsp;the sketch to make the library use I2C for communication with the NFC shield or breakout. &nbsp;The modified code should look like:

```
// Uncomment just _one_ line below depending on how your breakout or shield
// is connected to the Arduino:

// Use this line for a breakout with a SPI connection:
//Adafruit_PN532 nfc(PN532_SCK, PN532_MISO, PN532_MOSI, PN532_SS);

// Use this line for a breakout with a hardware SPI connection.  Note that
// the PN532 SCK, MOSI, and MISO pins need to be connected to the Arduino's
// hardware SPI SCK, MOSI, and MISO pins.  On an Arduino Uno these are
// SCK = 13, MOSI = 11, MISO = 12.  The SS line can be any digital IO pin.
//Adafruit_PN532 nfc(PN532_SS);

// Or use this line for a breakout or shield with an I2C connection:
Adafruit_PN532 nfc(PN532_IRQ, PN532_RESET);
```

Then upload the example to the&nbsp;Arduino and continue on. &nbsp; **Note that you need to make a similar change to pick the interface for any other NFC example from the library.**

## Testing MiFare
In the serial monitor, you should see that it found the **PN532** chip. Then you can place your tag nearby and it will display the 4 byte ID code (this one is 0xAE 0x4C 0xF0 0x6C) and then the integer version of all four bytes together. You can use this number to identify each card. Recently NXP made so many cards that they actually ran through all 4 Bytes (2^32) so the number is not guaranteed to be absolutely unique. However, the chances are extremely slim you will have two cards with the same ID so as long as you aren't using these cards for anything terribly important (like money transfer) its fine to use the number as a unique identifier  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/716/medium800/rfid___nfc_pn532test.gif?1448059596)

- [Previous Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/shield-wiring.md)
- [Next Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/python-circuitpython.md)

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
