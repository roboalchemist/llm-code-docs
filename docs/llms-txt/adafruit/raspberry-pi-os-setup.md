# Source: https://learn.adafruit.com/pi-thermal-printer/raspberry-pi-os-setup.md

# Internet of Things Printer for Raspberry Pi

## Raspberry Pi OS Setup

# OS Install and First-Time Configuration
At this point it is assumed you have a bootable&nbsp;SD card containing the Raspbian Lite software. If not, follow the directions on the “Preparation” page.

Warning: 

1. Connect a **monitor** and a **USB keyboard** to the Raspberry Pi (a mouse is _not_ required).
2. Insert the SD card containing the **Raspbian Lite** software.
3. Connect a micro-B USB cable to the power connector on the Raspberry Pi.
4. Plug the other end of the USB cable into a power source: a mobile phone charger, a powered USB hub, or simply a USB port on your computer.

The Raspberry Pi should now boot, and you’ll see the monitor fill with lots of “Unix stuff.”&nbsp;On first boot, the system may automatically reboot once as part of the setup process. This is normal.

Primary: 

Within a minute or so you should get a login prompt. Log in as user “ **pi** ” and password “ **raspberry** ”. Then enter the following command for essential system setup:

```
sudo raspi-config
```

Use the up/down arrow keys, tab and return/enter to navigate the config&nbsp;menu:

![](https://cdn-learn.adafruit.com/assets/assets/000/040/963/medium800/raspberry_pi_config.png?1492743155)

The following selections are **required:**

- Under “ **Interfacing Options** ,” select “ **Serial**.” Turn **OFF** the **&nbsp;login shell** over serial **,** and **ENABLE** the hardware **serial port**. **NO** and **YES** , respectively. This is vital!
- Under “ **Interfacing Options** ,” **enable SSH**. This permits network access to the Raspberry Pi without a monitor or keyboard attached later.
- Under “ **Localisation Options** ,” select “ **Change Timezone** ” and set this up for your location (a correct time zone is required for the time display and other examples to work).

The following are **optional but recommended:**

- “ **Change User Password** ,” because everybody knows the default (“raspberry”).
- “ **Hostname** ” to&nbsp;distinguish this system from other Raspberry Pis on the network (default is “raspberrypi,” consider changing to “iotp” or “piprinter” or any descriptive name).
- Under “ **Localisation Options** ,” configure&nbsp;the other options for **language** , **WiFi channels** and **keyboard**. _If your keyboard is generating unexpected characters, this is why!_
- Under “ **Advanced Options** ,” you can optionally&nbsp; **disable overscan compensation** if using an HDMI monitor. Though our ultimate goal is to use the Raspberry Pi “headless,” without a monitor, the extra space is welcome during the configuration steps.

**Do NOT** touch “Overclock” or other esoteric settings. Overclocking can wreak havoc&nbsp;with the serial port we’ll be&nbsp;relying on! **Do not overclock.**

Tab to&nbsp;"Finish" and press enter, but **DO NOT REBOOT YET.** We still need to set up the wireless networking. Select “No” when prompted to reboot. Raspi-config will exit to the command line.

Info: 

# Configure Wireless Networking
If you have a WiFi network that broadcasts its SSID (the wireless network name), this is fairly straightforward:

```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

Delete _everything_ in the file, then&nbsp;enter the below text in instead. Check your spelling, everything’s got to be spot-on! Then edit the SSID and password lines to reflect your actual network name and password (keeping the double quotes on both):

```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="SSID"
    psk="YOUR_PASSWORD"
    scan_ssid=1
}
```

[A more in-depth networking tutorial is available here](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/overview). Skip ahead to the “Reboot” section below. This next section pertains only to hidden wireless networks.

# Hidden Networks
Hidden WiFi networks are an ongoing point of contention…the following directions may or may not work for your particular network. If this doesn’t seem to work, consider changing your WiFi config to broadcast the SSID; it’s been shown that hidden networks aren’t actually any more secure than visible ones!

The network configuration in this case is a fair bit more complicated.&nbsp;And the slightest typo here, even one character, can prevent the system from joining the network! Again, we **strongly recommend using a “broadcast” network** , it’s far easier and less error-prone. But if you _must…_

```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

Delete _everything_ in the file, then&nbsp;enter the below text in instead. Check your spelling, everything’s got to be spot-on! Indent the 'network' section using tabs, not spaces. Then edit the ssid&nbsp;and psk (password)&nbsp;lines to reflect your actual network name and password (keeping the double quotes on both):

```
ctrl_interface=/var/run/wpa_supplicant
update_config=1
ap_scan=2
eapol_version=1
network={
	ssid="my-network-ssid"
	scan_ssid=1
	mode=0
	proto=WPA2
	auth_alg=OPEN
	pairwise=CCMP
	group=CCMP
	key_mgmt=WPA-PSK
	psk="my-network-password"
}
```

# Reboot
Finally, shut down the system:

```
sudo shutdown -h now
```

Wait for the system to report that it’s **halted** before disconnecting power. It should take about 30 seconds.  
  
Following shutdown, remove the keyboard (if using a Model A board), insert the WiFi adapter and re-connect power (keep the monitor attached for now). With a Model B board, you can keep both the keyboard and WiFi adapter attached until you know the networking is properly configured.

What's nice is Raspbian now comes with Bonjour so you do not need to memorize IP addresses.

If you have Mac, you don't have to do anything

If you have Windows, [go here and install the Bonjour support (via Apple print support)](../../../../bonjour-zeroconf-networking-for-windows-and-linux/)

Your Pi's name will be **raspberrypi.local** unless you changed the hostname in **raspi-config** in whichcase it will be _ **hostname** _ **.local**

If the wireless connection doesn’t work, unplug the WiFi adapter and connect the keyboard and double-check the network setup steps above. It might simply be a typo. Correct any mistakes and reboot.  
  
Once WiFi is working, the keyboard and monitor are no longer required. All further configuration can be done remotely via SSH, if you’ve enabled it in raspi-config.

- [Previous Page](https://learn.adafruit.com/pi-thermal-printer/preparation-pre-2017.md)
- [Next Page](https://learn.adafruit.com/pi-thermal-printer/raspberry-pi-software-setup.md)

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
