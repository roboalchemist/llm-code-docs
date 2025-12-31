# Source: https://learn.sparkfun.com/tutorials/stm32-thing-plus-hookup-guide

## Introduction

What incorporates a high-performance Arm® Cortex®-M4 32-bit RISC core, a full set of DSP instructions, memory protection unit (MPU), high-speed embedded memories, up to 4 Kbytes of backup SRAM, and an extensive range of enhanced I/Os and peripherals? The new [SparkFun STM32 Thing Plus](https://www.sparkfun.com/products/17712) has all this and more in the popular, Feather-compatible Thing Plus form factor.

Let\'s have a look at the details!

[![SparkFun Thing Plus - STM32](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/8/1/5/17712-Sparkfun_Thing_Plus_-_STM32-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-stm32.html)

### [SparkFun Thing Plus - STM32](https://www.sparkfun.com/sparkfun-thing-plus-stm32.html) 

[ DEV-17712 ]

With a 32-bit ARM® Cortex®-M4 RISC core, the SparkFun STM32 Thing Plus brings power and precision to your projects.

[ [\$45.65] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading here for an overview:

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/arm-programming)

### ARM Programming 

How to program SAMD21 or SAMD51 boards (or other ARM processors).

## Hardware Overview

### STM32F405

The STM32 Thing Plus exploits the vast capabilities of STMicroElectronics\' STM32F405 series. This family of ICs uses the ARM 32-bit Cortex M4 CPU to provide high performance, floating point single precision, a full set of DSP instructions, and a memory protection unit that enhances application security. For more information, refer to the [Datasheet](https://cdn.sparkfun.com/assets/4/c/b/0/2/stm32f405rg-1851084.pdf).

Features

- Core: ARM® 32-bit Cortex®-M4 CPU with FPU
- Adaptive real-time accelerator (ART Accelerator™) allowing 0-wait state execution from Flash memory
- Frequency up to 168 MHz
- Memory protection unit
- 210 DMIPS/1.25 DMIPS/MHz (Dhrystone 2.1)
- DSP instructions

[![STM32 Arm Cortex is highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-STM32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-STM32.jpg)

### Power

Power to the STM32 Thing Plus can be supplied either by a single-cell LiPo battery or by USB-C. The STM32 Thing Plus has an onboard **3.3V** regulator, as well as a LiPo battery charging circuit.

[![USBC connector and LiPo battery connector highlighted ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-USBCandBatt.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-USBCandBatt.jpg)

### Qwiic Connector

Our [Qwiic Ecosystem](https://www.sparkfun.com/qwiic) makes sensors pretty much plug and play. The Qwiic connector provides power and I^2^C connectivity simultaneously. In addition, the Thing Plus form factor breaks out the I^2^C functionality to PTH.

[![Qwiic connector is highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-QwiicConnector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-QwiicConnector.jpg)

### Boot and Reset Buttons

In order to upload code to the STM32 Thing Plus, you\'ll need these two buttons to put the board into Boot mode. To enter Boot mode, hold the **Boot** button down, press the **Reset** button (while still holding the **Boot** button), and then release the **Boot** button.

[![Boot and Reset Buttons are highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-BootandReset.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-BootandReset.jpg)

### MicroSD

Want extra storage space? Add a MicroSD card using the slot on the back of the board.

[![MicroSD slot is highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-MicroSD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-MicroSD.jpg)

### Flash

In addition to the STM32\'s internal Flash memory, we\'ve provided an additional (128M-bit) Serial Flash memory.

[![Flash chip is highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-Flash.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/17712-Sparkfun-Thing-Plus-STM32-Flash.jpg)

### Board Dimensions

[![Board Outline and Measurements](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/board_outline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/board_outline.png)

## Assembly Tips

### Headers

The STM32 Thing Plus ships without anything soldered into the header pins \-- ensuring that you can mold the board to best fit your project. To use the chip\'s pins you\'ll need to solder *something* to the I/O and power rail vias broken out to either side of the board.

[] New to soldering? Check out our [Through-Hole Soldering Tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) for a quick introduction!

*What* you solder to the STM32 Thing Plus\'s I/O pins is completely up to you. The header rows are breadboard-compatible, so you may want to solder [male headers](https://www.sparkfun.com/products/116) in.

[![STM32 Thing with male headers soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/STM32_Thing_Plus_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/STM32_Thing_Plus_Tutorial-01.jpg)

*STM32 Thing Plus with soldered male headers.*

Then plug it into the breadboard, hanging the USB and LiPo connectors off the end, and start wiring!

Alternatively, [female headers](https://www.sparkfun.com/products/115) (you may need two separate strips to solder all the pins), [right-angle headers](https://www.sparkfun.com/products/553), or [stranded wire](https://www.sparkfun.com/products/11375) are all good options, depending on your project\'s needs.

## Software Setup and Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Arduino Board Definition

Installation for the STM32 Thing Plus is relatively straight-forward. You will want to install the board definitions via the Arduino Boards manager. Search for ***SparkFun STM32*** and you should see the option for the STM32 Thing Plus show up.

[![Boards Manager with SparkFun STM32 boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/STM32BoardsManagerInstall.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/STM32BoardsManagerInstall.jpg)

For more information on installing boards via the Arduino Board Manager, check out the [add-ons section of our Installing Arduino IDE tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide#board-add-ons-with-arduino-board-manager).

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### Install STM32Cube Programmer Software

In order to work with the STM32 Thing Plus, you\'ll need to install the STM32Cube Programmer. This is an all-in-one multi-OS software tool for programming STM32 products. It primarily provides the driver we need, but you can also program your board using this GUI.

[Get the STM32Cube Programmer Here](https://www.st.com/en/development-tools/stm32cubeprog.html#get-software)

### DFU Bootloader

As of this writing, SparkFun is using the DFU bootloader to upload code to the STM32 Thing Plus. In order to do so, you need to do the following:

- Press and hold down the Boot button
- Press and release the Reset button while continuing to press the Boot button
- Keep pressing the Boot button until the code is uploaded

## Example - Blinky

With the STM32 Arduino core installed, you\'re ready to begin programming. If you haven\'t already, **plug the STM32 Thing Plus into your computer** using a USB-C cable.

Once the board is plugged in, it should be assigned a unique port identifier. On Windows machines, this will be something like `COM#`, and on Macs or Linux computers it will come in the form of `/dev/tty.usbserial-XXXXXX`.

### Select the Board and Port

You\'ll notice that there are quite a few options. Make sure you have the ***Generic STM32F4 Series*** board and ***SparkFun Thing Plus STM32F405*** board part number selected under your **Tools** menus.

The other options are more variable. For this example, you\'ll want to set your selections as you see below.

[![Tools Menu with options selected](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/Tools-BoardInfo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/Tools-BoardInfo.jpg)

### Loading Blink

To make sure your toolchain and board are properly set up, we\'ll upload the simplest of sketches \-- Blink! The builtin LED is perfect for this test. Copy and paste the example sketch below into a fresh Arduino sketch:

    language:c

    void setup()
    

    void loop()
    

With everything setup correctly, hit the upload button.

[] **IMPORTANT** In order to upload code via the DFU Bootloader, you will need to press and hold the *Boot* Button, then press the *Reset* Button, then release the *Reset* Button, then release the *Boot* Button.

Once the code finishes transferring, **open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics)** and set the baud rate to **115200**. You should see `Hello, world!`\'s begin to fly by.

[] **Note:** If the blue LED remains dimly lit, it\'s probably still sitting in the bootloader. After uploading a sketch, you may need to **tap the RST button** to get your STM32 Thing Plus to begin running the sketch.

[![Example serial port output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/2/ResetOutput1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/2/ResetOutput1.png)

You may also notice that when the STM32 boots up it prints out a long sequence of debug messages. These are emitted every time the chip resets \-- always at **115200 baud**.

[![STM32 Thing Plus with blinking LED!](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/STM32-02.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/STM32-02.gif)

## Example - I2C Scanner

The Qwiic Connect Ecosystem makes attaching sensors a breeze. That said, sometimes it\'s nice to be able to scan your I^2^C connections to find out the address of your sensor. That\'s what we\'ll do here!

Grab your STM32 Thing Plus and attach a Qwiic Sensor to the Qwiic port on the Thing Plus like so:

[![Image of STM32 TP and Qwiic sensor attached](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/STM32_Hookup_Guides-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/STM32_Hookup_Guides-04.jpg)

Copy and paste the code below into a new Arduino sketch.

    language:c
    // --------------------------------------
    // I2C Scanner example using Wire1
    //
    //
    // This sketch tests the standard 7-bit addresses
    // Devices with higher bit address might not be seen properly.
    //

    #include <Wire.h>

    TwoWire Wire1(SDA1,SCL1); //Intialize Wire1 class

    void setup()
    

    void loop()
    
        else if (error==4)
            
      }
      if (nDevices == 0)
        Serial.println("No I2C devices found\n");
      else
        Serial.println("done\n");

      delay(5000);           // wait 5 seconds for next scan
    }

Make sure your options are all set up correctly in the *Tools* menu, and make sure you put the Carrier Board into *Boot Mode* in order to upload the code.

- Press and hold down the Boot button
- Press and release the Reset button while continuing to press the Boot button
- Release the Boot button and press the *Upload* button in your Arduino IDE

After uploading, open the Serial Monitor and set the baud to **115200**. You should see something similar to the printout below.

[![GIF of screen monitor showing that the qwiic sensor has been found and address 0x48](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/ScannerFindingTMP117.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/ScannerFindingTMP117.gif)

## Example - Serial UART

Let\'s have a quick look at an example using UART. If you\'re unfamiliar with Serial Output, go ahead and have a look at our [Serial Basic Tutorial](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide).

Grab your MicroMod STM32 Thing Plus board and attach the Serial Basic Rx and Tx pins like so:

[![Hookup image showing Rx connected to Tx and Tx connected to Rx](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/4/STM32_Thing_Plus_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/4/STM32_Thing_Plus_Tutorial-02.jpg)

*Click on the image for a closer view*

Note that the RX pin functionality is D0 and the TX pin functionality is D1.

Copy and paste the code below into a new Arduino sketch.

    language:c
    // --------------------------------------
    // UART example using Serial1
    //
    //
    // This sketch prints "Hello World!" every second
    // using the secondary UART pins D0 and D1.
    //

    HardwareSerial Serial1(D0, D1); //Attach Serial1 to D0 and D1

    void setup() 
      Serial1.println("Goodnight moon!");

    }

    void loop() 

Make sure your options are all set up correctly in the *Tools* menu, and make sure you put your board into *Boot Mode* in order to upload the code.

- Press and hold down the Boot button
- Press and release the Reset button while continuing to press the Boot button
- Release the Boot button and press the *Upload* button in your Arduino IDE

Once your code is uploaded, open up the Serial Monitor attached to your Serial Basic with the baud set to **115200** to see your output!

[![Gif of the serial output printing \"Hello World\" every second](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/SerialOutput.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/2/7/SerialOutput.gif)

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