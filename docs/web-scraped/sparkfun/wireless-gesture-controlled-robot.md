# Source: https://learn.sparkfun.com/tutorials/wireless-gesture-controlled-robot

## Introduction

Control the RedBot wirelessly based on the movement of your hand using an accelerometer and XBees!

[![Full Demo](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/9/Wireless_Gesture_Controlled_Robot_XBee_Acclerometer_ADXL335_Glove_Demo_1.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/9/Wireless_Gesture_Controlled_Robot_XBee_Acclerometer_ADXL335_Glove_Demo_1.gif)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You will need wire, wire strippers, a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/1/14763-Wire_Strippers_-_758PL0066-03.jpg)](https://www.sparkfun.com/products/14763)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/14763) 

[ TOL-14763 ]

These are high grade wire strippers from Techni-Tool with a curved grip making them an affordable option if you need to remov...

**Retired**

### You Will Also Need

- Glove
- Scissors
- Non-Conductive Thread

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing. This tutorial continues on from the [Wireless Glove Controller](https://learn.sparkfun.com/tutorials/wireless-glove-controller) and [Wireless RC Robot with Arduino and XBees](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees) tutorials. Make sure to check through guides.

[](https://learn.sparkfun.com/tutorials/wireless-glove-controller)

### Wireless Glove Controller 

April 24, 2019

Build a wireless glove controller with Arduinos to trigger an LED using XBees!

[](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees)

### Wireless RC Robot with Arduino and XBees 

March 12, 2019

In this tutorial, we will expand on the SIK for RedBot to control the robot wirelessly with XBee radios! We\'ll explore a different microcontroller and wirelessly control the RedBot at a distance.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide)

### XBee Shield Hookup Guide 

How to get started with an XBee Shield and Explorer. Create a remote-control Arduino!

[](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis)

### Assembly Guide for RedBot with Shadow Chassis 

Assembly Guide for the RedBot Kit. This tutorial includes extra parts to follow to go along with the RedBot Inventor\'s Kit tutorial.

[](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu)

### Exploring XBees and XCTU 

How to set up an XBee using your computer, the X-CTU software, and an XBee Explorer interface board.

[](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis)

### Experiment Guide for RedBot with Shadow Chassis 

This Experiment Guide offers nine experiments to get you started with the SparkFun RedBot. This guide is designed for those who are familiar with our SparkFun Inventor\'s Kit and want to take their robotics knowledge to the next level.

## Understanding Your Circuit

### Wireless Glove Controller

The connection for this project should be the same as the [initial circuit](https://learn.sparkfun.com/tutorials/wireless-glove-controller#v1). The only differences are the connections for the accelerometer and analog reference pin as shown in the diagram below.

[![Wireless Gesture Controller Circuit Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/9/ADXL335_Accelerometer_Wireless_Gesture_Controlled_Robot_Arduino_XBee_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/9/ADXL335_Accelerometer_Wireless_Gesture_Controlled_Robot_Arduino_XBee_Fritzing_bb.jpg)

#### Analog Accelerometer

Since the ADXL335 requires 3.3V, we\'ll need to connect the VCC pin to 3.3V. To complete the connection for power, you will need to connect GND to GND. Then for the x, y, and z pins, you\'ll need to connect them to pin 2, 1, and 0, respectively.

**Note:** An analog accelerometer was chosen for simplicity. However, any digital accelerometer (like the MMA8452Q included in the RedBot kit) can work with the setup as long as you adjust the connection and code to communicate with the sensor. Make sure that the accelerometer is low-G so that it is sensitive enough to detect motion.

#### Configuring AREF

Since the ADXL335 is 3.3V, we\'ll need to connect the [Arduino\'s AREF pin](https://www.arduino.cc/reference/en/language/functions/analog-io/analogreference/) to the 3.3V pin. This will configure the reference voltage used for the analog output from the accelerometer. As a result, we can measure smaller voltages (i.e. your 3.3V output) with the best resolution on a 5V Arduino.

⚡ **Warning!** Make sure to check out this note from Arduino before powering and uploading code to your board!\
\

> **Don't use anything less than 0V or more than 5V for external reference voltage on the AREF pin! If you're using an external reference on the AREF pin, you must set the analog reference to EXTERNAL before calling `analogRead()`**. Otherwise, you will short together the active reference voltage (internally generated) and the AREF pin, possibly damaging the microcontroller on your Arduino board.

### Assembled Shadow Chassis

We\'ll assume that you have a fully [assembled robot with the Shadow Chassis](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis).

[](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis)

### Assembly Guide for RedBot with Shadow Chassis 

May 28, 2015

Assembly Guide for the RedBot Kit. This tutorial includes extra parts to follow to go along with the RedBot Inventor\'s Kit tutorial.

## Hardware Hookup

### Modify the XBee Shield

Adding on to the glove that was built in the [Wireless Glove Controller](https://learn.sparkfun.com/tutorials/wireless-glove-controller) tutorial, remove the tape and disconnect the braided wire from the shield. Then pull the XBee shield off the RedBoard.

[![Top View v1 Glove](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Secured.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Secured.jpg)

Using the [circuit diagram](https://learn.sparkfun.com/tutorials/wireless-gesture-controlled-robot#understanding-your-circuit) with the accelerometer, [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the ADXL335 breakout board to the shield. In this case, female headers were used with male headers soldered on the breakout. Then [strip solid core, hook-up wire](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-strip-a-wire) and solder them between the pins. If you are following along, your board should look similar to the images below. When you are ready, stack the board back on top of the RedBoard and secure the battery.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View of Components Soldered on XBee Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/9/Wireless_Glove_Gesture_Controller_Accelerometer__XBee_Arduino_Top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/9/Wireless_Glove_Gesture_Controller_Accelerometer__XBee_Arduino_Top.jpg)   [![Bottom View with Wires and Jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/9/Wireless_Glove_Gesture_Controller_Accelerometer__XBee_Arduino_Bottom.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/9/Wireless_Glove_Gesture_Controller_Accelerometer__XBee_Arduino_Bottom.jpg)
  *Top View of Components Soldered on XBee Shield*                                                                                                                                                                                                                                                                          *Bottom View with Wires and Jumpers*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Configuring XBees

**Note:** If you are using the XBees from the glove and RC robot tutorial, they should be the same configuration! You can move on to the next section.

To configure the XBees, we will be using the XBee Series 1 firmware. It is recommended to configure each XBee using the XBee Explorer USB.

[![XBee Inseted int XBee Explorer USB to Configure ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/6/8/XBee_3_Explorer_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/8/XBee_3_Explorer_USB.jpg)

If you have not already, check out the [Starting with XCTU](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu#starting-with-x-ctu) section under Exploring XBees and XCTU to configure your XBees.

[](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu)

### Exploring XBees and XCTU 

March 12, 2015

How to set up an XBee using your computer, the X-CTU software, and an XBee Explorer interface board.

### Point-to-Point Configuration

For simplicity, we will be sending commands with the XBees in transparent mode set for a point-to-point configuration. Make sure to configure each XBee with a unique MY address if there are more than two XBees in your CH and PAN ID. You will then need to adjust the DL address for each respective XBee.

  ---------------------------------------------------------------------------------------------------
  Setting                    Acronym           Transmitting XBee Node 1\     Receiving XBee Node 2\
                                               (Wireless Glove Controller)   (Robot)
  -------------------------- ----------------- ----------------------------- ------------------------
  Channel                    CH                C                             C

  PAN ID                     ID                3333                          3333

  Destination Address High   DH                0                             0

  Destination Address Low    DL                1                             0

  16-bit Source Address      MY                0                             1
  ---------------------------------------------------------------------------------------------------

## Setting Up Arduino

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### RedBot Mainboard

#### FTDI Drivers

Remember, to program your robot, you will first need to install some FTDI drivers. Follow the steps in [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) to do so. This is also explained in the RedBot Guides.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

June 4, 2013

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

#### Arduino Library

**Note:** If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Make sure to install the RedBot library as explained in the [RedBot Library Quick Reference](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/redbot-library-quick-reference). You\'ll also find the quick overview of the RedBot Library, classes, methods, and variables.

[RedBot Library Quick Reference](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/redbot-library-quick-reference)

------------------------------------------------------------------------

## Example

### Wireless Glove Code

**Note:** If you are not familiar with calibrating your accelerometer, check out this [tutorial about calibrating the ADXL335](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/calibrating-the-accelerometer).

In this part of the example, we\'ll have the glove send a character when the thumb and middle finger make contact. As long as the two fingers have contact, the robot will move forward, forward-left, back, or forward -right based on the orientation of your hand. When the custom button is not pressed, the buzzer will make a familiar 8-bit sound when waving your hand or \"jabbing\" the air. The RGB LED will light up based on the mode and orientation of the hand.

Copy the code, paste it into the Arduino IDE, select your board (**Arduino/Genuino Uno**), and COM port. Then upload the code to the glove.

    language:c
    // We'll use SoftwareSerial to communicate with the XBee:

    #include <SoftwareSerial.h>

    //For Atmega328P's
    // XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
    SoftwareSerial XBee(2, 3); // RX, TX

    //For Atmega2560, ATmega32U4, etc.
    // XBee's DOUT (TX) is connected to pin 10 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 11 (Arduino's Software TX)
    //SoftwareSerial XBee(10, 11); // RX, TX

    //set analog read pins
    const int xPin = 2;//x=A2
    const int yPin = 1;//y=A1
    const int zPin = 0;//z=A0

    //read the analog values from the accelerometer
    int xRead = analogRead(xPin);
    int yRead = analogRead(yPin);
    int zRead = analogRead(zPin);

    //LED Status Indicator
    int ledR = 5;//hardware PWM
    int ledG = 6;//hardware PWM
    int ledB = 9; //hardware PWM

    //Accelerate Button
    #define ACCELERATE_BUTTON 4 // Pin used for accelerate button
    const int ledPin1 = 13;  //LED on the push button

    boolean current_buttonACCELERATE_State;

    void setup() 
      sequenceTest();//visually initialization

      Serial.begin(9600);
      Serial.println("Wireless XBee Glove Controller Initialized");
    }

    void loop() 
        else if (xRead > 590) 
        else if (yRead > 590) 
        else if (yRead < 430) 
        else 

      }
      else 
        if (zRead < 400) 
        else 
      }

      //show that we are sending a character
      digitalWrite(ledPin1, HIGH);
      delay(50);
      digitalWrite(ledPin1, LOW);
      delay(50);
    }//end loop

    void allOFF() 

    void allON() 

    void redON() 

    void magentaON() 

    void blueON() 

    void cyanON() 

    void greenON() 

    void yellowON() 

    void sequenceTest() 

### Receiving XBee Robot Code

The commands to control the RedBot should be the same code that was used in the last example of the Wireless RC Robot with Arduino and XBees tutorial. Head over to [Experiment 4.2: Adding Audio with the ATmega328P](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/experiment-4-wirelessly-triggering-audio#redbot_audio) to upload code to the RedBot mainboard if you have not already.

[Experiment 4: Wirelessly Triggering Audio](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/experiment-4-wirelessly-triggering-audio#redbot_audio)

### What You Should See

After uploading, touch the metal snap pins between your thumb and middle finger to move the robot forward-left, forward, forward-right, or backward. The RGB LED will light up based on the orientation of your hand. Separate your fingers and punch the air as if there is a [question mark block](https://en.wikipedia.org/wiki/Super_Mario_Bros.) above you to hear coin sound effect! Wave your hand to see if you can make a fireball sound effect!

[![Full Demo of Glove Controlling Robot](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/9/Wireless_Gesture_Controlled_Robot_XBee_Acclerometer_ADXL335_Glove_Demo_1.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/9/Wireless_Gesture_Controlled_Robot_XBee_Acclerometer_ADXL335_Glove_Demo_1.gif)