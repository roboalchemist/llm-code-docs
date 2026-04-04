# Source: https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/installing-vnc.md

# Adafruit's Raspberry Pi Lesson 7. Remote Control with VNC

## Installing VNC

SSH (see<u><a href="http://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/overview">http://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/overview</a>)</u>is often all you need to control your Raspberry Pi, however sometimes it is useful to be able to remote control your Raspberry Pi using the mouse and seeing just what you would see on the screen of the Raspberry Pi.&nbsp;

VNC (Virtual Network Connection) is a standard for doing just this. To use it, you have to install some software on your Pi. There are a number of VNC server applications, and the one we are going to use is called “tightvnc”.

We can install the VNC server software using the SSH connection that we established earlier.

Enter the following command into your SSH terminal:

```
sudo apt-get update
sudo apt-get install tightvncserver
```

![](https://cdn-learn.adafruit.com/assets/assets/000/003/160/medium800/learn_raspberry_pi_vnc_install_1.png?1396792566)

You will be prompted to confirm installation by typing “Y' and finally when installation is complete, you should see the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/003/161/medium800/learn_raspberry_pi_vnc_install_2.png?1396792598)

We now need to run the VNC Server, so enter the following command into your SSH window:

```
vncserver :1
```

![](https://cdn-learn.adafruit.com/assets/assets/000/003/162/medium800/learn_raspberry_pi_vnc_server_run.png?1396792631)

You will be prompted to enter and confirm a password. It would make sense to use “raspberry” for this, but passwords are limited to 8 characters, so I use “raspberr”. Note that this is the password that you will need to use to connect to the Raspberry Pi remotely.

You will also be asked if you want to create a separate “read-only” password – say no.

From now on, the only command that you need to type within your SSH to start the VNC server will be:

```
vncserver :1
```

The VNC server is now running and so we can attempt to connect to it, but first we must switch to the computer from which we want to control the Pi and setup a VNC client to connect to the Pi.

- [Previous Page](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/overview.md)
- [Next Page](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/using-a-vnc-client.md)

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
