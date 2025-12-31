# Source: https://learn.adafruit.com/pi-wifi-radio/raspberry-pi-setup-1-of-3.md

# Raspberry Pi WiFi Radio

## Initial System Configuration

This project works well with the Raspbian “Lite” operating system; it fits easily on a 2 GB card with room to spare. _Do not_&nbsp;use the “desktop” images, they’re enormous&nbsp;and contain a ton of things we don’t need for this.

## **[Raspberry Pi Downloads Page](https://www.raspberrypi.org/downloads/raspbian/)**

While that’s downloading, you can work on **[assembling the LCD kit](../../../../adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/assembly)**.

If you’re new to Raspberry Pi and Linux, we strongly suggest working through the first few guides in the&nbsp;[**Learn Raspberry Pi**](../../../../category/learn-raspberry-pi)&nbsp;tutorial series…know how to “burn” an SD image, perform a first-time setup and get the Raspberry Pi connected to a network. Some familiarity with one of the text editors (such as the simple&nbsp;_nano_&nbsp;or the more daunting&nbsp;_vi_&nbsp;or&nbsp;_emacs_) is also recommended.

Install the Raspbian Lite OS on a&nbsp; **2GB or larger** &nbsp;card. You’ll need to connect a&nbsp; **monitor** &nbsp;and&nbsp; **USB keyboard** &nbsp;for basic system configuration, but this is only temporary…we’ll set it up to run “headless” later. For networking, connect either an Ethernet cable or use WiFi (built-in on some Pi models, else use a USB WiFi adapter).

 **At this point you should&nbsp;have an SD card containing the Raspbian Lite software, and an assembled LCD “Pi Plate.”**

![](https://cdn-learn.adafruit.com/assets/assets/000/018/995/medium800/raspberry_pi_PiPhiParts.jpg?1408742746)

You don’t need to install the LCD Plate atop the Pi yet, we’ll do that later. Let’s just get the basics set up.

1. Connect a monitor and keyboard to the Raspberry Pi.
2. Insert the SD card containing the Raspbian OS.
3. Connect a “Micro B” USB cable to the power connector on the Raspberry Pi.
4. Plug the other end of the USB cable into a power source: a mobile phone charger, a powered USB hub, or simply a USB port on your computer.

The Raspberry Pi should now boot, and you’ll see the monitor fill with lots of “Unix stuff.”

Danger: 

On first boot, you’ll get a login prompt. Log in as user “pi,” password “raspberry”.

Once&nbsp;you’re logged in successfully and have a command-line prompt, run the system configuration utility:

```
sudo raspi-config
```

![](https://cdn-learn.adafruit.com/assets/assets/000/068/576/medium800/projects_raspi-config.png?1546446475)

The following selections are&nbsp; **required** :

- Under “Interfacing Options,” enable **I2C**.
- If you’ll be using **WiFi** , under “Localisation Options,” select “Change Wi-fi Country.” Then, under “Network Options,” select “Wi-fi” to enter the SSID/password for your wireless network.

The following are&nbsp; **optional** , but&nbsp; **strongly recommended** :

- Change User Password (because everybody knows the default).
- Under “Localisation Options,” select “Change Locale,” “Change Timezone” and “Change Keyboard Layout” to suit your location. If your keyboard isn’t producing the expected symbols, this is why.
- Network Options→Change Hostname. I named mine “ **pandora** ” to distinguish it from other Raspberry Pi systems on the network.
- Interfacing Options→Enable SSH. This allows remote login from another system on the network, for performing administration tasks without a display attached.
- You can disable Overscan (under “Advanced Options”) if you like — we’ll reboot a few times during the setup process, and this provides a little extra screen real estate on HDMI monitors.

Tab over to the “Finish” button, press Return and confirm you’d like to reboot the system when prompted. You’ll need to log in again, using the password you established above.

Danger: 

If using a **USB WiFi adapter** based on the popular **Realtek 8192CU** chipset, disabling WiFi power management seems to help with reliability. Once you’re logged in, type (or copy and paste) this at the command prompt:

```
echo "options 8192cu rtw_power_mgnt=0 rtw_enusbss=0" | sudo tee --append /etc/modprobe.d/8192cu.conf
```

## Enable I2C Support for the LCD

The LCD doesn’t need to be attached yet, but we can get some setup started…

```
sudo nano /etc/modules
```

Add one or both of these lines if not already present:

```
i2c-bcm2708 
i2c-dev
```

## Optional: Enable USB Audio
If you plan to use this with a USB Audio Adapter, [this guide explains the process](http://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi). It’s pretty straightforward, a matter of editing one line in a file.

## Reboot
Finally, shut down the system:

```
sudo shutdown -h now
```

Wait for the system to report that it’s halted before disconnecting power. It should take about 20 seconds.  
  
Following shutdown, insert the USB WiFi adapter (if using one) and re-connect power (keep the monitor attached for now).

**Is using a Model A board:** &nbsp;you’ll need to remove the keyboard to plug in WiFi, or use a powered USB hub temporarily during setup. Without a hub,&nbsp; **ssh** is now the only way into the system…so if WiFi isn’t working,&nbsp;you’ll need to unplug the adapter, connect a keyboard and check the WiFi configuration.

**For all other boards:** &nbsp;keyboard can stay attached until you know the networking is properly configured.&nbsp;Log in again and you should be able to access the outside world now:

```
sudo ping adafruit.com
```

Do not proceed until internet access is working. If WiFi refuses to cooperate, make sure every step above has been followed carefully. If you’re trying to use a hidden network and it just won’t play nice, change the router configuration to broadcast the network name.

Raspbian Lite includes the “avahi” package by default,&nbsp;so the system appears on the network as “pandora.local” (or whatever hostname you configured) instead of a numeric IP address. You can easily access the Raspberry Pi remotely using an ssh client from another system on the network. For example, using the Terminal application in Mac OS X, one would type:

```
ssh pi@pandora.local
```

You should get a password prompt. Once logged in, you can perform all administration duties remotely (including the steps that follow), and the monitor and keyboard are no longer needed on the Raspberry Pi. It’s easier this way because you can cut-and-paste all the commands with their weird syntaxes.

- [Previous Page](https://learn.adafruit.com/pi-wifi-radio/parts-list.md)
- [Next Page](https://learn.adafruit.com/pi-wifi-radio/raspberry-pi-setup-2-of-3.md)

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
