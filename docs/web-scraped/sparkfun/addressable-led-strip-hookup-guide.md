# Source: https://learn.sparkfun.com/tutorials/addressable-led-strip-hookup-guide

## Light Up Your Life

Nothing looks as festive as a bunch of bright, colorful lights concentrated into a tight space. And for that, I heartily recommend an addressable [LED](https://www.sparkfun.com/leds) strip. It\'s very bright, super vivid, and easy to hookup. This tutorial covers all of the wiring and code necessary to light up a single string of addressable LEDs with just a RedStick and a AA Battery Pack.

[![LED RGB Strip - Addressable, Sealed, 1m (APA104)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/6/3/0/15205-LED_RGB_Strip_-_Addressable__Sealed__1m__APA104_-01.jpg)](https://www.sparkfun.com/led-rgb-strip-addressable-sealed-1m-apa104.html)

### [LED RGB Strip - Addressable, Sealed, 1m (APA104)](https://www.sparkfun.com/led-rgb-strip-addressable-sealed-1m-apa104.html) 

[ COM-15205 ]

These are sealed addressable 1 meter long 5V RGB LED strips that come packed with 60 APA104s per meter.

[ [\$35.50] ]

### Covered in This Tutorial

### Required Materials

To follow along with this tutorial, you will need the following parts:

You will also need to following tools:

- [Soldering tools](https://www.sparkfun.com/categories/49), including an [iron](https://www.sparkfun.com/products/9507) and [solder](https://www.sparkfun.com/products/9325)
- [Wire Strippers](https://www.sparkfun.com/products/12630)

### Suggested Reading

If you\'ve never worked with addressable LEDs or with the RedStick, we recommend checking out these other guides first.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/ws2812-breakout-hookup-guide)

### WS2812 Breakout Hookup Guide 

How to create a pixel string with the WS2812 and WS2812B addressable LEDs!

[](https://learn.sparkfun.com/tutorials/redstick-hookup-guide)

### RedStick Hookup Guide 

Learn about the SparkFun RedStick, a USB thumb drive-sized Arduino-compatible development platform.

[](https://learn.sparkfun.com/tutorials/mean-well-led-switching-power-supply-hookup-guide)

### Mean Well LED Switching Power Supply Hookup Guide 

In this tutorial, we will be connecting a Mean Well LED switching power supply to an addressable LED strip controlled by an Arduino.

## Hardware Assembly 

For the purposes of this tutorial, I\'m going to assume that you have some very basic soldering experience. There are only a handful of connections that you\'ll need to solder, so this isn\'t a bad project to start with However, if you *are* using this as your introduction to soldering, we strongly suggest reading [this tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) first.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

Addressable LED strips, like the one in this tutorial, tend to use a standardized 3-pin connector. This makes it easy to chain multiple LED strips together. Because the battery pack included with this project is not going to support a lot more than the 60 included LEDs, you may find it convenient to cut the female connector off the \"out\" end of the strip and solder it to the RedStick to make your LEDs detachable.

**Warning:** \*\*Make sure you\'re cutting the right connector!\*\* Look at the little black arrows on the LED strip. You want the connector with the arrow pointing \*toward\* it.

[![arrow](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/1/arrow.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/1/arrow.jpg)

The diagram below illustrates the handful of connections that you\'ll need to make. You\'ll notice that the red and yellow wires from the LED strip are connected directly to the battery connector. You may be tempted to connect them to the GND and VCC pins on the RedStick, but **don\'t do that.** The VCC pin draws current through the on-board voltage regulator, which isn\'t rated for the high current that the LEDs require to operate. If powered from VCC, the regulator will definitely get hot and may fail altogether.

[![diagram illustrating proper wiring connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/1/g935xy.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/1/g935xy.png)

*Click image for a closer look*

## Example Code

Once your LED strip is wired up, you can load some Arduino code onto the RedStick to animate the lights! For our example code, we\'ll be making use of Adafruit\'s fantastic [NeoPixel library](https://github.com/adafruit/Adafruit_NeoPixel).

Click [here](https://cdn.sparkfun.com/assets/0/4/a/f/8/51f1806cce395fcd20000004.zip) to download a copy of both the example code, as well as the NeoPixel library. The library is located in the \"Adafruit_NeoPixel\" folder, and the example code is found in the \"WS2812_Breakout_Example\" folder.

You\'ll need to **install the library**. For help there, check out our [installing Arduino libraries](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) tutorial.

We\'ve broken down the example code into a few separate sketches that each have a fun animation. We\'ve taken the liberty of cooking up a few special addition animations as well:

## Rainbow Cycle

This one is my favorite of the NeoPixel example animations. It scrolls through the entire rainbow of colors while evenly distributing the color spectrum across the LED strip.

    language:c
    #include <Adafruit_NeoPixel.h>
    #ifdef __AVR__
      #include <avr/power.h>
    #endif

    #define PIN 2

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, PIN, NEO_GRB + NEO_KHZ800);

    void setup() 

    void loop() 

    void rainbowCycle(uint8_t wait) 
        strip.show();
        delay(wait);
      }
    }

    // Input a value 0 to 255 to get a color value.
    // The colours are a transition r - g - b - back to r.
    uint32_t Wheel(byte WheelPos) 
      if(WheelPos < 170) 
      WheelPos -= 170;
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    }

## Candy Chase

This is a little animation that I worked up based on the \"Theater Chase\" animation included in the NeoPixel example code. It creates a crawling lights effect in red on a white background, like an animated candy cane!

    language:c
    #include <Adafruit_NeoPixel.h>
    #ifdef __AVR__
      #include <avr/power.h>
    #endif

    #define PIN 2

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, PIN, NEO_GRB + NEO_KHZ800);

    void setup() 

    void loop() 

    void candyChase(uint8_t wait) 
          for (uint16_t i=0; i < strip.numPixels(); i=i+3) 
          strip.show();

          delay(wait);

          for (uint16_t i=0; i < strip.numPixels(); i=i+3) 
        }
      }
    }

## Snowflakes

This animation creates an array of randomly twinkling white pixels reminiscent of snowfall.

    language:c
    #include <Adafruit_NeoPixel.h>
    #ifdef __AVR__
      #include <avr/power.h>
    #endif

    #define PIN 2

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, PIN, NEO_GRB + NEO_KHZ800);

    void setup() 

    void loop() 

    void snowflakes(uint8_t wait) 

    // Run some snowflake cycles
    for (int j=0; j<200; j++) 

    // Dim all pixels by 10
    for(int p=0; p<60; p++)
       strip.show();
       delay(wait);
    }

    }

