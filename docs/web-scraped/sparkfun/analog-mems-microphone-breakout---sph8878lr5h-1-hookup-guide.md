# Source: https://learn.sparkfun.com/tutorials/analog-mems-microphone-breakout---sph8878lr5h-1-hookup-guide

## Introduction

**Note:** This tutorial covers the latest version of the SparkFun Analog MEMS Microphone Breakout ([BOB-19389](https://www.sparkfun.com/products/19389)). We designed the updated version as a drop-in replacement so users with the previous versions of this breakout board ([BOB-9868](https://www.sparkfun.com/products/retired/9868) or [BOB-18011](https://www.sparkfun.com/products/18011)) can follow along with this tutorial. For specific details regarding the microphone ICs, refer to the Documents tab on their product pages or the previous release of this Hookup Guide:\

[ADMP401 & ICS-40180 MEMS Microphone Hookup Guide](https://learn.sparkfun.com/tutorials/mems-microphone-hookup-guide)

The [SparkFun Analog MEMS Microphone Breakout - SPH8878LR5H-1](https://www.sparkfun.com/products/19389) is a simple and easy-to-use microphone for a variety of sound-sensing projects. The on-board microphone is a low-power, omnidirectional microphone with an analog output. It works for both near and long-range uses and is particularly good for portable applications due to its low power consumption. Possible applications include: smartphones, digital video cameras, and keeping an \"ear\" on your pets while you\'re away.

[![SparkFun Analog MEMS Microphone Breakout - SPH8878LR5H-1](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/0/2/5/19389-SparkFun_Analog_MEMS_Microphone_Breakout_-_SPH8878LR5H-1-01.jpg)](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-sph8878lr5h-1.html)

### [SparkFun Analog MEMS Microphone Breakout - SPH8878LR5H-1](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-sph8878lr5h-1.html) 

[ BOB-19389 ]

The SparkFun Analog MEMS Microphone Breakout makes it easy to work with the SPH8878LR5H-1 analog microphone from Knowles.

[ [\$8.95] ]

Read this guide to get an overview of the breakout board and how to use it, including its technical specifications, how to hook it up to a microcontroller, and example code to get started!

### Required Materials

You\'ll need these items along with the MEMS Microphone Breakout to follow along with this tutorial. First up, you\'ll want a microcontroller to power the microphone and monitor its output:

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun Thing Plus - ESP32-S2 WROOM](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/6/2/17743-SparkFun_Thing_Plus_-_ESP32-S2_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html)

### [SparkFun Thing Plus - ESP32-S2 WROOM](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html) 

[ WRL-17743 ]

The SparkFun ESP32-S2 WROOM Thing Plus is a highly-integrated, Feather form-factor development board equipped with the 2.4 GH...

[ [\$24.50] ]

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

[![SparkFun Qwiic Micro - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/0/15423-SparkFun_Qwiic_Micro_-_SAMD21-01b.jpg)](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html)

### [SparkFun Qwiic Micro - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html) 

[ DEV-15423 ]

The SparkFun Qwiic Micro is molded to fit our standard 1\" x 1\" Qwiic board size which makes it our smallest SAMD21 micro-cont...

[ [\$22.95] ]

Building a circuit using this breakout requires some assembly and soldering. You may already have a few of these items but if not, the tools and hardware below help with that assembly:

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

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

### Recommended Reading

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

## Hardware Overview

The SparkFun Analog MEMS Microphone Breakout uses the SPH8878LR5H-1 microphone and amplifies the signal with an OPA344 OpAmp. Let\'s take a closer look at the SPH8878LR5H-1 and the other hardware on the board.

### SPH8878LR5H-1 Microphone

The SPH8878LR5H-1 microphone from Knowles Electronics is a bottom port analog microphone that supports both single-ended and differential modes.

[![MEMS Microphone Breakout - SPH8878LR5H-1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/9/0/MEMS_SPH8878LR5H-1_Mic_Breakout-Front.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/9/0/MEMS_SPH8878LR5H-1_Mic_Breakout-Front.jpg)

We opted for a single-ended output design on this breakout so it can act as a drop-in replacement for users with previous versions of the SparkFun MEMS microphone breakouts. The Left Out- pin is connected to a test point so savvy users who wish to use this microphone in differential mode can tap into that signal with some careful soldering.

The table below outlines some relevant specifications of the SPH8878LR5H-1. For a complete technical overview of the microphone, refer to the [datasheet](https://cdn.sparkfun.com/assets/0/5/8/b/1/SPH8878LR5H-1_Lovato_DS.pdf).

  Parameter                          Min   Typ   Max  Units              Notes
  --------------------------------- ----- ----- ----- ------------------ ------------------------------------------------
  Sensitivity                        -45   -44   -43  dBV/Pa             94 dB SPL @ 1kHz, Single-Ended Mode
  Signal-to-Noise Ratio (\"SNR\")    \-    66    \-   dBV/Pa             94 dB SPL @ 1kHz, A-weighted Single-Ended Mode
  Frequency Range                     7    \-    36   Hz(min)/kHz(max)   
  Acoustic Overload Point            \-    134   \-   dB SPL             

The microphone receives audio input from the bottom of the board. The board breaks out the power pins (VCC and Ground) and the audio output (AUD) from the microphone:

[![MEMS Microphone Breakout - Back](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/9/0/MEMS_SPH8878LR5H-1_Mic_Breakout-Back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/9/0/MEMS_SPH8878LR5H-1_Mic_Breakout-Back.jpg)

- **AUD** - Audio signal output.
- **VCC** - Voltage input (**2.3V to 3.6V**). Supply current of about 265µA.
- **GND** - Ground.

### OpAmp

The SparkFun breakout board includes an OPA344 operational amplifier with a gain of \*64 and a frequency response range of 7.2Hz-19.7KHz. The amplifier\'s AUD output floats at one-half VCC when the mic detects no sound. When held at arms length and talked into, the amplifier will produce a peak-to-peak output of just about 200 mV.

### Board Dimensions

The board measures 0.50\"x 0.40\" (12.70mm x 10.16mm).

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/c/e/3/6/4/SparkFun_Analog_MEMS_Microphone_Breakout_SPH8878LR5H-1_Dimensions.png)](https://cdn.sparkfun.com/assets/c/e/3/6/4/SparkFun_Analog_MEMS_Microphone_Breakout_SPH8878LR5H-1_Dimensions.png)

## Hardware Assembly

Now that we\'re familiar with the microphone breakout, let\'s connect it to a microcontroller and monitor some sound!

### Microphone Breakout Connections

For a permanent connection, we recommend [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) three [wires](https://learn.sparkfun.com/tutorials/working-with-wire) (or headers) to the PTHs on the breakout. We opted for soldering wires to the PTH connectors for a quick permanent connection to the breakout. For a temporary connection during prototyping, you can use IC hooks like [these](https://www.sparkfun.com/products/9741).

We recommend using the following colors of wire to easily distinguish the signals but you can always select a different color if you prefer (or do not have the colors used available).

- [**Red**] for VCC
- [**Black**] for GND
- [**Yellow**] (or some other color not Red or Black) for AUD

[![Wires soldered to MEMS Microphone Breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/9/0/MEMS_SPH8878LR5H-1_Mic_Breakout-Wires_Back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/9/0/MEMS_SPH8878LR5H-1_Mic_Breakout-Wires_Back.jpg)

**Note:** You can use any connection as explained above to connect. If you decide to solder straight header pins, we recommend inserting the straight header pin\'s tail from the top of the board so that the audio input for the microphone is facing away from a surface. However, depending on your application, you can also insert the pins on the side as well. For a low profile application, you will want to use right angle header pins.\
\

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Straight header pins being soldered to MEMS microphone.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_Straight_Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_Straight_Headers.jpg)   [![Right angle header pins being soldered to MEMS microphone.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_Right_Angle_Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/Analog_MEMS_Microphone_ICS-40180_Right_Angle_Headers.jpg)
  *Straight header pins being soldered to MEMS microphone.*                                                                                                                                                                                                                                          *Right angle header pins being soldered to MEMS microphone.*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Connecting to a Microcontroller

Next up we\'ll connect the breakout to a microcontroller we can use to monitor the audio signal output. For this tutorial, we used a [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123). Make the following connections between the breakout and RedBoard Qwiic (or whichever microcontroller you choose):

  RedBoard/Arduino   MEMS Microphone
  ------------------ -----------------
  A0                 AUD
  GND                GND
  3.3V               VCC

\
The completed circuit should look something like the photo below:

[![Completed MEMS Microphone Breakout Circuit with RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/9/0/MEMS_SPH8878LR5H-1_Mic_Breakout-Assembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/9/0/MEMS_SPH8878LR5H-1_Mic_Breakout-Assembly.jpg)

Read on to the next section for Arduino example code to monitor sound volume with the microphone breakout.

## Arduino Software Example

**Note:** If this is your first time using Arduino IDE or board add-on, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Interpreting the Audio Output Signal

The SPH8878LR5H-1 signal output is a varying voltage. When all is quiet, the AUD output floats at one-half the power supply voltage. For example, with a 3.3V power supply, the AUD output will be about 1.65V. In the photo below, the yellow marker on the left side of the oscilloscope screen marks the zero axis for the voltage (aka V = 0). The pulse is the AUD output of a finger snap close to the mic.

[![TestingSensor_Oscilloscope](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/7/TestingSensor_Oscilloscope1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/7/TestingSensor_Oscilloscope1.jpg)

#### Converting ADC to Voltage

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