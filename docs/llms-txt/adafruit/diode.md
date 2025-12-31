# Source: https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/diode.md

# Battery Power for LED Pixels and Strips

## Diode Fix for Alkaline Batteries

> “I don’t know if you wanna trust the safety of our country&nbsp;to some, uh…silicone diode!”

> > — General Beringer, _WarGames_

![](https://cdn-learn.adafruit.com/assets/assets/000/001/335/medium800/leds_1n4001.jpg?1396771117)

A single&nbsp;[1N4001 diode](https://www.adafruit.com/products/755)&nbsp;has about a 0.7 Volt drop across its leads. Wired to our 6 Volt battery pack (when using alkaline cells), this yields 5.3 Volts output.&nbsp;That’s within our 5V±10% target window, so this simple component addition is&nbsp;all that’s needed to&nbsp;use the battery pack with the LED strips and pixels.  
  
This same solution can&nbsp;be seen in our [Digital Programmable LED Belt Kit](http://adafruit.com/products/332 "Link: http://adafruit.com/products/332").  
  
Diodes have a specific _polarity,_ passing current in only one direction_…_the silver stripe is the + end.&nbsp;So we want to connect the + terminal from the battery pack to the “dark” end with no stripe.

Danger: 

Danger: 

Cut the **red** wire of the battery pack short by about an inch.

![leds_redclip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/336/medium640/leds_redclip.jpg?1396771186)

Strip off about 3/8" insulation from the red wire.

![leds_redstrip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/337/medium640/leds_redstrip.jpg?1396771193)

Then “tin” the end of the wire with a bit of solder&nbsp;to keep it from fraying.

![leds_redtin.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/338/medium640/leds_redtin.jpg?1396771200)

Clip the end of the diode (the “dark” end, _without_ a silver stripe)&nbsp;to a similar length, then solder the red wire to this.

![leds_diodesolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/339/medium640/leds_diodesolder.jpg?1396771208)

Clip the other end of the diode&nbsp;(the side with a silver stripe).

  

![leds_diodeclip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/340/medium640/leds_diodeclip.jpg?1396771213)

Cut off and slide a 2" piece of heat shrink tube onto the red wire. Keep sliding it all the way past the diode.

![leds_shrinkslide.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/341/medium640/leds_shrinkslide.jpg?1396771221)

Now solder the positive wire from your LED circuit to the “stripe” end of the diode. Or you can add a plug/receptacle pair between the two to make them easier to separate and service later on.

![leds_diodesolder2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/342/medium640/leds_diodesolder2.jpg?1396771231)

Take the piece of heat shrink you slid over the wire before…

![leds_diodeslide.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/343/medium640/leds_diodeslide.jpg?1396771237)

…and slide it back over the diode and the solder joints.

![leds_diodepreshrink.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/344/medium640/leds_diodepreshrink.jpg?1396771243)

Shrink the tubing to grip the diode and wires. You can use a heat gun, lighter or the edge of your soldering iron.

![leds_diodeshrink.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/345/medium640/leds_diodeshrink.jpg?1396771252)

Taa-daah!

![leds_diodeshrunk.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/346/medium640/leds_diodeshrunk.jpg?1396771262)

The black wire from the battery holder then connects to the ground wire of the LED circuit (or plug/receptacle, if you’ve installed one). This side is much simpler than the diode-equipped wire:

Slide a small 1" piece of heat shrink onto the black wire (this image shows a much shorter piece…oops…go a little longer than this).

![leds_negslide.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/347/medium640/leds_negslide.jpg?1396771272)

Solder together the ends of the wires. The dreaded _inline splice!_

![leds_negsolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/348/medium640/leds_negsolder.jpg?1396771284)

Then slide and shrink as you did before. Done!

![leds_negshrunk.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/349/medium640/leds_negshrunk.jpg?1396771292)

- [Previous Page](https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/about-batteries.md)
- [Next Page](https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/powering-the-microcontroller-too.md)

## Featured Products

### Digital programmable LED belt kit

[Digital programmable LED belt kit](https://www.adafruit.com/product/332)
By popular demand, we now have a project tutorial for how to make your own programmable, ultra-blinky LED belt. Perfect for parties, raves, parades, weddings, funerals, and bar mitzvahs. Wear it with pride, wear it with blinky! Follow our soldering tutorial to build your own heirloom LED belt,...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/332)
[Related Guides to the Product](https://learn.adafruit.com/products/332/guides)
### Alkaline AAA batteries - 2 pack

[Alkaline AAA batteries - 2 pack](https://www.adafruit.com/product/617)
Battery power for your portable project! These batteries are good quality at a good price, and work fantastic with any of the kits or projects in the shop that use AAA's.&nbsp;This is a pack of **2&nbsp;AAA batteries**.  
  
These batteries are Alkaline (MnO2) chemistry,...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/617)
[Related Guides to the Product](https://learn.adafruit.com/products/617/guides)
### 1N4001 Diode - 10 pack

[1N4001 Diode - 10 pack](https://www.adafruit.com/product/755)
This here is a 10 pack of the classic 1N4001 power blocking diode. These are good for reverse polarity protection (put it between your DC power jack and circuitry to avoid a negative-voltage that would zap your delicate electronics), kickback protection (place across your solenoids, relays...

In Stock
[Buy Now](https://www.adafruit.com/product/755)
[Related Guides to the Product](https://learn.adafruit.com/products/755/guides)
### 4 x AA Battery Holder with On/Off Switch

[4 x AA Battery Holder with On/Off Switch](https://www.adafruit.com/product/830)
Make a nice portable power pack with this 4 x AA battery holder. It fits any alkaline or rechargeable AA batteries in series. There's a snap on cover and an on/off switch which can be handy when wiring to something without a switch.

**New**! We now have 0.1" headers...

In Stock
[Buy Now](https://www.adafruit.com/product/830)
[Related Guides to the Product](https://learn.adafruit.com/products/830/guides)
### 12mm  Diffused Flat Digital RGB LED Pixels (Strand of 25)

[12mm  Diffused Flat Digital RGB LED Pixels (Strand of 25)](https://www.adafruit.com/product/738)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each RGB LED and controller chip is molded into a 'dot' of silicone. The dots are weatherproof and rugged. There are four flanges molded in so that you can 'push' them into a 12mm drill hole in...

In Stock
[Buy Now](https://www.adafruit.com/product/738)
[Related Guides to the Product](https://learn.adafruit.com/products/738/guides)
### 12mm  Diffused Thin Digital RGB LED Pixels (Strand of 25)

[12mm  Diffused Thin Digital RGB LED Pixels (Strand of 25)](https://www.adafruit.com/product/322)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each RGB LED and controller chip is molded into a 'dot' of silicone. The dots are weatherproof and rugged. There are four flanges molded in so that you can 'push' them into a 12mm drill hole in...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/322)
[Related Guides to the Product](https://learn.adafruit.com/products/322/guides)
### Digital RGB LED Weatherproof Strip - LPD8806 32 LED 5m

[Digital RGB LED Weatherproof Strip - LPD8806 32 LED 5m](https://www.adafruit.com/product/306)
These LED strips are fun and glowy. There are 32 RGB LEDs per meter, and you can control each LED individually! Yes, that's right, this is the digitally-addressable type of LED strip. You can set the color of each LED's red, green and blue component with 7-bit PWM precision (so 21-bit...

In Stock
[Buy Now](https://www.adafruit.com/product/306)
[Related Guides to the Product](https://learn.adafruit.com/products/306/guides)

## Related Guides

- [LPD8806 Digital RGB LED Strip](https://learn.adafruit.com/digital-led-strip.md)
- [3D Printed Battery Tester](https://learn.adafruit.com/3d-printed-battery-tester.md)
- [Adafruit LED Sequins](https://learn.adafruit.com/adafruit-led-sequins.md)
- [ISS Pin](https://learn.adafruit.com/iss-pin.md)
- [Bluetooth Controlled NeoPixel Headphones](https://learn.adafruit.com/bluetooth-controlled-neopixel-headphones.md)
- [Make It Glow - Your First NeoPixel Project](https://learn.adafruit.com/make-it-glow-your-first-neopixel-project.md)
- [Hexpad](https://learn.adafruit.com/hexpad.md)
- [Simon Game for PyRuler and CircuitPython](https://learn.adafruit.com/simon-game-with-pyruler-and-circuitpython.md)
- [Sipping Power With NeoPixels](https://learn.adafruit.com/sipping-power-with-neopixels.md)
- [Adafruit Neo Trinkey](https://learn.adafruit.com/adafruit-neo-trinkey.md)
- [Adalight for Circuit Playground](https://learn.adafruit.com/adalight-for-circuit-playground.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
- [GitHub Actions Status Tower Light](https://learn.adafruit.com/github-actions-status-tower-light.md)
- [LED Noodle Lantern](https://learn.adafruit.com/led-noodle-lantern.md)
- [Easy LED Jeweled Necklace](https://learn.adafruit.com/led-jeweled-necklace.md)
- [Make It Glow With Crickit](https://learn.adafruit.com/make-it-glow-with-crickit.md)
