# Source: https://learn.sparkfun.com/tutorials/marquee-party-bag

## Introduction

The Marquee Party Bag is a purse embedded with several [LED Matrices](https://www.sparkfun.com/products/12662) and a [Lilypad Microcontroller](https://www.sparkfun.com/products/12049). The LEDs are easily programmable for the user to convey marquee messages or to simply make beautiful patterns. In this tutorial we will go through the step by step process of making this project.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/1/Party_Bag-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/Party_Bag-03.jpg)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/Feldi_PartyBag.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/Feldi_PartyBag.gif)

## Required Materials

To follow along with this guide, you will need the following:

### You Will Also Need:

- A small purse
- A hot glue gun
- Hot glue sticks

## Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

## Hardware Overview

The two main components that the Marquee Party Bag use are the following:

- LilyPad Arduino USB - ATmega32U4 Board
- NeoPixel NeoMatrix 8x8 - 64 RGB LED

### LilyPad Arduino USB

[![LilyPad Arduino USB - ATmega32U4 Board](https://cdn.sparkfun.com/r/600-600/assets/parts/8/6/3/3/12049-LilyPad_Arduino_USB_-_ATmega32U4_Board-01.jpg)](https://www.sparkfun.com/lilypad-arduino-usb-atmega32u4-board.html)

### [LilyPad Arduino USB - ATmega32U4 Board](https://www.sparkfun.com/lilypad-arduino-usb-atmega32u4-board.html) 

[ DEV-12049 ]

LilyPad is a wearable e-textile technology designed to have large connecting pads to allow them to be sewn into clothing & co...

[ [\$31.95] ]

The brains behind the Marquee Party Bag is an LilyPad Arduino USB - ATmega32U4 Board, a sewable Arduino-compatible microcontroller. It features the ATmega32U4. The LilyPad Arduino can be powered either from the USB connection or a 3.7V LiPo battery. The board runs at 3.3V; applying more voltage (e.g. 5V) to its pins may damage it.

The LilyPad Arduino uses only a single microcontroller (the Atmel ATmega32U4) to both run your sketches and communicate over USB with the computer. This means that you only need a USB cable to program the LilyPad Arduino USB (as opposed to an FTDI USB-serial adaptor as with other LilyPads). It is programmable via the Arduino IDE.

LilyPad Arduino USB - ATmega32U4 Board Technical Specifications:

  ------------------------ -----------------------------------------------------
  Microcontroller          ATmega32u4
  Operating Voltage        3.3V
  Input Voltage            3.8V - 5V
  Digital I/O Pins         9
  PWM Channels             4
  Analog Input Channels    4
  DC Current per I/O Pin   40 mA
  Flash Memory             32 KB (ATmega32u4) of which 4 KB used by bootloader
  SRAM                     2.5 KB (ATmega32u4)
  EEPROM                   1 KB (ATmega32u4)
  Clock Speed              8 MHz
  ------------------------ -----------------------------------------------------

### NeoPixel NeoMatrix 8x8

[![NeoPixel NeoMatrix 8x8 - 64 RGB LED ](https://cdn.sparkfun.com/r/600-600/assets/parts/9/3/7/3/12662-01a.jpg)](https://www.sparkfun.com/products/12662)

### [NeoPixel NeoMatrix 8x8 - 64 RGB LED ](https://www.sparkfun.com/products/12662) 

[ COM-12662 ]

This is the NeoPixel NeoMatrix from Adafruit a large board with 64 WS2812 RGB LEDs arranged in an 8x8 matrix.

**Retired**

The NeoPixel NeoMatrix from Adafruit is a large board with 64 WS2812 RGB LEDs arranged in an 8x8 matrix. Each individual LED is addressable through your microcontroller.

There are two 3-pin connection ports to wire the NeoMatrix up. Solder wires to the input port, and provide 5VDC to the +5V and ground pins. Then connect the DIN pin to your microcontroller, and make a common ground from the 5V power supply to the microcontroller/Arduino.

Additionally, you can chain as many NeoMatrix panels together as you'd like. For the second panel, connect the DIN connection to the first panel's DOUT. Connect the ground pins together and power with 5V.

Please refer to the [NeoPixel Überguide](https://cdn.sparkfun.com/datasheets/Components/LED/adafruit-neopixel-uberguide.pdf) for a more in depth view of Neopixels.

## Hardware Assembly

To build your own Marquee Party Bag at home, you will need to collect all of your supplies fist.

The following diagram illustrates the circuit we will be putting together visually.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/1/marqueeBag_.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/marqueeBag_.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

Start by plotting out the position of your three matrices.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/1/Hello_Giggles-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/Hello_Giggles-01.jpg)

Solder the matrices in a row according to the Fritzing diagram above. I used all black wires to make them as invisible as possible.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/1/Hello_Giggles-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/Hello_Giggles-04.jpg)

When you finish this step, your three matrices should look like this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/1/Hello_Giggles-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/Hello_Giggles-03.jpg)

Use your hot glue gun to glue the matrices onto the front of your bag.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/1/Hello_Giggles-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/Hello_Giggles-05.jpg)

Bend the three hook up wires from the first matrix around to the inner flap of the bag, and solder your connections according to the Fritzing Diagram above.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/1/Hello_Giggles-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/Hello_Giggles-06.jpg)

This inside flap of your bag should look something like this when you are done:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/1/Party_Bag-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/1/Party_Bag-01.jpg)

