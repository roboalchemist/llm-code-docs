# Source: https://learn.sparkfun.com/tutorials/spectrum-shield-hookup-guide-v2

## Introduction

**Update:** This tutorial is an updated version of the [original hookup guide](https://learn.sparkfun.com/tutorials/spectrum-shield-hookup-guide) *(retired)* to make use of the Serial Plotter feature of the Arduino IDE, reduce the setup complexity in the examples, and update some of the format of the content. For users looking for the original tutorial, use the following link: *[retired version](https://learn.sparkfun.com/tutorials/spectrum-shield-hookup-guide)*.

Have you ever wanted to have your project react to music? Then this is the product for you! The [Spectrum Shield](https://www.sparkfun.com/products/13116) provides your Arduino board with the capability of measuring a stereo audio input across 7 frequency bands. By reading the amplitude of each band with the ADC of your Arduino board, the users can control how attached devices respond to the audio input.

[![SparkFun Spectrum Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/1/6/8/13116-01a.jpg)](https://www.sparkfun.com/sparkfun-spectrum-shield.html)

### [SparkFun Spectrum Shield](https://www.sparkfun.com/sparkfun-spectrum-shield.html) 

[ DEV-13116 ]

The Spectrum Shield enables your Arduino with the capability of splitting a stereo audio input into 7-bands per channel. You ...

[ [\$29.95] ]

### Materials Required

To follow along with this tutorial, we recommend the following items.

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Arduino Stackable Header Kit - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/7/2/1/6/11417-01a.jpg)](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html)

### [Arduino Stackable Header Kit - R3](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html) 

[ PRT-11417 ]

These headers are made to work with the Arduino Uno R3, Leonardo and new Arduino boards going forward. They are the perfect h...

[ [\$2.75] ]

[![USB Micro-B Cable - 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/3/0/13244-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6.html)

### [USB Micro-B Cable - 6\"](https://www.sparkfun.com/usb-micro-b-cable-6.html) 

[ CAB-13244 ]

This is a USB 2.0 type A to Micro-B 5-pin black cable. You know, the mini-B connector that usually comes with cell phones, Ca...

[ [\$2.50] ]

[![Audio Cable TRRS - 1ft](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/7/7/14163-01.jpg)](https://www.sparkfun.com/audio-cable-trrs-1ft.html)

### [Audio Cable TRRS - 1ft](https://www.sparkfun.com/audio-cable-trrs-1ft.html) 

[ CAB-14163 ]

This is a foot-long white audio cable that has been terminated with two TRRS connectors at each end. TRRS connectors are the ...

[ [\$2.25] ]

### Required Tools

Some assembly is required for this product. You will need a soldering iron, solder, and/or general soldering accessories to solder on headers to your Spectrum Shield.

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[**Additional Accessories**](#Additional_Accessories)

***Click the button** above to toggle a **list of accessories** that are available from our catalog.*

#### Additional Accessories

Below is a sample selection of our other headers and soldering tools in our catalog that you may be interested in. For a full selection of our available [**Headers**](https://www.sparkfun.com/categories/381) or [**Soldering Tools**](https://www.sparkfun.com/categories/49), click on the associated link.

[![Extended GPIO Header - Female (PTH, 0.1in., 2x20-Pin, 13.5mm/9.80mm)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/5/3/16764-2_X_20_Pin_Extended_GPIO_Header_-_Female_-_13.5mm_9.80mm-01.jpg)](https://www.sparkfun.com/extended-gpio-female-header-2x20-pin-13-5mm-9-80mm.html)

### [Extended GPIO Header - Female (PTH, 0.1in., 2x20-Pin, 13.5mm/9.80mm)](https://www.sparkfun.com/extended-gpio-female-header-2x20-pin-13-5mm-9-80mm.html) 

[ PRT-16764 ]

This 2x20 pin female header is meant to allow you to extend the reach of any board with the standard 2x20 GPIO pin footprint.

[ [\$3.25] ]

[![Socket, 24 pins, 0.1 inch (2.54 mm) Spacing](https://cdn.sparkfun.com/r/140-140/assets/parts/3/0/0/9/9/socket_24x1_28386.jpg)](https://www.sparkfun.com/socket-24-pins-0-1-inch-2-54-mm-spacing.html)

### [Socket, 24 pins, 0.1 inch (2.54 mm) Spacing](https://www.sparkfun.com/socket-24-pins-0-1-inch-2-54-mm-spacing.html) 

[ PRT-28386 ]

Single row of 24-holes, female header with standard 0.1\" (2.54mm) spacing.

[ [\$1.85] ]

[![Insulated GPIO Header - Female (PTH, 0.1in., 2x20-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/2/14017-07.jpg)](https://www.sparkfun.com/raspberry-pi-gpio-tall-header-2x20.html)

### [Insulated GPIO Header - Female (PTH, 0.1in., 2x20-Pin)](https://www.sparkfun.com/raspberry-pi-gpio-tall-header-2x20.html) 

[ PRT-14017 ]

This 2x20 \"tall\" header has the same number and spacing of pins as a Raspberry Pi and provides your board with the ability to...

[ [\$3.50] ]

[![GPIO Header - Male (PTH, 0.1in., 2x20-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/3/0/14275-01.jpg)](https://www.sparkfun.com/raspberry-pi-gpio-male-header-2x20.html)

### [GPIO Header - Male (PTH, 0.1in., 2x20-Pin)](https://www.sparkfun.com/raspberry-pi-gpio-male-header-2x20.html) 

[ PRT-14275 ]

This 2x20 male header has the same number and spacing of pins as a Raspberry Pi but is best served when used in conjunction w...

[ [\$1.10] ]

[![PINECIL - Smart Mini Portable Soldering Iron](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/2/7/0/23913-Pinecil-Smart-Mini-Portable-Soldering-Feature3.jpg)](https://www.sparkfun.com/pinecil-smart-mini-portable-soldering-iron.html)

### [PINECIL - Smart Mini Portable Soldering Iron](https://www.sparkfun.com/pinecil-smart-mini-portable-soldering-iron.html) 

[ TOL-23913 ]

The Pinecil is a smart mini portable soldering iron with a 32-bit RISC-V SoC.

[ [\$68.50] ]

[![PINECIL Soldering Iron Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/8/5/KIT-24063-PINECIL-Soldering-Iron-Kit-Feature.jpg)](https://www.sparkfun.com/pinecil-soldering-iron-kit.html)

### [PINECIL Soldering Iron Kit](https://www.sparkfun.com/pinecil-soldering-iron-kit.html) 

[ KIT-24063 ]

The PINECIL Soldering Iron Kit provides a compact powerhouse and everything you need to ignite your DIY dream.

[ [\$119.95] ]

[![Insulated Silicone Soldering Mat](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/7/0/14672-Insulated_Silicone_Soldering_Mat-01.jpg)](https://www.sparkfun.com/insulated-silicone-soldering-mat.html)

### [Insulated Silicone Soldering Mat](https://www.sparkfun.com/insulated-silicone-soldering-mat.html) 

[ TOL-14672 ]

With this Insulated Silicone Soldering Mat you will be provided with the means to protect your desktop, soldering station, or...

[ [\$15.95] ]

[![Soldering Stand with Brass Sponge](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/8/3/TOL-24061-Soldering-Stand-with-Brass-Sponge-Feature.jpg)](https://www.sparkfun.com/soldering-stand-with-brass-sponge.html)

### [Soldering Stand with Brass Sponge](https://www.sparkfun.com/soldering-stand-with-brass-sponge.html) 

[ TOL-24061 ]

A simple metal soldering iron stand with a brass tip cleaner.

[ [\$13.95] ]

### Suggested Reading

We recommend you be familiar with these resources before continuing on with this hookup guide.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/connector-basics)

### Connector Basics 

Connectors are a major source of confusion for people just beginning electronics. The number of different options, terms, and names of connectors can make selecting one, or finding the one you need, daunting. This article will help you get a jump on the world of connectors.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/integrated-circuits)

### Integrated Circuits 

An introduction to integrated circuits (ICs). Electronics\' ubiquitous black chips. Includes a focus on the variety of IC packages.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

## Hardware Overview

### Audio Connections

**Audio Jacks**

The Spectrum Shield contains two stereo audio jacks on the board. The first audio jack, is the input jack (labeled `Input`). This allows users to input audio from any device \-- such as an MP3 player, or cellular phone \-- using a basic [audio cable](https://www.sparkfun.com/products/14163). This connection does not have to be used, as there is another option for adding audio input, at the \"Audio In\" headers, described below.

[![Audio Jacks](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/Audio_Jacks.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/Audio_Jacks.jpg)

The second audio jack is the audio output, labeled `Output`. This jack allows you to pass the audio back out to a speaker or other audio system, while the sound levels are being processed by the Spectrum Analyzer ICs. (*\*Technically, both audio jacks and the audio header are all tied together and can be used as either an input or output.*)

**Audio In Header**

For some projects, you may not be piping audio from a pre-processed source such as a cell phone. For users who want to use things like a [MEMS Mic Breakout](https://www.sparkfun.com/products/9868) or the [Sound Detector](https://www.sparkfun.com/products/12642) as an audio source, there are three header pins that provide an alternative connection method to your shield.

[![Audio In Headers](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/Audio_In_Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/Audio_In_Headers.jpg)

These pins are as follows:

- **L** = Left Audio Input
- **G** = Ground Audio Input
- **R** = Right Audio Input

With both the left and right inputs, you can use stereo devices on these headers. The signals also passes through to the *Input* and *Output* audio jacks.

### MSGEQ7 ICs

The real power of this shield comes from the two MSGEQ7 ICs on the board. These are [CMOS](http://en.wikipedia.org/wiki/CMOS) chips, which are seven band graphic equalizers.

[![MSGEQ7 ICs](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/MSGEQ7_ICs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/MSGEQ7_ICs.jpg)

Upon receiving an audio signal in, these ICs split the the spectrum into seven bands, splitting it at the following frequencies:

- 63Hz
- 160Hz
- 400Hz
- 1kHz
- 2.5kHz
- 6.25kHz
- 16kHZ

For the visual learners, here\'s the frequency graph from the MSGEQ7 datasheet:

[![Frequency_Graph](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/Frequency_Graph.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/Frequency_Graph.JPG)

*Source: [Mixed Signal Integration MSGEQ7 Datasheet](https://www.sparkfun.com/datasheets/Components/General/MSGEQ7.pdf)*

Once the spectrum has been split into these ranges, each band is peak detected and multiplexed. The DC output is a representation of the amplitude of each frequency band. Using the strobe and reset pins on the ICs allows the user to select the DC peak output.

### Shield Connections

There are 4 main pins that the Arduino/RedBoard or other microcontroller connect to the Spectrum Shield.

**Analog Pins** - There are two analog pins connected to the MSGEQ7 ICs. `A0` is the DC analog output from the first IC for the **left** audio channel, while `A1` is the DC analog output from the second, **right** audio channel.

[![Analog Pin Connections](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/2/analog_pins_close_up.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/2/analog_pins_close_up.jpg)

**Control Pins**[] - The control pins connect to the *Strobe* and *Reset* pins on the MSGEQ7; `D4` and `D5`, respectively. In order to enable the *Strobe* pin, you must pull the *Reset* pin **LOW**. To reset the entire multiplexer, pull the *Reset* pin **HIGH**.

[![Strobe and Reset Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/2/control_pins_close_up.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/2/control_pins_close_up.jpg)

The *Strobe* pin, once activated, cycles through each of the channels. After the initial pulse, it starts at 63Hz, pulses each channel until 16kHz, and then repeats, starting back at 63Hz. The DC output for each channel will follow the *Strobe* pulse.

**Remember:** The reset line for the MSGEQ7 IC is **not** the same as the *Reset* push button that resets the entire system (RedBoard + Shield).

### Reset Button

The reset button allows you to reset your Arduino/RedBoard while the shield is inserted. Holding the reset button will pull the reset pin of the ATMega328 (or other microcontroller) low, allowing a system reset. This will restart any sketches currently running on the microcontroller.

[![Reset Button](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/Reset_button.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/3/Reset_button.jpg)

## Hardware Assembly

### Solder Headers

As with any shield, the first step is to choose a header type. We recommend the [stackable headers](https://www.sparkfun.com/products/11417) if you need to stack on other shields; otherwise, the [(straight) male headers](https://www.sparkfun.com/products/116) are the simplest to work with. Feel free to choose any connection method you prefer, but remember that his shield uses the [Arduino Uno R3](https://www.sparkfun.com/products/11021) form factor or footprint when selecting your headers.

\

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/arduino-shields-v2)

### Arduino Shields v2 

April 20, 2020

An update to our classic Arduino Shields Tutorial! All things Arduino shields. What they are and how to assemble them.

You will need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the headers to the shield, so make sure you have all the appropriate supplies before you begin. If you aren\'t sure how to solder on the headers to the shield, please check out our [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) and [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields#installing-headers-preparation) tutorials (*also linked above*).

Once completed, connect the shield to your microcontroller; if you are using [Arduino Uno](https://www.sparkfun.com/products/11224) or [SparkFun RedBoard](https://www.sparkfun.com/products/15123), stack the shield on top.

### Connect Audio System

In the following example, we will be using your computer as the audio source. Plug one end of the [audio cable](https://www.sparkfun.com/products/14163) into the audio jack on your computer and the other end into the `Input` jack on the Spectrum Shield. Feel free to use the `Output` jack on the Spectrum shield to pass the audio out to a speaker or set of headphones.

**Note:** You may need to turn up the volume to meet the threshold for the IC to respond to the audio input. This volume may be above your tolerance for \"comfortable listening\". If this is the case, try using a speaker with an adjustable volume knob to lower the volume to a more reasonable level.

### Connecting to the Computer

The last thing you will need to do is attach the microcontroller to the computer (*with a USB cable*). If you have done everything correctly, it should resemble the image below.

[![Hardware Assembly](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/1/1/3/2/assembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/2/assembly.jpg)

*RedBoard with Spectrum Shield attached to a computer.*

## Arduino Example Code

**Note:** This tutorial assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Serial Plotter Example

Now that you have your hardware all hooked up, it\'s time to analyze some audio signals. Below, we will walk through the [SparkFun_Spectrum_Shield_Serial_Plotter_Demo.ino](https://github.com/sparkfun/Spectrum_Shield/blob/master/Firmware/SparkFun_Spectrum_Serial_Plotter_Demo/SparkFun_Spectrum_Serial_Plotter_Demo.ino) sketch. To begin, download that sketch from the [GitHub Repository](https://github.com/sparkfun/Spectrum_Shield/archive/master.zip), and upload it to your Arduino. (*\*The .zip folder must be extracted and the file for the sketch is located in the **Spectrum_Shield** \> **Firmware** \> **SparkFun_Spectrum_Serial_Plotter_Demo** folder.*)

#### Code Overview

The start of the demo code defines the pins functionality. The Spectrum Shield pin connections to the microcontroller must be defined.

    language:c
    //Declare Spectrum Shield pin connections
    #define STROBE 4
    #define RESET 5
    #define DC_One A0
    #define DC_Two A1

    //Define spectrum variables
    int freq_amp;
    int Frequencies_One[7];
    int Frequencies_Two[7];
    int i;

Note that we declare two arrays `Frequencies_One[]` and `Frequencies_Two[]`; these will be used to store the output of the *seven* frequency bands from the MSGEQ7 ICs. (*\*The `freq_amp` and `i` variables are counters used for iterations in the code and carry minimal significance.*)

In the setup loop, the shield pins must also be declared as `OUTPUT`s for the `STROBE` and `RESET` pins so we can control the shield using the RedBoard. The DC analog pins are each declared as an `INPUT` in the code, because the RedBoard will be reading data *in* from these pins. Once the pins are declared, control pins (`STROBE` and `RESET`) are set to a `LOW` condition/output. A delay is added for the settings to take effect, then the [serial output](https://learn.sparkfun.com/tutorials/serial-communication) is initialized to a **9600 bps** bard rate.

    language:c
    /********************Setup Loop*************************/
    void setup() 

For the main section of the sketch, we loop through two user-defined functions. `Read_Frequenices()` and `Graph_Frequencies()` tell the RedBoard to read the frequencies coming off the Spectrum Shield, and serial print out the analog values, respectively.

    language:c
    /****************Main Function Loop***************************/
    void loop() 

The `Read_Frequencies()` function is defined next in the code. When called, the function initializes/resets the ICs by cycling the `RESET` pin as described earlier in the [Control Pins section](https://learn.sparkfun.com/tutorials/spectrum-shield-hookup-guide#hardware-overview). Then, the function steps through each frequency band on the Spectrum Shield using the `STROBE` pin, reads the DC analog outputs, and stores the values into the predefined frequency arrays.

    language:c
    /*************Pull frquencies from Spectrum Shield****************/
    void Read_Frequencies() 
    }

The data is retrieved through the `Graph_Frequencies()` function. With this function, the RedBoard returns the analog value for the frequencies being read by the Spectrum Shield through the serial port.

    language:c
    /*****************Print Out Band Values for Serial Plotter*****************/
    void Graph_Frequencies() 
      Serial.println();
    }

### Code Operation

With the sketch uploaded to your board, you are now able to analyze the different frequency bands of your audio input. Pull, up the [Serial Monitor](https://learn.sparkfun.com/tutorials/serial-communication) and set the baud rate to **9600**. Then, using your computer play an audio sample. You should see the numbers in the columns of the Serial Monitor change with the audio.

**Note:** The \"*strength*\" and quality of the audio output from your computer is dependent on the sound card/chip use by your computer. Users may need to change their audio/speaker settings; as a baseline, I recommend turning up the audio on your computer to about 65% as a starting point.

Below, are some audio samples that users can use to test the Spectrum Shield:

[Online Tone Generator](https://www.szynalski.com/tone-generator/) - a website based tone generator.

[Youtube Video](https://www.youtube.com/watch?v=qNf9nzvnd1k) - increases the (audio) signal frequency from 20 Hz to 20kHz.

Try playing the Youtube video and using the Serial Plotter of the Arduino IDE. You should see a response curve similar to the one below. Notice how the shapes resemble the figure from the datasheet in the [**Hardware Overview**](https://learn.sparkfun.com/tutorials/spectrum-shield-hookup-guide-v2#hardware-overview) section.

[![Serial Plotter](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/2/spectrum_plot.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/3/2/spectrum_plot.gif)

### Additional Examples

There are plenty of projects out there using the Spectrum Shield, so do a bit of searching if you need some more inspiration! Additionally, you can refer to the [original tutorial](https://learn.sparkfun.com/tutorials/spectrum-shield-hookup-guide), which provides other examples including one from Bliptronics, the collaborator on the Spectrum Shield, which works with the Spectrum Shield and an LED matrix.