# Source: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/using-ssh-on-a-mac-or-linux.md

# Adafruit's Raspberry Pi Lesson 6. Using SSH

## Using SSH on a Mac or Linux

Now switch over to using the computer from which you wish to control the Pi.

If you are using a Mac or Linux PC then open a Terminal. On the Mac, you can find this in the Utilities folder of your Applications folder.

Enter the following command into the Terminal window. _That's a lowercase L after the dash!_

```
ssh 192.168.1.13 -l pi
```

You can also use `ssh pi@192.168.1.13`

Note that you will need to replace the IP address above with that of your Pi. You can find this by running the command “sudo ifconfig” from the Terminal.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/154/medium800/learn_raspberry_pi_finding_ip_address.png?1396792421)

![](https://cdn-learn.adafruit.com/assets/assets/000/003/155/medium800/learn_raspberry_pi_mac_ssh.png?1396792450)

The option “-l pi' specifies that we want to **l** og into the Pi as the user “pi”. The first time you run the command, you will get a security warning about not being able to verify the identity of the machine, say that you want to continue and enter your password (“raspberry” by default) when prompted.

You will notice that the command prompt will change to indicate that you are now connected to your Pi. Try using the “ls” command to show the contents of the current folder on the Pi.

- [Previous Page](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/enabling-ssh.md)
- [Next Page](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/ssh-under-windows.md)

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
