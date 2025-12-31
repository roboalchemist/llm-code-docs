# Source: https://learn.adafruit.com/chumby-hacker-board/sd-card.md

# Chumby Hacker Board

## SD Card

The easiest way to do things for now is to use a linux machine or a bootable linux CD/DVD, or even a virtual machine running under Windows. Macintosh has most of these commands available too in a root window. Some things can be done on the Chumby hackerboard itself since dd (and fdisk) might be available.  
  

## Cloning/Copying
The original image is available from a link off the forum:  
  
[http://forum.chumby.com/viewtopic.php?pid=31177#p31177](http://forum.chumby.com/viewtopic.php?pid=31177#p31177)  
  
An earlier message references windiskimager:  
  
[https://launchpad.net/win32-image-writer/+download](https://launchpad.net/win32-image-writer/+download)  
  
The image in the .zip file has the partition table overlap problem, but it should be the original boot image.  
  
You can clone the 1G original microSD card if you have made modifications or otherwise don't want to use the image file. It can be written to any same or larger card. The standard way is to use "dd". Google "dd windows" for a version that works there, but basically you need to do a byte-for-byte image copy from the original device to the new one. You probably also want to make a backup of the card as well.  
  
Cloning can be done on the hackerboard itself if you have a USB to microSD adapter. This will be something like:  
```
dd if=/dev/mmcblk0 of=/dev/sda bs=64M
```

Since the board uses mmcblk0 for internal flash.  
  
NOTE: DD IS DANGEROUS SINCE IT ACCESSES THE HARDWARE DIRECTLY - YOU CAN END UP OVERWRITING YOUR WINDOWS DRIVE IF YOU AREN'T CAREFUL. Make sure everything is backed up or you know exactly what you are doing.  
```
dd if=/dev/sdX of=/dev/sdY bs=64M
```

Windows will have something different for the /dev entries. /dev/sdX is the original card. Under linux, if you do "cat /proc/partitions" you will find a list - /dev/sda is typically your system drive. You can do this before inserting the original card, then look what appears after about 10 seconds - the new partitions will be from the new drive, which should be the chumby hacker image. You can also do it directly on the Chumby - in this case the values should be if=/dev/mmcblk0, and of=/dev/sda but I would still check /proc/partitions to see what was there.  
  
If you can access your main hard drive, I would first back things up (if you have 1G of free space) by using dd, "dd if=/dev/sdX of=/media/c-drive/chb.img bs=64M". /media/cdrive is wherever the hard drive shows up under linux, or something like "C:\chb.img" under windows. This will create an image file of the uSD so it can be restored if anything goes wrong. The "bs=64M" copies 64 megabyte chunks which will be a lot faster as it normally copies bytes. Then you can remove the chumby SD and insert the clone target and just reverse "if" and "of": "dd if=/media/c-drive/chb.img of=/dev/sdX bs=64M". Then test the clone.  
  
You can also do so with the rom image:  
```
dd if=rom-falconwing.img of=/dev/sdX bs=64M
```

## Fixing the partition table
Before you can change the partition sizes you need to fix the partition table.  
  
The limited fdisk on the Chumby hacker board can't be used for this - you will need to boot into linux.  
  
(note, it is probably easier to patch a few bytes with a hex editor, especially the original - I need to compare the original with the fixed MBR table and document the changed bytes in the first partition entry).  
  
Reinsert the clone after the copy (remove and reinsert to get the updated disk structure). Run "fdisk /dev/sdX". This is a basic partition editor. It will complain because the structure is broken. Type "p" to print. You will see the first partition overlaps the next two. do "d" then "1" to delete the partition from the table (it isn't reformatted or anything), then "n", "p", it will default to partiton 1, then use the defaults for first and last. Do "t" then "1" then "53(return)" to reset the type, type "p" to see the changes (no overlaps!), then "w" to write it to the disk.  
## Resizing the partitions
I use gparted, available on some bootable fixit CDs or almost every bootable linux CD or USB stick.  
  
Partition 4 is the extended container, and within, partition 6 is the "storage" partion". You will first need to move and/or resize partition 4 to make partition 6 larger. I would suggest also moving it on larger cards so you can make the other (root) partitions larger too.  
  
Run gparted from the menu or "sudo gparted /dev/sdX" from the command line. Click on partition 4 and do move/resize, and slide it to give free space before if you want to expand the other partitions, but make sure it ends at the end of the disk. Then select the storage partition within and stretch it to the end of the new space. Tell it to apply changes.  
  
I have a 16Gb image with plenty of room for everything.  
  
(Note from BBotany on a different route to expanding the filesystem.) If you are working on a system that does not contain gparted, it is possible to use cfdisk to expand the final partition. Simply select the partition, and apply the "maximize" option. This will also extend the extended partition container (aka "partition 4") automatically. However, you will need to resize the filesystem that is on the partition separately; it is easy to use "resize2fs" to do this. If this is not on the machine you changed partition sizes on (or you forgot to expand the filesytem before reinserting the SD card in the hackerboard), it is present on the hackerboard by default. After the partition table has been modified, simply run resize2fs on the partition. If you are on your own linux host, you presumably know where this is. If you are on the hackerboard itself, then the commands are as follows: unmount the partition with "umount /mnt/storage/", run the resize as: "resize2fs /dev/mmcblk0p6", and then remount it with "mount /mnt/storage/". When I upgraded to an 8GB SD card, this gave me a /mnt/storage of 6.4GB.  
- [Previous Page](https://learn.adafruit.com/chumby-hacker-board/audio.md)

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
