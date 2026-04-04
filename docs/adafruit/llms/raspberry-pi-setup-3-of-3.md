# Source: https://learn.adafruit.com/pi-wifi-radio/raspberry-pi-setup-3-of-3.md

# Raspberry Pi WiFi Radio

## Configure Software Packages

Create a directory for the pianobar configuration:

```
cd
mkdir -p .config/pianobar
```

Then link to the configuration file included with the radio software:

```
cd .config/pianobar
ln -s ../../Python-WiFi-Radio/config .
```

(Note: there’s a space before the final period above. Copy and paste this exact line if possible.)

Danger: 

Edit the pianobar configuration file with your Pandora account name and password:

```
nano config
```

The login credentials are near the top of the file:

```
user = YOUR_EMAIL_ADDRESS
password = YOUR_PASSWORD
```

Replace these with&nbsp; **the email address and password that you use for accessing your Pandora account** ,&nbsp;_not_&nbsp;the account on the Raspberry Pi system! Save the changes to the file and exit from the editor.

Finally, enter the following command to make sure audio is routed to the headphone jack rather than the HDMI port **(you can skip this step if [using a USB audio device](http://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi))**:

```
sudo amixer cset numid=3 1
```

And with that all said and done, you should now be able to run pianobar from the command line:

```
pianobar
```

If that runs as expected, connect headphones or speakers. The initial volume level will be very low. Type right parenthesis several times to increase the volume:  
  
**))))))))**  
  
If that all works, press “q” to exit pianobar, then shut down the system in preparation for installing the final hardware:

```
sudo shutdown -h now
```

If you were remotely logged in via SSH, your connection will be closed and you won’t see a “halt” message. Allow about 20 seconds before disconnecting power.

