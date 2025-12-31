# Source: https://learn.adafruit.com/rgb-led-strips/usage.md

# RGB LED Strips

## Usage

Because these LED strips are very simple, we can easily use them with any microcontroller. We suggest&nbsp;using PWM dimming techniques to control the strip. Since each 'LED' pin may end up requiring an Amp or more to sink to ground, power transistors are **required**! Don't try to connect the pins directly to your everyday microcontroller, they will burn out and/or not work.  
  
You can use any power NPN or N-Channel MOSFET, make sure the transistor is rated to be able to pass as much current as you need. For example, since we draw about 0.2Amps per channel per meter, if you have a 5 meter strip you will need to pass up to 1 Ampere per transistor. Get the beefy "TO-220" packages, not the dinky little guys. Make sure they look like this:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/691/medium800/led_strips_7805_t.jpg?1396785811)

For basic, low-cost usage we suggest using [N-channel MOSFETs](http://www.adafruit.com/partfinder/transistors#mosfet) such as the [IRLB8721](https://www.adafruit.com/product/355) - they are very popular and inexpensive and work with 3.3V or 5V logic. If you can't get those, [TIP120](https://www.adafruit.com/products/976) are also good but there is more voltage loss in a transistor than in a MOSFET which is why we suggest those first (less heat loss, more light!)  
  
This diagram shows connecting up with N-Channel MOSFETs where the Gate is pin 1, the Drain is pin 2 and the Source is pin 3  
  
The **IRLB8721**'s can handle up to **16 Amps** of continuous current - so that's at least 750 LEDs, and if you don't have them all on bright white, 1500 LEDs. You may need to heat sink depending on the continuous/overall power draw/dissipation

Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/692/medium800/led_strips_ledstripfet.gif?1448059609)

This diagram shows connecting up with power NPN transistors such as TIP120, where Base is pin 1, Collector is pin 2 and Emitter is pin 3. Its very similar except this time we have 100-220 ohm resistors between the PWM output pin and the base.Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/693/medium800/led_strips_ledstripbjt.gif?1448059603)

Connect a 9-12V power supply to the Arduino so that **Vin** supplies the high voltage to the LED strip. If you want, you can also just use a separate wire that connects to a power supply that provides about +12V. Make sure to connect the ground of that supply to the ground of the Arduino/MOSFETs!  
  
TIP120's can handle up to **5 Amps** of continuous current - so that's at least 250 LEDs, and if you don't have them all on bright white, 500 LEDs.

