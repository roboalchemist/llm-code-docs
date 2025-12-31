# Source: https://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2.md

# Adafruit Raspberry Pi Educational Linux Distro

## Occidentalis v0.2

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/953/medium800/raspberry_pi_occidentalis.png?1396777747)

This is our second distro, **Occidentalis v0.2**. **Rubus occidentalis** is the black raspberry. It is derived from [Raspbian Wheezy August 16 2012](http://www.raspberrypi.org/downloads "Link: http://www.raspberrypi.org/downloads")  
  
We have made a few key changes to make it more hardware-hacker friendly!  
  
**Version 0.2 updates (new!)**

- Truncated image - only 2.6G now to fit on any 4G card
- raspi-config notice retained on boot
- Removed persistant wlan0 entry
- Password-change reminder on login  
- Added **RTC** and **lm-sensors** kernel module
- Included kernel modules for: DS1307, AD525x I2C digipots, HMC6352, BMP085, ADS1015
- **New! Adafruit's PWM/Servo kernel module for easy PWM/Servo control on GPIO#18**  

  
**Version 0.1 updates (still included)**  

- [Updated to Hexxeh firmware](https://raw.github.com/Hexxeh/rpi-update/master/rpi-update "Link: https://raw.github.com/Hexxeh/rpi-update/master/rpi-update")
- [I2C](http://www.bootc.net/archives/2012/05/19/i2c-and-the-raspberry-pi/) and [hardware SPI](http://www.brianhensley.net/2012/07/getting-spi-working-on-raspberry-pi.html) support
- I2C/SPI modules initialized on boot
- sshd on boot
- ssh keygen on first boot
- runs avahi daemon (Bonjour client) and is called **raspberrypi.local**
- [Realtek RTL8188CUS wifi support](http://www.adafruit.com/products/814)
- [One wire support on GPIO #4 when loaded](https://github.com/FrankBuss/linux-1/commit/71871509238d3e7bce4a74cdf616c3f12542acaa)

Please keep in mind, we are not full time linux distro maintainers - we will try to fix any bugs we find but this distro is not for beginners or people who are new to linux!  
Info: 

# How to Install!
  
Click below to download the ZIP file:  
  

- [Adafruit Raspberry Pi Educational Distro - Occidentalis v0.2](http://adafruit-raspberry-pi.s3.amazonaws.com/Occidentalisv02.zip) **!900 Megs!&nbsp;** (August 31, 2012)  
MD5 of the&nbsp;img itself (not the zip):&nbsp; **4256c0cdad82fa193c5e902143f1ca0e**  
MD5 of the&nbsp;zip:&nbsp; **43456900352bb8bd8860902167195d83**
- SHA1 of image:&nbsp; **a609f588bca86694989ab7672badbce423aa89fd**
- SHA1 of zip:&nbsp; **5f33ec07a183f336f973f82634f04108f690f5f3**

and decompress it. Note that it is 2.6 GB large! You will need a 4GB card or larger. [We suggest using our 4GB SD card which works great](http://adafruit.com/products/102 "Link: http://adafruit.com/products/102") After booting, run **sudo raspi-config** to auto-expand the file system to fit the card you've decided on  
  
You will also need a SD or MicroSD&nbsp;card writer to burn the image on.[&nbsp;We suggest using our speedy MicroSD card writer that works with any OS.](http://adafruit.com/products/939 "Link: http://adafruit.com/products/939")  
  
[Then follow the directions here](http://elinux.org/RPi_Easy_SD_Card_Setup "Link: http://elinux.org/RPi\_Easy\_SD\_Card\_Setup"), except use the downloaded and uncompressed&nbsp;Occidentalis image instead of Wheezy  
# Features!
  
[For details on the I2C, SPI, WiFi, Avahi, and 1-Wire modules please visit the v0.1 page](http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-1 "Link: http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-1")  
  
New Features in v0.2!  
  

# New in v0.2, we have some great goodies!

## Smaller Image
First up, we did not expand the filesystem beyond 2.6G, so the image itself is much smaller - only 2.6G instead of 4G. This will make writing the image faster, and it should also work better with a variety of 4G cards. There was no way to fit this in a 2G card, otherwise we would have done it.  
  

## Password and Configuration Reminders
Second, we retained the **raspi-config** notice on startup, just like the stock Wheezy distro. This will help people who wanted a reminder on how to set the timezone, disk size, password, keyboard, etc.  
  
We also added a basic password reminder into ~/.profile - it will just check if the password hasn't been changed from the default. Change your password as soon as you boot, please!  
  

## Hardware RTC Support
The biggest news is we added a bunch of fun goodies to the kernel. We added **RTC** support so you can have an external RTC and use **hwclock** &nbsp; - [we even have a tutorial about it here](http://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi).   
  

## Sensors Modules
We poked around the Kernel configuration file and added in module support for a few familiar sensors such as: AD525x Digipots, HMC6352 compass, BMP085 barometric/temp sensor, ADS1015 I2C ADCs, etc.   
  
**Please Note:** we didn't write or support these kernel modules, and we're not even sure if they all work, please experiment and read any kernel documentation about these modules as we do not have any tutorials or support for them at this time!  
  
  
# PWM and Servo Kernel Module
The most exciting addition is our custom-written kernel module specifically for handling the PWM/Servo capability of the Raspberry Pi's GPIO #18 pin. Unfortunately there is only one PWM pin available on the GPIO header **and** its shared with the Audio system. That means that **you can't use PWM/Servo output and play audio through the 3.5mm jack at the same time.** However, there might be a few situations where you just need a single servo or PWM and audio isn't a requirement.  
  
The module was written by Sean Cross for Adafruit Industries, code is available at our github repository (see below)  
  
This driver can be controlled through its sysfs entries. &nbsp;It will create the directory **/sys/class/rpi-pwm/pwm0/** and populate it with the following files:  

- **active** - Reports **1** if PWM is active. In **delayed** mode, write a **1** to this file to activate stored settings. Deactivate by writing a 0 to this file.
- **delayed** - If **0** , any settings made will become active immediately. If **1** , then settings are stored and won't take effect until a **1** is written into **active**.
- **mode** - The PWM mode. One of **servo** , **pwm** , or **audio**.
- **servo** - Moves the servo to this step. &nbsp;Range (0..servo\_max) where **0** is a 0.5ms-long pulse and **servo\_max** is a 2.5ms-long pulse.
- **servo\_max** - The maximum number of servo steps, default of 32
- **duty** - Duty cycle percentage for PWM mode. &nbsp;Range (1..99) where 1 is the shortest positive pulse and 99 is the widest positive   
- **frequency** - Desired frequency for PWM mode, write the value to this file  
- **real\_frequency** - The actual computed frequency, read the value from this file.  
- **mcf** - A maximum common frequency (see _Advanced_ below).

If you attempt to set a frequency or duty cycle that the Raspberry Pi does not support, you will get an error such as:  
**write error: Numerical result out of range**  
If this happens, the PWM will stop until you set values that are in range.  
  
The **mode** file can be used to switch between **pwm** , **servo** , and **audio** mode:  

- **pwm** - Drives a pulse with a frequency specified by the **frequency** file and a duty cycle of&nbsp; **duty**.
- **servo** - A special PWM mode that will drive a servo throughout its range of rotation, starting with 0.5ms wide pulse and ending with 2.5ms, some servos only respond to 1.0-2.0ms and some have a wider range, you will need to experiment to find the full range of your servo. Values are taken from the file **servo** ,&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; and range from 0 to **servo\_max** (default 32 which is the max resolution of 62.5us.) The PWM system does not seem to be able to handle a resolution better than 62.5us which is approximately 20 different servo positions or speeds. If you need better resolution, [please check out our 16-channel servo driver tutorial which has 16 channels and 4us resolution](http://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/overview "Link: http://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/overview")
- **audio** - Echos the unfiltered contents of the right audio channel out the PWM port. &nbsp;Also enables **delayed** mode so that accidentally modifying PWM parameters won't cause the audio system to lock.  

Using the PWM and playing audio at the same time is dicey at best. If you want to mirror audio out the PWM port, write **audio** into the **mode** file and leave it. When audio playback is done, you can switch back into **pwm** or **servo** mode. Then, either write **0** into the **delayed** file to get back into immediate mode, or set your parameters and write a **1** into the **activate** file.  
  

## Advanced settings

## 
The default **mcf** is 16000 Hz. This is the frequency at which the PCM audio clock will run. The actual PWM output is derived based on this value, so it should be higher than the desired output frequency. For small duty cycles or for higher frequencies (e.g. above about 8 kHz), you may need to increase this value to get a more accurate **real\_frequency**. Due to rounding, it may not be possible to get your desired output rate. Compare the contents of the **real\_frequency** file with that of the **frequency** file to determine accuracy.  
  
# Kernel Source
  
Want to compile your own modules? Or change the configuration of the kernel?[Advanced users can find our kernel repo here](https://github.com/adafruit/adafruit-raspberrypi-linux)  
  
[We also have a Kernel+Modules tgz file](http://adafruit-raspberry-pi.s3.amazonaws.com/OccidentalisV02Kernel.tgz), after you've copied this over to your pi, run the following commands  

- **tar -zxvf mykernel.tgz**
- **sudo cp tmp/kernel.img /boot/**
- **sudo cp -R tmp/modules/lib/\* /lib/**
- **rm -rf tmp**  

We do not have any tutorials on how to download, compile or install the linux kernel.  
  
  
- [Previous Page](https://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-3.md)
- [Next Page](https://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-1.md)

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

- [Skill Badge Requirements: Raspberry Pi](https://learn.adafruit.com/skill-badge-requirements-raspberry-pi.md)
- [Internet of Things Printer for Raspberry Pi](https://learn.adafruit.com/pi-thermal-printer.md)
- [Adafruit Prototyping Pi Plate](https://learn.adafruit.com/adafruit-prototyping-pi-plate.md)
- [Send Raspberry Pi Data to COSM](https://learn.adafruit.com/send-raspberry-pi-data-to-cosm.md)
- [Press Your Button for Raspberry Pi](https://learn.adafruit.com/press-your-button-for-raspberry-pi.md)
- [Introducing the Raspberry Pi 2 - Model B](https://learn.adafruit.com/introducing-the-raspberry-pi-2-model-b.md)
- [Running Programs Automatically on Your Tiny Computer](https://learn.adafruit.com/running-programs-automatically-on-your-tiny-computer.md)
- [Resizing the Raspberry Pi Boot Partition](https://learn.adafruit.com/resizing-raspberry-pi-boot-partition.md)
- [Debugging with the Raspberry Pi WebIDE](https://learn.adafruit.com/debugging-with-the-raspberry-pi-webide.md)
- [Raspberry Pi as an Ad Blocking Access Point](https://learn.adafruit.com/raspberry-pi-as-an-ad-blocking-access-point.md)
- [Kali Linux on the Raspberry Pi with the PiTFT](https://learn.adafruit.com/kali-linux-on-the-raspberry-pi-with-the-pitft.md)
- [An Illustrated Guide to Shell Magic: Standard I/O & Redirection](https://learn.adafruit.com/basic-shell-magic.md)
- [Adafruit's Raspberry Pi Lesson 9. Controlling a DC Motor](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-9-controlling-a-dc-motor.md)
- [Windows IoT Core Application Development: Headed Blinky](https://learn.adafruit.com/windows-iot-application-development-headed-blinky.md)
- [Chumby Hacker Board](https://learn.adafruit.com/chumby-hacker-board.md)
