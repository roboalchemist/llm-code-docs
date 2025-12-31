# Source: https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/tips-for-larger-projects.md

# Battery Power for LED Pixels and Strips

## Tips for Larger Projects

![](https://cdn-learn.adafruit.com/assets/assets/000/001/377/medium800/leds_belt.jpg?1396771617)

AA batteries are surprisingly potent little things, and a set of four can comfortably run about a meter of LPD8806 LED strip or one strand of 25 12mm pixels for a couple hours or more. You can go beyond this to create larger projects, with some forethought…

- A fully-lit 1 meter strip can demand close to 2 Amps, but the batteries and diode are only rated for a continuous output of&nbsp;about 1 Amp. You can push beyond this for brief intervals, but it <u>can’t be sustained</u>. Design your software so that the LEDs seldom or never exceed this level, using the 60 mA rule of thumb.
- Voltage diminishes slightly along the length of a strand. And when voltage drops too far, the LEDs will show dim and muddy colors. When using long runs of LEDs, we recommend adding an extra power tap every meter or 25 pixels to reduce this voltage drop.
- Remember that “off” pixels still need a tiny bit of current for the driver chips…about 50 mA per strand or meter…and another 25 mA for the microcontroller. Factor this into your battery calculations and software design. Large setups may be using hundreds of milliamps that are never seen, but continuously pass through that diode with its 1 Amp ceiling.
- C or D cells have more capacity for extra run time (up to 12,000 mAh with top-of-the-line NiMH D cells). We don't stock battery holders for these, but suitable ones can be found at Radio Shack and elsewhere. The 1N4001 diode is still rated for 1 Amp continuous output though…so for a larger project with many LEDs simultaneously lit, you might need to swap this out for a beefier diode such as a 1N5400, good for up to 3 Amps.&nbsp;This may get hot, so don’t leave it exposed to curious fingers.  

- [Previous Page](https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/estimating-running-time.md)

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
