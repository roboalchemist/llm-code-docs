# Source: https://learn.sparkfun.com/tutorials/lilypad-light-sensor-hookup-guide

## Introduction

The [LilyPad Light Sensor](https://www.sparkfun.com/products/8464) is an e-textile friendly version of the [Ambient Light Sensor Breakout](https://www.sparkfun.com/products/8688). If you\'ve used the breakout in a project before, the hookup and code will be very similar. You will need to connect to a LilyPad Arduino or other microcontroller to read the sensor values and use in your code.

This sensor outputs an analog value from 0 to 3.3V. In bright light (full daylight) this sensor will output 3.3V, and if completely covered will output 0V. In a typical indoor lighting situation, the sensor will output from around 1 to 2V.

[![LilyPad Light Sensor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/8/08464-01.jpg)](https://www.sparkfun.com/products/8464)

### [LilyPad Light Sensor](https://www.sparkfun.com/products/8464) 

[ DEV-08464 ]

This is a simple to use light sensor that outputs an analog value from 0 to 5V. With exposure to daylight, this sensor will o...

**Retired**

To follow along with the code examples, we recommend:

### Suggested Reading

To add this sensor to a project, you should be comfortable sewing with conductive thread and uploading code to your LilyPad Arduino. Here are some tutorials to review before working with this sensor:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/light)

### Light 

Light is a useful tool for the electrical engineer. Understanding how light relates to electronics is a fundamental skill for many projects.

[](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles)

### Insulation Techniques for e-Textiles 

Learn a few different ways to protect your conductive thread and LilyPad components in your next wearables project.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

[](https://learn.sparkfun.com/tutorials/getting-started-with-lilypad)

### Getting Started with LilyPad 

An introduction to the LilyPad ecosystem - a set of sewable electronic pieces designed to help you build soft, sewable, interactive e-textile projects.

If you have not used the TEMT6000 light sensor before, we recommend checking out the TEMT6000 Hookup Guide for basic information regarding that sensor.

[](https://learn.sparkfun.com/tutorials/temt6000-ambient-light-sensor-hookup-guide)

### TEMT6000 Ambient Light Sensor Hookup Guide 

October 26, 2016

Bring the ability to detect light levels to any project with the SparkFun TEMT6000 Ambient Light Sensor Breakout.

## Attaching to a LilyPad Arduino

The LilyPad Light Sensor has three sew tabs - **Power** (+), **Ground** (-), and **Signal** (S). The signal tab should be connected to an analog tab (marked with an \'A\') on the LilyPad Arduino.

To follow along with the code examples in this tutorial, connect the light sensor to a LilyPad Arduino as shown below. Use alligator clips to temporarily connect **Signal** to **A3** on a LilyPad Arduino, **(-)** to **(-)** on the LilyPad, and **(+)** to **A5**. When you are finished prototyping, replace the alligator clips with conductive thread traces for permanent installation in your project.

To make our diagrams easier to follow, and to avoid any potential short circuits in our stitching, we\'ll be connecting the **Power** pin to A5, which we will then set to **HIGH** in our code. This will act as an additional power attachment.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/1/LightSensorHookup_LilyUSB.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/1/LightSensorHookup_LilyUSB.png)

*Connecting to a [LilyPad Arduino USB](https://www.sparkfun.com/products/12049)*

If following along with a [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346), the light sensor is pre-wired to A2. The light sensor on the ProtoSnap is a slightly different version that the catalog item, but functions the same.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/1/ProtoSnapLightSensor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/1/ProtoSnapLightSensor.png)

#### Other LilyPad connection notes:

- If using the [ProtoSnap - LilyPad Development Simple](https://www.sparkfun.com/products/11201) - attach to the metal tab at the top right of the board, this connects to A3. You can also set pin A5 to HIGH as an additional power tab, as the LilyPad Simple\'s tab is hard to access in the ProtoSnap format.
- If using the the pre-wired light sensor on the [ProtoSnap - LilyPad Development Board](https://www.sparkfun.com/products/11262), it is attached to pin A6.

## Reading Values in Serial Monitor

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

After connecting the light sensor, let\'s take a look at the values it reads under different lighting conditions. For this we\'ll use `analogRead()` and `Serial.print()`.

Upload the following code to your LilyPad Arduino, making sure to select the correct LilyPad board from the drop down menu below. Choose **LilyPad Arduino USB** if using a LilyPad Arduino USB. The LilyPad Arduino Simple, LilyPad Arduino, and LilyPad Development Board, and Development Board Simple all use a **LilyPad ATmega 328**. Select **LilyPad USB Plus** if following along with the LilyPad ProtoSnap Plus.\
\
Don\'t forget to select the Serial Port that your LilyPad is connected to.\
\

- If prototyping with a LilyPad ProtoSnap Plus, change **sensorPin** to A2.
- If prototyping with a LilyPad Development Board, change **sensorPin** to A6.

Copy the following code and upload it to your LilyPad.

    language:c
    /******************************************************************************

    LilyPad Light Sensor Example
    SparkFun Electronics

    This example code reads the input from a LilyPad Light Sensor and displays in
    the Serial Monitor.

    Light Sensor connections:
       * S pin to A3
       * + pin to A5
       * - to -

    ******************************************************************************/

    // Set which pin the Signal output from the light sensor is connected to
    // If using the LilyPad Development Board, change this to A6
    int sensorPin = A3;
    // Create a variable to hold the light reading
    int lightValue;

    void setup()
    

    void loop()
    

Once your code is uploaded, open the [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics) in the IDE and see the output. Numbers should begin to stream by. Observe how the numbers change as the ambient light changes. Use your hand to cover the sensor or a flashlight to shine more light on it. Next we\'ll be using these values to control behaviors in our code.

## Using Values to Trigger Behaviors

Next, we\'ll make some decisions in the code based on the light sensor\'s readings. This example code creates a simple automatic night light that turns on an LED when it's dark.

We\'ll use the `analogRead()` function to get data from the light sensor and compare it to a variable we set for darkness level. When the readings from the light sensor fall below our threshold set for dark, it will turn on the LED.

You can hook up a LilyPad LED to pin 5 or use the built-in LED attached to pin 13.

    language:c
    /******************************************************************************

    LilyPad Light Sensor Trigger - Automatic Night Light
    SparkFun Electronics

    Adapted from Digital Sandbox Experiment 11: Automatic Night Light

    This example code reads the input from a LilyPad Light Sensor compares it to
    a set threshold named 'dark'. If the light reading is below the threshold,
    an LED will turn on.

    Light Sensor connections:
       * S pin to A3
       * + pin to A5
       * - to -

    Connect an LED to pin 5 or use the built-in LED on pin 13

    ******************************************************************************/
    // The dark variable determines when we turn the LEDs on or off. 
    // Set higher or lower to adjust sensitivity.
    const int darkLevel = 50;

    // Create a variable to hold the readings from the light sensor.
    int lightValue;

    // Set which pin the Signal output from the light sensor is connected to
    // If using the LilyPad Development Board, change this to A6
    int sensorPin = A3;

    // Set which pin the LED is connected to. 
    // Set to 13 if you'd rather use the LilyPad Arduino's built-in LED.
    int ledPin = 5;

    void setup()
    

    void loop()
    
        else // Otherwise, if "lightValue" is greater than "dark"
        

        // Delay so that the text doesn't scroll to fast on the Serial Monitor. 
        // Adjust to a larger number for a slower scroll.
        delay(100);
    }

If your light sensor isn\'t triggering correctly, check the output of the Serial Monitor to see if there\'s a better value for the dark variable than what is set in the example code.

## Project Examples

### Light Sensitive Hat

Let your geek shine with this hat that blinks when the lights go down.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/1/GeekHat.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/1/GeekHat.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/1/GeekHatDetail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/1/GeekHatDetail.jpg)

### Musical Bracelet

Combining the sensor with a [LilyPad Buzzer](https://www.sparkfun.com/products/8463) can create interesting interactive projects, for example this wearable light-controlled musical instrument or Opto-Theremin. Control tones on the buzzer by covering the LilyPad Light Sensor.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/CyberCuff.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/CyberCuff.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/CyberCuffDetail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/CyberCuffDetail.jpg)

### Twinkling Prom Dress

This prom dress project featured in this video uses an initial threshold setting and light sensor to trigger some [LilyPad Pixel Boards](https://www.sparkfun.com/products/13264).

### LilyPad Safety Scarf

Create a scarf lights up when it gets dark with LilyPad and sewable LED ribbon.

[](https://learn.sparkfun.com/tutorials/lilypad-safety-scarf)

### LilyPad Safety Scarf 

November 21, 2017

This scarf is embedded with a ribbon of LEDs that illuminate when it gets dark out, making yourself more visible to vehicle and other pedestrians.