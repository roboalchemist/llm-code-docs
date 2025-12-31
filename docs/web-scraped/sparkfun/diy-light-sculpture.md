# Source: https://learn.sparkfun.com/tutorials/diy-light-sculpture

## Introduction 

[] Design and build time: 5 Hours

In this project, we'll create a beautiful desktop light sculpture by edge-lighting laser cut acrylic with addressable [LED](https://www.sparkfun.com/leds)s. This project is embedded with a [QDuino Mini](https://www.sparkfun.com/products/13614), [8x8 Adafruit Neopixel Matrix](https://www.sparkfun.com/products/12662), [potentiometer](https://www.sparkfun.com/products/9939), [momentary pushbutton](https://www.sparkfun.com/products/10302), and [switch](https://www.sparkfun.com/products/102).

[![overview light sculpture](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Gif__1_.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Gif__1_.gif)

### Required Materials

Let\'s go over all of the things you\'ll need to put your project together. Depending on what you have, you may not need everything listed here. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You will need a [soldering iron](https://www.sparkfun.com/products/14734), [solder](https://www.sparkfun.com/products/10242), and [general soldering accessories](https://www.sparkfun.com/categories/49) as well as a [3D printer](https://www.sparkfun.com/products/13880) and [black filament](https://www.sparkfun.com/products/12954):

[![ABS Filament 3mm - 1kg (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/8/8/6/12954-01a.jpg)](https://www.sparkfun.com/products/12954)

### [ABS Filament 3mm - 1kg (Black)](https://www.sparkfun.com/products/12954) 

[ TOL-12954 ]

This is a 1kg (2.2lb) reel of 3mm black ABS (acrylonitrile butadiene styrene) plastic filament for 3D printing. ABS is a grea...

**Retired**

[![TAZ 6 3D Printer](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/1/2/13880-Action.jpg)](https://www.sparkfun.com/products/13880)

### [TAZ 6 3D Printer](https://www.sparkfun.com/products/13880) 

[ TOL-13880 ]

The LulzBot® TAZ 6 is the most reliable, easiest-to-use desktop 3D printer ever, featuring innovative self-leveling and self...

**Retired**

You will also need the following items:

- Laser Cutter
- Clear Acrylic (1/8\" thick)
- Hot Glue Gun and Glue

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

[](https://learn.sparkfun.com/tutorials/addressable-led-strip-hookup-guide)

### Addressable LED Strip Hookup Guide 

Add blinking lights to any holiday decoration with our Holiday Lights Kit using WS2812-based addressable LEDs!

## Software Installation 

### Arduino IDE

The Qduino Mini is programmable via the Arduino IDE. If this is your first time using Arduino, please review our tutorial on installing the Arduino IDE.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### Qduino Mini Drivers and Board Add-On

If this is your first time working with the Qduino Mini, you may need to add drivers and the board add-on through the boards manager. Please visit the Qduino Mini quick start guide for detailed instructions on installing drivers and programming a Qduino Mini via the Arduino IDE.

[Qduino Mini Quick Start Guide](https://www.hackster.io/team-qtechknow/qduino-mini-quickstart-guide-8b2d68?ref=platform&ref_id=6047_trending___&offset=0)

### Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

In this program, we will also be utilizing the Adafruit Neopixel Library. You can obtain this library through the Arduino Library Manager. Search for **Adafruit Neopixel** and you should be able to install the latest version of the library. If you prefer downloading the library manually you can grab it from the GitHub repository:

[Download the Adafruit Neopixel Library (ZIP)](https://github.com/adafruit/Adafruit_NeoPixel/archive/master.zip)

We have provided the code for this project below. Copy and paste it into your Arduino IDE and then upload it to your board. Make sure you have the correct board selected in the boards manager as well as the port under the port drop down.

    language:c
        /******************************************************************************
      lightsculpture.ino
      Melissa Felderman @ SparkFun Electronics
      creation date: July 31, 2018

      Resources:
      Adafruit_NeoPixel.h - Adafruit Neopixel library and example functions

    *****************************************************************************/

            #include <Adafruit_NeoPixel.h> //include afafruit library 
        #define PIN 6 //LED matrix pin
        #define brightPot A0 //potentiometer to controll brightness
        #define pwrSwitch 4 //power switch
        #define momBut 5 //button to control LED mode
        int numPix = 64; //total LED count
        int brightPotVal; //Variable to hold pot value
        int pixelBrightness; //variabe to hold brightness value
        int switchState; //variable to hold switch value
        int butState; //variable to hold button value
        int mode = 0; //starting mode for switch state
        int prevButState = LOW;
        boolean butBool = false;
        int topMode = 4; //max number of LED modes in switch state

        unsigned long lastDebounceTime = 0;
        unsigned long debounceDelay = 200;

        Adafruit_NeoPixel strip = Adafruit_NeoPixel(numPix, PIN, NEO_GRB + NEO_KHZ800); //declare neopixel matrix

        //create an array for each row of LEDs
        int rowOne[] = ;
        int rowTwo[] = ;
        int rowThree[] = ;
        int rowFour[] = ;
        int rowFive[] = ;
        int rowSix[] = ;
        int rowSeven[] = ;
        int rowEight[] = ;

        void setup() 

        void loop()  butBool = false;
          } if (mode > topMode) 

          Serial.println(mode);

          //switch state function to cycle through modes on LEDs, you can add as many or as few as you would like
          if (switchState == HIGH) 
                strip.show();
                break;
              case 1:
                rainbow();
                break;
              case 2:
                buleGreenGradient();
                break;
              case 3:
                pinkGradient();
                break;
              case 4:
                yellowGradient();
                break;

            }
          } else if (switchState == LOW) 
            strip.show();
          }
        }

        //functions for LED colors

        void everyOther() 
          strip.show();
        }

        void pinkGradient() 
          strip.show();
        }

        void buleGreenGradient() 
          strip.show();
        }

        void yellowGradient() 
          strip.show();
        }
        void rainbow()  for (int i = 0; i < 8; i++)  for (int i = 0; i < 8; i++)  for (int i = 0; i < 8; i++)  for (int i = 0; i < 8; i++)  for (int i = 0; i < 8; i++)  for (int i = 0; i < 8; i++)  for (int i = 0; i < 8; i++) 
          strip.show();
        }