## Iceflakes

Not a real thing, I know\... It\'s \"Snowflakes\" but blue instead of white.

    language:c
    #include <Adafruit_NeoPixel.h>
    #ifdef __AVR__
      #include <avr/power.h>
    #endif

    #define PIN 2

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, PIN, NEO_GRB + NEO_KHZ800);

    void setup() 

    void loop() 

    void iceflakes(uint8_t wait) 

    // Run some snowflake cycles
    for (int j=0; j<200; j++) 

    // Dim all pixels by 10
    for(int p=0; p<60; p++)
       strip.show();
       delay(wait);
    }

    }

## Extending Battery Life

The 60 LEDs on your addressable LED strip can drain a lot of batteries really fast. At full brightness, the strip will pull over 2 amps!! With a capacity of only 1.5 amp-hours, the AA batteries will only power the strip at full brightness, continuously, for under an hour. If you want to get more bang for your battery-buck, there are a few tricks you can use.

### Cap the Brightness

60 LEDs in a linear meter is *a lot* of LEDs, so running them at full brightness is really\... impressive. And mostly unnecessary. Luckily, the NeoPixel library includes a handy function called `setBrightness();` which limits the brightness of an LED strip. You\'ll notice that the examples in this tutorial all include the line `strip.setBrightness(64);`, which sets the strip brightness to about 25%. You can set it lower before noticing a huge difference in brightness, so play with that number until you find the right balance between brightness and battery life.

### Take a Break

Sometimes a cool lighting effect is more impressive if it *isn\'t* continuous. Try dropping a `delay();` into the main loop so that there\'s some downtime between animation cycles. Obviously, the less time you leave the LEDs on, the longer your batteries will last.

### Cut it Short

Maybe you don\'t *need* 60 LEDs. Maybe 30 would do just fine. You can cut a portion off the end of the strip with a pair of standard craft scissors. Just cut across the copper pads in between the LEDs, and now you have another small strip you could use elsewhere. You can always solder them back together if you change your mind!