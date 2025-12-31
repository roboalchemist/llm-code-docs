# Source: https://learn.sparkfun.com/tutorials/microsd-breakout-with-level-shifter-hookup-guide

## Introduction

The [MicroSD Breakout with Built-In Level Shifter](https://www.sparkfun.com/products/13743) makes it easy to add mass storage to your project while working with a 5V system.

[![SparkFun Level Shifting microSD Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/2/6/7/13743-01.jpg)](https://www.sparkfun.com/sparkfun-level-shifting-microsd-breakout.html)

### [SparkFun Level Shifting microSD Breakout](https://www.sparkfun.com/sparkfun-level-shifting-microsd-breakout.html) 

[ DEV-13743 ]

The SparkFun Level Shifting microSD Breakout is quite similar to the SparkFun microSD Transflash Breakout, but with the inclu...

[ [\$6.50] ]

### Required Materials

To follow along with this hookup guide, you will need the following:

### Suggested Reading

If any of these subjects sound unfamiliar, considering reading the following tutorials before continuing on.

- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino) - New to Arduino? Start here.
- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide) - A refresher on using the Arduino environment.
- [Serial Peripheral Interface (SPI)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) - This tutorial shows you how to communicate with an SD card over SPI.
- [SD Cards and Writing Images](https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images) - Learn the basics of SD and microSD cards.
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels) - Logic level basics for 3.3V and 5V systems.
- [How to Solder: Through Hole Soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) - Basic information on how to solder to PTH pins.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images)

### SD Cards and Writing Images 

How to upload images to an SD card for Raspberry Pi, PCDuino, or your favorite SBC.

## Hardware Overview

