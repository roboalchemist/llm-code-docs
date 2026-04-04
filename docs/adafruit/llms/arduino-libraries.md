# Source: https://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries.md

# Arduino Tips, Tricks, and Techniques

## Arduino Libraries

# Need Help Installing a Library?
Check out our super-detailed tutorial for all operating systems here:   
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")  
  
## What is a library?
Libraries are great places, and not yet illegal in the United States! If you ever need to learn how to do something, like say fix a motorcycle, you can go to your local library and take out a book. Sure you could buy the book but the library is nice because as a resource you can get the book whenever you need it, keeping your house uncluttered.  
  
Software Libraries are very similar. We already studied what a procedure is, in [lesson 3](http://www.ladyada.net/learn/arduino/lesson3.html): a procedure is a list of things to do. A library is a big collection of procedures, where all the procedures are related! If you, say, want to control a motor, you may want to find a Motor Control Library: a collection of procedures that have already been written for you that you can use without having to do the dirty work of learning the nuances of motors.  
  
For example, this is the Serial Library, which allows the Arduino to send data back to the computer:  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/304/medium800/learn_arduino_serial_library.gif?1448059518)

## Using Libraries
One of the best features of the Arduino project is the ability to add on pre-crafted libraries that add hardware support. There's tons of them, and you can pick and choose which to install. They're only loaded in when the sketch you're working on needs them, so for the most part you can download and stash them for future use.  
  
Sketches will often **depend** on libraries, you can see what they are by looking at the top of the sketch. If you see something like:  
```
#include &lt;FatReader.h&gt;
```

That means that you'll need a library called FatReader or a library that contains the file FatReader. If you dont have it installed you'll get an error:![](https://cdn-learn.adafruit.com/assets/assets/000/003/305/medium800/learn_arduino_fatreadernoliberror.gif?1448059512)

## What's in a library?
A library is a folder with some files in it, the files will end in&nbsp; **.cpp** &nbsp;(C++ code file) and&nbsp; **.h** &nbsp;(C++ header file).  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/306/medium800/learn_arduino_nsslibrary.gif?1448059507)

There may also be some **.o** files. The **.o** files are C++ compiled Objects. If you end up working on the library and modifying it, be sure to delete the **.o** files as that will force the Arduino IDE to recompile the modified **.cpp**'s into fresh **.o**'s.  
  
Two optional files you may see are **keywords.txt** (this is a hints file to tell the Arduino IDE how to colorize your sketch and **examples** folder, which may have some handy test-sketches. These will show up under the File→Examples→Library dropdown.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/307/medium800/learn_arduino_examplelibdropdown.gif?1448059501)

## It's important to remember!
The structure of the library folder is very important! The **.c** and **.h** files must be in the 'lowest level' of folders. For example, you cant have **Arduino/libraries/WaveHC/WaveHC/file.c** or **Arduino/libraries/MyLibraries/WaveHC/file.c** - it must be **Arduino/libraries/WaveHC/file.c**  
## How to install libraries
In Arduino v16 and earlier, libraries were stored in the **ArduinoInstallDirectory/hardware/libraries** folder, which also contained all the built-in libraries (like Wire and Serial).  
  
In v17 and up, the user libraries are now stored in the **ArduinoSketchDirectory/libraries** folder. You may need to make the **libraries** sub-folder the first time. However, the good thing about this is you wont have to move & reinstall your libraries every time you upgrade the software.  
  
For example, here is how it looks when NewSoftSerial is installed in Windows (of course your username will be different).  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/308/medium800/learn_arduino_nsslibrarypath.gif?1448059496)

On a Mac, your arduino sketch folder is likely going to be called **Documents/arduino** so create a NEW FOLDER inside that called **libraries** and place the uncompressed library folder inside of that.  
  
Check that the Documents/arduino/libraries/MyNewLibary folder contains the .cpp and .h files.  
  
After you're done, restart the Arduino IDE.

- [Previous Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-uno-faq.md)
- [Next Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/bootloader.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Arduino bootloader-programmed chip (Atmega328P)

[Arduino bootloader-programmed chip (Atmega328P)](https://www.adafruit.com/product/123)
This is a preprogrammed Atmega328P chip, useful if you want to make your own Arduino-compatible or repair a damaged chip on an exisiting Arduino UNO, Duemilanove, Diecimila, or NG!  
  
This chip is programmed with 'ADAboot', my version of the bootloader that is...

Out of Stock
[Buy Now](https://www.adafruit.com/product/123)
[Related Guides to the Product](https://learn.adafruit.com/products/123/guides)

## Related Guides

- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [WiFi Candy Bowl Monitor](https://learn.adafruit.com/wifi-candy-bowl.md)
- [Arduino Lesson 1. Blink](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
