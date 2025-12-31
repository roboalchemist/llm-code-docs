# Source: https://learn.sparkfun.com/tutorials/photon-oled-shield-hookup-guide

## Introduction

Want your [Photon](https://www.sparkfun.com/products/13774) projects to display sensor readings, play pong, or draw little doodles? The [Photon OLED Shield](https://www.sparkfun.com/products/13628?_ga=1.130787398.890988720.1429644996) might be the perfect fit, and we\'re going to show you how to use it.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/13628-01a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/13628-01a.jpg)

If the OLED screen in the picture above looks familiar, it\'s probably because we use the same component in our [Microview](https://www.sparkfun.com/products/12923) and [Micro OLED Breakout](https://www.sparkfun.com/products/13003) products, as well as the [OLED Block for the Edison](https://www.sparkfun.com/products/13035). We love it for it\'s combination of small footprint yet surprisingly clear graphics \-- the screen itself is 0.66\" across, with a display area measuring 64 pixels wide by 48 pixels tall.

**Please Note:** All SparkFun shields for the Photon are also compatible with the [Core](https://store.particle.io/?product=spark-core) from Particle. The WKP, DAC and VBT pins on the Photon will be labeled A7, A6 and 3V3\*, respectively, on the Core, but will not alter the functionality of any of the Shields.

### Covered in this Tutorial

This tutorial will cover the functionality of the OLED shield, how to hook it up in your project, and how to program with it using the SparkFun Micro OLED Library.

### Required Materials

All you need to get started with the Photon OLED Shield is a Photon, a micro-USB cable, and the OLED shield. You\'ll also want to sign up for an account on [particle.io](http://particle.io) and register your photon. Instructions on how to do this can be found at [docs.particle.io](http://docs.particle.io/photon/).

[![SparkFun Photon Micro OLED Shield](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/1/5/13628-01a.jpg)](https://www.sparkfun.com/sparkfun-photon-micro-oled-shield.html)

### [SparkFun Photon Micro OLED Shield](https://www.sparkfun.com/sparkfun-photon-micro-oled-shield.html) 

[ DEV-13628 ]

The SparkFun Photon Micro OLED Shield breaks out a small monochrome, blue-on-black OLED to use with your Photon module. It'...

**Retired**

[![Particle Photon (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/2/8/13774-01.jpg)](https://www.sparkfun.com/products/13774)

### [Particle Photon (Headers)](https://www.sparkfun.com/products/13774) 

[ WRL-13774 ]

Particle\'s IoT (Internet of Things) hardware development board, the Photon, provides everything you need to build a connected...

**Retired**

### Suggested Reading

- [Serial Peripheral Interface (SPI)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) \-- SPI is the preferred method of communication with the display.
- [I^2^C](https://learn.sparkfun.com/tutorials/i2c) \-- Alternatively, I^2^C can be used to control the display. It uses less wires, but is quite a bit slower.

## OLED Shield Overview

### Pin Descriptions

Since the shield does all of the work for you, there\'s no need to actually wire these connections - but in case you\'re looking at datasheets, or code for the Microview or OLED breakout, this table will give you a clue as to what the shield is doing. As always, you can check the schematic for more info.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/Screen_Shot_2015-06-30_at_1.51.24_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/Screen_Shot_2015-06-30_at_1.51.24_PM.png)

  OLED Shield Pin   Photon Pin   SPI Function     I^2^C Function                                      Notes
  ----------------- ------------ ---------------- --------------------------------------------------- ---------------------------------------------------------------------
  GND               GND          Ground           Ground                                              0V
  3V3 (VDD)         3V3          Power            Power                                               Should be a regulated 3.3V supply.
  D1 (SDI/MOSI)     A5           MOSI             SDA                                                 Serial data in
  D0 (SCK)          A3           SCK              SCL                                                 SPI and I^2^C clock
  D2 (SDO)          MISO         ---              Can be unused in SPI mode. No function for I^2^C.   ---
  D/C               D6           Data / Command   I^2^C address selection                             Digital pin to signal if incoming byte is a command or screen data.
  RST               D7           Reset            Reset                                               Active-low screen reset.
  CS                A2           ---              SPI chip select (active-low)                        ---

\

### Setting the Jumpers

With the board flipped over, you\'ll notice there are six jumpers. The majority of these jumpers are used to **switch between SPI and I^2^C mode**. As the board ships, these jumpers are set to configure the display in **SPI mode**.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/Screen_Shot_2015-06-30_at_1.51.40_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/Screen_Shot_2015-06-30_at_1.51.40_PM.png)

Here\'s an overview of each jumper, moving from left-to-right, top-to-bottom in the picture above:

- **VD/VB** \-- This jumper shorts the digital power supply (VDD) to the battery power supply (VBAT). Because both of these supplies can be powered at 3.3V, an easy one-supply solution is to short them together and provide them a single supply. If you need to power the digital supply at something lower, like 1.8V, you may need to cut this jumper and provide two supplies.
- **D1/D2** \-- This jumper can be used to **short D1 to D2**. If you want to use SPI, leave this jumper open. If you\'re using I^2^C, short the jumper. By default this jumper is open.
- **D/C** \-- This jumper can be used to short D/C to either 3.3V (1) or 0V (0). In I^2^C mode, the D/C pin sets the 7-bit address of the display. In SPI mode this jumper should be left open, as the D/C pin needs to be toggled to determine if an incoming byte is data or command.
- **BS2** and **BS1** \-- These pins on the OLED determine which interface you\'re using to control the OLED. With the two signals, there are four possible combinations:
    BS2   BS1   Interface
    ----- ----- -----------------------
    0     0     SPI
    0     1     I^2^C
    1     0     8-bit Parallel (6800)
    1     1     8-bit Parallel (8080)

  By default, both of these jumpers are set to 0, which puts the display in SPI mode. If you want to change it to I^2^C mode, clear the BS1 jumper and set it to 1.

------------------------------------------------------------------------

That brief overview should cover the 99% use case. Consult the schematic and the notes therein if you have any questions about jumpers or pins.

## Using the OLED Shield

When attaching your Photon to the top of the OLED shield, make sure the beveled end of your Photon (next to A0 and D0) matches up with the beveled lines on the top of the OLED shield (the end with the Open Source Hardware Logo). The pin labels on the Photon should match those on the OLED shield as well. You can stack many of our Photon shields together, which is why the OLED screen juts out to the side. So, you can end up with something like this:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/13345-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/13345-07.jpg)

## Using the Particle OLED Library

Great, now that we understand the hardware setup, let\'s put some code on this thing and see what it can do. Using the Particle library we\'ve written, you\'ll be able to write text, draw lines and shapes, and generally display anything that\'ll fit on the screen.

### Getting the Particle OLED Library

For this page we\'ll be using the [online Particle environment](https://build.particle.io). If you\'re using the Particle Dev environment instead, you can get the library and code examples from the [GitHub repository](https://github.com/sparkfun/SparkFun_Micro_OLED_Particle_Library).

[Download the Particle OLED Library](https://github.com/sparkfun/SparkFun_Micro_OLED_Particle_Library/archive/master.zip)

### Load the Demo Example

If you haven\'t created a Particle user account and claimed your board, you\'ll need to do that now. Starting [here](http://docs.particle.io/) is a great idea if you\'re having trouble.

Once you\'re logged into build.particle.io and have a device selected (all this is covered at the link above), you\'ll want to click on the `create new app` button in the sidebar \-- it\'s big and blue, you can\'t miss it. Call your app something like \'OLED_test\'.

Next \-- this is the important part \-- we include the `SparkFunMicroOLED` library. To do this:

- Click on the icon that looks like a bookmark (it\'s all the way to the left on the black skinny sidebar, 4th up from the bottom)
- In the text box under \'community libraries\', search for \'OLED\' and you\'ll see \'SparkFunMicroOLED\' come up (though it might be cut off a little bit, don\'t worry).

It should look something like this:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/Screen_Shot_2015-06-29_at_2.04.53_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/6/Screen_Shot_2015-06-29_at_2.04.53_PM.png)

- Click on the library name, and a bunch of stuff will pop up, including all the library files as well as a few options of what to do with the library.
- In this case, we just want to use the library in our app, so click on the \'include in app\' button.
- This will lead you to list of all your apps - click on the name of the app you just created, and you should see a statement like `#include "SparkFunMicroOLED/SparkFunMicroOLED.h"` at the top of your app.
- Last thing is to add the math library to our sketch - on the line below the first `#include` statement, type in: `#include "math.h"`

Now that we\'ve included the library in our app, let\'s give it some code - just copy the demo code below and **paste it into your app, below the include statements**.

    language:cpp
    /*
    Micro-OLED-Shield-Example.ino
    SparkFun Micro OLED Library Hello World Example
    Jim Lindblom @ SparkFun Electronics
    Original Creation Date: June 22, 2015

    This sketch prints a friendly, recognizable logo on the OLED Shield, then
      goes on to demo the Micro OLED library's functionality drawing pixels,
      lines, shapes, and text.

      Hardware Connections:
      This sketch was written specifically for the Photon Micro OLED Shield, which does all the wiring for you. If you have a Micro OLED breakout, use the following hardware setup:

        MicroOLED ------------- Photon
          GND ------------------- GND
          VDD ------------------- 3.3V (VCC)
        D1/MOSI ----------------- A5 (don't change)
        D0/SCK ------------------ A3 (don't change)
          D2
          D/C ------------------- D6 (can be any digital pin)
          RST ------------------- D7 (can be any digital pin)
          CS  ------------------- A2 (can be any digital pin)

      Development environment specifics:
        IDE: Particle Build
        Hardware Platform: Particle Photon
                           SparkFun Photon Micro OLED Shield

      This code is beerware; if you see me (or any other SparkFun
      employee) at the local, and you've found our code helpful,
      please buy us a round!

      Distributed as-is; no warranty is given.
    */

    //////////////////////////////////
    // MicroOLED Object Declaration //
    //////////////////////////////////
    // Declare a MicroOLED object. If no parameters are supplied, default pins are
    // used, which will work for the Photon Micro OLED Shield (RST=D7, DC=D6, CS=A2)

    MicroOLED oled;

    void setup()
    

    void loop()
    

    void pixelExample()
    
    }

    void lineExample()
    
        for (int deg=0; deg<360; deg+=15)
        
      }
    }

    void shapeExample()
    
        }
        // Check if the ball hit the right paddle
        if (ball_X + ball_rad > paddle1_X)
        
        }
        // Check if the ball hit the top or bottom
        if ((ball_Y <= ball_rad) || (ball_Y >= (oled.getLCDHeight() - ball_rad - 1)))
        
        // Move the paddles up and down
        paddle0_Y += paddle0Velocity;
        paddle1_Y += paddle1Velocity;
        // Change paddle 0's direction if it hit top/bottom
        if ((paddle0_Y <= 1) || (paddle0_Y > oled.getLCDHeight() - 2 - paddleH))
        
        // Change paddle 1's direction if it hit top/bottom
        if ((paddle1_Y <= 1) || (paddle1_Y > oled.getLCDHeight() - 2 - paddleH))
        

        // Draw the Pong Field
        oled.clear(PAGE);  // Clear the page
        // Draw an outline of the screen:
        oled.rect(0, 0, oled.getLCDWidth() - 1, oled.getLCDHeight());
        // Draw the center line
        oled.rectFill(oled.getLCDWidth()/2 - 1, 0, 2, oled.getLCDHeight());
        // Draw the Paddles:
        oled.rectFill(paddle0_X, paddle0_Y, paddleW, paddleH);
        oled.rectFill(paddle1_X, paddle1_Y, paddleW, paddleH);
        // Draw the ball:
        oled.circle(ball_X, ball_Y, ball_rad);
        // Actually draw everything on the screen:
        oled.display();
        delay(25);  // Delay for visibility
      }
      delay(1000);
    }

    void textExamples()
    
      }
      delay(500);  // Wait 500ms before next example

      // Demonstrate font 1. 8x16. Let's use the print function
      // to display every character defined in this font.
      oled.setFontType(1);  // Set font to type 1
      oled.clear(PAGE);     // Clear the page
      oled.setCursor(0, 0); // Set cursor to top-left
      // Print can be used to print a string to the screen:
      oled.print(" !\"#$%&'()*+,-./01234");
      oled.display();       // Refresh the display
      delay(1000);          // Delay a second and repeat
      oled.clear(PAGE);
      oled.setCursor(0, 0);
      oled.print("56789:;<=>?@ABCDEFGHI");
      oled.display();
      delay(1000);
      oled.clear(PAGE);
      oled.setCursor(0, 0);
      oled.print("JKLMNOPQRSTUVWXYZ[\\]^");
      oled.display();
      delay(1000);
      oled.clear(PAGE);
      oled.setCursor(0, 0);
      oled.print("_`abcdefghijklmnopqrs");
      oled.display();
      delay(1000);
      oled.clear(PAGE);
      oled.setCursor(0, 0);
      oled.print("tuvwxyz~");
      oled.display();
      delay(1000);

      // Demonstrate font 2. 10x16. Only numbers and '.' are defined. 
      // This font looks like 7-segment displays.
      // Lets use this big-ish font to display readings from the
      // analog pins.
      for (int i=0; i<25; i++)
      

      // Demonstrate font 3. 12x48. Stopwatch demo.
      oled.setFontType(3);  // Use the biggest font
      int ms = 0;
      int s = 0;
      while (s <= 50)
      
        delay(1);
      }
    }

    // Center and print a small title
    // This function is quick and dirty. Only works for titles one
    // line long.
    void printTitle(String title, int font)
        

Now, click the \'flash\' button (the one that looks like a lightning bolt) and wait for the magic to begin!