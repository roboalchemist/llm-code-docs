# Source: https://learn.sparkfun.com/tutorials/gps-shield-hookup-guide

## Introduction

The [SparkFun GPS shield](https://www.sparkfun.com/products/10710) has several convenient features that make it easy to use GPS modules with the [Arduino Uno](https://www.sparkfun.com/products/11224) and [SparkFun RedBoard](https://www.sparkfun.com/products/12757) (or any development board that supports the Arduino shield form factor).

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/full-shield.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/full-shield.jpg)

*A GPS Shield sporting a [UP501 GPS module](https://www.sparkfun.com/products/retired/10702), atop an Arduino Uno.*

### Assembly

Before use, you will need to solder headers to your shield. [Take a look at the Shield Assembly tutorial](https://learn.sparkfun.com/tutorials/arduino-shields#installing-headers-preparation) if you need a refresher. The GPS Shield uses the Uno R1 footprint with [2x 8-pin and 2x 6-pin headers](https://www.sparkfun.com/products/10007).

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/header-assembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/header-assembly.jpg)

### Required Materials

The [GPS Shield Kit](https://www.sparkfun.com/products/13199) comes with the shield, headers, an EM-506 GPS module and [foam tape](https://www.sparkfun.com/products/12752) for attaching the module to the shield.

If you purchased the GPS shield separately, you will need to acquire a GPS Module of your choice as well as the corresponding cables, headers or other connectors.

### Suggested Reading

If you haven\'t worked with GPS before, you may want to read the following tutorials before continuing with the GPS Shield.

- [GPS Basics](https://learn.sparkfun.com/tutorials/gps-basics) - If you\'ve always wanted to know how GPS works, this is the tutorial for you.

If you\'re not using Arduino or another microcontroller, you can still view the GPS module\'s serial output (and send commands to the GPS) using a terminal program.

- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [Serial Terminal Basics](https://learn.sparkfun.com/tutorials/terminal-basics)

## Shield Overview

The top of the GPS shield:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/shield-front1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/shield-front1.jpg)

and the bottom:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/shield-back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/shield-back.jpg)

The SparkFun GPS Shield includes a 6-pin JST-SH socket (labeled EM406 on the top) that fits both the [EM-506 (included with the GPS shield kit)](https://www.sparkfun.com/products/12751) and its discontinued predecessor the [EM-406A](https://www.sparkfun.com/products/retired/465) as well as the the [GP-635T](https://www.sparkfun.com/products/11571). There are exposed pins and a small prototyping area for use with [other GPS modules](https://www.sparkfun.com/products/8975). And there are unpopulated pads for the 5-pin JST-SH connector found on the discontinued [EM-408 module](https://www.sparkfun.com/products/retired/8234) (labeled EM408 on the top) .

The **UART/DLINE switch** connects the GPS module\'s serial lines to either Arduino hardware serial (D0/RX and D1/TX) or a user-selectable pair of software serial pins (D2 and D3 by default).

The closed solder jumpers marked **Dselect 2** and **3** determine which pins are used in DLINE mode.

ATMega328-based boards (like the Uno, Sparkfun RedBoard, and Sparkfun Pro Mini) support **change interrupts**, a hardware function that\'s necessary for software serial, on all digital pins. Arduino boards based on other chips (ATmega32u4, etc) have different levels of support for change interrupts and software serial. A list of software-serial compatible pins on various official Arduino boards is [here.](http://arduino.cc/en/Reference/softwareSerial)

The **ON/OFF switch** controls power to the GPS module. The **RESET** button connects to the Arduino underneath.

On the back of the shield, there is an unpopulated **[12mm coin cell battery holder](https://www.sparkfun.com/products/7948) footprint** for adding battery backup and warm start capabilities.

There is an additional unpopulated footprint for an 8-pin JST-SH connector as seen on the discontinued [85A GPS module](https://www.sparkfun.com/products/retired/8266).

The **BATT/3.3V jumper** connects the VBAT lines on the unpopulated JST connectors to either the (unpopulated) backup battery or to the Arduino\'s 3.3V line. 3.3V is selected by default.

## Code Example

For this example, you will need to install the [TinyGPSPlus library](https://github.com/mikalhart/TinyGPSPlus). Take a look at our [Arduino library install tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) if you\'ve never installed an Arduino library before.

[Download TinyGPSPlus Library](https://github.com/mikalhart/TinyGPSPlus/archive/master.zip)

Mikal Hart\'s Arduiniana.org [has a full overview](http://arduiniana.org/libraries/tinygpsplus/) of all of the capabilities of the TinyGPS++ library, but the most important one is parsing the GPS module\'s [NMEA sentence](https://learn.sparkfun.com/tutorials/gps-basics/message-formats) output into latitude and longitude.

Press your completed Arduino shield (with headers soldered and your GPS plugged in or soldered on) onto your Arduino, and connect your Arduino to your computer with your USB cable.

Make sure your DLINE/UART switch is in the DLINE position **every time you upload a sketch**, even if you\'re planning to use hardware serial. Having a GPS (or any other serial device) connected during upload will cause the upload to fail. If you want to use hardware serial, flip the switch back to UART after the upload finishes.

You will be using software serial for this example, so leave the switch in DLINE.

Upload the example sketch below to your Arduino.

    language:c
    #include <TinyGPS++.h>
    #include <SoftwareSerial.h>
    /*
     This example uses software serial and the TinyGPS++ library by Mikal Hart
     Based on TinyGPSPlus/DeviceExample.ino by Mikal Hart
     Modified by acavis
    */

    // Choose two Arduino pins to use for software serial
    // The GPS Shield uses D2 and D3 by default when in DLINE mode
    int RXPin = 2;
    int TXPin = 3;

    // The Skytaq EM-506 GPS module included in the GPS Shield Kit
    // uses 4800 baud by default
    int GPSBaud = 4800;

    // Create a TinyGPS++ object called "gps"
    TinyGPSPlus gps;

    // Create a software serial port called "gpsSerial"
    SoftwareSerial gpsSerial(RXPin, TXPin);

    void setup()
    

    void loop()
    
    }

    void displayInfo()
    
      else
      

      Serial.print(F("  Date/Time: "));
      if (gps.date.isValid())
      
      else
      

      Serial.print(F(" "));
      if (gps.time.isValid())
      
      else
      

      Serial.println();
    }

Open your Arduino [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) by going to Tools \> Serial Monitor

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/nmea_data.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/nmea_data.png)

Latitude, longitude, and time stamp values should be streaming by! You\'ll never get lost in front of your computer again!

## Using the GPS Breakout

If you are using a smaller Arduino like the [Pro Mini](https://www.sparkfun.com/search/results?term=pro+mini) you can use a [GPS Breakout](https://www.sparkfun.com/products/11818) instead of the GPS shield, though your selection of compatible modules is smaller than it is with the shield.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/gps-fritz.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/gps-fritz.jpg)

## Troubleshooting

#### \"No GPS Detected\" error

If you\'re using the EM-506 GPS from the GPS Shield Kit, make sure the JST-SH cable is firmly seated on both the module side and on the shield\'s socket.

Check that the serial select switch is in **DLINE**

Check that the shield\'s power switch is **ON**

If you\'re using an Arduino based on a chip other than the ATMega328, make sure you are using a pair of [software-serial compatible pins](http://arduino.cc/en/Reference/softwareSerial).

#### \"INVALID\" location, date, and time

`Location: INVALID Date/Time: INVALID INVALID`\
Give your GPS some time to get a fix. The EM-506 module shows a solid red light for no fix and flashes when the fix is successful.

If your module fails to get a fix after several minutes, try moving closer to a window or even outside. In severe cases, [such as in an **urban canyon**](https://learn.sparkfun.com/tutorials/gps-basics/gps-glossary) or inside a building with heavy concrete floors and ceilings, you may have to completely change locations.