- [Previous Page](https://learn.adafruit.com/pi-wifi-radio/raspberry-pi-setup-2-of-3.md)
- [Next Page](https://learn.adafruit.com/pi-wifi-radio/add-lcd-plate.md)

## Featured Products

### Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM

[Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM](https://www.adafruit.com/product/3775)
The Raspberry Pi 3 Model B is the most popular Raspberry Pi computer made, and the Pi Foundation knows you can always make a good thing _better_! And what could make the Pi 3 better? How about a&nbsp;_faster_ processor, 5 GHz WiFi, and updated Ethernet chip with PoE capability?...

In Stock
[Buy Now](https://www.adafruit.com/product/3775)
[Related Guides to the Product](https://learn.adafruit.com/products/3775/guides)
### SD/MicroSD Memory Card (8 GB SDHC)

[SD/MicroSD Memory Card (8 GB SDHC)](https://www.adafruit.com/product/1294)
Add mega-storage in a jiffy using this 8 GB class 4 micro-SD card. It comes with a SD adapter so you can use it with any of our shields or adapters. Preformatted to FAT so it works out of the box with our projects. Tested and works great with our <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/1294)
[Related Guides to the Product](https://learn.adafruit.com/products/1294/guides)
### 5V 2.5A Switching Power Supply with 20AWG MicroUSB Cable

[5V 2.5A Switching Power Supply with 20AWG MicroUSB Cable](https://www.adafruit.com/product/1995)
Our all-in-one 5V 2.5 Amp + MicroUSB cable power adapter is the perfect choice for powering single-board computers like Raspberry Pi, BeagleBone, or anything else that's power-hungry!

This adapter was specifically designed to provide 5.25V, not 5V, but we still call it a 5V USB...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1995)
[Related Guides to the Product](https://learn.adafruit.com/products/1995/guides)
### Adafruit RGB Positive 16x2 LCD+Keypad Kit for Raspberry Pi

[Adafruit RGB Positive 16x2 LCD+Keypad Kit for Raspberry Pi](https://www.adafruit.com/product/1109)
This new Adafruit Pi Plate makes it easy to use an RGB 16x2 Character LCD. We really like the RGB Character LCDs we stock in the shop. (For RGB we have [RGB negative](http://www.adafruit.com/products/399) and [RGB positive](http://www.adafruit.com/products/398).)...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1109)
[Related Guides to the Product](https://learn.adafruit.com/products/1109/guides)
### Adafruit RGB Negative 16x2 LCD+Keypad Kit for Raspberry Pi

[Adafruit RGB Negative 16x2 LCD+Keypad Kit for Raspberry Pi](https://www.adafruit.com/product/1110)
This new Adafruit Pi Plate makes it easy to use an RGB 16x2 Character LCD. We really like the RGB Character LCDs we stock in the shop. (For RGB we have [RGB negative](http://www.adafruit.com/products/399) and [RGB positive](http://www.adafruit.com/products/398).)...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1110)
[Related Guides to the Product](https://learn.adafruit.com/products/1110/guides)
### Adafruit Blue&White 16x2 LCD+Keypad Kit for Raspberry Pi

[Adafruit Blue&White 16x2 LCD+Keypad Kit for Raspberry Pi](https://www.adafruit.com/product/1115)
This new Adafruit Pi Plate makes it easy to use a blue and white 16x2 Character LCD. [We really like the 16x2 Character LCDs we stock in the shop](http://www.adafruit.com/products/181). Unfortunately, these LCDs do require quite a few digital pins, 6 to control the LCD and then...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1115)
[Related Guides to the Product](https://learn.adafruit.com/products/1115/guides)
### Adafruit Raspberry Pi B+ / Pi 2 / Pi 3 Case - Smoke Base

[Adafruit Raspberry Pi B+ / Pi 2 / Pi 3 Case - Smoke Base](https://www.adafruit.com/product/2258)
It took awhile to perfect&nbsp;-&nbsp;but that's okay&nbsp;since we can now safely say that the Adafruit case for Raspberry Pi Model B+ / Pi 2 / Pi 3&nbsp;is The Single&nbsp;Greatest Raspberry Pi Model B+ Case Ever.

This enclosure&nbsp;was designed by Mike Doell - just like our...

In Stock
[Buy Now](https://www.adafruit.com/product/2258)
[Related Guides to the Product](https://learn.adafruit.com/products/2258/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)

## Related Guides

- [Adafruit Class Library for Windows IoT Core](https://learn.adafruit.com/adafruit-class-library-for-windows-iot-core.md)
- [Character LCD with Raspberry Pi or BeagleBone Black](https://learn.adafruit.com/character-lcd-with-raspberry-pi-or-beaglebone-black.md)
- [Adafruit 16x2 Character LCD + Keypad for Raspberry Pi](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi.md)
- [Onion Pi](https://learn.adafruit.com/onion-pi.md)
- [Monitor Your Home With the Raspberry Pi B+](https://learn.adafruit.com/monitor-your-home-with-the-raspberry-pi-b-plus.md)
- [Pi Hole Ad Detection Display with PiTFT](https://learn.adafruit.com/pi-hole-ad-pitft-tft-detection-display.md)
- [Introducing the Raspberry Pi 2 - Model B](https://learn.adafruit.com/introducing-the-raspberry-pi-2-model-b.md)
- [Setting up a Raspberry Pi as a WiFi Access Point](https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Adafruit RGB Matrix + Real Time Clock HAT for Raspberry Pi](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi.md)
- [Raspberry Pi as an Ad Blocking Access Point](https://learn.adafruit.com/raspberry-pi-as-an-ad-blocking-access-point.md)
- [Internet of Things Printer for Raspberry Pi](https://learn.adafruit.com/pi-thermal-printer.md)
- [Adafruit Prototyping Pi Plate](https://learn.adafruit.com/adafruit-prototyping-pi-plate.md)
- [Node.js Embedded Development on the Raspberry Pi](https://learn.adafruit.com/node-embedded-development.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
