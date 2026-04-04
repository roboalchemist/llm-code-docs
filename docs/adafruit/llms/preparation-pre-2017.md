# Source: https://learn.adafruit.com/pi-thermal-printer/preparation-pre-2017.md

# Internet of Things Printer for Raspberry Pi

## Software Prep

We’ll deal with **software** first, then get into soldering&nbsp;and case assembly later.

The software for this project is built upon the **Raspbian Lite** operating system, a pared-down version of Linux for the Raspberry Pi.

The current kit comes with a card loaded with **NOOBS**. This can be used to download and install Raspbian Lite, but we recommend you overwrite the card so you have the most minimal setup (less things can go wrong!)

# Installing From the NOOBS Card

NOOBS has a **graphical interface** and requires temporarily setting up the Pi like a desktop computer. You’ll need a **monitor** connected, along with a **USB keyboard** and **mouse** (this may also require a **USB hub** ). Insert the card in the Raspberry Pi, then connect a USB micro-B cable from&nbsp;the board’s power connector to a USB power source&nbsp;— a phone charger, hub, or just a USB port on your “main”&nbsp;computer.

When booting the NOOBS card, you’ll briefly see the “rainbow screen” — normally bad news, but **it’s okay** in this case — the Pi will then reboot and launch the NOOBS installer menu:

