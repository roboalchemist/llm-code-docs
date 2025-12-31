# Source: https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/advanced-topics.md

# Adalight Project Pack

## Advanced Topics

This tutorial focused on the 25 LED&nbsp;Adalight project pack, which is good for monitors up to 27 inches diagonal. Some users want to build a larger rig for their living room TV. This can be done without too much trouble…but, just like the LED mount required some creative problem solving, boosting Adalight with additional LEDs will require some planning and a willingness to improvise in order to fit your specific situation.  
  
The first thing needed is a more potent power supply. The 2 Amp supply included with the project pack is perfect for one strand of RGB pixels, but for two to six strands&nbsp;(50 to 150 LEDs)&nbsp;you’ll instead want to use our [5 Volt 10 Amp power supply](https://www.adafruit.com/products/658):

![](https://cdn-learn.adafruit.com/assets/assets/000/001/569/medium800/led_pixels_ID658_LRG.jpg?1396773926)

Wiring for 50 LEDs is super easy: follow the wiring diagram that was given for the standard project pack (substituting the larger power supply above). Just as before, the DC jack adapter connects to the extra red and blue&nbsp;wires&nbsp;at the <u>end</u> of the <u>first strand</u> of LEDs. Then plug the second strand of LEDs into the end receptacle, and make sure <u>all</u> spare&nbsp;red/blue end wires&nbsp;are insulated or trimmed. Done! The second strand receives power through the mating connector.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/571/medium800/led_pixels_adalight-50.png?1396773957)

Wiring for 75, 100 or more LEDs is a little more complicated. You’ll need some additional wire for distributing power, and a bit of soldering may be required.  
  
The trick here is to minimize the length that power needs to travel along the LED strands. This ensures better brightness and more uniform color. As explained in the project pack tutorial, 5V can be applied at <u>either end</u> of a strand. We exploit this in the 50 LED setup above by connecting power near the middle…25 LEDs are powered in one direction, and 25 the other.  
  
With _more_ than 50 LEDs you’ll need to provide additional connections for power.&nbsp;This could be done at the start of every strand…but using the same trick as above, it’s also possible to alternate strands: for 100 pixels, connect power to the wires at the <u>end</u>&nbsp;of the <u>first</u> and <u>third</u> strands, and the others will receive power through the mating connectors.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/573/medium800/led_pixels_adalight-100.png?1396773979)

Distribute power using extra wires connected at the DC jack. You can screw down two or sometimes three wires in each terminal. If that’s too crowded or if you want more secure connections, solder your own “Y” connections and insulate these with heat-shrink tube.  
  
To connect to the strand power wires, you can either solder and insulate these connections, or use&nbsp;[Euro-style terminal blocks](http://adafruit.com/products/677)&nbsp;—&nbsp;these can be clipped apart to provide two + and two – junctions.

# Software Adjustments for Larger Setups
No changes are required in the Arduino software; it’s designed to work with&nbsp;arbitrarily large LED setups. If you’ve already uploaded the code to the Arduino board, you do not need to repeat this process.  
  
The Adalight Processing sketch <u>will</u> require modification.&nbsp;This is the tricky part that’s specific to your setup…it’s not a simple copy-and-paste change,&nbsp;because televisions have different bezel sizes, stands, speakers or other obstructions to take into account.&nbsp;Arts and crafts time!  
  
We need to sketch out a grid that’s close to the shape of the screen, with the right number of squares around the perimeter to match&nbsp;our LED strands. It’s recommended that you try&nbsp;a few sizes and&nbsp;iterations on paper.&nbsp;You don’t&nbsp;_have_&nbsp;to put LEDs in the corner squares (some users don’t like the look and will&nbsp;skip them), and in the end you might end up with a few more LEDs than grid squares — that’s okay, you can bundle the extra unused LEDs behind the screen.  
  
Number the columns starting from 0 at the left, and the rows starting from 0 at the top. We’ll need these coordinates later for&nbsp;telling the software the position of each LED pixel.&nbsp;One common arrangement with 50-pixel installations has 17 squares across and 10 squares down, because it’s close to the 16:9 aspect ratio of most HDTVs.&nbsp;Grid location (0,0) will then&nbsp;refer to the top left square, and (16,9) to the bottom&nbsp;right.  
  
I like to put the first LED (the one closest to the Arduino) at the bottom center of the screen, because the USB and power cords&nbsp;can be bundled alongside other cables already coming from the display. But you can start at any position, whatever works best with your own telly.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/578/medium800/led_pixels_grid-diagram.png?1396774029)

