# Source: https://learn.adafruit.com/electroknit/insert.md

# Electro-knit

## Insert New Patterns

Now we get to the fun part, showing how you can make an image on your computer and then inserting it into the memory file so that we can easily make new patterns without the tedious entering-by-hand part.  

The first thing we'll need to do is make the image. The image&nbsp; **must** &nbsp;be 1-bit/2-color/monochrome/black&white. You need to make sure that whatever image software can save the file in monochrome. A free program on every windows computer that can do this is **MS&nbsp;Paint** &nbsp;- its crummy but it does this stuff kinda well.

A nice thing you can do is zoom in and click pixels. Remember that stitches in knitting are not square, so you may want to squish your graphic horizontally just a bit before lowering its resolution.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/785/medium800/braincrafts_paintzoom.gif?1447976516)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/786/medium800/braincrafts_adazoomed_%281%29.gif?1447976524)

Again, make sure that its saved as a monochrome 1-bit Bitmap (BMP) file.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/787/medium800/braincrafts_monochromsave.gif?1447976533)

Next you'll need to figure out the pixel dimensions (width and height). You can count the pixels or, at least under windows and some paint programs, they'll report the image size for you.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/788/medium800/braincrafts_properties.gif?1447976541)

Write down or otherwise keep track of the pixel dimensions for the next step.

## Creating a container pattern

Our software can't add new patterns to the memory file (we don't understand enough of the format to do so) but it&nbsp; **can** &nbsp;edit existing patterns. So what we'll do is make a blank 'container' pattern on the knitting machine. Then we'll edit the pattern on the computer and re-upload the file.

In this step, you're going to create the blank "container" pattern of the appropriate dimensions using the knitting machine control panel. This pattern is going to be 32x32 and will have pattern ID #901.

Press INPUT

![](https://cdn-learn.adafruit.com/assets/assets/000/000/789/medium800/braincrafts_01_press_input.jpg?1396765884)

Note the pattern number that appears. User-input patterns get assigned a number in ascending order starting at 901.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/790/medium800/braincrafts_02_note_pattern_number.jpg?1396765893)

Press STEP

![](https://cdn-learn.adafruit.com/assets/assets/000/000/791/medium800/braincrafts_03_press_step.jpg?1396765904)

Enter your pattern's width (number of stitches), then press STEP

![](https://cdn-learn.adafruit.com/assets/assets/000/000/792/medium800/braincrafts_04_enter_number_of_stitches.jpg?1396765912)

The number of available rows in the machine's memory will appear on the display. Press CE to clear the display.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/793/medium800/braincrafts_04_remaining_available_rows_display.jpg?1396765923)

Enter the pattern's height (number of rows) and press STEP.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/794/medium800/braincrafts_05_enter_number_of_rows.jpg?1396765930)

Press INPUT once more to exit input mode.

Repeat for as many patterns as you'd like to create (and for which you have space).

## **Inserting the pattern**

Follow the&nbsp;[backup tutorial](http://learn.adafruit.com/electroknit/backup)&nbsp;to transfer the knitting machine memory to your computer

Now you'll run&nbsp; **insertpattern.py** &nbsp;by typing in&nbsp; **python insertpattern.py img/file-01.dat PATTERNNUM BMPFILE myfile.dat** &nbsp;which will insert the&nbsp; **BMPFILE** &nbsp;You made in part 1 into the pattern # location&nbsp; **PATTERNNUM** &nbsp;and when done, save the new data file to **myfile.dat** &nbsp;(so you dont overwrite the old file).

![](https://cdn-learn.adafruit.com/assets/assets/000/000/795/medium800/braincrafts_insertingqr.gif?1447976549)

If the pattern size doesn't match the image size it won't continue.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/796/medium800/braincrafts_wrongsize.gif?1447976556)

## **Split the file**
Now that we have the&nbsp; **myfile.dat** , we'll need to split the file into tracks. This lets the emulator load the files back like it was a diskette. We've included a simple program to do this, its called&nbsp; **splitfile2trakc.py** &nbsp;and you can run it by typing in&nbsp; **splitfile2track.py myfile.dat** &nbsp;it will create two files,&nbsp; **track0.dat** &nbsp;and&nbsp; **track1.dat**.![](https://cdn-learn.adafruit.com/assets/assets/000/000/797/medium800/braincrafts_screen_shot_2010-10-26_at_9.55.27_pm.png?1396765968)

Rename the files 00.dat and 01.dat respectively.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/798/medium800/braincrafts_screen_shot_2010-10-26_at_9.55.40_pm.png?1396765985)

And drag them into your&nbsp; **img** &nbsp;folder.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/799/medium800/braincrafts_screen_shot_2010-10-26_at_9.56.07_pm.png?1396766004)

If you're looking for a simple way to accomplish all that file-wrangling, check out Davi Post's img2track software that combines many of the above steps into one handy program.

Lastly, we'll reupload the files to the knitting machine, see the next section!

- [Previous Page](https://learn.adafruit.com/electroknit/view.md)
- [Next Page](https://learn.adafruit.com/electroknit/upload.md)

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