## Understanding Your Circuit

Inside the light sculpture enclosure is one [NeoPixel NeoMatrix 8x8 - 64 RGB LED](https://www.sparkfun.com/products/12662) containing a total of 64 addressable WS2812 LEDs, a [100uF Capacitor](https://www.sparkfun.com/products/96) to protect the first LED, one [Qduino Mini - Arduino Dev Board](https://www.sparkfun.com/products/13614) to act as the brains of the project, a [Mini Power Switch](https://www.sparkfun.com/products/102) to easily turn the project on or off, a [Tactile Button](https://www.sparkfun.com/products/10302) to navigate between light modes, and a [Potentiometer](https://www.sparkfun.com/products/9939) to control brightness. A small piece of [Snappable Protoboard](https://www.sparkfun.com/products/13268) is used to extend the \'+\' and \'-\' terminals on the Qduino Mini making it easier to connect the \'+\' and \'-\' leads from your components. A [MicroB USB](https://www.sparkfun.com/products/14741) cable is used to supply wall power directly to the USB port on the Qduino, but a large LiPo battery would work as well.

**⚡ Please note!** The Qduino mini runs on **3.3V**!

As shown in the circuit diagram below, the Qduino Mini is the brains of this project. Pin D6 is connected to the NeoPixel NeoMatrix, the potentiometer is connect to pin A0, the switch to pin D4, and the momentary pushbutton to D5. The first LED on the NeoPixel Matrix is protected using a 100uF capacitor between \'+\' and \'-\' on the matrix and \'+\' and \'-\' on the Qduino Mini. You may also notice that while the rest of the components directly connect to \'+\' on the Qduini Mini, the switch and button both connect to \'-\' of the Qduino via a resistor. This is called a pulldown resistor and allows the Qduino to get accurate readings of HIGH and LOW. To learn more about how to use pull up and pull down resistors with Arduino, [check out our tutorial](https://learn.sparkfun.com/tutorials/pull-up-resistors).

[![Light Sculpture Fritzing Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/lightsculpture.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/lightsculpture.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

## Enclosure Fabrication

The first part of this project is printing the enclosure on a 3D printer. If you do not have access to a 3D printer, check with your local library or maker space. There are also 3D printing services which you can use online like [Shapeways](https://www.shapeways.com/?utm_campaign=search_branded&utm_source=google&utm_medium=cpc&utm_content=286334583832&utm_term=shapeways&adgroupid=61960008368&gclid=EAIaIQobChMIjPvUgeLg3AIVQZRpCh2ZxQ6HEAAYASAAEgI_7fD_BwE).

### Download 3D Printer Drivers

Download any drivers and firmware needed to control your 3D printer. If you are working with a LulzBot like the ones sold through SparkFun, check out their [downloads page](https://www.lulzbot.com/content/downloads) in the support section of their website. If you are working with a different printer, check out the printer brand\'s website for information on drivers and firmware.

### Download Project File

Download the .stl file from the project page on [thingiverse](https://www.thingiverse.com/thing:3021554).

[Download File Here](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture.zip)

[![download stl](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Screen_Shot_2018-08-09_at_2.06.00_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Screen_Shot_2018-08-09_at_2.06.00_PM.png)

### Prepare GCode

Prepare your Gcode by loading the .stl into your driver software. Either save the Gcode to an SD card or prepare to print by connecting your computer to the printer via USB. Make sure your settings match the material you plan to use. I recommend using black filament because it is effective in blocking light. A lighter color may leak light. If you prefer a light colored enclosure, I would print it in black and then spray paint it afterwards before adding the electronics.

**Heads up!** To save time and filament, flip the enclosure over in your driver so that the horizontal slots are flat against the bed.

[![3D Printer Driver Prep](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Screen_Shot_2018-08-09_at_2.26.26_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Screen_Shot_2018-08-09_at_2.26.26_PM.png)

### Print

Print the enclosure!

[![print the enclosure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-01.jpg)

## Putting Your Electronics Together

Now that we have printed the enclosure, let\'s prepare the electronics for our circuit.

**PLEASE NOTE!** Always test your circuit on a breadboard before soldering it together in the enclosure.

### Solder Wire Leads

Solder wire leads of about 2\" to your components using solid core hook up wire. To make things easier for yourself later, use red wire for \'+\', black from GND, and white for GPIO input/output. Use heat shrink to secure and isolate your connections on the button and switch.

[![solder leads light sculpture](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-02.jpg)

*Click the image for a closer look.*

### Place Electronics

Place the electronics in their respective spaces in the enclosure. For the NeoPixel matrix, make sure your DIN pin is in the opposite corner of the potentiometer. This is to ensure your LED patterns align with the slots. You can secure the potentiometer in place with the nut that comes with it.

[![place electronics light sculpture](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-03.jpg)

For the button and switch, use a small dab of hot glue on the backside to hold them in place.

[![hot glue electronics light sculpture](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-04.jpg)

Solder a \'+\' and \'-\' lead to the VCC and GND of your Qduino respectively. There is only one \'+\' and one \'-\' pin on the Qduino so we will need to extend these two pins in order for your components to connect. To do this, grab a small piece of protoboard and solder the opposite end of the \'+\' lead to one corner and the opposite end of the \'-\' lead to the opposite corner.

[![solder entensions light sculpture](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-05.jpg)

Plug the USB cable into the Qduino and place it face down behind the potentiometer with the USB cable threaded through the tab in the back of the enclosure.

[![plug in Qduino Light Sculpture](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-06.jpg)

Before you begin soldering your circuit together, all parts in the enclosure should look like this:

[![All the parts together light scultprue](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-07.jpg)

### Solder Circuits

Solder your circuit together according to the fritzing diagram provided above. Use the \'+\' and \'-\' extensions on the protoboard for all of your \'+\' and \'-\' leads. Don\'t forget to solder a resistor between the GND extension and the the GND leads on your switch and button. It is also best practice to use a capacitor between the \'+\' and \'-\' leads on your NeoPixel matrix and the \'+\' and \'-\' extensions to protect the first LED from a rush of current.

[![Solder it together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-08.jpg)

### Verify

Test your circuit. Turn it on and make sure it is working according to the program.

## Laser Cutting Your Design

Now that we have the base enclosure completed with the electronics soldered together into a circuit, let\'s take a look at how to add a decorative flair to your project.

### Download Templates

Download the laser cutter template from the project [thingiverse](https://www.thingiverse.com/thing:3021554/files) page to prepare to cut your acrylic inserts. Open this with illustrator and begin to design your etching and/or cuts. I have found that the light is picked up by both the etched design *and* the edges of the plastic, so you can use both of these elements to create your final design. There are 8 rows of LEDs on your matrix so you will want to make 8 different acrylic inserts.

### Cut Your Designs

These inserts were cut and the designs rastered on our Epilog 75W laser cutter according to the manufacturer\'s specifications. If you do not have access to a laser cutter, check out your local library or hackerspace. Alternatively, you can order your designs online at [Ponoko](https://www.ponoko.com/).

[![laser cut acrylic inserts light culpture](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture_Tutorial-09.jpg)

### Light up your Life!

Pop the inserts into your enclosure and enjoy!

[![light sculpture gif](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Gif__1_.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Gif__1_.gif)

[![final light sculpture](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/7/Light_Sculpture-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/7/Light_Sculpture-05.jpg)