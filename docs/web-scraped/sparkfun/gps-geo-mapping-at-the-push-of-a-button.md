# Source: https://learn.sparkfun.com/tutorials/gps-geo-mapping-at-the-push-of-a-button

## Introduction

If you need an intermediate GPS project to tickle your fancy, we\'ve got one ready to go. In a [previous tutorial](https://learn.sparkfun.com/tutorials/displaying-your-coordinates-with-a-gps-module), we slapped some boards together to see our GPS locations on an OLED Screen. It was a great learning experience, but we need something more. Today we\'ll do some more good \'ol board slappin\', and we\'ll save multiple coordinates in a KML file and take over the world! Okay, not take over, but we can easily see collections of coordinates all over the world with Google Earth.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/Screen_Shot_2019-06-25_at_1.36.40_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/Screen_Shot_2019-06-25_at_1.36.40_PM.png)

### Required Materials

**Note:** Updated 10/14/20. Hardware list included a 9V battery and holder. 9V is above the threshold for the Turbo. Please replace with an appropriate LiPo/Li-Ion battery or another power source \<= 6V.

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/microsd-shield-and-sd-breakout-hookup-guide)

### MicroSD Shield and SD Breakout Hookup Guide 

Adding external storage in the form of an SD or microSD card can be a great addition to any project. Learn how in this hookup guide for the microSD shield and SD breakout boards.

