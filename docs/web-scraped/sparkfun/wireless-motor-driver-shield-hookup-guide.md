# Source: https://learn.sparkfun.com/tutorials/wireless-motor-driver-shield-hookup-guide

## Introduction

**Note:** The Wireless Motor Driver Shield was built off Ludus Protoshield Wireless. For more information on the older version, check out the [Ludus Protoshield Hookup guide](https://learn.sparkfun.com/tutorials/ludus-protoshield-hookup-guide).

**Heads up!** Originally, this tutorial was written to configure an XBee Series 1 to communicate in transparency mode. However, this can apply to the XBee Series 3 module as long as you configure the firmware to the legacy 802.15.4 protocol. For more information, check out the [Exploring XBees and XCTU](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu) tutorial.

The Wireless Motor Driver Shield is an Arduino shield designed to make it easier and faster to connect motors and sensors to your Arduino compatible development board. It\'s really handy for throwing together remote control rovers and small autonomous robots. This guide will get you up and running with your very own [Wireless Motor Driver Shield](https://www.sparkfun.com/products/14285)!

[![SparkFun Wireless Motor Driver Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/2/4/3/14285-01.jpg)](https://www.sparkfun.com/sparkfun-wireless-motor-driver-shield.html)

### [SparkFun Wireless Motor Driver Shield](https://www.sparkfun.com/sparkfun-wireless-motor-driver-shield.html) 

[ DEV-14285 ]

The SparkFun Wireless Motor Driver Shield is designed to make connecting motors, sensors and other components to your Arduino...

[\$26.95] [ [\$9.50] ]

### Required Materials

Aside from the Wireless Motor Driver Shield, you will also need to stack the shield to a microcontroller. We recommend the [SparkFun RedBoard](https://www.sparkfun.com/products/13975) or any other Arduino form factor boards such as the [Arduino Uno](https://www.sparkfun.com/products/11021) or the [Arduino Leonardo](https://www.sparkfun.com/products/11286).

One of the main features of the Driver Shield is to make working with motors easier for those just learning. In order to fully utilize this shield, you\'ll also need some motors to drive. Check out our [Motors Category](https://www.sparkfun.com/categories/178) for some ideas.

### Suggested Reading

You may find some of the following concepts useful before using your Driver Shield.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one)

### Motors and Selecting the Right One 

Learn all about different kinds of motors and how they operate.

[](https://learn.sparkfun.com/tutorials/arduino-shields-v2)

### Arduino Shields v2 

An update to our classic Arduino Shields Tutorial! All things Arduino shields. What they are and how to assemble them.

## Hardware Overview

The Wireless Motor Driver Shield has a number of connectors, switches, and ports for you to use. Let\'s take a look at each one.

### XBee Port

At the top of the board, you will find two rows of headers meant to accept an [XBee module](https://www.sparkfun.com/categories/223). The XBee UART is connected to digital pins 0 and 1 or analog pins A0 and A1, depending on the position of the XBee selector switch.

[![XBee port](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/XBee_port.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/XBee_port.jpg)

### XBee Pins Select Switch

The selector switch underneath the XBee port allows you to choose which pins to use to communicate to the XBee module. The table below shows which pins on the Arduino the XBee *RXI* and *TXO* pins are connected to, depending on the switch\'s position. If you use SW_SER (pins A0 and A1), you\'ll need to use the [Software Serial library](https://www.arduino.cc/en/Reference/SoftwareSerial).

**Note for Using Hardware Serial Pins (HW_SER) and Uploading to Arduino:** For the Arduino Uno and similar derivative boards, pins 0 and 1 are used to upload programs to the Arduino through serial. There is a possibility of bricking the XBee or issues uploading code to your Arduino with the XBee attached. You will also have issues uploading even if the XBee is removed and the switch left in the *HW_SER* position.\
\
So, if you plan to use *HW_SER* to communicate to the XBee, you\'ll need to switch it to *SW_SER* when uploading new code. When code has finished uploading to the Arduino, the switch will need to be flipped back to the *HW_SER* side to communicate to the XBee.

  Position   XBee RXI   XBee TXO
  ---------- ---------- ----------
  HW_SER     0          1
  SW_SER     A0         A1

[![XBee selector switch](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/XBee_switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/XBee_switch.jpg)

### I^2^C Port

Under the XBee footprint, you\'ll also find a 4-pin female header that breaks out the Arduino\'s I^2^C lines. You can use this to attach various sensors to your project.

[![I2C port](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/I2C_port.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/I2C_port.jpg)

### Analog Input Pins

On the left side of the shield, you\'ll find pins A0 through A5 broken out to headers with power and ground pins for each analog pin. Be aware that if you select *SW_SER* on the XBee switch, pins A0 and A1 will be used to connect to the XBee\'s *RXI* and *TXO*, respectively.

**Note:** The pins labeled \"PWR\" in this analog section are connected to the Arduino\'s IOREF pin, so if your Arduino uses 5V logic, these pins will be 5V. Similarly, if your Arduino runs on 3.3V logic, they will be 3.3V.

[![Analog pins](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/analog_in.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/analog_in.jpg)

### Digital Pins

On the right side, you\'ll see digital pins 0 through 13 broken out to headers with a power and ground pin for each pin. These are configured this way to allow you to easily connect [servos](https://www.sparkfun.com/categories/245). Note that the power pins can be connected to IOREF, VIN, or the Shield\'s power jack, depending on the position of the 2 power switches.

[![Digital pins](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/digital_pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/digital_pins.jpg)

### Motor Driver and Output

At the bottom of the Shield, you\'ll find a [TB6612FNG motor driver](https://www.sparkfun.com/products/9457) and a 4-pin header for connecting any number of [DC motors](https://www.sparkfun.com/categories/247). The unpopulated holes are spaced 0.100 inch apart and available for [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) wires from your motor(s).

**Watch out!** Although the TB6612FNG is rated for 1.2A per channel, we found through testing that **the practical limit is about 0.8A on both channels before the driver goes into thermal shutdown.** You may be able to remedy this with heatsinks and/or active cooling, but we recommend a continued load below 0.8A for most users.

[![Motor driver](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/motor_driver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/motor_driver.jpg)

### Power Jack

Often, driving motors from the Arduino\'s power supply (even VIN) will cause the voltage to dip and possibly reset your Arduino. To help with this issue, the power jack on the top-right of the Shield will accept a 5.5 x 2.1mm power plug from a variety of [wall adapters](https://www.sparkfun.com/categories/308) and [battery packs](https://www.sparkfun.com/products/9835).

Note that you will need to set the *Motor Power* switch to *VS* to power the motors from the power jack. If you also set the *Power Rail* switch to *VMOTOR,* then the power jack will be connected to the PWR rail on the digital pins (e.g. to power servos).

Additionally, this power jack will **not** power the Arduino. It is intended to provide a power supply to your motors separate from your Arduino.

[] **Caution!** Power supplies attached to the power jack can be up to **15V**. Note that the voltage supplied will be used to directly power motors and servos, so make sure you don\'t damage your motors with this raw voltage! Additionally, the circuitry can only support up to 3.0A of current (total) delivered to the motors and digital power rail.

[![Power jack](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/Power_port.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/Power_port.jpg)

In addition to the power jack, the **VS** pins are broken out next to the barrel jack connector as \"**+**\" and \"**-**\".

[![External Power Pins (VS)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/14285-04_ExternalPowerWirelessMotorDriverTopView.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/14285-04_ExternalPowerWirelessMotorDriverTopView.jpg)

⚡ **Warning!** For those using the Arduino Uno, the USB female type B connector can short power where the **VS** pins are located. Make sure to add some electrical tape on top of the Arduino Uno\'s USB connector or bottom of the shield where the **VS** pins are exposed.\
\

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/11021-04ArduinoUnoR3_USB_Type_B_Connector_Can_Create_Short.jpg "Arduino Uno's UBS Connector Highlighted")](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/11021-04ArduinoUnoR3_USB_Type_B_Connector_Can_Create_Short.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/14285-03_ExternalPowerWirelessMotorDriverBottomView.jpg "Bottom View of Wireless Motor Driver Shield VS Pins Highlighted")](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/14285-03_ExternalPowerWirelessMotorDriverBottomView.jpg)
  *Add Electrical Tape where the Arduino Uno\'s USB Connector is Exposed on the Top*                                                                                                                                                                                                            *Add Electrical Tape where the External **VS** Power Pins are Exposed on the Bottom*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Power Switches

In the middle of the board are 2 switches that can be used to set how power is distributed to the digital PWR rail and motor driver. The *Motor Power* switch allows you to select between *VS* (power jack) and *VIN* (from Arduino) to supply power to the motors (labeled *VMOTOR*). The *Power Rail* switch allows you to select between *IOREF* (from Arduino) and *VMOTOR* (output of the *Motor Power* switch) to power the *PWR* pins on the digital headers.

  Motor Power Switch Position   Power Rail Switch Position   Motor Driver is connected to\...   Digital PWR pins are connected to\...
  ----------------------------- ---------------------------- ---------------------------------- ---------------------------------------
  VS (power jack)               VMOTOR                       VS (power jack)                    VS (power jack)
  VS (power jack)               IOREF                        VS (power jack)                    IOREF
  VIN                           VMOTOR                       VIN                                VIN
  VIN                           IOREF                        VIN                                IOREF

[![Power switches](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/power_switches.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/power_switches.jpg)

## Simple Motor Control

In this section, we\'ll review how to connect a pair of motors to the Wireless Motor Driver Shield and get them spinning. Before we do that, however, let\'s talk a little bit about how we talk to the H-Bridge Driver. If we look at the [datasheet](https://www.sparkfun.com/datasheets/Robotics/TB6612FNG.pdf) for the TB6612FNG we find a table like this:

[![H-Bridge Logic Table](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/2/Screenshot_from_2015-07-14_15_12_45.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/2/Screenshot_from_2015-07-14_15_12_45.png)

This table shows the relationship between the input and output pins on the H-Bridge. Each of the two channels requires 3 pins to operate: **IN1, IN2** and **PWM**. By driving the IN pins high or low, you can control the **direction** of the motor on that channel as well as disengage it completely or even short it end-to-end (like pressing the brakes). The signal that you feed to the PWM pin determines the **speed** of the motor on that channel. By referencing the table above, we discover that in order to make the motor turn clockwise at 50% speed, we\'ll need set IN1 to High, IN2 to LOW and send a 50% PWM signal (that\'s `analogWrite(pin, 128)` in Arduino)

We can look at the silkscreen on the shield itself to find out which Arduino pins are connected to which inputs on the H-Bridge. Once we know that, we can start to write some basic example code to control the driver.

Before anything is going to move, we\'ll need to connect a pair of motors. If you\'re just starting out with robotics, we suggest the [DAGU Hobby Gearmotors](https://www.sparkfun.com/products/13302). These motors are the same ones that come with our [Ardumoto Shield Kit](https://www.sparkfun.com/products/13201). Since they have wires attached to the motors, plug them into the A+, A-, B+, and B- headers. The example code also allows you to control a servo, so if you\'d like to add a servo, plug it into pin 11.

Now, attach the shield to a the SparkFun RedBoard (or any Arduino with the Arduino Uno footprint). Connect a power supply like a [9V battery holder](https://www.sparkfun.com/products/10512) and [9V battery](https://www.sparkfun.com/products/10218). Once that\'s done, we can get the example code loaded onto the Arduino.

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Copy the example code below, and paste it in the Arduino IDE. (As an alternative, you can also download the example code from the [GitHub Repository](https://github.com/sparkfun/Ludus_ProtoShield_Wireless/blob/master/firmware/Ludus_Example/Ludus_Example.ino)). Connect your RedBoard or Arduino over USB, and make sure you have the correct board type and COM port selected. Now press \"upload\" to send the example code to the board!

    language:c
    /*
     * SparkFun Ludus ProtoShield Example Code
     * SparkFun Electronics
     * Nick Poole 2015
     * 
     * This is an Arduino shield that integrates an H-Bridge Driver and 
     * breaks out all I/O ports to three-pin headers on a GND/PWR/SIG 
     * standard. This enables quick prototyping and integration of 
     * Arduino projects w/o the need of a breadboard.
     * 
     * Ludus is the mascot of the SparkFun Education team. 
     * It is a highly intelligent octopus.
     * 
     * Please see the License.md file for license information.
    */

    #include <Servo.h> 

    Servo swivel;

    int pwm_a = 3;   // Channel A speed
    int pwm_b = 6;   // Channel B speed
    int dir_a0 = 4;  // Channel A direction 0
    int dir_a1 = 5;  // Channel A direction 1
    int dir_b0 = 7;  // Channel B direction 0
    int dir_b1 = 8;  // Channel B direction 1

    char inbit; // A place to store serial input

    int swivelpos = 90; // Servo position

    void setup()
    

    void loop()
    
      }  
    }

    void forward(int speed) // Move Forward
    

    void reverse(int speed) // Move Backward 
    

    void turnL(int speed) // Turn Left while moving forward
    

    void turnR(int speed) // Turn Right while moving forward
    

    void spinL(int speed) // Spin Left in place
    

    void spinR(int speed) // Spin Right in place
    

    void brake() // Short brake
    

    void shutoff() // Stop Motors w/o braking
    

    void draw() // Serial Instructions
    

    void servoL() // Spin servo (on pin 11) left 
    

    }

    void servoR() // Spin servo (on pin 11) right
    

    }

Make sure the *Motor Power* and *Power Rail* switches are set to *VIN* and *VMOTOR*, respectively.

[![Driver Shield switches](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/8/Wireless_Motor_Driver_Shied_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/Wireless_Motor_Driver_Shied_Hookup_Guide-01.jpg)

If everything went well, you should now be able to open a [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics) (such as the one built into the Arduino IDE), and type a bunch of \"w\"s to make the motors turn. This example was really written to be used with terminal programs, which allow you to type directly to the port without having to press return. That way, you can drive the robot by holding down the appropriate keys on your keyboard. My favorite terminal program for this is [RealTerm](https://learn.sparkfun.com/tutorials/terminal-basics/real-term-windows). You can get RealTerm [here](http://sourceforge.net/projects/realterm/files/).

You can also attach a servo to pin 11 and send the characters \'z\' and \'c\' through the Serial terminal to move the servo.

[![Servo attached to pin 11](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/8/Wireless_Motor_Driver_Shied_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/Wireless_Motor_Driver_Shied_Hookup_Guide-03.jpg)

Now that we\'ve seen this thing in action, let\'s dig through the example code. Understanding how the example code works is the first step towards writing your own!

## Understanding the Example Code

The example code is designed to let you control the H-Bridge, as well as a servo attached to pin 11, using [serial communication](https://learn.sparkfun.com/tutorials/serial-communication). Let\'s walk through a few excerpts from the code and see if we can understand a little better what\'s making it work. As with most sketches, it starts with some basic setup:

    language:c
    #include <Servo.h>

    Servo swivel;

    int pwm_a = 3; // Channel A speed
    int pwm_b = 6; // Channel B speed
    int dir_a0 = 4; // Channel A direction 0
    int dir_a1 = 5; // Channel A direction 1
    int dir_b0 = 7; // Channel B direction 0
    int dir_b1 = 8; // Channel B direction 1

    char inbit; // A place to store serial input
    int swivelpos = 90; // Servo position

    void setup()
    

As you can see, we started out by including the servo library and creating a servo object called \"swivel\". Next, we declare a handful of variables to keep track of which pins are responsible for which functions, and also variables for the servo position and incoming serial characters. The `setup()` function is where serial communication is initialized, the servo object is attached and the control pins are all set as output devices. Finally, we call the function `draw()`, which we\'ll look at in a minute.

    language:c
    void loop()
    
    }
    }

The main loop of the example code just waits to see input on the serial line and then stores the incoming value and compares it against a list of cases. By scrolling through the switch/case statements, you can see the behavior associated with each serial character. The rest of the code is composed of the various procedures that are called in the main loop. Let\'s look at a few of these:

    language:c
    void draw() // Serial Instructions
    

This one is pretty straightforward! The `draw()` procedure is just a bunch of print statements that tell you which keys are attached to which functions.

Finally, there are a bunch of procedures that actually set the speed and direction of the motors. These are the functions that you\'ll want to borrow for your own code because they wrap up all of the control pin stuff we talked about in the last section into intuitive commands like \"forward,\" \"turn,\" and \"brake.\" All of the motion commands are basically structured the same. For example:

    language:c
    void forward(int speed) // Move Forward
    

The `brake()` and `shutoff()` functions are structured the same as the motion procedures except that in the case of `brake()`, all of the pins are written high, and in the case of `shutoff()`, all of the pins are written low. The `brake()` procedure actually shorts the motor so that it resists turning. The `shutoff()` function simply shuts off power to the motors so that they come to a rolling stop. Try referring to the example code that was copied from *[Simple Motor Control](https://learn.sparkfun.com/tutorials/wireless-motor-driver-shield-hookup-guide#simple-motor-control)* for more details on how these functions were defined.

Finally, there are the servo control functions, which increment or decrement the servo position variable before writing it to the servo:

    language:c
    void servoL() // Spin servo (on pin 11) left
    
    }

The only kind of clever thing going on here is that we check ahead of time whether we\'ve reached the limits of the servo so we can\'t increment beyond its range of motion.

## Going Wireless

By using the power of [ZigBee](https://en.wikipedia.org/wiki/Zigbee), you can free your project from its USB tether! Do do this, you\'ll need a pair of [XBee radio modules](https://www.sparkfun.com/products/8665) and an [XBee Explorer USB](https://www.sparkfun.com/products/11812). Even if you\'re not familiar with XBee, you should be able to run the example code wirelessly as the radio modules should be configured properly by default. For an introduction to XBee, check out this [SparkFun tutorial for getting started with XBees](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu). There\'s a lot more you can do with XBee than what we\'ll cover here.

The first step is to plug an XBee radio into the Wireless Motor Driver Shield. The silkscreen on the board shows which orientation it should go. Make sure that the slide switch marked *XBee Serial Select* is set to *HW_SER*.

[![XBee on Driver Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/8/Wireless_Motor_Driver_Shied_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/Wireless_Motor_Driver_Shied_Hookup_Guide-04.jpg)

This will connect the XBee radio to the hardware serial lines of the Arduino. Next, plug your XBee Explorer into the USB port on your computer and open the serial terminal program that you were using in the *Simple Motor Control* section.

[![Xbee on Explorer Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/8/Wireless_Motor_Driver_Shied_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/8/Wireless_Motor_Driver_Shied_Hookup_Guide-02.jpg)

Open the COM port for the XBee Explorer, and switch the Arduino on.

The example code should now work exactly as it did before, only this time, your serial commands are being sent over the air! What\'s happening is that the XBee radio is acting like a wireless serial tunnel. As far as the Arduino knows, there\'s a USB cable hooked up to the serial line.