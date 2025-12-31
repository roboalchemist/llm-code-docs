# Source: https://learn.sparkfun.com/tutorials/ir-control-kit-hookup-guide

## Introduction

[Infrared](https://learn.sparkfun.com/tutorials/ir-communication) (IR) is a cheap and (as you\'ll soon discover) easy way to add wireless control to your project. The [IR Control Kit](https://www.sparkfun.com/products/13235) gives you everything you need to take control of the extravisible light waves (or are they particles?), so you can remotely control your custom [music box](https://learn.sparkfun.com/tutorials/mp3-player-shield-music-box) or build a controller for your TV or stereo.

[![IR Remote interfacing with Arduino](https://cdn.sparkfun.com/r/600-600/assets/d/7/8/0/e/524c4670757b7fa6768b4569.png)](https://www.sparkfun.com/products/11761)

In this tutorial we\'ll show you how to hook up all of the components included with the IR Control Kit, which includes:

[![IR Control Kit contents](https://cdn.sparkfun.com/assets/5/2/5/4/e/524c5cf4757b7fe9068b4568.png)](https://cdn.sparkfun.com/assets/5/2/5/4/e/524c5cf4757b7fe9068b4568.png)

- SparkFun\'s custom-made [Infrared Remote Control](https://www.sparkfun.com/products/11759)
- A [CR2025 Coin Cell Battery](https://www.sparkfun.com/products/11928) for the remote.
- Two 38kHz demodulating [Infrared Receiver Modules](https://www.sparkfun.com/products/10266)
- Two 950nm-emitting [Infrared LEDs](https://www.sparkfun.com/products/9349)
- A handful of [330Ω resistors](https://www.sparkfun.com/products/14490). You can never have enough current-limiting resistors.

### Required Materials

In this tutorial, we\'ll be using an Arduino to both transmit and interpret received IR data. On top of the components included with the IR Control Kit, you\'ll also need these to follow along with this tutorial:

- An [Arduino](https://www.sparkfun.com/products/13975) (or Arduino-compatible board) and a means to program it.
- A [breadboard](https://www.sparkfun.com/categories/149) is optional but recommended to help with the hardware hookup.
- As with the breadboard, [jumper wires](https://www.sparkfun.com/products/11026) are optional but the recommended tool to wire between breadboard and Arduino.
- The second of the examples uses a [common cathode RGB LED](https://www.sparkfun.com/products/9264) to create a fun, IR-controlled RGB LED project. This is optional.
- The third example uses a simple [momentary push-button](https://www.sparkfun.com/products/97) to trigger an IR code transmission. Optional again.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![LED - RGB Diffused Common Cathode](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/5/9/09264-LED_-_RGB_Diffused_Common_Cathode-01.jpg)](https://www.sparkfun.com/led-rgb-diffused-common-cathode.html)

### [LED - RGB Diffused Common Cathode](https://www.sparkfun.com/led-rgb-diffused-common-cathode.html) 

[ COM-09264 ]

Ever hear of a thing called RGB? Red, Green, Blue? How about an RGB LED? These 5mm units have four pins - Cathode is the long...

[ [\$2.30] ]

[![SparkFun USB Mini-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/6/9/8/0/11301-01.jpg)](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html)

### [SparkFun USB Mini-B Cable - 6 Foot](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html) 

[ CAB-11301 ]

This is a USB 2.0 type A to Mini-B 5-pin cable. You know, the mini-B connector that usually comes with USB Hubs, Cameras, MP3...

[ [\$5.50] ]

[![Mini Pushbutton Switch](https://cdn.sparkfun.com/r/140-140/assets/parts/9/0/00097-03-L.jpg)](https://www.sparkfun.com/mini-pushbutton-switch.html)

### [Mini Pushbutton Switch](https://www.sparkfun.com/mini-pushbutton-switch.html) 

[ COM-00097 ]

We use these little buttons on everything! These Miniature Single Pole Single Throw switches have a good click to them and ar...

[ [\$0.50] ]

[![Breadboard - Mini Modular (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/2/6/12043-01.jpg)](https://www.sparkfun.com/breadboard-mini-modular-white.html)

### [Breadboard - Mini Modular (White)](https://www.sparkfun.com/breadboard-mini-modular-white.html) 

[ PRT-12043 ]

This white Mini Breadboard is a great way to prototype your small projects! With 170 tie points there\'s just enough room to b...

[ [\$5.25] ]

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/light)

### Light 

Light is a useful tool for the electrical engineer. Understanding how light relates to electronics is a fundamental skill for many projects.

[](https://learn.sparkfun.com/tutorials/ir-communication)

### IR Communication 

This tutorial explains how common infrared (IR) communication works, as well as shows you how to set up a simple IR transmitter and receiver with an Arduino.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

## Hardware Overview

Before we dig into wiring stuff up and uploading sketches, let\'s quickly overview each of the components in the IR Control Kit.

### IR LED

Let\'s start with simplest of the components first \-- the [infrared LED](https://www.sparkfun.com/products/9349). Anyone who\'s ever worked with electronics has blinked an [LED](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds), but those blinking LEDs are usually in our visual spectrum. These IR LEDs are just like any LED you\'ve blinked before, but they emit light at a wavelength of about **950nm** \-- radiation well outside of our visual range (about 390 to 700nm).

[![LED - Infrared 950nm](https://cdn.sparkfun.com/r/600-600/assets/parts/2/9/1/3/09349-1.jpg)](https://www.sparkfun.com/led-infrared-950nm.html)

### [LED - Infrared 950nm](https://www.sparkfun.com/led-infrared-950nm.html) 

[ COM-09349 ]

This is a very simple, clear infrared LED. These devices operate between 940-950nm and work well for generic IR systems inclu...

[ [\$1.50] ]

You can\'t see these LEDs light up, but you can still use them just like any LED. They still have two [polarized](https://learn.sparkfun.com/tutorials/polarity) legs: an anode (positive, the long leg) and a cathode. They have a typical forward voltage of about **1.5V**, and a maximum forward current of 50mA. For more specs, you can check out the LED\'s [datasheet](http://cdn.sparkfun.com/datasheets/Components/LED/YSL-R531FR1C-F1.pdf).

#### 330Ω Current Limiting Resistor

Just as with any LED, the IR LED needs a series resistor to limit current. That\'s what the included [330Ω](https://www.sparkfun.com/products/8377) resistors are for.

[![Resistor 330 Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/2/1/7/14490-03.jpg)](https://www.sparkfun.com/resistor-330-ohm-1-4-watt-pth-20-pack-thick-leads.html)

### [Resistor 330 Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://www.sparkfun.com/resistor-330-ohm-1-4-watt-pth-20-pack-thick-leads.html) 

[ PRT-14490 ]

These are your run-of-the-mill 1/4 Watt, +/- 5% tolerance PTH resistors. Commonly used in breadboards and other prototyping a...

[ [\$1.25] ]

With a 5V supply connected to the resistor/LED series combo, current through the LED should be limited to about 10mA, which is well inside its safe operating range.

### TSOP38238 IR Receiver Module

While it may look like a simple transistor, the [TSOP38238 IR receiver module](https://www.sparkfun.com/products/10266) is actually a unique, light-demodulating [integrated circuit](https://learn.sparkfun.com/tutorials/integrated-circuits).

[![IR Receiver Diode - TSOP38238](https://cdn.sparkfun.com/r/600-600/assets/parts/4/6/2/8/10266-01.jpg)](https://www.sparkfun.com/ir-receiver-diode-tsop38238.html)

### [IR Receiver Diode - TSOP38238](https://www.sparkfun.com/ir-receiver-diode-tsop38238.html) 

[ SEN-10266 ]

Use this simple IR receiver for infrared remote control of your next project. With low power consumption and an easy to use p...

[ [\$2.25] ]

With three pins, it\'s about as simple as an IC can get. There are two pins for power \-- ground in the middle, and V~S~ to a side \-- and one, single data output pin.

[![IR receiver pinout](https://cdn.sparkfun.com/assets/6/a/f/b/f/524b36e8757b7f3d6c8b4567.png)](https://cdn.sparkfun.com/assets/6/a/f/b/f/524b36e8757b7f3d6c8b4567.png)

The IR receiver can be powered at anywhere from **2.5V to 5.5V**, so it plays very nicely with a variety of development boards.

This module is tuned to **demodulate 38kHz signals**, which are a very common in the IR signal world. It turns a spiky, modulated signal (as shown on the image on the left) into this cleaner much easier to read signal (as shown in the image on the right):

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![modulated input signal](https://cdn.sparkfun.com/r/600-600/assets/2/3/0/5/0/524b38c3757b7fbf6c8b4567.png "modulated input signal")](https://cdn.sparkfun.com/assets/2/3/0/5/0/524b38c3757b7fbf6c8b4567.png)   [![demodulated output signal](https://cdn.sparkfun.com/r/600-600/assets/d/d/6/b/5/524b38c3757b7fd26c8b4567.png "demodulated output signal")](https://cdn.sparkfun.com/assets/d/d/6/b/5/524b38c3757b7fd26c8b4567.png)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

So all we have to do to read the output of this device is count high and low pulses, and measure their durations. For more information on the TSOP38238, check out its [datasheet](https://www.sparkfun.com/datasheets/Sensors/Infrared/tsop382.pdf).

### IR Remote

**Note:** You will need to press the button multiple times in order to send more than one button press to the IR receiver. If you hold the button down, the example code may read 0xFFFFFFFF.

Finally, we come to the flashy part of the kit: SparkFun\'s custom-made [Infrared Remote Control](https://www.sparkfun.com/products/11759).

[![Infrared Remote Control](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/1/4/0/14865-Infrared_Remote_Control-01.jpg)](https://www.sparkfun.com/products/14865)

### [Infrared Remote Control](https://www.sparkfun.com/products/14865) 

[ COM-14865 ]

Our infrared remote control offers buttons for four directions, power, select, and three optional use buttons (labled \"A,\" \"B...

**Retired**

The **nine button** remote emits unique 32-bit codes for each button press. The codes are mapped as shown in the images below (this will come in handy in our first example). Depending on the IR remote that you are using, the values may be different.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Hex Codes for COM-11759](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/11759-Infrared_Remote_Control_Codes.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/11759-Infrared_Remote_Control_Codes.png)   [![Hex Codes for COM-14865](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/14865-Infrared_Remote_Control_Codes.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/14865-Infrared_Remote_Control_Codes.png)
  Hex Codes for [COM-11759](https://www.sparkfun.com/products/retired/11759)                                                                                                                                                   Hex Codes for [COM-14865](https://www.sparkfun.com/products/14865)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The remote\'s infrared output signal is modulated at 38kHz, so it works perfectly with the IR receiver module.

#### How to Battery?

**Note:** If you are buying the IR remote control seperate from the kit, the unit does **NOT** come with a CR2025 coin cell battery. You can use a CR2032 battery, but we found they get stuck easily because they're slightly too thick. It's recommended that you use the CR2025, it fits well.\
\

[![Coin Cell Battery - 20mm (CR2025)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/3/9/0/11928-Coin-Cell-Battery-20mm-Feature.jpg)](https://www.sparkfun.com/coin-cell-battery-20mm-cr2025.html)

### [Coin Cell Battery - 20mm (CR2025)](https://www.sparkfun.com/coin-cell-battery-20mm-cr2025.html) 

[ PRT-11928 ]

This is the CR2025 20mm coin cell battery. You may be wondering what sets this guy apart from the more common CR2032 coin cel...

[ [\$2.10] ]

The IR remote doesn\'t come with a battery installed but the IR Control Kit includes one for it. The battery compartment can be found on the bottom edge of the remote. To **open the battery compartment**, pinch the latch with your thumbnail while pushing the drawer out with another fingernail.

[![Adding a Coin Cell Battery to the Infared Remote Control](https://cdn.sparkfun.com/r/600-600/assets/4/e/b/9/5/524c4a87757b7fd56c8b456b.png)](https://cdn.sparkfun.com/assets/4/e/b/9/5/524c4a87757b7fd56c8b456b.png)

Insert the battery so that the positive (+) side is facing the **bottom** of the remote. Then slide the battery drawer back in.

## Library Overview

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Download and Install Ken Shirriff\'s IRremote Library

To quickly and easily add IR control to your Arduino, we recommend you download Ken Shirriff\'s IRremote library. Shirriff has written a library for IR remote. You can obtain this library through the Arduino Library Manager. Search for **IRremote by shirriff** and you should be able to install the latest version. If you prefer downloading the libraries manually you can grab them from the [GitHub repository](https://github.com/shirriff/Arduino-IRremote):

[Download Ken Shirriff\'s IRremote Library (ZIP)](https://github.com/z3t0/Arduino-IRremote/archive/master.zip)

**Warning:** Make sure the folder name that you copy into your \"libraries\" folder is named \"IRremote\". Use of the \` - \` in the directory name can lead to errors in compiling the code.

The IRremote library is a powerful tool for adding IR to your project. Whether you want to send IR codes out to an appliance, or transmit IR codes from a remote to your Arduino (or both!). We\'ll go over some of the simple stuff you can do with the library. For more help using it, check out [Ken Shirriff\'s blog](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html).

## Example 1: IR Remote Control Values

### Circuit Diagram

Ready to start hooking everything up? Check out the circuit diagram below to connect the components together.

[![IR Receiver Circuit Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/IR_Receiver_bb_Fritzing_Diagram.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/IR_Receiver_bb_Fritzing_Diagram.jpg)

### Reading IR Remote Control Values

Copy and paste the below code into your Arduino IDE. Then upload it to your Arduino to view the values associated with each button.

    language:c
    /*
      SparkFun Electronics 2013
      Modified by: Ho Yun "Bobby" Chan on 8/6/2018
      Playing with Infrared Remote Control
      Description: By pressing on one of the SparkFun infrared remote
      control's buttons, the serial monitor will output the associated
      hex value when a signal is received by an IR receiver.

      If using with the IR Receiver Breakout (SEN-8554):
      Supply voltage of 2.5V to 5.5V
        Attach
        OUT: To pin 11 on Arduino
        GND: GND
        VCC: 5V

      If using with the IR Receiver Diode (SEN-10266):
      Supply voltage of 2.5V to 5.5V
        Attach
        OUT: To pin 11 on Arduino
        GND: GND
        VS: 5V

      Note: This is based on Ken Shirriff's code found on GitHub.
      Make sure to install the library:
      https://github.com/shirriff/Arduino-IRremote/

      Note: This code also works with cheap remotes. If you want to look
      at the individual timing of the bits, use this code:
      http://www.arduino.cc/playground/Code/InfraredReceivers
    */

    #include <IRremote.h>

    int RECV_PIN = 11;
    IRrecv irrecv(RECV_PIN);
    decode_results results;

    //------------------------------------------------------------
    //Codes for Infrared Remote Control
    //COM-11759 https://www.sparkfun.com/products/retired/11759
    //Note: Uncomment out this section if you are using this w/ the older remote.

    /*
    #define POWER 0x10EFD827
    #define A 0x10EFF807
    #define B 0x10EF7887
    #define C 0x10EF58A7
    #define UP 0x10EFA05F
    #define DOWN 0x10EF00FF
    #define LEFT 0x10EF10EF
    #define RIGHT 0x10EF807F
    #define SELECT 0x10EF20DF
    */
    //------------------------------------------------------------
    //Codes for Infrared Remote Control
    //COM-14865 https://www.sparkfun.com/products/14865
    //Note: Comment out this section if you are using this w/ the older remote.

    #define POWER 0x00FF629D
    #define A 0x00FF22DD
    #define B 0x00FF02FD
    #define C 0x00FFC23D
    #define UP 0x00FF9867
    #define DOWN 0x00FF38C7
    #define LEFT 0x00FF30CF
    #define RIGHT 0x00FF7A85
    #define SELECT 0x00FF18E7

    //------------------------------------------------------------

    void setup()
    

    void loop()
    
        else if (results.value == A)
        
        else if (results.value == B)
        
        else if (results.value == C)
        
        else if (results.value == UP)
        
        else if (results.value == DOWN)
        
        else if (results.value == LEFT)
        
        else if (results.value == RIGHT)
        
        else if (results.value == SELECT)
        
        else 

        Serial.print("IR RECV Code = 0x ");
        Serial.println(results.value, HEX);
        irrecv.resume();
      }
    }

Open a [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at a **9600 baud**. Press the buttons on the IR remote to see the associated button values. If you have an older version of the IR remote control or received one outside of our catalog, make sure to update the code to reflect the corresponding button presses. Simply comment/uncomment the code for the remote or update the values for the remote that you are using. Now that we can read the button presses, we can control your project with IR!

## Example 2: Using the Remote

In the first example, we\'ll show how you can connect the IR receiver to an Arduino, and control it with the IR remote.

### Circuit Diagram

In this first example, we\'ll use the IR receiving capabilities of the IRremote library to use the SparkFun IR remote to control a common cathode RGB LED. An RGB LED isn\'t included with the [IR Control Kit](https://www.sparkfun.com/products/11761), but it might be something you\'ve already got in your parts box. If not, any set of three will do. Or you can even just use the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) as your output monitor.

This is how we\'ll connect the IR receiver and RGB LED to our Arduino:

[![Circuit fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/f/1/7/6/7/524b4959757b7f456d8b4568.png)](https://cdn.sparkfun.com/assets/f/1/7/6/7/524b4959757b7f456d8b4568.png)

The output of the IR receiver connects to D11, but it could be connected to any digital input pin. If you swap pins, make sure you reflect those changes in code!

We don\'t have a use for the IR LED yet, so, for now, set that safely aside.

### RGB Remote Control

Copy and paste the below code into your Arduino IDE. Then upload it to your Arduino to create your very own, remote controlled, RGB LED.

    language:c
    /* RGB Remote Control
       by: Jim Lindblom
       SparkFun Electronics
       date: October 1, 2013

       This sketch uses Ken Shirriff's *awesome* IRremote library:
           https://github.com/shirriff/Arduino-IRremote

       RGB Remote Control uses a combination of SparkFun's
       IR Remote (https://www.sparkfun.com/products/11759) and an
       IR receiver diode (https://www.sparkfun.com/products/10266) to
       control an RGB LED.

       The IR Remote's power button turns the LED on or off. The A, B,
       and C buttons select a channel (red, green, or blue). The up
       and down arrows increment or decrement the LED brightness on that channel.
       The left and right arrows turn a channel to min or max, and
       circle set it to the middle.

       Hardware setup:
         * The output of an IR Receiver Diode (38 kHz demodulating
           version) should be connected to the Arduino's pin 11.
           * The IR Receiver diode should also be powered off the
             Arduino's 5V and GND rails.
         * A common cathode RGB LED is connected to Arduino's pins
           5, 9, and 6 (red, green, and blue pins).
     */

    #include <IRremote.h> // Include the IRremote library

    /* Setup constants for SparkFun's IR Remote: */
    #define NUM_BUTTONS 9 // The remote has 9 buttons
    /* Define the IR remote button codes. We're only using the
       least signinficant two bytes of these codes. Each one
       should actually have 0x10EF in front of it. Find these codes
       by running the IRrecvDump example sketch included with
       the IRremote library.*/

    //------------------------------------------------------------
    //Codes for Infrared Remote Control
    //COM-11759 https://www.sparkfun.com/products/retired/11759
    //Note: Uncomment out this section if you are using this w/ the older remote.

    /*
    const uint16_t BUTTON_POWER = 0xD827; // i.e. 0x10EFD827
    const uint16_t BUTTON_A = 0xF807;
    const uint16_t BUTTON_B = 0x7887;
    const uint16_t BUTTON_C = 0x58A7;
    const uint16_t BUTTON_UP = 0xA05F;
    const uint16_t BUTTON_DOWN = 0x00FF;
    const uint16_t BUTTON_LEFT = 0x10EF;
    const uint16_t BUTTON_RIGHT = 0x807F;
    const uint16_t BUTTON_CIRCLE = 0x20DF;
    */
    //------------------------------------------------------------
    //Codes for Infrared Remote Control
    //COM-14865 https://www.sparkfun.com/products/14865
    //Note: Comment out this section if you are using this w/ the older remote.

    const uint16_t BUTTON_POWER = 0x629D;
    const uint16_t BUTTON_A = 0x22DD;
    const uint16_t BUTTON_B = 0x02FD;
    const uint16_t BUTTON_C = 0xC23D;
    const uint16_t BUTTON_UP = 0x9867;
    const uint16_t BUTTON_DOWN = 0x38C7;
    const uint16_t BUTTON_LEFT = 0x30CF;
    const uint16_t BUTTON_RIGHT = 0x7A85;
    const uint16_t BUTTON_CIRCLE = 0x18E7;

    //------------------------------------------------------------

    /* Connect the output of the IR receiver diode to pin 11. */
    int RECV_PIN = 11;
    /* Initialize the irrecv part of the IRremote  library */
    IRrecv irrecv(RECV_PIN);
    decode_results results; // This will store our IR received codes
    uint16_t lastCode = 0; // This keeps track of the last code RX'd

    /* Setup RGB LED pins: */
    enum ledOrder // Make an enum to add some clarity in the code
    ;
    const int rgbPins[3] = ; // Red, green, blue pins respectively
    byte rgbValues[3] = ; // This keeps track of channel brightness
    byte activeChannel = RED; // Start with RED as the active channel
    boolean ledEnable = 1; // Start with the LED on.

    void setup()
    
    }

    // loop() constantly checks for any received IR codes. At the
    // end it updates the RGB LED.
    void loop()
    
        irrecv.resume(); // Receive the next value
      }

      // Every time through the loop, update the RGB LEDs:
      if (ledEnable)
      
      }
      else
      
      }
    }

When the code initializes, the RGB LED will be set to a certain brightness. Then we\'re basically looping and checking to see if the IR receiver diode has received a known code from the IR remote. If so, it\'ll have some effect on the LED \-- turning it on/off, turning up or down red/green/blue, etc. Pressing on the buttons A, B, or C will allow you to adjust the corresponding color. Once a letter is pressed, you can adjust the brightness with the direction pad. Check the comments in the code for help understanding what\'s going on.

You can also check the output of the serial monitor to make sure the codes are being received. When a known code is received, it\'ll print out the corresponding button. When an unknown code is received (which shouldn\'t be often, if ever, if you\'re only using the SparkFun IR remote), it\'ll print that code out in hexadecimal.

**Heads up!** When the red LED is fully turned on, it may dominate over the other colors. Try turning it down by using a smaller value. For ideas on making your own custom colors, try looking at the [LilyPad protoSnap Plus Activity Guide: 3. Custom Color Mixing](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/3-custom-color-mixing) for ideas.

### Play!

That\'s all there is to it! Try exploring the code and replacing the RGB LED with other devices you can control. How about a servo motor? Or a relay! There are so many possibilities!

Do you have other IR remotes around? Try them out! As you press a button, check the serial monitor (at **9600 bps**) to see what code it spits out. Then add a case for those in the switch statement.

## Example 3: Transmitting

After you\'ve gotten the remote and receiver working, it\'s time to add some IR transmission to the setup.

For this example, we\'ll set up an infrared data relay using both the receiver and an IR LED to transmit data. IR codes received by the Arduino can be sent out the LED by the press of a button.

### Setting Up the Hardware

On the hardware level, using the IRremote library, there\'s only **one pin** we can use to transmit IR data: **pin 3**. There\'s not any give here; pin 3\'s [PWM](https://learn.sparkfun.com/tutorials/pulse-width-modulation)-capabilities make it one of the best choices for transmitting the 38kHz modulated IR data.

We\'ll also be adding a button to this circuit. If you don\'t have a button around, you can simply pull pin 12 LOW to emulate a button press. Here\'s the whole circuit:

[![Example 2 fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/3/5/4/0/3/525e55ec757b7fce268b456a.png)](https://cdn.sparkfun.com/assets/3/5/4/0/3/525e55ec757b7fce268b456a.png)

### Adding Code

Once you\'ve got the hardware all wired up, copy and paste the code below. Then upload it to your Arduino.

    language:c
    /* IRrecord (Redux)
       by: Jim Lindblom
       SparkFun Electronics
       date: October 1, 2013

       This sketch uses Ken Shirriff's *awesome* IRremote library:
           https://github.com/shirriff/Arduino-IRremote
       It's a slightly modified version of the IRrecord example that
       comes with that library.

       This sketch uses the IR receiver diode to "record" an IR code.
       Then, when triggered via a button on pin 12, it will transmit
       that IR code out of an attached IR LED on pin 3.

       Hardware setup:
         * The output of an IR Receiver Diode (38 kHz demodulating
           version) should be connected to the Arduino's pin 11.
           * The IR Receiver diode should also be powered off the
             Arduino's 5V and GND rails.
         * The anode (+, longer leg) of an IR LED should be connected to pin 3 of 
           the Arduino. The cathode (-) should be connected to a 330
           Ohm resistor, which connects to ground.
         * A button should be connected to ground on one end, and pin
           12 of the Arduino on the other.

    */
    #include <IRremote.h> // Include the IRremote library

    /* Connect the output of the IR receiver diode to pin 11. */
    int RECV_PIN = 11;
    /* Initialize the irrecv part of the IRremote  library */
    IRrecv irrecv(RECV_PIN);
    decode_results results; // This will store our IR received codes

    IRsend irsend; // Enables IR transmit on pin 3

    /* Storage variables for the received IR code: */
    unsigned int irLen = 0; // The length of the code
    unsigned int irBuffer[RAWBUF]; // Storage for raw (UNKNOWN) codes
    int codeType; // The type of code (NEC, SONY, UNKNOWN, etc.)
    unsigned int codeValue; // The value of a known code
    boolean codeReceived = false; // A boolean to keep track of if a code was received

    const int buttonPin = 12; // Button pin. Pulled up. Triggered when connected to ground.

    // setup() initializes serial and the Infrared receiver.
    void setup()
    

    // loop() checks for either a button press or a received IR code.
    void loop()
    

      // If the button is pressed, and we've received a code...
      if ((digitalRead(buttonPin) == LOW) && (codeReceived == true))
      
    }

    /* This function reads in the received IR data, and updates the
       following variables:
        * codeType -- How was the IR signal encoded? SONY, NEC, 
          UNKNOWN, etc.
        * irLen -- The length (number of marks and ticks) of an IR code.
        * Depending on the codeType, one of these two variables will
          be updated as well:
          * codeValue -- IF the codeType is a known type, this variable
            will contain the received code.
          * irBuffer -- If the codeType is UNKNOWN, this buffer will
            contain the format of the received code.

        This function borrows heavily from the IRrecord example code.
    */
    void updateIRReceive()
     
          else 
          
          Serial.print(irBuffer[i-1], DEC);
        }
        Serial.println();
      }
      else 
      
        } 
        else if (codeType == SONY) 
         
        else if (codeType == RC5) 
         
        else if (codeType == RC6) 
         
        else 
        
        Serial.println(results.value, HEX);
        codeValue = results.value;
        irLen = results.bits;
      }
    }

    void sendCode()
     
      else if (codeType == SONY)
       
      else if (codeType == RC5 || codeType == RC6) 
       
        else 
        
      } 
      else if (codeType == UNKNOWN /* i.e. raw */) 
      
    }

To use the sketch, you\'ll still need an IR remote. Begin by **opening the serial monitor** (at 9600 bps). Then **press a button** on the remote. The serial monitor should notify you that a IR code was received. The Arduino\'s now all loaded up, ready to spit out its own IR code.

To send out the IR code, **press the button** connected to pin 12 (or just short a jumper wire from 12 to GND). The way the example code is written, the IR LED will send the IR code once until the Arduino receives another IR code to record. Unless you have a device that is looking for specific IR codes, you may not see anything happen. Try the sketch out with some IR remotes and appliances around your house. Can your Arduino trigger your TV to mute?

#### Delving Into IR Sends

If you\'re using the IRremote library to transmit data, there are just a few lines of code you\'ll need to add. First, you\'ll need to declare an instance of `IRsend` at the top of your code:

    language:c
    IRsend irsend;

There are a variety of transmitting options made available by the library. They vary by encoding scheme, which usually depends on the manufacturer. You can use any of these functions to send out IR data:

    language:c
    void sendNEC(unsigned long data, int nbits);
    void sendSony(unsigned long data, int nbits);
    void sendRC5(unsigned long data, int nbits);
    void sendRC6(unsigned long data, int nbits);
    void sendDISH(unsigned long data, int nbits);
    void sendSharp(unsigned long data, int nbits);
    void sendPanasonic(unsigned int address, unsigned long data);
    void sendJVC(unsigned long data, int nbits, int repeat);

    void sendRaw(unsigned int buf[], int len, int hz);

If you don\'t have an appliance matching any of those manufacturers (NEC, Sony, DISH, Sharp, Panasonic, JVC, etc.), you\'ll have to use the `sendRaw` function to transmit your IR code.

**Looking for more power?** Infrared LEDs are awesome. Along with an IR receiver they can be used for remote control and even basic remote data communication. The only problem is that your Arduino won't drive them to their full potential. The transmission range of the LED might not be optimal. Output pins on the Arduino can only source up to about 30mA of current. This means the LED cannot be driven to its full power of 50mA. This will result in a loss of transmission distance.\
\
If you want to drive an IR LED properly, consider using the IR LED with a transistor and resistor that was used in the design of the old [SparkFun Max Power IR LED kit](https://www.sparkfun.com/products/retired/10732). To control, simply provide it with voltage (5V), ground, and connect the CTL pin to a digital pin on your Arduino, and you can drive this kit just like a normal LED. However, a 330Ω attached to your IR LED should give about 10 feet of range.\
\

[![SparkFun Max Power IR LED Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/5/6/3/1/10732-02a.jpg)](https://www.sparkfun.com/products/10732)

### [SparkFun Max Power IR LED Kit](https://www.sparkfun.com/products/10732) 

[ KIT-10732 ]

Infrared LEDs are awesome. Along with an IR receiver they can be used for remote control and even basic remote data communica...

**Retired**