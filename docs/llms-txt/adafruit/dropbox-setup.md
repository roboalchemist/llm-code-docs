# Source: https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/dropbox-setup.md

# DIY WiFi Raspberry Pi Touchscreen Camera

## Dropbox Setup

Dropbox is a “cloud” file storage and syncing service. A basic account is free and offers two gigabytes of storage. We can leverage this as a means of getting photos off the Raspberry Pi onto other devices (desktop computer, etc.) without cables or swapping cards.  
  
This pretty much requires a WiFi connection; trying to work a camera with an Ethernet cable continually attached would get tiresome. It also requires being in range of your wireless access point, with the Raspberry Pi suitably configured for access.

We’ll use **[this guide from RasPi.TV](http://raspi.tv/2013/how-to-use-dropbox-with-raspberry-pi)**&nbsp;(with minor changes as Dropbox has evolved) to get Dropbox and the Raspberry Pi to work together.&nbsp;The steps include:

- Set up Dropbox account if you don’t already have one.
- Locate the Dropbox Uploader software on the Raspberry Pi.
- Create a Dropbox app and get access credentials.

## 1. Create a Dropbox account if you don’t already have one.

A basic account (2GB limit) is free. Sign up at [Dropbox.com](http://www.dropbox.com).

## 2. Locate the Dropbox Uploader software

There should be a folder called “Dropbox-Uploader” in the pi user’s home directory. The camera installer script downloaded and placed it there.

```
cd ~/Dropbox-Uploader
```

## 3. Create a new Dropbox App through the Dropbox developer site

Visit&nbsp;[https://www.dropbox.com/developers/apps](https://www.dropbox.com/developers/apps)&nbsp;and log in with your Dropbox account credentials.

Use the “Create app” button to begin the process…

![](https://cdn-learn.adafruit.com/assets/assets/000/037/434/medium800/raspberry_pi_dropbox1.png?1479779720)

Select “Dropbox API” and “Full Dropbox,” then assign your app a unique name (e.g. “Bob’s Raspberry Pi Camera”), then click “Create App.”

![](https://cdn-learn.adafruit.com/assets/assets/000/037/435/medium800/raspberry_pi_dropbox2.png?1479779774)

In the Settings tab for your new app, there’s a section with the heading “OAuth 2.” Look for the button “Generate access token.” This will give a long string of seemingly random letters — a unique identifier for tying your camera to your Dropbox account. (This is different from the “App key” and “App secret” — don’t use those — look for the long _access token!_)

![](https://cdn-learn.adafruit.com/assets/assets/000/037/436/medium800/raspberry_pi_dropbox3.png?1479779865)

This last step is easiest if you have SSH enabled on the Pi and are logged in through a terminal program, so you can just copy-and-paste rather than having to type in that whole string exactly…

## 4. Set up Dropbox Uploader

You should be inside the Dropbox-Uploader directory at this point (i.e. typing “pwd” should return “/home/pi/Dropbox-Uploader”).

Run the dropbox\_uploader.sh script:

```
./dropbox_uploader.sh
```

You’ll be prompted to enter your access token that was generated in Step 3. This must be _exact,_ which is why ssh and copy-and-paste is so helpful.

If you mess up this process, you can run “./dropbox\_uploader.sh unlink” to clear out Dropbox Uploader’s settings and start over.

Let’s test it!

```
echo 12345 &gt; foo.txt
./dropbox_uploader.sh upload foo.txt /
```

This will create a small text file (foo.txt) containing the string “12345” and will upload it to the root level of your Dropbox drive. If Dropbox is installed on your “main” computer the file should appear there after a moment, else use a web browser to log into your Dropbox account and you should see it there among your files.

 **If this works, then next time you run the cam.py script you can go into _Settings_ and select _Dropbox_ for storage. Photos will be saved both in the “Photos” folder and uploaded immediately to Dropbox.**

- [Previous Page](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/pi-setup.md)
- [Next Page](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/using-the-camera.md)

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
