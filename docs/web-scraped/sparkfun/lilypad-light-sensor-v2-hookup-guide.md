# Source: https://learn.sparkfun.com/tutorials/lilypad-light-sensor-v2-hookup-guide

## Introduction

The [LilyPad Light Sensor](https://www.sparkfun.com/products/14629) is a sewable breakout board with an ALS-PT19 light sensor on it. To use the light sensor, you will need to connect to a LilyPad Arduino or other microcontroller to read the sensor values and use them in your code.

The LilyPad Light Sensor outputs voltage between **0V** and **3.3V** depending on the level of ambient light shining on it. As more light is applied on the sensor, more current will flow from the board through the signal tab to the microcontroller you connect the sensor to. If the sensor receives no light, no current will flow through it. In a typical indoor lighting situation, the sensor will output around 1 to 2V.

[![LilyPad Light Sensor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/0/8/14629-LilyPad_Light_Sensor-01.jpg)](https://www.sparkfun.com/lilypad-light-sensor.html)

### [LilyPad Light Sensor](https://www.sparkfun.com/lilypad-light-sensor.html) 

[ DEV-14629 ]

The LilyPad Light Sensor is a sewable breakout board with an ALS-PT19 light sensor built in and ready to use right away.

[ [\$5.25] ]

This sensor is also used on the [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346) and [LilyMini ProtoSnap](https://www.sparkfun.com/products/14063).

[![LilyPad ProtoSnap Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/2/4/14346-01.jpg)](https://www.sparkfun.com/lilypad-protosnap-plus.html)

### [LilyPad ProtoSnap Plus](https://www.sparkfun.com/lilypad-protosnap-plus.html) 

[ DEV-14346 ]

The LilyPad ProtoSnap Plus is a sewable electronics prototyping board that you can use to explore circuits and programming, t...

[ [\$47.50] ]

[![LilyPad LilyMini ProtoSnap](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/0/5/14063-01.jpg)](https://www.sparkfun.com/lilypad-lilymini-protosnap.html)

### [LilyPad LilyMini ProtoSnap](https://www.sparkfun.com/lilypad-lilymini-protosnap.html) 

[ DEV-14063 ]

The LilyMini ProtoSnap is a great way to get started learning about creating interactive e-textile circuits before you start ...

[ [\$19.50] ]

To follow along with the code examples, we recommend:

### Suggested Reading

To add this sensor to a project, you should be comfortable sewing with conductive thread and uploading code to a LilyPad Arduino. Here are some tutorials to review before working with this sensor:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

[](https://learn.sparkfun.com/tutorials/getting-started-with-lilypad)

### Getting Started with LilyPad 

An introduction to the LilyPad ecosystem - a set of sewable electronic pieces designed to help you build soft, sewable, interactive e-textile projects.

## Attaching to a LilyPad Arduino

The LilyPad Light Sensor has three sew tabs - **Power** (+), **Ground** (-), and **Signal** (S). Next to each tab is a white label on the top and bottom of the board for reference. The signal tab should be connected to an analog tab (marked with an \'A\') on a LilyPad Arduino.

[![Labeled top and bottom views of the LilyPad Light Sensor board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/8/LilyPadLightSensor_Views.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/8/LilyPadLightSensor_Views.jpg)

To follow along with the code examples in this tutorial, connect the light sensor to a LilyPad Arduino as shown below. Use alligator clips to temporarily connect **Signal** to **A2** on a LilyPad Arduino, **(-)** to **(-)** on the LilyPad, and **(+)** to **(+)**. When you are finished prototyping, replace the alligator clips with conductive thread traces for permanent installation in your project.

[![LilyPad Light Sensor clipped to a LilyPad USB with alligator clips](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/8/LightSensorV2_Hookup.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/8/LightSensorV2_Hookup.png)

*Connecting to a [LilyPad Arduino USB](https://www.sparkfun.com/products/12049)*

\

**Please Note:**\
If following along with a [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346), the light sensor is pre-wired to **Pin A2**. The light sensor on the ProtoSnap is a slightly different version than the catalog item, but functions the same.\
\
If following along with the [LilyMini ProtoSnap](https://www.sparkfun.com/products/14063),the light sensor is pre-wired to **Pin 1**. Again, the light sensor on the LilyMini ProtoSnap is a slightly different version than the catalog item, but functions the same.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/1/ProtoSnapLightSensor.png "LilyPad Light Sensor location circled on a LilyPad ProtoSnap Plus board")](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/1/ProtoSnapLightSensor.png)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/8/LilyMiniProtosnap1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/8/LilyMiniProtosnap1.jpg)\

  *LilyPad Light Sensor location circled on a LilyPad ProtoSnap Plus board*                                                                                                                                                                         *LilyPad Light Sensor location circled on a LilyMini ProtoSnap board*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Reading Values in Serial Monitor

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

After connecting the light sensor, let\'s take a look at the values it reads under different lighting conditions. For this we\'ll use `analogRead()` and `Serial.print()`.

Upload the following code to your LilyPad Arduino, making sure to select the correct LilyPad board from the Tools-\>Board drop down menu. Choose **LilyPad Arduino USB** if using a LilyPad Arduino USB. The LilyPad Arduino Simple, LilyPad Arduino, LilyPad Development Board, and Development Board Simple all use a **LilyPad ATmega 328**. Select **LilyPad USB Plus** if following along with the LilyPad USB Plus or LilyPad ProtoSnap Plus. Don\'t forget to select the Serial Port that your LilyPad is connected to. Note the following potential code changes:

- If prototyping with a LilyPad ProtoSnap Plus, change **sensorPin** to A2.
- If prototyping with a LilyMini ProtoSnap, change **sensorPin** to 1.

Copy the following code and upload it to your LilyPad.

    language:c
    /******************************************************************************

    LilyPad Light Sensor Example
    SparkFun Electronics

    This example code reads the input from a LilyPad Light Sensor and displays in
    the Serial Monitor.

    Light Sensor connections:
       * S tab to A2
       * + tab to +
       * - tab to -

    ******************************************************************************/

    // Set which pin the Signal output from the light sensor is connected to
    int sensorPin = A2;
    // Create a variable to hold the light reading
    int lightValue;

    void setup()
    

    void loop()
    

Once your code is uploaded, open the [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics) in the IDE and observe the output. Numbers should begin to stream by. Note how the numbers change as the ambient light changes. Use your hand to cover the sensor or a flashlight to shine more light on it. Next we\'ll be using these values to control behaviors in our code.

## Using Values to Trigger Behaviors

Next, we\'ll make some decisions in the code based on the light sensor\'s readings. This example code creates a simple automatic night light that turns on an LED when it's dark.

We\'ll use the `analogRead()` function to get data from the light sensor and compare it to a variable we set for darkness level. When the readings from the light sensor fall below our threshold set for dark, it will turn on the LED.

You can hook up a LilyPad LED to sew tab 5 or use the built-in LED attached to pin 13.

    language:c
    /******************************************************************************

    LilyPad Light Sensor Trigger - Automatic Night Light
    SparkFun Electronics

    Adapted from Digital Sandbox Experiment 11: Automatic Night Light

    This example code reads the input from a LilyPad Light Sensor compares it to
    a set threshold named 'dark'. If the light reading is below the threshold,
    an LED will turn on.

    Light Sensor connections:
       * S tab to A2
       * + tab to +
       * - to -

    Connect an LED to pin 5 or use the built-in LED on pin 13

    ******************************************************************************/
    // The dark variable determines when we turn the LEDs on or off. 
    // Set higher or lower to adjust sensitivity.
    const int darkLevel = 50;

    // Create a variable to hold the readings from the light sensor.
    int lightValue;

    // Set which pin the Signal output from the light sensor is connected to
    int sensorPin = A2;

    // Set which pin the LED is connected to. 
    // Set to 5 if you'd rather hook up your own LED to the LilyPad Arduino.
    int ledPin = 13;

    void setup()
    

    void loop()
    
        else // Otherwise, if "lightValue" is greater than "dark"
        

        // Delay so that the text doesn't scroll to fast on the Serial Monitor. 
        // Adjust to a larger number for a slower scroll.
        delay(100);
    }

If your light sensor isn\'t triggering correctly, check the output of the Serial Monitor to see if there\'s a better value for the dark variable than what is set in the example code.

## Sewing into a Project

Once you are finished prototyping your project using the LilyPad Light Sensor, you can replace any temporary connections with conductive thread.

For an overview of sewing with conductive thread, check out this guide:

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

December 17, 2016

Learn how to use conductive thread with LilyPad components.

To hide the sensor in your project, you can cover with a material making sure to leave an opening for the sensor to be exposed to light. Cutting a hole above the sensor in fabric is one way to do this.

[![Hole cut in fabric above light sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/8/FabricHoleforSensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/8/FabricHoleforSensor.jpg)

\

[![Hole cut in felt to allow sensor to take readings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/8/FabricHoleforSensor2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/8/FabricHoleforSensor2.jpg)

## Project Examples

### Light Sensitive Hat

Let your geek shine with this hat that blinks when the lights go down.

[![Geek Hat](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/1/GeekHat.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/1/GeekHat.jpg)

[![Geek Hat Detail](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/1/GeekHatDetail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/1/GeekHatDetail.jpg)

### Musical Bracelet

Combining the sensor with a [LilyPad Buzzer](https://www.sparkfun.com/products/8463) can create interesting interactive projects, for example this wearable light-controlled musical instrument or Opto-Theremin. Control tones on the buzzer by covering the LilyPad Light Sensor.

[![Musical Bracelet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/CyberCuff.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/CyberCuff.jpg)

[![Musical Bracelet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/CyberCuffDetail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/CyberCuffDetail.jpg)

### Twinkling Prom Dress

The prom dress project featured in this video uses an initial threshold setting and light sensor to trigger some [LilyPad Pixel Boards](https://www.sparkfun.com/products/13264).

### LilyPad Safety Scarf

Create a scarf that lights up when it gets dark with LilyPad and sewable LED ribbon.

[](https://learn.sparkfun.com/tutorials/lilypad-safety-scarf)

### LilyPad Safety Scarf 

November 21, 2017

This scarf is embedded with a ribbon of LEDs that illuminate when it gets dark out, making yourself more visible to vehicle and other pedestrians.