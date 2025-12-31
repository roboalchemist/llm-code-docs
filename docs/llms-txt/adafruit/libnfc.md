# Source: https://learn.adafruit.com/adafruit-pn532-rfid-nfc/libnfc.md

# Adafruit PN532 RFID/NFC Breakout and Shield

## Using with LibNFC

Warning: 

## Using the PN532 Breakout Boards with libnfc

[libnfc](https://github.com/nfc-tools/libnfc)&nbsp;is a mature, cross-platform, open-source NFC library that can be easily configured to work with the PN532 Breakout Board. While Linux is probably the easiest platform to use libnfc with, it can be configured for the Mac and Windows as well, though you may need to dig around on the libnfc Community Forums for some specific details on compiling .dlls for Windows, etc.  
  
If you want to test the PN532 Breakout Board out with libnfc, this simple tutorial should walk you through the absolute basics of compiling and configuring libnfc, and using some of the canned example SW included in the library.

Danger: 

# libnfc In Linux (Ubuntu 10.10 used in this example)

## Step One: Download libnfc

Download the latest version of [libnfc from GitHub](https://github.com/nfc-tools/libnfc) (ex. "libnfc-1.4.1.tar.gz") and extract the contents of the file as follows:

```
  $ wget http://libnfc.googlecode.com/files/libnfc-x.x.x.tar.gz
  $ tar -xvzf libnfc-x.x.x.tar.gz
  $ cd libnfc-x.x.x
```

## Step Two: Configure libnfc for PN532 and UART
libnfc currently only supports communication over UART, using any inexpensive USB to UART adapter like the FTDI Friend or a TTL FTDI cable. Before compiling, however, you will need to configure libnfc to include support for UART and the PN532 chipset, which can be done with the following commmand (executing in the folder where the above archive was unzipped):  
```
  $ ./configure --with-drivers=pn532_uart --enable-serial-autoprobe
```

 **Note** : If you also wish to include debug output, you can add the '–enable-serial-autoprobe' flag (minus the single quotes) to the configure options ![](https://cdn-learn.adafruit.com/assets/assets/000/002/733/medium800/rfid___nfc_libnfc_configure_600w.jpg?1396786403)

## Step Three: Build and install libnfc
You can build and install libnfc with the following three commands, also run from the folder where the original archive was unzipped:  
```
  $ make clean
  $ make
  $ make install
```

## Step Four: Check for installed devices
Now that libnfc is (hopefully) built and installed, you can run the 'nfc-list' example to try to detect an attached NFC board. Make sure the board is connected to the FTDI or USB/UART adapter, and that it is connected to your PC, and run the following commands:  
```
  $ cd examples
  $ ./nfc-list
```

This should list the devices that were detected## Step Five: Poll for an ISO14443A (Mifare, etc.) Card
Next, you can use the 'nfc-poll' example to wait 30 seconds for an ISO14443A card or tag and display some basic information about this card. In the examples folder that we changed to above, run the following command:  
```
  $ ./nfc-poll
```

This should give you some basic information on any card that entered the magnetic field within the specified delay.![](https://cdn-learn.adafruit.com/assets/assets/000/002/736/medium800/rfid___nfc_libnfc_poll_600w.jpg?1396786447)

# libnfc With Mac OSX Lion
scott-42 was kind of enough to post some tips on getting libnfc working on a Mac using an FTDI adapter. A couple simple changes to the code were required (as of v1.6.0-rc1), with the details&nbsp;[here](http://forums.adafruit.com/viewtopic.php?f=19&t=22085#p115684).  
  
Keeping in mind the code changes mentionned above, the following steps should get libnfc compiling and working via an FTDI type adapter and UART on Lion (using libnfc 1.6.0\_rc1):  
## Download and build libnfc and configure if for PN532 UART (making the code changes above before running&nbsp;make):
```
  wget http://libnfc.googlecode.com/files/libnfc-1.6.0-rc1.tar.gz
  tar -xvzf libnfc-1.6.0-rc1.tar.gz
  cd libnfc-1.6.0-rc1
  ./configure --with-drivers=pn532_uart --enable-serial-autoprobe
  sudo make
  sudo make install
```

## If everything worked out, switch to the examples folder and see if you can find the PN532 and wait for an appropriate tag:
```
  cd examples
  Kevins-Mac-mini:examples kevin$ ./nfc-poll
  /Users/kevin/libnfc-1.6.0-rc1/examples/.libs/nfc-poll uses libnfc 1.6.0-rc1 (r1326)
  NFC reader: pn532_uart:/dev/tty.usbserial-FTE5WWPB - PN532 v1.6 (0x07) opened
  NFC device will poll during 30000 ms (20 pollings of 300 ms for 5 modulations)
  ISO/IEC 14443A (106 kbps) target:
      ATQA (SENS_RES): 00  04  
         UID (NFCID1): 3e  b9  6e  66  
         SAK (SEL_RES): 08
```

There are some dependencies to get libnfc running, but since it isn't an Adafruit project and we can't really support it directly ourselves, you will probably have better luck looking at the [libnfc forums](http://www.libnfc.org/community/) for Mac support. There are a few active users developping on the Mac.

- [Previous Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/ndef.md)
- [Next Page](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/faq.md)

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
