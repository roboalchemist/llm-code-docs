# Source: https://learn.sparkfun.com/tutorials/pic-based-serial-enabled-character-lcd-hookup-guide

## Introduction

The [PIC-based serial enabled character LCD (a.k.a. SerLCD) backpack](https://www.sparkfun.com/products/258) is a simple and cost effective solution for interfacing to character Liquid Crystal Displays (LCDs) based on the HD44780 controller. The backpack simplifies the number of wires needed and allows your project to display all kinds of text and numbers.

[![SparkFun Serial Enabled LCD Backpack](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/0/00258-01a.jpg)](https://www.sparkfun.com/products/258)

### [SparkFun Serial Enabled LCD Backpack](https://www.sparkfun.com/products/258) 

[ LCD-00258 ]

The SparkFun Serial Enabled LCD Backpack allows you to control a parallel based LCD over a single-wire serial interface. The ...

**Retired**

The SerLCD backpack can also be found on a variety of serial enabled character LCDs with different color schemes, sizes, and input voltages. In this tutorial, we will connect to a serial enabled LCD and send ASCII characters to the display using an Arduino microcontroller.

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. Depending on what you have, you may not need everything on this list. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49), and screw driver depending on your setup.

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/ascii)

### ASCII 

A brief history of how ASCII came to be, how it\'s useful to computers, and some helpful tables to convert numbers to characters.

[](https://learn.sparkfun.com/tutorials/basic-character-lcd-hookup-guide)

### Basic Character LCD Hookup Guide 

Liquid crystal displays (LCDs) are a great way to output a string of words or sensor data to a display for visual feedback. In this tutorial, we\'ll learn about LCDs, how to print a string of words to a 16x2 basic character LCD and create custom characters.

[] **Note:** Click on any of the images in this tutorial for a closer look!

## Hardware Overview

SerLCD v2.5 has some new features that make the SerLCD even more powerful and economical:

- PIC microcontroller utilizes onboard UART for greater communication accuracy
  - The PIC16LF88 is populated on the SerLCD backpack
  - The PIC16F88 is populated on the built-in serial enabled LCDs
- Adjustable baud rates of 2400, 4800, **9600 (default)**, 14400, 19200 and 38400
- Operational backspace character
- Incoming buffer stores up to 80 characters
- Backlight transistor can handle up to 1A and can be connected to external loads
- Pulse width modulation of backlight allows direct control of backlight brightness and current consumption
- User definable splash screen

### PIC-Based Serial Controller

Using the serial enabled controller, it is easy to connect to any microcontroller that has a serial UART port such as an Arduino, AVR, PIC, etc. The SerLCD supports 16 and 20 character-wide screens with 2 or 4 lines of display.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/SIK_RedBoard_exp_15_01_parallelLCD.jpg "Parallel LCD")](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/SIK_RedBoard_exp_15_01_parallelLCD.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-03_Hello_World_Cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-03_Hello_World_Cropped.jpg)\

  *RedBoard Connected to a Basic Character LCD in Parallel*                                                                                                                                                          *RedBoard Connected to Serial Enabled LCD*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Voltage (VDD) and Logic Levels

Depending on your LCD\'s specs, the input voltage may be 3.3V or 5V. For the LCDs listed below, the input voltage for the backpack must be **3.3V** even though the silkscreen says 5V. The logic levels will be the same as the input voltage.

⚡ **Warning!** When connecting the serial enabled LCD, make sure to connect the input to 3.3V.\
\

