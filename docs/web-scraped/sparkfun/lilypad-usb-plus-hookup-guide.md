# Source: https://learn.sparkfun.com/tutorials/lilypad-usb-plus-hookup-guide

## Introduction

The [LilyPad USB Plus](https://www.sparkfun.com/products/14631) is a sewable electronics microcontroller that you can use with Arduino. In this tutorial, we\'ll introduce the features of the USB Plus and set up the free Arduino software you\'ll need to upload code to it.

[![Lilypad USB Plus](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/1/0/14631-Lilypad_USB_Plus-01.jpg)](https://www.sparkfun.com/lilypad-usb-plus.html)

### [Lilypad USB Plus](https://www.sparkfun.com/lilypad-usb-plus.html) 

[ DEV-14631 ]

This is the LilyPad USB Plus, a sewable electronics microcontroller board controlled by an ATmega32U4 with the Arduino bootlo...

**Retired**

The USB Plus is available as a standalone board or as part of the [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346) board.

[![LilyPad ProtoSnap Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/2/4/14346-01.jpg)](https://www.sparkfun.com/lilypad-protosnap-plus.html)

### [LilyPad ProtoSnap Plus](https://www.sparkfun.com/lilypad-protosnap-plus.html) 

[ DEV-14346 ]

The LilyPad ProtoSnap Plus is a sewable electronics prototyping board that you can use to explore circuits and programming, t...

[ [\$47.50] ]

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

[] **Note:** For a better look at any of the pictures in this tutorial, click on the image to enlarge them!

## Hardware Overview and Features

The LilyPad USB Plus is an Arduino-compatible microcontroller. It has fourteen sew tabs for connecting components with conductive thread. Four of these tabs are reserved for connecting power and ground of LilyPad sensors and accessory boards, and ten are input/output (I/O). For reference, each sew tab has a nearby label with its name and the pin number it is connected to on the ATmega32U4 chip at its center.

[![LilyPad USB plus with labels for power, ground, and input/output sew tabs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/7/USBPlus_TabLabels.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/USBPlus_TabLabels.png)

**Features:**

- USB port for connecting to a computer.
- Two sets of power (+) and ground (-) sew tabs.
- Built-in RGB LED attached to pins 12 (R), 13 (G), and 14 (B).
- A row of six white LEDs attached to pins 15-20.
- Charging circuit for single-cell (**3.7V**) Lithium-Polymer batteries.

[![Additional SMD LEDs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/LilyPadUSBPlusDetails.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/LilyPadUSBPlusDetails.png)

[ ] **Some of the sew tabs on the LilyPad USB Plus have special functionality:**\
\

- An \'A\' in front of the number denotes a tab that can function as an [analog input](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion). These sew tabs can read sensors that output a varying voltage like the light sensor built into the ProtoSnap Plus.\
  \
- A \'\~\' symbol in front of the number indicates that tab supports [PWM (Pulse Width Modulation) output](https://learn.sparkfun.com/tutorials/pulse-width-modulation). These tabs can output an \"analog\" signal that can be used to vary the brightness on LEDs, etc.

\
**Note:** The \"A\" in front of analog sew tab numbers in your code is optional. However, do not include the \"\~\" symbol for PWM outputs. It is only provided to make it easy for you to check which pins can produce PWM (analog) output and is not used in programming.

### Powering the LilyPad USB Plus

The LilyPad USB Plus can be powered in two ways:

- If you have a USB power source available (a computer, 5V USB wall adapter, USB battery pack, etc.), you can run the board from a USB cable.

- Once sewn into a project, you can easily attach a rechargable Lithium-polymer battery to the board. See [Technical Notes](#battery) section for more information on batteries and charging.

To power up the USB Plus, connect it to your computer using a micro-B USB cable or attach an [E-Textiles Battery](https://www.sparkfun.com/products/13112). Then slide the switch on the right side of the LilyPad USB Plus to the ON position.

[![Switch ON](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/7/TurnOnUSBPlus.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/TurnOnUSBPlus.jpg)

## Setting Up Arduino

[] **WARNING: There are known driver issues on older versions of Windows (7 and 8 specifically).** We are actively working on the issue and expect to have a resolution soon.

**Note:** The LilyPad USB Plus requires **Arduino version 1.8 or higher**. If this is your first time using Arduino, you can install it by following our [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide) tutorial. Otherwise, please make sure to install (or update to) the latest version of Arduino and verify that you are connected to the internet to download the LilyPad USB Plus software add-ons.

When you first install Arduino, it knows how to program a number of \"standard\" Arduino-compatible boards. Since the LilyPad USB Plus is a newer LilyPad microcontroller, you will need to manually add it to this list by following the steps below. You\'ll only have to do this once to add the board to Arduino.

**Note for Linux Users:** If you are installing the LilyPad USB Plus in Linux, this document has some specific notes: <https://github.com/sparkfun/LilyPad_ProtoSnap_Plus/blob/master/Documentation/LinuxInstallation.md>.

### Add SparkFun Boards to Arduino\'s Preferences

Start the Arduino IDE software (version 1.8 or higher) and open the Preferences window by choosing **File** \> **Preferences** from the menu.

Now copy the below text and paste it into the \"Additional Boards Manager URLs\" text box:

    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/master/IDE_Board_Manager/package_sparkfun_index.json

[![Additional Board Manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/PasteBoardURL2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/PasteBoardURL2.png)

**No room?** If there is already a URL in the box, click the button to the right of the box. This will open a window allowing you to paste the URL onto a new line.

[![Additional Board Manager URLs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/PasteBoardURLWindow.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/PasteBoardURLWindow.png)

When you\'re done, click the \"OK\" button.

### Install SparkFun AVR Boards

Next, you\'ll add the LilyPad USB Plus through Arduino\'s Boards Manager Menu. Open the Boards Manager by choosing **Tools** \> **Board** \> **Boards Manager\...** (The Boards Manager option is at the very top of the list of boards; you may need to scroll up to see it.)

[![Board Manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SelectBoardManager2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SelectBoardManager2.png)

When the Boards Manager window opens, it will present a long list of options. Type \"SparkFun\" (without quotes) into the *\"Filter your search\"* box at the top of the window. This will shrink the list down to SparkFun\'s options.

You should see several entries. Look for the one labeled **SparkFun AVR Boards by SparkFun Electronics**.

[![SparkFun AVR Boards by SparkFun Electronics GUI](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SearchSparkFun1_8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SearchSparkFun1_8.png)

**Troubleshooting:** If you don\'t see a SparkFun entry, it may mean that the URL you pasted into the Additional Boards Manager section of Arduino\'s preferences did not load correctly in Step #1, or you\'re not connected to the internet. Double check that the entire link was copied into the Additional Boards Manager URLs, and that you\'re connected to the internet. You might also try closing and restarting the Arduino software to refresh the preferences.

Click anywhere in the **SparkFun AVR Boards** box. A version number and an \"Install\" button will appear. Click the install button. This will download and install the extension. If you have already installed the SparkFun AVR Boards support, update to the latest version (LilyPad USB Plus is included in 1.1.8 and higher).

[![Select the Install Version](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SelectInstallVersion1_8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SelectInstallVersion1_8.png)

If everything worked, a blue \"INSTALLED\" note should appear next to the SparkFun AVR Boards title. You\'re ready to start programming.

[![Confirm the Install](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/ConfirmInstall1_8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/ConfirmInstall1_8.png)

## Uploading Code

Once you\'ve installed the LilyPad USB Plus extensions to Arduino, you\'re ready to start programming the board!

Note that you *won\'t* have to install the extensions again, but you *will* need to perform the below three steps every time you want to program the board. These three steps are:

1\. Connect the LilyPad USB Plus to your computer using a USB cable\
2. Select **\"LilyPad USB Plus\"** from Arduino\'s **\"Board\"** menu\
3. Select **\"LilyPad USB Plus\"** from Arduino\'s **\"Port\"** menu

Let\'s go over the three steps in detail:

### 1. Connect the LilyPad USB Plus to Your Computer

Place the LilyPad USB Plus on a clean, non-metal work surface. Connect the LilyPad USB Plus to a USB port on your computer using a micro-B USB cable. The cable can only be inserted one way, and should snap in securely.

[![USB Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/7/PlugInUSBPlus.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/PlugInUSBPlus.jpg)

**Tip:** Both the micro-B USB cable and the connector on the LilyPad have a subtle \"D\" shape to them. Match this shape to plug it in properly.

[![Connected to computer\'s USB port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/7/USBPlus_Laptop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/USBPlus_Laptop.jpg)

Slide the switch on the LilyPad USB Plus to the ON position. You will not be able to upload code to the board if it is set to the OFF position.

[![Turn LilyPad USB Plus on](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/7/TurnOnUSBPlus.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/TurnOnUSBPlus.jpg)

### 2. Select LilyPad USB Plus from the Board Menu

If the Arduino board support was installed correctly, \"LilyPad USB Plus\" option will be available in the **Tools** \> **Board** list under the SparkFun AVR Boards group. Open the menu and select **LilyPad USB Plus**. Depending on how many boards are already in the list, you may need to scroll down a bit to get to it. A dot (Windows) or check mark (Mac) will show next to the board in the menu when it is selected, and it will show next to Board in the Tools menu.

**IMPORTANT:** You\'ll see some LilyPad entries higher in the Arduino menu, but the **LilyPad USB Plus** is not one of them. You\'ll need to scroll down to the SparkFun section at the bottom of the list to find it. We\'re working on getting the LilyPad USB Plus added to the LilyPad group in the future.

[![Select Board Definition](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/SelectBoardArrow.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/SelectBoardArrow.png)

**Troubleshooting:** If you don\'t see \"LilyPad USB Plus\" in the board list, go back to [Setting Up Arduino](https://learn.sparkfun.com/tutorials/lilypad-usb-plus-hookup-guide#setting-up-arduino) and double check that you performed all the steps. You might try restarting Arduino as well.

### 3. Select LilyPad USB Plus from the Port Menu

Arduino needs to know which port your LilyPad USB Plus is attached to so it can program it. Whenever you plug a USB device into your computer, your computer will assign it a port number. This used to be difficult to determine, but this board has a handy feature that identifies itself. Go to the **Tools** \> **Port** menu, and select the port that has \"LilyPad USB Plus\" next to it.

On Windows, ports are listed as COM##; on a Mac or Linux machine they will be \"/dev/cu.usbmodem####\". Your screen may look different than the image below, depending on what operating system you are using, but all should show LilyPad USB Plus next to the port address.

[![COM Port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/7/SelectSerialPort1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/SelectSerialPort1.png)

**Troubleshooting:** If you don\'t see a port with \"LilyPad USB Plus\" next to it, ensure that the board is powered up (switch in the ON position), and that the USB cable is securely connected to both the board and your computer. Some micro-USB cables are only meant for charging and don\'t pass data - they\'ll power the board, but it won\'t show up in the port menu. If needed, try a different cable.

### Uploading Code

To review, once you\'ve:

1.  Connected the LilyPad USB Plus to your computer using a USB cable.
2.  Selected the board type (\"**LilyPad USB Plus**\" **NOT** \"*LilyPad Arduino USB*\").
3.  Selected the COM port.

You are ready to upload code! Let\'s upload some code to try it out:

Load the \"Blink\" example from the menu **File** \> **Examples** \> **01.Basics** \> **Blink**. This is a very simple example program; it just blinks a LED on and off once per second.

[![Blink Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/OpenBlinkExample.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/OpenBlinkExample.png)

Click the \"Upload\" button (the large round button with the right arrow in it).

[![Upload Button](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/ClickUpload.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/ClickUpload.png)

Arduino will compile the code, then send it to the LilyPad USB Plus via the USB cable. While the code is uploading, the built-in LED will blink to signal the code is transferring. When the code finally runs, the RGB LED at the center of the board will slowly blink green. Success!

If this all works, congratulations! You\'re all set up and ready to prototype with the LilyPad USB Plus.

### Troubleshooting: Error Messages on Upload?

If you are using a Mac and get an error message like the following:

    Board LilyPad USB Plus (platform avr, package SparkFun) is unknown

It is possible that old Arduino versions left over after updates are interfering with the LilyPad USB Plus support installation. If you want to clear out this old information, follow these steps:

[ ] **WARNING:** The following instructions will delete any extensions you\'ve previously applied to Arduino, returning it to its factory-default state. It should not delete any sketches that you\'ve created.

1.  Open Arduino\'s \"Preferences\" window.
2.  At the bottom of the window will be a link to your preferences file. Click on it and it will open a finder window.
3.  In the finder window, look for an \"Arduino15\" folder and delete it.
4.  Now open a finder window and open your personal folder (the one with your login name and a house icon next to it). Look for an \"Arduino\" folder (possibly in \"Documents\"). If the \"Arduino\" folder contains a \"Hardware\" folder, delete it. Your Arduino installation is now clean. Restart Arduino and repeat the LilyPad installation instructions from the previous page.

### Troubleshooting: Still Problems Uploading?

If you still have problems uploading code to the LilyPad USB Plus and they are not outlined here, try checking out the troubleshooting section of our [activity guide](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/troubleshooting):

[LilyPad Protosnap Plus Activity Guide: Troubleshooting](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/troubleshooting)

## Stitching Into a Project

As you plan your project and prototype your code, you can use alligator clips to connect individual LilyPad pieces to the USB Plus and test them before building into a project.

The connections you\'ve planned using alligator clips or a sketch of your circuit can then be recreated with conductive thread by stitching the components in your project once you are finished prototyping. If you\'d like to continue to refine your code after sewing into your project, make sure to leave the USB connector accessible.

[![Sew LilyPad Components](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/ProtoSnapSew.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/ProtoSnapSew.jpg)

These tutorials will give you some tips and tricks for project construction and insulation:

[](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles)

### Insulation Techniques for e-Textiles 

Learn a few different ways to protect your conductive thread and LilyPad components in your next wearables project.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

## Technical Notes

If you are already familiar with programming Arduino for a while, read on for some additional notes about the LilyPad USB Plus. It\'s similar to other Arduinos, but has some special features and limitations you\'ll want to know about.

### [][Using a Battery and Battery Charging](#battery)

SparkFun sells a number of LiPo batteries compatible with this board. If you are new to the LilyPad system, we recommend the [E-Textiles Battery](https://www.sparkfun.com/products/13112). If you\'re supplying your own battery, use a single-cell (**3.7V**) LiPo battery with a JST connector.

Batteries with larger capacities (measured as amp-hours or Ah) will run the board longer before needing recharging. How long will depend on how many LEDs your program turns on, etc. If you\'re just running a few LEDs, you can expect the board to run about 5 hours for every 100mAh of battery capacity.

#### Charge Rate

To recharge an attached battery, plug the board into a USB power source.

[![Inserting a battery into the LilyPad USB Plus](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/7/USBPlusLipo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/USBPlusLipo.jpg)

While the battery is charging, the \"CHG\" LED will illuminate. When the battery is fully charged the LED will turn off. The default charge current is set to **100mA**, so a 100mAh battery will recharge in one hour, a 1000mAh battery in 10 hours, etc. Since the board is set to charge at a rate of 100mA, we do not recommend connecting a lower capacity LiPo battery (i.e. 40mAh LiPo battery) to charge.

[![Location of CHG LED](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/USBPlus_ChgLED1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/USBPlus_ChgLED1.png)

*Location of the \"CHG\" LED*

It is safe to leave a LiPo battery attached to the board permanently, even with USB power applied. The battery will not be overcharged.

#### Notes on Washing LilyPad Projects

[ ] LilyPad projects are hand-washable, but **always remove the battery before washing your project** and air-dry your project for several days before replacing the battery.

#### Removing the LiPo Battery

The battery connector can be tight; to remove a battery never pull on the wires. Use a pair of needle nose pliers or cutters to gently hold pull the plug out of the connector.

**Tip:** There are two small \"nubs\" on the top of the plastic battery connector that can be shaved off with a hobby knife to make the battery easier to remove.

[ ] Always turn the LilyPad off before inserting or removing a battery.

[![Using needle nose pliers to help move the plastic battery connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/7/USBPlus_RemoveLipo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/7/USBPlus_RemoveLipo.jpg)

### Pin Numbering

Below is a list of the LilyPad USB Plus I/O pins and each function.

**Legend:**

- *n* = digital pin\
- \~*n* = PWM-capable pin\
- A*n* = analog-capable pin\
- (*n*) = internal pin (not connected to sew tab)\
- \[*n*\] = internal pin (available on an exposed via)\

  Function          Digital   Analog
  ----------------- --------- --------
  RX_LED            \(0\)     
  RX_LED/SS         \(1\)     
                    2         A2
                    3         A3
                    4         A4
                    5         A5
                    \~6       
                    \~7       A7
                    \~8       A8
                    9         A9
  SCL               \~10      
  SDA               11        
  RGB LED - Red     (\~12)    
  RGB LED - Green   (\~13)    
  RGB LED - Blue    (\~14)    
  Bar Graph LED 0   \(15\)    
  Bar Graph LED 1   \(16\)    
  Bar Graph LED 2   \(17\)    
  Bar Graph LED 3   \(18\)    
  Bar Graph LED 4   \(19\)    
  Bar Graph LED 5   \(20\)    
  SCLK              \[21\]    
  MOSI              \[22\]    
  MISO              \[23\]