# Source: https://learn.adafruit.com/light-painting-with-raspberry-pi/software.md

# Source: https://learn.adafruit.com/electroknit/software.md

# Electro-knit

## Software

In this section we will download and install the software that emulates a disk drive to the knitting machine.

**Python code**

Now that you have the cable running, its time to download the software. Visit the Adafruit [github](http://github.com/adafruit/knitting_machine) repository and click on **Download** to download the source code.

_This code is based on [Steve Conklin's knitting machine code](http://www.antitronics.com/wiki/index.php?title=Electroknit_Technical_Information) which is totally awesome but doesn't support pattern insertion. Still, check out his site for a lot of detailed information._

Download the file and unzip it into a directory that is easy for you to get to. For windows, we're going to stick the folder in **My Documents** in a folder called **brother** but if you are comfortable with command lines put it where-ever you'd like!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/768/medium800/braincrafts_brotherfolder.gif?1447976486)

We've had good luck running this software on Linux and Mac (OS X) systems, but it supposedly works on Windows now too, thanks to Steve's PDDEmulate.py bug fix. Try it and let us know!

You will need Python installed to run the code. To see if you have Python installed, open up a command line and type in **python**. If you're running Windows you probably don't have it, so download it from [the official Python site](http://www.python.org/download/) . You'll also need [PySerial (serial interface for python) from http://sourceforge.net/projects/pyserial/](http://sourceforge.net/projects/pyserial/)  
  
Open up a command line (windows) or Terminal (mac) or xterm (linux) and **cd** to the **brother** directory and then type in **ls** (or **dir** if **ls** doesnt work) to list all the files.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/769/medium800/braincrafts_brothercmd.gif?1447976493)

 **Determining the serial port**

Now we need to figure out what the name of the FTDI cable is. This process differs a little for Mac, Linux and Windows people.

Under Mac, in the Terminal window, type in **ls /dev/cu.\*** which should give the following responses or so.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/770/medium800/braincrafts_lscu.jpg?1396765724)

The name we are looking for is **/dev/cu.usbserial-XXXX** where the X's are going to be unique for each cable. Copy and paste the name into a text file so you'll remember it for later.

For Linux/Unix type **ls /dev/ttyUSB** \* into a terminal window, you should see a device file called something like **ttyUSB0**.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/771/medium800/braincrafts_lstty.png?1396765736)

If you are using Windows, go to the **Device Manager** (From the **Start Menu** , select **Settings→Control Panel**. Double click on **System** and select the **Hardware** tab. Then click on the **Device Manager** button).

![](https://cdn-learn.adafruit.com/assets/assets/000/000/772/medium800/braincrafts_devicemanager.jpg?1396765742)

- [Previous Page](https://learn.adafruit.com/electroknit/cable.md)
- [Next Page](https://learn.adafruit.com/electroknit/backup.md)

## Featured Products

### FTDI Serial TTL-232 USB Cable

[FTDI Serial TTL-232 USB Cable](https://www.adafruit.com/product/70)
Just about all electronics use TTL serial for debugging, bootloading, programming, serial output, etc. But it's rare for a computer to have a serial port anymore. This is a USB to TTL serial cable, with a FTDI FT232RL usb/serial chip embedded in the head. It has a 6-pin socket at the end...

In Stock
[Buy Now](https://www.adafruit.com/product/70)
[Related Guides to the Product](https://learn.adafruit.com/products/70/guides)

## Related Guides

- [Open Source Protective Face Shield Designs](https://learn.adafruit.com/open-source-face-shield-designs.md)
- [Pico Bluetooth Keyboard Bridge](https://learn.adafruit.com/pico-bluetooth-keyboard-bridge.md)
- [Dimmable Li-Ion Halogen Bike Light](https://learn.adafruit.com/dimmable-li-ion-halogen-bike-light.md)
- [Installing IronOS on an MHP30 Mini Hot Plate (DEPRECATED)](https://learn.adafruit.com/installing-ironos-on-a-mhp30-mini-hotplate.md)
- [Getting Started with Braille Output for CircuitPython REPL](https://learn.adafruit.com/getting-started-braille-output-circuitpython-repl.md)
- [Meowsic Cat Piano Line Out](https://learn.adafruit.com/meowsic-line-out.md)
- [Instagram Photo Frame](https://learn.adafruit.com/instagram-photo-frame.md)
- [ESP32 PlayStation Controller](https://learn.adafruit.com/esp32-playstation-controller.md)
- [NeoPIO: Drive lots of LEDs with Raspberry Pi Pico](https://learn.adafruit.com/neopio-drive-lots-of-leds-with-raspberry-pi-pico.md)
- [Ikea Vindriktning Hack with QT Py ESP32-S3 and Adafruit IO](https://learn.adafruit.com/ikea-vindriktning-hack-with-qt-py-esp32-s3-and-adafruit-io.md)
- [See N Say Brain Transplant](https://learn.adafruit.com/see-n-say-brain-transplant.md)
- [DIY Welded Bike Stand](https://learn.adafruit.com/diy-welded-bike-stand.md)
- [Setting up an Open Speech Recording Website](https://learn.adafruit.com/setting-up-an-open-speech-recording-website.md)
- [Authoring Playground Books with Bluefruit for iOS ](https://learn.adafruit.com/create-a-swift-playgroundbook-with-bluetooth-le.md)
- [Adafruit Feather RP2040 with USB Type A Host](https://learn.adafruit.com/adafruit-feather-rp2040-with-usb-type-a-host.md)
