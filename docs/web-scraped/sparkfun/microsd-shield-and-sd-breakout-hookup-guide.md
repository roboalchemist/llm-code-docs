# Source: https://learn.sparkfun.com/tutorials/microsd-shield-and-sd-breakout-hookup-guide

## Introduction

The [SparkFun microSD Shield](https://www.sparkfun.com/products/12761) makes it easy to add mass storage to your project.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/7/assembled_microsd.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/7/assembled_microsd.jpg)

### Required Materials

- 1x [SparkFun microSD Shield](https://www.sparkfun.com/products/12761)
- 1x [pack of R3 stackable headers](https://www.sparkfun.com/products/11417) for the shield.
- 1x microSD card of your choice, up to 32GB, like SparkFun\'s [8GB card and adapter pack](https://www.sparkfun.com/products/11609)
- 1x SparkFun [RedBoard](https://www.sparkfun.com/products/12757) or [Arduino Uno](https://www.sparkfun.com/products/11021) and a USB cable

### Assembly

Before use, you will need to solder headers to your shield. [Take a look at the Shield Assembly tutorial](https://learn.sparkfun.com/tutorials/arduino-shields#installing-headers-preparation) if you need a refresher. The microSD Shield uses the Uno R3 footprint with [1x 10-pin, 2x 8-pin, and 1x 6-pin headers](https://www.sparkfun.com/products/11417).

### Suggested Reading

- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino) - New to Arduino? Start here.
- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide) - A refresher on using the Arduino environment.
- [Arduino Shield Basics](https://learn.sparkfun.com/tutorials/arduino-shields-v2) - Covers shields from a general standpoint.
- [Serial Peripheral Interface (SPI)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) - This tutorial shows you how to communicate with an SD card over SPI.
- [SD Cards and Writing Images](https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images) - Learn the basics of SD and microSD cards.

## Hardware Overview

The features of the microSD Shield are as follows:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/7/sd-card-overview.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/7/sd-card-overview.jpg)

1.  A large protoyping area where you can solder other parts for your project.

2.  A hex converter IC (which acts as a voltage level shifter between the Arduino\'s 5V logic and the microSD card\'s 3.3V-tolerant pins). The datatsheet for that IC can be found [here](http://www.nxp.com/documents/data_sheet/74HC4050_CNV.pdf).

3.  A microSD socket.

4.  A power LED. Lights up as soon as the Arduino is powered.

5.  A reset button connected to the Arduino\'s reset line.

6.  **SCL** and **SDA** jumpers that tie the SDA and SCL pins (broken out on the R3 shield footprint) to the A4 and A5 pins to provide backward compatibility for older UNO models. These jumpers can be opened to free up pins A4 and A5 when using boards with a different I2C pin assignment like the [Leonardo, Mega, and Due](https://www.arduino.cc/en/Reference/Wire).

## Code Example

Press your completed microSD Shield onto your Arduino, and connect the board to your computer with the Arduino\'s USB cable.

For this example, you will use the **SD library** that comes with every [Arduino IDE installation](https://learn.sparkfun.com/tutorials/installing-arduino-ide). There are additional reference materials for the SD library [on the Arduino site](http://arduino.cc/en/Reference/SD). The SD library example sketches are in your Arduino examples folder under **Files \> Examples \> SD**

The SparkFun microSD shield uses Pin 8 as the **chip select line.** To use the SD library with the shield, you\'ll need to change the line `const int chipSelect = 4;` to `const int chipSelect = 8;` in the CardInfo.ino sketch (the sketch below is already modified if you\'d like to copy and paste it instead), then press **Upload**.

    language:c
    /*
      SD card test

      created  28 Mar 2011
      by Limor Fried
      modified 9 Apr 2012
      by Tom Igoe

      Hookup for the SparkFun microSD shield 
      on a SparkFun RedBoard/Arduino Uno R3

      MOSI - 11
      MISO - 12
      CLK - 13 
      CS - 8
    */

    // include the SD library:
    #include <SPI.h>
    #include <SD.h>

    // set up variables using the SD utility library functions:
    Sd2Card card;
    SdVolume volume;
    SdFile root;

    // The Sparkfun microSD shield uses pin 8 for CS
    const int chipSelect = 8;

    void setup()
    

      Serial.print("\nInitializing SD card...");

      // Note that even if it's not used as the CS pin, the hardware SS pin
      // (10 on most Arduino boards, 53 on the Mega) must be left as an output
      // or the SD library functions will not work.

      pinMode(10, OUTPUT);

      // we'll use the initialization code from the utility libraries
      // since we're just testing if the card is working!
      if (!card.init(SPI_HALF_SPEED, chipSelect))  else 

      // print the type of card
      Serial.print("\nCard type: ");
      switch (card.type()) 

      // Now we will try to open the 'volume'/'partition' - it should be FAT16 or FAT32
      if (!volume.init(card)) 

      // print the type and size of the first FAT-type volume
      uint32_t volumesize;
      Serial.print("\nVolume type is FAT");
      Serial.println(volume.fatType(), DEC);
      Serial.println();

      volumesize = volume.blocksPerCluster();    // clusters are collections of blocks
      volumesize *= volume.clusterCount();       // we'll have a lot of clusters
      volumesize *= 512;                            // SD card blocks are always 512 bytes
      Serial.print("Volume size (bytes): ");
      Serial.println(volumesize);
      Serial.print("Volume size (Kbytes): ");
      volumesize /= 1024;
      Serial.println(volumesize);
      Serial.print("Volume size (Mbytes): ");
      volumesize /= 1024;
      Serial.println(volumesize);

      Serial.println("\nFiles found on the card (name, date and size in bytes): ");
      root.openRoot(volume);

      // list all files in the card with date and size
      root.ls(LS_R | LS_DATE | LS_SIZE);
    }

    void loop(void) 

Open your [Arduino serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) by going to **Tools \> Serial Monitor** to see the results of the card test.

Once your card is detected, you can move on to *using* that extra space for something! Below is a simple analog data logging sketch from the SD card library with the same modification- changing the CS pin to 8. `const int chipSelect = 8;`

    language:c
    #include <SPI.h>
    #include <SD.h>

    // On the Ethernet Shield, CS is pin 4. Note that even if it's not
    // used as the CS pin, the hardware CS pin (10 on most Arduino boards,
    // 53 on the Mega) must be left as an output or the SD library
    // functions will not work.
    const int chipSelect = 8;

    void setup()
    

      Serial.print("Initializing SD card...");
      // make sure that the default chip select pin is set to
      // output, even if you don't use it:
      pinMode(10, OUTPUT);

      // The chipSelect pin you use should also be set to output
      pinMode(chipSelect, OUTPUT);

      // see if the card is present and can be initialized:
      if (!SD.begin(chipSelect)) 
      Serial.println("card initialized.");
    }

    void loop()
    
      }

      // open the file. note that only one file can be open at a time,
      // so you have to close this one before opening another.
      File dataFile = SD.open("datalog.txt", FILE_WRITE);

      // if the file is available, write to it:
      if (dataFile) 
      // if the file isn't open, pop up an error:
      else 

## SD Card Breakout Boards

If you have a smaller Arduino (or you\'d like to put a full-size SD card in your project), you can use the [SparkFun microSD Transflash Breakout](https://www.sparkfun.com/products/544) or the [SparkFun SD/MMC Card Breakout](https://www.sparkfun.com/products/12941) with the SD card library.

Since these smaller breakouts don\'t have built-in level shifting, make sure you have a logic level shifter like the [SparkFun Logic Level Converter](https://www.sparkfun.com/products/12009) in the circuit, or use a 3.3V Arduino like the [SparkFun Pro Mini 3.3V/8Mhz](https://www.sparkfun.com/products/11114)

Both examples use Pin 8 as the chip select line, just like the shield example above.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/7/micro_sd_hookup_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/7/micro_sd_hookup_bb.jpg)

*You can use either breakout with a 3.3V Arduino.*

\

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/7/full_sd_with_5v_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/7/full_sd_with_5v_bb.jpg)

*Use a level shifter between the card breakout and your 5V Arduino.*

## Troubleshooting

Arduino has troubleshooting tips on their [Notes on the Arduino SD Card Library](http://arduino.cc/en/Reference/SDCardNotes) page, including instructions for formatting new cards (if needed) and using the library with other Arduino boards.