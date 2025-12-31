# Source: https://learn.adafruit.com/light-painting-with-raspberry-pi/hardware.md

# Light Painting with Raspberry Pi

## Hardware

Interfacing Adafruit’s [Digital Addressable RGB LED](http://learn.adafruit.com/digital-led-strip) strip (aka “LPD8806 strip”) to the Raspberry Pi is super simple, requiring just a few connections between the board, strip and a [DC power jack](http://adafruit.com/products/368).  
  
The board’s&nbsp;MOSI pin connects to the DI pin on the LED strip, and SCLK connects to the CI pin.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/589/medium800/raspberry_pi_diagram.png?1396774138)

Instead of supplying power to the Raspberry Pi’s&nbsp;Micro USB connector, a&nbsp;5 Volt DC power supply is required because the LED strip&nbsp;draws&nbsp;significantly more current than the USB input can provide.&nbsp;A&nbsp;[2 Amp power supply](http://adafruit.com/products/276)&nbsp;is sufficient for a 1 meter LED strip, while our larger&nbsp;[10 Amp supply](http://adafruit.com/products/658)&nbsp;can power up to 5 meters of LED strip (plus the Raspberry Pi board, in both situations).

+5V and ground from the power supply&nbsp;connect to the 5V and GND pins on both the LED strip&nbsp;<u>and</u>&nbsp;the Raspberry Pi GPIO header.

In the above diagram, we’re directly connecting **3.3V** logic output from the Raspberry Pi to the **5V** logic input of the addressable LED strip. Strictly speaking, this is _not_ Good and Proper. Wildcards like actual power supply voltage (they’re never _precisely_ 5.0000V) or even temperature may contribute to whether this functions reliably. It did very well here, but your mileage may vary. If your LEDs _almost_ work but are glitchy, it’s time for a _logic level shifter_, [explained in this guide](https://learn.adafruit.com/neopixel-levelshifter) (which is about NeoPixels, but the principle is the same — just that we’ve got _two_ wires to level-shift here, rather than NeoPixels’ one).

![](https://cdn-learn.adafruit.com/assets/assets/000/001/669/medium800/raspberry_pi_ID658_LRG.jpg?1396774937)

An initial prototype was assembled using a [Pi Cobbler](http://adafruit.com/products/914) breakout kit. Because the finished project would be moving around a lot, and because breadboards aren’t the most robust thing, a 26-pin IDC cable was sacrificed for science to create a purpose-built cable between the Raspberry Pi GPIO header, LED strip and power supply. This is much more resilient to vibration and careless fingers.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/621/medium800/raspberry_pi_cable.jpg?1396774427)

To make connections easy to make/break for setup and take down, we also used two JST 4-pin inline cables ([plug](http://www.adafruit.com/products/578)and [receptacle](http://www.adafruit.com/products/579))&nbsp;and&nbsp;&nbsp;to attach and detach the LED strip. The connectors are polarized so they can't be plugged backwards!

![](https://cdn-learn.adafruit.com/assets/assets/000/001/634/medium800/raspberry_pi_jstsm4plug_LRG.jpg?1396774579)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/635/medium800/raspberry_pi_jstsm4receptacle_LRG.jpg?1396774588)

- [Previous Page](https://learn.adafruit.com/light-painting-with-raspberry-pi/overview.md)
- [Next Page](https://learn.adafruit.com/light-painting-with-raspberry-pi/software.md)

## Featured Products

### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### Digital RGB LED Weatherproof Strip - LPD8806 32 LED 5m

[Digital RGB LED Weatherproof Strip - LPD8806 32 LED 5m](https://www.adafruit.com/product/306)
These LED strips are fun and glowy. There are 32 RGB LEDs per meter, and you can control each LED individually! Yes, that's right, this is the digitally-addressable type of LED strip. You can set the color of each LED's red, green and blue component with 7-bit PWM precision (so 21-bit...

In Stock
[Buy Now](https://www.adafruit.com/product/306)
[Related Guides to the Product](https://learn.adafruit.com/products/306/guides)
### 4-pin JST SM Plug + Receptacle Cable Set

[4-pin JST SM Plug + Receptacle Cable Set](https://www.adafruit.com/product/578)
These 4-wire cables are 15cm long and come as a set, one side has a JST SM type connector plug on the end. The other side has a matching JST SM type receptacle connector. They are good for whenever you have 4 wires you want to be able to plug and unplug. We like the solid and compact nature of...

In Stock
[Buy Now](https://www.adafruit.com/product/578)
[Related Guides to the Product](https://learn.adafruit.com/products/578/guides)
### 5V 10A switching power supply

[5V 10A switching power supply](https://www.adafruit.com/product/658)
This is a beefy switching supply, for when you need a lot of power! It can supply 5V DC up to 10 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard computer/appliance...

In Stock
[Buy Now](https://www.adafruit.com/product/658)
[Related Guides to the Product](https://learn.adafruit.com/products/658/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### Female DC Power adapter - 2.1mm jack to screw terminal block

[Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
If you need to connect a DC power wall wart to a board that doesn't have a DC jack - this adapter will come in very handy! There is a 2.1mm DC jack on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/368)
[Related Guides to the Product](https://learn.adafruit.com/products/368/guides)

## Related Guides

- [LPD8806 Digital RGB LED Strip](https://learn.adafruit.com/digital-led-strip.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [DotStar Pi Painter](https://learn.adafruit.com/dotstar-pi-painter.md)
- [Web Enabled PIXEL on Raspberry Pi](https://learn.adafruit.com/web-enabled-pixel-on-raspberry-pi.md)
- [Adafruit 16-Channel PWM/Servo HAT & Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi.md)
- [Adafruit Sparkle Motion](https://learn.adafruit.com/adafruit-sparkle-motion.md)
- [CircuitPython on Raspberry Pi (Bare Metal / No OS)](https://learn.adafruit.com/circuitpython-on-raspberry-pi-bare-metal-no-os.md)
- [IoT Moon Phase Guide](https://learn.adafruit.com/moon-phase.md)
- [Make a Zelda Master Sword with the RP2040 Prop-Maker Feather](https://learn.adafruit.com/master-sword-rp2040.md)
- [LED Backpack Displays on Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/led-backpack-displays-on-raspberry-pi-and-beaglebone-black.md)
- [MCP230xx GPIO Expander on the Raspberry Pi](https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi.md)
- [Internet of Things Printer for Raspberry Pi](https://learn.adafruit.com/pi-thermal-printer.md)
- [Adafruit 16x2 Character LCD + Keypad for Raspberry Pi](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi.md)
- [Ultimate Youtube Live Camera](https://learn.adafruit.com/ultimate-youtube-live-camera.md)
- [Adafruit 128x64 OLED Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi.md)
- [Instant Camera using Raspberry Pi and Thermal Printer](https://learn.adafruit.com/instant-camera-using-raspberry-pi-and-thermal-printer.md)
