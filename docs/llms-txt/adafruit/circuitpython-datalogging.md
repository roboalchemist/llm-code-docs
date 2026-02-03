# Source: https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-datalogging.md

# Adafruit Ultimate GPS

## CircuitPython Datalogging

# Datalogging Example

Another handy task with GPS is logging all the raw output of the GPS module to a file.&nbsp; This is useful if you're importing the GPS data into a tool like Google Earth which can process raw NMEA sentences.&nbsp; You can perform this datalogging very easily with CircuitPython.

To store data you'll need to choose one of two options:

- Wire up a SD card holder to your board's SPI bus, or use a board with SD card holder built-in like the&nbsp;[Feather M0 Adalogger](https://www.adafruit.com/product/2796).&nbsp;&nbsp; **This is the recommended approach** &nbsp;as it gives you a lot of space to store data and you can easily copy the data to your computer from the card.
- Store data in your board's internal filesystem.&nbsp; This requires a little more setup but allows you to save to a file on the internal filesystem of your CircuitPython board, right next to where code and other data files live.&nbsp; This is more limited because depending on your board you might only have a few kilobytes or megabytes of space available and GPS sentences will quickly add up (easily filling multiple megabytes within a few hours of logging).

## Install SD Card Library

If you're storing data on a SD card you must ensure the SD card is wired to your board and you have installed the Adafruit SD card library.&nbsp; Luckily there's&nbsp;[an entire guide to follow to learn about this process of connecting a SD card and installing the necessary library](../../../../micropython-hardware-sd-cards/tdicola-overview).&nbsp; Be sure to carefully follow the guide so the card is connected, library installed, and you can confirm you're able to manually write data to the card from the Python prompt.

## Enable Internal Filesystem Writes

