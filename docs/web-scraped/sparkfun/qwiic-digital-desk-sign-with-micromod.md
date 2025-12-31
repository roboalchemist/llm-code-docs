# Source: https://learn.sparkfun.com/tutorials/qwiic-digital-desk-sign-with-micromod

## Introduction

\"Where\'s Bobby?\" A question that comes up when at work. While I\'m usually at my desk, there are times that I need to walk away for lunch, take a 15-minute break, head into a meeting, or check inventory. To help notify others of where I may be, I made the Qwiic-enabled digital desk sign using the SAMD51\'s USB host and a USB keyboard to type short custom messages while I am away!

[![Qwiic Digital Desk Sign with MicroMod](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign_MicroMod_SAMD51_Host_USB_Keyboard_Message.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign_MicroMod_SAMD51_Host_USB_Keyboard_Message.jpg)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun 20x4 SerLCD - RGB Backlight (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/2/4/16398-SparkFun_16x2_SerLCD_-_RGB_Backlight__Qwiic_-05.jpg)](https://www.sparkfun.com/sparkfun-20x4-serlcd-rgb-backlight-qwiic.html)

### [SparkFun 20x4 SerLCD - RGB Backlight (Qwiic)](https://www.sparkfun.com/sparkfun-20x4-serlcd-rgb-backlight-qwiic.html) 

[ LCD-16398 ]

The SparkFun Qwiic SerLCD is a serial enabled LCD that provides a simple and cost effective solution for adding a 20x4 Black ...

[ [\$42.95] ]

[![SparkFun USB Type A Female Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/9/4/4/0/12700-01.jpg)](https://www.sparkfun.com/sparkfun-usb-type-a-female-breakout.html)

### [SparkFun USB Type A Female Breakout](https://www.sparkfun.com/sparkfun-usb-type-a-female-breakout.html) 

[ BOB-12700 ]

This simple board breaks out a female USB type A connector\'s VCC, GND, D- and D+ pins to a 0.1\" pitch header. If you want to ...

[ [\$5.25] ]

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Reversible USB A to C Cable - 0.3m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/5/15426-Reversible_USB_A_to_C_Cable_-_0.3m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-3m.html)

### [Reversible USB A to C Cable - 0.3m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-3m.html) 

[ CAB-15426 ]

These 0.3m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the...

[ [\$5.50] ]

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![SparkFun MicroMod ATP Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/1/2/16885-SparkFun_MicroMod_ATP_Carrier_Board-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html)

### [SparkFun MicroMod ATP Carrier Board](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html) 

[ DEV-16885 ]

If you need a \"lot\" of GPIO with a simple to program, ready to go to market module, the ATP is the fix you need.

[ [\$20.50] ]

[![SparkFun MicroMod SAMD51 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/8/16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html)

### [SparkFun MicroMod SAMD51 Processor](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html) 

[ DEV-16791 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun MicroMod SAMD51 Processor Board is one powerful microcontroller packaged on a ...

[ [\$18.95] ]

### You Will Also Need

**Note:** Not all keyboards are compatible. The code used in this tutorial was tested on the following keyboards listed below. We found that the *Logitech K400 Plus Wireless Touch Keyboard* was not compatible with this project.

You will also need a USB keyboard. The following keyboards were tested.

- Dell KB216t
- Logitech K120

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

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

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Hook-up Wire - Black (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/2/08022-01.jpg)](https://www.sparkfun.com/hook-up-wire-black-22-awg.html)

### [Hook-up Wire - Black (22 AWG)](https://www.sparkfun.com/hook-up-wire-black-22-awg.html) 

[ PRT-08022 ]

Standard 22 AWG solid Black hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes ...

[ [\$3.25] ]

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

[![Hook-up Wire - Yellow (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/4/08024-01a.jpg)](https://www.sparkfun.com/hook-up-wire-yellow-22-awg.html)

### [Hook-up Wire - Yellow (22 AWG)](https://www.sparkfun.com/hook-up-wire-yellow-22-awg.html) 

[ PRT-08024 ]

Standard 22 AWG solid Yellow hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes...

[ [\$3.25] ]

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/6/6/15220_-_Wire_Strippers_-_20-30AWG.jpg)](https://www.sparkfun.com/products/15220)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/15220) 

[ TOL-15220 ]

These are higher grade wire strippers from Jonard Industries with a comfortable, curved grip making them an affordable option...

**Retired**

### Suggested Reading

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/micromod). We recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)   [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*                                                                                                                                        *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend checking out these tutorials before continuing. If you are using a Qwiic PIR motion sensor with the project, you could also look at its associated tutorial.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide)

### AVR-Based Serial Enabled LCDs Hookup Guide 

The AVR-based Qwiic Serial Enabled LCDs are a simple and cost effective solution to include in your project. These screens are based on the HD44780 controller, and include ATmega328P with an Arduino compatible bootloader. They accept control commands via Serial, SPI and I2C (via PTH headers or Qwiic connector). In this tutorial, we will show examples of a simple setup and go through each communication option.

[](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide)

### MicroMod SAMD51 Processor Board Hookup Guide 

This tutorial covers the basic functionality of the MicroMod SAMD51 and highlights the features of the ARM Cortex-M4F development board.

[](https://learn.sparkfun.com/tutorials/micromod-all-the-pins-atp-carrier-board)

### MicroMod All The Pins (ATP) Carrier Board 

Access All The Pins (ATP) of the MicroMod Processor Board with the Carrier Board!

[](https://learn.sparkfun.com/tutorials/qwiic-pir-hookup-guide)

### Qwiic PIR Hookup Guide 

Get started passively monitoring motion using the Panasonic EKMC and EKMB sensors with the SparkFun Qwiic PIR.

## Hardware Assembly

If you have not already, make sure to check out the [Getting Started with MicroMod: Hardware Hookup](https://learn.sparkfun.com/tutorials/getting-started-with-micromod#hardware-hookup) for information on inserting your Processor Board to your Carrier Board.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

October 21, 2020

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

Your board should look like the image below after connecting the MicroMod SAMD51 Processor Board to the MicroMod ATP. To program, insert the USB-C cable.

[![Processor Board inserted into Carrier Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/1/1/MicroMod_ATP_SAMD51_Processor_Board.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/1/1/MicroMod_ATP_SAMD51_Processor_Board.jpg)

Since the SAMD51 uses the USB connector for USB host, we\'ll [strip](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-strip-a-wire) and [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) wires to the board to connect an external 5V wall adapter.

[![Solder Wire to 5V and GND](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/MicroMod_ATP_Solder_Wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/MicroMod_ATP_Solder_Wires.jpg)

Then we\'ll strip the other end of the wires and insert them into a female barrel jack adapters with \"**+**\" to VIN and \"**−**\" to GND. We\'ll secure the wires by twisting them together.

[![Wires Inserted into Barrel Jack with Screw Terminals](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/MicroMod_SAMD51_Connect_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/MicroMod_SAMD51_Connect_USB.jpg)

Due to the design of the MicroMod SAMD51\'s host pins, we\'ll need to solder another USB Type A connector breakout to the ATP\'s host pins using male headers. If you have an adapter to convert the USB Type C to Type A, you can also use that as well.

[![Solder Header Pins to USB Breakout Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/Solder_USB_A_Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/Solder_USB_A_Headers.jpg)

While I could solder the breakout directly to the ATP\'s host pins, I decided to solder female headers to the board to be able to easily disconnect the USB keyboard.

[![Solder Female Header Pins to ATP Carrier Board\'s USB Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/Solder_USB_MicroMod_ATP.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/Solder_USB_MicroMod_ATP.jpg)

Add a Qwiic cable between the Qwiic SerLCD and MicroMod\'s Qwiic connector labeled as **I2C**

[![Qwiic Cable Between ATP Carrier Board and 20x4 RGB Character LCD](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/MicroMod_SAMD51_Connect_Connect_SerLCD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/MicroMod_SAMD51_Connect_Connect_SerLCD.jpg)

Insert a keyboard to the USB breakout board.

[![Insert Keyboard into USB breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/MicroMod_SAMD51_Connect_Connect_Keyboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/MicroMod_SAMD51_Connect_Connect_Keyboard.jpg)

When you have finished programming the SAMD51, you can insert a 5V wall adapter for power.

[![5V Wall Adapter connected to Barrel Jack for Power](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign_MicroMod_SAMD51_Connect_Power_Supply.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign_MicroMod_SAMD51_Connect_Power_Supply.jpg)

⚡ **Warning!** When programming your SAMD51 MicroMod, make sure to disconnect the 5V adapter to avoid conflicting voltages with the USB port.

To save power and the screen, you can also add a PIR motion sensor or distance sensor to toggle the screen on and off. An additional Qwiic cable and Qwiic PIR motion sensor was added between the MicroMod ATP and Qwiic SerLCD.

[![Qwiic PIR Motion Sensor Added to Setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign__MicroMod_PIR_Motion_Sensor_LCD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign__MicroMod_PIR_Motion_Sensor_LCD.jpg)

The 20x40 SerLCD was hard to see any messages with it flat on a table so a panel was eventually cut out from a SparkFun cardboard box to mount the project. for the scope of this tutorial, won\'t go over the specifics of cutting the cardboard in this tutorial or mounting the electronics to the panel.

[![Cardboard panel to mount the electronics](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign__MicroMod_Cardboard_Panel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign__MicroMod_Cardboard_Panel.jpg)

## Arduino Example Code

**Note:** If this is your first time using Arduino IDE or board add-on, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library/whats-a-library)

The example code can be found in the following [GitHub repository](https://github.com/bboyho/Qwiic_Digital_Desk_Sign_with_MicroMod). The example includes the original host keyboard code from Arduino. The code was modified to work with a 20x4 SerLCD and eventually the 16x2. To save power and the screen, the code was further modified to be used with the Qwiic PIR motion sensor in order to toggle the RGB LED and screen. For the scope of this project tutorial, we will be using examples 1b and 2.

[GitHub: Qwiic Digital Desk Sign with MicroMod](https://github.com/bboyho/Qwiic_Digital_Desk_Sign_with_MicroMod)

### Arduino SAMD Board Add-Ons

Since we are using the SAMD51, you will need to install the board add-on. Head over to the tutorial for instructions on installing the board definitions.

[](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide)

### MicroMod SAMD51 Processor Board Hookup Guide 

October 21, 2020

This tutorial covers the basic functionality of the MicroMod SAMD51 and highlights the features of the ARM Cortex-M4F development board.

### Additional Libraries

If you are using the Qwiic PIR motion sensor, make sure to download and install the library as [stated in its tutorial](https://learn.sparkfun.com/tutorials/qwiic-pir-hookup-guide#qwiic-pir-arduino-library).

[](https://learn.sparkfun.com/tutorials/qwiic-pir-hookup-guide)

### Qwiic PIR Hookup Guide 

March 25, 2021

Get started passively monitoring motion using the Panasonic EKMC and EKMB sensors with the SparkFun Qwiic PIR.

The Arduino Library Manager is the easiest way to install the library. Open the Library Manager, search for \"**SparkFun Qwiic PIR Arduino Library**\" and click the \"Install\" button to download the latest version. If you prefer manually installing the library from the [GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_PIR_Arduino_Library), you can download it here:

[Download the Qwiic PIR Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_PIR_Arduino_Library/archive/master.zip)

## Example 1b: Qwiic Digital Desk Sign

If you are using an external 5V wall adapter, make sure to disconnect it before inserting the USB C cable to your computer\'s COM port to upload the project\'s code. Let\'s upload a project\'s sketch to the board. Copy and paste the following code in the Arduino IDE. Head to **Tools** \> **Board** to select the correct board definition (in this case, **SparkFun MicroMod SAMD51**. Select the correct COM port that the board enumerated to. Hit upload.

    language:c
    /******************************************************************************
      Host Keyboard Controller with Qwiic Serial LCD 16x2 and 20x4
      Date Modified: 5 Aug 2021
      Modified by
      Ho Yun "Bobby" Chan
      Keyboard Controller Code Originally created 8 Oct 2012
      by Cristian Maglie

      ========== DESCRIPTION==========

      This project code takes input from a USB keyboard with
      the SAMD51's USB host pins and outputs characters to
      the Qwiic RGB Serial Enabled LCD 20x4. Leave a message
      behind as you walk away from your desk!

      Note: Not all keyboards are compatible. This code was tested on the following
      keyboards.

          - Dell KB216t
          - Logitech K120

      This example also builds off the example from Arduino which
      originally showed the output of a USB Keyboard connected to
      the Native USB port on an Arduino Due (SAMD21) Board.

      http://arduino.cc/en/Tutorial/KeyboardController

      This code is part of the public domain.

    ******************************************************************************/

    #include <KeyboardController.h> // Require keyboard control library
    #include <Wire.h> //Needed for I2C to SerLCD

    #define SerLCD_Address 0x72  //If using SerLCD with I2C
    #define SERIAL_PORT_MONITOR Serial1 //debug via hardware UART pins

    //assuming that we are using a SerLCD 20x4 screen
    //these variables keep track of cursor location
    int row = 0;
    int remappedRow = row;
    int column = 0;

    //depending on what screen you are using, we are counting 0 as well
    //int maxRow = 1;     // for 16x2
    int maxRow = 3;        //for 20x4
    //int maxColumn = 15; // for 16x2
    int maxColumn = 19;    //for 20x4

    boolean rgb_backlight = true; //used for function keys to immediately turn on/off backlight
    boolean blink_box = true; //used to keep track of blink box as a "cursor"

    //values to keep track of rgb backlight
    int rVal = 157; //128 = Off, 157 = 100%
    int gVal = 187; //158 = Off, 187 = 100%
    int bVal = 217; //188 = Off, 217 = 100%

    //values used to turn off rgb in Power Save Mode
    int rVal_OFF = 128;
    int gVal_OFF = 158;
    int bVal_OFF = 188;

    int lcdContrast = 40; //used to keep track of contast: Range is 255 to 0, 40 is default

    // Initialize USB Controller
    USBHost usb;

    // Attach keyboard controller to USB
    KeyboardController keyboard(usb);

    //boolean capsLock = false; //used to keep track of capsLock, this is not used in this code
    boolean numLock = false; //display numbers if numLock on, we'll assume that the keyboard resets every time so it's off by default

    // This function intercepts key press
    void keyPressed() 

    // This function intercepts key release
    void keyReleased() 

    void printKey() ' with Shift
          49 = '\' or '|' with Shift
          51 = ';' or ':' with Shift
          52 = `'` or '"' with Shift
          53 = '`' or '~' with Shift
          54 = ',' or '<' with Shift
          55 = '.' or '>' with Shift
          56 = '/' or '?' with Shift

          CURSOR CONTROL D-PAD (US LAYOUT)
          79 = `→` (e.g. right)
          80 = `←` (e.g. left)
          81 = `↓` (e.g. down)
          82 = `↑` (e.g. up)

          NUMERIC KEYPAD (US LAYOUT), NUMLOCK MUST BE ENABLED
          83 = 'NumLock'
          84 = '/'
          85 = '*'
          86 = '-'
          87 = '+'
          88 = 'Enter'
          89 = 'End'             or '1' w/ NumLock
          90 = '↓' (e.g. down)   or '2' w/ NumLock
          91 = 'Page Down'       or '3' w/ NumLock
          92 = '←' (e.g. left)   or '4' w/ NumLock
          93 =                      '5' w/ NumLock
          94 = '→' (e.g. right)  or '6' w/ NumLock
          95 = 'Home'             or '7' w/ NumLock
          96 = '↑' (e.g. up)      or '8' w/ NumLock
          97 = 'Page Up'          or '9' w/ NumLock
          98 = 'Insert'           or '0' w/ NumLock
          99 = 'Delete'           or '.' w/ NumLock

          OTHER
          41 = 'Escape'
          73 = 'Insert'
          74 = 'Home'
          75 = 'Page Up'
          76 = 'Delete'
          77 = 'End'
          78 = 'Page Down'

          FUNCTION KEYS
          58 = `F1`
          59 = `F2`
          60 = `F3`
          61 = `F4`
          62 = `F5`
          63 = `F6`
          64 = `F7`
          65 = `F8`
          66 = `F9`
          67 = `F10`
          68 = `F11`
          69 = `F12`

      */

      //----------TYPEWRITER AND KEYPAD KEYS (QWERTY, US LAYOUT) ----------
      if ((tempKey >= 4 && tempKey <= 39) ||
          (tempKey >= 44 && tempKey <= 49) ||
          (tempKey >= 51 && tempKey <= 56) ||
          (tempKey >= 84 && tempKey <= 87) ||
          ((tempKey >= 89 && tempKey <= 97) && numLock == true) ||
          tempKey == 73 ||
          tempKey == 98 ||
          (tempKey == 99 && numLock == true)) 
        else if ((tempKey == 49) && (mod == 0)) 
        else if ( (tempKey == 53) && ((mod == 2) || (mod == 32)) ) 
        else if (tempKey == 73) 
        else if (tempKey == 98 && numLock == false) 
        else 

        //after typing the cursor will move automatically to
        //next position so let's keep track of it
        if (column < maxColumn) 
        else 
          else 
        }

        //remap according to SerLCD's line number
        if (row == 0) 
        else if (row == 1) 
        else if (row == 2) 
        else if (row == 3) 

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission

      }

      /*NOTE: These keys move the cursor so it is kept
        as separate condition statements. We will
        also include most of the numLock keys when 'NUMLOCK'
        is disabled.*/
      else if ((tempKey >= 79 && tempKey <= 82) ||
               tempKey == 40 ||
               tempKey == 74 ||
               tempKey == 77 ||
               tempKey == 75 ||
               tempKey == 78 ||
               tempKey == 83 ||
               tempKey == 88 ||
               ((tempKey >= 89 && tempKey <= 97) && numLock == false) ) 

        //----------LEFT KEY----------
        else if ((tempKey == 80) || (tempKey == 92 && numLock == false)) 
          else 
            else 
          }
        }

        //----------RIGHT KEY----------
        else if ( (tempKey == 79) || (tempKey == 94 && numLock == false) ) 
          else 
            else 
          }
        }

        //----------UP KEY----------
        else if ( (tempKey == 82) || (tempKey == 96 && numLock == false) ) 
          else 
        }

        //----------DOWN KEY----------
        else if ( (tempKey == 81) || (tempKey == 90 && numLock == false) ) 
          else 
        }

        //----------ENTER KEY----------
        else if (tempKey == 40 || tempKey == 88) 
          else 
        }

        //----------HOME KEY----------
        else if (tempKey == 74 || (tempKey == 95 && numLock == false) ) 

        //----------END KEY----------
        else if (tempKey == 77 || (tempKey == 89 && numLock == false)) 

        //----------PAGE UP KEY----------
        else if (tempKey == 75 || (tempKey == 97 && numLock == false)) 

        //----------PAGE DOWN KEY----------
        else if (tempKey == 78 || (tempKey == 91 && numLock == false)) 

        else if (tempKey == 93 && numLock == false ) 
          else 

          Wire.endTransmission(); //Stop I2C transmission

        }

        //remap according to SerLCD's line number
        if (row == 0) 
        else if (row == 1) 
        else if (row == 2) 
        else if (row == 3) 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission

      }

      //----------ESCAPE KEY----------
      else if (tempKey == 41) 

      //----------BACKSPACE KEY----------
      else if (tempKey == 42) 
            else 
              else 
            }
          }

          //For backspace, we are replacing the current position
          //with a space. This moves the cursor forward once space
          //To correct this, we are going to move backward twice
          //with the help of the for() loop.
          if (column > 0) 
          else 
            else 
          }

          //remap according to SerLCD's line number
          if (row == 0) 
          else if (row == 1) 
          else if (row == 2) 
          else if (row == 3) 

          Wire.beginTransmission(SerLCD_Address);
          Wire.write(254); //Send command character
          Wire.write(128 + remappedRow + column); //update cursor position
          Wire.endTransmission(); //Stop I2C transmission
          delay(50);

        }//end for() loop for controlling cursor with 'Backspace'
      }//end condition statement for 'Backspace'

      //----------DELETE KEY----------
      else if (tempKey == 76 || (tempKey == 99 && numLock == false) ) 
        else 
          else 
        }

        //move cursor back to where it was
        if (column > 0) 
        else 
          else 
        }

        //remap according to SerLCD's line number
        if (row == 0) 
        else if (row == 1) 
        else if (row == 2) 
        else if (row == 3) 

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission

      }//end condition statement for 'Delete'

      else if (tempKey == 58) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(rVal); //Update red value
        Wire.endTransmission(); //Stop I2C transmission

      }

      else if (tempKey == 59) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(rVal); //Update red value
        Wire.endTransmission(); //Stop I2C transmission
      }

      else if (tempKey == 60) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(gVal); //Update green value
        Wire.endTransmission(); //Stop I2C transmission

      }

      else if (tempKey == 61) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(gVal); //Update green value
        Wire.endTransmission(); //Stop I2C transmission

      }

      else if (tempKey == 62) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(bVal); //Update blue value
        Wire.endTransmission(); //Stop I2C transmission
      }

      else if (tempKey == 63) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(bVal); //Update blue value
        Wire.endTransmission(); //Stop I2C transmission

      }

      else if (tempKey == 64) 
        else 

        if (rgb_backlight == 0)
        
        else
        

      }

      else if (tempKey == 65) 

      else if (tempKey == 66) 
        else 

        Wire.beginTransmission(SerLCD_Address);

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission
        delay(50);//short delay before sending next line

      }

      else if (tempKey == 67) 
        else 

        Wire.beginTransmission(SerLCD_Address);

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission
        delay(50);//short delay before sending next line

      }

      else if (tempKey == 68) 
        else 

        Wire.beginTransmission(SerLCD_Address);

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission
        delay(50);//short delay before sending next line

      }

      else if (tempKey == 69) 
        else 

        Wire.beginTransmission(SerLCD_Address);

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission
        delay(50);//short delay before sending next line

      }

      delay(50); //The maximum update rate of OpenLCD is about 100Hz (10ms). A smaller delay will cause flicker

    }

    //Set Custom Characters for 5x8 Character Position
    //'\'
    //0x0,0x10,0x8,0x4,0x2,0x1,0x0,0x0
    //%0,%10000,%1000,%100,%10,%1,%0,%0
    byte back_slash[8] = ;

    //'~'
    //0x0,0x0,0x0,0x8,0x15,0x2,0x0,0x0
    //%0,%0,%1000,%10101,%10,%0,%0,%0
    byte tilde[8] = ;

    //'♥'
    //0x0,0x0,0xa,0x1f,0x1f,0xe,0x4,0x0
    //%0,%0,%1010,%11111,%11111,%1110,%100,%0
    byte heart[8] = ;

    //'♡'
    //0x0,0x0,0xa,0x15,0x11,0xa,0x4,0x0
    //%0,%0,%1010,%10101,%10001,%1010,%100,%0
    byte empty_heart[8] = ;

    //Given a character number (0 to 7 is valid)
    //Given an 8 byte array
    //Record this data as a custom character to CGRAM
    void loadCustomCharacter(byte charNumber, byte charData[])
    

    //Display a given custom character that was previously loaded into CGRAM
    void printCustomChar(byte charNumber)
    

    void setup() 

    void loop() 

    //Given a number, i2cSendValue chops up an integer into four values and sends them out over I2C
    void i2cSendValue(int value)
    

