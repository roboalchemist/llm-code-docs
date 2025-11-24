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

- [Firework Ignitor](https://learn.adafruit.com/electric-ignitor.md)
- [Fruit Jam Chyron](https://learn.adafruit.com/fruit-jam-chyron.md)
- [Walkmellotron: Cassette Player Mods](https://learn.adafruit.com/walkmellotron.md)
- [Build your own BeBox and run BeOS using Virtualbox](https://learn.adafruit.com/build-a-bebox-with-beos-and-virtualbox.md)
- [BLE Sniffer with nRF52840](https://learn.adafruit.com/ble-sniffer-with-nrf52840.md)
- [Commodore 64 - The Most Popular Retro Computer of All Time](https://learn.adafruit.com/commodore-64-retro-guide.md)
- [Modifying Servos for Continuous Rotation](https://learn.adafruit.com/modifying-servos-for-continuous-rotation.md)
- [Convert your Model M Keyboard to Bluetooth with Bluefruit EZ-Key HID](https://learn.adafruit.com/convert-your-model-m-keyboard-to-bluetooth-with-bluefruit-ez-key-hid.md)
- [PlayStation Spinner Controller](https://learn.adafruit.com/playstation-spinner-controller.md)
- [Pico Four Keypad](https://learn.adafruit.com/pico-four-key-macropad.md)
- [BlueLive: Livestream Studio switcher controller](https://learn.adafruit.com/bluelive.md)
- [Compiling a cross-compiler on Windows](https://learn.adafruit.com/compiling-a-cross-compiler-on-windows.md)
- [Open Source Protective Face Shield Designs](https://learn.adafruit.com/open-source-face-shield-designs.md)
- [Android Smart Home Mirror](https://learn.adafruit.com/android-smart-home-mirror.md)
- [Fog Machine with Motion Sensor and Adafruit IO](https://learn.adafruit.com/fog-machine-remote-trigger.md)
