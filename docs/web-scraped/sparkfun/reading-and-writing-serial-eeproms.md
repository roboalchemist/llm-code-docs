# Source: https://learn.sparkfun.com/tutorials/reading-and-writing-serial-eeproms

## Introduction

**NOTE:** Users with the [Qwiic EEPROM](https://www.sparkfun.com/products/18355), will want to check out the [Qwiic EEPROM Hookup Guide](https://learn.sparkfun.com/tutorials/1661).

------------------------------------------------------------------------

**EEPROM**, or **E**lectrically **E**rasable **P**rogrammable **R**ead-**O**nly **M**emory, is a type of device that allows you to store small chunks of data and retrieve it later even if the device has been power cycled. A lot of modern microcontrollers -- such as the ATmega328 -- contain some built-in EEPROM, but that doesn\'t mean that you can\'t add more! Serial EEPROM devices like the [Microchip 24-series EEPROM](https://www.sparkfun.com/products/525) allow you to add more memory to any device that can speak I²C. Today we\'re going to learn how to read and write serial EEPROM devices using Arduino.

**Library Now Available:** We\'ve created an [External EEPROM Library](https://github.com/sparkfun/SparkFun_External_EEPROM_Arduino_Library) for Arduino that makes reading and writing an EEPROM easy. This tutorial is still very good knowledge and background to have. Please read then consider using the library.

[![I2C EEPROM - 256k Bit (24LC256)](https://cdn.sparkfun.com/r/600-600/assets/parts/3/0/5/00525-I2C_EEPROM_-_256k_Bit__24LC256_-01_.jpg)](https://www.sparkfun.com/products/525)

### [I2C EEPROM - 256k Bit (24LC256)](https://www.sparkfun.com/products/525) 

[ COM-00525 ]

This is an I2C, 256Kbit, Serial Electrically Erasable PROM (EEPROM), capable of operation across a 2.5V to 5.5V range.

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Jumper Wires - Connected 6\" (M/M, 20 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/6/1/3/12795-00.jpg)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html)

### [Jumper Wires - Connected 6\" (M/M, 20 pack)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html) 

[ PRT-12795 ]

These are 6\" long jumper wires with male connectors on both ends. Use these to jumper from any female header on any board, to...

[ [\$2.95] ]

[![SparkFun USB Mini-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/6/9/8/0/11301-01.jpg)](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html)

### [SparkFun USB Mini-B Cable - 6 Foot](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html) 

[ CAB-11301 ]

This is a USB 2.0 type A to Mini-B 5-pin cable. You know, the mini-B connector that usually comes with USB Hubs, Cameras, MP3...

[ [\$5.50] ]

[![I2C EEPROM - 256k Bit (24LC256)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/0/5/00525-I2C_EEPROM_-_256k_Bit__24LC256_-01_.jpg)](https://www.sparkfun.com/products/525)

### [I2C EEPROM - 256k Bit (24LC256)](https://www.sparkfun.com/products/525) 

[ COM-00525 ]

This is an I2C, 256Kbit, Serial Electrically Erasable PROM (EEPROM), capable of operation across a 2.5V to 5.5V range.

**Retired**

### Suggested Reading

Before continuing with this guide, we recommend you be somewhat familiar with the concepts in the following tutorials:

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/integrated-circuits)

### Integrated Circuits 

An introduction to integrated circuits (ICs). Electronics\' ubiquitous black chips. Includes a focus on the variety of IC packages.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## EEPROM Basics

Before we get into the hookup it\'s probably a good idea to familiarize ourselves with EEPROM and the history of ROM in general. That said, if you don\'t nerd-out on computer history it\'s probably safe to skip that section.

### What is ROM?

Read-Only Memory (**ROM**) is a type of computer memory which, generally speaking, is only programmed once (or very occasionally) and then gets read from the rest of the time. This is because it\'s very slow --- or impossible --- to write new data to ROM. The trade-off for very slow write times --- traditionally --- is that it\'s also non-volatile meaning that the data doesn\'t go away when power is removed from the device. This makes it ideal for things like firmware which need to be \"remembered\" by the computer, but never actually change. The BIOS in your PC is stored on a form of ROM.

### A Brief History of ROM

Early \"Stored-Program\" type computers --- such as desk calculators and keyboard interpreters --- began using ROM in the form of Diode Matrix ROM. This was memory made up of discrete semiconductor diodes placed on a specially organized PCB. This gave way to Mask ROM with the advent of integrated circuits. Mask ROM was a lot like Diode Matrix ROM only it was implemented on a much smaller scale. This meant, however, that you couldn\'t just move a couple of diodes around with a soldering iron and reprogram it. Mask ROM had to be programmed by the manufacturer and was thereafter not alterable.

Unfortunately, Mask ROM was expensive and took a long time to produce because each new program required a brand new device to be manufactured by a foundry. In 1956, however, this problem was solved with the invention of PROM (*Programmable* ROM) which allowed developers to program the chips themselves. That meant manufacturers could produce millions of the same *unprogrammed* device which made it cheaper and more practical. PROM, however, could only be written to *once* using a high-voltage programming device. After a PROM device was programmed, there was no way to return the device to its unprogrammed state.

![UV Erasable Microcontroller](https://cdn.sparkfun.com/assets/e/c/f/7/8/51155935ce395ff771000001.jpg)

*A UV Erasable Microcontroller. The window gives it away.*

This changed in 1971 with the invention of EPROM (*Erasable Programmable* ROM) which --- besides adding another letter to the acronym --- brought with it the ability to erase the device and return it to a \"blank\" state using a strong UV light source. That\'s right, you had to *shine a bright light* on the IC to reprogram it, how cool is that? Well, it turns out it\'s pretty cool unless you\'re a developer working on firmware in which case you\'d really like to be able to reprogram the device using electrical signals. This finally became a reality in 1983 with the development of EEPROM (*Electrically Erasable Programmable* ROM) and with that, we arrive at the current day unwieldy acronym.

### Quirks of EEPROM

There are two major drawbacks to EEPROM as a method of data storage. In most applications the pros outweigh the cons, but you should be aware of them before incorporating EEPROM into your next design.

First of all, the technology that makes EEPROM work also limits the number of times that it can be re-written. This has to do with electrons becoming trapped in the transistors that make up the ROM and building up until the charge difference between a \"1\" and a \"0\" is unrecognizable. But don\'t worry, most EEPROMs have a maximum re-write number of 1 million or more. As long as you\'re not continuously writing to the EERPROM it\'s unlikely you\'ll hit this maximum.

Secondly, EEPROM will not be erased if you remove power from it, but it won\'t hold onto your data indefinitely. Electrons can drift out of the transistors and through the insulator, effectively erasing the EEPROM over time. That said, this usually occurs over the course of years (although it can be accelerated by heat). Most manufacturers say that your data is safe on EEPROM for 10 years or more at room temperature.

And there\'s one more thing you should keep in mind when selecting an EEPROM device for your project. EEPROM capacity is measured in *bits* and not *bytes*. A 256K EEPROM will hold 256Kbits of data, in other words, just 32KB.

## Arduino Hardware Hookup 

Okay, now that we know what EEPROM is, let\'s hook one up and see what it can do! In order to get our device talking we\'ll need to connect power as well as I²C serial lines. This device in particular runs at 5**VDC** so we\'ll connect it to the 5V output of our Arduino UNO. Also, the I²C lines will need pullup resistors for communication to happen correctly. The value of these resistors depends on the capacitance of the lines and frequency you want to communicate at, but a good rule of thumb for non-critical applications is just keep it in the kΩ range. In this example, we\'ll use 4.7kΩ pullup resistors.

There are three pins on this device to select the I²C address, this way you can have more than one EEPROM on the bus and address them each differently. You could just ground them all, but we\'ll be wiring them so that we can drop in a higher-capacity device later in the tutorial.

We\'ll use a breadboard to connect everything together. The diagram below shows the correct hookup for most I²C EEPROM devices, including the [Microchip 24-series EEPROM](https://www.sparkfun.com/products/525) that we sell.

[![drawing showing the correct way to wire an I2C EEPROM device to an Arduino UNO](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/3/eeprom_wiring.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/eeprom_wiring.png)

That\'s it! Like most I²C devices, the hardware hookup is a breeze. Now we can move on to the code.

## Reading and Writing

Most of the time when you\'re using an EEPROM in conjunction with a microcontroller you won\'t actually need to see *all* of the contents of the memory at once. You\'ll just read and write bytes here and there as needed. In this example, however, we\'re going to write an entire file to EEPROM and then read all of it back off so we can view it on our computer. This should get us comfortable with the idea of using EEPROM and also give us a feeling for how much data can really fit on a small device.

To send and receive files using the example Arduino sketches below, you\'ll need a terminal program such as [TeraTerm](https://learn.sparkfun.com/tutorials/terminal-basics/tera-term-windows). Once you have that downloaded and installed, we can get down to business.

**Heads up!** If your EEPROM is larger than 512k (For Example: If it\'s marked \'**24LC1025**\') you may want to skip straight to the section on [higher capacity EEPROMs](https://learn.sparkfun.com/tutorials/reading-and-writing-serial-eeproms#higher-capacity-eeproms).

### Write Something

Our example sketch will simply take any byte that comes in over the serial port and write it to the EEPROM, keeping track along the way of how many bytes we\'ve written to memory.

Writing a byte of memory to the EEPROM generally happens in three steps:

1.  Send the Most Significant Byte of the memory address that you want to write to.
2.  Send the Least Significant Byte of the memory address that you want to write to.
3.  Send the data byte that you would like to store at this location.

There are probably a few key words there that bare explaining:

#### Memory Addresses

If you imagine all of the bytes in a 256 Kbit EEPROM standing in a line from 0 to 32000 --- because there are 8 bits to a byte and therefore you can fit 32000 bytes on a 256 Kbit EEPROM --- then a memory address is the *place in line* where you would find a particular byte. We need to send that address to the EEPROM so it knows where to put the byte that we\'re sending.

#### Most Significant and Least Significant Bytes

Because there are 32000 possible places in a 256 Kbit EEPROM --- and because 255 is the largest number you can encode in one byte --- we need to send this address in two bytes. First we send the Most Significant Byte (MSB) --- the first 8 bits in this case. Then we send the Least Significant Byte (LSB) --- the second 8 bits. Why? Because this is how the device expects to receive them, that\'s all.

### Page Writing

Writing one byte at a time is fine, but most EEPROM devices have something called a \"page write buffer\" which allows you to write multiple bytes at a time the same way you would a single byte. We\'ll be taking advantage of this in our example sketch.

The EEPROM uses an internal counter that automatically increases the memory location with each following data byte it receives. Once a memory address has been sent we can follow it with up to 64 bytes of data. The EEPROM assumes (rightly) that an address of 312 followed by 10 bytes will record byte 0 at address 312, byte 1 at address 313, byte 2 at address 314, and so on.

### Arduino Sketch Example [Write Something]

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Here\'s an example sketch to write some data to the EEPROM. Walk through the comments in the code for an explanation about what\'s going on.

    language:c
    //Include the Wire I2C Library
    #include <Wire.h>

    /*This address is determined by the way your address pins are wired.
    In the diagram from earlier, we connected A0 and A1 to Ground and 
    A2 to 5V. To get the address, we start with the control code from 
    the datasheet (1010) and add the logic state for each address pin
    in the order A2, A1, A0 (100) which gives us 0b1010100, or in 
    Hexadecimal, 0x54*/

    #define EEPROM_ADR 0x54

    /*Theoretically, the 24LC256 has a 64-byte page write buffer but 
    we'll write 16 at a time to be safe*/ 

    #define MAX_I2C_WRITE 16 

    byte tempStore[MAX_I2C_WRITE];

    void setup()
    

          timerReset = millis();
        }

        if (millis() - timerReset > 2000)
        
      }

    }

    void loop()
    

    /* This is the 3 step memory writing procedure that
    we talked about. First we send the MSB of the address. 
    Then we send the LSB of the address. Then we send the 
    data that we want to store. */

    void writeEEPROMPage(long eeAddress)
    

Upload this code to your Arduino board and open the terminal program that you installed earlier. For the purposes of this tutorial, I\'ll assume you\'re using TeraTerm.

When you open TeraTerm, it will ask you to setup a new connection:

[![TeraTerm window asking for connection information](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt1.PNG)

You\'ll need to select the serial port that your Arduino is connected to. Once you\'ve pressed OK on that, go to **Setup \> Serial Port** and set your Baud Rate to the one we selected in the code above (**19200**) then press OK.

[![TeraTerm serial port window with 19200 in the baud rate field](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt2.PNG)

Now you should be seeing a bunch of zeros appearing in your terminal window. This is our sketch telling us how many bytes we\'ve written. So far we\'ve written nothing; let\'s change that! Go to **File \> Send File\...** and select a file to send through the terminal. For testing purposes, I suggest using the complete text of the Ghostbusters theme as written and performed by Ray Parker Jr. You can get the text file below.

[Ghostbusters (TXT)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/ghostbusters.txt)

Select that file and be sure to click on the \"binary\" button, so that the file is written byte-for-byte over the serial port.

[![file selection window in TeraTerm with ghostbusters.txt highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt4.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt4.PNG)

When you press \"Open\" you\'ll see a file transfer window for just a moment as the file is dumped to the terminal.

[![TeraTerm file transfer window transferring ghostbusters.txt at 80% with 0:00 elapsed time](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt3.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt3.PNG)

Now the number in your terminal window should be **1344**, representing the memory location that we\'re sitting at after writing the complete text of the Ghostbusters theme as written and performed by Ray Parker Jr. You can go ahead and close TeraTerm, it worked! Well\... we don\'t actually know if it worked until we read it back, so let\'s read it back!

------------------------------------------------------------------------

### Read Something

Reading from the EEPROM basically follows the same three step process as writing to the EEPROM:

1.  Send the Most Significant Byte of the memory address that you want to write to.
2.  Send the Least Significant Byte of the memory address that you want to write to.
3.  Ask for the data byte at that location.

### Arduino Sketch Example [Read Something]

Here\'s an example sketch to write some data to the EEPROM. Walk through the comments in the code for an explanation about what\'s going on.

    language:c
    //Include the Wire I2C Library
    #include <Wire.h>

    /*This address is determined by the way your address pins are wired.
    In the diagram from earlier, we connected A0 and A1 to Ground and 
    A2 to 5V. To get the address, we start with the control code from 
    the datasheet (1010) and add the logic state for each address pin
    in the order A2, A1, A0 (100) which gives us 0b1010100, or in 
    Hexadecimal, 0x54*/

    #define EEPROM_ADR 0x54

    void setup()
    
    }

    void loop()
    

    /* This is the 3 step memory reading procedure that
    we talked about. First we send the MSB of the address. 
    Then we send the LSB of the address. Then we ask for the 
    number of bytes that we want to receive. Here, we're 
    going 1 byte at a time*/

    byte readEEPROM(long eeaddress)
    

Now load *this* sketch onto your Arduino and open TeraTerm again. Once again, you\'ll need to open the correct serial port but before we set the correct baud rate and get things moving, let\'s create a file to store all the memory that we\'re about to read. Go to **File \> Log\...** and create a logfile. Make sure to uncheck the \"Append\" option and check the \"Binary\" option. This makes sure that the terminal will start a fresh logfile and write to it byte-for-byte what comes over the terminal.

[![Log File window in TeraTerm with binary option selected and append option unselected. teraterm.log in the filename field.](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt5.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt5.PNG)

When you press \"Save\" another dialog window will appear but it may pop under the current window Go find it, it will come in handy in a second. Now go to **Setup \> Serial Port** and set your Baud Rate to the one we selected in the code above (**115200**) then press OK. Check the logfile window and see how many bytes have been transferred.

[![TeraTerm logfile transfer window showing 32000 bytes transferred](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt6.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/tt6.PNG)

Once we\'ve transferred 32000 bytes, we\'ve got everything on the chip. Now close everything and open up that logfile in a text editor. You should now be face to face with, you guessed it, the complete text of the Ghostbusters theme as written and performed by Ray Parker Jr. Oh yeah, plus a bunch of junk that represents the unwritten space in memory.

## Higher Capacity EEPROMs

So what if the thing that we want to store is bigger than complete text of the Ghostbusters theme as written and performed by Ray Parker Jr? As it happens, you can get EEPROM devices with much larger storage. For instance, the Microchip 24LC1025 can store up to 1025 Kbits! That\'s 128KB, enough space to have some real fun with!

Using the Microchip 24LC1025 is almost exactly like using the smaller EEPROM devices but with one minor tweak. Because the memory space is so much larger, two bytes is no longer enough to represent the memory address that we want to modify. To get around this problem, the 24LC1025 splits up the memory addresses into two separate blocks. When you address the chip, you send the block selector for the block that you want to manipulate in place of where you\'d usually send the first bit of the chip address. Because of this, pin A2 on the EEPROM isn\'t used and needs to be tied to 5V in order for the device to work. You\'ll notice that we\'ve already tied A2 to 5V in our previous example, so you could use the same example circuit to hook it up!

### Arduino Sketch Example [Write Something in a Higher Capacity EEPROM]

Along with that change to our Arduino hookup, we\'ll also need to add to our code in order to switch the block select when we reach above a certain memory address. Here\'s what that operation looks like when we\'re writing:

    language:c
    void writeEEPROM(long eeAddress, byte data)
    
      else
      

      Wire.write((int)(eeAddress >> 8)); // MSB
      Wire.write((int)(eeAddress & 0xFF)); // LSB
      Wire.write(data);
      Wire.endTransmission();
    }

### Arduino Sketch Example [Read Something in a Higher Capacity EEPROM]

\...and here it is when we\'re reading:

    language:c
    byte readEEPROM(long eeaddress)
    

It\'s just that easy! You can get the complete Arduino example sketches here if you want to play with it yourself:

**Heads up!** If you have an EEPROM device that already has data on it, running the \"Write an EEPROM\" code will write over the existing data and make it irretrievable. If you think there\'s interesting information on your device, try reading from it first!

- [Write an EEPROM](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/howToWriteAnEEPROM_1.ino)
- [Read an EEPROM](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/3/howToReadAnEEPROM.ino)