If you're storing data on the internal filesystem you&nbsp; **must** &nbsp;carefully&nbsp;[follow the steps in the CPU temperature logging guide to enable writing to internal storage](../../../../cpu-temperature-logging-with-circuit-python/writing-to-the-filesystem).&nbsp;&nbsp; **If you're writing to a SD card skip these steps and move on to look at the datalogging code below.** &nbsp; Edit the&nbsp; **boot.py** &nbsp;on your board (creating it if it doesn't exist) and add these lines:

```python
import digitalio
import board
import storage
 
switch = digitalio.DigitalInOut(board.D5)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP
 
# If the D5 is connected to ground with a wire
# you can edit files over the USB drive again.
storage.remount("/", not switch.value)
```

Remember once you remount("/")&nbsp; **you cannot edit code over the USB drive anymore!** &nbsp; That means you can't edit&nbsp; **boot.py** &nbsp;which is a bit of a conundrum. So we configure the&nbsp; **boot.py** &nbsp;to selectively mount the internal filesystem as writable based on a switch or even just alligator clip connected to ground.&nbsp; Like the&nbsp;[CPU temperature guide shows](../../../../cpu-temperature-logging-with-circuit-python/writing-to-the-filesystem#selectively-setting-readonly-to-false-on-boot)&nbsp;. In this example we're using&nbsp; **D5** &nbsp;but select any available pin.

This code will look at the D5 digital input when the board starts up and if it's connected to ground (use an alligator clip or wire, for example, to connect from D5 to board ground) it will disable internal filesystem writes and allow you to edit code over the USB drive as normal.&nbsp; Remove the alligator clip, reset the board, and the&nbsp; **boot.py** &nbsp;will switch to mounting the internal filesystem as writable so you can log images to it again (but not write any code!).&nbsp;

Remember when you enable USB drive writes (by connecting D5 to ground at startup) you&nbsp; **cannot write files** &nbsp;to the internal filesystem and any code in your&nbsp; **main.py** &nbsp;that attempts to do so (like the example below) will fail.&nbsp; Keep this in mind as you&nbsp;edit code--once you modify&nbsp;code you need to remove the alligator clip, reset the board to re-enable&nbsp;internal filesystem writes, and then watch the output of your program.

Danger: 

## Datalogging Example Code

The GPS library examples have a&nbsp; **datalogging.py** &nbsp;file you can edit and save as a&nbsp; **code.py** &nbsp;on your board:

https://github.com/adafruit/Adafruit_CircuitPython_GPS/blob/main/examples/gps_datalogging.py

By default this example expects to log GPS NMEA sentences to a file on the internal storage system at&nbsp; **/gps.txt**.&nbsp; New sentences will be appended to the end of the file every time the example starts running.

If you'd like to instead write to the SD card take note to uncomment&nbsp;the appropriate lines mentioned in the comments:

```
# Path to the file to log GPS data.  By default this will be appended to
# which means new lines are added at the end and all old data is kept.
# Change this path to point at internal storage (like '/gps.txt') or SD
# card mounted storage ('/sd/gps.txt') as desired.
#LOG_FILE = '/gps.txt'  # Example for writing to internal path /gps.txt
LOG_FILE = '/sd/gps.txt'     # Example for writing to SD card path /sd/gps.txt
```

And further below:

Should all be uncommented and look as above.&nbsp; This will configure the code to write GPS NMEA data to the&nbsp; **/sd/gps.txt** &nbsp;file, appending new data to the end of the file.

Once the example is running as a&nbsp; **main.py** &nbsp;on your board open the serial REPL and you should see the raw NMEA sentences printed out:

![](https://cdn-learn.adafruit.com/assets/assets/000/048/212/medium800/gps_Screen_Shot_2017-11-14_at_3.40.14_PM.png?1510704360)

Check the&nbsp; **gps.txt** &nbsp;file (either under the root or /sd path depending on how you setup the example) in a text editor and you'll see the same raw NMEA sentences:

![](https://cdn-learn.adafruit.com/assets/assets/000/048/213/medium800/gps_Screen_Shot_2017-11-14_at_3.40.39_PM.png?1510704380)

Awesome!&nbsp; That's all there is to basic datalogging of NMEA sentences with a GPS module and CircuitPython!

- [Previous Page](https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-python-uart-usage.md)
- [Next Page](https://learn.adafruit.com/adafruit-ultimate-gps/built-in-logging.md)

## Featured Products

### Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates

[Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates](https://www.adafruit.com/product/746)
We carry a few different GPS modules here in the Adafruit shop, but none that satisfied our every desire - that's why we designed this little GPS breakout board. We believe this is the **Ultimate** GPS module, so we named it that. It's got everything you want and...

In Stock
[Buy Now](https://www.adafruit.com/product/746)
[Related Guides to the Product](https://learn.adafruit.com/products/746/guides)
### Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates

[Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates](https://www.adafruit.com/product/4279)
The Ultimate GPS module you know and love has a _glow-up_ to let it be easily used with any computer, not just microcontrollers! With the built-in USB-to-Serial converter, you can now plug-n-play the Ultimate GPS into your computer, laptop, embedded Linux computer, and more. Power and...

In Stock
[Buy Now](https://www.adafruit.com/product/4279)
[Related Guides to the Product](https://learn.adafruit.com/products/4279/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA

[GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA](https://www.adafruit.com/product/960)
Give your Ultimate GPS V3 a boost with this external active antenna. This GPS antenna draws about 10mA and will give you an additional 28 dB of gain. It's got a 5 meter long cable so it will easily reach wherever you need it to. The antenna is magnetic so it will stick to the top of a car...

In Stock
[Buy Now](https://www.adafruit.com/product/960)
[Related Guides to the Product](https://learn.adafruit.com/products/960/guides)
### SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable

[SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable](https://www.adafruit.com/product/851)
This RF adapter cable is super handy for anyone doing RF work. Often times, small electronics save space by having a pick-and-placeable u.FL connector (also called uFL, IPEX, IPAX, IPX, MHF, and AM). But most antennas have SMA or RP-SMA connectors on them. This little cable will bridge the...

In Stock
[Buy Now](https://www.adafruit.com/product/851)
[Related Guides to the Product](https://learn.adafruit.com/products/851/guides)
### CR1220 12mm Diameter - 3V Lithium Coin Cell Battery

[CR1220 12mm Diameter - 3V Lithium Coin Cell Battery](https://www.adafruit.com/product/380)
These are the highest quality & capacity batteries, the same as shipped with the iCufflinks,&nbsp;iNecklace, Datalogging and GPS Shields, GPS HAT, etc. One battery per order (you'll want one battery per cufflink or pendant.)  
  
Brand may vary but all battery brands are verified...

Out of Stock
[Buy Now](https://www.adafruit.com/product/380)
[Related Guides to the Product](https://learn.adafruit.com/products/380/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [Ladyada's Learn Arduino - Lesson #2](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-2.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Wireless Game Show Poppers for the Classroom!](https://learn.adafruit.com/wireless-game-show-poppers.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials.md)
- [CircuitPython Libraries on Linux and ODROID C2](https://learn.adafruit.com/circuitpython-libaries-linux-odroid-c2.md)
- [2.2" TFT Display](https://learn.adafruit.com/2-2-tft-display.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
- [Halloween Pumpkin](https://learn.adafruit.com/halloween-pumpkin.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [Automatic Monitor Color Temperature Adjustment](https://learn.adafruit.com/automatic-monitor-color-temperature-adjustment.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Skill Badge Requirements: Microcontrollers](https://learn.adafruit.com/skill-badge-requirements-microcontrollers.md)
- [RePaper eInk Development Board](https://learn.adafruit.com/repaper-eink-development-board.md)
