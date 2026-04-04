# Source: https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/pi-setup.md

# DIY WiFi Raspberry Pi Touchscreen Camera

## Pi Setup

The optional tactile buttons on the PiTFT are not required for this project. You can install the buttons for other things if you like, but the camera software is entirely touchscreen-based. (Newer PiTFT variants already have all the buttons installed by default.)

# Load Operating System

To ensure that all the software interdependencies work, it’s best&nbsp;to **start with a clean installation**.  
  
Format a **4GB or larger** SD card and load it up with the Raspbian operating system. [This guide explains how to prepare a&nbsp;card for the Raspberry Pi](http://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi "Link: http://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi").&nbsp;The **Raspbian “Lite”** edition is recommended for this project.

With the Raspberry Pi powered off, install the **Pi camera** with its **ribbon connector** ,&nbsp;install the **PiTFT** display atop the GPIO header, connect an **HDMI monitor** and **USB keyboard** and go through the normal first-boot procedure.

After logging in, run&nbsp; **sudo raspi-config** for some basic configuration…

The following settings are useful and **recommended:**

- Under _Internationalization Options,_&nbsp;change the keyboard layout&nbsp;to match your region. If your keyboard is producing unexpected characters, this is usually the reason why.
- Also in _International,_ if planning to use wireless networking, change the WiFi country setting for your location. Then you can go back to the main menu and _Network Options_ to set up a WiFi connection.

The following are **optional:**

- Under _Interfacing Options,_&nbsp;enable SSH if you’d prefer to log in remotely and finish the system configuration over a network.
- Other settings can be configured to your liking.

The following should **not** be used:

- _Overclock._ This is a portable, battery-operated project and an overclocked Pi will draw more current. Overclocked systems don’t always play well with the PiTFT and are more likely to corrupt the SD card filesystem. Do not enable this option.

Select “Finish” and then **reboot** when prompted, then more configuration awaits…

Even if you don’t plan to use the Dropbox functionality of this project, it’s&nbsp; **necessary to get the Raspberry Pi on your network** &nbsp;at least temporarily to download additional software. This can be done using the wired&nbsp; **Ethernet** &nbsp;jack (no additional configuration needed), or over&nbsp; **WiFi** &nbsp;using either a USB WiFi adapter or the Pi 3’s built-in wireless networking. If raspi-config doesn’t handle the options you need,&nbsp;**[this guide may be helpful for setting that up](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup).**

Danger: 

# Install & Test PiTFT
Our PiTFT installation guide covers the basic setup (see notes below for specific options):

[Visit the PiTFT 2.8" Resistive Display guide to learn how to setup and install the PiTFT](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install-2)
When running the PiTFT installer script, select the #1 configuration option: “PiTFT 2.4", 2.8" or 3.2" resistive (240x320)”. This project can work with any of the **resistive** touch **320x240** PiTFT displays. It **will not work with capacitive displays or the 3.5" PiTFT**.

For rotation, select the #1 option: “90 degrees (landscape)”. This covers most situations, but if you find the screen is oriented 180° from what you need, just re-run the adafruit-pitft.sh script and select the #3 option instead (“270 degrees (landscape)”). You do _not_ need to re-run the camera installer script we’ll show later, just the PiTFT installer.

When asked about having the text console on the PiTFT, answer “y”. Then reboot when prompted.

**Make sure you've got the Raspberry Pi booting with the Text Console mode display on the PiTFT before you continue. You'll need to have that PiTFT stuff all working!**

Once you have it working, log in and then shutdown with **sudo shutdown** at the command line

![](https://cdn-learn.adafruit.com/assets/assets/000/013/587/medium800/raspberry_pi_1601console_LRG.jpg?1389246245)

# Setup Virtual Environment

If you are installing on the Bookworm version of Raspberry Pi OS or later, you will need to install your python modules in a virtual environment. You can find more information in the [Python Virtual Environment Usage on Raspberry Pi](https://learn.adafruit.com/python-virtual-environment-usage-on-raspberry-pi) guide. To Install and activate the virtual environment, use the following commands:

```terminal
sudo apt install python3-venv
python -m venv env --system-site-packages
```

To activate the virtual environment:

```terminal
source env/bin/activate
```

# Easy Install

Our camera software requires a complex set of software dependencies. We’ve written a script that takes care of all the ugly parts. You can download and run with&nbsp;these three lines (this is easiest if you login via _ssh_ and copy-and-paste these lines):

```terminal
cd ~
sudo apt-get update
sudo apt-get install -y git python3-pip
pip3 install --upgrade adafruit-python-shell click
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/pi-touch-cam.sh &gt; pi-touch-cam.py
sudo -E env PATH=$PATH python3 pi-touch-cam.py
```

The script explains what it’s about to do and prompts for a “Y” before continuing; any other input will cancel.

It may take **10 minutes** or so to run. Afterward, you’ll be prompted to **reboot** the system again. If this all works, **skip ahead** to the “ **Testing** ” section below!

Primary: 

# Complex Install From Scratch

If you used the “ **Easy Install** ” directions above, you can **ignore this section** and **skip ahead** to “ **Testing** ” below.

These are the steps taken by the pi-cam-install.sh script, if for some reason you need to perform any or all of these steps manually…

### System Tweaks

The file **/boot/config.txt** is modified to enable the camera (if not already active via raspi-config) and also boost the speed of the PiTFT display (changing the “speed” and “fps” values). These lines are usually at the bottom of the file.

```terminal
dtoverlay=pitft28c,rotate=90,speed=80000000,fps=60
start_x=1
gpu_mem=128
```

### Install Prerequisite Software

Our code relies on a few libraries for handling the camera and screen output. One of these, it’s necessary to intentionally _downgrade,_ in order for the touchscreen to interoperate correctly. It’s complicated. These lines in the script set that up (but don’t actually perform the downgrade yet):

```
# Enable Wheezy package sources
echo "deb http://archive.raspbian.org/raspbian wheezy main
" &gt; /etc/apt/sources.list.d/wheezy.list

# Set stable as default package source (currently jessie)
echo "APT::Default-release \"stable\";
" &gt; /etc/apt/apt.conf.d/10defaultRelease

# Set priority for libsdl from wheezy higher then the jessie package
echo "Package: libsdl1.2debian
Pin: release n=jessie
Pin-Priority: -10
Package: libsdl1.2debian
Pin: release n=wheezy
Pin-Priority: 900
" &gt; /etc/apt/preferences.d/libsdl
```

Update the APT package index files&nbsp;and&nbsp;install Python libraries:

```terminal
sudo apt-get update
sudo apt-get -y --force-yes install python-picamera python-pygame python-imaging
```

_Now_ we perform the actual SDL library downgrade (it has to follow the “apt-get update” above):

```terminal
apt-get -y --force-yes install libsdl1.2debian/wheezy
```

### Download the Camera and Dropbox Scripts

Just a couple more steps to download and uncompress these…

```terminal
cd ~pi
wget https://github.com/andreafabrizi/Dropbox-Uploader/archive/master.zip
unzip master.zip
rm master.zip
mv Dropbox-Uploader-master Dropbox-Uploader

wget https://github.com/adafruit/adafruit-pi-cam/archive/master.zip
unzip master.zip
rm master.zip
```

### Modify /etc/rc.local for auto-start (but don’t enable)

These lines are added to /etc/rc.local — the second is intentionally&nbsp;commented out by default. It’s a good idea to test the camera software manually before throwing the switch. These are inserted just before the final “exit 0” line that’s normally present.

```
# Enable this line to run camera at startup:
# cd /home/pi/adafruit-pi-cam-master ; sudo python cam.py
```

# Testing

Now&nbsp;give it a try. The software must be run as root (using the _sudo_ command) in order to access the TFT display:

```terminal
cd adafruit-pi-cam-master
sudo python cam.py
```

If all goes well, after a few seconds’ initialization you should see a live viewfinder preview on the screen, as well as two onscreen buttons.  
  
If this _doesn’t_ happen, an error message should give some sort of troubleshooting guidance; missing library or driver, etc.  
  
There’s still some work to be done if we want to use Dropbox, so quit the camera program for the time being…tap the gear icon (settings), the left arrow and then the confirmation button. You’ll be back at the command line now.

![](https://cdn-learn.adafruit.com/assets/assets/000/013/594/medium800/raspberry_pi_starter-ui.jpg?1389294573)

# Standalone mode

You can&nbsp;have the Pi boot straight into the camera software at startup by editing **/etc/rc.local** (this must be done as root, so “sudo” your text editor of preference):

```terminal
sudo nano /etc/rc.local
```

If you use the Easy Install script, the following line is already present, but commented out. Delete the initial “#” character on the line, save changes and reboot.

Otherwise, if doing this the long way, add&nbsp;the following line just before the final “exit 0”:

```terminal
cd /home/pi/adafruit-pi-cam-master; python cam.py
```

Next time you reboot you should see the text console for a few seconds and then it will start the cam.py&nbsp;software.

- [Previous Page](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/overview.md)
- [Next Page](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/dropbox-setup.md)

## Featured Products

### Raspberry Pi DIY Camera Pack

[Raspberry Pi DIY Camera Pack](https://www.adafruit.com/product/3275)
If the holidays promise anything, it’s almost certainly a deluge of photographs. Instead of taking out your smartphones, why not build your own camera?

With one of Adafruit’s best selling screens and an official Raspberry Pi camera, you’ll be ready to set up your very...

Out of Stock
[Buy Now](https://www.adafruit.com/product/3275)
[Related Guides to the Product](https://learn.adafruit.com/products/3275/guides)
### PiTFT Plus Assembled 320x240 2.8" TFT + Resistive Touchscreen

[PiTFT Plus Assembled 320x240 2.8" TFT + Resistive Touchscreen](https://www.adafruit.com/product/2298)
Is this not the cutest little display for the Raspberry Pi? It features a 2.8" display with 320x240 16-bit color pixels and a resistive&nbsp;touch overlay. The plate uses the high speed SPI interface on the Pi and can use the mini display as a console, X window port, displaying images or...

Out of Stock
[Buy Now](https://www.adafruit.com/product/2298)
[Related Guides to the Product](https://learn.adafruit.com/products/2298/guides)
### PiTFT Plus 320x240 3.2" TFT + Resistive Touchscreen

[PiTFT Plus 320x240 3.2" TFT + Resistive Touchscreen](https://www.adafruit.com/product/2616)
Is this not the cutest little display for the Raspberry Pi? It features a 3.2" display with 320x240 16-bit color pixels and a resistive&nbsp;touch overlay. The plate uses the high speed SPI interface on the Pi and can use the mini display as a console, X window port, displaying images or...

Out of Stock
[Buy Now](https://www.adafruit.com/product/2616)
[Related Guides to the Product](https://learn.adafruit.com/products/2616/guides)
### Adafruit PiTFT 2.4" HAT Mini Kit - 320x240 TFT Touchscreen

[Adafruit PiTFT 2.4" HAT Mini Kit - 320x240 TFT Touchscreen](https://www.adafruit.com/product/2455)
Is this not the cutest little display for the Raspberry Pi? It features a 2.4" display with 320x240 16-bit color pixels and a resistive touch overlay. The HAT uses the high speed SPI interface on the Pi and can use the mini display as a console, X window port, displaying images or video...

Out of Stock
[Buy Now](https://www.adafruit.com/product/2455)
[Related Guides to the Product](https://learn.adafruit.com/products/2455/guides)
### Adafruit PiTFT - 320x240 2.8" TFT+Touchscreen for Raspberry Pi

[Adafruit PiTFT - 320x240 2.8" TFT+Touchscreen for Raspberry Pi](https://www.adafruit.com/product/1601)
Is this not the cutest little display for the Raspberry Pi? It features a 2.8" display with 320x240 16-bit color pixels and a resistive touch overlay. The plate uses the high speed SPI interface on the Pi and can use the mini display as a console, X window port, displaying images or video...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1601)
[Related Guides to the Product](https://learn.adafruit.com/products/1601/guides)
### Raspberry Pi 3 - Model B - ARMv8 with 1G RAM

[Raspberry Pi 3 - Model B - ARMv8 with 1G RAM](https://www.adafruit.com/product/3055)
Did you really think the Raspberry Pi would stop getting better? At this point, we sound like a broken record, extolling on the new Pi’s myriad improvements like we’re surprised that the folks at the Raspberry Pi Foundation are continuously making their flagship board better.&nbsp;...

In Stock
[Buy Now](https://www.adafruit.com/product/3055)
[Related Guides to the Product](https://learn.adafruit.com/products/3055/guides)
### Raspberry Pi 2 - Model B v1.2 - ARM Cortex-A53 with 1G RAM

[Raspberry Pi 2 - Model B v1.2 - ARM Cortex-A53 with 1G RAM](https://www.adafruit.com/product/2358)
Didn't think the Raspberry Pi could get any better? You're in for a big surprise! The Raspberry Pi 2 Model B is out and it's amazing! With an upgraded ARM Cortex-A53&nbsp;quad-core processor, Dual Core VideoCore IV Multimedia coprocessor, and a full Gigabyte of RAM, this...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2358)
[Related Guides to the Product](https://learn.adafruit.com/products/2358/guides)
### Raspberry Pi Model A+ 512MB RAM

[Raspberry Pi Model A+ 512MB RAM](https://www.adafruit.com/product/2266)
 **Note:** As of August 10th, 2016 the Raspberry Pi A+ now includes 512 MB of RAM!

The Raspberry Pi Model A+ is the perfect board for the minimalist Pi fan. This low-cost Pi uses the same processor as the model B+, but does away with the Ethernet jack and three of the USB...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2266)
[Related Guides to the Product](https://learn.adafruit.com/products/2266/guides)

## Related Guides

- [Kali Linux on the Raspberry Pi with the PiTFT](https://learn.adafruit.com/kali-linux-on-the-raspberry-pi-with-the-pitft.md)
- [PiPhone - A Raspberry Pi based Cellphone](https://learn.adafruit.com/piphone-a-raspberry-pi-based-cellphone.md)
- [Processing on the Raspberry Pi & PiTFT](https://learn.adafruit.com/processing-on-the-raspberry-pi-and-pitft.md)
- [PiGRRL 2](https://learn.adafruit.com/pigrrl-2.md)
- [RasPipe: A Raspberry Pi Pipeline Viewer, Part 2](https://learn.adafruit.com/raspipe-a-raspberry-pi-pipeline-viewer-part-2.md)
- [Monitor PiCam and temperature on a PiTFT via adafruit.io](https://learn.adafruit.com/monitor-picam-and-temperature-on-a-pitft-via-adafruit-dot-io.md)
- [AstroPrint 3D Printing](https://learn.adafruit.com/astroprint-3d-printing.md)
- [Touchscreen Pi Timelapse Controller](https://learn.adafruit.com/touchscreen-pi-timelapse-controller.md)
- [Using the Slamtec RPLIDAR on a Raspberry Pi](https://learn.adafruit.com/slamtec-rplidar-on-pi.md)
- [Adafruit AMG8833 8x8 Thermal Camera Sensor](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor.md)
- [Pi Hole Ad Detection Display with PiTFT](https://learn.adafruit.com/pi-hole-ad-pitft-tft-detection-display.md)
- [SnapPiCam Raspberry Pi Camera](https://learn.adafruit.com/snappicam-raspberry-pi-camera.md)
- [JOY of Arcada — USB Game Pad for Adafruit PyGamer and PyBadge](https://learn.adafruit.com/joy-of-arcada-usb-game-pad-for-adafruit-pygamer-pybadge.md)
- [Go Fishing with Rotary Encoders](https://learn.adafruit.com/gone-fishing-game.md)
- [Set up and Blink - MATLAB and Simulink with Raspberry Pi](https://learn.adafruit.com/how-to-use-matlab-and-simulink-with-raspberry-pi.md)
