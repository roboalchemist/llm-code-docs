# Source: https://learn.sparkfun.com/tutorials/reaction-timer

## Push It!

[Mental chronometry](http://en.wikipedia.org/wiki/Mental_chronometry) is the study of how fast humans react to different inputs. It takes a few hundred milliseconds for the signal to get from your eyes, to your brain, out to your limbs to respond. The reaction timer is a great project to demonstrate this time delay. It also makes for a fun game between friends!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/8/5/7/6/0/52c0ab60ce395f73218b4569.jpg)](https://cdn.sparkfun.com/assets/8/5/7/6/0/52c0ab60ce395f73218b4569.jpg)

*It took 178ms to hit the button!*

The principal of the reaction timer is simple: when the user sees the light turn on, press the button! A microcontroller is perfect for this because it can time milliseconds very accurately.

### Required Materials

Here\'s a list of parts used in this project:

- [RedBoard](https://www.sparkfun.com/products/11575)
- [Big Dome Push Button - Red](https://www.sparkfun.com/products/9181)
- [OpenSegment Serial Display - 20mm (Blue)](https://www.sparkfun.com/products/11647)
- [JST 3 Wire Assembly](https://www.sparkfun.com/products/9915)
- [Enclosure - Flanged (Red)](https://www.sparkfun.com/products/11366)
- [5V Wall Adapter](https://www.sparkfun.com/products/8269)

[Wishlist to all of these parts](http://sfe.io/w81757)

### Suggested Reading

This tutorial assumes you know a few things about Arduino and serial communication. If you\'re a bit rusty consider checking out these tutorials:

- [What is Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [Switch Basics](https://learn.sparkfun.com/tutorials/switch-basics)
- [Powering a Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [OpenSegment Hookup Guide](https://learn.sparkfun.com/tutorials/using-opensegment)

## Hardware

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/9/d/2/1/5/52c0ab5fce395fdb7f8b4567.jpg)](https://cdn.sparkfun.com/assets/9/d/2/1/5/52c0ab5fce395fdb7f8b4567.jpg)

*Guts of the Reaction Timer*

The hardware is really simple. The RedBoard is connected to a large [dome push button](https://www.sparkfun.com/products/9181) and an [OpenSegment](https://www.sparkfun.com/products/11647) four-digit display. OpenSegment has a spot for a [3-pin JST](https://www.sparkfun.com/products/9915), which makes it easy to connect on the fly. Checkout [this page](https://learn.sparkfun.com/tutorials/using-opensegment/serial-communication) on the OpenSegment tutorial for more info.

[![Fritzing diagram showing connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/7/6/Reaction_Timer_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/6/Reaction_Timer_bb.jpg)

The RedBoard has the following connections:

- Pin 2 -\> RX Pin on OpenSegment
- Pin 9 -\> Anode of LED within large dome button
- Pin 7 \<- The *normally open* (labeled NO) blade of the arcade switch

One input (the button) and two outputs (the LED in the button and the time display) is all you need! We used jumper wires and simply plugged them into the RedBoard.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/8/6/7/8/7/52cb20b7ce395fee778b4567.jpg)](https://cdn.sparkfun.com/assets/8/6/7/8/7/52cb20b7ce395fee778b4567.jpg)

*288ms is pretty slow!*

This hardy [red enclosure](https://www.sparkfun.com/products/11366) was used to withstand the endless button pounding. Cutting a hole for the dome button is pretty straight forward, and a dremel rotary tool easily cuts the slot for the [7-segment display](https://www.sparkfun.com/products/11647). The edges are not very clean, but it was a quick project. If you wanted to get fancy, a printed graphic/bezel combo would provide instructions and give plenty of polish.

A few holes were drilled on the face that points down to allow for a USB cable and a power cable. The RedBoard is hotglued in place, the display is hotglued into the slot, and jumper wires provide the necessary connections. If this timer was being installed outside of SparkFun, we would solder and screw everything down, but this timer has survived quite a lot of abuse already!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/7/7/4/c/2/52c0ab60ce395f4f738b456e.jpg)](https://cdn.sparkfun.com/assets/7/7/4/c/2/52c0ab60ce395f4f738b456e.jpg)

*The final install*

The unit can run off a battery pack for a few days, but, since we are permanently installing the timer near the kegerators at work, a [5V wall adapter](https://www.sparkfun.com/products/8269) provides all the power we need.

## Firmware

The code that runs the reaction timer is very straight forward. We simply illuminate a light and wait for the user to press the button. Download and install the example sketch.

[Reaction Timer Sketch Download](https://github.com/sparkfun/Reaction_Timer/archive/master.zip)

A timer counts how many milliseconds it requires for the (slow, slow) human to respond. And, because we don\'t want the human to cheat, we pick a random amount of time before we turn on the light.

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /*
     Reaction Timer for the World of Wonder Childrens museum in Lafayette, CO
     By: Nathan Seidle (SparkFun Electronics)
     Date: May 6th, 2013
     This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

     How to play:
     The button will be pulsing with light. Pressing the button will cause the light to turn off and the game will begin.
     After a few seconds of darkness, the light will light up and the user must press the button as fast as they can.
     Their reaction time is displayed on a 7 segment display.

     If the user presses the button before it is illuminated the display will show '-Err' to indicate error.

     */

    #include <SoftwareSerial.h>
    SoftwareSerial segmentDisplay(3, 2); //RX, TX to the OpenSegment display

    int LED = 9;
    int button = 7;

    long timeDiff; //Global variable keeps track of your score
    int idleLoops = 0;

    String gameTime; //Contains the last game time
    int gamesPlayed; //Contains the total number of games played for the life of the device

    //These functions allow the LED to be really bright when on, and
    //just barely on when the game is in idle mode
    #define LEDON() analogWrite(LED, 255)
    #define LEDLOW() analogWrite(LED, 10)
    #define LEDOFF() analogWrite(LED, 0)

    void setup()
    

    void loop()
    

        pulseTheButton(); //If no one is playing, pulse LED to intice them. Function takes 6 seconds to complete.

        idleLoops++;
        if(idleLoops > 9) //Play a screen saver every 60 seconds.
        
    }

    void playGame()
    
        }

        //Begin game
        Serial.println("Go!");
        LEDON();
        long beginTime = millis(); //Record this as the beginning of the test

        //Wait for user to hit the button
        while(digitalRead(button) == HIGH)
        
        }

        gameTime = String(timeDiff);

        //Right adjust the time
        if(timeDiff < 10)
            gameTime = "   " + gameTime;
        else if(timeDiff < 100)
            gameTime = "  " + gameTime;
        else if(timeDiff < 1000)
            gameTime = " " + gameTime;

        segmentDisplay.write('v'); //Reset the display
        segmentDisplay.print(gameTime); //Display the game time

        Serial.print("Reaction time:");
        Serial.println(gameTime);

        blinkButton(); //Blink the LED to indicate the end of the game

        //Record that we have played this game
        gamesPlayed++;
        Serial.print("This time played:");
        Serial.println(gamesPlayed);

        //After the game is complete, the display will show the gameTime for awhile
    }

    //If there is no game going on, pulse the LED on/off
    //If the user ever presses the button then return immediately
    //This function takes approximately 6 seconds to complete
    void pulseTheButton(void)
    

        //Fade LED off
        for(int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5)
        

        //Turn LED off for awhile
        for(int x = 0 ; x < 100 ; x++)
        
    }

    //Quickly blinks to button indicating the end of a game
    void blinkButton()
    
    }

    //Quickly scrolls the title across the display
    void scrollTitle()
    
        }

        segmentDisplay.write('v'); //Reset the display
        segmentDisplay.print(gameTime); //Display the last game time
    }

Load this code onto the RedBoard, and [open the terminal](https://learn.sparkfun.com/tutorials/terminal-basics) at 115200bps. You should see a series of debug statements such as \'Games Played\' and \'Err!\'.