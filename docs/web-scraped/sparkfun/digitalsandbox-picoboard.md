# Source: https://learn.sparkfun.com/tutorials/digitalsandbox-picoboard

## Introduction

**Heads up!** As of the writing of this tutorial, Scratch 3.0 and 2.0 does not fully support the PicoBoard. We suggest using [Scratch 1.4](http://scratch.mit.edu/scratch_1.4/) until the full PicoBoard extensions are implemented, tested, and rolled out with Scratch 2.0+.

-\> [![alt text](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/2/7/0/12651-03.jpg)](https://www.sparkfun.com/products/12651) [![alt text](https://cdn.sparkfun.com/r/100-100/assets/learn_tutorials/2/7/0/9Tpee4Kqc.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/9Tpee4Kqc.png) [![alt text](https://cdn.sparkfun.com/r/200-200/assets/learn_tutorials/2/7/0/scratch-cat-transparent.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/scratch-cat-transparent.png) \<-

The Digital Sandbox (DS) is a creation that came about as a combination between the best features of the [PicoBoard](), [DangerShield](https://www.sparkfun.com/products/11649), and the [Lilypad Protosnap Development Board](https://www.sparkfun.com/products/11262). We combined the best of these three great introductory learning platforms to create a single board that has several commonly used peripheral devices \-- LEDs, RGB, slider, button, and a variety of sensors.

-\> [![alt text](https://cdn.sparkfun.com/r/200-200/assets/learn_tutorials/2/7/0/11649-Built_Up.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/11649-Built_Up.jpg) [![alt text](https://cdn.sparkfun.com/r/200-200/assets/learn_tutorials/2/7/0/11888-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/11888-05.jpg) [![alt text](https://cdn.sparkfun.com/r/200-200/assets/learn_tutorials/2/7/0/11262-04a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/11262-04a.jpg) \<-

Each of the sensors that are currently on the PicoBoard (slider, button, light, and sound) are also on this board. We thought it would be great to replicate the PicoBoard firmware to work on this device.

### Suggested Reading

- [What is Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [Alternative Arduino Interfaces](https://learn.sparkfun.com/tutorials/alternative-arduino-interfaces)

## Uploading Firmware

First, we need to upload firmware to the digital sandbox so that it mimics the same packet information as on the PicoBoard. The original C code for the PicoBoard is available on [GitHub](https://github.com/sparkfun/PicoBoard), but this code does not work directly in the Arduino programming IDE.

We ported this code base over and made a few adjustments based on the difference of pin configurations on the digital sandbox.

This code reads all of the sensors on the Digital Sandbox, creates data \"packets\" emulating the PicoBoard, and sends this over to your computer \-- to be read in by Scratch.

### PicoBoard Arduino Code

    language:c
        // DigitalSandboxPico
    //
    // PicoBoard Firmware modified for the DigitalSandBox 
    // Arduino Learning Platform.
    // Ported over from original C code.
    //
    // Modified by: Brian Huang, Sparkfun Electronics
    // Date:  August 7, 2014

    #define SCRATCH_DATA_REQUEST 0x01

    char request = 0;
    unsigned int sensor_value = 0;
    char data_packet[2]= "";

    int SLIDER = A3; // Slider on DS Board
    int SOUND = A2;  // Microphone on DS Board
    int LIGHT = A1;  // Light Detector on DS Board
    int BUTTON = 12; // Push Button on DS Board

    int RA = A0; // Temp
    int RB = 2;  // Switch
    int RC = 3;  // D3 -- Side Port 
    int RD = A4; // A4 -- Top Port

    void setup()
    

    void loop()
    
    }

    void buildScratchPacket(char * packet, int channel, int value)
    

    void sendScratchPacket(char * packet)
    

Copy-paste this code into your Arduino IDE. Select either Lilypad w/ ATMega328 as your board type or Digital Sandbox (if you are using our version of Arduino).

## Using Scratch

Scratch is an amazing platform for teaching an introduction to programming. It uses simple color-coded blocks that snap together to create programs or \"scripts.\" It is designed with kids in mind, but the features and functionality of Scratch are extensive enough for you to create your own data-logging dashboards, arcade-style games, or full-length animations. Once you\'ve uploaded the \"Picoboard Arduino Code,\" the Digital Sandbox will work identically to the PicoBoard in Scratch.

------------------------------------------------------------------------

**Heads up!** As of the writing of this tutorial, Scratch 3.0 and 2.0 does not fully support the PicoBoard. We suggest using [Scratch 1.4](http://scratch.mit.edu/scratch_1.4/) until the full PicoBoard extensions are implemented, tested, and rolled out with Scratch 2.0+.

------------------------------------------------------------------------

To use the PicoBoard Sensor Blocks, click on the blue Sensing Palette:

[![alt text](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/2/7/0/8-8-2014_3-39-58_PM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/8-8-2014_3-39-58_PM.jpg)

At the very bottom of the list, there are two blocks that we can use. One is (*slider* sensor value) and the other one is a boolean/logic block \< sensor *button pressed* ? \> All of the sensors on the PicoBoard (Digital Sandbox) return a value from 0 to 100. It is a scaled value where 0 V ==\> 0 and 5 V ==\> 100 in the Scratch environment.

[![alt text](https://cdn.sparkfun.com/r/300-900/assets/learn_tutorials/2/7/0/8-8-2014_3-41-55_PM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/8-8-2014_3-41-55_PM.jpg)

To help us get started, I like to just make a real quick and simple test script using just these four blocks:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/scratchDemo2.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/scratchDemo2.gif)

Connect / assemble these blocks into a simple program like this:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/scratchtestcomplete.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/scratchtestcomplete.gif)

### Test it out!

Click the green flag and see what happens. The color of Scratch the cat should change as you move the slider back and forth. You should see the cat change from Orange \--\> Yellow \--\> Green \--\> Blue.

It seems like we\'re missing some of the colors. A little digging into the documentation on Scratch shows that the *set color effect* block operates on a scale of 0 - 200. So, to get the full range, we need to multiply the sensor value by 2. Grab a multiply block from the math operators:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/8-8-2014_4-12-15_PM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/8-8-2014_4-12-15_PM.jpg)

Then, re-assemble the blocks so that it looks like this:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/8-8-2014_4-13-33_PM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/8-8-2014_4-13-33_PM.jpg)

Click the green flag and try it again! How many colors does Scratch go through now?

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/BlueScratch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/BlueScratch.jpg)

Play around with other effect options and features. You can tie these to any of the sensors on the PicoBoard (Digital Sandbox) \-- Slider, Light, or Sound. We tied the temperature to the Resistance-A sensor - which is also a range of values from 0 to 100.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/effectOptions.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/effectOptions.jpg)

## Reporting Temperature

Using the temperature scale on the Digital Sandbox is pretty simple - it does require a little math, though. Looking at the datasheet on the temperature sensor on this board [TMP36](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/TMP35_36_37.pdf) can be daunting, but what we care about is this:

------------------------------------------------------------------------

\"The TMP36 is specified from −40°C to +125°C, provides a 750 mV output at 25°C, and operates to 125°C from a single 2.7 V supply.\" and \"Both the TMP35 and TMP36 have an output scale factor of 10 mV/°C.\"

------------------------------------------------------------------------

### Translation

The TMP36 outputs a voltage that varies linearly with the temperature. Because it is linear, we can start with our favorite equation from [Algebra I](https://www.khanacademy.org/math/algebra) \-- the general equation for a line:

*y = mx + b*

*Temp = (slope) \* (voltage) + b*

The proportionality (ratio) between voltage and temperature is 10 mV/°C, but we want our slope in units of °C/mV. So, if we take the reciprocal of 10 mV/°C, this is 0.1 °C/mV. It\'s the same proportion, and it has the correct units. That\'s our slope!

The intercept point requires a little math. Using the information that says \"provides a 750 mV output at 25°C,\" we can find the intercept point.

*25 °C = (0.1 °C/mV)(750 mV) + b*

*25 °C = 75 °C + b*

*-50 °C = b*

### Final Equation

*Temp (°C) = (0.1 °C/mV) \* (voltage in mV) - 50 °C*

### In Scratch

In Scratch, the voltage is scaled from 0 to 100. So \-- let\'s see how this works:

*Temp = (0.1 °C/mV) \* (voltage in Scratch/100)\*(5000 mV) - 50 °C*

Looking at this, I see a lot of decimals, multiplication by 1000\'s and divide by 100s. It seems like we should be able to simplify this. First, let\'s simplify the divide by 100 and multiply by 5000.

*Temp = (0.1 °C/mV) \* (voltage in Scratch\*(50 mV) - 50 °C*

Next, multiply the 0.1 by the 50 and simplify to:

*Temp = (voltage in Scratch\*(5 °C) - 50 °C*

And, in Scratch \-- this looks like:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/tempCalc.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/tempCalc.gif)

## Sample Scratch Script

We created a little sample script to show all of the features all in one example. Feel free to use this, take parts of it, or re-mix it into your own new program. It changes the sprite based on the light input, the slider value, and the sound level.

The sprite will also walks back and forth if you flip the slide switch to the ON (1) position and will change color (and play a sound) when you push the button. Play around with this example. We\'re sure you\'ll come up with other fun ideas too!

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/sampleScratchProgram.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/DigitalSandboxPico.sb)

Click [here](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/0/DigitalSandboxPico.sb) to download a copy of the file to run on your own computer.