# Source: https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/powering-the-microcontroller-too.md

# Battery Power for LED Pixels and Strips

## Powering the Microcontroller

The Arduino (or other 5 Volt microcontroller) can be powered off the same supply as the LED strip, by splitting the power leads (_after_ the diode, if used) and connecting to the Arduino’s 5V pin (_not_ Vin) and GND.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/376/medium800/leds_schematic.png?1396771610)

LED strips aren’t picky about which side they receive power from, only data.&nbsp;In a pinch, if the situation really calls for it, you can connect the battery pack (with diode, if used)&nbsp;to the OUT end of the strip, then power the Arduino from the + and – connections on the IN end (along with the serial data and clock signals). This isn’t recommended though, because voltage drops slightly along the length of the strip, and the Arduino (which is supposed to be running everything) will give out sooner as the batteries approach depletion. Powering the Arduino close to the batteries ensures a healthy voltage,&nbsp;to stay&nbsp;in control for as long as possible.

- [Previous Page](https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/diode.md)
- [Next Page](https://learn.adafruit.com/battery-power-for-led-pixels-and-strips/estimating-running-time.md)

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
