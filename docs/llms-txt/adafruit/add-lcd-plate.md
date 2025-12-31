# Source: https://learn.adafruit.com/pi-wifi-radio/add-lcd-plate.md

# Raspberry Pi WiFi Radio

## LCD and Final Configuration

 **If you haven’t already assembled the LCD Pi Plate, do that step now.** [**Here’s a tutorial to guide you through the assembly**](http://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi)**.  
  
Raspberry Pi Model A users:**  
   the LCD Pi Plate is normally assembled with a rubber bumper near one corner for stability atop the Raspberry Pi. This bumper rests on the Ethernet jack, which is only present on the _Model B_ board. Model A users will need to find a suitable alternative to the bumper, non-conductive and about 5/8" tall. A cork or rubber eraser trimmed to size can work, a 5/8" nylon PC board spacer if you have one, or a 2x2 Lego® brick set on its side. ![](https://cdn-learn.adafruit.com/assets/assets/000/007/335/medium800/raspberry_pi_lego.jpg?1396850150)

Danger: 

If using the Pi Box case, [follow this tutorial](http://learn.adafruit.com/pi-box) to install the Raspberry Pi inside, leaving the top of the case off.  
  
Align the 26-pin headers on the LCD plate and Raspberry Pi, and install the plate by pressing straight down gently.  
  
Connect power to the Raspberry Pi. The red power light should come on. If not, there might be a soldering mistake on the LCD Pi Plate board.  
  
Allow 30 seconds to a minute for the Raspberry Pi to fully boot and situate itself on the network. At this point, you should be able to log in from a terminal over ssh, e.g.:  
  
**ssh pi@192.168.0.6** (or whatever address the system reported during the configuration process)  
  
If you previously installed netatalk (optional), and if you changed the Raspberry Pi’s default hostname, you might be able to use:  
  
**ssh pi@pandora.local**

Danger: 

You should be successfully logged into the system at this point.  
  
First, let’s test the LCD and buttons:

```
cd Python-WiFi-Radio
sudo python Adafruit_CharLCDPlate.py
```

If using an RGB-backlit LCD, the program should cycle through different backlight colors (with the Blue & White LCD, it will flash on and off a few times). Then it will ask you to try pressing buttons.  
  
Adjust the Contrast dial (using a small screwdriver if necessary) until the text is sharp and legible.  
  
When finished, press Control+C to exit. The LCD is ready!

Next, let’s try our radio software:

```
sudo python PiPhi.py
```

This is our own “wrapper” for pianobar, allowing us to use the LCD and buttons to interact with that program. If all goes well, the system should report its network address, fetch a list of stations from the Pandora server and start playing. If not, refer to the Troubleshooting page.  
  
With only a few buttons available, we’ve condensed only the most essential functions to this program. If you need to configure your Pandora account (such as adding new stations to the list), use a web browser to access the Pandora web site.  
  
From left to right, the button functions are:

- Play/Pause (tap once to pause, again to play, or hold for three seconds to exit the program).
- Station select (brings up a menu — can then use the up and down buttons to pick a station — press this button again to activate, or the Play/Pause button to cancel).
- Volume Up/Down (two buttons, one above the other)
- Next Track

Take a moment to experiment with the buttons and familiarize yourself with their use. If everything seems to be working, we’ll do some final configuration to make the system truly standalone. To exit from the PiPhi program, hold down Select (the leftmost button) for 3+ seconds.

Recent builds of pianobar seem resistant to quitting when the PiPhi.py script exits. If that occurs — if music is still playing even though you’ve quit the program — type:

```
sudo killall pianobar
```

This is only a potential issue during testing — once it’s set up as a fully standalone device with auto-start and shutdown, you shouldn't experience this problem.

## Final Configuration and Auto-Start
First, **cd** to the directory with the PiPhi.py script (you should already be there if you've followed the steps till now!) and edit the PiPhi.py script:

```
nano PiPhi.py
```

Two lines near the start of the code (around line 26) are of interest:

```
RGB_LCD      = False # Set to 'True' if using color backlit LCD
HALT_ON_EXIT = False # Set to 'True' to shut down system when exiting
```

If you’ve opted for an RGB-backlit LCD, change the first of these lines to:

```
RGB_LCD = True
```

Since our goal is a standalone system with no keyboard or monitor, we need some way to issue an orderly shutdown (Linux systems don’t like it when you just pull the plug). To make the 3-second button press shut down the system (rather than just exit to a command line prompt), change the second line to:

```
HALT_ON_EXIT = True
```

Nearly there! Now we just need to set up the system to start our program upon booting.

```
sudo nano /etc/rc.local
```

Before the final “exit 0” line, insert these two lines:

```
cd /home/pi/Python-WiFi-Radio
python PiPhi.py &amp;
```

If you downloaded or otherwise placed the radio software in a different location, the first line should be changed accordingly. “sudo” isn’t necessary here because the rc.local script is already run as root.  
  
Reboot the system to test the startup function:

```
sudo reboot
```

After 30 seconds to a minute, you should see the backlight turn on and music will begin. If not, connect to the system using ssh and confirm the configuration steps above.

- [Previous Page](https://learn.adafruit.com/pi-wifi-radio/raspberry-pi-setup-3-of-3.md)
- [Next Page](https://learn.adafruit.com/pi-wifi-radio/troubleshooting.md)

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
