# Source: https://learn.sparkfun.com/tutorials/light-seeking-robot

## Introduction

Euglena is a genus of single-celled organisms that live in bodies of fresh and salt water. Most species of Euglena have chloroplasts that are used for photosynthesis, much like plants. Additionally, most contain a single photoreceptor and eyespot, allowing the Euglena to track and move toward light sources. To learn more about Euglena, see [this Wikipedia page](https://en.wikipedia.org/wiki/Euglena). You can also see hundreds of Euglenas swimming around in [this video](https://vimeo.com/170849028).

To emulate Euglena behavior, we\'re going to make a light-seeking robot that moves toward areas of bright light. The SIK v4.0 only comes with one photocell (light sensor), which means that we will need to have our robotic \"organism\" turn left and right in order to detect the direction of brightest light.

### Required Materials

You can complete this project with parts from the [SparkFun Inventor\'s Kit v4.0](https://www.sparkfun.com/products/14265). Specifically, you will need:

You will also need (included in the SIK v4.0):

- Binder clip
- Velcro or Dual Lock fastener

#### Tools Needed:

- Scissors
- [Screwdriver](https://www.sparkfun.com/products/9146) (included in the SIK v4.0)

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing:

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/tb6612fng-hookup-guide)

### TB6612FNG Hookup Guide 

Basic hookup guide for the TB6612FNG H-bridge motor driver to get your robot to start moving!

## Hardware Assembly

To begin, make sure that your breadboard and Arduino are secured to the baseplate. Complete instructions for attaching both can be found [here](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/baseplate-assembly-).

[![Attaching Arduino to base plate](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/Baseplate4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/Baseplate4.jpg)

Using scissors, cut three strips of Dual Lock that are 1.25 inches (3.2cm) long and 1 inch (2.5cm) wide. Remove the adhesive backing, and attach two pieces to the corners under the baseplate and a third in the center.

[![Attaching dual lock to robot base plate](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/RobotAssemby2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/RobotAssemby2.jpg)

Cut two more strips that are 1.25 inches (3.175cm) long and ¾ inch (1.9cm) wide. Remove the adhesive backing, and attach the strips to the two motors. Be sure that your motors are **mirror images** of each other when you attach the Dual Lock.

[![Attach dual lock to motors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/RobotAssemby1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/RobotAssemby1.jpg)

Press the motors to the baseplate, connecting the two Dual Lock surfaces. Try to get the motors as straight as possible so your robot will drive straight.

[![Attach motors to robot base](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/RobotAssemby3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/RobotAssemby3.jpg)

The bottom of your baseplate should look like the image below. Remember that the two motors should be mirror images of each other.

[![Check your work](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/RobotAssemby4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/RobotAssemby4.jpg)

**Note:** The direction in which the motor wires face is arbitrary. Having them face out makes the circuit easier to build. Having them face in makes the circuit more robust against wires getting ripped out.

Attach the wheels by sliding them onto the plastic shafts on the gearmotor. The shaft is flat on one side, as is the wheel coupler. Align the two, and then press to fit the wheel onto the shaft.

[![Put wheels on motors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/RobotAssemby5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/RobotAssemby5.jpg)

Clip the binder clip onto the back end of the robot. This will act as a caster as the robot drives around.

[![Use a binder clip as a caster](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/RobotAssembly7.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/RobotAssembly7.jpg)

Cut a piece of Dual Lock that is about 1.25 inch x 1 inch (3.2cm x 2.5cm). Remove the adhesive backing and attach it to the back of the battery holder.

[![Attach dual lock to the battery pack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/BatteryPack1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/BatteryPack1.jpg)

Press the battery holder to the baseplate so that the two pieces of Dual Lock snap together. Insert the batteries into the holder if you have not done so already. Remember that batteries are polarized and can only go in one way.

[![Attach battery pack to robot base plate](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/RobotAssemby6.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/RobotAssemby6.jpg)

### Circuit Diagram

Using jumper wires, connect the components as shown in the diagram below.

[![Fritzing diagram of robot wiring](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/SIKv4_Light_Seeking_Robot_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/SIKv4_Light_Seeking_Robot_bb.png)

*Having a hard time seeing the circuit? Click on the image for a closer look.*

## Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

**Heads up!** Make sure your switch is in the OFF position. As soon as the code is finished uploading, your robot will begin driving. Make sure it cannot drive off a table or other high surface and injure itself.

Copy and paste the following code in the Arduino IDE. Click **Upload** and see what happens!

    language:c
    /**
     * Light Seeking Robot
     * Date: November 9, 2017
     * Author: Shawn Hymel (SparkFun Electronics)
     * 
     * 2-wheeled robot moves toward the brightest light by first
     * checking left, right, and center.
     * 
     * Parts for this project can be found in the SparkFun
     * Inventor's Kit v4.0: https://www.sparkfun.com/products/14265
     * 
     * This sketch was written by SparkFun Electronics, with lots of
     * help from the Arduino community. This code is completely free
     * for any use.
     */

    // Pins
    const int PWMB = 8; 
    const int BIN2 = 9;
    const int BIN1 = 10;
    const int AIN1 = 11;
    const int AIN2 = 12;
    const int PWMA = 13;
    const int SW_PIN = 7;     // Switch to turn the motors on and off
    const int LIGHT_PIN = A0; // Photocell

    // Constants
    const int SEARCH_DRIVE_TIME = 200;  // Time to run one motor while searching
    const int TURN_DRIVE_TIME = 200;    // Time to turn in a direction
    const int MOVE_DRIVE_TIME = 300;   // Time to drive in a direction
    const int STOP_DRIVE_TIME = 200;    // Time to stop after moving
    const int NUM_LIGHT_LEVELS = 3;

    void setup() 

    void loop() 
          Serial.print(light_levels[i]);
          Serial.print(" ");
        }
        Serial.println();
        Serial.print("Max light: ");
        Serial.println(max_light_index);

        // Move in the direction of max light
        if ( max_light_index == 0 )  else if ( max_light_index == 1 )  else 

      // If switch is not flipped, do nothing
      } else 
    }

    void rightMotor(int motorSpeed)                       
     else if (motorSpeed < 0)  else 
      analogWrite(PWMA, abs(motorSpeed));
    }

    void leftMotor(int motorSpeed)
     else if (motorSpeed < 0)  else 
      analogWrite(PWMB, abs(motorSpeed));
    }

    void drive(int leftSpeed, int rightSpeed) 

### What You Should See

When the switch is OFF, the robot will not move. When you turn the switch ON, the robot will turn left and right, taking light measurements at each extreme. It will also take a light measurement from the center.

[![Robot looking for light](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/SIKv4_Projects-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/SIKv4_Projects-12.jpg)

The robot turns to the direction with the most light and moves forward a small amount. It then repeats the pattern of looking for light and moves toward the direction of brightest light.

[![Robot moving toward light](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/3/SIKv4_Projects-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/3/SIKv4_Projects-13.jpg)

Note that trying to direct the robot with a flashlight or other light source can be difficult. Reflected light from the wheels can sometimes be brighter, for instance, than reflected light on the ground. It can take some patience to get the robot to move the way you want. You can also try modifying the code to make it faster at taking three measurements (by spinning the wheels more quickly or not turning as far to measure) or to take more than three measurements at a time.