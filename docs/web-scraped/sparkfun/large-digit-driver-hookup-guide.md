# Source: https://learn.sparkfun.com/tutorials/large-digit-driver-hookup-guide

## Introduction

Large numerical displays are a great addition to any project where you want to be able to see information at a distance. Scorekeepers and lap timers would be a great application for large 7-segment LED displays. The [Really Big 7-Segment Display (6.5\")](https://www.sparkfun.com/products/8530) fits that bill nicely. Driving several displays at the same time would be handy, which is where the [Large Digit Driver board](https://www.sparkfun.com/products/13279) comes in.

[![7-Segment Display - 6.5\" (Red)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/4/3/08530-05-L.jpg)](https://www.sparkfun.com/7-segment-display-6-5-red.html)

### [7-Segment Display - 6.5\" (Red)](https://www.sparkfun.com/7-segment-display-6-5-red.html) 

[ COM-08530 ]

No really - it\'s 6 inches (153mm) tall! This very large 7-segment display can be seen from a hundred feet away. So many proje...

[ [\$32.50] ]

[![SparkFun Large Digit Driver](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/0/4/13279-01.jpg)](https://www.sparkfun.com/sparkfun-large-digit-driver.html)

### [SparkFun Large Digit Driver](https://www.sparkfun.com/sparkfun-large-digit-driver.html) 

[ WIG-13279 ]

The SparkFun Large Digit Driver is a chainable controller backpack that can be soldered directly to the back of our large \[6....

[ [\$9.99] ]

[![HX711 Large Digit Driver board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-01.jpg)

The Large Digit Driver can be soldered directly to the bottom of the 7-Segment Display.

[![HX711 board attached to large 7 segment display](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-03.jpg)

Several Large Digit Drivers can be chained together to create a display with multiple digits.

[![HX711 boards chained together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-04.jpg)

### Covered in This Tutorial

In this tutorial, we will give you an overview of the Large Digit Driver and provide an example of hooking up the driver to an Arduino:

- [Board Overview](https://learn.sparkfun.com/tutorials/large-digit-driver-hookup-guide#board-overview) \-- To begin, we\'ll go over each of the pins on the breakout board and their function.
- [Hardware Hookup](https://learn.sparkfun.com/tutorials/large-digit-driver-hookup-guide#hardware-hookup) \-- In this section, we\'ll show you how to hook the Large Digit Driver up to an Arduino.
- [Example: One Large Digit](https://learn.sparkfun.com/tutorials/large-digit-driver-hookup-guide#example-one-large-digit) \-- Here, we give an example of an Arduino sketch to control one of the large 7-segment displays through the Large Digit Driver.
- [Example: Two Large Digits](https://learn.sparkfun.com/tutorials/large-digit-driver-hookup-guide#example-two-large-digits) \-- We show how to daisy chain two large 7-segment displays together and control them with two Large Digit Drivers.
- [Resources and Going Further](https://learn.sparkfun.com/tutorials/large-digit-driver-hookup-guide#resources-and-going-further) \-- This section gives some additional resources for getting more out of the Large Digit Driver.

### Materials Used

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. You will need a few components and tools to follow along with this tutorial. Here is the minimum parts needed for one 7-segment display.

For each additional digit you want to add, you will need:

- [7-Segment Display - 6.5\" (Red)](https://www.sparkfun.com/products/8530)
- [Large Digit Driver](https://www.sparkfun.com/products/13279)
- [Jumper Wire - 0.1\", 6-pin, 4\"](https://www.sparkfun.com/products/10366)

### Recommended Reading

Before getting started with the Large Digit Driver, there are a few concepts that you should be familiar with. Consider reading some of these tutorials before continuing:

- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino) \-- We will use an Arduino to control the Large Digit Driver
- [Shift Registers](https://learn.sparkfun.com/tutorials/shift-registers) \-- The Large Digit Driver uses a shift register to move data to each digit
- [How to Solder - Castellated Mounting Holes](https://learn.sparkfun.com/tutorials/how-to-solder-castellated-mounting-holes) \-- You will need to solder the Large Digit Driver to the back of the 7-segment LED display

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/shift-registers)

### Shift Registers 

An introduction to shift registers and potential uses.

[](https://learn.sparkfun.com/tutorials/how-to-solder-castellated-mounting-holes)

### How to Solder: Castellated Mounting Holes 

Tutorial showing how to solder castellated holes (or castellations). This might come in handy if you need to solder a module or PCB to another PCB. These castellations are becoming popular with integrated WiFi and Bluetooth modules.

## Board Overview

### Pin Descriptions

The Large Digit Driver has 6 input pins and 6 output pins.

[![Overview of HX711 board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-02.jpg)

  IN Pin   Description
  -------- ---------------------------------------------------------------
  GND      Connect to ground
  LAT      Data transfer in from SER on the rising edge of the latch pin
  CLK      Data transfer in from SER on the rising edge of the clock pin
  SER      Serial data in
  5V       Connect to power (5V)
  12V      Connect to power (12V)

\

  OUT Pin   Description
  --------- ----------------------------------------------------------------------------------------------
  GND       Connect to ground (used to provide a ground pin to the next Large Digit Driver in the chain)
  LAT       Connect to the LAT pin on the next Large Digit Driver in the chain
  CLK       Connect to the CLK pin on the next Large Digit Driver in the chain
  SER       Serial data out to the next Large Digit Driver
  5V        5V out to the next Large Digit Driver
  12V       12V out to the next Large Digit Driver

\

## Hardware Hookup

### Protect the Board

Before you attach the Large Digit Driver to the 7-segment display, you will need to isolate the exposed vias on the back of the board. Some of the Driver boards are created with through-hole vias that are not covered with solder mask. As a result, this could likely short out the traces on the back of the 7-segment display.

We recommend using a piece of [electrical tape](http://www.amazon.com/3M-Electrical-75-Inch-66-Foot-0085-Inch/dp/B00004WCCP/ref=sr_1_1?s=industrial&ie=UTF8&qid=1441921229&sr=1-1&keywords=electrical+tape) or [high temperature tape](https://www.sparkfun.com/products/10687) to cover the vias on the back of the Driver board.

[![Cover vias with tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-tape.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-tape.jpg)

### Attach the Board

You will need to solder the Large Digit Driver to the back of the 7-segment display. Have the Driver\'s 10 pins facing toward the bottom of the large 7-segment display and lined up with the traces on the back of the 7-segment display. Follow the [Soldering Castellated Vias Guide](https://learn.sparkfun.com/tutorials/how-to-solder-castellated-mounting-holes) to solder all 10 of the castellations as well as the 2 castellations at the top of the board (these should be attached to the 12V line and are just for mechanical support).

[![Soldering pins on HX711 Large Digit Driver](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-05.jpg)

### Connect the Board

We will be using the Arduino\'s regulated 5V and unregulated 12V (from the wall adapter) to power the 7-segment display and Large Digit Driver.

Connect the Large Digit Driver to the the following pins on the Arduino.

[![Fritzing of Large Digit Driver connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Hookup_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Hookup_bb.png)

Large Digit Driver

Arduino

GND

GND

LAT

5

CLK

6

SER

7

5V

5V

12V

VIN

\

## Example: One Large Digit

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Load the Single Digit Example Code

Plug your Arduino into your computer via USB cable. Open up the Arduino program and copy in the following sketch.

    language:c
        /*
     Controlling large 7-segment displays
     By: Nathan Seidle
     SparkFun Electronics
     Date: February 25th, 2015
     License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

     The large 7 segment displays can be controlled easily with a TPIC6C594 IC. This code demonstrates how to control
     one display.

     Here's how to hook up the Arduino pins to the Large Digit Driver

     Arduino pin 6 -> CLK (Green on the 6-pin cable)
     5 -> LAT (Blue)
     7 -> SER on the IN side (Yellow)
     5V -> 5V (Orange)
     Power Arduino with 12V and connect to Vin -> 12V (Red)
     GND -> GND (Black)

     There are two connectors on the Large Digit Driver. 'IN' is the input side that should be connected to
     your microcontroller (the Arduino). 'OUT' is the output side that should be connected to the 'IN' of addtional
     digits.

     Each display will use about 150mA with all segments and decimal point on.
    */

    //GPIO declarations
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    byte segmentClock = 6;
    byte segmentLatch = 5;
    byte segmentData = 7;

    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    void setup()
    
    }

    void loop()
    

    //Takes a number and displays 2 numbers. Displays absolute value (no negatives)
    void showNumber(float value)
    

      //Latch the current segment data
      digitalWrite(segmentLatch, LOW);
      digitalWrite(segmentLatch, HIGH); //Register moves storage register on the rising edge of RCK
    }

    //Given a number, or '-', shifts it out to the display
    void postNumber(byte number, boolean decimal)
    

      if (decimal) segments |= dp;

      //Clock these bits out to the drivers
      for (byte x = 0 ; x < 8 ; x++)
      
    }

### Run

Upload the sketch to your Arduino, and plug the 12V adapter into the Arduino.

[![Provide 12V to the Arduino to power the large 7 segment display](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-06.jpg)

Flip the 7-segment display over. You should see it count the digits 0-9 (the decimal point will appear on 9).

[![Single digit powered by HX711](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-07.jpg)

## Example: Two Large Digits

### Attach a Second Digit

Use the 6-pin jumper wire to attach a second 7-segment display to the first display unit. Make sure that you connect GND of the OUT on the first display to the GND of the IN on the second display, LAT of the OUT on the first display to the LAT of the IN on the second display, and so on.

[![Chaining HX711 boards together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-04.jpg)

*You will want to connect the Large Digit Driver on the right to the Arduino as per the [Hardware Hookup section](https://learn.sparkfun.com/tutorials/large-digit-driver-hookup-guide#hardware-hookup).*

### Load the Two Digit Example Code

Make sure the Arduino is plugged into your computer using a USB cable. Copy the following sketch into the Arduino program.

    language:c
        /*
     Controlling large 7-segment displays
     By: Nathan Seidle
     SparkFun Electronics
     Date: February 25th, 2015
     License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

     This code demonstrates how to post two numbers to a 2-digit display usings two large digit driver boards.

     Here's how to hook up the Arduino pins to the Large Digit Driver IN

     Arduino pin 6 -> CLK (Green on the 6-pin cable)
     5 -> LAT (Blue)
     7 -> SER on the IN side (Yellow)
     5V -> 5V (Orange)
     Power Arduino with 12V and connect to Vin -> 12V (Red)
     GND -> GND (Black)

     There are two connectors on the Large Digit Driver. 'IN' is the input side that should be connected to
     your microcontroller (the Arduino). 'OUT' is the output side that should be connected to the 'IN' of addtional
     digits.

     Each display will use about 150mA with all segments and decimal point on.

    */

    //GPIO declarations
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    byte segmentClock = 6;
    byte segmentLatch = 5;
    byte segmentData = 7;

    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    void setup()
    

    int number = 0;

    void loop()
    

    //Takes a number and displays 2 numbers. Displays absolute value (no negatives)
    void showNumber(float value)
    

      //Latch the current segment data
      digitalWrite(segmentLatch, LOW);
      digitalWrite(segmentLatch, HIGH); //Register moves storage register on the rising edge of RCK
    }

    //Given a number, or '-', shifts it out to the display
    void postNumber(byte number, boolean decimal)
    

      if (decimal) segments |= dp;

      //Clock these bits out to the drivers
      for (byte x = 0 ; x < 8 ; x++)
      
    }

### Run

Upload the sketch to your Arduino, and plug in the 12V supply. The 7-segment display (now two digits!) should count from 00 to 99.

[![Powering 2 digits from the HX711 Large Digti Driver](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/Large_Digit_Driver_Tutorial-08.jpg)

## Example: Speed Trap

To demonstrate the displays we built a device that measures the distance from the wall to a human. As that distance changes we can caculate speed. We present: The SparkFun Speed Trap!

[![Speedtrap on wall](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/8/SpeedTrap.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/8/SpeedTrap.jpg)

*Note the handprints from people running into the wall*

Here is a list of parts you\'ll need:

You can find the code and the PCB layout for the Speed Trap [here](https://github.com/sparkfun/Speed_Trap). You don\'t need the custom PCB, it\'s fairly easy to build just with jumpers and a bit of soldering. You can also use the ATX power connector in the wishlist to save some time when using the 12V/5V power supply.

    language:c
    /*
     Displaying instantaneous speed from a LIDAR on two large 7-segment displays
     By: Nathan Seidle
     SparkFun Electronics
     Date: January 5th, 2015
     License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

     The new LIDAR-Lite from PulsedLight is pretty nice. It outputs readings very quickly. From multiple distance
     readings we can calculate speed (velocity is the derivative of position).

     Here's how to hook up the Arduino pins to the Large Digit Driver backpack: 
     Arduino pin 5 -> LAT
     6 -> CLK
     7 -> SER
     GND -> GND
     5V -> 5V
     VIN/Barrel Jack -> External 12V supply (this should power the LDD as well)

     You'll also need to connect the LIDAR to the Arduino:
     Arduino 5V -> LIDAR 5V
     GND -> GND
     A5 -> SCL
     A4 -> SDA
    A0 -> Enable

    */

    #include <Wire.h> //Used for I2C

    #include <avr/wdt.h> //We need watch dog for this program

    #define    LIDARLite_ADDRESS   0x62          // Default I2C Address of LIDAR-Lite.
    #define    RegisterMeasure     0x00          // Register to write to initiate ranging.
    #define    MeasureValue        0x04          // Value to initiate ranging.
    #define    RegisterHighLowB    0x8F          // Register to get both High and Low bytes in 1 call.

    //GPIO declarations
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    byte statLED = 13; //On board status LED
    byte en_LIDAR = A0; //Low makes LIDAR go to sleep, high is normal operation

    byte segmentLatch = 5; //Display data when this pin goes high
    byte segmentClock = 6; //Clock one bit on each rising/falling edge
    byte segmentSerial = 7; //Serial data in

    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    long lastTime = 0;
    long lastReading = 0;
    int lastDistance = 265;
    float newDistance;

    const byte numberOfDeltas = 8;
    float deltas[numberOfDeltas];
    byte deltaSpot = 0; //Keeps track of where we are within the deltas array

    //This controls how quickly the display updates
    //Too quickly and it gets twitchy. Too slow and it doesn't seem like it's responding.
    #define LOOPTIME 50

    int maxMPH = 0; //Keeps track of what the latest fastest speed is
    long maxMPH_timeout = 0; //Forget the max speed after some length of time

    #define maxMPH_remember 3000 //After this number of ms the system will forget the max speed

    void setup()
    

      showSpeed(42); //Test pattern

      delay(500);

      /*postNumber('c', false);
      postNumber(' ', false);
      digitalWrite(segmentLatch, LOW);
      digitalWrite(segmentLatch, HIGH); //Register moves storage register on the rising edge of RCK
      delay(2000);*/

      wdt_reset(); //Pet the dog
      wdt_enable(WDTO_250MS); //Unleash the beast
    }

    void loop()
    

      //Take a reading every 50ms
      if (millis() - lastReading > (LOOPTIME-1)) // 49)
        

        //Insert this new delta into the array
        if(safeDelta)
        

        //Get average of the current deltas array
        float avgDeltas = 0.0;
        for (byte x = 0 ; x < numberOfDeltas ; x++)
          avgDeltas += (float)deltas[x];
        avgDeltas /= numberOfDeltas;

        //22.36936 comes from a big coversion from cm per 50ms to mile per hour
        float instantMPH = 22.36936 * (float)avgDeltas / (float)LOOPTIME;

        instantMPH = abs(instantMPH); //We want to measure as you walk away

        ceil(instantMPH); //Round up to the next number. This is helpful if we're not displaying decimals.

        if(instantMPH > maxMPH)
        
        else //maxMPH is king
        

        if(millis() - maxMPH_timeout > maxMPH_remember)
        

        Serial.print("raw: ");
        Serial.print(newDistance);
        Serial.print(" delta: ");
        Serial.print(deltaDistance);
        Serial.print(" cm distance: ");
        Serial.print(newDistance * 0.0328084, 2); //Convert to ft
        Serial.print(" ft delta:");
        Serial.print(abs(avgDeltas));
        Serial.print(" speed:");
        Serial.print(abs(instantMPH), 2);
        Serial.print(" mph");
        Serial.println();
      }

    }

    //A watch dog friendly delay
    void petFriendlyDelay(int timeMS)
    
    }

    //Get a new reading from the distance sensor
    int readLIDAR(void)
    
      else
      
    }

    //Takes a speed and displays 2 numbers. Displays absolute value (no negatives)
    void showSpeed(float speed)
    

      //Latch the current segment data
      digitalWrite(segmentLatch, LOW);
      digitalWrite(segmentLatch, HIGH); //Register moves storage register on the rising edge of RCK
    }

    //Given a number, or '-', shifts it out to the display
    void postNumber(byte number, boolean decimal)
    

      //The method uses 7954 bytes
      /*if(number == 1) segments = b|c;
      if(number == 2) segments = a|b|d|e|g;
      if(number == 3) segments = a|b|c|d|g;
      if(number == 4) segments = f|g|b|c;
      if(number == 5) segments = a|f|g|c|d;
      if(number == 6) segments = a|f|g|e|c|d;
      if(number == 7) segments = a|b|c;
      if(number == 8) segments = a|b|c|d|e|f|g;
      if(number == 9) segments = a|b|c|d|f|g;
      if(number == 0) segments = a|b|c|d|e|f;
      if(number == ' ') segments = 0;
      if(number == 'c') segments = g | e | d;
      if(number == '-') segments = g;*/

      if (decimal) segments |= dp;

      for (byte x = 0 ; x < 8 ; x++)
      
    }

    //Sometimes the LIDAR stops responding. This causes it to reset
    void disableLIDAR()
    

    void enableLIDAR()
    

    //Takes an average of readings on a given pin
    //Returns the average
    int averageAnalogRead(byte pinToRead)
    

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[SparkFun Forums](https://forum.sparkfun.com/)

### Can the Large 7-Segment Displays Work Outside?

For long term installations, we do not recommend installing the large digit outside under extreme weather conditions (especially in the heat). Additionally, it can be hard to view the LEDs in direct sunlight during the afternoon.

If you do use the large 7-segment displays outside, we recommend using red plexiglass to improve on the visibility. It would be better to have it under a tent or shadow when viewing the digits outside.