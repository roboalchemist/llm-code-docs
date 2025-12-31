# Source: https://learn.sparkfun.com/tutorials/badgerhack-synth-add-on-kit

## Introduction

The BadgerStick that you received by visiting a SparkFun booth at one of the various events we\'ve attended can be hacked to perform a wide variety of tasks. It can even make music, depending on your definition of music.

[![BadgerHack](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/badgerboard-02_tag.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/badgerboard-02_tag.png)

This tutorial will guide you through turning your BadgerStick into a little noise-making circuit that\'s easy to build, easy to program, and easy to alter and make your own!

[![BadgerStick with Synth Add-on](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/9/Screenshot_from_2016-02-15_11_57_56.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/9/Screenshot_from_2016-02-15_11_57_56.png)

*It looks a little messy, but it sounds pretty\... okay, it doesn\'t sound pretty either, but it is a lot of fun!*

Follow along with this guide and you\'ll be making sweet noise in no time!

**NOTE:** The BadgerStick and RedStick are two different products. The BadgerStick (aka BadgerHack) originated as an event-only platform to aid SparkFun in teaching soldering and programming at events like Maker local Faires and SXSW. The [RedStick](https://www.sparkfun.com/products/13741) evolved from that concept and is the retail version of the BadgerStick, available for sale on SparkFun.com. All of the BadgerStick tutorials and expansion kits are compatible with both the BadgerStick and the RedStick, unless otherwise stated.

#### Required Materials

We will need a few other components to make this thing work:

As you can see, the parts count is pretty low and none of the components we\'ll be using are very sophisticated. The BadgerStick (or RedStick) is doing all of the heavy lifting here. We just need a few control surfaces and a speaker.\

### Suggested Reading

Before starting this tutorial, we highly recommend you work through the main BadgerHack guide first.

[](https://learn.sparkfun.com/tutorials/badgerhack)

### BadgerHack 

September 23, 2015

This tutorial shows users how to solder their SparkFun interactive badges as well as put them to use in other projects.

Additionally, if you are new to soldering or electronics, we recommend you check out the following:

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)
- [What is Electricity](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [What is a Circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

When you are ready to start hacking your badge, we definitely recommend reading:

- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

## Hardware Hookup

### Badger on a Breadboard

The BadgerStick is a great form factor for breadboard prototyping. If you have a fresh BadgerStick or RedStick out of the box, you can add male breakaway headers to both sides and sink it right into the breadboard over the gap. Make sure to add headers to **pins A0 through VCC** and **pins 2 through 9**. The holes on the BadgerStick are staggered so that the headers will stay in place while you solder them, simply snap off two strips of 8 headers and press them into place before securing them with a series of solder joints.

I\'m going to assume for the purposes of this tutorial, however, that you\'ve already assembled the BadgerStick into an interactive badge and therefore already have female right-angle headers installed on **pins 2 through 9**. You can use [male right angle headers](https://www.sparkfun.com/products/553) to mate your BadgerStick/RedStick to the breadboard instead of having to desolder those headers. Alternatively, you can desolder the headers and replace them with [straight male headers](https://www.sparkfun.com/products/116).

[![Solder pins to the BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-29.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-29.jpg)

*This picture isn\'t exactly right but you get the idea*

### A Jungle of Jumper Wires

A pack of jumper wires on our site contains 30 jumpers. Today, we\'re going to be using every single one of those. Start by placing all of your parts on the breadboard like this:

[![Place parts on the breadbaord](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/9/Synth_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/9/Synth_bb.jpg)

*Potentiometers, DIP Switch, and BadgerStick on Breadboard.*

The potentiometers in the above picture don\'t look like the ones I suggested in my wishlist, but they\'ll work the same way. Now, with the jumper wires, begin making the connections listed here:

+----------------------------+---------------------------------------+
| Connect this:              | To This:                              |
+============================+========================+====+====+====+
| DIP Switch Pins 1-8        | BadgerStick Pins 2-9   |    |    |    |
+----------------------------+------------------------+----+----+----+
| All Potentiometers\' Pin 1 | GND Rail of Breadboard |    |    |    |
+----------------------------+------------------------+----+----+----+
| All Potentiometers\' Pin 3 | VCC Rail of Breadboard |    |    |    |
+----------------------------+------------------------+----+----+----+
| All Potentiometers\' Pin 2 | BadgerStick A0-A3      |    |    |    |
+----------------------------+------------------------+----+----+----+
| Speaker Pin 1              | BadgerStick A4         |    |    |    |
+----------------------------+------------------------+----+----+----+
| Speaker Pin 2              | BadgerStick A5         |    |    |    |
+----------------------------+------------------------+----+----+----+
| GND Rail of Breadboard     | BadgerStick GND        |    |    |    |
+----------------------------+------------------------+----+----+----+
| VCC Rail of Breadboard     | BadgerStick VCC        |    |    |    |
+----------------------------+------------------------+----+----+----+

Once these connections have been made, your breadboard should look more or less like the image below. I did use a larger breadboard just so that there was enough room to clearly illustrate each jumper connection:

[![All jumper connections have been made on the breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/9/SynthAddon_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/9/SynthAddon_bb.jpg)

*All jumper connections have been made on the breadboard.*

That wraps up the hardware portion of this hack, let\'s go take a look at the code!

## Code

Plug the USB side of your BadgerStick into your computer. Make sure \"BadgerStick\" and the associated COM port are selected in the window below. Click \"Run on Arduino.\"

**Note:** If you have the Redstick, make sure to instead selecte \"Arduino Uno\" in the window below.

Copy the code below, and upload it through the Arduino IDE.

    language:c
    /*BadgerSynth Example Sketch
    February 2016

    Written by Nick Poole
    SparkFun Electronics

    Code is released under the MIT License.
    */
    #define SPEAKER A4
    #define POT_A A0
    #define POT_B A1
    #define POT_C A2
    #define POT_D A3

    int x = 2;
    int osc1 = 0;
    int osc2 = 0;
    int ran = 0;
    int tempo = 0;
    int note;
    bool event = 0;

    void setup() 

    }

    void loop()  // Iterate through each step on our DIP Switch

    for(int y = 0; y<tempo; y++)

    }
    else // If the DIP Switch is off, shut up for a step

    }

    x++; event = 0;

    }

This code steps through each pin on the DIP switch, reading the input to the BadgerStick. If a switch is open, the BadgerStick will make a noise based on the potentiometer inputs. Changing the potentiometers will change the random tones created by the BadgerStick.