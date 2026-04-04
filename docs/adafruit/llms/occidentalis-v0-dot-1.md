# Source: https://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-1.md

# Adafruit Raspberry Pi Educational Linux Distro

## Occidentalis v0.1

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/532/medium800/raspberry_pi_occidentalis.png?1396773187)

This is our first distro, &nbsp; **Occidentalis v0.1**. **Rubus occidentalis&nbsp;** is the black raspberry.&nbsp;&nbsp;It is derived from&nbsp;Raspbian Wheezy&nbsp;July 15  
  
We have made a few key changes to make it more hardware-hacker friendly!

- [Updated to Hexxeh firmware](https://raw.github.com/Hexxeh/rpi-update/master/rpi-update)
- 4 Gig SD image (will not fit in 2 G cards!)
- [I2C](http://www.bootc.net/archives/2012/05/19/i2c-and-the-raspberry-pi/ "Link: http://www.bootc.net/archives/2012/05/19/i2c-and-the-raspberry-pi/") and [hardware SPI](http://www.brianhensley.net/2012/07/getting-spi-working-on-raspberry-pi.html) support
- I2C/SPI modules initialized on boot
- sshd on boot
- ssh keygen on first boot
- runs avahi daemon (Bonjour client) and is called&nbsp; **raspberrypi.local**
- [Realtek RTL8188CUS wifi support](http://www.adafruit.com/products/814 "Link: http://www.adafruit.com/products/814")
- [One wire support on GPIO #4 when loaded](https://github.com/FrankBuss/linux-1/commit/71871509238d3e7bce4a74cdf616c3f12542acaa)

Please keep in mind, we are not full time&nbsp;linux distro maintainers - we will try to fix any bugs we find but this distro is not for beginners or people who are new to linux!  
Info: 

# How to Install!
  
Click below to download the ZIP file:  
  

- [Adafruit Raspberry Pi Educational Distro - Occidentalis v0.1](http://adafruit-raspberry-pi.s3.amazonaws.com/Occidentalisv01.zip) **!700 Megs!&nbsp;** (August 2, 2012)  
MD5 of the&nbsp;img itself (not the zip): &nbsp; **34b5d3d511fcce0b82186816119d9881**  
MD5 of the&nbsp;zip:&nbsp; **cc3559cb6e7cb5f33b0e46118e16b748**  
SHA1 of the img: **&nbsp;e95dbb306bee8a9f77b486c729c7869923b7ee43**  
SHA1 of the zip: **&nbsp;72eb71d316b8765d5594878b8662f2118dc4320a**

  
and decompress it. Note that it is 4 GB large! You will need a 4GB card or larger. [We suggest using our 4GB SD card which works great](http://adafruit.com/products/102 "Link: http://adafruit.com/products/102")  
  
You will also need a SD or MicroSD&nbsp;card writer to burn the image on.[&nbsp;We suggest using our speedy MicroSD card writer that works with any OS.](http://adafruit.com/products/939 "Link: http://adafruit.com/products/939")  
  
[Then follow the directions here](http://elinux.org/RPi_Easy_SD_Card_Setup "Link: http://elinux.org/RPi\_Easy\_SD\_Card\_Setup"), except use the downloaded and uncompressed&nbsp;Occidentalis image instead of Wheezy # I2C Support
I2C support is on SDA and SCL pins. To test, connect any I2C device to power, ground, SDA and SCL. Then run &nbsp; **i2cdetect -y 0** (as root)&nbsp;to detect which addresses are on the bus  
  
[For more ideas, check out this post](http://www.bootc.net/archives/2012/05/19/i2c-and-the-raspberry-pi/ "Link: http://www.bootc.net/archives/2012/05/19/i2c-and-the-raspberry-pi/") (by the most awesome cboot) and others on the Raspberry Pi forums  
  
**Our [BMP085](http://learn.adafruit.com/using-the-bmp085-with-raspberry-pi "Link: http://learn.adafruit.com/using-the-bmp085-with-raspberry-pi"), [MCP4725,](http://learn.adafruit.com/mcp4725-12-bit-dac-with-raspberry-pi "Link: http://learn.adafruit.com/mcp4725-12-bit-dac-with-raspberry-pi") [Servo Driver](http://http://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi), and [7-segment breakout](http://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi) tutorials cover using I2C via Python on the Pi - so please check those out and read the code examples for I2C interfacing ideas!**  # SPI Support
SPI support is on the CLK/MOSI/MISO/CS0/CS1 pins. To test, connect your logic analyser/scope to the pins and run **echo "testtext" \>&nbsp;/dev/spidev0.0** to send some dummy data to the SPI port. You can simply read/write the /dev/spidev files to read/write from SPI  
  
**Our** [**Light Painting**](http://learn.adafruit.com/light-painting-with-raspberry-pi) **tutorial uses the hardware SPI system to write to digital LED strip,&nbsp;** [**we also have a 'bitbanging' software SPI tutorial here**](http://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi "Link: http://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi") **if you need such a thing**  
# One Wire Support
One wire is most commonly used for DS18B20 temp sensors. The Pi does not have 'hardware' 1-wire support but it can bitbang it with some success. Connect a DS18B20 with VCC to 3V, ground to ground and Data to GPIO #4. Then connect a 4.7K resistor from Data to VCC.  
  
Then run as **root** : **modprobe w1-gpio** and then **modprobe w1-therm** to attach the temperature submodule. Then you can run **cat /sys/bus/w1/devices/28-\*/w1\_slave** to read the temperature data from the bus  
  
The first line has the CRC, if its "NO" then the data is corrupted. If you get a good CRC check, the second line has t=temperature in 1/1000 of a degree Centigrade. For example, below, the temperature is 24.5°C  
  
Since 1-wire is bitbanged, its flakier than SPI or I2C. [We have a short tutorial on using a DS18B20 sensor](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing)  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/531/medium800/1wire.bmp?1343962063)

# WiFi support
[We wanted to get our WiFI modules working](http://www.adafruit.com/products/814), so we applied the RTL8192cu-based patches to the kernel. Please note that you almost certianly need a powered USB hub to run a wifi dongle.   
  
Type **ifconfig -a** to verify that **wlanN** (wlan0, wlan1, etc) entry has been created.  
  
You will have to edit **/etc/network/interfaces** with your SSID and password but after that, it should 'just work' - check **iwconfig** and **iwscan** if you're having problems  
  
[We have a tutorial on WiFi setup here](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/overview)  
Info: 

# Bonjour Support
  
Bonjour is what Apple uses to make it easier to find new devices on a LAN. Instead of having to look up the IP address, there's a local name. This distro uses&nbsp; **raspberrypi.local** by default. All Apple machines have Bonjour servers. If you have ever installed iTunes, it comes with it. [Other Windows users can get it from here](http://support.apple.com/kb/DL999)- its called the print server but its what you want  
  
Test by trying to&nbsp; **ping raspberrypi.local** when the Pi is booted and connected to Ethernet (or WiFi once you have configured WiFi) # sshd on Boot
  
This image has **sshd** on boot - that means you can immediately ssh in using&nbsp; **raspberrypi.local**! The ssh keys are generated on boot but since the user/pass is simply&nbsp; **pi** / **raspberry** you should not put this on an&nbsp;accessible&nbsp;network &nbsp;until you've changed the password # Kernel Source
  
Want to compile your own modules? Or change the configuration of the kernel?[Advanced users can find our kernel repo here](https://github.com/adafruit/adafruit-raspberrypi-linux)  
  
We do not have any tutorials on how to download, compile or install the linux kernel.  
- [Previous Page](https://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2.md)

## Featured Products

### USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC

[USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC](https://www.adafruit.com/product/939)
This is the cutest little microSD card reader/writer - but don't be fooled by its adorableness! It's wicked fast and supports up to 64 GB SDXC cards! Simply slide the card into the edge and plug it into your computer. No drivers are required, it shows up as a standard 'Mass...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/939)
[Related Guides to the Product](https://learn.adafruit.com/products/939/guides)
### Raspberry Pi - Skill badge, iron-on patch

[Raspberry Pi - Skill badge, iron-on patch](https://www.adafruit.com/product/906)
You are learning to use the small Linux based board, the Raspberry Pi! Adafruit offers a fun and exciting "badges" of achievement for electronics, science and engineering. We believe everyone should be able to be rewarded for learning a useful skill, a badge is just one of the many...

In Stock
[Buy Now](https://www.adafruit.com/product/906)
[Related Guides to the Product](https://learn.adafruit.com/products/906/guides)
### SD/MicroSD Memory Card (8 GB SDHC)

[SD/MicroSD Memory Card (8 GB SDHC)](https://www.adafruit.com/product/1294)
Add mega-storage in a jiffy using this 8 GB class 4 micro-SD card. It comes with a SD adapter so you can use it with any of our shields or adapters. Preformatted to FAT so it works out of the box with our projects. Tested and works great with our <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/1294)
[Related Guides to the Product](https://learn.adafruit.com/products/1294/guides)

## Related Guides

- [Internet of Things Printer for Raspberry Pi](https://learn.adafruit.com/pi-thermal-printer.md)
- [Skill Badge Requirements: Raspberry Pi](https://learn.adafruit.com/skill-badge-requirements-raspberry-pi.md)
- [Adafruit Prototyping Pi Plate](https://learn.adafruit.com/adafruit-prototyping-pi-plate.md)
- [Adafruit's Raspberry Pi Lesson 2. First Time Configuration](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration.md)
- [Raspberry Pi Kernel-o-Matic](https://learn.adafruit.com/raspberry-pi-kernel-o-matic.md)
- [Raspberry Pi Analog to Digital Converters](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters.md)
- [Controlling Motors using the Raspberry Pi and RasPiRobot Board V2](https://learn.adafruit.com/controlling-motors-using-the-raspberry-pi-and-raspirobot-board-v2.md)
- [CircuitPython Libraries on Linux and Orange Pi](https://learn.adafruit.com/circuitpython-on-orangepi-linux.md)
- [Raspberry Pi as an Ad Blocking Access Point](https://learn.adafruit.com/raspberry-pi-as-an-ad-blocking-access-point.md)
- [Using an External Drive as a Raspberry Pi Root Filesystem](https://learn.adafruit.com/external-drive-as-raspberry-pi-root.md)
- [Teddy Ruxpin Rebuild](https://learn.adafruit.com/teddy-ruxpin-rebuild.md)
- [RasPipe: A Raspberry Pi Pipeline Viewer, Part 1](https://learn.adafruit.com/raspipe-a-raspberry-pi-pipeline-viewer.md)
- [Running Programs Automatically on Your Tiny Computer](https://learn.adafruit.com/running-programs-automatically-on-your-tiny-computer.md)
- [Speech Synthesis on the Raspberry Pi](https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi.md)
- [Read-Only Raspberry Pi](https://learn.adafruit.com/read-only-raspberry-pi.md)
