# Source: https://learn.sparkfun.com/tutorials/vernier-photogate

## Introduction

In this project tutorial, we will show you how to create a cheap but accurate photogate (similar to the one pictured below) for use in classroom applications, particularly physics experiments.

[![alt text](https://cdn.sparkfun.com/assets/1/6/e/d/d/51a7b078ce395f5a12000002.jpg)](https://cdn.sparkfun.com/assets/1/6/e/d/d/51a7b078ce395f5a12000002.jpg)

This project started as part of a [grant](http://www.aps.org/programs/education/highschool/teachers/pair.cfm) I co-authored for my classroom. The grant, called *Physics and Instructional Resource* (PAIR), is designed to help support physics teachers in need of content or material resources. The grant pairs together a classroom teacher with a physics professional to develop new materials and resources for the classroom. I had the idea of integrating an Arduino with and LCD screen to create a hand-held photogate timer like this one:

[![alt text](https://cdn.sparkfun.com/assets/6/f/b/2/a/51a7b786ce395faa11000003.jpg)](https://cdn.sparkfun.com/assets/6/f/b/2/a/51a7b786ce395faa11000003.jpg)

These smart timer units are costly (\$200-\$300 each), they require a power adapter, and the user interface is not customizable. With the flexibility and low cost of the Arduino platform, we set out to develop a unique solution that we could integrate into a [Physics First](http://en.wikipedia.org/wiki/Physics_First) program for freshman at the high school. Our school has access to a large supply of Vernier hardware and photogates, but but the use of these are restricted to the physics lab where we have computers to perform the data collection and analysis.

I was looking for a simple, portable device to interface these sensors. Using an Arduino seemed like a pretty straight-forward solution.

### Required Materials

If you would like to follow along an build your own photogate timer(s), you will need the following:

### Suggested Reading

This tutorial builds on several other concepts. Please familiarize yourself with the concepts below if you are familiar already.

- [What is an Arduino](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Arduino Comparison Guide](https://learn.sparkfun.com/tutorials/arduino-comparison-guide)
- [Powering Your Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [Buttons and Switches](https://learn.sparkfun.com/tutorials/button-and-switch-basics)
- [Light](https://learn.sparkfun.com/tutorials/light)

## Our First Prototype

[![alt text](https://cdn.sparkfun.com/assets/7/c/e/9/b/51a7bc49ce395f5a12000003.jpg)](https://cdn.sparkfun.com/assets/7/c/e/9/b/51a7bc49ce395f5a12000003.jpg)

Using a standard [Arduino UNO](https://www.sparkfun.com/products/11021), an [LCD screen](https://www.sparkfun.com/products/709), and a pair of [Photo Interrepters](https://www.sparkfun.com/products/9299), we started with a proof of concept design.

This prototype was a great success. We modified stopwatch [code](http://danthompsonsblog.blogspot.com/2008/11/timecode-based-stopwatch.html) from Dan Thompson. Unfortunately, this prototype was far from ready to be put in the hands of kids. I still needed to find a cleaner, tighter solution. The first part I needed to replace were the small photo-interrupers (photogates) you see in this picture.

## Photogates

We started our original prototype design with these [photo-interrupters](http://www.amazon.com/gp/product/B005WMZHH2/ref=oh_details_o02_s00_i00?ie=UTF8&psc=1) that we found on Amazon. These little modules are great. They have 4 leads and there is a small IR LED on one side. The other side is an IR receiver.

[![alt text](https://cdn.sparkfun.com/assets/b/f/2/5/d/51ae43d5ce395f0a36000000.jpg)](https://cdn.sparkfun.com/assets/b/f/2/5/d/51ae43d5ce395f0a36000000.jpg)

The only drawback to using these devices is that the IR LED still needs a current limiting resistor. I figured that out the hard way! They aren\'t easy to mount, and they have a really small gate opening. Digging around in the closets at the school I discovered several drawers full of [photogates](http://www.vernier.com/products/sensors/vpg-btd/) from Vernier. I would guess that several other schools might be in the same situation.

[![alt text](https://cdn.sparkfun.com/assets/0/f/f/b/0/51ad82c8ce395f9352000000.jpg)](https://cdn.sparkfun.com/assets/0/f/f/b/0/51ad82c8ce395f9352000000.jpg)

These photogates are fantastic. The detectors each have a Schmidt trigger built in and a LED to indicate when the gate is broken. The only drawback is that Vernier has a special British Telecom connector on their devices. The photogate uses a left-hand version of this connector. We had an option to simply cut the ends off, but then these photogates would not be usable with the LabPro devices in our Physics lab. Thankfully, Vernier sells these [breadboard connectors](http://www.vernier.com/products/accessories/btd-elv/). Using these I could build an interface directly to an Arduino. I just had to figure out the sensor pin-outs.

## Sensor Pin-Outs

Vernier provides sensor pin-out definitions for their [British Telecom digital connector](http://www.vernier.com/support/sensor-pinouts/).

[![alt text](https://cdn.sparkfun.com/assets/1/5/7/6/4/51ae4756ce395fe335000001.jpg)](https://cdn.sparkfun.com/assets/1/5/7/6/4/51ae4756ce395fe335000001.jpg)

Looking for a cleaner LCD / Arduino shield solution, I stumbled across the [Serial-Enabled LCD kit](https://www.sparkfun.com/products/10097).

[![alt text](https://cdn.sparkfun.com/assets/e/a/8/9/4/51ae49f8ce395f1b36000000.jpg)](https://cdn.sparkfun.com/assets/e/a/8/9/4/51ae49f8ce395f1b36000000.jpg)

This is quite the misnomer for what it is. SparkFun has used a standard ATMega 328 chip controlling the serial-to-parallel interface. Basically, this is an Arduino with an LCD - no extra shield, and no extra frills needed. I called up some friends and we soldered up 8 of these guys in one night. While we were at it, we soldered on a right-angle male header to the side so that we could access the FTDI programming pins, too.

[![alt text](https://cdn.sparkfun.com/r/800-800/assets/6/5/0/d/4/51ae4b56ce395f9235000000.jpg)](https://cdn.sparkfun.com/assets/6/5/0/d/4/51ae4b56ce395f9235000000.jpg)

## Putting it all Together

I made several measurements for the LCD. Links to the drawing files can be found below. I added a couple buttons for mode/select, reset, and I cut holes on the side to access the FTDI programming pins.

### Cutting out the Case

- [LCD Window Cut-out](https://cdn.sparkfun.com/assets/0/f/1/0/4/51ae2751ce395f505d000002.pdf)
- [Case Cut-out Drawings](https://cdn.sparkfun.com/assets/7/0/9/2/6/51ae2656ce395f541b000000.pdf)

[![alt text](https://cdn.sparkfun.com/assets/5/a/c/e/0/51a7b078ce395f3511000003.jpg)](https://cdn.sparkfun.com/assets/5/a/c/e/0/51a7b078ce395f3511000003.jpg)

The initial grant stipulated we build up 8 of these units to test. So, I set up an assembly line to do this.

[![alt text](https://cdn.sparkfun.com/assets/4/8/0/f/3/51a7b078ce395f3012000000.jpg)](https://cdn.sparkfun.com/assets/4/8/0/f/3/51a7b078ce395f3012000000.jpg)

[![alt text](https://cdn.sparkfun.com/assets/2/d/9/c/9/51a7b078ce395f7012000003.jpg)](https://cdn.sparkfun.com/assets/2/d/9/c/9/51a7b078ce395f7012000003.jpg)

*A few screws, a little hot glue, and we\'re in business!*

I added an [LED button](https://www.sparkfun.com/products/10443) for the MODE switch and a [standard 12 mm push button](https://www.sparkfun.com/products/9190) for the RESET.

### The Wiring

Using some standard 18 AWG hook-up wire I connected up the Vernier BTD Connector, two [push buttons](https://www.sparkfun.com/products/9190), and added a [female barrel jack adaptor](https://www.sparkfun.com/products/10288) for power.

[![alt text](https://cdn.sparkfun.com/assets/d/3/c/b/7/51a7b078ce395f6511000002.jpg)](https://cdn.sparkfun.com/assets/d/3/c/b/7/51a7b078ce395f6511000002.jpg)

Since you probably can\'t tell where all of these wires are going, here is a simplified Fritzing diagram illustrating the connections.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/Vernier_PhotoGateBuild_bb_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/Vernier_PhotoGateBuild_bb_1.png)

Click [here](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/Vernier_PhotoGateBuild_2.fzz) for the Fritzing drawing.

### Assembly Complete

Here are the 8 fully assembled photogate timer units. Ready for programming.

[![alt text](https://cdn.sparkfun.com/assets/c/2/3/5/5/51a7b079ce395fb011000001.jpg)](https://cdn.sparkfun.com/assets/c/2/3/5/5/51a7b079ce395fb011000001.jpg)

## The Code

There are two primary uses for photogates in a physics classroom. The first mode - sometimes called *GATE mode* - shows the amount of time that the photogate is broken. The second mode is typically called *PULSE mode*. This mode will start the timer when the gate is first broken, and then stop the timer when the gate is broken again. This works great if you have daisy-chained photogates.

If you\'re interested, Vernier has a nice [Introduction to Photogate Timing Tutorial](https://cdn.sparkfun.com/assets/1/7/8/3/a/51ae30b5ce395f7b1b000000.pdf).

Starting with the initial code base we used with our prototype we integrated a MODE button to select between the various operations, and we also incorporated a RESET feature. The code is currently setup to support 3 modes of operation.

- Mode 1 - GATE Mode
- Mode 2 - PULSE Mode
- Mode 3 - Standard Stopwatch mode (start/stop using the MODE button)

Here\'s the latest version of the code that we developed, or you can download a copy [here](https://cdn.sparkfun.com/assets/5/7/4/1/6/52cb1ae2ce395fca138b456d.zip):

    language:c
    /*
      LCD Photogate Timer
      Written by:  Brian Huang
      Date:  05.06.13
      Sparkfun Electronics

     Code based on: http://danthompsonsblog.blogspot.com/2008/11/timecode-based-stopwatch.html
     Coded by: arduinoprojects101.com

     3 modes of operation:
       Mode 1:  Displays the time that the gate is broken.
       Mode 2:  Breaking the gate starts the timer, and breaking it again, stops the timer - for use with Vernier photogates daisy-chained together.
       Mode 3:  Standard Start/Stop Stopwatch.  Start & Stop triggered with the Mode Button.

    Future work to be done: 
       Store data into an array so that multiple instances of start/stop can be tracked. This can be used for measuring acceleration.

    */ 
    // include the library code:
    #include <LiquidCrystal.h>
    #include <EEPROM.h>

    int ledPin = 13;                    // LED connected to digital pin 13
    int gatePin = 10;                   // gate on pin 8
    int buttonPin = 12;                 // mode button

    int LEDstate = LOW;                    // previous value of the LED

    int gateState;                      // variable to store gate state
    int lastgateState;                  // variable to store last gate state

    int buttonState;                    // variable to store button state
    int lastButtonState;                    // variable to store button state

    int mode = 1;

    boolean refresh = false;                    // condition for refresh - timer is timing

    int frameRate = 1000;               // the frame rate (frames per second) at which the stopwatch runs - Change to suit
    long interval = 1;                  // blink interval
    long previousMillis = 0;            // variable to store last time LED was updated
    long startTime ;                    // start time for stop watch
    long elapsedTime ;                  // elapsed time for stop watch

    long dataBuffer[127]= 
    ;                  // elapsed time for stop watch
    int dataIndex=0;

    int fractional;                     // variable used to store fractional part of Frames
    int fractionalSecs;                 // variable used to store fractional part of Seconds
    int fractionalMins;                 // variable used to store fractional part of Minutes
    int fractionalHrs;                 // variable used to store fractional part of Minutes

    int elapsedFrames;                  // elapsed frames for stop watch
    int elapsedSeconds;                 // elapsed seconds for stop watch
    int elapsedMinutes;                 // elapsed Minutes for stop watch
    int elapsedHours;                   // elapsed Hours for stop watch

    char buf[10];                       // string buffer for itoa function

    // --- EEPROM ADDRESS DEFINITIONS
    #define LCD_BACKLIGHT_ADDRESS 1  // EEPROM address for backlight setting
    #define BAUD_ADDRESS 2  // EEPROM address for Baud rate setting
    #define SPLASH_SCREEN_ADDRESS 3 // EEPROM address for splash screen on/off
    #define ROWS_ADDRESS 4  // EEPROM address for number of rows
    #define COLUMNS_ADDRESS 5  // EEPROM address for number of columns

    // --- SPECIAL COMMAND DEFINITIONS
    #define BACKLIGHT_COMMAND 128  // 0x80
    #define SPECIAL_COMMAND 254 // 0xFE
    #define BAUD_COMMAND 129  // 0x81

    // --- ARDUINO PIN DEFINITIONS
    uint8_t RSPin = 2;
    uint8_t RWPin = 3;
    uint8_t ENPin = 4;
    uint8_t D4Pin = 5;
    uint8_t D5Pin = 6;
    uint8_t D6Pin = 7;
    uint8_t D7Pin = 8;
    uint8_t BLPin = 9;

    char inKey;  // Character received from serial input
    uint8_t Cursor = 0;  // Position of cursor, 0 is top left, (rows*columns)-1 is bottom right
    uint8_t LCDOnOff = 1;  // 0 if LCD is off
    uint8_t blinky = 0;  // Is 1 if blinky cursor is on
    uint8_t underline = 0; // Is 1 if underline cursor is on
    uint8_t splashScreenEnable = 1;  // 1 means splash screen is enabled
    uint8_t rows = 2;  // Number rows, will be either 2 or 4
    uint8_t columns = 16; // Number of columns, will be 16 or 20
    uint8_t characters; // rows * columns

    // initialize the LCD at pins defined above
    LiquidCrystal lcd(RSPin, RWPin, ENPin, D4Pin, D5Pin, D6Pin, D7Pin);

    /* ----------------------------------------------------------
     In the setup() function, we'll read the previous baud,
     screen size, backlight brightness, and splash screen state
     from EEPROM. Serial will be started at the proper baud, the
     LCD will be initialized, backlight turned on, and splash
     screen displayed (or not) according to the EEPROM states.
     ----------------------------------------------------------*/

    void setup()
    

    /*----------------------------------------------------------
     ----------------------------------------------------------*/
    void loop()
    
        else
        
      }

      switch(mode)
      

        // check for a high to low transition if true then found a new button press while clock is running - stop the clock and report
        else if (gateState == HIGH && lastgateState == LOW && refresh == true)
        else
          lastgateState = gateState;                  // store gateState in lastgateState, to compare next time
          if ((millis() - previousMillis > interval) & (refresh == true )) 
          
        break;

      case 2:
        if (gateState == LOW && lastgateState == HIGH  &&  refresh == false)
        

        // check for a high to low transition if true then found a new button press while clock is running - stop the clock and report
        else if (gateState == LOW && lastgateState == HIGH  &&  refresh == true)
        

        else
        

        if ((millis() - previousMillis > interval) & (refresh == true)) 
        
        break;
      case 3:
        Serial.print(buttonState);
        Serial.print("\t");
        Serial.print(lastButtonState);
        Serial.print("\t");
        Serial.println(refresh);
        delay(100);

        if ((buttonState == LOW) && (lastButtonState == HIGH)  &&  (refresh == false))
        

        // check for a high to low transition if true then found a new button press while clock is running - stop the clock and report
        else if ((buttonState == LOW) && (lastButtonState == HIGH)  &&  (refresh == true))
        
        else
        

        if ((millis() - previousMillis > interval) & (refresh == true)) 
            
        break;
      }
      // check for a low to high transition if true then found a new button press while clock is not running - start the clock    
    }

    void displayElapsedTime()
    

      lcd.print(itoa(fractionalMins, buf, 10));   // convert the int to a string and print a fractional part of 60 Minutes to the LCD
      lcd.print(":");                             //print a colan. 

      if (fractionalSecs < 10)
      

      lcd.print(itoa(fractionalSecs, buf, 10));   // convert the int to a string and print a fractional part of 60 Seconds to the LCD
      lcd.print(".");                             //print a colan. 

      if (fractional < 100)
      

      if (fractional < 10)
      
      lcd.print(itoa((fractional), buf, 10));  // convert the int to a string and print a fractional part of 25 Frames to the LCD
    }

    void setBacklight(uint8_t backlightSetting)
    

    /* ----------------------------------------------------------
     setBaudRate() is called from SpecialCommands(). It receives
     a baud rate setting balue that should be between 0 and 10.
     The baud rate is then set accordingly, and the new value is
     written to EEPROM. If the EEPROM value hasn't been written
     before (255), this function will default to 9600. If the value
     is out of bounds 10<baud<255, no action is taken.
     ----------------------------------------------------------*/
    void setBaudRate(uint8_t baudSetting)
    
      if ((baudSetting>=0)&&(baudSetting<=10))
        EEPROM.write(BAUD_ADDRESS, baudSetting);
    }

[![alt text](https://cdn.sparkfun.com/assets/8/2/0/8/f/51a7b078ce395fb710000000.jpg)](https://cdn.sparkfun.com/assets/8/2/0/8/f/51a7b078ce395fb710000000.jpg)