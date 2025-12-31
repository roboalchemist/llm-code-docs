# Source: https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi/making-an-sd-card-using-a-mac.md

# Adafruit's Raspberry Pi Lesson 1. Preparing an SD Card for your Raspberry Pi

## Making an SD Card – Using a Mac

We really like using balena **Etcher** for burning SD cards. Works great on Mac OS X 10.9 or later, won't over-write your backup disk drive, and can handle compressed images so you do not need to unzip them!

## Mac OS Catalina Issues

If you are having issues running Etcher on the Catalina release of Mac OS, see the links below for more information and some suggested workarounds.

- [Issue 2833](https://github.com/balena-io/etcher/issues/2833)
- [Issue 2911](https://github.com/balena-io/etcher/issues/2911)
- [Balena forum post](https://forums.balena.io/t/balena-and-mac-catalina-not-working/38073)

Most success has been reported by simply running Etcher from the command line using sudo:

```none
sudo /Applications/balenaEtcher.app/Contents/MacOS/balenaEtcher
```

# **Step 1.**

Download Etcher from&nbsp;[https://www.balena.io/etcher/](https://www.balena.io/etcher/)

[Download Etcher](https://www.balena.io/etcher/)
# **Step 2.**

Open the downloaded disk image and drag the balenaEtcher application to the Applications folder. You can then eject the disk image.

![](https://cdn-learn.adafruit.com/assets/assets/000/075/472/medium800/learn_raspberry_pi_Screen_Shot_2019-05-08_at_3.34.47_PM.png?1557351367)

# **Step 3.**

Eject any external storage devices such as USB flash drives and backup hard disks. This makes it easier to identify the SD card. Then insert the SD card into the slot on your computer or into the reader.

# **Step 4.**

Run the Etcher application.

![](https://cdn-learn.adafruit.com/assets/assets/000/075/473/medium800/learn_raspberry_pi_Screen_Shot_2019-05-08_at_3.37.47_PM.png?1557351503)

The first time you run Etcher you’ll be asked to confirm the download. Click “Open” to continue.

![](https://cdn-learn.adafruit.com/assets/assets/000/037/679/medium800/learn_raspberry_pi_3confirm.png?1480733697)

This will launch the Etcher application…

![](https://cdn-learn.adafruit.com/assets/assets/000/037/680/medium800/learn_raspberry_pi_4file1.png?1480733779)

# **Step 5.**

Select the SD card image file by clicking&nbsp; **Select Image.** &nbsp;You can choose&nbsp;a compressed SD image file such as a&nbsp; **.zip&nbsp;** or&nbsp; **.gz** or an uncompressed **.img** , it’s all good!

![](https://cdn-learn.adafruit.com/assets/assets/000/037/681/medium800/learn_raspberry_pi_4file2.png?1480733845)

# **Step 6.**

Etcher will automatically try to detect the SD drive.&nbsp;If you don’t have an SD card currently inserted, you’ll be prompted to connect one.

![](https://cdn-learn.adafruit.com/assets/assets/000/037/682/medium800/learn_raspberry_pi_5drive.png?1480734002)

Check the disk size to make sure its the right one, that it’s not overwriting your main drive or anything nasty.&nbsp;

Then click&nbsp; **Flash!** _A-ah!_

![](https://cdn-learn.adafruit.com/assets/assets/000/037/683/medium800/learn_raspberry_pi_6flash.png?1480734053)

Etcher will work for a few minutes to “burn” the SD image to the card. You’ll see&nbsp;a progress bar as it works.&nbsp;This is about the time you’ll wish you’d splurged on a high-speed card.

Once the SD card is ready, you will see the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/037/684/medium800/learn_raspberry_pi_7complete.png?1480734065)

The card will be unmounted automatically, so you can pull it out now and use it in your Raspberry Pi.

# **Faster Writes**

If you find yourself burning a lot of SD cards, you can speed things up by clicking the gear icon at the top-right, then turn off the “Validate write” option. I’ve written _hundreds_ of cards and only had _one_ fail validation.

![](https://cdn-learn.adafruit.com/assets/assets/000/037/685/medium800/learn_raspberry_pi_8settings.png?1480734077)

- [Previous Page](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi/making-an-sd-card-using-a-windows-vista-slash-7.md)
- [Next Page](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi/what-next.md)

## Featured Products

### Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM

[Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM](https://www.adafruit.com/product/3775)
The Raspberry Pi 3 Model B is the most popular Raspberry Pi computer made, and the Pi Foundation knows you can always make a good thing _better_! And what could make the Pi 3 better? How about a&nbsp;_faster_ processor, 5 GHz WiFi, and updated Ethernet chip with PoE capability?...

In Stock
[Buy Now](https://www.adafruit.com/product/3775)
[Related Guides to the Product](https://learn.adafruit.com/products/3775/guides)
### Raspberry Pi 2 Model B Starter Pack - Includes a Raspberry Pi 2

[Raspberry Pi 2 Model B Starter Pack - Includes a Raspberry Pi 2](https://www.adafruit.com/product/2380)
Why not trick out your fresh new board with some&nbsp;accessories? The Pi 2 is a big deal - a big, big deal. &nbsp;It has an upgraded ARMv7 multicore procssor and a full Gigabyte of RAM - meaning you're going to see ~2x the performance on processor-upgrade only and 4x on average for...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2380)
[Related Guides to the Product](https://learn.adafruit.com/products/2380/guides)
### Budget Pack for Raspberry Pi 1 Model B (Doesn't include RasPi)

[Budget Pack for Raspberry Pi 1 Model B (Doesn't include RasPi)](https://www.adafruit.com/product/965)
An optimized collection of parts and pieces to experiment with Raspberry Pi at home, school or work. Great for students and those that want to get their feet wet, no soldering required! **THIS PACK DOES NOT INCLUDE A RASPBERRY PI 1 MODEL B and is NOT compatible with Model B+ or Raspberry Pi...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/965)
[Related Guides to the Product](https://learn.adafruit.com/products/965/guides)
### USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC

[USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC](https://www.adafruit.com/product/939)
This is the cutest little microSD card reader/writer - but don't be fooled by its adorableness! It's wicked fast and supports up to 64 GB SDXC cards! Simply slide the card into the edge and plug it into your computer. No drivers are required, it shows up as a standard 'Mass...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/939)
[Related Guides to the Product](https://learn.adafruit.com/products/939/guides)
### SD/MicroSD Memory Card - 16GB Class 10 - Adapter Included

[SD/MicroSD Memory Card - 16GB Class 10 - Adapter Included](https://www.adafruit.com/product/2693)
Add speedy mega-storage in a jiffy using this 16 GB Class 10 micro-SD card. It comes with a SD adapter so you can use it with any of our shields or adapters! Preformatted to FAT so it works out of the box with our projects. Works great with any device in the Adafruit shop that uses micro-SD...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2693)
[Related Guides to the Product](https://learn.adafruit.com/products/2693/guides)
### SD/MicroSD Memory Card (8 GB SDHC)

[SD/MicroSD Memory Card (8 GB SDHC)](https://www.adafruit.com/product/1294)
Add mega-storage in a jiffy using this 8 GB class 4 micro-SD card. It comes with a SD adapter so you can use it with any of our shields or adapters. Preformatted to FAT so it works out of the box with our projects. Tested and works great with our <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/1294)
[Related Guides to the Product](https://learn.adafruit.com/products/1294/guides)
### Raspberry Pi 1 Model B Starter Pack - Includes a Raspberry Pi

[Raspberry Pi 1 Model B Starter Pack - Includes a Raspberry Pi](https://www.adafruit.com/product/1014)
You want to get hacking with your Pi fast, right? Get everything you need to start with the Adafruit Starter Pack for Raspberry Pi. It's the perfect accompaniment to your new Pi, everything you need to boot up your Pi Model B and get going. **We pre-assemble the Cobbler for you, no...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1014)
[Related Guides to the Product](https://learn.adafruit.com/products/1014/guides)
### Low-profile microSD card adapter for Raspberry Pi

[Low-profile microSD card adapter for Raspberry Pi](https://www.adafruit.com/product/966)
Make your Pi a little slimmer with this microSD card adapter board. It slides in where the SD card goes but is half the length. Pop in a microSD card for a sleeker machine. The microSD card holder is a push-push type so you can push on the edge that sticks out to remove the card when...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/966)
[Related Guides to the Product](https://learn.adafruit.com/products/966/guides)

## Related Guides

- [Press Your Button for Raspberry Pi](https://learn.adafruit.com/press-your-button-for-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 5. Using a Console Cable](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable.md)
- [Adafruit's Raspberry Pi Lesson 2. First Time Configuration](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration.md)
- [Raspberry Pi as an Ad Blocking Access Point](https://learn.adafruit.com/raspberry-pi-as-an-ad-blocking-access-point.md)
- [Set up and Blink - MATLAB and Simulink with Raspberry Pi](https://learn.adafruit.com/how-to-use-matlab-and-simulink-with-raspberry-pi.md)
- [Pi Video Output Using pygame](https://learn.adafruit.com/pi-video-output-using-pygame.md)
- [Drive a 16x2 LCD with the Raspberry Pi](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 4. GPIO Setup](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup.md)
- [Windows IoT Core Application Management](https://learn.adafruit.com/windows-iot-application-management.md)
- [Read-Only Raspberry Pi](https://learn.adafruit.com/read-only-raspberry-pi.md)
- [Getting Started With Windows IoT Core on Raspberry Pi](https://learn.adafruit.com/getting-started-with-windows-iot-on-raspberry-pi.md)
- [Adafruit NFC/RFID on Raspberry Pi](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi.md)
- [Windows IoT Core Application Development: Headless Blinky](https://learn.adafruit.com/windows-iot-application-development-headless-application.md)
- [USB Audio Cards with a Raspberry Pi ](https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi.md)
- [Node.js Embedded Development on the Raspberry Pi](https://learn.adafruit.com/node-embedded-development.md)
