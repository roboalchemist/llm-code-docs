# Source: https://learn.adafruit.com/20mm-led-pixels.md

# 20mm LED Pixels

## Overview

Info: 

RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each pixel contains an RGB LED and a controller chip molded into a 'dot' of silicone, with flanges so they can be pushed into holes in thin sheet material. The dots are waterproof and rugged — they're typically used to make outdoor signs.

**Basic stats**

- 20mm diameter round waterproof pixels
- Approximately 3 inches (75mm) apart on 4-pin strand
- 5 Volts DC, 60 milliamps max per pixel (all LEDs on, full white)
- LPD6803 LED driver chip provides 15-bit color:&nbsp;[Datasheet](http://www.adafruit.com/datasheets/LPD6803.pdf)
- 2-pin SPI-like protocol — easy for Arduino and other microcontrollers

Here is a video showing our similar 12mm dots running a test pattern:

http://www.flickr.com/photos/adafruit/5262163094/

These pixels use a "5050" clear RGB LED and are brighter than our 12mm pixels. The trade off is that they are not diffused, so the color mixing is not as nice; close up, you can see the three separate LEDs. At 5 Volts, they draw a maximum of 60 mA per pixel: 20mA each for red, green and blue.![](https://cdn-learn.adafruit.com/assets/assets/000/001/126/medium800/led_pixels_20mmpixels.jpg?1396769027)

The LED pixels are spaced along a strand of ribbon cable, with about 3 inches or 75mm between pixels. If additional distance is needed you can cut the ribbon cable and solder 4 wires to extend the gap to the desired length.![](https://cdn-learn.adafruit.com/assets/assets/000/001/127/medium800/led_pixels_20mmwires.jpg?1396769033)

Each pixel contains a small microchip within the silicone dot. The LPD6803 LED driver chip is custom designed for this purpose. These chips are very simple to communicate with — all they do is shift color data in from one pin and out another. To issue data from a microcontroller such as an Arduino, one "shifts out" 16 bits of color information. To write data to 10 LEDs, you would issue 160 bits (10 \* 16). Following the data, 32 zero bits will "latch" the data and show the new LED colors.

This chip can handle PWM for controlling color brightness, all it needs is a 'pixel PWM clock' which sets the PWM speed. The faster the clock, the smoother the color…but this signal has to travel all the way down the strand, so it can't be too fast or it'll snag the chips.

An interesting point is that the PWM clock is the same as the data clock. This is nice in that it saves a pin, but does mean that data must be carefully synchronized to the PWM counter in order to avoid unsightly flicker. This is okay but a little annoying because the PWM clock must be continuously issued, and on the Arduino this requires a timer interrupt and costs a fair chunk of CPU performance. We provide an Arduino library that takes care of all&nbsp;this unpleasantness behind the scenes, so you won’t have to fuss with the details.

- [Next Page](https://learn.adafruit.com/20mm-led-pixels/wiring.md)

## Featured Products

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

## Related Guides

- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [How to Choose a Microcontroller](https://learn.adafruit.com/how-to-choose-a-microcontroller.md)
- [Circuit Playground: D is for Diode](https://learn.adafruit.com/circuit-playground-d-is-for-diode.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [Sending an SMS with Temboo](https://learn.adafruit.com/sending-an-sms-with-temboo.md)
- [Arduino "Hunt The Wumpus"](https://learn.adafruit.com/arduino-hunt-the-wumpus.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [2.8" TFT Touch Shield](https://learn.adafruit.com/2-8-tft-touch-shield.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Arduino Lesson 15. DC Motor Reversing](https://learn.adafruit.com/adafruit-arduino-lesson-15-dc-motor-reversing.md)
- [Arduino Lesson 6. Digital Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs.md)
- [Skill Badge Requirements: Microcontrollers](https://learn.adafruit.com/skill-badge-requirements-microcontrollers.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
