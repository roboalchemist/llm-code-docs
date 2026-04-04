# Source: https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/configuring-the-pi-for-i2c.md

# Using the BMP085/180 with Raspberry Pi or Beaglebone Black

## Configuring the Pi for I2C

Danger: 

 **If you're using a Raspberry Pi, follow the steps below to configure it to use the I2C interface. If you're using a Beaglebone Black with its standard Debian distribution, you can skip this page and move on to the next step.**  
  
Before you can get started with I2C on the Pi, you'll need to run through a couple quick steps from the console.   
Check out this tutorial for more details and follow it completely  
  
[http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)  
  
When you're done, run  
```
sudo i2cdetect -y 0 (if you are using a version 1 Raspberry Pi)
sudo i2cdetect -y 1 (if you are using a version 2 Raspberry Pi)        
```

This will search /dev/i2c-0 or /dev/i2c-1 for all address, and if an Adafruit&nbsp;BMP085 Breakout is properly connected it should show up at 0x77 as follows:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/618/medium800/raspberry_pi_i2ctools_i2cdetect.png?1396774407)

Once both of these packages have been installed, you have everything you need to get started accessing I2C and SMBus devices in&nbsp;Python.

- [Previous Page](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/overview.md)
- [Next Page](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/hooking-everything-up.md)

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