**Note:** Since we are using the USB pins on the SAMD51 for host mode, you\'ll notice that port will disappear as it is running the sketch. If you need to upload code again to the board, you will need to [hit the reset button twice to enter bootloader mode](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/uf2-bootloader--drivers) in order to upload code to the SAMD51 again.

### What You Should See

Unplug the USB cable from your computer and insert it into the MicroMod ATP\'s host port. Power up the board with the 5V wall adapter. Type a custom message using a USB keyboard to see the output on the Qwiic SerLCD!

[![Message about 15 minute break and when I\'ll be back](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign_Message_MicroMod_SAMD51.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign_Message_MicroMod_SAMD51.jpg)

Use the d-pad to move the cursor around and adjust the message.

[![Gone away to lunch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign_Message_Lunch_MicroMod_SAMD51.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/2/Qwiic_Digital_Desk_Sign_Message_Lunch_MicroMod_SAMD51.jpg)

## Example 2: Qwiic Digital Desk Sign w/ PIR

If you are using an external 5V wall adapter, make sure to disconnect it before inserting the USB C cable to your computer\'s COM port to upload the project\'s code. Let\'s upload a project\'s sketch to the board. Copy and paste the following code in the Arduino IDE. Head to **Tools** \> **Board** to select the correct board definition (in this case, **SparkFun MicroMod SAMD51**. Select the correct COM port that the board enumerated to. Hit upload.

    language:c
    /******************************************************************************
      Host Keyboard Controller with Qwiic Serial LCD and Qwiic PIR
      Date Modified: 5 Aug 2021
      Modified by
      Ho Yun "Bobby" Chan
      Keyboard Controller Code Originally created 8 Oct 2012
      by Cristian Maglie

      ========== DESCRIPTION==========

      This project code takes input from a USB keyboard with
      the SAMD51's USB host pins and outputs characters to
      the Qwiic RGB Serial Enabled LCD 4x20. Leave a message
      behind as you walk away from your desk!

      Note: Not all keyboards are compatible. This code was tested on the following
      keyboards.

          - Dell KB216t
          - Logitech K120

      This example also builds off the example from Arduino which
      originally showed the output of a USB Keyboard connected to
      the Native USB port on an Arduino Due (SAMD21) Board.

      http://arduino.cc/en/Tutorial/KeyboardController

      This code is part of the public domain.

    ******************************************************************************/

    #include <KeyboardController.h> // Require keyboard control library
    #include <SparkFun_Qwiic_PIR.h>
    QwiicPIR pir;

    //#include <Wire.h> //Was needed for I2C to SerLCD and Qwiic PIR but it is defined in the Qwiic PIR library so we comment it out

    #define SerLCD_Address 0x72  //If using SerLCD with I2C
    #define SERIAL_PORT_MONITOR Serial1 //debug via hardware UART pins

    //assuming that we are using a SerLCD 20x4 screen
    //these variables keep track of cursor location
    int row = 0;
    int remappedRow = row;
    int column = 0;

    //depending on what screen you are using, we are counting 0 as well
    //int maxRow = 1;     // for 16x2
    int maxRow = 3;        //for 20x4
    //int maxColumn = 15; // for 16x2
    int maxColumn = 19;    //for 20x4

    boolean rgb_backlight = true; //used for function keys to immediately turn on/off backlight
    boolean blink_box = true; //used to keep track of blink box as a "cursor"

    //values to keep track of rgb backlight
    int rVal = 157; //128 = Off, 157 = 100%
    int gVal = 187; //158 = Off, 187 = 100%
    int bVal = 217; //188 = Off, 217 = 100%

    //values used to turn off rgb in Power Save Mode
    int rVal_OFF = 128;
    int gVal_OFF = 158;
    int bVal_OFF = 188;

    int lcdContrast = 40; //used to keep track of contast: Range is 255 to 0, 40 is default

    boolean activity = true; //used to keep track of movement or keyboard presses
    const int noActivityMillis = 10000; //used to compare amount of time when no activity to turn of screen
    int currentMillis = 0;  //get time based on how long the Arduino has been running
    int lastActivityMillis = 0;

    // Initialize USB Controller
    USBHost usb;

    // Attach keyboard controller to USB
    KeyboardController keyboard(usb);

    //boolean capsLock = false; //used to keep track of capsLock, this is not used in this code
    boolean numLock = false; //display numbers if numLock on, we'll assume that the keyboard resets every time so it's off by default

    // This function intercepts key press
    void keyPressed() 

    // This function intercepts key release
    void keyReleased() 

    void printKey() ' with Shift
          49 = '\' or '|' with Shift
          51 = ';' or ':' with Shift
          52 = `'` or '"' with Shift
          53 = '`' or '~' with Shift
          54 = ',' or '<' with Shift
          55 = '.' or '>' with Shift
          56 = '/' or '?' with Shift

          CURSOR CONTROL D-PAD (US LAYOUT)
          79 = `→` (e.g. right)
          80 = `←` (e.g. left)
          81 = `↓` (e.g. down)
          82 = `↑` (e.g. up)

          NUMERIC KEYPAD (US LAYOUT), NUMLOCK MUST BE ENABLED
          83 = 'NumLock'
          84 = '/'
          85 = '*'
          86 = '-'
          87 = '+'
          88 = 'Enter'
          89 = 'End'             or '1' w/ NumLock
          90 = '↓' (e.g. down)   or '2' w/ NumLock
          91 = 'Page Down'       or '3' w/ NumLock
          92 = '←' (e.g. left)   or '4' w/ NumLock
          93 =                      '5' w/ NumLock
          94 = '→' (e.g. right)  or '6' w/ NumLock
          95 = 'Home'             or '7' w/ NumLock
          96 = '↑' (e.g. up)      or '8' w/ NumLock
          97 = 'Page Up'          or '9' w/ NumLock
          98 = 'Insert'           or '0' w/ NumLock
          99 = 'Delete'           or '.' w/ NumLock

          OTHER
          41 = 'Escape'
          73 = 'Insert'
          74 = 'Home'
          75 = 'Page Up'
          76 = 'Delete'
          77 = 'End'
          78 = 'Page Down'

          FUNCTION KEYS
          58 = `F1`
          59 = `F2`
          60 = `F3`
          61 = `F4`
          62 = `F5`
          63 = `F6`
          64 = `F7`
          65 = `F8`
          66 = `F9`
          67 = `F10`
          68 = `F11`
          69 = `F12`

      */

      //----------TYPEWRITER AND KEYPAD KEYS (QWERTY, US LAYOUT) ----------
      if ((tempKey >= 4 && tempKey <= 39) ||
          (tempKey >= 44 && tempKey <= 49) ||
          (tempKey >= 51 && tempKey <= 56) ||
          (tempKey >= 84 && tempKey <= 87) ||
          ((tempKey >= 89 && tempKey <= 97) && numLock == true) ||
          tempKey == 73 ||
          tempKey == 98 ||
          (tempKey == 99 && numLock == true)) 
        else if ((tempKey == 49) && (mod == 0)) 
        else if ( (tempKey == 53) && ((mod == 2) || (mod == 32)) ) 
        else if (tempKey == 73) 
        else if (tempKey == 98 && numLock == false) 
        else 

        //after typing the cursor will move automatically to
        //next position so let's keep track of it
        if (column < maxColumn) 
        else 
          else 
        }

        //remap according to SerLCD's line number
        if (row == 0) 
        else if (row == 1) 
        else if (row == 2) 
        else if (row == 3) 

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission

      }

      /*NOTE: These keys move the cursor so it is kept
        as separate condition statements. We will
        also include most of the numLock keys when 'NUMLOCK'
        is disabled.*/
      else if ((tempKey >= 79 && tempKey <= 82) ||
               tempKey == 40 ||
               tempKey == 74 ||
               tempKey == 77 ||
               tempKey == 75 ||
               tempKey == 78 ||
               tempKey == 83 ||
               tempKey == 88 ||
               ((tempKey >= 89 && tempKey <= 97) && numLock == false) ) 

        //----------LEFT KEY----------
        else if ((tempKey == 80) || (tempKey == 92 && numLock == false)) 
          else 
            else 
          }
        }

        //----------RIGHT KEY----------
        else if ( (tempKey == 79) || (tempKey == 94 && numLock == false) ) 
          else 
            else 
          }
        }

        //----------UP KEY----------
        else if ( (tempKey == 82) || (tempKey == 96 && numLock == false) ) 
          else 
        }

        //----------DOWN KEY----------
        else if ( (tempKey == 81) || (tempKey == 90 && numLock == false) ) 
          else 
        }

        //----------ENTER KEY----------
        else if (tempKey == 40 || tempKey == 88) 
          else 
        }

        //----------HOME KEY----------
        else if (tempKey == 74 || (tempKey == 95 && numLock == false) ) 

        //----------END KEY----------
        else if (tempKey == 77 || (tempKey == 89 && numLock == false)) 

        //----------PAGE UP KEY----------
        else if (tempKey == 75 || (tempKey == 97 && numLock == false)) 

        //----------PAGE DOWN KEY----------
        else if (tempKey == 78 || (tempKey == 91 && numLock == false)) 

        else if (tempKey == 93 && numLock == false ) 
          else 

          Wire.endTransmission(); //Stop I2C transmission

        }

        //remap according to SerLCD's line number
        if (row == 0) 
        else if (row == 1) 
        else if (row == 2) 
        else if (row == 3) 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission

      }

      //----------ESCAPE KEY----------
      else if (tempKey == 41) 

      //----------BACKSPACE KEY----------
      else if (tempKey == 42) 
            else 
              else 
            }
          }

          //For backspace, we are replacing the current position
          //with a space. This moves the cursor forward once space
          //To correct this, we are going to move backward twice
          //with the help of the for() loop.
          if (column > 0) 
          else 
            else 
          }

          //remap according to SerLCD's line number
          if (row == 0) 
          else if (row == 1) 
          else if (row == 2) 
          else if (row == 3) 

          Wire.beginTransmission(SerLCD_Address);
          Wire.write(254); //Send command character
          Wire.write(128 + remappedRow + column); //update cursor position
          Wire.endTransmission(); //Stop I2C transmission
          delay(50);

        }//end for() loop for controlling cursor with 'Backspace'
      }//end condition statement for 'Backspace'

      //----------DELETE KEY----------
      else if (tempKey == 76 || (tempKey == 99 && numLock == false) ) 
        else 
          else 
        }

        //move cursor back to where it was
        if (column > 0) 
        else 
          else 
        }

        //remap according to SerLCD's line number
        if (row == 0) 
        else if (row == 1) 
        else if (row == 2) 
        else if (row == 3) 

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission

      }//end condition statement for 'Delete'

      else if (tempKey == 58) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(rVal); //Update red value
        Wire.endTransmission(); //Stop I2C transmission

      }

      else if (tempKey == 59) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(rVal); //Update red value
        Wire.endTransmission(); //Stop I2C transmission
      }

      else if (tempKey == 60) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(gVal); //Update green value
        Wire.endTransmission(); //Stop I2C transmission

      }

      else if (tempKey == 61) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(gVal); //Update green value
        Wire.endTransmission(); //Stop I2C transmission

      }

      else if (tempKey == 62) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(bVal); //Update blue value
        Wire.endTransmission(); //Stop I2C transmission
      }

      else if (tempKey == 63) 
        else 

        Wire.beginTransmission(SerLCD_Address);
        Wire.write('|'); //Put LCD into setting mode
        Wire.write(bVal); //Update blue value
        Wire.endTransmission(); //Stop I2C transmission

      }

      else if (tempKey == 64) 
        else 

        if (rgb_backlight == 0)
        
        else
        

      }

      else if (tempKey == 65) 

      else if (tempKey == 66) 
        else 

        Wire.beginTransmission(SerLCD_Address);

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission
        delay(50);//short delay before sending next line

      }

      else if (tempKey == 67) 
        else 

        Wire.beginTransmission(SerLCD_Address);

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission
        delay(50);//short delay before sending next line

      }

      else if (tempKey == 68) 
        else 

        Wire.beginTransmission(SerLCD_Address);

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission
        delay(50);//short delay before sending next line

      }

      else if (tempKey == 69) 
        else 

        Wire.beginTransmission(SerLCD_Address);

        Wire.write(254); //Send command character
        Wire.write(128 + remappedRow + column); //update cursor position
        Wire.endTransmission(); //Stop I2C transmission
        delay(50);//short delay before sending next line

      }

      delay(50); //The maximum update rate of OpenLCD is about 100Hz (10ms). A smaller delay will cause flicker

    }

    //Set Custom Characters for 5x8 Character Position
    //'\'
    //0x0,0x10,0x8,0x4,0x2,0x1,0x0,0x0
    //%0,%10000,%1000,%100,%10,%1,%0,%0
    byte back_slash[8] = ;

    //'~'
    //0x0,0x0,0x0,0x8,0x15,0x2,0x0,0x0
    //%0,%0,%1000,%10101,%10,%0,%0,%0
    byte tilde[8] = ;

    //'♥'
    //0x0,0x0,0xa,0x1f,0x1f,0xe,0x4,0x0
    //%0,%0,%1010,%11111,%11111,%1110,%100,%0
    byte heart[8] = ;

    //'♡'
    //0x0,0x0,0xa,0x15,0x11,0xa,0x4,0x0
    //%0,%0,%1010,%10101,%10001,%1010,%100,%0
    byte empty_heart[8] = ;

    //Given a character number (0 to 7 is valid)
    //Given an 8 byte array
    //Record this data as a custom character to CGRAM
    void loadCustomCharacter(byte charNumber, byte charData[])
    

    //Display a given custom character that was previously loaded into CGRAM
    void printCustomChar(byte charNumber)
    

    void setup() 

      SERIAL_PORT_MONITOR.println("PIR acknowledged. Waiting 30 Seconds while PIR warms up");
      Wire.beginTransmission(SerLCD_Address);
      Wire.print("Waiting 30 secs for PIR up");
      Wire.endTransmission(); //Stop I2C transmission
      for (uint8_t seconds = 0; seconds < 30; seconds++)
      

      SERIAL_PORT_MONITOR.println("PIR warm!");

      //Use this function call to change the debounce time of the PIR sensor
      //The parameter is the debounce time in milliseconds
      pir.setDebounceTime(500);

      Wire.beginTransmission(SerLCD_Address);
      Wire.write('|'); //Put LCD into setting mode
      Wire.write('-'); //Send clear display command
      Wire.endTransmission(); //Stop I2C transmission
      delay(50); //short delay before sending next line

      Wire.beginTransmission(SerLCD_Address);
      Wire.write('|'); //Send command character
      Wire.write('/'); //disable system messages since current buffer on the SerLCD does not save what is on screen or custom characters correctly
      Wire.endTransmission(); //Stop I2C transmission
      delay(50); //short delay before sending next line

    }

    void loop() 
        activity = false; //reset flag
      }
      else 
        else 
        }
      }

      delay(50);

      // Process USB tasks
      usb.Task();

      //check if there is an available PIR event, and tell us what it is!
      if (pir.available()) 
        if (pir.objectRemoved()) 
        pir.clearEventBits();
      }

    }

    //Given a number, i2cSendValue chops up an integer into four values and sends them out over I2C
    void i2cSendValue(int value)
    

