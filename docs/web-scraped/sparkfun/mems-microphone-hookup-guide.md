# Source: https://learn.sparkfun.com/tutorials/mems-microphone-hookup-guide

## Introduction

**Note:** This tutorial was originally written for the MEMS microphone breakout with ADMP401. However, the IC is EOL. The replacement is ICS-40180 from InvenSense. The overall functionality is the same with some slight differences in the specifications, which will be outlined in the Hardware Overview.

### Introduction

The [SparkFun MEMS microphone breakout board](https://www.sparkfun.com/products/18011) is a simple and easy-to-use microphone for a variety of sound-sensing projects. The on-board microphone is a low-power, omnidirectional microphone with an analog output. It works for both near and long-range uses and is particularly good for portable applications due to its low power consumption. Possible applications include: smartphones, digital video cameras, and keeping an \"ear\" on your pets while you\'re away. Below are boards that breakout the ADMP401 and ICS-40180 microphones.

[![SparkFun MEMS Microphone Breakout - INMP401 (ADMP401)](https://cdn.sparkfun.com/r/600-600/assets/parts/3/9/5/1/09868-01a.jpg)](https://www.sparkfun.com/products/9868)

### [SparkFun MEMS Microphone Breakout - INMP401 (ADMP401)](https://www.sparkfun.com/products/9868) 

[ BOB-09868 ]

This tiny breakout board features the ADMP401 MEMS microphone. One of the key advantages to this breakout and microphone is t...

**Retired**

[![SparkFun Analog MEMS Microphone Breakout - ICS-40180](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/2/2/1/18011-SparkFun_Analog_MEMS_Microphone_Breakout_-_ICS-40180-01.jpg)](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-ics-40180.html)

### [SparkFun Analog MEMS Microphone Breakout - ICS-40180](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-ics-40180.html) 

[ BOB-18011 ]

The SparkFun Analog MEMS Microphone Breakout makes it easy to work with the InvenSense ICS-40180 analog microphone.

**Retired**

Read this hook-up guide to get an overview each breakout board and how to use it, including its technical specifications, how to hook it up to a microcontroller, and an example code to get started!

Questions? Feedback? Want to share an awesome project you built using this sensor? Write a [comment](https://learn.sparkfun.com/tutorials/mems-microphone-hookup-guide/discuss) at the end of this tutorial!

### Suggested Reading

To successfully use the SparkFun MEMS microphone breakout board, you\'ll need to be familiar with Arduino microcontrollers, analog (aka ADC) input, and sound waves. For folks new to these topics, check out the following resources to get a feel for the concepts and verbiage used throughout this tutorial.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

We also suggest reading the following for more information about sound and specifications for the IC that is populated on your version of the MEMs microphone breakout.

- [The Wikipedia page on the science of sound!](https://en.wikipedia.org/wiki/Sound)
- And finally, and most importantly, the datasheet for your IC!
  - [ADMP401](http://www.analog.com/media/en/technical-documentation/obsolete-data-sheets/ADMP401.pdf)
  - [ICS-40180](https://cdn.sparkfun.com/assets/8/e/7/e/b/DS-000021-v1.22.pdf)

## Hardware Overview

**Note:** While the characteristics for each MEMS microphone are similar, the footprint for the ADMP401 is different for the ICS-40180. Make sure to check the design files for more information if you are designing your own board with the IC.

The SparkFun MEMS Microphone breakout board breaks out the microphone for sound detection. Each version breaks out the ADMP401 and ICS-40180 on the top side of the board. The signal is amplified with the OPA344 OpAmp.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View of ADMP401 Breakout](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/09868-02a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/09868-02a.jpg)   [![Top View of ICS-40180](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/18011-SparkFun_Analog_MEMS_Microphone_Breakout_-_ICS-40180-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/18011-SparkFun_Analog_MEMS_Microphone_Breakout_-_ICS-40180-03.jpg)
  *Top View of ADMP401 Breakout*                                                                                                                                                *Top View of ICS-40180 Breakout*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The board receives audio input from the bottom of the board. There are three ports, which are labeled next to each pin.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Bottom View of ADMP401 Breakout](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/09868-03a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/09868-03a.jpg)   [![Bottom View of ICS-40180](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/18011-SparkFun_Analog_MEMS_Microphone_Breakout_-_ICS-40180-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/18011-SparkFun_Analog_MEMS_Microphone_Breakout_-_ICS-40180-02.jpg)
  *Bottom View of ADMP401 Breakout*                                                                                                                                                *Bottom View of ICS-40180 Breakout*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- **AUD** - Audio signal output.
- **VCC** - Voltage input (**1.5V to 3.3V**). To power this lil\' mic, use a DC voltage with a supply current of about 250μA for ADMP401 or 260μA for ICS-40180. We\'ll be using **3.3V** from an Arduino\'s.
- **GND** - Ground.

For technically-minded folks, here are some of the features of the ADMP401 and ICS-40180. Make sure to check out datasheet for the [ADMP401](http://www.analog.com/media/en/technical-documentation/obsolete-data-sheets/ADMP401.pdf) or [ICS-40180](https://cdn.sparkfun.com/assets/8/e/7/e/b/DS-000021-v1.22.pdf) for a complete overview of the microphone.

  Electrical Characteristics             ADMP401            ICS-10480
  -------------------------------------- ------------------ -----------------
  High Signal-to-Noise Ratio (\"SNR\")   62 dbA             65 dbA
  Sensitivity                            about -42 dBV      about -38 dBV
  Flat Frequency Response                100 Hz to 15 kHz   60 Hz to 20 kHz
  Low Current Consumption                \<250 μA @ 3.3V    \<260 μA @ 3.3V
  Maximum Acoustic Input                 120 dB             124 dB

The SparkFun breakout board includes an amplifier with a gain of 67 for the ADMP401 and a gain of 65 for the ICS-10480, which is more than sufficient for the microphones. The amplifier\'s AUD output will float at one-half Vcc when there is no sound. When held at arms length and talked into, the amplifier will produce a peak-to-peak output of about 200 mV.

### Board Dimensions

The board dimensions for the breakout are 0.55\"x 0.40\". The location of the audio input and header pins for each microphone is the same even though the size of the IC and locations of the components are different.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Board Dimensions for ADMP401](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/SparkFun_MEMS_Mic_Breakout-ADMP401_Board_Dimension.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/SparkFun_MEMS_Mic_Breakout-ADMP401_Board_Dimension.png)   [![Board Dimensions for ICS-40180](https://cdn.sparkfun.com/r/734-734/assets/learn_tutorials/2/9/7/SparkFun_Analog_MEMS_Microphone_Breakout_ICS40180_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/SparkFun_Analog_MEMS_Microphone_Breakout_ICS40180_Board_Dimensions.png)
  *Board Dimensions for ADMP401*                                                                                                                                                                                                                                            *Board Dimensions for ICS-40180*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Click on image for a closer view.*

## Hardware Hookup (Quickstart)

If all of this is super familiar, here\'s all you need to get started:

1.  For a temporary connection, you can use IC hooks. For a permanent connection, we recommend [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) three [wires](https://learn.sparkfun.com/tutorials/working-with-wire) (or headers) to each MEMS microphone breakout board ports.

2.  Connect the Vcc port to 3.3V (or anything between 1.5 and 3.3V) and the GND port to ground.

3.  Connect the AUD port to an analog (ADC) input on a microcontroller.

4.  Read in the ADMP401 analog signal and measure/record all the sounds! (Also remember it\'s a sound signal, so you\'ll likely want to use the *amplitude* of the sound wave rather than the raw voltage output.)

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Wires Soldered to ADMP401](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/MEMS_Microphone_ADMP401_wires-back1A.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/MEMS_Microphone_ADMP401_wires-back1A.jpg)   [![IC Hook Connected to ICS-40180](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_IC_Hooks.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_IC_Hooks.jpg)
  *Wires Soldered to ADMP401*                                                                                                                                                                                                                *IC Hook Connected to ICS-40180*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** You can use any connection as explained above to connect. If you decide to solder straight header pins, we recommend inserting the straight header pin\'s tail from the top of the board so that the audio input for the microphone is facing away from a surface. However, depending on your application, you can also insert the pins on the side as well. For a low profile application, you will want to use right angle header pins.\
\

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Straight header pins being soldered to MEMS microphone.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_Straight_Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_Straight_Headers.jpg)   [![Right angle header pins being soldered to MEMS microphone.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_Right_Angle_Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_Right_Angle_Headers.jpg)
  *Straight header pins being soldered to MEMS microphone.*                                                                                                                                                                                                                                          *Right angle header pins being soldered to MEMS microphone.*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Hardware Hookup

For a more in-depth example, follow along with the following steps:

1.  For a temporary connection, you can use IC Hooks. For a permanent connection, [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) three [wires](https://learn.sparkfun.com/tutorials/working-with-wire) (or header pins) to the breakout board ports. We recommend using the following colors to easily distinguish the board ports. If you do not have the color wire available, you can always select a different color as well.

    - red for Vcc
    - black for GND
    - yellow (or some other color) for AUD\
      \

2.  Connect the Vcc port to the 3.3 V output of a [microcontroller](https://www.sparkfun.com/categories/242) (or any power supply between 1.5 and 3.3 V).

3.  Connect the GND port to GND on the microcontroller.

4.  Connect the AUD port to an analog, or ADC, input on the microcontroller. In this case, we are using A0.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/Arduino_Nano_Analog_MEMS_Microphone_Sensor_Bradboard_Wire_Closeup1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/Arduino_Nano_Analog_MEMS_Microphone_Sensor_Bradboard_Wire_Closeup1.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_IC_Hooks_Arduino_RedBoard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_IC_Hooks_Arduino_RedBoard.jpg)
  *Wire Connected to Arduino*                                                                                                                                                                                                                                                   *IC Hooks Connected to Arduino*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also use the following hookup table as a quick reference.

  Arduino   MEMS Microphone
  --------- -----------------
  A0        AUD
  GND       GND
  3.3V      VCC

The next section will cover how to read the audio signal from the microphone to a microcontroller.

## Arduino Software Example

**Note:** If this is your first time using Arduino IDE or board add-on, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

The ADMP401 signal output is a varying voltage. When all is quiet (shhhh), the AUD output will float at one-half the power supply voltage. For example, with a 3.3V power supply, the AUD output will be about 1.65V. In the photo below, the yellow marker on the left side of the oscilloscope screen marks the zero axis for the voltage (aka V = 0). The pulse is the AUD output of a finger snap close to the mic.

[![TestingSensor_Oscilloscope](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/TestingSensor_Oscilloscope1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/TestingSensor_Oscilloscope1.jpg)

### Converting ADC to Voltage

The microcontroller analog (ADC) input converts our audio signal into an integer. The range of possible ADC values depends on which microcontroller you are using. For an Arduino microcontroller with an ATmega328P, the analog resolution is 10-bits. This range is between 0 and 1023, so the resolution of our ADC measurement is 1024. To convert our analog measurement into a voltage, we use the following equation:

[![equation](https://cdn.sparkfun.com/assets/3/9/0/b/6/51140300ce395f777e000002.png)](https://cdn.sparkfun.com/assets/3/9/0/b/6/51140300ce395f777e000002.png)

In our case, the *ADC Resolution* is 1024, and the *System Voltage* 3.3 V. We\'ll need to add this equation in our code to convert our *ADC Reading* into a voltage.

### But Wait, What Are We Actually Measuring??

For many applications that deal with sound (which is a wave), we\'re mostly interested in the [**amplitude**](https://en.wikipedia.org/wiki/Amplitude) of the signal. In general, and for the sake of simplicity, a larger amplitude means a louder sound, and a smaller amplitude means a quieter sound (and the sound wave frequency roughly corresponds to [pitch](https://en.wikipedia.org/wiki/Sound#Pitch)). Knowing the amplitude of our audio signal allows us to build a [sound visualizer](https://www.youtube.com/watch?v=0jW1Kuw79hA), a volume unit (\"VU\") meter, set a volume threshold trigger, and other cool and useful projects!

To find the audio signal amplitude, take a bunch of measurements in a small time frame (e.g. 50 ms, the lowest frequency a human can hear). Find the minimum and maximum readings in this time frame and subtract the two to get the [peak-to-peak amplitude](https://en.wikipedia.org/wiki/Amplitude#Peak-to-peak_amplitude). We can leave it at that, or divide the peak-to-peak amplitude by a factor of two to get the wave amplitude. We can use the ADC integer value, or convert this into voltage as described above.

[![MEMS_OutputTable](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/MEMS_OutputTable_012017.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/MEMS_OutputTable_012017.jpg)

### Example Code

**Note:** For a simple test to see if your microphone is working, try using the example below! Select your Arduino board, COM port, and hit the upload button.\
\

``` c
/***************************
  Simple Example Sketch for the SparkFun MEMS Microphone Breakout Board

**************************/

// Connect the MEMS AUD output to the Arduino A0 pin
int mic = A0;

// Variable to hold analog values from mic
int micOut;

void setup() 

void loop() 
```

Open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) or Serial Plotter to view the output. Snap, clap, or speak into the microphone and observe the readings. The raw value will be higher as the microphone picks up louder sounds. For a more refined example, check out the example code below! You can also view the raw output in the example code below but it requires a little bit more effort.

Below is a simple example sketch to get you started with the MEMS microphone breakout board. You can find the code in the [GitHub repo](https://github.com/jenfoxbot/MEMSMicHookUpGuide) as well. The code, written for an Arduino microcontroller, includes a conversion equation from the ADC Reading to voltage, a function to find the audio signal peak-to-peak amplitude, and a simple VU Meter that outputs to the Arduino [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux). For a more visual output, you can also use the Serial Plotter.

Be sure to read the comments in the code to understand how it works and to adapt it to fit your needs. Select your Arduino board, COM port, and hit the upload button.

    language:c
    /***************************
     * Example Sketch for the SparkFun MEMS Microphone Breakout Board
     * Written by jenfoxbot <jenfoxbot@gmail.com>
     * Code is open-source, beer/coffee-ware license.
     */

    // Connect the MEMS AUD output to the Arduino A0 pin
    int mic = A0;

    // Variables to find the peak-to-peak amplitude of AUD output
    const int sampleTime = 50; 
    int micOut;

    //previous VU value
    int preValue = 0; 

    void setup() 

    void loop()    

    // Find the Peak-to-Peak Amplitude Function
    int findPTPAmp()
            else if (micOut < minAmp)
            
          }
       }

      PTPAmp = maxAmp - minAmp; // (max amp) - (min amp) = peak-to-peak amplitude
      double micOut_Volts = (PTPAmp * 3.3) / 1024; // Convert ADC into voltage

      //Uncomment this line for help debugging (be sure to also comment out the VUMeter function)
      //Serial.println(PTPAmp); 

      //Return the PTP amplitude to use in the soundLevel function. 
      // You can also return the micOut_Volts if you prefer to use the voltage level.
      return PTPAmp;   
    }

    // Volume Unit Meter function: map the PTP amplitude to a volume unit between 0 and 10.
    int VUMeter(int micAmp)
    }