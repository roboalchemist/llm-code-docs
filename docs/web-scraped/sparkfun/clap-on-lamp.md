# Source: https://learn.sparkfun.com/tutorials/clap-on-lamp

## Introduction

Perhaps you remember an \"As Seen on TV\" product known as \"The Clapper\" in the 1980s and 1990s. The [TV commercials](https://www.youtube.com/watch?v=Ny8-G8EoWOw) could be seen on almost every channel. The premise was simple: a 120 VAC relay would control power to appliances and respond to two sharp noises, specifically two claps. We\'re going to make our own version of this, but instead of controlling any appliance, we will operate a lamp chain using a servo.

### Required Materials

You can complete this project with parts from the [SparkFun Inventor\'s Kit v4.0](https://www.sparkfun.com/products/14265) and a [Sound Detector board](https://www.sparkfun.com/products/14262). Specifically, you will need:

- Lamp with pull chain
- [Electrical Tape](https://www.amazon.com/Electrical-Tape-several-colors-Black/dp/B003ZWN5ZM/)
- 1x [1 in. Hose Clamp](https://www.amazon.com/Precision-Brand-Miniature-Partial-Stainless/dp/B0036R4TDI/)
- 2x [Zip Ties](https://www.amazon.com/White-Nylon-Cable-Locking-2-5mm/dp/B000RB2DRK/)
- 1x [Paper Clip](https://www.amazon.com/Officemate-Small-Paper-Silver-97219/dp/B00K5WQSQ8/)

#### Tools Needed:

- Scissors
- [Screwdriver](https://www.sparkfun.com/products/9146) (included in the SIK v4.0)
- [Needle-Nose Pliers](https://www.sparkfun.com/products/8793)

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing:

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial)

### Hobby Servo Tutorial 

Servos are motors that allow you to accurately control the rotation of the output shaft, opening up all kinds of possibilities for robotics and other projects.

## Hardware Assembly

### Lamp Assembly

To start, we\'ll attach the servo to the lamp first. If you want to protect your lamp\'s finish, wrap some electrical tape around the post, covering about a 3-inch section.

[![Wrapping electrical tape around lamp](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/SIKv4_Projects-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/SIKv4_Projects-01.jpg)

Use a screwdriver to tighten the hose clamp around the post about 1 inch above the base. Note that you may need to adjust the position of the servo later so that it can effectively pull the chain. Leave a small gap on one side.

[![Attaching hose clamp to lamp](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/SIKv4_Projects-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/SIKv4_Projects-02.jpg)

Thread two zip ties through the gap in the hose clamp

[![Pulling zip ties through hose clamp](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/SIKv4_Projects-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/SIKv4_Projects-03.jpg)

Carefully pull the zip ties around the servo on either side of the flange. Pull the zip ties tight (you may need to use a set of needle-nose pliers).

[![Pulling zip ties through hose clamp](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/SIKv4_Projects-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/SIKv4_Projects-04.jpg)

Tighten the hose clamp as needed and cut the ends of the zip ties.

[![Cut ends of zip ties](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/SIKv4_Projects-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/SIKv4_Projects-05.jpg)

Using a screw, attach a servo arm to the servo\'s shaft. Make sure that the arm can rotate from pointing directly up to directly down, rotating away from the lamp\'s post. We\'ll use that motion to pull the lamp\'s chain.

[![Put servo arm on servo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/SIKv4_Projects-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/SIKv4_Projects-06.jpg)

Straighten out a paper clip, and bend a hook in one end using needle-nose pliers.

[![Bending paper clip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/SIKv4_Projects-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/SIKv4_Projects-07.jpg)

With the servo arm facing up, thread the hook through the outermost hole in the servo arm. Hold the other end of the paper clip up to the chain, and bend the paper clip so that it hooks onto the chain.

[![Attach other end of paper clip to chain](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/SIKv4_Projects-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/SIKv4_Projects-08.jpg)

Try rotating the servo to make sure that the chain is pulled fully to switch the lamp. This may require readjusting a second paper clip hook so that the chain is pulled successfully on each rotation.

[![Make sure that the servo pulls the chain](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/SIKv4_Projects-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/SIKv4_Projects-09.jpg)

### Circuit Diagram

Using jumper wires, connect the components as shown in the diagram below.

[![Clap on lamp Fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/5/Clap_On_Light_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/Clap_On_Light_bb.png)

*Having a hard time seeing the circuit? Click on the image for a closer look.*

## Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Copy and paste the following code in the Arduino IDE. Click **Upload** to send your compiled code to the Arduino.

    language:c
    /**
     * Clap On Light
     * Date: November 9, 2017
     * Author: Shawn Hymel (SparkFun Electronics)
     * 
     * Connect a servo to a lamp chain/switch to turn it on and off
     * with two successive claps (or other loud noises).
     * 
     * To complete this project, you will need parts from the
     * SparkFun Inventor's Kit v4.0: 
     * https://www.sparkfun.com/products/14265 as well as a sound
     * detector board: https://www.sparkfun.com/products/14262 along
     * with a lamp, electrical tape, hose clamp, zip ties, and a
     * paper clip.
     * 
     * This sketch was written by SparkFun Electronics, with lots of
     * help from the Arduino community. This code is completely free
     * for any use.
     */

    #include <Servo.h>

    // Pins
    const int SERVO_PIN = 9;
    const int SOUND_PIN = A0;

    // Constants
    const int THRESHOLD = 30;                           // Raw ADC
    const unsigned long TIMEOUT = 500;                  // ms
    const unsigned long TIME_BETWEEN_PULSES_MIN = 300;  // ms
    const unsigned long TIME_BETWEEN_PULSES_MAX = 1000; // ms
    const int PULSE_MIN = 40;                           // ms
    const int PULSE_MAX = 300;                          // ms
    const int SERVO_WAIT = 1000;                        // ms
    const int SERVO_CCW = 0;                            // deg
    const int SERVO_CW = 180;                           // deg

    // Globals
    unsigned long last_pulse_time = 0;
    Servo servo;

    void setup() 

    void loop() 

        last_pulse_time = pulse_time;
      }
    }

    // If the analog value is above the threshold, wait for it to
    // drop below the threshold and return the time it was above
    // the threshold. Return 0 if it's not above the threshold, and
    // return the timeout value if it stays above the threshold for
    // too long.
    unsigned long readPulse(int pin, int threshold, unsigned long timeout) 

      return t;
    }

    // Pull the lamp chain by moving the servo far counterclockwise,
    // wait 500 ms, and then move it far clockwise.
    void pullChain() 

### What You Should See

Clap twice near the sound detector with a pause of about 1/2 second between claps. The servo should activate and pull the chain to switch the light on. Clap twice again, and the lamp should turn off.

[![Clap twice to switch the lamp!](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/ILoveLamp.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/5/ILoveLamp.gif)