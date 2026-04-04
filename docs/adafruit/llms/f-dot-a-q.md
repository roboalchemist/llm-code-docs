# Source: https://learn.adafruit.com/rgb-lcd-shield/f-dot-a-q.md

# RGB LCD Shield

## F.A.Q.

### 

The monochrome display only responds to backlight colors with RED in them. &nbsp;Use "ON" and "OFF" instead.&nbsp; See the code snippet under&nbsp;"Using with Monochrome Displays"

### What pins are used? What pins are available?

The shield uses only the **SCL** and **SDA** I2C pins, and 5V power and ground. You can use the I2C pins for other I2C sensors/devices as long as they do not share the same address. If you are using an Arduino UNO, **Analog 4** and **Analog 5** are shared with SCL/SDA so you can't use them. Likewise, Arduino Leonardos share SCL/SDA with **Digital 2** & **Digital 3** so those would not be available.

### 

If you're seeing error messages that look like any (or all) of the following, it means that the Arduino IDE is not finding the Adafruit libraries

  - error: Adafruit\_MCP23017.h: No such file or directory
  - error: Adafruit\_RGBLCDShield.h: No such file or directory
  - error: 'Adafruit\_RGBLCDShield' does not name a type
  - error: 'lcd' was not declared in this scope
  - error: 'BUTTON\_UP' was not declared in this scope
  - error: 'BUTTON\_DOWN' was not declared in this scope
  - error: 'BUTTON\_LEFT' was not declared in this scope
  - error: 'BUTTON\_RIGHT' was not declared in this scope
  - error: 'BUTTON\_SELECT' was not declared in this scope

  
There are three possible causes for this:  

> **1. You didn't download the library folder.**

