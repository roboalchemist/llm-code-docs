# Source: https://learn.adafruit.com/rgb-lcd-shield/using-the-rgb-lcd-shield.md

# RGB LCD Shield

## Arduino Usage

The shield is really easy to use. Once you have attached the LCD of choice, plug it onto the Arduino and [download our library from GitHub](https://github.com/adafruit/Adafruit-RGB-LCD-Shield-Library). The example included shows how to use the RGB backlight control and reading from the keypad.

# Download the Library

To interface with the LCD and buttons you must use our library which translates the commands through the port expander

Open up the Arduino library manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/084/031/medium800/arduino_compatibles_library_manager_menu.png?1573523568)

Search for the&nbsp; **Adafruit RGB LCD Shield** &nbsp;library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/032/medium800/arduino_compatibles_lcd_shield.png?1573523592)

We also have a great tutorial on Arduino library installation at:  
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")

# Adjusting Contrast
The shield uses a character LCD with an external contrast potentiometer. The first time you use it, adjust the potentiometer in the bottom right until you see the text clearly. If you don't upload code to the Arduino, some boxes will appear instead  
Danger: 

# Shared Pins
**The I2C pins are shared with other pins, and each Arduino type has a different sharing scheme. Those pins cannot be used for anything else than I2C when this shield is used!**  
**Uno** /Duemilanove/Diecimila - I2C pins are also the same pins as **Analog 4** and **Analog 5**  
**Mega** 1280 and 2560 - I2C pins are also the same pins as **Digital 20** and **21**  
**Leonardo** and other 32u4-based - I2C pins are also the same pins as **Digital 2** and **3**  
# Writing Your Own Sketches
The **Adafruit\_RGBLCDShield** library is a derivative of the **LiquidCrystal** library that comes with Arduino so you can call any of the functions that you're used to and they'll work just the same.

There are two extra functions you may want to use. One is **lcd.setBacklight(_color_);** which will change the backlight color assuming you have an RGB LCD on. At this time, the library does not do any PWM on the RGB backlight, so you can select from 8 different colors (inlcuding OFF) - if you place these #define's at the top of your sketch you can simply call whichever color you want to appear.

```
// These #defines make it easy to set the backlight color
#define OFF 0x0
#define RED 0x1
#define YELLOW 0x3
#define GREEN 0x2
#define TEAL 0x6
#define BLUE 0x4
#define VIOLET 0x5
#define WHITE 0x7 
```

Another extra of the shield is a 4-way directional keypad plus select button. This will let you design your own control interface for 'stand-alone' Arduino projects. All the buttons are read at once when you call **lcd.readButtons();**&nbsp;which returns a variable that has individual bits set for the buttons. You can easily test for which buttons were held down at the time of the readButtons() call by using bitwise & as seen in this code snippet.  
  
Note that the library handles button debouncing internally.&nbsp; There is **no need to debounce the buttons** in your code.

```
uint8_t buttons = lcd.readButtons();

  if (buttons) {
    if (buttons &amp; BUTTON_UP) {
      lcd.setBacklight(RED);
    }
    if (buttons &amp; BUTTON_DOWN) {
      lcd.setBacklight(YELLOW);
    }
    if (buttons &amp; BUTTON_LEFT) {
      lcd.setBacklight(GREEN);
    }
    if (buttons &amp; BUTTON_RIGHT) {
      lcd.setBacklight(TEAL);
    }
    if (buttons &amp; BUTTON_SELECT) {
      lcd.setBacklight(VIOLET);
    }
  }
```

# Using with Monochrome Displays
Displays with monochrome backlights are controlled by the RED pin and will only respond to colors that have RED in them (RED, YELLOW, VIOLET). For these displays, you can use ON and OFF instead as in the snippet below:  
```auto
uint8_t buttons = lcd.readButtons();

  if (buttons) {
    lcd.clear();
    lcd.setCursor(0,0);
    if (buttons &amp; BUTTON_UP) {
      lcd.print("UP ");
      lcd.setBacklight(HIGH);
    }
    if (buttons &amp; BUTTON_DOWN) {
      lcd.print("DOWN ");
      lcd.setBacklight(LOW);
    }
```

# Detached Usage
If you want to have the shield disconnected from the Arduino (say to panel mount it) or if you want to use it with a different type of processor board, its very easy!

Just power the&nbsp; **5V&nbsp;** pin with 5V, common ground to&nbsp; **GND** &nbsp;and then connect the **&nbsp;SCL** &nbsp;labeled pin (top left) to I2C clock and **&nbsp;SDA&nbsp;** to I2C data. Those are the only four wires you need to control the entire shield.

- On Uno-shaped Arduinos,&nbsp; **SCL** &nbsp;is also connected to Analog 5 and&nbsp; **SDA&nbsp;** is connected to Analog 4.
- On Mega Arduinos,&nbsp; **SCL** &nbsp;is also connected to Digital 21 and&nbsp; **SDA&nbsp;** is connected to Digital 20.
- On Leonardo Arduinos,&nbsp; **SCL** &nbsp;is also connected to Digital 3 and&nbsp; **SDA&nbsp;** is connected to Digital 2.

Danger: 

Warning: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/439/medium800/lcds___displays_RGB_LCD_WIRING_rev1.png?1396772126)

- [Previous Page](https://learn.adafruit.com/rgb-lcd-shield/assembly.md)
- [Next Page](https://learn.adafruit.com/rgb-lcd-shield/circuitpython.md)

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