Now our circuit is done, and it\'s time to move onto programming.

## Software Installation

### Arduino IDE

The LilyPad Arduino USB - ATmega32U4 Board is programmable via the Arduino IDE. If this is your first time using Arduino, please review our tutorial on installing the Arduino IDE.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### Neopixel Library

If this is your first time working with neopixels, you will also need to download the [Adafruit Neopixel Library](https://github.com/adafruit/Adafruit_NeoPixel). For Arduino IDE users, click on the button below to download a copy of the NeoPixel library along with some example code SparkFun has created.

[Download Neopixel Library](https://cdn.sparkfun.com/assets/0/4/a/f/8/51f1806cce395fcd20000004.zip)

If you have not previously installed an Arduino library, please check out our installation guide.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

January 11, 2013

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

## Example Code

I am providing two separate programs for you to work with:

- Marquee
- Simple Rainbow Cycle

### Example 1: Marquee

The first is the Marquee option. I have added a handful of comments in the code to show you how and where to edit for customization.

    language:c
    //Marquee Party bag by Melissa Felderman for SparkFun Electronics. 
    // Based on Adafruit_NeoMatrix example for single NeoPixel Shield.
    // Scrolls 'PARTY BAG!' across the matrix in a landscape (horizontal) orientation.

    #include <Adafruit_GFX.h> //include graphics library
    #include <Adafruit_NeoMatrix.h> //include neopixel matrix library
    #include <Adafruit_NeoPixel.h> //include neopixel library
    #ifndef PSTR
     #define PSTR // Make Arduino Due happy
    #endif

    #define PIN 2

    Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, 3, 1, PIN,
      NEO_MATRIX_TOP     + NEO_MATRIX_LEFT +
      NEO_MATRIX_ROWS + NEO_MATRIX_PROGRESSIVE,
      NEO_GRB            + NEO_KHZ800);

    //Inlcude the colors that you would like your writing to reflect in the colors array
    const uint16_t colors[] = ;

    void setup() 

    int x    = matrix.width();
    int pass = 0;

    void loop() 
      matrix.show();
      delay(100);
    }

### Example 2: Simple Rainbow Cycle

The second is a simple rainbow cycle.

    language:c
    //rainbow LED bag by Melissa Felderman for Spsarfun
    //This sketch is an edited version of the Adafruit Neopixel Strand Test example code from the Neopixel Library. 

    #include <Adafruit_NeoPixel.h>
    #ifdef __AVR__
      #include <avr/power.h>
    #endif

    #define PIN 2

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(198, PIN, NEO_GRB + NEO_KHZ800);

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

When you are ready, pick your program, copy it, and paste it into a new window in your Arduino IDE. Make sure the correct board is selected by going to **Tools \> Board \> Lilypad Arduino USB**. Then, connected your Lilypad to your computer via USB. Turn the Lilypad on, and select the active port from **Tools \> Port**. Now all you need to do is upload the program to your Lilypad by hitting the upload button!