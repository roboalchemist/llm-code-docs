# Source: https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/troubleshooting.md

# Source: https://learn.adafruit.com/internet-of-things-printer/troubleshooting.md

# Source: https://learn.adafruit.com/digital-led-strip/troubleshooting.md

# Source: https://learn.adafruit.com/36mm-led-pixels/troubleshooting.md

# Source: https://learn.adafruit.com/20mm-led-pixels/troubleshooting.md

# Source: https://learn.adafruit.com/12mm-led-pixels/troubleshooting.md

# 12mm LED Pixels

## Troubleshooting

### 

It's pretty easy! Simply drill a 12mm hole into any material up to 1.5mm/0.06" thick. Then push the LED bulb first into the hole. It takes a little wiggling but there are four flanges molded in so that you can 'push' them thru and the flanges will keep the LED pixel in place

Many support issues arise&nbsp;from&nbsp;eager users getting ahead of themselves, changing the code and wiring before confirming that all the pieces work in the standard configuration.&nbsp;We recommend always starting out with the examples as shown. Use the pinouts and wiring exactly as in the tutorial, and run the stock, unmodified “strandtest” example sketch. Only then should you start switching things around.  
  
Here are the most common issues and solutions…

### 

- Double-check all wiring. Are the clock and data wires swapped? Is ground connected to the Arduino?
- Confirm the Arduino is connected to the <u>input</u> end of the strand.
- Check power supply polarity and voltage. Are + and – swapped? If you have a multimeter, confirm 5V DC output (±10%) from the power supply.
- Are the power wires at the opposite end of the strand insulated or trimmed? They should not be left exposed where they might make contact with metal, or each other.
- Is the correct board type&nbsp;selected in the Arduino Tools→Board menu?  

### 

The power supply is probably OK. Check for any of the following:

- Double-check all wiring. Are the clock and data wires swapped? Is ground connected to the Arduino?
- Confirm the Arduino is connected to the <u>input</u> end of the strand.
- Is the correct board type&nbsp;selected in the Arduino Tools→Board menu?  
- Did the strandtest code successfully compile and upload?

### 

- Confirm that the number of LEDs in the&nbsp;Adafruit\_WS2801() constructor match the number of LEDs in the strand (both will be 25 if using the strandtest example and a single strand of LEDs).
- Inside each pixel there’s a small circuit board. Give the first bad pixel (and the one immediately&nbsp;before it) a firm squeeze where the ribbon cable joins the board — it may simply be a dodgy connection. If that works, you can either cut out the offending pixel and join the two sub-strands, or arrange for a replacement strand if new.

### 

Are the clock and data wires swapped? Is ground connected to the Arduino?

### 

- This can happen when trying to power too long of a strand from one end. Voltage will drop along the length of the strand and the furthest pixels will “brown out.” Connect power to _every_ 25 pixel strand.

### 

- Confirm the library is <u>unzipped</u> prior to installation.
- Confirm the library is properly named and located. The folder should be called&nbsp;Adafruit\_WS2801, and placed inside your personal&nbsp;Documents/Arduino/Libraries folder — _not_ inside the Arduino application folder!
- After installation, the Arduino IDE needs to be restarted for new libraries to be used.  

- [Previous Page](https://learn.adafruit.com/12mm-led-pixels/circuitpython-usage.md)
- [Next Page](https://learn.adafruit.com/12mm-led-pixels/dimensions.md)

## Featured Products

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
### 5V 10A switching power supply

[5V 10A switching power supply](https://www.adafruit.com/product/658)
This is a beefy switching supply, for when you need a lot of power! It can supply 5V DC up to 10 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard computer/appliance...

Out of Stock
[Buy Now](https://www.adafruit.com/product/658)
[Related Guides to the Product](https://learn.adafruit.com/products/658/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

In Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### Female DC Power adapter - 2.1mm jack to screw terminal block

[Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
If you need to connect a DC power wall wart to a board that doesn't have a DC jack - this adapter will come in very handy! There is a 2.1mm DC jack on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/368)
[Related Guides to the Product](https://learn.adafruit.com/products/368/guides)
### 4-pin JST SM Plug + Receptacle Cable Set

[4-pin JST SM Plug + Receptacle Cable Set](https://www.adafruit.com/product/578)
These 4-wire cables are 15cm long and come as a set, one side has a JST SM type connector plug on the end. The other side has a matching JST SM type receptacle connector. They are good for whenever you have 4 wires you want to be able to plug and unplug. We like the solid and compact nature of...

In Stock
[Buy Now](https://www.adafruit.com/product/578)
[Related Guides to the Product](https://learn.adafruit.com/products/578/guides)

## Related Guides

- [Bluefruit Controlled Macetech RGB LED Shades](https://learn.adafruit.com/ledshades.md)
- [Make it Glow: NeoPixel and LED Diffusion Tips & Tricks](https://learn.adafruit.com/make-it-glow-neopixel-and-led-diffusion-tips-tricks.md)
- [Starduino: 8-Bit Super Mario Tree Topper](https://learn.adafruit.com/starduino-neopixel-8-bit-mario-star-tree-topper.md)
- [NeoPixel Ring Clock](https://learn.adafruit.com/neopixel-ring-clock.md)
- [Star Fragment IoT Lamp](https://learn.adafruit.com/star-fragment-iot-lamp.md)
- [Talking Musical NeoPixel Clock with Infrared, BLE and Touch Controls](https://learn.adafruit.com/talking-musical-neo-pixel-clock-with-infrared-ble-and-touch-controls.md)
- [Perfect Pitch Machine](https://learn.adafruit.com/perfect-pitch-machine.md)
- [CheerLights](https://learn.adafruit.com/cheerlights.md)
- [NeuroDreamer Teardown](https://learn.adafruit.com/neurodreamer-teardown.md)
- [Holiday Lights: Easy DIY Christmas Wreath & Garland with WLED](https://learn.adafruit.com/holiday-garland-decor-app-control-with-no-coding.md)
- [Adafruit IO Home: Security ](https://learn.adafruit.com/adafruit-io-home-security.md)
- [Adafruit NeoPot](https://learn.adafruit.com/adafruit-neopot.md)
- [NeoKey Socket Breakout with NeoPixel for MX and CHOC Key Switches](https://learn.adafruit.com/neokey-breakout.md)
- [NeoPixie Dust Bag](https://learn.adafruit.com/neopixel-pixie-dust-bag.md)
- [Multi-tasking the Arduino - Part 3](https://learn.adafruit.com/multi-tasking-the-arduino-part-3.md)
