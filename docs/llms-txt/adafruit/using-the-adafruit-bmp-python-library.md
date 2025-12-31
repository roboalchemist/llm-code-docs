# Source: https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/using-the-adafruit-bmp-python-library.md

# Using the BMP085/180 with Raspberry Pi or Beaglebone Black

## Using the Adafruit BMP Python Library (Updated)

Danger: 

Using the BMP sensor with a Raspberry Pi or Beaglebone Black is easy with the [Adafruit Python BMP sensor library](https://github.com/adafruit/Adafruit_Python_BMP "Link: https://github.com/adafruit/Adafruit\_Python\_BMP"). First make sure your device is powered on and has access to the internet (through a wired or wireless connection). Then connect to your device in a terminal and navigate to a directory where you want to download the library (like /home/pi on a Raspberry Pi or /root on a Beaglebone Black). Finally execute the following commands to download dependencies and install the library:

```
sudo apt-get update
sudo apt-get install git build-essential python-dev python-smbus
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
```

If you already have git or python-smbus installed you can ignore the message about the package already being installed.  
  
Once the library is installed it will be accessible to any Python script on your device. You can see a few example scripts included in the library source's **examples** folder. Try running the **simpletest.py** example which grabs a single reading from the BMP sensor and displays it by executing:

```
cd examples
sudo python simpletest.py
```

If you receive an error message, carefully check that the library was installed correctly in the previous steps and try again. Note that the command needs to be run as root with sudo so that it can access the hardware's I2C bus.  
  
After running the script you should see an output such as:

> Temp = 20.20 \*C  
> Pressure = 101667.00 Pa  
> Altitude = -28.27 m  
> Sealevel Pressure = 101665.00 Pa

  
Open the **simpletest.py** code in a text editor to see how to use the library to read the BMP sensor. First the library is imported with this command:  
  
```
import Adafruit_BMP.BMP085 as BMP085
```

Next a BMP085 sensor instance is created with this command:

```
# Default constructor will pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
#
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with SCL = P9_19 and SDA = P9_20.
sensor = BMP085.BMP085()

# Optionally you can override the bus number:
#sensor = BMP085.BMP085(busnum=2)

# You can also optionally change the BMP085 mode to one of BMP085_ULTRALOWPOWER, 
# BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES.  See the BMP085
# datasheet for more details on the meanings of each mode (accuracy and power
# consumption are primarily the differences).  The default mode is STANDARD.
#sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)
```

You can see from the comments there are a few ways to create the sensor instance. By default if you pass no parameters the library will try to find the right I2C bus for your device. For a Raspberry Pi the library will detect the revision number and use the appropriate bus (0 or 1). For a Beaglebone Black there are multiple I2C buses so the library defaults to bus 1, which is exposed with pin P9\_19 as SCL clock and P9\_20 as SDA data. You can explicitly set the bus number by passing it in the busnum parameter.

**Note if you're using a BeagleBone Black with the Ubuntu operating system you might need to change busnum to 2 to use the P9\_19 & P9\_20 pin I2C connection.** &nbsp;Just change the line to look like: **sensor = BMP.BMP085(busnum=2)**  
  
The library will also choose by default to use the BMP sensor's standard operation mode. You can override this by passing a mode parameter with an explicit mode value--check the [BMP datasheet](http://www.adafruit.com/datasheets/BMP085_DataSheet_Rev.1.0_01July2008.pdf) for more information on its modes.  
  
Once the BMP sensor instance is created, you can read its values by calling the **read\_temperature** , **read\_pressure** , **read\_altitude** , and **read\_sealevel\_pressure** functions like below:

```
print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())
```

That's all you need to do to read BMP sensor values using the Adafruit Python BMP library!  
  
For another example of using the BMP library, check out the **google\_spreadsheet.py** example. This code is similar to the [DHT sensor Google Docs spreadsheet logging code](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview "Link: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview"), but is modified to use the BMP sensor and write the temperature, pressure, and altitude to a Google Docs spreadsheet. Check out the [page on configuring Google Docs](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/connecting-to-googles-docs-updated "Link: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/connecting-to-googles-docs-updated") to see more details on how to create the spreadsheet and configure the username, password, and spreadsheet name.

- [Previous Page](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/hooking-everything-up.md)
- [Next Page](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/using-the-adafruit-bmp085-python-library.md)

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
  
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C still has a blistering 1GHz processor and 512MB onboard DDR3...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1876)
[Related Guides to the Product](https://learn.adafruit.com/products/1876/guides)
### BeagleBone Black Rev C - 4GB - Pre-installed Debian

[BeagleBone Black Rev C - 4GB - Pre-installed Debian](https://www.adafruit.com/product/1996)
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C has a blistering 1GHz AM3358 processor and 512MB onboard DDR3 RAM, two 46-pin headers, micro HDMI for audio/video output, USB ports, 10/100 Ethernet and other I/O features. The Rev C is an ultra-powered embedded...

In Stock
[Buy Now](https://www.adafruit.com/product/1996)
[Related Guides to the Product](https://learn.adafruit.com/products/1996/guides)

## Related Guides

- [Raspberry Pi radio player with touchscreen](https://learn.adafruit.com/raspberry-pi-radio-player-with-touchscreen.md)
- [Adafruit PiTFT - 2.8" Touchscreen Display for Raspberry Pi](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi.md)
- [AD8495 Analog Output K-Type Thermocouple Amplifier](https://learn.adafruit.com/ad8495-thermocouple-amplifier.md)
- [Temperature and Humidity Sensing in Home Assistant with CircuitPython](https://learn.adafruit.com/temperature-and-humidity-sensing-in-home-assistant-with-circuitpython.md)
- [3D Printed Raspberry Pi A+ Case](https://learn.adafruit.com/3d-printed-raspberry-pi-a-plus-case.md)
- [RGB Matrix Portal Room CO2 Monitor](https://learn.adafruit.com/matrix-portal-room-co2-monitor.md)
- [Adafruit AMG8833 8x8 Thermal Camera Sensor](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor.md)
- [10" Raspberry Pi Desktop](https://learn.adafruit.com/10-raspberry-pi-desktop.md)
- [Networked Thermal Printer using Raspberry Pi and CUPS](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi.md)
- [Raspberry Pi NFC Minecraft Blocks](https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks.md)
- [Processing on the Raspberry Pi & PiTFT](https://learn.adafruit.com/processing-on-the-raspberry-pi-and-pitft.md)
- [Running Programs Automatically on Your Tiny Computer](https://learn.adafruit.com/running-programs-automatically-on-your-tiny-computer.md)
- [DHT Humidity Sensing on Raspberry Pi or Beaglebone Black with GDocs Logging](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.md)
- [Kali Linux on the Raspberry Pi with the PiTFT](https://learn.adafruit.com/kali-linux-on-the-raspberry-pi-with-the-pitft.md)
- [Adafruit SHT31-D Temperature & Humidity Sensor Breakout](https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout.md)
