# Source: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.md

# DHT Humidity Sensing on Raspberry Pi or Beaglebone Black with GDocs Logging

## Overview

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/866/medium800/raspberry_pi_dht22wiring.gif?1447864319)

Time to start exploring more sensors with the Raspberry Pi and Beaglebone Black! Today we'll be checking out the [DHT11](https://www.adafruit.com/products/386), [DHT22](https://www.adafruit.com/products/385) and [AM2302](https://www.adafruit.com/products/393 "Link: https://www.adafruit.com/products/393") humidity and temperature sensors available from Adafruit  
  
In this tutorial we'll be showing how to install a DHT sensor Python library which utilizes C for high-speed GPIO polling to handle bit-banged sensor output. Many low cost sensors have unusual output formats, and in this case, a "Manchester-esque" output that is not SPI, I2C or 1-Wire compatible must be polled continuously by the Pi to decode. Luckily, the C GPIO libraries are fast enough to decode the output.   
  
Once we have that working, we add the fun of Python to update a google spreadsheet live with the temperature/humidity data. This project would be the great basis for home or garden automation!  
  
 [You can check out our spreadsheet here, it wont be updated live after Aug 24 2012 but it will show you the format of data you get](https://docs.google.com/spreadsheet/ccc?key=0AlwXpwqqd84DdFVobHFCWXZLU2l2V212WnFrS3QwdkE#gid=0 "Link: https://docs.google.com/spreadsheet/ccc?key=0AlwXpwqqd84DdFVobHFCWXZLU2l2V212WnFrS3QwdkE#gid=0")

http://youtu.be/Skr2uPZzviM

- [Next Page](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/wiring.md)

## Featured Products

### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### BeagleBone Black Rev C - 4GB Flash - Pre-installed Debian

[BeagleBone Black Rev C - 4GB Flash - Pre-installed Debian](https://www.adafruit.com/product/1876)
Note: As of May 12, 2014 Adafruit is shipping Rev C. We have discontinued selling Rev B. There are no exchanges or "upgrades" for Rev B to Rev C.  
  
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C still has a blistering 1GHz processor and 512MB onboard DDR3...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1876)
[Related Guides to the Product](https://learn.adafruit.com/products/1876/guides)
### BeagleBone Black - Rev B

[BeagleBone Black - Rev B](https://www.adafruit.com/product/1278)
**[Adafruit is no longer shipping the BeagleBone Black Rev B, it has been replaced with the Rev C as of 5/12/14](https://www.adafruit.com/products/1876) - the Rev C now has 4G flash and also comes with Debian, it also costs slightly more. There are no exchanges or...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1278)
[Related Guides to the Product](https://learn.adafruit.com/products/1278/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### AM2302 (wired DHT22)  temperature-humidity sensor

[AM2302 (wired DHT22)  temperature-humidity sensor](https://www.adafruit.com/product/393)
Discontinued - [**you can grab** AM2301B - Wired Enclosed AHT20 - Temperature and Humidity Sensor&nbsp; **instead!**](https://www.adafruit.com/product/5181)

The AM2302 is a wired version of the [DHT22](http://www.adafruit.com/products/385), in a large plastic...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/393)
[Related Guides to the Product](https://learn.adafruit.com/products/393/guides)
### DHT11 basic temperature-humidity sensor + extras

[DHT11 basic temperature-humidity sensor + extras](https://www.adafruit.com/product/386)
 **Discontinued -**  **you can grab the&nbsp;** [DHT20 - AHT20 Pin Module - I2C Temperature and Humidity Sensor](https://www.adafruit.com/product/5183)&nbsp; **instead!&nbsp;**

The DHT11 is a basic, ultra low-cost digital temperature and humidity sensor. It uses...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/386)
[Related Guides to the Product](https://learn.adafruit.com/products/386/guides)
### DHT22  temperature-humidity sensor + extras

[DHT22  temperature-humidity sensor + extras](https://www.adafruit.com/product/385)
The DHT22 is a basic, low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air and spits out a digital signal on the data pin (no analog input pins needed). It's fairly simple to use but requires careful timing...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/385)
[Related Guides to the Product](https://learn.adafruit.com/products/385/guides)
### BeagleBone Black Rev C - 4GB - Pre-installed Debian

[BeagleBone Black Rev C - 4GB - Pre-installed Debian](https://www.adafruit.com/product/1996)
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C has a blistering 1GHz AM3358 processor and 512MB onboard DDR3 RAM, two 46-pin headers, micro HDMI for audio/video output, USB ports, 10/100 Ethernet and other I/O features. The Rev C is an ultra-powered embedded...

In Stock
[Buy Now](https://www.adafruit.com/product/1996)
[Related Guides to the Product](https://learn.adafruit.com/products/1996/guides)

## Related Guides

- [Freq Show: Raspberry Pi RTL-SDR Scanner](https://learn.adafruit.com/freq-show-raspberry-pi-rtl-sdr-scanner.md)
- [Adding a Real Time Clock to Raspberry Pi](https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi.md)
- [LED Backpack Displays on Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/led-backpack-displays-on-raspberry-pi-and-beaglebone-black.md)
- [Raspberry Pi SelfieBlock](https://learn.adafruit.com/selfieblock.md)
- [How Cold Is It?](https://learn.adafruit.com/how-cold-is-it.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Introducing the Raspberry Pi 2 - Model B](https://learn.adafruit.com/introducing-the-raspberry-pi-2-model-b.md)
- [Send Raspberry Pi Data to COSM](https://learn.adafruit.com/send-raspberry-pi-data-to-cosm.md)
- [Adafruit HTS221 - Temperature & Humidity Sensor](https://learn.adafruit.com/adafruit-hts221-temperature-humidity-sensor.md)
- [Using Piezo Buzzers with WipperSnapper](https://learn.adafruit.com/using-piezo-buzzers-with-wippersnapper.md)
- [Using Melexis MLX90614 Non-Contact Sensors](https://learn.adafruit.com/using-melexis-mlx90614-non-contact-sensors.md)
- [reef-pi Guide 2: Power Controller](https://learn.adafruit.com/reef-pi-power-controller.md)
- [Adafruit Pi Box Plus](https://learn.adafruit.com/adafruit-pi-box-plus.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Adafruit Si7021 Temperature + Humidity Sensor](https://learn.adafruit.com/adafruit-si7021-temperature-plus-humidity-sensor.md)
