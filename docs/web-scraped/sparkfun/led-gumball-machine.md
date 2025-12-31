# Source: https://learn.sparkfun.com/tutorials/led-gumball-machine

## Introduction

Do you need an LED? The answer is always yes. But what if you need one right **now**? Build yourself an LED gumball machine and never run out again!

[![Gumball machine filled with LEDs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-06.jpg)

*Approximately 3,000 red 5mm LEDs ready to blink*

This machine was created for the [BTU Lab](http://btulab.com/) at CU Boulder because students constantly needed LEDs but filling parts bins always seemed to fall to the [tragedy of the commons](https://en.wikipedia.org/wiki/Tragedy_of_the_commons). We'd put 1,000 LEDs into the bin and they'd be gone in less than 2 weeks.

[![Dispensing LEDs](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine_Demo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine_Demo.gif)

With the LED Gumball dispenser the LEDs last for more than a semester. It's amazing how much a 15 second pause will cause people to think twice.

### Suggested Reading

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial)

### Hobby Servo Tutorial 

Servos are motors that allow you to accurately control the rotation of the output shaft, opening up all kinds of possibilities for robotics and other projects.

[](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40)

### SparkFun Inventor\'s Kit Experiment Guide - v4.0 

The SparkFun Inventor\'s Kit (SIK) Experiment Guide contains all of the information needed to build all five projects, encompassing 16 circuits, in the latest version of the kit, v4.0a.

And if you really want to get geeky, have a look at this posting on [state machines](https://www.sparkfun.com/news/1801). State machines are a good way to change between the states \'wait for user to press button\' to \'ignore buttons and don\'t dispense right now\'.

## Hardware Overview

Here's the list of parts for this project:

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Servo - Generic High Torque Continuous Rotation (Standard Size)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/1/1/09347-1.jpg)](https://www.sparkfun.com/servo-generic-high-torque-continuous-rotation-standard-size.html)

### [Servo - Generic High Torque Continuous Rotation (Standard Size)](https://www.sparkfun.com/servo-generic-high-torque-continuous-rotation-standard-size.html) 

[ ROB-09347 ]

Here, for all your mechatronic needs, is a simple, high quality continuous rotation servo motor. This servo is able to take i...

[ [\$20.50] ]

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![SparkFun ProtoShield Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/1/2/13820-SparkFun_ProtoShield_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-protoshield-kit.html)

### [SparkFun ProtoShield Kit](https://www.sparkfun.com/sparkfun-protoshield-kit.html) 

[ DEV-13820 ]

The SparkFun ProtoShield Kit lets you customize your own Arduino shield using whatever circuit you can come up with and then ...

[ [\$14.95] ]

[![Metal Pushbutton with Wires - Momentary (16mm, Red)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/4/4/6/11966-Metal-Pushbutton-Feature.jpg)](https://www.sparkfun.com/metal-pushbutton-momentary-16mm-red.html)

### [Metal Pushbutton with Wires - Momentary (16mm, Red)](https://www.sparkfun.com/metal-pushbutton-momentary-16mm-red.html) 

[ COM-11966 ]

This is a perfect choice if you are in need of a heavy duty push button! These metal push buttons are a very tough, small, pa...

[ [\$8.95] ]

A [proto shield](https://www.sparkfun.com/products/13820) works great. We used an [old shield](https://www.sparkfun.com/products/retired/9598) we had lying around but you can use any shield that has a few GPIO broken out that you can solder to.

You'll of course need a gumball machine. We haven't verified the continuous servo works with different brands but we're pretty confident this [Gumball Machine](https://www.candymachines.com/Bubble-Machine-Single-Stand-P124.aspx) will work with this tutorial.

### Tools

The tools for this project are pretty common. You may or may not have the various tools around so double check that you have access to the follow:

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

[![Wire Strippers - 22-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/0/14762-Wire_Strippers-03.jpg)](https://www.sparkfun.com/products/14762)

### [Wire Strippers - 22-30AWG](https://www.sparkfun.com/products/14762) 

[ TOL-14762 ]

These are your basic, run-of-the-mill wire strippers from Techni-Tool with a comfortable grip making them an affordable optio...

**Retired**

### Continuous Rotation Servo

The magic of the LED Gumball Machine is the fact that a continuous rotation servo mates utterly fantastically with the dispensing cogs within the machine.

[![Head of servo lining up with cogs on bottom of bowl](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-02.jpg)

A [high torque continuous rotation servo](https://www.sparkfun.com/products/9347) is just the ticket for getting electronic control of the dispenser mechanism.

Most servos come with a variety of *control horns*. These are the plastic bits of different shapes that you screw into the servo to connect the servo to your application. In this tutorial we'll want the star control horn (highlighted below). Out of complete luck, this horn has roughly the same pitch as the teeth on the gumball machine.

[![Various servo control horns](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine_-_Continuous_Servo_Horns-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine_-_Continuous_Servo_Horns-2.jpg)

The servo has quite a lot of torque and we want that applied to the dispenser mechanism. We mounted the servo with zip ties and hot glue. First, use zip ties to roughly mount the servo in place. Once you get the alignment between the servo head and dispenser gear use hot glue to solidify everything in place. This combination creates the right combination of rough alignment and rigidity so that as much of the torque from the servo is transferred to the dispenser.

[![Mounted servo with zip ties and hot glue](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-04.jpg)

### Button

We chose a [momentary light up button](https://www.sparkfun.com/products/11966).

[![Single button where knob should be](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-01.jpg)

This fit superbly into the existing hole where the twist knob originally resided. Once mounted, it was a small matter to figure out which pins illuminated the LED and which pins shorted together when the button was pressed.

[![Wiring behind the momentary button](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine_-_Button_Wiring2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine_-_Button_Wiring2.jpg)

### RedBoard

To tie it all together we used a [RedBoard](https://www.sparkfun.com/products/15123) and an old [MIDI shield](https://www.sparkfun.com/products/retired/9598). The MIDI part is not important. Instead, the row of breakout pins at the edge of the board made it easy to solder the handful of wires from the servo and button onto the board and then plug the shield onto the RedBoard.

[![All parts wired together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-03.jpg)

This was a more resilient connection method than point soldering to the SMD pads on the I/O of the RedBoard. We could have also used a the [Proto Shield](https://www.sparkfun.com/products/13820) or an [Arduino Pro Mini](https://www.sparkfun.com/products/11113) but we had these parts lying around.

[![RedBoard with shield connected to servo and button](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine_-_RedBoard_Wiring2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine_-_RedBoard_Wiring2.jpg)

### Power

The servo requires a fair amount of current at 5V so we used [5V 2A wall supply](https://www.sparkfun.com/products/12889). The power cable was routed up through the pedestal column and through the mounting plates to plug into the Arduino.

### Gumball Machine

Obviously you're going to need a gumball machine.

[![Gumball machine filled with LEDs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-01.jpg)

These are amazing little machines that are well designed for rough use and easy maintenance. We aren't charging money for the LEDs so we used the area where quarters usually get stored for our electronics.

[![Cavity showing electronics inside machine](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-04.jpg)

Be sure to get a machine with a metal base and a hollow post. The metal base makes your installation last much longer (students are only slightly less tough on equipment than hyenas) and the hollow post allows us to route power up through the base. I had to enlarge a few holes to ½" in order to allow the DC barrel plug through.

## Software

We want the gumball machine to dispense LEDs when the button is pressed, that's straightforward enough. But we want to avoid dispensing *all* the LEDs. Also, we don't want someone to stand in front of the free machine and continually hit the 'gimme' button. We implement a timeout of 15 seconds that prevents users from activating the servo constantly. You can get the software [here](https://github.com/sparkfun/LED_Gumball_Machine).

[GitHub: LED Gumball Machine](https://github.com/sparkfun/LED_Gumball_Machine)

### Dispensing with PWM

Almost all servos operate on [PWM](https://learn.sparkfun.com/tutorials/pulse-width-modulation). Before installing the continuous servo in our machine we found the servo responded in the follow ways:

- `gumballServo.write(95);` - Stops movement of continous servo
- `gumballServo.write(200);` - Servo turns CCW rapidly
- `gumballServo.write(10);` - Servo turns CW rapidly (but not used)

Our gumball dispenser was designed to operate clock wise so we only operate our servo counter clockwise.

[![Handful of LEDs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/0/LED_Gumball_Machine-06.jpg)

The dispenser was designed for gumballs obviously so when dispensing LEDs the number of LEDs that actually come out varies wildly. In general the user gets 1 to 5 LEDs when the servo is activated for 1 second. This works well. In the eventual case that LEDs fail to dispense, the user just has to wait 15 seconds to try again. Since we\'re not charging anything this is an acceptable outcome.

    language:c
    gumballServo.detach(); //Be sure the servo won't move

After dispensing we detach the servo. This turns off the PWM signal going to the servo guaranteeing the servo won\'t move. We noticed the servo jittered or moved very slowly at 90 (when it shouldn\'t be moving) so this extra step insures the LED Gumball Machine won\'t slowly disgorge itself onto the carpet overnight.

Along those same lines of concern, we noticed that the dispensing mechanism will sometimes bind up causing the servo to draw significantly more current for a short period of time. This can cause the power supply to shut down, causing the Arduino to reset. You\'ll see at the beginning of setup()

    language:c
    gumballServo.attach(GUMBALL_SERVO); //Be sure the servo won't move
    gumballServo.write(95); //Stop movement on continous servo
    gumballServo.detach(); //Be sure the servo won't move

The above code is the first thing the Arduino runs and insures any previous servo movement is stopped. This helps prevent weird rolling reset situations where the servo causes a brownout and as the Arduino comes back on line the servo begins moving, causing a brownout, etc\...

### Button Monitoring

The button shorts to ground when pressed so we use the internal pullups to pull the button pin high when the button is *not* pressed.

The button has a built in LED so we connect the +/- pins on the back of the button directly to a PWM enabled pin and Ground. The LED measured 12mA at 5V, well below the 20mA max so we didn\'t need a resistor.

    language:c
    //Check if we are allowed to dispense
    else if (millis() - lastDispenseTime < minTimeBetweenPresses)
    

In the code above, we check to see if enough time has passed since the last button press for us to vend again.

    language:c
    unsigned long minTimeBetweenPresses = 15 * 1000; //Make users wait this amount of ms between dispenses

We found 15 seconds (15,000 milliseconds) between vends was enough time to dissuade students from taking *all* the LEDs.