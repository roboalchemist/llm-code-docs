# Source: https://learn.sparkfun.com/tutorials/red-box-robot-hookup-guide

## Redbox Robot

Here at SparkFun, we get a lot of compliments on our red boxes. They\'re strong, stylish and hard to lose on a messy workbench. But, did you know that they also make pretty great robots? Okay, you can make a robot out of almost any box, but it won\'t be as stylish. This kit has everything you need to transform your favorite cardboard box into a robotic buddy!

[![Cyber Monday Redbox Robot](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/9/0/3/14062-02.jpg)](https://www.sparkfun.com/products/14062)

### [Cyber Monday Redbox Robot](https://www.sparkfun.com/products/14062) 

[ KIT-14062 ]

Bring one of our classic red boxes to life! We know that starting a robotics hobby can be expensive, so we wanted to put toge...

**Retired**

#### Kit Includes:

- [SparkFun RedStick](https://www.sparkfun.com/products/13741)
- [SparkFun Motor Driver \-- Dual TB6612FNG (1A)](https://www.sparkfun.com/products/9457)
- [Hook-up Wire \-- White (22 AWG)](https://www.sparkfun.com/products/8026)
- [Breadboard \-- Self-Adhesive (White)](https://www.sparkfun.com/products/12002)
- 2x [Break Away Headers \-- Straight](https://www.sparkfun.com/products/116)
- 3x [1500 mAh Alkaline Battery \-- AA](https://www.sparkfun.com/products/9100)
- [Battery Holder 3xAA with Cover and Switch](https://www.sparkfun.com/products/10891)
- [Mini Speaker \-- PC Mount 12mm 2.048kHz](https://www.sparkfun.com/products/7950)
- [Ultrasonic Sensor \-- HC-SR04](https://www.sparkfun.com/products/13959)
- [Hobby Gearmotor \-- 200 RPM (Pair)](https://www.sparkfun.com/products/13302)
- [Wheel \-- 65mm (Rubber Tire, Pair)](https://www.sparkfun.com/products/13259)
- [Super Bright LED \-- Red 10mm](https://www.sparkfun.com/products/8862)
- Double-Sided Tape (to attach motors to the box)

## Covered in This Tutorial

This tutorial will guide you through the assembly, wiring and programming of an obstacle-avoiding robot. You will need to have some basic soldering experience, and you\'ll need to cut a few holes in a cardboard box. Beyond that, you shouldn\'t need any special tools or technical skill.

## Materials Required

Besides the parts included in your kit, you\'ll need to following tools:

- [Soldering tools](https://www.sparkfun.com/categories/49), including an [iron](https://www.sparkfun.com/products/9507) and [solder](https://www.sparkfun.com/products/9325)
- Scissors or a [hobby knife](https://www.sparkfun.com/products/9200)
- [Wire Strippers](https://www.sparkfun.com/products/12630)
- Googly eyes and other adornments (optional)

### Suggested Reading

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one)

### Motors and Selecting the Right One 

Learn all about different kinds of motors and how they operate.

[](https://learn.sparkfun.com/tutorials/redstick-hookup-guide)

### RedStick Hookup Guide 

Learn about the SparkFun RedStick, a USB thumb drive-sized Arduino-compatible development platform.

[](https://learn.sparkfun.com/tutorials/tb6612fng-hookup-guide)

### TB6612FNG Hookup Guide 

Basic hookup guide for the TB6612FNG H-bridge motor driver to get your robot to start moving!

## Building the Chassis

Before we can start to wire our robot, we\'ll need to assemble the mechanical parts. Luckily, this robot is about as simple as it gets!

Empty out the box in which your kit came. That box is going to become the body for our robot. The included breadboard has a peel-and-stick backing, so let\'s start by sticking that to the topside of the box, along the hinged side of the box, near the center. In order to connect the rest of the parts, you\'ll need the strip of double-sided tape that came in your kit. Cut off about an inch of that tape, and use it to stick down the battery pack just below the breadboard, as pictured in the diagram below. Don\'t worry about the parts stuck into the breadboard just yet. We\'ll get to that after the mechanical portion is assembled.

[![Top down diagram of the robot chassis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/0/g103870.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/g103870.png)

*Click image for a closer look*

As you can see, there are a few places where it is suggested you cut a hole into the box so wires can be fed through. One hole that you can\'t see is underneath the battery case so you can access the power switch on the underside. Otherwise, you could just turn it to \"ON\" and leave it there. Two other such holes are found on the bottom of the box where we\'re going to attach the motors.

If you look at the hobby motors in the kit, you\'ll notice that there is an axle running through them so that a wheel can be pressed onto either side. You\'ll also notice that the wires are gathered on one side of the motor. It\'ll be easiest to wire the motors if you make sure that they\'re attached with the wires pointing in toward the middle of the box. Use the remaining length of double-sided tape to mount the motors on the bottom side, front corners of the box. Check out the diagram below for an idea of how it should look.

**Heads Up!** One side of the motor has a sticker on it. Make sure to remove that sticker before using double-sided tape to mount the motor because this sticker doesn\'t have as much grip as the tape included in your kit.

[![Bottom up diagram of the robot chassis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/0/g7439.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/g7439.png)

As there are only two motors on this robot, we\'ll need to add something on the backside to keep it from just dragging around. In this case, we\'re going to use a 10mm LED as a caster. Not only is this a nice, cheap way to keep your robot\'s backside off the ground, but it\'ll also allow us to add cool lighting effects! You shouldn\'t need to glue the LED into place; just poke it through the cardboard and splay the legs out as pictured below. Later, we\'ll solder a few wires to this LED, and that should hold it in place.

[![Diagram illustrating proper LED placement](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/0/0/g1038755.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/g1038755.png)

Once you have all the essentials taped into place, you can add some fun decoration to give your robot a little personality. Below, you can see that I\'ve glued down a pair of googly eyes and drawn on a derpy smile with a magic marker.

[![Completed robot chassis](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/14062-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/14062-01.jpg)

## Wiring the Motors

Now that our robot friend has a body (and maybe even a face) it\'s time to start wiring things together. To ease assembly, we\'ll be jumping everything together on a breadboard. Before we can do that, though, you\'ll need to solder headers to the RedStick and the Motor Driver Board. I won\'t cover that process here; if you\'re just getting started with soldering, then [check out this tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering). Once everything has headers attached, press the parts into your breadboard as pictured below. Pay close attention to how many rows are free on either side of the breadboard; you\'ll need them for the motor connections.

[![Parts placed on a breadboard](https://cdn.sparkfun.com/r/470-470/assets/learn_tutorials/6/0/0/g20562.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/g20562.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

Now that everything is in place, let\'s add jumper wires to complete our circuit. There\'s a spool of solid core wire included in your kit, which you\'ll [cut into short lengths and strip](https://learn.sparkfun.com/tutorials/working-with-wire) on either end. We\'re going to make a lot of connections here, so the diagram might get messy. To make things easier to follow, I\'ve broken it into stages. In case following a diagram isn\'t your flavor, I\'ve put together a table that outlines all of the connections. You can find it at the end of this section.

**Heads Up!** I\'ve colored the wiring in these diagrams to make them easier to follow. You only have one color of wire in your kit, but don\'t worry; the color doesn\'t matter.

[![wiring diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/0/g83409.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/g83409.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

A quick note about the connections above: the motors and battery pack come with wire leads attached, which you should be able to press directly into the breadboard without having to add your own wire.

[![wiring diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/0/g80910.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/g80910.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

Notice in the diagram above that there are two wires connected to the battery terminals on the RedStick. You may be tempted to connect these wires to VCC and GND instead, but don\'t do it! The battery connector actually passes through a booster circuit, so as your batteries drain, the RedStick won\'t power down prematurely.

[![wiring diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/0/g75900.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/g75900.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

  ---------------------- ------------------ --------------------
  **Motor Driver Pin**   **RedStick Pin**   **Other**
  VM                     Battery +          Battery Pack +
  VCC                    VCC                
  GND                    GND                Battery Pack -
  A01                                       Left Motor +
  A02                                       Left Motor -
  B01                                       Right Motor +
  B02                                       Right Motor -
  PWMA                   10                 
  AIN2                   4                  
  AIN1                   2                  
  STBY                                      Any VCC connection
  BIN1                   5                  
  BIN2                   7                  
  PWMB                   6                  
                         A4                 10mm LED Anode
                         GND                10mm LED Cathode
  ---------------------- ------------------ --------------------

## Making Moves

Now that you\'ve made all of the connections you need to get the motors running, let\'s get some code on that RedStick to spin our wheels! I\'m going to assume for the purposes of this section that you have some experience with Arduino programming and that you\'re already set up to load code onto the SparkFun RedStick. If you need a little help getting started, [check out this tutorial](https://learn.sparkfun.com/tutorials/redstick-hookup-guide).

In order to get code onto your RedStick, you will need to either remove it from the breadboard (carefully) or use a [USB extension cable](https://www.sparkfun.com/products/13309) to plug it into your computer\'s USB port.

The Arduino code below takes advantage of our library. If you are unfamiliar with installing an Arduino library, check out our [tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library).

Download the library using the link below, or grab the latest version from our [GitHub repository](https://github.com/sparkfun/SparkFun_TB6612FNG_Arduino_Library).

[TB6612FNG Arduino Library](https://github.com/sparkfun/SparkFun_TB6612FNG_Arduino_Library/archive/master.zip)

This example code will make your robot do a little dance. This is a great way to make sure you\'ve wired everything right so far. Besides, we\'ve been staring at this thing long enough; it\'s about time it did something!

    language:c
    /******************************************************************
    TestRun.ino
    TB6612FNG H-Bridge Motor Driver Example code
    Michelle @ SparkFun Electronics
    8/20/16
    https://github.com/sparkfun/SparkFun_TB6612FNG_Arduino_Library

    Uses 2 motors to show examples of the functions in the library.  This 
    causes a robot to do a little 'jig'.  Each movement has an equal and 
    opposite movement so assuming your motors are balanced the bot should 
    end up at the same place it started.

    Resources:
    TB6612 SparkFun Library
    *****************************************************************/

    // This is the library for the TB6612 that contains the class Motor and all the
    // functions
    #include <SparkFun_TB6612.h>

    // Pins for all inputs, keep in mind the PWM defines must be on PWM pins
    // the default pins listed are the ones used on the Redbot (ROB-12097) with
    // the exception of STBY which the Redbot controls with a physical switch
    #define AIN1 2
    #define BIN1 7
    #define AIN2 4
    #define BIN2 5
    #define PWMA 10
    #define PWMB 6
    #define STBY 9

    // these constants are used to allow you to make your motor configuration 
    // line up with function names like forward.  Value can be 1 or -1
    const int offsetA = -1;
    const int offsetB = -1;

    // Initializing motors.  The library will allow you to initialize as many
    // motors as you have memory for.  If you are using functions like forward
    // that take 2 motors as arguements you can either write new functions or
    // call the function more than once.
    Motor motor1 = Motor(AIN1, AIN2, PWMA, offsetA, STBY);
    Motor motor2 = Motor(BIN1, BIN2, PWMB, offsetB, STBY);

    void setup()
    

    void loop()
    

With this code compiled and running on your robot, you\'ve made the first step toward bringing your red box to life. You\'ve probably noticed, however, that it\'s a little clumsy. It just runs right into anything in its path! The next thing we\'re going to do is give it the ability to avoid those obstacles\...

## Avoiding Obstacles

Before we upload fresh code to take advantage of our robot\'s ultrasonic sensor, we\'ll need to wire the sensor to the RedStick. This sensor only requires four wires to work, and I\'ve highlighted them in the diagram below.

[![wiring diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/0/g90961.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/g90961.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

Once you\'ve added these wires, it\'s just a matter of uploading the example code below:

    language:c
    #include <SparkFun_TB6612.h>

    // these constants are used to allow you to make your motor configuration 
    // line up with function names like forward.  Value can be 1 or -1
    const int offsetA = -1;
    const int offsetB = -1;

    // Pins for all inputs, keep in mind the PWM defines must be on PWM pins
    // the default pins listed are the ones used on the Redbot (ROB-12097) with
    // the exception of STBY which the Redbot controls with a physical switch
    #define AIN1 2
    #define BIN1 7
    #define AIN2 4
    #define BIN2 5
    #define PWMA 10
    #define PWMB 6
    #define STBY 9

    // Initializing motors.  The library will allow you to initialize as many
    // motors as you have memory for.  If you are using functions like forward
    // that take 2 motors as arguements you can either write new functions or
    // call the function more than once.
    Motor motor1 = Motor(AIN1, AIN2, PWMA, offsetA, STBY);
    Motor motor2 = Motor(BIN1, BIN2, PWMB, offsetB, STBY);

    // Pins
    const int TRIG_PIN = 11;
    const int ECHO_PIN = 12;

    // Anything over 400 cm (23200 us pulse) is "out of range"
    const unsigned int MAX_DIST = 23200;

    void setup() 

    void loop() else
      delay(2500);}

      // Wait at least 60ms before next measurement
      delay(60);
    }

    // Coinflip function that randomly returns a 1 or 0
    bool flip()
      else
      
      return buf & 0x01;

    }

If everything is working correctly, your robot should be dodging obstacles. More specifically, if an object comes within 20 centimeters of the front of the robot, the robot will reverse direction and turn randomly before continuing on its way. This is a nice self-preservation instinct for a robot to have. However, if science fiction movies have taught me anything, a small robot needs a cute voice to survive.

## The Voice 

There\'s one more quick connection we\'ll need to make before your robot can whistle. Wire one side of the mini speaker to the A4 pin on the RedStick and wire the other side to ground as illustrated below.

[![wiring diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/0/g88447.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/g88447.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

The final update that we\'re going to make to our code today is to add a fun little function I call \"Whistle,\" which picks nine random frequencies and beeps them out in quick succession to approximate a sort of wordless interjection. It doesn\'t sound like much, but it adds a lot of personality.

    language:c
    #include <SparkFun_TB6612.h>

    // these constants are used to allow you to make your motor configuration 
    // line up with function names like forward.  Value can be 1 or -1
    const int offsetA = -1;
    const int offsetB = -1;

    // Pins for all inputs, keep in mind the PWM defines must be on PWM pins
    // the default pins listed are the ones used on the Redbot (ROB-12097) with
    // the exception of STBY which the Redbot controls with a physical switch
    #define AIN1 2
    #define BIN1 7
    #define AIN2 4
    #define BIN2 5
    #define PWMA 10
    #define PWMB 6
    #define STBY 9

    // Initializing motors.  The library will allow you to initialize as many
    // motors as you have memory for.  If you are using functions like forward
    // that take 2 motors as arguements you can either write new functions or
    // call the function more than once.
    Motor motor1 = Motor(AIN1, AIN2, PWMA, offsetA, STBY);
    Motor motor2 = Motor(BIN1, BIN2, PWMB, offsetB, STBY);

    // Pins
    const int TRIG_PIN = 11;
    const int ECHO_PIN = 12;

    // Anything over 400 cm (23200 us pulse) is "out of range"
    const unsigned int MAX_DIST = 23200;

    void setup() 

    void loop() else
      delay(2500);}

      // Wait at least 60ms before next measurement
      delay(60);
    }

    // Coinflip function that randomly returns a 1 or 0
    bool flip()
      else
      
      return buf & 0x01;

    }

    // Make a series of cute random beeping sounds
    int whistle()

Assuming everything has gone well, your robot should be whistling an adorable little tune every time it encounters an obstacle. Consider it the [Mouse Droid](http://starwars.wikia.com/wiki/MSE-6-series_repair_droid) for your personal Death Star. Or perhaps it\'s the first recruit for your robot army. Or maybe it\'s just something to keep you company at home. Hey, whatever floats your boat, we\'re not judging.

[![Completed robot chassis](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/14062-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/0/14062-01.jpg)