# Source: https://learn.adafruit.com/adafruit-pn532-rfid-nfc/about-nfc.md

# Adafruit PN532 RFID/NFC Breakout and Shield

## About NFC

## NFC (Near Field Communication)
NFC (Near Field Communication) is a set of short-range (typically up to 10cm) wireless communication technologies designed to offer light-weight and secure communication between two devices. While NFC was invented by NXP (Phillips at the time), Nokia and Sony, the main body behind the NFC 'standard' today is the [NFC Forum](http://www.nfc-forum.org/home/ "Link: http://www.nfc-forum.org/home/"), who are responsible for publishing and maintaining a variety of standards relating to NFC technology.  
  
NFC operates at 13.56MHz, and is based around an "initiator" and "target" model where the initiator generates a small magnetic field that powers the target, meaning that the target does not require a power source. This means of communication is referred to as **Passive Communication** , and is used to read and write to small, inexpensive 13.56MHz RFID tags based on standards like ISO14443A. **Active communication** (peer-to-peer) is also possible when both devices are powered, where each device alternately creates its own magentic field, with the secondary device as a target and vice versa in continuous rotation.## Passive Communication: ISO14443A Cards (Mifare, etc.)
While the PN53x family of transceivers from NXP are compatible with a number of 13.56MHz RFID card standards, by far the most popular standard is ISO14443A. A variety of manufacturers produce ISO14443A compatible cards or chips, but the most common are based around the **Mifare** family from NXP. Mifare Classic and Mifare Ultralight are probably the most frequently encountered and useful for basic projects, though many tags with improved security and encryption also exist (Mifare DESFire, etc.). All of the tags sold at adafruit.com are Mifare Classic 1K, meaning that they contains 1K (1024 bytes) of programmable EEPROM memory which can be read and modified in passive mode by the initiator device (the PN532).  
  
While all ISO14443A cards share certain common characteristics on the highest level (defined by the four part standard), each set of Mifare chips (Classic, Ultralight, Plus, DESFire, etc.) has it's own features and peculiarities. The two most common formats are described below.  

- [Mifare Classic](http://learn.adafruit.com/adafruit-pn532-rfid-nfc "Link: http://learn.adafruit.com/adafruit-pn532-rfid-nfc"): These cards are extremely common, and contain 1K or 4K of EEPROM, with basic security for each 64 byte (1K/4K cards) or 256 byte (4K cards) sector.
- [Mifare Ultralight](http://learn.adafruit.com/adafruit-pn532-rfid-nfc): Contains 512 bytes of EEPROM, including 32-bits of OTP memory. These tags are inexpensive, often come in sticker format and are are frequently used for transportation ticketing, concert tickets, etc.

## Active Communication (Peer-to-Peer)
Active or "Peer-to-Peer" communication is still based around the Initiator/Target model described earlier, but both devices are actively powered and switch roles from being an Initiator or a Target during the communication. When one device is initiating a conversation with the other, it enables it's magnetic field and the receiving device listens in (with it's own magnetic field disabled). Afterwards, the target/recipient device may need to respond and will in turn activate it's own magnetic field and the original device will be configured as the target. Despite two devices being present, only one magnetic field is active at a time, with each device constantly enabling or disabling its own magnetic field.  
  
ToDo: Add better description of active mode, but I need to test it out a bit first myself!  
## NFC Data Exchange Format (NDEF)
The NFC Data Exchange Format (NDEF) is a standardised data format that can be used to exchange information between any compatible NFC device and another NFC device or tag. The data format consists of **NDEF Messages** and **NDEF Records**. The standard is maintained by the NFC Forum and is freely available for consultation but requires accepting a license agreement to [download](http://www.nfc-forum.org/specs/spec_list/).  
  
The NDEF format is used to store and exchange information like URIs, plain text, etc., using a commonly understood format. NFC tags like Mifare Classic cards can be configured as NDEF tags, and data written to them by one NFC device (NDEF Records) can be understood and accessed by any other NDEF compatible device. NDEF messages can also be used to exchange data between two active NFC devices in "peer-to-peer" mode. By adhering to the NDEF data exchange format during communication, devices that would otherwise have no meaningful knowledge of each other or common language are able to share data in an organised, mutually understandable manner.  
  
The NDEF standard includes numerous **Record Type Definitions (RTDs)** that define how information like URIs should be stored, and each NDEF device, tag or message can contained multiple RTDs. Standard RTD definitions are described in "NFC Record Type Definition (RTD) Specification” maintained by the NFC Forum.  
  
\* [NDEF Overview](http://learn.adafruit.com/adafruit-pn532-rfid-nfc): This page offers a more detailed explanation of NDEF, including how Mifare Classic cards can be used to store NDEF messages.  
  
**NOTE** : The dedicated NDEF page is still a work in progress and some information is currently incomplete.  
## Reading
For more details about NFC/RFID and this chip we suggest the following fantastic resources:
- [RFID selection guide](http://www.adafruit.com/datasheets/rfid%20guide.pdf "Link: http://www.adafruit.com/datasheets/rfid%20guide.pdf") - a lot of details about RFID in general
- [Nokia's Introduction to NFC&nbsp;](http://www.adafruit.com/datasheets/Introduction_to_NFC_v1_0_en.pdf)- a lot of details about NFC in general
- [NXP S50 chip datasheet](http://www.adafruit.com/datasheets/S50.pdf "Link: http://www.adafruit.com/datasheets/S50.pdf")&nbsp;, the chip&nbsp;_inside_&nbsp;MiFare classic tags
- [NXP PN532 Short Form Datasheet](http://www.adafruit.com/datasheets/pn532ds.pdf "Link: http://www.adafruit.com/datasheets/pn532ds.pdf")
- [NXP PN532 Long Form Datasheet](http://www.adafruit.com/datasheets/pn532longds.pdf)
- [NXP PN532 User Manual](http://www.adafruit.com/datasheets/pn532um.pdf "Link: http://www.adafruit.com/datasheets/pn532um.pdf")
- [NXP PN532 App Note](http://www.adafruit.com/datasheets/PN532C106_Application%20Note_v1.2.pdf)
- [Using PN532 with libnfc](http://www.microbuilder.eu/Blog/11-02-19/Using_libnfc_with_the_PN532_Linux.aspx "Link: http://www.microbuilder.eu/Blog/11-02-19/Using\_libnfc\_with\_the\_PN532\_Linux.aspx")

- [NFC Glossary](http://www.nfc-research.at/index.php?id=40)

- [Previous Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/python-circuitpython.md)
- [Next Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/mifare.md)

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
