# Source: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/enabling-ssh.md

# Adafruit's Raspberry Pi Lesson 6. Using SSH

## Enabling SSH

Secure Shell (SSH)&nbsp;is a feature of Linux that allows you to effectively open a terminal session on your Raspberry Pi from the command line of your host computer.

**Recent versions of Rasbpian do not enable SSH access by default.&nbsp;** You can use an empty boot file or **raspi-config** , which you first saw [back in Lesson 2](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration)

# Using a blank boot file

For truly headless setups, if you can't **ssh** into your Pi you can't turn on **ssh**!

It's a bit of conundrum! But you can easily get around it by using a trick in Raspbian. To do so, we simply create a file called **ssh**. _This file does not exist by default and needs to be created_. It can be empty. The system looks for it at boot time and will enable ssh if it is there. It is then deleted. So just create a new file and save it as **ssh** to the **boot** folder. If you plug the SD card into your computer, just put that **ssh** file directly in the SD card director's root directory

![](https://cdn-learn.adafruit.com/assets/assets/000/045/315/medium800/learn_raspberry_pi_sshfile.png?1502842890)

# Using Raspi-Config

In order to do this, open LX Terminal on your Pi and enter the following command to start Raspi Config:

```
sudo raspi-config
```

![](https://cdn-learn.adafruit.com/assets/assets/000/003/150/medium800/learn_raspberry_pi_starting_raspi-config.png?1396792319)

Scroll down to the “ssh” option, it might be under **Interfaces** or **Advanced** (they move it around)

![](https://cdn-learn.adafruit.com/assets/assets/000/003/151/medium800/learn_raspberry_pi_raspi_config_ssh1.png?1396792349)

Hit the Enter key and then select “Enable”

![](https://cdn-learn.adafruit.com/assets/assets/000/003/152/medium800/learn_raspberry_pi_raspi_config_ssh2.png?1396792370)

A script will run and then you will see the following as confirmation:

![](https://cdn-learn.adafruit.com/assets/assets/000/003/153/medium800/learn_raspberry_pi_raspi_config_ssh3.png?1396792389)

You will need to reboot your Pi to make the change permanent

- [Previous Page](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/overview.md)
- [Next Page](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/using-ssh-on-a-mac-or-linux.md)

## Featured Products

### Budget Pack for Raspberry Pi 1 Model B (Doesn't include RasPi)

[Budget Pack for Raspberry Pi 1 Model B (Doesn't include RasPi)](https://www.adafruit.com/product/965)
An optimized collection of parts and pieces to experiment with Raspberry Pi at home, school or work. Great for students and those that want to get their feet wet, no soldering required! **THIS PACK DOES NOT INCLUDE A RASPBERRY PI 1 MODEL B and is NOT compatible with Model B+ or Raspberry Pi...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/965)
[Related Guides to the Product](https://learn.adafruit.com/products/965/guides)
### Programming the Raspberry Pi: Getting Started with Python

[Programming the Raspberry Pi: Getting Started with Python](https://www.adafruit.com/product/1089)
 **Program your own Raspberry Pi projects!**

An updated guide to programming your own Raspberry Pi projects. Learn to create inventive programs and fun games on your powerful Raspberry Pi--with no programming experience required. **This practical book has been revised...**

In Stock
[Buy Now](https://www.adafruit.com/product/1089)
[Related Guides to the Product](https://learn.adafruit.com/products/1089/guides)

## Related Guides

- [Raspberry Gear](https://learn.adafruit.com/raspberry-gear.md)
- [Raspberry Pi Thermal Printer One Time Pads](https://learn.adafruit.com/raspberry-pi-thermal-printer-one-time-pads.md)
- [A DigitalOcean droplet in 10 minutes](https://learn.adafruit.com/a-digitalocean-droplet-in-10-minutes.md)
- [Raspberry Pi Kernel-o-Matic](https://learn.adafruit.com/raspberry-pi-kernel-o-matic.md)
- [7" Portable HDMI Monitor](https://learn.adafruit.com/7-hdmi-portable-monitor.md)
- [Using OSC to Communicate with a Raspberry Pi](https://learn.adafruit.com/raspberry-pi-open-sound-control.md)
- [DotStar Pi Painter](https://learn.adafruit.com/dotstar-pi-painter.md)
- [Raspberry Pi Computer Quick-Start](https://learn.adafruit.com/raspberry-pi-computer-quick-start.md)
- [Wood Case for Raspberry Pi 3](https://learn.adafruit.com/wood-case-for-raspberry-pi-3.md)
- [Using an External Drive as a Raspberry Pi Root Filesystem](https://learn.adafruit.com/external-drive-as-raspberry-pi-root.md)
- [Getting Started With Windows IoT Core on Raspberry Pi](https://learn.adafruit.com/getting-started-with-windows-iot-on-raspberry-pi.md)
- [Pi Box](https://learn.adafruit.com/pi-box.md)
- [Kali Linux on the Raspberry Pi with the PiTFT](https://learn.adafruit.com/kali-linux-on-the-raspberry-pi-with-the-pitft.md)
- [Raspberry Pi RGB LED Matrix Webapp](https://learn.adafruit.com/raspberry-pi-rgb-led-matrix-webapp.md)
- [Raspberry Pi Pygame UI basics](https://learn.adafruit.com/raspberry-pi-pygame-ui-basics.md)