> > Adafruit has written some extra software to make it easy to use your shield. This software is contained in a library folder that you can download here:
> 
> > [https://github.com/adafruit/Adafruit-RGB-LCD-Shield-Library](https://github.com/adafruit/Adafruit-RGB-LCD-Shield-Library)
> 
> > You download the folder by clicking on the[Downloads](https://github.com/adafruit/Adafruit-RGB-LCD-Shield-Library/downloads) button in the top right. You will have the option of downloading the library in one of two compressed formats: '.zip' or '.tar.gz'. Windows and Mac users will probably want to select .zip, while Linux users may prefer .tar.gz.  
> >   
> > MacOS will automatically uncompress the downloaded file into a folder, which you should find in the Downloads folder.   
> >   
> > Windows users can double-click on the downloaded file. This will open an Explorer window which will allow you to extract the compressed library folder.

> > _(Continue to the next paragraph to find out what to do with the uncompressed download)_

> **2. The library folder has the wrong name.**  
> 
> > After downloading and uncompressing the library folder, you **_must_** change the name of the folder to **_exactly_**"Adafruit\_RGBLCDShield". Don't abbreviate, add any spaces, underscores or other characters. Make sure the capitalization is the same as shown here.

> > _(Continue to the next paragraph to find out where to put the library folder)_
> 
> **3. The library folder is in the wrong place.**  
> 
> > When you installed your Arduino IDE, it created a 'sketch folder' for you (if you don't already know where that sketch folder is, go into the Arduino application's 'Sketch' menu, and select 'Show Sketch Folder').  
> >   
> > _ **Inside** _ of the sketch folder, there should be another folder called 'libraries'. If not, create a new folder _inside_ of the sketch folder, and name it "libraries" (the name **_must_** be **_exactly_**"libraries" - not "library" or"librarys" - not _<u>even</u>_ "Libraries" with a capital 'L' ! ).  
> >   
> > Move your new Adafruit\_RGBLCDShield folder into this libraries folder.

Once you've made sure the folder has the right name and is in the right place, you have to close and reopen the Arduino IDE, so that it will recognize the new library.  
  
if you're curious, you can learn more about libraries here:   

> [http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries](http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries "Link: http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries")

### Does the shield do the button de-bounce logic internally, or do I need to do that in software when reading the buttons?

The&nbsp;`Adafruit_RGBLCDShield` library handles button&nbsp;debouncing&nbsp;for you, when you use the `readButtons()` function.

### Is this compatible with my Arduino?  There are two extra pins on the header that don't plug into anything.

The shield will work fine with older Arduino boards. Extra pins were added to the R3 version of the Uno and Mega. &nbsp;These are duplicates of other header pins and are not required for proper operation of the shield. &nbsp;

### 

At this time, it does not! This shield is for Arduinos only!

### 

Only the ground pin next to the VIN pin is used. You need to connect your ground wire to this pin.

### 

Technically, yes. The pinouts for 20x4 and 16x2 are identical. However, the screen is way bigger, and it covers the buttons up so we don't suggest it.

- [Previous Page](https://learn.adafruit.com/rgb-lcd-shield/circuitpython.md)
- [Next Page](https://learn.adafruit.com/rgb-lcd-shield/downloads.md)

## Primary Products

### Adafruit I2C Controlled + Keypad Shield Kit for 16x2 LCD

[Adafruit I2C Controlled + Keypad Shield Kit for 16x2 LCD](https://www.adafruit.com/product/715)
We really like the range of LCDs we stock in the shop, such as our classic [blue & white](http://www.adafruit.com/products/181) and the fancy [RGB negative](http://www.adafruit.com/products/399) and [RGB positive](http://www.adafruit.com/products/398)....

In Stock
[Buy Now](https://www.adafruit.com/product/715)
[Related Guides to the Product](https://learn.adafruit.com/products/715/guides)

## Featured Products

### RGB backlight negative LCD 16x2 + extras

[RGB backlight negative LCD 16x2 + extras](https://www.adafruit.com/product/399)
This is a fancy upgrade to standard 16x2 LCDs, instead of just having blue and white, or red and black, this LCD has full color RGB characters on a dark/black background! That means you can change the character display colors to anything you want - red, green, blue, pink, white, purple yellow,...

In Stock
[Buy Now](https://www.adafruit.com/product/399)
[Related Guides to the Product](https://learn.adafruit.com/products/399/guides)
### RGB backlight positive LCD 16x2 + extras

[RGB backlight positive LCD 16x2 + extras](https://www.adafruit.com/product/398)
This is a fancy upgrade to standard 16x2 LCDs, instead of just having blue and white, or red and black, this LCD has black characters on a full color RGB-backlight background! That means you can change the background color to anything you want - red, green, blue, pink, white, purple yellow,...

In Stock
[Buy Now](https://www.adafruit.com/product/398)
[Related Guides to the Product](https://learn.adafruit.com/products/398/guides)
### LCD Shield Kit w/ 16x2 Character Display - Only 2 pins used!

[LCD Shield Kit w/ 16x2 Character Display - Only 2 pins used!](https://www.adafruit.com/product/772)
This new Adafruit shield makes it easy to use a 16x2 Character LCD. We really like the [Blue & White 16x2 LCDs we stock in the shop](http://www.adafruit.com/products/181). Unfortunately, these LCDs do require quite a few digital pins, 6 to control the LCD and then another pin to...

In Stock
[Buy Now](https://www.adafruit.com/product/772)
[Related Guides to the Product](https://learn.adafruit.com/products/772/guides)
### RGB LCD Shield Kit w/ 16x2 Character Display - Only 2 pins used!

[RGB LCD Shield Kit w/ 16x2 Character Display - Only 2 pins used!](https://www.adafruit.com/product/716)
This new Adafruit shield makes it easy to use a 16x2 Character LCD. We really like the RGB LCDs we stock in the shop both the [RGB negative](http://www.adafruit.com/products/399) and [RGB positive](http://www.adafruit.com/products/398). Unfortunately, these LCDs do...

Out of Stock
[Buy Now](https://www.adafruit.com/product/716)
[Related Guides to the Product](https://learn.adafruit.com/products/716/guides)
### RGB LCD Shield Kit w/ 16x2 Character Display - Only 2 pins used!

[RGB LCD Shield Kit w/ 16x2 Character Display - Only 2 pins used!](https://www.adafruit.com/product/714)
This new Adafruit shield makes it easy to use a 16x2 Character LCD. We really like the RGB LCDs we stock in the shop both the [RGB negative](http://www.adafruit.com/products/399) and [RGB positive](http://www.adafruit.com/products/398). Unfortunately, these LCDs do...

In Stock
[Buy Now](https://www.adafruit.com/product/714)
[Related Guides to the Product](https://learn.adafruit.com/products/714/guides)

## Related Guides

- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Simple Arduino-based USB VID & PID tester](https://learn.adafruit.com/simple-arduino-based-usb-vid-and-pid-tester.md)
- [Arduino "Hunt The Wumpus"](https://learn.adafruit.com/arduino-hunt-the-wumpus.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
- [Trinket Ultrasonic Rangefinder](https://learn.adafruit.com/trinket-ultrasonic-rangefinder.md)
- [Trinket RGB Shield Clock](https://learn.adafruit.com/trinket-rgb-shield-clock.md)
- [Adafruit Capacitive Touch Sensor Breakouts](https://learn.adafruit.com/adafruit-capacitive-touch-sensor-breakouts.md)
- [Trinket Temperature & Humidity LCD Display](https://learn.adafruit.com/trinket-temperature-humidity-lcd-display.md)
- [Character LCD with Raspberry Pi or BeagleBone Black](https://learn.adafruit.com/character-lcd-with-raspberry-pi-or-beaglebone-black.md)
- [eInk Literature Quotes Clock for MagTag](https://learn.adafruit.com/eink-literary-quotes-clock-for-magtag.md)
- [Adafruit Feather RP2040 with DVI Output Port](https://learn.adafruit.com/adafruit-feather-rp2040-dvi.md)
- [Portable Solar Charging Tracker](https://learn.adafruit.com/portable-solar-charging-tracker.md)
- [Adafruit E-Ink Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-e-ink-bonnet-for-raspberry-pi.md)
- [What’s Fresh Today? In-Season Produce Reminder for Adafruit MagTag](https://learn.adafruit.com/seasonal-produce-for-adafruit-magtag.md)
- [No-Solder Visualizer Capacitive Touch Controller](https://learn.adafruit.com/no-solder-visualizer-capacitive-touch-controller.md)