(This is the view from the <u>front</u> of the screen. When installing the LEDs on the back, you’ll want to mirror the layout, flipping everything left-to-right.)  
  
Open the Adalight sketch in Processing and look for the following block of code starting around line 68:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/576/medium800/led_pixels_codeblock1.png?1396773998)

The two numbers highlighted above should be changed to the width and height of your grid (17 and 10 for our sample grid above). Leave the initial '0' untouched. And you can ignore the second line (in gray) — that’s for multiple monitor setups.  
  
Next, look for this block of code, starting around line 87:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/579/medium800/led_pixels_codeblock2.png?1396774035)

Each set of three numbers in curly brackets {a,b,c} represents one LED pixel, specified in-order along the strand (the first set is pixel #1, second set is pixel #2, and so forth). The first number of each set should always be 0, while the second and third numbers are the column and row (or “x” and “y” coordinates) of that pixel. For our 50 LED sample grid above, the first pixel (at the bottom center) would be {0,8,9}, the second pixel {0,7,9}, progressing around the perimeter in the order we chose earlier.&nbsp;(More hints:&nbsp;pixel #11 is at {0,0,7}, pixel #30 is at {0,12,0}, and pixel #40 is at {0,16,6}…see how it works?)  
  
If you try to run the modified program but it throws an error, you’ve probably mis-typed one of these number sets. Make sure there are three numbers in each set, separated with commas both between numbers and between sets.

# Building a Standalone Adalight Program
Once the Processing sketch is working to your satisfaction, you can build a double-clickable standalone version that doesn’t require running the Processing IDE every time.  
  
Load the Adalight.pde sketch in Processing. Then, from the “File” menu, select “Export Application.” Select your OS type, <u>do not</u> check the full-screen option, then click the “Export” button. This will create an application folder containing the standalone program and some support files. You can quit Processing now and just use the standalone version.  
  
We’ve experimented with a stealth windowless version of Adalight…can’t say for certain how reliable this technique will be across all different systems,&nbsp;but you can try out the technique [described in this this forum discussion](http://forums.adafruit.com/viewtopic.php?f=47&t=29978 "Link: http://forums.adafruit.com/viewtopic.php?f=47&t=29978") and see what you get.

# Third-Party Software Options
If editing Processing code isn’t your style, there are third-party software options that can also drive Adalight.  
  
Because we didn’t write these packages and aren’t familiar with their inner workings, we can’t provide technical support.&nbsp;If you’re having trouble getting an Adalight system up and running, we’ll always ask that you start with the Processing sketch first. Once that’s working, then feel free to explore.  
  
We’ve found [Lightpack](http://code.google.com/p/light-pack/) to be easy to use&nbsp;with a nice GUI and good performance. Don’t download the firmware file, just the software — with Adalight mode selected,&nbsp;this works with our&nbsp;LEDstream sketch already&nbsp;on the Arduino. The [Russian site for Lightpack](http://code.google.com/p/lightpack/) is a little more bleeding-edge, and includes&nbsp;Mac and Linux versions.  
  
[Boblight](http://code.google.com/p/boblight/) is another popular choice among Linux&nbsp;users.&nbsp;This is perhaps the most complex to set up, even moreso than the Processing code.&nbsp;With the right plug-in it’s said to also work with [xbmc](http://xbmc.org), but we’ve never gotten this far with it.

- [Previous Page](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/troubleshooting.md)

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

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [Arduino Tips, Tricks, and Techniques](https://learn.adafruit.com/arduino-tips-tricks-and-techniques.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [Wireless Power Switch with Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/wireless-power-switch-with-arduino-and-the-cc3000-wifi-chip.md)
- [Arduino Lesson 12. LCD Displays - Part 2](https://learn.adafruit.com/adafruit-arduino-lesson-12-lcd-displays-part-2.md)
- [How to Choose a Microcontroller](https://learn.adafruit.com/how-to-choose-a-microcontroller.md)
- [Adafruit Ultimate GPS Logger Shield](https://learn.adafruit.com/adafruit-ultimate-gps-logger-shield.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [A REST API for Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/a-rest-api-for-arduino-and-the-cc3000-wifi-chip.md)
- [Skill Badge Requirements: Microcontrollers](https://learn.adafruit.com/skill-badge-requirements-microcontrollers.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
- [How to program a Zumo Robot with Simulink](https://learn.adafruit.com/zumo-robot-control-with-simulink.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
