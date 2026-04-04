# Source: https://learn.adafruit.com/hl1606-led-strip/basic-usage.md

# HL1606 LED Strip

## Basic Usage

The HL1606 is not a common chip for most people, so the best way to explain it is to say its basically a 74HC595 shift register. Like a '595 there is an SPI input and then there is a shift-output so you can chain them. The HL1606 has 6 outputs and they're specifically for driving LEDs. The most basic way to use them is to set each LED on or off. This means you can have up to 8 primary 'colors' on an LED: red, yellow, green, teal, blue, violet, white and black.

There are some pros and cons to driving the strips this way…&nbsp;  
**Pro:** &nbsp;Very simple, easy and fast. Use any 3 pins, No interrupts or constant updating required.  
**Con:&nbsp;** Only a handful of colors.

Let's get the strip up and running using this method to start.

**The most important thing to remember is that you need a lot of current (power) to drive these strips, so you will need to arrange a 5V power supply. This test will require about 1 Ampere per meter!**

![](https://cdn-learn.adafruit.com/assets/assets/000/001/152/medium800/led_strips_basicwiring.gif?1447976734)

Note in the image above that the 5V can come from a separate power supply that can provide the power you need. Be sure to tie the grounds together and check the polarity…sticking -5V by accident into the strip could be a sad and expensive mistake. We'll be using an Arduino to demonstrate the strip but the code can easily be ported to your favorite microcontroller.

Note that we have **Latch** connected to digital I/O pin #2, **Clock** connected to #3 and **Data** to #4

To install the required library, first, open up the Arduino library manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/084/296/medium800/led_strips_library_manager_menu.png?1573835562)

Search for the&nbsp; **HL1606&nbsp;** library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/297/medium800/led_strips_hl1606.png?1573835713)

We also have a great tutorial on Arduino library installation at:  
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")

You should now see a new **example** folder called **HL1606strip** and inside, an example called **basicPatterns**. Upload that sketch to your Arduino. You should see the following:

http://www.flickr.com/photos/adafruit/5387932657/

You can change how long the strip is by adjusting the object creation (instantiation) line:

```
HL1606strip strip = HL1606strip(STRIP_D, STRIP_L, STRIP_C, 32);
```

The last argument "32" is the number of LEDs to address. Count how many are in your strip! The display may be wonky otherwise

The&nbsp; **basicPatterns** &nbsp;sketch has many examples of how to set the color of each pixel by calling

```
 strip.setLEDcolor(n, color);
```

where&nbsp; **n&nbsp;** indicates which LED you want to change and&nbsp; **color** &nbsp;is&nbsp; **RED, YELLOW, GREEN, TEAL, BLUE, VIOLET, WHITE,&nbsp;** or&nbsp; **BLACK**. After you've set the pixel color, you need to&nbsp; **write** &nbsp;the changes to the strip by calling

```
 strip.writeStrip();
```

**writeStrip()**&nbsp;isnt very fast, it will take a few milliseconds to write the changes and it takes longer the more LEDs there are. So change all the LED's you want at once and then write them!

- [Previous Page](https://learn.adafruit.com/hl1606-led-strip/wiring.md)
- [Next Page](https://learn.adafruit.com/hl1606-led-strip/advanced-usage.md)

## Related Guides

- [Pocket Galaxy](https://learn.adafruit.com/pocket-galaxy.md)
- [Mailbox Notification Service](https://learn.adafruit.com/mailbox-notification-service.md)
- [Digital LED Belt](https://learn.adafruit.com/digital-led-belt.md)
- [Bike Wheel POV Display](https://learn.adafruit.com/bike-wheel-pov-display.md)
- [NeoPixel Bracelet](https://learn.adafruit.com/neopixel-bracelet.md)
- [Magic Band Reader](https://learn.adafruit.com/magic-band-reader.md)
- [HalloWing Light Paintstick](https://learn.adafruit.com/hallowing-light-paintstick.md)
- [Stick Person Costume with Neon LED Strips](https://learn.adafruit.com/led-neon-stick-person-costume.md)
- [Light-Up Reactive Ukulele](https://learn.adafruit.com/light-up-reactive-ukulele.md)
- [Gemma 3D Printed Tree Topper](https://learn.adafruit.com/gemma-3d-printed-tree-topper.md)
- [NeoPixel Infinity Mirror Coaster](https://learn.adafruit.com/infinity-mirror-coaster.md)
- [Halloween Skeleton Transformation Illusion Prop](https://learn.adafruit.com/halloween-skeleton-transformation-illusion-prop.md)
- [Magic Mirror with Glowing Secret Messages](https://learn.adafruit.com/magic-mirror-with-glowing-secret-messages.md)
- [Monster Matrix with WLED](https://learn.adafruit.com/monster-matrix-with-wled.md)
- [Mini Neon Sign Prop & n00ds Booster Case](https://learn.adafruit.com/nood-booster-case.md)
