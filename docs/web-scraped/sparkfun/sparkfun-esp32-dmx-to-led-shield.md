# Source: https://learn.sparkfun.com/tutorials/sparkfun-esp32-dmx-to-led-shield

## Introduction

The [SparkFun ESP32 DMX to LED Shield](https://www.sparkfun.com/products/15110) is the perfect way to send and receive [DMX](https://en.wikipedia.org/wiki/DMX512) data whether it be coming in over the onboard XLR-3 jack or ArtNet, or outputting over the XLR-3 Jack/ArtNet, this shield has you covered. It\'s the perfect way to get started developing your own custom DMX fixtures, or even adding ArtNet capabilities to a current fixture. It also holds up to the DMX standard which requires electrical isolation between the controller and communication side to avoid ground loops.

[![SparkFun ESP32 Thing Plus DMX to LED Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/7/7/15110-SparkFun_ESP32_Thing_Plus_DMX_to_LED_Shield-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing-plus-dmx-to-led-shield.html)

### [SparkFun ESP32 Thing Plus DMX to LED Shield](https://www.sparkfun.com/sparkfun-esp32-thing-plus-dmx-to-led-shield.html) 

[ DEV-15110 ]

The SparkFun ESP32 DMX to LED Shield is the perfect way to send and receive DMX data whether it\'s coming in or out over the o...

[ [\$18.50] ]

In this hookup guide we\'ll go over the several different ways that the DMX to LED Shield can be configured, go through simple DMX output and input, look at how to use ArtNet input to control arrays of LEDs and even servos using the available poke-home connectors and finally check out how to turn ArtNet input into DMX output to enable ArtNet control on an existing DMX fixture.

### Required Materials

**Note:** You might not need all of these items to get started on your specific DMX application, so head down to the [Examples](https://learn.sparkfun.com/tutorials/sparkfun-esp32-dmx-to-led-shield#examples) section to determine, which example best suits your needs and the products that are needed for the example.\
\
To do all the examples, users will need:

- +2 [DMX to LED Shields](https://www.sparkfun.com/products/15110) (Controller/Peripheral) with [ESP32 Thing Plus](https://www.sparkfun.com/products/14689) -OR- Separate DMX Controller/Peripheral
- [XLR-3 Cable](https://www.sparkfun.com/search/results?term=dmx)
- [Addressable LEDs](https://www.sparkfun.com/categories/286)
- [Pan Tilt servo kit](https://www.sparkfun.com/products/14391)
- [Headers](https://www.sparkfun.com/categories/381) and [Soldering Tools](https://www.sparkfun.com/categories/49)

[![Pan/Tilt Bracket Kit (Single Attachment)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/0/7/14391-01a.jpg)](https://www.sparkfun.com/pan-tilt-bracket-kit-single-attachment.html)

### [Pan/Tilt Bracket Kit (Single Attachment)](https://www.sparkfun.com/pan-tilt-bracket-kit-single-attachment.html) 

[ ROB-14391 ]

This is an easy-to-assemble pan/tilt bracket kit that utilizes servos to move on two axes fit for camera and helping-hand app...

[ [\$11.50] ]

[![SparkFun Thing Plus - ESP32 WROOM](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/9/4/14689-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/products/14689)

### [SparkFun Thing Plus - ESP32 WROOM](https://www.sparkfun.com/products/14689) 

[ WRL-14689 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

**Retired**

[![SparkFun LuMini LED Matrix - 8x8 (64 x APA102-2020)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/8/1/15047-SparkFun_LuMini_LED_Matrix_-_8x8__APA102-2020_-01.jpg)](https://www.sparkfun.com/sparkfun-lumini-led-matrix-8x8-64-x-apa102-2020.html)

### [SparkFun LuMini LED Matrix - 8x8 (64 x APA102-2020)](https://www.sparkfun.com/sparkfun-lumini-led-matrix-8x8-64-x-apa102-2020.html) 

[ COM-15047 ]

The 8x8 SparkFun LuMini LED Matrix, packed with 64 individually addressable LEDS, each capable of producing 16 million colors...

**Retired**

[![XLR-3 Cable - 10ft](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/2/15309-XLR-3__DMX__Cable_-_10ft-01.jpg)](https://www.sparkfun.com/products/15309)

### [XLR-3 Cable - 10ft](https://www.sparkfun.com/products/15309) 

[ CAB-15309 ]

This is a 10 foot long DMX cable capable of better communications for lighting and special effects through standard or digita...

**Retired**

#### Headers and Soldering Tools

The DMX to LED shield is designed with a Feather footprint. Make sure to choose the appropriate header combo to suit your microcontroller and project.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

[![Feather Stackable Header Set](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/0/4/15187-Feather_Stackable_Header_Kit-01.jpg)](https://www.sparkfun.com/feather-stackable-header-kit.html)

### [Feather Stackable Header Set](https://www.sparkfun.com/feather-stackable-header-kit.html) 

[ PRT-15187 ]

These stackable headers are made to work with the \[SparkFun ESP32 Thing Plus\](https://www.sparkfun.com/products/14689) to con...

[ [\$2.25] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

### Suggested Reading

We\'d recommend checking out the following tutorials and hookup guides before getting started if you\'re not familiar with the topics. At the very least check out the DMX related tutorials if you haven\'t used the protocol before.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/using-artnet-dmx-and-the-esp32-to-drive-pixels)

### Using Artnet DMX and the ESP32 to Drive Pixels 

In this tutorial, we\'ll find out how to use Resolume Arena, a popular video jockey software, to control custom-made ArtNet DMX fixtures.

[](https://learn.sparkfun.com/tutorials/introduction-to-dmx)

### Introduction to DMX 

DMX512 is an industry standard in lighting and stage design, whether it be controlling lights, motors, or lasers, DMX512 has many uses. In this tutorial we'll cover DMX512 (Digital Multiplex with 512 pieces of information).

[](https://learn.sparkfun.com/tutorials/lumini-ring-hookup-guide)

### LuMini Ring Hookup Guide 

The LuMini Rings (APA102-2020) are the highest resolution LED rings available.

[](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide)

### ESP32 Thing Plus Hookup Guide 

Hookup guide for the ESP32 Thing Plus (Micro-B) using the ESP32 WROOM\'s WiFi/Bluetooth system-on-chip in Arduino.

[](https://learn.sparkfun.com/tutorials/lumini-8x8-matrix-hookup-guide)

### LuMini 8x8 Matrix Hookup Guide 

The LuMini 8x8 Matrix (APA102-2020) are the highest resolution LED matrix available.

## Hardware Overview

### Power

You should always power the DMX shield with **5V** to provide proper power for RS485. The DMX to LED shield can be powered through either the screw terminals or the USB connection on your microcontroller that is plugged into the shield.

#### Power Screw Terminal

For applications with high current draw be sure to use the available screw terminals to provide power. If you are powering a large LED array or many servos, you may start seeing power dips due to your USB power supply\'s inability to give enough current. The screw terminal is a 2-pin **3.5 mm** screw terminal that should be able to accept **26-16 AWG** wire with a strip length of \~5-6 mm. The screws are M2 screws, so you will probably need a smaller jewelry size screw driver.

[![Annotated picture of power screw termial](https://cdn.sparkfun.com/r/350-350/assets/learn_tutorials/8/8/4/Power-Screw_Terminal.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/Power-Screw_Terminal.jpg)

*Screw Terminal for 5V power. Note the polarity markings.*

#### Logic Level Converter

Since many Feather boards are **3.3V logic**, there is a logic level converter between the microcontroller and LED data pins to bring the poke-home connectors up to **5V logic**.

[![Annotated picture of Logic Level Converter](https://cdn.sparkfun.com/r/350-350/assets/learn_tutorials/8/8/4/Logic_Level_Converter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/Logic_Level_Converter.jpg)

*Logic level converter*

#### Power and Data Isolation

As per DMX spec, microcontroller power should be electrically isolated from XLR communication. This has been accomplished with a DC-DC converter and optoisolators. The DC-DC converter has an isolation voltage of **1 kVDC** (rated to 1 min.) and isolation resistance of **1 GΩ**. The DC-DC converter outputs **200 mA** at **5V** and can take a surge voltage of 9 VDC (for 100 μs).

[![Annotated picture of Power Isolation](https://cdn.sparkfun.com/r/350-350/assets/learn_tutorials/8/8/4/Power_Isolation.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/Power_Isolation.jpg)

*Power isolation through DC-DC converter and data isolation through optocouplers.*

#### XLR Connectors

**Warning:** Be very careful **[NOT]** to plug into any sound boards as you will likely damage your DMX to LED Shield.

XLR cables are commonly used in the stage lighting and sound industry. Each [DMX to LED Shield](https://www.sparkfun.com/products/15110) has a 3-pin (aka XLR-3) male and female XLR connector. When using these, [be very careful **NOT** to plug into any audio equipment] as you will likely damage your DMX to LED Shield. To remove a cable, just press down on the button on the cable or connector and pull it out. Typically, the male XLR connector on the peripheral is the input while the female is the output.

[![Annotated picture of XLR connections](https://cdn.sparkfun.com/r/500-350/assets/learn_tutorials/8/8/4/XLR_Connectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/XLR_Connectors.jpg)

*Controller and peripheral XLR connections.*

**Note:** Three-pin XLR connection is essentially the same as five-pin connection, the primary difference between the two are in cost and that three-pin cable can be connected to a sound boards by mistake. Sound boards usually generate a much higher voltage; therefore, there is a potential to damage your DMX512 devices.

### Poke Home Connectors

The outputs for the poke home connectors are laid out to match up with [APA102 LED strips](https://www.sparkfun.com/search/results?term=apa102) and [LuMini devices](https://www.sparkfun.com/search/results?term=lumini).

[![Wiring between DMX shield and LuMini Matrix](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/Poke_Home_Layout.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/Poke_Home_Layout.gif)

*Pin match up between a [LuMini 8x8 Matrix](https://www.sparkfun.com/products/15047) and the DMX to LED Shield (\*products not to scale).*

Due to this, all of the clock lines have been connected to the same output on the ESP32 (or whatever microcontroller you happen to be using). The pins on the shield have been labeled with the corresponding poke home connectors in the image below, so you know which pins to connect to if you want to use them for other purposes.

[![Poke-Home Connections](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/DMX_Pin_Connections2_Updated.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/DMX_Pin_Connections2_Updated.gif)

*Poke-Home Connections. (Click to enlarge)*

Poke Home Pin Connections on DMX Shield

  ----------------------------------- -----------------------------------
         **ESP32 Thing Plus**                   **DMX Shield**

                  SCK                                 CO\
                                                      C1\
                                                      C2\

                 COPI                                 D0

                 CIPO                                 D1

                Pin 27                                D2
  ----------------------------------- -----------------------------------

**Note:** You may not recognize the COPI/CIPO labels for SPI pins. SparkFun has joined with other members of OSHWA in a resolution to move away from using \"Master\" and \"Slave\" to describe signals between the controller and the peripheral. Check out [this page](https://www.sparkfun.com/spi_signal_names) for more on our reasoning behind this change. You can also see OSHWA\'s resolution [here](https://www.oshwa.org/a-resolution-to-redefine-spi-signal-names).

    To use the poke-home connector, simply press down on the tab with a ballpoint pen (a key or screwdriver also works well) while pushing in the wire. The tabs to depress are highlighted in the image below, be aware that it'll take some extra finesse to get stranded core wire into these connectors. These connections should be able to accept **24-18 AWG** wire.

[![Poke Home](https://cdn.sparkfun.com/r/350-350/assets/learn_tutorials/8/8/4/poke-home.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/poke-home.png)

*Poke-Home Use*

### Termination Resistor Pad

A pad for a 120 Ω termination resistor is broken out on the shield. This is used to help increase the signal reflection, if the shield is at the end of a chain of DMX devices. If you don\'t have a 120 Ω resistor, a [100 Ω resistor](https://www.sparkfun.com/products/14493) can be used.

[![Termination Resistor](https://cdn.sparkfun.com/r/350-350/assets/learn_tutorials/8/8/4/Termination_Resistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/Termination_Resistor.jpg)

*Termination Resistor*

## Hardware Assembly

The DMX to LED shield is designed with a Feather footprint; we recommend using the [SparkFun ESP32 Thing Plus](https://www.sparkfun.com/products/14689) for it\'s WiFi capabilities. Make sure to choose the appropriate header combo to suit your needs when soldering headers into your microcontroller board. In the examples below, we will be using an [ESP32 Thing Plus](https://www.sparkfun.com/products/14689) with soldered [male headers](https://www.sparkfun.com/products/116). Check out the [assembly section](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide#assembly-tips) of the ESP32 Thing Plus Hookup Guide for tips on soldering the [ESP32 Thing Plus](https://www.sparkfun.com/products/14689).

[![ESP32 Thing with male headers soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/2/SparkFun_Transparent_Graphical_OLED_Breakout__Qwiic__Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/2/SparkFun_Transparent_Graphical_OLED_Breakout__Qwiic__Hookup_Guide-01.jpg)

*ESP32 Thing Plus with soldered male headers.*

This shield is easy to plug in and start playing around with. When creating a high current installation, make sure to power your system through the screw terminals. If you know the board will be at the end of a chain of DMX devices, solder in a 120 Ohm resistor in the **term** spot (highlighted below). If you don\'t have a 120 Ω reisitor, a [100 Ω resistor](https://www.sparkfun.com/products/14493) can be used.

[![Termination Resistor](https://cdn.sparkfun.com/r/350-350/assets/learn_tutorials/8/8/4/Termination_Resistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/Termination_Resistor.jpg)

*Termination Resistor*

## Software Overview

For some of these examples, we\'ll be using a software that will be new to most Arduino users, Resolume Arena 6, which is a popular video jockey software. If you plan on following along with some of the ArtNet examples, you\'ll need to download the demo [here](https://resolume.com/download/) in order to output some ArtNet data to your network. If you have another device generating ArtNet signals on your network, you can just stick with that.

[Resolume Arena 6](https://resolume.com/download/)

First, you\'ll need the **SparkFunDMX Arduino library**, **ArtnetWifi Arduino Library**, **ESP32Servo Arduino Library**, and **Resolume Arena 6** (click button above). You can obtain these libraries through the Arduino Library Manager by searching for them to install the latest version. If you prefer downloading the [library from the GitHub repository](https://github.com/sparkfun/SparkFunDMX) and manually installing it, you can grab them here:

[SparkFunDMX (ZIP)](https://github.com/sparkfun/SparkFunDMX/archive/master.zip) [ArtnetWifi (ZIP)](https://github.com/rstephan/ArtnetWifi/archive/master.zip) [ESP32Servo (ZIP)](https://github.com/jkb-git/ESP32Servo/archive/master.zip)

**Note:** This tutorial assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### SparkFunDMX Library Functions

Below is a list of the available SparkFunDMX library functions.

`.initRead(int maxChan)` - Enables XLR input.

Input: int *maxChan*

Integer for total number of channels being used.

`.initWrite(int maxChan)` - Enables XLR output.

Input: int *maxChan*

Integer for total number of channels being used.

`.read(int Channel)` - Reads data in buffer from *Channel*.

Input: int *Channel*

Specifies channel or device (1-512) that the code is looking at.

Output: uint8_t (Value between 0-255)

Unsigned 8-bit integer to do with what you please.

`.write(int Channel, uint8_t value)` - Writes data (*value*) in buffer for *Channel*.

Input: int *Channel*

Specifies channel (1-512) to write to.

uint8_t *value*\
Unsigned 8-bit integer to be written to channel.

`.update()` - Writes data buffer to Serial output if we are in write mode, reads data into buffer if we are in read mode.

## Examples

### Example 1 - Controller

#### Materials

- DMX Cable
- DMX Fixture/Additional DMX to LED Shield

To start, we\'ll output DMX over the XLR Jack to control a DMX capable peripheral device. We\'ll map out our channels so they control the peripheral device we\'ll create in the next example. For the sake of simplicity in this first example, we\'ll control the color of the entire 8x8 matrix as well as the values of each servo. Go ahead and open **File**-\>**Examples**-\>**SparkFun DMX**-.**Example1-DMXOutput**. Looking at the beginning of the example, we include the SparkFunDMX library and create a `SparkFunDMX` object called `dmx` We\'ll use channels 1, 2, and 3 for hue, saturaion and value, the 4th channel will contain pan, and the 5th will be tilt. These are defined in the preamble of the example to help keep track of which channels are where. If we are using two DMX to LED shields (one as output and one as input) we\'ll want the channel definitions sections to be identical on both output and input sides

    language:c
    #include <SparkFunDMX.h>

    SparkFunDMX dmx;

    //Channel Definitions
    #define TOTAL_CHANNELS 5

    #define HUE_CHANNEL 1
    #define SATURATION_CHANNEL 2
    #define VALUE_CHANNEL 3
    #define PAN_CHANNEL 4
    #define TILT_CHANNEL 5

In our `setup()` loop we begin our DMX shield in write mode by calling `dmx.initWrite(TOTAL_CHANNELS);`, which enables XLR output. We can then write to our buffer using `dmx.write(int channel, uint8_t value);` and then send that out over the XLR jack using `dmx.update();`. In our `void loop()` we use a `for` loop and several `if` statements to decide what to put in each channel, then send that data out. This is shown below.

    language:c
    void loop() 
        else if (channel == HUE_CHANNEL || channel == PAN_CHANNEL || channel == TILT_CHANNEL) //Sweep across our servos as well as a rainbow cycle.
        
      }
      Serial.print(x++);//Print and increment x. Since x is an unsigned 8 bit integer it will loop back to 0 if we try to increment it past 255
      dmx.update(); // update the DMX bus witht he values that we have written
      Serial.println(": updated!");
      delay(100);
    }

You can open the Serial Monitor to 115200 baud if you\'d like to see the current value being written to hue and the servos, but we won\'t truly be able to see the output until we connect to a peripheral device.

### Example 2 - Peripheral

#### Materials

- DMX Cable
- DMX Controller/additional DMX to LED Shield
- LED\'s (Optional)
- Pan/tilt Servo (Optional)

In this example, we\'ll be creating the world\'s most adorable [moving head light](https://www.amazon.com/MFL-Rotating-Activated-Master-slave-Nightclub/dp/B00YIKO4CI/ref=sr_1_2?qid=1553190586&refinements=p_n_feature_keywords_browse-bin%3A7103859011&s=musical-instruments&sr=1-2) using a [LuMini 8x8 Matrix](https://www.sparkfun.com/products/15047) and our [Pan/Tilt Servo Kit](https://www.sparkfun.com/products/14391), although you\'re totally allowed to use different servos with our [other servo mounting kit](https://www.sparkfun.com/products/10335) if you want some nicer servos. What we\'ll do is set our ESP32 to send our first 3 channels of DMX data to our LED matrix to color it, the 4th and 5th channels will be used to control the servos.

#### Optional Hardware Assembly

If you\'re deciding to create a tiny version of a moving head, assemble your pan and tilt servos as well as soldering some wire onto the LuMini Matrix if you haven\'t already. Attach your LED\'s to your moving head how you see fit, I\'ve used poster putty to attach mine for this simple demo. Go ahead and connect the data pin (orange on the Pan/Tilt Servo Kit) on your pan servo (left to right) to the **D1** poke-home connector and the tilt servo to the **D2** poke-home. Connect **D0** and **C0** to **DI** and **CI** on whatever APA102/LuMini LED\'s you\'ve decided to use. If you\'re using WS2812 type LED\'s, you\'ll only need to connect your **DATA** line to **D0**. My setup is shown below, with the LED lines on the left set of poke-home connectors and the servos on the two right sets.

[![Moving Head Wiring](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/4/DMX_to_LED_Shield_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/DMX_to_LED_Shield_Hookup_Guide-02.jpg)

*Moving Head Wiring*

#### Peripheral Code

If you haven\'t already, go ahead and open up **File**-\>**Examples**-\>**SparkFun DMX**-.**Example2-DMXInput**. On our peripheral side, we\'ll want to make sure that our channel definitions in our preamble match those in our output example, as we\'ll need to know how many channels we\'ll be receiving and what to do with each part of the data. We\'ll then need to declare our hardware for our custom DMX fixture, in this case two servos and a matrix of LED\'s. All of the definitions are shown below.

    language:c
    //Channel Defintions
    #define TOTAL_CHANNELS 5

    #define HUE_CHANNEL 1
    #define SATURATION_CHANNEL 2
    #define VALUE_CHANNEL 3
    #define PAN_CHANNEL 4
    #define TILT_CHANNEL 5

    //Fixture Hardware Definitinos
    #define NUM_LEDS 64
    CRGB matrix[NUM_LEDS];
    Servo pan;
    Servo tilt;

In our `setup()` loop we initialize our LEDs and servos as well as put our shield in read mode by calling `dmx.initRead(totalChannels);`.

    language:c
    void setup()
    

We can then call `dmx.update();` to update our data buffer, which we can then access by calling `dmx.read(int channel);`. We use this process to read our data from the corresponding channels into the proper hardware peripherals in the `void loop()`.

    language:c
    void loop()
    
      pan.write(map(dmx.read(PAN_CHANNEL), 0, 255, 0, 160));
      tilt.write(map(dmx.read(TILT_CHANNEL), 0, 255, 0, 160));
      FastLED.show();
    }

Loading example 1 up to one shield and example 2 up to another and connecting them via XLR should yield an output similar to the below GIF.

[![Moving Head](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/DMX_Demo_01.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/DMX_Demo_01.gif)

*Moving Head*

### Example 3 - ArtNet Input

#### Materials

- LED\'s (Optional)
- Pan/tilt Servo (Optional)

#### Arduino Code

This example is quite similar to the previous peripheral example, except this time we will be receiving ArtNet data over WiFi from Resolume Arena 6, a popular video jockey software. Let\'s begin by setting up our ArtNet Input, we\'ll be taking our hardware setup from the previous example and leveraging it here, so all of the definitions for the hardware peripherals will remain the same. However, in this example, we\'ll be controlling each LED on our matrix individually, so we\'ll use 192 (64 LED\'s multiplied by 3 channels per LED) channels for LED\'s instead of 3. This makes our Channel definition section look like the below.

    language:c
    //Channel and Peripheral Definitions
    #define NUM_LEDS 64
    #define NUM_LED_CHANNELS NUM_LEDS * 3 //Ends up being 192 channels for our 8x8 LED matrix
    #define PAN_CHANNEL 193
    #define TILT_CHANNEL 194
    CRGB matrix[NUM_LEDS];
    Servo pan;
    Servo tilt;

We then need to begin WiFi and ArtNet. The example defaults to using the ESP32 as a standalone access point but you can change lines 23, 24, 54, 55 and 57 if you\'d like to connect to an existing network. If not however, the standalone access point will have an SSID of **myDMX** and the password will be `artnetnode`. We then initialize our `artnet` object (which we created in the preamble with `ArtnetWifi artnet;`) with `artnet.begin();` which will begin scouring the network for Artnet packets. We then use `artnet.setArtDMXCallback(onDmxFrame);` so that `onDmxFrame` is called each time we see an Artnet packet on the network. `onDmxframe` is the function that we will be changing based on our setup to parse data into the proper hardware attachments. We loop through all of our channels and place them into the proper segments using if statements. This code is outlined below.

    language:c
    void onDmxFrame(uint16_t universe, uint16_t length, uint8_t sequence, uint8_t* data)
    
        else if (channel == PAN_CHANNEL - 1) //Subtract 1 due to the fact that we index at 0 and ignore the startcode
        
        else if (channel == TILT_CHANNEL - 1)
        
      }
      previousDataLength = length;
      if (universe == endUniverse) //Display our data if we have received all of our universes, prevents incomplete frames when more universes are concerned.
      
    }

#### Resolume Setup

If you haven\'t yet, go check out the [ArtNet DMX and ESP32 Pixel Pushing Guide](https://learn.sparkfun.com/tutorials/using-artnet-dmx-and-the-esp32-to-drive-pixels/all#resolume-setup) for some help setting up custom fixtures in Resolume. You\'ll need to create two fixtures, one for your 8x8 display, and a single channel fixture to control pan and tilt. Then, create a Lumiverse with your 8x8 matrix in the center and the two fixtures; one for pan and one for tilt in each corner. Also ensure that you change TargetIP to **IPAddress** and change the address to `192.168.4.1` to send data directly to your ESP32.

[![Advanced Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/4/advancedoutput.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/advancedoutput.PNG)

*Advanced Output*

We\'ll then downsize our main video source so it isn\'t taking up the corners of the display and affecting the inputs for the pan and tilt channels. We\'ll then add two solid color blocks in the corners so we can affect the pan and tilt channels of our fixture. This is a very hacky way to do things, but Resolume is meant for video screens and not full fledged fixtures. We will then modulate the brightness of our solid color blocks in order to send data to the corresponding DMX channels. You can set all this up yourself, or download the composition below.

[DOWNLOAD RESOLUME COMPOSITION](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/Example4Composition.avc)

Connecting to the same network as the ESP32 will send data to your screens and servos. Check out the below gif to see what should be going on if you\'ve set everything up correctly.

[![ArtNet to Moving Head](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/DMX_Demo_02.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/DMX_Demo_02.gif)

*Artnet to Moving Head*

### Example 4 - ArtNet to XLR

#### Materials

- DMX Cable
- DMX Fixture

This final example will combine everything we\'ve learned so far to control a non ArtNet capable peripheral over ArtNet. Our Controller board will be turning Artnet data into DMX output. Our main change here will be that we change our `onDmxFrame` function to write our incoming Artnet data to our XLR buffer. This is accomplished with a simple for loop, shown below.

    language:c
    void onDmxFrame(uint16_t universe, uint16_t length, uint8_t sequence, uint8_t* data)
    
      previousDataLength = length;
      if (universe == endUniverse) //Display our data if we have received all of our universes, prevents incomplete frames when more universes are concerned.
      
    }

I have a non Artnet capable fixture laying around; an old Casa laser. I did some digging round on the internet to find this [slot map.](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/ctl-dcm.pdf) I then mapped out channels in Resolume to match up with the 7 channels available on the laser. To do this, I simply created three separate solid colors and placed an LED on each one. This makes my red value on my first led channel one, green channel 2, and so on. The second LED is channels 4-6 and sits on the second color. This is shown in the below image.

[![Advanced Output for Laser](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/4/advanced_output2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/advanced_output2.PNG)

*Advanced Output for Laser*

With all of these and my fixture map, I am able to send the data I want over to the laser over WiFi. The below clip consists of simply moving some channels around at random and watching the output.

[![Artnet Laser Control](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/DMX_Demo_03.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/4/DMX_Demo_03.gif)

*Artnet Laser Control*