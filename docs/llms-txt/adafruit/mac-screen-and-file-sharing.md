# Source: https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/mac-screen-and-file-sharing.md

# Adafruit's Raspberry Pi Lesson 7. Remote Control with VNC

## Mac Screen and File Sharing

If you are a Mac user and have a few Macs on your network, then you will probably be used to seeing other Macs in the network automatically show up in the Finder, so that you can log on to them and browse the file system or even remote control them. &nbsp;

![](https://cdn-learn.adafruit.com/assets/assets/000/003/299/medium800/learn_raspberry_pi_finder1.png?1396795088)

The screen sharing feature of Macs uses VNC, so if you already have TightVNC server installed (as we do) then with a bit of configuration, we can get it to be recognized by other Macs on the network.

The tutorial here:<u><a href="http://4dc5.com/2012/06/12/setting-up-vnc-on-raspberry-pi-for-mac-access/" title="Link: http://4dc5.com/2012/06/12/setting-up-vnc-on-raspberry-pi-for-mac-access/">http://4dc5.com/2012/06/12/setting-up-vnc-on-raspberry-pi-for-mac-access/</a>
</u>explains how to do this. It also includes the installation of TightVNC server, which you do not need to repeat as we already have that.

Once its all set up, you will be able to connect to the file system of your raspberry Pi.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/300/medium800/learn_raspberry_pi_mac_file_browse_login.png?1396795104)

Remember to change the user field to pi and as usual the default password is 'raspberry'.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/301/medium800/learn_raspberry_pi_mac_file_browse.png?1396795136)

This makes it super-easy to copy files back and forth between your Mac and Pi.

If you click on the Share Screen button, you will get another login prompt.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/302/medium800/learn_raspberry_pi_mac_screen_share.png?1396795147)

This time, the password is the password you set up for the VNC server – I suggested 'raspberr'. That is with the 'y' missing from the end.

You should then get a VNC window using the Mac's built-in VNC viewer.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/303/medium800/learn_raspberry_pi_mac_screen_share2.png?1396795186)

- [Previous Page](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/running-vncserver-at-startup.md)
- [Next Page](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/test-and-configure.md)

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