The [SparkFun Shifting microSD Breakout](https://www.sparkfun.com/products/13743) is quite similar to the [SparkFun microSD Transflash Breakout](https://www.sparkfun.com/products/544), but with the additional feature of being 5.0V tolerant for ease of use. No more discrete level shifting is required! If you are using a 3.3V device, we recommend using the microSD Transflash Breakout without the level translation.

[![Logic Translator Populated on the Back of the Level Shifting micrOSD Breakout](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/2/13743-03_Level_Shifting_micro_SD_Breakout_Back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/2/13743-03_Level_Shifting_micro_SD_Breakout_Back.jpg)

*Back of the Level Shifting microSD Breakout*

One thing that makes this product stand out is that it is `SPI_FULL_SPEED` stable. Some errors were seen in our testing with other products, but none have been caught using this board. We didn\'t have NIST do our testing. We can\'t rule out the influence of environmental factors or the host processor used, but if we were looking for stability and reliability at high speed, we\'d use this board.

If your processor is capable of it, this board supports the use of even the fastest UHS µSD cards. We only tested to 25MHz, but it should be good to two to four times that. Today most Arduino type µControllers are only capable of `SPI_HALF_SPEED` (6Mbps). Consider this board if you want a little future proofing or have a faster setup. The Arduino SD library is capable of `SPI_FULL_SPEED` (25Mbps).

The SparkFun Shifting µSD is also a bit unique from its competitors in that it is bi-directional - it level translates all of its outputs back to the level of the hardware it\'s connected to.

## Hardware Hookup

There are numerous ways to wire up an equivalent circuit to the one used in this guide. That will all depend on the type of Arduino you are using, the availability of a breadboard, or the types of wires you have laying around. The required materials list above assumes you have access to one of the most popular 5V Arduino form factors and you will wire it directly to the Shifting µSD board with jumper wires. No breadboard required, and only [minimal soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) to get a connection to the µSD board.

Here is how you would wire up the Shifting µSD to a 5V [RedBoard](https://www.sparkfun.com/products/12757) or [Arduino Uno](https://www.sparkfun.com/products/11224) [^\[1\]^](https://learn.sparkfun.com/tutorials/microsd-breakout-with-level-shifter-hookup-guide#arduino_mega).

[![Shifting microSD connected to RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/2/RedBoard_Shifting_SD.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/2/RedBoard_Shifting_SD.png)

*Shifting µSD board wired to 5V RedBoard*

**Warning!** From the Ardino SPI library: If the SS pin ever becomes a LOW INPUT then SPI automatically switches to Slave, so the data direction of the SS pin MUST be kept as OUTPUT. This is pin 10, so be careful.

[\[1\]](https://learn.sparkfun.com/tutorials/microsd-breakout-with-level-shifter-hookup-guide#arduino_mega) **Note:** If you are using this with an Arduino Mega 2560, the [SPI pins are broken out on a different location](https://www.arduino.cc/en/reference/SPI). You will need to wire the SPI pins differently on the Arduino Mega 2560.

## Code Example

**Note:** If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Copy and paste the code in the Arduino IDE. Selected the correct board (in this case, the **Arduino Uno**) and serial port that the Arduino enumerated to. Finally, hit the upload button.

    language:c
    /*
     * A simple file logger that allows the user to write to a file on the µSD card
     * using the Arduino IDE Serial Monitor (57600 baud). Entered text is written
     * to the µSD card every 20 characters, but to make sure everything is written
     * append 'EOF' to your writing. Doing so writes everything remaining in the
     * buffer to the file and reads back the contents of the file.
     */

    #include <SPI.h>
    #include <SD.h>

    File fd;
    const uint8_t BUFFER_SIZE = 20;
    char fileName[] = "demoFile.txt"; // SD library only supports up to 8.3 names
    char buff[BUFFER_SIZE+2] = "";  // Added two to allow a 2 char peek for EOF state
    uint8_t index = 0;

    const uint8_t chipSelect = 8;
    const uint8_t cardDetect = 9;

    enum states: uint8_t ;
    uint8_t state = NORMAL;

    bool alreadyBegan = false;  // SD.begin() misbehaves if not first call

    ////////////////////////////////////////////////////////////////////////////////
    // Standard Arduino setup function
    ////////////////////////////////////////////////////////////////////////////////
    void setup()
    

    ////////////////////////////////////////////////////////////////////////////////
    // Arduino calls this function over and over again when running
    ////////////////////////////////////////////////////////////////////////////////
    void loop()
    

      if (Serial.available() > 0)
      
      }
    }

    ////////////////////////////////////////////////////////////////////////////////
    // Do everything from detecting card through opening the demo file
    ////////////////////////////////////////////////////////////////////////////////
    void initializeCard(void)
    

      // Card seems to exist.  begin() returns failure
      // even if it worked if it's not the first call.
      if (!SD.begin(chipSelect) && !alreadyBegan)  // begin uses half-speed...
      
      else
      
      Serial.println(F("Initialization done."));

      Serial.print(fileName);
      if (SD.exists(fileName))
      
      else
      

      Serial.print("Opening file: ");
      Serial.println(fileName);

      Serial.println(F("Enter text to be written to file. 'EOF' will terminate writing."));
    }

    ////////////////////////////////////////////////////////////////////////////////
    // This function is called after the EOF command is received. It writes the
    // remaining unwritten data to the µSD card, and prints out the full contents
    // of the log file.
    ////////////////////////////////////////////////////////////////////////////////
    void eof(void)
    
      }
      else
      
      fd.close();
    }

    ////////////////////////////////////////////////////////////////////////////////
    // Write the buffer to the log file. If we are possibly in the EOF state, verify
    // that to make sure the command isn't written to the file.
    ////////////////////////////////////////////////////////////////////////////////
    void flushBuffer(void)
    
        fd.write(buff, index);
        fd.flush();
        index = 0;
        fd.close();
      }
    }

    ////////////////////////////////////////////////////////////////////////////////
    // Reads a byte from the serial connection. This also maintains the state to
    // capture the EOF command.
    ////////////////////////////////////////////////////////////////////////////////
    void readByte(void)
    
      else if (byteRead == 'O' && state == E)
      
      else if (byteRead == 'F' && state == EO)
      
    }

The example code for this product is a simple file logger that allows the user to write to a file on the µSD card using the [Arduino IDE Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/all#arduino-serial-monitor-windows-mac-linux) (**57600 baud**). When the board boots you should see the following in the Serial Monitor:

    language:bash
    Initializing SD card...Initialization done.
    demoFile.txt doesn't exist. Creating.
    Opening file: demoFile.txt
    Enter text to be written to file. 'EOF' will terminate writing.

The last line of that block of text is important to note. Your work is written to the µSD card every 20 characters, but to make sure everything is written append `EOF` to your writing. Doing so writes everything remaining in the buffer to the file and reads back the contents of the file.

    language:bash
    EOF

    demoFile.txt:
    Test line of text.
    Bacon ipsum dolor amet beef picanha drumstick alcatra brisket, short ribs sirloiBacon ipsum dolor amet beef picanha drumstick alcatra brisket, short ribs sirloin.

One thing to note is that the UART buffer on the Arduino might limit the number of characters entered on a single line. In one test I noticed that my Arduino only accepted 164 bytes before loosing data, but I\'ve seen that vary a bit.

## Troubleshooting

Arduino has troubleshooting tips on their [Notes on the Arduino SD Card Library](http://arduino.cc/en/Reference/SDCardNotes) page, including instructions for formatting new cards (if needed) and using the library with other Arduino boards.