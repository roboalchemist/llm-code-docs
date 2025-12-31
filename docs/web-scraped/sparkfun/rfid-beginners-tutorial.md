# Source: https://learn.sparkfun.com/tutorials/rfid-beginners-tutorial

## Introduction

In this tutorial we\'ll show you how to make a remote \"clock punch\" that logs time, location, and identification.

[RFID](https://www.sparkfun.com/rfid) is as magic as waving a card in front of a little black box and doors open for all to pass. This technology is so versatile that it was projected in 2017 to support a \$31.42 billion market by 2023. We've enjoyed RFID tech as much as the next and we want to share it with you. In this tutorial we'll touch on some key topics of the technology. Then we'll work on making a remote work clock punch that can log time, location, and identification. Who knows, maybe you'll find your own magic in RFID as well.

[![Items we will be using in this tutorial.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/4/Remote_RFID_Logger-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/4/Remote_RFID_Logger-01.jpg)

### What Is RFID?

In simple terms, RFID Technology is a method of wireless communication between two (or more) electrical components. There is a reader that can emit a signal and passively reads incoming signals. Tags are devices that contain identification or other information. They come in two types, passive or active. Active tags have their own power source to actively transmit their contained information. Passive tags are 'powered' through radiated signals from the reader to transmit unique information. Either way it boils down to two devices yelling at each other like two cranky people. This transmission is how we'll pass this information to our microcontroller to log our \"in's and out's\".

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

#### Suggested Reading

Before going further, brave adventurer, please feel free to brush up on other tutorials and content that will help you on your journey.

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/rfid-basics)

### RFID Basics 

Dive into the basics of Radio Frequency Identification (RFID) technology.

[](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-rfid-idxxla-hookup-guide)

### SparkFun Qwiic RFID-IDXXLA Hookup Guide 

The Qwiic RFID ID-XXLA is an I2C solution that pairs with the ID-LA modules: ID-3LA, the ID-12LA, or the ID-20LA, and utilizes 125kHz RFID chips. Let\'s take a look at the hardware used for this tutorial.

[](https://learn.sparkfun.com/tutorials/sparkfun-gps-breakout-zoe-m8q-and-sam-m8q-hookup-guide)

### SparkFun GPS Breakout (ZOE-M8Q and SAM-M8Q) Hookup Guide 

The SparkFun ZOE-M8Q and SAM-M8Q are two similarly powerful GPS units but with different project applications. We\'ll compare both chips before getting each up and running.

[](https://learn.sparkfun.com/tutorials/displaying-your-coordinates-with-a-gps-module)

### Displaying Your Coordinates with a GPS Module 

This Arduino tutorial will teach you how to pinpoint and display your GPS coordinates with a press of a button using hardware from our Qwiic Connect System (I2C).

[](https://learn.sparkfun.com/tutorials/hookup-guide-for-the-sparkfun-redboard-artemis-nano)

### Hookup Guide for the SparkFun RedBoard Artemis Nano 

Get started with the powerful RedBoard Artemis Nano

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

## Hardware Overview

We\'ll be using the Artemis Nano to read the RFID tags and GPS modules. We will be using Arduino to program the Artemis nano. For more information about each component, click on the links to the product pages.

### [[[Artemis Nano]](https://www.sparkfun.com/products/15443)]

> \"With 1MB flash and 384k RAM you\'ll have plenty of room for your sketches. The Artemis module runs at 48MHz with a 96MHz turbo mode available and with Bluetooth to boot! The SparkFun Artemis Nano is an incredibly flexible device for a small footprint\...\"

### [[[Qwiic RFID Reader]](https://www.sparkfun.com/products/15191)]

> \"The SparkFun RFID Qwiic Kit is a simple, yet all-in-one I2C based RFID starting point for the ID-3LA, ID-12LA, and ID-20LA readers. Simply plug a reader into the headers and use a Qwiic cable to connect to any Qwiic enabled development board, then scan your 125kHz ID tag and the unique 32-bit ID will be shown on the screen.\"

### [[[SAM-M8Q - Chip Antenna]](https://www.sparkfun.com/products/15210)]

> \"The SparkFun SAM-M8Q GPS Breakout is a high quality, GPS board with equally impressive configuration options. The SAM-M8Q is a 72-channel GNSS receiver, meaning it can receive signals from the GPS, GLONASS, and Galileo constellations. This increases precision and decreases lock time and thanks to the onboard rechargable battery, you\'ll have backup power enabling the GPS to get a hot lock within seconds!\"

## Hardware Hookup

As far as the hardware is concerned, we're going to lean hard on the [Qwiic](https://www.sparkfun.com/qwiic) ecosystem. This ecosystem allows us to easily connect devices together without needing to solder. No mess, no fuss!

[![SparkFun Artemis Nano, Qwiic RFID Reader and Qwiic GPS connected together.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/4/Remote_RFID_Logger-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/4/Remote_RFID_Logger-04.jpg)

## Software

**Note:** This code/library has been written and tested on Arduino IDE version 1.8.12 . Otherwise, make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Our final code will be a mash up of two basic examples for our components. We'll take a quick look at each part of the examples that we'll use and talk about the main points.

### Qwiic RFID Reader

The Qwiic RFID library will give you the full functionality of the Qwiic RFID ID-XXLA without the hub bub of the I²C data transactions. Also included are examples codes to demonstrate the full functionality of the library. You can click the link below to download the file directly and install it manually, or navigate through the Arduino Library Manager by searching **SparkFun Qwiic RFID**. You can also go the [GitHub page](https://github.com/sparkfun/SparkFun_Qwiic_RFID_Arduino_Library) and get download it from there.

[SparkFun Qwiic RFID Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_RFID_Arduino_Library/archive/master.zip)

[![Qwiic RFID Reader connected to the SparkFun Artemis Nano](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/4/Remote_RFID_Logger-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/4/Remote_RFID_Logger-03.jpg)

[RFID: Example1 Read Tag Basics](https://github.com/sparkfun/SparkFun_Qwiic_RFID_Arduino_Library/blob/master/examples/Example1_Read_Tag_Basics/Example1_Read_Tag_Basics.ino)

In the Read_Tag_Basics example, the reader logs all tags that are recognized in a memory buffer. We read the buffer and clear it for a new read. We see that functionality below:

    language:c
    serialInput = Serial.read(); 
    if (serialInput == 49)

`Serial.read();` reads the buffer into the micro-controller\'s memory and clears the reader\'s buffer for another swipe. The tag is printed in the serial output along with the scan time. What we need to take away from this is the `Serial.read();` and `myRfid.getTag();`.

### SAM-M8Q GPS Module

**Note:** At the time of writing, this tutorial used the [SparkFun Ublox Arduino Library v1](https://github.com/sparkfun/SparkFun_Ublox_Arduino_Library). The library has been depreciated. For the latest version that is supported, feel free to download the [SparkFun u-blox GNSS Arduino Library](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) and adjust the libary name in the example code from `#include "SparkFun_Ublox_Arduino_Library.h"` to `#include "SparkFun_u-blox_GNSS_Arduino_Library.h"`.

The SparkFun U-blox Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun Ublox**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_Ublox_Arduino_Library):

[SparkFun U-blox Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Ublox_Arduino_Library/archive/master.zip)

[![SAM-M8Q GPS connected to the SparkFun Artemis Nano](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/4/Remote_RFID_Logger-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/4/Remote_RFID_Logger-02.jpg)

Using SparkFun's u-blox Arduino Library and Example2_NMEAParsing.ino, we'll get our GPS coordinates and time. If you look closely at the code below, you'll notice that something is missing:

    language:c
    long latitude_mdeg = nmea.getLatitude();
    long longitude_mdeg = nmea.getLongitude();

    Serial.print("Latitude (deg): ");
    Serial.println(latitude_mdeg / 1000000., 6);
    Serial.print("Longitude (deg): ");
    Serial.println(longitude_mdeg / 1000000., 6);

We're missing functions to get time. However, if we look at the [u-blox library header file](https://github.com/sparkfun/SparkFun_Ublox_Arduino_Library/blob/master/src/SparkFun_Ublox_Arduino_Library.h) we can see the following functions that we'll add in to the final code similarly to how the latitude and longitude functions are called in the example:

    language:c
    uint16_t getYear(uint16_t maxWait = getPVTmaxWait);
    uint8_t getMonth(uint16_t maxWait = getPVTmaxWait);
    uint8_t getDay(uint16_t maxWait = getPVTmaxWait);
    uint8_t getHour(uint16_t maxWait = getPVTmaxWait);
    uint8_t getMinute(uint16_t maxWait = getPVTmaxWait);
    uint8_t getSecond(uint16_t maxWait = getPVTmaxWait);

These functions will give us time. Now let\'s combine all our parts. The full code is below:

    language:c
    /******************************************************************************
    Remote Work Punch Clock
    brandon.williams@sparkfun.com
    May 6, 2019

    Description When a card is read then the GPS coordinates and time are read from
        the GPS module.

    Development environment specifics:
    Arduino IDE 1.8.12 (or most recent)

    Board Definition Packages (or most recent):
      SparkFun Apollo3 Boards           1.1.1
      MicroNMEA                         2.0.1
      SparkFun_Qwiic_Rfid.h             1.1.6
      SparkFun_u-blox_GNSS_Arduino_Library    2.0.2
    ******************************************************************************/

    #include <MicroNMEA.h>

    #include <SparkFun_Qwiic_Rfid.h>

    #include <SparkFun_u-blox_GNSS_Arduino_Library.h>//http://librarymanager/All#SparkFun_u-blox_GNSS

    #define RFID_ADDR 0x7D // Default Qwiic RFID I2C address

    // Variables and Constants
          /*GPS*/
    SFE_UBLOX_GNSS myGNSS;
    char nmeaBuffer[100];
    MicroNMEA nmea(nmeaBuffer, sizeof(nmeaBuffer));
          /*RFID*/
    Qwiic_Rfid myRFID(RFID_ADDR);
    String tag;
    float scanTime;
    int serialInput;

    void setup() 

    }

    void loop() 
            }
            else
          }
          delay(500);
        }
    }

    //This function gets called from the SparkFun Ublox Arduino Library
    //As each NMEA character comes in you can specify what to do with it
    //Useful for passing to other libraries like tinyGPS, MicroNMEA, or even
    //a buffer, radio, etc.
    void SFE_UBLOX_GNSS::processNMEA(char incoming)
    

When we swipe a card over the scanner then we should get something like below:

[![Serial Output RFID Tag Location](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/4/remote_worklog_screenshot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/4/remote_worklog_screenshot.png)

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.