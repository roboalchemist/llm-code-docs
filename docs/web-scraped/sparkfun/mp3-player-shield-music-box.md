# Source: https://learn.sparkfun.com/tutorials/mp3-player-shield-music-box

## Tardis Music Box Project

Got a few favorite things that you need to keep safe? A custom music box is a fun project to house anything ranging from necklaces to sonic screwdrivers. In this tutorial, you will see the basic instructions and parts used in making this fan-made Doctor Who TARDIS (Time and Relative Dimension in Space) music box. This can be used as a starting point for your own music box, TARDIS, or mischievous creation.

[![Tardis Music Box Closed](https://cdn.sparkfun.com/r/600-600/assets/7/6/d/3/2/5150bf06ce395fac7c000000.jpg)](https://cdn.sparkfun.com/assets/7/6/d/3/2/5150bf06ce395fac7c000000.jpg)

[![Tardis Music Box Open ](https://cdn.sparkfun.com/r/600-600/assets/d/5/6/d/d/5150bf06ce395f157b000000.jpg)](https://cdn.sparkfun.com/assets/d/5/6/d/d/5150bf06ce395f157b000000.jpg)

### Suggested Reading

Here is a list of other tutorials you might find helpful while following this tutorial:

- [MP3 Player Shield](https://www.sparkfun.com/tutorials/295)
- [Mono Audio Amplifier Quickstart Guide](https://www.sparkfun.com/tutorials/392)
- [LED Current Limiting Resistors](https://www.sparkfun.com/tutorials/219)
- [Arduino Main Board Quickstart Guide](https://www.sparkfun.com/tutorials/182)

## Parts List

You will also need a box of some sort. This is where the fun starts! You can use tons of different types of materials ranging from wood to plastic. For this project, a laser cutter was used to make cut-outs from soft wood. A crafter knife would have worked too.

## Circuit Diagram

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/3/8/5/a/2/5150bf06ce395f4578000000.png)](https://cdn.sparkfun.com/assets/3/8/5/a/2/5150bf06ce395f4578000000.png)

You will need to put the reed switch near the opening doors of your box/case, and a magnet on the other side, so when the box is closed the magnet and the reed switch are right next to each other. Based on your project, you may consider different types of switches instead of a [reed switch](http://en.wikipedia.org/wiki/Reed_switch). If you have a smaller box, you might want to check out the other sound modules we carry. For example: an [Audio-Sound Breakout - WTV020SD](https://www.sparkfun.com/products/11125?) with an [Arduino Pro Mini 3.3V](https://www.sparkfun.com/products/11114?) as the development board. Please keep in mind when changing the parts to get the appropriate motors and power supply.

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Before uploading code, make sure to install the SFEMP3 library.

[GitHub SFEMP3 Library](https://github.com/madsci1016/Sparkfun-MP3-Player-Shield-Arduino-Library)

When you are ready, copy the following code and upload it to your Arduino!

    language:c
    //SFEMP3Library author Bill Porter
    //SFEMP3Library author Michael P. Flaga
    /* MP3 Player Shield Music Box Code Example:
      SparkFun Electronics, Pamela, 1/24/2013
      Beerware License

      Hardware Connections:
      -LED = D3 on MP3 Player Shield;
      -Motor = D5 on MP3 Player Shield;
      -Reed Switch = D4 on MP3 Player Shield;
      -Mono Audio Amp Breakout Board Shutdown Pin = D10 on MP3 Player Shield;
      You will need to solder header pins to the MP3 Player Shield.
      Put the shield on top of an Arduino Uno.

      Usage:
      When the door opens, the motor will spin and a sound file will play.
      The sound file will loop.
      Then when the door closes the motor stops spinning and a new track plays one time. */

    #include <SPI.h>

    //Add the SdFat Libraries
    #include <SdFat.h>
    #include <SdFatUtil.h>
    //and the MP3 Shield Library
    #include <SFEMP3Shield.h>

    SFEMP3Shield MP3player;

    int led = 3;
    int motor = 5;
    int reedSwitch = 4;
    int speaker = 10;

    int fadeAmount = 5;
    int brightness = 0;
    boolean active = false;

    void setup() 

    void loop() 
      else if (digitalRead(reedSwitch) == LOW && active)//when door closing
      
      else if (digitalRead(reedSwitch) == LOW) //while door is closed
      
      else
      
        brightness += fadeAmount;
      }

      delay(100);
    }

## See it in Action!

As with any DIY project, you should always customize and tweak what you want for maximum awesomeness!

There was a lot of lessons learned in this Demo Project. The biggest one is to have patience with the wood glue. As you can see little nails were used in place due to lack of time/patience. If you are making a project like this one as a gift with limited time, remember to KISS! (Keep It Simple, Stupid!)