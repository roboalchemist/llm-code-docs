# Source: https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/running-the-software.md

# Adalight Project Pack

## Running the Software

Info: 

Launch the Processing IDE. After a moment, you should see a simple gray and white window that looks _very_ similar to the Arduino IDE.  
  
From the&nbsp; **File** &nbsp;menu, select&nbsp; **Sketchbook** , which should “roll over” to show&nbsp; **Adalight** and **Colorswirl**. Select the latter first: **Colorswirl**.  
  
Click the&nbsp; **Run** &nbsp;button near the top-left of the window:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/529/medium800/led_pixels_run-button.png?1396773755)

If the Arduino is the first or only serial device on the system, this should start a colorful rainbow of animation on the LEDs.  
  
If this is _not_ what happens, then you’ll need to edit some code. Around line 26, look for this statement:  
  
**&nbsp; myPort = new Serial(this, Serial.list()[0], 115200);**    
We need to change how the code opens the serial connection to the Arduino. One route is just through trial and error:&nbsp;try&nbsp;**Serial.list()[1]**, then **&nbsp;**** Serial.list()[2]**, and so forth, re-starting the program each time to see if it works. For a more scientific approach, add one new line of code before running the sketch:  
  
**&nbsp; println(Serial.list());**    
When run, this displays a list of all serial ports or devices. If you know which device or COM port corresponds to the Arduino, you can then change the original line to include this data. For example, it might now read:  
  
**&nbsp; myPort = new Serial(this, "COM6", 115200);**    
This will be different on every system, so we can’t just tell you what to put there.  
  
Another way to locate the port name: in the Arduino IDE, this is the port you selected in the&nbsp;Tools→Serial Port menu before programming the chip.  
  
Once you have Colorswirl working, make note of the change (if any), because the same change will need to be made in the Adalight code.  

![](https://cdn-learn.adafruit.com/assets/assets/000/001/527/medium800/led_pixels_COMselect.gif?1447864292)

Moving ahead…  
  
From the&nbsp; **File** &nbsp;menu, select&nbsp; **Sketchbook** , then&nbsp; **Adalight**. If you changed the Colorswirl sketch to find the serial port, make that same change to the Adalight code.&nbsp;Now click the **Run** button.  
  
Though they’re in a jumbled mess on your desk right now, the LEDs should light up in colors resembling the perimeter of your screen. Move some windows around the edge — you should see the LEDs react to this.  
  
As it runs, the software performs a continual series of screen captures, averaging the pixels in blocks around the perimeter of the screen and issuing the resulting color data to the LEDs. You can hide the preview window and let the sketch continue working in the background. Being capture-based, it’s not tied to any one specific media player, and most anything you can put on your display —&nbsp;MPEG&nbsp;movies, YouTube, games and so forth — can benefit from the effect. It seems to work especially well with the outer space sequences in&nbsp;_Cosmos_…a bit ironic in that Carl Sagan’s “Spaceship of the Imagination” from this series featured a giant flat screen and mood lighting decades before Philips turned it into a commercial product!

![](https://cdn-learn.adafruit.com/assets/assets/000/001/528/medium800/led_pixels_5-sampling.jpg?1396773738)

If you plan to arrange the LEDs similarly to our examples — 25 pixels in a ring, 1 pixel gap at the bottom, with the first pixel starting just left of the gap — then nothing&nbsp;more needs to be changed in the software.&nbsp;If using a different layout, you’ll need to make adjustments in the code.&nbsp;You'll find extensive notes in the source code for making this (and other) changes.

Once all the hardware and software is working, it’s time to get crafty and mount the LEDs on the telly…

- [Previous Page](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/download-and-install.md)
- [Next Page](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/choosing-leds.md)

## Featured Products

### Adalight - DIY Ambient Monitor Lighting Project Pack

[Adalight - DIY Ambient Monitor Lighting Project Pack](https://www.adafruit.com/product/461)
Build your own ambient-light addition for a monitor or media PC television with the Adalight project pack! This project pack is for our ["Adalight" project tutorial](http://learn.adafruit.com/adalight-diy-ambient-tv-lighting). By running the Processing code on your...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/461)
[Related Guides to the Product](https://learn.adafruit.com/products/461/guides)
### 12mm  Diffused Thin Digital RGB LED Pixels (Strand of 25)

[12mm  Diffused Thin Digital RGB LED Pixels (Strand of 25)](https://www.adafruit.com/product/322)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each RGB LED and controller chip is molded into a 'dot' of silicone. The dots are weatherproof and rugged. There are four flanges molded in so that you can 'push' them into a 12mm drill hole in...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/322)
[Related Guides to the Product](https://learn.adafruit.com/products/322/guides)
### 12mm  Diffused Flat Digital RGB LED Pixels (Strand of 25)

[12mm  Diffused Flat Digital RGB LED Pixels (Strand of 25)](https://www.adafruit.com/product/738)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each RGB LED and controller chip is molded into a 'dot' of silicone. The dots are weatherproof and rugged. There are four flanges molded in so that you can 'push' them into a 12mm drill hole in...

In Stock
[Buy Now](https://www.adafruit.com/product/738)
[Related Guides to the Product](https://learn.adafruit.com/products/738/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Female DC Power adapter - 2.1mm jack to screw terminal block

[Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
If you need to connect a DC power wall wart to a board that doesn't have a DC jack - this adapter will come in very handy! There is a 2.1mm DC jack on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/368)
[Related Guides to the Product](https://learn.adafruit.com/products/368/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

In Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [2.2" TFT Display](https://learn.adafruit.com/2-2-tft-display.md)
- [Arduin-o-Phone](https://learn.adafruit.com/arduin-o-phone-arduino-powered-diy-cellphone.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [Adafruit 1.27" and 1.5" Color OLED Breakout Board](https://learn.adafruit.com/adafruit-1-5-color-oled-breakout-board.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Arduino Lesson 7. Make an RGB LED Fader](https://learn.adafruit.com/adafruit-arduino-lesson-7-make-an-rgb-led-fader.md)
- [Wave Shield](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino.md)
- [Adafruit 1.14" 240x135 Color TFT Breakout LCD Display](https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout.md)
- [Adafruit Arduino Selection Guide](https://learn.adafruit.com/adafruit-arduino-selection-guide.md)
- [Arduino Lesson 3. RGB LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