[](https://learn.sparkfun.com/tutorials/qwiic-micro-oled-hookup-guide)

### Qwiic Micro OLED Hookup Guide 

Get started displaying things with the Qwiic Micro OLED.

[](https://learn.sparkfun.com/tutorials/redboard-turbo-hookup-guide)

### RedBoard Turbo Hookup Guide 

An introduction to the RedBoard Turbo. Level up your Arduino-skills with the powerful SAMD21 ARM Cortex M0+ processor!

[](https://learn.sparkfun.com/tutorials/adding-more-sercom-ports-for-samd-boards)

### Adding More SERCOM Ports for SAMD Boards 

How to setup extra SPI, UART, and I2C serial ports on a SAMD-based boards.

[](https://learn.sparkfun.com/tutorials/sparkfun-gps-breakout-zoe-m8q-and-sam-m8q-hookup-guide)

### SparkFun GPS Breakout (ZOE-M8Q and SAM-M8Q) Hookup Guide 

The SparkFun ZOE-M8Q and SAM-M8Q are two similarly powerful GPS units but with different project applications. We\'ll compare both chips before getting each up and running.

## Hardware Overview

If you followed along with the last GPS tutorial, you\'ll have an idea of where we\'re going. However, since we\'re packing more stuff into a small module, we\'ll need more power. Unfortunately, the 5 libraries we\'ll be using pushes the original RedBoard to its limits. So to make up the gap, we\'ll use the SAMD21. Specifically speaking, the SparkFun RedBoard Turbo!

### RedBoard Turbo

The Turbo is a relatively new development board, sporting the versatile ATSAMD21G18 ARM Cortex-M0+ microcontroller. It\'s also carrying an RTC Crystal, WS2812 addressable RGB LED, and a LiPo battery connector with charging capabilities. It\'s almost **TOO** powerful for our purposes, but it conveniently has everything we need.

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

### MicroSD Shield

The microSD shield is an Arduino Uno layout compatible memory shield. We\'ll interact with the microSD shield using the SPI bus through the shield\'s on board hex converter. Quick note, since the microSD shield is an older component than the Turbo there are some communication bugs, but we\'ll get to that a little later.

[![SparkFun microSD Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/9/5/2/8/12761-05.jpg)](https://www.sparkfun.com/sparkfun-microsd-shield.html)

### [SparkFun microSD Shield](https://www.sparkfun.com/sparkfun-microsd-shield.html) 

[ DEV-12761 ]

Running out of memory space in your Arduino project? The SparkFun microSD Shield equips your Arduino with mass-storage capabi...

[ [\$17.95] ]

### SAM-M8Q Chip Antenna GPS Breakout and Qwiic Micro OLED

It\'s worth mentioning once more the components carried across from the last tutorial. The SAM-M8Q Chip Antenna GPS provides simple and powerful GPS capabilities from Ublox\'s GPS systems. Those coordinates are then displayed to the user on the easy to wire, and no solder required, Qwiic Micro OLED screen.

[![SparkFun GPS Breakout - Chip Antenna, SAM-M8Q (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/4/8/15210-SparkFun_GPS_Breakout_-_Chip_Antenna__SAM-M8Q__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gps-breakout-chip-antenna-sam-m8q-qwiic.html)

### [SparkFun GPS Breakout - Chip Antenna, SAM-M8Q (Qwiic)](https://www.sparkfun.com/sparkfun-gps-breakout-chip-antenna-sam-m8q-qwiic.html) 

[ GPS-15210 ]

The SparkFun SAM-M8Q GPS Breakout is a high quality GPS board with equally impressive configuration options.

[ [\$43.95] ]

[![SparkFun Micro OLED Breakout (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/6/2/1/14532-SparkFun_Micro_OLED_Breakout__Qwiic_-01.jpg)](https://www.sparkfun.com/products/14532)

### [SparkFun Micro OLED Breakout (Qwiic)](https://www.sparkfun.com/products/14532) 

[ LCD-14532 ]

The SparkFun Qwiic Micro OLED Breakout is a Qwiic enabled version of our popular MicroView and micro OLED display!

**Retired**

## Hardware Hookup

This part of the build will require some assembly (but that\'s what we\'re all really here for anyway). Since most of our components carry over from the simple push button GPS tracker tutorial, we only have a few additional parts to assemble. Now, if you\'re fresh to the GPS tracker projects you don\'t have to worry. We\'ll run through all of it again anyway.

### Assembly

#### Push Button Wiring

Our push button will be rather straightforward. The table below shows the connections between the button and our Turbo via the microSD shield.

[![push button terminal hookup](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/2/button_hookup.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/2/button_hookup.png)

  Button Pin   RedBoard Pin
  ------------ ---------------
  \+           5V
  \-           GND
  C1           **GND**
  NO1          Digital Pin 2

These pins will connect to the Turbo pins (via the microSD shield PTH pins) as shown in the fritzing diagram above

#### MicroSD Shield

The first step would be to solder our break away headers to the pins aligning with the Redboard Turbo female headers. We also need to solder the 2x3 Female ISP connector to the bottom of the microSD shield. We\'ll use that ISP header for a modification needed for communication.

I mentioned earlier that there was a special note for communication between the Turbo and our microSD shield. The best explanation currently is there is a naming difference in libraries and the SERCOM tools used on the Turbo. We can easily circumvent the issue by hardwiring our Digital Pins (13 -11) to the ISP header found on all our Redboards.

[![microSD communication soldering](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/microSDHotwire2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/microSDHotwire2.jpg)

I discovered this issue when I was running a simple datalogger sketch and I kept getting a false return from the `SD.begin()` call. After making these hotwiring corrections, I got correct functionality.

Once we\'re done with the headers, we can move on to connecting our pushbutton. Following the table mentioned earlier, we need to solder our wires to the microSD shield. There are PTH holes alongside all the header holes to solder to. We\'re looking for these specific pins:

[![pushbutton pins](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/microSDHotwire2_highlightedPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/microSDHotwire2_highlightedPins.jpg)

  Button Pin   microSD Shield Pin
  ------------ --------------------
  \+           5V
  \-           GND
  C1           **GND**
  NO1          Digital Pin 2

#### Reference Diagrams

[![Hookup of Button to Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/4/Fritzing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/Fritzing.jpg)

[![Hookup of Turbo, GPS, and Display](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/4/TurboGPSFritzing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/TurboGPSFritzing.jpg)

### Optional Assembly

#### Aluminum Case

We do have an aluminum case added to the required materials list. While it is optional, it provides a sturdy case for practical application purposes. If you purchase the case then you\'ll have to make extra modifications. We\'ll need to drill screw holes and protuding areas for our OLED screen and GPS chip antenna.

[![Full assembly with aluminum case](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/4/GPS_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/GPS_Tutorial-01.jpg)

## Software Setup

**Note:** This code/library has been written and tested on Arduino IDE version 1.8.9. Otherwise, make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Component Libraries

**Note:** At the time of writing, this tutorial used the [SparkFun Ublox Arduino Library v1](https://github.com/sparkfun/SparkFun_Ublox_Arduino_Library). The library has been depreciated. For the latest version that is supported, feel free to download the [SparkFun u-blox GNSS Arduino Library](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library). Make sure to [follow the steps to migrate when using the latest library](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library#migrating-to-v20).

First let\'s start with the two libraries for our Qwiic Micro OLED Breakout and SAM-M8Q Chip Antenna GPS Module.

[SparkFun Micro OLED Library (ZIP)](https://github.com/sparkfun/Micro_OLED_Breakout/archive/master.zip)

[SparkFun Ublox Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library/archive/master.zip)

Add these libraries using the Include Library option under the Arduino IDE option \"Sketch\".

[![How to add a .zip library in Arduino](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/AddZipLibraries.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/AddZipLibraries.png)

### Turbo Specialties

The Turbo does require some extras before we can program. Those are all done through the SAMD Arduino Libraries. Open **Tools** -\> **Board: \" \"** -\> **Boards Manager\...** and find the following:

[![Boards Manager with SAMD](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/4/Screen_Shot_2019-06-12_at_10.49.57_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/Screen_Shot_2019-06-12_at_10.49.57_PM.png)

*Arduino SAMD21 board files are needed, version 1.6.21 specifically*

After the main Arduino board files are installed, we\'ll need the Sparkfun specific boards. For those we\'ll need to copy and paste the following in our Arduino \"Additional Boards Manager URLs\" preferences. Copy and paste:

    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/master/IDE_Board_Manager/package_sparkfun_index.json

[![Boards Manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/0/4/Screen_Shot_2019-06-12_at_10.50.17_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/9/0/4/Screen_Shot_2019-06-12_at_10.50.17_PM.png)

*We want Sparkfun SAMD21 board files of version 1.6.1 (or newest available)*

If you need reminders for what you\'re looking for later down the road, the code in the next section will have all required software components listed in the comments.

### Google Earth and KML

Off the bat, if you need to download [Google Earth](https://www.google.com/earth/versions/#earth-pro). See you in a minute, no worries.

With that out of the way, KML is starkly different from the Arduino C or MicroPython we usually see here. It's very similar to HTML used for websites. If you're not familiar with the Hyper Text Markup Language, don't worry because I'll give you a rough (and I mean rough) overview of what we're trying to achieve with it.

#### HTML

HTML mostly is a file with text (or images, or videos, or whatever black magic websites use nowadays) that is formatted using sectioning tags. Tags act like boxes, what's in a box is owned by the box.

For example, in our code, we'll see a tag called Placemark. In Google Earth, we will see our placemarks as yellow pins on the globe. If we save a placemark as follows:

``` xml

    
         12.345678, 123.456789 
    
```

Then we've made a box called placemark with the GPS values inside. When Google Earth reads this a yellow pin will be placed on that exact coordinate. There are many more useful tags and tools for KML files. If you want to dive deeper, please feel free to visit the [Google Developers page for KML](https://developers.google.com/kml/documentation/kml_tut). All of that is, in essence, what we're trying to achieve.

## Example Code

The code below is nothing fancy and doesn\'t have clever algorithms. There are many places within that can be improved for performance and efficiency. My hope was to allow a novice programmer to read and understand the big picture of what we\'re trying to do. From there improvements can and should be made!

Feel free to download the code from the [GitHub location](https://github.com/will2055/SFE_GPS_Tracker_Tutorial/), or by clicking on the button below:

[Download GPS Tracker Tutorial Example Code](https://github.com/will2055/SFE_GPS_Tracker_Tutorial/archive/master.zip)

Alternatively, you can copy and paste the code from here:

    language:c
    /******************************************************************************
    Google Earth KML GPS Position Logger v1.7
    brandon.williams@sparkfun.com
    May 6, 2019

    The user will press a momentary button to log a GPS location into a KML file, 
    a file that's stored on a microSD card in the microSD shield. If the user holds 
    the button for 5 seconds, the program will effectively "end" with an infinite 
    while loop after safely closing the file. The user can then remove the memory 
    card to retrive the file and open using Google Earth.

    ** Significant changes and improvements can be made, please enjoy mod-ing! **

    Resources:
    SFE MicroOLED library: SFE_MicroOLED.h
    SFE u-blox GNSS library: //http://librarymanager/All#SparkFun_u-blox_GNSS 
    Arduino SD required libraries: SPI.h & SD.h

    Download Google Earth: https://www.google.com/earth/versions/

    Development environment specifics:
    Arduino IDE 1.8.9
    Board Definition Packages:
      Arduino SAMD board Boards (32-bits ARM Cortex-M0+) 1.6.21
      SFE SAMD Boards 1.6.1
    ******************************************************************************/
    //SD Shield libraries
    #include <SPI.h>
    #include <SD.h>
    //OLED and Ublox libraries
    #include <Wire.h>
    #include <SFE_MicroOLED.h>
    #include <SparkFun_u-blox_GNSS_Arduino_Library.h> //http://librarymanager/All#SparkFun_u-blox_GNSS

    #define PIN_RESET 9   //OLED
    #define DC_JUMPER 1   //OLED

    //create objects
    SFE_UBLOX_GNSS myGNSS;
    MicroOLED oled(PIN_RESET, DC_JUMPER);
    File dataFile;

    //declare global variables
    const int buttonPin =  2;
    const int chipSelect = 8; //Specific for SFE microSD shield, differs from Arduino SD libraries
    int buttonState = 0;

    void setup() 
      oled.setCursor(0,0);
      oled.clear(PAGE);
          //Oh yea! don't forget the GPS shield needs to get it's first fix
      oled.print("Revving up the GPS unit, please wait");
      oled.display();
      delay(29000);
      oled.setCursor(0,0);
      oled.clear(PAGE);
      oled.print("Ready to start!");
      oled.display();
      oled.clear(PAGE);
      oled.display();

    }

    void loop() 
            buttonState = digitalRead(buttonPin);
            if(buttonState == LOW && state == 1)

            }

          }
        }
      }
    }

Upload the code using your Arduino IDE, and with any luck you\'ll start seeing coordinates across your OLED screen!