![](https://cdn-learn.adafruit.com/assets/assets/000/040/973/medium800/raspberry_pi_NOOBS.jpg?1492824358)

First order of business is to connect NOOBS to a **wireless network** so software can be downloaded. Use the “ **WiFi networks** ” icon (top center) to set this up. It’s a fairly straightforward WiFi configurator…select a network from the available list and enter a network password if required.

Danger: 

Danger: 

With an internet connection now made, select “ **Raspbian Lite** ” from the list of available operating systems. **Do NOT** select “Raspbian with PIXEL” — this contains a whole lot of software we do not need or want!

Click the “Install” icon. This will download Raspbian Lite (about 300 megabytes), install it on the SD card and (after prompting) will reboot into the newly-installed operating system. You can then skip ahead to the “Setup” page.

More information on NOOBS is available [in this guide](../../../../setting-up-a-raspberry-pi-with-noobs/overview) if needed.

# Overwriting&nbsp;NOOBS with Raspbian Lite

If you have some prior experience with Raspberry Pi and Linux, you might find this approach simpler…

[Start by downloading&nbsp;the latest version of **Raspbian Lite** from the Raspberry Pi web site](https://www.raspberrypi.org/downloads/raspbian/).

**Do NOT** &nbsp;use “Raspbian with Desktop PIXEL” — this contains a whole lot of software we do not need or want!&nbsp;Also, if you’ve previously downloaded Raspbian Lite for other projects, check if a **newer version** is available. This project relies on some recent features!

[Here’s a tutorial explaining how to install the Raspbian&nbsp;software on the SD card](http://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi/overview "Link: http://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi/overview")&nbsp;(replacing NOOBS), with links to nice GUI apps for Windows and Mac. The first couple of pages can be skipped, as we’re already downloading the right software for this project.

If you ever need to restore the NOOBS card to its original state, [this guide](../../../../setting-up-a-raspberry-pi-with-noobs/overview) explains the whole process.

- [Previous Page](https://learn.adafruit.com/pi-thermal-printer/parts.md)
- [Next Page](https://learn.adafruit.com/pi-thermal-printer/raspberry-pi-os-setup.md)

## Primary Products

### Adafruit IoT Pi Printer Project Pack

[Adafruit IoT Pi Printer Project Pack](https://www.adafruit.com/product/1289)
Build an "Internet of Things" connected mini printer that will do your bidding! This is a fun weekend project that comes with a beautiful laser cut case. Once assembled, the little printer connects wirelessly to get Internet data for printing onto 2 1/4" wide receipt paper....

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1289)
[Related Guides to the Product](https://learn.adafruit.com/products/1289/guides)

## Featured Products

### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### Raspberry Pi - Skill badge, iron-on patch

[Raspberry Pi - Skill badge, iron-on patch](https://www.adafruit.com/product/906)
You are learning to use the small Linux based board, the Raspberry Pi! Adafruit offers a fun and exciting "badges" of achievement for electronics, science and engineering. We believe everyone should be able to be rewarded for learning a useful skill, a badge is just one of the many...

In Stock
[Buy Now](https://www.adafruit.com/product/906)
[Related Guides to the Product](https://learn.adafruit.com/products/906/guides)
### Adafruit Pi Unassembled T-Cobbler Breakout Kit for Raspberry Pi

[Adafruit Pi Unassembled T-Cobbler Breakout Kit for Raspberry Pi](https://www.adafruit.com/product/1105)
Now that you've finally got your hands on a [Raspberry Pi®](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi T-Cobbler from Adafruit, which can break out all those tasty...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1105)
[Related Guides to the Product](https://learn.adafruit.com/products/1105/guides)
### Mini Thermal Receipt Printer Starter Pack

[Mini Thermal Receipt Printer Starter Pack](https://www.adafruit.com/product/600)
Hit the ground running (and printing!) with this starter pack that includes a thermal printer and all the extras and save a few dollars while you're at it.  
  
Includes:

- [A mini thermal receipt printer](http://www.adafruit.com/products/597) - with cables and...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/600)
[Related Guides to the Product](https://learn.adafruit.com/products/600/guides)
### Thermal paper roll - 50' long, 2.25" wide

[Thermal paper roll - 50' long, 2.25" wide](https://www.adafruit.com/product/599)
A mini roll of thermal paper, this fits very nicely into our mini thermal printer. 2.25" wide (about 57mm) and 50 feet long (15 meters). BPA-free.  
  
[Perfect for use with our mini thermal printer!](http://www.adafruit.com/products/597)

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/599)
[Related Guides to the Product](https://learn.adafruit.com/products/599/guides)
### Mini Thermal Receipt Printer

[Mini Thermal Receipt Printer](https://www.adafruit.com/product/597)
Add a mini printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an enclosure. This printer is ideal...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/597)
[Related Guides to the Product](https://learn.adafruit.com/products/597/guides)
### Rugged Metal Pushbutton with White LED Ring

[Rugged Metal Pushbutton with White LED Ring](https://www.adafruit.com/product/558)
These chrome-plated metal buttons are rugged&nbsp;and look real good while doing it! Simply drill a 16mm hole into any material up to 1/2" thick and you can fit these in place, there's even a rubber gasket to keep water out of the enclosure. On the front of the button is a flat metal...

In Stock
[Buy Now](https://www.adafruit.com/product/558)
[Related Guides to the Product](https://learn.adafruit.com/products/558/guides)
### 5V 10A switching power supply

[5V 10A switching power supply](https://www.adafruit.com/product/658)
This is a beefy switching supply, for when you need a lot of power! It can supply 5V DC up to 10 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard computer/appliance...

In Stock
[Buy Now](https://www.adafruit.com/product/658)
[Related Guides to the Product](https://learn.adafruit.com/products/658/guides)

## Related Guides

- [Skill Badge Requirements: Raspberry Pi](https://learn.adafruit.com/skill-badge-requirements-raspberry-pi.md)
- [Adafruit Prototyping Pi Plate](https://learn.adafruit.com/adafruit-prototyping-pi-plate.md)
- [Adafruit Raspberry Pi Educational Linux Distro](https://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro.md)
- [Open Source Protective Face Shield Designs](https://learn.adafruit.com/open-source-face-shield-designs.md)
- [PyPortal IoT Plant Monitor with Google Cloud IoT Core and CircuitPython](https://learn.adafruit.com/pyportal-iot-plant-monitor-with-google-cloud-iot-core-and-circuitpython.md)
- [Adafruit QT Py ESP32-C3 WiFi Dev Board](https://learn.adafruit.com/adafruit-qt-py-esp32-c3-wifi-dev-board.md)
- [AstroPrint 3D Printing](https://learn.adafruit.com/astroprint-3d-printing.md)
- [No-Code Rain Sensing Smart Desktop Umbrella Stand](https://learn.adafruit.com/no-code-rain-sensing-smart-desktop-umbrella-stand.md)
- [MacroPad Remote Procedure Calls over USB to Control Home Assistant](https://learn.adafruit.com/macropad-remote-procedure-calls-over-usb-to-control-home-assistant.md)
- [PiPhone - A Raspberry Pi based Cellphone](https://learn.adafruit.com/piphone-a-raspberry-pi-based-cellphone.md)
- [Adafruit 128x64 OLED Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi.md)
- [Set up and Blink - MATLAB and Simulink with Raspberry Pi](https://learn.adafruit.com/how-to-use-matlab-and-simulink-with-raspberry-pi.md)
- [Mini Raspberry Pi Handheld Notebook](https://learn.adafruit.com/mini-raspberry-pi-handheld-notebook-palmtop.md)
- [Adafruit's Raspberry Pi Lesson 2. First Time Configuration](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration.md)
- [Huzzah Weather Display](https://learn.adafruit.com/huzzah-weather-display.md)
