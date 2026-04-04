# Source: https://learn.adafruit.com/webide/installation.md

# Adafruit WebIDE

## Installation

http://youtu.be/8NoiBBgaKCI

Installation of the editor can be performed in two ways. &nbsp;One is the more trusting, but much easier way, the second is a bit more manual.

## Easy installation:
Log into your Raspberry Pi. &nbsp;If you're on a Mac, you can open Terminal.app to log into the Raspberry Pi over SSH.&nbsp;Linux users can open the default terminal application.&nbsp;If you're using Windows, you'll want to download a good terminal application. &nbsp;My favorite is [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html "Link: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html"). &nbsp;  
  
Once you have the terminal application open, assuming you're using Occidentalis, type in the following: ```
$ ssh pi@raspberrypi.local
pi@raspberrypi.locals password: 
```

Once you type your password in, and get a prompt, you can copy and paste the following command, and hit enter. &nbsp;This command will download an install.sh script from our github repository, and execute it automatically for you.

```
    curl https://raw.githubusercontent.com/adafruit/Adafruit-WebIDE/master/scripts/install.sh | sudo sh
  
```

The editor will be&nbsp;installed into /usr/share/adafruit/webide using the user webide. &nbsp;The script will install node, npm, redis-server, git, and i2c-tools. &nbsp;If you'd like to review the script, it's located in our [repository](https://raw.github.com/adafruit/Adafruit-WebIDE/alpha/scripts/install.sh "Link: https://raw.github.com/adafruit/Adafruit-WebIDE/alpha/scripts/install.sh").

Danger: 

After the installation is&nbsp;complete, you'll see the following prompt:

```
**** Starting the server...(please wait) ****
**** The Adafruit WebIDE is installed and running! ****
**** Commands: sudo systemctl {start,stop,restart} adafruit-webide  ****
**** Navigate to http://raspberrypi.local:8080 to use the WebIDE
```

The editor is now installed, and you can open a browser to access it from any computer in your network. &nbsp;  
  
Due to&nbsp;our very small development team, and limited resources, the only browsers that are supported are Google Chrome, and Mozilla Firefox at this time. &nbsp;We hope to support more in the future!  
## Manual Installation:

You can manually install the editor by following along in the following installer script and choosing the components you'd like to install:

```
https://raw.githubusercontent.com/adafruit/Adafruit-WebIDE/master/scripts/install.sh
```

## Uninstallation:

To uninstall the editor you can run the following script:

```
curl https://raw.githubusercontent.com/adafruit/Adafruit-WebIDE/master/scripts/uninstall.sh | sh
```

You can also manually uninstall by removing the following components:

- Delete the folder the editor exists in.
- Uninstall nodejs npm redis-server git avahi-daemon i2c-tools.

- [Previous Page](https://learn.adafruit.com/webide/overview.md)
- [Next Page](https://learn.adafruit.com/webide/getting-started.md)

## Featured Products

### Raspberry Pi Model B 512MB RAM

[Raspberry Pi Model B 512MB RAM](https://www.adafruit.com/product/998)
Adafruit ships the **Raspberry Pi Model B 512MB RAM** as of 10/18/2012.  
  
The Raspberry Pi® is a single-board computer developed in the UK by the Raspberry Pi Foundation with the intention of stimulating the teaching of basic computer science in schools. The Raspberry...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/998)
[Related Guides to the Product](https://learn.adafruit.com/products/998/guides)
### BeagleBone Black - Rev B

[BeagleBone Black - Rev B](https://www.adafruit.com/product/1278)
**[Adafruit is no longer shipping the BeagleBone Black Rev B, it has been replaced with the Rev C as of 5/12/14](https://www.adafruit.com/products/1876) - the Rev C now has 4G flash and also comes with Debian, it also costs slightly more. There are no exchanges or...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1278)
[Related Guides to the Product](https://learn.adafruit.com/products/1278/guides)
### Adafruit Pi Box -  Enclosure for Raspberry Pi Model A or B

[Adafruit Pi Box -  Enclosure for Raspberry Pi Model A or B](https://www.adafruit.com/product/859)
 **Discontinued** - you can grab&nbsp;[Adafruit Pi Box Plus - Enclosure for RasPi Model B+/Pi 2/ Pi 3](https://www.adafruit.com/product/1985) instead!&nbsp;

**We're still selling this classic Adafruit case for those who specifically want it but <a...></a...>**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/859)
[Related Guides to the Product](https://learn.adafruit.com/products/859/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)

## Related Guides

- [Trellis Python Library](https://learn.adafruit.com/trellis-python-library.md)
- [Adafruit DVI Sock for Pico](https://learn.adafruit.com/adafruit-dvi-sock-for-pico.md)
- [Introducing Adafruit ItsyBitsy M4](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4.md)
- [SMT Breadboard Prototyping Using Breakout PCBs](https://learn.adafruit.com/smt-prototyping-using-breakout-pcbs.md)
- [Getting Started with RTL-SDR and SDR-Sharp and CubicSDR](https://learn.adafruit.com/getting-started-with-rtl-sdr-and-sdr-sharp.md)
- [Adafruit STEMMA Reflective Photo Interrupt Sensor](https://learn.adafruit.com/adafruit-stemma-reflective-photo-interrupt-sensor.md)
- [Adafruit 9-DOF Orientation IMU Fusion Breakout - BNO085](https://learn.adafruit.com/adafruit-9-dof-orientation-imu-fusion-breakout-bno085.md)
- [Adafruit I2C to 8 Channel Solenoid Driver](https://learn.adafruit.com/adafruit-i2c-to-8-channel-solenoid-driver.md)
- [Controlling Motors using the Raspberry Pi and RasPiRobot Board V2](https://learn.adafruit.com/controlling-motors-using-the-raspberry-pi-and-raspirobot-board-v2.md)
- [Adafruit Feather 32u4 FONA](https://learn.adafruit.com/adafruit-feather-32u4-fona.md)
- [Adafruit Pi Stemma QT Breakout](https://learn.adafruit.com/adafruit-pi-stemma-qt-breakout.md)
- [Adafruit's Raspberry Pi Lesson 8. Using a Servo Motor](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor.md)
- [IoT Bird Feeder with Camera](https://learn.adafruit.com/iot-window-bird-feeder-with-camera.md)
- [Using the BMP085/180 with Raspberry Pi or Beaglebone Black](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi.md)
- [AR1100 Resistive Touch Screen Controller Guide](https://learn.adafruit.com/ar1100-resistive-touch-screen-controller-guide.md)
