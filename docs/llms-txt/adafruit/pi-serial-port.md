# Source: https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/pi-serial-port.md

# Adafruit NFC/RFID on Raspberry Pi

## Pi Serial Port

The easiest way to use libnfc with the Adafruit NFC Breakout is via _serial UART,_ since it's well-supported by libnfc out of the box. Unfortunately the serial UART port on the Pi is already dedicated to other purposes, and needs to be freed up for libnfc…  
  
The following steps (based on a clean Raspberry Pi OS installation) should make the serial UART available to us:

### Using the Desktop/GUI “Full” OS

You’ll find these settings in the Raspberry Pi Configuration tool. From the Raspberry menu at the top-left…

Go to the “Interfaces” tab and you’ll see two options “Serial Port” and “Serial Console.” Toggle _both_ of these away from their default states. Serial Port should be _enabled,_ Serial Console _disabled._ Then click “OK.” Reboot when prompted.

_With each new OS release, it’s normal that some configuration options may move to different menus or positions. If you can’t find it where shown, check under the other top-level menu options…even if moved, the name will likely remain similar._

![rfid___nfc_gui-serial-1.png](https://cdn-learn.adafruit.com/assets/assets/000/108/815/medium640/rfid___nfc_gui-serial-1.png?1644360436)

![rfid___nfc_gui-serial-2.png](https://cdn-learn.adafruit.com/assets/assets/000/108/816/medium640/rfid___nfc_gui-serial-2.png?1644360443)

### Using the “Lite” Command-Line OS

These options can be found in the `raspi-config` tool, which must be run as root:

```auto
sudo raspi-config
```

Navigate down to “Interface Options” and then “Serial Port.” Answer “No” to the login shell question, and “Yes” to the serial port hardware.

Navigate back to the main menu, tab to the “Finish” button and reboot when prompted.

_With each new OS release, it’s normal that some configuration options may move to different menus or positions. If you can’t find it where shown, check under the other top-level menu options…even if moved, the name will likely remain similar._

![rfid___nfc_cmdline-serial-1.png](https://cdn-learn.adafruit.com/assets/assets/000/108/817/medium640/rfid___nfc_cmdline-serial-1.png?1644360613)

![rfid___nfc_cmdline-serial-2.png](https://cdn-learn.adafruit.com/assets/assets/000/108/818/medium640/rfid___nfc_cmdline-serial-2.png?1644360618)

![rfid___nfc_cmdline-serial-3.png](https://cdn-learn.adafruit.com/assets/assets/000/108/819/medium640/rfid___nfc_cmdline-serial-3.png?1644360623)

![rfid___nfc_cmdline-serial-4.png](https://cdn-learn.adafruit.com/assets/assets/000/108/820/medium640/rfid___nfc_cmdline-serial-4.png?1644360627)

- [Previous Page](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/overview.md)
- [Next Page](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/building-libnfc.md)

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
