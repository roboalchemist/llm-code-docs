# Source: https://learn.adafruit.com/flora-pixel-brooch/add-more-pixels.md

# Source: https://learn.adafruit.com/flora-rgb-smart-pixels/add-more-pixels.md

# Sewable NeoPixels

## Sewing more pixels

https://youtu.be/eGtGoPhjmcc

![](https://cdn-learn.adafruit.com/assets/assets/000/027/379/medium800thumb/led_pixels_gemma-d1-stitching.jpg?1448319641)

The pixels are chainable - so you only need 1 pin/wire to control as many LEDs as you like. They're easy to sew, and the chainable design means no crossed [conductive threads](http://www.adafruit.com/products/641). The output of one pixel connects directly to the input of the next.

To begin sewing, stitch around the data pin of your microcontroller ( **A1** on Circuit Playground, **D1** on GEMMA or Gemma M0 and **D6** on FLORA are ideal&nbsp;because they're right between power and ground), and stitch over to your first pixel.

![](https://cdn-learn.adafruit.com/assets/assets/000/027/380/medium800thumb/led_pixels_gemma-neopixel-input-stitching.jpg?1448319657)

Make sure that each arrow points away from the microcontroller in a line. Stitch around the input pad tightly, even knotting the thread here to form an extra sturdy connection.

![](https://cdn-learn.adafruit.com/assets/assets/000/027/387/medium800thumb/led_pixels_sealing-conductive-thread-knot.jpg?1448319683)

Stitch back to the thread origin and tie the two ends in a square knot. Use clear nail polish to seal this knot and pull the ends tight until it dries. Do not clip the thread tails until&nbsp;later on.

![](https://cdn-learn.adafruit.com/assets/assets/000/027/388/medium800thumb/led_pixels_sewing-ground-bus.jpg?1448319698)

All the positive pads (marked with a **+** ) connect together to form one power bus. Likewise all the negative pads (marked with a **-** ) connect together to form one ground bus.

![](https://cdn-learn.adafruit.com/assets/assets/000/027/383/medium800/led_pixels_gemma-pixels-sewn-in-back.jpg?1440522371)

Here's what a three-pixel circuit looks like from the back. See the individual data connections in the center and the continuous power and ground buses above and below?

![](https://cdn-learn.adafruit.com/assets/assets/000/027/389/medium800thumb/led_pixels_snip-threads-clean-up.jpg?1448319712)

Double check your knots are secure before clipping all your thread tails. Clean up your work space so there aren't any stray bits of conductive thread hanging around.

![](https://cdn-learn.adafruit.com/assets/assets/000/027/376/medium800/led_pixels_gemma-pixels-sewn-in.jpg?1440521603)

Visually inspect your circuit to check for shorts or stray threads.

![](https://cdn-learn.adafruit.com/assets/assets/000/027/393/medium800thumb/led_pixels_three-pixels-glowing.jpg?1448319724)

Plug your microcontroller into your computer with a USB cable. Change the number of pixels in the Arduino sketch or MakeCode project to match the number of pixels in your projects, and make sure the pin number matches what you sewed to.&nbsp; Upload the strandtest sample code as you did when testing a pixel earlier in this guide. Your pixels should light up and animate different colors and patterns.

If they don't all come on or some later in the chain are flickering, your stitches might not be snug enough against the pads of the circuit board. Double check your sewing and reinforce it where necessary (with the circuit off/unplugged).

![](https://cdn-learn.adafruit.com/assets/assets/000/027/378/medium800/led_pixels_gemma-pixels-sewn-in-lit-up.jpg?1440521708)

The library for these pixels is very similar to our [Adafruit\_WS2801](http://learn.adafruit.com/12mm-led-pixels/code "Link: http://learn.adafruit.com/12mm-led-pixels/code")[library for other types of RGB pixels](http://learn.adafruit.com/12mm-led-pixels/code "Link: http://learn.adafruit.com/12mm-led-pixels/code").

- [Previous Page](https://learn.adafruit.com/flora-rgb-smart-pixels/run-pixel-test-code.md)
- [Next Page](https://learn.adafruit.com/flora-rgb-smart-pixels/project-ideas.md)

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
