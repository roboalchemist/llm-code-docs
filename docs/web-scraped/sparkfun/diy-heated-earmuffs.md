# Source: https://learn.sparkfun.com/tutorials/diy-heated-earmuffs

## Introduction 

[] Design and build time: 5 Hours

In this project, we'll create a wearable pair of heated earmuffs with decorative addressable LEDs. These earmuffs are embedded with a Pro Micro 5v, two heating pads, and four rings of WS2812 addressable LEDs, or \'Neopixels\'. This project is designed to keep the user extra warm while still looking stylish.

[![overview](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/IMG_8549sm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/IMG_8549sm.jpg)

### Suggested Reading

Before you get started, take some time to familiarize yourself with the following:

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

[](https://learn.sparkfun.com/tutorials/planning-a-wearable-electronics-project)

### Planning a Wearable Electronics Project 

Tips and tricks for brainstorming and creating a wearables project.

[](https://learn.sparkfun.com/tutorials/addressable-led-strip-hookup-guide)

### Addressable LED Strip Hookup Guide 

Add blinking lights to any holiday decoration with our Holiday Lights Kit using WS2812-based addressable LEDs!

## Materials and Tools

Let\'s go over all of the things you\'ll need to put your project together.

[] **Attention:** Please make sure to use the appropriate power requirements when operating this heating pad. We do not recommend this product for beginners.

### You Will Also Need:

- [Hook Up Wire](https://www.sparkfun.com/products/11367)
- [Soldering Iron](https://www.sparkfun.com/products/11704)
- [Solder](https://www.sparkfun.com/products/10243)
- [Flush Cutters](https://www.sparkfun.com/products/11952)
- [Wire Strippers](https://www.sparkfun.com/products/12630)
- [Heat Shrink](https://www.sparkfun.com/products/9353)
- [Heat Gun](https://www.sparkfun.com/products/10326)
- Foam (1\" thick)
- Interfacing
- Matte Board or Cardboard
- Headband
- Hot Glue Gun and Glue
- Soft Fabric
- Scissors
- Soft Silicone Wire
- Disappearing Ink Marker
- Ruler

## Software Installation 

### Arduino IDE

The Pro Micro 5V is programmable via the Arduino IDE. If this is your first time using Arduino, please review our tutorial on installing the Arduino IDE.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### Pro Micro Drivers and Board Add-On

If this is your first time working with the Pro Micro, you may need to add drivers and the board add-on through the boards manager. Please visit the Pro Micro hookup guide for detailed instructions on installing drivers and programming a Pro Micro via the Arduino IDE.

[Pro Micro Hookup Guide](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide#installing-mac--linux)

### Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

In this program, we will also be utilizing the Adafruit Neopixel Library. You can download the library below.

[Adafruit Neopixel Library](https://github.com/adafruit/Adafruit_NeoPixel/archive/master.zip)

We have provided the code for this project below. Copy and paste it into your Arduino IDE and then upload it to your board. Make sure you have the correct board selected in the boards manager as well as the port under the port drop down.

    language:c
        /******************************************************************************
      earmuffs.ino
      Melissa Felderman @ SparkFun Electronics
      creation date: January 22, 2018

      Resources:
      Adafruit_NeoPixel.h - Adafruit Neopixel library and example functions

    *****************************************************************************/

    #include <Adafruit_NeoPixel.h>

    int heatPin = 3;
    int ring = 4;

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(80, ring, NEO_GRB + NEO_KHZ800);

    void setup() 

    void loop() 

    // Slightly different, this makes the rainbow equally distributed throughout
    void rainbowCycle(uint8_t wait) 
        strip.show();
        delay(wait);
      }
    }

    // Input a value 0 to 255 to get a color value.
    // The colours are a transition r - g - b - back to r.
    uint32_t Wheel(byte WheelPos) 
      if (WheelPos < 170) 
      WheelPos -= 170;
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    }

## Understanding Your Circuit

Inside the earmuffs are four [NeoPixel Rings](https://www.sparkfun.com/products/12665) containing a total of 80 WS2812 addressable LEDs, two [5x10cm Heating Pads](https://www.sparkfun.com/products/11288), a [Pro Micro 5v/18MHz](https://www.sparkfun.com/wish_lists/143567), a [N-Channel MOSFET](https://www.sparkfun.com/products/10213), one [10k resistor](https://www.sparkfun.com/products/11508), two small pieces of [Snappable Protoboard](https://www.sparkfun.com/products/13268), and lots [Hook Up Wire](https://www.sparkfun.com/products/11375). The project is powered by our [Lithium Ion Battery Pack](https://www.sparkfun.com/products/14169) via the [SparkFun microB USB Breakout](https://www.sparkfun.com/products/12035). A [Mini Power Switch](https://www.sparkfun.com/products/102) is connected to the power source for easy user control.

As expressed in the circuit diagram below, the Pro Micro 5v is the brains of this project. Pin 4 is connected to one of the 24x Neopixel Rings Din, with VCC connected to Raw on the Pro Micro, and GND to GND. Dout of that same Neopixel ring is connected to Din on of the 12x Neopixel Ring, VCC to VCC and GND to GND. Dout of the smaller Neopixel Ring is connected to Din on the second 24x Neopixel Ring, who\'s VCC and GND are connected to Raw and GND on the Microcontroller. Dout of this ring is connected to Din of the second 12x Neopixel ring, with VCC to VCC and GND to GND.

The [heating pads](https://www.sparkfun.com/products/11288) require about \~750mA, which is more than the microcontroller I/O pin can handle. In order to accomplish that, we will be using a [N-Channel Mosfet Transisitor](https://www.sparkfun.com/products/10213). One lead of each of the heating pads should connect directly to RAW on the microcontroller. The second connects to the Drain (D) lead on the transistor, or the center lead. Pin 3 on the microcontroller connects to the Gain (G) lead, which is the left lead. There is also a 10k resistor pulling the G lead down to GND. Finally, the Source (S) lead connects directly to GND.

Two long flexible wires are included in the circuit. One connects to GND and one directly to Raw. The GND wire will connect to GND on the USB Breakout. The Raw wire will connect to the center lead of the switch. Finally VCC on the USB breakout will connect with a second lead on the switch.

The Heated Earmuffs pose a unique design challenge as a wearable circuit in that the components require a **5v** power supply. That\'s not something you want to wear on your head. Because of this, the Heated Earmuffs have a similar physical design to headphones, with soft flexible wires connecting the circuit above with a control switch and power source in your pocket. Not only does this put the bulky power supply in a hidden location, but it also allows the user to conveniently and discretely switch the circuit on and off.

**Heads up!** Please note the the max current output for the battery pack used in this project is around 1A. In order to make sure the battery does not overdraw and thus overheat, we have reduced the brightness of the LEDs in the code to minimize the current draw of the circuit. Different battery packs will yield different max currents, always test while building your project.

[![Fritzing Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/earmuffs_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/earmuffs_bb.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

## Building the Structure 

The first part of this project is building the earmuffs structure which we will build our circuit around.

### STEP 1:

Download and print out the circles template.

[Download Circles Template Here](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/circles.pdf)

Then cut along the outline of each circle. Set aside the larger circle for later.

[![cut template](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-01.jpg)

### STEP 2:

Place the smaller circle on your matte board or cardboard and trace it.

[![trace circle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-02.jpg)

Repeat once more so that you have drawn two even circles on the matte board or card board.

[![repeat trace](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-03.jpg)

### STEP 3:

Cut out both circles.

[![cut circles](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-04.jpg)

### STEP 4:

Add some hot glue to the lower inch and a half of one side of the headband.

[![add glue](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-05_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-05_1.jpg)

### STEP 5:

Place one of the matte board of cardboard circles to the area with hot glue. The bottom point of the headband should be at the approximate center of the circle.

[![glue circle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-06.jpg)

Repeat on the second side.

[![glue second circle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-07.jpg)

### STEP 6:

Grab the small circle template again and trace it on your foam.

[![trace on foam](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-15.jpg)

Repeat once more so you have two circles.

[![second foam circle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-16.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-16.jpg)

### STEP 7:

Cut out both circles from the foam.

[![cut foam](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-17.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-17.jpg)

### STEP 8:

Use your scissors to sculpt one side of each foam circle into a dome.

[![sculpt foam](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-18.jpg)

When you are done, your foam circles side view should look like this:

[![foam dome](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-19.jpg)

### STEP 9:

Add hot glue around the perimeter of one of the circles on the headband and then place the foam dome on top. Repeat on the second side.

[![add glue](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-20.jpg)

[![place foam](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-21.jpg)

### STEP 10:

Grab the small circle template again and trace it on to interfacing twice.

[![trace on interfacing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-22.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-22.jpg)

[![repeat trace](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-23.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-23.jpg)

### STEP 11:

Cut out both circle from the interfacing.

[![cut interfacing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-24.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-24.jpg)

### STEP 12:

Add hot glue to the perimeter of the inner side of your board circle, and then place the interfacing on top. Repeat this on the second side.

[![glue inner circle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-25.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-25.jpg)

[![place interfacing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-26.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-26.jpg)

## Preparing Your Electronics

Now that we have build the structure of the earmuffs, let\'s begin to prepare the electronics for our circuit.

### STEP 13:

Add a small touch of hot glue to one edge of your heating pad, then fold it over making it half it\'s original size.

[![glue heating pad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-09.jpg)

[![fold heating pad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-10.jpg)

### STEP 14:

On one side of the folded pad, add hot glue to all four corners.

[![glue heating pad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-27.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-27.jpg)

### STEP 15:

Glue it on to the interfacing, with the two leads pointing up and aligned with the leg of the headband as much as possible. Repeat for the second heating pad on the opposite side.

[![place heating pad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-29.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-29.jpg)

### STEP 16:

[Strip a short amount of wire](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-strip-a-wire) (about 1\" - 2\") and [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) to both of the smaller Neopixel rings on VCC, GND, and DIN.

[![solder neopixel leads](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-11.jpg)

### STEP 17:

Place the larger neopixel ring around each smaller one, make sure the smaller one is relatively centered, and then add a small piece of tape over them to keep them in position.

[![Tape NeoPixels](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-12.jpg)

### STEP 18:

Solder the Neopixel Ring pairs together according to the circuit diagram. (From inside ring to outside ring, DIN -\> DOUT, VCC -\> VCC, and GND -\> GND.

[![solder rings together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-13.jpg)

### STEP 19:

Add hot glue to the back of the smaller Neopixel ring.

[![glue neopixel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-30.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-30.jpg)

### STEP 20:

Place rings on top of the foam dome. Repeat with the second set of rings on the opposite side.

[![Hot Glue NeoPixel Ring](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-31.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-31.jpg)

### STEP 21:

Solder medium length wire leads to Raw, GND, Pin 3 and Pin 4 on your Pro Micro.

[![Solder Wire to Pro Micro](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-32.jpg)

### STEP 22:

Place a small amount of hot glue to the back of the Pro Micro and then place it on the headband off to the side.

[![glue pro micro](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-33.jpg)

[![place pro micro](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-34.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-34.jpg)

## Soldering It Together

Now that all of our parts are in place, let\'s begin to solder the circuit together.

**Heads up!** Always test your circuit with alligator clips or on a breadboard before soldering together.

### STEP 23:

Take a long piece of hook up wire and solder one end to DOUT of one of your smaller NeoPixel Rings.

[![DOUT](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-44.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-44.jpg)

### STEP 24:

Lead it along the bottom edge of the headband, hot gluing it down along the way until you make it to the opposite side.

[![lead wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-46.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-46.jpg)

### STEP 25:

Solder the other end to DIN of the larger ring on the opposite side. This in effect created one long LED strand of 80x WS2812 addressable LEDs.

[![connect rings on both sides](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-47.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-47.jpg)

### STEP 26:

Cut the wire lead connected to Raw on the microcontroller down to about 1.5\" - 2\". Solder the free end to the corner of a piece of protoboard that is no wider than the headband. We will call this our Raw extension, and moving forward all connection to Raw will be made on this protoboard.

[![Solder raw lead](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-42.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-42.jpg)

### STEP 27:

Repeat step 26 for the GND wire lead. Make sure to solder it to the opposite end of the protoboard, leaving physical space between the two connections. We will call this our GND extension, and moving forward all connection to GND will be made on this protoboard.

[![solder gnd lead](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-43.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-43.jpg)

### STEP 28:

Solder a red wire lead to the Raw extension on the protoboard, and a black one to the GND extension. Take the red wire and solder it to VCC on one of the large Neopixel Rings. Take the black wire and solder it to GND on one of the large NeoPixel rings. Repeat for the second large ring on the opposite side.

[![Solder to Neopixel ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-49.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-49.jpg)

While you are doing this, make sure to bend your wires to fit the form of the earmuffs.

[![bend wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-48.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-48.jpg)

### STEP 29:

Find the wire lead connected to pin 4.

[![find pin 4](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-50.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-50.jpg)

Solder this wire to the remaining DIN on your NeoPixel Ring. As we have soldered the two sides together, there should only be on DIN left for you to use.

[![DIN NeoPixel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-51.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-51.jpg)

### STEP 30:

Cut a second small piece of protoboard, also no wider than the headband width, and solder the transistor along one edge.

[![solder transistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-52.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-52.jpg)

### STEP 31:

Trim the excess leads with a diagonal cutter and then fold the transistor back so that it lies flat in a plane with the protoboard.

[![bend transistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-57.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-57.jpg)

### STEP 32:

Solder a 10k resistor to the protoboard, connecting one end to the Gain (G) lead of the transistor and the other to a solder pad off to the side. Then use a jumper wire to solder the second side of the resistor to the GND extension.

[![solder resistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-58.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-58.jpg)

### STEP 33:

Holding the transistor protoboard to the headband with your thumb, solder the wire lead connected to pin 3 on the microcontroller to the same Gain (G) lead as the resistor on the transistor.

[![hold down](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-60.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-60.jpg)

[![solder pin 3 lead](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-61.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-61.jpg)

### STEP 34:

Take two medium pieces of red wire and two medium pieces of black wire. Solder each red wire to the red leads on the heating pads, and each black wire to the black leads on each heating pad, in essence fabricating longer leads for the heating pads.

[![Heating pad leads](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-62.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-62.jpg)

### STEP 35:

Place a small piece of heat shrink over each new connection and then use the heat gun to secure it around the soldered connections.

[![heat shrink](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-63.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-63.jpg)

[![heat gun](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-64.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-64.jpg)

### STEP 36:

Take both black leads from the heating pads and solder them to the middle lead on your transistor - also known as the Drain (D).

[![Solder to drain](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-65.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-65.jpg)

### STEP 37:

Grab a medium black length wire and solder one end to the GND extension on the first protoboard.

[![GND Extension](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-66.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-66.jpg)

### STEP 38:

Solder the second end of that wire to the Source (S) or rightmost lead on the transistor.

[![Solder source](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-67.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-67.jpg)

### STEP 39:

Solder header pins to your USB breakout.

[![header pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-69.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-69.jpg)

### STEP 40:

Cut a third piece of protoboard slightly wider than your USB breakout, and solder the other end of the header pins to one edge.

[![proto](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-70.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-70.jpg)

[![Solder breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-71.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-71.jpg)

### STEP 41:

Solder the switch to the opposite edge of the protoboard.

[![solder switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-73.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-73.jpg)

### STEP 42:

Use a very small piece of wire to connect VCC on your breakout to either the leg on the rightmost or leftmost of the switch. It does not matter which.

[![Solder switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-35.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-35.jpg)

### STEP 43:

Cut two long pieces of silicone wire in white. These should be long enough to reach from the crown of your head to your pants pocket.

[![cut silicone wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-72.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-72.jpg)

### STEP 44:

Solder one wire to GND of the USB breakout, and the other to the middle lead of the switch. Label these right away with masking tape. The GND wire should be \'-\' and the Switch wire \'+\'.

[![Solder silicone wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-36.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-36.jpg)

[![label wire ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-37.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-37.jpg)

### STEP 45:

Twist the silicone wires lightly, the solder the \'+\' silicone lead to the Raw extension and the \'-\' silicone lead to the GND extension.

[![solder to extensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-38.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-38.jpg)

### STEP 46:

Plug the battery pack into the USB port and switch your project on to test. This is to make sure that the solder joints are strong and that there are no shorts.

### STEP 47:

Add hot glue to the bottom of the protoboard for insulation.

[![insulate](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-39.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Earmuff_Tutorial_Images-39.jpg)

## Completing the Enclosure

### STEP 48:

Grab both of the circles you cut from the template in Step 1. On the backside of your fabric, trace the large circle twice and the small circle twice. Then use a ruler to trace a 10.5\" x 3.5\" rectangle. Cut these out.

[![cut fabric](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__10_58_17_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__10_58_17_AM.jpg)

### STEP 49:

Find the center of the rectangle piece of fabric on the backside by folding it in half and marking it. Then add a small dab of hot glue.

[![mark center](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_01_32_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_01_32_AM.jpg)

### STEP 50:

Place the top and center most point of your headband on top of the hot glue.

[![place headbandt](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_03_48_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_03_48_AM.jpg)

### STEP 51:

Continue to hot glue the fabric rectangle over the headband.

[![glue fabric](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_05_38_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_05_38_AM.jpg)

### STEP 52:

Add hot glue on the bottom side of the headband along one edge and fold the fabric over, beginning to cover the bottom of the headband.

[![glue bottom](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_06_00_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_06_00_AM.jpg)

[![fold fabric](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_06_45_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_06_45_AM.jpg)

### STEP 53:

Add hot glue to the free edge of the fabric on the backside and fold this over too. Once completed, your headband should be completely wrapped by fabric.

[![fold over](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_08_10_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_08_10_AM.jpg)

[![wrap headband](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_09_15_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_09_15_AM.jpg)

### STEP 54:

Add hot glue around the edge of the interfacing on one side, and place a small circle of fabric on top. Repeat on the second side.

[![hot glue interfacing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_09_46_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_09_46_AM.jpg)

[![place small circle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_10_34_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_10_34_AM.jpg)

### STEP 55:

Add some hot glue to the center of one of your foam domes, and then drape one of the larger circles of fabric on top, placing it as centered as possible.

[![hot glue domes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_12_54_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_12_54_AM.jpg)

[![drape large circle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_13_47_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_13_47_AM.jpg)

### STEP 56:

Add hot glue to the free edges of the larger circle and begin to wrap it around the dome until it is completely wrapped.

[![Glue edge of large circle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_14_05_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_14_05_AM.jpg)

[![wrap around dome](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_14_21_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_14_21_AM.jpg)

### STEP 57:

Plug in your power supply and turn the switch on!

[![plug in](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_24_36_AM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/Photo_Jan_25__11_24_36_AM.jpg)

[![DIY Heated Earmuffs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/IMG_8626sm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/IMG_8626sm.jpg)

[![Wearable DIY Heated Earmuffs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/2/IMG_8549sm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/2/IMG_8549sm.jpg)