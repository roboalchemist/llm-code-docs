# Source: https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/using-the-adafruit-bmp085-python-library.md

# Using the BMP085/180 with Raspberry Pi or Beaglebone Black

## Using the Adafruit BMP085 Python Library

Danger: 

Warning: 

The BMP085&nbsp;Python code for Pi&nbsp;is available on Github at&nbsp;[https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code)  
  
While many of these drivers and classes are works in progress -- we're still trying to figure out how we can make accessing HW as painless as possible on the Pi -- the current code should serve as a good starting point to understanding how you can access SMBus/I2C devices with your Pi, and getting some basic data out of your BMP085.

# Downloading the Code from Github
The easiest way to get the code onto your Pi is to hook up an Ethernet cable, and clone it directly using 'git', which is installed by default on most distros. &nbsp;Simply run the following commands from an appropriate location (ex. "/home/pi"): ```
$ git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
$ cd Adafruit-Raspberry-Pi-Python-Code
$ cd Adafruit_BMP085 
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/660/medium800/raspberry_pi_GitClone.png?1396774761)

# Testing the Library
If you're using a version 2 Pi (512 M) then you'll have to change the I2C bus as it flipped from #0 to #1 in the version 2.  
Edit Adafruit\_I2C.py with **nano Adafruit\_I2C.py** and change this line  

> **def \_\_init\_\_(self, address, bus=smbus.SMBus(0), debug=False):**

to  

> **def \_\_init\_\_(self, address, bus=smbus.SMBus(1), debug=False)**

  
Once the code has be downloaded to an appropriate folder, and you have your BMP085 properly connected, you can start reading some data via the following command (the driver includes a simple demo program):   
  
```
sudo python Adafruit_BMP085_example.py
```

Which should give you something similar to the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/661/medium800/raspberry_pi_BMP085Example_Update.png?1396774771)

# Modifying the Code
The BMP085 library is organized as two seperate classes. &nbsp;There is one class to&nbsp;handle the low-level SMBus/I2C calls (Adafruit\_I2C), and another class that handles the BMP085-specific functionality.  
  
The library includes the basic example shown above, but you can also customize the code a bit to provide full debug output if you're having any problems, change the address, or use the BMP085 in one of it's four different modes (ULTRALOWPOWER, STANDARD, HIRES, and ULTRAHIRES),&nbsp;as seen in the commented out&nbsp;initializors in the sample code below: ```
#!/usr/bin/python

from Adafruit_BMP085 import BMP085

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)

# To specify a different operating mode, uncomment one of the following:
# bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
# bmp = BMP085(0x77, 1)  # STANDARD Mode
# bmp = BMP085(0x77, 2)  # HIRES Mode
# bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

temp = bmp.readTemperature()
pressure = bmp.readPressure()
altitude = bmp.readAltitude()

print "Temperature: %.2f C" % temp
print "Pressure:    %.2f hPa" % (pressure / 100.0)
print "Altitude:    %.2f" % altitude
```

- [Previous Page](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/using-the-adafruit-bmp-python-library.md)
- [Next Page](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/faqs.md)

## Featured Products

### BMP180 Barometric Pressure/Temperature/Altitude Sensor- 5V ready

[BMP180 Barometric Pressure/Temperature/Altitude Sensor- 5V ready](https://www.adafruit.com/product/1603)
This precision sensor from Bosch is the best low-cost sensing solution for measuring barometric pressure and temperature. Because pressure changes with altitude you can also use it as an altimeter! The sensor is soldered onto a PCB with a 3.3V regulator, I2C level shifter and pull-up resistors...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1603)
[Related Guides to the Product](https://learn.adafruit.com/products/1603/guides)
### Raspberry Pi Model B 512MB RAM

[Raspberry Pi Model B 512MB RAM](https://www.adafruit.com/product/998)
Adafruit ships the **Raspberry Pi Model B 512MB RAM** as of 10/18/2012.  
  
The Raspberry Pi® is a single-board computer developed in the UK by the Raspberry Pi Foundation with the intention of stimulating the teaching of basic computer science in schools. The Raspberry...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/998)
[Related Guides to the Product](https://learn.adafruit.com/products/998/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### BeagleBone Black Rev C - 4GB Flash - Pre-installed Debian

[BeagleBone Black Rev C - 4GB Flash - Pre-installed Debian](https://www.adafruit.com/product/1876)
Note: As of May 12, 2014 Adafruit is shipping Rev C. We have discontinued selling Rev B. There are no exchanges or "upgrades" for Rev B to Rev C.  
  
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C still has a blistering 1GHz processor and 512MB...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1876)
[Related Guides to the Product](https://learn.adafruit.com/products/1876/guides)
### BeagleBone Black Rev C - 4GB - Pre-installed Debian

[BeagleBone Black Rev C - 4GB - Pre-installed Debian](https://www.adafruit.com/product/1996)
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C has a blistering 1GHz AM3358 processor and 512MB onboard DDR3 RAM, two 46-pin headers, micro HDMI for audio/video output, USB ports, 10/100 Ethernet and other I/O features. The Rev C is an ultra-powered embedded...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1996)
[Related Guides to the Product](https://learn.adafruit.com/products/1996/guides)

## Related Guides

- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Modern Replacements for DHT11 and DHT22 Sensors](https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors.md)
- [Adding a Real Time Clock to Raspberry Pi](https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi.md)
- [Adafruit AHT20 Temperature & Humidity Sensor](https://learn.adafruit.com/adafruit-aht20.md)
- [Wood Case for Raspberry Pi 3](https://learn.adafruit.com/wood-case-for-raspberry-pi-3.md)
- [Adafruit DPI Display Kippah](https://learn.adafruit.com/adafruit-dpi-display-kippah-ttl-tft.md)
- [Adafruit's Raspberry Pi Lesson 6. Using SSH](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh.md)
- [3.5" PiTFT OctoPrint Rig](https://learn.adafruit.com/3-dot-5-pitft-octoprint-rig.md)
- [Adafruit TMP117 High Accuracy I2C Temperature Monitor](https://learn.adafruit.com/adafruit-tmp117-high-accuracy-i2c-temperature-monitor.md)
- [Instant Camera using Raspberry Pi and Thermal Printer](https://learn.adafruit.com/instant-camera-using-raspberry-pi-and-thermal-printer.md)
- [User-space SPI TFT Python Library - ILI9341](https://learn.adafruit.com/user-space-spi-tft-python-library-ili9341-2-8.md)
- [USB Audio Cards with a Raspberry Pi ](https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi.md)
- [micro:bit Lesson 4. Sensing Light](https://learn.adafruit.com/micro-bit-lesson-4-sensing-light-and-temperature.md)
- [No-Code Indoor Grow Monitor with PPFD and VPD Measurements](https://learn.adafruit.com/no-code-indoor-grow-monitor.md)
- [PyBadge Thermal Camera Case](https://learn.adafruit.com/pybadge-thermal-camera-case.md)
