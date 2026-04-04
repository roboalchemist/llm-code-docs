# Source: https://learn.adafruit.com/chumby-hacker-board/connecting-with-ttl-serial.md

# Chumby Hacker Board

## Connecting with TTL serial

The chumby has a four-pin, 3v level TTL serial connection port running at **115.2 Kbps**. You **cannot** just connect this to your computer's serial port, parallel port or USB port without a converter. We think the best way to connect is using an [FTDI cable](http://www.adafruit.com/index.php?main_page=product_info&cPath=33&products_id=70 "Link: http://www.adafruit.com/index.php?main\_page=product\_info&cPath=33&products\_id=70") which can be easily modified.

## Make the Cable
![](https://cdn-learn.adafruit.com/assets/assets/000/002/370/medium800/microcomputers_propcable33v.jpeg?1396782396)

You **must** use a 3.3v logic level FTDI cable, look for the letters "3V3" or similar on the cable. We also suggest checking with a multimeter that the voltage on the logic pins (everything but Red) is no higher than 3.3V. 5V logic will damage the chumby board, and it would be a shame if it broke before you got to have some fun!  
  
Also, make sure you have an adapter thats a cable, so that you can move around the pins.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/371/medium800/microcomputers_propcablestart.jpeg?1396782400)

Use tweezers to lift up the black connector tabs.![](https://cdn-learn.adafruit.com/assets/assets/000/002/372/medium800/microcomputers_propcableremovewire.jpeg?1396782407)

Then gently pull out the wires![](https://cdn-learn.adafruit.com/assets/assets/000/002/373/medium800/microcomputers_propcablepullout.jpeg?1396782412)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/374/medium800/microcomputers_propcableremoved.jpeg?1396782419)

Repeat!![](https://cdn-learn.adafruit.com/assets/assets/000/002/375/medium800/microcomputers_rawcable.jpeg?1396782427)

Rearrange the wires as shown, so you have Black (GND) then a space, Orange (TX) and Yellow (RX). You can clip the unused pins or cover them with heatshrink. They wont be used. Just make sure you don't have the conductive pins accidentally touch your Hacker Board!!!

![](https://cdn-learn.adafruit.com/assets/assets/000/002/376/medium800/microcomputers_chumbyftdi.jpeg?1396782435)

## Connect
![](https://cdn-learn.adafruit.com/assets/assets/000/002/377/medium800/microcomputers_rebootdriver.jpeg?1396782440)

Plug in your FTDI cable, and install any drivers. See our instructions for driver installation for [Windows](http://www.ladyada.net/learn/arduino/lesson0-win.html), [Mac](http://www.ladyada.net/learn/arduino/lesson0-mac.html) and [Linux](http://www.ladyada.net/learn/arduino/lesson0-lin.html).  
  
Once the driver is installed, verify the COM or tty port. For example, the COM port for our FTDI cable is COM34 (we have a lot of FTDI cables!). Open up a Serial Terminal program and connect to that COM or tty port at 115.2Kbps without hardware handshaking.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/378/medium800/microcomputers_termconnect.gif?1447864331)

Connect a 5V regulated supply into the chumby and your FTDI cable so that the black wire lines up with the&nbsp; **GND** &nbsp;labeled pin.![](https://cdn-learn.adafruit.com/assets/assets/000/002/379/medium800/microcomputers_serialconnect.jpeg?1396782462)

You should see the following on your terminal:![](https://cdn-learn.adafruit.com/assets/assets/000/002/380/medium800/microcomputers_serialboot.gif?1447864331)

Hit return a few times to get the shell!![](https://cdn-learn.adafruit.com/assets/assets/000/002/381/medium800/microcomputers_firstshell.gif?1447864332)

- [Previous Page](https://learn.adafruit.com/chumby-hacker-board/power.md)
- [Next Page](https://learn.adafruit.com/chumby-hacker-board/compiler.md)

## Featured Products

### USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply

[USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply](https://www.adafruit.com/product/961)
Add lots more USB capability to your Raspberry Pi or computer using this powered USB 2.0 hub. It adds a full **seven powered ports** , all at USB 2.0 speeds so you can use video cameras and other high speed devices (cheaper hubs are v1.1 and not as fast!)  
  
The extra sauce...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/961)
[Related Guides to the Product](https://learn.adafruit.com/products/961/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### 2.1mm to 1.7mm DC jack adapter

[2.1mm to 1.7mm DC jack adapter](https://www.adafruit.com/product/411)
We're carrying this adapter primarily to allow Chumby Hacker Board users to adapt our nice [5V @ 2A power supply](http://www.adafruit.com/products/276) to their CHB. But you can use this adapter for anything else that has a 1.7mm DC jack, such as a PSP.

In Stock
[Buy Now](https://www.adafruit.com/product/411)
[Related Guides to the Product](https://learn.adafruit.com/products/411/guides)
### USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC

[USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC](https://www.adafruit.com/product/939)
This is the cutest little microSD card reader/writer - but don't be fooled by its adorableness! It's wicked fast and supports up to 64 GB SDXC cards! Simply slide the card into the edge and plug it into your computer. No drivers are required, it shows up as a standard 'Mass...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/939)
[Related Guides to the Product](https://learn.adafruit.com/products/939/guides)
### Ethernet Cable - 10 ft long

[Ethernet Cable - 10 ft long](https://www.adafruit.com/product/730)
We have so many Internet-connected goodies in the shop, we figured it's time to carry a cable so you can easily connect them up! This cable is 10 feet long, black and has all 8 wires installed. Perfect for use with the [BeagleBone](http://www.adafruit.com/products/513), <a...></a...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/730)
[Related Guides to the Product](https://learn.adafruit.com/products/730/guides)
### USB to TTL Serial Cable - Debug / Console Cable for Raspberry Pi

[USB to TTL Serial Cable - Debug / Console Cable for Raspberry Pi](https://www.adafruit.com/product/954)
The cable is easiest way ever to connect to your microcontroller/Raspberry Pi/WiFi router serial console port. Inside the big USB plug is a USB\<-\>Serial conversion chip and at the end of the 36" cable are four wire - red power, black ground, white RX into USB port, and green TX out...

In Stock
[Buy Now](https://www.adafruit.com/product/954)
[Related Guides to the Product](https://learn.adafruit.com/products/954/guides)
### FTDI Serial TTL-232 USB Cable

[FTDI Serial TTL-232 USB Cable](https://www.adafruit.com/product/70)
Just about all electronics use TTL serial for debugging, bootloading, programming, serial output, etc. But it's rare for a computer to have a serial port anymore. This is a USB to TTL serial cable, with a FTDI FT232RL usb/serial chip embedded in the head. It has a 6-pin socket at the end...

In Stock
[Buy Now](https://www.adafruit.com/product/70)
[Related Guides to the Product](https://learn.adafruit.com/products/70/guides)

## Related Guides

- [CircuitPython Libraries on MicroPython using the Raspberry Pi Pico](https://learn.adafruit.com/circuitpython-libraries-on-micropython-using-the-raspberry-pi-pico.md)
- [Hallowing Minotaur Maze](https://learn.adafruit.com/hallowing-minotaur-maze.md)
- [Raspberry Pi Azure IoT Hub Dashboard with CircuitPython](https://learn.adafruit.com/raspberry-pi-iot-dashboard-with-azure-and-circuitpython.md)
- [Adafruit 2.9" eInk Display Breakouts and FeatherWings](https://learn.adafruit.com/adafruit-2-9-eink-display-breakouts-and-featherwings.md)
- [Pi SSD Media Server](https://learn.adafruit.com/pi-ssd-media-server.md)
- [Creating Slideshows in CircuitPython](https://learn.adafruit.com/creating-slideshows-in-circuitpython.md)
- [Network Interface Failover using FONA](https://learn.adafruit.com/network-interface-failover-using-fona.md)
- [Matrix Keypad](https://learn.adafruit.com/matrix-keypad.md)
- [Native MP3 decoding on Arduino](https://learn.adafruit.com/native-mp3-decoding-on-arduino.md)
- [Raspberry Pi HQ Camera Case](https://learn.adafruit.com/raspberry-pi-hq-camera-case.md)
- [Articulated Pi Display V2 Mount](https://learn.adafruit.com/pi-wall-mount.md)
- [World's Smallest MAME Arcade Cabinet](https://learn.adafruit.com/worlds-smallest-mame-arcade-cabinet.md)
- [Raspberry Pi E-Ink Weather Station using Python](https://learn.adafruit.com/raspberry-pi-e-ink-weather-station-using-python.md)
- [Getting Started with Raspberry Pi Pico and CircuitPython](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython.md)
- [Adafruit QT Py and NeoPixel LEDs](https://learn.adafruit.com/qt-py-and-neopixel-leds.md)
