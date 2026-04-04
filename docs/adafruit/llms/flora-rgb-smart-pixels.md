# Source: https://learn.adafruit.com/flora-rgb-smart-pixels.md

# Sewable NeoPixels

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/027/390/medium800/led_pixels_flora_collin_tie_full.jpg?1440527634)

What's a wearable project without LEDs? These tiny smart pixels are our favorite thing. Designed specifically for wearables, [we found the brightest RGB LEDs available (an eye-blistering ~3800mcd)](http://adafruit.com/products/1260 "Link: http://adafruit.com/products/619") and paired them with a constant-current driver chip. The contacts are easily sewn with conductive thread. Use this guide to test your first pixel and start on a blinding wearables project with Circuit Playground Express, FLORA or GEMMA!

_Pictured above:&nbsp;[LED Ampli-Tie](../../../led-ampli-tie)_

![](https://cdn-learn.adafruit.com/assets/assets/000/027/391/medium800/led_pixels_1260-00.jpg?1440527669)

## Prerequisite guides

Before you begin, familiarize yourself with&nbsp;the following tutorials:

- [Adafruit Circuit Playground Express](https://learn.adafruit.com/adafruit-circuit-playground-express)
- [Getting Started with FLORA](../../../../getting-started-with-flora)
- [Introducing GEMMA](../../../../introducing-gemma)
- [NeoPixel Uberguide](../../../../adafruit-neopixel-uberguide)
- [Conductive Thread](../../../../conductive-thread)

## Lots of Pixels?

Each pixel draws as much as 60mA (all three RGB LEDs on for full brightness white). In theory, FLORA&nbsp;can drive up to 500 pixels at 30 FPS (above which it will&nbsp;run out of RAM). Circuit Playground Express can drive more than that.&nbsp; However, above&nbsp;about 20 pixels (and/or if the overall length of conductive thread exceeds ~6 feet/2 meters), the nontrivial resistance of the thread adds up and can affect the power supply. For large quantities of pixels over 20 or if you need to insulate your circuit, you should upgrade to [silicone coated&nbsp;stranded core wire](https://www.adafruit.com/search?q=silicone+cover+wire&b=1),&nbsp;which will&nbsp;provide better conductivity&nbsp;for the pixels - the current draw will add up fast!

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/544/medium800/flora_1060insitu_LRG.jpg?1396784270)

_Pictured above: a FLORA prototype with v1 pixels_

- [Next Page](https://learn.adafruit.com/flora-rgb-smart-pixels/hook-up-alligator-clips.md)

## Featured Products

### Flora RGB Smart NeoPixel version 3 - Pack of 4

[Flora RGB Smart NeoPixel version 3 - Pack of 4](https://www.adafruit.com/product/1260)
What's a wearable project without LEDs? Our favorite part of the Flora platform is these tiny smart pixels. Designed specifically for wearables, these updated Flora NeoPixels have ultra-cool technology: these ultra-bright LEDs have a constant-current driver cooked right into the LED...

In Stock
[Buy Now](https://www.adafruit.com/product/1260)
[Related Guides to the Product](https://learn.adafruit.com/products/1260/guides)
### Flora RGB Smart NeoPixel version 3 - Sheet of 20

[Flora RGB Smart NeoPixel version 3 - Sheet of 20](https://www.adafruit.com/product/1559)
So, you want lots and lots of NeoPixels? And you want them for less? Not a problem! Here's a sheet of Flora NeoPixels fresh from the (reflow) oven. Cut them off as you need 'em and save a pretty penny while you're at it.  
  
**Each order comes with 20 pixels on a...**

In Stock
[Buy Now](https://www.adafruit.com/product/1559)
[Related Guides to the Product](https://learn.adafruit.com/products/1559/guides)
### Circuit Playground Express

[Circuit Playground Express](https://www.adafruit.com/product/3333)
 **Circuit Playground Express** is the next step towards a perfect introduction to electronics and programming. We've taken the original Circuit Playground Classic and made it even better! Not only did we pack even more sensors in, we also made it even easier to...

In Stock
[Buy Now](https://www.adafruit.com/product/3333)
[Related Guides to the Product](https://learn.adafruit.com/products/3333/guides)
### Adafruit GEMMA M0 - Miniature wearable electronic platform

[Adafruit GEMMA M0 - Miniature wearable electronic platform](https://www.adafruit.com/product/3501)
The **Adafruit Gemma M0** is a super small microcontroller board, with just enough built-in to create many simple projects. It may look small and cute: round, about the size of a quarter, with friendly alligator-clip sew pads. But do not be fooled! The Gemma M0 is incredibly...

In Stock
[Buy Now](https://www.adafruit.com/product/3501)
[Related Guides to the Product](https://learn.adafruit.com/products/3501/guides)
### FLORA - Wearable electronic platform: Arduino-compatible

[FLORA - Wearable electronic platform: Arduino-compatible](https://www.adafruit.com/product/659)
FLORA is Adafruit's fully-featured wearable electronics platform. It's a round, sewable, Arduino-compatible microcontroller designed to empower amazing wearables projects.FLORA comes with Adafruit's support, [tutorials and...](http://learn.adafruit.com/category/flora)

In Stock
[Buy Now](https://www.adafruit.com/product/659)
[Related Guides to the Product](https://learn.adafruit.com/products/659/guides)
### Small Alligator Clip Test Lead (set of 12)

[Small Alligator Clip Test Lead (set of 12)](https://www.adafruit.com/product/1008)
Connect this to that without soldering using these handy mini alligator clip test leads. 15" cables with alligator clip on each end, color coded. You get 12 pieces in 6 colors. Strong and grippy, these always come in handy! We often use these in conjunction with a multimeter so we...

In Stock
[Buy Now](https://www.adafruit.com/product/1008)
[Related Guides to the Product](https://learn.adafruit.com/products/1008/guides)
### Short Wire Alligator Clip Test Lead (set of 12)

[Short Wire Alligator Clip Test Lead (set of 12)](https://www.adafruit.com/product/1592)
Connect this to that without soldering using these handy mini alligator clip test leads. Approximately 4.5" overall cables with alligator clip on each end, color coded. You get 12 pieces in 6 colors. Strong and grippy, these always come in handy! We often use these in conjunction with a...

In Stock
[Buy Now](https://www.adafruit.com/product/1592)
[Related Guides to the Product](https://learn.adafruit.com/products/1592/guides)
### Stainless Thin Conductive Thread - 2 ply - 23 meter/76 ft

[Stainless Thin Conductive Thread - 2 ply - 23 meter/76 ft](https://www.adafruit.com/product/640)
After months of searching, we finally have what we consider to be the ultimate conductive thread. It's thin, strong, smooth, and made completely of 316L stainless steel. Once you start working with this thread you'll quickly agree its optimal for any wearables work!  
  
This...

In Stock
[Buy Now](https://www.adafruit.com/product/640)
[Related Guides to the Product](https://learn.adafruit.com/products/640/guides)

## Related Guides

- [Adafruit Circuit Playground Express](https://learn.adafruit.com/adafruit-circuit-playground-express.md)
- [Plush Game Controller](https://learn.adafruit.com/plush-game-controller.md)
- [Twinkling Neopixel Parasol](https://learn.adafruit.com/twinkling-led-parasol.md)
- [NYE Circuit Playground Drop](https://learn.adafruit.com/nye-circuit-playground-drop.md)
- [Mason Jar Snow Globe](https://learn.adafruit.com/snow-globe-makecode.md)
- [FLORA and GEMMA ICSP](https://learn.adafruit.com/flora-and-gemma-isp.md)
- [Crickit Powered Dancin' Snowman!](https://learn.adafruit.com/crickit-powered-dancin-snowman.md)
- [Circuit Playground Express Spooky Laughing Box](https://learn.adafruit.com/spooky-circuit-playground-express-mystery-box.md)
- [GEMMA Hoop Earrings](https://learn.adafruit.com/gemma-hoop-earrings.md)
- [LEGO Compatible Crickit Rover](https://learn.adafruit.com/lego-compatible-crickit-rover.md)
- [Debugging the SAMD21 with GDB](https://learn.adafruit.com/debugging-the-samd21-with-gdb.md)
- [3D Printed LED Fire Horns](https://learn.adafruit.com/3d-printed-led-fire-horns.md)
- [PianoGlove](https://learn.adafruit.com/pianoglove.md)
- [Circuit Playground Express Serial Communications](https://learn.adafruit.com/circuit-playground-express-serial-communications.md)
- [Motion Gift Box](https://learn.adafruit.com/motion-gift-box.md)
- [Kaleidoscope Eyes (Trinket-Powered NeoPixel LED Ring Goggles)](https://learn.adafruit.com/kaleidoscope-eyes-neopixel-led-goggles-trinket-gemma.md)
