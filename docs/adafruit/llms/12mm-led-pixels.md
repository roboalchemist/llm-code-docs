# Source: https://learn.adafruit.com/12mm-led-pixels.md

# 12mm LED Pixels

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/001/021/medium800/led_pixels_title.jpg?1396768160)

RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each pixel contains an RGB LED and a controller chip molded into a 'dot' of silicone, with flanges so they can be pushed into holes in thin sheet material. The dots are waterproof and rugged — they're typically used to make outdoor signs.  

![](https://cdn-learn.adafruit.com/assets/assets/000/083/629/medium800/led_pixels_738-00.jpg?1572990308)

12mm RGB pixels come in two different shapes: “bullet” (thin) and “square” (flat). Both use the same type of LED, driver chip and data protocols…the main difference is how they can be mounted: bullets fit better into narrow spaces, while squares are better suited to shallow spaces.

![](https://cdn-learn.adafruit.com/assets/assets/000/083/630/medium800/led_pixels_322-00.jpg?1572990332)

Both types use an 8mm diffused RGB LED (“12mm” refers to the size of the mounting hole for installation)&nbsp;— diffused pixels mix colors nicer. At **5 volts** , they draw a maximum of **60 milliamps** per pixel: 20 mA each for red, green and blue.  
  
The LED pixels are spaced along a strand of ribbon cable, with about **3 inches (75mm)** between pixels. If additional distance is needed you can cut the ribbon cable and solder 4 wires to extend the gap to the desired length.

![](https://cdn-learn.adafruit.com/assets/assets/000/083/631/medium800/led_pixels_738-01.jpg?1572990390)

Each pixel contains a small microchip within the silicone dot. The WS2801 LED driver chip is custom designed for this purpose. We provide an Arduino library for communicating with the pixels (explained in subsequent pages), but if you want to write your own code for other microcontrollers, they’re very easy to communicate with using an SPI-like protocol. For each pixel, one “shifts out” 24 bits of color information — the first data out corresponds to the pixel closest to the microcontroller. To write colors to 10 LEDs, you would issue 240 bits (10 \* 24). Following the data, a 500 microsecond pause will then “latch” the data and display the new LED colors.

![](https://cdn-learn.adafruit.com/assets/assets/000/083/632/medium800/led_pixels_322-02.jpg?1572990409)

- [Next Page](https://learn.adafruit.com/12mm-led-pixels/project-ideas.md)

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