[![Basic 16x2 Character LCD - Black on Green 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/1/6/09053-action.jpg)](https://www.sparkfun.com/basic-16x2-character-lcd-black-on-green-3-3v.html)

### [Basic 16x2 Character LCD - Black on Green 3.3V](https://www.sparkfun.com/basic-16x2-character-lcd-black-on-green-3-3v.html) 

[ LCD-09053 ]

This is a 16 character by 2 line display that runs at 3.3V. Utilizes the common ST7066/HD44780 parallel interface (\[datasheet...

[ [\$22.50] ]

[![Basic 16x2 Character LCD - Red on Black 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/1/4/09051-action.jpg)](https://www.sparkfun.com/products/9051)

### [Basic 16x2 Character LCD - Red on Black 3.3V](https://www.sparkfun.com/products/9051) 

[ LCD-09051 ]

This is a 16 character by 2 line display that runs at 3.3V. Utilizes the common ST7066/HD44780 parallel interface (\[datasheet...

**Retired**

[![Basic 16x2 Character LCD - White on Black 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/1/5/09052-Action.jpg)](https://www.sparkfun.com/products/9052)

### [Basic 16x2 Character LCD - White on Black 3.3V](https://www.sparkfun.com/products/9052) 

[ LCD-09052 ]

This is a 16 character by 2 line display that runs at 3.3V. Utilizes the common ST7066/HD44780 parallel interface (\[datasheet...

**Retired**

The following LCDs already have the backpacks installed.\
\

[![SparkFun Serial Enabled 16x2 LCD - Black on Green 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/7/09066_action-01.jpg)](https://www.sparkfun.com/products/9066)

### [SparkFun Serial Enabled 16x2 LCD - Black on Green 3.3V](https://www.sparkfun.com/products/9066) 

[ LCD-09066 ]

The serial enabled LCD allows you to control a parallel based LCD over a single-wire serial interface. Included in this produ...

**Retired**

[![SparkFun Serial Enabled 16x2 LCD - White on Black 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/8/09067_action-01.jpg)](https://www.sparkfun.com/products/9067)

### [SparkFun Serial Enabled 16x2 LCD - White on Black 3.3V](https://www.sparkfun.com/products/9067) 

[ LCD-09067 ]

The serial enabled LCD allows you to control a parallel based LCD over a single-wire serial interface. Included in this produ...

**Retired**

[![SparkFun Serial Enabled 16x2 LCD - Red on Black 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/9/RedonBlack.jpg)](https://www.sparkfun.com/products/9068)

### [SparkFun Serial Enabled 16x2 LCD - Red on Black 3.3V](https://www.sparkfun.com/products/9068) 

[ LCD-09068 ]

The serial enabled LCD allows you to control a parallel based LCD over a single-wire serial interface. Included in this produ...

**Retired**

The LCDs listed below require an input voltage of **5V**. Higher than 5.5V will cause damage to the PIC, LCD, and backlight (if attached). At 5V, the SerLCD uses 3mA with the backlight turned off and \~60mA with the backlight activated. The following LCDs do not have a SerLCD backpack.

[![Basic 16x2 Character LCD - White on Black 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/1/00709-action.jpg)](https://www.sparkfun.com/basic-16x2-character-lcd-white-on-black-5v.html)

### [Basic 16x2 Character LCD - White on Black 5V](https://www.sparkfun.com/basic-16x2-character-lcd-white-on-black-5v.html) 

[ LCD-00709 ]

This is a basic 16 character by 2 line display with a snazzy black background with white characters. Utilizes the extremely c...

[ [\$24.95] ]

[![Basic 16x2 Character LCD - Black on Green 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/7/00255-action.jpg)](https://www.sparkfun.com/basic-16x2-character-lcd-black-on-green-5v.html)

### [Basic 16x2 Character LCD - Black on Green 5V](https://www.sparkfun.com/basic-16x2-character-lcd-black-on-green-5v.html) 

[ LCD-00255 ]

This is a basic 16 character by 2 line display. Black text on Green background. Utilizes the extremely common HD44780 paralle...

[ [\$22.50] ]

[![Basic 16x2 Character LCD - RGB Backlight 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/5/8/9/1/10862-Action_new.jpg)](https://www.sparkfun.com/basic-16x2-character-lcd-rgb-backlight-5v.html)

### [Basic 16x2 Character LCD - RGB Backlight 5V](https://www.sparkfun.com/basic-16x2-character-lcd-rgb-backlight-5v.html) 

[ LCD-10862 ]

This is similar to other 16x2 character LCDs that you\'ve seen before but with one vibrant difference: The backlight is actual...

[ [\$18.95] ]

[![Basic 16x2 Character LCD - Yellow on Blue 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/5/5/6/00790-action.jpg)](https://www.sparkfun.com/products/790)

### [Basic 16x2 Character LCD - Yellow on Blue 5V](https://www.sparkfun.com/products/790) 

[ LCD-00790 ]

This is a basic 16 character by 2 line display with a Blue background and a Yellow backlight. Utilizes the extremely common H...

**Retired**

The following LCDs have a backpack built into the board.\

[![Serial Enabled 16x2 LCD - Red on Black 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/9/7/09394_action-01.jpg)](https://www.sparkfun.com/products/9394)

### [Serial Enabled 16x2 LCD - Red on Black 5V](https://www.sparkfun.com/products/9394) 

[ LCD-09394 ]

This is the latest evolution of our serial LCD. Included on a single board is a 16x2 LCD and an embedded circuit based around...

**Retired**

[![Serial Enabled 16x2 LCD - White on Black 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/9/8/09395_action-01.jpg)](https://www.sparkfun.com/products/9395)

### [Serial Enabled 16x2 LCD - White on Black 5V](https://www.sparkfun.com/products/9395) 

[ LCD-09395 ]

This is the latest evolution of our serial LCD. Included on a single board is a 16x2 LCD and an embedded circuit based around...

**Retired**

[![Serial Enabled 20x4 LCD - Black on Green 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/3/3/4/6/09568Actiona.jpg)](https://www.sparkfun.com/products/9568)

### [Serial Enabled 20x4 LCD - Black on Green 5V](https://www.sparkfun.com/products/9568) 

[ LCD-09568 ]

This is the latest evolution of our serial LCD. Included on a single board is a 20x4 LCD and an embedded circuit based around...

**Retired**

### Contrast Control

The SerLCD and built-in serial LCDs comes equipped with a 10k potentiometer to control the contrast of the LCD. This is set during assembly and testing but may need correcting for your specific LCD module. Temperature and supply voltage can affect the contrast of the LCD. While powered, simply adjust the potentiometer with a screw driver.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/00258-02a_potentiometerLCDContrast.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/00258-02a_potentiometerLCDContrast.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09395-03potentiometerLCDContrast.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09395-03potentiometerLCDContrast.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09568-03apotentiometerLCDContrast.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09568-03apotentiometerLCDContrast.jpg)
  *SerLCD Backpack*                                                                                                                                                                                   *Serial Enabled LCD 16x2*                                                                                                                                                                       *Serial Enabled LCD 20x4*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Hi-Current Control Pin

The SerLCD v2.5 uses a general purpose, 1000mA NPN transistor to control the LCDs backlight. If you purchased the SerLCD module, you may use this pin as a general purpose, high power control pin. If you issue the backlight on/off command to the SerLCD or built-in serial LCD, the BL pin on the board can also be used to power / control other circuits with a maximum current of 1000 mA. This is usually the last pin on the top row of the LCD. Check your datasheet for proper pin outs.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/00258-02a_backlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/00258-02a_backlight.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09395-03backlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09395-03backlight.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09568-03abacklight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09568-03abacklight.jpg)
  *SerLCD Backpack*                                                                                                                                                     *Serial Enabled LCD 16x2*                                                                                                                                         *Serial Enabled LCD 20x4*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Hardware Hookup

### Assembling the SerLCD Backpack

Insert the SerLCD backpack\'s long end of the headers through the back of a basic LCD. [Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the header on the top side of the LCD. The LCD should look like the images below after the terminals are cleaned (assuming that you are using water-soluble flux). If you are using the through holes under the screw terminals, make sure to solder to the pins before assembling the backpack to the basic LCD.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09068-02_LCDwithBackpackTopView.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09068-02_LCDwithBackpackTopView.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09068-03LCDwithBackpackBottomView.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09068-03LCDwithBackpackBottomView.jpg)
  *Top View*                                                                                                                                                                                    *Bottom View*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Connecting to an Arduino

To power and control a serial enabled LCD, you will need three pins. There are two rows of headers broken out on the backpack and built-in serial enabled LCDs. They are electrically identical, so you can use either one. The SerLCD backpack comes pre-populated with a 3-pin screw terminal. Simply insert [M/M jumper wire](https://www.sparkfun.com/products/8431) to each of the screw terminals and tighten. You can also solder directly to the plated through holes on the bottom of the backpack.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/00258-01aSerialEnabledLCDBackpackScrewTerminals.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/00258-01aSerialEnabledLCDBackpackScrewTerminals.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/00258-03aSerialEnabledLCDBackpackPTH.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/00258-03aSerialEnabledLCDBackpackPTH.jpg)
  *Screw Terminals*                                                                                                                                                                                                             *Plated Through Holes*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instead of a screw terminal, the built-in serial enabled LCDs come pre-populated with a 3-pin polarized JST connector. The [JST to breadboard jumper](https://www.sparkfun.com/products/13685) would be the easiest to connect to an Arduino. The cable only connects one way; press it in until it clicks. JST connectors are designed to be very snug; don\'t pull on the wires to disconnect it, [see our tutorial on the proper way to disconnect JST cables](https://www.sparkfun.com/tutorials/241).

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09395-03SerialEnabledLCDInputJST.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09395-03SerialEnabledLCDInputJST.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09568-03aSerialEnabledLCDInputJST.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09568-03aSerialEnabledLCDInputJST.jpg)
  *Input for Serial Enabled LCD 16x2*                                                                                                                                                             *Input for Serial Enabled LCD 20x4*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[] **Note:** The JST\'s pinout for the 16x2 and 20x4 are different. Make sure to reference the silkscreen to power and control the LCD as opposed to the wire\'s color.

#### Hookup Table

There are only three connections you need to make to the LCD. Check your LCD\'s pinout before connecting to your Arduino. If you look closely at the LCD\'s with the JST connector, the input voltage (VDD) and Rx are in different locations on the board depending on how it was populated.

  ---------------------------------------------------------------------------------------------------------------
  Serial Enabled LCD Pinout   Arduino Pin             Description
  --------------------------- ----------------------- -----------------------------------------------------------
  RX                          D11                     Serial UART receive input to the display.\
                                                      9600 baud (default), 8 bits, 1 stop, no parity.

  GND                         GND                     Ground for the power supply.

  VDD                         3.3V or 5V              Power supply, this should be either **+3.3V** or **+5V**\
                                                      depending on the specs of your LCD.
  ---------------------------------------------------------------------------------------------------------------

[] **Warning!** The RX input should be a TTL-level signal based on your input voltage. If you are using a 3.3V LCD and a 5V Arduino, you will need a logic level converter between the two.\
\

[![SparkFun Logic Level Converter - Bi-Directional](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/2/2/12009-06.jpg)](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html)

### [SparkFun Logic Level Converter - Bi-Directional](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html) 

[ BOB-12009 ]

The SparkFun bi-directional logic level converter is a small device that safely steps down 5V signals to 3.3V AND steps up 3....

[ [\$3.95] ]

[![SparkFun Voltage-Level Translator Breakout - TXB0104](https://cdn.sparkfun.com/r/140-140/assets/parts/8/0/0/6/11771-01.jpg)](https://www.sparkfun.com/sparkfun-voltage-level-translator-breakout-txb0104.html)

### [SparkFun Voltage-Level Translator Breakout - TXB0104](https://www.sparkfun.com/sparkfun-voltage-level-translator-breakout-txb0104.html) 

[ BOB-11771 ]

This is a breakout board for the Texas Instruments TXB0104 module. The TXB0104 is a 4-bit bidirectional voltage-level transla...

[ [\$5.95] ]

[![SparkFun Level Translator Breakout - PCA9306](https://cdn.sparkfun.com/r/140-140/assets/parts/8/4/3/0/11955-01.jpg)](https://www.sparkfun.com/products/11955)

### [SparkFun Level Translator Breakout - PCA9306](https://www.sparkfun.com/products/11955) 

[ BOB-11955 ]

This is a breakout board for the PCA9306 dual bidirectional voltage-level translator. Because different parts sometimes use d...

**Retired**

You should **NOT** connect the board directly to RS232-level voltages (which are around +/-10V). This will damage the board. For more information on RS232, [see our explanation here](http://www.sparkfun.com/tutorials/215). If you do wish to connect this display to RS232 signals, you can use a level-shifting board to translate the RS232 signals to TTL-level signals.\
\

[![SparkFun Transceiver Breakout - MAX3232](https://cdn.sparkfun.com/r/140-140/assets/parts/6/7/3/8/11189-02a.jpg)](https://www.sparkfun.com/sparkfun-transceiver-breakout-max3232.html)

### [SparkFun Transceiver Breakout - MAX3232](https://www.sparkfun.com/sparkfun-transceiver-breakout-max3232.html) 

[ BOB-11189 ]

The \'must have\' IC for TTL/CMOS projects finally has its own breakout board! This RS232 IC is capable of running at 3V and co...

[ [\$7.26] ]

[![SparkFun RS232 Shifter - SMD](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/00449-01a.jpg)](https://www.sparkfun.com/sparkfun-rs232-shifter-smd.html)

### [SparkFun RS232 Shifter - SMD](https://www.sparkfun.com/sparkfun-rs232-shifter-smd.html) 

[ PRT-00449 ]

The smallest and easiest to use serial conversion circuit on the market! This board has one purpose in life - to convert RS23...

[ [\$17.50] ]

[![SparkFun RS232 Shifter SMD (No DE9)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/0/4/08780-01.jpg)](https://www.sparkfun.com/sparkfun-rs232-shifter-smd-no-db9.html)

### [SparkFun RS232 Shifter SMD (No DE9)](https://www.sparkfun.com/sparkfun-rs232-shifter-smd-no-db9.html) 

[ PRT-08780 ]

The smallest and easiest to use serial conversion circuit on the market! This board has one purpose in life - to convert RS23...

[ [\$1.95] ]

## Firmware Overview

### Baud Rate

Set the serial interface to: **9600 baud**, 8 bits of data, 1 start bit, 1 stop bit, and no parity (9600,8,1,1,N). This can be changed or updated using the following command set. However, be aware that if you change the communication protocol, you may not be able to re-connect or control the device until your microcontroller\'s baud rate matches.

### Data & Display Information

All settings are stored on onboard EEPROM and loaded during power up. To display data on the SerLCD and built-in serial enabled LCDs, you simply send ASCII-formatted characters using a serial interface which matches the communication protocol. This means that if you pass the ASCII character \'**r**\' to the module, an \'**r**\' will be displayed on the LCD at the next cursor position.

### Configuration & Command Set

There are two reserved control characters used to control and configure various features on the LCD. The control characters are **0xFE** and **0x7C**. Sending a control character followed by a command will allow you to control the cursor, backlight, and other features on the SerialLCD. A complete table of commands are shown below in hexadecimal and decimal value in brackets. Either representation is acceptable when sending a control or command character. The HD44780 LCD controller is very common. The extended commands for this chip include but are not limited to those described in table. Please refer to the HD44780 datasheet for more information.

+-----------------------+--------------------------+------------------------------------------+
| Control Character     | Command Character        | Description                              |
+:=====================:+==========================+==========================================+
| 0xFE \[ 0d254 \]      | 0x01 \[ 0d1 \]           | Clear Display                            |
|                       +--------------------------+------------------------------------------+
|                       | 0x14 \[ 0d20 \]          | Move Cursor Right 1 Space                |
|                       +--------------------------+------------------------------------------+
|                       | 0x10 \[ 0d16 \]          | Move Cursor Left 1 Space                 |
|                       +--------------------------+------------------------------------------+
|                       | 0x1C \[ 0d28 \]          | Scroll Right 1 Space                     |
|                       +--------------------------+------------------------------------------+
|                       | 0x18 \[ 0d24 \]          | Scroll Left 1 Space                      |
|                       +--------------------------+------------------------------------------+
|                       | 0x0C \[ 0d12 \]          | Turn Display On / Hide Cursor            |
|                       +--------------------------+------------------------------------------+
|                       | 0x08 \[ 0d8 \]           | Turn Display Off                         |
|                       +--------------------------+------------------------------------------+
|                       | 0x0E \[ 0d14 \]          | Underline Cursor On                      |
|                       +--------------------------+------------------------------------------+
|                       | 0x0D \[ 0d13 \]          | Blinking Cursor On                       |
|                       +--------------------------+------------------------------------------+
|                       | 0x80 + n \[ 0d128 + p \] | Set Cursor Position,\                    |
|                       |                          | where n is the hexadecimal position and\ |
|                       |                          | p is the decimal value of the position   |
+-----------------------+--------------------------+------------------------------------------+
| 0x7C \[ 0d124 \]      | 0x03 \[ 0d3 \]           | 20 Characters Wide                       |
|                       +--------------------------+------------------------------------------+
|                       | 0x04 \[ 0d4 \]           | 16 Characters Wide                       |
|                       +--------------------------+------------------------------------------+
|                       | 0x05 \[ 0d5 \]           | 4 Lines                                  |
|                       +--------------------------+------------------------------------------+
|                       | 0x06 \[ 0d6 \]           | 2 Lines                                  |
|                       +--------------------------+------------------------------------------+
|                       | 0x09 \[ 0d9 \]           | Turn Splash Screen On/Off                |
|                       +--------------------------+------------------------------------------+
|                       | 0x0A \[ 0d10 \]          | Set Splash Screen                        |
|                       +--------------------------+------------------------------------------+
|                       | 0x0B \[ 0d11 \]          | Set to 2400 Baud                         |
|                       +--------------------------+------------------------------------------+
|                       | 0x0C \[ 0d12 \]          | Set 4800 Baud                            |
|                       +--------------------------+------------------------------------------+
|                       | 0x0D \[ 0d13 \]          | Set **9600 Baud (Default)**              |
|                       +--------------------------+------------------------------------------+
|                       | 0x0E \[ 0d14 \]          | Set 14400 Baud                           |
|                       +--------------------------+------------------------------------------+
|                       | 0x0F \[ 0d15 \]          | Set 19200 Baud                           |
|                       +--------------------------+------------------------------------------+
|                       | 0x10 \[ 0d16 \]          | Set 38400 Baud                           |
|                       +--------------------------+------------------------------------------+
|                       | 0x80 \[ 0d128 \]         | Backlight Off                            |
|                       +--------------------------+------------------------------------------+
|                       | 0x9D \[ 0d157 \]         | Backlight Full On                        |
+-----------------------+--------------------------+------------------------------------------+
| 0x12 \[ 0d18 \]       |                          | Reset to Default Baud While\             |
|                       |                          | LCD\'s Splash Screen is Still Active     |
+-----------------------+--------------------------+------------------------------------------+

*SerLCD Command Set*

### Clear Screen and Set Cursor Position

Clear display and set cursor position are the two commands that are used frequently. To clear the screen, send the control character **0xFE** followed by **0x01**. Clearing the screen resets the cursor position back to position 0 (i.e. the first character on the first line).

To set the active cursor position, send the control character **0xFE** followed by **0x80 + n**, where n is an offset in hexadecimal as described in the tables below. In this case, it would be easier to use the decimal value for setting the cursor position (**0d128**) with the viewable cursor position (**p**) and then send the value.

+---------------------------------------------------+
| 16 Character Displays                             |
+=============+=====================================+
| Line Number | Viewable Cursor Positions (Decimal) |
+-------------+-------------------------------------+
| 1           | 0-15                                |
+-------------+-------------------------------------+
| 2           | 64-79                               |
+-------------+-------------------------------------+
| 3           | 16-31                               |
+-------------+-------------------------------------+
| 4           | 80-95                               |
+-------------+-------------------------------------+

+---------------------------------------------------+
| 20 Character Displays                             |
+=============+=====================================+
| Line Number | Viewable Cursor Positions (Decimal) |
+-------------+-------------------------------------+
| 1           | 0-19                                |
+-------------+-------------------------------------+
| 2           | 64-83                               |
+-------------+-------------------------------------+
| 3           | 20-39                               |
+-------------+-------------------------------------+
| 4           | 80-103                              |
+-------------+-------------------------------------+

#### Example of Setting the Cursor Position

Say we want to the place a character on the third character position of the second line in a 16x2 character display. The cursor position is not what you would expect. Notice that the last character on line 2 jumps from 15 to 64 on the next line? To do this we need to:

- Add 0x80 to the viewable cursor position as stated earlier. Since we are trying to add a hexadecimal value with a decimal, you would need to convert a value to the same representation. Since we know that 0x80 is also 0d128, we will just stick with decimal. Therefore, the third character on the second line in decimal is: 128 + 66 = 194.
- Now that we know the position, send the command character **0xFE** to tell the SerLCD you want to send a command followed by the number **194**. If you are comfortable converting back to hexadecimal, you can also send **0xC2**.
- The cursor should now be sitting in the third position of the second line. Sending any other character will display on the LCD starting at this position.

### Setting Up the LCD Size

The SerLCD backpack\'s firmware includes settings to interface for the following types of LCDs:

- 16x2
- 16x4
- 20x2
- 20x4

If you purchased the SerLCD backpack module by itself, you will have to configure the module to the type of LCD it is going to be, or is currently attached. To set the type of LCD the SerLCD module is attached to, transmit the control character **0x7C** followed with either 0x03, 0x04, 0x05, or 0x06 as explained in the SerLCD Command Set above. These commands set the LCD character width and number of lines. These settings are used to correctly wrap the cursor to keep it within the viewable screen. The type of LCD is saved to EEPROM after each change.

If you purchased the built-in serial enabled LCD, it has already been configured to work with that specific LCD. You should not have to configure anything.

### Changing the Baud Rate

The backpack and built-in serial enabled LCD defaults to **9600 baud**, but they can be set to a variety of baud rates.

[] **Caution!** Once you change the baud rate, you need to change the baud rate of your controlling device to match this. To change the LCD\'s baud rate from 9600 to 14400, first enter the control character **0x7C** control and **0x0E**. Then adjust your microcontroller\'s code to match the baud rate of 14400.

If the serial enabled LCD gets into an unknown state or you otherwise can\'t communicate with it, try sending a \"CTRL-R\" (**0x12**) character at 9600 baud while the splash screen is active (during the first 500 ms of boot-up) and the unit will reset to 9600 baud.

### Backlight Brightness

The SerLCD v2.5 provides you with control of the backlight to one of 30 different brightness levels. To control the backlight, send the control character **0x7C** followed by a number from **0x80 to 0x9D**. Sending a **0x80** sets the backlight to off and **0x9D** sets the backlight to fully on.

This is handy when power consumption of the unit must be minimized. By reducing the brightness, the overall backlight current consumption is reduced.

[] **Note:** You may need to add a small delay (around 0.5 second to 1 second) to let the display settle. Otherwise, the display may go dark with no text.

### Splash Screen

The SerLCD and built-in serial enabled LCD displays a splash screen by default. This splash screen verifies that the unit is powered, working correctly, and that the connection to the LCD is correct. The splash screen is displayed for 500 ms during boot-up and may be turned off if desired.

[![PIC-Based Serial Enabled Character LCD Tutorial-04 Splash Screen](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-04_Splash_Screen.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-04_Splash_Screen.jpg)

#### Setting Splash Screen

A new addition to the V2.5 firmware is the ability for the user to set their own splash screen (2 lines). To do this, just set the top 2 lines as you would like them to appear, send the control character **0x7C** followed by \"CTRL-J\" (**0x09**) to save it to memory. To test, just cycle power.

#### Turning Splash Screen On/Off

To disable the splash screen, send the control character **0x7C** to the unit followed by \"CTRL-J\" (**0x0A**). Every time this command is sent to the unit, the splash screen display option will toggle. If the splash screen is currently being displayed, sending the **0x7C** and **0x0A** characters will disable the splash screen during the next boot, and sending the **0x7C** and **0x0A** characters again will enable the splash screen.

### Extended Command

When testing the extended LCD command 0x0C, the command used all three of the following commands:

- Turn Visual Display On
- Underline Cursor Off
- Blinking Box Cursor Off

So if you had the cursor/blinking box on and turned the visual display off, the cursor/blinking box would not remain on after after issuing the **0xFE** control and **0x0C** command value to turn the screen back on.

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

[] **Warning:** Arduino and other systems with bootloaders may send \"garbage\" characters to the display while the system is starting up or being reprogrammed. This may cause the display to be bricked. To avoid this, you can use a software serial library to create a separate serial port from the USB port, as in the following examples. For more information about the library, head over to the reference:\
\

[Arduino.cc Reference: Software Serial Library](https://www.arduino.cc/en/Reference/SoftwareSerial)

\

For simplicity, we will be using an Arduino microcontroller. In this example, we connected a serial enabled LCD to the RedBoard programmed with Arduino (basically an Arduino Uno with an ATmega328P).

### Example 1: Hello World!

Copy and paste these sketch into your Arduino IDE.

    language:c
    // SparkFun Serial LCD example 1
    // Clear the display and say "Hello World!"

    // This sketch is for Arduino versions 1.0 and later
    // If you're using an Arduino version older than 1.0, use
    // the other example code available on the tutorial page.

    // Use the Software Serial library to create a new "soft" serial port
    // for the display. This prevents display corruption when uploading code.
    #include <SoftwareSerial.h>

    // Attach the serial enabld LCD's RX line to digital pin 11
    SoftwareSerial LCD(10, 11); // Arduino SS_RX = pin 10 (unused), Arduino SS_TX = pin 11 

    void setup()
    

    void loop()
    

When you power up the board, you\'ll briefly see a SparkFun splash screen, and then the display will go blank. To send text to the board, wait 1/2 second (500ms) after power up for the splash screen to clear, then send text to the display through your serial port. The display understands all of the standard ASCII characters (upper and lowercase text, numbers, and punctuation), plus a number of graphic symbols and Japanese characters. See the [HD44780 datasheet](http://www.sparkfun.com/datasheets/LCD/HD44780.pdf) for the full list of supported characters.

If you send data that goes past the end of the first line, it will skip to the start of the second line. If you go past the end of the second line, the display will jump back up to the beginning of the first line.

**Tip:** You can simulate a scrolling window in software by copying the second line to the first line, and clearing the second line.

Here\'s what you should see after uploading the code to your Arduino. Try changing the text with a different message!

[![Tutorial-03 Hello World](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-03_Hello_World.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-03_Hello_World.jpg)

### Example 2: Move the Cursor

A common LCD technique is to repeatedly display changing numbers such as RPM or temperature in the same place on the display. You can easily do this by moving the cursor before sending your data.

To move the cursor, send the special character (**0xFE**), followed by the cursor position you\'d like to set. Each cursor position is represented by a number, see the table below to determine the number in decimal to send for a serial enabled LCD set to 16x2:

  Position   1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16
  ---------- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
  Line 1     128   129   130   131   132   133   134   135   136   137   138   139   140   141   142   143
  Line 2     192   193   194   195   196   197   198   199   200   201   202   203   204   205   206   207

For example, if you want to move to the beginning of the second line, send the control character **0xFE** and command character **0d192**.

Here\'s a slightly more complex example showing how to display data at fixed points on the display, plus the use of `sprintf()` to convert numbers to strings (this right-justifies the numbers with leading spaces, which keeps them from \"jumping around\" if the number of digits changes):

    language:c
    // SparkFun Serial LCD example 2
    // Format and display fake RPM and temperature data

    // This sketch is for Arduino versions 1.0 and later
    // If you're using an Arduino version older than 1.0, use
    // the other example code available on the tutorial page.

    // Use the Software Serial library to create a new "soft" serial port
    // for the display. This prevents display corruption when uploading code.
    #include <SoftwareSerial.h>

    // Attach the serial enabld LCD's RX line to digital pin 11
    SoftwareSerial LCD(10, 11); // Arduino SS_RX = pin 10 (unused), Arduino SS_TX = pin 11

    void setup()
     

    int temp, rpm;
    char tempstring[10], rpmstring[10]; // create string arrays

    void loop() 
    

You should see something similar to the image below. Try reading a sensor and displaying the values on the screen!

[![Move Cursor RPM Temp](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-02_Move_Cursor_RPM_Temp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-02_Move_Cursor_RPM_Temp.jpg)

### SerLCD Demo

This is an extensive example sketch that shows you how to create a scrolling marquee, create a timer, display sensor data, and control the backlight. Copy and paste the following example to the Arduino IDE. Upload the example to your Arduino to test!

    language:c
    /***********************************************************************
      SerLCD Demo Example Code
      Written by: Joel Bartlett @ SparkFun Electronics
      Date: December 20, 2012 
      Modified by: Ho Yun "Bobby" Chan @ SparkFun Electronics 
      Date: May 3, 2018

      This code uses the information presented in the SerLCD Datasheet 
      to create an Arduino example using the SerLCD from SparkFun Electonics. 
      Each of the SerLCD's capabilities is broken up into seperate functions
      within the sketch. Simply call each function with the correct parameters
      to get the desired result form the LCD screen. 

      This code was developed for the Arduino IDE v102

      To use, connect the following pins
          VDD -> 5V
          GND -> GND
          LCD RX -> Arduino TX (pin 11)

        ***Don't forget to disconnect the LCD's RX pin from the TX pin of 
    the Arduino's UART line while programming!***

      You can also check out the SerLCD library from Arduino 
    http://playground.arduino.cc/Code/SerLCD

      If you need to reprogram often, or need the UART for another device,
      you can use the Software Serial libary to create a 
      seperate UART for the LCD.
      Arduino IDE -> Sketch -> Import Library ->Software Serial

      To declare a new UART using SoftwareSerial, insert this line:
      SoftwareSerial NAME(x,y); // RX, TX
      where Name is the name of the new UART, x is the RX pin, and y is the TX     pin.

      "THE BEER-WARE LICENSE"
      As long as you retain this notice you can do whatever you want with this stuff. 
      If we meet some day, and you think this stuff is worth it, you can buy me a beer.
    ************************************************************************/
    #include <SoftwareSerial.h>

    SoftwareSerial LCD(10, 11); // Arduino SS_RX = pin 10 (unused), Arduino SS_TX = pin 11

    //-------------------------------------------------------------------------------------------
    void setup()
    
    //-------------------------------------------------------------------------------------------
    void loop()
    
    //-------------------------------------------------------------------------------------------
    void clearScreen()
    
    //-------------------------------------------------------------------------------------------
    void selectLineOne()
    
    //-------------------------------------------------------------------------------------------
    void selectLineTwo()
    
    //-------------------------------------------------------------------------------------------
    void moveCursorRightOne()
    
    //-------------------------------------------------------------------------------------------
    void moveCursorLeftOne()
    
    //-------------------------------------------------------------------------------------------
    void scrollRight()
    
    //-------------------------------------------------------------------------------------------
    void scrollLeft()
    
    //-------------------------------------------------------------------------------------------
    void turnDisplayOff()
    
    //-------------------------------------------------------------------------------------------
    void turnDisplayOn()
    
    //-------------------------------------------------------------------------------------------
    void underlineCursorOn()
    
    //-------------------------------------------------------------------------------------------
    void underlineCursorOff()
    
    //-------------------------------------------------------------------------------------------
    void boxCursorOn()
    
    //-------------------------------------------------------------------------------------------
    void boxCursorOff()
    
    //-------------------------------------------------------------------------------------------
    void toggleSplash()
    
    //-------------------------------------------------------------------------------------------
    int backlight(int brightness)// 128 = OFF, 157 = Fully ON, everything in between = varied      
    
    //-------------------------------------------------------------------------------------------
    void scrollingMarquee()
    
    }
    //-------------------------------------------------------------------------------------------
    void counter()
    
    }
    //-------------------------------------------------------------------------------------------
    void tempAndHumidity()
    
    //-------------------------------------------------------------------------------------------
    void backlight()
    
    }
    //-------------------------------------------------------------------------------------------
    void cursors()
    

### Alternative Libraries

Alternatively, you can use the SerLCD library found on the Arduino.cc website.

[Arduino.cc - serLCD Library](http://playground.arduino.cc/Code/SerLCD)

If you are using Linux, you may want to try this library instead.

[serLCD Library for Linux (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/SerLCDLibLinux.zip)

## Troubleshooting

### Random Character

If the display is powered up without the RX line connected to anything, the display may fill with strange characters. This is because the display is receiving random noise on the disconnected line. If you connect the RX line to a true TX port, this will not happen.

### Faded Characters on Display

If the display is unreadable or washed out, the contrast may need to be adjusted. Send some text to the display (see the first example sketch above), then use a miniature Phillips screwdriver to gently turn the contrast trimpot labeled VR1 on the back of the display until the text is as clear as possible (please be gentle with the trimpot). This display also has a backlight that can be adjusted for best readability, see the LCD datasheet for information.

### Bricked LCD

If you are seeing two rows of ASCII blocks (i.e. █ ) or random characters, it\'s possible that you might have bricked the serial enabled LCD by putting it into an unknown state. This is a common problem if you are uploading code to the Arduino while another device is connected to the same hardware UART line (i.e. pin 0 and 1). Some systems like Arduino send bootloader information out the serial port when the system starts up. This will cause the LCD to output random characters usually on the screen or not even show anything on the screen. If this is a problem, make sure to use a software defined serial pin to create a TX pin that doesn\'t get used during startup.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-400/assets/learn_tutorials/7/7/4/Red_Bricked_PIC-Based_Serial_Enabled_LCD_20x4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/Red_Bricked_PIC-Based_Serial_Enabled_LCD_20x4.jpg)   [![](https://cdn.sparkfun.com/r/600-400/assets/learn_tutorials/7/7/4/Parallel_CharactersBricked_PIC-based_SerialEnabledLCD_16x2.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/Parallel_CharactersBricked_PIC-based_SerialEnabledLCD_16x2.JPG)
  *Bricked Serial Enabled LCD 20x4*                                                                                                                                                                                                   *Bricked Serial Enabled LCD 16x2*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Recovering from Unknown State: Software Reset

If the Serial LCD gets into an unknown state and you are not able to communicate with it anymore, just write **0x12** in the loop so that it is constantly sending the hex value to the screen when the LCD\'s splash screen is active (or when the LCD is powered) to reset the unit back to 9600 baud as explained earlier. The screen will temporarily revert to 9600 baud until power is cycled. This is to allow you to regain control of the display if you set it to an unknown baud rate. Make sure to also change the baud rate in the EEPROM.

The [old datasheet in section 3.4](https://www.sparkfun.com/datasheets/LCD/SerLCD_V2_5.PDF) indicates that you need to send a command character **0x7C** in hexadecimal. If you look at the ASCII table for the [non-printing control characters](http://www.physics.udel.edu/~watson/scen103/ascii.html) (CTRL-K through CTRL-P), there are hex values for the different baud rates that you would need to send to the LCD.

  ------------------------------------------------------------------------------------------------
  Non-Printing Control Characters   Command Character       Description
  --------------------------------- ----------------------- --------------------------------------
  \<control\>K                      0x0B \[ 0d11 \]         Set to 2400 Baud

  \<control\>L                      0x0C \[ 0d12 \]         Set 4800 Baud

  \<control\>M                      0x0D \[ 0d13 \]         **Set 9600 Baud (Default)**

  \<control\>N                      0x0E \[ 0d14 \]         Set 14400 Baud

  \<control\>O                      0x0F \[ 0d15 \]         Set 19200 Baud

  \<control\>P                      0x10 \[ 0d16 \]         Set 38400 Baud

  \<control\>R                      0x12 \[ 0d18 \]         Reset to Default Baud While\
                                                            LCD\'s Splash Screen is Still Active
  ------------------------------------------------------------------------------------------------

All you have to do is create a new void function similar to the one below and call it when you are running the Arduino sketch file like this:

    language:c
    void changeBaud()

Here\'s some code with Arduino to try and unbrick the PIC16F88 on the serial enabled LCDs. This sometimes works and there is a higher probability of recovering your LCD if you still are able to see the splash screen.

[SerLCD Software Reset Example](https://github.com/bboyho/SerLCD/blob/master/Arduino/SerLCD_Arduino_Example_v3/SerLCD_Arduino_Example_v3.ino#L89)

### Recovering from Unknown State: PICkit Programmer

The last resort is to use the PICkit 3 programmer and reupload the firmware on the LCD using MPLAB. If you are trying to recover a bricked serLCD backpack, you will need a few of the following materials listed below to connect to the programming header. The built-in serial enabled LCD will have standard 0.1\" spaced headers so the IC hooks will not be necessary as long as there is contact with the pins during programming.

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![Long Centered Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/4/2/7/12693-02.jpg)](https://www.sparkfun.com/break-away-headers-40-pin-male-long-centered-pth-0-1.html)

### [Long Centered Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-40-pin-male-long-centered-pth-0-1.html) 

[ PRT-12693 ]

This is a row of 40 break away headers spaced 0.1\" apart with long pins on both sides. This header is especially useful when ...

[ [\$1.50] ]

[![MPLAB PICkit 3](https://cdn.sparkfun.com/r/140-140/assets/parts/4/1/0/7/09973-_03.jpg)](https://www.sparkfun.com/products/9973)

### [MPLAB PICkit 3](https://www.sparkfun.com/products/9973) 

[ PGM-09973 ]

Fast programming, increased functionality, at the same price as its predecessor, the PICkit™ 3. The MPLAB PICkit 4 now h...

**Retired**

#### Using MPLAB X IDE v2.30

For this example, we will be using MPLAB X IDE V2.30 for Windows. Head over to MicroChip\'s archived downloads to download and install.

[MPLAB X IDE Download Archives](http://www.microchip.com/development-tools/pic-and-dspic-downloads-archive)

**Heads up!** You can also download an older version or the [latest MPLAB X IDE](http://www.microchip.com/mplab/mplab-x-ide) but the directions may be slightly different than the ones listed in this tutorial.

Also, make sure to download the hex file specific for your LCD to recover. We will be using the **.hex** file linked for the serial enabled LCD backpack below. If you are using the ones with the built-in serial, you will need to unzip the folder before using the file.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09068-03LCDwithBackpackBottomView.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09068-03LCDwithBackpackBottomView.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09395-03_Built-In_Serial_LCD_16x2_Bottom_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09395-03_Built-In_Serial_LCD_16x2_Bottom_View.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09568-03a_Built-In_Serial_LCD_20x4_Bottom_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/09568-03a_Built-In_Serial_LCD_20x4_Bottom_View.jpg)

  [Download\                                                                                                                                                                                        [Download\                                                                                                                                                                                                                [Download\
  serlcd-v2_6_2line_10MHz (HEX)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/serlcd-v2_6_2line_10MHz.hex)                                                              serlcd-v2_7_2line_10MHz (ZIP)](http://cdn.sparkfun.com/datasheets/LCD/Monochrome/serlcd-v2_7_2line_10MHz.zip)                                                                                          serlcd-v2_7_4line_10MHz (ZIP)](http://cdn.sparkfun.com/datasheets/LCD/Monochrome/serlcd-v2_7_4line_10MHz.zip)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[] **Reminder:** You can click on any of the images in this tutorial for a closer look!

Once installed, select **File \> Import \> Hex/ELF\... (Prebuilt) File**.

[![Import Hex/ELF](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Import_hex.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Import_hex.jpg)

Click on the **Browse\...** button and head to the location where the **.hex** file is stored on your computer. This will probably be in your recent downloads. Select the file and click on the **Open** button. This will automatically provide the path for the **Prebuilt Filename** which is **\.../serlcd-v2_6_2line_10MHz.hex**.

[![Browse for hex file](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Import_Browse_hex.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Import_Browse_hex.jpg)

Then type in the **Device** field: **PIC16F88**. If you have a *PIC16**L**F88* that is populated on the SerLCD backpack, this is the same device that you would select. **[The programmer will not notice a difference between the two PICs](http://www.microchip.com/forums/m636583.aspx#636585)**. Once selected, click on the **Next \>** button.

[![Select Device or Microcontroller](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Select_Device.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Select_Device.jpg)

Click **Finish** to save as a project.

[![Save Project](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Project_Folder.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Project_Folder.jpg)

Connect the PICkit 3 to your computer using the USB cable. At this point, make the connection from the PICkit 3 to the programming pins of the LCD. Power the target (your PIC16LF88) from a separate power supply like an Arduino using wires. The [PICkit 3 may not have enough power to power the target](http://microchipdeveloper.com/pickit3:power-target).

If you are using a 3.3V LCD, make sure to read the note highlighted in red below.

⚡ **Oh snap!** Make sure that the logic levels between your PICkit 3 and LCD match. If you do not have a logic level converter between the PICKit 3 and the serial enabled LCD\'s programming pins, the PIC or the LCD may become damaged. If not, head over to the menu and click on **Run \> Set Project Configuration \> Customize\...** .\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Project_Config_Voltage.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Project_Config_Voltage.jpg)

\
From the **Categories:** tree, select the **PICkit 3 programmer**. Under the **Option categories:** drop down menu, select **Power**.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Project_PICkit3_Config_Voltage.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Project_PICkit3_Config_Voltage.jpg)

\
Under **Voltage Level**, select **3.25**. This should be a sufficient enough for flashing the PIC. Click **OK** button to save.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Project_PICkit3_Config_Voltage_3_3V.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Project_PICkit3_Config_Voltage_3_3V.jpg)

The PICkit 3 programmer\'s pinout is listed on [page 15 of PICkit 3 user manual](http://www.sparkfun.com/datasheets/Programmers/PICkit_3_User_Guide_51795A.pdf). To connect, start by connecting the LCD\'s programming header indicated by the polarity marker and move toward the other side.

  PICkit 3 Programmer Connector Pinout   Notes
  -------------------------------------- -------------------------------------------------------------------------------
  V~PP~                                  Indicated by an Arrow, connect to pin \"**1**\" or a straight bar \" **¯** \"
  V~DD~ Target                           3.3V or 5V depending on your LCD
  V~SS~ (GND)                            Ground
  PGD                                    Data
  PGC                                    Clock
  LVP                                    Not Connected on SerLCD backpack

If you are using a 5V LCD, you can connect to the backpack with jumper wires (specifically [wires with small pins](https://www.sparkfun.com/products/11026)) like the images shown below. When reflashing, the target voltage and GND pins were connected to the screw terminal. The PIC16LF88 can be reflashed as long as the pins are held in place during programming. Make sure the pins are not touching the LCD underneath.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-05_PICkit3_Programmer_Reflash.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-05_PICkit3_Programmer_Reflash.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-06_PICkit3_Programmer_Reflash_Closeup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-06_PICkit3_Programmer_Reflash_Closeup.jpg)
  *Jumper Wires Between PICkit3 and SerLCD Backpack*                                                                                                                                                                                                                                                  *Make Sure the Pins are Not Touching the LCD Underneath*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For those with the built-in serial enabled LCD programming pins, you could just connect using header pins by aligning the arrow to the pin \"**1**\".

[![Tutorial-07 PICkit3 Programmer Reflash](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-07_PICkit3_Programmer_Reflash_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/PIC-Based_Serial_Enabled_Character_LCD_Tutorial-07_PICkit3_Programmer_Reflash_2.jpg)

Then click on the icon\'s drop down menu that looks like the software is downloading to a PIC chip (i.e. the button next to the Run Project button) and select **Make and Program Device Programmer to Go PICkit3 (Project serlcd-v2_6_2line_10MHz)**.

[![Program Button to Flash](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Make_and_Program_Button.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Make_and_Program_Button.jpg)

A message will pop up if you did not select the correct programmer.

ICD 3 not found. The last tool used for this project is unavailable. Please select the tool that you want to use to debug or program from the following list of available tools.

Select PICkit 3 in the tree and click the **OK** button.

[![Select Correct Programmer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_IDC_Not_Found.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_IDC_Not_Found.jpg)

The software will pop up with this message:

CAUTION: Check that the device selected in MPLAB IDE (PIC16F88) is the same one that is physically attached to the debug tool. Selecting a 5V device when a 3.3V device is connected can result in damage to the device when the debugger checks the device ID. Do you wish to continue?

If you followed the steps earlier to configure the PICkit 3 for a 3.3V LCD or are using a 5V LCD, click **OK**.

[![Caution](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Caution_Device_VoltageLevel2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Caution_Device_VoltageLevel2.jpg)

From there, the hex file should begin flashing on the chip and the program will run immediately after displaying this output:

    language:c
    *****************************************************

    Connecting to MPLAB PICkit 3...
    Firmware Suite Version.....01.28.90 *
    Firmware type..............Midrange

    Target voltage detected
    Target device PIC16F88 found.
    Device ID Revision = 8

    The following memory area(s) will be programmed:
    program memory: start address = 0x0, end address = 0x4ab
    configuration memory

    Device Erased...

    Programming...
    Programming/Verify complete 

You should see this output at the bottom of the MPLAB X IDE.

[![Programming Complete](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Uploaded.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/4/MPLAB_X_PIC_Uploaded.jpg)

Power cycle the screen. Congrats! We have recovered the LCD! Or, at least for a 16x2 character LCD\... The firmware we flashed was set for the 16 characters and 2 lines. The next step is to configure the PIC for a 20x4 character LCD. To do this, we just need to send the control and command flags to adjust the width and lines. Place this your Arduino\'s `setup()` function after setting your Arduino\'s software serial port.

    language:c
    void set_20x4()

Power cycle the screen and run the demo example to see if everything is working as expected. Ok, now we have recovered your 20x4 serial enabled LCD!

### More Examples of Setting Cursor Position

As stated earlier, to set the LCD\'s cursor position, you would send the command character/flag. Then send additional number related to the cursor\'s position on the LCD screen. This example goes over how to set the cursor position for a 20x4 serial enabled LCD. Just add *128* to the cursor\'s position as stated on [page 3 of the datasheet](https://www.sparkfun.com/datasheets/LCD/SerLCD_V2_5.PDF) to place the cursor at the correct coordinates.

For example, if you are trying to place the cursor at (line 3, position 0), you would send the command character **0xFE** and the associated coordinates. Looking at the datasheet, for the 20x4 serial enabled LCD screen, it looks like 128+20 = **148** . Therefore:

    language:c
    selectLineThree()

As another example, if you are trying to place the cursor at (line 4, position 0), you would send the command character **0xFE** and the associated coordinates. Looking at the datasheet, for the 20x4 serial enabled LCD screen, it looks like 128+84= **212**. Therefore:

    language:c
    selectLineFour()

### Using the Serial Enabled LCD on an Atmega32U4\'s Hardware UART

If you are using the serial enabled LCD with an Atmega32U4-based Arduino (like a Pro Micro, Arduino Leonardo, Arduino LilyPad USB etc), you might need to add a small delay in the setup before you can get it working with the hardware UART (pins 0 and 1). Here\'s an example:

    language:c
    ///test example using ATmega32U4's hardware UART and delay
    void setup() 

    void loop() 

### Software Serial for Arduino Due

Unfortunately, you are not able to use the serial enabled LCDs with an Arduino Due due the differences in how change interrupts are used for the ARM processor. The software serial library is not included in the Arduino Due\'s tree:

[Arduino.cc Forums - Software Serial for Arduino Due?](http://forum.arduino.cc/index.php?topic=142902.0)

Try using the other hardware serial UARTs that are not connected to the Arduino Due\'s programming pins for uploading. Make sure to adjust the code for the hardware serial UARt.

### Changing Width and Character Lines

To adjust the default width and character lines, there is some code listed in this example based on the datasheet to configure the serial enabled LCD.

[SerLCD Example Update Character Lines](https://github.com/bboyho/SerLCD/blob/master/Arduino/SerLCD_Arduino_Example_v3/SerLCD_Arduino_Example_v3.ino#L66)