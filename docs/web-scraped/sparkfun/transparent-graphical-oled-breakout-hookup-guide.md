# Source: https://learn.sparkfun.com/tutorials/transparent-graphical-oled-breakout-hookup-guide

## Introduction

The future is here! You asked and we delivered - our [Qwiic Transparent Graphical OLED Breakout](https://www.sparkfun.com/products/15173) allows you to display custom images on a transparent screen using either I^2^C or SPI connections.

With Qwiic connectors it\'s quick (ha ha) and easy to get started with your own images. However, we still have broken out 0.1\"-spaced pins in case you prefer to use a breadboard. Brilliantly lit in the dark and still visible by daylight, this OLED sports a display area of 128x64 pixels, 128x56 of which are completely transparent. Control of the OLED is based on our new HyperDisplay library.

[![SparkFun Transparent Graphical OLED Breakout (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/8/8/15173-SparkFun_Transparent_Graphical_OLED_Breakout__Qwiic_-01a.jpg)](https://www.sparkfun.com/products/15173)

### [SparkFun Transparent Graphical OLED Breakout (Qwiic)](https://www.sparkfun.com/products/15173) 

[ LCD-15173 ]

The SparkFun Qwiic Transparent Graphical OLED Breakout allows you to display custom images on a transparent screen using eith...

**Retired**

The Arduino sketch required to drive this display requires quite a bit of dynamic memory, meaning that it is not going to fit on a smaller controller like an ATmega328. Any controller with larger RAM should have no problem. In this tutorial, we\'re using the [ESP32 Thing Plus](https://www.sparkfun.com/products/14689).

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything, depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

If you want to use the broken out GPIO pins along the bottom of the board, you\'ll need to solder some headers to them so you\'ll need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: text-center                                                                                                                                     |
| [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic) |
| :::                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide)

### ESP32 Thing Plus Hookup Guide 

Hookup guide for the ESP32 Thing Plus (Micro-B) using the ESP32 WROOM\'s WiFi/Bluetooth system-on-chip in Arduino.

[](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay)

### Everything You Should Know About HyperDisplay 

This is a tutorial to go in-depth about the SparkFun HyperDisplay Arduino Library.

## Hardware Overview

Let\'s check out some of the characteristics of the Qwiic we\'re dealing with, so we know what to expect out of the board.

  **Characteristic**   **Range**
  -------------------- --------------------------
  Operating Voltage    **1.65V-3.3V**
  Supply Current       **400 mA**
  I^2^C Addresses      **0x3C (Default)**, 0x3D

### Graphical Display

The graphical display is where all the fun stuff happens. The glass itself measures 42mm x 27.16mm, with a pixel display that is 35.5 x 18mm. It houses 128x64 pixels, 128x56 of which are transparent.

[![Display Screen](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/GraphicalDisplay1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/GraphicalDisplay1.jpg)

*Graphical Display*

### Qwiic Connectors

There are two Qwiic connectors on the board such that you can daisy-chain the boards should you choose to do so. If you\'re unfamiliar with our Qwiic system, head on over to our [Qwiic page](https://www.sparkfun.com/qwiic) to see the advantages!

[![Qwiic Connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/QwiicConnectors1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/QwiicConnectors1.jpg)

*Qwiic Connectors*

### GPIO Pins

When you look at the GPIO pins, you\'ll notice that the labels are different from one side to the other. One side is labeled for I^2^C, the other side is labeled for SPI.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/GPIOPinsFront1.jpg "I<sup>2</sup>C Pins")](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/GPIOPinsFront1.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/15173-GPIOBackCorrected.jpg "SPI Pins")](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/15173-GPIOBackCorrected.jpg)\

  *I^2^C Labels*                                                                                                                                                                    *SPI Labels*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Power LED

This bad boy will light up when the board is powered up correctly.

[![Power LED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/PowerLED1.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/PowerLED1.jpg)

*Power LED*

You can disable the power LED by cutting the LED jumpers on the back of the board.

[![Power LED Jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/15173-LEDJumper.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/15173-LEDJumper.jpg)

*Power LED Jumpers*

### JPX Jumpers

The JPX jumpers are used to either change the I^2^C address or configure the board to use SPI communications. The other two jumpers allow you to disconnect the power LED and to disconnect the I^2^C pull-up resistors when chaining several Qwiic devices.

  **Jumper**   **Function**
  ------------ -------------------------------------------------------------------------------------------------------------------------------
  JP1          Holds the Chip Select line low when closed. Close for I^2^C, open for SPI
  JP2          Selects the address in I^2^C mode. Closed for **0x30 by default** and open for 0x31. Open for SPI mode to release the D/C pin
  JP3          Used to select I^2^C or SPI mode. Close for I^2^C, open for SPI
  JP4          This jumper should be closed for I^2^C and open for SPI. This connection allows SDA to be bi-directional

[![JP1-JP4](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/JPJumpersBackCorrected.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/JPJumpersBackCorrected.jpg)

*JPX Jumpers*

### I^2^C Pull-Up Jumper

I^2^C devices contain open drains so we include resistors on our boards to allow these devices to pull pins high. This becomes a problem if you have a large number of I^2^C devices chained together. If you plan to daisy chain more than a few Qwiic boards together, you\'ll need to [cut this I^2^C pull-up jumper](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces#cutting-a-trace-between-jumper-pads).

[![I2C Pullup jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/15173-I2CPUJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/15173-I2CPUJumper.jpg)

*I^2^C PU Jumpers*

## Hardware Hookup

Now that you know what\'s available on your breakout board we can check out the options for connecting it to the brains of your project. There are two options to use - either I^2^C or SPI - and they each have their own advantages and drawbacks. Read on to choose the best option for your setup.

**⚡ Reminder!** This breakout can only handle up to **3.3V** on the pins, so make sure to do some [**level shifting**](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide) if you\'re using a 5V microcontroller.

### I^2^C (Qwiic)

The easiest way to start using the Transparent Graphical OLED is to use a [Qwiic Cable](https://www.sparkfun.com/products/15081) along with a Qwiic compatible microcontroller (such as the [ESP32 Thing Plus](https://www.sparkfun.com/products/14689)). You can also use the [Qwiic Breadboard Cable](https://www.sparkfun.com/products/14425) to attach any I^2^C capable microcontroller, or take the scenic route and [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) in all the I^2^C wires to the plated-through connections on the board.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connector](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/1/2/QwiicConnectors1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/QwiicConnectors1.jpg)   [![I2C Pinout](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/1/2/GPIOPinsFront.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/GPIOPinsFront.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

So why use I^2^C? It\'s easy to connect with the Qwiic system, and you can put up to two of the Transparent Graphical Breakouts on the same bus without using any more microcontroller pins. That simplicity comes at a cost to performance though. The maximum clock speed of the I^2^C bus is 400 kHz, and there is additional overhead in data transmission to indicate which bytes are data and which are commands. This means that the I^2^C connection is best for showing static images.

  **Breakout Pin**   **Microcontroller Pin Requirements**
  ------------------ ---------------------------------------------------------------------------
  GND                Ground pin. Connect these so the two devices agree on voltages
  3V3                3.3V supply pin, capable of up to 400 mA output
  SDA                SDA - the bi-directional data line of your chosen I2C port
  SCL                SCL - the clock line of your chosen I2C port
  SA0                *Optional* : change the I2C address of the breakout. Make sure to cut JP2
  RST                *Optional* : reset the breakout to a known state by pulsing this low

### SPI

SPI solves the I^2^C speed problems. With SPI there is a control signal that indicates data or command and the maximum clock speed is 10 MHz \-- giving SPI 50x more speed! However, it doesn\'t have the same conveniences of the polarized Qwiic connector and low pin usage. You\'ll need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) to the pins.

[![SPI Pinout](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/1/2/15173-GPIOBackCorrected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/15173-GPIOBackCorrected.jpg)

You can use SPI to connect as many breakouts as you want. For N displays you will need to use at least N + 3 data pins. That\'s because the MOSI, SCLK, and D/C pins can be shared between displays but each breakout needs its own dedicated Chip Select (CS) pin.

  **Breakout Pin**   **Microcontroller Pin Requirements**
  ------------------ ----------------------------------------------------------------
  CS                 A GPIO pin, set low when talking to the breakout
  D/C                A GPIO pin, indicates if bytes are data or commands
  SCLK               The clock output of your chosen SPI port
  MOSI               The data output of your chosen SPI port
  3V3                3.3V supply pin, capable of up to 400 mA output
  GND                Ground pin. Connect these so the two devices agree on voltages

[] Make sure to cut jumpers JP1, JP2, JP3, and JP4 when using SPI mode!\
\

[![Cut Jumpers for SPI Mode](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/15173-CutJumpers.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/15173-CutJumpers.jpg)

## Software Setup and Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Drivers and Board Add-Ons

Depending on your development board, you may need to install drivers and a board add-on. For the scope of this tutorial, we will be using the ESP32 Thing Plus. If you have not already, make sure that you install the drivers and ESP32 Arduino core files as explained in our [ESP32 Thing Plus Hookup Guide](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide#software-setup).

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Installing ESP32 Board Add on Files](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/7/Preferences-hardwareFolderLocation.png)](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide#software-setup)
  *[Software Setup for the ESP32](https://learn.sparkfun.com/tutorials/esp32-thing-plus-hookup-guide#software-setup)*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Arduino Libraries

The software for the Transparent Graphical OLED Breakout is built on the HyperDisplay libraries developed by SparkFun. If you are unfamiliar with how this abstracted library works, head over to our [Everything You Should Know About HyperDisplay](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay) tutorial.

[](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay)

### Everything You Should Know About HyperDisplay 

February 20, 2019

This is a tutorial to go in-depth about the SparkFun HyperDisplay Arduino Library.

HyperDisplay is an abstracted library that requires multiple layers in order to function correctly. For the Transparent Graphical OLED to work, you\'ll need our base [HyperDisplay Library](https://github.com/sparkfun/SparkFun_HyperDisplay), the [HyperDisplay SSD1309 Arduino Library](https://github.com/sparkfun/HyperDisplay_SSD1309_ArduinoLibrary), and the somewhat painfully but informatively named [HyperDisplay UG2856KLBAG01 Arduino Library](https://github.com/sparkfun/HyperDisplay_UG2856KLBAG01_ArduinoLibrary). You can obtain these libraries through the Arduino Library Manager by searching for \"**HyperDisplay Library**\", \"**HyperDisplay SSD1309**\", \"**HyperDisplay Transparent Graphical OLED**\", respectively. You can download the required libraries from their individual GitHub pages or download the following **\*.zip** file that contains all three libraries to manually install:

[SparkFun Transparent Graphical OLED Breakout Libraries (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/SparkFun_Transparent_Graphical_OLED_Breakout_Libraries.zip)

If you are manually downloading the libraries, unzip them and copy all three libraries to your **Arduino** \> **Libraries** folder, wherever that may be located on your machine.

[![Copy the HyperDisplay libraries to your Arduino Libraries folder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/LibsDir.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/LibsDir.png)

*Having a hard time seeing? Click the image for a closer look.*

## Examples

Included in the HyperDisplay_UG2856KLBAG01_ArduinoLibrary are three examples to help you get started using the Transparent Graphical OLED Breakout. If you haven\'t already downloaded the libraries from the afore-mentioned locations, click on the button below to download the library bundle. Unzip and copy it into your **Arduino** \> **Libraries** folder.

[SparkFun Transparent Graphical OLED Breakout Libraries (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/SparkFun_Transparent_Graphical_OLED_Breakout_Libraries.zip)

If you are following along with this tutorial using an ESP32 Thing Plus board (as we are), make sure you set your board definition to **Adafruit ESP32 Feather**.

[![Choose The Adafruit Feather Board Definition](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/BoardDefFeather.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/BoardDefFeather.png)

### Example 1: DisplayTest

The purpose of this example is to act like the \"Hello World\" message for your display. Uploading this sketch will help confirm that you have followed the hardware hookup correctly. The sketch runs through a couple of different display test, beginning with a custom SparkFun logo display.

To show the logo, Owen whipped up a quick python script that looks at a jpg image and writes out, pixel by pixel, a function to make the display. We\'ve included his script and our image here\--have a look! With just a little modification it could be useful in your own application.

[Python Script to Convert Image to Pixel (zip)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/image_to_pixel_py.zip)

To get started, either select **File** \> **Examples** \> **SparkFun HyperDisplay Transparent Graphical OLED Library** \> **Example1_DisplayTest** or copy and paste the code below into a new Arduino window.

    language:c
    /*
      Verify that your Qwiic Transparent Grahical OLED is connected correctly and working.

      By: Owen Lyke
      SparkFun Electronics
      Date: February 26, 2019
      License: MIT. See license file for more information but you can
      basically do whatever you want with this code.
      Feel like supporting open source hardware?
      Buy a board from SparkFun! https://www.sparkfun.com/products/15173

      The graphics library is like a 3-layer cake. Here they are from top-down
      https://github.com/sparkfun/SparkFun_HyperDisplay
      https://github.com/sparkfun/HyperDisplay_SSD1309_ArduinoLibrary
      https://github.com/sparkfun/HyperDisplay_UG2856KLBAG01_ArduinoLibrary

      Hardware Compatibility
        - The IO pins on this board are designed for use with 3.3V so if you are using a 5V microcontroller
          please use a level shifter. Note: Qwiic connectors on SparkFun dev boards are already at 3.3V
        - This display relies on a copy of graphics data in your microcontroller, a total of 1024 bytes. 
          That is half the RAM available on an Uno so it is easy to run into sinister low-memory related
          bugs. We reccomend using a micro with more memory like a SAMD21, Esp32, Teensy, etc.

      Hardware Connections:
      Option 1 (I2C):
        Connect using a Qwiic jumper if you have a Qwiic compatible board and you plan to use I2C

      Option 2 (SPI):
        Connect SCLK and MOSI to the SPI port of your choice (13 and 11 for SPI on Uno-like boards) 
        Also connect D/C and CS to two unused GPIO pins of your choice (and set the proper pin definitions below)
        Don't forget power - connect 3.3V and GND
    */

    #include "HyperDisplay_UG2856KLBAG01.h"   // Your library can be installed here: http://librarymanager/All#SparkFun_Transparent_Graphical_OLED
                                              // The rest of the Layer Cake:         http://librarymanager/All#SparkFun_HyperDisplay_SSD1309
                                              //                                     http://librarymanager/All#SparkFun_HyperDisplay
    //////////////////////////
    //      User Setup      //
    //////////////////////////
    #define SERIAL_PORT Serial  
    #define WIRE_PORT Wire      // Used if USE_SPI == 0
    #define SPI_PORT SPI        // Used if USE_SPI == 1

    #define RES_PIN 2           // Optional
    #define CS_PIN 4            // Used only if USE_SPI == 1
    #define DC_PIN 5            // Used only if USE_SPI == 1

    #define USE_SPI 1           // Choose your interface. 0 = I2C, 1 = SPI

    // END USER SETUP

    // Object Declaration. A class exists for each interface option
    #if USE_SPI
      UG2856KLBAG01_SPI myTOLED;  // Declare a SPI-based Transparent OLED object called myTOLED
    #else
      UG2856KLBAG01_I2C myTOLED;  // Declare a I2C-based Transparent OLED object called myTOLED
    #endif /* USE_SPI */

    void setup() 

    void loop() 

    void lineTest( void )
    

      for(hd_hw_extent_t indi = 0; indi < myTOLED.yExt; indi+=5)
      

      for(hd_hw_extent_t indi = 0; indi < myTOLED.xExt; indi+=5)
      

      for(hd_hw_extent_t indi = 0; indi < myTOLED.yExt; indi+=5)
      
    }

    void rectTest( void )
    

      for(uint8_t indi = 0; indi < myTOLED.yExt/2; indi+=1)
      

      for(uint8_t indi = 0; indi < myTOLED.yExt/2; indi+=1)
      
    }

    void circleTest( void )
    
      myTOLED.circleSet((myTOLED.xExt/2 - 1),(myTOLED.yExt/2 - 1), myTOLED.xExt/2, true);
    }

    #if !defined(__AVR_ATmega328P__) && !defined(__AVR_ATmega168__)
    void showLogo( void )
      delay(5000);
      for(uint8_t indi = 255; indi > 1; indi--)
      
      myTOLED.setContrastControl(0);
      myTOLED.clearDisplay();
      myTOLED.setContrastControl(128);
    }
    #endif

Once you\'ve uploaded the code to your board successfully, you should see something like the GIF below:

[![Example 1 GIF](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/SparkFun_Transparent_Graphical_OLED_Breakout__Qwiic__Hookup_Guide.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/SparkFun_Transparent_Graphical_OLED_Breakout__Qwiic__Hookup_Guide.gif)

If you have a look at the `showLogo` function, you\'ll see that the SparkFun logo is calculated and drawn out pixel by pixel. This was calculated using the image_to_pixel python script above. The image is drawn this way due to memory limitations in some Arduino boards. Perhaps not the most efficient way to do this, but it does the trick.

You\'ll also notice that the comments in this example are sparse - this example is intended to get you up and running and show you that the OLED works. The next example is where we will more thoroughly demonstrate how to make your own application with the drawing functions.

### Example 2: DrawingBasics

This example shows some of the basic functions for drawing shapes, including line, rectangle, circle, and polygon. Once uploaded, you should notice different shapes showing up on your transparent OLED. Either select **File** \> **Examples** \> **SparkFun HyperDisplay Transparent Graphical OLED Library** \> **Example2_DrawingBasics** or copy and paste the code below into a new Arduino window.

    language:c
    /*
      Take a guided tour of the basic capabilities of the Transparent Graphical OLED

      By: Owen Lyke
      SparkFun Electronics
      Date: February 27, 2019
      License: MIT. See license file for more information but you can
      basically do whatever you want with this code.
      Feel like supporting open source hardware?
      Buy a board from SparkFun! https://www.sparkfun.com/products/15173

      The graphics library is like a 3-layer cake. Here they are from top-down
      https://github.com/sparkfun/SparkFun_HyperDisplay
      https://github.com/sparkfun/HyperDisplay_SSD1309_ArduinoLibrary
      https://github.com/sparkfun/HyperDisplay_UG2856KLBAG01_ArduinoLibrary

      Hardware Compatibility
        - The IO pins on this board are designed for use with 3.3V so if you are using a 5V microcontroller
          please use a level shifter. Note: Qwiic connectors on SparkFun dev boards are already at 3.3V
        - This display relies on a copy of graphics data in your microcontroller, a total of 1024 bytes. 
          That is half the RAM available on an Uno so it is easy to run into sinister low-memory related
          bugs. We reccomend using a micro with more memory like a SAMD21, Esp32, Teensy, etc.

      Hardware Connections:
      Option 1 (I2C):
        Connect using a Qwiic jumper if you have a Qwiic compatible board and you plan to use I2C

      Option 2 (SPI):
        Connect SCLK and MOSI to the SPI port of your choice (13 and 11 for SPI on Uno-like boards) 
        Also connect D/C and CS to two unused GPIO pins of your choice (and set the proper pin definitions below)
        Don't forget power - connect 3.3V and GND
    */

    #include "HyperDisplay_UG2856KLBAG01.h"   // Your library can be installed here: http://librarymanager/All#SparkFun_Transparent_Graphical_OLED
                                              // The rest of the Layer Cake:         http://librarymanager/All#SparkFun_HyperDisplay_SSD1309
                                              //                                     http://librarymanager/All#SparkFun_HyperDisplay
    //////////////////////////
    //      User Setup      //
    //////////////////////////
    #define SERIAL_PORT Serial  
    #define WIRE_PORT Wire      // Used if USE_SPI == 0
    #define SPI_PORT SPI        // Used if USE_SPI == 1

    #define RES_PIN 2           // Optional
    #define CS_PIN 4            // Used only if USE_SPI == 1
    #define DC_PIN 5            // Used only if USE_SPI == 1

    #define USE_SPI 0           // Choose your interface. 0 = I2C, 1 = SPI

    // END USER SETUP

    // Object Declaration. A class exists for each interface option
    #if USE_SPI
      UG2856KLBAG01_SPI myTOLED;  // Declare a SPI-based Transparent OLED object called myTOLED
    #else
      UG2856KLBAG01_I2C myTOLED;  // Declare a I2C-based Transparent OLED object called myTOLED
    #endif /* USE_SPI */

    void setup() ;
      hd_extent_t y[] = ;
      uint8_t numSides = sizeof(x)/sizeof(hd_extent_t);
      myTOLED.polygonSet(x, y, numSides);               // Make a polygon with numSides at the x, y coordinate pairs
      //  myTOLED.polygonClear(x, y, numSides);
    }

    void loop() 

[![Example Two Display](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/2/SparkFun_Transparent_Graphical_OLED_Breakout__Qwiic__Hookup_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/SparkFun_Transparent_Graphical_OLED_Breakout__Qwiic__Hookup_Guide-06.jpg)

Although **Example2** is detailed in how to use the drawing functions, it falls short in explaining one thing; specifically the options you have when creating and beginning the `myTOLED` object. When creating the object you can choose either the `_I2C` or the `_SPI` suffix to the name of the class (UG2856KLBAG01). That of course changes the intended communication protocol.

If you\'re using Qwiic, choose I^2^C. The interface decision also impacts your use of the `begin()` function by changing which parameters are expected. For I^2^C, you can specify an Arduino \'Wire\' object to use, which I^2^C address to use, and a pin to use to select the I^2^C address.

For I^2^C, all parameters have defaults so it works to just use `myTOLED.begin();` For SPI, the first two arguments are required but the third (which allows you to choose which SPI port to use) can be left out (e.g. `myTOLED.begin(CS_PIN, DC_PIN);`).

### Example 3: AdvancedFeatures

This example has some serious Mario goalz. When you upload this, you\'ll see Mario jumping up and down and eventually landing on a pipe. Either select **File** \> **Examples** \> **SparkFun HyperDisplay Transparent Graphical OLED Library** \> **Example3_AdvancedFeatures** or copy and paste the code below into a new Arduino window.

    language:c
    /*
      Take a guided tour of the basic capabilities of the Transparent Graphical OLED

      By: Owen Lyke
      SparkFun Electronics
      Date: February 28, 2019
      License: MIT. See license file for more information but you can
      basically do whatever you want with this code.
      Feel like supporting open source hardware?
      Buy a board from SparkFun! https://www.sparkfun.com/products/15173

      The graphics library is like a 3-layer cake. Here they are from top-down
      https://github.com/sparkfun/SparkFun_HyperDisplay
      https://github.com/sparkfun/HyperDisplay_SSD1309_ArduinoLibrary
      https://github.com/sparkfun/HyperDisplay_UG2856KLBAG01_ArduinoLibrary

      Hardware Compatibility
        - The IO pins on this board are designed for use with 3.3V so if you are using a 5V microcontroller
          please use a level shifter. Note: Qwiic connectors on SparkFun dev boards are already at 3.3V
        - This display relies on a copy of graphics data in your microcontroller, a total of 1024 bytes. 
          That is half the RAM available on an Uno so it is easy to run into sinister low-memory related
          bugs. We reccomend using a micro with more memory like a SAMD21, Esp32, Teensy, etc.

      Hardware Connections:
      Option 1 (I2C):
        Connect using a Qwiic jumper if you have a Qwiic compatible board and you plan to use I2C

      Option 2 (SPI):
        Connect SCLK and MOSI to the SPI port of your choice (13 and 11 for SPI on Uno-like boards) 
        Also connect D/C and CS to two unused GPIO pins of your choice (and set the proper pin definitions below)
        Don't forget power - connect 3.3V and GND
    */

    #include "HyperDisplay_UG2856KLBAG01.h"   // Your library can be installed here: http://librarymanager/All#SparkFun_Transparent_Graphical_OLED
                                              // The rest of the Layer Cake:         http://librarymanager/All#SparkFun_HyperDisplay_SSD1309
                                              //                                     http://librarymanager/All#SparkFun_HyperDisplay
    //////////////////////////
    //      User Setup      //
    //////////////////////////
    #define SERIAL_PORT Serial  
    #define WIRE_PORT Wire      // Used if USE_SPI == 0
    #define SPI_PORT SPI        // Used if USE_SPI == 1

    #define RES_PIN 2           // Optional
    #define CS_PIN 4            // Used only if USE_SPI == 1
    #define DC_PIN 5            // Used only if USE_SPI == 1

    #define USE_SPI 0           // Choose your interface. 0 = I2C, 1 = SPI

    // END USER SETUP

    // Object Declaration. A class exists for each interface option
    #if USE_SPI
      UG2856KLBAG01_SPI myTOLED;  // Declare a SPI-based Transparent OLED object called myTOLED
    #else
      UG2856KLBAG01_I2C myTOLED;  // Declare a I2C-based Transparent OLED object called myTOLED
    #endif /* USE_SPI */

    void setup() 

    void loop() 

    void moveWindow( int8_t x, int8_t y, wind_info_t* pwind)

    #if !defined(__AVR_ATmega328P__) && !defined(__AVR_ATmega168__)
    void showMario( void )

    void showPipe( void )

    #else
    void showMario( void )

    void showPipe( void )
    #endif

Once you\'ve uploaded the code, you should see a bouncing Mario heading towards the finish line.

[![Mario I2C display](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/SparkFun_Transparent_Graphical_OLED_Breakout__Qwiic__Hookup_Guide_2.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/2/SparkFun_Transparent_Graphical_OLED_Breakout__Qwiic__Hookup_Guide_2.gif)

The \'Advanced Feature\' referenced in this example is the ability to draw in relation to pre-defined \'windows.\' Windows allow you to easily constrain drawing to a particular area or to group related objects. To highlight this fact we made a Mario character with a bunch of hard-coded `pixelSet(x,y)` calls but were able to move him simply by moving the active window and re-drawing. In that case, all the individual pixels that make up Mario were the related objects that we wanted to move together.

One feature not shown in this example is the built-in HyperDisplay text printing. The reason for this is that on, ESP32 boards the `<avr/pgmspace.h>` header is not supported so we can\'t use the default font. However, the printing functions should work on micrcontrollers that both support `<avr/pgmspace.h>` and have enough RAM to be stable. Check out the [HyperDisplay tutorial](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay) for more information on this.