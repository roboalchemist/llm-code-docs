# Source: https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images

## Introduction

This tutorial is designed to give you a basic understanding of SD Cards and how to write different images to the SD card of your choice.

SD cards, short for [Secure Digital](http://en.wikipedia.org/wiki/Secure_Digital), are everywhere you look now, from digital cameras, to phones and tablets, and even Single Board Computers (SBCs). In many cases your SBC won\'t come with Linux or any other operating system on it. It is up to you to provide the OS on an SD card. With the exception of Noobs for Raspberry Pi, this is usually not a drag and drop procedure.

In this tutorial, we are going to talk about different types of SD cards and readers, formatting your card to erase any data that may be lurking around, installing your image, and then how to use any left over space on the card.

[![MicroSD Card and Adapter](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/Sd_Card.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/Sd_Card.jpg)

*Single Board Computers, such as the Raspberry Pi, use SD and microSD cards to house various operating systems. Pictured here: a microSD card with full-size adapter.*

### Required Materials

To follow along with this tutorial, you will need an [SD card](https://www.sparkfun.com/categories/351), and a [card reader](https://www.sparkfun.com/search/results?term=microsd+reader+adapter) (see related sections for more information on different types). The minimum card size depends on the Linux distribution. Make sure to check the image distribution that you are planning on using for your Single Board Computer before flashing. You will also need a computer and an Internet connection (if you don\'t have all the software and your image already on your computer). Last, you\'ll want your SBC or whatever device into which you are installing your card.

- [microSD Card](https://www.sparkfun.com/categories/351) w/ Minimum Card Size
- [microSD Card Reader](https://www.sparkfun.com/products/13004)
- Linux Image
- Single Board Computer (i.e. Raspberry Pi, NVIDIA Jetson Nano, etc.)
- Internet Connection

### Recommended Reading

There is no one best place to start when it comes to single board computers. However, you may find these links useful in your SBC adventure.

- [Getting started with the Command Line](https://p1k3.com/userland-book/)
- [Setting up a Raspberry Pi with Raspbian using Noobs](https://learn.sparkfun.com/tutorials/setting-up-raspbian-and-doom)

## SD Cards

SD Cards can be found most everywhere, online, at your local store. But whats sets one apart from the rest? What makes a good SD card? Besides manufacture, the main differences between cards are physical size, capacity/standards, and speed. Here is a brief overview of each of those elements.

#### Size

SD cards come in two main sizes. Full sized SD cards are used in digital cameras all over the globe, and microSD (often called µSD or uSD) cards are used in cellphones and tablets, amongst others. Electrically they are the same thing, though. Ever notice the cheap plastic adapters that come with some microSD cards? They are nothing more than a plastic shell with connectors to pass through the microSD connectors to the full size connectors. Installing images on them is the same, just make sure you have the right card (and adapter, if needed) for your device and reader.

#### Standards

There are actually 4 different standards of SD card, with each new version came higher capacity and often higher speeds. The 4 versions are: Standard or SD (up to 4GB), High Capacity or SDHC (up to 32GB and formatted as FAT32), Extended High Capacity or SDXC (up to 2TB and formatted as exFAT), and SDIO (has support for I/O). Any of these should work but be careful with SDXC cards; because of licensing issues, not all devices can support exFAT.

#### Speed

Most cards will also list a class or speed on them to distinguish how fast they can read and write. Class 2,4,6,8 and 10 are 2MB/s, 4MB/s, 6MB/s, 8MB/s, and 10MB/s, respectively. UHS Class 1 and UHS Class 3 are 10MB/s and 30MB/s, respectively. For the most part, these numbers are irrelevant; just keep in mind that there are different speeds so if things are running slower than you\'d like, check the card.

For this tutorial, any of these cards will work with. However, make sure you have the correct physical size for your device, and the the card has a high enough capacity to hold the image you want to use. This [8GB card](https://www.sparkfun.com/products/11609) should work for just about everything since it has an SD adapter as well as a card reader.

[![SD cards, uSD cards, uSD adapters, and Wifi enabled SD card](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/6/SD_Card_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/SD_Card_Tutorial-01.jpg)

*SD cards, uSD cards, uSD adapters, and Wifi enabled SD card*

## Card Readers

You can find almost as many SD card readers as SD cards but there really aren\'t that many differences. Your local computer store, or even conveinence store will most likely have at least one USB adapters. If your computer doesn\'t have one there are plenty of choices available for adapters, for the most part these will connect to your computer over USB. Some will do just uSD, uSD and SD or, a whole bunch of different card types. Any of these should work fine for our examples.

[![A few different SD and uSD card readers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/6/SD_Card_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/SD_Card_Tutorial-02.jpg)

*A few different SD and uSD card readers*

Most laptops and even some desktops now have direct slots in them to read and write SD cards. Often these are directly connected to the USB port inside your machine, making them the same as the USB adapters, but not always. These should work just fine for our examples, but if you are having problems try a USB adapter.

[![SD card Slot or USB as Options](https://cdn.sparkfun.com/r/600-600//assets/parts/7/6/3/6/11609-Action.jpg)](https://cdn.sparkfun.com//assets/parts/7/6/3/6/11609-Action.jpg)

Most cameras now use SD cards and can be plugged into your computer via a USB cable. For the most part the data is going through the camera and not being read directly from the computer. For that reason this will not work for our examples, this is true for phones and other devices as well. Basically if your device has a name other than \"SD adapter\" it probably won\'t work.

For this tutorial, you will need either an SD slot in your computer or a USB adapter. Make sure it fits the size card you have or you have the appropriate adapter. Otherwise, grab the microSD USB reader from the [SparkFun catalog](https://www.sparkfun.com/categories/351).

[![microSD USB Reader](https://cdn.sparkfun.com/r/600-600/assets/parts/9/9/5/8/13004-01.jpg)](https://www.sparkfun.com/microsd-usb-reader.html)

### [microSD USB Reader](https://www.sparkfun.com/microsd-usb-reader.html) 

[ COM-13004 ]

This is an awesome little microSD USB reader. Just slide your microSD card into the inside of the USB connector, then stick t...

**Retired**

## Formatting Your Card

We are going to start with formatting your SD card. This step is not strictly necessary, but it does help clean off your card. In some cases if something has gone wrong this will help clean up the mess instead of bring the mess with you.

Always be careful when doing this, it will erase everything on your card, so make sure you are OK losing everything on the card. Also, make sure you select the correct drive! Alternately the tools used to change partition size will also format any card or partition. If your card has been partitioned because it already has an image on it, see the last section on [resizing and deleting partitions](#partitions).

### Windows

The SD Association has a formatter that is designed to work with both Windows and Mac that they recommend, you can try it or use the following directions - [SD Card Formatter](https://www.sdcard.org/downloads/formatter_4/)

[Download SD Memory Card Formatter](https://www.sdcard.org/downloads/formatter_4/)

- Open \"My Computer\"
- Right click on the drive with the SD card
- Select \"Format\"

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/WindowsFormat1_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/WindowsFormat1_1.jpg)

- Select your file system (FAT32 works fine)
- Feel free to name your card in \"Volume Label\"
- Quick Format is not quite as thorough but a bit quicker, either option is fine
- Select \"Start\"

[![microSD card formatter on Windows](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/WindowsFormat2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/WindowsFormat2.jpg)

### Mac

The SD Association has a formatter that is designed to work with both Windows and Mac that they recommend, you can try it or use the following directions - [SD Card Formatter](https://www.sdcard.org/downloads/formatter_4/).

[Download SD Memory Card Formatter](https://www.sdcard.org/downloads/formatter_4/)

- Open the Disk Utility (Applications -\> Utilities -\>Disk Utility)
- Select the SD Card
- Select the \"Erase\" tab
- Select your file system - MSDOS(FAT)
- Feel free to name your card in the \"Name\" field
- Select \"Erase\"

[![microSD card formatter on Mac](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/6/MacFormat1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/MacFormat1.png)

### Linux

- Run Gparted (you may need to install it first using `sudo apt-get install gparted`)
- Select the correct device from the drop down menu on the top right
- Select Partition → Format to → fat32
- Click Apply

[![Gparted memory card formatter on linux](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/6/LinuxFormat1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/LinuxFormat1.jpg)

## Downloading and Installing the Image

Finally, this is what we\'ve been waiting for. So, why can\'t you just copy the file onto the card? When you look at the SD card you actually don\'t see all the bits on the card, you just see the main storage area. There are other parts that allow the card the card to be bootable, and this is what needs to be written. While you can do that by hand and then add all the files you need, generally your files are released as an image that has all the information in it. This way you can make the disk bootable and add the files all in one easy step. Just like formatting your SD card, this will erase everything on it. Make sure you want to do this and you select the correct disk.

### Downloading the image

Start by downloading the image you want to use, and don\'t forget to extract your image so you have a **\*.img** file. Here are some files for a few common boards; notice there are often different downloads available. You will find different Linux distributions, Android images, and even different images depending on the display you want to use. Pick the one that best works for your application, and remember, you can always go back and pick a different one.

- Raspberry Pi (Noobs install is done differently follow the directions on the Raspberry page) - [Downloads](https://www.raspberrypi.org/downloads/)
- NVIDIA Jetson Nano [Downloads](https://developer.nvidia.com/embedded/downloads)
- PCDuino 3 - [Downloads](http://www.linksprite.com/?page_id=855)
- Acadia - [Downloads](http://www.linksprite.com/?page_id=1112)

### The Easy Way

To install your own image on your card we recommend software called [Etcher](https://etcher.io/).

[Download Balena Etcher](https://etcher.io/)

These guys have taken all the different steps needed and put them all in one piece of software to take care of everything. Download your image, then run the program, select your image, select your uSD card drive, and then hit flash. Etcher will flash the card, verify the install and unmount your card. Once it is done, remove your card and you are good to go.

[![Etcher Install](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/EtcherInstall.gif)](https://etcher.io/)

*GIF Courtesy of [Etcher.io](https://etcher.io/)*

### The Hard Way - Windows

- Download and unzip [Win32DiskImager](http://sourceforge.net/projects/win32diskimager/)
- Run Win32DiskImager.exe (you may need to run as Adminstrator)
- Select the drive of your SD card
- Click the folder icon and select the image you downloaded
- Click \"Write\" and wait until it is done

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/WindowsWrite1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/WindowsWrite1.jpg)

### The Hard Way - Mac

- Run `diskutil list` to display all disks, find the correct disk
- Run `diskutil unmountDisk /dev/disk4` to unmount the disk (replace disk4 with the correct disk)
- Run `sudo dd bs=1M if=your/file/here.img of=/dev/disk4` (again replace disk4 with the correct disk, and add the correct path to your image)
- Wait until it is done

[![Win32 Disk Imager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/6/MacWrite1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/MacWrite1.png)

### The Hard Way - Linux

- Run `df-h` to see what devies are mounted on your system, you may want to do this without the card in and then with the card in.
- Take a look at the card name on the left column. There will most likely be a number at the end, this in the partition number. In the example below my card /dev/sdd has 1 partition (/dev/sdd5). You may also have more than 1 partition on your card, keep that in mind if you do.
- Unmount any partitions you see using the command `umount /dev/sdd5` where /dev/sdd5 is the partition on your card.
- Next run the following command to actually write to the card, keep in mind you will need to know where your image is and you will want to use the path to the card without any partition numbers on the end. You may or may not need to run this as \"sudo\" depending on your permissions `dd if=2015-05-05-raspbian-wheezy.img of=/dev/sdd` (make sure to use the correct path to your file and your SD card)
- Wait\... this will take a few minutes, there is no status bar, but even on a live Linux distro this only took a couple of minutes.
- Run `sync` (this will flush the write cache, and other fancy things)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/6/LinuxWrite1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/LinuxWrite1.jpg)

## Resizing the partition

[] At this point you should have a working bootable SD card, feel free to stop here. Sometimes though you go grab that 16GB card you have lying around, burn a 1GB image and then think, well that\'s silly, I\'ve lost 15GB of space! Now we are going to change partition sizes around so that the remainder of your card shows up as a separate partition that you can still use for storage. Before we start you may want to boot your card and take a look around, many distrobutions have a built in utility to do this. You can also use these programs to resize the partition if you\'d rather.

Keep in mind that Windows can only read the first partition, so you will not be able to use this as general storage if you use a Windows device. But you can use it as storage on your Linux based Single Board Computer (SBC).

This is also a good way to get your SD card back to the original full sized partition if you no longer want to use it on your SBC. You wil need to delete all partitions, then make a new one and format it.

Most of these programs actually have very similar layout and directions, and there will be [plenty of other options](http://alternativeto.net/software/gparted/) available online as well.

### All Windows

- Newer versions of Windows have a partition manager built in (see below), but for older versions of Windows or a more full featured partion manager try [EaseUS Partition Manager](http://www.easeus.com/partition-manager/)
- Download [EaseUS Partition Manager](http://www.partition-tool.com/download.htm)
- Unzip, and run the program
- Select the Disk in the upper part of the window
- You should see a graphical representation of the partitions in the bottom half
- Depending on the image you installed, you may have various options. Any unallocated space can be turned into a new partition and formatted. You can also take the last partition and resize it so it takes up the rest of the card.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/6/WindowsPartition1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/WindowsPartition1.jpg)

- Make sure you apply your changes (check mark in the toolbar on top). This applies all changes you make to the card.

### Windows Vista,7,8

- Open Control Panel
- Type Partition into the search box
- Select the option \"Create and format hard disk partitions\"
- Select the Disk in the upper part of the window
- You should see a graphical representation of the partitions in the bottom half
- Depending on the image you installed, you may have various options. Any unallocated space can be turned into a new partition and formatted. You can also take the last partition and resize it so it takes up the rest of the card.
- Make sure you apply your changes (check mark in the toolbar on top), this applies all changes you make to the card

### Mac

- Depending on whether your image uses a Windows based file system or not, this may or may not work. If you are having problems try these [alternatives](http://alternativeto.net/software/gparted/?platform=mac).
- Open the Disk Utility (Applications -\> Utilities)
- Select the SD Card
- Select the \"Partition\" tab
- Click the \"+\" in the bottom left corner to add a partition
- Select the partition and drag the bottom right corner to resizse
- Click Apply

### Linux

- Run Gparted (you may need to install it first using `sudo apt-get install gparted`)
- Select the correct device from the drop down menu on the top right
- Depending on the image you installed you may have various options. Any unallocated space can be turned into a new partition and formatted. You can also take the past partition and resize it so it takes up the rest of the card.
- Make sure you apply your changes. This applies all changes you make to the card.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/LinuxPartition1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/LinuxPartition1.jpg)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/LinuxPartition2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/6/LinuxPartition2.jpg)