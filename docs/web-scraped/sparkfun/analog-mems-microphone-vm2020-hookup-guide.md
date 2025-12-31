# Source: https://learn.sparkfun.com/tutorials/analog-mems-microphone-vm2020-hookup-guide

## Introduction

**Note:** This tutorial covers the SparkFun Analog MEMS Microphone - VM2020 ([BOB-21537](https://www.sparkfun.com/products/21537)). While this tutorial was based on the previous MEMS microphone tutorials, this version of the MEMS microphone is a differential microphone and was designed for noisy environments. For specific details regarding the microphone ICs, refer to the Documents tab on their product pages or the previous release of this Hookup Guide:\

[ADMP401 & ICS-40180 MEMS Microphone Hookup Guide](https://learn.sparkfun.com/tutorials/mems-microphone-hookup-guide)

The [SparkFun Analog MEMS Microphone Breakout](https://www.sparkfun.com/products/21537) makes it easy to work with the Vesper VM2020 analog microphone. The VM2020 is an ultra-high Acoustic Overload Point (AOP), high dynamic range, differential analog output piezoelectric MEMS microphone. What separates this from other analog MEMS microphones is that it was designed to be used in loud environments.

[![SparkFun Analog MEMS Microphone Breakout - VM2020](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/3/6/7/21537-_BOB-_01.jpg)](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-vm2020.html)

### [SparkFun Analog MEMS Microphone Breakout - VM2020](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-vm2020.html) 

[ BOB-21537 ]

The SparkFun Analog MEMS Microphone Breakout makes it easy to work with the Vesper VM2020 analog microphone.

**Retired**

[![](https://embed-ssl.wistia.com/deliveries/456a2a560c5434c311cbedbe3f2ee45be87768c7.jpg?image_play_button_size=2x&image_crop_resized=960x540&image_play_button=1&image_play_button_color=54bbffe0)](https://vespermems.com/products/vm2020/?wvideo=2mxkgzjpme)

*[VM2020 Compared to Capacitive MEMS Microphone in the Back Cavity of a Smart Speaker. Video courtesy of Vesper Technologies.](https://vespermems.com/products/vm2020/?wvideo=2mxkgzjpme)*

Read this guide to get an overview of the breakout board and how to use it, including its technical specifications, how to hook it up to a microcontroller, and example code to get started!

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Arduino Microcontroller

You\'ll want a microcontroller to power the microphone. We will be using the ESP32 WROOM.

[![SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/9/6/8/20168Diagonal.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html)

### [SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html) 

[ WRL-20168 ]

The USB-C variant of ESP32 Thing Plus is a development board with WiFi, SPP, BLE, Qwiic connector, 21 I/O pins, RGB status LE...

[ [\$33.73] ]

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

### Amplifier and Differential ADC Converter

Since the analog pins on an Arduino microcontroller are usually single-ended, you will need a way to amplify the signal to a reasonable level. You will also need an differential ADC converter. We recommend using the audio codec breakout WM8960. The audio codec can amplify the signal to a reasonable level and already has input pins for a differential microphone.

[![SparkFun Audio Codec Breakout - WM8960 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/0/1/0/21250-_BOB_SparkFun_Audio_Codec_Breakout-_01.jpg)](https://www.sparkfun.com/sparkfun-audio-codec-breakout-wm8960.html)

### [SparkFun Audio Codec Breakout - WM8960 (Qwiic)](https://www.sparkfun.com/sparkfun-audio-codec-breakout-wm8960.html) 

[ BOB-21250 ]

The SparkFun WM8960 Audio Codec Breakout is a low-power, high-quality stereo codec with 1W Stereo Class D speaker drivers and...

**Retired**

### Tools

Building a circuit using this breakout requires some assembly and soldering. You may already have a few of these items but if not, the tools and hardware below help with that assembly.

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

#### Prototyping Accessories

Depending on your setup, you may want to use IC hooks for a temporary connection. However, you will want to solder header pins to connect devices to the plated through holes for a secure connection. Depending on your application, you could use straight headers or right angle headers. Of course, you could also solder wire as well.

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![IC Hook with Pigtail](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/9/6/09741-01.jpg)](https://www.sparkfun.com/ic-hook-with-pigtail.html)

### [IC Hook with Pigtail](https://www.sparkfun.com/ic-hook-with-pigtail.html) 

[ CAB-09741 ]

These are good quality IC test hooks with a male connection wire. Instead of a single hook, these have two hooks that are cap...

[ [\$5.75] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

### Recommended Reading

To successfully use the SparkFun MEMS microphone breakout board, you\'ll need to be familiar with Arduino microcontrollers, analog (aka ADC) input, and sound waves. For folks new to these topics, check out the following resources to get a feel for the concepts and verbiage used throughout this tutorial.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide)

### IoT RedBoard ESP32 Development Board Hookup Guide 

Delve into the functionality-rich world of the IoT RedBoard ESP32 Development Board!

[](https://learn.sparkfun.com/tutorials/audio-codec-breakout---wm8960-hookup-guide)

### Audio Codec Breakout - WM8960 Hookup Guide 

The SparkFun Audio Codec Breakout - WM8960 is a low power, high quality stereo codec chock full of features. In this tutorial, some of these features by using an Arduino microcontroller to configure the audio codec and pass audio to the headphone or speaker channels.

## Hardware Overview

**Note:** The footprint for the VM2020 is different compared to previous versions of the Analog MEMS Microphone. Besides just being a differential MEMS microphone, the location of the header pins are slightly different.

The SparkFun Analog MEMS microphone breakout board breaks out the microphone for sound detection in loud environments. Each version breaks out the VM2020 on the top side of the board.

[![top view of Analog MEMS Microphone - VM2020](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Top_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Top_View.jpg)

The board receives audio input from the bottom of the board. For users soldering straight headers, you may want to consider soldering them from the back.

[![bottom view of Analog MEMS Microphone - VM2020](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Bottom_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Bottom_View.jpg)

- **OUT−** - Audio signal output for differential −output.
- **OUT+** - Audio signal output for differential +output.
- **VCC** - Voltage input (**1.6V to 3.6V**). To power this lil\' mic, use a DC voltage with a supply current of about 248μA for VM2020. We\'ll be using **3.3V** from an Arduino.
- **GND** - Ground.

For technically-minded folks, here are some of the features of the VM2020 and a comparison with other SparkFun MEMS Microphone Breakout boards. Make sure to check out VM2020 datasheet in the [Resources & Going Further](https://learn.sparkfun.com/tutorials/analog-mems-microphone-vm2020-hookup-guide#resources-and-going-further) for a complete overview of the microphone.

  Electrical Characteristics             ICS-10480         SPH8878LR5H-1     VM2020
  -------------------------------------- ----------------- ----------------- -----------------
  High Signal-to-Noise Ratio (\"SNR\")   65dbA             67dBA             50dbA
  Sensitivity                            about -38dBV      about -44dBV      about -63dBV
  Flat Frequency Response                60Hz to 20kHz     7Hz to 36kHz      80Hz to 10kHz
  Low Current Consumption                \<260 μA @ 3.3V   \<265 µA @ 3.6V   \<248 μA @ 3.6V
  Acoustic Overload Point (AOP)          124 dB            134 dB            152 dB

Note that the acoustic overload point of the VM2020 is greater than the other MEMS microphones. The audio is less likely to be clipped in louder settings (such as concerts, dance studios, etc.) or when the microphone is placed beside a speaker. Below is a table of typical sounds, their approximate decibel levels, and the AOP of the three microphones listed earlier. The information was gathered from a variety of sources online. Keep in mind noise-induced hearing loss varies depending on the sound intensity, the amount of exposure time, and how close your ears are to the sound source.

  Sound Source          Approximate Decibel Level \[dB\]   Sound Intensity                                      Microphone Type
  --------------------- ---------------------------------- ---------------------------------------------------- ----------------------------
  Rocket Launch         180                                Death of Hearing Tissue                              
  Shotgun Blast         165                                                                                     
  Firecrackers          150                                                                                     Reaching VM2020 AOP
  Jet Engine            140                                Harmful                                              
  Jackhammer            130                                                                                     Reaching SPH8878LR5H-1 AOP
  Car Siren             120                                                                                     Reaching ICS-10480 AOP
  Rock Concert          115                                                                                     
  Lawn Mower            90                                 Risk of hearing loss when sustained levels of 90dB   
  Loud City Traffic     85                                 Sounds above 85dB are harmful                        
  Normal Conversation   60                                                                                      
  Quiet                 0                                  Normal Hearing Threshold                             

### Board Dimensions

The board dimensions for the breakout are 0.40\" x 0.55\" (10.16mm x 13.97mm). The location of the header pins are different compared to previous versions with the extra pin for the differential output.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/7/1/b/3/d/SparkFun_Analog_MEMS_Microphone_Breakout_VM2020_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/7/1/b/3/d/SparkFun_Analog_MEMS_Microphone_Breakout_VM2020_Board_Dimensions.png)

## Hardware Hookup

Now that we\'re familiar with the microphone breakout, let\'s connect it to a microcontroller and monitor some sound!

### Microphone Breakout Connections

For a permanent connection, we recommend [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) four [wires](https://learn.sparkfun.com/tutorials/working-with-wire) (or headers) to the PTHs on the breakout. We opted for soldering header pins and using jumper wires. Of course, you could also solder wires to the breakout board as well. For a temporary connection during prototyping, you can use IC hooks like [these](https://www.sparkfun.com/products/9741).

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

February 8, 2013

How to strip, crimp, and work with wire.

We recommend soldering right angle headers. Right angle headers will provide a low height profile. This is more versatile as users can angle the microphone or add M/F jumper wires between the board and breadboard. The microphone will also sit up and away from the board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Soldered_Right_Angle_Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Soldered_Right_Angle_Headers.jpg)

**Note:** You can use any connection as explained above to connect. If you decide to solder straight header pins, we recommend inserting the straight header pin\'s tail from the top of the board so that the audio input for the microphone is facing away from a surface. This can also be a low profile as the board is flush with the breadboard.\
\

[![Straight header pins being soldered to MEMS microphone.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Soldered_Straight_Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Soldered_Straight_Headers.jpg)\
\
*Straight header pins being soldered to MEMS microphone.*

\
\
However, depending on your application, you can also solder wires to the board. We recommend using the following colors of wire to easily distinguish the signals but you can always select a different color if you prefer (or do not have the colors used available).\
\

[![Right angle header pins being soldered to MEMS microphone.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Soldered_Wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/1/3/21537-Analog_MEMS_Microphone_Breakout-VM2020_Soldered_Wires.jpg)\
\
*Right angle header pins being soldered to MEMS microphone.*

\

- [**Green**] (or some other color not Red or Black) for Output−
- [**Blue**] (or some other color not Red or Black) for Output+
- [**Red**] for VCC
- [**Black**] for GND

### Connecting to a Microcontroller and Audio Codec WM8960

Next up we\'ll connect the breakout to an audio codec to amplify and read the signal. Then we will connect the boards to a microcontroller to monitor the audio signal output. For this tutorial, we used the MEMS microphone with the audio codec WM8960 and SparkFun IoT RedBoard - ESP32. The ESP32 module has I^2^S support and is recommended in this setup with the WM8960. Make the following connections between the breakout and IoT RedBoard - ESP32 (or whichever ESP32 variant that you choose).

**Note:**If you decide to use a variant of the ESP32 like the Thing Plus, you can adjust the I^2^S connections by using a different GPIO. Make sure to adjust the pin definitions in the example code if you decide to use a different ESP32 module.

  ----------------------------------------------------------------------------------------------------
  IoT RedBoard - ESP32 (or Arduino)   MEMS Microphone   WM8960                     TRS Connector
  ----------------------------------- ----------------- -------------------------- -------------------
  5V                                                    VIN                        

  Qwiic Cable\'s SCL pin\                               Qwiic Cable\'s SCL pin\    
  (or SCL)                                              (or SCL)                   

  Qwiic Cable\'s SDA pin\                               Qwiic Cable\'s SDA pin\    
  (or SDA)                                              (or SDA)                   

  Qwiic Cable\'s 3.3V pin\                              Qwiic Cable\'s 3.3V pin\   
  (or 3.3V)                                             (or 3.3V)                  

  Qwiic Cable\'s GND pin\                               Qwiic Cable\'s GND pin\    
  (or GND)                                              (or GND)                   

                                      Output −          LIN1                       

                                      Output +          LIN2                       

                                      GND               GND                        

                                      VCC               AVDD\                      
                                                        (i.e. 3.3V)                

  25                                                    ALRC                       

  17                                                    ADAT                       

  16                                                    BCLK                       

                                                        HPL                        TIP

                                                        OUT3                       GND (i.e. Sleeve)

                                                        HPR                        RNG (i.e. Ring)
  ----------------------------------------------------------------------------------------------------

The completed circuit should look something like the photo below:

[![Fritzing Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/1/3/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_I2S_VM2020_Differential_Mic_bb2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/1/3/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_I2S_VM2020_Differential_Mic_bb2.jpg)

## Software Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Arduino Board Definitions and Driver

We\'ll assume that you installed the necessary board files and drivers for your development board. In this case, we used the IoT RedBoard - ESP32 which uses the CH340 USB-to-serial converter. If you are using a Processor Board, make sure to check out its hookup guide for your Processor Board.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

September 9, 2020

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide)

### IoT RedBoard ESP32 Development Board Hookup Guide 

August 18, 2022

Delve into the functionality-rich world of the IoT RedBoard ESP32 Development Board!

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

### Installing the Arduino Library

We\'ll be using the WM8960 audio codec and connecting to the differential microphone input pins. The SparkFun Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun Audio Codec Breakout WM8960**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library) to manually install.

[SparkFun WM8960 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/archive/refs/heads/main.zip)

## Arduino Example

**Note:** We used espressif\'s **v2.0.6** board package for the SparkFun IoT RedBoard - ESP32. Previous versions of the board package seem to save the channels differently in the buffer. When reading the WM8960\'s I^2^S left microphone channel with v2.0.5 and this example, the Serial Plotter would only display the \"right channel.\"

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **Example_15_VolumePlotter_MEMS_Mic_Differential**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Plotter and set it to **115200** baud to view the output. Make some noise by saying \"Woooo!,\" clapping, or rubbing your fingers on the microphone. You should see an output showing the left input microphone\'s audio signal!

[![Arduino Serial Plotter Output from the Left Microphone Channel Input](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/1/3/Arduino_Serial_Output_VM2020_Audio_Codec_WM8960_Left_Mic_Channel_Input_ESP32_I2S.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/1/3/Arduino_Serial_Output_VM2020_Audio_Codec_WM8960_Left_Mic_Channel_Input_ESP32_I2S.JPG)

Try placing the microphone next to a loud amplified speaker and adjusting the PGA as necessary for your application. Or add a second MEMS microphone to the right channel and adjusting code to include the right channel.

**Note:** To adjust the code to include the right channel as well, you will need to adjust the mean for both the left and right channels in the `if (result == ESP_OK)` statement. You will then need to calculate and plot the values as comma separated values (CSV) for the Arduino Serial Plotter to display properly. Below is how the adjusted code should look like.\
\

``` c
  if (result == ESP_OK)
  
      
      // Only looking at right signal samples in the buffer (e.g. 1,2,5,7,9...)
      // Notice in our for loop here, we are incrementing the index by 2.
      for (int16_t i = 1; i < samples_read; i += 2) 

      // Average the data reading
      // Calculate left input for this example. So we must divide by
      // "half of samples read" (because it is stereo I2S audio data)
      meanLeft /= (samples_read / 2); 
      
      // Calculate right input for this example. So we must divide by
      // "half of samples read" (because it is stereo I2S audio data)
      meanRight /= (samples_read / 2);

      // Print to serial plotter
      Serial.print(meanLeft);
      Serial.print(",");
      Serial.println(meanRight);
    }
```

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
If you don\'t find what you need there, our [SparkFun Forums](https://forum.sparkfun.com/viewforum.php?f=143) are a great place to find and ask for help.\
\

[SparkFun Forums](https://forum.sparkfun.com/)