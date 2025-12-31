# Source: https://learn.sparkfun.com/tutorials/si4703-fm-radio-receiver-hookup-guide

## Introduction

**Heads up!** This tutorial was written for **Si4703 FM Tuner Evaluation Board V13 ([WRL-12938](https://www.sparkfun.com/products/12938))**. The 3.3V and GND pins are switched in the new revision. Make sure you connect to the correct pins for power if you are using an older version like V11 ([WRL-10663](https://www.sparkfun.com/products/retired/10663)) or the breakout board.

The [Si4703 FM tuner evaluation breakout board](https://www.sparkfun.com/products/12938) enables you to tune in to FM radio stations, using the Si4703 FM tuner chip from Silicon Laboratories. This IC also works well for filter and carrier detection, and enables data such as the station ID and song name to be displayed to the user.

[![SparkFun FM Tuner Evaluation Board - Si4703](https://cdn.sparkfun.com/r/600-600/assets/parts/9/8/6/6/12938-01.jpg)](https://www.sparkfun.com/sparkfun-fm-tuner-evaluation-board-si4703.html)

### [SparkFun FM Tuner Evaluation Board - Si4703](https://www.sparkfun.com/sparkfun-fm-tuner-evaluation-board-si4703.html) 

[ WRL-12938 ]

This is an evaluation board for the Silicon Laboratories Si4703 FM tuner chip. Beyond enabling you to tune in to FM radio sta...

[ [\$26.50] ]

### Required Materials

You will need the following materials to work on this project.

Keep in mind you will also need standard soldering materials to complete this tutorial, as well as either a set of speakers or headphones with a 3.5mm jack to plug into the Si4703 board.

### Suggested Reading

If you aren\'t familiar with any of the concepts below, check out these links and get caught up before moving ahead with the Si4703.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/using-github-to-share-with-sparkfun)

### Using GitHub to Share with SparkFun 

A simple step-by-step tutorial to help you download files from SparkFun\'s GitHub site, make changes, and share the changes with SparkFun.

[](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v)

### Using the Arduino Pro Mini 3.3V 

This tutorial is your guide to all things Arduino Pro Mini. It explains what it is, what it\'s not, and how to get started using it.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

## Hardware Overview

**Heads up!** This tutorial was written for **Si4703 FM Tuner Evaluation Board V13 ([WRL-12938](https://www.sparkfun.com/products/12938))**. The 3.3V and GND pins are switched in the new revision. Make sure you connect to the correct pins for power if you are using an older version like V11 ([WRL-10663](https://www.sparkfun.com/products/retired/10663)) or the breakout board.\
\

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![version 13](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/Si4703_back_version13_highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/Si4703_back_version13_highlighted.jpg)   [![Version 11](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/10663-03a_SI4703_version11_highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/10663-03a_SI4703_version11_highlighted.jpg)
  *V13*                                                                                                                                                                                                       *V11 (Retired)*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Si4703 Breakout Board breaks out multiple pins from the IC. For the power bus, the 3.3V and GND pins are broken out. Keep in mind that while the IC is tolerant up to 5V, the communication pins are only 3.3V tolerant, and therefore should only be used in 3.3V systems. If you need to use this in a 5V system, check out our tutorial on using [logic level converters](https://learn.sparkfun.com/tutorials/using-the-logic-level-converter).

[![Back of Si4703 Breakout Board](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/Si4703_back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/Si4703_back.jpg)

*Underside of breakout board showing pin labels*

For communication, the breakout board provides access to SDIO and SCLK for I^2^C communication. The RST pin is also broken out for ease of resetting the module.

SEN is also broken out, and enables the user to change the mode of functionality of the IC. SEN is pulled high on the breakout board to enable I^2^C communication as mentioned previously. However, by changing the state of SEN along with SDIO, you can change the mode of functionality between a 3-wire interface and 2-wire interface.

Finally, the last two pins broken out are the GPIO1 and GPIO2 pins. These can be used as general input/output pins, but also can be used for things like the RDS ready, seeking or tuning functions.

The board does not have a built-in antenna on it. However, by using headphones or a 3 foot-long 3.5mm audio cable, the wires will function as an antenna and will therefore negate the need for an external antenna on the board. If you are not planning on using either of these, you will need to modify the board to add in an antenna.

## Hooking Up to an Arduino

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

First, you will need to prepare both the Si4703 board and the Arduino Pro Mini. Solder on the male headers to both boards. You will need headers on both the FTDI header, as well as the pins that you will be connecting to the Si4703.

### Pin Connections

Once you have headers soldered, you will need to use the jumper wires to connect between the Si4703 and the Pro Mini. Remember, we are using a 3.3V Pro Mini to prevent damage to the logic on the Si4703.

**Si4703 → 3.3V Pro Mini**

- GND → GND
- 3.3V → VCC
- SDIO → A4
- SCLK → A5
- RST → D2
- GPIO2 → D3

You will then also need to hook up the Pro Mini to the FTDI board, and connect to your computer over USB.

**Warning!** If you are using a different microcontroller that is 5V, you will need to connect to the [respective I2C pins](https://www.arduino.cc/en/reference/wire), and match the [logic levels](https://learn.sparkfun.com/tutorials/logic-levels). Below is a logic level converter that you could use to connect between SDIO, SCLK, RST, and GPIO2.\
\

[![SparkFun Logic Level Converter - Bi-Directional](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/2/2/12009-06.jpg)](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html)

### [SparkFun Logic Level Converter - Bi-Directional](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html) 

[ BOB-12009 ]

The SparkFun bi-directional logic level converter is a small device that safely steps down 5V signals to 3.3V AND steps up 3....

[ [\$3.95] ]

### Installing the Library

Now that the hardware is hooked up and connected, it\'s time to prepare to upload code. First you need to install the Arduino library into the IDE. If you are unaware how to do this, please check out our tutorial [here](https://learn.sparkfun.com/tutorials/installing-an-arduino-library). You can download the code [here](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/Si4703_Breakout.zip).

Once the library is properly installed, please open up the example sketch labeled \"Si4703_Radio_Test\". Make sure you select the \"Arduino Pro or Pro Mini (3.3V, 8MHz) w/ ATMega328\" under the \"Tools -\> Boards\" heading. Select the proper COM port for your FTDI device under \"Tools -\> Serial Port\". Upload the sketch to the board.

Once you have it uploaded, open up your Serial terminal (either through the Arduino IDE or your favorite terminal program). Open the connection with the settings 9600bps, 8, N, 1, and you should see the following displayed on the terminal.

[![Terminal prompt](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/Si4703_terminal_prompt.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/Si4703_terminal_prompt.png)

You can then choose from any of the options listed. If you initially send the board option \"a\", you should see the following displayed back.

[![Favorite Station](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/favoritestation.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/favoritestation.png)

These favorite stations are pre-determined in the sketch, so feel free to change those to your own favorite stations if you would like.

    else if (ch == 'a')
    
    else if (ch == 'b')
    

Keep in mind you will need to upload the code to the board again to update to the new stations. You can then direct the tuning either up or down, and control the volume of the board. For example, to tune to station 95.7 FM here in Boulder, I sent the commands: u, u, +, +, +, +, +, +, +, +, +, +, +, +, +, u, u, u, u, u, u. This results in the following in the serial terminal.

[![Tuned Radio Station](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/tunedstation.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/tunedstation.png)

For this example, I am using my headphone wire as the anntena. Because of this, I was not necessarily able to receive stations that I often can when I\'m not using a headphone wire as an antenna while connected to my computer ([EMI is so much fun!](https://en.wikipedia.org/wiki/Electromagnetic_interference)). Play around with moving around or using different headphone wires and see how radio reception can change.