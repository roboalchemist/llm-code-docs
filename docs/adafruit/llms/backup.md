# Source: https://learn.adafruit.com/electroknit/backup.md

# Electro-knit

## Backup

This step will show how to download the custom patterns from the knitting machine memory to your computer. This is just for the 'custom' patterns, it wont download the 'built in' patterns that are shown in the manual.

**Plug in the cable** into the back of the machine.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/773/medium800/braincrafts_knitport_t.jpg?1396765745)

There is a 'key' on the plug so you should be able to use it without accidentally putting it backwards. Still, check to make sure you have the right colored wires in the right places now, before plugging it in.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/774/medium800/braincrafts_cableplugged_t.jpg?1396765751)

Now back to the computer. Start up the disk drive emulator in the command line by typing in&nbsp; **python PDDemulate-1.0.py img COMPORT** &nbsp;where&nbsp; **COMPORT** &nbsp;is your serial connection. For example on a mac the command might be&nbsp; **python PDDemulate-1.0.py img /dev/tty.usbserial-A7TKMHYD** &nbsp;this will make an 'image' of the knitting memory in a directory called&nbsp; **img**.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/775/medium800/braincrafts_screen_shot_2010-11-01_at_3.57.41_pm.png?1396765762)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/776/medium800/braincrafts_screen_shot_2010-11-01_at_3.57.52_pm.png?1396765774)

Now over on your knitting machine... When "ready" lamp is lit, clear display with&nbsp; **CE** &nbsp;key, then prepare to save pattern data to "disk" by typing&nbsp; **552** , then&nbsp; **STEP**.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/777/medium800/braincrafts_01_press_ce_then_552.jpg?1396765779)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/780/medium800/braincrafts_03_display_goes_dark.jpg?1396765794)

Display will go blank and then "ready" and "pattern no" lamps will light up with the "track" number 1 in the display. Press&nbsp; **STEP**.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/781/medium800/braincrafts_02_press_step_track_1_appea.jpg?1396765787)

Machine will beep when finished, and the track data will now be in the&nbsp; **img** &nbsp;folder along with your emulator and other scripts. Ignore the .id files.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/782/medium800/braincrafts_screen_shot_2010-11-01_at_3.58.46_pm.png?1396765815)

The emulator also makes a handy&nbsp; **file-01.dat** &nbsp;file to make it easy to preview the patterns using&nbsp; **dumppattern.py** &nbsp;(see the next step)

We'll need that&nbsp; **file-01.dat** &nbsp;file, so make a backup of it somewhere else for safekeeping! That file contains all your patterns.

- [Previous Page](https://learn.adafruit.com/electroknit/software.md)
- [Next Page](https://learn.adafruit.com/electroknit/view.md)

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
