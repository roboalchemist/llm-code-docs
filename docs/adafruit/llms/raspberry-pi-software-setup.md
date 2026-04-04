# Source: https://learn.adafruit.com/pi-thermal-printer/raspberry-pi-software-setup.md

# Internet of Things Printer for Raspberry Pi

## Raspberry Pi Software Setup

Danger: 

Further configuration of the Raspberry Pi will take place over the network using **SSH** , not the keyboard and mouse. You also don't have access to the serial console so you can only use ssh or logging in over HDMI + Keyboard.

[As you can probably figure by now, we have an in-depth SSH tutorial](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh). In summary:

- The **SSH server** should already be **enabled** on the Raspberry Pi — this was done during the initial raspi-config setup.
- On Mac or Linux systems, you can use a Terminal or xterm window.
- For Windows systems, you can [download PuTTY](http://www.putty.org).

The terminal command to access the system would be either:

```
ssh pi@raspberrypi.local
```

(If you changed the hostname in raspi-config, use that instead, e.g. **iotp.local** )

Or — if&nbsp;your computer&nbsp;can’t resolve the “.local” address&nbsp;—&nbsp;try the numeric IP address that you can get from your pi by typing in **hostname -I**

![](https://cdn-learn.adafruit.com/assets/assets/000/046/023/medium800/raspberry_pi_hostname.png?1504560289)

```
ssh pi@10.0.1.10
```

(Substitute the numeric IP address actually reported by the system during boot.)

You’ll be prompted for a password — either use the password that you set up from raspi-config, or “raspberry” if you left the default. Additionally, the first time connecting you may be prompted regarding a host key for security…enter Y (or click Yes) when prompted.

# Update&nbsp;Packages, Install Libraries and Printer Essentials
Once logged in, type the following at the command prompt (if logged in through **ssh** , you can **copy-and-paste** from this browser window to the terminal):

```
sudo apt-get update
sudo apt-get install git cups wiringpi build-essential libcups2-dev libcupsimage2-dev python-serial python-pil python-unidecode
```

The “update” step refreshes the list of available software packages and takes a couple of minutes.

The “install” step downloads and installs a number of packages…this may take 20 minutes or so.

# Install Printer Driver
 **The printer does not&nbsp;need to be connected yet.** &nbsp;We can prepare the system the same regardless.

```
cd ~
git clone https://github.com/adafruit/zj-58
cd zj-58
make
sudo ./install
```

![](https://cdn-learn.adafruit.com/assets/assets/000/046/024/medium800/raspberry_pi_zj.png?1504561183)

Your thermal printer may have arrived with a&nbsp; **test page** &nbsp;in the box or the paper bay. If not, or if you threw that away, you can generate a new one by installing a roll of paper and holding the feed button while connecting power.

Look for the&nbsp; **baud rate** &nbsp;that’s printed near the bottom of the page. This is typically either&nbsp; **9600** &nbsp;or&nbsp; **19200** &nbsp;baud. This is important…you’ll need to know the correct value for your printer.

You can recreate the test page by holding down the feed button and then powering the printer.

![](https://cdn-learn.adafruit.com/assets/assets/000/040/964/medium800/camera_raspberry_pi_components_test-baud.jpg?1492748044)

To set up this printer as the system default, we’ll be typing two lines similar to the following (but not necessarily identical…read on)…

```
sudo lpadmin -p ZJ-58 -E -v serial:/dev/serial0?baud=19200 -m zjiang/ZJ-58.ppd
sudo lpoptions -d ZJ-58
```

On the first line, change the “ **baud** ” value to **9600** or **19200** as required for your printer.&nbsp;The rest of the line should be typed _exactly_ as it appears above. Likewise for the second line, which needs no changes.

![](https://cdn-learn.adafruit.com/assets/assets/000/046/025/medium800/raspberry_pi_lpadmin.png?1504561307)

# Finish Up
Shut down the system. We'll work on the case and wiring next, then return to the final software configuration later.

```
sudo shutdown -h now
```

After about 30 seconds, you can disconnect the USB power cable.  
  
Remove the SD card and WiFi adapter, and get your soldering iron ready…

- [Previous Page](https://learn.adafruit.com/pi-thermal-printer/raspberry-pi-os-setup.md)
- [Next Page](https://learn.adafruit.com/pi-thermal-printer/soldering-pre-2017.md)

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
