# Source: https://learn.sparkfun.com/tutorials/hackers-in-residence---hacking-mindwave-mobile

## Introduction

**Note:** Brought to you by Hacker in Residence, Sophi Kravitz!\
\

[](https://news.sparkfun.com/1299 "October 29, 2013: We're excited to introduce you to our latest hackers-in-residence: Sophi Kravitz and Shane Clements!")

### Hackers-in-Residence: Sophi Kravitz & Shane Clements 

[October 29, 2013]

Read Post

Have you ever wanted to control something just by thinking about it? Well, you\'re in luck. The [MindWave](http://store.neurosky.com/products/mindwave-1) allows you to turn electronic signals that flow in your body into digital signals that can be understood by a microcontroller. There is also the [MindWave Mobile](http://store.neurosky.com/products/mindwave-mobile), which is designed to interface with your mobile devices.

[![NeuroSky MindWave Mobile 2](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/9/9/4/14758-NeuroSky_MindWave_Mobile2-04.jpg)](https://www.sparkfun.com/products/14758)

### [NeuroSky MindWave Mobile 2](https://www.sparkfun.com/products/14758) 

[ SEN-14758 ]

The MindWave Mobile 2 from NeuroSky is an EEG headset that safely measures and transfers the power spectrum data via Bluetoot...

**Retired**

This tutorial will serve as half teardown/review and half project. After we explore the inner-workings of the MindWave Mobile, we\'ll switch gears and focus on hacking it.

[![mindwave mobile](https://cdn.sparkfun.com/r/600-600/assets/e/c/e/5/4/52cda9afce395f610c8b456a.jpg)](https://cdn.sparkfun.com/assets/e/c/e/5/4/52cda9afce395f610c8b456a.jpg)

### Covered in This Tutorial

This tutorial will go over:

- What is MindWave Mobile?
- Configuring the RN42 Bluetooth module
- Pairing MindWave Mobile with the RN42
- What is the data you will see coming out of the MindWave? What does it mean?
- Programming the Arduino with provided source code to see MindWave data
- Using Processing to graph specific values from the digital data
- Next steps, after the MindWave

### Suggested Reading

This tutorial builds on some previously covered topics. Please visit any of the links below if you are unfamiliar with the concepts mentioned.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/what-is-electricity)

### What is Electricity? 

We can see electricity in action on our computers, lighting our houses, as lightning strikes in thunderstorms, but what is it? This is not an easy question, but this tutorial will shed some light on it!

[](https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing)

### Connecting Arduino to Processing 

Send serial data from Arduino to Processing and back - even at the same time!

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/bluetooth-basics)

### Bluetooth Basics 

An overview of the Bluetooth wireless technology.

[](https://learn.sparkfun.com/tutorials/using-the-bluesmirf)

### Using the BlueSMiRF 

How to get started using the BlueSMiRF and Bluetooth Mate Silvers.

### Suggested Viewing

## What is the MindWave Mobile?

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/9/f/e/0/3/52cda964ce395f401b8b456b.jpg)](https://cdn.sparkfun.com/assets/9/f/e/0/3/52cda964ce395f401b8b456b.jpg)

*The MindWave Mobile from [NeuroSky](http://neurosky.com/)*

To understand the MindWave and MindWave Mobile, we must first understand what an EEG sensor is. The first recording of the human brain\'s electric field was made by [Hans Berger](http://en.wikipedia.org/wiki/Hans_Berger), a German psychiatrist, in 1924. Berger gave the recording the name [electroencephalogram (EEG)](http://en.wikipedia.org/wiki/Electroencephalography). Put simply, the EEG is performed by placing electrodes all over the subject\'s scalp, and then reading in the electrical signals for analysis. Fast forward to today, and you have all of this technology packed into a compact form factor that is the MindWave and the MindWave Mobile.

### Project Scope

The amplitude of the EEG is \~ 100 µV when measured on the scalp, and about 1-2 mV when measured on the surface of the brain. The bandwidth of this signal is from under 1 Hz to about 50 Hz.

Because of the amplitude and low frequency of the brainwave signal, I was curious about how well a relatively cheap (\~\$100) sensor would measure brain signals.

In this project, the analog brainwaves enter a processing ASIC chip and have digital values that are communicated over Bluetooth. I accessed only the digital data. It is certainly possible to look at the analog brain waves before they enter the processing ASIC, but it would be much more difficult, requiring a schematic and specialized oscilloscope probes.

The Mindwave Mobile was chosen because because it uses Bluetooth, making it easier to interface it with a microcontroller or other hardware. Please note that Neurosky has multiple models of the MindWave.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/1/3/9/d/52cda965ce395f260c8b4567.jpg)](https://cdn.sparkfun.com/assets/e/1/3/9/d/52cda965ce395f260c8b4567.jpg)

*SFE Creative Technologist, [Nick Poole](https://www.sparkfun.com/users/207060), sporting the MindWave. The electrode rests on the forehead, above the eyebrow, and the reference clips onto the ear.*

## Taking it Apart

Pictured here is the MindWave headset. Nick Poole took one of these apart, so the insides of the headset are pictured here as well.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/0/d/d/9/e/52cda965ce395f02198b4567.jpg)](https://cdn.sparkfun.com/assets/0/d/d/9/e/52cda965ce395f02198b4567.jpg)

Here is a closeup of the internal circuitry. You may recognize the MSP430 hanging out at the top.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/d/e/a/0/52cda967ce395f400c8b4568.jpg)](https://cdn.sparkfun.com/assets/e/d/e/a/0/52cda967ce395f400c8b4568.jpg)

And, the backside\....

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/1/d/c/3/4/52cda968ce395f0e558b4567.jpg)](https://cdn.sparkfun.com/assets/1/d/c/3/4/52cda968ce395f0e558b4567.jpg)

In between the two boards is an [ASIC](http://en.wikipedia.org/wiki/Application-specific_integrated_circuit). The ASIC on the Neurosky calculates a value for Attention and Meditation. It also processes five types of brainwaves (more on this shortly) and sends out unitless values for each one. This unit measures eyeblinks too.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/c/2/a/f/8/52cda964ce395f77648b456b.jpg)](https://cdn.sparkfun.com/assets/c/2/a/f/8/52cda964ce395f77648b456b.jpg)

## Gathering Materials

In order to interface with the MindWave, you\'ll need a few bits of hardware and software.

### Hardware

To interface with the MindWave, the [RN-42 Bluetooth](https://www.sparkfun.com/products/10253) module was chosen. For this project, I created a custom PCB, however, you could also use a [BlueSMiRF](https://www.sparkfun.com/products/12577) or a [Bluetooth Mate](https://www.sparkfun.com/products/12576). The Bluetooth module will be connected to an [Arduino Uno](https://www.sparkfun.com/products/11021) to read in the data being transmitted wirelessly.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/bluesmirf.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/bluesmirf.jpg)

*The [BlueSMiRF Silver](https://www.sparkfun.com/products/12577) module from SparkFun.*

Once you\'ve decided on which hardware you\'ll be using, connect everything. Again, the Bluetooth Basics and BlueSMiRF tutorials should cover how to do this extensively.

### Software

You'll want to get some programs to be able to read data from and configure the RN42 Bluetooth module.

- [X-CTU](http://www.digi.com/support/kbase/kbaseresultdetl?id=2125), [CoolTerm](http://freeware.the-meiers.org/), or another serial terminal program of your choice.
- [RS232 Port Logger](http://www.eltima.com/products/rs232-data-logger/)

If you are unfamiliar with serial terminal emulators, please check out our [tutorial](https://learn.sparkfun.com/tutorials/terminal-basics).

### Firmware

Here is the firmware for the Arduino side of this project. If you are following along, you\'ll want to upload this to whichever Arduino board you are using.

    language:c
    ///////////////////////////////////////////////////////////////
    // Arduino Bluetooth Interface with Mindwave
    // Sophi Kravitz edit 11-4
    // Shane Clements edit 11-5
    //////////////////////////////////////////////////////////////////////// 
    #include <SoftwareSerial.h>     // library for software serial
    SoftwareSerial mySerial(5, 6);  // RX, TX
    int LED = 8;                    // yellow one
    int LED1 = 7;                   //white one
    int BAUDRATE = 57600;

    // checksum variables
    byte payloadChecksum = 0;
    byte CalculatedChecksum;
    byte checksum = 0;              //data type byte stores an 8-bit unsigned number, from 0 to 255
    int payloadLength = 0;
    byte payloadData[64] = ;
    byte poorQuality = 0;
    byte attention = 0;
    byte meditation = 0;

    // system variables
    long lastReceivedPacket = 0;
    boolean bigPacket = false;
    boolean brainwave = false;
    void setup() 
    byte ReadOneByte() 

    unsigned int delta_wave = 0;
    unsigned int theta_wave = 0;
    unsigned int low_alpha_wave = 0;
    unsigned int high_alpha_wave = 0;
    unsigned int low_beta_wave = 0;
    unsigned int high_beta_wave = 0;
    unsigned int low_gamma_wave = 0;
    unsigned int mid_gamma_wave = 0;

    void read_waves(int i) 

    int read_3byte_int(int i) 

    void loop() 
          checksum = ReadOneByte();                     //Read checksum byte from stream
          payloadChecksum = 255 - payloadChecksum;      //Take one’s compliment of generated checksum
          if(checksum == payloadChecksum) 
         brainwave = false;
         for(int i = 0; i < payloadLength; i++)                                  // switch
            }                                   // for loop

            if(bigPacket) 
              else
             }

                if(brainwave && attention > 0 && attention < 100) 

              if(attention > 40)
              else
                digitalWrite(LED1, LOW);
            } 
            }
          }

Here is the Processing code, which interprets the data coming from the MindWave to the Arduino, and then gives you a visual representation of that data.

    language:java
    //Processing code to graph Attention values
    //Comment out all of the lines after “if(brainwave && attention > 0 && attention < 100) 

    void draw () 

     void serialEvent (Serial myPort)  
       else 
     }
     }

