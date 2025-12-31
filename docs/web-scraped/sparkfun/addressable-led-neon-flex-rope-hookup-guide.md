# Source: https://learn.sparkfun.com/tutorials/addressable-led-neon-flex-rope-hookup-guide

## Introduction

The addressable [LED Neon Flex Rope](https://www.sparkfun.com/products/14555) adds cool lighting effects for outdoor and indoor uses including in hallways and stairs, holiday lighting and more! In this hookup guide, you will learn how to connect, power, and control the LED segments with an Arduino.

[![LED Neon Flex Rope](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/8/5/14555-LED_Neon_Flex_Rope-04.jpg)](https://www.sparkfun.com/products/14555)

### [LED Neon Flex Rope](https://www.sparkfun.com/products/14555) 

[ COM-14555 ]

This Neon Flex Rope is a \~6.5ft (2m) long, non-addressable LED strip simulates the neon effects that you see in store fronts ...

**Retired**

### Required Materials

To follow along with this project tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. If you are just looking at powering up the LED neon flex rope and using its demo mode, you will need the following.

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Power Supply - 24V (5A)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/2/0/13758-Power_supply_24V_5A-01.jpg)](https://www.sparkfun.com/products/13758)

### [Power Supply - 24V (5A)](https://www.sparkfun.com/products/13758) 

[ TOL-13758 ]

This 5A power supply outputs both 24VDC and is terminated with a center-positive 5.5 x 2.1mm barrel connector.

**Retired**

[ ![Power Cable - 10A IEC C13 - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/2/8/14935-Power_Cable_-_10A_IEC_C13_-_2m-01.jpg) ]

### Power Cable - 10A IEC C13 - 2m 

[ TOL-14935 ]

This power cable has a C13 connector on one side and a standard US 3-prong plug on the other. It\'s rated for 10A at 125V.

**Retired**

**Note:** The product showcases uses a [24VDC/14.6A Meanwell switching power supply](https://www.sparkfun.com/products/14100) with adapter cable. We will be using the 24V/5A power supply throughout this tutorial.

To test and control the segments, you will need the following materials listed below.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![USB Wall Charger - 5V, 1A (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/3/1/0/11456-USB_Wall_Charger_-_5V__1A__Black_-01.jpg)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html)

### [USB Wall Charger - 5V, 1A (Black)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html) 

[ TOL-11456 ]

USB is being implemented as a power connection standard more and more these days, but you don\'t always have a computer on han...

[ [\$5.95] ]

[![SparkFun USB Mini-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/6/9/8/0/11301-01.jpg)](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html)

### [SparkFun USB Mini-B Cable - 6 Foot](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html) 

[ CAB-11301 ]

This is a USB 2.0 type A to Mini-B 5-pin cable. You know, the mini-B connector that usually comes with USB Hubs, Cameras, MP3...

[ [\$5.50] ]

[![Alligator Clip with Pigtail (10 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/6/5/14303-Alligator_Clip_with_Pigtail__10_Pack_-01.jpg)](https://www.sparkfun.com/alligator-clip-with-pigtail-10-pack.html)

### [Alligator Clip with Pigtail (10 Pack)](https://www.sparkfun.com/alligator-clip-with-pigtail-10-pack.html) 

[ CAB-14303 ]

This is a 10-pack of wires that are pre-terminated with an alligator clip on one end and a male header on the other.

[ [\$9.25] ]

[![Hook-up Wire - Black (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/2/08022-01.jpg)](https://www.sparkfun.com/hook-up-wire-black-22-awg.html)

### [Hook-up Wire - Black (22 AWG)](https://www.sparkfun.com/hook-up-wire-black-22-awg.html) 

[ PRT-08022 ]

Standard 22 AWG solid Black hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes ...

[ [\$3.25] ]

### Tools

Depending on the application, you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49) for a more secure connection. Otherwise, the following tools will suffice for hooking up and testing.

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

[![Wire Strippers - 30AWG Hakko](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/1/2/12630-Hakko-Wire-Strippers-30AWG-Feature.jpg)](https://www.sparkfun.com/wire-strippers-30awg-hakko.html)

### [Wire Strippers - 30AWG Hakko](https://www.sparkfun.com/wire-strippers-30awg-hakko.html) 

[ TOL-12630 ]

It can be used as: Shears, Multi-diameter Wire stripper, pliers.

[ [\$13.95] ]

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

## Hardware Overview

The LED Neon Flex Rope uses the UCS1903 chipset and LEDs. The electronics are sealed in a waterproof IP65 silicone housing and diffuses the light emitting from the LEDs.

### Pinout

To power or control the LED neon flex rope, you will need to connect to the female bare wire connector. **24V** is required to power the LED Neon flex rope using the wire with the red stripe. The center wire is the data pin when using with a microcontroller. The third wire on the other side is for ground.

[![LED Neon Flex Rope Pinout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/3/LEDNeonFlexRopePinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/LEDNeonFlexRopePinout.png)

Below lists a hookup table of the pinout for reference.

  LED Neon Flex Rope   Pinout
  -------------------- --------
  Vcc (Red Striped)    24V
  DAT (Middle)         Data
  GND (Side)           Ground

### LED Strip Segments

For those interested in cutting the LED neon flex rope down, you can reduce the length with the help of the colored markers on the bottom of the housing. The markers are guides and are not exact locations between the LED segments.

[![LED Neon Flex Rope Markers on Bottom](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Tutorial_Markers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Tutorial_Markers.jpg)

Each LED strip segment is about 20 inches long.

[![Segment Measured](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Tutorial_Length_Between_Markers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Tutorial_Length_Between_Markers.jpg)

Each segment uses wires to connect between each LED strip that is sealed in the housing.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Closeup Side View of Cut LED Neon Flex Rope](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Tutorial_Cut_Closeup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Tutorial_Cut_Closeup.jpg)   [![Teardown of LED Strip inside Housing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Tutorial_Teardown.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Tutorial_Teardown.jpg)
  *Closeup Side View of a Cut LED Neon Flex Rope*                                                                                                                                                                                                                    *Teardown of the LED Neon Flex Rope*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Heads up!** Remember the colored markers are guides and are not exact locations between the LED segments. We recommend using a box cutter and hobby knife to partially cut into the housing. If necessary, you can individually address the LEDs to help determine the relative location between the segments. The parts that are not as bright is the gap between the LED strips.\
\

[![](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/7/6/3/14555-LED_Neon_Flex_Rope-Action-Sections.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/14555-LED_Neon_Flex_Rope-Action-Sections.jpg)

\
Once you determine the location of the wires connecting the LED segments, you can completely cut through the LED neon flex rope. Make sure that the LED strip is not powered when adjusting the length.

If you decide to cut the strip down, make sure to seal the exposed circuit with some epoxy or hot glue.

## Hardware Hookup w/ Power Only

When powering the LED neon flex rope with only power, it will display a demo. Insert the 3-prong power cable into the 24V power supply. Then make the following connections with using a female DC barrel jack adapter.

  24V Power Supply   Female DC Barrel Jack Adapter   LED Neon Flex Rope Pinout
  ------------------ ------------------------------- ---------------------------
  Center Positive    \+                              Vcc (Red Striped) = 24V
                                                     Clear (Middle) = DAT
  GND                \-                              Clear (Side) = GND

Once connected, insert and fasten the adapter to the female bare wire connector into the LED neon flex rope. The setup should look like the image below. Tape was used to insulate the DAT pin since the wire was exposed.

[![Hardware Hookup with Only Power](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/3/LEDNeon_FlexRopeHardwareHookup_Demo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/LEDNeon_FlexRopeHardwareHookup_Demo.jpg)

## Demo Mode

By connecting only to the power pins, the LED Neon Flex Rope will run a demo mode. This can include the rope cycling colors using different patterns. This can include:

- one solid color
- pulse and fade
- alternating between colors
- each segment incrementally lighting up with one color

## Hardware Hookup w/ Arduino

**Heads up!** For a more secure connection make sure to solder the wires and make a custom connection.

For users that want to control the animations or react to input from a sensor, an Arduino microcontroller can be used to control the LED neon flex rope\'s segments. For a quick connection, we will use an alligator clip with pigtail and hookup wire.

### Connecting to the DAT Pin

For initial testing, we will be using an alligator clip with pigtail to connect the LED Neon flex\'s DAT pin to the software defined control pin on the Arduino. Use the alligator clip to clamp on the DAT pin wire and then connect the other end to D5.

### Additional Power Supply and GND Reference

Since the recommended input voltage via the barrel jack for the RedBoard is **15V**, an additional power supply is required. For the scope of this tutorial, we will use the mini-USB connector on the Arduino to power the control circuit with **5V**. A 5V USB port from a computer can be used during testing. A 5V USB wall adapter can be used when powering the Arduino in a project or installation.

Since we are adding an additional power supply, make sure to ground the LED neon flex rope with the control circuit. [Strip a piece of wire](https://learn.sparkfun.com/tutorials/working-with-wire). Then connect the \"-\" on the DC barrel jack adapter to the Arduino\'s GND pin. Wrap the wires together to make a more secure connection.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Circuit_Ground.jpg "Insert Wire to GND for Reference")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Circuit_Ground.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Secure_Ground_Wire.jpg "Screw In GND Wires")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Secure_Ground_Wire.jpg)
  *Insert Wire to GND for Reference*                                                                                                                                                                                                             *Screw In GND Wires*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Hookup Table

Based on the connections described above, here is a hookup table of the connections.

  24V Power Supply   Female DC Barrel Jack Adapter   LED Neon Flex Rope Pinout   Arduino                          5V Power Supply
  ------------------ ------------------------------- --------------------------- -------------------------------- -----------------
  Center Positive    \+                              Vcc (Red striped) = 24V                                      
                                                                                 5V                               5V
                                                     Clear (middle wire) = DAT   Pin 5 (or whatever is defined)   
  GND                \-                              Clear (side) = GND          GND                              GND

The final circuit should look similar to the image below.

[![LED Neon Flex Rope Controlled by Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Hardware_Hookup_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/3/LED_Neon_Flex_Rope_Hardware_Hookup_Arduino.jpg)

## Library Overview

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

To control the LED Neon Flex Rope, you could use a 5V Arduino-based microcontroller. You will need to download and install Daniel Garcia's FastLED library using the library manager. You can also manually install it from the [GitHub Repository](https://github.com/FastLED/FastLED) by downloading the library from the button below.

[Download FastLED Library (ZIP) Here](https://github.com/FastLED/FastLED/archive/master.zip)

### Parameters

When using the FastLED library, certain parameters need to be adjusted to be compatible with the chipset. When using the FastLED library, the `LED_TYPE` would be defined as the `UCS1903` chipset. There are 16 segments per LED Neon Flex Rope to control so the `NUM_LEDs` is `16`. The `COLOR_ORDER` is `BRG` so:

    red = blue
    green = red
    blue = green

## Example Code

The FastLED library includes a few examples for a variety of addressable LED chipsets to get started. The following examples will demonstrate how to modify the example to use with the UCS1903 chipset. For more information, check out the [FastLED Library\'s wiki](https://github.com/FastLED/FastLED/wiki/Chipset-reference#other-stuff).

[FastLED Library Wiki: Chipset Reference](https://github.com/FastLED/FastLED/wiki/Chipset-reference#other-stuff)

### FastLED Blink Modification

For simplicity, lets blink one segment of one LED neon flex rope using the FastLED\'s **Blink.ino** example by following the steps listed below:

- First adjust the number of LEDs in the strip to 16.
- Change the `DATA_PIN` to pin 5.
- Comment out the `CLOCK_PIN` and LED arrangement for the `neopixel`.
- Uncomment out the LED arrangement for the `UCS1903` chipset.
- Modify the color order by changing `RGB` to `BRG`.

Or copy and paste the modified example in an Arduino sketch. After uploading, you should see one segment blink with red.

    language:c
    /*Modified FastLED Blink.ino Example
     * 
     * Description: This modified example is used to control one segment 
         * of the LED Neon Flex Rope.
     */
    #include "FastLED.h"

    // How many leds in your strip?
    #define NUM_LEDS 16 //# of segments on the LED Neon Flex Rope

    // For led chips like Neopixels, which have a data line, ground, and power, you just
    // need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
    // ground, and power), like the LPD8806 define both DATA_PIN and CLOCK_PIN
    #define DATA_PIN 5
    //#define CLOCK_PIN 13

    // Define the array of leds
    CRGB leds[NUM_LEDS];

    void setup() 

    void loop() 

### Blink Each Segment

To control all the segments with control, you would need to address each segment in the array with a color. Write code to address each segment defined in the array and reduce the delay between each blink. Or copy and paste the modified blink example in an Arduino sketch. After uploading, you should see each segment blink red.

    language:c
    /*Modified FastLED Blink.ino Example
    * 
    * Description: This modified example is used to control all segments
    * of the LED Neon Flex Rope.
    */
    #include "FastLED.h"

    // How many leds in your strip?
    #define NUM_LEDS 16 //# of segments on the LED Neon Flex Rope

    // For led chips like Neopixels, which have a data line, ground, and power, you just
    // need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
    // ground, and power), like the LPD8806 define both DATA_PIN and CLOCK_PIN
    #define DATA_PIN 5
    //#define CLOCK_PIN 13 //not used with UCS1903 chipset

    // Define the array of leds
    CRGB leds[NUM_LEDS];

    void setup() 

    void loop() 

### Color Palette Modification

Let\'s try modifying one more example from the Fast LED library to add the color paltette animation to the LED Neon Flex Rope light. After uploading, you should see the patterns cycling.

    language:c
    /*Modified FastLED ColorPalette.ino Example
    * 
    * Description: This modified ColorPalette example is used to control all segments
    * of the LED Neon Flex Rope.
    */

    #include <FastLED.h>

    #define LED_PIN     5
    #define NUM_LEDS    16
    #define BRIGHTNESS  255
    #define LED_TYPE    UCS1903
    #define COLOR_ORDER BRG
    CRGB leds[NUM_LEDS];

    #define UPDATES_PER_SECOND 100

    // This example shows several ways to set up and use 'palettes' of colors
    // with FastLED.
    //
    // These compact palettes provide an easy way to re-colorize your
    // animation on the fly, quickly, easily, and with low overhead.
    //
    // USING palettes is MUCH simpler in practice than in theory, so first just
    // run this sketch, and watch the pretty lights as you then read through
    // the code.  Although this sketch has eight (or more) different color schemes,
    // the entire sketch compiles down to about 6.5K on AVR.
    //
    // FastLED provides a few pre-configured color palettes, and makes it
    // extremely easy to make up your own color schemes with palettes.
    //
    // Some notes on the more abstract 'theory and practice' of
    // FastLED compact palettes are at the bottom of this file.

    CRGBPalette16 currentPalette;
    TBlendType    currentBlending;

    extern CRGBPalette16 myRedWhiteBluePalette;
    extern const TProgmemPalette16 myRedWhiteBluePalette_p PROGMEM;

    void setup() 

    void loop()
    

    void FillLEDsFromPaletteColors( uint8_t colorIndex)
    
    }

    // There are several different palettes of colors demonstrated here.
    //
    // FastLED provides several 'preset' palettes: RainbowColors_p, RainbowStripeColors_p,
    // OceanColors_p, CloudColors_p, LavaColors_p, ForestColors_p, and PartyColors_p.
    //
    // Additionally, you can manually define your own color palettes, or you can write
    // code that creates color palettes on the fly.  All are shown here.

    void ChangePalettePeriodically()
    
            if( secondHand == 10)  
            if( secondHand == 15)  
            if( secondHand == 20)  
            if( secondHand == 25)  
            if( secondHand == 30)  
            if( secondHand == 35)  
            if( secondHand == 40)  
            if( secondHand == 45)  
            if( secondHand == 50)  
            if( secondHand == 55)  
        }
    }

    // This function fills the palette with totally random colors.
    void SetupTotallyRandomPalette()
    
    }

    // This function sets up a palette of black and white stripes,
    // using code.  Since the palette is effectively an array of
    // sixteen CRGB colors, the various fill_* functions can be used
    // to set them up.
    void SetupBlackAndWhiteStripedPalette()
    

    // This function sets up a palette of purple and green stripes.
    void SetupPurpleAndGreenPalette()
    

    // This example shows how to set up a static color palette
    // which is stored in PROGMEM (flash), which is almost always more
    // plentiful than RAM.  A static PROGMEM palette like this
    // takes up 64 bytes of flash.
    const TProgmemPalette16 myRedWhiteBluePalette_p PROGMEM =
    ;

    // Additionl notes on FastLED compact palettes:
    //
    // Normally, in computer graphics, the palette (or "color lookup table")
    // has 256 entries, each containing a specific 24-bit RGB color.  You can then
    // index into the color palette using a simple 8-bit (one byte) value.
    // A 256-entry color palette takes up 768 bytes of RAM, which on Arduino
    // is quite possibly "too many" bytes.
    //
    // FastLED does offer traditional 256-element palettes, for setups that
    // can afford the 768-byte cost in RAM.
    //
    // However, FastLED also offers a compact alternative.  FastLED offers
    // palettes that store 16 distinct entries, but can be accessed AS IF
    // they actually have 256 entries; this is accomplished by interpolating
    // between the 16 explicit entries to create fifteen intermediate palette
    // entries between each pair.
    //
    // So for example, if you set the first two explicit entries of a compact 
    // palette to Green (0,255,0) and Blue (0,0,255), and then retrieved 
    // the first sixteen entries from the virtual palette (of 256), you'd get
    // Green, followed by a smooth gradient from green-to-blue, and then Blue.

### More Examples!

Now that we have some experience using two of the examples, try modifying and testing out the others in the FastLED library!

[FastLED \> Examples](https://github.com/FastLED/FastLED/tree/master/examples)