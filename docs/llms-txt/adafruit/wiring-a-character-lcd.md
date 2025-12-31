# Source: https://learn.adafruit.com/character-lcds/wiring-a-character-lcd.md

# Character LCDs

## Wiring a Character LCD

## Installing the Header Pins
![](https://cdn-learn.adafruit.com/assets/assets/000/000/922/medium800/lcds___displays_parts.jpg?1396766765)

OK now you've got your LCD, you'll also need a couple other things. First is a 10K potentiometer. This will let you adjust the contrast. Each LCD will have slightly different contrast settings so you should try to get some sort of trimmer. You'll also need some 0.1" header - 16 pins long.![](https://cdn-learn.adafruit.com/assets/assets/000/000/923/medium800/lcds___displays_headersize.jpg?1396767162)

If the header is too long, just cut/snap it short!

Next you'll need to solder the header to the LCD. **You must do this, it is not OK to just try to 'press fit' the LCD!**

Also watch out not to apply too much heat, or you may melt the underlying breadboard. You can try 'tacking' pin 1 and pin 16 and then removing from the breadboard to finish the remaining solder points

![](https://cdn-learn.adafruit.com/assets/assets/000/000/924/medium800/lcds___displays_lcdbb.jpg?1396767167)

The easiest way we know of doing this is sticking the header into a breadboard and then sitting the LCD on top while soldering. this keeps it steady.## Power and Backlight
K now we're onto the interesting stuff! Get your LCD plugged into the breadboard.![lcds___displays_lcdbb2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/925/medium640/lcds___displays_lcdbb2.jpg?1396767174)

Now we'll provide power to the breadboard. Connect +5V to the red rail, and Ground to the blue rail.![lcds___displays_bbpower.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/926/medium640/lcds___displays_bbpower.jpg?1396767183)

Next we'll connect up the backlight for the LCD. Connect pin 16 to ground and pin 15 to +5V. On the vast majority of LCDs (including ones from Adafruit) the LCD includes a series resistor for the LED backlight.  
  
If you happen to have one that does not include a resistor, you'll need to add one between 5V and pin 15. To calculate the value of the series resistor, look up the maximum backlight current and the typical backlight voltage drop from the data sheet. Subtract the voltage drop from 5 volts, then divide by the maximum current, then round up to the next standard resistor value. For example, if the backlight voltage drop is 3.5v typical and the rated current is 16mA, then the resistor should be (5 - 3.5)/0.016 = 93.75 ohms, or 100 ohms when rounded up to a standard value. If you can't find the data sheet, then it should be safe to use a 220 ohm resistor, although a value this high may make the backlight rather dim.

![lcds___displays_backlitepower.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/927/medium640/lcds___displays_backlitepower.jpg?1396767190)

Connect the Arduino up to power, you'll notice the backlight lights up.![lcds___displays_backlitetest.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/928/medium640/lcds___displays_backlitetest.jpg?1396767199)

Note that some low-cost LCDs dont come with a backlight. Obviously in this case you should just keep going.## Contrast Circuit
Next, lets place the contrast pot, it goes on the side near pin 1.![lcds___displays_potplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/929/medium640/lcds___displays_potplace.jpg?1396767206)

Connect one side of the pot to +5V and the other to Ground (it doesn't matter which goes on what side). The middle of the pot (wiper) connects to pin 3 of the LCD.

![lcds___displays_potwire.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/930/medium640/lcds___displays_potwire.jpg?1396767214)

Now we'll wire up the logic of the LCD - this is seperate from the backlight! Pin 1 is ground and pin 2 is +5V.![lcds___displays_lcdpower.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/931/medium640/lcds___displays_lcdpower.jpg?1396767221)

Now turn on the Arduino, you'll see the backlight light up (if there is one), and you can also twist the pot to see the first line of rectangles appear.![lcds___displays_contrasttest1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/932/medium640/lcds___displays_contrasttest1.jpg?1396767229)

![lcds___displays_contrasttest.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/933/medium640/lcds___displays_contrasttest.jpg?1396767240)

This means you've got the logic, backlight and contrast all worked out. Don't keep going unless you've got this figured out!## Bus Wiring
Now we'll finish up the wiring by connecting the data lines. There are 11 bus lines:&nbsp; **D0** &nbsp;through&nbsp; **D7** &nbsp;(8 data lines) and&nbsp; **RS** ,&nbsp; **EN** , and&nbsp; **RW**. D0-D7 are the pins that have the raw data we send to the display. The **RS** &nbsp;pin lets the microcontroller tell the LCD whether it wants to display that data (as in, an&nbsp;ASCII&nbsp;character) or whether it is a command byte (like, change posistion of the cursor). The&nbsp; **EN** &nbsp;pin is the 'enable' line we use this to tell the LCD when data is ready for reading. The&nbsp; **RW** &nbsp;pin is used to set the direction - whether we want to write to the display (common) or read from it (less common)

The good news is that not all these pins are necessary for us to connect to the microcontroller (Arduino).&nbsp; **RW** &nbsp;for example, is not needed if we're only writing to the display (which is the most common thing to do anyways) so we can 'tie' it to ground. There is also a way to talk to the LCD using only 4 data pins instead of 8. This saves us 4 pins! Why would you ever want to use 8 when you could use 4? We're not 100% sure but we think that in some cases its faster to use 8 - it takes twice as long to use 4 - and that speed is important. For us, the speed isn't so important so we'll save some pins!

So to recap, we need 6 pins:&nbsp; **RS, EN, D7, D6, D5,&nbsp;** and&nbsp; **D4** &nbsp;to talk to the LCD.

We'll be using the&nbsp; **LiquidCrystal** &nbsp;library to talk to the LCD so a lot of the annoying work of setting pins and such is taken care of. Another nice thing about this library is that you can use&nbsp; **any** &nbsp;Arduino pin to connect to the LCD pins. So after you go through this guide, you'll find it easy to swap around the pins if necessary

As mentioned, we'll not be using the&nbsp; **RW** &nbsp;pin, so we can tie it go ground. That's pin 5 as shown here.![lcds___displays_rwpin.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/934/medium640/lcds___displays_rwpin.jpg?1396767245)

Next is the&nbsp; **RS** &nbsp;pin #4. We'll use a brown wire to connect it to Arduino's digital pin # **7.** ![lcds___displays_rspin.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/935/medium640/lcds___displays_rspin.jpg?1396767255)

Next is the&nbsp; **EN** &nbsp;pin #6, we'll use a white wire to connect it to Arduino digital # **8.** ![lcds___displays_enpin.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/936/medium640/lcds___displays_enpin.jpg?1396767261)

Now we will wire up the data pins.&nbsp; **DB7** &nbsp;is pin #14 on the LCD, and it connects with an orange wire to Arduino # **12.** ![lcds___displays_db7pin.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/937/medium640/lcds___displays_db7pin.jpg?1396767271)

Next are the remaining 3 data lines,&nbsp; **DB6** &nbsp;(pin #13 yellow)&nbsp; **DB5** &nbsp;(pin #12 green) and&nbsp; **DB4** &nbsp;(pin #11 blue) which we connect to Arduino # **11, 10** &nbsp;and&nbsp;**9.  
  
You should have four 'gap' pins on the LCD between the 4 data bus wires and the control wires.**

![lcds___displays_datapins.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/938/medium640/lcds___displays_datapins.jpg?1396767276)

This is what you'll have on your desk.![lcds___displays_bigpicture.jpg](https://cdn-learn.adafruit.com/assets/assets/000/000/939/medium640/lcds___displays_bigpicture.jpg?1396767286)

- [Previous Page](https://learn.adafruit.com/character-lcds/lcd-varieties.md)
- [Next Page](https://learn.adafruit.com/character-lcds/arduino-code.md)

## Featured Products

### Standard LCD 16x2 + extras

[Standard LCD 16x2 + extras](https://www.adafruit.com/product/181)
Standard HD44780 LCDs are useful for creating standalone projects.

- 16 characters wide, 2 rows
- White text on blue background
- Connection port is 0.1" pitch, single row for easy breadboarding and wiring
- Pins are documented on the back of the LCD to assist...

In Stock
[Buy Now](https://www.adafruit.com/product/181)
[Related Guides to the Product](https://learn.adafruit.com/products/181/guides)
### Assembled Standard LCD 16x2 + extras - White on Blue

[Assembled Standard LCD 16x2 + extras - White on Blue](https://www.adafruit.com/product/1447)
Standard HD44780 LCDs are useful for creating standalone projects. &nbsp;This product is similar to our [Standard LCD 16x2 display **but comes with the header soldered on!**](https://www.adafruit.com/products/181)

- 16 characters wide, 2 rows
- White text...

In Stock
[Buy Now](https://www.adafruit.com/product/1447)
[Related Guides to the Product](https://learn.adafruit.com/products/1447/guides)
### RGB backlight positive LCD 16x2 + extras

[RGB backlight positive LCD 16x2 + extras](https://www.adafruit.com/product/398)
This is a fancy upgrade to standard 16x2 LCDs, instead of just having blue and white, or red and black, this LCD has black characters on a full color RGB-backlight background! That means you can change the background color to anything you want - red, green, blue, pink, white, purple yellow,...

In Stock
[Buy Now](https://www.adafruit.com/product/398)
[Related Guides to the Product](https://learn.adafruit.com/products/398/guides)
### RGB backlight negative LCD 16x2 + extras

[RGB backlight negative LCD 16x2 + extras](https://www.adafruit.com/product/399)
This is a fancy upgrade to standard 16x2 LCDs, instead of just having blue and white, or red and black, this LCD has full color RGB characters on a dark/black background! That means you can change the character display colors to anything you want - red, green, blue, pink, white, purple yellow,...

In Stock
[Buy Now](https://www.adafruit.com/product/399)
[Related Guides to the Product](https://learn.adafruit.com/products/399/guides)
### Standard LCD 20x4 + extras

[Standard LCD 20x4 + extras](https://www.adafruit.com/product/198)
Standard HD44780 LCDs are useful for creating standalone projects.

- 20 characters wide, 4 rows
- White text on blue background
- Connection port is 0.1" pitch, single row for easy breadboarding and wiring
- Single LED backlight with a resistor included, you can...

In Stock
[Buy Now](https://www.adafruit.com/product/198)
[Related Guides to the Product](https://learn.adafruit.com/products/198/guides)
### RGB backlight positive LCD 20x4 + extras

[RGB backlight positive LCD 20x4 + extras](https://www.adafruit.com/product/499)
This is a fancy upgrade to standard 20x4 LCDs, instead of just having blue and white, or red and black, this LCD has black characters on a full color RGB background! That means you can change the display background color to anything you want - red, green, blue, pink, white, purple yellow,...

In Stock
[Buy Now](https://www.adafruit.com/product/499)
[Related Guides to the Product](https://learn.adafruit.com/products/499/guides)
### RGB backlight negative LCD 20x4 + extras

[RGB backlight negative LCD 20x4 + extras](https://www.adafruit.com/product/498)
This is a fancy upgrade to standard 20x4 LCDs, instead of just having blue and white, or red and black, this LCD has full color RGB characters on a dark/black background! That means you can change the character display colors to anything you want - red, green, blue, pink, white, purple yellow,...

Out of Stock
[Buy Now](https://www.adafruit.com/product/498)
[Related Guides to the Product](https://learn.adafruit.com/products/498/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
- [Adafruit VS1053 MP3/AAC/Ogg/MIDI/WAV Codec Breakout Tutorial](https://learn.adafruit.com/adafruit-vs1053-mp3-aac-ogg-midi-wav-play-and-record-codec-tutorial.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [How to Build a Testing Jig](https://learn.adafruit.com/how-to-build-a-testing-fixture.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [WiFi Controlled Mobile Robot](https://learn.adafruit.com/wifi-controlled-mobile-robot.md)
- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [RGB LCD Shield](https://learn.adafruit.com/rgb-lcd-shield.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
