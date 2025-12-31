# Source: https://learn.sparkfun.com/tutorials/lilypad-development-board-hookup-guide

## Introduction

#### Note to Users:

This resource is for users who are using the [LilyPad Development Board](https://www.sparkfun.com/products/retired/11262).\
\
For users with the [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346), please refer to the [LilyPad ProtoSnap Plus Hookup Guide](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-hookup-guide).

Interested in getting into LilyPad? Or maybe it\'s Arduino that tickles your fancy? Both? Well, whatever it is, the [ProtoSnap LilyPad Development Board](https://www.sparkfun.com/products/11262) is a great tool to start with!

[![LilyPad ProtoSnap Development Board](https://cdn.sparkfun.com/r/600-600/assets/parts/6/8/8/6/11262-01.jpg)](https://www.sparkfun.com/products/11262)

### [LilyPad ProtoSnap Development Board](https://www.sparkfun.com/products/11262) 

[ DEV-11262 ]

The ProtoSnap series is a new way to prototype your project without a breadboard. Everything is wired together on a single bo...

**Retired**

[![LilyPad Lab Pack](https://cdn.sparkfun.com/r/600-600/assets/parts/7/9/9/3/LilyPack.jpg)](https://www.sparkfun.com/products/11762)

### [LilyPad Lab Pack](https://www.sparkfun.com/products/11762) 

[ LAB-11762 ]

The ProtoSnap LilyPad Development Board is a good way to introduce and explore e-textiles. This LabPack includes everything y...

**Retired**

The ProtoSnap LilyPad Development Board features a conglomerate of some of our favorite LilyPad boards. At the center of this mish-mash is our [LilyPad Arduino Simple Board](https://www.sparkfun.com/products/10274) \-- a small, LilyPad version of the popular Arduino development platform. Using the included [FTDI Basic Breakout](http://www.sparkfun.com/products/10275), you can program this board to work with a whole mess of inputs and outputs:

- 1 x [LilyPad Button](http://www.sparkfun.com/products/8776)
- 1 x [LilyPad Slide Switch](http://www.sparkfun.com/products/9350)
- 5 x [LilyPad Bright White LED](http://www.sparkfun.com/products/10081)
- 1 x [LilyPad RGB Tri-Color LED](http://www.sparkfun.com/products/8467)
- 1 x [LilyPad Light Sensor](http://www.sparkfun.com/products/8464)
- 1 x [LilyPad Temperature Sensor](http://www.sparkfun.com/products/8777)
- 1 x [LilyPad Buzzer](http://www.sparkfun.com/products/8463)
- 1 x [LilyPad Vibe Board](http://www.sparkfun.com/products/8468)

All of these are already wired up to the LilyPad Arduino Simple. Then, once you feel comfortable programming the Arduino to talk to all those boards, you can break each piece off individually and implement them into your project however you see fit. But\...

[ ] **Don't snap apart your LilyPad Development Board** until you\'re ready to use the pieces in a project. If you leave the pieces attached to the board, you\'ll be able to prototype and test your project before you start sewing.

### Required Materials

To reprogram and recharge the board, you\'ll need to connect a mini-B USB cable. Double check that it is not labeled 'Power Only' as these type of cables will not transmit the programming data needed by the LilyPad Arduino Simple Board. If you don\'t have one you can get one from SparkFun:

[![SparkFun USB Mini-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/6/9/8/0/11301-01.jpg)](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html)

### [SparkFun USB Mini-B Cable - 6 Foot](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html) 

[ CAB-11301 ]

This is a USB 2.0 type A to Mini-B 5-pin cable. You know, the mini-B connector that usually comes with USB Hubs, Cameras, MP3...

[ [\$5.50] ]

**Note:** The [LilyPad FTDI](https://www.sparkfun.com/products/10275) is included in the LilyPad Development Board. If you bought the LilyPad Arduino Simple board separately, you will need both the mini-B USB cable and FTDI to follow along with this guide.

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/planning-a-wearable-electronics-project)

### Planning a Wearable Electronics Project 

Tips and tricks for brainstorming and creating a wearables project.

## Hardware Overview and Features

[ ] **Don't snap apart your LilyPad Development Board** until you\'re ready to use the pieces in a project. If you leave the pieces attached to the board, you\'ll be able to prototype and test your project before you start sewing.

The LilyPad Development Board features twelve LilyPad components connected to a LilyPad Arduino Simple microcontroller by conductive pathways called traces. Many of these traces are hidden, but for reference, each component on the ProtoSnap has a nearby label printed in white silkscreen with the number of the LilyPad Arduino Simple sew tab it is connected to.

If you\'ve used an Arduino before, you\'re probably familiar with its pins \-- both digital and analog. An Arduino has 14 [digital pins](http://arduino.cc/en/Tutorial/DigitalPins), and six to eight [analog pins](http://www.arduino.cc/en/Tutorial/AnalogInputPins), all of which can be used to interface with other components; for instance, those surrounding the Arduino on the ProtoSnap LilyPad Development Board.

It\'s important to know which pin on the Arduino is tied to which component. Should you ever need a reminder of what pin connects to what, all you really need to do is look down.

[![LilyPad Development Board Pin Labels Annotated](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/0/Dev_Labels_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/Dev_Labels_2.png)

[ ] **Some of the sew tabs on the LilyPad Arduino Simple have special functionality:**\
\

- An \'A\' in front of the number denotes a tab that can function as an [analog input](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion). These sew tabs can read sensors that output a varying voltage like the light sensor built into the LilyPad Arduino Simple.\
  \
- Referring to the annotated image above of the LilyPad Development Board, a \'\~\' symbol in front of the number indicates that tab supports [PWM (Pulse Width Modulation) output](https://learn.sparkfun.com/tutorials/pulse-width-modulation). These tabs can output an \"analog\" signal that can be used to vary the brightness on LEDs, etc.

\
**Note:** The \"A\" in front of analog sew tab numbers in your code is optional. However, do not include the \"\~\" symbol for PWM outputs. It is only provided to make it easy for you to check which pins can produce PWM (analog) output and is not used in programming.

But, in case your eyes aren\'t up to reading that tiny text, here\'s a list of the components that are connected to the LilyPad Arduino Simple:

  LilyPad Component                     Arduino Pin            Connected to LilyPad Arduino Simple Sew Tab   Description
  ------------------------------------- ---------------------- --------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------
  LilyPad Vibe Board                    \~3                                                                  Haptic feedback is provided with the motor\'s vibration and is controlled by the LilyPad Arduino Simple.
  LilyPad Tri-Color (RGB) LED - Red     \~9                    ✓                                             The tri-color LED\'s red is controlled by the LilyPad Arduino Simple.
  LilyPad Tri-Color (RGB) LED - Blue    \~10                   ✓                                             The tri-color LED\'s blue is controlled by the LilyPad Arduino Simple.
  LilyPad Tri-Color (RGB) LED - Green   \~11                   ✓                                             The tri-color LED\'s green is controlled by the LilyPad Arduino Simple.
  LilyPad Button                        A5                     ✓                                             LilyPad Arduino Simple receives button presses as an input.
  LilyPad Slide Switch                  2                                                                    LilyPad Arduino Simple receives switch state (on/off) input.
  LilyPad White LEDs                    \~5, \~6, A2, A3, A4   ✓ (all 5 LEDs)                                A set of white LEDs controlled by the LilyPad Arduino Simple.
  LilyPad Buzzer (+)                    7                                                                    A buzzer that create tones controlled by the LilyPad Arduino Simple.
  LilyPad Buzzer (-)                    12                                                                   A buzzer that create tones controlled by the LilyPad Arduino Simple. While normally connected to GND, it can be connected to an Arduino pin.
  LilyPad Light Sensor                  A6                                                                   LilyPad Arduino Simple receives ambient light level input from light sensor.
  LilyPad Temperature Sensor            A1                                                                   LilyPad Arduino Simple receives temperature from a physical touch based on body heat and ambient conditions with the analog sensor.

**Heads up!** When planning to snap the LilyPad components apart for a project, not all the components will be able to connect due to the design of the LilyPad Arduino Simple\'s sew tabs. Certain components are currently connected to the LilyPad Arduino Simple via small traces instead of the petals. The table above indicates which pins are currently connected to the sew tabs. Make sure to plan the project accordingly. You will also need to redefine the pins in code when reconnecting the components to the sew tabs.\
\
For example, if you decide to snap the components off and use the light sensor instead of a white LED, you will need to reconnect the light sensor to another analog pin (like A2-A5). By replacing the connection of one of the components, the sensor will be able to be controlled by the LilyPad Arduino Simple again. Replacing the LED on A3, will require the code to be adjusted for the LilyPad light sensor on A3.

### LilyPad Tri-Color LED

Inside an RGB LED are three smaller LEDs - a red, green, and blue. Each of these LEDs is connected to a sew tab on the [Tri-Color LED](https://www.sparkfun.com/products/8467), and they are all connected through a common anode (positive) pin. Unlike other RGB LEDs, this configuration means that to light up the LED you need to ground the individual red, green, and blue LEDs instead of sending them power.

[![LilyPad Tri-Color LED Common Anode](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LilyPad_Tri-Color_LED_Dev_RGBDetail_Common_Anode.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LilyPad_Tri-Color_LED_Dev_RGBDetail_Common_Anode.png)

### LilyPad Arduino Simple Board

Most of the individual boards on the ProtoSnap LilyPad Development Board are relatively simple; they\'ve got one big component, and maybe a few small supporting components, like resistors. But there are a few complexities to the [LilyPad Arduino Simple](https://www.sparkfun.com/products/10274) we should overview.

[![LilyPad Arduino Simple Board](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/5/2/0/10274-04c.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10274-04c.jpg)

**Features:**

- 5 Digital I/O pins
- 4 Analog pins
- ATmega328P
- Built-in LED on pin 13
- Built-in ON/OFF switch
- Built-in power supply socket (JST connector) for a 3.7V LiPo battery and charging circuit (no additional battery charger needed)
- Simplified layout with less pins, giving more space for sewing or less complex projects

Central to the Simple board is the **ATmega328** \-- the big black square in the middle of the board. This is the microprocessor, the \"brains of the operation.\" This is what stores and executes your Arduino sketch. Surrounding the ATmega328 are a few passive supporting components, nothing all that important to you.

[![LilyPad Arduino Simple Atmega328P](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/5/2/0/10274-04c_ATmega328.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10274-04c_ATmega328.png)

To the right of the ATmega328 (though it\'ll be hard to see unless it\'s lit) is a tiny little **LED**. This could be classified as the most important component on the Arduino. The LED is tied to Arduino pin 13, and can be used for all your blinking needs. At the top left, there\'s a momentary push button, used to **reset** the ATmega328. This will make whatever sketch the Arduino is running start from the very top again.

[![LilyPad Arduino Simple Built-In LED](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/5/2/0/10274-04c_LilyPadArduinoSimpleBuiltInLED.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10274-04c_LilyPadArduinoSimpleBuiltInLED.png)

There\'s an **On/Off slide switch **under the ATmega328. The functionality of that is pretty obvious, but it can be a little misleading. There are a few ways to power the ProtoSnap LilyPad Development Board, and in most cases, you\'ll probably use the included FTDI board to power it using your computer\'s USB. If the board is powered by the FTDI board, the On/Off switch will do absolutely nothing. The switch only controls power to the Arduino if you\'re powering it via that little white connector to the left of the ATmega.

[![LilyPad Arduino Simple Battery Power Switch](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/5/2/0/10274-04c_LilyPadArduinoSimpleBatteryPowerSwitch.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10274-04c_LilyPadArduinoSimpleBatteryPowerSwitch.png)

The **white connector** on the Simple board is a somewhat common power connector, hailing from the JST family of connectors. It\'s mainly geared towards connecting one of our [Lithium Polymer](http://www.sparkfun.com/search/results?term=lithium+ion&what=products) batteries. LiPo\'s are rechargable batteries, so we\'ve also included a **battery charger** on the LilyPad Arduino Simple. So if you have the battery plugged in, and an FTDI Basic Breakout connected, you can charge the battery from your computer.

[![LilyPad Arduino Simple JST Connector](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/5/2/0/10274-04c_LilyPadArduinoSimpleBatteryJSTConnector.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10274-04c_LilyPadArduinoSimpleBatteryJSTConnector.png)

Oh, and where do you connect the FTDI board? Well, spiking up at the top of the Arduino Simple is a **right-angle six-pin male header**. The female header on the FTDI board should slide smoothly onto that connector.

[![LilyPad Arduino Simple FTDI Programming Header](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/5/2/0/10274-04c_LilyPadArduinoSimpleFTDIProgrammingHeader.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10274-04c_LilyPadArduinoSimpleFTDIProgrammingHeader.png)

### Powering the LilyPad Development Board

The LilyPad LilyPad Development Board can be powered in two ways:

- If you have a USB power source available (a computer, 5V USB wall adapter, USB battery pack, etc.), you can run the board from a USB cable and FTDI.

- If you\'d like your project to be more portable, you can easily attach a rechargable Lithium-polymer battery to the board. See [Technical Notes](#battery) section for more information on batteries and charging.

## Exploring the Sample Circuit

[ ] **Don't snap apart your LilyPad Development Board** until you\'re ready to use the pieces in a project. If you leave the pieces attached to the board, you\'ll be able to prototype and test your project before you start sewing.

The LilyPad Development Board ships with pre-loaded code that showcases all of the LilyPad pieces connected to it. To power up the LilyPad Development Board, connect it to your computer using a FTDI and mini-B USB cable, or attach an [E-Textiles Battery](https://www.sparkfun.com/products/13112). Then slide the switch on the right side of the LilyPad Arduino Simple to the ON position.

First the white LEDs turn on individually one at a time. Then the RGB LED will blink each color. Once the sequence completes, the LilyPad Development Board will be ready to take inputs! Try placing your finger over the temperature sensor. Once the sensor reads a certain threshold, the red LED will light up. Placing your finger over the light sensor will turn on the white LEDs. Pressing on the momentary push button will cause the buzzer to make some noise. Flipping the LilyPad slide switch (located on the bottom left side of the board) to the ON position will cause the vibe motor to begin vibrating for haptic feedback.

[![LilyPad Development Board Demo](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10958-04a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10958-04a.jpg)

## Setting Up Arduino

**Note:** This guide assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### Install FTDI Drivers

If you\'ve never used a LilyPad Arduino before, you will need to install FTDI drivers. Depending on your computer's operating system, you will need to follow specific instructions. Please go to [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/usb-serial-driver-quick-install-), for specific instructions on how to install the FTDI drivers onto your computer.

\

[](https://learn.sparkfun.com/tutorials/usb-serial-driver-quick-install-)

### USB Serial Driver Quick Install 

August 31, 2017

How to install USB serial drivers on Windows, MacOS , and Linux.

Note that you *won\'t* have to install the FTDI drivers again.

## Uploading Code

You *will* need to perform the below three steps every time you want to program the board. These three steps are:

1\. Connect the LilyPad Development Board to your computer using the FTDI board and a USB cable.\
2. Select **\"LilyPad Arduino\"** from Arduino\'s **\"Board\"** menu.\
3. Select **\"ATmega328\"** from Arduino\'s **\"Processor\"** menu.\
4. Select the serial port the LilyPad is connected to from Arduino\'s **\"Port\"** menu.

Let\'s go over the three steps in detail:

### 1. Connect the LilyPad Development Board to Your Computer

Place the LilyPad Development Board on a clean, non-metal work surface. Connect the LilyPad FTDI Board to the headers on the LilyPad Arduino Simple at the center of the Development Board.

[![Attach FTDI to LilyPad Development Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/0/LilyPadDev_AttachFTDI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LilyPadDev_AttachFTDI.jpg)

Connect the other side of the FTDI board to a mini-B USB cable.The cable can only be inserted one way, and should snap in securely.

[![Attach USB Cable to LilyPad Development Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/0/LilyPadDev_FTDIUSB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LilyPadDev_FTDIUSB.jpg)

Then connect the other end of the USB cable to a USB port on your computer.

[![Connect LilyPad Development Board to Computer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/0/LilyPadDev_PluggedIn.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LilyPadDev_PluggedIn.jpg)

Slide the switch on the LilyPad Arduino to the ON position. You will not be able to upload code to the board if it is set to the OFF position.

[![Turn LilyPad Development Board\'s Switch to ON Position](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/0/LilyPadDEV_OnSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LilyPadDEV_OnSwitch.jpg)

### 2. Select LilyPad Arduino from the Board Menu

To program the LilyPad Arduino Simple at the center of the LilyPad Development Board, open the **Tools** \> **Board** list and select **LilyPad Arduino**. A dot (Windows) or check mark (Mac) will show next to the board in the menu when it is selected, and it will show next to Board in the Tools menu.

[![Select LilyPad Development Board in Arduino IDE](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/0/LilyPadSelectArduino.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LilyPadSelectArduino.png)

### 3. Select ATmega328 from the Processor Menu

After selecting the LilyPad Arduino, there will be two options available in the next menu down labeled **Processor**. Select **ATmega328** for your LilyPad Arduino.

[![Select ATmega328 for LilyPad Development Board in Arduino IDE](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/0/LilyPadDevSelectProcessor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LilyPadDevSelectProcessor.png)

### 4. Select Port from the Port Menu

Arduino needs to know which port your LilyPad Arduino is attached to so it can program it. Whenever you plug a USB device into your computer, your computer will assign it a port number. Go to the **Tools** \> **Port** menu, and select the port that has the LilyPad Arduino attached to it.

On Windows ports are listed as COM##; on a Mac or Linux machine they will be \"/dev/cu.usbmodem####\". Your screen may look different than the image below, depending on what operating system you are using.

[![Select LilyPad Development Board\'s COM Port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/0/LIlyPadDevSelectSerial.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LIlyPadDevSelectSerial.png)

**Troubleshooting:** If you don\'t see a port in the menu, ensure that the board is powered up (switch in the ON position), and that the USB cable is securely connected to both the board and your computer and that you have installed the FTDI drivers. Some USB cables are only meant for charging and don\'t pass data - they\'ll power the board, but it won\'t show up in the port menu. If needed, try a different cable.

### Upload Blink

In the world of embedded electronics, every good development platform has to have an LED, and the first test program to be run on any development platform is almost always the blinking of an LED. So let\'s blink that little LED on the LilyPad Simple Arduino board.

To review, once you\'ve:

1.  Connected the LilyPad Development Board to your computer using the FTDI and USB cable.
2.  Selected the board type (\"**LilyPad Arduino**\" as the board and ATmega328 as the processor).
3.  Selected the COM port from the **\"Port\"** menu.

You are ready to upload code! Let\'s upload some code to try it out.

Load the \"Blink\" example from the menu **File** \> **Examples** \> **01.Basics** \> **Blink**, and click the \"Upload\" button (the large round button with the right arrow in it). This is a very simple example program; it just blinks a LED on and off once per second.

[![Blink Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/0/OpenBlinkExample.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/OpenBlinkExample.png)

Arduino will compile the code, then send it to the LilyPad Arduino Simple via the USB cable. While the code is uploading, the built-in LED will blink to signal the code is transferring. When the code finally runs, the LED at the center of the board will slowly blink green. Success!

If this all works, congratulations! You\'re all set up and ready to prototype with the LilyPad Development Board.

### Default Example Code

If you are interested in re-uploading the default example code that you explored earlier, it is available in the [product GitHub repository](https://github.com/sparkfun/ProtoSnap-LilyPad_Development_Board) and in the download button shown below.

[Download LilyPad Development Board Sample Code](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/LilyPadDev_v11rev.ino)

### Beyond the Blinking

Well, we\'ve just opened an enormous can of worms, and you\'ve taken your first step into the life-consuming world of Arduino. From here, you may want to explore some of Arduino\'s other example sketches. There\'s one for the button **(File \> Examples \> 2.Digital \> Button)**, or you could fade those RGB LEDs **(File \> Examples \> 1.Basics \> Fade)**, or you could play a song on the buzzer **(File \> Examples \> 2.Digital \> toneMelody)**, or maybe try adapting the AnalogInOutSerial sketch **(File \> Examples \> 3.Analog \> AnalogInOutSerial)** to the temperature and light sensors. Just make sure you change the pins to their proper mapping on the LilyPad Development Board!

[![Uploading to the LilyPad Development Board](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10506-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/0/10506-04.jpg)

You can also check out the [LilyPad Development Board Activity Guide](https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide):

[](https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide)

### LilyPad Development Board Activity Guide 

December 7, 2017

Learn how to program in Arduino with the LilyPad Development Board. This guide includes 11 example activities that use the pre-wired LilyPad boards on the LilyPad Development Board.

## Stitching Into A Project

Once you feel comfortable with the Arduino programming, maybe you\'ll start to feel constrained by the current configuration of the ProtoSnap LilyPad Development Board. At that point, feel free to snap each individual part off, and turn them into the next great creation! You\'ll have a solid foundation in Arduino programming, so you can put all your focus into getting the hardware just right.

For ideas, check out the example project used in the smaller [LilyPad Development Simple board](https://learn.sparkfun.com/tutorials/protosnap-lilypad-development-simple-hookup-guide) in order to snap the components and sew to fabric.

[](https://learn.sparkfun.com/tutorials/protosnap-lilypad-development-simple-hookup-guide)

### ProtoSnap LilyPad Development Simple Hookup Guide 

September 5, 2013

Interested in getting into LilyPad? Or maybe it\'s Arduino that tickles your fancy? Just want to add a little white-blinky-LED zest to your vest? All of the above? The ProtoSnap LilyPad Simple is a great tool to explore any of these subjects.

These tutorials will give you some tips and tricks for [project construction](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing) and [insulation](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles):

[](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles)

### Insulation Techniques for e-Textiles 

Learn a few different ways to protect your conductive thread and LilyPad components in your next wearables project.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

## Technical Notes

If you've already programmed Arduino for a while, read on for some additional notes about the LilyPad Development Board. It's very similar to other Arduinos, but has some special features and limitations you'll want to know about.

### Pin Numbering

Below is a list of the LilyPad Arduino Simple I/O pins and each function.

**Legend:**

- *n* = digital pin\
- \~*n* = PWM-capable pin\
- *n, serial* = hardware serial pin for either UART, I2C, or SPI
- A*n* = analog-capable pin\
- (*n*) = internal pin (not connected to sew tab)\
- \[*n*\] = internal pin (available on an exposed via)
-  = internal pin (available on male header pin)\

  Function                Digital        Analog
  ----------------------- -------------- ---------
  Rx-I                    , RX        
  Tx-O                    , TX        
  Slide Switch            \(2\)          
  Vibe Board              (\~3)          
  White LED               \~5            
  White LED               \~6            
  Buzzer                  \(7\)          
  RGB LED - Red           \~9            
  RGB LED - Blue          \~10, SS       
  RGB LED - Green         11, MOSI       
                          \[12\], MISO   
  Built-in Green LED      \[13\], SCK    
  Temperature Sensor      \(15\)         (A1)
  White LED               16             A2
  White LED               17             A3
  White LED               18             A4, SDA
  Momentary Push Button   19             A5, SCL
  Light Sensor                           (A6)

### [][Using a LiPo Battery and Battery Charging](#battery)

SparkFun sells a number of LiPo batteries compatible with this board. If you are new to the LilyPad system, we recommend the [E-Textiles Battery](https://www.sparkfun.com/products/13112). If you\'re supplying your own battery, use a single-cell (3.7V) LiPo battery with a JST connector.

Batteries with larger capacities (measured as amp-hours or Ah) will run the board longer before needing recharging. How long will depend on how many LEDs your program turns on, etc. If you\'re just running a few LEDs, you can expect the board to run about 5 hours for every 100mAh of battery capacity.

#### Charge Rate

To recharge an attached battery, plug the board into a USB power source. While the battery is charging, the \"CHG\" LED will illuminate. When the battery is fully charged the LED will turn off. The default charge current is set to **100mA**, so a 100mAh battery will recharge in one hour, a 1000mAh battery in 10 hours, etc. Since the board is set to charge at a rate of 100mA, we do not recommend connecting a lower capacity LiPo battery (i.e. 40mAh LiPo battery) to charge.

[![Connecting a LiPo Battery to the LilyPad ProtoSnap Plus](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/InsertBattery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/InsertBattery.jpg)

*An example of inserting a LiPo battery into a JST connector on a different LilyPad board.*

It is safe to leave a LiPo battery attached to the board permanently, even with USB power applied. The battery will not be overcharged.

#### Notes on Washing LilyPad Projects

[ ] LilyPad projects are hand-washable, but **always remove the battery before washing your project** and air-dry your project for several days before replacing the battery.

#### Removing the LiPo Battery

The battery connector can be tight; to remove a battery never pull on the wires. Use a pair of needle nose pliers or cutters to gently hold pull the plug out of the connector.

**Tip:** There are two small \"nubs\" on the top of the plastic battery connector that can be shaved off with a hobby knife to make the battery easier to remove.

[ ] Always turn the LilyPad off before inserting or removing a battery.

Below is an image of the a LiPo battery being removed from a different LilyPad with needle nose pliers.

[![Removing a LiPo Battery from a LilyPad Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/PliersBattery_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/PliersBattery_1.jpg)

*An example of how to remove a LiPo battery from the JST connector on a different LilyPad board.*

## Troubleshooting

### Common Arduino Compile Error Message

Not working as expected? Don\'t worry, it happens to us all. Sometimes things do not go as planned even though you followed the guide. This section highlights a few possible errors that you may encounter when trying to upload code to the LilyPad Development Board.

------------------------------------------------------------------------

#### Error 1: avrdude: stk500_getsync(): not in sync

If you get an error message at the bottom of the Arduino IDE like the following:

    avrdude: stk500_getsync(): not in sync: resp=0x00
    avrdude: stk500_disable(): protocol error, expect=0x14, resp=0x51

or

    avrdude: stk500_recv(): programmer is not responding
    avrdude: stk500_getsync() attempt 10 of 10: not in sync: resp=0x8c

The error output that you are seeing can be due to a number of reasons.

The value of the \"`sync resp`\" is different and not always the same, so it's hard to say. Here are a few common reasons for the error and possible solutions that are known in our knowledge base:

- You don\'t have the *Board* and *Processor* correctly set.
  - The **Tools \> Board** menu should be set to **LilyPad Arduino** for the board and **ATmega328** as the processor. It should only be set to **LilyPad Arduino w/ ATmega328**.
- *Serial Port* may not be set correctly.
  - If you\'ve got more than one Serial Port listed in the menu, try selecting some of the others.
- Or the drivers didn\'t install properly.

## \* Try unplugging and re-plugging the ProtoSnap in. If it prompts you to [install the drivers](https://learn.sparkfun.com/tutorials/usb-serial-driver-quick-install-), try doing so again. If that still fails, I\'d recommend shooting an email over to our [technical support team](https://www.sparkfun.com/technical_assistance). 

#### Error 2: avrdude: ser_open(): can\'t open device

If you get an error message like the following:

    avrdude: ser_open(): can't open device "\\.\COM15": Access is denied.

- It\'s possible that the wrong COM port was selected.
  - Ensure that the COM port is the same as the FTDI connected to your computer. If not, select the correct COM port.
- It could also mean that there is a bad connection between the LilyPad Arduino Simple and your computer.
  - In this case, the correct COM port was selected on `COM15` but the Lilypad Arduino Simple was not connected physically to the FTDI.

------------------------------------------------------------------------

### More Problems Uploading?

If you still have problems uploading code to the LilyPad Arduino Simple and it is not outlined here, try checking out the troubleshooting section of our [activity guide](https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide/troubleshooting):

[LilyPad Development Board Activity Guide: Troubleshooting](https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide/troubleshooting)

Or you can also try following the link provided at the end of the upload error:

    Problem uploading to board.  See http://www.arduino.cc/en/Guide/Troubleshooting#upload for suggestions.

The link heads over to [Arduino.cc\'s general troubleshooting page](http://www.arduino.cc/en/Guide/Troubleshooting#upload) with a few possible solutions that are not outlined in our guides.