**Note:** Since we are using the USB pins on the SAMD51 for host mode, you\'ll notice that port will disappear as it is running the sketch. If you need to upload code again to the board, you will need to [hit the reset button twice to enter bootloader mode](https://learn.sparkfun.com/tutorials/micromod-samd51-processor-board-hookup-guide/uf2-bootloader--drivers) in order to upload code to the SAMD51 again.

### What You Should See

Unplug the USB cable from your computer and insert it into the MicroMod ATP\'s host port. Power up the board with the 5V wall adapter. You should see something similar to Example 1b. However, the RGB Character LCD turn off whenever there is no activity from the keyboard or motion. This will save a little power as well as grab someone\'s attention when the Character LCD lights up and displays a custom message.

## Making It Better

There's always room for improvement. After the project was completed, I realized that the project could be improved. Below are a list of possible upgrades and improvements that could be implemented for future builds.

- Efficient Arduino Code
  - After the finishing the code to display a message on the serial character LCD, I found out there was also an [SerLCD Arduino Library](https://github.com/sparkfun/SparkFun_SerLCD_Arduino_Library) to control the serial character LCD. The examples used in this tutorial could be updated with latest SerLCD Arduino Library functions to reduce redundancies in the code.
  - I could also create modular function to move the cursor on the serial character LCD to reduce redundancies in code.
  - To make the code more efficient, run slightly faster, and save space on the processor, I could use `#ifdef`\'s use `Serial.print()` only when I am debugging the code. The trade off is that this would create more lines of code. \*The display would react slowly to the button press. Adjusting the delay between each I^2^C transmission and using the SerLCD Arduino Library could increase amount of characters sent to improve the performance.
- More macros to include more predefined messages
  - The predefined messages were limited to just the function keys. I could include more predefined messages by using button combinations.
- Alternative Processors
  - When writing the code, the only processor that had USB host was the MicroMod SAMD51 Processor Board. Now that the MicroMod Teensy Processor Board is available, the code could be modified to use with [PJRC\'s USB Host Library](https://github.com/PaulStoffregen/USBHost_t36), which can has additional keyboard support. There\'s also the MicroMod RP2040 Processor Board also has host support through the [Raspbbery Pi Pico SDK](https://github.com/raspberrypi/pico-examples/tree/f800a7e3031e278062639e070c5764adb4a8a0fc#usb-host).
- Alternative Displays
  - The 16x2 and 20x4 Character LCDs only provide a limited number of characters on the display. Using a [different display from the SparkFun catalog](https://www.sparkfun.com/categories/76) could allow for more space to add longer messages or add intricate animations depending on the type of display.

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)

- USB Keyboard Not Compatible
  - Not all USB keyboards are compatible with the USBHost Arduino Library. Try using a different keyboard. Another alternative is to use the MicroMod Teensy Processor Board, which has additional keyboard support.