## Configuring the Bluetooth Module

The RN42 module can be configured to behave in a variety of different ways. If you have never configured one of the RN Bluetooth modules, please read our [BlueSMiRF Hookup Guide](https://learn.sparkfun.com/tutorials/using-the-bluesmirf).

You can use any serial terminal you wish to configure the bluetooth module. For this project, I used my Android phone with an app called [S2 Terminal for Bluetooth](https://play.google.com/store/apps/details?id=jp.side2.apps.btterm&hl=en) to configure the RN42. The configuration process went as so:

\*\*Note: \*\*If you are using the S2 Terminal program, you will need to type in ASCII and put a return after each command. Also, you only have 60 seconds after power up to enter the first command.

1.  To put the RN42 into COMMAND mode, type \$\$\$ (NO carriage return). If successful, you will see "CMD".

2.  Type: `D` + carriage return. You will see the current configuration of the RN42.

    ::: 
    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/phone1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/phone1.jpg)
    :::

3.  Type: `SP,0000` + carriage return. This will change the pincode from \'1234\' to \'0000\'. You will see "AOK" if this is done properly.

4.  Type: `SM, 3` + carriage return. This will configure the RN42 to Auto-Connect Mode. Once the module is powered up, it will immediately look to connect (pair).You will see "AOK" if this is done properly.

5.  Type: `SR,MAC ADDRESS` + carriage return. Insert the 12 digit address you copied from the MindWave Mobile. Look for AOK. If you don't see AOK, you'll have to retype the MAC address command.

6.  Now type: `SU,57.6` + carriage return. This will change the baud rate from 115200 to 57600.

    ::: 
    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/phone2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/phone2.jpg)
    :::

