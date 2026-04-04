# Source: https://learn.adafruit.com/hl1606-led-strip/advanced-usage.md

# HL1606 LED Strip

## Advanced Usage

Now that you have the basics down, we can get a little more complicated. The really fun part about color LEDs is not just having 8 primary colors but having hundreds or thousands of colors! Again, as we said before, the HL1606 is a rather stupid chip, it is just a shift register. It doesn't really have a PWM system built in which is why it is so low power and low cost. However, we can coax it into display many colors by writing data to the strip&nbsp;_really fast_. This will PWM the entire strip and will create a blended color effect.

The trade off with the added color-space is that we need to use an interrupt (we use timer #2) to refresh the strip constantly and that the arduino has to do a bunch of crunching in the background.

**Pro:** &nbsp;Hundreds/thousands of colors!&nbsp;  
**Con:&nbsp;** Uses timer #2, must use hardware SPI on pins 11, and 13, uses background CPU.

To wire this up, we'll have to make a small change. The clock and data lines must now connect to the hardware SPI pins to be fast enough. On atmega168/328 Arduinos, this means 11 and 13 are used for&nbsp; **Data** &nbsp;and&nbsp; **Clock** &nbsp;output (for the Mega, pins 51 and 52). The&nbsp; **latch pin** &nbsp;(L) can be any pin but pin 10 (Arduino) or 53 (Mega) but it&nbsp; **MUST BE AN OUTPUT!**

![](https://cdn-learn.adafruit.com/assets/assets/000/001/153/medium800/led_strips_pwmwiring.gif?1447976741)

[Now visit our github repository](https://github.com/adafruit/HL1606-LED-Strip-PWM) and click on the **Download ZIP** button near the top left to download a zip of the library and examples. Uncompress the folder, rename it **HL1606stripPWM** and make sure that inside that folder is the cpp and .h files. Then copy it to your Documents/Arduino/Libraries folder. [See our tutorial for more details](http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries "Link: http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries").

Restart the Arduino software. You should see a new **example** folder called **HL1606stripPWM** and inside, an example called **colorswirl**. Upload that sketch to your Arduino. You should see the following:

http://www.flickr.com/photos/adafruit/5388068211/

(Our camera's sensor didn't film the PWMing very well, its not that flickery in person)

This sketch and library is a little more complex than the one before but should be pretty easy to adapt. Change the object instantiation so the first argument is the number of LEDs in the strip.

```
 HL1606stripPWM strip = HL1606stripPWM(32, latchPin); 
```

You can then set the color LED resolution, hardware SPI interface speed and how long you're willing to spend on PWMing the strip:

```
  // You can customize/control the pulse width modulation and color 
  // resolution by setting how many bits of PWM you want per LED
  // For example, 3 bits is 8 different PWM values per LED and 9 bits, 512
  // values for full color. 4 bits is 16 PWM per LED, 12 bit color with
  // 4096 different colors available.
  // Increasing the PWMbits by 1 means you need *TWICE* as much CPU !!!
  // We suggest starting with 3 and tweaking the other variables to get
  // the fastest SPI and maximum CPU. Then try upping this to 4. For short
  // strips (like 1 meter) that are ok with SPIdiv of 16, you can try 5
  strip.setPWMbits(3);
 
  // We use the built-in hardware SPI module. We can change the speed
  // of the module to push data out faster. In theory, HL1606's should work with
  // the SPI divider set to 16 but we found that this makes some strips
  // spaz out. Start with 32 and once it works try reducing it to 16
  // If you're lucky, you can even try 8 
  // Valid divider values are: 2, 4, 8, 16, 32, 64, and 128, dont try others!
  strip.setSPIdivider(32);
 
  // all the hard work of running the strip is done in an interrupt
  // we can configure the interrupt so that we spend more or less
  // time running the strip, letting you do other stuff like sensors
  // or an LED or whatever. Set it between 0 and 100, where 100 means
  // higher quality colorstrip display but no time for anything else.
  strip.setCPUmax(70);    // 70% is what we start at
```

The initial settings are a good place to start. You can then tweak the values as necessary. Although it may seem like 70% CPU is a lot, the vast majority of Arduino projects we have seen use only maybe 10% of the CPU usage, a lot of time is spent waiting for input.

Updating the SPI divider to be lower (faster) is 'free' so do that first. Then you can change the PWMbits as you'd like, and finally the CPU max to get good refresh performance.

- [Previous Page](https://learn.adafruit.com/hl1606-led-strip/basic-usage.md)

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
