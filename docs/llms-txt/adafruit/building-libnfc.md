# Source: https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/building-libnfc.md

# Adafruit NFC/RFID on Raspberry Pi

## Building libnfc

# Step One: Prepare for and Download libnfc

Before you can do anything, you will need to get the libnfc library. Make sure you have internet access on your Pi, through Ethernet or WiFi.

If using the full/GUI Raspberry Pi OS, open a terminal window for typing commands.

```xml
cd
sudo apt-get install git autoconf libtool libusb-dev
git clone https://github.com/nfc-tools/libnfc
```

This will create a new directory “libnfc” in your home directory. Answer “Y” when prompted on the apt-get installation.

# Step Two: Set Up libnfc For the Pi

Before libnfc can be built, it needs to be configured for the target system and based on some parameters specific the NFC device you have connected.

libnfc requires a configuration file in a specific location. We’ll start by creating the required folder, then (unrelated) change to the libnfc directory for subsequent steps.

```xml
sudo mkdir -p /etc/nfc/devices.d
cd libnfc
```

Next step varies by target system. This refers to the **machine where the NFC reader will be connected** …occasionally one might set up the OS on one machine, then move the card to a different Pi for use. Follow one or other, not both! If you upgrade or downgrade the Raspberry Pi to a different model later, you _might_ need to recompile everything, depending on which Pi models.

## For Recent Raspberry Pi Models

This step works for Raspberry Pi 400, Pi 4, and Pi 3 models B and B+.&nbsp;It _almost certainly_ works on Compute Module 4 and Pi Zero 2W, but did not have hardware on-hand to confirm (worst case, if later tests fail, you can “make clean” and re-try the alternate instructions below).

Enter this command to install the libnfc serial configuration file for these Pi models:

```auto
sudo cp contrib/libnfc/pn532_uart_on_rpi_3.conf.sample /etc/nfc/devices.d/pn532_uart_on_rpi_3.conf
```

_This should be entered as one continuous long line…it might appear wrapped to two lines in your browser, but enter it as one with a space character in-between. Or use the “Copy Code” button._

## For Earlier Pi Models

This step works for Raspberry Pi 2, Pi 1, and initial Pi Zero models (not Pi Zero 2W). This _may_ work on the wireless Pi Zero W models, but did not have hardware on-hand to confirm (worst case, if later tests fail, you can “make clean” and try the alternate instructions above).

Enter this command to install the libnfc serial configuration file for these systems:

```auto
sudo cp contrib/libnfc/pn532_uart_on_rpi.conf.sample /etc/nfc/devices.d/pn532_uart_on_rpi.conf
```

_This should be entered as one continuous long line…it might appear wrapped to two lines in your browser, but enter it as one with a space character in-between. Or use the “Copy Code” button._

# Step Three: Configure the Library

The next step is to configure the project itself using the 'configure' tool, as follows:

```xml
autoreconf -vis
./configure --with-drivers=pn532_uart --sysconfdir=/etc --prefix=/usr
```

This may take a minute or two to complete, that’s normal. The output will resemble the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/108/822/medium800/rfid___nfc_libnfc-config.png?1644365567)

# Step Four: Build and Install!

Once configured, the following commands then build and install the library:

```auto
make
sudo make install all
```

This may take a few minutes to complete. Some compiler warning messages might be generated along the way…these can be safely ignored.

Once the process is complete, you’re ready to test on actual hardware…

- [Previous Page](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/pi-serial-port.md)
- [Next Page](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/testing-it-out.md)

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