- [Previous Page](https://learn.adafruit.com/rgb-led-strips/wiring.md)
- [Next Page](https://learn.adafruit.com/rgb-led-strips/arduino-code.md)

## Featured Products

### Flexible RGB Neon-like LED Strip 120 LEDs - 1 meter long

[Flexible RGB Neon-like LED Strip 120 LEDs - 1 meter long](https://www.adafruit.com/product/4245)
Here at Adafruit we love discovering new and exotic glowing things. Like moths to the flame, we were intrigued by these fresh&nbsp; **Flexible Silicone Neon-Like LED Strips**! They _look_ a lot like neon, but without the need for expensive transformers, glass tubing or inert...

In Stock
[Buy Now](https://www.adafruit.com/product/4245)
[Related Guides to the Product](https://learn.adafruit.com/products/4245/guides)
### RGB LED weatherproof flexi-strip - 30 LED/m - 5m

[RGB LED weatherproof flexi-strip - 30 LED/m - 5m](https://www.adafruit.com/product/285)
These LED strips are fun and glowy. There are **30** RGB LEDs per meter, and you can control the entire strip at once with any microcontroller and three transistors. The way they are wired, you will need a 9-12VDC power supply and then ground the R/G/B pins to turn on the three colors. Use...

In Stock
[Buy Now](https://www.adafruit.com/product/285)
[Related Guides to the Product](https://learn.adafruit.com/products/285/guides)
### RGB LED Weatherproof flexi-strip 60 LED/m- 5m

[RGB LED Weatherproof flexi-strip 60 LED/m- 5m](https://www.adafruit.com/product/346)
These LED strips are fun and glowy. There are **60** RGB LEDs per meter - twice as many as our other strip, and you can control the entire strip at once with any microcontroller and three transistors. The way they are wired, you will need a 9-12VDC power supply and then ground the R/G/B...

In Stock
[Buy Now](https://www.adafruit.com/product/346)
[Related Guides to the Product](https://learn.adafruit.com/products/346/guides)
### Analog RGBW LED Strip - RGB plus Cool White - 60 LED/m

[Analog RGBW LED Strip - RGB plus Cool White - 60 LED/m](https://www.adafruit.com/product/2440)
_A dream come true...an analog&nbsp;LED strip with both RGB and Cool White LEDs...It's so........bbbeeeaaaaauuuttttiiiifuuulllll!!!_

These LED strips are fun and glowy. There are **60** RGB and Cool White LEDs per meter - you can control the entire strip at once with any...

In Stock
[Buy Now](https://www.adafruit.com/product/2440)
[Related Guides to the Product](https://learn.adafruit.com/products/2440/guides)
### Analog RGBW LED Strip - RGB plus Warm White - 60 LED/m

[Analog RGBW LED Strip - RGB plus Warm White - 60 LED/m](https://www.adafruit.com/product/2439)
_A dream come true...an analog&nbsp;LED strip with both RGB and Warm White LEDs...It's so........bbbeeeaaaaauuuttttiiiifuuulllll!!!_

These LED strips are fun and glowy. There are **60** RGB and Warm White LEDs per meter - you can control the entire strip at once...

In Stock
[Buy Now](https://www.adafruit.com/product/2439)
[Related Guides to the Product](https://learn.adafruit.com/products/2439/guides)
### Solderless DotStar and Analog RGB LED Strip Clip Sampler

[Solderless DotStar and Analog RGB LED Strip Clip Sampler](https://www.adafruit.com/product/1004)
These ingenious little clips make it easier than ever to use our analog RGB LED strips - no need to solder! The clips snap onto the ends of the LED strip and hold securely. They're not waterproof but you could cover them in heat-shrink to make them weatherproof.  
  
You get one...

In Stock
[Buy Now](https://www.adafruit.com/product/1004)
[Related Guides to the Product](https://learn.adafruit.com/products/1004/guides)
### TIP120 Power Darlington Transistors - 3 pack

[TIP120 Power Darlington Transistors - 3 pack](https://www.adafruit.com/product/976)
Transistors are powerful little electronic switches, and when our little NPN transistors aren't power enough for your project, we have been known to use these beefy TIP120 Darlington transistors. Great for whenever you need to control medium to high-power electronics such as motors,...

In Stock
[Buy Now](https://www.adafruit.com/product/976)
[Related Guides to the Product](https://learn.adafruit.com/products/976/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [Wakanda Forever Game](https://learn.adafruit.com/wakanda-forever-game.md)
- [NeoPixel Cyber Falls Wig](https://learn.adafruit.com/neopixel-cyber-falls.md)
- [Halloween Skeleton Transformation Illusion Prop](https://learn.adafruit.com/halloween-skeleton-transformation-illusion-prop.md)
- [Alohamora Bottle](https://learn.adafruit.com/alohamora-bottle.md)
- [NeoPixel Aquarium with Submersible Lights](https://learn.adafruit.com/neopixel-aquarium-with-submersible-lights.md)
- [Adafruit Sparkle Motion](https://learn.adafruit.com/adafruit-sparkle-motion.md)
- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Cosplay Glow Fur Raver Bandolier](https://learn.adafruit.com/cosplay-glow-fur-raver-bandolier.md)
- [Make it Glow: NeoPixel and LED Diffusion Tips & Tricks](https://learn.adafruit.com/make-it-glow-neopixel-and-led-diffusion-tips-tricks.md)
- [LIGHTSHIP: LED Animation over WiFi](https://learn.adafruit.com/lightship-led-animation-over-wifi.md)
- [DRAFT PUNK](https://learn.adafruit.com/draft-punk.md)
- [NeoPixel LED Heart Necklace](https://learn.adafruit.com/neopixel-led-heart-necklace.md)
- [Stick Person Costume with Neon LED Strips](https://learn.adafruit.com/led-neon-stick-person-costume.md)
- [FunHouse Parking Assistant](https://learn.adafruit.com/funhouse-parking-assistant.md)
- [Sparkle Motion Dance Shoes](https://learn.adafruit.com/sparkle-motion-dance-shoes.md)
