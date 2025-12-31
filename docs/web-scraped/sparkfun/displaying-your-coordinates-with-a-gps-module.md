# Source: https://learn.sparkfun.com/tutorials/displaying-your-coordinates-with-a-gps-module

## Introduction

What's better than learning [GPS](https://www.sparkfun.com/gps)? Learning it Qwiic-ly! Today we will be making a simple project to help get your feet wet with GPS. This project is quick and easy thanks to our [Qwiic Connect System](https://www.sparkfun.com/qwiic). The general idea is to push a button and see your latitude and longitude coordinates. We may be starting simple, but there is certainly room for more advanced users to modify and grow the project!

Software developers start with "Hello World!" and every hardware engineer remembers their first LED circuit, right? So let\'s fuse the ideas by creating a project that receives a GPS signal and outputs it to a screen for a user. Then we can bump it up by making it mobile. I've got just the thing in mind!

[![project parts image](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/2/Simple_GPS_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/2/Simple_GPS_Tutorial-01.jpg)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything, depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/qwiic-micro-oled-hookup-guide)

### Qwiic Micro OLED Hookup Guide 

Get started displaying things with the Qwiic Micro OLED.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

[](https://learn.sparkfun.com/tutorials/sparkfun-gps-breakout-zoe-m8q-and-sam-m8q-hookup-guide)

### SparkFun GPS Breakout (ZOE-M8Q and SAM-M8Q) Hookup Guide 

The SparkFun ZOE-M8Q and SAM-M8Q are two similarly powerful GPS units but with different project applications. We\'ll compare both chips before getting each up and running.

## Hardware Overview

We're using three large components, a 9V battery, and Qwiic cables. Let's look into the bigger components first before we start.

#### RedBoard Qwiic

First up, the brains of our project. This development board is an evolution on our classic RedBoard. No change to programming with Arduino, so software is still easy. However, this allows us to streamline Qwiic development without the need for a shield. If you have the classic RedBoard and still want to make this project, arm yourself and grab a [shield!](https://www.sparkfun.com/products/14352)

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

#### Qwiic Micro OLED

We will read our coordinates using a simple OLED screen. Our product page describes this component best: "This version of the Micro OLED Breakout is exactly the size of its non-Qwiic sibling, featuring a screen that is 64 pixels wide and 48 pixels tall and measuring 0.66\" across." So we have small but powerful screen and that's perfect for our purposes.

[![SparkFun Micro OLED Breakout (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/2/1/14532-SparkFun_Micro_OLED_Breakout__Qwiic_-01.jpg)](https://www.sparkfun.com/products/14532)

### [SparkFun Micro OLED Breakout (Qwiic)](https://www.sparkfun.com/products/14532) 

[ LCD-14532 ]

The SparkFun Qwiic Micro OLED Breakout is a Qwiic enabled version of our popular MicroView and micro OLED display!

**Retired**

#### SAM-M8Q Chip Antenna GPS Breakout

Lastly, we will use a GPS module and we have one perfect for this occasion. This new GPS Breakout brings the ease, quality, and affordability from a great line of GPS modules from u-blox. The biggest feature is hot start and low lock time with a rechargeable coin cell battery. This means we have a powerful, inexpensive GPS that fits in a small space and will do all our talking with the satellites up above!

[![SparkFun GPS Breakout - Chip Antenna, SAM-M8Q (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/6/4/8/15210-SparkFun_GPS_Breakout_-_Chip_Antenna__SAM-M8Q__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gps-breakout-chip-antenna-sam-m8q-qwiic.html)

### [SparkFun GPS Breakout - Chip Antenna, SAM-M8Q (Qwiic)](https://www.sparkfun.com/sparkfun-gps-breakout-chip-antenna-sam-m8q-qwiic.html) 

[ GPS-15210 ]

The SparkFun SAM-M8Q GPS Breakout is a high quality GPS board with equally impressive configuration options.

[ [\$43.95] ]

## Hardware Hookup

Technically, we only have one component to actually solder - the button switch. Truth be told, you could just use some alligator clips and not even need an iron. We have other colors, but I have a bias to green and I really liked the strength and feel of the metal momentary switch. When we solder the connections to jumper wires that fit the headers on the RedBoard, I'm assuming that you've developed some skills soldering. If not, that's fine. We have a [tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) for that as well. Feel free to head over there and then put those wizard skills to work!

**If you are soldering**, then you can follow my connections. There are many ways to use switches, but I went for a momentary digital low. That just means that when I push the button the voltage on the digital pin assigned will be down from 5 volts to 0 volts. On the bottom of the switch you\'ll see a \'+\' and a \'-\'. These are for the LED backlight, and those will go to 5V and GND respectively. When you angle the button and look at that bottom portion, you\'ll see a few pin indicators labeled \'C1\', \'NC1\', and \'NO1\'. NC1 and NO1 stand for normally closed and normally open. We\'ll want to solder C1 and NO1. This combination will give us the digital low when we push the button.

[![Image of the button and it\'s pins](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/2/button_hookup.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/2/button_hookup.png)

Attach the button pins to the RedBoard Qwiic as follows:

  Button Pin   RedBoard Pin
  ------------ ---------------
  \+           5V
  \-           GND
  C1           **GND**
  NO1          Digital Pin 2

The next part for assembly is really simple. Just connect our boards together with our Qwiic cables, order doesn't really matter!

Your final assembly should look something like this:

[![Fritzing image of assembly](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/2/Fritzing4.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/2/Fritzing4.jpg)

*Having a hard time seeing the circuit? Click the image for a closer look.*

If you want to take the above in steps then you can hook up each component separately to the RedBoard to experiment. If you want to skip it and just throw caution to the wind, then please jump down to final code.

## Software Setup

**Note:** This code/library has been written and tested on Arduino IDE version 1.8.5. Otherwise, make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### SparkFun Micro OLED library

First, you\'ll need to download and install the Sparkfun Micro OLED library. You can install the library via the Arduino Library Manager by searching \'**SparkFun Micro OLED Breakout**\'. Alternatively, you can either grab the library from the [GitHub repository](https://github.com/sparkfun/Micro_OLED_Breakout) or use the button below:

[SparkFun Micro OLED Library (ZIP)](https://github.com/sparkfun/Micro_OLED_Breakout/archive/master.zip)

### SparkFun U-blox Arduino Library

You will also need to install the Ublox library for the GPS unit. The SparkFun U-blox Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun ublox GPS**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_Ublox_Arduino_Library):

[SparkFun U-blox Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Ublox_Arduino_Library/archive/master.zip)

**Note:** At the time of writing, this tutorial used the [SparkFun Ublox Arduino Library v1](https://github.com/sparkfun/SparkFun_Ublox_Arduino_Library). The library has been depreciated. The example code is still functional, however it is recommended to use a microcontroller with a larger memory if you decide to use the latest [SparkFun u-blox GNSS Arduino Library](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library). Make sure to [follow the steps to migrate when using the latest library](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library#migrating-to-v20).

From the hookup guides, I hope you have a good understanding with how we're setting this project up. We want to read a GPS location and output our latitude and longitude to the Micro OLED screen so we can see where we're at. Sounds simple enough. So let's start with our Qwiic Micro OLED Screen.

## Example Code

### Micro OLED Code

I've modified a snippet of code from our hookup guide for a small test of writing text to the OLED screen. Before it can be used, make sure you\'ve installed the micro OLED library as listed in the [Software Setup](https://learn.sparkfun.com/tutorials/displaying-your-coordinates-with-a-gps-module#software-setup) section above. Copy the code, paste it into the Arduino IDE, select the **Arduino/Genuino Uno**, and the COM port, and hit upload to test!

    language:c
    #include <Wire.h>  // Include Wire if you're using I2C
    #include <SFE_MicroOLED.h>  // Include the SFE_MicroOLED library

    //////////////////////////
    // MicroOLED Definition //
    //////////////////////////
    //The library assumes a reset pin is necessary. The Qwiic OLED has RST hard-wired, so pick an arbitrarty IO pin that is not being used
    #define PIN_RESET 9  
    //The DC_JUMPER is the I2C Address Select jumper. Set to 1 if the jumper is open (Default), or set to 0 if it's closed.
    #define DC_JUMPER 1 

    //////////////////////////////////
    // MicroOLED Object Declaration //
    //////////////////////////////////
    MicroOLED oled(PIN_RESET, DC_JUMPER);    // I2C declaration

    void setup()
    

    void loop()

    void printTest(String title, int font)
    

Once the library is installed we can simply compile and see a dummy text on our screen.

[![Image of MicroOLED with coordinates](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/2/Simple_GPS_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/2/Simple_GPS_Tutorial-02.jpg)

### GPS Code

One done, two to go. Next we have our SAM-M8Q GPS module to test. I personally found the *Example3_GetPosition* code by Nathan Seidle to be the easiest and most convenient to experiment with. We find this sketch under *File\>Examples\>Sparkfun u-Blox GNSS Arduino Library*. Can't find it? Make sure you\'ve got the library for this GPS module installed as explained above in the [Software Setup](https://learn.sparkfun.com/tutorials/displaying-your-coordinates-with-a-gps-module#software-setup). It's ok, I'll wait. I may perhaps make some tea. Let me know when you're ready and busting out data to the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics). If that's new to you, just verify and upload the code the board and hit that magnifying glass in the upper right hand corner. Set the baud rate to **115200**, unless you want to see what our alien overlords have to say.

[![GPS module hooked up to RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/6/9/GPS_Module_ZOE-M8Q__GPS_SAM-M8Q_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/9/GPS_Module_ZOE-M8Q__GPS_SAM-M8Q_Hookup_Guide-03.jpg)

### Final Code

If you\'re here, I take it that you've mastered the OLED Screen and SAM-M8Q module? Then I believe you're ready! Seriously, this is the simple part. I blended the two previous sections of code to use the button to trigger a read from the GPS module and output the latitude and longitude to the OLED Screen. If you feel savvy, read through it and reverse engineer what I did so you can make glorious modifications! I say learn by breaking, master by rebuilding.

    language:c
    #include <Wire.h>
    #include <SFE_MicroOLED.h> 
    #include "SparkFun_Ublox_Arduino_Library.h" //http://librarymanager/All#SparkFun_Ublox_GPS

    #define PIN_RESET 9
    #define DC_JUMPER 1

    SFE_UBLOX_GPS myGPS;
    MicroOLED oled(PIN_RESET, DC_JUMPER);

    const int buttonPin = 2;
    const int ledPin =  13;

    int buttonState = 0;

    void setup() 

    void loop() 
          if(myGPS.begin() == true)
        }

    }

With everything connected, press the button to view your coordinates on the OLED! Instead of using your USB for power, connect a 9V battery to the RedBoard to go mobile!

[![GIF of pushing button and getting coordinates](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/2/Simple_GPS_Demo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/2/Simple_GPS_Demo.gif)

## Let\'s Wrap it Up

For myself, this project has a special purpose. I love to go fishing and I'm a nerd. So my usage for this project is to map my catches. When I make record breaking catch of unearthly magnitudes (okay most of my trophies are around 4 inches, but lets both just move on), I'll take a photo and then safely release the little guy. What I'd like to do is geo-tag those catches by using the coordinates I write down from my gadget and then pin them to the pictures of my catches. This way I can look back at where my biggest catches were so I can go there again, or just make some hypothesis as to the health of the lake.

### Take the next step

Now that you can literally find your location on earth with a push of a button let\'s do something more useful and put our locations on a map. With just a few different pieces of hardware, the following tutorial teaches you how to do just that.

[](https://learn.sparkfun.com/tutorials/gps-geo-mapping-at-the-push-of-a-button)

### GPS Geo-Mapping at the Push of a Button 

September 27, 2019

Let\'s ramp up our GPS tracking skills with KML files and Google Earth. We\'ll make a tracker that logs location and allows us to visualize our steps with Google Earth.