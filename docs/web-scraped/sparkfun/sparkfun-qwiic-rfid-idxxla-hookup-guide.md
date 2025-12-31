# Source: https://learn.sparkfun.com/tutorials/sparkfun-qwiic-rfid-idxxla-hookup-guide

## Introduction

The [Qwiic RFID ID-XXLA](https://www.sparkfun.com/products/15191) is an I^2^C solution that pairs with the ID-LA modules: [ID-3LA](https://www.sparkfun.com/products/11862), the [ID-12LA](https://www.sparkfun.com/products/11827), or the [ID-20LA](https://www.sparkfun.com/products/11828), and utilizes 125kHz RFID chips. Using the product\'s interrupt pin, we\'ll discuss how to get, store, and compare unique RFID IDs. Let\'s take a look at the hardware used for this RFID tutorial.

[![SparkFun RFID Qwiic Reader](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/6/1/0/15191-SparkFun_RFID_Qwiic_Reader-01a.jpg)](https://www.sparkfun.com/sparkfun-rfid-qwiic-reader.html)

### [SparkFun RFID Qwiic Reader](https://www.sparkfun.com/sparkfun-rfid-qwiic-reader.html) 

[ SEN-15191 ]

The SparkFun RFID Qwiic Reader is a simple I2C based RFID breakout board for the ID-3LA, ID-12LA, and ID-20LA readers.

[ [\$23.50] ]

[![SparkFun RFID Qwiic Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/6/4/0/15209-SparkFun_RFID_Qwiic_Kit-01a.jpg)](https://www.sparkfun.com/sparkfun-rfid-qwiic-kit.html)

### [SparkFun RFID Qwiic Kit](https://www.sparkfun.com/sparkfun-rfid-qwiic-kit.html) 

[ KIT-15209 ]

The SparkFun RFID Qwiic Kit is a simple, yet all-in-one I2C based RFID starting point for the ID-3LA, ID-12LA, and ID-20LA re...

[ [\$49.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![RFID Reader ID-12LA (125 kHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/8/7/11827-01.jpg)](https://www.sparkfun.com/rfid-reader-id-12la-125-khz.html)

### [RFID Reader ID-12LA (125 kHz)](https://www.sparkfun.com/rfid-reader-id-12la-125-khz.html) 

[ SEN-11827 ]

RFID (radio-frequency identification) is the wireless non-contact use of radio-frequency electromagnetic fields, for the purp...

[ [\$32.50] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

[![RFID Tag (125kHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/9/1/14325-01.jpg)](https://www.sparkfun.com/rfid-tag-125khz.html)

### [RFID Tag (125kHz)](https://www.sparkfun.com/rfid-tag-125khz.html) 

[ COM-14325 ]

You might know RFID as the technology that Big Brother uses to \*track your every move\*. Quickly, don the \[tinfoil hats\](https...

[ [\$2.75] ]

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

**Heads up!** For the scope of the tutorial, we will be using the ID-12LA RFID reader. The board is also compatible with the following **ID-xxLA modules at 125kHz**. The range varies with each model. Keep in mind that you will need to an external antenna for the ID-3LA.\
\

[![RFID Reader ID-20LA (125 kHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/8/8/11828-01.jpg)](https://www.sparkfun.com/rfid-reader-id-20la-125-khz.html)

### [RFID Reader ID-20LA (125 kHz)](https://www.sparkfun.com/rfid-reader-id-20la-125-khz.html) 

[ SEN-11828 ]

RFID (radio-frequency identification) is the wireless non-contact use of radio-frequency electromagnetic fields, for the purp...

[ [\$37.50] ]

[![RFID Reader ID-3LA (125 kHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/2/6/5/11862-01.jpg)](https://www.sparkfun.com/rfid-reader-id-3la-125-khz.html)

### [RFID Reader ID-3LA (125 kHz)](https://www.sparkfun.com/rfid-reader-id-3la-125-khz.html) 

[ SEN-11862 ]

RFID (radio-frequency identification) is the wireless non-contact use of radio-frequency electromagnetic fields, for the purp...

[ [\$27.95] ]

The following **RFID tags** are also compatible with the RFID reader.\
\

[![RFID Glass Capsule (125kHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/0/4/6/09416-02.jpg)](https://www.sparkfun.com/rfid-glass-capsule-125khz.html)

### [RFID Glass Capsule (125kHz)](https://www.sparkfun.com/rfid-glass-capsule-125khz.html) 

[ SEN-09416 ]

This is a glass, cylindrical RFID tag; it\'s very similar to those \[implanted into pets\](http://en.wikipedia.org/wiki/Pet_chip...

[ [\$5.75] ]

[![RFID Button - 16mm (125kHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/0/4/7/09417-02.jpg)](https://www.sparkfun.com/rfid-button-16mm-125khz.html)

### [RFID Button - 16mm (125kHz)](https://www.sparkfun.com/rfid-button-16mm-125khz.html) 

[ SEN-09417 ]

This is a simple, thumbnail-size RFID tag. These tags are great for sensing presence, identification, etc., and they\'re small...

[ [\$4.75] ]

[![RFID Tag (125kHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/9/1/14325-01.jpg)](https://www.sparkfun.com/rfid-tag-125khz.html)

### [RFID Tag (125kHz)](https://www.sparkfun.com/rfid-tag-125khz.html) 

[ COM-14325 ]

You might know RFID as the technology that Big Brother uses to \*track your every move\*. Quickly, don the \[tinfoil hats\](https...

[ [\$2.75] ]

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/rfid-basics)

### RFID Basics 

Dive into the basics of Radio Frequency Identification (RFID) technology.

## Hardware Overview

### Qwiic Connectors

This is a [Qwiic](https://www.sparkfun.com/qwiic) product but not a \"pure\" Qwiic product. You\'ll still need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) or connect the interrupt pin if you decide to use that to indicate when an RFID card has been read (more on that later). Outside of that, Qwiic is an eco-system designed for I^2^C devices that allows you to prototype quickly without needing to solder anything. Just plug your Qwiic product into a Qwiic capable microcontroller and you\'re good to go! There are two on this product which means you can daisy chain the product with other I^2^C devices, like a Qwiic [Keypad](https://www.sparkfun.com/products/14836) for example.

[![The two large connectors on the product are the Qwiic connectors and are highlighted in this picture.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/QwiicConnectors1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/QwiicConnectors1.jpg)

### Power

The SparkFun Qwiic RFID ID-xxLA is a **3.3V** system. You can power the product with a Qwiic cable plugged into a capable microcontroller. You can also provide power through the `3V3` pin on the header.

### LEDs and Buzzer

When you provide power to the board you will see the onboard red power LED light up. There\'s another LED opposite the power LED labeled **READ**. This blue stat LED and the onboard buzzer will light or beep respectively when an RFID tag is brought into range.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![The image shows the ATtiny side of the product with the power and read LEDs above the connectors highlighted.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/LEDs1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/LEDs1.jpg)   [![The image shows the buzzer on the side of the RFID reader](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/Buzzer1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/Buzzer1.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### RFID Modules

There are three **ID-xxLA** options in our catalog that are listed above in the Introduction: the [ID-3LA](https://www.sparkfun.com/products/11862), the [ID-12LA](https://www.sparkfun.com/products/11827), and [ID-20LA](https://www.sparkfun.com/products/11828). If you purchased the [SparkFun RFID kit](https://www.sparkfun.com/products/15209) then it includes the ID-12LA and RFID cards that you need. Pictured below is the ID-12LA plugged into the Qwiic RFID.

[![Pictured is the product with the RFID module plugged into its headers.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/7/ID-12LA_module1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/ID-12LA_module1.jpg)

Each option is similar but there is a small variance in power consumption which translates into different read range capabilities. The ID-3LA is designed to be used with an external antenna which will get you 30cm of range. The ID-12LA and ID-20LA have a range of 12cm and 18cm respectively.

When plugging in your module, just take care that the side with less pins goes into the header with less pins.

[![Pictured is the module with the two female headers highlighted.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/Headers_Module1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/Headers_Module1.jpg)

*Smaller header on the left, larger on the right.*

### Jumpers

There are *four* jumpers on the header side of the product. Facing the product with the buzzer at the top, you\'ll see a jumper on the left side labeled `INT`. The interrupt pin can be disconnected here by [cutting the trace](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces). Now moving to the bottom near the header is a jumper labeled `I2C` that connects the I^2^C pull-up resistors to the I^2^C data lines. On the right side is a jumper labeled `Buzzer` that disconnects the buzzer when cut. This will disable the beeping sound when a RFID card is in range. Finally, the `ADDR` jumper allows you to change the default I^2^C jumper from **0x13** to **0x14**.

[![There are four jumpers on the side of the header side of the product that are highlighted in this picture.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/Jumpers1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/Jumpers1.jpg)

**Note:** As ofv1.2.0, the default address is 0x13 and the alternative address is 0x14 in the SparkFun Qwiic RFID Arduino Library. Previously, the default address was 0x7D and the alternative address was 0x7C.

## Hardware Assembly

Simply insert a Qwiic cable between the RedBoard Qwiic and the Qwiic RFID reader. You will also need to solder wire between the Qwiic RedBoard\'s pin 8 and the Qwiic RFID reader\'s INT pin. When you are ready, align the headers of the module with the Qwiic RFID reader.

[![Here is an image of the Qwiic RFID module connected to the Redboard Edge via a Qwiic cable with an additional wire connecting the product\'s interrupt with pin 8 on the Redboard.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/7/SparkFun_RFID_Qwiic_Reader_Hookup_Guide-031.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/SparkFun_RFID_Qwiic_Reader_Hookup_Guide-031.jpg)

**Note:** The Qwiic system has a logic level of **3.3V**. I have attached the interrupt to pin 8 on the Redboard Qwiic even though the pin is at 5 volts. This will not harm the Qwiic RFID because we\'re doing a simple **digitalRead()** but also because the ATTiny84 is tolerant of voltages up to 5.5V.

## Arduino Library 

We\'ve written a library to make it even easier to get started with the SparkFun Qwiic RFID ID-XXLA. The library will give you the full functionality of the Qwiic RFID ID-XXLA without the hub bub of the I²C data transactions. Also included are examples codes to demonstrate the full functionality of the library. You can click the link below to download the file directly and install it manually, or navigate through the Arduino Library Manager by searching **SparkFun Qwiic RFID**. You can also go the [Github page](https://github.com/sparkfun/SparkFun_Qwiic_RFID_Arduino_Library) and get download it from there.

[SparkFun Qwiic RFID Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_RFID_Arduino_Library/archive/master.zip)

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

## Example Code 

Let\'s take a look at the first two example sketches provided in the **SparkFun Qwiic RFID Arduino Library**.

### Example 1 - Read Tag Basics

For this first example we\'ll be grabbing the scanned card and the *time* between when it was scanned and when we request the number, by typing the number `1` into the Arduino IDE\'s Serial Terminal. If you downloaded the SparkFun Qwiic RFID Arduino Library directly then open the example located in the in the examples folder: **SparkFun_Qwiic_RFID_Arduino_Library** \> **Examples** \>**Example1_Read_Tag_Basics.ino** . If you\'ve downloaded the library through the Arduino Library Manager, then in the Arduino IDE you can navigate to **File**\>**Examples**\>**SparkFun Qwiic RFID Arduino LIbrary**\>**Example1_Read_Tag_Basics**.

Let\'s walk through the setup at the very top of the code. Nothing too surprising here, we\'ve `#included`-ed the Wire library as well as the SparkFun Qwiic RFID library. We then initialize the library with the `Qwiif Rfid myRfid(RFID_ADDR)` declaration. You may notice that it takes the Qwiic RFID Reader\'s address as one of it\'s arguments: `RFID_ADDR`. In the setup we `begin` the Wire, Serial, as well as the Qwiic RFID library. If there is a problem between your Redboard and the SparkFun Qwiic RFID board, then we\'ll print out an error message.

    language:c
    #include <Wire.h> 
    #include "SparkFun_Qwiic_Rfid.h"

    //#define RFID_ADDR 0x7D // Old Default I2C Address
    #define RFID_ADDR 0x13 // Default I2C address 

    Qwiic_Rfid myRfid(RFID_ADDR);

    String tag; 
    float scanTime;
    int serialInput; 

    void setup()
    

        Serial.println("Ready to scan some tags!"); 

        // Want to clear tags sitting on the Qwiic RFID card?
        //myRfid.clearTags();
    }

In the main loop, we\'re looking for the number **1** to be entered into the Serial terminal. When that\'s entered we\'re going to grab the RFID tag with the `myRFId.getTag()` function call and get its\' \"scan\" time (in seconds) with the `myRFID.getPrecReqTime()` function call. Just a quick note on the \"time\". This is not the time of day the tag was scanned but rather the time between when it was scanned and when you requested it. This gives each RFID tag a unique property even when you scan the same card twice, because their scan times will be different.

    language:c
    void loop()
    

      }
    }

After scanning a card and waiting a number of seconds, then entering **1** into the Serial Terminal, my output looks like this.

[![This picture shows the Serial Terminal of the Arduino IDE which diplays the RFID tag and it\'s scan time.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/Serial_OUTPUT_Serial_INPUT.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/Serial_OUTPUT_Serial_INPUT.JPG)

If you need a similar example, but one that reads all 20 tags that can be stored on the SparkFun Qwiic RFID ID-XXLA Reader, then check out **Example5_Get_All_Available_Tags**

### Example 2 - Read Tag Interrupt

For this next example we\'ll be using an additional pin as an interrupt that will indicate that a card has been scanned, which makes this not a *pure* Qwiic example. We\'ll use that interrupt to initiate a request to read the tag that the SparkFun Qwiic RFID Reader is holding onto. If you the downloaded the SparkFun Qwiic RFID Arduino Library directly then open the example located in the in the examples folder: **SparkFun_Qwiic_RFID_Arduino_Library** \> **Examples** \>**Example2_Read_Tag_Interrupt.ino** . If you\'ve downloaded the library through the Arduino Library Manager, then in the Arduino IDE you can navigate to **File**\>**Examples**\>**SparkFun Qwiic RFID Arduino LIbrary**\>**Example2_Read_Tag_Interrupt**.

At the top we `#include` the new library and use the default address for our `Qwiic Rfid myRfid(RFID_ADDR)` declaration. In the setup we communicate with the SparkFun Qwiic RFID Reader with the `myRfid.begin` statement. If there is any issue communicating with the Qwiic RFID we\'ll know about them here. Last but not least we pull the interrupt pin on pin 3 up high with `pinMode(intPin, INPUT_PULLUP)` to put it into a known **HIGH** state. When a tag is read this line will go **LOW**.

    language:c
    #include <Wire.h> 
    #include "SparkFun_Qwiic_Rfid.h"

    //#define RFID_ADDR 0x7D // Old Default I2C Address
    #define RFID_ADDR 0x13 // Default I2C address 

    // Interrupt Pin on pin 3. 
    const int intPin = 3; 
    String tag; 

    Qwiic_Rfid myRfid(RFID_ADDR);

    void setup()
    

        Serial.println("Ready to scan some tags!"); 

        // Put the interrupt pin in a known HIGH state. 
        pinMode(intPin, INPUT_PULLUP); 

        // Want to clear tags sitting on the Qwiic RFID card?
        //myRfid.clearTags();

    }

In the loop, we\'re just monitoring the Qwiic RFID\'s interrupt pin that will indicate that a tag has just been read. This will initiate a call to `myRfid.getTag()` that will pull in the scanned card\'s RFID tag ID.

    language:c
    void loop()
    

        delay(500);

    }

And that\'s it!

If you have not already, select the board and COM port of your Arduino and upload the **Example1_ReadTag.ino** code. Then open your [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **115200** and scan a tag,

[![There is a gif here showing a person placing their RFID tag in range of the RFID module.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/SparkFun_RFID_Qwiic_Reader_Demo1.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/SparkFun_RFID_Qwiic_Reader_Demo1.gif)

You should see the following. Note at the image indicates a baud rate of 9600 but the latest code uses a baud rate of 115200.

[![Pictured is an image of Arduino\'s Serial Monitor with an RFID tag\'s number printed.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/7/SerialOutput_Single_NoTime.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/7/SerialOutput_Single_NoTime.JPG)

## Python Package

**Note:** This tutorial assumes you are using the latest version of Python 3. If this is your first time using Python or I^2^C hardware on a Raspberry Pi, please checkout our tutorial on [Python Programming with the Raspberry Pi](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi) and the [Raspberry Pi SPI and I2C Tutorial](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial). Jetson Nano users can check out this tutorial on [Working with Qwiic on a Jetson Nano through Jupyter Notebooks](https://learn.sparkfun.com/tutorials/working-with-qwiic-on-a-jetson-nano-through-jupyter-notebooks).

We\'ve written a Python package to easily get setup and take readings from the ID-LA RFID module. There are two methods for installing the Python package for the Qwiic RFID.

1.  Install the all inclusive SparkFun Qwiic Python package.
2.  Independently install the SparkFun RFID Python package.

The all inclusive SparkFun Qwiic Python package, is recommended as is also installs the required I^2^C driver as well.

**Note:** Don\'t forget to double check that the hardware I^2^C connection is enabled on your single board computer.

### SparkFun Qwiic Package

This repository is hosted on PyPi as the `sparkfun-qwiic` package. On systems that support PyPi installation via `pip3` (use `pip` for Python 2) is simple, using the following commands:

For **all users** (note: the user must have [**sudo**](https://en.wikipedia.org/wiki/Sudo) privileges):

    language:bash
    sudo pip3 install sparkfun-qwiic

For the **current user**:

    language:bash
    pip3 install sparkfun-qwiic

### Independent Installation

You can install the `sparkfun-qwiic-rfid` Python package independently, which is hosted by PyPi. However, if you prefer to manually download and install the package from the [GitHub repository](https://github.com/sparkfun/Qwiic_RFID_Py), you can grab them here (*\*Please be aware of any package dependencies. You can also check out the repository documentation page, hosted on [ReadtheDocs](https://qwiic-rfid-py.readthedocs.io/en/latest/index.html).*):

[Download the SparkFun Qwiic RFID Python Package (ZIP)](https://github.com/sparkfun/Qwiic_RFID_Py/archive/main.zip)

#### PyPi Installation

This repository is hosted on PyPi as the `sparkfun-qwiic-rfid` package. On systems that support PyPi installation via `pip3` (use `pip` for Python 2) is simple, using the following commands:

For **all users** (note: the user must have [**sudo**](https://en.wikipedia.org/wiki/Sudo) privileges):

    language:bash
    sudo pip3 install sparkfun-qwiic-rfid

For the **current user**:

    language:bash
    pip3 install sparkfun-qwiic-rfid

#### Local Installation

To install, make sure the `setuptools` package is installed on the system.

Direct installation at the command line (use `python` for Python 2):

    language:bash
    python3 setup.py install

To build a package for use with `pip3`:

    language:bash
    python3 setup.py sdist

A package file is built and placed in a subdirectory called dist. This package file can be installed using `pip3`.

    language:bash
    cd dist
    pip3 install sparkfun_qwiic_rfid-<version>.tar.gz

### Python Package Operation

Before we jump into getting readings, let\'s take a closer look at the available functions in the Python package. Below, is a description of the basic functionality of the Python package. This includes the package organization, built-in methods, and their inputs and/or outputs. For more details on how the Python package works, check out the [source code](https://github.com/sparkfun/Qwiic_RFID_Py/blob/main/qwiic_rfid.py) and [package documentation](https://qwiic-rfid-py.readthedocs.io/en/latest/index.html).

#### Dependencies

This Python package has a very few dependencies in the code, listed below:

    language:python
    import qwiic_i2c
    import time

#### Default Variables

The default variables, in the code, for this Python package are listed below:

    language:python
    # qwiic_rfid GLOBAL VARIABLES
    #----------------------------------------------------------------------------------------------------
    # Define the device name and I2C addresses. These are set in the class defintion 
    # as class variables, making them avilable without having to create a class instance.
    # This allows higher level logic to rapidly create a index of qwiic devices at 
    # runtine
    #
    # The name of this device 
    _DEFAULT_NAME = "Qwiic RFID"

    # Some devices have multiple availabele addresses - this is a list of these addresses.
    # NOTE: The first address in this list is considered the default I2C address for the 
    # device.
    _AVAILABLE_I2C_ADDRESS = [0x13, 0x14]

**Note:** This package is different from previous packages as the register variables are declared in the object class.

    language:python
    # QwiicRFID CLASS VARIABLES
    #----------------------------------------------------------------------------------------------------
    ALTERNATE_ADDR = 0x7C
    ADDRESS_LOCATION = 0xC7

    TAG_AND_TIME_REQUEST = 10
    MAX_TAG_STORAGE = 20
    BYTES_IN_BUFFER = 4

    RFID_TAG = None
    RFID_TIME = None
    TAG_ARRAY = [None] * MAX_TAG_STORAGE
    TIME_ARRAY = [None] * MAX_TAG_STORAGE

#### Class

**`QwiicRFID()`** or **`QwiicRFID(address)`**\
This Python package operates as a class object, allowing new instances of that type to be made. An `__init__()` constructor is used that creates a connection to an I^2^C device over the I^2^C bus using the default or specified I^2^C address.

##### The Constructor

A constructor is a special kind of method used to initialize (assign values to) the data members needed by the object when it is created.

**`__init__(address=None, i2c_driver=None):`**

Input: value

The value of the device address. If not defined, the Python package will use the default I^2^C address (**0x13**) stored under `_AVAILABLE_I2C_ADDRESS` variable.

Input: *i2c_driver*

Loads the specified I^2^C driver; by default the [Qwiic I^2^C driver](https://github.com/sparkfun/Qwiic_I2C_Py) is used: `qwiic_i2c.getI2CDriver()`. Users should use the default I^2^C driver and leave this field blank.

#### Functions

A function is an attribute of the class, which defines a method for instances of that class. In simple terms, they are objects for the operations (or methods) of the class. A list of all the available functions are detailed on the [API Reference page](https://qwiic-rfid-py.readthedocs.io/en/latest/apiref.html) of ReadtheDocs for the [Qwiic_RFID_Py Python package](https://github.com/sparkfun/Qwiic_RFID_Py).

### Upgrading the Python Package

In the future, changes to the Python package might be made. Updating the installed packages has to be done individually for each package (i.e. sub-modules and dependencies won\'t update automatically and must be updated manually). For the `sparkfun-qwiic-rfid` Python package, use the following command (use `pip` for Python 2):

For **all users** (note: the user must have [**sudo**](https://en.wikipedia.org/wiki/Sudo) privileges):

    language:bash
    sudo pip3 install --upgrade sparkfun-qwiic-rfid

For the **current user**:

    language:bash
    pip3 install --upgrade sparkfun-qwiic-rfid

## Python Examples

**Note:** Work on this section is in progress. We will update the content as soon as we can.