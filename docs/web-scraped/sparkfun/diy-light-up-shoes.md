# Source: https://learn.sparkfun.com/tutorials/diy-light-up-shoes

## Introduction

These DIY Light-Up Kicks are high top sneakers embedded with a [WS2812 Addressable LED Strip](https://www.sparkfun.com/products/12027) and a [Qduino Mini Microcontroller](https://www.sparkfun.com/products/13614). The [LED](https://www.sparkfun.com/leds)s are easily programmable and re-programmable for countless customizations of color, pattern, and animation. In this tutorial we will go through the step-by-step process of building this project.

[![Light-Up Kicks](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/IMG_7062sm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/IMG_7062sm.jpg)

### Required Materials

To follow along with this guide, you will need the following:

### You Will Also Need:

- High Top Sneakers (Cloth or canvas is preferable to leather)
- [Soldering Iron](https://www.sparkfun.com/products/9507)
- [Solder](https://www.sparkfun.com/products/9163)
- [Wire Cutters](https://www.sparkfun.com/products/11952)
- [Wire Strippers](https://www.sparkfun.com/products/12630)
- Super Glue
- Hot Glue Sticks
- Hot Glue Gun
- White Felt
- Scissors
- Needle and Thread
- Velcro

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/addressable-led-strip-hookup-guide)

### Addressable LED Strip Hookup Guide 

Add blinking lights to any holiday decoration with our Holiday Lights Kit using WS2812-based addressable LEDs!

## Hardware Overview

The two main components that the Light-Up Kicks use are the following:

- Qduino Mini - Arduino Dev Board
- WS2812 Addressable RGB LED Strip

### Qduino Mini

[![Qduino Mini - Arduino Dev Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/9/8/7/13614-01b.jpg)](https://www.sparkfun.com/qduino-mini-arduino-dev-board.html)

### [Qduino Mini - Arduino Dev Board](https://www.sparkfun.com/qduino-mini-arduino-dev-board.html) 

[ DEV-13614 ]

The Qduino Mini is a tiny, Arduino-compatible board with a battery connector and charger built-in as well as a fuel gauge tha...

[ [\$35.95] ]

The brains behind the Light-Up Kicks are a set of Qduino Mini - Arduino Dev Boards, a small Arduino-compatible microcontroller that includes a switch AND a LiPo battery connector.

Qduino Mini Technical Specifications:

  ------------------- ----------------------
  Microcontroller     ATmega32U4
  Operating Voltage   3.3V @ 8MHz
  Digital I/O Pins    19 with 13 dedicated
  Analog Channels     12 with 6 dedicated
  Flash Memory        32 KB
  SRAM                2.5 KB (ATmega32U4)
  EEPROM              1 KB (ATmega32U4)
  Clock Speed         8 MHz
  ------------------- ----------------------

This board also features:

- SPI, I2C, UART available
- Two RGB LEDs built-in - one for: Charge Status, TX, RX, and the other user programmable
- AP2112K 3.3V 600mA Regulator
- MCP73831 LiPo Battery Charger
- MAX17048 LiPo Battery Fuel Gauge

### WS2812 Addressable RGB LED Strip

[![LED RGB Strip - Addressable, Sealed (1m)](https://cdn.sparkfun.com/r/600-600/assets/parts/8/5/5/5/12027.jpg)](https://www.sparkfun.com/products/12027)

### [LED RGB Strip - Addressable, Sealed (1m)](https://www.sparkfun.com/products/12027) 

[ COM-12027 ]

Gone are the days that you have to worry about silicone weather proofing splitting and breaking on you! These are sealed addr...

**Retired**

The WS2812 Addressable LED Strip is a long strip with WS2812 RGB LEDs. Each individual LED is addressable through your microcontroller. They are preterminated with 0.1\" spaced 3-pin connectors as well as a 2 wire power connector. Hooking these LEDs up to a microcontroller can be done by either soldering leads to the connection pads or using the existing wire power connectors. DIN should always connect to a digital pin which will be assigned to the LED strip in your code. VCC and GND can connect to their respective pads on the Qduino Mini. A longer strip might need a more powerful or separate power source than this project requires.

**Note:** It is usually advised to include a small smoothing capacitor in between VCC and GND of your LED strip to protect the first few LEDs from power surges. While it is suggested to use the smoothing capacitor with the addressable LEDs, the LiPo battery provides sufficient power to the addressable LEDs without any fluctuations in current drawn by the LED strip. In this setup, it is not necessary to use a capacitor.

## Software Installation

### Arduino IDE

The Qduino Mini - Arduino Dev Board is programmable via the Arduino IDE. If this is your first time using Arduino, please review our tutorial on installing the Arduino IDE.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### Qduino Drivers and Board Add-On

If this is your first time working with the Qduino, you will need to add the board through the boards manager to your program. Please visit the [Qduino hookup guide](https://www.hackster.io/team-qtechknow/qduino-mini-quickstart-guide-8b2d68) for detailed instructions on installing drivers and programming a Qduino via the Arduino IDE.

### Addressable LED Library

If this is your first time working with addressable LEDs, you will also need to download the [Adafruit Neopixel Library](https://github.com/adafruit/Adafruit_NeoPixel). For Arduino IDE users, click on the button below to download a copy of the NeoPixel library along with some example code SparkFun has created.

[Download Neopixel Library](https://cdn.sparkfun.com/assets/0/4/a/f/8/51f1806cce395fcd20000004.zip)

If you have not previously installed an Arduino library, please check out our installation guide.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

January 11, 2013

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

## Example Code

The below code is designed to animate a strip of 39 addressable LEDs. In order to test before soldering, our first step will be to program the microcontrollers.

    language:c
    /******************************************************************************
    LED Sneakers by
    Melissa Felderman @ SparkFun Electronics

    This sketch directly lifts code from Adafruits Neopixel Library. 
    To learn more about the neopixel library and to view more sample code, 
    please visit here: 
    https://learn.adafruit.com/adafruit-neopixel-uberguide/overview
    *****************************************************************************/
    #include <Adafruit_NeoPixel.h>
    #ifdef __AVR__
      #include <avr/power.h>
    #endif

    #define PIN 6

    int numPix = 39 //UPDATE THIS WITH THE NUMBER OF LEDs ON YOUR STRIP

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(numPix, PIN, NEO_GRB + NEO_KHZ800);

    void setup() 

    void loop() 

    void rainbow(uint8_t wait) 
        strip.show();
        delay(wait);
      }
    }

    // Slightly different, this makes the rainbow equally distributed throughout
    void rainbowCycle(uint8_t wait) 
        strip.show();
        delay(wait);
      }
    }

    //Theatre-style crawling lights with rainbow effect
    void theaterChaseRainbow(uint8_t wait) 
          strip.show();

          delay(wait);

          for (int i=0; i < strip.numPixels(); i=i+3) 
        }
      }
    }

    // Input a value 0 to 255 to get a color value.
    // The colours are a transition r - g - b - back to r.
    uint32_t Wheel(byte WheelPos) 
      if(WheelPos < 170) 
      WheelPos -= 170;
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    }

When you are ready, copy and paste the below program into a new window in your Arduino IDE. Update the value for `int numPix` to reflect the number of pixels on your strip around the shoe\'s sole. Make sure the correct board is selected by going to **Tools \> Board \> Qduino Mini**. Then, connect your Qduino to your computer via USB. Turn it on, and select the active port from **Tools \> Port**. Now all you need to do is upload the program to your Qduino by hitting the upload button!

### Testing Your Code

To test the program before putting it together on the shoe, try using a combination of IC hooks, alligator clips, and jumper wires to create the circuit shown below and turn on your Qduino. Make sure to connect the LiPo battery to the Qduino for sufficient power. If the LEDs animate with rainbow patterns, you are ready to move on!

[![circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/LightUpSneaker_bb_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/LightUpSneaker_bb_1.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

Since each shoe will have a Qduino attached to control its own set of addressable LEDs, make sure to upload code to the second Qduino. Follow the steps to upload code. make sure to have the correct board and COM port selected when uploading to the second Qduino.

## Putting It Together

Now that we have tested our program with our parts, it\'s time to put everything together.

### STEP 1:

Measure the length of your shoe\'s sole with the LED strip. While taking note of the length, cut one LED strip to the desired shoe length between the gold pads. Cut part of the flexible silicon jacket that is used to seal the addressable LED strip so that there is room to solder to the pads.

Then cut three pieces of hook-up wire, around 3-4 inches each. [Strip](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-strip-a-wire) a tiny bit at one end of each piece.

[![step1 wire strip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/2_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/2_1.jpg)

[Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) each wire to each of the three pads on the LED strip.

[![step1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/3-1Scaled.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/3-1Scaled.png)

**Heads up!** Make sure to solder to the DIN pad and not the DOUT pad on the opposite side of the strip. The strip will not work if you have connected to DOUT.

### STEP 2:

Remove the backing from the clear rubber protection around the LED strip. Starting with the soldered pads at the inner heel, begin to wrap the strip around the shoe sole. While the clear rubber does have some adhesive on the back - it is not enough to weather walking. Use super glue to make sure the LED strip is secured to the shoe sole.

[![step2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/3_Glue.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/3_Glue.JPG)

### STEP 3:

Make a small hole in the shoe directly above the end of the strip with the leads attached.

[![make a hole](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/6_2.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/6_2.JPG)

### STEP 4:

Thread the soldered leads through the hole from the outside to the inside of the shoe.

[![step 4](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/7_1.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/7_1.JPG)

### STEP 5:

Glue the programmed Qduino to the inner ankle area, making sure to place it in a way that it will not rub against your body.

[![step 5](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/10_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/10_2.jpg)

### STEP 6:

The following diagram illustrates the circuit we will be putting together visually.

[![circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/LightUpSneaker_bb_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/LightUpSneaker_bb_1.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

Carefully solder the LED strip leads to the Qduino.

[![step 6](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/11.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/11.JPG)

### STEP 7:

Insulate all exposed wire and solder with hot glue.

[![step 7](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/12.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/12.JPG)

### STEP 8:

Add a small piece of Velcro to the outer side of the shoe, directly on top of the area with the Qduino glued on the other side.

[![step 8](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/14.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/14.JPG)

### STEP 9:

Add the complimentary piece of Velcro to one side of your battery.

[![step 9](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/15.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/15.JPG)

**\*PLEASE NOTE:** It is never a good idea to apply heat to a LiPo battery using a hot glue gun. A safer solution is to secure the battery with Velcro.

### STEP 10:

Poke another hole in the shoe, this time right below your Qduino.

[![step 10](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/16.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/16.JPG)

### STEP 11:

Thread the battery leads through the new hole from the outside to the inside.

[![step 11](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/17.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/17.JPG)

### STEP 12:

Attach the battery to the outer side of the shoe via the Velcro.

[![step 12](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/18.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/18.JPG)

### STEP 13:

Connect the battery to the Qduino via the JST connector.

[![step 13](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/19.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/19.JPG)

### STEP 14:

Cut out two small patches of white felt. One should be slightly larger than the Qduino and one slightly larger than the battery.

[![Step 14](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/20.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/20.JPG)

### STEP 15:

Sew or super glue the felt patched over your electronics, protecting them from the elements as well as protecting your ankles from scratching against the hardware.

[![step 15](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/21.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/21.JPG)

### STEP 16:

Repeat steps 1-16 for the other shoe.

### STEP 17:

Use the switch on the Qduino to turn your shoes on, and enjoy!

[![step 16](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/22.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/22.JPG)

[![final object](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/9/IMG_7062sm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/9/IMG_7062sm.jpg)