# Source: https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/testing-it-out.md

# Adafruit NFC/RFID on Raspberry Pi

## Testing it Out

# Hooking Everything Up

The Adafruit [NFC Breakout](https://www.adafruit.com/products/364) board is much more appropriate with the Pi than the [NFC Shield](https://www.adafruit.com/products/789 "Link: https://www.adafruit.com/products/789"), since the breakout doesn't have 5V level shifting (which means you won't accidentally damage your Pi!), and you have easier access to the bus select pins, etc.  
  
If it isn't already hooked up,&nbsp;you can connect your breakout&nbsp;now using&nbsp;a convenient [Pi Cobbler](http://adafruit.com/products/914), following the image below: There are two places to do this: either the board end header (fits more nicely in a breadboard), or the FTDI header along one side (shown in photo below):

![](https://cdn-learn.adafruit.com/assets/assets/000/001/533/medium800/raspberry_pi_NFCBreakout_Pi_Hookup_1000w.jpg?1396773171)

 **Note:** Make sure that the **SEL0** and **SEL1** jumpers on the NFC breakout are set to **OFF** , which will cause the PN532 to boot into UART mode (rather than SPI and I2C, which aren't currently supported by libnfc). &nbsp;You will need to reset the breakout after changing these pins, which you can do by cycling the power pin.  
  
Use a 5V supply pin from the Pi, and the 5V input on either the FTDI header or board end header, rather than the Pi’s 3.3V supply, since the 3.3V supply is used by the core on the Raspberry Pi and you don't want to pull sharp, heavy loads from it, like when you first enable and charge the near field.

# Read an ISO14443-A (Mifare, etc.) Card with nfc-poll

With libnfc configured, built and installed, you can go back to the command-line, place a card on the reader, and run the following command to get the tags unique ID:

```auto
nfc-poll
```

_nfc-poll should be able to run this way thanks to the “make install” step on the prior page, which puts it in the /user/bin directory. If it doesn’t run, check if you did the install step, or you can find the executable program in&nbsp;__~/libnfc/examples_

A successful run will yield the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/511/medium800/raspberry_pi_5_nfc_poll.png?1396773578)

That's it! &nbsp;From here, you can explore some of the other examples in the 'examples' folder, and&nbsp;figure out how to get started writing your own applications based on libnfc! &nbsp;Be sure to have a look at the [libnfc project page](https://github.com/nfc-tools/libnfc "Link: http://www.libnfc.org/documentation/introduction").

## Common Issues

If nfc-poll returns this message:

**pn53x\_check\_communication error**

The culprit is usually one of two things:

- Try swapping the RX and TX wires.
- The particular model of Pi might be an exception to the “Recent” vs “Earlier” rules on the previous page. If the wire swap didn’t fix the issue, try using the opposite library setup steps…do a “make clean” first so that everything’s rebuilt.

- [Previous Page](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/building-libnfc.md)

## Featured Products

### 13.56MHz RFID/NFC tag assortment - Classic 1K

[13.56MHz RFID/NFC tag assortment - Classic 1K](https://www.adafruit.com/product/365)
One of each of our favorite 13.56MHz RFID/NFC Classic 1K tags - 5 in total!

- [Credit card size](http://www.adafruit.com/products/359)
- [1" diameter 'laundry' clear tag](http://www.adafruit.com/products/361)
- <a...></a...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/365)
[Related Guides to the Product](https://learn.adafruit.com/products/365/guides)
### 13.56MHz RFID/NFC Clear Keychain Fob - Classic 1K

[13.56MHz RFID/NFC Clear Keychain Fob - Classic 1K](https://www.adafruit.com/product/363)
This is a blank 13.56MHz RFID/NFC keychain fob - often used for keys but also an easy way to tag something. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be read by almost any 13.56MHz...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/363)
[Related Guides to the Product](https://learn.adafruit.com/products/363/guides)
### 13.56MHz RFID/NFC Bracelet - Classic 1K

[13.56MHz RFID/NFC Bracelet - Classic 1K](https://www.adafruit.com/product/921)
This is a blank 13.56MHz RFID/NFC silicone bracelet. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be read by almost any 13.56MHz RFID/NFC reader but make sure it can handle&nbsp;ISO/IEC...

In Stock
[Buy Now](https://www.adafruit.com/product/921)
[Related Guides to the Product](https://learn.adafruit.com/products/921/guides)
### 13.56MHz RFID/NFC Charm - Classic 1K

[13.56MHz RFID/NFC Charm - Classic 1K](https://www.adafruit.com/product/884)
This is a blank 13.56MHz RFID/NFC embedded in a phone charm&nbsp;- often used for train/bus passes but also found in other systems where a proximity card is desired. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/884)
[Related Guides to the Product](https://learn.adafruit.com/products/884/guides)
### 13.56MHz RFID/NFC Clear Tag - Classic 1K

[13.56MHz RFID/NFC Clear Tag - Classic 1K](https://www.adafruit.com/product/361)
This is a blank 13.56MHz Classic 'laundry' tag - often used for laundry or identification but also found in other systems where a small proximity card is desired. This one is clear! &nbsp;The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer...

In Stock
[Buy Now](https://www.adafruit.com/product/361)
[Related Guides to the Product](https://learn.adafruit.com/products/361/guides)
### 13.56MHz RFID/NFC White Tag - Classic 1K

[13.56MHz RFID/NFC White Tag - Classic 1K](https://www.adafruit.com/product/360)
This is a blank 13.56MHz RFID/NFC laundry tag&nbsp;- often used for laundry but also general tagging. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be read by almost any 13.56MHz RFID/NFC...

In Stock
[Buy Now](https://www.adafruit.com/product/360)
[Related Guides to the Product](https://learn.adafruit.com/products/360/guides)
### 13.56MHz RFID/NFC Card - Classic 1K

[13.56MHz RFID/NFC Card - Classic 1K](https://www.adafruit.com/product/359)
This is a blank 13.56MHz RFID/NFC card - often used for train/bus passes but also found in other systems where a proximity card is desired. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be...

In Stock
[Buy Now](https://www.adafruit.com/product/359)
[Related Guides to the Product](https://learn.adafruit.com/products/359/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)

## Related Guides

- [Collin's Lab: RFID](https://learn.adafruit.com/collins-lab-rfid.md)
- [Mystery Box: Remote Chess Board Puzzle Lock](https://learn.adafruit.com/mystery-box-remote-chess-board-puzzle-lock.md)
- [Raspberry Pi NFC Minecraft Blocks](https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks.md)
- [Adafruit PN532 RFID/NFC Breakout and Shield](https://learn.adafruit.com/adafruit-pn532-rfid-nfc.md)
- [NFC Raspberry Pi Media Player](https://learn.adafruit.com/nfc-raspberry-pi-media-player.md)
- [I2C Addresses and Troublesome Chips](https://learn.adafruit.com/i2c-addresses.md)
- [Magic Band Teardown](https://learn.adafruit.com/magic-band-teardown.md)
- [Adafruit DPI Display Kippah](https://learn.adafruit.com/adafruit-dpi-display-kippah-ttl-tft.md)
- [Set up Home Assistant with a Raspberry Pi](https://learn.adafruit.com/set-up-home-assistant-with-a-raspberry-pi.md)
- [Adafruit 2.4" PiTFT HAT with Resistive Touchscreen Mini Kit](https://learn.adafruit.com/adafruit-2-4-pitft-hat-with-resistive-touchscreen-mini-kit.md)
- [Adafruit 16-Channel PWM/Servo HAT & Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi.md)
- [Mini Raspberry Pi Handheld Notebook](https://learn.adafruit.com/mini-raspberry-pi-handheld-notebook-palmtop.md)
- [Bonjour (Zeroconf) Networking for Windows and Linux](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux.md)
- [Mini Smart Home with Huzzah, HASSio and Crickit](https://learn.adafruit.com/mini-smart-home-with-esp8266-huzzah-feather-raspberry-pi-hassio-crickit.md)
- [Programming Microcontrollers using OpenOCD on a Raspberry Pi](https://learn.adafruit.com/programming-microcontrollers-using-openocd-on-raspberry-pi.md)
