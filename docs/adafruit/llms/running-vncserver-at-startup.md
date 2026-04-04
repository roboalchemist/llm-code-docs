# Source: https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/running-vncserver-at-startup.md

# Adafruit's Raspberry Pi Lesson 7. Remote Control with VNC

## Running VNCServer at Startup

Info: 

Connecting to your Raspberry Pi remotely with VNC is fine as long as your Pi does not reboot. If it does, then you either have to connect with SSH and restart the VNC Server or arrange for the VNC Server to run automatically after the Raspberry Pi reboots.

There are several different methods of arranging for some code to be run as the Pi starts. The method described below is probably the easiest to use. You can adapt it to run other commands instead of starting the VNC server.

**Step 1.**

Open a Terminal session on the Pi, or connect using SSH. A new terminal or SSH session will automatically start you off in your home directory of /home/pi. If you are not in this directory,&nbsp;change to it by typing:

```
$ cd /home/pi
```

Then cd to the .config directory by typing:

```
$ cd .config
```

Note the '.' at the start of the folder name. This makes it a hidden folder that will not show up when you type 'ls'.

**Step 2.**

Issue the command below to create a new directory inside .config called 'autostart'.

```
$ mkdir autostart
```

cd into that new directory by typing:

```
$ cd autostart
```

![](https://cdn-learn.adafruit.com/assets/assets/000/003/297/medium800/learn_raspberry_pi_autostart1.png?1396795036)

 **Step 3.**

All that remains is to edit a new configuration file. So type the following command to open the nano editor on the new file:

```
$ nano tightvnc.desktop
```

Edit the contents of the file with the following text.

```
[Desktop Entry]
Type=Application
Name=TightVNC
Exec=vncserver :1
StartupNotify=false
```

![](https://cdn-learn.adafruit.com/assets/assets/000/003/298/medium800/learn_raspberry_pi_autostart2.png?1396795066)

Type ctrl-X and then Y to save the changes to the file.

Thats all there is to it. The next time you reboot the VNC server will restart automatically.

- [Previous Page](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/using-a-vnc-client.md)
- [Next Page](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/mac-screen-and-file-sharing.md)

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

- [Using a Mini PAL/NTSC Display with a Raspberry Pi](https://learn.adafruit.com/using-a-mini-pal-ntsc-display-with-a-raspberry-pi.md)
- [Arm-based IoT Kit for Cloud IoT Core - Getting Started](https://learn.adafruit.com/raspberry-pi-3-and-sensor-kit-for-google-cloud-iot-core.md)
- [Windows IoT Core Application Development: Headless Blinky](https://learn.adafruit.com/windows-iot-application-development-headless-application.md)
- [Simple Raspberry Pi Robot](https://learn.adafruit.com/simple-raspberry-pi-robot.md)
- [NeoPixels on Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi.md)
- [Portable 5in Monitor with HDMI](https://learn.adafruit.com/portable-5in-monitor-with-hdmi.md)
- [2.2" PiTFT HAT Enclosure](https://learn.adafruit.com/3d-printed-2-2-pitft-raspberry-pi-a-plus-enclosure.md)
- [Bluefruit LE Python Library](https://learn.adafruit.com/bluefruit-le-python-library.md)
- [Adafruit Pi Cobbler Kit](https://learn.adafruit.com/adafruit-pi-cobbler-kit.md)
- [Naughty or Nice Machine](https://learn.adafruit.com/naughty-or-nice-machine.md)
- [DHT Humidity Sensing on Raspberry Pi or Beaglebone Black with GDocs Logging](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.md)
- [Adafruit's Raspberry Pi Lesson 1. Preparing an SD Card for your Raspberry Pi](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi.md)
- [Mini Raspberry Pi Handheld Notebook](https://learn.adafruit.com/mini-raspberry-pi-handheld-notebook-palmtop.md)
- [Pi Box](https://learn.adafruit.com/pi-box.md)
- [Running Programs Automatically on Your Tiny Computer](https://learn.adafruit.com/running-programs-automatically-on-your-tiny-computer.md)
