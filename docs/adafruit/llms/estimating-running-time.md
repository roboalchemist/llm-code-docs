# Source: https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/estimating-running-time.md

# Battery Power for LED Pixels and Strips

## Estimating Running Time

### 

This can be fiendishly difficult to predict! Sometimes the only way to be sure is to plug it in with a fresh set of batteries and check the circuit and a clock periodically, until the LEDs fade or start to act erratically.

### 

Digital LEDs seldom run in one fixed state — they’re usually animated. We can estimate the power use for a steady configuration, but animation is constantly in flux.  
  
Also, battery manufacturers often overstate their cells’ capacity, or express it under extremely idealized circumstances.

### 

Track down a datasheet for your batteries! You might find it on the manufacturer’s web site, or a vendor site such as Digi-Key. Easiest is just to use a web search engine. In most battery datasheets you’ll see one or more charts like this one:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/351/medium800/leds_chart.png?1396771322)

This chart shows the cell’s output voltage over time, at different discharge rates.&nbsp;You can see that the expected service life is&nbsp;_not_&nbsp;directly proportional to power drain — halving the latter more than doubles the former.&nbsp;Again, with a fixed configuration, we could plan for this, but our LEDs are in motion, which doesn’t make things any easier. You’ll probably just have to come up with an informed _average._  
  
Elsewhere in the datasheet (or often printed on the cell itself, in the case of rechargeables), you may find a capacity in mAh (milliamp-hours).

![](https://cdn-learn.adafruit.com/assets/assets/000/001/374/medium800/leds_fuel.png?1396771579)

LED current use is measured in milliamps (mA). As a rule of thumb, we usually use&nbsp; **20 mA** &nbsp;as a guideline for a single LED at full brightness, and each color&nbsp;“pixel” contains three LEDs (one each for red, green and blue), for a total of&nbsp; **60 mA per pixel** &nbsp;when displaying white at full brightness. If we leave that pixel on in that state for one hour, we’ve used 60 milliamp-hours (60 mA&nbsp;×&nbsp;1 hour = 60 mAh). If the stated battery capacity is 2100 mAh, we could expect to run that one pixel for about 35 hours continuously before the battery peters out (2100 mAh&nbsp;÷&nbsp;60 mA = 35 hours).

![](https://cdn-learn.adafruit.com/assets/assets/000/001/375/medium800/leds_mAh.png?1396771595)

But single pixels are seldom left on at full brightness for hours. Usually there’s some combination of brightness levels being mixed, some number of pixels are off entirely, and these states may change many times per second. **That’s why we just use reasonable estimates** , as in “On average, running this code,&nbsp;I think there’s about ten pixels on at any given time, and the average color mix represents a brightness level of 75%.” Starting with the “60 mA per pixel” rule of thumb: 60 mA&nbsp;×&nbsp;0.75 = 45 mA average per pixel. 45 mA&nbsp;×&nbsp;10 pixels = 450 mA. Left to run continuously, with a 2100 mAh battery pack, 2100 mAh&nbsp;÷&nbsp;450 mA = 4.66 hours.  
  
Complicating matters further, the LED driver chips themselves use a tiny bit of current, even when the LEDs themselves are “off.” Each chip needs about 2 mA extra…for a strand of 25, it’s using about 50 mA just in this idle state. You may want to factor this into your estimation. Oh, and we forgot to mention power use for the microcontroller that’s driving all this…about 25 mA or so for an Arduino. So we’ll add about 75 mA to the above estimate: 2100 mAh&nbsp;÷&nbsp;525 mA = 4 hours.  
  
If you have a really nice multimeter with an average current recording mode, it will be your new best friend, because it’s doing this based on actual readings. But this capability is usually present only in high-end meters.  
  
You may also want to add some “engineering overhead” to your estimate. Remember what was said about battery capacity often being idealized. So we’ll de-rate the battery by a bit, let’s assume reality is about 80% of the stated capacity: 2100 mAh&nbsp;×&nbsp;0.8 = 1680 mAh. 1680 mAh&nbsp;÷&nbsp;525 mA = 3.2 hours.  
  
As you can see, there’s an awful&nbsp;lot of fudging and speculation in this process.&nbsp;This is why we say it’s easiest sometimes just to plug in some batteries and keep an eye on it!

- [Previous Page](https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/powering-the-microcontroller-too.md)
- [Next Page](https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/tips-for-larger-projects.md)

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
- [NeoPixel GoPro Lens Light](https://learn.adafruit.com/neopixel-gopro-lens-light.md)
- [FancyLED Library for CircuitPython](https://learn.adafruit.com/fancyled-library-for-circuitpython.md)
- [Infinity Mirror Valentine's Candy Box](https://learn.adafruit.com/infinity-mirror-candy-box.md)
- [Circuit Playground Seashell Pendant](https://learn.adafruit.com/circuit-playground-seashell-pendant.md)
- [NYE Circuit Playground Drop](https://learn.adafruit.com/nye-circuit-playground-drop.md)
- [Feather Scorpio Snap Fit Case](https://learn.adafruit.com/feather-scorpio-snap-fit-case.md)
- [LED Noodle Lantern](https://learn.adafruit.com/led-noodle-lantern.md)
- [GitHub Actions Status Tower Light](https://learn.adafruit.com/github-actions-status-tower-light.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [Light Up Prop with Prop-Maker](https://learn.adafruit.com/prop-maker-light-wand.md)
- [ISS Pin](https://learn.adafruit.com/iss-pin.md)
- [Flapping Halloween Vampire Bat](https://learn.adafruit.com/flapping-halloween-vampire-bat.md)
- [PyPortal Philips Hue Lighting Controller](https://learn.adafruit.com/pyportal-philips-hue-lighting-controller.md)
- [Adafruit Sparkle Motion Stick](https://learn.adafruit.com/adafruit-sparkle-motion-stick.md)
- [Computer Perfection Synthesizer](https://learn.adafruit.com/computer-perfection-synthesizer.md)
