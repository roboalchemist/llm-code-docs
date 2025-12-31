# Source: https://learn.sparkfun.com/tutorials/i2s-audio-breakout-hookup-guide

## Introduction

The [I2S Audio Breakout](https://www.sparkfun.com/products/14809) board uses the MAX98357A digital to analog converter (DAC), which converts I2S (not be confused with I2C) audio to an analog signal to drive speakers. The MAX98357A has a built in class D amplifier which can deliver up to 3.2W of power into a 4Ω load. For more information, see the [Hardware Overview](https://learn.sparkfun.com/tutorials/i2s-audio-breakout-hookup-guide#hardware-overview) section below.

[![SparkFun I2S Audio Breakout - MAX98357A](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/0/7/6/14809-SparkFun_I2S_Audio_Breakout-01.jpg)](https://www.sparkfun.com/sparkfun-i2s-audio-breakout-max98357a.html)

### [SparkFun I2S Audio Breakout - MAX98357A](https://www.sparkfun.com/sparkfun-i2s-audio-breakout-max98357a.html) 

[ DEV-14809 ]

The SparkFun I2S Audio Breakout board uses the MAX98357A digital to analog converter (DAC), which converts I2S audio to an an...

[ [\$7.50] ]

### Suggested Tools

You will need a soldering iron, solder, [general soldering accessories](https://www.sparkfun.com/categories/49), screw driver, and hobby knife.

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

[![Weller WE1010 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/6/1/14734-Weller_WE1010_Soldering_Station_-01.jpg)](https://www.sparkfun.com/products/14734)

### [Weller WE1010 Soldering Station](https://www.sparkfun.com/products/14734) 

[ TOL-14734 ]

The WE1010 from Weller is a powerful 70 watt soldering station that is perfect for passionate hobbyists, DIYers, and anyone w...

**Retired**

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide)

### ESP32 Thing Hookup Guide 

An introduction to the ESP32 Thing\'s hardware features, and a primer on using the WiFi system-on-chip in Arduino.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/esp32-thing-motion-shield-hookup-guide)

### ESP32 Thing Motion Shield Hookup Guide 

Getting started with the ESP32 Thing Motion Shield to detect movements using the on-board LSM9DS1 IMU and adding a GPS receiver. Data can be easily logged by adding an microSD card to the slot.

## Hardware Overview

The I2S audio breakout converts the digital audio signals using the [I2S standard](https://en.wikipedia.org/wiki/I%C2%B2S) to an analog signal and amplifies the signal using a class D amplifier. The board can be configured to output only the left channel, right channel, or both. For more information about how to configure the board, refer to the Jumper Selection section below.

[![I2S Audio Breakout Board Top View](https://cdn.sparkfun.com/assets/parts/1/3/0/7/6/14809-SparkFun_I2S_Audio_Breakout-02.jpg)](https://cdn.sparkfun.com/assets/parts/1/3/0/7/6/14809-SparkFun_I2S_Audio_Breakout-02.jpg)

### Board Specs

Parameter

Description

Supply Voltage Range

**2.5V - 5.5V.**

Output Power

3.2W into 4Ω at 5V.

Output Channel Selection

Left, Right, or Left/2 + Right/2 (Default).

Sample Rate

8kHz - 96kHz.

Sample Resolution

16/32 bit.

Quiescent Current

2.4mA.

Additional Features

Filterless Class D outputs, no MCLK required, click and pop reduction, short-circuit and thermal protection.

\

### Pin Descriptions

The SparkFun I2S audio breakout board is fairly simple, requiring only a few pin connections to get the board working.

[![Highlight of Input Connections](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/I2S_Pin_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/I2S_Pin_Highlight.jpg)

#### Inputs

Pin Label

Description

LRCLK

Frame clock (left/right clock) input.

BCLK

Bit clock input.

DIN

Serial data input.

GAIN

Gain setting. Can be set to +3/6/9/12/15dB. Set to +9dB by default.

SD

Shutdown and channel select. Pull low to shutdown, or use the jumpers to select the channel output (see jumper selection for more information).

GND

Connect to ground

VDD

Power input. Must be between **2.5** and **5.5VDC**.

\

#### Outputs

The output is where you\'ll connect your speaker.

[![Highlight of Output Connections](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/I2S_Output_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/I2S_Output_Highlight.jpg)

Pin Label

Description

\+

Positive speaker output.

\-

Negative speaker output.

\

Speaker wire can either be [soldered](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) directly to the output pads, but if screw terminals are more your style, you can use our [3.5mm screw terminals](https://www.sparkfun.com/products/8084).

[![Screw Terminals 3.5mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/7/08084-01.jpg)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html)

### [Screw Terminals 3.5mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html) 

[ PRT-08084 ]

Screw Terminal 3.5mm pitch pins with slide-locking together to form any size you need. Rated up to 125V @ 6A, and can accept ...

[ [\$1.25] ]

### Jumper Selection

By default the board is configured in \"mono\" operation, meaning the left and right signals are combined together to drive a single speaker.

[![Highlight Of Jumper Selection](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/I2S_Jumper_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/I2S_Jumper_Highlight.jpg)

If you want a separate speaker for the left and right audio channels you\'ll first need to cut the mono jumper as pictured below.

[![Mono Trace Jumper Cut](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/2/Mono_Cut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/Mono_Cut.jpg)

To configure the board to respond to a specific audio channel, you\'ll need to close the stereo jumper as shown below.

[![Single Channel Select Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/2/Left_Right.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/Left_Right.jpg)

### Gain Selection

In addition to being able to select the audio channel output, the gain can also be configured in a few ways. The gain of the amplifier can be configured from as **low as +3dB to as high as +15dB**. While the channel selection can be configured on board, the gain however is controlled externally using the gain pin. By default, the board is configured for **+9dB**, but can be changed using the table below.

Gain (dB)

Gain Pin Connection

15

Connected to GND through a 100kΩ resistor.

12

Connected to GND.

9

Unconnected (**Default**).

6

Connected to VDD.

3

Connected to VDD through a 100kΩ resistor.

\

## Examples

**Note:** These example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

This board should work with any microcontroller or single board computer that has I2S capable pins. In these examples, we\'re going to look at a pretty powerful library that allows you to use an [ESP32 Thing](https://www.sparkfun.com/products/13907) to play audio from a wide variety of sources. First, we\'ll play an audio file which is stored in the ESP32\'s program memory, and once we have that working we\'ll look at creating a MP3 trigger. The following libraries are needed to run the examples that were originally written for the ESP8266, but also work with the ESP32.

### ESP8266Audio Arduino Library

You\'ll need to install the [ESP8266 Audio Arduino Library](https://github.com/earlephilhower/ESP8266Audio), written by [Earle F. Philhower](https://github.com/earlephilhower), which you can get from the link below. This library will allow you to play a wide variety of audio formats including: AAC, FLAC, MIDI, MOD, MP3, RTTTL, and WAV. To use the library, you can add the library from Arduino by selecting **Sketch \*\* \> \*\*Include Library \*\* \> \*\*Add .ZIP Library**\... and selecting the **.zip** file from wherever you store your file downloads.

[ESP8266 Audio Library (ZIP)](https://github.com/earlephilhower/ESP8266Audio/archive/master.zip)

### ESP8266_Spiram Arduino Library

The ESP8266 Audio library depends on the [ESP8266 Spiram library](https://github.com/Gianbacchio/ESP8266_Spiram), written by [Giancarlo Bacchio](https://github.com/Gianbacchio), which will also need to be downloaded. You can download the library from the link below. Installing the library follows the same process as outlined above.

[ESP8266 Spiram Library (ZIP)](https://github.com/Gianbacchio/ESP8266_Spiram/archive/master.zip)

### First Test

In this first example, we\'ll run a quick example sketch to make sure the I2S audio breakout board is wired correctly and is working.

[![ESP32 Connected to I2S Breakout Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/2/I2S_Example_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/I2S_Example_1.jpg)

#### Required Materials

The parts used in this example are listed in the wishlist below. You may not need everything though depending on what you have. Add it to your cart, read through the example, and adjust the cart as necessary.

#### Hookup Table

The connections that need to be made to the ESP32 are list below.

  ESP32 Pin   I2S Audio Breakout Pin
  ----------- ------------------------
  VUSB/3V3    VDD
  GND         GND
  GPIO 22     DIN
  GPIO 26     BCLK
  GPIO 25     LRCLK

\

Make sure to also connect a speaker to the I2S audio breakout board\'s output pins.

#### Example Code

We\'re going to use one of the examples that comes with the library named **\"PlayAACFromPROGMEM\"**. With the library installed, open the example located in: **File** \> **Examples** \> **ESP8266Audio** \> **PlayAACFromPROGMEM** .

[![Where to find Example Sketch \"PlayAACFromPROGMEM\"](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/2/Example_Sketch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/Example_Sketch.jpg)

Before we upload the code, we\'re going to add two lines of code (as highlighted in the image below). The first line is going to adjust the volume, which we add after we initialize the I2S output (`out = new AudioOutputI2S();`). After the output is initialized, we\'re going to add `out -> SetGain(0.125);`. As the name suggests this sets the gain of the output, which takes a floating point number and has a maximum value of 4.0. The second line will reduce hum at the end of the audio clip by adding `aac -> stop();` in the else statement in the main `loop()`. After you upload the sketch to your ESP32, you should hear Homer Simpson\'s thoughts of perpetual motion machines if everything is working.

[![Hightlight of changes made to the example sketch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/2/Example_Sketch_Changes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/Example_Sketch_Changes.jpg)

### ESP32 MP3 Trigger

Now that we know the board is working, let\'s take it up a notch. In this next example, we\'ll create a MP3 trigger that works similar to our [MP3 Trigger](https://www.sparkfun.com/products/13720).

[![ESP32 Connected to I2S Breakout and pushbuttons](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/2/I2S_Example_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/2/I2S_Example_2.jpg)

#### Required Materials

For this example, we\'ll need to add a few more parts to the ones we used in the previous example (including a second breadboard). You may not need everything though depending on what you have. Add it to your cart, read through the example, and adjust the cart as necessary.

Before we add code, we\'ll need some audio files to play. Any MP3 audio file should work, you\'ll just need to copy them over to your microSD card using a [microSD USB Reader](https://www.sparkfun.com/products/13004). Before ejecting the microSD card from your computer, make sure to relabel the files **TRACKn.mp3**, where n is a integer number between 0-9. The I2S audio breakout board has the same pin connections as the previous example, but this time we\'re going to change the audio source from PROGMEM to our microSD card. The last step before adding the code below, is to add headers to the [ESP32 Thing](https://www.sparkfun.com/products/13907), as well as the [Motion Shield](https://www.sparkfun.com/products/14430), as outlined in the [hookup guide](https://learn.sparkfun.com/tutorials/esp32-thing-motion-shield-hookup-guide).

    language:c
    /* SparkFun I2S Audio Breakout Demo
     * Created by: Alex Wende
     * 8/3/2018
     * 
     * Uses a ESP32 Thing to create a MP3 trigger using 
     * the I2S Audio Breakout board.
     * 
     * Parts you'll need:
     * - I2S Audio Breakout board (https://www.sparkfun.com/products/14809)
     * - ESP32 Thing (https://www.sparkfun.com/products/13907)
     * - Micro SD Breakout (https://www.sparkfun.com/products/544)
     * - A microSD card (https://www.sparkfun.com/products/13833)
     * - Speaker (4-8ohms)
     * 
     * The following libraries need to be installed before
     * uploading this sketch:
     * - ESP8266 Audio (https://github.com/earlephilhower/ESP8266Audio)
     * - SRam Library (https://github.com/Gianbacchio/ESP8266_Spiram)
     */

    #include <Arduino.h>
    #include "AudioGeneratorMP3.h"
    #include "AudioOutputI2S.h"
    #include "AudioFileSourceSD.h"
    #include "driver/i2s.h"
    #include <SD.h>

    //define trigger pins
    #define TRIGGER0 13
    #define TRIGGER1 12
    #define TRIGGER2 14
    #define TRIGGER3 27
    #define TRIGGER4 32
    #define TRIGGER5 5
    #define TRIGGER6 15
    #define TRIGGER7 2
    #define TRIGGER8 0
    #define TRIGGER9 4

    //Initialize ESP8266 Audio Library classes
    AudioGeneratorMP3 *mp3;
    AudioFileSourceSD *file;
    AudioOutputI2S *out;

    volatile bool playing = 0;
    volatile byte loadTrack = 0;

    //External Interrupt function with software switch debounce
    void IRAM_ATTR handleInterrupt()
    
      last_interrupt_time = interrupt_time;
    }

    void setup()
    
      Serial.println("initialization done.");
      delay(100);
    }

    void loop()
    

      if(playing && mp3->isRunning()) 
      }
    }

With the code on the board, we can see what the sketch does. You can connect [momentary pushbutton switches](https://www.sparkfun.com/products/97) to each of the trigger pins outlined in the table below, with the other end of the switch connected to ground. Another option is to take a ground wire and touch it to one of the trigger pins. When the pin is pulled down to ground, it triggers the corresponding track to play. If a track is still playing when a new pin is triggered, that track will stop and the new track will play.

  Audio File   ESP32 GPIO Pin
  ------------ ----------------
  TRACK0.mp3   13
  TRACK1.mp3   12
  TRACK2.mp3   14
  TRACK3.mp3   27
  TRACK4.mp3   32
  TRACK5.mp3   5
  TRACK6.mp3   15
  TRACK7.mp3   2
  TRACK8.mp3   0
  TRACK9.mp3   4

\