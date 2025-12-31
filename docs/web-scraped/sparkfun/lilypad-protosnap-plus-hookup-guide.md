# Source: https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-hookup-guide

## Introduction

The [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346) is a sewable electronics prototyping board that you can use to learn circuits and programming, then break apart to make an interactive fabric or wearable project. In this tutorial we\'ll introduce the components that make up the ProtoSnap board, and set up the free Arduino software you\'ll need to reprogram the LilyPad USB Plus at its center. Once you\'ve done this, you\'ll be able to write and upload your own programs to the board, making it do almost anything you want.

[![LilyPad ProtoSnap Plus](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/3/2/4/14346-01.jpg)](https://www.sparkfun.com/lilypad-protosnap-plus.html)

### [LilyPad ProtoSnap Plus](https://www.sparkfun.com/lilypad-protosnap-plus.html) 

[ DEV-14346 ]

The LilyPad ProtoSnap Plus is a sewable electronics prototyping board that you can use to explore circuits and programming, t...

[ [\$47.50] ]

At the center of the ProtoSnap Plus is a **LilyPad USB Plus** microcontroller, pre-wired to LilyPad pieces including a LilyPad Light Sensor, [LilyPad Buzzer](https://www.sparkfun.com/products/8463), [LilyPad Button Board](https://www.sparkfun.com/products/8776), four pairs of colored LilyPad LEDs, and a [LilyPad Slide Switch](https://www.sparkfun.com/products/9350). Because these components are connected together on the ProtoSnap board, you can test out your project ideas before you sew. The ProtoSnap Plus also includes **Expansion Ports**; these let you use alligator cables to easily connect external sensors and components to the board. After testing out your coding ideas using the attached LilyPad pieces, you can break apart the board and sew them into your project.

**Warning:** There are known driver issues on older versions of Windows (7 and 8 specifically). We are actively working on the issue and expect to have a resolution soon.

### Required Materials

To reprogram and recharge the board, you\'ll need a micro-B USB cable. This is a common cable used by many devices, so you may already have one. Double check that it is not labeled 'Power Only' as these type of cables will not transmit the programming data needed by the LilyPad USB Plus board. If you don\'t have one you can get one from SparkFun:

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![USB Micro-B Cable - 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/3/0/13244-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6.html)

### [USB Micro-B Cable - 6\"](https://www.sparkfun.com/usb-micro-b-cable-6.html) 

[ CAB-13244 ]

This is a USB 2.0 type A to Micro-B 5-pin black cable. You know, the mini-B connector that usually comes with cell phones, Ca...

[ [\$2.50] ]

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

[ ] **Don't snap apart your LilyPad ProtoSnap Plus** until you\'re ready to use the pieces in a project. If you leave the pieces attached to the board, you\'ll be able to prototype and test your project before you start sewing.

The LilyPad ProtoSnap Plus features twelve LilyPad components connected to a LilyPad microcontroller by conductive pathways called traces. For reference, each component on the ProtoSnap has a nearby label with its name and the number of the LilyPad USB Plus sew tab it is connected to.

[![LilyPad Protosnap Plus parts Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/ProtoSnapPlusPartLabels.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/ProtoSnapPlusPartLabels.png)

### LilyPad USB Plus

The LilyPad USB Plus is an Arduino-compatible microcontroller similar to the [LilyPad Arduino USB - ATmega32U4 Board](https://www.sparkfun.com/products/12049) but with some additional features and three additional sew tabs. It is currently only available on the LilyPad ProtoSnap Plus.

[![Additional SMD LEDs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/LilyPadUSBPlusDetails.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/LilyPadUSBPlusDetails.png)

**Features:**

- USB port for connecting to a computer.
- Two sets of power (+) and ground (-) sew tabs.
- Built-in RGB LED attached to pins 12 (R), 13 (G), and 14 (B).
- A row of six white LEDs attached to pins 15-20.
- Charging circuit for single-cell (3.7V) Lithium-Polymer batteries.

[ ] **Some of the sew tabs on the LilyPad USB Plus have special functionality:**\
\

- An \'A\' in front of the number denotes a tab that can function as an [analog input](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion). These sew tabs can read sensors that output a varying voltage like the light sensor built into the ProtoSnap Plus.\
  \
- A \'\~\' symbol in front of the number indicates that tab supports [PWM (Pulse Width Modulation) output](https://learn.sparkfun.com/tutorials/pulse-width-modulation). These tabs can output an \"analog\" signal that can be used to vary the brightness on LEDs, etc.

\
**Note:** The \"A\" in front of analog sew tab numbers in your code is optional. However, do not include the \"\~\" symbol for PWM outputs. It is only provided to make it easy for you to check which pins can produce PWM (analog) output and is not used in programming.

Below is a table that lists the components connected to the LilyPad USB Plus sew tabs.

LilyPad Component

Connected to LilyPad USB Plus Sew Tab

Description

LilyPad Light Sensor (S)

A2

LilyPad USB Plus receives ambient light level input from light sensor.

LilyPad Buzzer (+)

A3

A buzzer that create tones controlled by LilyPad USB Plus.

LilyPad Button

A4

LilyPad USB Plus receives button press input.

2x LilyPad Y LEDs (+)

A5

A pair of yellow LEDs controlled by LilyPad USB Plus.

2x LilyPad R LEDs (+)

\~6

A pair of red LEDs controlled by LilyPad USB Plus.

2x LilyPad G LEDs (+)

\~A7

A pair of green LEDs controlled by LilyPad USB Plus.

2x LilyPad B LEDs (+)

\~A8

A pair of blue LEDs controlled by LilyPad USB Plus.

LilyPad Switch

A9

LilyPad USB Plus receives switch state (on/off) input to change modes.

Expansion Port A9

A9

Clippable pads to connect another LilyPad piece to. Shares connection with the LilyPad Switch.

Expansion Port (+)

(+)

Clippable pads connected to LilyPad USB Plus\'s power (+) sew tab.

Expansion Port \~10/SCL

\~10/SCL

Clippable pads connected to LilyPad USB Plus\'s sew tab 10. This can be used to connect to a I2C clock pin.

Expansion Port 11/SDA

11/SDA

Clippable pads connected to LilyPad USB Plus\'s sew tab 11. This can be used to connect to a I2C data pin.

Expansion Port (-)

(-)

Clippable pads connected to LilyPad USB Plus\'s ground (-) sew tab.

All components (-)

(-)

All components share a common ground connection back to the LilyPad USB Plus.

### Powering the LilyPad ProtoSnap Plus

The LilyPad ProtoSnap Plus can be powered in two ways:

- If you have a USB power source available (a computer, 5V USB wall adapter, USB battery pack, etc.), you can run the board from a USB cable.

- If you\'d like your project to be more portable, you can easily attach a rechargable Lithium-polymer battery to the board. See [Technical Notes](#battery) section for more information on batteries and charging.

## Exploring the Sample Circuit

[ ] **Don't snap apart your LilyPad ProtoSnap Plus** until you\'re ready to use the pieces in a project. If you leave the pieces attached to the board, you\'ll be able to prototype and test your project before you start sewing.

The LilyPad ProtoSnap Plus ships with pre-loaded code that showcases all of the LilyPad pieces connected to it. To power up the ProtoSnap Plus, connect it to your computer using a micro-B USB cable or attach an [E-Textiles Battery](https://www.sparkfun.com/products/13112). Then slide the switch on the right side of the LilyPad USB Plus to the ON position.

[![Switch ON](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/TurnOnLilyPadSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/TurnOnLilyPadSwitch.jpg)

The board has two modes to choose from: when the LilyPad Slide Switch (the other switch at the bottom right of the board) is turned OFF, all of the LEDs will turn on in sequence. When the LilyPad Slide Switch is turned ON, the white LEDs on the LilyPad USB Plus will form a bar graph showing the ambient light level - move your hand over the Light Sensor to see the level change. And if you press the LilyPad Button (at the bottom left of the board), you\'ll be treated to a short song.

Continue to the [Setting Up Arduino](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-hookup-guide#setting-up-arduino) section for directions on installing the LilyPad USB Plus support for Arduino to enable you to upload your own custom code.

## Using the Expansion Ports

The LilyPad ProtoSnap Plus features five expansion ports connected to sew tabs on the LilyPad USB Plus. These allow you to easily attach external components to the board, including LilyPad and non-LilyPad boards. The expansion ports can accommodate alligator clips, IC clips, and other temporary attachment cables for testing and experimentation. Below are a few ways to connect an alligator cable to the sew tabs.

[![Alligator Clip Parallel to a Sew Tab](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/ClipCable2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/ClipCable2.jpg)

*Alligator clip attached parallel to the expansion port.*

[![Alligator Clip Perpendicular to a Sew Tab](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/ClipCable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/ClipCable.jpg)

*Alligator clip attached perpenticular to the expansion port.*

[![Testing a LilyPad Temperature Sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/ClippingSensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/ClippingSensor.jpg)

*A LilyPad temperature sensor attached to the LilyPad ProtoSnap Plus expansion ports for testing.*

### Using Expansion Port A9

You may have noticed that tab A9 is connected to both the LilyPad Slide Switch and an Expansion Port. You can only use A9 for one of these connections; either the switch as an input or the expansion port as an input/output.

If you\'re using an external component or sensor on expansion port A9, move the slide switch to the OFF position to keep the switch from interfering with your input or output signal.

[![Turn Switch OFF for A9](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/TurnOffSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/TurnOffSwitch.jpg)

Below is an image of the LilyPad temperature sensor attached to the LilyPad ProtoSnap Plus expansion ports for testing.

[![Testing Temperature Sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SensorConnected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SensorConnected.jpg)

For more information about about expansion port A9 in the [Technical Notes](#A9) section.

## Setting Up Arduino

**Note:** The LilyPad ProtoSnap Plus and the LilyPad USB Plus requires **Arduino version 1.8 or higher**. If this is your first time using Arduino, you can install it by following our [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide) tutorial. Otherwise, please make sure to install (or update to) the latest version of Arduino and verify that you are connected to the internet to download the LilyPad USB Plus software add-ons.

[] **WARNING: There are known driver issues on older versions of Windows (7 and 8 specifically).** We are actively working on the issue and expect to have a resolution soon.

Now that you\'ve explored the board\'s features, it\'s time to upload some code! When you first install Arduino, it knows how to program a number of \"standard\" Arduino-compatible boards. Since the LilyPad USB Plus is a newer LilyPad microcontroller, you will need to manually add it to this list by following the steps below. You\'ll only have to do this once to add the board to Arduino.

**Note for Linux Users:** If you are installing the LilyPad ProtoSnap Plus in Linux, this document has some specific notes: <https://github.com/sparkfun/LilyPad_ProtoSnap_Plus/blob/master/Documentation/LinuxInstallation.md>.

### 1. Add SparkFun Boards to Arduino\'s Preferences

Start the Arduino IDE software (version 1.8 or higher) and open the Preferences window by choosing **File** \> **Preferences** from the menu.

Now copy the below text and paste it into the \"Additional Boards Manager URLs\" text box:

    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/master/IDE_Board_Manager/package_sparkfun_index.json

[![Additional Board Manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/PasteBoardURL2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/PasteBoardURL2.png)

**No room?** If there is already a URL in the box, click the button to the right of the box. This will open a window allowing you to paste the URL onto a new line.

[![Additional Board Manager URLs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/PasteBoardURLWindow.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/PasteBoardURLWindow.png)

When you\'re done, click the \"OK\" button.

### 2. Install SparkFun AVR Boards

Next, you\'ll add the LilyPad USB Plus through Arduino\'s Boards Manager Menu. Open the Boards Manager by choosing **Tools** \> **Board** \> **Boards Manager\...** (The Boards Manager option is at the very top of the list of boards; you may need to scroll up to see it.)

[![Board Manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SelectBoardManager2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SelectBoardManager2.png)

When the Boards Manager window opens, it will present a long list of options. Type \"sparkfun\" (without quotes) into the *\"Filter your search\"* box at the top of the window. This will shrink the list down to SparkFun\'s options.

You should see several entries. Look for the one labeled **SparkFun AVR Boards by SparkFun Electronics**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SearchSparkFun1_8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SearchSparkFun1_8.png)

**Troubleshooting:** If you don\'t see a SparkFun entry, it may mean that the URL you pasted into the Additional Boards Manager section of Arduino\'s preferences did not load correctly in Step #1, or you\'re not connected to the internet. Double check that the entire link was copied into the Additional Boards Manager URLs, and that you\'re connected to the internet. You might also try closing and restarting the Arduino software to refresh the preferences.

Click anywhere in the **SparkFun AVR Boards** box. A version number and an \"Install\" button will appear. Click the install button. This will download and install the extension. If you have already installed the SparkFun AVR Boards support, update to the latest version (LilyPad USB Plus and example code is included in 1.1.8 and higher).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SelectInstallVersion1_8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SelectInstallVersion1_8.png)

If everything worked, a blue \"INSTALLED\" note should appear next to the SparkFun AVR Boards title. You\'re ready to start programming.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/ConfirmInstall1_8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/ConfirmInstall1_8.png)

## Uploading Code

Once you\'ve installed the LilyPad USB Plus extensions to Arduino, you\'re ready to start programming the board!

Note that you *won\'t* have to install the extensions again, but you *will* need to perform the below three steps every time you want to program the board. These three steps are:

1\. Connect the LilyPad ProtoSnap Plus to your computer using a USB cable\
2. Select **\"LilyPad USB Plus\"** from Arduino\'s **\"Board\"** menu\
3. Select **\"LilyPad USB Plus\"** from Arduino\'s **\"Port\"** menu

Let\'s go over the three steps in detail:

### 1. Connect the LilyPad ProtoSnap Plus to Your Computer

Place the LilyPad ProtoSnap Plus on a clean, non-metal work surface. Connect the LilyPad ProtoSnap Plus to a USB port on your computer using a micro-B USB cable. The cable can only be inserted one way, and should snap in securely.

[![USB Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/PlugInProtoSnap.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/PlugInProtoSnap.jpg)

**Tip:** Both the micro-B USB cable and the connector on the LilyPad have a subtle \"D\" shape to them. Match this shape to plug it in properly.

[![Connecto to Computer\'s USB Port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/ProtoSnapConnectedtoLaptop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/ProtoSnapConnectedtoLaptop.jpg)

Slide the switch on the LilyPad USB Plus to the ON position. You will not be able to upload code to the board if it is set to the OFF position.

[![Turn LilyPad ProtoSnap Plus ON](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/TurnOnLilyPadSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/TurnOnLilyPadSwitch.jpg)

### 2. Select LilyPad USB Plus from the Board Menu

If the Arduino board support was installed correctly, \"LilyPad USB Plus\" option will be available in the **Tools** \> **Board** list under the SparkFun AVR Boards group. Open the menu and select **LilyPad USB Plus**. Depending on how many boards are already in the list, you may need to scroll down a bit to get to it. A dot (Windows) or check mark (Mac) will show next to the board in the menu when it is selected, and it will show next to Board in the Tools menu.

**IMPORTANT:** You\'ll see some LilyPad entries higher in the Arduino menu, but the **LilyPad USB Plus** is not one of them. You\'ll need to scroll down to the SparkFun section at the bottom of the list to find it. We\'re working on getting the LilyPad USB Plus added to the LilyPad group in the future.

[![Select Board Definition](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SelectBoardArrow.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SelectBoardArrow.png)

**Troubleshooting:** If you don\'t see \"LilyPad USB Plus\" in the board list, go back to [Setting Up Arduino](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-hookup-guide#setting-up-arduino) and double check that you performed all the steps. You might try restarting Arduino as well.

### 3. Select LilyPad USB Plus from the Port Menu

Arduino needs to know which port your LilyPad USB Plus is attached to so it can program it. Whenever you plug a USB device into your computer, your computer will assign it a port number. This used to be difficult to determine, but this board has a handy feature that identifies itself. Go to the **Tools** \> **Port** menu, and select the port that has \"LilyPad USB Plus\" next to it.

On Windows ports are listed as COM##; on a Mac or Linux machine they will be \"/dev/cu.usbmodem####\". Your screen may look different than the image below, depending on what operating system you are using, but all should show LilyPad USB Plus next to the port address.

[![COM Port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SelectSerialPort.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SelectSerialPort.png)

**Troubleshooting:** If you don\'t see a port with \"LilyPad USB Plus\" next to it, ensure that the board is powered up (switch in the ON position), and that the USB cable is securely connected to both the board and your computer. Some micro-USB cables are only meant for charging and don\'t pass data - they\'ll power the board, but it won\'t show up in the port menu. If needed, try a different cable.

### Uploading Code

To review, once you\'ve:

1.  Connected the LilyPad ProtoSnap Plus to your computer using a USB cable.
2.  Selected the board type (\"**LilyPad USB Plus**\" **NOT** \"*LilyPad Arduino USB*\").
3.  Selected the COM port.

You are ready to upload code! Let\'s upload some code to try it out:

Load the \"Blink\" example from the menu **File** \> **Examples** \> **01.Basics** \> **Blink**, and click the \"Upload\" button (the large round button with the right arrow in it). This is a very simple example program; it just blinks a LED on and off once per second.

[![Blink Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/OpenBlinkExample.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/OpenBlinkExample.png)

Arduino will compile the code, then send it to the LilyPad USB Plus via the USB cable. While the code is uploading, the built-in LED will blink to signal the code is transferring. When the code finally runs, the RGB LED at the center of the board will slowly blink green. Success!

If this all works, congratulations! You\'re all set up and ready to prototype with the LilyPad ProtoSnap Plus. Check out our activity guide for more information on writing your own code to prototype for the ProtoSnap Plus:

[](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide)

### LilyPad ProtoSnap Plus Activity Guide 

December 7, 2017

Learn how to program in Arduino with the LilyPad ProtoSnap Plus. This guide includes 10 example activities that use the pre-wired LilyPad boards on the LilyPad ProtoSnap Plus.

### Troubleshooting: Error Messages on Upload?

If you are using a Mac and get an error message like the following:

    Board LilyPad USB Plus (platform avr, package SparkFun) is unknown

It is possible that old Arduino versions left over after updates are interfering with the LilyPad USB Plus support installation. If you want to clear out this old information, follow these steps:

[ ] WARNING: The following instructions will delete any extensions you\'ve previously applied to Arduino, returning it to its factory-default state. It should not delete any sketches that you\'ve created.

1.  Open Arduino\'s \"Preferences\" window.
2.  At the bottom of the window will be a link to your preferences file. Click on it and it will open a finder window.
3.  In the finder window, look for an \"Arduino15\" folder and delete it.
4.  Now open a finder window and open your personal folder (the one with your login name and a house icon next to it). Look for an \"Arduino\" folder (possibly in \"Documents\"). If the \"Arduino\" folder contains a \"Hardware\" folder, delete it. Your Arduino installation is now clean. Restart Arduino and repeat the LilyPad installation instructions from the previous page.

## Stitching Into a Project

Once you are done exploring the parts of the ProtoSnap Plus and prototyping your code, you can snap along the perforations on the board to remove the individual LilyPad pieces and build them into a project.

[![Snap LilyPad Components](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/BreakApartProtoSnap.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/BreakApartProtoSnap.jpg)

Carefully snap the pieces of the ProtoSnap apart to prepare for sewing. Use a set of pliers or diagonal cutters if you are having trouble snapping the pieces apart. Discard the non-sewable pieces and scraps. The conductive pathways on the ProtoSnap can then be recreated with conductive thread by stitching the components in your project.

[![Sew LilyPad Components](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/ProtoSnapSew.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/ProtoSnapSew.jpg)

These tutorials will give you some tips and tricks for project construction and insulation:

[](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles)

### Insulation Techniques for e-Textiles 

Learn a few different ways to protect your conductive thread and LilyPad components in your next wearables project.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

## Technical Notes

If you\'ve already programmed Arduino for a while, read on for some additional notes about the LilyPad ProtoSnap Plus. It\'s very similar to other Arduinos, but has some special features and limitations you\'ll want to know about.

### Pin Numbering

Below is a list of the LilyPad USB Plus I/O pins and each function.

**Legend:**

- *n* = digital pin\
- \~*n* = PWM-capable pin\
- A*n* = analog-capable pin\
- (*n*) = internal pin (not connected to sew tab)\
- \[*n*\] = internal pin (available on an exposed via)\

  Function                  Digital   Analog
  ------------------------- --------- --------
  RX_LED                    \(0\)     
  RX_LED/SS                 \(1\)     
  Light Sensor              2         A2
  Buzzer                    3         A3
  Button                    4         A4
  Yellow LED                5         A5
  Red LED                   \~6       
  Green LED                 \~7       A7
  Blue LED                  \~8       A8
  Switch / Expansion Port   9         A9
  Expansion Port / SCL      \~10      
  Expansion Port / SDA      11        
  RGB LED - Red             (\~12)    
  RGB LED - Green           (\~13)    
  RGB LED - Blue            (\~14)    
  Bar Graph LED 0           \(15\)    
  Bar Graph LED 1           \(16\)    
  Bar Graph LED 2           \(17\)    
  Bar Graph LED 3           \(18\)    
  Bar Graph LED 4           \(19\)    
  Bar Graph LED 5           \(20\)    
  SCLK                      \[21\]    
  MOSI                      \[22\]    
  MISO                      \[23\]    

### [][Expansion Port A9 Notes](#A9)

If you look closely at the ProtoSnap board, you\'ll notice that sew tab A9 is shared between the switch and an expansion port. Because of this, remember: ***if you\'re using the A9 expansion port, ensure that the switch is turned OFF*** to keep the input or output signal from shorting to ground.

[![Switch OFF](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/TurnOffSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/TurnOffSwitch.jpg)

A hard short between power and ground could damage the board. But if you look even closer at the ProtoSnap, you\'ll see a tiny 1K surface-mount resistor in the ground trace connected to the switch. (On the back of the board you\'ll see a zig-zag resistor symbol in that spot.) This resistor prevents hard shorts from power to ground if the switch is ON and you connect a voltage source to the expansion port (or output a HIGH signal from A9).

### [][Using a Battery and Battery Charging](#battery)

SparkFun sells a number of LiPo batteries compatible with this board. If you are new to the LilyPad system, we recommend the [E-Textiles Battery](https://www.sparkfun.com/products/13112). If you\'re supplying your own battery, use a single-cell (3.7V) LiPo battery with a JST connector.

Batteries with larger capacities (measured as amp-hours or Ah) will run the board longer before needing recharging. How long will depend on how many LEDs your program turns on, etc. If you\'re just running a few LEDs, you can expect the board to run about 5 hours for every 100mAh of battery capacity.

#### Charge Rate

To recharge an attached battery, plug the board into a USB power source. While the battery is charging, the \"CHG\" LED will illuminate. When the battery is fully charged the LED will turn off. The default charge current is set to **100mA**, so a 100mAh battery will recharge in one hour, a 1000mAh battery in 10 hours, etc. Since the board is set to charge at a rate of 100mA, we do not recommend connecting a lower capacity LiPo battery (i.e. 40mAh LiPo battery) to charge.

[![Connecting a LiPo Battery to the LilyPad ProtoSnap Plus](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/InsertBattery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/InsertBattery.jpg)

It is safe to leave a LiPo battery attached to the board permanently, even with USB power applied. The battery will not be overcharged.

#### Notes on Washing LilyPad Projects

[ ] LilyPad projects are hand-washable, but **always remove the battery before washing your project** and air-dry your project for several days before replacing the battery.

#### Removing the LiPo Battery

The battery connector can be tight; to remove a battery never pull on the wires. Use a pair of needle nose pliers or cutters to gently hold pull the plug out of the connector.

**Tip:** there are two small \"nubs\" on the top of the plastic battery connector that can be shaved off with a hobby knife to make the battery easier to remove.

[ ] Always turn the LilyPad off before inserting or removing a battery.

[![Remove LiPo Battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/PliersBattery_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/PliersBattery_1.jpg)