7.  Type `D` + carriage return. Double check that the stored address is the Mac address you entered in step 5 and that it\'s configured to Auto, not Slave.

8.  Type: `---` (three minus signs) + carriage return You should then see END.

    ::: 
    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/phone3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/phone3.jpg)
    :::

Turn the Mindwave on. The blue light flashes for a few moments, then it will pair with your hardware. You\'ll know that the Mindwave Mobile is paired because the blue light on the Mindwave Mobile is solid. If it is solid red, it is out of battery (AAA, lasts for about 8 hours).

## Deciphering the MindWave Data

Using an [FTDI basic](https://www.sparkfun.com/products/9873), I was able to view the data coming in from the Arudino through my USB port. I used X-CTU to read the data. The Arduino code mentioned in the Gathering Materials section is mostly a combination of the Mindwave Mobile example code and Shane Clements' massaging. The code is set up to print all of the digital data available out of the Mindwave Mobile. The data runs through the software serial port and is read easily on the X-CTU screen.

You can see unitless values for Delta, Theta, Alpha, Low Beta, High Beta and Gamma waves. The Mindwave's ASIC also presents a calculated value for both Attention and Meditation. A number between 20 and 100 for Attention is normal, and a value above 40 means you are concentrating.

I was able to get repeatable values with the Attention value by counting backwards from 100 to1. We had a Bring A Hack dinner in Boulder, CO, and a few other people were able to make the Attention value rise by counting backwards from 100 to 1 also.

What is interesting is that the 5 types of brainwaves measured and reported originate from different parts of the brain. They also have extremely low amplitudes and frequencies.

[![Brain-anatomy](//upload.wikimedia.org/wikipedia/commons/5/5b/Brain-anatomy.jpg)](http://commons.wikimedia.org/wiki/File%3ABrain-anatomy.jpg "By User:Primalchaos (Image:Human_brain_NIH.jpg) [Public domain], via Wikimedia Commons")

- [Gamma waves](http://en.wikipedia.org/wiki/Gamma_wave) are oscillating waves with frequencies around 40 Hz, although they can be as high as 100 Hz and as low as 24 Hz. These originate from the thalamus (buried deep in the center of the brain) and are responsible for states of high attention and concentration.
- [Beta waves](http://en.wikipedia.org/wiki/Beta_wave) are between 12 and 30 Hz and are the states associated with normal waking consciousness. These are emitted from the motor cortex, a region of the cerebral cortex, which is the outermost layer of tissue on the brain. Beta waves are split into three sections: Low Beta Waves (12.5-16 Hz, \"Beta 1 power\"); Beta Waves (16.5--20 Hz, \"Beta 2 power\"); and High Beta Waves (20.5-28 Hz, \"Beta 3 power\").
- [Alpha waves](http://en.wikipedia.org/wiki/Alpha_wave) originate at the Occipital lobe and have a frequency of 8-12Hz. These are most present when you are awake but are very drowsy or relaxed.
- [Theta waves](http://en.wikipedia.org/wiki/Theta_wave) are oscillating waves that are located in the Hippocampus and are associated with dreaming. They are in the 4-7Hz range.
- [Delta waves](http://en.wikipedia.org/wiki/Delta_wave) are associated with very deep, dreamless sleep cycles and are high amplitude waves, which have a 0 to 3Hz frequency. These waves emit from both the thalamus and the cortex.

The difference between these waves can be more easily understood when seen side-by-side.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/Brain-Waves-Graph.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/Brain-Waves-Graph.jpg)

If you used an Arduino with the code from the Gathering Materials section uploaded, you should be able to see these values printed out in X-CTU or the Serial terminal program of your choice.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/printout.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/printout.jpg)

The Processing code found in the same section as the Arduino code can be used and modified to graph different values from the Arduino.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/scrnsht.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/scrnsht.jpg)

*The attention value being graphed on Processing.*